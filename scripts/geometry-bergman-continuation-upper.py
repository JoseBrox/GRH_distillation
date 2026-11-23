#!/usr/bin/env python3
"""Authenticate upper cusp norms and supplement the written proof with exact checks.

No Lean build or automated proof of the general arithmetic/analytic theorem
is performed.  The actual mathematical proofs are the two shared TeX files.
"""
from __future__ import annotations

import argparse
import hashlib
import json

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

import check_geometry_arithmetic_frontier_geometric_filtration as auth

STEM = "geometry-bergman-continuation-upper"
DP = "Development.AbelianVarietyTheory.Proofs.DivisorProofs."
CP = "Development.AbelianVarietyTheory.Proofs.CuspFormEvaluations."
FD = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.FundamentalDomains."
HB = "Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights."
RANGES = {
    "Development.AbelianVarietyTheory.Definitions.Divisors.UnifOfSpaceEq": [(103,116)],
    FD+"MaxBoundPf": [(12,115),(116,230),(231,257)],
    CP+"ExistsThickPointHyperbolic": [(269,335),(335,423)],
    DP+"CardGroupElementsChartReturnLe": [(128,213)],
    DP+"NormFactorAndDensityNearOneInFlagChart": [(97,185)],
    DP+"CuspFormSupNormLePeterssonIntegralComponent": [(67,110),(107,194)],
    "Development.AbelianVarietyTheory.PublishedTheorems.Divisors₂.TamagawaSpecialUnitary": [(11,26)],
    DP+"RiemannianLieVolumeFormula": [(13,28)],
    DP+"RealUnitaryCovolumeSum": [(89,145)],
    DP+"CovolumeRealSpecialUnitaryEqFlagDomainMass": [(129,160)],
    DP+"NormOneTorusClassNumberBoundProof": [(14,44)],
    DP+"FiniteAdeleQuadraticExistsUnitEqMulSg": [(181,264)],
    DP+"MassBoundOfTamagawaUnitary": [(15,87)],
    DP+"FramedDictionaryBound": [(20,57)],
    DP+"WeightedFrameSumPositive": [(86,164)],
    DP+"LevelGeometryWeightBound": [(38,107)],
    DP+"SupConstantLogBound": [(37,83)],
    HB+"ShortGeneratorNormComparison": [(25,101)],
    DP+"ExistsLatFrameOfIsShortGen": [(19,60)],
    DP+"ExistsCuspFrameWeights": [(76,112),(187,231)],
}


def diagnostics():
    torus_cases = 0
    for r in range(2,19):
        assert (sp.eye(r-1)+sp.ones(r-1)).det() == r
        torus_cases += 1

    chart_cases = 0
    for r in range(2,7):
        for p in range(r+1):
            J=sp.diag(*([1]*p+[-1]*(r-p)))
            for pattern in (1,-1):
                rho=sp.Rational(1,200*r**3*2)
                g=sp.eye(r)
                for i in range(r):
                    for j in range(i):
                        g[i,j]=rho*(1 if pattern==1 else (-1)**(i+j))
                U=g[:,:p]
                P=sp.zeros(r) if p==0 else U*(U.T*J*U).inv()*U.T*J
                Q=2*J*P-J
                assert Q==Q.T
                for k in range(1,r+1):
                    assert (Q-sp.eye(r)/2)[:k,:k].det()>0
                    assert (2*sp.eye(r)-Q)[:k,:k].det()>0
                chart_cases += 1

    generator_cases = 0
    for d in range(1,6):
        for index in (2,7,101,1009):
            A=sp.eye(d)*index
            for i in range(1,d): A[i,i-1]=i+1
            B=A.inv()
            N=B.applyfunc(lambda x:sp.floor(x+sp.Rational(1,2)))
            C=B-N
            assert all(abs(v)<=sp.Rational(1,2) for v in C)
            assert A*C==sp.eye(d)-A*N
            integral_generators=A.row_join(A*C)
            assert all(v.q==1 for v in integral_generators)
            snf=smith_normal_form(integral_generators,domain=sp.ZZ)
            assert all(abs(snf[i,i])==1 for i in range(d))
            generator_cases += 1

    z=sp.symbols('z',nonnegative=True)
    # Symbolic budget checks after the general logarithmic inequalities
    # in the proof.  These do not replace those analytic inequalities.
    mass_margin=sp.expand(76*(2+z)**2-261)
    assert all(c>=0 for c in sp.Poly(mass_margin,z).all_coeffs())
    assert 80+86+14+8==188 and 188<=250
    assert 8**7>=806000 and 8**9>=5000
    f,r=sp.symbols('f r',positive=True)
    assert sp.simplify(f*(r*r-1)/2/(2*f)-(r*r-1)/4)==0
    for p,a in ((2,2),(2,3),(3,1),(5,1)):
        for b in (1,3,7):
            if b%p==0: continue
            n=(1+p**a*b)**p-1
            val=0
            while n%p==0: val+=1;n//=p
            assert val==a+1
    return {"compact_torus_and_trace_zero_Gram_cases":torus_cases,
            "exact_indefinite_chart_models":chart_cases,
            "exact_integral_generator_models":generator_cases,
            "all_rank_mass_margin_polynomial":str(mass_margin),
            "budget_and_discriminant_identities":True,
            "scope":"Finite exact models and symbolic accounting only; no numerical verification of all arithmetic fields or the general theorem."}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--offline',action='store_true')
    args=ap.parse_args()
    auth.RANGES=RANGES
    sources=auth.provenance(args.offline)
    primary_path=auth.ROOT/'build/geometry-upper-references/prasad-1989.pdf'
    primary_text=primary_path.with_suffix('.txt').read_text().splitlines()
    primary={"url":"https://www.numdam.org/item/PMIHES_1989__69__91_0.pdf",
             "sha256":hashlib.sha256(primary_path.read_bytes()).hexdigest(),
             "used":"Section 3.3: Tamagawa number one for outer type A; section 3.7: invariant local-factor formula. The written proof retains its own original-measure conversion.",
             "bounded_text_excerpts":[{"lines":[a,b],"sha256":auth.sha(('\n'.join(primary_text[a-1:b])+'\n').encode())}
                                      for a,b in ((908,935),(979,1033),(1058,1081))]}
    paths=['paper/shared/geometry-bergman-continuation-upper.tex',
           'paper/shared/geometry-cusp-frame-continuation.tex',
           'paper/shared/geometry-bergman-continuation-upper-references.tex',
           'notes/geometry-bergman-continuation-upper.md',
           'scripts/geometry-bergman-continuation-upper.py']
    result={"status":"PASS",
            "classification":"closed original upper Bergman, multiplication and full integral cusp-frame suppliers",
            "sources":sources,"primary_reference":primary,"diagnostics":diagnostics(),
            "artifacts":{p:auth.sha((auth.ROOT/p).read_bytes()) for p in paths},
            "verification_scope":"Source-byte authentication and exact supplementary diagnostics. General proofs are in TeX; no Lean build or global proof completion is claimed.",
            "independent_review":"Root reviewed upper analytic, lattice and numerical argument; global_norm_frontier reviewed arithmetic volume and required the now-explicit principal-level torsionfree correction.",
            "guards":["E/E+ unramified at all finite primes","original self-dual Hermitian lattice, including nonfree modules","different and trace factor two","correct unsquared half-maximum then squared norm","stabilizer weights at level one; ordinary flag volume only at torsionfree principal level","original component probability normalization","entire integral Z-generation proved independently of its index"],
            "remaining":["thin lower Bergman estimate","actual point heights","final arithmetic section remainder","construction of original numerical records where still separate"],
            "whole_node_counts_changed":False}
    out=auth.ROOT/'certificates'/(STEM+'.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({"status":"PASS","sources":len(sources),"diagnostics":result['diagnostics']}))


if __name__=='__main__': main()
