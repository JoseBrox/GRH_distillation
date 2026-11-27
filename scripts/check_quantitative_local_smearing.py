#!/usr/bin/env python3
"""Exact finite checks of the truncated Howe spanning matrices.

Noncompact examples deliberately use small parameters so their polynomial
spaces are finite and manageable. They test algebraic spanning and integer
minors, not the source large-gap condition or any analytic theorem.
"""

from fractions import Fraction as Q
from itertools import product
from math import gcd, lcm
import json
from pathlib import Path

from check_noncompact_fock_bridge import Pair, add, scale, monomials, lowest, harmonic


def nullspace(matrix, ncols):
    a = [list(row) for row in matrix]
    pivots = []
    row = 0
    for col in range(ncols):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        value = a[row][col]
        a[row] = [x / value for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                value = a[i][col]
                a[i] = [x - value * y for x, y in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    free = [j for j in range(ncols) if j not in pivots]
    result = []
    for j in free:
        vector = [Q(0)] * ncols
        vector[j] = Q(1)
        for i, pivot in enumerate(pivots):
            vector[pivot] = -a[i][j]
        denominator = lcm(*(x.denominator for x in vector))
        integer = [int(x * denominator) for x in vector]
        divisor = gcd(*integer)
        result.append([Q(x // divisor) for x in integer])
    return result


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
            if a[j][i]:
                factor = a[j][i] / value
                for k in range(i + 1, len(a)):
                    a[j][k] -= factor * a[i][k]
                a[j][i] = Q(0)
    return result


def in_cone(weight, target, order):
    delta = [weight[i] - target[i] for i in order]
    return sum(delta) == 0 and all(sum(delta[:i]) >= 0 for i in range(1, len(delta)))


def highest_spaces(pair, l, degree):
    if degree < 0:
        return []
    groups = {}
    for p in monomials(pair.nvars, degree):
        (power,) = p
        weight = tuple(pair.row(p, a, a).get(power, Q(0)) for a in range(pair.n))
        groups.setdefault(weight, []).append(p)
    raising = [(a, b) for a, b in product(range(pair.n), repeat=2)
               if pair.eps[a] == pair.eps[b] and l[a] > l[b]]
    result = []
    for weight, basis in groups.items():
        rows = {}
        for j, p in enumerate(basis):
            for a, b in raising:
                for power, value in pair.row(p, a, b).items():
                    rows.setdefault((a, b, power), [Q(0)] * len(basis))[j] = value
        for vector in nullspace(list(rows.values()), len(basis)):
            q = add(*(scale(value, p) for value, p in zip(vector, basis)))
            assert q and all(value.denominator == 1 for value in q.values())
            assert all(not pair.row(q, a, b) for a, b in raising)
            for a in range(pair.n):
                assert pair.row(q, a, a) == scale(weight[a], q)
            result.append((weight, q))
    return result


def compact_orbit(pair, lprime, phi):
    d0 = next(iter({sum(power) for power in phi}))
    lowering = [(d, c) for c, d in product(range(pair.m), repeat=2)
                if pair.epsprime[c] == pair.epsprime[d] and lprime[c] > lprime[d]]
    terms = [phi]
    previous = [phi]
    for depth in range(1, (pair.m - 1) * d0 + 1):
        current = [pair.col(p, c, d) for p in previous for c, d in lowering]
        current = [p for p in current if p]
        terms.extend(current)
        previous = current
        if not previous:
            break
    assert all(not pair.col(p, c, d) for p in previous for c, d in lowering)
    return terms


def spanning_check(pair, l, lprime, phi, degree):
    rowweight = lowest(l, pair.eps)
    order = sorted(range(pair.n), key=lambda a: l[a], reverse=True)
    d0 = next(iter({sum(power) for power in phi}))
    basis = list(monomials(pair.nvars, degree))
    powers = [next(iter(p)) for p in basis]
    index = {power: i for i, power in enumerate(powers)}
    columns = []

    def append(p, label):
        if p:
            assert all(sum(power) <= degree for power in p)
            assert all(value.denominator == 1 for value in p.values())
            columns.append((p, label))

    if degree >= 1:
        for p in monomials(pair.nvars, degree - 1):
            append(p, 'lower_degree')
    if degree >= 2:
        for p in monomials(pair.nvars, degree - 2):
            for c, d in product(range(pair.m), repeat=2):
                if pair.epsprime[c] != pair.epsprime[d]:
                    append(pair.col(p, c, d), 'noncompact_column')
    for p in basis:
        for a in range(pair.n):
            append(add(pair.row(p, a, a), scale(-rowweight[a], p)), 'row_diagonal')
        for a, b in product(range(pair.n), repeat=2):
            if pair.eps[a] == pair.eps[b] and l[a] > l[b]:
                append(pair.row(p, b, a), 'row_lowering')
    for weight, p in highest_spaces(pair, l, degree - 2):
        if not in_cone(weight, rowweight, order):
            for a, b in product(range(pair.n), repeat=2):
                append(pair.row(p, a, b), 'off_cone_row')
    if degree >= d0:
        for p in compact_orbit(pair, lprime, phi):
            append(p, 'compact_phi')

    echelon = {}
    selected = []
    for j, (p, label) in enumerate(columns):
        vector = [Q(0)] * len(basis)
        for power, value in p.items():
            vector[index[power]] = value
        for pivot in sorted(echelon):
            if vector[pivot]:
                factor = vector[pivot]
                vector = [x - factor * y for x, y in zip(vector, echelon[pivot])]
        pivot = next((i for i, value in enumerate(vector) if value), None)
        if pivot is not None:
            value = vector[pivot]
            echelon[pivot] = [x / value for x in vector]
            selected.append(j)
        if len(selected) == len(basis):
            break
    assert len(selected) == len(basis), (pair.n, pair.m, degree, len(selected), len(basis))
    matrix = [[columns[j][0].get(power, Q(0)) for j in selected] for power in powers]
    det = determinant(matrix)
    assert det and det.denominator == 1
    return dict(degree=degree, dimension=len(basis), generated_columns=len(columns),
                determinant=str(det), selected_types=sorted({columns[j][1] for j in selected}))


def main():
    cases = []
    p = Pair((1,), (1,))
    cases.append(('compact_characters', p, [4], [-6],
                  { (2,): Q(1) }, 6))
    p = Pair((1,), (1, -1))
    cases.append(('one_row_noncompact_columns', p, [0], [-3, -1],
                  p.variable(0, 0), 6))
    p = Pair((1, -1), (1, -1))
    cases.append(('two_noncompact_groups', p, [1, -1], [-5, -3],
                  { (2, 0, 0, 0): Q(1) }, 4))
    p = Pair((1, 1, -1), (1, 1))
    cases.append(('nontrivial_row_highest_kernels', p, [2, 0, -2], [-7, -5],
                  p.minor([0, 1], [0, 1]), 3))
    reports = []
    for name, pair, l, lprime, phi, maxdegree in cases:
        check = harmonic(pair, l, lprime)
        assert check['degree'] == next(iter({sum(power) for power in phi}))
        reports.append(dict(name=name, row_rank=pair.n, column_rank=pair.m,
                            full_source_gap=check['full_source_gap'],
                            checks=[spanning_check(pair, l, lprime, phi, j)
                                    for j in range(maxdegree + 1)]))
    result = dict(status='passed', arithmetic='exact rational and integer', cases=reports,
                  scope=('Finite algebraic truncated-spanning and nonzero integer-minor checks. '
                         'The noncompact cases do not meet the source large gap. No analytic '
                         'bump seminorm, projection, theta integral, or Lean build was tested.'))
    target = Path(__file__).resolve().parents[1] / 'certificates/quantitative-local-smearing.json'
    target.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(status='passed', cases=len(reports),
                         finite_spanning_matrices=sum(len(x['checks']) for x in reports),
                         maximum_dimension=max(y['dimension'] for x in reports for y in x['checks'])),
                     indent=2))


if __name__ == '__main__':
    main()
