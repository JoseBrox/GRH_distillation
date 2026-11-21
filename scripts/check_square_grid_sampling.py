#!/usr/bin/env python3
"""Exact finite checks for the square-grid analytic reduction.

The note and shared manuscript fragment contain the universal proofs.
This script checks endpoint and cancellation identities in rational
arithmetic, the continuous error integral symbolically, and the same
bounded analytic premises pinned by the integer-table certificate.
It supplies no arithmetic construction or zero computation.
"""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = "notes/square-grid-sampling.md"
FRAGMENT = "paper/shared/square-grid-sampling.tex"
CERT = "certificates/square-grid-sampling.json"
DEPENDENCIES = [
    ("paper/sections/recovered/03-sec-one-sided.tex", 337, 381,
     "ce3e87093500a6e5235d7efd687f7f8832ec60c33d8b8bce154eb4dbfeca0fcf"),
    ("paper/rh/sections/01-introduction.tex", 31, 60,
     "96606f00a60113d4b636dc162c243ed3b1c21ab0d35f87b2b692e8e97c759c63"),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def floor(q):
    return q.numerator//q.denominator


def ceil(q):
    return -(-q.numerator//q.denominator)


def rows(n,q):
    """q=exp(h/2)>1; the log of each factor is h*a_{n,k}."""
    assert n >= 1 and q > 1
    top=q*n
    return [(k,(min(F(k+1),top)/k)**2)
            for k in range(n,ceil(top))]


def product(values):
    result=F(1)
    for value in values:
        result *= value
    return result


def row_checks():
    cases=endpoints=0
    ratios=[F(10001,10000),F(101,100),F(3,2),F(2),F(7,3),F(4),F(13,3)]
    for n in [*range(1,37),100,1000]:
        for q in ratios:
            row=rows(n,q)
            assert row[0][0]==n and row[-1][0]==ceil(q*n)-1
            assert all(factor>1 for _,factor in row)
            assert product(factor for _,factor in row)==q*q
            if (q*n).denominator==1:
                # The endpoint v=h has zero integration weight.
                endpoint=floor(q*n)
                assert endpoint==row[-1][0]+1
                endpoints+=1
            cases+=1
    return cases,endpoints


def window_checks():
    cases=0
    for N in range(2,13):
        for X in [F(N)+F(1,3),F(N)+F(2,3),F(N+1),F(N*N)]:
            # X=N^b is any real endpoint index above N.
            # Every listed rational X corresponds to some b>1.
            L=floor(X)
            for q in [F(10001,10000),F(3,2),F(2),F(7,3),F(4)]:
                K=ceil(q*X)
                for n in range(N,L+1):
                    row=rows(n,q)
                    assert all(N<=k<=K for k,_ in row)
                    assert N<=floor(q*n)<=K  # Includes zero-weight endpoint.
                    assert N<=n<=ceil(X)     # h=0 identity row.
                for theta in [F(1),F(3,2),F(2)]:
                    power=int(2*theta)
                    weights=[(F(n)**(-power)-F(n+1)**(-power))/theta
                             for n in range(N,L+1)]
                    assert all(w>0 for w in weights)
                    full=sum(weights,F(0))
                    exact=(F(N)**(-power)-X**(-power))/theta
                    assert exact<=full
                    assert full==(F(N)**(-power)-F(L+1)**(-power))/theta
                    cases+=1
    return cases


def distance_checks():
    cases=0
    for n in range(1,25):
        for offset in [F(0),F(1,7),F(1,2),F(6,7),F(999,1000)]:
            a=F(n)+offset  # sqrt(x)
            x=a*a
            for q in [F(1),F(10001,10000),F(3,2),F(2),F(7,3),F(17,10)]:
                z=n*q
                k=floor(z)
                assert x-n*n<=2*a
                assert z*z-k*k<=2*z
                assert 0<=x*q*q-k*k<=2*a*(q*q+q)
                cases+=1
    return cases


def cancellation_checks():
    cases=0
    for n in [*range(1,41),100]:
        row=rows(n,F(4))  # h=log(16)
        low=product(f for k,f in row if k<2*n)
        high=product(f for k,f in row if k>=2*n)
        assert low==high==4
        assert product(f for _,f in row)==16
        # Signed row=(-log4+log4)/log16=0.
        # Taking positive parts first gives log4/log16=1/2.
        cases+=1
    return cases


def positive_part_checks():
    cases=0
    for value in [F(i,3) for i in range(-20,21)]:
        for error in [F(i,5) for i in range(11)]:
            assert max(value+error,0)<=max(value,0)+error
            cases+=1
    # Enlarging a final cell is legitimate for a nonnegative constant,
    # and is false in general for the signed constant itself.
    assert F(1,3)*F(-1)>F(1)*F(-1)
    assert F(1,3)*max(F(-1),0)<=F(1)*max(F(-1),0)
    return cases


def symbolic_checks():
    u,delta,ell=sp.symbols("u delta ell",positive=True)
    primitive=-sp.exp(-delta*u)*(
        (ell+u)**2/delta+2*(ell+u)/delta**2+2/delta**3)
    assert sp.simplify(sp.diff(primitive,u)-sp.exp(-delta*u)*(ell+u)**2)==0
    assert sp.limit(primitive,u,sp.oo)==0
    assert -primitive.subs(u,0)==ell**2/delta+2*ell/delta**2+2/delta**3
    x,theta=sp.symbols("x theta",positive=True)
    assert sp.simplify(sp.diff(-x**(-theta)/theta,x)-x**(-theta-1))==0
    return {
        "tail_integral": "PASS",
        "square_cell_weight": "PASS",
        "strict_requirement": "delta=theta-1/2>0",
        "error_coefficient": "2*C*(d_h+d_(h/2))",
    }


def main():
    dependencies=[]
    for path,lo,hi,expected in DEPENDENCIES:
        data=(ROOT/path).read_bytes()
        excerpt=b"".join(data.splitlines(keepends=True)[lo-1:hi])
        assert hi-lo+1<=120 and sha(excerpt)==expected,path
        dependencies.append({
            "path":path,"ranges":[{"start":lo,"end":hi,"sha256":expected}],
            "reuse":"Same bounded analytic premise as the integer-table checker.",
        })
    row_count,endpoint_count=row_checks()
    results={
        "exact_rational_rows":row_count,
        "zero_weight_integral_upper_endpoints":endpoint_count,
        "finite_window_and_cell_weight_cases":window_checks(),
        "rational_square_distance_cases":distance_checks(),
        "exact_signed_cancellation_cases":cancellation_checks(),
        "positive_part_cases":positive_part_checks(),
        "symbolic":symbolic_checks(),
    }
    record={
        "schema_version":1,
        "status":"PASS",
        "claim":"Square-spaced finite upper tables supply the same positive-part scale-averaged analytic criterion, with the explicit decaying error.",
        "note":{"path":NOTE,"sha256":sha((ROOT/NOTE).read_bytes())},
        "checker":{"path":str(Path(__file__).relative_to(ROOT)),
                   "sha256":sha(Path(__file__).read_bytes())},
        "manuscript_fragment":{"path":FRAGMENT,"sha256":sha((ROOT/FRAGMENT).read_bytes())},
        "proof_dependencies":dependencies,
        "dependency_provenance":"The bounded analytic premises reuse the published integer-table certificate's exact excerpt hashes; no temporary local Git commit is used.",
        "checks":results,
        "independent_reviews":[
            {"reviewer":"/root","status":"PASS",
             "scope":"Complete shared proof: one-sided derivative, exact positive row mass, error constant and tail, h=0, full last-cell weight, finite table endpoints, fixed-accuracy cofinal square windows and subpolynomial acceptance criterion."},
            {"reviewer":"/root/geometric_simplify","status":"PASS",
             "scope":"Complete written note and compact theorem: weights, final positive cell, h=0, finite table coverage, delta>0 tail, fixed analytic data, cofinal square windows, signed cancellation, optional pointwise criterion. Explicit domain and zero-weight endpoint precisions incorporated."}
        ],
        "limits":[
            "Universal proofs are in the note and TeX fragment; finite cases supplement them.",
            "No signed dyadic filter is applied.",
            "Every sampled square must have its actual arithmetic comparison.",
            "No new arithmetic, geometric, spectral or Selmer estimate is supplied.",
            "No zero computation or Lean replay is performed.",
            "Final document build and visual review are separate.",
        ],
    }
    (ROOT/CERT).write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":"PASS","certificate":CERT,**results},indent=2))


if __name__=="__main__":
    main()
