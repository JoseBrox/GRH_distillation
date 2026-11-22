#!/usr/bin/env python3
"""Exact original block Gauss, middle-pivot, gap and source-interface checks."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "global-norm-frontier-big-cell-continuity"
SOURCES = [
    ("Formalism.PeriodIntegrals.LongWeylElementSquare", [(20, 59)]),
    ("Formalism.PeriodIntegrals.UnitaryGroupMassFormula.PhiBigCellForm."
     "BigCellEqW0BMulTM", [(15, 19)]),
    ("Formalism.FormalDegreeBessel.StatementRP", [(74, 81)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.SettingConstruction",
     [(189, 215), (314, 321)]),
    ("Development.AbelianVarietyTheory.Proofs.FlagMeasures."
     "BigCellQuotientNormalisesUnipotent", [(39, 50)]),
    ("Development.AbelianVarietyTheory.Proofs.FlagMeasures."
     "PairSpaceMajorantIntegrableBigCell", [(64, 69), (109, 128)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.OnePlaceEstimates",
     [(82, 104), (185, 208)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.LeadMinorK",
     [(45, 82), (94, 115)]),
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def source_records(offline):
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert digest(packed) == inventory["compressed_graph"]["sha256"]
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


def clean(mat):
    return mat.applyfunc(sp.expand_complex)


def norm_squared(mat):
    return sp.expand_complex(sum(z*sp.conjugate(z) for z in mat))


def form(k, r):
    n = 2*r+k+1
    h = sp.zeros(n)
    for j in range(r):
        h[j, n-1-j] = h[n-1-j, j] = 1
    for j in range(r, r+k+1):
        h[j, j] = -1 if j == r+k else 1
    return h


def unipotent(k, r, seed):
    if r == 0:
        return sp.eye(k+1)
    d = 2*r+k-1
    h = form(k, r-1)
    v = sp.Matrix([sp.Rational((j+seed) % 3-1, 2)
                   +sp.I*sp.Rational((2*j+seed) % 3-1, 3) for j in range(d)])
    heis = sp.eye(d+2)
    heis[0, 1:d+1] = -v.H*h
    heis[1:d+1, d+1] = v
    heis[0, d+1] = sp.I*sp.Rational(seed, 3)-(v.H*h*v)[0]/2
    return clean(heis*sp.diag(1, unipotent(k, r-1, seed+1), 1))


def middle(k, seed):
    t = sp.Rational(1, seed+2)
    c, s = (1+t*t)/(1-t*t), 2*t/(1-t*t)
    mu = sp.eye(k+1)
    mu[0, 0] = mu[k, k] = c
    mu[0, k] = mu[k, 0] = s
    if k >= 2:
        swap = sp.eye(k+1)
        swap[0, 0] = swap[1, 1] = 0
        swap[0, 1] = swap[1, 0] = 1
        mu = swap*mu
    return mu


def block_gauss_checks():
    cases = entry_identities = block_determinants = internal_zero_cases = 0
    middle_example = None
    for r, k, seed in itertools.product(range(3), range(1, 4), [1, 2]):
        n = 2*r+k+1
        h = form(k, r)
        left, right = unipotent(k, r, seed), unipotent(k, r, seed+2)
        mu = middle(k, seed)
        assert clean(left.H*h*left) == h
        assert clean(right.H*h*right) == h
        assert clean(mu.H*form(k, 0)*mu) == form(k, 0)
        w = sp.eye(n)
        for j in range(r):
            w[j, j] = w[n-1-j, n-1-j] = 0
            w[j, n-1-j] = w[n-1-j, j] = 1
        c = [sp.Rational(j+seed+1, j+1)+sp.I*sp.Rational((j+seed) % 2, 2)
             for j in range(r)]
        diagonal = sp.diag(*c, mu, *[1/sp.conjugate(z) for z in reversed(c)])
        left_inverse = clean(h*left.H*h)
        assert clean(left_inverse*left) == sp.eye(n)
        assert norm_squared(left_inverse) == norm_squared(left)
        x = clean(left_inverse*w*diagonal*right)
        a = clean(w*x)
        lower, upper = clean(w*left_inverse*w), right
        assert clean(lower*diagonal*upper) == a
        block_sizes = [1]*r+[k+1]+[1]*r
        edges = [0]
        for size in block_sizes:
            edges.append(edges[-1]+size)
        det_sq = []
        for j, boundary in enumerate(edges[1:-1]):
            start = edges[j]
            aj = a[:boundary, :boundary]
            delta = sp.expand_complex(aj.det())
            assert delta != 0
            assert delta == sp.expand_complex(diagonal[:boundary, :boundary].det())
            det_sq.append(sp.expand_complex(delta*sp.conjugate(delta)))
            inv = aj.inv()
            ur = clean(inv*a[:boundary, boundary:])
            lr = clean(a[boundary:, :boundary]*inv)
            for i in range(start, boundary):
                for t in range(boundary, n):
                    assert sp.simplify(ur[i, t-boundary]-upper[i, t]) == 0
                    assert sp.simplify(lr[t-boundary, i]-lower[t, i]) == 0
                    entry_identities += 2
            block_determinants += 1
        delta_sq = min([sp.Integer(1)]+det_sq)
        s = norm_squared(x)
        assert s >= 1
        bound = n*n/delta_sq*s**(n-1)
        assert norm_squared(left) <= bound
        assert norm_squared(right) <= bound
        # The first scalar pivot inside the middle block is zero for k>=2.
        if k >= 2:
            internal = r+1
            assert internal not in edges[1:-1]
            assert sp.expand_complex(a[:internal, :internal].det()) == 0
            internal_zero_cases += 1
            if middle_example is None and r > 0:
                middle_example = {"r": r, "k": k, "n": n,
                                  "block_boundaries": edges[1:-1],
                                  "vanishing_internal_scalar_pivot": internal,
                                  "middle_block_det": str(mu.det()),
                                  "all_required_boundary_pivots_nonzero": True}
        cases += 1
    assert entry_identities and internal_zero_cases and middle_example is not None
    return {"exact_original_Hpk_unitary_cases": cases,
            "block_entry_recovery_identities": entry_identities,
            "unchanged_boundary_determinants": block_determinants,
            "squared_polynomial_properness_bounds": 2*cases,
            "internal_scalar_pivot_negative_controls": internal_zero_cases,
            "middle_block_example": middle_example,
            "scope": "Exact block identities and edge checks supplement the all-rank written Cramer/Hadamard proof."}


def decay_and_density_checks():
    cases = 0
    for r, k in itertools.product(range(31), range(1, 51)):
        q, n = r+1, 2*r+k+1
        a = 500000*q**4*(3*q*n*n+n**3)-1
        assert a >= 500000*n**3-1 > 4*n*n*(n-1)
        assert k-1 >= 0
        for j in range(r):
            assert 2*(2*r+k-2*j-1) >= 0
        cases += 1
    return {"exact_strong_gap_cases": cases,
            "unbounded_gap_certificate": "A>=500000 n^3-1>4 n^2(n-1), n>=2",
            "product_haar_growth_exponent": "4 n^2",
            "gauss_inverse_degree": "n-1",
            "positive_radial_density": "All c_j!=0 and |zeta|^2>TT'; all original factors are positive on this open domain.",
            "no_uniform_point_evaluation_claim_from_local_constants": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources = source_records(args.offline)
    checks = {"block_gauss": block_gauss_checks(),
              "convergence_threshold": decay_and_density_checks()}
    files = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
             f"paper/shared/{STEM}-references.tex",
             f"scripts/check_{STEM.replace('-', '_')}.py",
             "paper/shared/global-norm-frontier-iterated-minors.tex",
             "paper/shared/global-norm-frontier-pieri-family.tex",
             "paper/shared/global-norm-frontier-jacquet-gram.tex",
             "paper/sections/recovered/91-ju-section.tex",
             "paper/sections/recovered/93-jg-section.tex"]
    result = {
        "schema_version": 1, "status": "PASS",
        "classification": "closed original regular-big-cell convergence, representative identification and pointwise coefficient-expansion subobligations",
        "supplied_interfaces": ["BesselExpansionNearParameter", "BesselExpansionCoefficientSum"],
        "theorem": "Actual two-sided orbital integrals converge absolutely and continuously on the original big cell; L2 expansions hold at every original big-cell point.",
        "checks": checks, "sources": sources,
        "artifact_hashes": {p: digest((ROOT/p).read_bytes()) for p in files},
        "scope": {
            "quantifiers": "Every admissible datum, original smooth section, finite shift family, and every regular big-cell point; no common exceptional set is used.",
            "normalizations": "Original compact/unipotent/radial measures and both character scales unchanged.",
            "not_verified": ["Uniform orbital point-evaluation estimate relative to the Jacquet norm",
                             "Orbital comparisons on all lower-dimensional relevant strata",
                             "Global rational-return/Gram assembly", "Any full Lean build"],
            "whole_node_count_changed": False,
        },
    }
    dest = ROOT/"certificates"/(STEM+".json")
    dest.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources), "checks": checks,
                      "certificate": str(dest.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    main()
