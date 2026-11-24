#!/usr/bin/env python3
"""Exact finite checks of CP2, CP4, fixed spectrum fields and resonance.
These are diagnostics, not a proof of automorphy or of the Selmer bound.
"""
from math import gcd, isqrt
import sympy as s

W = ((1, 1), (0, 1), (1, 0), (0, 0))
A,P,B,H = (1,0),(0,1),(-1,1),(1,1)
neg=lambda w: tuple(-a for a in w)
ma,mp,mb,mh = map(neg,(A,P,B,H))
R={A,P,B,H,ma,mp,mb,mh}
def weight(i,j): return tuple(a-b for a,b in zip(W[i],W[j]))
rows=[{B,mb,ma,mh,mp},{B,mb,A,H,P},{H,mh,P,B,ma},
      {H,mh,mp,mb,A},{A,ma,mh,mp,mb},{A,ma,H,P,B},
      {P,mp,B,ma,mh},{P,mp,mb,A,H},{B,mb,H,mh}]
actual=set()
for mask in range(1,15):
    I={i for i in range(4) if mask>>i&1}
    J=set(range(4))-{3-i for i in I}
    forbidden={weight(i,j) for V in (I,J) for j in V for i in set(range(4))-V}
    actual.add(frozenset(R-forbidden))
assert actual=={frozenset(row) for row in rows}
for S in rows:
    if (mp in S and (B in S or ma in S)) or {ma,mb}<=S:
        assert len(S&{A,B,H})<=1
special={i+1 for i,S in enumerate(rows) if ma in S or {B,mh}<=S}
assert special=={1,3,5,6,7,9}
for i,w in [(1,ma),(3,ma),(5,A),(6,A),(7,ma),(9,H)]:
    S=rows[i-1]-{w}
    assert not {ma,B,mh}<=S and len(S&{A,mb,H})<=1
print('CP2: all 14 coordinate subsets, nine loci, both strictness tables pass')

J=s.Matrix([[0,0,0,1],[0,0,1,0],[0,-1,0,0],[-1,0,0,0]])
a,b,c,d,e,f,g,h,i,j,z=s.symbols('a b c d e f g h i j z')
Q=s.Matrix([[a,b,c,d],[b,e,f,g],[c,f,h,i],[d,g,i,j]])
X=-J*Q
assert X.T*J+J*X==s.zeros(4)
N=s.eye(4);N[2,0]=z;N[3,1]=z
assert N.T*J*N==J
T=N.inv()*X*N
assert s.expand(T[1,0]-(X[1,0]+z*X[1,2]))==0
assert s.expand(T[3,0]+2*z*T[1,0]-(X[3,0]+z*z*X[1,2]))==0
assert s.expand(T[2,1]-(X[2,1]-2*z*X[0,1]-z*z*X[0,3]))==0
print('CP4: symplectic and lower-entry identities over Z[z] pass')

for D, primes in [(-7,(11,23,29,37)),(-11,(23,31,37,47)),(-19,(7,11,17,23)),(-43,(11,13,17,23))]:
    forms=[]
    for aa in range(1,isqrt(abs(D)//3)+1):
        for bb in range(-aa,aa+1):
            if (bb*bb-D)%(4*aa):continue
            cc=(bb*bb-D)//(4*aa)
            if aa>cc or gcd(gcd(aa,bb),cc)!=1:continue
            if (abs(bb)==aa or aa==cc) and bb<0:continue
            forms.append((aa,bb,cc))
    assert len(forms)==1
    for p in primes: assert s.isprime(p) and pow(D%p,(p-1)//2,p)==1
print('FS4: four class-number-one fields and all sixteen split primes pass')

for ee in range(2,501):
    ps=[p for p in range(3,2*ee+2,2) if 2*ee%(p-1)==0 and s.isprime(p)]
    assert len(ps)<=2*ee+1 and sum(8*p*p for p in ps)<=8*(2*ee+1)**3
print('Resonant enumeration: all twists 2..500 pass (diagnostic only)')
