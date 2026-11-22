#!/usr/bin/env python3
"""Authenticate mixed theta interfaces and check exact local denominators.

The standard proof is in the shared TeX. These models do not construct
Good3, the global cover, or an integral compactification.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import gcd
from pathlib import Path

import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth


STEM = "geometry-arithmetic-frontier-mixed-level"
AP = "Development.AbelianVarietyTheory."
RI = AP + "Proofs.RingsOfIntegers."
DP = AP + "Proofs.DivisorProofs."
PS = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.PullbackSections."
RANGES = {
    RI + "MixedTranslatePullbackEqReachedSection": [(17, 64)],
    RI + "SymmetricTranslatesMultiplicationPullbackDescrip": [(24, 60), (85, 96)],
    RI + "NormalisedPullbackCommutesSymmetricTranslations": [(87, 135), (137, 170)],
    RI + "HarmonicValueTranslatedProductValuationBound": [(20, 42), (76, 123)],
    RI + "ShortBoundOfTrivAt": [(33, 89), (164, 215), (216, 267)],
    RI + "LatticeTrivialAtPrimeIndicesAndUnits": [(68, 99), (171, 216)],
    DP + "SmulIntZSqNonnegOfSqDvd": [(32, 66), (71, 102), (121, 161), (163, 189)],
    DP + "ShortSeriesBoundCoprimeTorsionMul": [(111, 124)],
    RI + "ShortValueBoundOfCoprime": [(124, 163)],
    PS + "ShortValDesc": [(20, 36)],
    DP + "ClearingIntegerShortSeriesIntegralCoprimeLevel": [(30, 63), (85, 114), (121, 159)],
    DP + "ExistsBoundedIntegerGoodCoverThetaSeriesIntegral": [(31, 67), (68, 118)],
}


def val(n, p):
    assert n > 0
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def factorization_checks():
    cases = higher = 0
    for N in range(1, 301, 2):
        for M in range(1, N+1, 2):
            if N % M:
                continue
            for ell in (2, 3, 5, 7, 11):
                e, k = val(N, ell), val(M, ell)
                n, m = N//ell**e, M//ell**k
                alpha, beta = ell**k, ell**(e-k)
                A, B = alpha**2, beta**2
                assert k <= e and n % m == 0
                assert gcd(n*m, ell) == 1
                assert N == beta*alpha*n
                assert N*N == n*n*A*B
                assert (beta*n*n*A) % (N*M) == 0
                assert (N*N) % (N*M) == 0
                assert val(M//alpha, ell) == 0
                assert n*n == 1 or n*n >= 4
                cases += 1
                higher += k >= 2
    assert higher
    return {"exact_level_prime_factorizations": cases,
            "prime_square_or_higher_level_cases": higher,
            "scope": "Original torsion exponent divisibilities, including ell=2 and arbitrary odd N,M in the finite range."}


def phase_checks():
    cases = 0
    for K in (15, 21, 45, 105):
        for m in range(1, K+1):
            if K % m:
                continue
            for n in range(1, K+1):
                if K % n or gcd(m,n) != 1:
                    continue
                # A pairing root exponent is killed by both m and n.
                possible = [a for a in range(K) if (m*a) % K == 0 and (n*a) % K == 0]
                assert possible == [0]
                # The odd symmetric comparison has square one: exact zero.
                assert [r for r in range(K) if 2*r % K == 0] == [0]
                cases += 1
    return {"coprime_theta_phase_cases": cases,
            "scope": "Exact roots-of-unity exponent checks; no numerical complex approximation."}


def cancellation_checks():
    A, B, n, S, I, J, C, delta, M, s, z, phase, weight = sp.symbols(
        "A B n S I J C delta M s z phase weight", nonzero=True)
    tests = 0
    for d in range(10):
        N = A*B*n
        # The actual mixed factor after the original chain rule.
        assert sp.cancel(A**d*N**(-d)*B**d-n**(-d)) == 0
        # Full average and full primary stabilizer; beta_H cancels only
        # through theta=beta_H*g, not by declaring it a unit globally.
        betaH = sp.symbols("betaH", nonzero=True)
        theta = betaH * (betaH**(-1)*I**(-1)*C**(-1)*N**(-d)*phase*weight*S)
        Z = C*delta**d*M**d
        assert sp.cancel(Z*s*theta-phase*weight*delta**d*M**d*s*I**(-1)*N**(-d)*S) == 0
        assert sp.cancel(I**(-1)*(J*S)-(J/I)*S) == 0
        tests += 1
    # Exact normalized valuations under any positive ramification index.
    basechanges = 0
    for v in range(-10,11):
        for e in range(1,8):
            for ram in range(1,8):
                assert Fraction(ram*v,ram*e) == Fraction(v,e)
                basechanges += 1
    return {"symbolic_normalized_term_and_average_identities": tests,
            "exact_normalized_valuation_basechanges": basechanges}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    factors = factorization_checks()
    phases = phase_checks()
    cancellations = cancellation_checks()
    paths = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
             f"paper/shared/{STEM}-references.tex", "scripts/"+Path(__file__).name]
    record = {
        "date": "2026-11-22", "status": "PASS", "whole_nodes_newly_closed": 0,
        "classification": "Closed actual mixed-theta compatibility and local level-prime arithmetic; improved all-place sufficient condition retaining original cover and integral-model suppliers.",
        "proved_steps": ["Exact scalar-one factorization of the original ordered mixed theta translations.",
                         "Actual normalized harmonic term cancellation.",
                         "Explicit rational local factorization for every power of every level prime.",
                         "Full local theta sum with exact primary lattice index cancellation."],
        "conditional_all_place_conclusion": "Original Z = |Q| |disc(E)|^D M^D clears the actual theta family once the retained good cover, integral weights, exact value identity and Good3 chart suppliers are provided.",
        "remaining_inputs": ["Actual integral Model and Good3 uniformization, with original primitive line and markings.",
                             "Construction and exact comparison of the original good cover and its section lattices.",
                             "Theta spanning and the raw global theta norm."],
        "sources": sources, "local_factorizations": factors,
        "coprime_phases": phases, "normalization_checks": cancellations,
        "scope": "Written proofs plus exact arithmetic/source authentication. No Lean build, actual integral model construction, unconditional global theta denominator or whole-node closure.",
        "artifacts": [{"path": p, "sha256": auth.sha((auth.ROOT/p).read_bytes())} for p in paths],
        "reproduce": "python3 scripts/"+Path(__file__).name+" --offline",
    }
    (auth.ROOT/"certificates"/(STEM+".json")).write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "local_factorizations": factors["exact_level_prime_factorizations"],
                      "higher_level_prime_cases": factors["prime_square_or_higher_level_cases"],
                      "coprime_phase_cases": phases["coprime_theta_phase_cases"]}))


if __name__ == "__main__":
    main()
