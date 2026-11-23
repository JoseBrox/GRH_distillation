#!/usr/bin/env python3
"""Authenticate bounded thin-region interfaces and exact supplementary checks.

This checks identities and numerical accounting, not all period tori.
The general proof is the accompanying TeX, reviewed separately.
No Lean build is performed.
"""
from __future__ import annotations
import argparse
import importlib.util
import itertools
import json
from fractions import Fraction
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "auth", ROOT / "scripts/check_geometry_arithmetic_frontier_geometric_filtration.py")
auth = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(auth)
SQ = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.SquareIntegrability."
PU = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.PullbackSections."
CP = "Development.AbelianVarietyTheory.Proofs.CuspFormEvaluations."
TS = "Development.AbelianVarietyTheory.Proofs.TorusSplitting."
DP = "Development.AbelianVarietyTheory.Proofs.DivisorProofs."
HB = "Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights."
TH = "Development.AutomorphicArithmetic.LocalEmbeddings."
RANGES = {
    "Formalism.LocalRingCardinality.Params": [(6,32)],
    SQ+"GCauchyStatement": [(29,95),(98,185),(197,229)],
    SQ+"SplitSt": [(34,102)],
    PU+"NonemptyUnitAt": [(47,90)],
    TS+"ThetaFunctionTorusL2Norm": [(61,100),(124,152)],
    CP+"SumLeFinsumOfSurjectsOntoFinset": [(232,337)],
    CP+"IsTorusAtOfIsTorusOf": [(205,233)],
    CP+"ExistsBlockProductMemIntegralHarmonic": [(226,242),(292,338)],
    "Development.AbelianVarietyTheory.Definitions.ThetaValues.IsBlockProd": [(15,43)],
    SQ+"TiledBoundaries.NstatementOf": [(22,68),(70,119),(161,210)],
    CP+"CardLatticeQuotientHalfLevel": [(15,39),(43,79)],
    TH+"ThinCore": [(26,34),(134,199),(201,247),(251,344)],
    TH+"ThinCover": [(117,141),(194,231)],
    DP+"CuspFormExistsBelowFrameBound": [(117,161),(165,190)],
    DP+"EtaBoundLengthUnit": [(139,177)],
    HB+"BergmanKernelThinPartEstimate": [(16,49)],
    HB+"ExistsConstantTwistOfThinDivisor": [(12,49)],
}


def diagnostics():
    z,v,h,l,t,a,ab,zb = sp.symbols("z v h l t a ab zb")
    jet_cases = laguerre_cases = 0
    for c in range(13):
        exp_part = sum((l*z)**j/sp.factorial(j) for j in range(c+1))
        got = sp.expand((v*z-h)**c/sp.factorial(c)*exp_part).coeff(z,c)*sp.factorial(c)
        expected = sum(sp.binomial(c,j)/sp.factorial(j)*(-h)**j
                       *v**(c-j)*l**j for j in range(c+1))
        assert sp.expand(got-expected) == 0
        jet_cases += 1
        # Normalized Bargmann moments: integral z^k zbar^j = delta(k,j) k!/t^k.
        integrand = sp.expand(zb**c*(z-a)**c*
                             sum((t*z*ab)**j/sp.factorial(j) for j in range(c+1)))
        moment = 0
        for (k,j),coef in sp.Poly(integrand,z,zb).terms():
            if k==j:
                moment += coef*sp.factorial(k)/t**k
        got = sp.expand(moment/(sp.factorial(c)/t**c))
        expected = sum(sp.binomial(c,j)*(-t*a*ab)**j/sp.factorial(j)
                       for j in range(c+1))
        assert sp.expand(got-expected) == 0
        laguerre_cases += 1
    y,u,b,q,p = sp.symbols("y u b q p")
    lhs = -p*q*(y*y+(y-b)**2)-2*p*u*(2*y-b)
    rhs = -2*p*q*(y-b/2+u/q)**2+2*p*u*u/q-p*q*b*b/2
    assert sp.expand(lhs-rhs) == 0
    x,aa = sp.symbols("x aa")
    assert sp.expand(-p*q*(x*x+(x-aa)**2)/2
                     +p*q*(x-aa/2)**2+p*q*aa*aa/4) == 0
    # Finite exact anisotropic models of the general Voronoi rounding proof.
    voronoi_cases = 0
    for scales in ((1,1),(1,37),(7,101)):
        for nums in itertools.product(range(-4,5),repeat=2):
            point = [Fraction(s*n,8) for s,n in zip(scales,nums)]
            for s,x in zip(scales,point):
                w=2*x/s+Fraction(1,2)
                k=w.numerator//w.denominator
                ell=s*k
                rr=2*x-ell
                assert abs(rr)<=Fraction(s,2)
                assert abs(ell)<=Fraction(3*s,2)
                assert x==Fraction(ell,2)+rr/2
            voronoi_cases += 1
    # Positive margins after pi>3, log4<7/5, log120<5.
    D0,g0,d,Lq,Ld=sp.symbols("D0 g0 d Lq Ld", nonnegative=True)
    D=D0+1
    g=g0+1
    b_margin=sp.expand(sp.Rational(3,2)*(4*D*(7+Lq+Ld)+d+1)
                       -(sp.Rational(7,5)+D*(5+Lq+sp.Rational(3,2)*Ld)
                         +sp.Rational(7,5)*d)-30*D)
    a_margin=sp.expand(sp.Rational(3,4)*90*(g+D)
                       -(sp.Rational(7,5)+sp.Rational(14,5)*g)-30*D)
    assert all(c>=0 for c in sp.Poly(b_margin,D0,d,Lq,Ld).coeffs())
    assert all(c>=0 for c in sp.Poly(a_margin,D0,g0).coeffs())
    for arg,bound in ((Fraction(7,5),4),(Fraction(5),120)):
        assert sum(arg**j/Fraction(int(sp.factorial(j))) for j in range(30)) > bound
    # A rational Taylor remainder proves e<11/4<3<pi.
    assert sum(Fraction(1,int(sp.factorial(j))) for j in range(9)) + \
        Fraction(1,int(sp.factorial(9)))*Fraction(10,9) < Fraction(11,4)
    f,m,R=sp.symbols("f m R",positive=True)
    ds=2*f*m
    radius_ratio=sp.cancel((sp.Rational(9,4)*ds**6)/
                           (8100*m**4*ds**4*R**7*2*f/R**2))
    assert radius_ratio==f/(1800*m*m*R**5)
    assert Fraction(8100*22*16,7*1000**6)<=Fraction(1,2500)
    assert 1000**8>=2500*100000
    M,xi=sp.symbols("M xi",positive=True)
    for degree in range(1,10):
        assert sp.cancel(M**(-2*degree)*M**degree*(2*xi)**degree
                         -(2*xi/M)**degree)==0
    return {
        "ordinary_jet_factorial_identities":jet_cases,
        "normalized_Bargmann_Laguerre_identities":laguerre_cases,
        "exact_Voronoi_rounding_models":voronoi_cases,
        "absolute_overlap_square_completion":True,
        "all_dimension_frequency_margin":str(b_margin),
        "all_dimension_abelian_margin":str(a_margin),
        "frequency_radius_ratio":str(radius_ratio),
        "exact_terminal_budget_and_theta_scalar_checks":True,
        "scope":"Exact identities and sufficient numeric margins; finite lattice models do not replace the general Voronoi or periodization proof.",
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--offline",action="store_true")
    args=ap.parse_args()
    auth.RANGES=RANGES
    sources=auth.provenance(args.offline)
    checks=diagnostics()
    files=[
        "paper/shared/geometry-bergman-continuation-thin.tex",
        "paper/shared/geometry-bergman-continuation-thin-references.tex",
        "notes/geometry-bergman-continuation-thin.md",
        "scripts/geometry-bergman-continuation-thin.py",
    ]
    result={
        "status":"PASS",
        "classification":"actual thin-region determinant-jet and Bergman supplier",
        "sources":sources,"diagnostics":checks,
        "artifacts":{p:auth.sha((ROOT/p).read_bytes()) for p in files},
        "verification_scope":"Pinned source-byte authentication, exact identities and sufficient all-parameter accounting. General mathematical proof is in TeX; no Lean build.",
        "independent_review":"Root reviews determinant, anisotropy and downstream source interfaces; global_norm_frontier reviews frequency separation, periodization, absolute unfolding, L2 and Gaussian tails.",
        "retained_hypotheses":[
            "original principally polarized CM period lattice and isotropic semicharacter",
            "all displayed numeric family hypotheses with growing fields and dimensions",
            "original disjoint-column harmonic block polynomial",
            "original normalized theta evaluation and exact finite half-level group",
            "same-component flat/key twisting comparison",
        ],
        "remaining":["actual point-height suppliers","final arithmetic section remainder",
                     "construction of original numerical family where still separate"],
        "whole_node_counts_changed":False,
    }
    path=ROOT/"certificates/geometry-bergman-continuation-thin.json"
    path.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"PASS","sources":len(sources),"diagnostics":checks}))


if __name__=="__main__":
    main()
