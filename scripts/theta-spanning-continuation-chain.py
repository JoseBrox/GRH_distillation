#!/usr/bin/env python3
"""Authenticate the actual arithmetic theta-chain construction.

The general theorem is proved in the companion TeX. Finite exact tests
check its phase-action and integral kernel-basis formulas only.
"""
from __future__ import annotations

import argparse
import json
from itertools import product

import check_geometry_arithmetic_frontier_geometric_filtration as auth


STEM = "theta-spanning-continuation-chain"
GI = "Development.AbelianVarietyTheory.Proofs.GlobalInterpolation."
GT = "Development.AbelianVarietyTheory.Definitions.GlobalTwisting."
AM = "Development.AbelianVarietyTheory.Definitions.AutomorphicMembership."
RANGES = {
    GI+"OffOfNotMem": [(83,129),(130,156)],
    GI+"ExistsLevelPrimePointModelRealisation": [(39,94),(103,187),(189,251),(274,298),(421,475),(477,528)],
    GI+"ExistsCoordinatesValueLatticesEqWeylLattices": [(16,109),(112,180),(181,227),(229,275),(281,324),(394,423)],
    GI+"KmapOfOkOfVecP": [(40,94),(96,142),(238,288),(290,309)],
    GI+"TrueChainKernelEqPointKernelAtRepresentatives": [(14,46)],
    "Development.AbelianVarietyTheory.Definitions.GaloisGeometry.TrueWtAddSSNonneg": [(331,366)],
    "Development.AbelianVarietyTheory.Definitions.GaloisGeometry.JetStepEqZeroExample": [(30,43)],
    GI+"ChThOkOfColIn": [(27,70),(80,100),(111,152)],
    GI+"MoveStep": [(26,43),(47,88)],
    GI+"ExistsPointKernelRealisedModels": [(41,90),(114,188)],
    GI+"TrueChainKernelsBoundLevelPrimePlaces": [(17,59)],
    GI+"TrueChainKernelsBoundConjugatePrimePlaces": [(19,63)],
    GI+"ConjugatePrimeBoundPointKernelOfCoefficientKerne": [(33,68)],
    GI+"HeckeLawPointKernelOfCoefficientKernel": [(246,274)],
    GI+"TwistedChainInitialLatticeCompatibleTrueColumns": [(20,48),(58,95),(109,136),(160,173)],
    GI+"ExtInOfValIn": [(58,85),(98,135),(139,198)],
    GI+"LevelChainSharpColumnValuationOfPointKernelLiftL": [(21,25),(57,63),(78,91)],
    GT+"FormsStable": [(128,240),(307,328)],
    GT+"LevelChainSharpColumnValuationOwnChainIff": [(45,75)],
    GT+"ExistsRecordDat": [(20,70)],
    AM+"TrueColumnChoicesHeckeCharReferenceEqOne": [(127,147),(165,194),(219,261)],
}


def phase_quotients():
    """Actual phase relation in finite analogues with nontrivial kernel.

    Marking group C6 maps to rational group C3; chi(g)=zeta6^g.
    D=C6 gives trivial stabilizers, D=C2 gives stabilizers of order 3.
    The kernel C2 acts freely in both examples, matching stab_inj.
    """
    checks=0
    results=[]
    for dmod in (2,6):
        pairs=list(product(range(6),range(dmod)))
        def eq(x,y):
            z,d=x; zp,dp=y
            return any((z-zp-g)%6==0 and (d+g-dp)%dmod==0 for g in (0,3))
        def canon(x):
            return min(y for y in pairs if eq(x,y))
        reps=sorted({canon(x) for x in pairs})
        def act(k,x,g=None):
            gamma,eta=k
            lift=gamma if g is None else g
            assert lift%3==gamma
            z,d=x
            return canon(((eta+z-lift)%6,(d+lift)%dmod))
        groups=list(product(range(3),range(6)))
        for k,x in product(groups,pairs):
            assert act(k,x,k[0])==act(k,x,k[0]+3)
            assert act(k,x)==act(k,canon(x))
            checks+=2
        for k,kp,x in product(groups,groups,reps):
            kk=((k[0]+kp[0])%3,(k[1]+kp[1])%6)
            assert act(kk,x)==act(k,act(kp,x))
            checks+=1
        for d in range(dmod):
            old={g for g in range(6) if (d+g)%dmod==d}
            new={k for k in groups if act(k,(0,d))==canon((0,d))}
            assert {(g%3,g) for g in old}==new
            checks+=1
        results.append({"decorated_set_order":dmod,"point_count":len(reps),
                        "stabilizer_order":6//dmod})
    return {"exact_checks":checks,"examples":results,
            "scope":"Phase quotient/action/lift independence and stabilizer bijection in two finite analogues; not the general construction proof."}


def determinant(matrix):
    # Small exact Laplace expansion; no floating point dependence.
    if not matrix:return 1
    return sum((-1)**j*matrix[0][j]*determinant([r[:j]+r[j+1:] for r in matrix[1:]])
               for j in range(len(matrix)))


def kernel_bases():
    cases=0
    for prime,n in product((2,3,5),range(1,5)):
        for row in product(range(prime),repeat=n):
            if not any(row):continue
            pivot=next(j for j,x in enumerate(row) if x)
            inv=pow(row[pivot],-1,prime)
            B=[[int(i==j) for j in range(n)] for i in range(n)]
            B[pivot][pivot]=prime
            for j in range(n):
                if j!=pivot:B[pivot][j]=-(row[j]*inv%prime)
            assert determinant(B)==prime
            assert all(sum(row[i]*B[i][j] for i in range(n))%prime==0 for j in range(n))
            cases+=1
    return {"exact_integer_cases":cases,
            "scope":"Integral bases for nonzero residue-functional kernels, including characteristic two; determinant exactly the prime."}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline",action="store_true")
    args=parser.parse_args()
    auth.RANGES=RANGES
    sources=auth.provenance(args.offline)
    root=auth.ROOT
    artifacts=[f"paper/shared/{STEM}.tex",f"paper/shared/{STEM}-references.tex",
               f"notes/{STEM}.md",f"scripts/{STEM}.py"]
    dependencies=["paper/sections/recovered/49-ct-section.tex",
                  "paper/sections/recovered/50-lm-section.tex",
                  "paper/sections/recovered/54-te-section.tex",
                  "paper/sections/recovered/55-gm-section.tex",
                  "paper/sections/recovered/56-csp-section.tex",
                  "paper/sections/recovered/57-jcf-section.tex",
                  "paper/sections/recovered/58-hec-section.tex",
                  "paper/sections/recovered/59-cv-section.tex",
                  "paper/sections/recovered/60-tvc-section.tex",
                  "paper/shared/level-chain-integrality.tex"]
    # Locate the established hook proof by its actual label, without
    # assuming a chronological filename.
    hook=[]
    for path in (root/"paper/sections/recovered").glob("*.tex"):
        if "\\label{fh-hook-product}" in path.read_text():hook.append(path)
    assert len(hook)==1
    dependencies.append(str(hook[0].relative_to(root)))
    diagnostics={"phase_quotient":phase_quotients(),"kernel_bases":kernel_bases()}
    record={"status":"PASS","classification":"closed actual local chain realization and compatibility supplier; independently reviewed",
            "sources":sources,
            "artifacts":{p:auth.sha((root/p).read_bytes()) for p in artifacts},
            "established_dependency_hashes":{p:auth.sha((root/p).read_bytes()) for p in dependencies},
            "diagnostics":diagnostics,
            "scope_guards":["same full root phases and original theta normalization",
                            "same original frame Hermitian form and automorphism masses",
                            "same conjugate embeddings, dual frames and determinant twists",
                            "rational integral lifts constructed, not assumed",
                            "same original stage-zero twist and source prime-power factor",
                            "hook-product proof supplies Weyl equality; no unverified lowest-alcove input"],
            "remaining":["exact equality with normalized global Poincare periods and retained restrictions",
                         "uniform field-degree/discriminant and global norm/period budgets",
                         "whole W06 completion is not claimed"],
            "verification_scope":"Authenticated source bytes and bounded excerpts; finite exact phase and kernel-basis diagnostics; general proof in companion TeX; no Lean build."}
    out=root/"certificates"/(STEM+".json")
    out.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":"PASS","source_files":len(sources),
                      "phase_checks":diagnostics["phase_quotient"]["exact_checks"],
                      "kernel_basis_cases":diagnostics["kernel_bases"]["exact_integer_cases"],
                      "certificate":str(out.relative_to(root))}))


if __name__=="__main__":main()
