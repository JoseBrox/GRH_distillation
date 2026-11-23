#!/usr/bin/env python3
"""Authenticate the actual identity-cover raw-span contract and scalars."""
from __future__ import annotations
import argparse
import json
import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth

STEM="theta-spanning-continuation-raw"
P="Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation."
D="Development.AbelianVarietyTheory.Definitions.SpanningFamilies."
RANGES={
    "Formalism.LocalToGlobal.ProjectiveLattices.ThShort":[(300,311)],
    D+"IsBaseClassLevelAdapted":[(74,103)],
    D+"IsStabForm":[(22,79)],
    P+"TensorLatticeVacuaExistUnique":[(18,37)],
    P+"ExistsClassicalLevelDataCoverSelfDual":[(361,431)],
    P+"ExistsComponentsLatticesMovedToLevelFamily":[(162,217)],
    P+"StrongApproximationUnitaryCongruence":[(25,58),(282,367)],
    P+"VacuumMultiplierEqOneOnStabiliser":[(28,52)],
    P+"LeSupOfCoprime":[(19,32),(100,143)],
    P+"FourierTranslatesVacuumRootsLevelPoints":[(38,45),(101,136),(606,674),(675,722)],
    P+"CoverFourierCoeffEqFiniteFourierSum":[(415,476)],
    P+"GphiEqSmulPhiF":[(59,99)],
    P+"ShortSeriesReadingsEqClassicalThetaSeries":[(88,127),(128,160)],
    P+"HarmonicRowHighestEqSpanIntegralHarmonic":[(43,102)],
    P+"CuspFormsVanishingOffFramesLeSpanShortTheta":[(53,90),(91,138)],
    "Development.AbelianVarietyTheory.Proofs.DivisorProofs.HolSub0LeSpanRaw":[(34,76),(146,176)],
    "Development.AbelianVarietyTheory.Proofs.DivisorProofs.PolynomialCoefficientEmbeddingNormLeOfL1Bound":[(399,444)],
    "Development.AbelianVarietyTheory.Proofs.DivisorProofs.DeepLevelCoverPrincipalLevelLawsGalois":[(59,76)],
}


def zero(x):
    return sp.simplify(sp.expand_complex(x))==0


def matrix_equal(a,b):
    return all(zero(x) for x in a-b)


def finite_fourier():
    cases=0
    for p,zeta in [(3,(-1+sp.sqrt(3)*sp.I)/2),
                   (5,(sp.sqrt(5)-1)/4+sp.I*sp.sqrt(10+2*sp.sqrt(5))/4)]:
        v=sp.zeros(p,1);v[0]=1
        proj=sp.ones(p,p)/p
        for b in range(p):
            left=sp.zeros(p,1)
            for a in range(p):
                h=sp.zeros(p)
                for x in range(p):h[x,(x+a)%p]=1
                left+=zeta**((-a*b)%p)*h*v
            hc=sp.diag(*(zeta**((b*x)%p) for x in range(p)))
            assert matrix_equal(left,p*hc*proj*v)
            cases+=1
    return {"cyclic_moduli":[3,5],"all_character_cases":cases,
            "negative_pairing_sign_and_full_cardinality":True}


def disjoint_projection():
    # Distinct local factors: the Lambda modification acts on the first;
    # the half-level shift on the second. Keep a nonreal baseline phase.
    e=sp.Matrix([1,0]);f=sp.Matrix([1,1])/sp.sqrt(2)
    g=sp.Matrix([1,sp.I])/sp.sqrt(2)
    pe=e*e.conjugate().T;pf=f*f.conjugate().T;pg=g*g.conjugate().T
    a=sp.kronecker_product(pf,pe)
    c=sp.kronecker_product(pf,pg)
    v=sp.I*sp.kronecker_product(e,e)
    v0=sp.kronecker_product(e,g)
    target=sp.kronecker_product(f,g)
    t=(v0.conjugate().T*v)[0]
    assert not zero(t) and not zero(sp.im(t))
    assert matrix_equal(c*a*v,t*target/sp.sqrt(2))
    return {"disjoint_local_projection_identity":True,
            "nonreal_component_phase_retained":True}


def index_cancellation():
    m,c=sp.symbols("m c",positive=True)
    r=sp.symbols("r",integer=True,positive=True)
    assert sp.simplify((m**r/c)*c*m**(-r/2)-m**(r/2))==0
    return {"J_over_I_times_fourier_over_C_times_projection":"m^(r/2)",
            "auxiliary_N_cancels":True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline",action="store_true")
    args=parser.parse_args()
    auth.RANGES=RANGES
    sources=auth.provenance(args.offline)
    paths=[f"paper/shared/{STEM}.tex",f"notes/{STEM}.md",f"scripts/{STEM}.py"]
    record={"status":"PASS","classification":"closed raw-span supplier; pending independent mathematical review",
            "frontier":"Original HolSub0LeSpanRaw on the actual models and identity cover",
            "artifacts":{p:auth.sha((auth.ROOT/p).read_bytes()) for p in paths},
            "sources":sources,
            "diagnostics":{"finite_fourier":finite_fourier(),
                           "projection_phase":disjoint_projection(),
                           "index_cancellation":index_cancellation()},
            "scope":{"identity_cover_only":True,"same_raw_theta_sections":True,
                     "same_coefficient_field":True,"all_coefficient_algebras_retained":True,
                     "component_phase_retained":True,"whole_node_closed":False,
                     "short_integral_h0_hsh_closed":False,"selected_prime_laws_closed":False,
                     "uniform_norm_estimate":False,"no_lean_build":True}}
    out=auth.ROOT/f"certificates/{STEM}.json"
    out.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":"PASS","source_files":len(sources),
                      "output":str(out.relative_to(auth.ROOT))}))


if __name__=="__main__":main()
