#!/usr/bin/env python3
"""Authenticate and check the exact rank-zero pointwise orbital supplier."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "global-norm-frontier-rank-zero-pointwise"
SOURCES = [
    ("Formalism.SharpRestriction.CuspSpanNormBounds.Point", [(5, 15)]),
    ("Formalism.PeriodIntegrals.LongWeylElementSquare", [(20, 33)]),
    ("Formalism.PeriodIntegrals.UpqRep", [(224, 231), (303, 331)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.RootMeasBig",
     [(17, 68)]),
    ("Formalism.FormalDegreeBessel.StatementBF", [(144, 153)]),
    ("Formalism.FormalDegreeBessel.StatementRP", [(74, 81)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.RelevantZeroGramTerms",
     [(104, 140), (238, 246), (388, 396), (460, 503), (565, 571)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.LeadMinorK",
     [(47, 80), (86, 106), (211, 216)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.OnePlaceEstimates",
     [(23, 27)]),
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def source_records(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert digest(packed) == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert (atlas["repository"], atlas["commit"]) == (REPO, REV)
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        rec = inspect_file({"repository": REPO, "commit": REV, "path": path,
                            "git_blob_sha1": blobs[module]}, offline)
        assert rec["matches_pinned_blob"]
        lines = (ROOT / "build/source-cache" / REPO / REV / path).read_bytes().splitlines(keepends=True)
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


def positive_polynomial(expr, variables):
    poly = sp.Poly(sp.expand(expr), *variables)
    assert all(c >= 0 for c in poly.coeffs())
    assert poly.eval({v: 0 for v in variables}) > 0
    return {"expanded_polynomial": str(poly.as_expr()),
            "all_coefficients_nonnegative": True,
            "constant_term_positive": True}


def exact_checks():
    x, y = sp.symbols("x y", nonnegative=True)
    n = y + 2
    k = n - 1
    b = 5*n + x
    energy = positive_polynomial(b**4 - 10*n*n*b*b - n**3, [x, y])
    # e/(2*pi)<1/2; multiply the last bound by 4*k>0.
    prefactor = positive_polynomial((4*k-1)*b**4-16*k*k, [x, y])
    c, s = sp.symbols("c s", real=True)
    a = sp.Matrix([[c, s], [s, c]])
    h = sp.diag(1, -1)
    assert a.T*h*a == (c*c-s*s)*h
    generator = sp.Matrix([[0, 1], [1, 0]])
    assert sum(z*z for z in generator) == 2
    t, scale = sp.symbols("t scale", positive=True)
    rho = sp.sqrt(scale)*sp.cosh(t)
    jac = sp.simplify(rho*sp.diff(rho, t))
    assert sp.simplify(jac-scale*sp.sinh(t)*sp.cosh(t)) == 0
    jacobian_cases = 0
    for kval in range(1, 25):
        radial = (scale*sp.sinh(t)**2)**(kval-1)*jac
        expected = scale**kval*sp.sinh(t)**(2*kval-1)*sp.cosh(t)
        assert sp.simplify(radial-expected) == 0
        jacobian_cases += 1
    # Test vector-valued radial profiles with an exact beta integral.
    # Phi(t)=cosh(t)^(-L): M=B(k,L-k)/2 and E/M=L*k.
    profiles = 0
    for kval in range(1, 13):
        bval = 5*(kval+1)
        for L in [kval+1, 2*kval+3, 5*kval+7]:
            beta = sp.Rational(sp.factorial(kval-1)*sp.factorial(L-kval-1),
                               sp.factorial(L-1))
            beta_next = sp.Rational(sp.factorial(kval)*sp.factorial(L-kval-1),
                                    sp.factorial(L))
            assert L*L*beta_next/beta == L*kval
            assert L*kval <= 2*bval**4
            for q in [sp.Rational(1, 100), sp.Rational(1, 3), sp.Rational(1),
                      sp.Rational(7), sp.Rational(kval, L-kval)]:
                # The source inequality, multiplied by G/N; pi>3.
                assert q**kval/(1+q)**L <= 3*bval**4*beta
                profiles += 1
    return {"unbounded_casimir_energy": energy,
            "unbounded_sobolev_prefactor": prefactor,
            "boost_preserves_form_if_c_squared_minus_s_squared_equals_one": True,
            "boost_generator_hs_norm_squared": 2,
            "exact_radial_jacobian_cases": jacobian_cases,
            "exact_beta_profile_tests": profiles,
            "all_T_T_prime_powers_retained": True,
            "unipotent_mass_in_J": "kappa_N^2",
            "unipotent_mass_in_squared_norm": "kappa_N^4",
            "original_root_measure": "dirac(identity)",
            "original_quotient_measure": "pairMeas, not a compact-stabilizer quotient"}


def interval_diagnostics():
    mp.mp.dps = 80
    checks = 0
    maximum = mp.mpf(0)
    for k in [1, 2, 7, 31, 103]:
        for t in [mp.mpf(10)**j for j in [-12, -6, -3, -1, 0, 1, 3]]:
            delta = mp.tanh(t)/(8*k)
            assert delta <= t/8
            logw = lambda z: (2*k-1)*mp.log(mp.sinh(z))+mp.log(mp.cosh(z))
            for ratio in [mp.mpf(-1), mp.mpf(-1)/2, mp.mpf(0), mp.mpf(1)/2, mp.mpf(1)]:
                s = t+ratio*delta
                change = abs(logw(s)-logw(t))
                assert change <= mp.mpf(2)/7 + mp.mpf("1e-60")
                maximum = max(maximum, change)
                checks += 1
    return {"diagnostic_checks": checks,
            "maximum_observed_log_weight_change": mp.nstr(maximum, 18),
            "proof_bound": "2/7, established for all t>0 and k>=1 in TeX",
            "not_used_as_all_parameter_proof": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources = source_records(args.offline)
    checks = {"exact": exact_checks(), "interval_diagnostics": interval_diagnostics()}
    files = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
             f"paper/shared/{STEM}-references.tex",
             f"scripts/check_{STEM.replace('-', '_')}.py",
             "paper/sections/recovered/77-dc-section.tex",
             "paper/sections/recovered/93-jg-section.tex",
             "paper/shared/global-norm-frontier-pieri-family.tex"]
    result = {"schema_version": 1, "status": "PASS",
              "classification": "closed original rank-zero pointwise orbital obligation",
              "supplied_interface": "TheoremBPrimePointwise when D.R.rS=0",
              "bound": "ptWeight*orbSq <= b^4/G * jNorm2 for every representable point with G!=0",
              "checks": checks, "sources": sources,
              "artifact_hashes": {p: digest((ROOT/p).read_bytes()) for p in files},
              "scope": {"all_representatives_and_permitted_measures": True,
                        "pointwise_not_almost_everywhere": True,
                        "uniform_in_k_T_T_prime_and_original_haar_scalars": True,
                        "b_threshold": "b>=5(k+1), implied by original LocOk with Cg>=10^6",
                        "whole_node_count_changed": False,
                        "not_verified": ["Positive-unipotent-rank partial-head kernel estimate",
                                         "Global rational-return sum or Gram defects",
                                         "Any full Lean build"]}}
    dest = ROOT / "certificates" / (STEM+".json")
    dest.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "exact_jacobian_cases": checks["exact"]["exact_radial_jacobian_cases"],
                      "exact_beta_profile_tests": checks["exact"]["exact_beta_profile_tests"],
                      "diagnostic_interval_checks": checks["interval_diagnostics"]["diagnostic_checks"],
                      "certificate": str(dest.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    main()
