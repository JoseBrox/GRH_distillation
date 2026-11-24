"""Exact good-prime differential operator checks, not a global norm test."""
from math import comb
from sympy import primerange
import numpy as np


def deriv(f, p, c):
    out = {}
    def add(key, v):
        out[key] = (out.get(key, 0)+v) % p
    for (a, b), v in f.items():
        if b == 0:
            if a: add((a-1, 1), 2*a*v)
        else:
            add((a+2, 0), (2*a+3)*v)
            if a: add((a-1, 0), 2*a*c*v)
    return {k:v for k,v in out.items() if v}


def powers(f, p, c, n):
    ans=[f]
    for _ in range(n): ans.append(deriv(ans[-1], p, c))
    return ans


def basis(m):
    return [(a,b) for b in (0,1) for a in range((m-3*b)//2+1)]


def matrix(p, j, n):
    src, dst = basis(2*n), basis(3*n)
    idx={k:i for i,k in enumerate(dst)}
    M=np.zeros((len(src)*len(dst), n+1), dtype=np.int64)
    for i,k in enumerate(src):
        for z,f in enumerate(powers({k:1},p,2**(2*j),n)):
            for mon,v in f.items(): M[i*len(dst)+idx[mon], z]=v
    return M


def rank(M,p):
    A=M.copy()%p
    r=0
    for j in range(A.shape[1]):
        candidates=np.flatnonzero(A[r:,j])
        if candidates.size==0: continue
        k=r+int(candidates[0])
        A[[r,k]]=A[[k,r]]
        A[r,j:]=(A[r,j:]*pow(int(A[r,j]),-1,p))%p
        # Eliminate below pivot; all products are < p^2.
        A[r+1:,j:]=(A[r+1:,j:]-A[r+1:,j,None]*A[r,j:])%p
        r+=1
        if r==A.shape[0]: break
    return r


results=[]
count=split=total=0
for p in map(int,primerange(5,400)):
    A=comb((p-1)//2,(p-1)//3)%p if p%3==1 else 0
    for j in range(3):
        H=A*pow(2,j*((p-1)//3),p)%p if p%3==1 else 0
        for f in [{(1,0):1},{(0,1):1}]:
            lhs=powers(f,p,2**(2*j),p)[-1]
            rhs={k:H*v%p for k,v in deriv(f,p,2**(2*j)).items() if H*v%p}
            assert lhs==rhs,(p,j,f)
        total+=1
    if p%3==1:
        count+=1
        split+=pow(2,(p-1)//3,p)==1
for p in (7,13,31):
    is_split=pow(2,(p-1)//3,p)==1
    for n in (p-1,p,2*p-2,2*p):
        ms=[matrix(p,j,n) for j in range(3)]
        ranks=[rank(ms[0],p), rank(np.vstack(ms[:2]),p), rank(np.vstack(ms),p)]
        expect=[min(n+1,p),min(n+1,p if is_split else 2*p-1),min(n+1,p if is_split else 3*p-2)]
        assert ranks==expect,(p,n,ranks,expect)
        results.append({'p':p,'n':n,'split':is_split,'ranks':ranks})
if __name__=='__main__':
    import json
    print(json.dumps({'curve_prime_checks':total,'degree_one_primes_checked':count,'cubic_split_primes':split,'matrix_tests':results,'scope':'Exact finite Hasse identities and ranks only.'},indent=2))
