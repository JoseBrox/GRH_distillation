#!/usr/bin/env python3
"""Exact finite checks of the strengthened Smith-window inequality.

This verifies rational test instances, not the general theorem. All
Smith valuations are computed independently from determinantal ideals.
The test seed and all parameter grids are fixed for reproducibility.
"""
from fractions import Fraction
from itertools import combinations
from math import factorial, inf
import json
import random

import sympy as sp

z = sp.Symbol("z")


def vp(x, p):
    if x == 0:
        return inf
    x = Fraction(x)
    a, b = abs(x.numerator), x.denominator
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v


def smith_valuations_from_minors(mat, p):
    n = mat.rows
    partial = [0]
    exponents = []
    for k in range(1, n + 1):
        mu = min(vp(mat.extract(ii, jj).det(), p)
                 for ii in combinations(range(n), k)
                 for jj in combinations(range(n), k))
        if mu == inf:
            exponents.extend([inf] * (n - k + 1))
            break
        exponents.append(mu - partial[-1])
        partial.append(mu)
    assert all(a <= b for a, b in zip(exponents, exponents[1:]))
    assert all(a >= 0 for a in exponents)
    return exponents


def binpoly(k):
    ans = sp.Integer(1)
    for j in range(k):
        ans *= z - j
    return sp.expand(ans / factorial(k))


def check_instance(mat, Delta, p, t, d, Y, caps):
    f = sp.Poly(sp.expand(mat.det()), z)
    if f.is_zero:
        return 0
    r = f.degree()
    lc = vp(f.LC(), p)
    L, power = 0, p
    while power <= Delta:
        L += 1
        power *= p
    C = (Y - 1) * vp(d, p) + vp(factorial(Y - 1), p)
    vals = [smith_valuations_from_minors(mat.subs(z, t + d*j), p)
            for j in range(Y)]
    checks = 0
    for E in caps:
        lhs = E * sum(sum(a >= E for a in row) for row in vals)
        rhs = Y * lc + r * (E + L + C)
        assert lhs <= rhs, (p, Delta, t, d, Y, E, lhs, rhs, str(mat))
        checks += 1
    return checks


def main():
    rng = random.Random(20261125)
    checks = 0
    matrices = 0
    for p in (2, 3, 5, 7):
        for n in (1, 2, 3):
            for Delta in (0, 1, 2, 4):
                coeffs = [sp.Matrix(n, n,
                    [rng.randrange(-3, 4) * p**rng.randrange(0, 3)
                     for _ in range(n*n)]) for _ in range(Delta + 1)]
                mat = sp.zeros(n)
                for k, coeff in enumerate(coeffs):
                    mat += coeff * binpoly(k)
                if mat.det() == 0:
                    continue
                matrices += 1
                for a in (0, 1, 2):
                    for Y in (1, 3, 9):
                        checks += check_instance(mat, Delta, p, -2, p**a,
                                                 Y, (1, 2, 3, 7, 20))
    # Actual singular samples, ramified steps, and rational binomial data.
    structured = [
        (sp.diag(z, z-1, z-2), 1),
        (sp.diag(binpoly(5), z*(z-1), 8), 5),
        (sp.Matrix([[z, 1], [0, binpoly(4)]]), 4),
    ]
    for mat, Delta in structured:
        matrices += 1
        for p in (2, 3, 5):
            for a in (0, 2):
                checks += check_instance(mat, Delta, p, 0, p**a, 13,
                                         (Fraction(1, 2), 1, 2, 4, 15))
    # Exact root-location improvement: all integer samples have unit values.
    assert all(vp(2*j-1, 2) == 0 for j in range(-30, 31))
    # Omitting the ramified-step term is false: A(z)=z, p=2, d=4, E=2.
    Y, E = 16, 2
    bad = sum(vp(4*j, 2) >= E for j in range(Y))
    wrong_rhs = E + vp(factorial(Y-1), 2)
    assert E*bad > wrong_rhs
    print(json.dumps({
        "status": "passed",
        "source": {
            "repository": "jimjamzola/RH-Alpoge-Reconstruction",
            "commit": "aa9c86bf2a7d29b08575641fecea19a2a603e87c",
            "path": "manuscript/sec12_loss.tex",
            "lines": [689, 794],
            "sha256": "22929e6fd051373261a10e4c8281b4a1e77e50dd853821a39d0e60918c1744c7"
        },
        "method": "exact rational matrices; Smith exponents from all minors",
        "seed": 20261125,
        "matrices": matrices,
        "inequality_checks": checks,
        "primes": [2, 3, 5, 7],
        "includes": ["singular evaluations", "p-divisible progression steps",
                     "Y greater than p^h", "fractional positive caps",
                     "constant determinants", "outside-unit-disk root"],
        "ramified_step_counterexample": {
            "p": 2, "A": "z", "d": 4, "Y": Y, "E": E,
            "left_side": E*bad, "incorrect_unit_step_rhs": wrong_rhs},
        "scope": "Finite checks corroborate the written proof; no Lean replay."
    }, indent=2))


if __name__ == "__main__":
    main()
