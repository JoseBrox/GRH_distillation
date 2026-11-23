#!/usr/bin/env python3
"""Exact diagnostics and pinned provenance for the actual valid-cut top lift.

The TeX supplies the proof in every rank and word length.  This script
independently tests its noncommutative slope identities, weighted adjoint,
scalar Weyl conjugations, restricted inverse and degree budgets.  It does
not build Lean or turn finite tests into an analytic proof.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from functools import lru_cache
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s

import check_global_norm_frontier_off_diagonal as provenance

ROOT = Path(__file__).resolve().parents[1]
STEM = "global-norm-frontier-top-lift"
P = "Formalism.HermitianCurvature."
H = P + "HermitianCurvatureProofs."
SOURCES = [
    (P + "StatementTL", [(13, 73), (109, 157)]),
    (P + "RealInputsClosedAdmissibleSettings", [(14, 16), (56, 132)]),
    (P + "BigCellVanishingOfCommute", [(18, 19), (79, 103)]),
    (P + "StatementM", [(88, 112)]),
    (P + "CompositeFormulaLevelZero", [(103, 109)]),
    (P + "StatementQ", [(152, 159), (193, 196), (687, 691)]),
    (P + "StatementR", [(97, 119)]),
    (P + "StatementFr", [(60, 125), (354, 373)]),
    (H + "InvMulVecOfFixedVector", [(1, 120), (121, 240), (241, 283)]),
    (H + "XFibreOfParts", [(48, 141), (142, 183)]),
    (H + "LiftOfXOfParts", [(9, 38)]),
    (H + "ActualAlgebraFacts", [(86, 163)]),
    (H + "LiftCapelliOperators", [(148, 209)]),
    (H + "LiftOfFunctions", [(130, 198)]),
    (H + "LiftClosedUnderOperations", [(251, 305)]),
    (H + "FnComm", [(14, 110), (111, 144)]),
    (H + "CommuteAvrBvrOfCommuteSiteOps", [(190, 254), (255, 328)]),
    (H + "BasicLift", [(144, 263)]),
    (H + "MinusId", [(146, 225), (226, 313)]),
    (H + "L0ConstantPartCommute", [(313, 351)]),
    (H + "StarStartConjugationIdentity", [(476, 550), (553, 628)]),
    (H + "LetterLiftOfParts", [(113, 230), (284, 367), (368, 420)]),
    (H + "MatrixUnitZeroZeroEqInsert", [(202, 271)]),
    (H + "TLFinal", [(26, 105), (106, 144)]),
]
DEPENDENCIES = [
    "paper/sections/recovered/82-rd-section.tex",
    "paper/sections/recovered/84-rl-section.tex",
    "paper/sections/recovered/88-rr-section.tex",
    "paper/sections/recovered/89-re-section.tex",
    "paper/shared/global-norm-frontier-big-cell-continuity.tex",
    "paper/shared/global-norm-frontier-terminal-degree.tex",
    "scripts/check_global_norm_frontier_off_diagonal.py",
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def eq(a, b):
    diff = a - b
    if isinstance(diff, s.MatrixBase):
        assert all(s.cancel(v) == 0 for v in diff), diff
    else:
        assert s.cancel(diff) == 0, diff


def slope_checks():
    """Noncommuting matrices, with no unintended [L,X]=0 assumption."""
    cases = 0
    for n in (2, 3, 4):
        for seed in range(1, 5):
            xx = s.Matrix(n, n, lambda i, j: (i + seed + 2) if i == j
                          else (seed if j == i + 1 else 0))
            xi = xx.inv()
            ee = s.Matrix(n, n, lambda i, j: (i + 1)**2 - (j + seed)**2)
            lzero = xx**2 + (seed + 1)*s.eye(n)
            ll = s.Matrix(n, n, lambda i, j: (i + 2)*(j + 3) + seed*(i == j))
            assert ll*xx != xx*ll
            phi, tau, ya, q = map(s.Rational, [seed+1, seed+2, seed+3, seed+4])
            old = lzero + phi*ee
            delta = old-ll
            low = s.kronecker_product(s.eye(2), lzero)
            eplus = s.BlockMatrix([
                [ee-(xi*ee*xx-ee)+tau*s.eye(n), -s.eye(n)/ya],
                [s.zeros(n), xi*ee*xx]]).as_explicit()
            lhs = low + phi*eplus-s.kronecker_product(s.eye(2), ll)
            corr = xi*(ll*xx-xx*ll)+xi*delta*xx-delta
            rhs = s.kronecker_product(s.eye(2), delta)
            rhs += s.BlockMatrix([[phi*tau*s.eye(n)-corr, -phi*s.eye(n)/ya],
                                  [s.zeros(n), corr]]).as_explicit()
            eq(lhs, rhs)
            # The original minus factor includes two separate inverses.
            xm = xx+2*s.eye(n)
            coeff = -q/(ya-1)*xi*xm.inv()
            eminus = s.BlockMatrix([[ee, s.zeros(n)],
                                   [coeff, ee+tau*s.eye(n)]]).as_explicit()
            lhs = low+phi*eminus-s.kronecker_product(s.eye(2), ll)
            rhs = s.kronecker_product(s.eye(2), delta)
            rhs += s.BlockMatrix([[s.zeros(n), s.zeros(n)],
                                  [phi*coeff, phi*tau*s.eye(n)]]).as_explicit()
            eq(lhs, rhs)
            cases += 2
    return {"noncommuting_update_cases": cases,
            "matrix_sizes": [2, 3, 4], "both_inverse_minus_factor": True}


def weighted_adjoint_checks():
    z, b = s.symbols("z b", nonzero=True)
    tt = s.Rational(5, 3)
    gg = z*b-tt
    wt = z*b/gg
    ph, tau = z/(b*gg), tt/z
    shift = ph*tau
    eq(s.diff(wt, b)/wt, -shift)
    cc = s.Matrix([[1, 2], [3, 7]])
    ci = cc.inv()
    bb = s.Matrix([[2, 1], [5, 4]])
    aa = s.Matrix([[1, 3], [2, 8]])
    zz = s.Matrix([[z+b, z-b], [z*b, b**2]])
    fun = s.Matrix([z**2+b**3+1, z*b**2-z+3])
    dd = aa*(zz*bb-bb*zz)+ph*bb+shift*aa

    def mm(f):
        return f.diff(b)+zz*f

    for nn in range(7):
        lhs = ci*(mm(wt**nn*cc*fun)+dd*(wt**nn*cc*fun))/wt**nn
        rhs = mm(fun)+ci*(zz*cc-cc*zz)*fun+ci*dd*cc*fun-nn*shift*fun
        eq(lhs, rhs)
    return {"weighted_adjoint_cases": 7, "exact_shift": "-N*TT'/(bar(zeta)*G)"}


class Weyl:
    """Exact rational-coefficient differential operators in ordered variables."""
    def __init__(self, variables, terms=None):
        self.variables = tuple(variables)
        self.terms = {a: s.cancel(c) for a, c in (terms or {}).items() if c != 0}
        self.terms = {a: c for a, c in self.terms.items() if c != 0}

    @classmethod
    def mulfun(cls, variables, coeff):
        return cls(variables, {(0,)*len(variables): coeff})

    def __add__(self, other):
        if not isinstance(other, Weyl):
            other = self.mulfun(self.variables, other)
        ans = defaultdict(lambda: s.S.Zero, self.terms)
        for a, c in other.terms.items():
            ans[a] += c
        return Weyl(self.variables, ans)

    __radd__ = __add__

    def __neg__(self):
        return Weyl(self.variables, {a: -c for a, c in self.terms.items()})

    def __sub__(self, other):
        return self+-other

    def __mul__(self, other):
        if not isinstance(other, Weyl):
            other = self.mulfun(self.variables, other)
        assert self.variables == other.variables
        ans = defaultdict(lambda: s.S.Zero)
        for a, f in self.terms.items():
            for beta in itertools.product(*(range(i+1) for i in a)):
                choose = s.prod(s.binomial(i, j) for i, j in zip(a, beta))
                for b, g in other.terms.items():
                    h = derivative(g, self.variables, beta)
                    if h != 0:
                        power = tuple(i-j+k for i, j, k in zip(a, beta, b))
                        ans[power] += choose*f*h
        return Weyl(self.variables, ans)

    def __rmul__(self, other):
        return Weyl.mulfun(self.variables, other)*self


@lru_cache(maxsize=None)
def derivative(f, variables, powers):
    for x, p in zip(variables, powers):
        if p:
            f = s.diff(f, x, p)
    return s.cancel(f)


def weq(a, b):
    assert not (a-b).terms, (a-b).terms


def weyl_checks():
    cases = 0
    for r in range(3):
        z, b, yy = s.symbols("z b Y", nonzero=True)
        cs = s.symbols("c0:"+str(r), nonzero=True)
        bs = s.symbols("cb0:"+str(r), nonzero=True)
        variables = (z, b)+cs+bs
        one = Weyl.mulfun(variables, 1)
        zero = Weyl(variables)

        def derivative_op(j):
            a = tuple(int(i == j) for i in range(len(variables)))
            return Weyl(variables, {a: 1})

        dz, db = derivative_op(0), derivative_op(1)
        gg = z*b-s.Rational(7, 3)
        q11 = gg*one
        q10 = -gg*dz-(yy+s.Rational(1, 2))*b*one
        q01 = gg*db-(yy-s.Rational(1, 2))*z*one
        q00 = -gg*dz*db-(yy+s.Rational(1, 2))*b*db
        q00 += (yy-s.Rational(1, 2))*z*dz+yy**2*one
        weq(q10*z-z*q10, -q11)
        weq(q01*b-b*q01, q11)
        weq(q00*b-b*q00, q10)
        weq(q00*z-z*q00, -q01)

        def site_column(arg, dual=False):
            aa, bb = one, zero
            for j in range(r):
                c = bs[j] if dual else cs[j]
                pp = c*derivative_op(2+r+j if dual else 2+j)
                if dual:
                    pp = -pp
                aa, bb = (arg+pp)*aa-c*bb, (1/c)*aa
            return aa, bb

        aa, bb = site_column(yy)
        av, bv = site_column(yy, True)
        n0, n1 = q00*aa+q01*bb, q10*aa+q11*bb
        cap = av*n0+bv*n1
        bp = (1/b)*n1
        bm = (1/z)*(q01*av+q11*bv)
        dr, drb = s.prod(cs), s.prod(bs)
        dd, dbar = dr*z, drb*b
        fullg = dr*drb*gg
        extp, extm = zero, zero
        for ss in range(r+2):
            lam = s.Rational((-1)**(r+1-ss), s.factorial(ss)*s.factorial(r+1-ss))
            lhs = dbar**(-ss)*cap*dbar**ss
            avs, bvs = site_column(yy-ss, True)
            weq(lhs, avs*(n0+ss*bp)+bvs*n1)
            extp += (-1)**r*lam*lhs
            lhs = dd**(-ss)*cap*dd**ss
            ass, bss = site_column(yy+ss)
            weq(lhs, (av*q00+bv*q10-ss*bm)*ass+(av*q01+bv*q11)*bss)
            extm -= lam*lhs
            cases += 2
        weq(extp, bp)
        weq(extm, bm)
        shifted_a, _ = site_column(yy+1)
        shifted_av, _ = site_column(yy-1, True)
        weq((dbar/fullg)*(bp*dr-(dr/dd)*bp*dd), (1/z)*shifted_a)
        weq((-dd/fullg)*(bm*drb-(drb/dbar)*bm*dbar), (1/b)*shifted_av)
        cases += 4
        derivative.cache_clear()
    return {"Weyl_identity_cases": cases, "ranks": [0, 1, 2],
            "scope": "Independent exact differential-operator realization of every used commutator; not a substitute for the actual Capelli radial proof."}


def inverse_and_cost_checks():
    xx = s.symbols("X")
    types = [(1, 3), (3, 1), (2, 4)]
    u = s.eye(4)
    u[0, 0], u[0, 3], u[3, 0], u[3, 3] = map(s.Rational, [s.Rational(3, 5), s.Rational(4, 5), -s.Rational(4, 5), s.Rational(3, 5)])
    proj = u*s.diag(1, 1, 1, 0)*u.T
    count = 0
    for sign in (-1, 1):
        for yy in (s.Rational(1, 2), s.Rational(3, 2), s.Rational(7, 3)):
            vals = [sign*s.prod(yy+t for t in rho) for rho in types]
            pp = s.Poly(s.prod(xx-v for v in vals), xx)
            qq = s.Poly(s.cancel((1-pp.as_expr()/pp.eval(0))/xx), xx)
            mat = u*s.diag(*vals, 0)*u.T
            inv = s.zeros(4)
            for (power,), coeff in qq.terms():
                inv += coeff*mat**power
            eq(inv*mat*proj, proj)
            eq(mat*inv*proj, proj)
            assert mat.det() == 0  # unused constituent deliberately singular
            count += 1
    rr, delta, nn = s.symbols("R Delta N", integer=True, nonnegative=True)
    # R>=1 and d>=R; every displayed polynomial has nonnegative coefficients.
    uu = s.symbols("U", integer=True, nonnegative=True)
    rrv, dd = uu+1, uu+1+delta
    budgets = {
        "finite_difference": s.expand(3*rrv*dd-(rrv**2+2*rrv*dd)),
        "brace": s.expand(6*rrv*dd-(5*rrv*dd+2*rrv-1)),
        "first_column": s.expand(8*rrv*dd-(6*rrv*dd+rrv)),
        "tau": s.expand(9*rrv*dd-(8*rrv*dd+rrv-1)),
        "word": s.expand(11*(nn+1)*rrv*dd-(9*rrv*dd+11*nn*rrv*dd+2*rrv*dd)),
    }
    for poly in budgets.values():
        assert all(c >= 0 for c in s.Poly(poly, uu, delta, nn).coeffs())
    return {"restricted_inverse_cases": count,
            "repeated_spectral_values": True, "singular_unused_constituent": True,
            "all_rank_budget_certificates": {k: str(v) for k, v in budgets.items()}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    provenance.SOURCES = SOURCES
    sources = provenance.source_records(args.offline)
    checks = {"slope": slope_checks(), "weighted_adjoint": weighted_adjoint_checks(),
              "Weyl": weyl_checks(), "inverse_and_budget": inverse_and_cost_checks()}
    files = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", f"scripts/check_{STEM.replace('-', '_')}.py"]
    cert = {
        "status": "PASS", "classification": "closed local supplier; independent mathematical review recorded separately",
        "claim": "Actual valid-cut TL.TopLiftExists3 with Cb=11 and exact original InDDplus2",
        "source_commit": provenance.REV, "sources": sources, "checks": checks,
        "files": [{"path": path, "sha256": sha((ROOT/path).read_bytes())} for path in files],
        "established_mathematical_dependencies": [
            {"path": path, "sha256": sha((ROOT/path).read_bytes())} for path in DEPENDENCIES],
        "retained_hypotheses": [
            "original real place, actual radial data and original Haar normalizations",
            "valid cut 1<=l0<=k, original cut inequalities and separation >2; local k=1 uses the empty compact Capelli product, while actual KB.Pl retains k>=2",
            "original finite compact common-type fibres and exact sign (-1)^(k-l0)",
            "inverse polynomials only on covariant common-type fibres",
            "FibBound constants may depend on fixed representation and spectral parameters"],
        "not_claimed": ["unrestricted KB.TopLiftExists2", "uniform compact-inverse norm or spectral gap",
                        "global arithmetic period Gram or rational-return estimate",
                        "completion of W06 or W08", "a Lean build",
                        "finite diagnostics as proof of an all-rank analytic theorem"],
        "proof_scope": "The TeX proves every rank and cut word, with exact scalar inverses, no intermediate-minor denominators and linear word cost."}
    (ROOT/"certificates"/(STEM+".json")).write_text(json.dumps(cert, indent=2)+"\n")
    print(json.dumps({"status": cert["status"], "source_modules": len(sources),
                      "slope_cases": checks["slope"]["noncommuting_update_cases"],
                      "weighted_adjoint_cases": checks["weighted_adjoint"]["weighted_adjoint_cases"],
                      "Weyl_cases": checks["Weyl"]["Weyl_identity_cases"],
                      "inverse_cases": checks["inverse_and_budget"]["restricted_inverse_cases"]}))


if __name__ == "__main__":
    main()
