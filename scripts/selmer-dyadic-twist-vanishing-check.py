#!/usr/bin/env python3
"""Finite exact diagnostics for the Bernoulli-unit and RH rank-four frame proofs.

No finite test proves the all-conductor theorem or computes Selmer lengths.
Requires sympy. Run from any working directory.
"""
import sympy as sp


def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def bernoulli_checks():
    X = sp.Symbol('X')
    cases = [(3,1),(3,3),(3,5),(3,7),(5,1),(5,3),(5,5),(5,7),
             (7,1),(7,3),(7,7),(11,1),(11,5),(13,1),(13,13),(17,1)]
    for ell, f in cases:
        d = 1 if ell % 4 == 1 else 2
        h = v2(ell**d - 1)
        n = (f*4**h - 1).bit_length()
        M = 2**n
        def phi(a):
            return 1 if f == 1 else int(sp.legendre_symbol(a % f, f))
        sums = [sum((u+j*M)*phi(u+j*M) for j in range(f)) for u in range(M)]
        assert all((a-sums[0]) % f == 0 for a in sums)
        g = [(a-sums[0])//f*pow(M,-1,ell) % ell for a in sums]
        S, s = sum(phi(a) for a in range(f)), f*2**h
        assert all((g[u]-g[(u-s)%M]-2**h*S*pow(M,-1,ell)
                    +(phi(u) if u<s else 0)) % ell == 0 for u in range(M))
        order, sign = M//4, -phi(f-1)
        u, coeff = 1, []
        for _ in range(order):
            coeff.append((g[u]+sign*g[-u%M]) % ell)
            u = 5*u % M
        poly = sp.Poly.from_list(coeff[::-1], X, modulus=ell)
        assert sp.gcd(poly, sp.Poly(X**(order//2)+1, X, modulus=ell)).degree() == 0
        assert len({pow(ell**d,j,M) for j in range(M)}) == 2**(n-h)
    return len(cases)


def frame_checks():
    count = 0
    for ell in sp.primerange(3, 212):
        ell = int(ell)
        d = 1 if ell % 4 == 1 else 2
        h = v2(ell**d-1)
        for b in range(11):
            # N >= 2^b is all these numerical inequalities require.
            N = max(4,2**b)
            n = (max(ell*N*4**h, 2**(b+6)*ell**3)-1).bit_length()
            assert n > v2(ell**2-1)+b+1
            assert n > b and n >= 4
            assert 2**n <= 128*N*ell**5
            assert pow(ell, 2**(b+2), 2**n) != 1
            count += 1
    return count


if __name__ == '__main__':
    print('Bernoulli polynomial and difference checks:', bernoulli_checks())
    print('Rank-four threshold checks:', frame_checks())
