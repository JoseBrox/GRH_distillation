#!/usr/bin/env python3
"""Exact diagnostics and bounded provenance for the terminal degree supplier.

The TeX contains the all-rank mathematical proof.  These independent finite
checks use explicit unitary radicals and PBW reduction in U(gl_n); they do
not certify an analytic theorem by numerical sampling or build Lean.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s

import check_global_norm_frontier_off_diagonal as pb

ROOT = Path(__file__).resolve().parents[1]
STEM = "global-norm-frontier-terminal-degree"
P = "Formalism.HermitianCurvature."
H = P + "HermitianCurvatureProofs."
SOURCES = [
    ("Formalism.FormalDegreeBessel.StatementG", [(9, 9)]),
    ("Formalism.FormalDegreeBessel.StatementWR", [(19, 38)]),
    (P + "StatementHeads", [(72, 94)]),
    (P + "OperatorsCommuteTranslations", [(11, 50), (241, 248), (269, 297)]),
    (P + "RealInputsClosedAdmissibleSettings", [(90, 121), (272, 288)]),
    (P + "StatementTL", [(133, 145)]),
    (P + "StatementQ", [(388, 405)]),
    (H + "CornerMatrixFirstLineZero", [(54, 145)]),
    (H + "CornerMatrixRightTranslate", [(91, 140)]),
    (H + "PolyTopOf", [(1, 76)]),
    (H + "RadAATopOfParts", [(13, 48)]),
    (H + "WeylCellMulVecBasis", [(196, 277), (278, 317)]),
    (H + "ChainX1", [(9, 117)]),
    (H + "QminorZero", [(18, 47), (87, 206)]),
    (H + "RadialSideRaising", [(140, 214), (222, 258)]),
    (H + "JacquetRaisingOperator", [(227, 286)]),
    (H + "MatrixUnitZeroZeroEqInsert", [(202, 250)]),
    (H + "TopFirstOfParts", [(186, 199)]),
    (H + "GaugeNormPower", [(55, 91), (101, 150)]),
    (H + "ThetaCompactSupport", [(81, 132)]),
]
DEPENDENCIES = [
    "paper/shared/global-norm-frontier-off-diagonal.tex",
    "paper/shared/global-norm-frontier-unitary-density.tex",
    "paper/shared/global-norm-frontier-big-cell-continuity.tex",
    "paper/shared/global-norm-frontier-partial-head-transfer.tex",
    "scripts/check_global_norm_frontier_off_diagonal.py",
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def eq(a, b):
    diff = a - b
    if isinstance(diff, s.MatrixBase):
        assert all(s.simplify(v) == 0 for v in diff)
    else:
        assert s.simplify(diff) == 0, diff


def clean(a):
    return a.applyfunc(s.cancel)


def normal_form_checks():
    cases = []
    for r in range(1, 6):
        for p in range(r):
            k = 2
            ss = r + 1 - p
            t = s.Rational(3, 2) + s.I * s.Rational(p + 1, 3)
            hh = s.Matrix(p, p, lambda a, b:
                          a + 2 if a == b else s.I / 3 if b == a + 1 else 0)
            zz = s.diag(hh, s.Matrix(ss, ss, lambda a, b:
                                    t if a + b == ss - 1 else 0))
            jw = s.diag(1, 1, -1)
            j = s.zeros(2 * r + k + 1)
            j[:r, r+k+1:] = s.eye(r)
            j[r:r+k+1, r:r+k+1] = jw
            j[r+k+1:, :r] = s.eye(r)
            zp = s.Matrix([0, 0, 2])
            wp = s.Matrix([-s.conjugate(t) / 2, 0, -s.conjugate(t) / 2])
            eq((wp.conjugate().T * jw * wp)[0], 0)
            eq((wp.conjugate().T * jw * zp)[0], t)
            yp = s.zeros(2*r+k+1, r)
            for a in range(r):
                if a == p:
                    yp[r:r+k+1, a] = wp
                else:
                    yp[r+k+1:, a] = s.conjugate(zz[a, :r]).T
            eq(yp.conjugate().T * j * yp, s.zeros(r))
            x = s.Matrix(k+1, r, lambda a, b:
                         s.Rational(a+b+1, 3) + s.I*s.Rational(2*a-b, 4)
                         if a < k else 0)
            tmp = s.Matrix(r, r, lambda a, b:
                           s.Rational(2*a+b+1, 5) + s.I*s.Rational(a-3*b+2, 4))
            kk = tmp - tmp.conjugate().T

            def radical(xx, central):
                nn = s.eye(2*r+k+1)
                nn[:r, r:r+k+1] = -xx.conjugate().T*jw
                nn[r:r+k+1, r+k+1:] = xx
                nn[:r, r+k+1:] = central-xx.conjugate().T*jw*xx/2
                return clean(nn)

            nn = radical(x, kk)
            yy = clean(nn*yp)
            indices = [a for a in range(r) if a != p]
            lower = yy[r+k+1:, :]
            mid = yy[r:r+k+1, :]
            upper = yy[:r, :]
            xx = s.zeros(k+1, r)
            if indices:
                xb = clean(mid[:, indices] * lower.extract(indices, indices).inv())
                for col, a in enumerate(indices):
                    xx[:, a] = xb[:, col]
            yy_p = mid[:, p]
            projection = clean(yy_p-zp*(zp.conjugate().T*jw*yy_p)[0]/
                               (zp.conjugate().T*jw*zp)[0])
            norm = s.simplify((projection.conjugate().T*jw*projection)[0])
            assert norm != 0
            xx[:, p] = clean(-s.conjugate(upper[p, p])/norm*projection)
            eq(xx.conjugate().T*jw*zp, s.zeros(r, 1))
            eq(upper[:, p]+xx.conjugate().T*jw*yy_p, s.zeros(r, 1))
            central = s.zeros(r)
            if indices:
                kb = clean((upper[:, indices]+xx.conjugate().T*jw*
                            xx*lower[:, indices]/2)*lower.extract(indices, indices).inv())
                for col, a in enumerate(indices):
                    central[:, a] = kb[:, col]
            for a in indices:
                central[a, p] = -s.conjugate(central[p, a])
            eq(central+central.conjugate().T, s.zeros(r))
            n0 = radical(xx, central)
            eq(n0.conjugate().T*j*n0, j)
            zfull = s.zeros(2*r+k+1, 1)
            zfull[r:r+k+1, :] = zp
            eq(n0*zfull, zfull)
            eq(n0[:, :r], s.eye(2*r+k+1)[:, :r])
            # The reconstructed radical need not equal the one used to make
            # the data.  It must reduce precisely the actual isotropic tuple.
            reduced = s.zeros(2*r+k+1, r)
            reduced[r+k+1:, :] = lower
            reduced[r:r+k+1, p] = yy_p
            eq(n0*reduced, yy)
            eq((reduced.conjugate().T*j)[:, :r], zz[:r, :r])
            # This is the scalar which must not accidentally be conjugated.
            eq((yy_p.conjugate().T*jw*zp)[0], t)
            cases.append({"r": r, "k": k, "preceding_size": p,
                          "last_block": ss, "nonreal_t": str(t)})
    return cases


def terminal_minor_checks():
    pb.gen_key = lambda g: (g[0] < g[1], g[0], g[1])
    pb.pbw.cache_clear()

    def right_character(poly, r):
        ans = defaultdict(Q)
        z = {r: Q(3), r+1: Q(0), r+2: Q(5)}
        for word, coeff in poly.items():
            rest = []
            for a, b in word:
                if a < b:
                    if a < r and b < r:
                        coeff *= Q(b == a+1)
                    elif a < r <= b <= r+2:
                        coeff *= z[b] if a == r-1 else Q(0)
                    else:
                        raise AssertionError("Unlicensed middle-block root")
                else:
                    rest.append((a, b))
            ans[tuple(rest)] += coeff
        return pb.clean(ans)

    cases = 0
    for r in range(1, 6):
        for p in range(r):
            ss = r+1-p
            hh = s.Matrix(p, p, lambda a, b: a+2 if a == b else
                          1 if b == a+1 else 0)
            t = Q(7)
            zz = s.diag(hh, s.Matrix(ss, ss, lambda a, b:
                                    int(t) if a+b == ss-1 else 0))
            xi = s.zeros(r, 2*r+3)
            for a in range(r):
                if a != p:
                    for b in range(r):
                        xi[a, b] = zz[a, b]
            covector = [-s.Rational(7, 2), s.Rational(0), s.Rational(7, 2)]
            for b in range(3):
                xi[p, r+b] = covector[b]
            assert sum(covector[b]*[3, 0, 5][b] for b in range(3)) == 7
            for u in [Q(-4, 3)+a for a in range(r+1)]:
                lhs = {}
                for b in range(3):
                    cols = tuple(v for v in range(r) if v != p)+(r+b,)
                    co = Q(xi.extract(range(r), cols).det())
                    lhs = pb.add(lhs, pb.minor(tuple(range(r)), cols, u), co)
                principal = tuple(range(p))
                factor = Q(zz.det())*Q((-1)**(ss-1))/t
                difference = pb.add(lhs, pb.minor(principal, principal, u), -factor)
                assert right_character(difference, r) == {}, (r, p, u)
                cases += 1
    return {"PBW_cases": cases, "max_r": 5,
            "parameter_nodes_per_case": "r+1, certifying degree at most r",
            "actual_middle_character": [3, 0, 5],
            "empty_principal_minor_and_s_two": "included",
            "status": "PASS"}


def toda_checks():
    # A different PBW ordering exposes both Whittaker characters:
    # negative roots first, diagonal next, positive roots last.
    pb.gen_key = lambda g: (0 if g[0] > g[1] else 1 if g[0] == g[1]
                           else 2, g[0], g[1])
    pb.pbw.cache_clear()
    cases = 0
    for r in range(1, 6):
        diagonal = s.symbols("d:"+str(r))
        cs = s.symbols("c:"+str(r), nonzero=True)
        for u in [Q(-2, 5)+a for a in range(r+1)]:
            result = 0
            for word, coefficient in pb.minor(tuple(range(r)), tuple(range(r)), u).items():
                term = s.Rational(coefficient.numerator, coefficient.denominator)
                for a, b in word:
                    if a > b:
                        term *= cs[a]/cs[b] if a == b+1 else 0
                    elif a < b:
                        term *= 1 if b == a+1 else 0
                    else:
                        term *= diagonal[a]
                result += term
            f, g = s.Integer(1), s.Integer(0)
            for a in range(r):
                f, g = ((s.Rational(u.numerator, u.denominator)-a+diagonal[a])*f-cs[a]*g,
                        f/cs[a])
            assert s.expand(result-f) == 0
            cases += 1
    # Exact symbolic Wirtinger derivative and the all-index gauge shift.
    x, y, alpha = s.symbols("x y alpha", real=True)
    radial = (x*x+y*y)**alpha
    p_radial = (x+s.I*y)*(s.diff(radial, x)-s.I*s.diff(radial, y))/2
    eq(p_radial, alpha*radial)
    r, a, k = s.symbols("r a k")
    eq((2*r+k)/2-a, (2*(r-a)+k)/2)
    return {"independent_double_Whittaker_PBW_cases": cases,
            "max_r": 5, "symbolic_gauge_identities": 2, "status": "PASS"}


def interpolation_checks():
    lam = s.Rational(2, 5)-s.I/5
    vec = s.Matrix([2+s.I, -1])
    cases = 0
    for p in range(4):
        for length in range(4):
            grids = [[s.Rational(2*a+3*b+1, a+2) for b in range(p+1)]
                     for a in range(length)]
            mats = [s.Matrix([[a+1, 2+a*s.I], [-1+s.I, 3-a]]) for a in range(p)]
            def ay(v):
                out = lam*v**p*s.eye(2)
                for degree in range(p):
                    out += v**degree*mats[degree]
                return out
            got = s.zeros(2, 1)
            for indices in itertools.product(range(p+1), repeat=length):
                weight = s.Integer(1)
                product = s.eye(2)
                for a, n in enumerate(indices):
                    for b in range(p+1):
                        if b != n:
                            weight /= grids[a][n]-grids[a][b]
                    product = product*ay(grids[a][n])
                got += weight*product*vec
            eq(got, lam**length*vec)
            cases += 1
    zi, zbi, gg, ell, aa, bb = s.symbols("zi zbi gg ell aa bb", commutative=False)
    top = s.Matrix([[zi, 0], [0, zbi]])*s.Matrix([[1, 0], [gg*ell, gg]])*s.Matrix([aa, bb])
    assert s.expand(top[0]-zi*aa) == 0
    assert s.expand(top[1]-zbi*gg*(ell*aa+bb)) == 0
    return {"noncommuting_matrix_grid_cases": cases,
            "p_zero_K_zero": "included", "actual_triangular_first_column": "PASS",
            "status": "PASS"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    pb.SOURCES = SOURCES
    sources = pb.source_records(args.offline)
    checks = {"explicit_radical_normal_form": normal_form_checks(),
              "terminal_contracted_minor": terminal_minor_checks(),
              "radial_Toda_and_gauge": toda_checks(),
              "word_and_Lagrange": interpolation_checks()}
    files = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", f"scripts/check_{STEM.replace('-', '_')}.py"]
    cert = {
        "status": "PASS", "classification": "closed local supplier; independent mathematical review recorded separately",
        "claim": "Actual PolyTop, RadAATop, TopFirst and DegTop with every original quantifier",
        "source_commit": pb.REV, "sources": sources, "checks": checks,
        "files": [{"path": path, "sha256": sha((ROOT/path).read_bytes())} for path in files],
        "established_mathematical_dependencies": [
            {"path": path, "sha256": sha((ROOT/path).read_bytes())} for path in DEPENDENCIES],
        "retained_hypotheses": [
            "original real place and normalized tower, with all Haar constants",
            "original compact coefficients with positive Gram cutoff",
            "original top lift regular radial identity and InDDplus2",
            "all augmented words admissible for the original cut",
            "all grids injective, with no equally-spaced-grid restriction"],
        "not_claimed": ["construction of the top lift", "unrestricted KB.TopLiftExists2",
                        "global period Gram or rational-return bound", "completion of W06 or W08",
                        "a Lean build", "finite diagnostics as a proof of the analytic theorem"],
        "proof_scope": "The TeX proves every rank/head/word/grid case; exact finite checks diagnose the algebra and conventions."}
    path = ROOT/"certificates"/(STEM+".json")
    path.write_text(json.dumps(cert, indent=2)+"\n")
    print(json.dumps({"status": cert["status"], "source_modules": len(sources),
                      "normal_forms": len(checks["explicit_radical_normal_form"]),
                      "terminal_PBW": checks["terminal_contracted_minor"]["PBW_cases"],
                      "Toda_PBW": checks["radial_Toda_and_gauge"]["independent_double_Whittaker_PBW_cases"],
                      "grids": checks["word_and_Lagrange"]["noncommuting_matrix_grid_cases"]}))


if __name__ == "__main__":
    main()
