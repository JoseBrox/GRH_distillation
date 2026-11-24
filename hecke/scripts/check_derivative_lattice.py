#!/usr/bin/env python3
"""Exact small-degree tests in the S3 splitting field. Requires SymPy 1.14.

This checks global value/derivative preimage indices by modular integer HNF.
The first-divided-difference index is calculated from the proved local
formula, not from a second independent HNF. No asymptotic or zero check.
"""
import json
from itertools import product
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form
from sympy.polys.numberfields import round_two, prime_decomp

# Raw basis: omega^i alpha^j, i=0,1 and j=0,1,2.
# Integral basis: 1,omega,alpha,omega*alpha,beta,omega*beta,
# beta=(1+alpha)^2/(1-omega).
B = s.zeros(6)
for i in range(4):
    B[i, i] = 1
B[:, 4] = s.Matrix([2, 1, 4, 2, 2, 1])/3
B[:, 5] = s.Matrix([-1, 1, -2, 2, -1, 1])/3
Bi = B.inv()


def rawmul(v, w):
    out = [0]*6
    for j, i in product(range(3), range(2)):
        for k, ell in product(range(3), range(2)):
            c = v[2*j+i]*w[2*k+ell]
            if not c:
                continue
            a, b = j+k, i+ell
            if a >= 3:
                a -= 3
                c *= 2
            if b == 2:
                out[2*a] -= c
                out[2*a+1] -= c
            else:
                out[2*a+b] += c
    return s.Matrix(out)


mult = []
for a in range(6):
    mat = Bi*s.Matrix.hstack(*(rawmul(B[:, a], B[:, b]) for b in range(6)))
    assert all(v.q == 1 for v in mat)
    mult.append(mat)
assert s.Matrix(6, 6, lambda i, j: s.trace(mult[i]*mult[j])).det() == -34992

# Independent maximal-order computation and prime ideal norms.
x, y = s.symbols('x y')
T = s.Poly(s.resultant(x**3-2, (y-x)**2+(y-x)+1, x), y)
ZK, disc = round_two(T)
assert disc == -34992
norms = []
for p in s.primerange(2, 14):
    norms.extend(int(p)**int(P.f) for P in prime_decomp(p, T, ZK=ZK, dK=disc))

# 76 deterministic nodes, including the rational nodes 0,...,13.
S = {(j,0,0,0,0,0) for j in range(14)}
S.update(product(range(2), repeat=6))
S = sorted(S, key=lambda v: (sum(abs(x) for x in v), v))
assert len(S) == 76


def expected(n, r):
    result = 1
    for q in norms:
        power = q
        while power <= n:
            result *= q**sum(max(i//power-r, 0) for i in range(n+1))
            power *= q
    return result


def hnf_index(blocks, n):
    A = s.Matrix.vstack(*blocks)
    assert all(v.q == 1 for v in A)
    # Determinant of the square rational-node value submatrix is a
    # certified multiple of the full row-lattice index.
    modulus = int(s.prod(s.factorial(j)**6 for j in range(1,n+1)))
    H = hermite_normal_form(A.T.applyfunc(int), D=modulus)
    assert H.shape == (6*(n+1),)*2
    return abs(int(H.det()))


results = []
for n in (3,4,5,6,7,8,9,10):
    values, derivatives = [], []
    for v in S:
        M = sum((int(a)*m for a,m in zip(v,mult)), s.zeros(6))
        powers = [s.eye(6)]
        for k in range(n):
            powers.append(powers[-1]*M)
        values.append(s.Matrix.hstack(*powers))
        derivatives.append(s.Matrix.hstack(s.zeros(6),
                           *[k*powers[k-1] for k in range(1,n+1)]))
    a = hnf_index(values, n)
    b = hnf_index(values+derivatives, n)
    c = expected(n, 1)
    # Equality with the proved local value formula certifies that S
    # tests the whole degree-n value lattice, also for derivatives.
    assert a == expected(n, 0)
    assert a % b == 0 and b % c == 0
    # Degree-one prime 3, when it is above sqrt(n).
    if n < 9:
        assert (b//c) % 3 != 0
    results.append(dict(n=n, value_minor_norm=a,
                        derivative_minor_norm=b,
                        divided_difference_minor_norm_formula=c,
                        derivative_relative_index=a//b,
                        divided_difference_relative_index_formula=a//c,
                        difference_factor=b//c))
print(json.dumps(dict(sympy_version=s.__version__, discriminant=int(disc),
                      nodes=len(S), prime_ideal_norms=sorted(norms),
                      results=results), indent=2))
