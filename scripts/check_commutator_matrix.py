#!/usr/bin/env python3
"""Exact finite checks of the new Capelli commutator formulas.

This is an independent differential representation check, not a proof of
the universal identities.  The proof is in commutator-matrix.tex.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from functools import cache
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def signature(permutation):
    return (-1) ** sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )


def run_rank(n):
    eta = sp.symbols(f'a0:{n}')
    y = sp.symbols(f'b0:{n}')
    u = sp.Symbol('u')
    variables = eta + y
    full = tuple(range(n))

    def e(a, b, f):
        return sp.expand(eta[a] * sp.diff(f, eta[b])
                         - y[b] * sp.diff(f, y[a]))

    @cache
    def minor(rows, columns, v, f):
        total = 0
        for perm in itertools.permutations(range(len(rows))):
            term = f
            for j in reversed(range(len(rows))):
                a, b = rows[perm[j]], columns[j]
                term = e(a, b, term) + (v-j) * term * int(a == b)
                term = sp.expand(term)
            total += signature(perm) * term
        return sp.expand(total)

    def determinant(f):
        return minor(full, full, u, f)

    def cofactor(i, j, v, f):
        return (-1)**(i+j) * minor(tuple(a for a in full if a != i),
                                    tuple(a for a in full if a != j), v, f)

    def double_cofactor(i, l, j, a, v, f):
        if i == l or j == a:
            return 0
        sign = (1 if i < l else -1) * (1 if j < a else -1)
        return sign * (-1)**(i+l+j+a) * minor(
            tuple(t for t in full if t not in (i, l)),
            tuple(t for t in full if t not in (j, a)), v, f)

    functions = [sp.Integer(1), *variables]
    functions.extend(a*b for i, a in enumerate(variables)
                     for b in variables[i:])
    functions.extend([sp.prod(eta), sp.prod(y), eta[0]**3,
                      y[0]**3, eta[0]**2*y[-1]])
    functions = list(dict.fromkeys(functions))
    counts = {'determinant_covector': 0, 'determinant_vector': 0,
              'cofactor_vector': 0, 'mixed_commutator': 0}

    for f in functions:
        df = determinant(f)
        for p in full:
            got = determinant(eta[p]*f)-eta[p]*df
            want = sum(eta[i]*cofactor(i, p, u-1, f) for i in full)
            assert sp.expand(got-want) == 0, (n, 'covector', p, f)
            counts['determinant_covector'] += 1
        for q in full:
            got = determinant(y[q]*f)-y[q]*df
            want = -sum(y[j]*cofactor(q, j, u, f) for j in full)
            assert sp.expand(got-want) == 0, (n, 'vector', q, f)
            counts['determinant_vector'] += 1
        for p, q in itertools.product(full, repeat=2):
            got = (determinant(eta[p]*y[q]*f)
                   - eta[p]*determinant(y[q]*f)
                   - y[q]*determinant(eta[p]*f) + eta[p]*y[q]*df)
            want = sum(eta[i]*y[a]*double_cofactor(i, q, a, p, u-1, f)
                       for i, a in itertools.product(full, repeat=2))
            assert sp.expand(got-want) == 0, (n, 'mixed', p, q, f)
            counts['mixed_commutator'] += 1
        # Check the key intermediate identity independently, with all indices.
        if f in (1, eta[0], y[-1], eta[0]*y[-1]):
            for i, j, l in itertools.product(full, repeat=3):
                got = cofactor(i, j, u, y[l]*f)-y[l]*cofactor(i, j, u, f)
                want = -sum(y[a]*double_cofactor(i, l, j, a, u, f)
                            for a in full)
                assert sp.expand(got-want) == 0, (n, 'cofactor', i, j, l, f)
                counts['cofactor_vector'] += 1

    return {'rank': n, 'test_polynomials': len(functions),
            'symbolic_parameter': 'u', 'identities_checked': counts,
            'status': 'passed'}


def main():
    results = []
    for rank in (1, 2, 3):
        results.append(run_rank(rank))
        print(json.dumps(results[-1]), flush=True)
    report = {
        'scope': 'Finite exact checks in the polynomial differential representation '
                 'E_ab = a_a d/da_b - b_b d/db_a; not a universal proof.',
        'method': 'SymPy exact polynomial arithmetic over Q[u]',
        'sympy_version': sp.__version__,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'manuscript_sha256': hashlib.sha256(
            (ROOT/'paper/sections/new/commutator-matrix.tex').read_bytes()).hexdigest(),
        'results': results,
        'status': 'passed',
    }
    target = ROOT/'certificates/commutator-matrix-check.json'
    target.write_text(json.dumps(report, indent=2) + '\n')
    print(target.relative_to(ROOT))


if __name__ == '__main__':
    main()
