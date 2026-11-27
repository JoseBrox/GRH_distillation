#!/usr/bin/env python3
"""Exact local checks for Liu, Hexagon 2611.00421v2, sections 6–7.
Requires SymPy. Not a check of the analytic induction or all comparisons.
"""
import sympy as s
r,B,delta,M,ell,z,t=s.symbols('r B delta M ell z t')
Q=s.Poly(19**5*(3*r-2)**5*(9*r+2)**5-7*r**4*(r-s.Rational(2,3))*3**5*(45*r-14)**5,r)
q,rem=s.div(Q,s.Poly(3*r-2,r)); assert rem.is_zero
P=s.Poly(s.together(q.as_expr().subs(r,(12*B-14)/(108*B-99))).as_numer_denom()[0],B).primitive()[1]
if P.LC()<0: P=-P
assert P.all_coeffs()==[487371101862528,-4126408710053184,15517896164111592,-34020380857037616,47916748658170215,-44964545308854309,28111661257098222,-11291220876239226,2643837682856883,-274959111914881]
lo,hi=map(s.Rational,['0.87334585610671857680','0.87334585610671857681'])
assert P.count_roots(lo,hi)==1 and P.eval(lo)*P.eval(hi)<0
assert s.Poly(q,r).count_roots(s.Rational('0.7523220538'),s.Rational('0.7523220539'))==1
# Rabin criterion over F_11: degree 9 has sole prime divisor 3.
f=s.Poly(P,B,modulus=11).monic(); x=s.Poly(B,B,modulus=11)
assert f.degree()==9
def powmod(a,n):
    out=s.Poly(1,B,modulus=11)
    while n:
        if n&1: out=(out*a).rem(f)
        n//=2; a=(a*a).rem(f)
    return out
h=x
for i in range(1,10):
    h=powmod(h,11)
    if i==3: assert s.gcd(h-x,f).degree()==0
assert h==x
# Exact rational bisection; signs from Horner evaluation by SymPy.
for _ in range(180):
    m=(lo+hi)/2
    if P.eval(lo)*P.eval(m)<=0: hi=m
    else: lo=m
assert hi-lo<s.Rational(1,10**70)
print('endpoint (rounding displayed, exact bracket width < 1e-70):',s.N((hi+lo)/2,70))
# Differential identities with H'/H and H''/H, avoiding branch simplification.
a=(45*r-24)/(r*(45*r-30)); b=(9*r-7)/(r*(45*r-30))
L=s.Rational(4,5)/r+s.Rational(1,5)/(r-s.Rational(2,3))
assert s.factor(s.diff(L,r)+L**2+16/(25*r**2*(3*r-2)**2))==0
assert s.factor(L-a)==0
assert s.factor(s.Rational(11,16)-a*(11*r/16-s.Rational(7,24))-b)==0
k=(5*r/4-s.Rational(5,6))/(r-s.Rational(1,2)-z)
Y=t/r*z+(1/k-2)*(1-t/r)/6
assert s.factor(Y-z-(t-r)*(a*z+b))==0
# LP dual lower bound and unique intersection.
L0=s.Rational(5,6)+M/12-ell/6
LK=s.Rational(1,3)+7*M/12+ell/3
H=1+3*delta/4-(s.Rational(1,2)+delta/4)*M+3*delta*ell/4
u=(25*delta+8)/(6*(4*delta+3)); v=(4-delta)/(6*(4*delta+3)); w=1/(4*delta+3)
D=(14+25*delta)/(18+24*delta)
assert s.factor(u+v+w-1)==0 and s.factor(u*L0+v*LK+w*H-D)==0
sol=s.solve([L0-LK,L0-H],[M,ell]); assert s.factor(L0.subs(sol)-D)==0
print('dual equality point:',{str(k):s.factor(v) for k,v in sol.items()})
d=(45*r-14)/(6+54*r); br=(99*r-14)/(12*(9*r-1))
assert s.factor(D.subs(delta,d)-br)==0
assert s.factor(s.diff(br,r)-9/(4*(9*r-1)**2))==0
print('all endpoint, irreducibility, differential, tangent, and dual checks passed')
