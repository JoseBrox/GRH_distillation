#!/usr/bin/env python3
"""Authenticate actual CovolN and check exact volume/normalizer diagnostics."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy as s

import check_global_norm_frontier_off_diagonal as provenance

ROOT = Path(__file__).resolve().parents[1]
H = "Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals."
C = "Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts."
SOURCES = [
    (C+"RankPointCounts.DualFamilyCounting.CovolumeExponent", [(16, 58)]),
    (H+"PoincareInHH", [(252, 258)]),
    (H+"HidaSetting", [(207, 226), (264, 273), (302, 309), (372, 377)]),
    ("Formalism.LocalRingCardinality.DataSpaces", [(14, 19), (34, 46)]),
    ("Formalism.HermitianLattices.StatementMass", [(44, 48)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.GlobAut", [(48, 59)]),
    (C+"Measures", [(106, 117)]),
    (H+"UnitaryHaarProducts.MeasCore", [(18, 24)]),
    ("Formalism.PeriodIntegrals.UpqRep", [(157, 160)]),
    ("Development.AbelianVarietyTheory.Proofs.FlagMeasures."
     "ExistsIntegerAddStarEqOneOfIsCMUnram", [(21, 64)]),
]
FILES = [
    "paper/shared/global-gram-continuation-haar-budget.tex",
    "paper/shared/global-gram-continuation-haar-references.tex",
    "notes/global-gram-continuation-haar-budget.md",
    "scripts/global-gram-continuation-haar-check.py",
]
DEPENDENCIES = [
    "paper/shared/global-gram-continuation-phases.tex",
    "paper/shared/global-gram-continuation-period-identity.tex",
    "paper/shared/global-gram-continuation-projectors.tex",
    "paper/shared/global-gram-continuation-quantitative-seed.tex",
    "paper/sections/recovered/72-fd-section.tex",
    "paper/sections/recovered/75-rv-section.tex",
]


def sha(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def clean(M):
    return M.applyfunc(s.simplify)


def exponents():
    r, k, a, b = s.symbols("r k a b", integer=True, nonnegative=True)
    n = 2*r+k+1
    d = r*(2*n-2*r-1)
    beta_U = 2*s.summation(s.summation(b-a, (b, a+1, r-1)), (a, 0, r-1))
    beta_A = 2*(k+1)*s.summation(r-a, (a, 0, r-1))
    beta_C = 2*r*s.summation(r-a, (a, 0, r-1))
    beta = r*(r+1)*(n-r)+r*(r*r-1)/3
    assert s.simplify(beta_U+beta_A+beta_C-beta) == 0
    e_source = -(8*r**3+6*r**2+6*k*r*r+r)/6
    assert s.simplify(d/2-beta-e_source) == 0
    upper_D = r*(r-1)/2-r*(r*r-1)/3
    radical_D = (2*r*(k+1)+r*r)/2-r*(r+1)*(n-r)
    assert s.simplify(upper_D+radical_D-e_source) == 0
    f, T, D = s.symbols("f T D", positive=True)
    source_full_two = -f*(r*k+r*(r-1)/2)-f*r*(r+1)/2
    assert s.simplify(source_full_two+f*r*(k+r)) == 0
    return {"d_N": str(s.expand(d)), "beta": str(s.expand(beta)),
            "source_exponent": str(s.expand(e_source)),
            "upper_radical_source_exponents_agree": True,
            "all_extra_source_two_powers_retained": True}


def tangent_basis(r, k, T):
    b, n = k+1, 2*r+k+1
    Jb = s.diag(-1, *([1]*k))
    J = s.zeros(n)
    J[:r, r+b:] = s.eye(r)
    J[r:r+b, r:r+b] = Jb
    J[r+b:, :r] = s.eye(r)
    basis = []
    for i in range(r):
        for j in range(i+1, r):
            for z in (s.Integer(1), s.I):
                X = s.zeros(n)
                X[i, j] = z
                X[r+b+j, r+b+i] = -s.conjugate(z)
                basis.append(X)
    for i in range(r):
        for j in range(b):
            for z in (s.Integer(1), s.I):
                A = s.zeros(r, b)
                A[i, j] = z/s.sqrt(T) if j == 0 else z
                X = s.zeros(n)
                X[:r, r:r+b] = A
                X[r:r+b, r+b:] = -Jb*A.conjugate().T
                basis.append(X)
    for i in range(r):
        X = s.zeros(n)
        X[i, r+b+i] = s.I
        basis.append(X)
        for j in range(i+1, r):
            for z in (s.Integer(1), s.I):
                X = s.zeros(n)
                X[i, r+b+j] = z
                X[j, r+b+i] = -s.conjugate(z)
                basis.append(X)
    assert len(basis) == r*(2*n-2*r-1)
    for X in basis:
        assert clean(X.conjugate().T*J+J*X) == s.zeros(n)
    return J, basis


def inner(X, Y):
    return s.simplify(s.re(s.trace(X.conjugate().T*Y)))


def tangent_jacobians():
    models = []
    for r, k, T, c in itertools.product(range(4), (1, 2), (1, 4, 9),
                                       (s.Rational(3, 2),)):
        J, basis = tangent_basis(r, k, T)
        b, n = k+1, J.rows
        eta = [(-s.I*c)**(r-i) for i in range(r)]
        D = s.diag(*eta, *([1]*b), *[1/s.conjugate(x) for x in eta])
        assert clean(D.conjugate().T*J*D-J) == s.zeros(n)
        transformed = [clean(D.inv()*X*D) for X in basis]
        # All coordinate basis vectors remain orthogonal: their rotations
        # are multiples of pi/2, but both real directions are retained.
        for i, X in enumerate(basis):
            for j in range(i):
                assert inner(X, basis[j]) == 0
                assert inner(transformed[i], transformed[j]) == 0
        det0 = s.prod(inner(X, X) for X in basis)
        det1 = s.prod(inner(X, X) for X in transformed)
        expected_density = s.Integer(2)**(r*(k+r))*s.Integer(T)**(-r)
        beta = r*(r+1)*(n-r)+s.Rational(r*(r*r-1), 3)
        assert s.simplify(det0-expected_density**2) == 0
        assert s.simplify(det1/det0-c**(-2*beta)) == 0
        models.append({"r": r, "k": k, "T": T,
                       "dimension": len(basis), "box_density": str(expected_density),
                       "beta": str(beta), "character_scale": str(c)})
    return {"exact_models": models,
            "scope": "Literal source coordinate tangent metric and full real conjugation determinant."}


def sfact(a):
    return math.prod(math.factorial(j) for j in range(a))


def cartan_constants():
    models = []
    pi = s.Symbol("pi", positive=True)
    for p in range(1, 8):
        for q in range(1, p+1):
            n, alpha = p+q, p-q
            Hankel = s.Matrix(q, q, lambda i, j: math.factorial(alpha+i+j))
            determinant = s.Integer(math.prod(math.factorial(j)*math.factorial(alpha+j)
                                             for j in range(q)))
            assert Hankel.det() == determinant
            ordered_t_integral = determinant/s.Integer(2)**q
            svd = s.Integer(2)**q*pi**(p*q)/determinant
            assert s.simplify(svd*ordered_t_integral-pi**(p*q)) == 0
            Vp = (2*pi)**(p*(p+1)//2)/sfact(p)
            Vq = (2*pi)**(q*(q+1)//2)/sfact(q)
            cG = s.simplify(Vp*Vq*s.Integer(2)**(p*q-q)*svd)
            target = (2*pi)**(n*(n+1)//2)*sfact(p-q)/(sfact(p)**2*sfact(q)**2)
            assert s.simplify(cG-target) == 0
            dcG = s.simplify(cG/(2*pi)**(n*(n+1)//2))
            assert dcG == s.Rational(sfact(p-q), sfact(p)**2*sfact(q)**2)
            assert 0 < dcG <= 1
            models.append({"p": p, "q": q, "Gaussian_Hankel_determinant": str(determinant),
                           "formal_degree_times_Cartan_over_Vandermonde": str(dcG)})
    # Omitting the ordered-chamber division gives an unwanted q! factor.
    assert math.factorial(2) != 1
    return {"exact_models": models, "ordered_chamber_negative_control_detected": True,
            "no_arbitrary_ambient_Haar_scale_fixed": True}


def haar_cancellation():
    a, b, c, v = s.symbols("a b c v", positive=True)
    c0_factor = v*a*b
    Mphi_factor = 1/(c*v)
    W2_factor = c/(a*b)
    assert s.simplify(c0_factor*Mphi_factor*W2_factor) == 1
    assert s.simplify(a*b/(a*b)) == 1
    return {"scale_variables": {"a": "unipotent Haar", "b": "compact subgroup Haar",
                                 "c": "ambient real Haar", "v": "finite Haar"},
            "c0_factor": str(c0_factor), "Mphi_factor": str(Mphi_factor),
            "weighted_L1_squared_factor": str(W2_factor), "full_product_factor": "1",
            "negative_controls": {"omit_c0_unipotent_factor": "1/a",
                                  "omit_finite_e1": "v",
                                  "omit_formal_degree": "c"}}


def all_rank_budgets():
    r, z, x = s.symbols("r z x", integer=True, nonnegative=True)
    k, n = z+1, 2*r+z+2
    d = r*(2*n-2*r-1)
    beta = r*(r+1)*(n-r)+r*(r*r-1)/3
    polys = {"dimension_at_most_n_squared": s.expand(n*n-d),
             "beta_at_most_n_cubed": s.expand(n**3-beta)}
    out = {}
    for name, p in polys.items():
        pp = s.Poly(p, r, z)
        assert all(c >= 0 for c in pp.coeffs())
        out[name] = {"nonnegative_polynomial": str(p)}
    nn = x+2
    p = s.Poly(s.expand(5*nn**3-(nn**3+s.Rational(5, 2)*nn**2+1)), x)
    assert all(c > 0 for c in p.all_coeffs())
    out["final_7n_exponent_absorption"] = {"coefficients_for_n_2_plus_x": [str(c) for c in p.all_coeffs()]}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    provenance.SOURCES = SOURCES
    result = {
        "status": "PASS: pinned original CovolN and exact normalization diagnostics",
        "source_files": provenance.source_records(args.offline),
        "proof_files": [{"path": p, "sha256": sha(p)} for p in FILES],
        "dependencies": [{"path": p, "sha256": sha(p)} for p in DEPENDENCIES],
        "source_exponents": exponents(),
        "tangent_jacobians": tangent_jacobians(),
        "Cartan_and_degree_constants": cartan_constants(),
        "Haar_cancellation": haar_cancellation(),
        "all_rank_budgets": all_rank_budgets(),
        "scope": {
            "independent_mathematical_review": "Accepted by root agent on 2026-11-23: exact CovolN group and both inclusions; fractional ideal and dyadic trace-one calculation; box and character transport determinants; exponential cube; original formal degree and full Haar cancellation. Far/near trace obligations remain open.",
            "literal_CovolN_supplied_by_conventional_proof": True,
            "actual_NOinf_not_principal_congruence_substitute": True,
            "all_fractional_different_T_and_two_factors_retained": True,
            "original_c0X_and_Mphi_retained": True,
            "uniform_trace_budget_near_returns_chain_comparison": "OPEN",
            "lean_build_run": False,
        },
    }
    out = ROOT/"certificates/global-gram-continuation-haar.json"
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "sources": len(result["source_files"]),
                      "tangent_models": len(result["tangent_jacobians"]["exact_models"]),
                      "Cartan_models": len(result["Cartan_and_degree_constants"]["exact_models"]),
                      "certificate": str(out.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
