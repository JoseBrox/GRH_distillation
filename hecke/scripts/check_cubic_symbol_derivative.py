#!/usr/bin/env python3
"""Exact local Newton symbol-derivative matrix ranks; no asymptotic estimate."""
import json
Z=(0,0,0); ONE=(1,0,0)
def sub(x,y,q): return tuple((a-b)%q for a,b in zip(x,y))
def add(x,y,q): return tuple((a+b)%q for a,b in zip(x,y))
def mul(x,y,q):
    a,b,c=x; d,e,f=y
    return ((a*d+2*(b*f+c*e))%q,(a*e+b*d+2*c*f)%q,(a*f+b*e+c*d)%q)
def power(a,n,q):
    b=ONE
    while n:
        if n&1: b=mul(b,a,q)
        a=mul(a,a,q); n//=2
    return b
def test(p,m):
    assert pow(2,(p-1)//3,p)!=1
    M=m*(p-1)+1; n=min(p*p-1,2*M+3)
    branches=[(0,0)]+[(j,a) for j in range(m) for a in range(1,p)]
    def pt(j,a,i):
        z=[0,0,0]; z[j]=a+p*i; return tuple(z)
    nodes=[pt(j,a,k//M) for k in range(n+1) for j,a in [branches[k%M]]]
    q=p**max(1,n//M)
    rows=[]
    for j,a in branches:
        for i in range(p):
            x=pt(j,a,i); P,Q=ONE,Z; row=[]
            for k in range(n+1):
                t=k//M
                if t:
                    u=p**(t-1)
                    assert all(c%u==0 for c in Q)
                    row.append(tuple(c//u%p for c in Q))
                if k<n:
                    dx=sub(x,nodes[k],q)
                    Q=add(mul(dx,Q,q),P,q); P=mul(dx,P,q)
            rows.append(row)
    rank=0; cols=n+1-M
    for j in range(cols):
        k=next((i for i in range(rank,len(rows)) if rows[i][j]!=Z),None)
        assert k is not None,(p,m,j)
        rows[rank],rows[k]=rows[k],rows[rank]
        inv=power(rows[rank][j],p**3-2,p)
        piv=[mul(v,inv,p) for v in rows[rank][j:]]
        assert piv[0]==ONE
        for i in range(rank+1,len(rows)):
            a=rows[i][j]
            if a!=Z:
                rows[i][j:]=[sub(x,mul(a,y,p),p) for x,y in zip(rows[i][j:],piv)]
        rank+=1
    return {'p':p,'lines':m,'max_degree':n,'residue_classes':M,'row_count':len(rows),'rank':rank,'prefix_ranks_verified':n+1,'expected':max(0,n+1-M)}
if __name__=='__main__':
    ans=[test(p,m) for p in (7,13) for m in (1,2,3)]
    print(json.dumps({'tests':ans,'scope':'Exact finite symbol-derivative ranks; no global height or prime estimate'},indent=2))
