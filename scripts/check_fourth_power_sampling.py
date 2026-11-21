#!/usr/bin/env python3
"""Exact checks supplementing the fourth-power interpolation proof.

The universal argument is in the note and TeX fragment. These checks
verify its delicate algebra, endpoint coverage, signed cancellation and
error integration. They do not supply the arithmetic table or verify RH.
"""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = "notes/fourth-power-sampling.md"
FRAGMENT = "paper/shared/fourth-power-sampling.tex"
CERT = "certificates/fourth-power-sampling.json"
DEPENDENCIES = [
    ("paper/sections/recovered/03-sec-one-sided.tex", 337, 381,
     "ce3e87093500a6e5235d7efd687f7f8832ec60c33d8b8bce154eb4dbfeca0fcf"),
    ("paper/rh/sections/01-introduction.tex", 31, 60,
     "96606f00a60113d4b636dc162c243ed3b1c21ab0d35f87b2b692e8e97c759c63"),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def ceil(q):
    return -(-q.numerator // q.denominator)


def ramp(x, m):
    return max(x / m - 1, F(0))


def ramp_checks():
    cases = 0
    for u in [F(1), F(7, 3), F(9, 2), F(16), F(257, 7)]:
        for delta in [F(1, 4), F(3, 2), F(7), F(65), F(175)]:
            v = u + delta
            for m in range(max(1, int(u) - 1), ceil(v) + 2):
                peak = ((m-u)*(v-m)/(m*delta)
                        if u < m < v else F(0))
                assert 0 <= peak <= delta/(4*u)
                points = [u, v, (u+v)/2, u+delta/7, u+6*delta/7]
                if u < m < v:
                    points.append(F(m))
                for x in points:
                    chord = ((v-x)*ramp(u,m)+(x-u)*ramp(v,m))/delta
                    gap = chord-ramp(x,m)
                    assert 0 <= gap <= peak
                    if x == m and u < m < v:
                        assert gap == peak
                    cases += 1
    return cases


def grid_checks():
    m = sp.symbols("m", nonnegative=True)
    n = m+2
    delta = (n+1)**4-n**4
    polynomial = sp.Poly(sp.expand(9*n**3-delta-1),m)
    assert polynomial.as_expr() == 5*m**3+24*m**2+32*m+6
    assert all(c > 0 for c in polynomial.all_coeffs())
    cases = 0
    for n in [*range(2,100),1000,10**6]:
        a, b = n**4,(n+1)**4
        delta = b-a
        assert delta+1 <= 9*n**3
        assert F(delta*(delta+1),a) <= 81*n*n
        # The logarithmic bound follows analytically from log(1+t)<=t.
        assert F(4,n) <= 2
        for scale in [F(1),F(1001,1000),F(3,2),F(4),F(17)]:
            assert (scale*delta)*(scale*delta+1)/(scale*a) <= (
                scale*delta*(delta+1)/a)
            cases += 1
    return cases


def endpoint_checks():
    cases = exact_endpoints = 0
    for N in range(2,12):
        for upper_index in [F(N)+F(1,3),F(N+1),F(N*N)]:
            L = ceil(upper_index)
            assert L**4 >= upper_index**4
            for q in [F(1),F(1001,1000),F(3,2),F(2),F(7,3)]:
                # q=exp(h/4), including h=0 exactly.
                K = ceil(q*L)
                for n in range(N,L+1):
                    if q == 1:
                        assert N <= n <= K
                    else:
                        final = q*n
                        cells = range(n,ceil(final))
                        assert cells.start == n
                        assert cells.stop-1 < final
                        for k in cells:
                            lo,hi = F(k),min(F(k+1),final)
                            assert lo < hi
                            assert N <= k < k+1 <= K
                            assert n**4 <= lo**4 < hi**4 <= (q*n)**4
                        if final.denominator == 1:
                            exact_endpoints += 1
                            assert cells.stop == final
                            assert cells.stop <= K
                    cases += 1
    return cases,exact_endpoints


def hat_and_cancellation_checks():
    x,z,a,b,h = sp.symbols("x z a b h",positive=True)
    alpha,beta = sp.symbols("alpha beta",real=True)
    left = (b*(beta-alpha)-x*(sp.exp(beta)-sp.exp(alpha)))/(h*(b-a))
    right = (x*(sp.exp(beta)-sp.exp(alpha))-a*(beta-alpha))/(h*(b-a))
    assert sp.simplify(left+right-(beta-alpha)/h) == 0
    # Any affine table is reproduced exactly by its hat interpolant.
    s,t = sp.symbols("s t",real=True)
    assert sp.simplify((b-z)/(b-a)*(s*a+t)+(z-a)/(b-a)*(s*b+t)
                       -(s*z+t)) == 0
    cases = 0
    for n in [2,3,7,10]:
        h = sp.log(16)
        weights = {k:sp.S(0) for k in range(n,2*n+1)}
        for k in range(n,2*n):
            a,b = sp.Integer(k**4),sp.Integer((k+1)**4)
            width = sp.log(b/a)
            weights[k] += (b*width-(b-a))/(h*(b-a))
            weights[k+1] += ((b-a)-a*width)/(h*(b-a))
        assert sp.expand_log(sum(weights.values()),force=True).simplify() == 1
        center = sp.Integer(15*n**4)/h
        cancellation = sum(weights[k]*(k**4-center) for k in weights)
        assert sp.expand_log(cancellation,force=True).simplify() == 0
        # For h=log16, 1<15/h<16 follows from 15/16<log16<15.
        # Therefore this affine table has both signs although its row is zero.
        # Averaging its positive part is strictly positive by integration.
        cases += 1
    return cases


def quadrature_and_tail_checks():
    x,Y,delta,c = sp.symbols("x Y delta c",positive=True)
    h = sp.symbols("h",nonnegative=True)
    phi = sp.sqrt(x)*(3+h+sp.log(x))
    assert sp.simplify(sp.diff(phi,x,2)+(3+h+sp.log(x))/(4*x**sp.Rational(3,2))) == 0
    assert sp.simplify(sp.diff(sp.sqrt(x),x,2)+1/(4*x**sp.Rational(3,2))) == 0
    tail = Y**(-delta)*((c+sp.log(Y))/delta+1/delta**2)
    assert sp.simplify(sp.diff(tail,Y)+Y**(-delta-1)*(c+sp.log(Y))) == 0
    assert sp.limit(tail,Y,sp.oo) == 0
    theta = sp.symbols("theta",positive=True)
    s,t = sp.symbols("s t",real=True)
    primitive = s*x**(1-theta)/(1-theta)-t*x**(-theta)/theta
    assert sp.simplify(sp.diff(primitive,x)-(s*x+t)*x**(-1-theta)) == 0
    cases = 0
    # Exact rational positive intervals verify the clipping rule, including
    # zero rows, one zero endpoint, and a crossing in either direction.
    for a,b in [(F(16),F(81)),(F(81),F(256))]:
        for u in map(F,[-3,-1,0,1,3]):
            for v in map(F,[-3,-1,0,1,3]):
                slope=(v-u)/(b-a)
                intercept=(b*u-a*v)/(b-a)
                if u <= 0 and v <= 0:
                    interval=None
                elif u >= 0 and v >= 0:
                    interval=(a,b)
                else:
                    root=-intercept/slope
                    assert a <= root <= b
                    interval=(root,b) if slope > 0 else (a,root)
                for i in range(21):
                    at=a+(b-a)*F(i,20)
                    positive=max(slope*at+intercept,F(0))
                    selected=(slope*at+intercept if interval is not None
                              and interval[0] <= at <= interval[1] else F(0))
                    assert positive == selected
                cases += 1
    return cases


def main():
    dependencies=[]
    for path,lo,hi,expected in DEPENDENCIES:
        excerpt=b"".join((ROOT/path).read_bytes().splitlines(keepends=True)[lo-1:hi])
        assert hi-lo+1 <= 120 and sha(excerpt) == expected,path
        dependencies.append({"path":path,"start":lo,"end":hi,"sha256":expected})
    endpoints,exact_endpoints=endpoint_checks()
    results={
        "rational_ramp_chord_cases":ramp_checks(),
        "grid_and_scaled_interval_cases":grid_checks(),
        "finite_table_endpoint_cases":endpoints,
        "exact_upper_endpoint_cases":exact_endpoints,
        "exact_signed_affine_cancellation_cases":hat_and_cancellation_checks(),
        "positive_interval_clipping_cases":quadrature_and_tail_checks(),
        "symbolic_checks":["grid polynomial with positive coefficients",
            "positive hat row mass and affine reproduction",
            "concavity of sqrt(x) and sqrt(x)*(3+h+log(x))",
            "affine-cell antiderivative","tail identity and vanishing limit"],
    }
    record={
        "schema_version":1,"status":"PASS",
        "claim":"Fourth-power upper tables supply the original positive-part scale-averaged criterion with O(Y^(1/2-theta)*log Y) error; a nonnegative prime kernel removes the logarithm.",
        "note":{"path":NOTE,"sha256":sha((ROOT/NOTE).read_bytes())},
        "checker":{"path":str(Path(__file__).relative_to(ROOT)),"sha256":sha(Path(__file__).read_bytes())},
        "manuscript_fragment":{"path":FRAGMENT,"sha256":sha((ROOT/FRAGMENT).read_bytes())},
        "proof_dependencies":dependencies,
        "checks":results,
        "independent_reviews":{
            "record":"certificates/continuation-review-2026-11-22.json",
            "scope":"Independent mathematical reviews are recorded in certificates/continuation-review-2026-11-22.json; this report covers automated checks only.",
        },
        "limits":[
            "Universal inequalities and limiting quantifiers are proved in the note and TeX fragment, not by the finite test cases.",
            "Hat positivity follows by integrating nonnegative affine basis functions; row-mass and cancellation algebra are checked exactly.",
            "The argument uses the exact ramp structure, not merely a generic derivative bound.",
            "Each sampled fourth power still needs its compatible arithmetic comparison.",
            "No arithmetic, geometric, spectral, Selmer estimate or zero computation is supplied.",
            "No Lean build or formal proof replay is performed.",
            "Document compilation and visual review are separate.",
        ],
    }
    (ROOT/CERT).write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":"PASS","certificate":CERT,**results},indent=2))


if __name__ == "__main__":
    main()
