#!/usr/bin/env python3
"""Authenticate the actual cutoff and check its uniform absorption arithmetic.

The analytic and arithmetic argument is in the accompanying TeX.  This
script is not a Lean build and does not prove a positive trace estimate.
"""
from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
S = "Formalism.SharpRestriction."
A = "Development.AbelianVarietyTheory.Proofs.FlagMeasures."
SOURCES = [
    (S+"CuspSpanNormBounds.StandingNumericalData", [(14, 23), (39, 45), (106, 136)]),
    ("Formalism.LocalRingCardinality.Params", [(6, 48), (50, 62)]),
    (A+"CountParameterConditionsOfSizeHypotheses", [(9, 83)]),
    (A+"GapThresholdPaysFarTerms", [(25, 59)]),
    (A+"FarTermsModerateRegionOfFlagBound", [(53, 98)]),
    (S+"CuspSpanNormBounds.StandingHypothesesHoldFamily",
     [(334, 416), (795, 813), (1665, 1699)]),
    (S+"ParamsHeightRankConstant", [(104, 118), (126, 175)]),
]
PROOF = [
    "paper/shared/global-gram-continuation-far-absorption.tex",
    "paper/shared/global-gram-continuation-far-references.tex",
    "notes/global-gram-continuation-far-absorption.md",
    "scripts/global-gram-continuation-far-check.py",
]
DEPENDENCIES = [
    "paper/shared/global-gram-continuation-haar-budget.tex",
    "paper/shared/global-gram-continuation-quantitative-seed.tex",
    "paper/shared/global-gram-continuation-minimum.tex",
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def authenticate():
    data = json.load(gzip.open(ROOT / "blueprint/lean-source-imports.json.gz", "rt"))
    assert data["commit"] == REV
    atlas = {row[0]: row for row in data["modules"]}
    evidence = []
    for module, ranges in SOURCES:
        path = "lean/src/"+module.replace(".", "/")+".lean"
        raw = (ROOT / "build/source-cache/jsmorph/rh" / REV / path).read_bytes()
        git_blob = hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
        assert git_blob == atlas[module][1], module
        assert len(raw) == atlas[module][2], module
        lines = raw.splitlines(keepends=True)
        excerpts = []
        for first, last in ranges:
            assert 1 <= first <= last <= len(lines) and last-first < 120
            excerpts.append({"lines": [first, last],
                             "sha256": digest(b"".join(lines[first-1:last]))})
        evidence.append({"module": module, "repository": "jsmorph/rh", "commit": REV,
                         "path": path, "git_blob_sha1": git_blob,
                         "sha256": digest(raw), "excerpts": excerpts})
    return evidence


def exact_arithmetic():
    n, f, L, Cl = s.symbols("n f L Cl", positive=True)
    G, AT, AH, Cg, CT, U = s.symbols("G AT AH Cg CT U", nonnegative=True)
    ep = 1/(10**6*n**8*f**2)
    h = Cl*n**19*f**5*L
    assert s.cancel(h*ep**2/8) == Cl*n**3*f*L/(8*10**12)
    assert s.cancel(h*ep**2/16) == Cl*n**3*f*L/(16*10**12)
    assert s.cancel(h*ep) == Cl*n**11*f**3*L/10**6
    A = G+6+AT/2
    Z0 = s.expand(2*(9+4*A)+5*(1+AT+7*AH))
    assert Z0 == 71+8*G+9*AT+35*AH
    Z = s.expand(Z0.subs({G: 2*Cg, AT: CT, AH: U+13}))
    assert Z == 526+16*Cg+9*CT+35*U
    threshold = 8*10**12*(Z+1)
    assert s.simplify(Z-threshold/(8*10**12)) == -1
    # U=max(2,Cu), hence Z>=596 and Cl>=8e12*597.
    Cl_min = 8*10**12*597
    assert Cl_min >= 120
    assert s.Rational(Cl_min, 10**6) >= 64
    assert s.Rational(Cl_min, 16*10**12) >= 1
    assert 2 <= 10**12
    assert s.Rational(2, 10**6) < s.Rational(1, 2)
    # The proof uses log(2)>=1/2 and log(3)<2, not floating values.
    assert 10**6+3 <= 1801**2
    assert 100 <= 1801
    # The coefficient bounds leave nonnegative polynomial remainders
    # after n>=1, f>=1, L>=1. Check the two used coarse comparisons.
    x, y = s.symbols("x y", nonnegative=True)
    remainders = [
        4*n**3*f-(2*n+2*f),
        5*n**3*f-(5*n**2*f),
    ]
    for p in remainders:
        coeffs = s.Poly(s.expand(p.subs({n: 1+x, f: 1+y})), x, y).coeffs()
        assert all(c >= 0 for c in coeffs)
    return {
        "literal_cutoff": str(ep),
        "gap": str(h),
        "negative_exponent": str(s.cancel(h*ep**2/8)),
        "positive_cost_coefficient": str(Z),
        "fixed_gap_threshold": str(threshold),
        "remaining_exponent_coefficient": "-1",
        "all_rank_cutoff_envelope": "n>=1801, f>=1, L>1, 1<=q<=n, U>=2",
        "verification": "Exact rational and symbolic identities; all-variable inequalities are proved in TeX. No finite-sample inference.",
    }


def main():
    report = {
        "classification": "closed numerical far-return absorption supplier under retained cited FarBound and original standing data",
        "source_files": authenticate(),
        "exact_arithmetic": exact_arithmetic(),
        "proof_files": [{"path": p, "sha256": digest((ROOT/p).read_bytes())} for p in PROOF],
        "established_dependencies": [{"path": p, "sha256": digest((ROOT/p).read_bytes())}
                                     for p in DEPENDENCIES],
        "remaining": ["near-return weighted period estimate", "final arithmetic-map identification",
                      "positive trace comparison", "construction of all original standing data"],
        "scope": "Pinned source integrity and explicit arithmetic checked; no Lean build, no whole W08 completion.",
    }
    dest = ROOT / "certificates/global-gram-continuation-far-absorption.json"
    dest.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"certificate": str(dest.relative_to(ROOT)), "source_files": len(SOURCES),
                      "result": "exact cutoff and all cost coefficients passed",
                      "scope": report["scope"]}))


if __name__ == "__main__":
    main()
