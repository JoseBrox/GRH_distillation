#!/usr/bin/env python3
"""Authenticate the weighted flag sum and check exact integral gluings."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import sympy as s

from check_sources import inspect_file

ROOT=Path(__file__).resolve().parents[1]
REV="ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
P="Development.AbelianVarietyTheory.Proofs.FlagMeasures."
D="Development.AbelianVarietyTheory.Definitions.SemilocalFrames."
SOURCES=[
    (D+"NormalFormDualOrthogonalLast",
     "05c633d7e619d916d6041040f1a0fc0711da10bb31f42984cacd40631cb290a6",[[89,120]]),
    (D+"FlagPairDefinitePartLattice",
     "33962c30e534b2a499694f1493e8c69f69e6ef92fb7c9ef076edc543ed0aa5a7",[[128,176]]),
    (D+"AdaptSelf",
     "d6b5eb53446b362a59db0635fb25a30f011976a7b40e964b3550386cc8b1c7b3",[[12,44]]),
    (P+"FlagPairDefiniteThetaLatticeLeFixedIndexBound",
     "4083f765e6ccae099248cf903d1b2134a08d558f6aa42bdd846aa37a8253137b",[[125,190]]),
    (P+"HermFramePairOmSumSameDatumLe",
     "70e40ffeaabc32669fe7c452b1725cbee02322dc8d0e4973504de5c1530b2784",[[237,318]]),
    (P+"HermFrameWeightSumSameDatumLe",
     "7e092fd3010d3c1b72bdf544c73761f337c0c603e538d3809cc736dbcbd314a9",[[48,117]]),
    (P+"SumWeightsInequivalentHermFrameTermsLe",
     "b9c9f3cc3f106977dcccf63b946872b7914318d58cb1c0725345a33e193c73b9",[[44,95]]),
    (P+"FlagFrameVectorMemCommonSubspace",
     "4cd1051e8212941292de4ebc8167c9c5443c67f883a5db727b5b9de5b29cb3c6",[[120,175],[204,270]]),
    (P+"TermPairsRowLatticeCountedViaEmbeddings",
     "6dfd6333685cb70fe079a958eba263dbe5b6bfa4c35edc570232dd5ca1b0687e",[[114,213]]),
]
ARTIFACTS=["paper/shared/weighted-flag-lattice-sum.tex",
           "paper/shared/weighted-flag-lattice-sum-references.tex",
           "notes/weighted-flag-lattice-sum.md",
           "scripts/weighted-flag-lattice-sum-check.py"]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def cm_gluings():
    t=s.symbols("t"); modulus=t**4-t**2+1
    def red(x):
        return s.rem(s.Poly(s.expand(x),t,domain=s.QQ),
                     s.Poly(modulus,t,domain=s.QQ)).as_expr()
    def bar(x):
        return red(s.sympify(x).subs(t,t-t**3))
    def bm(A):
        return A.applyfunc(bar)
    def rm(A):
        return A.applyfunc(red)
    def norm(a):
        M=s.Matrix.hstack(*[s.Matrix([
            s.Poly(red(a*t**j),t).coeff_monomial(t**i)
            for i in range(4)]) for j in range(4)])
        return abs(M.det())
    H=s.Matrix([[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,-1]])
    e,f,w,z=[s.eye(4)[:,i] for i in range(4)]
    def h(a,b):
        return red((a.T*H*bm(b))[0])
    # Primitive isotropic pair with all of the normalized determinant
    # in its saturation index: a=16 and n=b=1.
    ep=t**3*e+2*f
    assert h(ep,ep)==0 and h(e,ep)==2
    B=s.Matrix([[1,t**3],[0,2]])
    a1=norm(B.det()); Delta1=norm(h(e,ep))
    assert a1==Delta1==16
    assert norm(t**3)==1  # ep is primitive, not merely nonzero.
    # Primitive pair with a=1 and nontrivial orthogonal-complement index n=16.
    ep=2*f+w+z; last=e+w+3*z
    assert h(ep,ep)==0 and h(e,ep)==2
    assert h(last,last)==-8 and h(last,ep)==h(last,e)==0
    qw=w-e/2; qz=z+e/2
    assert h(qw,qw)==1 and h(qz,qz)==-1 and h(qw,qz)==0
    C=s.Matrix([[1,0],[1,2]])
    Jp=s.Matrix([[s.Rational(1,2),-1],[s.Rational(1,2),1]])
    HQ=s.diag(1,-1)
    assert Jp.T*HQ*Jp==s.Matrix([[0,-1],[-1,0]])
    assert (Jp.inv()*C).applyfunc(lambda x:x.q)==s.ones(2)
    n2=norm(C.det()); deltaC=s.sqrt(norm((C.T*HQ*C).det()))
    assert n2==deltaC==16
    paired=s.Matrix.hstack(e,ep)
    # Rows e,w form a unit minor, hence the paired lattice is saturated.
    assert paired.extract([0,2],[0,1]).det()==1
    full=s.Matrix.hstack(e,ep,w+z,e+2*z)
    assert norm(full.det())==256
    assert s.sqrt(norm((paired.T*H*paired).det()))==16
    # The actual second isotropic quotient lifts these two generators.
    assert rm((qw+qz)/2-ep/2)==-f
    assert rm(-qw+qz)==e-w+z
    assert h(-qw+qz,ep)==0
    # J intersect J' = C: in J' coordinates, (alpha/2-beta,
    # alpha/2+beta) is integral exactly when alpha is in 2 O_E.
    intersection=s.Matrix([[1,-1],[1,1]])
    assert (C.inv()*intersection).det()==1
    assert all(x.q==1 for x in C.inv()*intersection)
    # Nontrivial common-isotropic integral defect, with b^2=Delta sharply.
    H6=s.zeros(6); H6[:2,2:4]=s.eye(2); H6[2:4,:2]=s.eye(2)
    H6[4,4]=1; H6[5,5]=-1
    p,q,ps,qs,ww,zz=[s.eye(6)[:,i] for i in range(6)]
    def h6(a,b):
        return red((a.T*H6*bm(b))[0])
    radical=2*p-q; v=ps+2*qs
    e0=q; e1=radical/2; ep0=-radical+2*v
    for a,b in [(e0,e0),(e1,e1),(ep0,ep0),(e0,e1),(ep0,e1)]:
        assert h6(a,b)==0
    assert h6(p,v)==1 and h6(radical,v)==0
    assert h6(e0,ep0)==4
    # First flag: p=e1+e0/2. Second: v=e1+ep0/2.
    assert p==e1+e0/2 and v==e1+ep0/2
    b1=norm(s.Matrix([[0,2],[1,-1]]).det())
    b2=norm(s.Matrix([[-1,1],[2,0]]).det())
    Delta3=norm(h6(e0,ep0))
    assert b1==b2==16 and b1**2==Delta3==256
    discE=int(s.discriminant(modulus,t)); discF=int(s.discriminant(t*t-3,t))
    assert discE==discF**2==144
    return {"field":"Q(zeta_12)/Q(sqrt(3))","relative_discriminant_norm":1,
            "all_indices_are_absolute_additive_indices":True,
            "cases":[{"r":1,"j":1,"a":16,"n":1,"b":1,"Delta":16},
                     {"r":1,"j":1,"a":1,"n":16,"b":1,"Delta":16,
                      "T":8,"discriminant_gluing_order":256,
                      "common_quotient_intersection_equals_C":True},
                     {"r":2,"j":1,"a":1,"n":1,"b":16,"Delta":256,
                      "x":1,"i":1,"x_i_squared_b_squared_equals_Delta":True}],
            "scope":"Exact examples with primitive lattices and original leading-ideal conditions, including a sharp nontrivial b^2 factor; not a proof of the general theorem."}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline",action="store_true"); args=parser.parse_args()
    packed=(ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inv=json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert sha(packed)==inv["compressed_graph"]["sha256"]
    atlas=json.loads(gzip.decompress(packed))
    assert atlas["repository"]=="jsmorph/rh" and atlas["commit"]==REV
    rows={r[0]:r for r in atlas["modules"]}; records=[]
    for module,expected,ranges in SOURCES:
        item={"repository":"jsmorph/rh","commit":REV,
              "path":"lean/src/"+module.replace(".","/")+".lean",
              "git_blob_sha1":rows[module][1]}
        actual=inspect_file(item,args.offline); assert actual["sha256"]==expected
        records.append({"module":module,"sha256":expected,
                        "git_blob_sha1":rows[module][1],"inspected_ranges":ranges})
    deps={}
    for name in ["maximal-hermitian-mass","unipotent-stabilizer-covolume","flag-lattice-transport"]:
        path="certificates/"+name+".json"
        previous=json.loads((ROOT/path).read_text())
        for artifact,expected in previous["artifact_sha256"].items():
            assert sha((ROOT/artifact).read_bytes())==expected,(path,artifact)
        deps[path]=sha((ROOT/path).read_bytes())
    r=s.symbols("r",nonnegative=True,integer=True)
    q=2*r+1; e=12*r+50
    exponent=s.expand(r+2*q+2*(8*e+22)*q*q)
    assert exponent==768*r**3+4144*r**2+3573*r+846
    slack=s.Poly(s.expand(10000*(r+1)**3-exponent),r)
    assert slack.all_coeffs()==[9232,25856,26427,9154]
    cm=cm_gluings()
    cert={"result":"Original fixed-normal-form weighted sum and exact datBd arithmetic expression",
          "classification":"closed actual arithmetic suppliers; term correspondence and full W08 remain open",
          "source_repository":"jsmorph/rh","source_revision":REV,
          "source_records":records,"dependency_certificates":deps,
          "exact_CM_discriminant_diagnostics":cm,
          "source_exponent_check":{"actual_polynomial":str(exponent),"positive_slack_coefficients":slack.all_coeffs()},
          "written_proof_labels":["lem:flag-fixed-index-constraint","thm:fixed-normal-form-weighted-sum"],
          "artifact_sha256":{p:sha((ROOT/p).read_bytes()) for p in ARTIFACTS},
          "remaining":["adapted-normal-form assignment for original relevant terms",
                       "transport of actual flag classes and embedded datum",
                       "reciprocal original row-automorphism multiplicity"],
          "verification_scope":"Pinned-source byte authentication, dependency hashes, exact CM lattice examples and exact exponent arithmetic. General integral gluing, orbit weights and counts are written proofs. No Lean build or full PerRowC/W08 claim."}
    path=ROOT/"certificates/weighted-flag-lattice-sum.json"
    path.write_text(json.dumps(cert,indent=2,ensure_ascii=False,default=int)+"\n")
    print(json.dumps({"certificate":str(path.relative_to(ROOT)),"sources":len(records),
                      "CM_gluing_examples":len(cm["cases"]),"sharp_b_squared":True,"passed":True}))


if __name__=="__main__":
    main()
