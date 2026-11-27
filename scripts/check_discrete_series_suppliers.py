#!/usr/bin/env python3
"""Exact convention checks for lsernau-discrete-series-suppliers.md.

These finite checks cover compact dominance, the PRV sorting calculation, and
the trailing-minor orientation of Sun's integral. They do not prove or test
the cited representation-theoretic theorems, analytic integrability, or Lean.
"""

from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path


def half_roots(eps):
    r = len(eps)
    rho = [Q(r - 1 - 2 * i, 2) for i in range(r)]
    compact = [Q(sum(eps[j] == eps[i] for j in range(i + 1, r))
                 - sum(eps[j] == eps[i] for j in range(i)), 2)
               for i in range(r)]
    return rho, compact, [x - y for x, y in zip(rho, compact)]


def parameter(gaps):
    r = len(gaps) + 1
    lam = [Q(r - 1, 2)]
    for gap in gaps:
        lam.append(lam[-1] - gap)
    return lam


def dominant(weight, eps):
    return all(weight[i] >= weight[j]
               for i in range(len(eps)) for j in range(i + 1, len(eps))
               if eps[i] == eps[j])


def compact_sort(weight, eps):
    out = list(weight)
    for sign in (-1, 1):
        indices = [i for i, e in enumerate(eps) if e == sign]
        for i, value in zip(indices, sorted((weight[i] for i in indices), reverse=True)):
            out[i] = value
    return out


def check_parameter(lam, eps, counts):
    r = len(eps)
    rho, rc, rn = half_roots(eps)
    nu = [x - y for x, y in zip(lam, rho)]
    lowest = [x + y - z for x, y, z in zip(lam, rn, rc)]
    a = [x - y for x, y in zip(lam, rc)]
    assert all(x.denominator == 1 for x in nu + lowest)
    assert all(nu[i] >= nu[i + 1] for i in range(r - 1))
    assert dominant(lowest, eps) and dominant(rn, eps) and dominant(a, eps)
    assert [x - y for x, y in zip(lowest, rn)] == a
    assert [x + y for x, y in zip(a, rc)] == lam
    counts['parameter_and_bottom_prv_checks'] += 1
    if len(set(eps)) == 1:
        return
    h = min(abs(lam[i] - lam[j]) for i in range(r) for j in range(i + 1, r)
            if eps[i] != eps[j])
    for i in range(r):
        for j in range(i + 1, r):
            if eps[i] == eps[j]:
                continue
            lowered = list(a)
            lowered[i] -= 1
            lowered[j] += 1
            actual = compact_sort(lowered, eps)
            i0 = max(k for k in range(r) if eps[k] == eps[i] and a[k] == a[i])
            j0 = min(k for k in range(r) if eps[k] == eps[j] and a[k] == a[j])
            predicted = list(a)
            predicted[i0] -= 1
            predicted[j0] += 1
            assert actual == predicted
            assert i0 < j0 and lam[i0] - lam[j0] >= h
            # Equality of a within a sign block forces a contiguous same-sign
            # run with all intervening global lambda gaps equal to one.
            assert all(eps[k] == eps[i] for k in range(i, i0 + 1))
            assert all(lam[k] - lam[k + 1] == 1 for k in range(i, i0))
            assert all(eps[k] == eps[j] for k in range(j0, j + 1))
            assert all(lam[k] - lam[k + 1] == 1 for k in range(j0, j))
            shifted = [x + y for x, y in zip(actual, rc)]
            difference = sum(x * x for x in shifted) - sum(x * x for x in lam)
            assert difference == -2 * (lam[i0] - lam[j0]) + 2
            if h > 1:
                assert difference < 0
                counts['strict_lowered_prv_checks'] += 1
            counts['lowered_prv_sorting_checks'] += 1


def determinant(matrix):
    a = [list(row) for row in matrix]
    result = Q(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return Q(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            result = -result
        value = a[i][i]
        result *= value
        for j in range(i + 1, len(a)):
            multiplier = a[j][i] / value
            for k in range(i + 1, len(a)):
                a[j][k] -= multiplier * a[i][k]
    return result


def weight_minors(matrix, weight):
    levels = sorted(set(weight))
    assert all(x.denominator == 1 for x in levels)
    result = determinant(matrix) ** int(levels[0])
    for before, after in zip(levels, levels[1:]):
        indices = [i for i, w in enumerate(weight) if w >= after]
        minor = [[matrix[i][j] for j in indices] for i in indices]
        result *= determinant(minor) ** int(after - before)
    return result


def check_trailing_minors(counts):
    for r in range(1, 8):
        for trial in range(1, 5):
            n = [[Q(1 if i == j else 0) if i >= j
                  else Q((i + 1) * (j + trial + 1) % 7 - 3, i + j + 2)
                  for j in range(r)] for i in range(r)]
            diagonal = [Q(i + trial + 1, i + 1) for i in range(r)]
            z = [[sum(n[i][k] * diagonal[k] * n[j][k] for k in range(r))
                  for j in range(r)] for i in range(r)]
            lam = parameter([1 + (i + trial) % 3 for i in range(r - 1)])
            rho = [Q(r - 1 - 2 * i, 2) for i in range(r)]
            # Common central shifts exercise negative, mixed, and positive
            # principal-minor weights, including determinant normalization.
            for shift in (-2 * r, 0, 2 * r):
                w = [-lam[i] - shift - rho[i] for i in range(r)]
                expected = Q(1)
                for d, exponent in zip(diagonal, w):
                    expected *= d ** int(exponent)
                assert weight_minors(z, w) == expected
                counts['upper_cholesky_minor_checks'] += 1


def main():
    counts = dict(parameter_and_bottom_prv_checks=0,
                  lowered_prv_sorting_checks=0,
                  strict_lowered_prv_checks=0,
                  upper_cholesky_minor_checks=0)
    for r in range(1, 6):
        for gaps in product((1, 2, 3), repeat=r - 1):
            lam = parameter(gaps)
            for eps in product((-1, 1), repeat=r):
                check_parameter(lam, eps, counts)
    for r in range(2, 8):
        for eps in product((-1, 1), repeat=r):
            gaps = [1 if eps[i] == eps[i + 1] else 500 * r ** 3
                    for i in range(r - 1)]
            check_parameter(parameter(gaps), eps, counts)
    check_trailing_minors(counts)
    result = dict(status='passed', arithmetic='exact rational; no floating point',
                  **counts,
                  scope=('Finite algebraic convention checks only. No discrete-series '
                         'existence, Sun formula, Dirac or Vogan-Zuckerman theorem, '
                         'analytic integrability, or Lean replay was computationally checked.'))
    path = Path(__file__).resolve().parents[1] / 'certificates/discrete-series-suppliers.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
