#!/usr/bin/env python3
"""Authenticate the actual key-line and h0/hsh proof; check exact accounting.

The all-base key formula is cited to Moret--Bailly. The actual boundary
construction and general spanning argument are proved in the companion TeX.
Finite arithmetic diagnostics below do not prove those general arguments.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import product

import check_geometry_arithmetic_frontier_geometric_filtration as auth


STEM = "theta-spanning-continuation-key"
DP = "Development.AbelianVarietyTheory.Proofs.DivisorProofs."
HB = "Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights."
RANGES = {
    "Development.AbelianVarietyTheory.Definitions.KeyFormula.KeyRootOfKeyFormula": [(13,45)],
    DP+"ThetaKeySectionNormComplexPointsEqTwoPiPow": [(101,148)],
    DP+"ThetaKeySectionValuationBoundsDifferent": [(238,250),(275,293)],
    DP+"IntegralOfArcsAndGoodReductionPoints": [(75,135),(140,185),(186,225)],
    "Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsNormalAtOfUnif": [(83,137)],
    DP+"ExistsThetaWeightExponentsOfLargeGap": [(48,82)],
    DP+"ThetaWeightAndFlatExponentSizeBound": [(32,66)],
    HB+"ShortSpanCompositionClosed": [(24,105),(106,154)],
    DP+"LatticeBasisPeterssonFirst": [(41,81),(87,135)],
    DP+"LatticeBasisPeterssonSecond": [(54,89),(102,115)],
    DP+"SizeBoundsForFamily": [(43,112),(132,141)],
    DP+"SizeBoundsForFamilyStatement": [(25,26)],
    HB+"ShortVectorsSpanCuspLattice": [(28,80),(81,115)],
    HB+"ShortVectorWeightBound": [(23,78),(79,101)],
    HB+"ExistsDegreeParametersBound": [(33,76)],
}


def metric_check():
    # Exponents are ordered as 2, pi, det(Im Omega), |c|, |det M|.
    mb = (4,4,0,0,0)
    theta_factor = (-2,0,0,0,0)
    hodge_factor = (0,-2,0,0,0)
    assert tuple(sum(xs) for xs in zip(mb,theta_factor,hodge_factor)) == (2,2,0,0,0)
    # Set g=1 for the g-linear exponents; |c| and |det M| exponents
    # already refer to the whole scalar and determinant.
    nth = (Fraction(-1,2),0,Fraction(-1,2),2,0)
    neta = (2,1,1,0,-2)
    product_exponents = tuple(4*a+2*b for a,b in zip(nth,neta))
    assert product_exponents == (2,2,0,8,-4)
    return {"metric_conversion":"2^(-2g) pi^(-2g) (2pi)^(4g) = (2pi)^(2g)",
            "original_gaussian_identity":"nth^4 neta^2 = (2pi)^(2g) |c|^8 / |det M|^4"}


def weight_checks():
    cases = 0
    for f,p,q,base,step,extra in product((3,4,8),(1,2,3),(1,2,3),(-1000,-17,0,23,1000),(0,1,7),(0,1,50)):
        r=p+q
        m=f*r+1
        n=8*m
        gap=8*f*r+10+extra
        weights=[]
        n0s=[]
        ds=[]
        for tau in range(f):
            b=base+13*tau
            la=[b+gap+(p-1-i)*step for i in range(p)]+[b-j*step for j in range(q)]
            assert all(la[i]>=la[i+1] for i in range(r-1))
            n0=1+4*m-la[p-1]
            lp=[x+n0 for x in la]
            pos=[x-4*m for x in lp[:p]]
            neg=[-x-4*m for x in reversed(lp[p:])]
            assert min(pos+neg)>=1
            assert all(a>=b for a,b in zip(pos,pos[1:]))
            assert all(a>=b for a,b in zip(neg,neg[1:]))
            recovered=[x+4*m for x in pos]+[-x-4*m for x in reversed(neg)]
            assert recovered==lp
            weights.extend(la)
            n0s.append(n0)
            ds.append(sum(pos)+sum(neg))
        S=sum(abs(x) for x in weights)
        kappa0=sum(ds)+f*r*(n//2)
        assert n%2==0 and n>=8*f*r+4
        assert kappa0<=(1+r)*S+f*r*(4*m+1)
        assert sum(abs(x) for x in n0s)<=S+f*(4*m+1)
        # Lb>=1: testing its weakest value also verifies these integer
        # coefficient inequalities; the general monotonicity is in TeX.
        X=f*r
        assert kappa0<=2*X*S+9*X*X
        assert sum(abs(x) for x in n0s)<=S+9*X*X
        assert n//2-4*m==0
        cases+=1
    return cases


def budget_checks():
    C=400000
    coefficient_S=60000+Fraction(3,2)
    coefficient_X5=270000+8+Fraction(27,2)+Fraction(391,2)+40+1
    assert coefficient_X5==270258
    assert coefficient_S<C and coefficient_X5<C
    cases=0
    for f,r in product(range(8,17),range(100,111)):
        D=f*r*(r-1)//2
        assert D+1>=8*f*r+10
        for Lb,kappa,T in product((6*C,6*C+1,10*C),(1,7,100),(1,5,1000)):
            X=f*r*Lb
            PP=X**12
            Y=Fraction(kappa,T)+1
            S0=3*D*X*X*Y
            assert C*(X**3*S0+X**5)<=D*PP*Y
            Si=X*X*kappa
            assert C*(X**3*Si+X**5)<=PP*kappa
            cases+=1
    return {"norm_coefficients":{"X3S":str(coefficient_S),"X5":str(coefficient_X5),"C":C},
            "h0_hsh_exact_rational_cases":cases,"sufficient_original_host_threshold":6*C}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline",action="store_true")
    args=parser.parse_args()
    auth.RANGES=RANGES
    sources=auth.provenance(args.offline)
    root=auth.ROOT
    pdf=root/"build/theta-spanning-continuation-key-references/moret-bailly-theta.pdf"
    digest="b5d7ff907fc30da527e83cf62c3ab2cd5774a9d1de10e6eac83e2270eae2cdab"
    assert auth.sha(pdf.read_bytes())==digest
    txt=pdf.with_suffix(".txt").read_bytes().splitlines(keepends=True)
    ranges=[(30,98),(98,147),(201,252),(689,704),(706,774)]
    primary={"url":"https://www.numdam.org/item/CM_1990__75_2_203_0.pdf","pdf_sha256":digest,
             "text_sha256":auth.sha(pdf.with_suffix(".txt").read_bytes()),
             "excerpts":[{"lines":[a,b],"sha256":auth.sha(b"".join(txt[a-1:b]))} for a,b in ranges],
             "scope":"Theorem 0.2 over Z, metric Theorem 3.3 for both parities; Section 2.5 Tate discriminant leading term."}
    paths=[f"paper/shared/{STEM}.tex",f"paper/shared/{STEM}-references.tex",f"notes/{STEM}.md",f"scripts/{STEM}.py"]
    deps=["geometry-arithmetic-frontier-integral-theta", "geometry-arithmetic-frontier-formal-arcs",
          "geometry-arithmetic-frontier-dvr-uniformization", "theta-spanning-continuation-short",
          "theta-spanning-continuation-flat", "theta-spanning-continuation-twist"]
    dependency_hashes={}
    for dep in deps:
        path=root/"paper/shared"/(dep+".tex")
        if not path.exists():
            # The DVR theorem has a longer filename in earlier checkpoints.
            matches=list((root/"paper/shared").glob("*dvr*unif*.tex"))
            if dep=="geometry-arithmetic-frontier-dvr-uniformization" and len(matches)==1:
                path=matches[0]
            else:
                raise FileNotFoundError(path)
        dependency_hashes[str(path.relative_to(root))]=auth.sha(path.read_bytes())
    diagnostics={"metric":metric_check(),"exact_weight_cases":weight_checks(),**budget_checks()}
    record={"status":"PASS", "classification":"closed original key shift and actual h0/hsh suppliers; independently reviewed",
            "sources":sources,"primary_reference":primary,
            "artifacts":{p:auth.sha((root/p).read_bytes()) for p in paths},
            "established_dependency_hashes":dependency_hashes,"diagnostics":diagnostics,
            "scope_guards":["same original primitive line and rigidification","all dyadic factors retained",
                            "ramified eigenframe factor det(U)^4 retained","field spanning, not an integral module basis",
                            "generic t-order checked through a finite-data complex realization","odd elliptic boundary obstruction retained"],
            "remaining":["original Bergman/height comparisons and section remainder","selected-prime and retained-chain same-map compatibility"],
            "verification_scope":"Authenticated source and reference bytes, exact metric exponents and finite integer/rational accounting diagnostics; general theorem proved in TeX; no Lean build."}
    out=root/"certificates"/(STEM+".json")
    out.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":"PASS","source_files":len(sources),"weight_cases":diagnostics["exact_weight_cases"],
                      "h0_hsh_cases":diagnostics["h0_hsh_exact_rational_cases"],"certificate":str(out.relative_to(root))}))


if __name__=="__main__":
    main()
