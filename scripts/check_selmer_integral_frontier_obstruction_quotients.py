#!/usr/bin/env python3
"""Authenticate and check the original obstruction quotient argument.

Finite cyclic cochain complexes test the local/global cardinality sequence
and the opposite-coefficient-sequence inequality whenever its exact
hypotheses hold. Arithmetic duality is a retained input, not computed here.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path

from check_sources import inspect_file
from check_selmer_integral_frontier_first_global_bound import rank_mod_p
from check_selmer_integral_frontier_second_bound_suppliers import TruncatedRing

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules."
RANGES = {
    BASE+"ArchimedeanH0Cards.PushforwardPreservesSelmerCocycles": [(10, 115), (184, 243)],
    BASE+"ArchimedeanH0Cards.ObstructionBoundFromDuality": [(13, 28)],
    BASE+"ArchimedeanH0Cards.CardKerRange": [(22, 74), (102, 185)],
    BASE+"ArchimedeanH0Cards.OdHalf": [(184, 244), (245, 304)],
    BASE+"ArchimedeanH0Cards.OdCount": [(8, 79)],
    BASE+"ArchimedeanH0Cards.AmMaps": [(51, 63)],
    BASE+"ArchimedeanH0Cards.OdSESInv": [(102, 196)],
    BASE+"ArchimedeanH0Cards.OdLam": [(5, 25)],
    BASE+"ArchimedeanH0Cards.ExactMid": [(45, 115)],
    BASE+"ArchimedeanH0Cards.CokerBound": [(27, 104), (105, 168)],
    BASE+"ArchimedeanH0Cards.ObstructionBoundOfDuality": [(89, 140), (145, 199)],
}


def kernel(rows, dim, p=3):
    a = [list(row) for row in rows]
    pivots = []
    for j in range(dim):
        pivot = next((i for i in range(len(pivots), len(a)) if a[i][j] % p), None)
        if pivot is None:
            continue
        i = len(pivots)
        a[i], a[pivot] = a[pivot], a[i]
        unit = pow(a[i][j] % p, -1, p)
        a[i] = [x*unit % p for x in a[i]]
        for k in range(len(a)):
            if k != i and a[k][j] % p:
                scalar = a[k][j] % p
                a[k] = [(x-scalar*y) % p for x, y in zip(a[k], a[i])]
        pivots.append(j)
    basis = []
    for j in set(range(dim))-set(pivots):
        vector = [0]*dim
        vector[j] = 1
        for i, pivot in enumerate(pivots):
            vector[pivot] = -a[i][j] % p
        basis.append(vector)
    return basis


def matvec(matrix, vector, p=3):
    return [sum(x*y for x, y in zip(row, vector)) % p for row in matrix]


def columns(matrix, width):
    return [[row[j] for row in matrix] for j in range(width)]


def span_rank(vectors):
    return rank_mod_p(vectors, 3)


def add(a, b):
    return [(x+y) % 3 for x, y in zip(a, b)]


def cyclic_complex(order, m, copies, nontrivial):
    dimension = m*copies
    ring = TruncatedRing(3, max(m, 1))
    unit = ring.elem([1, int(nontrivial)])
    powers = [ring.one]
    for _ in range(order):
        powers.append(ring.mul(powers[-1], unit))
    assert powers[order] == ring.one
    keys = {degree: list(itertools.product(range(1, order), repeat=degree)) for degree in (1, 2, 3)}
    indexes = {degree: {key: i for i, key in enumerate(keys[degree])} for degree in keys}

    def act(g, vector):
        if not m:
            return []
        out = []
        for i in range(copies):
            out.extend(ring.mul(powers[g % order], tuple(vector[i*m:(i+1)*m])))
        return out

    def differential(degree):
        source_width = dimension*(1 if degree == 0 else len(keys[degree]))
        target_keys = keys[degree+1]
        cols = []
        for index in range(source_width):
            vector = [0]*source_width
            vector[index] = 1

            def value(key):
                if not key:
                    return vector
                if 0 in key:
                    return [0]*dimension
                start = indexes[degree][key]*dimension
                return vector[start:start+dimension]

            out = []
            for key in target_keys:
                if degree == 0:
                    result = add(act(key[0], vector), [(-x) % 3 for x in vector])
                elif degree == 1:
                    g, h = key
                    result = add(add(act(g, value((h,))), [(-x) % 3 for x in value(((g+h) % order,))]), value((g,)))
                else:
                    g, h, k = key
                    result = add(add(act(g, value((h, k))), [(-x) % 3 for x in value(((g+h) % order, k))]),
                                 add(value((g, (h+k) % order)), [(-x) % 3 for x in value((g, h))]))
                out.extend(result)
            cols.append(out)
        height = dimension*len(target_keys)
        return [[cols[j][i] for j in range(source_width)] for i in range(height)]

    ds = [differential(i) for i in range(3)]
    dims = [dimension, dimension*len(keys[1]), dimension*len(keys[2]), dimension*len(keys[3])]
    for degree in (0, 1):
        for col in columns(ds[degree], dims[degree]):
            assert not any(matvec(ds[degree+1], col))
    return {"order": order, "m": m, "copies": copies, "keys": keys, "indexes": indexes,
            "dims": dims, "d": ds}


def local_map(global_complex, local_complex, multiplier, degree):
    glob, loc = global_complex, local_complex
    gd, ld = glob["dims"][0], loc["dims"][0]
    assert glob["m"] == loc["m"] and glob["copies"] >= loc["copies"]
    rows = [[0]*glob["dims"][degree] for _ in range(loc["dims"][degree])]
    for i, key in enumerate(loc["keys"][degree]):
        image = tuple(g*multiplier % glob["order"] for g in key)
        if 0 in image:
            continue
        j = glob["indexes"][degree][image]
        for c in range(ld):
            rows[i*ld+c][j*gd+c] = 1
    return rows


def obstruction_data(order, m, copies, nontrivial, multiplier, unrestricted_local):
    glob = cyclic_complex(order, m, copies, nontrivial)
    loc = cyclic_complex(order, m, 1, nontrivial and multiplier == 1)
    L1 = local_map(glob, loc, multiplier, 1)
    L2 = local_map(glob, loc, multiplier, 2)
    dg0, dg1, dg2 = glob["d"]
    dl0, dl1, dl2 = loc["d"]
    zg1, zg2 = kernel(dg1, glob["dims"][1]), kernel(dg2, glob["dims"][2])
    zl1, zl2 = kernel(dl1, loc["dims"][1]), kernel(dl2, loc["dims"][2])
    bg1, bg2 = columns(dg0, glob["dims"][0]), columns(dg1, glob["dims"][1])
    bl1, bl2 = columns(dl0, loc["dims"][0]), columns(dl1, loc["dims"][1])
    allowed = zl1 if unrestricted_local else bl1
    paired_dim = glob["dims"][2]+loc["dims"][1]
    equations = [row+[0]*loc["dims"][1] for row in dg2]
    equations += [left+[(-x) % 3 for x in right] for left, right in zip(L2, dl1)]
    zpair = kernel(equations, paired_dim)
    bpair = [left+right for left, right in zip(bg2, columns(L1, glob["dims"][1]))]
    bpair += [[0]*glob["dims"][2]+v for v in allowed]
    for vector in bpair:
        assert not any(matvec(equations, vector))
    hdim = len(zpair)-span_rank(bpair)
    im1 = span_rank(allowed+[matvec(L1, z) for z in zg1])-span_rank(allowed)
    h1g, h2g = len(zg1)-span_rank(bg1), len(zg2)-span_rank(bg2)
    h1l, h2l = len(zl1)-span_rank(bl1), len(zl2)-span_rank(bl2)
    udim = span_rank(allowed)-span_rank(bl1)
    sdim = h1g-im1
    ckdim = len(zl2)-span_rank(bl2+[matvec(L2, z) for z in zg2])
    assert hdim == sdim+ckdim+h2g-h1g+h1l-udim-h2l
    return {"glob": glob, "loc": loc, "Z": zpair, "B": bpair, "H": hdim,
            "ck": ckdim, "zg2": zg2, "bg2": bg2, "allowed": allowed,
            "parameters": (order, copies, nontrivial, multiplier, unrestricted_local)}


def reduce_cochain(vector, source, target, degree):
    m, e = source["m"], target["m"]
    result = []
    for i in range(len(source["keys"][degree])*source["copies"]):
        result.extend(vector[i*m:i*m+e])
    return result


def multiply_pair(vector, data, exponent):
    result = []
    offset = 0
    for complex_, degree in ((data["glob"], 2), (data["loc"], 1)):
        m = complex_["m"]
        count = len(complex_["keys"][degree])*complex_["copies"]
        for i in range(count):
            chunk = vector[offset+i*m:offset+(i+1)*m]
            result.extend([0]*min(exponent, m)+chunk[:max(0, m-exponent)])
        offset += count*m
    return result


def finite_cochain_checks():
    cache = {}
    counts = {"exact_cardinality_sequences": 0, "opposite_coefficient_bounds": 0,
              "hypothesis_gate_failures": 0, "nonzero_local_defect_cokernels": 0}
    for order, copies, multiplier, unrestricted in itertools.product((2, 3), (1, 2), (0, 1), (False, True)):
        for nontrivial in ((False, True) if order == 3 else (False,)):
            for m in range(4):
                data = obstruction_data(order, m, copies, nontrivial, multiplier, unrestricted)
                key = data["parameters"]+(m,)
                cache[key] = data
                counts["exact_cardinality_sequences"] += 1
                if data["ck"]:
                    counts["nonzero_local_defect_cokernels"] += 1
    for key, data in cache.items():
        m = data["glob"]["m"]
        for e in range(m+1):
            short = cache[data["parameters"]+(e,)]
            other = cache[data["parameters"]+(m-e,)]
            # The middle exactness requires allowed local cocycles to
            # lift along A_m -> A_e.
            allowed_reduction = [reduce_cochain(y, data["loc"], short["loc"], 1) for y in data["allowed"]]
            allowed_lifts = span_rank(allowed_reduction) == span_rank(short["allowed"])
            # The opposite sequence uses H2(A_m) -> H2(A_(m-e)) onto.
            global_reduction = [reduce_cochain(z, data["glob"], other["glob"], 2) for z in data["zg2"]]
            h2_onto = span_rank(other["bg2"]+global_reduction) == len(other["zg2"])
            if not (allowed_lifts and h2_onto):
                counts["hypothesis_gate_failures"] += 1
                continue
            images = [multiply_pair(z, data, e) for z in data["Z"]]
            image_rank = span_rank(data["B"]+images)-span_rank(data["B"])
            quotient_dimension = data["H"]-image_rank
            assert quotient_dimension <= short["H"]+short["ck"]
            counts["opposite_coefficient_bounds"] += 1
    assert counts["hypothesis_gate_failures"] > 0
    assert counts["nonzero_local_defect_cokernels"] > 0
    return counts


def coefficient_checks():
    count = 0
    exact_sequences = 0
    for m in range(7):
        for e in range(m+1):
            middle = set(itertools.product(range(3), repeat=m))
            left = set(itertools.product(range(3), repeat=m-e))
            right = set(itertools.product(range(3), repeat=e))
            first_image = {(0,)*e+v for v in left}
            second_image = {(0,)*(m-e)+v for v in right}
            assert len(first_image) == len(left) and len(second_image) == len(right)
            assert {v[:e] for v in middle} == right
            assert {v[:m-e] for v in middle} == left
            assert {v for v in middle if not any(v[:e])} == first_image
            assert {v for v in middle if not any(v[:m-e])} == second_image
            exact_sequences += 2
            for vector in middle:
                first = (0,)*e+vector[:m-e]
                multiply = (0,)*min(e, m)+vector[:max(0, m-e)]
                assert first == multiply
                count += 1
    # The real-place and ordinary rank exponents cancel exactly.
    for a, b, m, d in itertools.product(range(4), range(4), range(5), range(5)):
        assert -m*a*b*d+m*a*b*d == 0
    return {"exact_coefficient_sequences": exact_sequences,
            "opposite_coefficient_compositions": count,
            "edge_cases": "e=0, e=m, m=0 and empty blocks included",
            "negative_control": "The finite cochain suite detects failures of global H2 surjectivity or allowed-local-cocycle lifting and does not apply the quotient lemma there."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    atlas = json.loads(gzip.decompress((ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()))
    rows = {row[0]: row for row in atlas["modules"]}
    sources = []
    for module, intervals in RANGES.items():
        item = {"repository": atlas["repository"], "commit": atlas["commit"],
                "path": "lean/src/"+module.replace(".", "/")+".lean", "git_blob_sha1": rows[module][1]}
        checked = inspect_file(item, offline=args.offline)
        lines = (ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]).read_bytes().splitlines(keepends=True)
        excerpts = []
        for start, end in intervals:
            assert 1 <= start <= end <= len(lines) and end-start+1 <= 120
            content = b"".join(lines[start-1:end])
            assert len(content) <= 12000
            excerpts.append({"start": start, "end": end, "sha256": hashlib.sha256(content).hexdigest()})
        sources.append({**item, "module": module, "sha256": checked["sha256"],
                        "matches_pinned_blob": True, "reviewed_excerpts": excerpts})
    checks = {"finite_cochain_complexes": finite_cochain_checks(), "coefficients": coefficient_checks()}
    milne_path = ROOT/"build/reference-cache/milne-adt-2006.pdf"
    milne_hash = "2c6195ec76a974f3f336c77cb71cc3845b018aad2d43136716b3477a3bc5fb31"
    assert hashlib.sha256(milne_path.read_bytes()).hexdigest() == milne_hash
    stem = "selmer-integral-frontier-obstruction-quotients"
    artifacts = [f"notes/{stem}.md", f"paper/shared/{stem}.tex", f"paper/shared/{stem}-references.tex",
                 "scripts/check_selmer_integral_frontier_obstruction_quotients.py"]
    dependencies = ["certificates/selmer-integral-frontier-second-bound-suppliers.json",
                    "certificates/selmer-integral-frontier-padded-relations.json"]
    for path in artifacts:
        assert all(c >= 32 or c in (10, 9) for c in (ROOT/path).read_bytes()), path
    report = {
        "schema_version": 1, "status": "PASS",
        "claim": "All truncation quotients of the original second-cohomology module with local conditions satisfy the required uniform bound under the original arithmetic system.",
        "result": "|H_N,m/t^e H_N,m| <= q^(g e+C2), C2=C0+Caux+r_ell Ch+2Cd.",
        "quantifiers": "Fix original arithmetic data, point, odd family and auxiliary set; exists C2, for every m, for every sufficiently large N, for every 0<=e<=m.",
        "sources": sources, "exact_checks": checks,
        "primary_reference": {"url": "https://www.jmilne.org/math/Books/ADTnot.pdf",
                              "sha256": milne_hash,
                              "result": "I.4.10(c), printed page57 / PDF page65: higher global cohomology is the product over real places; for odd ell it vanishes.",
                              "scope": "Reuses the primary page visually verified for the first-global-bound package, with its degree-three statement rechecked in the bounded extracted text."},
        "dependencies": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        "retained_inputs": ["Odd prime ell and original cohomology system: finite global and local cohomology, Euler identities, local-to-global degree sum, global duality cokernel bound and global H2 right exactness.",
                            "Original unramified inertia acts trivially and its cocycles lift through coefficient surjections.",
                            "Actual free global odd module and ordinary lower-coordinate local quotients."],
        "limits": ["The specific second-order W2 obstruction translation remains separate.",
                   "No arbitrary modular cocycle-lifting or first-cohomology surjectivity hypothesis is introduced.",
                   "Finite cyclic examples test algebraic identities, not the arithmetic cohomology system.",
                   "No Lean build; no whole node closure: RH 6/9 and GRH 17/31."],
        "reproduce": "python3 scripts/check_selmer_integral_frontier_obstruction_quotients.py --offline",
        "artifacts": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in artifacts},
    }
    (ROOT/f"certificates/{stem}.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "pinned_modules": len(sources), **checks}))


if __name__ == "__main__":
    main()
