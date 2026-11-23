#!/usr/bin/env python3
"""Authenticate the original transport interfaces and check exact matrices."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s

from check_sources import inspect_file

ROOT=Path(__file__).resolve().parents[1]
REV="ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
P="Development.AbelianVarietyTheory.Proofs.FlagMeasures."
D="Development.AbelianVarietyTheory.Definitions.SemilocalFrames."
SOURCES=[
    ("Formalism.FlagUnipotentLattices.MemOfOrthogonalAnisotropic",
     "fc33d4865a039411e31601b93421288ed3c78eafc99fee7da465cef04b4120e2",[[20,27],[55,58]]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.FractionFieldToGenericStalkAlgebraMapEq",
     "6279e779358b26282318021b6a1efb212df0428d7c34e5674c8b9fe96712923e",[[150,168]]),
    (D+"NormalFormDualOrthogonalLast",
     "05c633d7e619d916d6041040f1a0fc0711da10bb31f42984cacd40631cb290a6",[[33,120]]),
    (D+"FlagPairDefinitePartLattice",
     "33962c30e534b2a499694f1493e8c69f69e6ef92fb7c9ef076edc543ed0aa5a7",[[128,176]]),
    (P+"NormalFormFlagLatticesNearUnderStabiliser",
     "14826316fe348f0e49cbb1f9cef72f0a56b4b44d073ca2c6c27d5e4973214f31",[[86,151],[875,919]]),
    (P+"NormalFormIdealDivisibility",
     "02f6abeb81a2e822affb80289ac476efa4da8e196b1bde71bc27ae305594c2c1",[[559,637]]),
    (P+"HermFramePairExistsUnipotentSplitLattice",
     "4964860aaec5fe92a2b2d97b1b8160ed646f9e0c8c0622a83d364199ec81c91f",[[148,186]]),
    (P+"HermFramePairSplitTermNearReferenceBySkew",
     "1fb2792fc23e24ae822de028ac63d114f2d44f76ad6b391a92a793d18b847e15",[[153,298]]),
    (P+"HermFramePairNormalFormExistsConjNearReference",
     "1814e4233df323c63117f15bcaa39eb130462b0efa5765901db6a7be3d0070b6",[[143,174]]),
    (P+"HermFramePairNormalFormInvVolTopLayerLe",
     "5f96bae4799398e712162ea6eded8016d2bef54f8c924c32c7119e81817640c2",[[88,142]]),
    (P+"HermFramePairNormalFormInvVolSkewLayerLe",
     "03dcf2243fcb5f331ecddecfbe946da4cfe73fe7100edfb9d630733e8f7445a2",[[74,126]]),
    (P+"SplitTermWeightLeNearReferenceLattice",
     "8bbd16091fecd56e0b5e5351f0401469080536981f75548068864f94d8713abb",[[35,76]]),
]
ARTIFACTS=["paper/shared/flag-lattice-transport.tex",
           "paper/shared/flag-lattice-transport-references.tex",
           "notes/flag-lattice-transport.md",
           "scripts/flag-lattice-transport-check.py"]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def compositions(n):
    if n==0:
        yield []
    else:
        for first in range(1,n+1):
            for tail in compositions(n-first):
                yield [first]+tail


def integral(A):
    return all(x.q==1 for x in A)


def paired_blocks():
    cases=cofactors=schur=0
    boundaries=set()
    for j in range(5):
        for blocks in compositions(j):
            for signs in itertools.product([-1,1],repeat=j):
                B=s.zeros(j); U=s.eye(j); V=s.eye(j)
                ends=[]; start=0
                for number,length in enumerate(blocks):
                    end=start+length; ends.append(end)
                    for a in range(start,end):
                        b=start+end-1-a
                        B[a,b]=(number+1)*signs[b]
                    start=end
                for a in range(j):
                    for b in range(a+1,j):
                        U[a,b]=s.Rational((a+1)*(b+2)-3,2)
                        V[a,b]=s.Rational((a+2)*(b+1)+1,3)
                G=U.T*B*V
                scale=s.ilcm(*[x.q for x in G]) if len(G)>1 else 1
                B*=scale; G*=scale
                assert integral(G)
                S=s.eye(j); start=0
                for end in ends:
                    S[start:end,start:end]=U[start:end,start:end].inv()
                    start=end
                Sp=B.inv()*S.T.inv()*B if j else s.zeros(0)
                assert S.T*B*Sp==B
                assert Sp.is_upper and all(Sp[a,a]==1 for a in range(j))
                A=(S*U).T; C=Sp*V
                assert A*B*C==G
                start=0
                for end in ends:
                    assert A[start:end,start:end]==s.eye(end-start)
                    start=end
                deltas=[G[:end,:end].det() for end in ends]
                c=3*s.prod(abs(d)**2 for d in deltas)
                assert integral(c*A) and integral(c**2*C)
                assert integral(c*B) and integral(c*B.inv())
                start=0
                for end,delta in zip(ends,deltas):
                    for col in range(start,end):
                        column=A[:end,:end].inv()[:,col]
                        assert column==s.eye(end)[:,col]
                        for row in range(end,j):
                            replacement=G[:end,:end].copy()
                            replacement[col,:]=G[row,:end]
                            assert replacement.det()==delta*A[row,col]
                            cofactors+=1
                    residual=G[start:end,start:]
                    if start:
                        residual-=G[start:end,:start]*G[:start,:start].inv()*G[:start,start:]
                    assert residual==B[start:end,start:end]*C[start:end,start:]
                    schur+=1; start=end
                for r in [j,j+1]:
                    boundaries.add((r,j))
                cases+=1
    # A nonintegral scalar block can occur even though every leading
    # determinant and the full Gram matrix are integral.
    B=s.diag(2,s.Rational(1,2))
    A=s.Matrix([[1,0],[s.Rational(1,2),1]])
    C=A.T; G=A*B*C
    assert G==s.Matrix([[2,1],[1,1]])
    c=3*(G[:1,:1].det()*G.det())**2
    assert integral(c*B) and integral(c*B.inv())
    assert integral(c*A) and integral(c**2*C)
    return {"signed_block_cases":cases,"Cramer_replacement_identities":cofactors,
            "Schur_identities":schur,"boundary_pairs_r_j":sorted(boundaries),
            "nonintegral_scalar_block":"diag(2,1/2), integral Gram [[2,1],[1,1]]",
            "scope":"Exact finite diagnostics; the arbitrary-rank proof is written in FT4--FT8."}


def cm_matrices():
    t=s.symbols("t"); modulus=t**4-t**2+1
    def red(x):
        return s.rem(s.Poly(s.expand(x),t,domain=s.QQ),
                     s.Poly(modulus,t,domain=s.QQ)).as_expr()
    def bar(x):
        return red(s.sympify(x).subs(t,t-t**3))
    def rm(A):
        return A.applyfunc(red)
    def bm(A):
        return A.applyfunc(bar)
    w=t**2
    assert red(w+bar(w))==1
    H0=s.diag(2,-3)
    H=s.zeros(6); H[:2,4:]=s.eye(2); H[4:,:2]=s.eye(2); H[2:4,2:4]=H0
    C=s.Matrix([[s.Rational(1,3)+t,t**2],[1-t,s.Rational(2,5)]])
    Cs=rm(H0.inv()*bm(C).T)
    n=s.eye(6); n[:2,2:4]=C; n[2:4,4:]=-Cs; n[:2,4:]=rm(-w*C*Cs)
    assert rm(n.T*H*bm(n))==H
    graph=s.zeros(6,2); graph[:2,:]=-C; graph[2:4,:]=s.eye(2)
    flat=s.zeros(6,2); flat[2:4,:]=s.eye(2)
    assert rm(n*graph)==flat
    D=s.Matrix([[1,t/3],[0,1]]); A=s.diag(1,-1)
    diagonal=s.diag(D,A,bm(D.inv()).T)
    lift=rm(n*diagonal)
    assert rm(lift.T*H*bm(lift))==H
    assert lift[:2,2:4]==rm(C*A)
    assert lift[:2,:2]==D and lift[2:4,2:4]==A
    b=s.Matrix([[t/2,1+t**3],[t**2,s.Rational(1,5)]])
    M=rm(b+bm(b).T); K=rm(b-w*M)
    assert rm(K+bm(K).T)==s.zeros(2)
    central=s.eye(6); central[:2,4:]=-K
    assert rm(central.T*H*bm(central))==H
    phi=s.zeros(6,2); phi[:2,:]=b; phi[2:4,:]=C; phi[4:,:]=s.eye(2)
    assert rm(central*phi)[:2,:]==rm(w*M)
    discE=int(s.discriminant(modulus,t)); discF=int(s.discriminant(t*t-3,t))
    assert discE==discF**2==144
    return {"field":"Q(zeta_12)/Q(sqrt(3))","relative_discriminant_norm":1,
            "common_isotropic_rank":2,"middle_Gram":"diag(2,-3)",
            "trace_one_element":"t^2","graph_splitting_unitary":True,
            "ordered_top_lift_unitary":True,"top_right_action":"C A = B",
            "skew_adjoint_correction_unitary":True,
            "scope":"Exact quotient-field arithmetic with the convention h linear in its first argument."}


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
    dep="certificates/unipotent-stabilizer-covolume.json"
    previous=json.loads((ROOT/dep).read_text())
    for path,expected in previous["artifact_sha256"].items():
        assert sha((ROOT/path).read_bytes())==expected,(dep,path)
    r,e=s.symbols("r e",nonnegative=True,integer=True)
    assert s.expand(3*(2*r+2)+4)==6*r+10
    assert s.Poly(12*r+50-(6*r+10),r).all_coeffs()==[6,40]
    assert s.expand(3*e+11-1-(2*e+1))==e+9
    block=paired_blocks(); cm=cm_matrices()
    cert={"result":"Original integral flag transport and top/central stabilizer bounds",
          "classification":"closed actual arithmetic suppliers; not a full W08 proof-map node",
          "source_repository":"jsmorph/rh","source_revision":REV,
          "source_records":records,"dependency_certificates":{dep:sha((ROOT/dep).read_bytes())},
          "paired_block_diagnostics":block,"exact_CM_diagnostics":cm,
          "written_proof_labels":["lem:flag-reference-dual-ideal","thm:flag-lattice-near-representative",
                                  "thm:flag-small-stabilizer-quotients"],
          "artifact_sha256":{p:sha((ROOT/p).read_bytes()) for p in ARTIFACTS},
          "remaining":["adapted-normal-form term assignment and exact reciprocal row multiplicity"],
          "verification_scope":"Pinned-source bytes and exact matrix/exponent diagnostics; general projective-lattice and group arguments are written proofs. No Lean build or full W08 claim."}
    path=ROOT/"certificates/flag-lattice-transport.json"
    path.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"certificate":str(path.relative_to(ROOT)),"sources":len(records),
                      "block_cases":block["signed_block_cases"],"CM_checks":3,"passed":True}))


if __name__=="__main__":
    main()
