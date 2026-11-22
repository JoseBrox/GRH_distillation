#!/usr/bin/env python3
"""Authenticate bounded sources and check exact flag-moment calculations.

The general proofs are in the note. This checker does not supply the original
Bessel isometry, the first-length recursion, a Lean build or a whole node.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import subprocess

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PRIOR = "1d6b784075cf61ce5d6b2f1b03cb0196c64130ab"
REPO = "jsmorph/rh"
STEM = "global-norm-frontier-mixed-ratio-moments"
J = "Development.AbelianVarietyTheory.Proofs.JetHarmonics."
F = "Development.AbelianVarietyTheory.Proofs.FlagMeasures."
B = "CompanionTheory.AutomorphicTheory.PieriRules.ThetaBesselIsometries."
SOURCES = [
    ("Development.AbelianVarietyTheory.Definitions.Jets.SumIoPr",
     [(16, 30), (53, 57)]),
    (J + "ExistsLieUnitaryElementSimpleRoot", [(55, 112)]),
    (B + "BesselCayleySideBound", [(60, 118)]),
    (B + "FamilySetupCayleyBound", [(78, 94), (185, 213)]),
    (B + "FamilySetupCayleyRecursion", [(19, 49)]),
    (F + "ProductMomentFirstLengthsLowestVector", [(66, 115)]),
    (F + "BesselExteriorPowerConstantBoundLargeGap", [(34, 45)]),
    (B + "FamilySetupBesselGrowth", [(31, 68)]),
    (B + "FamilySetupCayleyMoment", [(110, 150), (160, 207)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.OnePlaceEstimates",
     [(57, 77)]),
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
        excerpts = []
        for lo, hi in ranges:
            part = b"".join(lines[lo-1:hi])
            assert len(part) <= 12_288
            excerpts.append({"lines": [lo, hi], "bytes": len(part), "sha256": sha(part)})
        out.append({"module": module,
                    **{k: rec[k] for k in ["repository", "commit", "path", "bytes",
                                           "sha256", "git_blob_sha1", "matches_pinned_blob"]},
                    "excerpts": excerpts})
    prior_path = "paper/sections/recovered/77-dc-section.tex"
    data = subprocess.check_output(["git", "show", f"{PRIOR}:{prior_path}"], cwd=ROOT)
    prior_excerpt = b"".join(data.splitlines(keepends=True)[502:596])
    return out, {"repository": "JoseBrox/GRH_distillation", "commit": PRIOR,
                 "path": prior_path, "sha256": sha(data),
                 "lines": [503, 596], "excerpt_sha256": sha(prior_excerpt),
                 "role": "Existing Casimir energy argument, reused rather than new"}


def reduced(a):
    return a.applyfunc(sp.cancel)


def square_norm(v):
    return sp.cancel((v.H*v)[0])


def is_zero(a):
    return all(sp.cancel(x) == 0 for x in a)


def unitary_matrix(signs, variant):
    """Products of exact rational compact rotations and hyperbolic rotations."""
    n = len(signs)
    g = sp.eye(n)
    for j in range(n-1):
        t = sp.Rational(1+((j+variant) % 2), 5)
        a = sp.eye(n)
        if signs[j] == signs[j+1]:
            c, s = (1-t*t)/(1+t*t), 2*t/(1+t*t)
            a[j, j] = a[j+1, j+1] = c
            a[j, j+1], a[j+1, j] = s, -s
        else:
            c, s = (1+t*t)/(1-t*t), 2*t/(1-t*t)
            a[j, j] = a[j+1, j+1] = c
            a[j, j+1] = a[j+1, j] = s
        g = reduced(a*g)
    phase = sp.eye(n)
    phase[variant % n, variant % n] = sp.Rational(3, 5) + sp.I*sp.Rational(4, 5)
    return reduced(phase*g)


def flag_checks():
    cases = adjacent = 0
    for r, k, variant in [(1, 1, 0), (1, 2, 1), (2, 1, 0), (2, 2, 1),
                          (3, 1, 0), (3, 2, 1)]:
        n, p = 2*r+k+1, r+k
        signs = [1]*p + [-1]*(r+1)
        form = sp.diag(*signs)
        g = unitary_matrix(signs, variant)
        assert is_zero(g.H*form*g-form)
        gi = reduced(form*g.H*form)
        assert is_zero(g*gi-sp.eye(n))
        f = [sp.eye(n)[:, a]+sp.eye(n)[:, p+a] for a in range(r)]
        f.append(sp.eye(n)[:, p+r])
        vs = [reduced(gi*x) for x in f]
        residuals = []
        for v in vs:
            e = v
            for previous in residuals:
                e = reduced(e-previous*((previous.H*v)[0]/square_norm(previous)))
            assert square_norm(e) > 0
            residuals.append(e)
        for a in range(r):
            e, u = residuals[a], residuals[a+1]
            w = reduced(-sp.I*form*u)
            x = reduced(e*w.H*form-w*e.H*form)
            assert is_zero(x.H*form+form*x)
            assert is_zero(x*x*x)
            assert sp.cancel((e.H*form*e)[0]) == 0
            assert sp.cancel((e.H*form*w)[0]) == 0
            x2 = sp.cancel(sum(sp.conjugate(z)*z for z in x))
            assert sp.cancel(4*square_norm(e)*square_norm(u)-x2) >= 0
            for j in range(a+1):
                assert is_zero(x*vs[j])
            assert is_zero(x*vs[a+1]-sp.I*square_norm(u)*e)
            for j in range(a+1, r+1):
                assert is_zero(x*vs[j]-e*(w.H*form*vs[j])[0])
                assert is_zero(x*x*vs[j])
            # The root's coordinate relative to v_a modulo predecessors.
            assert is_zero(e-vs[a]+sum(
                (residuals[j]*((residuals[j].H*vs[a])[0]/square_norm(residuals[j]))
                 for j in range(a)), sp.zeros(n, 1)))
            adjacent += 1
        cases += 1
    return {"exact_complex_rational_unitary_flags": cases,
            "rank_two_adjacent_root_cases": adjacent,
            "checked": ["original Hermitian form", "positive Gram--Schmidt lengths",
                        "skew adjointness for the indefinite form", "nilpotence of order three",
                        "Hilbert--Schmidt coefficient bound", "adjacent character coordinate",
                        "vanishing of all earlier adjacent coordinates"]}


def polynomial_checks():
    x, y = sp.symbols("x y", nonnegative=True)
    n = x+1
    b = 16*n**3+y
    differences = [2*n*b-16*n**3-2*n**4,
                   n**2*b**2-n**3, b**2-73*n**2]
    certificates = []
    for expression in differences:
        poly = sp.Poly(sp.expand(expression), x, y)
        assert all(c >= 0 for c in poly.coeffs())
        certificates.append({"polynomial": str(poly.as_expr()),
                             "all_coefficients_nonnegative": True})
    l = sp.symbols("l", integer=True, positive=True)
    assert sp.expand((l+1)*l*(l-1)/2-l*(l*l-1)/2) == 0
    assert sp.cancel(4*(l*(l*l-1)/2)/(l+1)-2*l*(l-1)) == 0
    return {"substitution": "n=x+1, B0=16*n^3+y, x,y>=0",
            "energy_inequalities": certificates,
            "symbolic_holder_exponent_identities": 2}


def reserve_checks():
    cases = 0
    for r in range(81):
        n = 2*r+2  # smallest possible n; larger k only helps
        for l in range(r+2):
            if l == 0:
                h, exterior, total = 0, 0, 0
            elif l == 1:
                h, exterior, total = 1, 2, 0
            else:
                h, exterior = l+1, 2*l+1
                alpha = [(l+1)*(l-1-a) for a in range(l-1)]
                total = sum(alpha)
                assert total == l*(l*l-1)//2
                assert Q(l, l+1)+Q(1, l+1) == 1
                assert Q(4*total, l+1) == 2*l*(l-1)
                assert Q(l, l+1)*h == l
            assert total <= n**3
            assert h <= (r+1)**2
            assert exterior <= (r+1)*(r+2)
            assert 2*l*(l-1) <= 4*r*l
            assert 2*h <= 4*n*n
            cases += 1
    return {"boundary_and_reserve_cases": cases, "includes_r_zero": True,
            "includes_l_zero_and_one": True,
            "old_integer_shift_budget_replaced_only_conditionally": True}


def controls():
    # One point with unchanged mass: common scale is invisible to all ratios.
    l, c = 3, 5
    lengths = [Q(2), Q(3), Q(7)]
    scaled = [c*x for x in lengths]
    ratios = [lengths[a+1]/lengths[a] for a in range(l-1)]
    assert ratios == [scaled[a+1]/scaled[a] for a in range(l-1)]
    original = sp.prod(x*x for x in lengths)
    changed = sp.prod(x*x for x in scaled)
    assert changed == c**(2*l)*original
    # Fixed mass alone gives no uniform weighted estimate, even on one point.
    mass, weight, proposed_bound = 1, 101, 100
    assert mass == 1 and weight*mass > proposed_bound
    return {"controls_rejected": 2,
            "labels": ["ratio estimates used to control common length scale",
                       "mass bound substituted for a weighted norm bound"]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources, prior = source_records(args.offline)
    exact = {"flag_geometry": flag_checks(), "polynomials": polynomial_checks(),
             "reserves": reserve_checks(), "negative_controls": controls()}
    artifacts = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
                 f"paper/shared/{STEM}-references.tex",
                 "scripts/check_global_norm_frontier_mixed_ratio_moments.py"]
    certificate = {
        "date": "2026-11-22", "status": "PASS",
        "claim": "Conditional simultaneous flag-ratio moments with original Bessel mass, "
                 "and a smaller first-length shift reserve in the flag-product argument.",
        "new_result": "Mixed-ratio induction and optimized Holder assembly, "
                      "not the already proved Casimir energy identity.",
        "retained_data": ["original quotient measure", "original formal degree",
                          "original Bessel character and flag lengths", "original vector norm",
                          "homogeneous zero-map and zero-vector cases",
                          "original family and two-branch gap assumptions"],
        "analytic_inputs_not_closed_here": ["original Bessel mass/isometry",
                                             "original first-length moment recursion"],
        "sources": sources, "existing_mathematics_reused": prior,
        "exact_checks": exact,
        "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())}
                      for p in artifacts],
        "limitations": ["Finite exact checks supplement the general mathematical proof.",
                        "No full Lean build.",
                        "No proof of the original leading-minor Jacquet norm bound.",
                        "No weighted orbital bound or global Gram estimate.",
                        "No RH or GRH whole-node count change."],
        "reproduce": "python3 scripts/check_global_norm_frontier_mixed_ratio_moments.py --offline",
    }
    output = ROOT/"certificates"/f"{STEM}.json"
    output.write_text(json.dumps(certificate, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "checks": exact, "certificate": str(output.relative_to(ROOT))},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
