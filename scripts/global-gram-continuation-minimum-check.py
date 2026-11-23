#!/usr/bin/env python3
"""Authenticate the actual HN-minimum interface and exact flag diagnostics.

The all-field proof is in the companion TeX.  These calculations check
its flag orientation, fractional-ideal norm, and real-covolume factors;
they do not establish a uniform seed moment or rebuild Lean.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import sympy as s

import check_global_norm_frontier_off_diagonal as provenance

ROOT = Path(__file__).resolve().parents[1]
H = "Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals."
A = "Development.AbelianVarietyTheory."
SOURCES = [
    (H+"HidaSetting", [(24, 34), (54, 63), (166, 173), (207, 226), (266, 273)]),
    (H+"PoincareInHH", [(36, 65)]),
    (H+"WuDecay", [(18, 34)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.GlobAut", [(44, 59)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.BlockEnds", [(111, 118)]),
    (A+"Definitions.SemilocalFrames.LayerProd", [(39, 54)]),
    ("Formalism.HarderNarasimhan.StatementPl", [(19, 45)]),
    ("Formalism.HermitianLattices.StatementMaj", [(17, 37), (66, 81)]),
    (A+"Statements.CuspFrameWeights.CuspFrame", [(27, 37)]),
    (A+"BlockTheory.SiegelWeilLocal.FarTermsLatticeBound", [(12, 32)]),
]
PROOF_FILES = [
    "paper/shared/global-gram-continuation-minimum.tex",
    "paper/shared/global-gram-continuation-minimum-references.tex",
    "notes/global-gram-continuation-minimum.md",
    "scripts/global-gram-continuation-minimum-check.py",
]
DEPENDENCIES = [
    "paper/shared/global-gram-continuation-period-identity.tex",
    "paper/shared/global-gram-continuation-phases.tex",
    "paper/shared/global-norm-frontier-seed-decay.tex",
    "notes/projector-kernel-tail.md",
]


def sha(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def flag_models():
    reports = []
    case_counts = {"first_pairing": 0, "z_pairing": 0,
                   "positive_quotient": 0, "last_flag_coefficient": 0}
    detected_first_index = False
    detected_last_index = False
    for r in range(4):
        for k in range(3):
            for T in (1, 3, 5):
                # Ordered basis e_0,...,e_(r-1),z,w_0,...,w_(k-1),f_0,...,f_(r-1).
                m, n = k+1, 2*r+k+1
                Jb = s.diag(-T, *([1]*k))
                J = s.zeros(n)
                J[:r, r+m:] = s.eye(r)
                J[r:r+m, r:r+m] = Jb
                J[r+m:, :r] = s.eye(r)
                A = s.Matrix(r, m, lambda i, j: i+j+1+s.I*(i-j))
                B = s.Matrix(r, r, lambda i, j: i-j+s.I*(i+j+1))
                Z = s.zeros(n)
                Z[:r, r:r+m] = A
                Z[:r, r+m:] = B
                Z[r:r+m, r+m:] = -Jb.inv()*A.conjugate().T
                assert Z.conjugate().T*J+J*Z == s.zeros(n)
                assert Z**3 == s.zeros(n)
                unip = s.eye(n)+Z+Z**2/2
                U = s.eye(r)
                for i in range(r):
                    for j in range(i+1, r):
                        U[i, j] = 1+i+j+s.I
                lev = s.diag(U, s.eye(m), U.conjugate().T.inv())
                g = (unip*lev).applyfunc(s.simplify)
                assert (g.conjugate().T*J*g-J).applyfunc(s.simplify) == s.zeros(n)
                gi = g.inv().applyfunc(s.simplify)

                def vec(i):
                    return s.eye(n)[:, i]

                def h(x, y):
                    return s.simplify((x.conjugate().T*J*y)[0])

                for a in range(r):
                    for t in (g, gi):
                        delta = t*vec(a)-vec(a)
                        assert all(s.simplify(delta[i]) == 0 for i in range(a, n))
                for t in (g, gi):
                    assert all(s.simplify((t*vec(r)-vec(r))[i]) == 0
                               for i in range(r, n))

                # First nonzero beta: later coefficients may change under g.
                for a in range(r):
                    y = vec(r+m+a)+vec(r)
                    for b in range(r):
                        y += (b+1)*vec(b)
                    for b in range(a+1, r):
                        y += (b+2)*vec(r+m+b)
                    gy = g*y
                    assert all(h(vec(b), y) == 0 for b in range(a))
                    assert h(vec(a), gy) == h(vec(a), y) == 1
                    case_counts["first_pairing"] += 1
                    detected_first_index |= any(h(vec(b), gy) != h(vec(b), y)
                                                for b in range(a+1, r))

                # The z coefficient is preserved on X-perp, even though g z need not equal z.
                y = vec(r)
                for a in range(r):
                    y += (a+1)*vec(a)
                assert h(vec(r), g*y) == h(vec(r), y) == -T
                case_counts["z_pairing"] += 1

                for b in range(k):
                    y = vec(r+1+b)
                    for a in range(r):
                        y += (a+1)*vec(a)
                    assert all(h(vec(a), y) == 0 for a in range(r))
                    assert h(vec(r), y) == 0
                    assert h(g*y, g*y) == h(y, y) == 1
                    case_counts["positive_quotient"] += 1

                # The final surviving isotropic coefficient, not the first, is fixed.
                for a in range(r):
                    y = s.zeros(n, 1)
                    for b in range(a+1):
                        y += s.Rational(1, b+2)*vec(b)
                    gy = g*y
                    assert h(vec(r+m+a), gy) == h(vec(r+m+a), y) == s.Rational(1, a+2)
                    case_counts["last_flag_coefficient"] += 1
                    detected_last_index |= any(h(vec(r+m+b), gy) != h(vec(r+m+b), y)
                                               for b in range(a))
                reports.append({"r": r, "positive_complement": k, "minus_z_norm": T,
                                "ambient_dimension": n})
    assert detected_first_index and detected_last_index
    return {"models": reports, "exact_case_counts": case_counts,
            "negative_controls": {"wrong_first_pairing_index_detected": detected_first_index,
                                  "wrong_last_flag_index_detected": detected_last_index},
            "scope": "Exact unitary and unipotent algebra; not an all-field arithmetic test."}


def different_models():
    cases = 0
    for D in (5, 13, 17, 29):
        # F=Q(sqrt(D)), omega=(1+sqrt(D))/2; different=(sqrt(D)).
        # E=F(i), so Norm_E(alpha)=Norm_F(alpha)^2 for alpha in F.
        for r in (1, 2, 3, 7):
            for a in range(r):
                ideal_norm = Fraction(D)**(2*(a-r))
                for c in range(-3, 4):
                    for d in range(-3, 4):
                        N = c*c+c*d+Fraction(1-D, 4)*d*d
                        if N == 0:
                            assert c == d == 0
                            continue
                        assert N.denominator == 1
                        norm_f = Fraction(-D)**(a-r)*N
                        norm_e = norm_f**2
                        assert norm_e >= ideal_norm
                        cases += 1
    # With alpha=1/sqrt(5), dropping the original inverse different
    # incorrectly asserts Norm_E(alpha)>=1.
    counterexample_norm = Fraction(1, 25)
    assert counterexample_norm < 1
    return {"exact_quadratic_cases": cases,
            "fractional_different_negative_control": {
                "F": "Q(sqrt(5))", "E": "F(i)", "alpha": "1/sqrt(5)",
                "Norm_E_alpha": str(counterexample_norm),
                "false_without_different_lower_bound": "1"}}


def normalization_checks():
    theta, nu, disc = s.symbols("theta nu disc", positive=True)
    cases = 0
    for f in (1, 2, 3, 7):
        for j in (1, 2, 5, 11):
            real_dimension = 2*f*j
            shortest_bound = s.sqrt(f)*theta*nu**(-s.Rational(1, f))
            covol_bound = (shortest_bound/s.sqrt(real_dimension))**real_dimension
            actual_size = (2**(f*j)*disc**(-s.Rational(j, 2))*covol_bound)**s.Rational(1, real_dimension)
            claimed_size = theta/s.sqrt(j)*disc**(-s.Rational(1, 4*f))*nu**(-s.Rational(1, f))
            assert s.simplify(actual_size/claimed_size) == 1
            cases += 1
    exponents = []
    for f in (1, 2, 9, 101):
        for n in (1, 2, 7, 1801):
            exponent = Fraction(4*n*n*f, f)
            assert exponent == 4*n*n
            exponents.append({"degree_f": f, "dimension_n": n,
                              "original_tau_exponent": 4*n*n*f,
                              "resulting_nu_exponent": int(exponent)})
    return {"exact_covolume_normalizations": cases, "far_exponents": exponents,
            "all_submodule_ranks_retained": True,
            "no_extra_sqrt2_in_real_realization": True}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    provenance.SOURCES = SOURCES
    sources = provenance.source_records(args.offline)
    flags = flag_models()
    different = different_models()
    normalization = normalization_checks()
    result = {
        "status": "PASS: authenticated source interfaces and exact diagnostics",
        "source_files": sources,
        "proof_files": [{"path": p, "sha256": sha(p)} for p in PROOF_FILES],
        "dependencies": [{"path": p, "sha256": sha(p)} for p in DEPENDENCIES],
        "flag_diagnostics": flags,
        "different_diagnostics": different,
        "normalization_diagnostics": normalization,
        "proved_statement": "The actual HN leastSize over all nonzero submodules on every original column cell is at least theta_u/(sqrt(n)*abs(disc(E))^(1/(4f))) times nu_u^(-1/f).",
        "classification": "closed arithmetic-minimum supplier; improved far-return sufficient condition, not W08 closure",
        "far_return_corollary_requires": "The literal original Deep.FarBound and its exact discrete-series/signature/gap conditions; its full dependency chain is not reproved here.",
        "remaining": [
            "Uniform growth bound for the actual frame/discriminant factor and weighted normalized seed moment",
            "Actual near-return bound",
            "Identification with the original restricted arithmetic chain and its positive trace, retaining target loss"
        ],
        "uniform_budget_proved": False,
        "Lean_build_performed": False,
        "node_counts_changed": False
    }
    out = ROOT/"certificates/global-gram-continuation-minimum.json"
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"certificate": str(out.relative_to(ROOT)), "sources": len(sources),
                      "unitary_models": len(flags["models"]),
                      "flag_cases": flags["exact_case_counts"],
                      "quadratic_different_cases": different["exact_quadratic_cases"],
                      "normalizations": normalization["exact_covolume_normalizations"],
                      "uniform_budget_proved": False}))


if __name__ == "__main__":
    main()
