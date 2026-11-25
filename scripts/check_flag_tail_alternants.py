"""Finite diagnostics for the flag-tail alternant proof; not a general proof."""
from fractions import Fraction as F
from math import factorial, comb, prod
import sympy as s

def wedge_step(a, shifts):
    out = {}
    for j, b in enumerate(a):
        c = shifts(b)
        if c < 0 or c in a[:j]+a[j+1:]:
            continue
        v = a[:j]+(c,)+a[j+1:]
        sig = (-1)**sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v)))
        v = tuple(sorted(v))
        out[v] = out.get(v,0)+sig
    return {v:c for v,c in out.items() if c}

ncomm = nhook = nres = 0
for N in range(1,25):
    v = tuple(range(N))
    for k in range(1,N+1):
        for m in range(1,N+1):
            out = {}
            for a,c in wedge_step(v,lambda i:i+k).items():
                for b,d in wedge_step(a,lambda i:i-m).items():
                    out[b]=out.get(b,0)+c*d
            assert {b:d for b,d in out.items() if d} == ({v:k} if m==k else {})
            ncomm += 1
        for r in range(k):
            shape=[k-r]+[1]*r
            def dimension(n):
                return prod(F(n+j-i,shape[i]-j+sum(l>j for l in shape[i+1:]))
                            for i in range(len(shape)) for j in range(shape[i]))
            c=F(factorial(N-1-r),factorial(N-1-r+k))
            assert c*dimension(N)==F(comb(k-1,r),factorial(k))
            assert dimension(N+1+k)<=2*4**k*dimension(N)
            nhook+=1

# Check confluent residue formula for H=1 and power sums of degrees 1..4.
t,z,e=s.symbols('t z e')
for p,q in [(2,1),(2,2),(3,2),(3,3)]:
    N=p+q
    a=[e*i for i in range(p)]+[1+e*i for i in range(q)]
    I=list(range(p,N))
    for k in range(5):
        def H(x): return 1 if k==0 else sum(v**k for v in x)
        terms=[]
        for i in I:
            shifted=a.copy();shifted[i]+=t
            terms.append(prod((a[i]+t-a[j])/(a[i]-a[j]) for j in range(N) if i!=j)*H(shifted))
        tt=s.Rational(1,7)
        lhs=s.limit(s.cancel(sum(terms).subs(t,tt)),e,0)
        expr=(1+tt/(1+z))**p*(1 if k==0 else q+(1+z+tt)**k-(1+z)**k)
        rhs=sum(comb(q,l)*tt**(l-1)*s.diff(expr,z,l-1).subs(z,0)/factorial(l-1) for l in range(1,q+1))
        assert lhs==rhs,(p,q,k,lhs,rhs)
        nres+=1
assert F(7,2)*F(129,1024)/(1-F(129,1024))<1
assert 7*13*16*F(1,2)/(2*(1-F(1,2)))==728
print(f'exterior cases={ncomm}; hook cases={nhook}; residue cases={nres}; rational constants passed')
