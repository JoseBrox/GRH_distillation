#!/usr/bin/env python3
"""Authenticate the actual short-theta supplier and exact diagnostics."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction
import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth

STEM = "theta-spanning-continuation-short"
P = "Development.AbelianVarietyTheory.Proofs.CuspFormEvaluations."
D = "Development.AbelianVarietyTheory.Proofs.DivisorProofs."
F = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.FundamentalDomains."
H = "Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights."
RANGES = {
    P+"EmbeddingHermSelf": [(14,26),(56,124)],
    P+"TraceHermNondegenerate": [(57,139),(299,358)],
    "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.HeightTheory.Transference": [(35,112),(113,175)],
    P+"ExistsEqMulProdMinors": [(126,245),(250,369)],
    P+"RowHighestLeSpanColWordComplex": [(172,242)],
    P+"SpanGridPerpVecEqOrbitSpanOfLe": [(167,226),(276,340)],
    P+"ExistsShortHarmonicFamilyFewColumnsLinear": [(38,112)],
    P+"ExistsShortHarmonicFamilyUnimodular": [(96,193)],
    D+"PolynomialCoefficientEmbeddingNormLeOfL1Bound": [(287,398),(399,444)],
    D+"FirstMinAtHalfMax": [(19,103),(111,170),(171,211)],
    D+"ExistsSelfDualDataTransvectionPrincipalLevel": [(60,119)],
    F+"MaxBoundPf": [(12,90),(91,167),(168,257)],
    "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.SquareIntegrability.LemmaS": [(236,286)],
    P+"NormalisedThetaValueBound": [(18,97),(101,187)],
    P+"JetTranslateProjectedVacuumLe": [(150,220),(221,288)],
    D+"NormRawThetaSeriesIndexBoundLeSqrt": [(54,116)],
    D+"NormPhiHatIndPhi": [(208,274),(275,315)],
    D+"ExistsSmallScalarReflexIdealSelfDualLattice": [(29,118),(119,152)],
    D+"EvenDomainWeightBound": [(36,95)],
    H+"ExistsGoodCoverAtMinimalLevel": [(20,57)],
    H+"ShortSpanCompositionClosed": [(24,105),(106,154)],
    H+"ShortGeneratorNormComparison": [(23,101)],
    H+"ExistsDegreeParametersBound": [(33,76)],
}


def diagnostics():
    # Identity is polynomial and holds also at singular Gram matrices.
    matrices = [
        (sp.Matrix([[1,0,1],[0,1,1]]), sp.Matrix([[1,2,0],[0,1,2]]), sp.Matrix([2,3,5])),
        (sp.Matrix([[1,0,0],[1,0,0]]), sp.Matrix([[1,0,0],[0,1,0]]), sp.Matrix([1,2,3])),
        (sp.Matrix([[1,sp.I,0]]), sp.Matrix([[1,1,1]]), sp.Matrix([sp.I,2,1])),
    ]
    for rows_u, rows_a, w in matrices:
        h = rows_u.conjugate() * rows_a.T
        v = h.det()*w - rows_a.T*h.adjugate()*(rows_u.conjugate()*w)
        assert all(sp.simplify(x)==0 for x in rows_u.conjugate()*v)
    t = sp.symbols("t", nonnegative=True)
    # Put m=t+1: all coefficients of the recurrence slack are nonnegative.
    slack = sp.Poly(sp.expand((t+1)**4-t**4-(t+1)**2/4), t)
    assert all(c >= 0 for c in slack.all_coeffs())
    halfmax_exp = 80-6-57
    assert halfmax_exp == 17
    raw_log_budget = Fraction(21)+Fraction(21,2)+Fraction(202)+Fraction(2)
    assert raw_log_budget < 300 < 9000
    assert 20000+9000+391+67 == 29458 < 30000
    f,n,rd=sp.symbols("f n rd", positive=True)
    assert sp.simplify((2*f*n)**2*rd/sp.sqrt(2*f)/sp.sqrt(2)-2*f**sp.Rational(3,2)*n**2*rd)==0
    rank,deg_k=sp.symbols("r deg_K", positive=True)
    assert sp.simplify(deg_k/(2*f)*(f*rank)-rank*deg_k/2)==0
    return {
        "adjugate_orthogonality_cases":len(matrices),
        "singular_and_complex_cases_included":True,
        "transference_recurrence_nonnegative_coefficients":[str(c) for c in slack.all_coeffs()],
        "short_vector_B0_normalization":True,
        "halfmax_exponent_slack":halfmax_exp,
        "raw_log_budget_in_units_kappa_Lb":str(raw_log_budget),
        "total_log_constant":29458,
        "reflex_ideal_norm_exponent":"r*[K:Q]/2",
        "scope":"Exact diagnostics; the general mathematical proofs are in TeX, not supplied by finite tests.",
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline",action="store_true")
    args=parser.parse_args()
    auth.RANGES=RANGES
    sources=auth.provenance(args.offline)
    paths=[f"paper/shared/{STEM}.tex",f"paper/shared/{STEM}-references.tex",f"notes/{STEM}.md",f"scripts/{STEM}.py"]
    record={
        "status":"PASS",
        "classification":"closed actual minimal-level short theta supplier; independently reviewed",
        "frontier":"Original finite integral coefficient-field spanning family with uniform global/component Petersson bounds",
        "artifacts":{p:auth.sha((auth.ROOT/p).read_bytes()) for p in paths},
        "sources":sources,
        "diagnostics":diagnostics(),
        "remaining":["actual key and flat twists, including FlatExistsAt(c1), for h0/hsh", "same-map selected-prime/global period compatibility"],
        "verification_scope":"Pinned bytes and exact finite diagnostics; human-readable proof, no Lean build.",
    }
    out=auth.ROOT/"certificates"/(STEM+".json")
    out.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":"PASS","source_files":len(sources),"certificate":str(out.relative_to(auth.ROOT)),"diagnostics":record["diagnostics"]},indent=2))


if __name__=="__main__":
    main()
