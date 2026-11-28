#!/usr/bin/env python3
"""Independent exact checks of the finite good-type density chapter.

Polynomials are enumerated and factored over small prime fields. Primitive
polynomials are tested by multiplicative order in the quotient field. Counts
and rational Green degree masses are then compared to the stated formulas.
This does not test an automorphic moment or a global parameter budget.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
import json
from math import comb, gcd, prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
Poly = tuple[int, ...]  # coefficients from constant term upwards


def trim(a: list[int] | Poly) -> Poly:
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a) if a else (0,)


def divide(a: Poly, b: Poly, p: int) -> tuple[Poly, Poly]:
    assert b != (0,)
    rem = list(a)
    ans = [0] * max(1, len(a) - len(b) + 1)
    inv = pow(b[-1], -1, p)
    while len(rem) >= len(b) and tuple(rem) != (0,):
        shift = len(rem) - len(b)
        c = rem[-1] * inv % p
        ans[shift] = c
        for j, bj in enumerate(b):
            rem[j + shift] = (rem[j + shift] - c * bj) % p
        rem = list(trim(rem))
    return trim(ans), trim(rem)


def poly_gcd(a: Poly, b: Poly, p: int) -> Poly:
    while b != (0,):
        a, b = b, divide(a, b, p)[1]
    inv = pow(a[-1], -1, p)
    return tuple(x * inv % p for x in a)


def mulmod(a: Poly, b: Poly, modulus: Poly, p: int) -> Poly:
    result = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            result[i + j] = (result[i + j] + ai * bj) % p
    return divide(trim(result), modulus, p)[1]


def powmod(a: Poly, exponent: int, modulus: Poly, p: int) -> Poly:
    value = (1,)
    while exponent:
        if exponent & 1:
            value = mulmod(value, a, modulus, p)
        a = mulmod(a, a, modulus, p)
        exponent //= 2
    return value


def evaluate(a: Poly, x: int, p: int) -> int:
    value = 0
    for c in reversed(a):
        value = (value * x + c) % p
    return value


def monics(p: int, degree: int):
    for lower in product(range(p), repeat=degree):
        yield lower + (1,)


def prime_divisors(n: int) -> list[int]:
    answer = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            answer.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        answer.append(n)
    return answer


def phi(n: int) -> int:
    answer = n
    for ell in prime_divisors(n):
        answer = answer // ell * (ell - 1)
    return answer


def irreducibles_through(p: int, maximum: int) -> list[Poly]:
    answer: list[Poly] = []
    for d in range(1, maximum + 1):
        for a in monics(p, d):
            if all(divide(a, b, p)[1] != (0,)
                   for b in answer if 2 * (len(b) - 1) <= d):
                answer.append(a)
    return answer


def factor(a: Poly, p: int, irreducibles: list[Poly]) -> list[Poly]:
    rem = a
    answer = []
    for b in irreducibles:
        while len(b) <= len(rem):
            quotient, residue = divide(rem, b, p)
            if residue != (0,):
                break
            answer.append(b)
            rem = quotient
        if rem == (1,):
            break
    assert rem == (1,)
    return answer


def primitive(a: Poly, p: int, is_irreducible: bool) -> bool:
    if not is_irreducible or a[0] == 0:
        return False
    n = p ** (len(a) - 1) - 1
    x = (0, 1)
    assert powmod(x, n, a, p) == (1,)
    return all(powmod(x, n // ell, a, p) != (1,)
               for ell in prime_divisors(n))


def allowed_count(q: int, r: int, a: int) -> int:
    def squarefree_count(d: int) -> int:
        return 1 if d == 0 else q if d == 1 else q**d - q**(d - 1)
    return sum((-1)**j * comb(a + j - 1, j) * squarefree_count(r - j)
               for j in range(r + 1))


def main() -> None:
    cases = [(2, range(2, 7)), (3, range(2, 6)), (5, range(2, 5)),
             (7, range(2, 5)), (11, range(2, 4))]
    rows = []
    polynomial_checks = weight_checks = count_checks = tuple_checks = 0
    for q, ranks in cases:
        irr = irreducibles_through(q, max(ranks))
        for r in ranks:
            group_order = q**(r * (r - 1) // 2) * prod(q**j - 1 for j in range(1, r + 1))
            b_r = prod((1 - Fraction(1, q**j) for j in range(1, r + 1)),
                       start=Fraction(1))
            omega = b_r / (q**r * (1 - Fraction(1, q**r))**2)
            assert 0 < q**r * omega < 1
            sum_regular = Fraction(0)
            primitive_mass = Fraction(0)
            primitive_count = 0
            nonsquarefree = 0
            records = []
            for a in monics(q, r):
                factors = factor(a, q, irr)
                squarefree = len(factors) == len(set(factors))
                derivative = trim(tuple((j * a[j]) % q for j in range(1, len(a))))
                assert squarefree == (poly_gcd(a, derivative, q) == (1,))
                is_primitive = primitive(a, q, len(factors) == 1)
                primitive_count += is_primitive
                nonsquarefree += not squarefree
                polynomial_checks += 1
                if not squarefree or a[0] == 0:
                    assert not is_primitive
                    continue
                degree = Fraction(prod(q**j - 1 for j in range(1, r + 1)),
                                  prod(q**(len(b) - 1) - 1 for b in factors))
                assert degree.denominator == 1
                weight = degree**2 / group_order
                direct_weight = b_r / (
                    q**r * prod((1 - Fraction(1, q**(len(b) - 1)))**2
                                for b in factors))
                assert weight == direct_weight
                assert weight >= omega
                assert (weight == omega) == (len(factors) == 1)
                sum_regular += weight
                if is_primitive:
                    primitive_mass += weight
                records.append((a, weight, is_primitive))
                weight_checks += 1
            assert nonsquarefree == q**(r - 1)
            assert primitive_count == phi(q**r - 1) // r
            assert phi(q**r - 1) % r == 0
            expected_p = Fraction(phi(q**r - 1), q**r - 1) * (
                b_r / (1 - Fraction(1, q**r))) / r
            assert primitive_mass == primitive_count * omega == expected_p
            assert sum_regular <= 1
            h_rows = []
            for h in range(1, 9):
                roots = [0] + [x for x in range(1, q) if pow(x, h, q) == 1]
                g = gcd(h, q - 1)
                assert len(roots) == g + 1
                actual = [(a, w, pr) for a, w, pr in records
                          if all(evaluate(a, x, q) != 0 for x in roots)]
                count = len(actual)
                assert count == allowed_count(q, r, g + 1)
                assert q**r - count <= (g + 2) * q**(r - 1)
                assert sum(pr for _, _, pr in actual) == primitive_count
                alpha = sum((w for _, w, _ in actual), start=Fraction(0))
                a0 = count * omega
                assert 0 < expected_p <= a0 <= alpha <= 1
                epsilon = Fraction(g + 2, q) + sum(
                    (Fraction(1, q**j) for j in range(1, r + 1)), start=Fraction(0))
                assert 1 - a0 <= epsilon
                assert epsilon <= Fraction(g + r + 2, q) <= Fraction(1 + h + 2*r, q)
                bounds = []
                for f in range(1, 7):
                    bad = 1 - alpha**f + (alpha - expected_p)**f
                    sharp = 1 - a0**f + (a0 - expected_p)**f
                    simple = f * (1 - a0) + (1 - expected_p)**f
                    assert 0 <= bad <= sharp <= simple
                    bounds.append({"f": f, "actual_bad_mass": str(bad),
                                   "sharp_bound": str(sharp)})
                    tuple_checks += 1
                h_rows.append({"H": h, "forbidden_roots": roots,
                               "allowed_count": count, "allowed_mass": str(alpha),
                               "minimum_mass_bound": str(a0),
                               "epsilon_star": str(epsilon),
                               "tuple_bounds": bounds})
                count_checks += 1
            rows.append({"q": q, "rank": r, "polynomials": q**r,
                         "regular_label_mass": str(sum_regular),
                         "primitive_count": primitive_count,
                         "primitive_mass": str(primitive_mass),
                         "minimum_label_mass": str(omega),
                         "forbidden_exponents": h_rows})
    result = {
        "status": "PASS",
        "scope": "Exact polynomial enumeration, primitive order and rational Green degree masses; no analytic moment or global parameter-existence claim.",
        "polynomials_enumerated": polynomial_checks,
        "regular_label_weight_checks": weight_checks,
        "allowed_count_cases": count_checks,
        "tuple_deficit_checks": tuple_checks,
        "cases": rows,
    }
    target = ROOT / "certificates" / "finite-good-type-density.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "cases"}, indent=2))


if __name__ == "__main__":
    main()
