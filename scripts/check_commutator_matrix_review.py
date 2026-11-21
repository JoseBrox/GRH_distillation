#!/usr/bin/env python3
"""Independent exact normal-order checks for the radial commutator formulas.

This is a second implementation. It compares complete differential-operator
coefficient maps for n=1,2, rather than evaluations on selected functions.
It also tests a sandwich with genuinely noncommuting middle entries and a
negative control violating their independence of the outer coordinates.
It verifies these representations, not the universal enveloping-algebra
identities or the analytic restriction theorem in all ranks.
"""
from __future__ import annotations

from itertools import permutations, product
from math import comb
from pathlib import Path
import hashlib
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


class Ring:
    def __init__(self, variables):
        self.variables = tuple(variables)
        self.zero_index = (0,) * len(self.variables)

    def mul(self, coefficient):
        return Op(self, {self.zero_index: sp.sympify(coefficient)})

    def derivative(self, index):
        powers = list(self.zero_index)
        powers[index] = 1
        return Op(self, {tuple(powers): sp.Integer(1)})


class Op:
    def __init__(self, ring, terms):
        self.ring = ring
        self.terms = {}
        for index, coefficient in terms.items():
            coefficient = sp.cancel(sp.expand(coefficient))
            if coefficient != 0:
                self.terms[index] = coefficient

    def coerce(self, other):
        if isinstance(other, Op):
            assert self.ring is other.ring
            return other
        return self.ring.mul(other)

    def __add__(self, other):
        other = self.coerce(other)
        terms = self.terms.copy()
        for index, coefficient in other.terms.items():
            terms[index] = terms.get(index, 0) + coefficient
        return Op(self.ring, terms)

    __radd__ = __add__

    def __neg__(self):
        return Op(self.ring, {index: -v for index, v in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) + (-self)

    def __mul__(self, other):
        other = self.coerce(other)
        terms = {}
        for alpha, left in self.terms.items():
            for beta, right in other.terms.items():
                for gamma in product(*(range(a + 1) for a in alpha)):
                    coefficient = right
                    factor = 1
                    for variable, a, g in zip(self.ring.variables, alpha, gamma):
                        factor *= comb(a, g)
                        if g:
                            coefficient = sp.diff(coefficient, variable, g)
                        if coefficient == 0:
                            break
                    if coefficient == 0:
                        continue
                    index = tuple(a - g + b for a, g, b in zip(alpha, gamma, beta))
                    terms[index] = terms.get(index, 0) + left * factor * coefficient
        return Op(self.ring, terms)

    def __rmul__(self, other):
        return self.coerce(other) * self

    def comm(self, other):
        return self * other - self.coerce(other) * self

    def is_zero(self):
        return not self.terms


def sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p)))


def check_rank(n):
    eta = sp.symbols(f'eta0:{n}')
    y = sp.symbols(f'y0:{n}')
    x = sp.symbols(f'x0:{n}')
    xi = sp.symbols(f'xi0:{n}')
    u = sp.Symbol('u')
    ring = Ring(eta + y)
    identity, zero = ring.mul(1), ring.mul(0)
    E = [[eta[a] * ring.derivative(b) - y[b] * ring.derivative(n+a)
          for b in range(n)] for a in range(n)]
    indices = tuple(range(n))

    def minor(rows, columns, parameter):
        total = zero
        for permutation in permutations(range(len(rows))):
            term = identity
            for j, col in enumerate(columns):
                row = rows[permutation[j]]
                term = term * (E[row][col] + ((parameter-j) if row == col else 0))
            total += sign(permutation) * term
        return total

    def cofactor(i, j, parameter):
        return (-1)**(i+j) * minor(tuple(a for a in indices if a != i),
                                   tuple(a for a in indices if a != j), parameter)

    def double_cofactor(i, l, j, a, parameter):
        if i == l or j == a:
            return zero
        epsilon = (1 if i < l else -1) * (1 if j < a else -1)
        return epsilon * (-1)**(i+l+j+a) * minor(
            tuple(t for t in indices if t not in (i, l)),
            tuple(t for t in indices if t not in (j, a)), parameter)

    lie_count = 0
    for a, b, c, d in product(indices, repeat=4):
        residual = E[a][b].comm(E[c][d]) - (E[a][d] if b == c else zero) + (E[c][b] if d == a else zero)
        assert residual.is_zero(), ('Lie relation', n, a, b, c, d)
        lie_count += 1

    D = minor(indices, indices, u)
    Z = ring.mul(sum(eta[j] * x[j] for j in indices))
    B = ring.mul(sum(xi[j] * y[j] for j in indices))
    Heta = sum((eta[i] * x[j] * cofactor(i, j, u-1)
                for i, j in product(indices, repeat=2)), zero)
    Hy = sum((xi[i] * y[j] * cofactor(i, j, u)
              for i, j in product(indices, repeat=2)), zero)
    H2 = sum(((eta[i] * xi[l] - eta[l] * xi[i]) *
              (y[a] * x[j] - y[j] * x[a]) * double_cofactor(i, l, a, j, u-1)
              for i in indices for l in indices if i < l
              for a in indices for j in indices if a < j), zero)
    for name, residual in [
        ('determinant_covector', D.comm(Z) - Heta),
        ('determinant_vector', D.comm(B) + Hy),
        ('mixed_commutator', D.comm(Z).comm(B) - H2),
    ]:
        assert residual.is_zero(), (n, name, residual.terms)

    cofactor_count = 0
    for i, j, l in product(indices, repeat=3):
        residual = cofactor(i, j, u).comm(ring.mul(y[l])) + sum(
            (y[a] * double_cofactor(i, l, j, a, u) for a in indices), zero)
        assert residual.is_zero(), ('cofactor_vector', n, i, j, l)
        cofactor_count += 1
    return {'dimension': n, 'lie_relation_identities': lie_count,
            'cofactor_vector_identities': cofactor_count,
            'contracted_commutator_identities': 3,
            'parameters': 'u and every x_i, xi_i are independent exact symbols',
            'method': 'All normal-ordered differential coefficients compared exactly',
            'status': 'passed'}


def check_sandwich():
    c, b, s, Y = sp.symbols('c barc s Y')
    ring = Ring((c, b, s))
    m = ring.mul
    dc, db, ds = (ring.derivative(i) for i in range(3))
    p, bp = c * dc, b * db
    L = [[Y-bp, m(1/b)], [m(-b), m(0)]]
    T = [[Y+p, m(-c)], [m(1/c), m(0)]]

    def mm(A, B):
        return [[sum((A[i][k] * B[k][j] for k in range(2)), m(0))
                 for j in range(2)] for i in range(2)]

    def residuals(t):
        M = mm(mm(L, t), T)
        C = M[0][0]
        predicted = [[C, -C.comm(m(c))], [C.comm(m(b)), -C.comm(m(c)).comm(m(b))]]
        return [M[i][j] - predicted[i][j] for i in range(2) for j in range(2)]

    a, bb, d, e = s * ds, m(s), ds, s*s * ds + 1
    assert not a.comm(bb).is_zero()
    assert not d.comm(bb).is_zero()
    assert not a.comm(d).is_zero()
    good = residuals([[a, bb], [d, e]])
    assert all(r.is_zero() for r in good)
    bad = residuals([[dc, bb], [d, e]])
    nonzero_entries = [list(divmod(i, 2)) for i, r in enumerate(bad) if not r.is_zero()]
    assert nonzero_entries, 'Negative control unexpectedly passed'
    return {'status': 'passed', 'middle_entries': ['s d/ds', 's', 'd/ds', 's^2 d/ds + 1'],
            'noncommuting_pairs_confirmed': ['[a,b]', '[d,b]', '[a,d]'],
            'sandwich_entries_verified': 4,
            'negative_control': {'change': 'a replaced by d/dc, violating coordinate independence',
                                 'nonzero_residual_entries_zero_based': nonzero_entries,
                                 'status': 'rejected as expected'},
            'domain': 'c and barc nonzero; formal independent Wirtinger coordinates'}


def main():
    results = [check_rank(n) for n in (1, 2)]
    sandwich = check_sandwich()
    source_paths = ['paper/sections/new/commutator-matrix.tex',
                    'paper/sections/recovered/87-rq-section.tex',
                    'paper/sections/recovered/88-rr-section.tex']
    report = {'scope': 'Independent exact differential representation checks; not a universal or analytic proof.',
              'method': 'Leibniz composition and complete normal-order coefficient comparison over exact rational-function fields',
              'sympy_version': sp.__version__,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'source_sha256': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in source_paths},
              'ranks': results, 'noncommuting_sandwich': sandwich, 'status': 'passed'}
    target = ROOT/'certificates/radial-commutator-independent-check.json'
    target.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'status': report['status'], 'ranks': results,
                      'noncommuting_sandwich': sandwich, 'certificate': str(target.relative_to(ROOT))}, indent=2))


if __name__ == '__main__':
    main()
