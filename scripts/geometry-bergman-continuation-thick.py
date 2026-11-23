#!/usr/bin/env python3
"""Authenticate the actual thick peak and exact normalization diagnostics.

This checker does not prove the general analytic or automorphic theorem.
The ordinary proof and independent review are separate evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction

import sympy as sp

import check_geometry_arithmetic_frontier_geometric_filtration as auth

STEM = "geometry-bergman-continuation-thick"
P = "Development.AbelianVarietyTheory.Proofs.DivisorProofs."
H = "Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights."
A = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.ArakelovVolumes."
RANGES = {
    P + "DeepCongruenceElementSeparatesChartBallThickFram": [(75,139),(141,169),(181,242)],
    P + "SelfDualAndPrincipalCongruenceOrbitsOfGoodLevel": [(27,58),(113,152)],
    P + "MemFullLevelGroupIffCongruenceLcm": [(39,118)],
    P + "ExistsCuspFormPeakAtInjectiveChartFrame": [(23,90),(91,121)],
    P + "CuspFormLowerBoundBergmanFunctionOnComponent": [(49,90),(91,154)],
    H + "BergmanKernelThickPartEstimate": [(11,76)],
    H + "ExistsDegreeParametersBound": [(33,76)],
    A + "ArakelovInstances.CurvatureStatementHolds": [(15,75)],
    A + "UpperBounds.CurvNumStatementPf": [(15,97)],
    P + "ComplexUniformizationLawsOfGoodDeepCover": [(21,49)],
    "Development.AbelianVarietyTheory.Definitions.Divisors.NormNegCmConstantEqAtAllEmbeddings": [(187,203)],
    "Formalism.LocalToGlobal.ProjectiveLattices.PetersonNormSubspace": [(55,82)],
    P + "ExistsThetaWeightExponentsOfLargeGap": [(58,84)],
    "Development.AbelianVarietyTheory.Definitions.Foundations.ExistsFlatSecRankZero": [(341,356)],
}

PRIMARY = [
    ("demailly-l2.pdf", "https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/estimations_l2.pdf",
     "f7fd2dc6fc7f912b24bf5ccbe103699e546941c4aa16e25072e078d18db861fb", [(1815,1837)], "Theorem 8.4"),
    ("harris-localization.pdf", "https://webusers.imj-prg.fr/~michael.harris/BBlocalization_web.pdf",
     "5dcb07389baab2b94f44d7a97dde98382bec3a246070f478c1ca0589bb601925", [(455,487),(1375,1400)], "Theorem 1.4.1 and Proposition 3.3.2"),
    ("miller-schmid-rapid-decay.pdf", "https://arxiv.org/pdf/1106.2149v1",
     "83a460ea43560fad40d630621e4078be72b4d8e14f18d85736f29f429d41a02e", [(82,100),(201,226),(1157,1183)], "Theorem A and Section 6"),
]


def diagnostics():
    z = sp.symbols("z", real=True)
    gram_cases = regular_cases = tensor_cases = cone_cases = 0
    for r in range(2,8):
        for p in range(1,r):
            signs = [1]*p+[-1]*(r-p)
            J = sp.diag(*signs)
            lam0 = [-i if i<p else r-i for i in range(r)]
            for i in range(r):
                for j in range(i+1,r):
                    U = sp.eye(r); U[j,i] = z
                    G = U.T*J*U
                    # Along this root, log|Delta_k| has z^2 coefficient
                    # Delta_k''(0)/(2 Delta_k(0)); its first derivative is zero.
                    c = [sp.Integer(0)]
                    for k in range(1,r+1):
                        d = sp.expand(G[:k,:k].det())
                        assert sp.diff(d,z).subs(z,0)==0
                        c.append(sp.diff(d,z,2).subs(z,0)/(2*d.subs(z,0)))
                    value = sum(lam0[k]*(c[k+1]-c[k]) for k in range(r))
                    expected = signs[i]*signs[j]*(lam0[i]-lam0[j])
                    assert value == expected and 1 <= value <= r
                    gram_cases += 1
            for m in (r+1,2*r+3,100*r**8):
                for shift in (-7,0,11):
                    lam = [shift-m*i-i*(i+1) for i in range(p)]
                    last = shift+m+3
                    lam += [last+m*(r-1-i)+(r-1-i)**2 for i in range(p,r)]
                    for i in range(r):
                        for j in range(i+1,r):
                            assert signs[i]*signs[j]*(lam[i]-lam[j]) >= m*signs[i]*signs[j]*(lam0[i]-lam0[j])
                    mu = [-v for v in reversed(lam[:p])]+[-v for v in reversed(lam[p:])]
                    nu = [mu[i]-(r-p if i<p else -p) for i in range(r)]
                    assert all(nu[i]-nu[i+1] > 0 for i in range(r-1))
                    assert nu[p-1]-nu[p] >= m-r
                    regular_cases += 1
    for r in range(2,15):
        for offset in range(-5,6):
            c=[(-1)**j*(j+offset) for j in range(r)]+[0]
            B=1+max([abs(v) for v in c]+[abs(c[j]-c[j+1]) for j in range(r)])
            b=[B*(r-j) for j in range(r)]+[0]
            a=[b[j]+c[j] for j in range(r+1)]
            assert min(a)>=0 and all(a[j]>=a[j+1] for j in range(r))
            assert all(a[j]-b[j]==c[j] for j in range(r+1))
            cone_cases+=1
    for n in range(1,7):
        radii = [Fraction(j+1,j+2) for j in range(n)]
        left, right = min(radii), min(1/x for x in radii)
        for k in range(1,n+1):
            for offset in range(n):
                # Integral tensors in L tensor L*, exact matrix norm.
                hs = sum((radii[i]/radii[(i+offset)%n])**2 for i in range(k))
                assert hs >= (left*right)**2/k
                tensor_cases += 1
    x=sp.symbols("x",nonnegative=True)
    assert all(v>=0 for v in sp.Poly(sp.expand(100*(x+1)**4-6*(x+1)),x).all_coeffs())
    return {"exact_Gram_root_cases":gram_cases,"exact_regular_weight_cases":regular_cases,
            "exact_tensor_models":tensor_cases,"exact_character_cone_cases":cone_cases,"all_rank_thick_threshold_polynomial":True,
            "scope":"Finite exact sign, weight and tensor diagnostics; no numerical proof of the general peak or cusp assertion."}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--offline",action="store_true");args=ap.parse_args()
    auth.RANGES=RANGES;sources=auth.provenance(args.offline)
    primary=[]
    for name,url,expected,ranges,theorem in PRIMARY:
        p=auth.ROOT/"build/geometry-positivity-references"/name
        actual=hashlib.sha256(p.read_bytes()).hexdigest();assert actual==expected,(name,actual)
        lines=p.with_suffix(".txt").read_text().splitlines()
        primary.append({"url":url,"sha256":actual,"theorem":theorem,
                        "inspected_text_excerpts":[{"start":a,"end":b,"sha256":auth.sha(("\n".join(lines[a-1:b])+"\n").encode())} for a,b in ranges]})
    paths=[f"paper/shared/{STEM}.tex",f"paper/shared/{STEM}-references.tex",f"notes/{STEM}.md",f"scripts/{STEM}.py"]
    result={"status":"PASS","classification":"closed actual thick peak and injectivity supplier; independently reviewed",
            "sources":sources,"primary_references":primary,"diagnostics":diagnostics(),
            "artifacts":{p:auth.sha((auth.ROOT/p).read_bytes()) for p in paths},
            "verification_scope":"Pinned source/reference bytes and exact supplemental diagnostics; the general theorem is the written proof, not an automated or Lean verification.",
            "guards":["original weighted firstMinimumSq and trace duality","original group compared to principal returns by actual fine moduli","original metric/Haar normalization","regular highest-weight cuspidality, not arbitrary L2 cuspidality","no varying-dimensional compactness estimate"],
            "independent_review":"Theta-agent full mathematical review plus parent primary/source checks; recorded in certificates/arithmetic-frontier-second-review.json",
            "remaining":["original thin-region estimate","global integral cusp-frame norm","actual point-height bound","numerical host wrapper and final section remainder"],
            "whole_node_counts_changed":False}
    out=auth.ROOT/"certificates"/(STEM+".json");out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"PASS","sources":len(sources),"primary_references":len(primary),"diagnostics":result['diagnostics']}))


if __name__=="__main__":
    main()
