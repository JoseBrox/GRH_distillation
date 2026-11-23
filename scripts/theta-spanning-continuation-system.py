#!/usr/bin/env python3
"""Authenticate the actual finite theta system and check finite phase models.

Finite Heisenberg calculations are exact normalization diagnostics. The
all-rank and all-number-field proof remains the argument in the TeX file;
no Lean build or uniform arithmetic norm estimate is performed.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth

STEM="theta-spanning-continuation-system"
P="Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation."
D="Development.AbelianVarietyTheory.Definitions.SpanningFamilies."
RANGES={
    D+"IsSystem":[(113,144),(146,179),(194,218)],
    P+"ExistsVacuaAndMultipliers":[(39,106)],
    P+"LevelTestFunctionFiniteSumEquivariant":[(346,387),(393,414),(416,491)],
    P+"ThetaTestFunctionNormAndOverlapBound":[(198,232)],
    P+"ThetaTestFunctionOverlapEqZeroOutsideLevel":[(172,206),(207,233)],
    P+"ThetaTestFunctionNoCoinvariantsIsotropic":[(144,214),(216,275)],
    P+"DoubledLatticeSplit":[(226,273),(274,328)],
    P+"DoubledVacuumEqHermitianCharacter":[(554,585),(586,637)],
    P+"AdmissibleDoubledHermitianThetaFamily":[(126,179),(413,462)],
    P+"HermitianThetaLevelDataFormsSystem":[(60,113),(138,177)],
    P+"KernelIdentity":[(50,118),(181,210),(279,341)],
    P+"HermitianThetaSeriesSpanBoundedForms":[(168,210),(211,254)],
    P+"LevelThetaSpan":[(10,20)],
    P+"StableFormsEqSumThetaSeriesFreeLowerRows":[(30,51)],
    "Development.AbelianVarietyTheory.Proofs.DivisorProofs.HolSub0LeSpanRaw":[(146,176)],
}


def simp(x):
    return sp.simplify(sp.expand_complex(x))


def equal(A,B):
    return all(simp(v)==0 for v in A-B)


def finite_heisenberg():
    pairs=tensor_pairs=0
    for p in (2,3):
        zeta=-sp.Integer(1) if p==2 else (-1+sp.sqrt(3)*sp.I)/2
        lines=[(0,1)]+[(1,b) for b in range(p)]
        projectors=[]
        for a,b in lines:
            H=sp.zeros(p)
            for x in range(p):
                H[x,(x+a)%p]=zeta**(b*x)
            # At two the mixed Weyl generator squares to -1; the
            # semicharacter correction i is indispensable.
            if p==2 and a*b:
                assert equal(H**2,-sp.eye(p))
                H=sp.I*H
            assert equal(H**p,sp.eye(p))
            P0=sum((H**j for j in range(p)),sp.zeros(p))/p
            assert equal(P0*P0,P0) and equal(P0.conjugate().T,P0)
            assert simp(sp.trace(P0))==1
            projectors.append(P0)
        for i,A in enumerate(projectors):
            for j,B in enumerate(projectors):
                expected=1 if i==j else sp.Rational(1,p)
                assert simp(sp.trace(A*B))==expected
                pairs+=1
                assert simp(sp.trace(sp.kronecker_product(A,A)*sp.kronecker_product(B,B)))==expected**2
                tensor_pairs+=1
        # The same Lagrangian with a different character is orthogonal:
        # agreement of semicharacters on intersections is a real input.
        v=sp.zeros(p,1);v[1,0]=1
        wrong=v*v.T
        assert simp(sp.trace(projectors[0]*wrong))==0
    return {"primes":[2,3],"ordered_projector_pairs":pairs,
            "tensor_square_overlap_pairs":tensor_pairs,
            "dyadic_weyl_phase_required_and_retained":True,
            "incompatible_character_countercheck":True}


def lattice_counts():
    cases=0
    for d in range(1,7):
        for p in (2,3,5,7):
            for e in range(1,6):
                count=Fraction(1)
                for j in range(1,e+1):
                    count*=Fraction(p**(d+j-1)-1,p**j-1)
                assert count.denominator==1 and count<=p**(d*e)
                cases+=1
    bound=sum((Fraction(1,m*m) for m in range(2,21)),Fraction(0))+Fraction(1,20)
    assert bound<Fraction(65,100)
    return {"exact_elementary_divisor_cases":cases,
            "tail_upper_bound":str(bound),"tail_lt_065":True}


def annihilator():
    w=(-1+sp.sqrt(3)*sp.I)/2
    chars=[(1,0),(0,1),(1,1)]
    generators=[(1,0),(0,1),(1,0)]
    def val(c,v):return w**((c[0]*v[0]+c[1]*v[1])%3)
    A=sp.eye(len(chars));augmentation=sp.Integer(1)
    for c,v in zip(chars,generators):
        scalar=val(c,v)
        assert simp(scalar-1)!=0
        A=A*(sp.diag(*(val(other,v) for other in chars))-scalar*sp.eye(len(chars)))
        augmentation*=1-scalar
    assert equal(A,sp.zeros(len(chars))) and simp(augmentation)!=0
    return {"characters":len(chars),"product_annihilator_zero":True,
            "augmentation_nonzero":True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline",action="store_true")
    args=parser.parse_args()
    auth.RANGES=RANGES
    sources=auth.provenance(args.offline)
    paths=[f"paper/shared/{STEM}.tex",f"notes/{STEM}.md",f"scripts/{STEM}.py"]
    record={"status":"PASS","classification":"closed actual suppliers; pending independent mathematical review",
            "frontier":"All original IsSystem fields and actual LevelThetaSpan at even n >= 4[E:Q]r+4",
            "artifacts":{p:auth.sha((auth.ROOT/p).read_bytes()) for p in paths},
            "sources":sources,"diagnostics":{"finite_heisenberg":finite_heisenberg(),
            "lattice_counts":lattice_counts(),"isotropic_annihilator":annihilator()},
            "scope":{"same_vectors_levels_and_lattices":True,"dyadic_semicharacter_retained":True,
              "exact_doubled_phase_retained":True,"field_degree_in_threshold_retained":True,
              "original_class_mass_kappa_rho_retained":True,"whole_node_closed":False,
              "global_raw_span_transfer_closed":False,"short_integral_h0_hsh_closed":False,
              "no_uniform_global_norm_claim":True,"no_lean_build":True}}
    out=auth.ROOT/f"certificates/{STEM}.json"
    out.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":"PASS","source_files":len(sources),"output":str(out.relative_to(auth.ROOT))}))


if __name__=="__main__":main()
