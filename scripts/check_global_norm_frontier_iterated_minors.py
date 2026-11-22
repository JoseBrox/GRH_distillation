#!/usr/bin/env python3
"""Exact collision/reserve checks and original weighted-L2 interface hashes."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction
from math import comb, floor, prod
from pathlib import Path

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "global-norm-frontier-iterated-minors"
PREFIX = "Formalism.SharpRestriction.CuspSpanNormBounds."
SOURCES = [
    (PREFIX+"LeadMinorK", [(86, 117), (211, 221)]),
    (PREFIX+"OnePlaceEstimates", [(57, 104), (164, 208)]),
    ("CompanionTheory.AutomorphicTheory.PieriRules.ThetaBesselIsometries."
     "TensorMomentWeighted", [(54, 120)]),
    ("Development.AbelianVarietyTheory.Proofs.JetHarmonics."
     "BesselNormSqEqConstMulArchPairing", [(18, 53), (59, 76)]),
    ("Development.AbelianVarietyTheory.Statements.DiscreteSeriesShifts."
     "ThmBpDS", [(12, 27)]),
    ("Formalism.HermitianCurvature.StatementTBB", [(118, 133), (181, 190)]),
    ("Development.AbelianVarietyTheory.Proofs.FlagMeasures."
     "BesselPointwiseBoundAtLargeGaps", [(17, 52)]),
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


def vandermonde(mu):
    return prod(mu[i]-mu[j] for i in range(len(mu)) for j in range(i+1, len(mu)))


def plus_i_power(z, power):
    a, b = z
    return [(a, b), (-b, a), (-a, -b), (b, -a)][power % 4]


def collision_checks():
    cases = degree_columns = colliding_endpoints = cancellations = 0
    example = None
    for n in range(2, 8):
        q = n//2
        mu = tuple(8*(n-j)+(n-j)**2 for j in range(n))
        base_degree = vandermonde(mu)
        words = [[1], [1, 1], [1, 1, 1, 1]]
        if q >= 2:
            words += [[1, 2], [2, 1, 2], [2, 2, 1]]
        if q >= 3:
            words += [[3, 1, 2]]
        for word, with_phase in itertools.product(words, [False, True]):
            initial = (0,)*n
            amplitude = {initial: (1, 0)}
            path_count = Counter({initial: 1})
            for step, ell in enumerate(word):
                new_amplitude, new_count = {}, Counter()
                for eta, z in amplitude.items():
                    current = tuple(mu[j]+eta[j] for j in range(n))
                    d = vandermonde(current)
                    assert d > 0
                    total_ratio = 0
                    for subset in itertools.combinations(range(n), ell):
                        endpoint = tuple(eta[j]+int(j in subset) for j in range(n))
                        shifted = tuple(mu[j]+endpoint[j] for j in range(n))
                        ratio = Fraction(vandermonde(shifted), d)
                        assert ratio > 0
                        total_ratio += ratio
                        phase = (sum(subset)+sum((j+1)*eta[j] for j in range(n))+step) if with_phase else 0
                        add = plus_i_power(z, phase)
                        old = new_amplitude.get(endpoint, (0, 0))
                        new_amplitude[endpoint] = (old[0]+add[0], old[1]+add[1])
                        new_count[endpoint] += path_count[eta]
                    assert total_ratio == comb(n, ell)
                    degree_columns += 1
                amplitude, path_count = new_amplitude, new_count
            # Every path coefficient telescopes to a Gaussian integer times
            # sqrt(d_final/d_initial). The final squared norm is rational.
            norm = Fraction(0)
            for eta, z in amplitude.items():
                assert sum(eta) == sum(word) <= q*len(word)
                ratio = Fraction(vandermonde(tuple(mu[j]+eta[j] for j in range(n))), base_degree)
                norm += (z[0]**2+z[1]**2)*ratio
                if path_count[eta] > 1:
                    colliding_endpoints += 1
                if z[0] == z[1] == 0 and path_count[eta]:
                    cancellations += 1
            majorant = prod(comb(n, ell) for ell in word)**2
            assert 0 <= norm <= majorant
            if example is None and any(v > 1 for v in path_count.values()):
                example = {"n": n, "minor_orders": word, "norm_squared": str(norm),
                           "l1_path_majorant_squared": majorant,
                           "max_endpoint_path_multiplicity": max(path_count.values())}
            cases += 1
    assert colliding_endpoints and cancellations and example is not None
    # Matrix [1 1] has individual column norm 1, but sends (1,1) of
    # squared norm 2 to 2 of squared norm 4. Column L2 iteration fails.
    column_norm_squared, input_norm_squared, output_norm_squared = 1, 2, 4
    assert output_norm_squared > column_norm_squared*input_norm_squared
    return {"exact_degree_weighted_path_models": cases,
            "exact_formal_degree_columns": degree_columns,
            "colliding_final_parameters": colliding_endpoints,
            "phase_cancellation_endpoints": cancellations,
            "collision_example": example,
            "column_l2_negative_control": {
                "matrix": [[1, 1]], "input": [1, 1],
                "column_norm_squared": 1, "input_norm_squared": 2,
                "output_norm_squared": 4},
            "scope": "Exact models check the collision and same-Haar degree algebra; they do not replace the local representation or analytic proofs."}


def reserve_checks():
    cases = 0
    for r, p, delta in itertools.product(range(19), range(16), [0, 1, 7]):
        q, m = r+1, 2*(r+1)
        for fractional_part in [Fraction(0), Fraction(1, 3), Fraction(9, 10)]:
            budget = Fraction(delta+q*(p+q+1))+fractional_part
            family_size = floor(budget)
            for depth in range(p+1):
                assert delta+q*depth+q*(q+1) <= family_size
                assert (delta+q*(p+q+1))-(delta+q*depth+q*(q+1)) == q*(p-depth)
                cases += 1
            for ell in range(1, q+1):
                assert m*m-ell >= 4*q*q-q >= 0
    return {"exact_floor_and_intermediate_reserve_cases": cases,
            "unbounded_reserve_identity": "q(p+q+1)-qt-q(q+1)=q(p-t)>=0 for t<=p",
            "unbounded_exponent_reserve": "m^2-ell>=4q^2-q>=0 for 1<=ell<=q, q>=1",
            "original_constants": "Cq>=200, Cg>=10^6, Cb>=Ch+5"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources = source_records(args.offline)
    checks = {"colliding_pieri_paths": collision_checks(),
              "uniform_budget": reserve_checks()}
    files = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
             f"paper/shared/{STEM}-references.tex",
             f"scripts/check_{STEM.replace('-', '_')}.py",
             "paper/shared/global-norm-frontier-pieri-family.tex",
             "paper/shared/global-norm-frontier-jacquet-gram.tex",
             "paper/sections/recovered/94-jp-section.tex"]
    result = {
        "schema_version": 1, "status": "PASS",
        "classification": "closed original higher weighted Jacquet norm subobligations",
        "supplied_interfaces": ["BesselIterationNearParameter", "BesselDerivativeIteration"],
        "theorem": "N_kappa(D^alpha F)<=b^(2 Cb m^2 |alpha|) N_kappa(F), with all original parameter reserves and both scales.",
        "checks": checks, "sources": sources,
        "artifact_hashes": {p: digest((ROOT/p).read_bytes()) for p in files},
        "scope": {
            "analytic_equalities": "Original radial L2; for fixed data/finite representatives a common full-measure set suffices.",
            "not_verified": ["Every-point coefficient expansions", "Pointwise weighted orbital bound on all relevant strata",
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
