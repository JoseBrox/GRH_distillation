#!/usr/bin/env python3
"""Check the recovered bordered Capelli expansion in exact PBW normal form.

The full determinant is expanded independently by permutations of columns.
The right side is the four main terms and two central-root remainder terms
of recovered section 88. Normal ordering uses only the defining gl_n Lie
relations and integer polynomial coefficients in the spectral parameter.
This is a finite-dimensional symbolic check, not a proof for every rank or
an analytic check of restriction/integration. No third-party packages needed.
"""
from pathlib import Path
import hashlib
import argparse
from functools import cache
from itertools import permutations
from collections import defaultdict
import json

@cache
def normal(w):
    for i in range(len(w)-1):
        a,b=w[i];c,d=w[i+1]
        if w[i]>w[i+1]:
            terms=defaultdict(int)
            for key,v in normal(w[:i]+(w[i+1],w[i])+w[i+2:]):terms[key]+=v
            if b==c:
                for key,v in normal(w[:i]+((a,d),)+w[i+2:]):terms[key]+=v
            if d==a:
                for key,v in normal(w[:i]+((c,b),)+w[i+2:]):terms[key]-=v
            return tuple((k,v) for k,v in terms.items() if v)
    return ((w,1),)

def add(*items):
    r=defaultdict(int)
    for x in items:
        for k,v in x.items():r[k]+=v
    return {k:v for k,v in r.items() if v}
def scale(x,s):return {k:s*v for k,v in x.items() if s*v}
def mul(a,b):
    r=defaultdict(int)
    for (wa,pa),va in a.items():
      for (wb,pb),vb in b.items():
       for wc,vc in normal(wa+wb):r[(wc,pa+pb)]+=va*vb*vc
    return {k:v for k,v in r.items() if v}
def prod(*xs):
    r={((),0):1}
    for x in xs:r=mul(r,x)
    return r
def E(a,b):return {(((a,b),),0):1}
def T(a,b,shift):
    r=E(a,b)
    return add(r,{((),1):1,((),0):-shift}) if a==b else r
@cache
def minor(I,J,shift):
    r={}
    for perm in permutations(range(len(I))):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(len(I)) for j in range(i+1,len(I)))
        term=prod(*(T(I[perm[j]],J[j],shift+j) for j in range(len(I))))
        r=add(r,scale(term,sign))
    return r

def check(d, wrong_terminal_shift=False):
    n=d+2;e=0;f=n-1;mid=tuple(range(1,d+1));allidx=tuple(range(n))
    full=minor(allidx,allidx,0)
    rhs=prod(T(e,e,0),minor(mid,mid,1),T(f,f,d if wrong_terminal_shift else d+1))
    for i in mid:
      for j in mid:
        Ih=tuple(t for t in mid if t!=i);Jh=tuple(t for t in mid if t!=j)
        rhs=add(rhs,scale(prod(E(f,j),T(e,e,0),minor(Ih,Jh,1),E(i,f)),-(-1)**(i+j)))
        rhs=add(rhs,scale(prod(E(i,e),minor(Ih,Jh,2),T(f,f,d+1),E(e,j)),-(-1)**(i+j)))
        for ip in mid:
          for jp in mid:
            if i==ip or j==jp:continue
            eps=(1 if i<ip else -1)*(1 if j<jp else -1)*(-1)**(i+ip+j+jp)
            I2=tuple(t for t in mid if t not in (i,ip));J2=tuple(t for t in mid if t not in (j,jp))
            rhs=add(rhs,scale(prod(E(i,e),E(f,j),minor(I2,J2,2),E(e,jp),E(ip,f)),-eps))
    rhs=add(rhs,scale(prod(E(f,e),minor((e,)+mid,mid+(f,),1)),(-1)**(d+1)))
    for i in mid:
      rows=tuple(t for t in mid if t!=i)+(f,)
      rhs=add(rhs,scale(prod(E(i,e),minor(rows,mid,1),E(e,f)),(-1)**(i+d)))
    diff=add(full,scale(rhs,-1))
    return {'d':d,'full_terms':len(full),'rhs_terms':len(rhs),'residual_terms':len(diff),'sample':[(str(k),v) for k,v in list(diff.items())[:5]]}

if __name__=='__main__':
 root=Path(__file__).resolve().parents[1]
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--output',type=Path,default=root/'certificates/bordered-capelli-review-check.json')
 args=parser.parse_args()
 results=[check(d) for d in [1,2,3]]
 assert all(r['residual_terms']==0 for r in results),results
 negative=check(2,wrong_terminal_shift=True)
 assert negative['residual_terms']>0,negative
 source=root/'paper/sections/recovered/88-rr-section.tex'
 report={
  'scope':'Exact PBW coefficient checks of the six-term bordered expansion in middle dimensions 1,2,3; no all-rank or analytic conclusion from finite computation.',
  'method':'Independently expand the full quantum determinant and bordered expression; normal-order every word using [E_ab,E_cd]=delta_bc E_ad-delta_da E_cb. Coefficients are integer polynomials in the symbolic spectral parameter.',
  'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  'recovered_scalar_source':str(source.relative_to(root)),
  'recovered_scalar_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
  'results':results,
  'negative_control':{'change':'First diagonal terminal factor shifted by one in the wrong direction','residual_terms':negative['residual_terms'],'status':'rejected as expected'},
  'status':'passed'
 }
 args.output.parent.mkdir(parents=True,exist_ok=True)
 args.output.write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'status':'passed','middle_dimensions':[1,2,3],'residual_terms':[r['residual_terms'] for r in results],'negative_control_residual_terms':negative['residual_terms'],'certificate':str(args.output.relative_to(root))}))
