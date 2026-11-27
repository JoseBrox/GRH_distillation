#!/usr/bin/env python3
"""Exact finite checks of the conventions in lsernau-noncompact-real-edges.md.

Uses only Python's standard library, with Fraction coefficients and sparse
polynomials. This checks finite algebraic examples, not the analytic kernel
package, theta nonvanishing, smearing, or a Lean build.
"""

from fractions import Fraction as Q
from itertools import combinations_with_replacement, permutations, product
import json
from pathlib import Path


def add(*polys):
    out = {}
    for poly in polys:
        for power, coefficient in poly.items():
            out[power] = out.get(power, Q(0)) + coefficient
    return {power: coefficient for power, coefficient in out.items() if coefficient}


def scale(c, poly):
    return {power: c * coefficient for power, coefficient in poly.items() if c * coefficient}


def mul(left, right):
    out = {}
    for a, x in left.items():
        for b, y in right.items():
            power = tuple(i + j for i, j in zip(a, b))
            out[power] = out.get(power, Q(0)) + x * y
    return {power: coefficient for power, coefficient in out.items() if coefficient}


def power(poly, exponent, nvars):
    if not exponent:
        return {(0,) * nvars: Q(1)}
    if len(poly) == 1:
        ((a, c),) = poly.items()
        return {tuple(i * exponent for i in a): c ** exponent}
    result = {(0,) * nvars: Q(1)}
    while exponent:
        if exponent & 1:
            result = mul(result, poly)
        exponent //= 2
        if exponent:
            poly = mul(poly, poly)
    return result


def multiply_variable(poly, i):
    out = {}
    for a, c in poly.items():
        b = list(a)
        b[i] += 1
        out[tuple(b)] = c
    return out


def derivative(poly, i):
    out = {}
    for a, c in poly.items():
        if a[i]:
            b = list(a)
            b[i] -= 1
            out[tuple(b)] = c * a[i]
    return out


def sign(x):
    return (x > 0) - (x < 0)


class Pair:
    def __init__(self, eps, epsprime, sigma=1, gamma=0, gammaprime=0):
        self.eps, self.epsprime = tuple(eps), tuple(epsprime)
        self.n, self.m = len(eps), len(epsprime)
        self.nvars = self.n * self.m
        self.sigma, self.gamma, self.gammaprime = sigma, gamma, gammaprime
        self.eta = tuple(sigma * a * b for a in eps for b in epsprime)
        self.one = {(0,) * self.nvars: Q(1)}

    def variable(self, r, c):
        return multiply_variable(self.one, r * self.m + c)

    def A(self, poly, r, c):
        i = r * self.m + c
        return multiply_variable(poly, i) if self.eta[i] == 1 else scale(-1, derivative(poly, i))

    def B(self, poly, r, c):
        i = r * self.m + c
        return derivative(poly, i) if self.eta[i] == 1 else multiply_variable(poly, i)

    def row(self, poly, a, b):
        s = 1 if self.eps[a] == self.eps[b] else self.sigma
        return add(scale(s, add(*(self.A(self.B(poly, b, c), a, c) for c in range(self.m)))),
                   scale(self.gamma if a == b else 0, poly))

    def col(self, poly, c, d):
        s = 1 if self.epsprime[c] == self.epsprime[d] else self.sigma
        return add(scale(-s, add(*(self.B(self.A(poly, r, d), r, c) for r in range(self.n)))),
                   scale(self.gammaprime if c == d else 0, poly))

    def centred_casimir(self, poly, column=False):
        N = self.m if column else self.n
        centre = (Q(self.gammaprime) - Q(self.n, 2)) if column else (Q(self.gamma) - Q(self.m, 2))
        action = self.col if column else self.row

        def centred(v, a, b):
            return add(action(v, a, b), scale(-centre if a == b else 0, v))

        return add(*(centred(centred(poly, b, a), a, b)
                     for a in range(N) for b in range(N)))

    def minor(self, rows, columns):
        out = {}
        for perm in permutations(range(len(rows))):
            inversions = sum(perm[a] > perm[b]
                             for a in range(len(perm)) for b in range(a + 1, len(perm)))
            term = self.one
            for i, r in enumerate(rows):
                term = mul(term, self.variable(r, columns[perm[i]]))
            out = add(out, scale((-1) ** inversions, term))
        return out


def monomials(nvars, degree):
    yield {(0,) * nvars: Q(1)}
    for d in range(1, degree + 1):
        for inds in combinations_with_replacement(range(nvars), d):
            a = [0] * nvars
            for i in inds:
                a[i] += 1
            yield {tuple(a): Q(1)}


def lowest(l, eps):
    result = [Q(l[r] + sum(eps[r] * eps[a] * sign(l[a] - l[r]) for a in range(len(l))), 2)
              for r in range(len(l))]
    assert all(x.denominator == 1 for x in result)
    return [int(x) for x in result]


def harmonic(pair, l, lprime):
    rowweight, colweight = lowest(l, pair.eps), lowest(lprime, pair.epsprime)
    relative = [rowweight[r] - pair.gamma + sum(pair.eta[r * pair.m + c] == -1
                                               for c in range(pair.m)) for r in range(pair.n)]
    relativeprime = [colweight[c] - pair.gammaprime + sum(pair.eta[r * pair.m + c] == 1
                                                        for r in range(pair.n)) for c in range(pair.m)]
    u = [x - 2 * pair.gamma + pair.m for x in l]
    uprime = [x - 2 * pair.gammaprime + pair.n for x in lprime]
    matching = [(r, c) for r in range(pair.n) for c in range(pair.m)
                if u[r] == -uprime[c] and pair.eta[r * pair.m + c] * u[r] > abs(pair.n - pair.m)]
    assert len({r for r, c in matching}) == len(matching)
    assert len({c for r, c in matching}) == len(matching)
    for r, c in matching:
        assert relative[r] == -relativeprime[c]
        assert relative[r] == 0 or sign(relative[r]) == pair.eta[r * pair.m + c]
    for r in range(pair.n):
        assert any(a == r for a, c in matching) or (abs(u[r]) < pair.n - pair.m and relative[r] == 0)
    for c in range(pair.m):
        assert any(b == c for r, b in matching) or (abs(uprime[c]) < pair.m - pair.n and relativeprime[c] == 0)

    result = pair.one
    for a, b in product((-1, 1), repeat=2):
        block = [(r, c) for r, c in matching if pair.eps[r] == a and pair.epsprime[c] == b]
        previous = 0
        for h in sorted({abs(relative[r]) for r, c in block if relative[r]}):
            layer = [(r, c) for r, c in block if abs(relative[r]) >= h]
            minor = pair.minor([r for r, c in layer], [c for r, c in layer])
            result = mul(result, power(minor, h - previous, pair.nvars))
            previous = h
    assert result
    for r in range(pair.n):
        assert pair.row(result, r, r) == scale(rowweight[r], result)
        for a in range(pair.n):
            if pair.eps[r] == pair.eps[a] and l[r] > l[a]:
                assert not pair.row(result, r, a)
    for c in range(pair.m):
        assert pair.col(result, c, c) == scale(colweight[c], result)
        for d in range(pair.m):
            if pair.epsprime[c] == pair.epsprime[d] and lprime[c] > lprime[d]:
                assert not pair.col(result, c, d)
    for a, b, c in product(range(pair.n), range(pair.n), range(pair.m)):
        if pair.eps[a] != pair.eps[b]:
            assert not derivative(derivative(result, a * pair.m + c), b * pair.m + c)
    for r, c, d in product(range(pair.n), range(pair.m), range(pair.m)):
        if pair.epsprime[c] != pair.epsprime[d]:
            assert not derivative(derivative(result, r * pair.m + c), r * pair.m + d)
    matching_coordinates = {r * pair.m + c for r, c in matching}
    value = sum(coef for powers, coef in result.items()
                if all(not exponent or i in matching_coordinates for i, exponent in enumerate(powers)))
    assert value == 1
    degrees = {sum(a) for a in result}
    assert degrees == {sum(abs(x) for x in relative)}
    return {"rank": [pair.n, pair.m], "degree": next(iter(degrees)),
            "monomials": len(result), "matching_value": str(value),
            "relative_row_weights": relative,
            "full_source_gap": all(abs(l[a] - l[b]) >= 1000 * (pair.n + pair.m) ** 3
                                   for a in range(pair.n) for b in range(pair.n)
                                   if pair.eps[a] != pair.eps[b])
            and all(abs(lprime[c] - lprime[d]) >= 1000 * (pair.n + pair.m) ** 3
                    for c in range(pair.m) for d in range(pair.m)
                    if pair.epsprime[c] != pair.epsprime[d])}


def run():
    coefficient_checks = 0
    commutator_checks = 0
    cases = [Pair((1, -1), (1, -1, 1), sigma, 2, -1) for sigma in (-1, 1)]
    cases += [Pair((1,), (-1, 1), sigma, -2, 3) for sigma in (-1, 1)]
    for pair in cases:
        for p in monomials(pair.nvars, 2):
            diff = add(pair.centred_casimir(p, True), scale(-1, pair.centred_casimir(p)))
            assert diff == scale(Q(pair.n * pair.m * (pair.n - pair.m), 4), p)
            coefficient_checks += 1
            for a, b, c, d in product(range(pair.n), range(pair.n), range(pair.m), range(pair.m)):
                assert pair.row(pair.col(p, c, d), a, b) == pair.col(pair.row(p, a, b), c, d)
                commutator_checks += 1
    actual = harmonic(Pair((1, -1), (1, -1, 1)),
                      [200001, 400001], [-200006, -400006, -2])
    determinant_example = harmonic(Pair((1, 1, -1, -1), (1, 1, -1, -1)),
                                   [7, 5, 3, 1], [-15, -13, -11, -9])
    assert actual["full_source_gap"]
    assert not determinant_example["full_source_gap"]
    return {
        "status": "passed",
        "arithmetic": "exact rational coefficients; no floating point",
        "casimir_test_vectors": coefficient_checks,
        "row_column_commutator_checks": commutator_checks,
        "large_gap_noncompact_example": actual,
        "small_gap_determinant_example": determinant_example,
        "scope": "Finite algebraic checks only. No analytic kernel, projection, smearing, return estimate, or Lean replay was checked."
    }


if __name__ == "__main__":
    report = run()
    target = Path(__file__).resolve().parents[1] / "certificates" / "noncompact-fock-bridge.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
