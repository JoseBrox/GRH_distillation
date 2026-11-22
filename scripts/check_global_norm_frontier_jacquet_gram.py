#!/usr/bin/env python3
"""Exact checks and bounded-source authentication for the Jacquet Gram transfer."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from math import comb
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "global-norm-frontier-jacquet-gram"
B = "CompanionTheory.AutomorphicTheory.PieriRules.ThetaBesselIsometries."
SOURCES = [
    (B+"TensorMomentTransfer", [(65, 108)]),
    (B+"TensorMomentWeighted", [(54, 120)]),
    (B+"TensorMomentEstimate", [(59, 123)]),
    (B+"TensorWeightedBesselGap", [(65, 83)]),
    (B+"BesselSettingUniformConstant", [(62, 112)]),
    ("Development.AbelianVarietyTheory.Proofs.FlagMeasures."
     "BesselExteriorPowerConstantBoundLargeGap", [(34, 124)]),
    ("CompanionTheory.AutomorphicTheory.BesselWaveGrids."
     "WaveBallEstimateWeightedDualAlt", [(44, 66), (215, 258), (766, 848)]),
    ("Development.AbelianVarietyTheory.Proofs.JetHarmonics."
     "BesselNormSqEqConstMulArchPairing", [(18, 53), (59, 76)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.LeadMinorK",
     [(18, 61), (68, 115)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.OnePlaceEstimates", [(57, 64)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.RelevantZeroGramTerms",
     [(138, 154), (163, 176), (256, 259), (460, 498)]),
    ("Formalism.PeriodIntegrals.UpqRep",
     [(201, 207), (228, 235), (296, 302), (327, 332)]),
    ("Formalism.PeriodIntegrals.BesselPeriodGGP", [(24, 25)]),
    ("Development.AbelianVarietyTheory.Definitions.Jets.SumIoPrAlt", [(155, 169)]),
    ("Development.AbelianVarietyTheory.Proofs.JetHarmonics.NumericalFamilyShapeGaps",
     [(73, 116)]),
    ("Formalism.HermitianCurvature.BesselNonvanishingReduction", [(22, 34)]),
    ("Development.AbelianVarietyTheory.Proofs.FlagMeasures."
     "ExistsUnitaryTorusScaleBesselCharacter", [(15, 17), (178, 196), (207, 230)]),
    ("Development.AbelianVarietyTheory.Proofs.FlagMeasures."
     "NormalizedBesselMapsAnyScalePieriConstants", [(18, 59)]),
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def exact_equal(a, b):
    return sp.simplify(a-b) == 0


def norm_sq(z):
    return sp.expand_complex(z*sp.conjugate(z))


def source_records(offline):
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert digest(packed) == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert (atlas["repository"], atlas["commit"]) == (REPO, REV)
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        path = "lean/src/"+module.replace(".", "/")+".lean"
        rec = inspect_file({"repository": REPO, "commit": REV, "path": path,
                            "git_blob_sha1": blobs[module]}, offline)
        assert rec["matches_pinned_blob"]
        lines = (ROOT/"build/source-cache"/REPO/REV/path).read_bytes().splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            data = b"".join(lines[lo-1:hi])
            assert len(data) <= 12288
            excerpts.append({"lines": [lo, hi], "bytes": len(data), "sha256": digest(data)})
        records.append({"module": module, **{key: rec[key] for key in
                        ["repository", "commit", "path", "bytes", "sha256",
                         "git_blob_sha1", "matches_pinned_blob"]},
                        "excerpts": excerpts})
    return records


def vandermonde(x):
    return sp.prod(x[i]-x[j] for i in range(len(x)) for j in range(i+1, len(x)))


def degree_checks():
    symbolic = 0
    for n in range(1, 6):
        x = sp.symbols("x:"+str(n))
        delta = vandermonde(x)
        for ell in range(n+1):
            total = sum(vandermonde([x[j]+int(j in I) for j in range(n)])
                        for I in itertools.combinations(range(n), ell))
            assert sp.expand(total-comb(n, ell)*delta) == 0
            symbolic += 1
    numerical = 0
    for n in range(2, 10):
        for gap in [2, 3, 7]:
            mu = [sp.Rational(2, 3)+gap*(n-j)+j*j for j in range(n)]
            # Force decreasing order while retaining nonuniform gaps >= 2.
            mu = [sp.Rational(2, 3)+gap*(n-j)+(n-j)**2 for j in range(n)]
            for ell in range(n+1):
                ratios = [vandermonde([mu[j]+int(j in I) for j in range(n)])/vandermonde(mu)
                          for I in itertools.combinations(range(n), ell)]
                assert all(z > 0 for z in ratios)
                assert sum(ratios) == comb(n, ell)
                numerical += 1
    x = [sp.Rational(1, 4), sp.Integer(0)]
    crossing = sum(abs(vandermonde([x[j]+int(j in I) for j in range(2)]))
                   for I in itertools.combinations(range(2), 1))
    assert crossing != 2*abs(vandermonde(x))
    return {"symbolic_polynomial_identities": symbolic,
            "exact_ordered_parameter_cases": numerical,
            "chamber_crossing_negative_control": {
                "parameters": ["1/4", "0"], "sum_positive_degrees": str(crossing),
                "claimed_without_gap": str(2*abs(vandermonde(x)))}}


def signed_projection_checks():
    gamma = sp.diag(1, -1)
    count = 0
    for u in [sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(2, 3)]:
        c, s = (1+u*u)/(1-u*u), 2*u/(1-u*u)
        inc = sp.Matrix([[c, s], [s, c]])
        proj = inc.inv()
        assert inc.H*gamma*inc == gamma
        assert proj == gamma*inc.H*gamma
        for i in range(2):
            y = 2+sp.I
            v = inc[:, i]*y
            assert exact_equal(abs((v.H*gamma*v)[0]), norm_sq(y))
            assert sum(norm_sq(z) for z in v) >= norm_sq(y)
            for j in range(2):
                e = sp.eye(2)[:, j]
                a = gamma*e*v[j]
                pair = sp.conjugate(y)*(proj*a)[i]
                assert exact_equal(norm_sq(pair), norm_sq(v[j])**2)
                count += 1
    return {"signed_adjoint_coordinate_checks": count,
            "nonisometric_inclusions_tested": True}


def finite_period_gram_checks():
    """C4 model with nonunit Haar masses and both original subgroup masses."""
    cases = zero_cases = 0
    for haar, left, right, radial in itertools.product(
            [sp.Rational(3, 2), sp.Integer(2)],
            [sp.Rational(5, 3), sp.Integer(1)],
            [sp.Rational(7, 2), sp.Integer(1)],
            [sp.Rational(2, 5), sp.Integer(1)]):
        degree = 1/(4*haar)
        for f in [0, 1+2*sp.I]:
            weights = [0, 1, 2]
            signs = [1, -1, 1]
            omega = [1+sp.I, 2, sp.Rational(1, 2)-sp.I]
            prime = [2-sp.I, 1+3*sp.I, sp.Rational(2, 3)]
            scalars = [signs[j]*prime[j]*sp.conjugate(omega[j])
                       for j in range(3)]
            coeffs = [[scalars[j]*(sp.I**(weights[j]*g))*f for g in range(4)]
                      for j in range(3)]
            for i in range(3):
                for j in range(3):
                    if i != j:
                        assert exact_equal(sum(coeffs[i][g]*sp.conjugate(coeffs[j][g])
                                               for g in range(4)), 0)
            period = [left*right*sum(coeffs[j][g] for j in range(3)) for g in range(4)]
            exact_norm = sp.simplify(radial*haar/(left*right)*sum(norm_sq(z) for z in period))
            s_squared = left*right*norm_sq(f)
            rhs = sp.simplify(radial*s_squared*sum(norm_sq(z)/degree for z in scalars))
            assert exact_equal(exact_norm, rhs)
            cases += 1
            zero_cases += int(f == 0)
            if f != 0 and left*right != 1:
                wrong = sp.simplify(radial*norm_sq(f)*sum(norm_sq(z)/degree for z in scalars))
                assert not exact_equal(exact_norm, wrong)
    d, di, mp, mq = sp.symbols("d di mp mq", positive=True)
    # Bound products of the two original normalized scalar squares.
    assert sp.simplify((mp*di/d)*(mq*di/d)*d/di-mp*mq*di/d) == 0
    return {"exact_C4_gram_models": cases, "zero_models": zero_cases,
            "nonunit_Haar_and_period_masses_retained": True,
            "wrong_period_mass_negative_control": True,
            "formal_degree_cancellation": "symbolically exact"}


def reserve_checks():
    count = 0
    for r in range(101):
        for k in [1, 2, 7, 23]:
            n, m = 2*r+k+1, 2*r+2
            for ell in range(r+2):
                a = 0 if ell == 0 else 1 if ell == 1 else ell+1
                assert ell+a <= (r+1)*(r+2)
                assert 2*a <= 4*n*n
                assert 2*ell <= m
                # (TT')^ell <= b^(2 C m ell); remaining exponent <= 9m^2.
                assert 8*m*m+ell <= 9*m*m
                count += 1
    return {"all_integer_reserves_r_0_to_100": count,
            "r_zero_included": True}


def original_budget_checks():
    rounding = 0
    for r in range(41):
        reserve = (r+1)*(r+2)
        for norm in range(11):
            for slack in [0, sp.Rational(1, 7), sp.Rational(1, 2),
                          sp.Rational(6, 7), 1, sp.Rational(19, 3)]:
                real_budget = norm+reserve+slack
                integer_budget = sp.floor(real_budget)
                assert norm+reserve <= integer_budget
                assert 100*(integer_budget+1) <= 200*real_budget
                assert 100*(integer_budget+1) <= 200**2*real_budget
                rounding += 1
    lattice = 0
    for r in range(21):
        for k in range(1, 12):
            n = 2*r+k+1
            full_offset = sp.Rational(n-1, 2)
            compact_offset = sp.Rational(k-1, 2)
            for a in [-7, 0, 9]:
                for b in [-3, 0, 11]:
                    assert (a+full_offset-b-compact_offset-sp.Rational(1, 2)).is_integer
                    assert (a+full_offset-b-full_offset).is_integer
                    lattice += 1
    q, n, x, y = sp.symbols("q n x y")
    r, k = q-1, n-2*q+1
    ag = 4*(k+r)*q
    dn = r*(r-1)+2*r*(k+1)+r*r
    ass = (n-1)*dn
    mex = 2*(r*r+r+1)
    polynomials = {
        "dN": 2*q*n-dn,
        "first_GapOK_gate": 20*q**3*n**2-(2*mex*(ass+ag)+ag+3),
        "second_GapOK_gate": 16*q*n**2-(9*q*n**2+3*ag+3),
    }
    certificate = {}
    for name, difference in polynomials.items():
        poly = sp.Poly(sp.expand(difference.subs(n, 2*q+y).subs(q, x+1)), x, y)
        assert all(c >= 0 for c in poly.coeffs())
        certificate[name] = {
            "substitution": "q=x+1, n=2q+y, x=r>=0, y=k-1>=0",
            "positive_coefficient_polynomial": str(poly.as_expr()),
            "terms": len(poly.terms()),
        }
    q, cg, n = sp.symbols("q Cg n", positive=True)
    original_h = cg*(2*q)**sp.Rational(9, 2)*(3*q*n*n+n**3)
    assert sp.simplify(original_h/(32*sp.sqrt(2*q))
                       -cg*q**4*(3*q*n*n+n**3)/2) == 0
    return {"exact_rounding_cases": rounding, "HC_lattice_cases": lattice,
            "unbounded_gap_certificates": certificate,
            "noncompact_gap_normalizer": "symbolically exact",
            "empty_cloud_pair_convention": "retained as sInf(empty)=0; positive reserve impossible"}


def original_scale_checks():
    torus_cases = flag_cases = 0
    for r in range(6):
        for k in [1, 2, 4]:
            n = 2*r+k+1
            hermitian = sp.zeros(n)
            for i in range(r):
                hermitian[i, n-1-i] = hermitian[n-1-i, i] = 1
            for i in range(r, r+k+1):
                hermitian[i, i] = -1 if i == r+k else 1
            for scale in [sp.Rational(1, 3), 1, 2, sp.Rational(5, 2)]:
                scale = sp.Rational(scale)
                diag = [sp.Integer(1)]*n
                for i in range(r):
                    diag[i] = scale**(i-r)
                    diag[n-1-i] = 1/diag[i]
                t = sp.diag(*diag)
                assert t.H*hermitian*t == hermitian
                for ell in range(r+2):
                    ss = r*ell-ell*(ell-1)//2
                    assert sp.prod(1/diag[i] for i in range(min(ell, r))) == scale**ss
                    flag_cases += 1
                torus_cases += 1
    branch_cases = 0
    for r in range(101):
        m = 2*r+2
        for ell in range(r+2):
            ss = r*ell-ell*(ell-1)//2
            assert 4*ss-4*r*ell == -2*ell*(ell-1)
            exponent_one = 4*r*ell
            exponent_a = 4*r*ell-2*ell*(ell-1)
            assert 0 <= exponent_a <= exponent_one
            assert 2*m*ell+4*r*ell <= 2*m*m
            assert 8*m*m+ell <= 9*m*m
            branch_cases += 2
    return {"exact_Hpk_torus_cases": torus_cases,
            "exact_original_flag_scalings": flag_cases,
            "two_scale_branch_exponent_cases": branch_cases,
            "normalization": "Original subgroup/quotient measures are pushed; group and radial measures retained",
            "sufficient_constants": {"Cq": ">=200", "Cg": ">=1000000", "Cb": ">=Ch+5"}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    records = source_records(args.offline)
    checks = {"formal_degrees": degree_checks(),
              "signed_projections": signed_projection_checks(),
              "period_gram": finite_period_gram_checks(),
              "reserves": reserve_checks(),
              "original_real_budget": original_budget_checks(),
              "original_character_scales": original_scale_checks()}
    files = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
             f"paper/shared/{STEM}-references.tex", f"scripts/check_{STEM.replace('-', '_')}.py",
             "paper/shared/global-norm-frontier-first-length.tex",
             "paper/shared/global-norm-frontier-quotient-mass.tex",
             "paper/sections/recovered/72-fd-section.tex",
             "paper/sections/recovered/94-jp-section.tex"]
    result = {
        "schema_version": 1, "status": "PASS",
        "classification": [
            "closed Gram-transfer, real-budget and character-scale subobligations",
            "improved sufficient condition for the complete original leading-minor interface"],
        "theorem": "Original weighted Jacquet norm <= binom(n,ell) kappa^(4 S_ell) (T T')^ell b^(8 m^2) times its same unweighted norm, including both original scales and original q0 reserve",
        "exact_identity": "Mutually orthogonal exterior-Pieri Jacquet summands; sum of same-measure degree ratios is binom(n,ell)",
        "checks": checks, "sources": records,
        "artifact_hashes": {p: digest((ROOT/p).read_bytes()) for p in files},
        "scope": {
            "written_proof": "Shared TeX and mathematical note",
            "computation": "Exact identities and bounded regressions supplement the written proof",
            "not_verified": ["Existence of the representation/Pieri families",
                             "Existence of the original period-normalized Bessel families",
                             "Exact normalized-lowering and Capelli inputs retained from the preceding theorem",
                             "Weighted orbital estimate", "Global period Gram assembly",
                             "Any full Lean build"],
            "whole_node_count_changed": False,
        },
    }
    dest = ROOT/"certificates"/(STEM+".json")
    dest.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(records),
                      "checks": checks, "certificate": str(dest.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    main()
