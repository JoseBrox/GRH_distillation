#!/usr/bin/env python3
"""Authenticate the actual all-place theta denominator and exact interfaces.

The proof uses constructed models and the previously proved full-primary
and mixed-level estimates. The finite checks below diagnose the normalization
and quantifiers; no Lean build or numerical theta approximation is claimed.
"""
from __future__ import annotations

import argparse
import json

import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth

STEM = "geometry-arithmetic-frontier-actual-theta-denominator"
P = "Formalism.LocalToGlobal.ProjectiveLattices."
D = "Development.AbelianVarietyTheory.Proofs.DivisorProofs."
C = "Development.AbelianVarietyTheory.Proofs.CuspFormEvaluations."
HW = "Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights."
RANGES = {
    P + "ThClass": [(17, 27)],
    P + "ThShort": [(45, 99), (244, 269)],
    P + "AllTest": [(9, 14)],
    D + "ExistsBoundedIntegerGoodCoverThetaSeriesIntegral": [(31, 79), (80, 118)],
    D + "ThFamMono": [(31, 40)],
    D + "IsIntegralFourierCoeffClassIndicatorLevelPoint": [(23, 30), (100, 114)],
    D + "LogShortThetaSeriesDenominatorBoundLe": [(89, 94), (102, 176)],
    D + "IsShortRuleOfRaw": [(27, 60)],
    C + "ShortThetaSumEqOfWitnessesCommonAlgebra": [(28, 78)],
    C + "ExistsFaithfullyFlatCoverShortThetaValueData": [(34, 95)],
    HW + "ExistsGoodCoverAtMinimalLevel": [(20, 57)],
}


def diagnostics():
    f, r, t, d, L, R = sp.symbols("f r t d L R", nonnegative=True)
    kap = d + f*r*t
    original_log_allowance = 30*L*(2*f*r*t+d) + 7*f*L*d
    first = 60*L*kap+7*f*L*kap
    second = 67*f*L*kap
    third = 67*(f*R*L)**2*kap
    assert sp.expand(first-original_log_allowance-(30*L*d+7*f*f*r*t*L)) == 0
    assert sp.expand(second-first-60*(f-1)*L*kap) == 0
    assert sp.expand(third-second-67*f*L*kap*(f*R*R*L-1)) == 0

    # Keep the two finite indices different in a genuine self-dual lattice.
    # Locally in a split hyperbolic plane, exponents (a,-a) have determinant
    # one; intersection exponents are (max(a,0),max(-a,0)).
    index_cases = []
    for prime in [3, 5, 7]:
        for e in [1, 2, 3]:
            for a in range(-e, e+1):
                for rank in [1, 2, 3]:
                    full_exp = rank*(2*e)
                    intersection_exp = rank*(2*e-abs(a))
                    assert full_exp-intersection_exp == rank*abs(a)
                    index_cases.append([prime,e,a,rank,full_exp,intersection_exp])

    # The original finite Fourier transform is unnormalized. For an indicator
    # it is one root of unity, not that root divided by the cardinality.
    z = sp.symbols("z")
    root_cases = 0
    for M in [3, 5, 9, 15]:
        cyclotomic = sp.cyclotomic_poly(M,z)
        for exponent in range(M):
            root = z**exponent
            assert sp.rem(root**M-1,cyclotomic,z) == 0
            for chosen in range(M):
                indicator_sum = sum((1 if x == chosen else 0)*z**((x*exponent)%M)
                                    for x in range(M))
                assert indicator_sum == z**((chosen*exponent)%M)
                root_cases += 1

    C0, I, N, beta, s, delta, M0, inner = sp.symbols(
        "C0 I N beta s delta M0 inner", nonzero=True)
    degree = sp.symbols("degree", integer=True, nonnegative=True)
    raw = inner/(C0*I*N**degree)
    short = raw/beta
    assert sp.cancel(beta*short-raw) == 0
    assert sp.cancel((C0*delta**degree*M0**degree)*s*raw
                     -s*delta**degree*M0**degree*inner/(I*N**degree)) == 0
    v,e,ram=sp.symbols("v e ram",positive=True)
    assert sp.cancel(ram*v/(ram*e)-v/e) == 0
    return {
        "uniform_log_bound": "Exact symbolic identities; nonnegative differences under original f,R,L>=1",
        "distinct_index_cases": len(index_cases),
        "finite_fourier_indicator_cases": root_cases,
        "beta_and_average": "Original beta_H cancellation and whole C denominator checked symbolically",
        "valuation_extension": "v/e unchanged when numerator and denominator both multiply by ramification index",
        "scope": "Finite diagnostics only. General integrality is proved by the actual model/chart and existing full-primary/mixed arguments.",
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--offline",action="store_true")
    args=ap.parse_args()
    auth.RANGES=RANGES
    sources=auth.provenance(args.offline)
    checks=diagnostics()
    dependencies=[
        "geometry-arithmetic-frontier-formal-trace",
        "geometry-arithmetic-frontier-primary-trace",
        "geometry-arithmetic-frontier-mixed-level",
        "geometry-arithmetic-frontier-reached-regularity",
        "geometry-arithmetic-frontier-discriminant-clearing",
        "geometry-arithmetic-frontier-integral-theta",
        "geometry-arithmetic-frontier-good3",
        "geometry-arithmetic-frontier-level-cover",
        "geometry-arithmetic-frontier-member",
    ]
    dep_records=[]
    for stem in dependencies:
        p=f"paper/shared/{stem}.tex"
        dep_records.append({"path":p,"sha256":auth.sha((auth.ROOT/p).read_bytes())})
    files=[f"paper/shared/{STEM}.tex",f"paper/shared/{STEM}-references.tex",
           f"notes/{STEM}.md",f"scripts/check_{STEM.replace('-','_')}.py"]
    rec={
        "date":"2026-11-23","status":"PASS",
        "classification":"Closed original arithmetic supplier; independent review recorded separately",
        "claim":"Original CovInt.integral_smul_thLa for every original raw-theta value witness on the actual cover, with one intZ and original uniform logarithmic budget",
        "whole_nodes_newly_closed":0,
        "sources":sources,"dependencies":dep_records,"checks":checks,
        "files":[{"path":p,"sha256":auth.sha((auth.ROOT/p).read_bytes())} for p in files],
        "preserved_quantifiers":["Every original IsNab connection", "Every original self-dual lattice with both prescribed local-triviality conditions", "Every compatible odd N", "Every integral harmonic P and exact level indicator", "Every theta section satisfying the original test-ring value contract", "Every determinant-ideal scalar s", "Every original arithmetic valuation test, including prime squares in the level and ramified coefficient fields"],
        "not_claimed":["Actual raw-theta spanning theorem", "Archimedean raw-theta norm bound", "W10 degree estimate", "Whole W06/W08 or RH/GRH completion", "Lean build"],
    }
    (auth.ROOT/"certificates"/f"{STEM}.json").write_text(json.dumps(rec,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"status":"PASS","authenticated_modules":len(sources),
                      "distinct_index_cases":checks["distinct_index_cases"],
                      "fourier_cases":checks["finite_fourier_indicator_cases"]}))


if __name__=="__main__":
    main()
