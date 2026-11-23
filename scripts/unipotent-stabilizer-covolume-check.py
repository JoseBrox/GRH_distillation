#!/usr/bin/env python3
"""Authenticate the actual middle stabilizer and check exact CM examples."""
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
    ("Formalism.FlagUnipotentLattices.MemOfOrthogonalAnisotropic",
     "fc33d4865a039411e31601b93421288ed3c78eafc99fee7da465cef04b4120e2",[[20,27],[41,64]]),
    (D+"FlagPairDefinitePartLattice",
     "33962c30e534b2a499694f1493e8c69f69e6ef92fb7c9ef076edc543ed0aa5a7",[[128,176]]),
    (D+"NormalFormDualOrthogonalLast",
     "05c633d7e619d916d6041040f1a0fc0711da10bb31f42984cacd40631cb290a6",[[33,120]]),
    (P+"HaarInvVolumeMiddleLayerEichlerLe",
     "14fe6ec1d6829c32d5612de3f1310c213717b3f1073aa5531f392ce6c31e9cd3",[[561,576],[780,853],[961,1004],[1008,1100],[1100,1183]]),
    (P+"SplitTermWeightLeNearReferenceLattice",
     "8bbd16091fecd56e0b5e5351f0401469080536981f75548068864f94d8713abb",[[35,76]]),
    (P+"FlagPairDefiniteThetaLatticeLeFixedIndexBound",
     "4083f765e6ccae099248cf903d1b2134a08d558f6aa42bdd846aa37a8253137b",[[125,190]]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.FlagEEqHyperbolic",
     "f2bd94d759cda5036cef38b6093c3b471feb6e17be2f9fb43b33f1bec3b16e08",[[93,100],[119,120]]),
]
ARTIFACTS=["paper/shared/unipotent-stabilizer-covolume.tex",
           "paper/shared/unipotent-stabilizer-covolume-references.tex",
           "notes/unipotent-stabilizer-covolume.md",
           "scripts/unipotent-stabilizer-covolume-check.py"]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def cm_computations():
    t=s.symbols("t")
    modulus=t**4-t**2+1
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
    # Rank-one definite complement W, one common isotropic direction,
    # and the additional norm-minus-one last vector z, so T=1.
    H=s.Matrix([[0,0,0,1],[0,-1,0,0],[0,0,1,0],[1,0,0,0]])
    x=s.Matrix([1,0,0,0])
    v=s.Matrix([0,0,1+t,0])
    u=-v
    def h(a,b):
        return red((a.T*H*bm(b))[0])
    q=red(-w*h(u,u))
    def eich(u0,q0):
        return rm(s.eye(4)+x*(H*bm(u0)).T-u0*(H*bm(x)).T
                  +q0*x*(H*bm(x)).T)
    E=eich(u,q)
    Ei=eich(-u,bar(q))
    assert rm(E.T*H*bm(E))==H
    assert rm(E*Ei)==s.eye(4) and rm(Ei*E)==s.eye(4)
    assert rm(E*x)==x and rm(E*s.Matrix([0,1,0,0]))==s.Matrix([0,1,0,0])
    assert red((E*s.Matrix([0,0,0,1]))[2])==1+t
    for entry in list(E)+list(Ei):
        assert all(coef.q==1 for coef in s.Poly(entry,t).all_coeffs())
    # Integral norm matrices give an independent degree-aware index check.
    def mult_matrix(a):
        return s.Matrix.hstack(*[
            s.Matrix([s.Poly(red(a*t**j),t).coeff_monomial(t**i)
                      for i in range(4)]) for j in range(4)])
    B=mult_matrix(1+t**2)
    assert abs(B.det())==9
    M=(2*s.eye(4)).row_join(s.eye(4)).col_join(s.zeros(4).row_join(B))
    lattice_index=int(abs(M.det()))
    ideal_index=2**4
    tensor_index=int(abs((2*M).det()))
    assert lattice_index==144
    assert tensor_index==ideal_index**2*lattice_index==36864
    disc_E=int(s.discriminant(modulus,t))
    disc_F=int(s.discriminant(t*t-3,t))
    assert disc_E==disc_F**2==144
    return {
        "field":"E=Q(zeta_12), F=Q(sqrt(3))",
        "basis":"1,t,t^2,t^3 with t^4-t^2+1=0",
        "conjugation_t":"t-t^3","trace_one_element":"t^2",
        "norm_relative_discriminant":disc_E//disc_F**2,
        "Eichler":{
            "q":str(q),"matrix":[[str(E[i,j]) for j in range(4)] for i in range(4)],
            "isometry":True,"inverse_both_orders":True,
            "both_matrices_integral":True,"actual_row_image":"1+t"},
        "ideal_lattice_index":{
            "rank_over_E":2,"absolute_degree":4,
            "A":"3 O_E","C":"6 O_E",
            "M_basis_in_L":"columns of [[2,1],[0,1+t^2]]",
            "A_over_C_index":ideal_index,"L_over_M_index":lattice_index,
            "AL_over_CM_index":tensor_index,
            "verified_identity":"[AL:CM]=[A:C]^rank_E * [L:M]"},
        "scope":"Exact examples of the written theorem in a valid finite-unramified CM field, not identification of an original RH auxiliary field."}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline",action="store_true")
    args=parser.parse_args()
    packed=(ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inv=json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert sha(packed)==inv["compressed_graph"]["sha256"]
    atlas=json.loads(gzip.decompress(packed))
    assert atlas["repository"]=="jsmorph/rh" and atlas["commit"]==REV
    rows={r[0]:r for r in atlas["modules"]}
    records=[]
    for module,expected,ranges in SOURCES:
        item={"repository":"jsmorph/rh","commit":REV,
              "path":"lean/src/"+module.replace(".","/")+".lean",
              "git_blob_sha1":rows[module][1]}
        actual=inspect_file(item,args.offline)
        assert actual["sha256"]==expected
        records.append({"module":module,"sha256":expected,
                        "git_blob_sha1":rows[module][1],"inspected_ranges":ranges})
    cert={"result":"Original middle unipotent stabilizer bound b^k(xi)^(r-j)",
          "classification":"closed actual quantitative arithmetic supplier",
          "source_repository":"jsmorph/rh","source_revision":REV,
          "source_records":records,"exact_CM_diagnostics":cm_computations(),
          "written_proof_labels":["thm:middle-unipotent-stabilizer"],
          "artifact_sha256":{p:sha((ROOT/p).read_bytes()) for p in ARTIFACTS},
          "downstream_written_suppliers":["flag-lattice-transport", "weighted-flag-lattice-sum"],
          "remaining":["adapted-normal-form term assignment",
                       "exact flag-class correspondence and reciprocal row-automorphism multiplicity"],
          "verification_scope":"Pinned-source byte authentication and exact quotient-field/matrix computations. General trace, Eichler, lattice filtration and covolume arguments are written proofs. No Lean build or full W08 claim."}
    path=ROOT/"certificates/unipotent-stabilizer-covolume.json"
    path.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"certificate":str(path.relative_to(ROOT)),"sources":len(records),
                      "integral_Eichler_inverse_checked":True,
                      "degree_aware_tensor_index":36864,"passed":True}))


if __name__=="__main__":
    main()
