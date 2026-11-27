#!/usr/bin/env python3
"""Exact scalar checks for the fixed-inducing insertion in Liu v2.
The final sensitivity figures are illustrative numerical quadrature only.
"""
import sympy as s
from fractions import Fraction as Q
import mpmath as mp

# Reference-width and prior-strip margins (all rational).
beta = Q(7,8)
eta = Q(707,1000)
assert 3*(1-eta)>beta
Hmin=Q(47,50); ratio=Q(7,50)
old=Q(101,1000); direct=Q(19,200); packed=Q(7,100)
for name,ell in [('original',old),('improved direct',direct),('packed only',packed)]:
    p=Hmin*(1-4*ratio)-4*ell
    f=Q(5,6)+ell-Q(9,10)
    assert p>0 and f>0
    print(name, 'Poisson reserve:', p, 'fixed-side reserve:', f)
assert Q(5,6)+Q(2,3)*old-Q(9,10)==Q(1,1500)
assert Q(5,6)+eta*direct-Q(9,10)==Q(299,600000)
assert Q(5,6)+packed-Q(9,10)==Q(1,300)
# The relaxed inverse-stage condition and tangent map are independent of eta.
R,r,z,k,w,e=s.symbols('R r z k w e')
Fhigh=s.Rational(5,6)-(s.Rational(5,4)-3*k/2)*w-k*(1+R)/2-k*z
N=5*R/4-s.Rational(5,6); D=R-s.Rational(1,2)-z
assert s.factor(Fhigh.subs(w,R)-(k*D-N))==0
A=(45*R-24)/(R*(45*R-30)); C=(9*R-7)/(R*(45*R-30))
H=r/R; u=(1-H)/6
Y=H*z+u*(1/k-2)
assert s.factor(Y.subs(k,N/D)-z-(r-R)*(A*z+C))==0
v_eps=(z+s.Rational(1,3))/R-D/(6*R*(N-e))
assert s.factor(v_eps.subs(e,0)-A*z-C)==0
assert s.factor(s.diff(v_eps,e).subs(e,0)+D/(6*R*N**2))==0
# Global dual identities of sections 6.2 and 7.3.
B,M,l,b,d,t=s.symbols('B M l b d t')
L0=s.Rational(5,6)+M/12-l/6
LK=s.Rational(1,3)+7*M/12+l/3
Hc=1+3*d/4-(s.Rational(1,2)+d/4)*M+3*d*l/4
weights=[(25*d+8)/(6*(4*d+3)),(4-d)/(6*(4*d+3)),1/(4*d+3)]
Bstar=(14+25*d)/(18+24*d)
assert s.factor(sum(weights)-1)==0
assert s.factor(sum(a*p for a,p in zip(weights,[L0,LK,Hc-t]))-(Bstar-weights[2]*t))==0
Ms=4*(Bstar-weights[2]*t-s.Rational(2,3)); ls=1-Ms
assert all(s.factor(p.subs({M:Ms,l:ls})-(Bstar-weights[2]*t))==0 for p in (L0,LK,Hc-t))
h=1-(M-b)/2+l; ly=(M+b)/2
G0=2*b/3-M/4; mu=s.Rational(37,100)
c0=11*(4-3*mu)/6
cs=[s.Rational(22,3)-25*mu/4,s.Rational(2,3)+mu/4,3*mu/4]
assert s.expand(h-ly-mu*h-c0+sum(a*p for a,p in zip(cs,[L0,LK,L0+G0])))==0
assert c0-sum(cs)*s.Rational(8741,10000)==s.Rational(41671,12000000)
Hhalf=1+5*d/8-(s.Rational(1,2)+d/16)*M+d*b/16+5*d*l/8
qe=19-21*d/2; ve=13/qe; ue=(6-21*d/2)/qe; we=ue/3+5*d*ve/8; ze=d*ve/16+we/2
assert s.factor(B-ve-ue*(B-LK)-ve*(B-Hhalf)-we*(h-2*ly)-ze*b)==0
assert s.Rational(13)/(19-s.Rational(21,2)*s.Rational(21,50))>s.Rational(89,100)
c=s.Rational(1,250); d0=s.Rational(37,100); r0=s.Rational(24257,33000); R0=s.Rational(4471723,6600000)
assert R0+d0*(r0+(1-r0)/2+c)==1
assert R0+d0*(3*r0/2)==(1+5*(3*r0/2))/6
assert r0/2<mu
Hsmall=(1+d0)/2-ly/2+h*((3*R0+1)/4-s.Rational(1,6))+(d0-1)*l/2-d0*(2*ly-h)/8-h*d0*c/4
w1,w2,w3,w4=[s.Rational(57303411,83204812),s.Rational(10501401,83204812),s.Rational(3850000,20801203),s.Rational(3553203,166409624)]
small=s.Rational(72703411,83204812)
assert s.expand(B-small-w1*(B-L0)-w2*(B-LK)-w3*(B-Hsmall)-w4*(s.Rational(7,18)*h-(h-ly)))==0
# Isolate contact and verify sign margins with exact rational intervals.
rlo,rhi=map(s.Rational,['0.7523220538','0.7523220539'])
poly=s.Poly(19**5*(3*r-2)**5*(9*r+2)**5-7*r**4*(r-s.Rational(2,3))*3**5*(45*r-14)**5,r)
assert poly.count_roots(rlo,rhi)==1 and poly.eval(rlo)*poly.eval(rhi)<0
Delt=(45*r-14)/(6+54*r); Br=(99*r-14)/(12*(9*r-1))
assert s.factor(s.diff(Delt,r)-1026/(6+54*r)**2)==0
assert s.factor(s.diff(Br,r)-9/(4*(9*r-1)**2))==0
assert s.Rational(21,50)<Delt.subs(r,rlo)<Delt.subs(r,rhi)<s.Rational(1,2)
assert Br.subs(r,rhi)<small
print('all exact reference, envelope, contact and dual checks passed')
# Numerical (not certified) conditional response of the relaxed envelope.
mp.mp.dps=50
G=lambda x:11*x/16-mp.mpf(7)/24-mp.mpf(5)/16*(7*x**4*(x-mp.mpf(2)/3))**(mp.mpf(1)/5)
delta=lambda x:(45*x-14)/(6+54*x)
req=lambda x:4/(9*delta(x))-mp.mpf(2)/3-x/2
rr=mp.findroot(lambda x:G(x)-req(x),(mp.mpf('.75'),mp.mpf('.76')))
f=lambda x:x**(mp.mpf(4)/5)*(x-mp.mpf(2)/3)**(mp.mpf(1)/5)
num=lambda x:5*x/4-mp.mpf(5)/6
den=lambda x:x-mp.mpf(1)/2-G(x)
J=f(rr)*mp.quad(lambda x:den(x)/(6*x*num(x)**2*f(x)),[rr,mp.mpf(7)/9])
response= -9/(4*(9*rr-1)**2)*J/(mp.diff(G,rr)-mp.diff(req,rr))
print('delta*:',mp.nstr(delta(rr),18))
print('dual weight on numerator plane:',mp.nstr(1/(4*delta(rr)+3),18))
print('hypothetical long-count saving: dG/depsilon=',mp.nstr(J,18),'dBrel/depsilon=',mp.nstr(response,18))
