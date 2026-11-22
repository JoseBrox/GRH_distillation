#!/usr/bin/env python3
"""Exact checks for the original low-level tensor projection supplier.

Authenticates bounded source excerpts and checks algebra/constants. Finite
matrix models supplement, rather than replace, the general proof in the TeX.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "global-norm-frontier-tensor-projections"
J = "Development.AbelianVarietyTheory.Proofs.JetHarmonics."
B = "CompanionTheory.AutomorphicTheory.PieriRules.ThetaBesselIsometries."
SOURCES = [
    ("Development.AbelianVarietyTheory.Definitions.Jets.SumIoPr",
     [(16, 30), (39, 57)]),
    (J + "UnitaryGlModuleLevelOffDiagNormSqLe", [(148, 172)]),
    (J + "UnitaryGlModuleProjComponentsLevelAddTwo", [(11, 35)]),
    (J + "UnitaryGlModuleProjDualTensorLevelAddTwo", [(13, 43)]),
    (J + "InvariantHermitianFormNonnegOfCloudEigen", [(12, 58)]),
    (J + "CloudNodeProjectionNormLowLevel", [(17, 92)]),
    (J + "SumNormSqProjectionsTensorUnitaryGlLe", [(15, 44)]),
    (B + "FamilySetupCayleyMoment", [(134, 163)]),
    (B + "FamilySetupMomentGrowth", [(66, 113)]),
    (B + "DualTensorBesselMoment", [(88, 95)]),
    (J + "LoweringBound", [(12, 25), (43, 49), (70, 89)]),
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
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            part = b"".join(lines[lo-1:hi])
            assert len(part) <= 12_288
            excerpts.append({"lines": [lo, hi], "bytes": len(part), "sha256": sha(part)})
        out.append({"module": module,
                    **{k: rec[k] for k in ["repository", "commit", "path", "bytes",
                                           "sha256", "git_blob_sha1", "matches_pinned_blob"]},
                    "excerpts": excerpts})
    return out


def polynomial_checks():
    mu, rho, rk = sp.symbols("mu rho rho_K")
    lam = mu+rho-2*rk
    compact = (lam+rk)**2-rk**2
    assert sp.expand(2*compact-(mu**2-rho**2)-lam**2
                     -(2*mu*rho+2*rho**2-4*rk**2)) == 0
    x, y = sp.symbols("x y", nonnegative=True)
    n = x+1
    bound = 10**6*n**7+y
    off = (384*n**4+51*n**2)*bound+1152*n**6+n**3/sp.Integer(2)
    expressions = {
        "small_off_diagonal": 512*n**4*bound-off,
        "off_diagonal_scale": bound-131072*n**5,
        "weight_interval_reserve": sp.Rational(17, 800)*bound-6*n**2-sp.Rational(3, 2)*n,
        "lowest_weight_bound": bound-2*n,
        "projection_sum_constant": 36*bound**2-9*bound-2,
    }
    coefficients = []
    for name, value in expressions.items():
        poly = sp.Poly(sp.expand(value), x, y)
        assert all(c >= 0 for c in poly.coeffs())
        coefficients.append({"inequality": name, "degree": poly.total_degree(),
                             "terms": len(poly.terms()),
                             "all_coefficients_nonnegative": True})
    # The exact circle-distance and resolvent constants.
    assert sp.Rational(18, 32)-sp.Rational(3, 32) == sp.Rational(15, 32)
    assert sp.Rational(31, 32)-sp.Rational(16, 32) == sp.Rational(15, 32)
    assert sp.Rational(15, 32)-sp.Rational(1, 16) == sp.Rational(13, 32)
    assert sp.Rational(9, 16)/sp.Rational(13, 32) == sp.Rational(18, 13)
    assert sp.Rational(1, 16)/sp.Rational(15, 16) == sp.Rational(1, 15)
    assert 1-2*sp.Rational(1, 15)**2 == sp.Rational(223, 225)
    return {"casimir_cancellation": True,
            "substitution": "n=x+1, B0=10^6*n^7+y, x,y>=0",
            "coefficient_certificates": coefficients,
            "exact_circle_and_sign_constants": 6}


def zero(a):
    return all(sp.cancel(z) == 0 for z in a)


def reduced(a):
    return a.applyfunc(sp.cancel)


def hs_square(a):
    return sp.cancel(sum(sp.conjugate(z)*z for z in a))


def positive_definite(a):
    assert zero(a.H-a)
    return all(a[:j, :j].det() > 0 for j in range(1, a.rows+1))


def projection_checks():
    models = interpolations = empty = 0
    for n, k in [(2, 1), (3, 1), (3, 2), (4, 2), (5, 2), (5, 4),
                  (6, 3), (6, 5), (7, 2), (7, 6)]:
        cloud = list(range(k-1))
        nodes = list(range(k-1, n))
        m = len(nodes)
        bound = sp.Integer(10**6*n**7)
        signs = [1 if a in cloud else -1 for a in range(n)]
        form = sp.diag(*signs)
        g = sp.eye(n)
        if cloud:
            t = sp.Rational(1, 1000)
            c, s = (1+t*t)/(1-t*t), 2*t/(1-t*t)
            a, b = cloud[-1], nodes[0]
            g[a, a] = g[b, b] = c
            g[a, b] = g[b, a] = s
        else:
            empty += 1
        gi = reduced(form*g.H*form)
        assert zero(g.H*form*g-form) and zero(g*gi-sp.eye(n))
        eigenvalues = [(-bound/sp.Integer(16)+2*a if a in cloud
                        else bound+2*(a-(k-1))) for a in range(n)]
        diag = sp.diag(*eigenvalues)
        operator = reduced(g*diag*gi)
        off = operator-diag
        # A stronger Frobenius-norm bound certifies the needed operator bound.
        assert hs_square(off) <= (bound/16)**2
        assert zero(operator.H*form-form*operator)
        projections = []
        for a in range(n):
            e = sp.zeros(n)
            e[a, a] = 1
            proj = reduced(g*e*gi)
            projections.append(proj)
            assert zero(operator*proj-eigenvalues[a]*proj)
            assert zero(proj*proj-proj)
            column = g[:, a]
            assert sp.cancel((column.H*form*column)[0]) == signs[a]
        pc = sum((projections[a] for a in cloud), sp.zeros(n))
        assert positive_definite(sp.Rational(18, 13)**2*sp.eye(n)-pc.H*pc)
        for a in nodes:
            polynomial = sp.eye(n)-pc
            for b in nodes:
                if a != b:
                    polynomial = reduced((operator-eigenvalues[b]*sp.eye(n))*polynomial
                                         /(eigenvalues[a]-eigenvalues[b]))
            assert zero(polynomial-projections[a])
            assert hs_square(projections[a]) <= 9*(6*bound)**(2*m-2)
            interpolations += 1
        assert positive_definite((6*bound)**(2*m)*sp.eye(n)-gi.H*gi)
        models += 1
    return {"exact_indefinite_projection_models": models,
            "exceptional_projection_interpolations": interpolations,
            "empty_cloud_models": empty,
            "scope": "Finite models check the spectral/sign algebra, not existence of the original representations."}


def controls():
    # A fixed spectral gap and signed isometries alone do not give small norms.
    t = sp.Rational(9, 10)
    c, s = (1+t*t)/(1-t*t), 2*t/(1-t*t)
    g = sp.Matrix([[c, s], [s, c]])
    form = sp.diag(1, -1)
    gi = form*g.T*form
    projector = g*sp.diag(1, 0)*gi
    assert zero(g.T*form*g-form)
    assert zero(projector*projector-projector)
    assert hs_square(projector) > 100
    operator = g*sp.diag(0, 1)*gi
    assert operator.eigenvals() == {sp.Integer(0): 1, sp.Integer(1): 1}
    return {"controls_rejected": 1,
            "label": "fixed eigenvalue gap and signed isometries without small off-diagonal control",
            "rank_one_projector_squared_operator_norm": str(hs_square(projector))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources = source_records(args.offline)
    exact = {"algebra_and_constants": polynomial_checks(),
             "projection_models": projection_checks(), "negative_control": controls()}
    artifacts = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
                 f"paper/shared/{STEM}-references.tex",
                 "scripts/check_global_norm_frontier_tensor_projections.py"]
    certificate = {
        "date": "2026-11-22", "status": "PASS",
        "claim": "Original indefinite dual-tensor projection sum and level increase by two, "
                 "with exponent 2*(2r+2) independent of compact-cloud size.",
        "new_supplier": "Casimir diagonal cancellation, small off-diagonal bound, "
                        "cloud resolvent and exceptional spectral interpolation for original projections.",
        "retained_data": ["original level and parameter shape", "original Hilbert norm",
                          "original indefinite tensor form and signed isometries",
                          "actual split-Casimir eigenvalues", "exact exponent 2*(2r+2)"],
        "sources": sources, "exact_checks": exact,
        "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())}
                      for p in artifacts],
        "limitations": ["Original tensor-decomposition existence is retained as a hypothesis, as in source target.",
                        "Normalized Bessel lowering constants and original mass/isometry remain open.",
                        "Finite checks supplement the general proof; no Lean build.",
                        "No original leading-minor norm or weighted orbital norm theorem yet.",
                        "No RH/GRH whole-node count change."],
        "reproduce": "python3 scripts/check_global_norm_frontier_tensor_projections.py --offline",
    }
    output = ROOT/"certificates"/f"{STEM}.json"
    output.write_text(json.dumps(certificate, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "checks": exact, "certificate": str(output.relative_to(ROOT))},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
