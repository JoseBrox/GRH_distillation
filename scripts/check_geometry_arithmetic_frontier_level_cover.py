#!/usr/bin/env python3
"""Authenticate the actual level-cover supplier and its nonreduced algebra edge.

Finite symbolic checks are normalization/edge diagnostics, not a substitute
for the all-algebra formal construction or the finite etale cover proof.
"""
from __future__ import annotations

import argparse
import json
from math import factorial

import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth


STEM = "geometry-arithmetic-frontier-level-cover"
P = "Formalism.LocalToGlobal.ProjectiveLattices."
A = "Development.AbelianVarietyTheory."
RANGES = {
    P + "IsCombAt": [(67, 85)],
    P + "IsThRule": [(20, 26)],
    P + "ThGerm": [(189, 217)],
    P + "ThShort": [(114, 177), (181, 189)],
    P + "AllTest": [(9, 14)],
    A + "Proofs.CuspFormEvaluations.GlobalBasisAlgebra": [(22, 58)],
    A + "Proofs.CuspFormEvaluations.ExistsBiextensionChartWithGermsFramedPoint": [(37, 54)],
    A + "Proofs.CuspFormEvaluations.ExistsIsNab": [(19, 43)],
    A + "Proofs.CuspFormEvaluations.FramedPointsLiftToLevelCoverStatement": [(12, 14)],
    A + "Proofs.UnitaryExistence.FramedPointReducedFromTestRing": [(227, 288)],
    A + "Proofs.UnitaryExistence.ExistsDeltaDatumHigherLevel": [(72, 94)],
    A + "Definitions.Divisors.NormNegCmConstantEqAtAllEmbeddings": [(187, 208), (484, 499)],
}


def nilpotent_checks():
    eps, x, y, z, t = sp.symbols("eps x y z t")

    def red(p, n=2):
        q = sp.Poly(sp.expand(p), eps)
        return sp.expand(sum(q.nth(i)*eps**i for i in range(n)))

    def group(a, b):
        return red(a+b-2*eps*a*b)

    log = lambda a: red(a+eps*a*a)
    exp = lambda a: red(a-eps*a*a)
    assert red(group(group(x, y), z)-group(x, group(y, z))) == 0
    assert red(log(group(x, y))-log(x)-log(y)) == 0
    assert red(exp(log(x))-x) == 0
    assert red(log(exp(x))-x) == 0
    assert red(group(exp(x), exp(y))-exp(x+y)) == 0

    cases = []
    for m in range(9):
        f, series = x**m, 0
        for j in range(m+2):
            series += f.subs(x, 0)*t**j/factorial(j)
            f = red((1-2*eps*x)*sp.diff(f, x))
        assert red(series-exp(t)**m) == 0
        assert red(series).subs(eps, 0) == t**m
        cases.append(m)

    # The two CM embeddings remain separated by a unit even with nilpotents.
    rt = sp.sqrt(-7)
    w, wb = (1+rt)/2, (1-rt)/2
    change = sp.Matrix([[1, eps], [0, 1]])
    action = change*sp.diag(w, wb)*change.inv()
    one = sp.eye(2)
    plus, minus = (action-wb*one)/(w-wb), (w*one-action)/(w-wb)
    clean = lambda m: m.applyfunc(lambda p: sp.simplify(red(p)))
    for mat in [plus*plus-plus, minus*minus-minus, plus*minus,
                plus+minus-one, action*plus-w*plus, action*minus-wb*minus]:
        assert clean(mat) == sp.zeros(2)
    assert clean(plus*change[:, 0]-change[:, 0]) == sp.zeros(2, 1)
    assert clean(minus*change[:, 1]-change[:, 1]) == sp.zeros(2, 1)

    # The addition homotopy works over Q[eps]/eps^3, including nilpotent terms.
    cocycles = 0
    for degree in range(2, 8):
        h = (1+eps+3*eps**2)*(1+z+z*z)*x**degree
        c = red(h+h.subs(x, y)-h.subs(x, x+y), 3)
        one_form = -sp.diff(c, y).subs(y, 0)
        recovered = red(sp.integrate(x*one_form.subs(x, t*x), (t, 0, 1)), 3)
        assert red(recovered-h, 3) == 0
        cocycles += 1

    return {
        "nonreduced_base": "Q[eps]/(eps^2), and Q[eps]/(eps^3) for gauge homotopy",
        "group_law": "x+y-2*eps*x*y",
        "logarithm": "x+eps*x^2",
        "formal_exponential": "t-eps*t^2",
        "invariant_derivation": "(1-2*eps*x)*d/dx",
        "ordinary_derivative_factorials": "exact PASS",
        "tested_monomial_degrees": cases,
        "nonflat_quotient_eps_to_zero": "exact PASS",
        "original_d7_quadratic_CM_idempotents": "exact PASS",
        "nilpotent_parameter_cocycle_homotopies": cocycles,
    }


def references():
    path = "build/reference-cache/stacks-01ZM.html"
    expected = "f24dc66991adbc1a0c758cb5bf409ca15f4fbf78c306608006471fa4a3aa88ce"
    assert auth.sha((auth.ROOT/path).read_bytes()) == expected
    return [{"path": path, "sha256": expected,
             "url": "https://stacks.math.columbia.edu/tag/01ZM",
             "verified_statement": "32.10.1(2): finite-presentation morphisms descend through qcqs inverse systems with affine transitions",
             "application": "An S-point of the actual finite-presentation frame scheme descends to a finitely generated coefficient subalgebra"}]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    src = auth.provenance(args.offline)
    checks = nilpotent_checks()
    refs = references()
    paths = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", "scripts/check_geometry_arithmetic_frontier_level_cover.py"]
    cert = {
        "status": "PASS", "date": "2026-11-23",
        "classification": "closed exact supplier, independently reviewed",
        "claim": "Original DeltaDat.IsLev, IsNab over every coefficient algebra, AllTest, and exact harmonic framed base change",
        "whole_nodes_newly_closed": 0,
        "sources": src, "primary_references": refs, "checks": checks,
        "files": [{"path": p, "sha256": auth.sha((auth.ROOT/p).read_bytes())} for p in paths],
        "scope": "Human proof establishes all-algebra formal geometry and the actual finite etale cover. Symbolic examples verify the nonreduced and nonflat edges only.",
        "not_claimed": ["Full Deep.Good or Member supplier", "Component-field or degree bound",
                        "Uniform global theta norm", "W10 completion", "Lean build"],
    }
    path = auth.ROOT / "certificates" / f"{STEM}.json"
    path.write_text(json.dumps(cert, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "PASS", "sources": len(src),
                      "monomial_cases": len(checks["tested_monomial_degrees"]),
                      "nilpotent_cocycles": checks["nilpotent_parameter_cocycle_homotopies"],
                      "primary_references": len(refs)}))


if __name__ == "__main__":
    main()
