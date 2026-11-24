#!/usr/bin/env python3
"""Exact diagnostic for the s=s'=0 mixed-multiplicity calculation."""
from math import comb
from functools import lru_cache
from itertools import product

@lru_cache(None)
def H(r, rp, d0, d1, d2):
    if min(d0, d1, d2) < 0:
        return 0
    a, b = 2*d0+4*d2, 2*d1+2*d2
    return comb(a+r-1,r-1)*sum(comb(b-2*j+rp,rp) for j in range(b//2+1))

count = 0
for r, rp in product(range(1,7),range(0,6)):
    for d0,d1,d2 in product(range(8,11),range(8,11),range(4,7)):
        got = sum((-1)**(i+j+k)*comb(r-1,i)*comb(rp,j)*H(r,rp,d0-i,d1-j,d2-k)
                  for i in range(r) for j in range(rp+1) for k in range(2))
        assert got == 2**(r-1+rp), (r,rp,d0,d1,d2,got)
        count += 1
print('mixed-multiplicity checks:', count)
