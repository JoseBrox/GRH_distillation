#!/usr/bin/env python3
"""Check exact primitive local densities, signs, and original source scope.

The note contains the general proof. These independent finite counts and
exact inequalities are not a Lean build or a global period-norm proof.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
import gzip
import hashlib
import itertools
import json
from pathlib import Path

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "global-norm-frontier-primitive-density"
SR = "Formalism.SharpRestriction.CuspSpanNormBounds."
SOURCES = [
    ("Formalism.LocalRingCardinality.Params", [(6, 46)]),
    (SR + "FractionFieldToGenericStalkAlgebraMapEq",
     [(10, 26), (31, 59), (71, 80)]),
    (SR + "LinQRawRange", [(43, 52), (105, 120), (165, 174)]),
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.SiegelMassRatios.DensExact",
     [(9, 39)]),
    ("Formalism.PeriodIntegrals.UnitaryGroupMassFormula."
     "LocalDensityCorank.CongruenceDensity", [(43, 52)]),
    (SR + "LocalBesselAndTopKernel", [(87, 96), (139, 167), (577, 578)]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def sources(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert (atlas["repository"], atlas["commit"]) == (REPO, REV)
    blobs = {r[0]: r[1] for r in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        rec = inspect_file({"repository": REPO, "commit": REV,
                            "path": path, "git_blob_sha1": blobs[module]}, offline)
        assert rec["matches_pinned_blob"]
        lines = (ROOT / "build/source-cache" / REPO / REV / path).read_bytes().splitlines(keepends=True)
        assert all(1 <= lo <= hi <= len(lines) and hi - lo < 120 for lo, hi in ranges)
        records.append({"module": module,
                        **{k: rec[k] for k in ["repository", "commit", "path", "bytes",
                                               "sha256", "git_blob_sha1", "matches_pinned_blob"]},
                        "excerpts": [{"lines": [lo, hi],
                                      "sha256": sha(b"".join(lines[lo-1:hi]))}
                                     for lo, hi in ranges]})
    return records


def product(q, eta, n, m, c):
    out = Q(1)
    for j in range(n-m-c+1, n+1):
        out *= 1 - Q(eta) ** j * Q(q) ** (-j)
    return out


class QuadraticField:
    """F4=F2[t]/(t²+t+1), F9=F3[t]/(t²−2), without external algebra."""
    def __init__(self, p):
        assert p in (2, 3)
        self.p = p
        self.size = p*p
        self.add = [[((a % p + b % p) % p) + p*((a//p + b//p) % p)
                     for b in range(p*p)] for a in range(p*p)]
        self.neg = [((-a % p) % p) + p*((- (a//p)) % p) for a in range(p*p)]
        self.mul = [[self.multiply(a, b) for b in range(p*p)] for a in range(p*p)]
        self.bar = [self.power(a, p) for a in range(p*p)]
        assert all(self.mul[a][self.bar[a]] < p for a in range(p*p))
        assert all(self.power(a, p*p-1) == 1 for a in range(1, p*p))

    def multiply(self, x, y):
        p = self.p
        a, b, c, d = x % p, x//p, y % p, y//p
        constant = a*c + b*d*(1 if p == 2 else 2)
        linear = a*d + b*c + (b*d if p == 2 else 0)
        return constant % p + p*(linear % p)

    def power(self, x, n):
        out = 1
        for _ in range(n):
            out = self.mul[out][x]
        return out

    def inner(self, x, y):
        out = 0
        for a, b in zip(x, y):
            out = self.add[out][self.mul[self.bar[a]][b]]
        return out

    def scalar(self, a, v):
        return tuple(self.mul[a][b] for b in v)


def matrix_rank_small(entries, m, p):
    if m == 1:
        return int(entries[0] != 0)
    a, b, c, d = entries
    return 2 if (a*d-b*c) % p else int(any(entries))


def inert_case(p, n, m):
    field = QuadraticField(p)
    vectors = list(itertools.product(range(p*p), repeat=n))
    nonzero = vectors[1:]
    norms = {v: field.inner(v, v) for v in vectors}
    hist = Counter()
    if m == 1:
        for v in nonzero:
            hist[(norms[v],)] += 1
        targets = itertools.product(range(p), repeat=1)
    else:
        for v in nonzero:
            span = {field.scalar(a, v) for a in range(p*p)}
            for w in vectors:
                if w not in span:
                    hist[(norms[v], norms[w], field.inner(v, w))] += 1
        targets = itertools.product(range(p), range(p), range(p*p))
    checks = 0
    for target in targets:
        if m == 1:
            rank = int(target[0] != 0)
        else:
            a, b, z = target
            det = (a*b-field.mul[z][field.bar[z]]) % p
            rank = 2 if det else int(any(target))
        predicted = Q(p) ** (2*n*m-m*m) * product(p, -1, n, m, m-rank)
        assert predicted == hist[target], ("inert", p, n, m, target, predicted, hist[target])
        checks += 1
    return {"q": p, "N": n, "m": m, "gram_matrices": checks,
            "primitive_frames": sum(hist.values())}


def split_case(p, n, m):
    vectors = list(itertools.product(range(p), repeat=n))
    nonzero = vectors[1:]
    if m == 1:
        frames = [(v,) for v in nonzero]
    else:
        frames = []
        for v in nonzero:
            span = {tuple(a*x % p for x in v) for a in range(p)}
            frames.extend((v, w) for w in vectors if w not in span)
    hist = Counter()
    for x in frames:
        for y in frames:
            a = tuple(sum(u*v for u, v in zip(xi, yj)) % p for xi in x for yj in y)
            hist[a] += 1
    checks = 0
    for target in itertools.product(range(p), repeat=m*m):
        rank = matrix_rank_small(target, m, p)
        predicted = Q(p) ** (2*n*m-m*m) * product(p, 1, n, m, m-rank)
        assert predicted == hist[target], ("split", p, n, m, target, predicted, hist[target])
        checks += 1
    return {"q": p, "N": n, "m": m, "gram_matrices": checks,
            "primitive_frame_pairs": sum(hist.values())}


def exact_estimates():
    signed = parity = 0
    qs = (2, 3, 4, 5, 7, 8, 9, 11)
    for q in qs:
        for m in range(1, 9):
            for n in range(2*m, 2*m+7):
                for c in range(m+1):
                    d = n-m-c+1
                    split = product(q, 1, n, m, c)
                    inert = product(q, -1, n, m, c)
                    assert 0 < split <= 1
                    assert 1-split <= Q(q)**(-d)/(1-Q(1, q))
                    if d % 2:
                        assert 1 <= inert <= 1+Q(q)**(-d)
                    else:
                        assert 1-Q(q)**(-d) <= inert <= 1
                    signed += 1
        for m in range(2, 13, 2):
            for k in range(m+4, m+23, 2):
                for c in range(m+1):
                    n, d0 = k+m-1, k-m
                    for eta in (-1, 1):
                        density = product(q, eta, n, m, c)
                        assert abs(density-1) <= 2*Q(q)**(-d0)
                        assert density <= 1+Q(q)**(-d0-1)
                        if density > 1:
                            assert eta == -1 and c % 2 and c <= m-1
                        parity += 1
    # Exact norm-vector formulas via independently computed field elements.
    norm_checks = 0
    for p in (2, 3):
        field = QuadraticField(p)
        for n in range(1, 5):
            hist = Counter(field.inner(v, v) for v in itertools.product(range(p*p), repeat=n))
            for a in range(p):
                wanted = p**(2*n-1) + ((p-1) if a == 0 else -1)*(-1)**n*p**(n-1)
                assert hist[a] == wanted
                norm_checks += 1
    return {"signed_endpoint_cases": signed, "original_even_rank_cases": parity,
            "norm_count_cases": norm_checks}


def negative_controls():
    # Removing primitivity destroys the split upper bound.
    vec = list(itertools.product(range(2), repeat=2))
    count = sum(sum(a*b for a, b in zip(x, y)) % 2 == 0 for x in vec for y in vec)
    assert Q(count, 2**3) == Q(5, 4) > 1
    # Replacing a singular residue Gram matrix by a nonsingular one changes density.
    assert product(2, -1, 3, 1, 1) != product(2, -1, 3, 1, 0)
    # The original denominator is 2Nm−m², not Nm.
    n, m, p = 3, 1, 2
    nonzero_norm_count = p**(2*n-1)-(-1)**n*p**(n-1)
    assert Q(nonzero_norm_count, p**(n*m)) != product(p, -1, n, m, 0)
    # Dropping even k loses the extra power in the positive-error bound.
    k, m, c, p = 5, 2, 2, 2
    assert product(p, -1, k+m-1, m, c) > 1+Q(p)**(-(k-m+1))
    return {"controls_rejected": 4,
            "nonprimitive_split_density": "5/4",
            "labels": ["primitivity deletion", "corank deletion", "wrong denominator", "even-rank deletion"]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    records = sources(args.offline)
    counts = []
    for p, maximum in ((2, 4), (3, 3)):
        for n in range(1, maximum+1):
            for m in range(1, min(2, n)+1):
                counts.append({"inert": inert_case(p, n, m),
                               "split": split_case(p, n, m)})
    estimates = exact_estimates()
    controls = negative_controls()
    artifacts = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
                 "scripts/check_global_norm_frontier_primitive_density.py"]
    cert = {
        "schema_version": 1, "status": "PASS", "claim": "Signed refinement of the previously proved original primitive local density",
        "proof": "General proof in the note; finite checks independently verify counts, parity and normalization.",
        "prior_result": {"path": "paper/sections/recovered/70-md-section.tex",
                         "labels": ["md-frame-count", "md-lifting"],
                         "scope": "Exact count and source primitive-density application already proved; no new closure credited here."},
        "not_claimed": ["Lean build", "new closure of the previously proved exact count", "scalar-pair density invariance", "archimedean orbital estimate",
                        "period-Gram bound", "new RH or GRH whole node"],
        "sources": records, "exhaustive_finite_field_counts": counts,
        "exact_checks": estimates, "negative_controls": controls,
        "artifacts": [{"path": path, "sha256": sha((ROOT/path).read_bytes())} for path in artifacts],
    }
    out = ROOT / "certificates" / f"{STEM}.json"
    out.write_text(json.dumps(cert, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "PASS", "sources": len(records),
                      "finite_field_cases": 2*len(counts),
                      "gram_matrices": sum(r[t]["gram_matrices"] for r in counts for t in ("inert", "split")),
                      **estimates, **controls, "certificate": str(out.relative_to(ROOT))}, ensure_ascii=False))


if __name__ == "__main__":
    main()
