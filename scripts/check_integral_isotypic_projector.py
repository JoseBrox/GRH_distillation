#!/usr/bin/env python3
"""Exact checks of the imported isotypic projector denominator bound.

Independent matrix construction: polynomial Casimir spectral projectors on
Sym^a(Q^2) tensor Sym^b(Q^2), in the ordinary monomial tensor lattice.
No floating-point arithmetic. This verifies finite examples, not the theorem.
"""
from math import lcm
import json
from pathlib import Path
import sympy as sp


def vp(n, p):
    n = abs(int(n))
    if n == 0:
        raise ValueError("vp(0) not used")
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def ilog(n, p):
    out = 0
    while n >= p:
        out += 1
        n //= p
    return out


def sym_power(a):
    # Basis x^(a-i) y^i, i=0,...,a.
    E = sp.zeros(a + 1)
    F = sp.zeros(a + 1)
    for i in range(a + 1):
        if i:
            E[i - 1, i] = i
        if i < a:
            F[i + 1, i] = a - i
    H = sp.diag(*[a - 2 * i for i in range(a + 1)])
    return E, F, H


records = []
projectors_checked = 0
prime_cases = 0
strict_improvements = 0
for a in range(6):
    for b in range(a, 6):
        E0, F0, H0 = sym_power(a)
        E1, F1, H1 = sym_power(b)
        E = sp.kronecker_product(E0, sp.eye(b + 1)) + sp.kronecker_product(sp.eye(a + 1), E1)
        F = sp.kronecker_product(F0, sp.eye(b + 1)) + sp.kronecker_product(sp.eye(a + 1), F1)
        H = sp.kronecker_product(H0, sp.eye(b + 1)) + sp.kronecker_product(sp.eye(a + 1), H1)
        I = sp.eye((a + 1) * (b + 1))
        C = H * H + 2 * H + 4 * F * E
        d = a + b
        js = list(range(min(a, b) + 1))
        eigen = {j: (d - 2 * j) * (d - 2 * j + 2) for j in js}
        Ps = []
        for j in js:
            P = I
            for k in js:
                if k != j:
                    P = P * (C - eigen[k] * I) / (eigen[j] - eigen[k])
            P = P.applyfunc(sp.cancel)
            assert P * P == P
            assert P * E == E * P and P * F == F * P and P * H == H * P
            assert sp.trace(P) == d - 2 * j + 1
            Ps.append(P)
            projectors_checked += 1
            den = lcm(*[int(entry.q) for entry in P])
            by_prime = {}
            for p in (2, 3, 5, 7, 11):
                actual = vp(den, p)
                predicted = max(0, ilog(d - j + 1, p) - vp(d - 2 * j + 1, p))
                original = ilog(d + 1, p)
                assert actual <= predicted <= original, (a, b, j, p, actual, predicted, original)
                prime_cases += 1
                strict_improvements += predicted < original
                by_prime[str(p)] = {"actual": actual, "new_bound": predicted, "coarse_bound": original}
            records.append({"a": a, "b": b, "j": j, "dimension": d - 2 * j + 1,
                            "denominator": int(den), "primes": by_prime})
        assert sum(Ps, sp.zeros(I.rows)) == I
        for j in range(len(Ps)):
            for k in range(j):
                assert Ps[j] * Ps[k] == sp.zeros(I.rows)

result = {"status": "passed", "representations": 21,
          "projectors_checked": projectors_checked, "prime_cases": prime_cases,
          "strict_improvements": strict_improvements,
          "method": "exact rational Casimir spectral projectors on monomial lattices",
          "records": records}
output = Path(__file__).resolve().parents[1] / "certificates" / "integral-isotypic-projector-check.json"
with output.open("w") as f:
    json.dump(result, f, indent=2)
print(json.dumps({k: v for k, v in result.items() if k != "records"}, indent=2))
