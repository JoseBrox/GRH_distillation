#!/usr/bin/env python3
"""Exact diagnostics for the actual compact inverse-parameter supplier.

The all-rank analytic proof is in the shared TeX file.  These checks
authenticate source interfaces and independently exercise the ordered
universal-enveloping-algebra calculation; they are not a Lean build.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
import gzip
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp
from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REPO = "jsmorph/rh"
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
STEM = "global-norm-frontier-off-diagonal"
P = "Formalism.HermitianCurvature."
H = P + "HermitianCurvatureProofs."
SOURCES = [
    (P + "StatementTBB", [(64, 71)]),
    (P + "RealInputsClosedAdmissibleSettings", [(169, 178)]),
    (P + "StatementHeads", [(32, 50)]),
    (P + "OperatorsCommuteTranslations", [(11, 39)]),
    (H + "Imports", [(14, 16)]),
    (H + "SigmaFiniteOfHaar", [(69, 110), (121, 215)]),
    (H + "FirstPeelingMinorMemIdeal", [(42, 72), (102, 179)]),
    (H + "ThirdPeelingMinorMemIdeal", [(61, 147)]),
    (H + "FirstExpansionIdentity", [(48, 129)]),
    (H + "SecondExpansionIdentity", [(54, 125)]),
    (H + "BaseIndexConstantInjective", [(175, 214), (225, 261)]),
    (H + "FirstDerivativeAtNormalSet", [(15, 55), (136, 219)]),
    (H + "LeftFubiniNormalizedTower", [(72, 120)]),
    (H + "RightAverageSmoothComm", [(63, 175)]),
    (H + "PBGLift", [(64, 154)]),
    (H + "DegLiftOf", [(26, 136), (215, 259)]),
]
DEPENDENCIES = [
    "paper/shared/global-norm-frontier-kernel-fourier.tex",
    "paper/shared/global-norm-frontier-mixed-cauchy.tex",
    "paper/shared/global-norm-frontier-partial-head-transfer.tex",
    "paper/shared/global-norm-frontier-jacquet-gram.tex",
    "paper/sections/recovered/79-ca-section.tex",
    "paper/sections/recovered/80-cg-section.tex",
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert (atlas["repository"], atlas["commit"]) == (REPO, REV)
    blobs = {m[0]: m[1] for m in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        rec = inspect_file({"repository": REPO, "commit": REV, "path": path,
                            "git_blob_sha1": blobs[module]}, offline)
        assert rec["matches_pinned_blob"]
        lines = (ROOT / "build/source-cache" / REPO / REV / path).read_bytes().splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            data = b"".join(lines[lo - 1:hi])
            assert len(data) <= 12288
            excerpts.append({"lines": [lo, hi], "bytes": len(data), "sha256": sha(data)})
        records.append({"module": module, **{k: rec[k] for k in [
            "repository", "commit", "path", "bytes", "sha256", "git_blob_sha1", "matches_pinned_blob"]},
                        "excerpts": excerpts})
    return records


def clean(a):
    return {w: c for w, c in a.items() if c}


def add(a, b, factor=Q(1)):
    ans = defaultdict(Q, a)
    for w, c in b.items():
        ans[w] += factor * c
    return clean(ans)


def gen_key(g):
    # All upper nilpotent generators lie last.  This gives an independent
    # induced Whittaker-module reduction after PBW normalization.
    a, b = g
    return (a < b, a, b)


@lru_cache(None)
def pbw(word):
    """Exactly normalize U(gl_n) by xy=yx+[x,y], using a fixed order."""
    for pos in range(len(word) - 1):
        x, y = word[pos:pos + 2]
        if gen_key(x) > gen_key(y):
            pre, post = word[:pos], word[pos + 2:]
            ans = dict(pbw(pre + (y, x) + post))
            a, b = x
            c, d = y
            if b == c:
                ans = add(ans, dict(pbw(pre + ((a, d),) + post)))
            if d == a:
                ans = add(ans, dict(pbw(pre + ((c, b),) + post)), Q(-1))
            return tuple(ans.items())
    return ((word, Q(1)),)


def mul(a, b):
    ans = defaultdict(Q)
    for w1, c1 in a.items():
        for w2, c2 in b.items():
            for w, c in pbw(w1 + w2):
                ans[w] += c1 * c2 * c
    return clean(ans)


def tm(a, b, u):
    ans = {((a, b),): Q(1)}
    if a == b and u:
        ans[()] = Q(u)
    return ans


def parity(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))


def minor(a, b, u):
    assert len(a) == len(b)
    ans = {}
    for perm in itertools.permutations(range(len(a))):
        v = {(): Q(parity(perm))}
        for j in range(len(a)):
            v = mul(v, tm(a[perm[j]], b[j], Q(u) - j))
        ans = add(ans, v)
    return ans


def whit(a):
    ans = defaultdict(Q)
    for word, c in a.items():
        rest = []
        for x, y in word:
            if x < y:
                if y != x + 1:
                    c = Q(0)
                    break
            else:
                rest.append((x, y))
        ans[tuple(rest)] += c
    return clean(ans)


def laplace_checks():
    cases = 0
    # Every ordered injective pair through rank three in gl_3, plus
    # genuinely nonprincipal rank-four cases in gl_5.
    for m in range(1, 5):
        if m <= 3:
            pairs = list(itertools.product(itertools.permutations(range(3), m), repeat=2))
        else:
            pairs = [((0, 1, 2, 3), (0, 1, 2, 3)),
                     ((4, 2, 1, 0), (0, 1, 3, 4)),
                     ((0, 2, 3, 4), (4, 3, 1, 0)),
                     ((3, 2, 1, 0), (3, 2, 1, 0))]
        # m+1 exact nodes certify each degree <= m polynomial identity.
        for a, b in pairs:
            for u in [Q(-2, 3) + v for v in range(m + 1)]:
                q = minor(a, b, u)
                col = row = {}
                for ell in range(m):
                    sign = Q((-1) ** (m - 1 + ell))
                    col = add(col, mul(minor(a[:ell] + a[ell + 1:], b[:-1], u),
                                       tm(a[ell], b[-1], u - m + 1)), sign)
                    row = add(row, mul(minor(a[:-1], b[:ell] + b[ell + 1:], u - 1),
                                       tm(a[-1], b[ell], u)), sign)
                assert q == col, (m, a, b, u, "column")
                assert q == row, (m, a, b, u, "row")
                cases += 1
    return {"maximum_minor_rank": 4, "exact_PBW_Laplace_cases": cases,
            "all_ordered_injective_pairs_gl3": True,
            "method": "PBW in U(gl_n), m+1 rational parameter nodes at degree at most m",
            "status": "PASS"}


def peeling_checks():
    cases = 0
    for j in range(1, 6):
        for i in range(j):
            for u in [Q(-5, 3), Q(0), Q(7, 2)]:
                a = tuple(range(j - 1))
                b = tuple(v for v in range(j) if v != i)
                principal = tuple(range(i))
                assert whit(add(minor(a, b, u), minor(principal, principal, u), Q(-1))) == {}
                dual = lambda seq: tuple(j - 1 - v for v in seq)
                qa = minor(dual(b), dual(a), u + j - 2)
                qb = minor(dual(principal), dual(principal), u + i - 1)
                assert whit(add(qa, qb, Q(-1))) == {}
                cases += 1
    return {"max_head_size": 5, "two_signed_peelings_cases": cases,
            "method": "exact PBW quotient with upper root generators acting by adjacent-root character",
            "s_one_and_empty_head": "included", "status": "PASS"}


def determinant_checks():
    cases = 0
    for i in range(5):
        H = sp.Matrix(i, i, lambda a, b: (a + 2) if a == b else (1 if b == a + 1 else 0))
        for s in range(1, 7):
            t = sp.Rational(3, 2) + sp.I * sp.Rational(2, 5)
            anti = sp.Matrix(s, s, lambda a, b: t if a + b == s - 1 else 0)
            Z = sp.diag(H, anti)
            j = i + s
            cols = [a for a in range(j) if a != i]
            coeff = Z.extract(range(j - 1), cols).det()
            assert sp.simplify(coeff / Z.det() - (-1) ** (s - 1) / t) == 0
            for skip in range(j):
                if skip != i:
                    assert Z.extract(range(j - 1), [a for a in range(j) if a != skip]).det() == 0
            assert sp.simplify(sp.conjugate(coeff / Z.det()) - (-1) ** (s - 1) / sp.conjugate(t)) == 0
            cases += 1
    return {"normal_block_cases": cases, "nonreal_parameter": True,
            "unique_omitted_column_and_both_scalar_ratios": "exact PASS"}


def normalized_pair_checks():
    cases = 0
    A = sp.Matrix([[1, 2 + sp.I], [0, 0]])
    gram = A.conjugate().T * A  # deliberately semidegenerate
    x, y = sp.Matrix([1 + sp.I, 2]), sp.Matrix([3, 2 - sp.I])
    beta = lambda v, w: (w.conjugate().T * gram * v)[0]
    for j in range(1, 8):
        for s in range(1, j + 1):
            for t, tp in [(1 + sp.I, 2 - sp.I), (sp.Rational(3, 2), sp.Rational(3, 2))]:
                cp = (-1) ** (s - 1) / t
                cm = (-1) ** (s - 1) / sp.conjugate(tp)
                got = beta(cp * x, y) - beta(x, cm * y)
                expected = (-1) ** (s - 1) * (1 / t - 1 / tp) * beta(x, y)
                assert sp.simplify(got - expected) == 0
                assert 1 <= 2 * j - s <= 2 * j - 1
                cases += 1
    scalar = 0
    for ah, bh, sw, p, q, det in itertools.product([Q(1, 3), Q(1), Q(7, 2)], repeat=6):
        spw, smw = sw * p, sw * q
        assert ah * bh / (sw * sw) * spw / ah * smw / bh / det == p * q / det
        scalar += 1
    maxima = 0
    for a, b, c, d in itertools.product([Q(0), Q(1, 4), Q(2), Q(9)], repeat=4):
        m1, m2 = max(a, b), max(c, d)
        assert a * c <= m1 * m2 and b * d <= m1 * m2
        assert 4 * m1 * m2 <= (m1 + m2) ** 2
        maxima += 1
    return {"semidegenerate_mixed_leading_cases": cases,
            "two_distinct_point_normalization_cases": scalar,
            "two_independent_extension_maxima_cases": maxima,
            "status": "exact PASS"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    sources = source_records(args.offline)
    checks = {"ordered_minor": laplace_checks(), "actual_peelings": peeling_checks(),
              "normal_head": determinant_checks(), "mixed_normalization": normalized_pair_checks()}
    paths = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", f"scripts/check_{STEM.replace('-', '_')}.py"]
    cert = {"status": "PASS", "classification": "closed local supplier, pending independent review",
            "claim": "Actual compact LiftDegAll, DegLift, and KernelArgumentHypothesisScalar on the original separated finite grids",
            "source_commit": REV, "sources": sources, "checks": checks,
            "files": [{"path": p, "sha256": sha((ROOT / p).read_bytes())} for p in paths],
            "established_mathematical_dependencies": [
                {"path": p, "sha256": sha((ROOT / p).read_bytes())} for p in DEPENDENCIES],
            "proof_scope": "The written argument proves all ranks, heads, compact coefficients and words. Finite exact checks diagnose algebraic order, spectral shifts and normalization only.",
            "not_claimed": ["finite-decay eigenfunction extension", "block-growth limit",
                            "uniform arithmetic top lift", "global theta Gram norms",
                            "W06 or W08 completion", "Lean source build"]}
    (ROOT / "certificates" / (STEM + ".json")).write_text(json.dumps(cert, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "source_count": len(sources), "checks": checks}))


if __name__ == "__main__":
    main()
