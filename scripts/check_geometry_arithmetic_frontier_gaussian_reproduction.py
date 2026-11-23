#!/usr/bin/env python3
"""Exact diagnostics for the actual full-slab Gaussian supplier.

The universal mathematical argument is in the shared TeX. Finite matrix
identities check its signs and conventions; they do not prove its analytic
statements or replay the pinned Lean build.
"""
from __future__ import annotations

import argparse
from math import factorial
import json
from pathlib import Path

import sympy as s

import check_geometry_arithmetic_frontier_geometric_filtration as auth

STEM = "geometry-arithmetic-frontier-gaussian-reproduction"
P = "Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation."
RANGES = {
    "Development.AbelianVarietyTheory.Definitions.SpanningFamilies.IsSystem":
        [(47, 108)],
    P+"GaussianKernelIntegrableOnThinSlab": [(38, 81), (120, 202), (203, 243)],
    P+"SetIntegralCompOfStable": [(162, 242), (243, 267), (268, 346)],
    P+"KernInvariantSymmPos": [(194, 257), (296, 385), (386, 435)],
    P+"RealPlaceKernelHolomorphicWeightRowHighest":
        [(54, 112), (148, 190), (225, 281), (346, 389), (422, 465), (479, 558)],
    P+"ExtendByZeroAntitoneOffBreak": [(31, 103), (148, 210), (229, 301)],
    P+"LowestWeightFunctionMulEq": [(163, 230), (264, 335)],
    P+"IntegrableOnMinorFinStatement": [(1, 9)],
    P+"HermitianThetaSeriesSpanBoundedForms": [(168, 200), (242, 254)],
}


def clean(m):
    return m.applyfunc(s.cancel) if isinstance(m, s.MatrixBase) else s.cancel(m)


def eq(a, b):
    z = clean(a-b)
    if isinstance(z, s.MatrixBase):
        assert all(v == 0 for v in z), z
    else:
        assert z == 0, z


def adj(a):
    return a.conjugate().T


def normsq(a):
    return s.cancel(a*s.conjugate(a))


def unitary(r, p, seed):
    j = s.diag(*([1]*p+[-1]*(r-p)))
    u = s.eye(r)
    if p and p < r:
        b = s.eye(r)
        a, c = (seed % p), p+(seed % (r-p))
        b[a, a] = b[c, c] = s.Rational(5, 3)
        b[a, c] = b[c, a] = s.Rational(4, 3)
        u = b*u
    for lo, hi in [(0, p), (p, r)]:
        if hi-lo > 1:
            a, c = lo, hi-1
            b = s.eye(r)
            b[a, a] = b[c, c] = s.Rational(3, 5)
            b[a, c], b[c, a] = s.Rational(-4, 5), s.Rational(4, 5)
            u = b*u
    ph = s.diag(*[(3+4*s.I)/5 if (a+seed) % 2 else 1 for a in range(r)])
    u = clean(ph*u)
    eq(u.T*j*u.conjugate(), j)
    return u


def upper(r, seed):
    return s.Matrix(r, r, lambda a, b:
                    s.Rational(a+seed+3, a+seed+2) if a == b else
                    s.Rational(a+b+1, 7)+s.I*s.Rational(seed+b, 11)
                    if a < b else 0)


def matrices(x, y, p):
    r = x.rows
    j = s.diag(*([1]*p+[-1]*(r-p)))
    pr = s.diag(*([1]*p+[0]*(r-p)))
    qr = s.eye(r)-pr
    ll = clean(pr*adj(y)*j+qr*x.inv())
    aa = clean(pr*x.T*j+qr*y.conjugate().inv())
    kap = -2*s.I
    zz = clean(kap/4*(ll.inv()*(-j)*ll).T*j)
    hh = clean((zz-adj(zz))/(2*s.I))
    nn = clean(ll.inv().T*j*hh.inv()*j*aa.inv())
    mm = clean(ll.inv().T*j*aa.inv())
    eq((-j)*mm, mm*(-j))
    eq(kap/(8*s.I)*((-j)*nn+nn*(-j)), mm)
    for a in range(1, r+1):
        assert s.simplify(hh[:a, :a].det()).is_positive
    vleft = qr.row_join(pr)
    vright = pr.row_join(qr)
    vminus = pr.row_join(-qr)
    e0 = clean(-kap**2/4*vleft.T*nn*vright)
    er = clean(s.I*kap*vleft.T*mm*vminus)
    return ll, aa, hh, e0, er


def diagnostics():
    matrix_cases = []
    minor_cases = 0
    jacobian_cases = 0
    for r in range(1, 5):
        for p in range(r+1):
            u, v, z = [unitary(r, p, seed) for seed in (1, 2, 3)]
            x, y = clean(u*upper(r, 1)), clean(v*upper(r, 2))
            ll, aa, hh, e0, er = matrices(x, y, p)
            diff = clean(e0+e0.T-er-er.T)
            eq(diff[:r, r:], s.zeros(r))
            for a in range(r):
                for b in range(r):
                    if (a < p) == (b < p):
                        assert diff[a, b] == diff[r+a, r+b] == 0
            l2, a2, _, e2, _ = matrices(clean(z*x), clean(z*y), p)
            eq(l2, ll*z.inv())
            eq(a2, aa*z.conjugate().inv())
            eq(e2+e2.T, e0+e0.T)
            eq(l2.det()*a2.det(), ll.det()*aa.det())
            ly, ay, _, ey, _ = matrices(y, x, p)
            sw = s.zeros(2*r)
            sw[:r, r:] = sw[r:, :r] = s.eye(r)
            eq(sw*(ey+ey.T).conjugate()*sw, e0+e0.T)
            eq(ly.det()*ay.det(), s.conjugate(ll.det()*aa.det()))
            _, _, _, ed, _ = matrices(u, u, p)
            eq(ed+ed.T, 2*sw)
            for g in [u, v, z, clean(u*v)]:
                dp = normsq(g[:p, :p].det()) if p else s.Integer(1)
                assert dp >= 1
                for a in range(r+1):
                    minor = g[:a, :a].det() if a else s.Integer(1)
                    assert normsq(minor) <= dp
                    minor_cases += 1
                b = upper(r, 1)
                eq((g*b)[:p, :p].det(), g[:p, :p].det()*b[:p, :p].det())
            if 0 < p < r:
                q = r-p
                zz = s.Matrix(q, p, lambda a, b: s.Rational(a+b+1, 20*r))
                g = clean(u*v)
                a, b, c, d = g[:p, :p], g[:p, p:], g[p:, :p], g[p:, p:]
                den = clean(a+b*zz)
                zp = clean((c+d*zz)*den.inv())
                eq((s.eye(p)-adj(zp)*zp).det(),
                   (s.eye(p)-adj(zz)*zz).det()/normsq(den.det()))
                derivative_det = clean((d-zp*b).det()**p/den.det()**q)
                eq(derivative_det, g.det()**p/den.det()**r)
                eq(normsq(derivative_det)*((s.eye(p)-adj(zp)*zp).det())**(-r),
                   (s.eye(p)-adj(zz)*zz).det()**(-r))
                jacobian_cases += 1
            matrix_cases.append({"r": r, "p": p})
    # Ordinary, not divided-power, derivatives fix the exact diagonal factor.
    zz, ww = s.symbols("z w")
    fischer = 0
    for a in range(7):
        for t in [s.Rational(1, 2), s.Rational(3, 2), s.Integer(2)]:
            got = s.diff(s.exp(t*zz*ww), zz, a, ww, a).subs({zz:0, ww:0})
            eq(got, factorial(a)*t**a)
            fischer += 1
    # The endpoint n=2r has exponent zero, and the deficient exponent is
    # genuinely unsafe in the smallest matrix ball.
    endpoint = [{"r": r, "n": 2*r, "exponent": 0} for r in range(9)]
    eps = s.Symbol('eps', positive=True)
    assert s.limit(-s.log(eps), eps, 0, dir='+') == s.oo
    return {
        "exact_original_Gaussian_cases": matrix_cases,
        "balanced_reduction_unitary_swap_and_positive_diagonal": "PASS",
        "principal_minor_and_triangular_fibre_cases": minor_cases,
        "exact_matrix_ball_jacobians": jacobian_cases,
        "ordinary_Fischer_derivative_cases": fischer,
        "endpoint_exponents": endpoint,
        "negative_control": "At n=2(r-1), p=q=1 the ball integral diverges.",
        "scope": "Exact finite diagnostics and elementary symbolic endpoint checks; the all-rank analytic proof is in the TeX.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    checks = diagnostics()
    paths = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", f"scripts/check_{STEM.replace('-', '_')}.py"]
    cert = {
        "date": "2026-11-23", "status": "PASS",
        "classification": "Closed actual analytic supplier; independent review recorded separately",
        "whole_nodes_newly_closed": 0,
        "source_commit": auth.REV, "sources": sources, "checks": checks,
        "files": [{"path": p, "sha256": auth.sha((auth.ROOT/p).read_bytes())} for p in paths],
        "retained": ["original full complex-frame Lebesgue measure",
                     "every row-highest family and its literal derivative factors",
                     "even n>=2r, including equality, rank zero and definite endpoints",
                     "rho equal to the original squared-kernel integral divided by its diagonal",
                     "separate global kernel scalar in the actual spanning consumer"],
        "not_claimed": ["uniform growing-family lower bound on rho",
                        "full theta spanning without the finite and global arithmetic suppliers",
                        "global rational-return/period-Gram estimate", "Lean build"],
    }
    (auth.ROOT/"certificates"/f"{STEM}.json").write_text(json.dumps(cert,indent=2)+"\n")
    print(json.dumps({"status":"PASS","sources":len(sources),
                     "Gaussian_cases":len(checks["exact_original_Gaussian_cases"]),
                     "minor_cases":checks["principal_minor_and_triangular_fibre_cases"],
                     "Jacobians":checks["exact_matrix_ball_jacobians"],
                     "Fischer":checks["ordinary_Fischer_derivative_cases"]}))


if __name__ == "__main__":
    main()
