#!/usr/bin/env python3
"""Authenticate and check the original first-length recursion assembly."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "global-norm-frontier-first-length"
B = "CompanionTheory.AutomorphicTheory.PieriRules.ThetaBesselIsometries."
SOURCES = [
    (B+"FamilySetupCayleyMoment", [(56, 87), (110, 118), (134, 163), (174, 207)]),
    (B+"FamilySetupCayleyRecursion", [(19, 48)]),
    (B+"TensorBesselTransfer", [(31, 63)]),
    (B+"DualTensorCayleyWeighted", [(30, 68)]),
    ("Development.AbelianVarietyTheory.Proofs.JetHarmonics.LenEqOfUnitriangular",
     [(170, 199)]),
    (B+"FamilySetupBesselGrowth", [(31, 60)]),
]
DEPENDENCIES = ["global-norm-frontier-tensor-projections",
                "global-norm-frontier-normalized-lowering",
                "global-norm-frontier-quotient-mass",
                "global-norm-frontier-mixed-ratio-moments"]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records(offline):
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert (atlas["repository"], atlas["commit"]) == (REPO, REV)
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    out = []
    for module, ranges in SOURCES:
        path = "lean/src/"+module.replace(".", "/")+".lean"
        rec = inspect_file({"repository": REPO, "commit": REV,
                            "path": path, "git_blob_sha1": blobs[module]}, offline)
        assert rec["matches_pinned_blob"]
        lines = (ROOT/"build/source-cache"/REPO/REV/path).read_bytes().splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            data = b"".join(lines[lo-1:hi])
            assert len(data) <= 12_288
            excerpts.append({"lines": [lo, hi], "bytes": len(data), "sha256": sha(data)})
        out.append({"module": module,
                    **{key: rec[key] for key in
                       ["repository", "commit", "path", "bytes", "sha256",
                        "git_blob_sha1", "matches_pinned_blob"]},
                    "excerpts": excerpts})
    return out


def scalar(matrix):
    return sp.simplify(matrix[0])


def equal(a, b):
    if isinstance(a, sp.MatrixBase):
        return all(sp.simplify(x) == 0 for x in a-b)
    return sp.simplify(a-b) == 0


def flag_evaluation_checks():
    cases = rank_zero = isotropic = 0
    for n, u, tau in itertools.product([2, 3, 4],
                                       [sp.Rational(1, 3), sp.Rational(1, 2)],
                                       [sp.Integer(1), sp.Integer(2)]):
        J = sp.diag(1, -1, *([1]*(n-2)))
        boost = sp.eye(n)
        boost[0, 0] = boost[1, 1] = (1+u*u)/(1-u*u)
        boost[0, 1] = boost[1, 0] = 2*u/(1-u*u)
        g = sp.diag(sp.I, -sp.I, *([1]*(n-2)))*boost
        assert equal(g.H*J*g, J)
        Q = sp.eye(n)
        Q[0, 0] = Q[1, 1] = sp.Rational(3, 5)
        Q[0, 1] = Q[1, 0] = 4*sp.I/5
        assert equal(Q.H*Q, sp.eye(n))
        vectors = [("r0", sp.Matrix([0, tau*sp.I]+[0]*(n-2)))]
        if n >= 4:
            vectors.append(("isotropic", sp.Matrix([1/sp.sqrt(2), sp.I/sp.sqrt(2)]+[0]*(n-2))))
        for kind, f in vectors:
            omega = J*sp.conjugate(f)
            dual_g = g.inv().T
            values = []
            for d in range(n):
                covector = dual_g*Q.row(d).T
                evaluation = scalar(f.T*covector)
                contraction = scalar(omega.H*J*covector)
                assert equal(evaluation, contraction)
                values.append(evaluation)
            length_sq = scalar((g.inv()*f).H*(g.inv()*f))
            assert equal(sum(v*sp.conjugate(v) for v in values), length_sq)
            if kind == "r0":
                assert equal(scalar(f.H*J*f), -tau*tau)
                rank_zero += 1
            else:
                assert scalar(f.H*J*f) == 0
                isotropic += 1
            cases += 1
    return {"complex_flag_evaluations": cases, "r_zero_cases": rank_zero,
            "isotropic_first_vector_cases": isotropic}


def cauchy_checks():
    cases = zero_terms = 0
    for n in range(2, 7):
        for offset in range(5):
            zs = [sp.Matrix([j-offset+sp.I*(j+1),
                             (j+offset)*sp.I-(j % 2)]) for j in range(n)]
            if offset == 0:
                zs[-1] = sp.zeros(2, 1)
                zero_terms += 1
            total = sum(zs, sp.zeros(2, 1))
            deficit = sp.simplify(n*sum(scalar(z.H*z) for z in zs)-scalar(total.H*total))
            pairwise = sum(scalar((zs[i]-zs[j]).H*(zs[i]-zs[j]))
                           for i in range(n) for j in range(i+1, n))
            assert equal(deficit, pairwise) and deficit >= 0
            cases += 1
    # Without the factor n, two equal nonzero summands violate the bound.
    z = sp.Matrix([1, 0])
    assert scalar((2*z).H*(2*z)) > 2*scalar(z.H*z)
    return {"exact_vector_cauchy_cases": cases, "zero_summand_cases": zero_terms,
            "missing_dimension_factor_negative_control": True}


def reserve_checks():
    transitions = zero_moments = 0
    for n in range(2, 5):
        for nu in itertools.product(range(-2, 3), repeat=n):
            size = sum(abs(x) for x in nu)
            for a in range(5):
                q0 = size+a
                for j in [0, 4*n*n-2*a]:
                    assert size+a <= q0 and j+2*a <= 4*n*n
                    if a == 0:
                        zero_moments += 1
                        continue
                    for s in range(n):
                        new = list(nu)
                        new[s] -= 1
                        assert sum(abs(x) for x in new)+(a-1) <= q0
                        assert (j+2)+2*(a-1) <= 4*n*n
                        transitions += 1
    nu, q0 = (-3, 0), 3
    assert sum(abs(x) for x in nu) == q0
    assert sum(abs(x) for x in (-4, 0)) > q0
    return {"shift_and_level_transitions": transitions,
            "zero_moment_boundaries": zero_moments,
            "missing_shift_reserve_negative_control": True}


def polynomial_checks():
    x, y, ell, spare, extra = sp.symbols("x y ell spare extra", nonnegative=True)
    # b>=B>=36 makes (6B)^2<=b^3.
    base, b = y+36, y+36+x
    p = sp.Poly(sp.expand(b**3-36*base**2), x, y)
    assert all(c >= 0 for c in p.coeffs())
    # m>=2 gives 3m+5<=6m.
    assert sp.expand(6*(2+extra)-(3*(2+extra)+5)) == 3*extra+1
    # The full b>=10^6 n^7 hypothesis implies b>=n^2 and b>=36.
    n = extra+2
    lower = 10**6*n**7
    for margin in [lower-n*n, lower-36]:
        assert all(c > 0 for c in sp.Poly(sp.expand(margin), extra).coeffs())
    m = 2*ell+spare
    product_margin = sp.Poly(sp.expand(4*m*m-6*m*ell-2*ell*(ell-1)), ell, spare)
    assert all(c >= 0 for c in product_margin.coeffs())
    return {"squared_base_comparison": str(p.as_expr()),
            "product_exponent_margin": str(product_margin.as_expr()),
            "auxiliary_nonnegative_polynomials": 3}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources = source_records(args.offline)
    dependencies = []
    for stem in DEPENDENCIES:
        certificate = ROOT/"certificates"/(stem+".json")
        data = json.loads(certificate.read_text())
        assert data["status"] == "PASS"
        for artifact in data["artifacts"]:
            assert sha((ROOT/artifact["path"]).read_bytes()) == artifact["sha256"]
        dependencies.append({"path": str(certificate.relative_to(ROOT)),
                             "sha256": sha(certificate.read_bytes())})
    checks = {"flag_evaluation": flag_evaluation_checks(),
              "cauchy": cauchy_checks(), "reserves": reserve_checks(),
              "power_comparisons": polynomial_checks()}
    artifacts = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
                 f"paper/shared/{STEM}-references.tex",
                 "scripts/check_global_norm_frontier_first_length.py"]
    data = {
        "date": "2026-11-22", "status": "PASS",
        "claim": "The actual first-length moment is bounded by "
                 "[n^2*T*b^4*(6B)^(2m)]^a ||v||^2 under the original integer "
                 "shift and level reserves. Mixed flag products are bounded "
                 "relative to the same Bessel quotient norm.",
        "novelty": "Assembly of the newly supplied tensor, lowering, and quotient "
                   "mass estimates; no first-length moment remains assumed.",
        "sources": sources, "supplier_certificates": dependencies,
        "exact_checks": checks,
        "artifacts": [{"path": path, "sha256": sha((ROOT/path).read_bytes())}
                      for path in artifacts],
        "limitations": [
            "Original discrete-series, Pieri family and subgroup-period Bessel map "
            "existence remain retained inputs.",
            "The same quotient norm is proved; identification with the original "
            "leading-minor Jacquet/Gram expression remains open.",
            "No factor T^ell is dropped. The original real-parameter reserve is "
            "not silently replaced by the smaller integer-family reserve.",
            "Weighted orbital estimates and global norm assembly remain separate.",
            "Exact finite checks supplement the written proof; no Lean build or whole-node claim."
        ],
        "reproduce": "python3 scripts/check_global_norm_frontier_first_length.py --offline"
    }
    output = ROOT/"certificates"/(STEM+".json")
    output.write_text(json.dumps(data, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "supplier_certificates": len(dependencies), "checks": checks,
                      "certificate": str(output.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
