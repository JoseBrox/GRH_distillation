#!/usr/bin/env python3
"""Exact finite checks supporting the averaged-error identities.

These finite checks do not prove the general theorems or construct the
required arithmetic data. The proofs and hypotheses are in the manuscript.
"""
from fractions import Fraction as F
A=range(4)
G=[(r,s,a) for r in range(2) for s in range(2) for a in A]
def ch(z,g):
 r,s,a=z; e,h,v=g
 return (-1)**(r*e+s*h+(a&v).bit_count())
def zfun(z,y):
 c=8*z[0]+4*z[1]+z[2]
 return (1+c%3)*y*y+(c-7)*y+F((-1)**c,2)
def weight(u,i,e,a): return F(2+i+e+(a^u),2)
results=[]
for B in [[0],[0,1],[0,1,2,3]]:
 for S in [B[:1],B]:
  T=[0,1,2];m=2;b=F(7);f=8
  X=[z for z in G if all(ch(z,(0,0,u))==1 for u in B)]
  E=Et=Tsg=F(0)
  for u in B:
   for t in T:
    at=F(13+2*t)
    for i in range(m):
     for e in range(2):
      for a in A:
       w=weight(u,i,e,a);phase=(1,1^e,t^a);thick=e==1 and (a^u) in S
       for z in G:
        v=ch(z,phase)*w*zfun(z,at/w);E+=v
        if z in X:Et+=v
        Tsg+=v-ch(z,phase)*(b*zfun(z,at/b) if thick else 0)
  E/=len(B)*f;Et/=len(B)*f;Tsg/=len(B)*f
  Q=sum(F(ch(z,(1,0,t)))*zfun(z,F(13+2*t)/b) for t in T for z in X)/len(T)
  k=F(len(T)*m)*b*F(len(S),4)/2
  assert E==Et and E==k*Q+Tsg
  alpha={z:F(sum(ch(z,(1,0,t)) for t in T),len(T)) for z in X}
  assert sum(alpha.values())==0
  results.append({'B_size':len(B),'S_size':len(S),'E':str(E),'k':str(k)})
z=(0,0,1);E=F(0)
for u in A:
 for e in range(2):
  for a in A:
   w=F(2 if (u,e,a)==(0,1,0) else 1)
   E+=ch(z,(1,1^e,a))*w*(F(6)/w)**2
E/=32
assert E==F(-9,16)
mu=[F(1,2),F(1,3),F(1,6),F(0)];mu0=[F(1,4)]*4
hat=[sum((mu[a]-mu0[a])*(-1)**((h&a).bit_count()) for a in A) for h in A]
assert sum(v*v for v in hat)==4*sum((mu[a]-mu0[a])**2 for a in A)
def leg(n,p):
 r=pow(n%p,(p-1)//2,p)
 return -1 if r==p-1 else r
kernels=[((1+leg(n,3))*(1-leg(n,7)),(1-leg(n,3))*(1-leg(n,7))) for n in range(21)]
assert all(min(v)>=0 for v in kernels)
CHECKS={'fraction_cases':results,'signed_budget':'pass exactly','covariant_projection':'pass exactly','zero_coefficient_sum':'pass exactly','failed_covariance_off_quotient':str(E),'parseval':'pass exactly','quadratic_kernel_residues':21,'quadratic_kernel_nonnegative':'pass exactly'}

if __name__ == '__main__':
 import json
 print(json.dumps(CHECKS, indent=2))

