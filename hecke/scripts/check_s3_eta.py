#!/usr/bin/env python3
"""Exact finite checks supplementing the S3 eta identity (not a zero test)."""
from math import isqrt

X = 30_000
# Enumerate the primary generator of every ideal prime to 6.
c, d, e = ([0] * (X + 1) for _ in range(3))
B = isqrt(4 * X // 3) + 2
for b in range(-B, B + 1):
    if b % 3:
        continue
    for a in range(-B, B + 1):
        if a % 3 != 1 or (a % 2 == 0 and b % 2 == 0):
            continue
        N = a*a - a*b + b*b
        if 1 <= N <= X:
            if b % 2 == 0:
                c[N] += 1
            elif a % 2 == 0:
                d[N] += 1
            else:
                e[N] += 1
assert d == e
coeff = [c[j] - e[j] for j in range(X + 1)]
# Independently enumerate the two pentagonal series.
eta = [0] * (X + 1)
B = isqrt(4 * X) + 2
lo, hi = -(B + 1)//6 - 1, (B + 1)//6 + 1
for m in range(lo, hi + 1):
    u = 6*m - 1
    for n in range(lo, hi + 1):
        v = 6*n - 1
        N = (u*u + 3*v*v)//4
        if N <= X:
            eta[N] += (-1 if (m+n) % 2 else 1)
assert eta == coeff
# Sieve primes; compare independent form and cube tests.
prime = bytearray(b'\x01') * (X + 1)
prime[0:2] = b'\x00\x00'
for p in range(2, isqrt(X) + 1):
    if prime[p]:
        prime[p*p:X+1:p] = b'\x00' * ((X-p*p)//p+1)
count = split = 0
for p in range(5, X + 1):
    if not prime[p]:
        continue
    count += 1
    represented = any(isqrt(p-27*b*b)**2 == p-27*b*b
                      for b in range(isqrt(p//27)+1))
    cube = p % 3 == 1 and pow(2, (p-1)//3, p) == 1
    assert represented == cube, p
    assert eta[p] == (2 if cube else -1 if p % 3 == 1 else 0), p
    split += cube
print(f'All coefficients agree through {X}; {count} primes p>3 checked; {split} split completely.')
