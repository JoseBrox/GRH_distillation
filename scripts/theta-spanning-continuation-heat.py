#!/usr/bin/env python3
"""Authenticate the actual heat comparison and exact normalization diagnostics.

The all-rank proof is in the TeX file. These symbolic checks catch the
heat coefficient and scope traps; they are not a Lean build or an
arithmetic norm calculation.
"""
from __future__ import annotations

import argparse
import json
import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth

STEM = "theta-spanning-continuation-heat"
P = "Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation."
D = "Development.AbelianVarietyTheory.Definitions.SpanningFamilies."
RANGES = {
    D + "IsHeatZero": [(13, 50)],
    D + "IsSystem": [(61, 103)],
    P + "IsHeatThH": [(99, 133), (182, 216)],
    P + "EisensteinSeriesOfSchwartzIsHolomorphic": [(156, 207), (213, 242)],
    P + "IsHeatSwd": [(43, 66)],
    P + "PolyDerivPairingEqZeroOfIsHeat": [(167, 184), (250, 290)],
    P + "InvariantPolyDerivKillsDoubledHeatSolution": [(261, 288), (293, 321), (333, 359)],
    P + "KernelIdentity": [(279, 301), (311, 341)],
}


def diagnostics():
    z, c, d, t = sp.symbols("z c d t")
    n = 5
    x = sp.symbols("x:5")
    y = sp.symbols("y:5")
    a = c*z+d
    f = a**(-n)*sp.exp(-t*c/a*sum(u*v for u,v in zip(x,y)))
    lap = sum(sp.diff(f,u,v) for u,v in zip(x,y))
    assert sp.simplify((lap-t*sp.diff(f,z))/f) == 0
    zero = {u:0 for u in x+y}
    assert sp.simplify(lap.subs(zero)/f.subs(zero)+n*t*c/a) == 0
    # A holomorphic heat solution can have zero Jacobi value and a
    # nonzero uncontracted derivative. The proof only kills invariants.
    f0 = x[0]
    assert sum(sp.diff(f0,u,v) for u,v in zip(x,y)) == t*sp.diff(f0,z) == 0
    assert f0.subs(zero) == 0 and sp.diff(f0,x[0]).subs(zero) == 1
    t00,t01,t10,t11,b0,b1=sp.symbols("t00 t01 t10 t11 b0 b1")
    mat=sp.Matrix([[t00,t01],[t10,t11]])
    b=sp.Matrix([b0,b1])
    g=sp.eye(3)
    v=mat.inv()*b
    g[0,2],g[1,2]=v
    xx=sp.Matrix([[1,0],[0,1],[0,0]])
    yy=mat.row_join(b)
    assert g*xx == xx
    assert (yy*g.inv()-mat.row_join(sp.zeros(2,1))).applyfunc(sp.simplify) == sp.zeros(2,3)
    return {"scalar_heat_equation_n":n,"symbol_t_substitutes_2_pi_i":True,
            "determinant_exponent_term_retained":True,
            "zero_value_does_not_kill_uncontracted_jets":True,
            "generic_dense_rank_normal_form_n3_r2":True,
            "scope":"Exact symbolic identities, not an all-rank computational proof"}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline",action="store_true")
    args=parser.parse_args()
    auth.RANGES=RANGES
    sources=auth.provenance(args.offline)
    paths=[f"paper/shared/{STEM}.tex",f"notes/{STEM}.md",f"scripts/{STEM}.py"]
    record={"status":"PASS","classification":"closed exact supplier; independent mathematical review recorded",
            "frontier":"Actual invariant harmonic heat comparison for admitted class-sum differences in the original n>4r range",
            "artifacts":{p:auth.sha((auth.ROOT/p).read_bytes()) for p in paths},
            "sources":sources,"diagnostics":diagnostics(),
            "independent_review":{"reviewer":"integrating agent",
              "checked":["original IsHeatZero convention","actual doubled dimensions", "KernelIdentity lines 279-284", "matrix heat signs", "invariant polynomial argument"],
              "correction":"Constant-term contribution vanishes, not necessarily the constant coefficient itself"},
            "scope":{"actual_series_and_gaussian":True,"original_scalars_preserved":True,
                     "no_general_invariant_theory_input":True,"ordinary_rh_and_dirichlet_grh":True,
                     "whole_node_closed":False,"finite_schwartz_system_supplied_by_this_file":False,
                     "no_uniform_global_norm_claim":True,"no_lean_build":True}}
    out=auth.ROOT/f"certificates/{STEM}.json"
    out.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":"PASS","source_files":len(sources),"output":str(out.relative_to(auth.ROOT))}))


if __name__=="__main__":
    main()
