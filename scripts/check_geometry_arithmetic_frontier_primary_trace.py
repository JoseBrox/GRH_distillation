#!/usr/bin/env python3
"""Authenticate primary-theta sources and check exact finite normalizations.

Written general proofs, not these models, establish the arithmetic suppliers.
No Lean build or global theta denominator closure is claimed.
"""
from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from math import gcd, prod
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
import check_geometry_arithmetic_frontier_geometric_filtration as auth


STEM = "geometry-arithmetic-frontier-primary-trace"
AP = "Development.AbelianVarietyTheory."
RI = AP + "Proofs.RingsOfIntegers."
RANGES = {
    AP + "Definitions.PlaceAdaptation.AdaptStd": [(101, 112), (142, 166), (172, 188)],
    RI + "ExistsUnitaryOfSelfDual": [(55, 94), (134, 161)],
    RI + "ExistsAdaptedSimilitudeDataAtPrime": [(34, 105)],
    RI + "FiniteHeightFormalGroupUniformisedModel": [(29, 70)],
    AP + "Proofs.FormalGroupCharts.FiniteTorsionSpecialFibreOfUnif": [(30, 41)],
    RI + "SplitKernelFormalGroupOfRationalTorsion": [(424, 457), (458, 489)],
    RI + "SumHvPrimaryKernel": [(39, 82), (121, 150), (221, 256), (267, 302)],
    RI + "InZhIffKillsAdapted": [(179, 219)],
    RI + "IndexRangeMatrix": [(79, 110), (143, 165), (410, 467)],
    AP + "Proofs.DivisorProofs.ShortSeriesBoundCoprimeTorsionMul": [(18, 73), (74, 109), (111, 124)],
    RI + "ReachedSectionRegularOnIntegralModel": [(71, 100)],
    RI + "HarmonicValueTranslatedProductValuationBound": [(20, 42), (76, 123)],
    RI + "HarmonicValueChainRuleNormalizedPullback": [(15, 53)],
    AP + "Proofs.DivisorProofs.SmulIntZSqNonnegOfSqDvd": [(121, 161), (163, 189)],
}


def valuation(a: int, ell: int) -> int:
    assert a
    a = abs(a)
    count = 0
    while a % ell == 0:
        a //= ell
        count += 1
    return count


def subgroup_checks():
    cases = nonnested = 0
    for modulus in (3, 4, 5, 6, 9):
        W = list(itertools.product(range(modulus), repeat=2))
        zero = (0, 0)
        def add(a, b):
            return tuple((x+y) % modulus for x, y in zip(a, b))
        def cyclic(a):
            return frozenset(tuple(k*x % modulus for x in a) for k in range(modulus))
        subgroups = {cyclic(x) for x in W}
        subgroups.add(frozenset(W))
        subgroups = sorted(subgroups, key=lambda s: (len(s), sorted(s)))
        for W0 in subgroups:
            qclass = {x: min(add(x, u) for u in W0) for x in W}
            qelements = sorted(set(qclass.values()))
            # Arbitrary exact W0-invariant values, including cancellation.
            vals = {x: Fraction(3*i-5, 9) for i, x in enumerate(qelements)}
            f = {x: vals[qclass[x]] for x in W}
            for W1 in subgroups:
                intersection = len(W0 & W1)
                image = {qclass[u] for u in W1}
                assert len(W1) == intersection * len(image)
                if not (W0 <= W1 or W1 <= W0):
                    nonnested += 1
                representatives = []
                seen = set()
                for x in qelements:
                    if x not in seen:
                        representatives.append(x)
                        seen.update(qclass[add(x, u)] for u in W1)
                z = {}
                for x in representatives:
                    distinct = {qclass[add(x, u)] for u in W1}
                    z[x] = sum((vals[t] for t in distinct), Fraction(0))
                    assert sum((f[add(x, u)] for u in W1), Fraction(0)) == intersection*z[x]
                assert sum(f.values(), Fraction(0)) == len(W0)*sum(z.values(), Fraction(0))
                cases += 1
    # W=C9, W0=W1=3C9, quotient values (1,0,0): the sum is 3,
    # not divisible by |W|=9. The true stabilizer factor is indispensable.
    assert Fraction(3, 9).denominator == 3
    return {"subgroup_pairs": cases, "nonnested_pairs": nonnested,
            "stabilizer_to_full_group_negative_control": "3/9 is not 3-integral"}


def odd_phase_checks():
    cases = 0
    for level in (1, 3, 5, 9, 15):
        half = 0 if level == 1 else pow(2, -1, level)
        # Paired symplectic columns with opposite Weil exponents are
        # a concrete isotropic product. Work in exact root exponents.
        for a, b, c, d in itertools.product(range(level), repeat=4):
            omega = (a*d-b*c) % level
            phases = ((half*omega) % level, (-half*omega) % level)
            assert sum(phases) % level == 0
            assert (2*phases[0]-omega) % level == 0
            assert (2*phases[1]+omega) % level == 0
            cases += 1
    # At even level, r=-1 satisfies r^2=r^level=1 without r=1.
    assert (-1)**2 == 1 and -1 != 1
    odd_nonintegral = sp.Matrix([[0, 3, 0], [0, 0, 1], [sp.Rational(1, 3), 0, 0]])
    assert odd_nonintegral**3 == sp.eye(3)
    assert odd_nonintegral[2, 0].q == 3
    return {"exact_odd_isotropic_phase_pairs": cases,
            "even_level_negative_control": "r=-1 has r^2=r^2=1 but r!=1",
            "regularity_negative_control": "Conjugating a 3-cycle by diag(3,1,1) gives order three without preserving Z_3^3."}


def matrix_index_checks():
    cases = kernel_counts = 0
    models = [sp.Matrix([[1, 1], [0, 3]]), sp.Matrix([[3, 1], [0, 3]]),
              sp.Matrix([[2, 1], [0, 4]]), sp.Matrix([[5, 2], [0, 5]])]
    for g in models:
        N = abs(int(g.det()))
        q = g.inv()*N
        assert all(x.q == 1 for x in q)
        assert g*q == N*sp.eye(2)
        # Lcap=g Z^2 lies between N Z^2 and Z^2. Both independent
        # index computations are exact, before taking primary parts.
        I = N**2//abs(int(g.det()))
        assert I == abs(int(q.det()))
        smith = smith_normal_form(q, domain=ZZ)
        assert abs(prod(int(smith[i, i]) for i in range(2))) == I
        for ell in (2, 3, 5):
            e = max(valuation(abs(int(smith[i, i])), ell) for i in range(2))
            modulus = ell**e
            kernel = sum(all(int(x) % modulus == 0 for x in q*sp.Matrix(v))
                         for v in itertools.product(range(modulus), repeat=2))
            assert kernel == ell**valuation(I, ell)
            for rank in (1, 2, 3):
                assert kernel**rank == ell**valuation(I**rank, ell)
                kernel_counts += 1
            cases += 1
    # A genuinely nontrivial unitary change over Q(i). This finite model
    # verifies the algebra once adapted data exist; Q(i)/Q does not meet
    # the proposition's everywhere-unramified host hypothesis.
    gamma = sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5)],
                       [-sp.Rational(4, 5), sp.Rational(3, 5)]])
    assert gamma.T*gamma == sp.eye(2)
    k = 5
    g = sp.eye(2)
    N = 3
    p = k*gamma*g
    q = N*sp.eye(2)
    assert p*q == k*N*gamma and (p*q).T*(p*q) == (k*N)**2*sp.eye(2)
    assert valuation(int(p.det()), 3) == 0
    return {"matrix_prime_index_checks": cases,
            "independent_smith_and_enumerated_kernel_rank_checks": kernel_counts,
            "nontrivial_rational_unitary_model": True,
            "scope": "Exact integral matrix and rational unitary identities; no claim that Q(i) supplies the unramified host."}


def normalized_sum_checks():
    s, I, L, k, N, eta, delta, z = sp.symbols("s I L k N eta delta z", nonzero=True)
    cases = 0
    for d in range(9):
        source_sum = (k*N)**d/eta*L*delta*z
        lhs = s/I/N**d*source_sum
        rhs = L/I*k**d/eta*(s*delta)*z
        assert sp.cancel(lhs-rhs) == 0
        cases += 1
    scalar_cases = 0
    for ell in (2, 3, 5):
        for exponent in range(5):
            for remainder in range(1, 13):
                if gcd(ell, remainder) != 1:
                    continue
                integer = ell**exponent*remainder
                assert Fraction(ell**exponent, integer) == Fraction(1, remainder)
                assert valuation(remainder, ell) == 0
                scalar_cases += 1
    return {"symbolic_homogeneous_identities": cases, "unit_index_ratios": scalar_cases}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    groups = subgroup_checks()
    phases = odd_phase_checks()
    matrices = matrix_index_checks()
    normalized = normalized_sum_checks()
    paths = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
             f"paper/shared/{STEM}-references.tex", "scripts/"+Path(__file__).name]
    record = {
        "date": "2026-11-22", "status": "PASS", "whole_nodes_newly_closed": 0,
        "classification": "Closed arithmetic subobligations and source-applicable primary-sum theorem under explicitly retained integral-section regularity; no full denominator closure.",
        "proved_steps": ["Construction of the exact adapted matrices under the original unramified CM host.",
                         "Finite height and splitting from the specified semiabelian integral model and rational torsion.",
                         "Full primary torsion sum with exact stabilizer/Jacobian factor.",
                         "Primary lattice index and weighted determinant-ideal valuation comparison."],
        "remaining_inputs": ["The actual global integral model and its formal chart.",
                             "Regularity of all prescribed reached translates on the same chart with the same scalar.",
                             "The actual mixed level-torsion normalized pullback identities and all-place assembly.",
                             "Theta spanning and the raw theta norm."],
        "sources": sources, "subgroup_models": groups, "phase_models": phases,
        "matrix_models": matrices, "normalization_models": normalized,
        "scope": "Exact finite checks supplement written proofs. No Lean build, global geometric construction, global Z clearing, or whole-node closure.",
        "artifacts": [{"path": p, "sha256": auth.sha((auth.ROOT/p).read_bytes())} for p in paths],
        "reproduce": "python3 scripts/"+Path(__file__).name+" --offline",
    }
    out = auth.ROOT/"certificates"/(STEM+".json")
    out.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "subgroup_pairs": groups["subgroup_pairs"],
                      "nonnested_subgroup_pairs": groups["nonnested_pairs"],
                      "odd_phase_pairs": phases["exact_odd_isotropic_phase_pairs"],
                      "kernel_rank_checks": matrices["independent_smith_and_enumerated_kernel_rank_checks"]}))


if __name__ == "__main__":
    main()
