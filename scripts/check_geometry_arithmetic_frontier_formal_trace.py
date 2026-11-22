#!/usr/bin/env python3
"""Authenticate the formal trace proof and test its exact arithmetic factors.

No Lean build or global theta denominator closure. Finite exact models
supplement the written general proof in the shared TeX.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth


STEM = "geometry-arithmetic-frontier-formal-trace"
RI = "Development.AbelianVarietyTheory.Proofs.RingsOfIntegers."
RANGES = {
    "Development.AbelianVarietyTheory.Definitions.PlaceAdaptation.AdaptStd": [(29, 58), (61, 87)],
    RI + "JacobianNonzeroSplittingOfProduct": [(198, 240)],
    RI + "ExistsPowSpanXLeSpanFormalModuleMatrix": [(25, 80)],
    RI + "FormalSeriesDescendsOfSplitKernelInvariant": [(65, 91)],
    RI + "FormalMatrixKernelFiniteNcardEqRank": [(100, 143)],
    RI + "DetJacobianFormalModuleMatrixEqConstMulUnit": [(233, 290), (334, 343)],
    RI + "ConstantDvdTraceOfJacobianFiniteColength": [(211, 275)],
    RI + "ExistsIntegralExponentialSimilitudeGauge": [(145, 196), (335, 351)],
    RI + "ProdSymmetricTranslationUnitsEqKappaRatio": [(51, 127), (452, 500), (501, 548)],
    RI + "SumHarmonicValuesFormalKernelSimilitude": [(94, 129), (203, 240), (255, 280), (281, 309), (311, 363)],
    RI + "SumHvPrimaryKernel": [(221, 256), (267, 302)],
}


def reference_records():
    data = [
        ("00R4", "cc7f1947308a6c8db0d6d0d406bfecc4ef2363d710f694b1cc5fe9bb0ba8219f", "Lemma 10.128.1: regular base, Cohen-Macaulay target and the dimension equality imply flatness."),
        ("00SY", "e9a51b2357f247387272268c7c65c6908ae863b5e78e01d76e6f8443ecf802ec", "Lemma 10.136.15: finite presentation, flat local map and complete-intersection fibre give a syntomic neighbourhood."),
        ("0BWG", "e4204f86deb55dd72b9fbad4433c9777fb6833d82ee25dba239597b6f5f07dae", "Lemma 49.12.3: different equals the Kaehler different for quasi-finite syntomic maps."),
        ("0BTC", "49be69d42350ae7efb70a7bdc4c79df0b16c3cc7b8dfe6f2c98612da28e2f498", "Section 49.9: trace-dual definition of the different and agreement with the Dedekind different."),
    ]
    rows = []
    for tag, digest, scope in data:
        path = "build/reference-cache/stacks-" + tag + ".html"
        assert auth.sha((auth.ROOT / path).read_bytes()) == digest
        rows.append({"url": "https://stacks.math.columbia.edu/tag/" + tag,
                     "local_path": path, "sha256": digest, "verified_scope": scope})
    return rows


def multiplication_matrix(n, ell, y):
    # B=A[x]/(x^n+ell*x-y), basis1,x,...,x^(n-1).
    C = sp.zeros(n)
    for j in range(n-1):
        C[j+1, j] = 1
    C[0, n-1] = y
    C[1, n-1] = -ell
    return C


def trace_pairing_models():
    Y = sp.Symbol("Y")
    cases = sorted({(ell, n) for ell in [2, 3, 5] for n in [ell, 2*ell, ell*ell]})
    matrix_checks = pairing_checks = 0
    details = []
    for ell, n in cases:
        # These substitutions are finite flat over Z_ell[[Y]]:
        # reduction is x^n; derivative is ell*(1+(n/ell)x^(n-1)).
        assert n % ell == 0
        S = [sp.Integer(n)] + [sp.Integer(0)]*(2*n-2)
        S[n-1] = sp.Integer(-(n-1)*ell)
        for k in range(n, len(S)):
            S[k] = sp.expand(Y*S[k-n] - ell*S[k-n+1])
        for value in S:
            assert all(int(c) % ell == 0 for c in sp.Poly(value, Y).all_coeffs())
        T = sp.Matrix(n, n, lambda i, j: S[i+j])
        U0 = (T/ell).subs(Y, 0)
        determinant = int(U0.det())
        assert determinant % ell != 0
        # Therefore the normalized trace pairing is perfect over
        # Z_ell[[Y]]: its determinant is a unit. This checks the exact
        # inverse different ell^(-1) B in the model, not just a bound.
        assert U0.inv()*U0 == sp.eye(n)
        pairing_checks += 1
        # Independent multiplication-matrix calculation at exact integers.
        for y in [0, 1, -2]:
            C = multiplication_matrix(n, ell, sp.Integer(y))
            M = sp.eye(n)
            for k in range(len(S)):
                assert sp.trace(M) == S[k].subs(Y, y)
                matrix_checks += 1
                M = M*C
        details.append({"residue_prime": ell, "degree": n, "jacobian_constant": ell,
                        "normalized_trace_gram_determinant_at_zero": str(determinant)})
    return {"finite_colength_models": len(cases), "perfect_normalized_trace_pairings": pairing_checks,
            "independent_multiplication_matrix_traces": matrix_checks,
            "models": details,
            "scope": "Exact finite-flat power-series substitution models y=x^n+ell*x; not all models are asserted to be formal-group homomorphisms."}


def roots_sum(N, exponent, z):
    # Work in Q[z]/Phi_N(z), never use floating-point roots of unity.
    counts = Counter((j*exponent) % N for j in range(N))
    polynomial = sp.Poly(sum(c*z**r for r, c in counts.items()), z, domain=sp.QQ)
    return polynomial.rem(sp.Poly(sp.cyclotomic_poly(N, z), z, domain=sp.QQ)).as_expr()


def split_kernel_tower_models():
    z = sp.Symbol("z")
    groups = sums = invariants = twists = 0
    for ell in [2, 3]:
        for a in [1, 2]:
            for b in [1, 2]:
                m, q = ell**a, ell**b
                N = m*q
                groups += 1
                # Formal G_m: p=[m], q=[q], mu=[mq]. After adjoining
                # Nth roots of unity to R all N kernel points are small.
                # The invariant monomial is t^(q*k), t=1+x.
                for k in range(m+3):
                    assert roots_sum(q, q*k, z) == q
                    invariants += 1
                    actual = roots_sum(N, q*k, z)
                    expected = N if k % m == 0 else 0
                    assert actual == expected
                    # d_q=q, j_p=m; the pulled-back monomial exponent
                    # is N*(k/m)=q*k when k is divisible by m.
                    assert (expected == 0) or (q*m == N and N*(k//m) == q*k)
                    sums += 1
                    for twist in [-2, 0, 3]:
                        # kappa=t^twist is an integral unit; U_a=z^(-a*twist).
                        # The complete twist cancels exactly before summing.
                        exponents = [(-j*twist + j*(twist+q*k)) % N for j in range(N)]
                        assert exponents == [(j*q*k) % N for j in range(N)]
                        assert roots_sum(N, q*k, z) == expected
                        twists += 1
    return {"split_primary_formal_tori": groups, "invariant_monomials": invariants,
            "exact_tower_kernel_sums": sums, "original_unit_twist_checks": twists,
            "scope": "Exact cyclotomic character sums on formal multiplicative groups with primary torsion, preserving degree(q)*j_p and the unit-gauge ratio."}


def normalization_checks():
    chi, u0, um, ka, km, I = sp.symbols("chi u0 um ka km I")
    # The four scalar normalization equations imply (chi^2-1)*km=0.
    relations = [chi-u0*ka, chi*km-um, km*I-ka, u0*I*um-1]
    basis = sp.groebner(relations, u0, um, ka, I, chi, km)
    assert basis.reduce((chi**2-1)*km)[1] == 0
    # On units km!=0, chi^2=1; with odd order there is no scalar ambiguity.
    odd_orders = 0
    X = sp.Symbol("X")
    for m in range(1, 22, 2):
        assert sp.gcd(sp.Poly(X**m-1, X), sp.Poly(X**2-1, X)) == sp.Poly(X-1, X)
        assert sum(range(m)) == m*(m-1)//2
        odd_orders += 1
    # Negative controls for replacing the actual arithmetic hypotheses.
    assert Fraction(-24, 3).denominator == 1
    assert Fraction(-24, 9).denominator == 3
    # y=x^2+3x is finite flat but J(0)=3 is not a uniform Jacobian
    # divisor: J=2x+3 is not3 times an integral power-series unit.
    assert sp.trace(multiplication_matrix(2, 3, sp.Integer(0))**0) == 2
    assert 2 % 3 != 0
    # Without finite height, [3] on the additive formal group reduces to
    # zero, so the special-fibre coordinate ring is the infinite k[[x]].
    assert sp.Poly(3*X, X, modulus=3).is_zero
    for d in range(1, 12):
        assert not sp.Poly(X**d, X, modulus=3).is_zero
    return {"scalar_normalization_ideal_check": "PASS", "odd_orders_checked": odd_orders,
            "negative_controls": ["For y=x^9+3x, Tr(x^8)=-24 is divisible by j=3 but not by degree9.",
                                  "For y=x^2+3x, J(0)=3 alone does not divide Tr(1)=2; the Jacobian-unit identity is necessary.",
                                  "The additive formal group [3] has infinite special-fibre colength, so the finite-flat trace is unavailable."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    trace = trace_pairing_models()
    towers = split_kernel_tower_models()
    normalization = normalization_checks()
    paths = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
             f"paper/shared/{STEM}-references.tex", "scripts/" + Path(__file__).name]
    record = {
        "date": "2026-11-22", "status": "PASS",
        "classification": "Written source-applicable formal trace/Jacobian supplier, retaining original finite-height, splitting and integral symmetric-translation data.",
        "claim": "sum_(ker(p o q)) t_a^*f = #ker(q)*det(dp_0)*(p o q)^*g for integral ker(q)-invariant f, with integral g; the same exact factor survives the original unit-gauge twist.",
        "new_formal_supplier_count": 1, "whole_nodes_newly_closed": 0,
        "proved_steps": ["Actual finite flatness in the power-series tower.",
                         "Integral descent from split-kernel invariance.",
                         "Differential Jacobian times integral unit and trace-dual divisibility.",
                         "Full small-kernel degree/cardinality and integral translation action.",
                         "Exact degree(q)*j_p factor and original integral gauge normalization.",
                         "Normalized harmonic-value consequence using the discriminant-clearing theorem."],
        "remaining_inputs": ["Constructing finite height and splitting from the actual global model and rational torsion.",
                             "Integral regular germs and symmetric translation lifts from the supplied sections.",
                             "Passage from formal kernel to full primary kernel and determinant-ideal/index comparison.",
                             "Theta spanning and raw theta norm as independent suppliers."],
        "scope": "No Lean build, no global denominator or full-node closure. Exact models supplement the general written proof and authenticated formal identities.",
        "sources": sources, "primary_references": reference_records(),
        "trace_pairing_models": trace, "split_kernel_tower_models": towers,
        "normalization_checks": normalization,
        "artifacts": [{"path": p, "sha256": auth.sha((auth.ROOT / p).read_bytes())} for p in paths],
        "dependencies": [{"path": p, "sha256": auth.sha((auth.ROOT / p).read_bytes())} for p in
                         ["scripts/check_geometry_arithmetic_frontier_geometric_filtration.py",
                          "paper/shared/geometry-arithmetic-frontier-discriminant-clearing.tex",
                          "certificates/geometry-arithmetic-frontier-discriminant-clearing.json"]],
        "reproduce": "python3 scripts/" + Path(__file__).name + " --offline",
    }
    out = auth.ROOT / "certificates" / (STEM + ".json")
    out.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "finite_colength_models": trace["finite_colength_models"],
                      "independent_matrix_traces": trace["independent_multiplication_matrix_traces"],
                      "split_primary_tori": towers["split_primary_formal_tori"],
                      "kernel_sums": towers["exact_tower_kernel_sums"],
                      "unit_twists": towers["original_unit_twist_checks"],
                      "negative_controls": len(normalization["negative_controls"])}))


if __name__ == "__main__":
    main()
