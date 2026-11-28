#!/usr/bin/env python3
"""Exact finite checks for the determinant-period arithmetic chapter.

These checks verify finite identities and denominator exponents only.
They do not evaluate an automorphic period or establish its nonvanishing.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def multiply(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    ans: dict[int, Fraction] = {}
    for i, x in a.items():
        for j, y in b.items():
            ans[i + j] = ans.get(i + j, Fraction(0)) + x * y
    return {i: x for i, x in ans.items() if x}


def qbinomial(n: int, i: int, q: int) -> int:
    if i < 0 or i > n:
        return 0
    result = Fraction(1)
    for j in range(i):
        result *= Fraction(q ** (n - j) - 1, q ** (i - j) - 1)
    assert result.denominator == 1
    return result.numerator


def main() -> None:
    radical_rows = []
    for p in (2, 3, 5):
        modulus = p * p
        count = 0
        units = 0
        # The trivial determinant character is extended by zero on singular
        # matrices; quadratic characters give a nontrivial tame test too.
        for a, b, c, d in product(range(modulus), repeat=4):
            det = (a * d - b * c) % modulus
            red_det = ((a % p) * (d % p) - (b % p) * (c % p)) % p
            assert det % p == red_det
            assert (det % p != 0) == (red_det != 0)
            if p > 2:
                tame = 0 if det % p == 0 else pow(det, (p - 1) // 2, p)
                residue_tame = 0 if red_det == 0 else pow(red_det, (p - 1) // 2, p)
                assert tame == residue_tame
            count += 1
            units += int(red_det != 0)
        expected_units = p**4 * (p**2 - 1) * (p**2 - p)
        assert units == expected_units
        radical_rows.append({"p": p, "matrices": count, "invertible_matrices": units})

    qbinomial_cases = 0
    indicator_cases = 0
    for q in (2, 3, 4, 5, 7, 8, 9, 11):
        for n in range(9):
            lhs = {i: Fraction((-1) ** i * q ** comb(i, 2) * qbinomial(n, i, q))
                   for i in range(n + 1)}
            rhs = {0: Fraction(1)}
            for j in range(n):
                rhs = multiply(rhs, {0: Fraction(1), 1: Fraction(-q**j)})
            assert lhs == rhs
            qbinomial_cases += 1
            value = sum(lhs.values())
            assert value == int(n == 0)
            indicator_cases += 1

    euler_rows = []
    for q in (2, 3, 4, 5, 7, 8, 9, 11):
        # P_2((q*y)^-1) = (1-y^-1)(1-q^-1*y^-1).
        period_factor = {0: Fraction(1), -1: -1-Fraction(1, q), -2: Fraction(1, q)}
        direct = multiply({0: Fraction(1), -1: Fraction(-1)},
                          {0: Fraction(1), -1: -Fraction(1, q)})
        assert period_factor == direct
        conjugate = {-i: x for i, x in period_factor.items()}
        square = multiply(period_factor, conjugate)
        target = {0: Fraction(1)}
        for e in (0, 1):
            target = multiply(target, {0: Fraction(1), 1: -Fraction(1, q**e)})
            target = multiply(target, {0: Fraction(1), -1: -Fraction(1, q**e)})
        assert square == target
        assert sum(square.values()) == 0  # y=1 is an allowed imprimitive zero.
        euler_rows.append({"q": q, "square_laurent_coefficients":
                           {str(i): str(x) for i, x in sorted(square.items())}})

    denominator_cases = 0
    for f in range(1, 17):
        for h in range(0, 66, 2):
            source_M, source_d = 16*f + 2*h, h
            improved_M, improved_d = 4*f + h, h//2
            assert source_M - improved_M == 12*f + h
            assert source_d - improved_d == h//2
            assert improved_M >= 0 and improved_d >= 0
            denominator_cases += 1

    report = {
        "scope": "Exact finite algebra only; no period nonvanishing or analytic L-value identity.",
        "radical_prime_square_checks": radical_rows,
        "q_binomial_polynomial_cases": qbinomial_cases,
        "invertible_indicator_corank_cases": indicator_cases,
        "rank_two_euler_factors": euler_rows,
        "denominator_exponent_cases": denominator_cases,
        "source_scale": "vacuumScale^4 jetScale^h M^(16f+2h) d^h",
        "improved_scale": "vacuumScale^4 jetScale^h M^(4f+h) d^(h/2)",
        "quotient": "M^(12f+h) d^(h/2)",
        "status": "passed",
    }
    out = ROOT / "certificates/rank-two-period-arithmetic.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "passed", "prime_square_matrices": sum(r["matrices"] for r in radical_rows),
                      "q_binomial_cases": qbinomial_cases, "euler_cases": len(euler_rows),
                      "denominator_cases": denominator_cases, "certificate": str(out.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
