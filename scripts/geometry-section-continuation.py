#!/usr/bin/env python3
"""Authenticate the actual component section-degree supplier.

Source hashes and exact symbolic accounting supplement the human proof.
No Lean build or automatic verification of geometric theorems is claimed.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "auth", ROOT/"scripts/check_geometry_arithmetic_frontier_geometric_filtration.py")
auth = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(auth)
D = "Development.AbelianVarietyTheory.Definitions.Divisors."
P = "Development.AbelianVarietyTheory.Proofs.DivisorProofs."
H = "Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights."
T = "Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries."
RANGES = {
    D+"BarCompSubsetClosure": [(86,121)],
    D+"ExistsResolProjSpace": [(181,220),(231,264)],
    D+"NonemptyCuspFrame": [(118,194)],
    D+"HasBoundedPolesGlobalData": [(109,145),(336,368)],
    D+"PointHeight": [(27,35)],
    D+"AevalEqZeroOfMemConeIdeal": [(220,269)],
    D+"IsHomogeneousCompIdeal": [(152,165)],
    P+"FormHeightEqHt": [(16,25),(41,77)],
    P+"IsImageHeightUnique": [(403,442),(449,472)],
    P+"DegreeSupLatticeComponentEq": [(17,55),(57,80),(84,109)],
    P+"HilbertSamuelComponentShortBasisBound": [(26,37)],
    P+"CuspFormsExtendVanishCompactifiedFlagSpace": [(25,35),(53,101)],
    H+"ExistsWeightHodgeBundleGenerated": [(22,53)],
    H+"HodgeBundleSandwichBound": [(24,53)],
    H+"HermitianGeometricHypothesisHolds": [(19,47)],
    H+"ExistsDegreeParametersBound": [(33,76)],
    T+"ExistsDegreeParametersBound": [(34,70)],
    "Formalism.LocalToGlobal.IndefiniteForms.IndefiniteTree.RealCubicMeans.LogMeanShares.LogMeanStatements.HSClaim":
        [(7,22)],
    P+"HermitianSystemSlopeBoundOfDeterminantSlopeInequ": [(14,88)],
}
REFERENCES = [
    ("lan-analytic.pdf","https://www.kwlan.org/articles/cpt-ana-alg.pdf",
     "c77eb9b5132320aa8ecbfb445de8c76839bc5e3027109557f8feac8eed4c89f5",
     [(4070,4092),(4135,4147),(4223,4233)]),
    ("lan-stroh.pdf","https://msp.org/ant/2014/8-8/ant-v8-n8-p01-p.pdf",
     "c9959cf140c155c7f9fd371ebb85f0fcdd4da77b537907fbce3a1b421a9bdb38",
     [(67,82),(100,108)]),
]


def diagnostics():
    D,j,k,u,v,F1,F2,B,Krel=s.symbols("D j k u v F1 F2 B Krel")
    # Formal additive Picard group; k is the exact canonical automorphic weight.
    omegaY=k-B+Krel
    LA=v+D*u
    L=u-F1
    L2=v-F2
    assert s.expand(LA-L2-D*L-(F2+D*F1))==0
    assert s.expand(omegaY+LA+j*L-
                    (k+v+(D+j)*u+Krel-B-j*F1))==0
    assert s.expand((k+v+(D+j)*u)+u-(k+v+(D+j+1)*u))==0
    # The sum G is over complex places, each representing a conjugate pair.
    a,d,ln2,ldisc,lI,G=s.symbols("a d ln2 ldisc lI G",positive=True)
    logcovol=-a*d*ln2/2+d*ldisc/2+lI+G
    normalized=-logcovol/a-d*ln2/2+d*ldisc/(2*a)
    assert s.expand(normalized+(lI+G)/a)==0
    # Literal HSClaimS26: all coefficients of the gap are nonnegative.
    D0,t0,ln,la,lb,rhoextra,lt,habs=s.symbols(
        "D0 t0 ln la lb rhoextra lt habs",nonnegative=True)
    dim=D0+1
    time=dim+1+t0
    an=(ln+1)/2
    c=la+ln+an
    rho=c+rhoextra
    g=(dim+1)*an+1
    gap=s.expand(3*(dim+1)*habs+26*dim**2*(rho+lt)-dim*(dim+1)*c+
                 (time+dim+1-time/2)*lb+(time+dim**2)*(g+2)-time*an)
    coefficients=s.Poly(gap,D0,t0,ln,la,lb,rhoextra,lt,habs).coeffs()
    assert all(x>=0 for x in coefficients)
    # rho-c >= 26log2 +(49/2)log n -1/2 >=25/2.
    lnr=s.symbols("lnr",nonnegative=True)
    assert s.expand(26*(s.Rational(1,2)+lnr)-s.Rational(3,2)*lnr-
                    s.Rational(1,2))==s.Rational(25,2)+s.Rational(49,2)*lnr
    PP,kap,TT,DD=s.symbols("P kap T D",positive=True)
    exactJ=DD*PP*(kap/TT+1)
    wrapperJ=4*(exactJ+TT*PP)+2*DD*PP*kap/TT
    assert s.expand(wrapperJ-exactJ-
                    (3*exactJ+4*TT*PP+2*DD*PP*kap/TT))==0
    theta,ha,cost,J,LD,LT,bb,tt,dd=s.symbols("theta ha cost J LD LT bb tt dd")
    expression=theta*(tt*ha-tt*an-dd*(dd+1)*cost-J-tt*bb/2)-\
        (1-theta)*(tt*cost+tt*bb/2+LD+LT)
    separated=theta*tt*ha-tt*bb/2-theta*(tt*an+dd*(dd+1)*cost+J)-\
        (1-theta)*(tt*cost+LD+LT)
    assert s.expand(expression-separated)==0
    return {
        "exact_Picard_and_weight_identities":True,
        "exact_covolume_degree_and_squared_slope_normalization":True,
        "literal_HSClaimS26_nonnegative_gap_terms":len(coefficients),
        "literal_HSClaimS26_gap":str(gap),
        "rho_minus_c_lower_bound":"25/2+(49/2)log n",
        "exact_J_and_signed_component_sum":True,
        "scope":"Symbolic identities and all-parameter sufficient inequalities; no finite test substitutes for the geometric proof.",
    }


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--offline",action="store_true")
    args=ap.parse_args()
    auth.RANGES=RANGES
    sources=auth.provenance(args.offline)
    refs=[]
    for name,url,digest,ranges in REFERENCES:
        path=ROOT/"build/geometry-section-references"/name
        assert auth.sha(path.read_bytes())==digest
        txt=path.with_suffix(".txt").read_bytes().splitlines(keepends=True)
        refs.append({"url":url,"pdf_sha256":digest,
                     "text_sha256":auth.sha(b"".join(txt)),
                     "excerpts":[{"lines":[lo,hi],"sha256":auth.sha(b"".join(txt[lo-1:hi]))}
                                 for lo,hi in ranges]})
    checks=diagnostics()
    artifacts=[
        "paper/shared/geometry-section-continuation.tex",
        "paper/shared/geometry-section-continuation-references.tex",
        "notes/geometry-section-continuation.md",
        "scripts/geometry-section-continuation.py",
    ]
    result={
        "status":"PASS",
        "classification":"actual original component arithmetic section-degree supplier",
        "sources":sources,"primary_references":refs,"diagnostics":checks,
        "artifacts":{p:auth.sha((ROOT/p).read_bytes()) for p in artifacts},
        "verification_scope":"Authenticated bounded source and primary references; exact algebra and numerical inequalities; general proof in the TeX; no Lean build.",
        "independent_review":"Root reviews actual geometric/canonical construction; global_norm_frontier reviews height, norm, degree and arithmetic transport.",
        "retained_hypotheses":[
            "constructed original smooth projective toroidal full flag model and component field",
            "exact original canonical weight, divided weights and strict gap conditions",
            "original complete integral lattices and Petersson probability metrics",
            "already supplied short families and global upper Bergman bound",
            "all original numerical family assumptions where separately required",
        ],
        "not_claimed":[
            "individual integral jet-lifting or arithmetic point-selection theorems",
            "the separate all-point corrected-height comparison",
            "construction of any still separate original numerical family",
            "completion of W10 or of RH or GRH",
        ],
        "whole_node_counts_changed":False,
    }
    target=ROOT/"certificates/geometry-section-continuation.json"
    target.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"PASS","sources":len(sources),"primary_references":len(refs),
                      "literal_HSClaimS26_gap_terms":checks["literal_HSClaimS26_nonnegative_gap_terms"]}))


if __name__=="__main__":
    main()
