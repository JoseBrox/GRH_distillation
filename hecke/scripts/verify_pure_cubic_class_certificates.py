#!/usr/bin/env python3
"""Unconditional class-number divisibility certificates for Q(cuberoot(2),sqrt(-q)).

Verify using integer arithmetic and exact Hermite normal forms (SymPy).
The known maximal order is the product basis (coprime discriminants).
See hecke/notes/pure-cubic-class-certificates.md for the proof and scope.
"""
from itertools import product
from math import isqrt
from fractions import Fraction
import json, sys
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form

I=s.eye(6); units=[tuple(int(x) for x in I[:,i]) for i in range(6)]

def prime_list(n):
    return [p for p in range(2,n+1) if all(p%a for a in range(2,isqrt(p)+1))]

def norm_c(x):
    a,b,c=x; return a*a*a+2*b*b*b+4*c*c*c-6*a*b*c

def cmul(x,y):
    a,b,c=x; d,e,f=y
    return (a*d+2*(b*f+c*e),a*e+b*d+2*c*f,a*f+b*e+c*d)

def emul(x,y,q):
    m=(q+1)//4
    ac,bd,ad,bc=cmul(x[:3],y[:3]),cmul(x[3:],y[3:]),cmul(x[:3],y[3:]),cmul(x[3:],y[:3])
    return tuple(ac[i]-m*bd[i] for i in range(3))+tuple(ad[i]+bc[i]+bd[i] for i in range(3))

def enorm(x,q):
    m=(q+1)//4; a,b=x[:3],x[3:]; aa,ab,bb=cmul(a,a),cmul(a,b),cmul(b,b)
    return abs(norm_c(tuple(aa[i]+ab[i]+m*bb[i] for i in range(3))))

def multmat(x,q):
    return s.Matrix.hstack(*(s.Matrix(emul(x,y,q)) for y in units))

def factor_cubic(p):
    # Monic factors, ascending coefficient order; distinct factors only.
    coeff=[(-2)%p,0,0,1]; factors=[]
    for a in range(p):
        if sum(x*pow(a,i,p) for i,x in enumerate(coeff))%p:continue
        factors.append(((-a)%p,1))
        while len(coeff)>1 and sum(x*pow(a,i,p) for i,x in enumerate(coeff))%p==0:
            div=[0]*(len(coeff)-1);div[-1]=coeff[-1]
            for i in range(len(div)-2,-1,-1):div[i]=(coeff[i+1]+a*div[i+1])%p
            coeff=div
    if len(coeff)>1:factors.append(tuple(coeff))
    return factors

def fmul(x,y,g,p):
    n=len(g)-1; z=[0]*(2*n-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y):z[i+j]+=a*b
    for i in range(len(z)-1,n-1,-1):
        for j in range(n):z[i-n+j]-=z[i]*g[j]
    return tuple(a%p for a in z[:n])

def fpowers(g,p):
    f=len(g)-1; one=(1,)+(0,)*(f-1); a=((-g[0])%p,) if f==1 else (0,1)+(0,)*(f-2)
    return [one,a,fmul(a,a,g,p)]

def kernel_lattice(M,p):
    """HNF basis of {x in Z^6 : Mx=0 mod p}; rows span quotient."""
    A=[list(map(lambda x:int(x)%p,row)) for row in M]; r=0; piv=[]
    for j in range(6):
        k=next((k for k in range(r,len(A)) if A[k][j]),None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]; inv=pow(A[r][j],-1,p); A[r]=[x*inv%p for x in A[r]]
        for i in range(len(A)):
            if i!=r:
                c=A[i][j]; A[i]=[(a-c*b)%p for a,b in zip(A[i],A[r])]
        piv.append(j); r+=1
        if r==len(A):break
    assert r==len(M)
    cols=[]
    for j in range(6):
        col=[0]*6
        if j in piv:col[j]=p
        else:
            col[j]=1
            for i,k in enumerate(piv):col[k]=-A[i][j]
        cols.append(s.Matrix(col))
    return hermite_normal_form(s.Matrix.hstack(*cols))

def primes(q,B):
    m=(q+1)//4; out=[]
    for p in prime_list(B):
        for g in factor_cubic(p):
            f=len(g)-1
            if p**f>B:continue
            ps=fpowers(g,p); one=ps[0]
            # Factor beta^2-beta+m over F_{p^f} by exhaustive root search.
            # p^f <= B by construction. All residue fields enumerated are small.
            roots=[]
            for b in product(range(p),repeat=f):
                bb=fmul(b,b,g,p)
                if all((bb[i]-b[i]+m*one[i])%p==0 for i in range(f)):roots.append(b)
            if roots:
                for b in roots:
                    cols=ps+[fmul(x,b,g,p) for x in ps]
                    M=list(map(list,zip(*cols)))
                    out.append(dict(p=p,f=f,g=g,b=b,M=M))
            elif p**(2*f)<=B:
                cols=[x+(0,)*f for x in ps]+[(0,)*f+x for x in ps]
                out.append(dict(p=p,f=2*f,g=g,b=None,M=list(map(list,zip(*cols)))))
    for P in out:
        P['H']=kernel_lattice(P['M'],P['p']);assert P['H'].det()==P['p']**P['f']
    return out

def contains(P,x):
    return all(sum(a*b for a,b in zip(row,x))%P['p']==0 for row in P['M'])

def ideal_mul(A,B,q):
    cols=[s.Matrix(emul(tuple(int(x) for x in A[:,i]),tuple(int(x) for x in B[:,j]),q)) for i in range(6) for j in range(6)]
    return hermite_normal_form(s.Matrix.hstack(*cols))

def bound(q):
    # Certified rational upper bound on Minkowski bound using pi>157/50.
    # sqrt(q) < ceil(sqrt(q)*10^6)/10^6; no floats.
    sq=Fraction(isqrt(q*10**12)+1,10**6)
    return int(Fraction(200,157)**3*Fraction(720,6**6)*108*q*sq)

def row_for_element(Ps,x,q):
    # Reconstruct candidate ideal exponents from norm and residue tests.
    # Ambiguous cases are rejected. The final HNF identity certifies the row.
    N=enorm(x,q); nn=N; assert N>0
    row=[0]*len(Ps)
    for p in sorted(set(P['p'] for P in Ps)):
        if nn%p:continue
        k=0
        while nn%p==0:nn//=p;k+=1
        hits=[i for i,P in enumerate(Ps) if P['p']==p and contains(P,x)]
        assert hits
        if len(hits)==1:
            f=Ps[hits[0]]['f'];assert k%f==0
            row[hits[0]]=k//f
        else:
            assert sum(Ps[i]['f'] for i in hits)==k
            for i in hits:row[i]=1
    assert nn==1
    A=I
    for P,e in zip(Ps,row):
        for _ in range(e):A=ideal_mul(A,P['H'],q)
    M=multmat(x,q)
    assert A==hermite_normal_form(M)
    assert abs(int(M.det()))==N
    assert N==int(s.prod(P['p']**(P['f']*e) for P,e in zip(Ps,row)))
    return row

def verify(cert):
    q,ell=cert['q'],cert['ell'];assert q>3 and q%4==3 and q in prime_list(q)
    assert ell in prime_list(ell)
    B=bound(q);assert B==cert['minkowski_bound'] and cert['discriminant']==-108**2*q**3
    Ps=primes(q,B);n=len(Ps)
    assert n==cert['generator_count']==len(cert['elements'])
    rows=[]
    for x in cert['elements']:
        assert len(x)==6 and all(type(a)==int for a in x)
        rows.append(row_for_element(Ps,x,q))
    det=abs(int(s.polys.matrices.DomainMatrix.from_Matrix(s.Matrix(rows)).det()))
    assert det==cert['relation_det'] and det%ell!=0
    # Since prime ideal classes of norm <= B generate, h divides det.
    return {'q':q,'discriminant':cert['discriminant'],'bound':B,'generators':n,'class_number_divides':det}

if __name__=='__main__':
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'certificates'/'pure-cubic-class-certificates.json'
    for cert in json.load(path.open()):print(json.dumps(verify(cert)),flush=True)
