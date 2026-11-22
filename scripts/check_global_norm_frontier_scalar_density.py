#!/usr/bin/env python3
"""Authenticate the scalar-pair density proof and audit exact lattice algebra.

The general proof is in the note. Finite checks do not assert an unrun Lean
build, an archimedean Bessel estimate or a whole RH/GRH node completion.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

from check_sources import inspect_file
from check_global_norm_frontier_primitive_density import product

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "global-norm-frontier-scalar-density"
SR = "Formalism.SharpRestriction.CuspSpanNormBounds."
SOURCES = [
    (SR + "FractionFieldToGenericStalkAlgebraMapEq",
     [(10, 26), (31, 59), (76, 80)]),
    (SR + "LinQRawRange",
     [(12, 19), (43, 78), (105, 120), (133, 174)]),
    (SR + "LocalBesselAndTopKernel", [(87, 96), (149, 167)]),
    ("Formalism.LocalRingCardinality.Params", [(6, 46)]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert (atlas["repository"], atlas["commit"]) == (REPO, REV)
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    out = []
    for module, ranges in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        rec = inspect_file({"repository": REPO, "commit": REV,
                            "path": path, "git_blob_sha1": blobs[module]}, offline)
        assert rec["matches_pinned_blob"]
        data = (ROOT / "build/source-cache" / REPO / REV / path).read_bytes()
        lines = data.splitlines(keepends=True)
        assert all(1 <= lo <= hi <= len(lines) and hi-lo < 120 for lo, hi in ranges)
        out.append({"module": module,
                    **{k: rec[k] for k in ["repository", "commit", "path", "bytes",
                                           "sha256", "git_blob_sha1", "matches_pinned_blob"]},
                    "excerpts": [{"lines": [lo, hi],
                                  "sha256": sha(b"".join(lines[lo-1:hi]))}
                                 for lo, hi in ranges]})
    return out


def block_gram(z, w, t, tp):
    a = z.rows
    e = sp.zeros(a)
    e[a-1, a-1] = 1
    return (-t*e).row_join(z).col_join(w.row_join(-tp*e))


def determinant_checks():
    symbolic = numerical = modified = 0
    t, tp = sp.symbols("t tp")
    for a in (1, 2):
        z = sp.Matrix(a, a, sp.symbols(f"z0:{a*a}"))
        w = sp.Matrix(a, a, sp.symbols(f"w0:{a*a}"))
        expected = (-1)**a * (z.det()*w.det()
                     - t*tp*z[:a-1, :a-1].det()*w[:a-1, :a-1].det())
        assert sp.expand(block_gram(z, w, t, tp).det() - expected) == 0
        symbolic += 1
    for a in range(1, 5):
        for seed in range(6):
            z = sp.Matrix(a, a, lambda i, j:
                          (a+seed+7 if i == j else (i+2*j+seed) % 3 - 1)
                          + sp.I*((2*i+j+seed) % 3 - 1))
            w = z.conjugate().T
            t0, tp0 = sp.Rational(seed+1, 3), sp.Rational(seed+2, 5)
            raw = block_gram(z, w, t0, tp0)
            expected = (-1)**a*(z.det()*w.det()
                     - t0*tp0*z[:a-1, :a-1].det()*w[:a-1, :a-1].det())
            det_raw = sp.expand(raw.det(method="domain-ge"))
            assert sp.expand(det_raw-expected) == 0
            assert det_raw != 0
            numerical += 1
            for level in (2, 6, 15):
                # Column change: (f,f') -> (f,(f'-f)/level).
                b = sp.eye(a).row_join(-sp.eye(a)/level).col_join(
                    sp.zeros(a).row_join(sp.eye(a)/level))
                transformed = b.conjugate().T * raw * b
                assert sp.expand(transformed.det(method="domain-ge")
                                 - det_raw/sp.Integer(level)**(2*a)) == 0
                modified += 1
    return {"symbolic_block_identities": symbolic,
            "nontrivial_conjugation_cases": numerical,
            "exact_modified_tuple_determinants": modified}


def invariant_factors(matrix, nonunits=False):
    d = smith_normal_form(matrix, domain=sp.ZZ)
    entries = [abs(int(d[i, i])) for i in range(min(d.rows, d.cols))]
    assert all(entries)
    return [x for x in entries if x != 1] if nonunits else entries


def rank_mod(matrix, p):
    a = [[int(matrix[i, j]) % p for j in range(matrix.cols)]
         for i in range(matrix.rows)]
    rank = 0
    for col in range(matrix.cols):
        piv = next((i for i in range(rank, matrix.rows) if a[i][col]), None)
        if piv is None:
            continue
        a[rank], a[piv] = a[piv], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(x*inv) % p for x in a[rank]]
        for row in range(matrix.rows):
            if row != rank and a[row][col]:
                scalar = a[row][col]
                a[row] = [(x-scalar*y) % p for x, y in zip(a[row], a[rank])]
        rank += 1
        if rank == matrix.rows:
            break
    return rank


def complement_checks():
    modules = reductions = 0
    for m in range(1, 5):
        for extra in (0, 1, 3):
            n = 2*m+extra
            for seed in range(6):
                c = sp.Matrix(m, m, lambda i, j: (i+2*j+seed) % 3 - 1)
                a = sp.diag(*[2**((seed+j) % 3) * 3**((seed+2*j) % 2)
                              * 5**((seed+j) % 2) for j in range(m)])
                left, right = sp.eye(m), sp.eye(m)
                for j in range(m-1):
                    left[j, j+1] = seed+j+1
                    right[j+1, j] = 1-seed-j
                a = left*a*right
                d = (a-c).T
                x = sp.eye(m).col_join(c).col_join(sp.zeros(extra, m))
                y = d.col_join(sp.eye(m)).col_join(sp.zeros(extra, m))
                kp = sp.eye(m).row_join(sp.zeros(m, extra)).col_join(
                    (-d.T).row_join(sp.zeros(m, extra))).col_join(
                    sp.zeros(extra, m).row_join(sp.eye(extra)))
                km = (-c.T).row_join(sp.zeros(m, extra)).col_join(
                    sp.eye(m).row_join(sp.zeros(m, extra))).col_join(
                    sp.zeros(extra, m).row_join(sp.eye(extra)))
                # An integral ambient isometry in the split algebra acts by
                # S on the first component and (S^-1)^T on the second.
                s = sp.eye(n)
                for j in range(n-1):
                    s[j, j+1] = (j+seed) % 3 - 1
                dual = s.inv().T
                x, kp, y, km = s*x, s*kp, dual*y, dual*km
                assert y.T*kp == sp.zeros(m, m+extra)
                assert x.T*km == sp.zeros(m, m+extra)
                assert invariant_factors(x) == [1]*m
                assert invariant_factors(y) == [1]*m
                assert invariant_factors(kp) == [1]*(m+extra)
                assert invariant_factors(km) == [1]*(m+extra)
                gm, gk = y.T*x, km.T*kp
                assert gm == a
                factors = invariant_factors(gm, True)
                assert invariant_factors(gk, True) == factors
                assert invariant_factors(x.row_join(kp), True) == factors
                assert invariant_factors(y.row_join(km), True) == factors
                modules += 1
                for p in (2, 3, 5, 7):
                    cm = m-rank_mod(gm, p)
                    ck = m+extra-rank_mod(gk, p)
                    assert cm == ck == sum(v % p == 0 for v in factors)
                    assert rank_mod(gm, p) == rank_mod(gm.T, p)
                    reductions += 1
    return {"split_discriminant_module_cases": modules,
            "independent_residue_rank_cases": reductions,
            "module_maps_checked": ["M discriminant", "K discriminant",
                                    "Lambda/(M+K), first component",
                                    "Lambda/(M+K), second component"]}


def integral_at(x, p):
    return Q(x).denominator % p != 0


def split_level_checks():
    cases = congruent = weaker_failures = 0
    for p in (2, 3, 5):
        values = [Q(j, p*p) for j in range(-p*p, p*p+1)]
        for unit in (1, p+1, 2*p+1):
            level = p*unit
            for a, b in itertools.product(values, repeat=2):
                # Modified-basis coordinates of u-u' are (a-b,-level*b).
                divided = ((a-b)/level, -b)
                graph = all(integral_at(x, p) for x in divided)
                expected = integral_at(a, p) and integral_at(b, p) \
                           and integral_at((a-b)/level, p)
                assert graph == expected
                if graph:
                    assert integral_at(a, p) and integral_at(b, p)
                    congruent += 1
                weaker = integral_at(a-b, p) and integral_at(-level*b, p)
                if weaker and not (integral_at(a, p) and integral_at(b, p)):
                    weaker_failures += 1
                cases += 1
    assert congruent > 0 and weaker_failures > 0
    return {"exact_local_coefficient_cases": cases,
            "valid_congruence_cases": congruent,
            "weaker_condition_failures": weaker_failures,
            "original_generators_retained": True}


def controls():
    # Without primitive M, its discriminant can change while K does not.
    p = 3
    assert 1-rank_mod(sp.Matrix([[p*p]]), p) == 1
    assert 2-rank_mod(sp.eye(2), p) == 0
    # Without self-duality of Lambda=p O^3, primitive complementary
    # coordinate sublattices have unequal residue coranks.
    assert 1-rank_mod(p*p*sp.eye(1), p) != 2-rank_mod(p*p*sp.eye(2), p)
    # Mere integral difference at a split level loses coefficient integrality.
    a = b = Q(1, p)
    assert integral_at(a-b, p) and integral_at(-p*b, p)
    assert not integral_at(b, p)
    assert not integral_at(-b, p)
    # An actual rank-two designated tuple: f=e1, f'=e1+p e2.
    # Its modified tuple is (e1,e2). T=-1,T'=-(1+p²), Z=1.
    # Both T are units; T-T'=p²; Gdet=-p² != 0.
    # The raw tuple is not primitive and has a different residue corank.
    raw = sp.Matrix([[1, 1], [1, 1+p*p]])
    changed = sp.Matrix([[1, -Q(1, p)], [0, Q(1, p)]])
    assert changed.T*raw*changed == sp.eye(2)
    assert 2-rank_mod(raw, p) == 1
    assert 2-rank_mod(sp.eye(2), p) == 0
    assert product(p, 1, 7, 2, 1) != product(p, 1, 7, 2, 0)
    # The cross determinant alone does not imply nondegeneracy.
    assert block_gram(sp.eye(1), sp.eye(1), 1, 1).det() == 0
    return {"controls_rejected": 5,
            "labels": ["primitivity deletion", "self-duality deletion",
                       "split graph replaced by integral difference",
                       "modified tuple replaced by raw tuple",
                       "nonzero Gdet condition deleted"],
            "actual_modified_tuple_example": {"r": 0, "p": 3, "N": 7,
                "T": -1, "T_prime": -10, "Gdet": -9,
                "modified_corank": 0, "raw_corank": 1}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources = source_records(args.offline)
    exact = {"determinants": determinant_checks(),
             "complements": complement_checks(),
             "split_level": split_level_checks(),
             "negative_controls": controls()}
    artifacts = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
                 "scripts/check_global_norm_frontier_scalar_density.py"]
    dependencies = ["certificates/global-norm-frontier-primitive-density.json",
                    "paper/sections/recovered/70-md-section.tex"]
    certificate = {
        "date": "2026-11-22", "status": "PASS",
        "claim": "Original scalar pairs have equal primitive local densities; "
                 "with the already proved density bound this proves T1 with constant one.",
        "new_result": "Isometry of the original orthogonal-intersection lattices, "
                      "hence isomorphism of the modified frame discriminant modules.",
        "retained_data": ["maximal integral algebra", "original modified tuple",
                          "original designated split generator and congruence graph",
                          "both integral quotient-lattice images",
                          "each original self-dual lattice; common residue field and density denominator"],
        "sources": sources, "exact_checks": exact,
        "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())}
                      for p in artifacts],
        "dependencies": [{"path": p, "sha256": sha((ROOT/p).read_bytes())}
                         for p in dependencies],
        "limitations": ["Finite checks supplement the general proof in the note.",
                        "No full Lean build.",
                        "No new closure of the previously proved primitive count.",
                        "No other local assertion or global period norm estimate.",
                        "No RH or GRH whole-node count change."],
        "reproduce": "python3 scripts/check_global_norm_frontier_scalar_density.py --offline",
    }
    output = ROOT/"certificates"/f"{STEM}.json"
    output.write_text(json.dumps(certificate, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "checks": exact, "certificate": str(output.relative_to(ROOT))},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
