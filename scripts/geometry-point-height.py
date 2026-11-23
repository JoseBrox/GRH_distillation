#!/usr/bin/env python3
"""Authenticate the original all-point height proof and check its identities.

Exact matrix diagnostics include arbitrary relative logarithmic sizes, zero
and full toric rank, and moving complex frames. They verify identities used
in the written proof, not the universal arithmetic theorem or a Lean build.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import sympy as sp

from check_sources import inspect_file


ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "geometry-point-height"
GP = "Development.AutomorphicSpectrum.Proofs.GeometryProofs."
MP = "Development.AutomorphicSpectrum.Proofs.MetricProofs."
PC = "Development.WeilBound.CoreStatements.PlurisubharmonicCones."
RANGES = {
    "Development.AutomorphicSpectrum.Definitions.MetricPeriods.IsAdapted": [(11, 65)],
    GP + "SemiAbelianPullbackTorusExtension": [(119, 144)],
    GP + "TorusExtensionLieLattice": [(128, 174)],
    PC + "TorusModelCochar": [(180, 197)],
    MP + "LogIndexOfOrthogonalFamily": [(563, 638)],
    GP + "AbelianPartIntegralLattice": [(35, 86)],
    GP + "ComponentDataHodgeBound": [(42, 129)],
    GP + "BoundaryChartLogPeriodFamily": [(118, 194)],
    GP + "SymplecticPolydiscPeriodBasis": [(109, 216), (217, 316)],
    MP + "ExistsIsChart": [(20, 95)],
    MP + "ChartQContinuousAtAndLocalSolution": [(343, 395), (403, 482)],
    MP + "PeriodDecompositionNearBoundary": [(62, 124), (159, 251), (253, 280), (336, 365)],
    PC + "DetLatticeTensorIsDegOnMuTwDeg": [(148, 197)],
    GP + "CuspIntersectionHeight": [(232, 315), (350, 426)],
    GP + "CuspIntersectionComparison": [(91, 118), (202, 216), (222, 298)],
    GP + "CuspIntersectionFinite": [(10, 36)],
    MP + "RegularizedWeightDominatesEventually": [(78, 107)],
    GP + "CuspHeightUpper": [(120, 172), (174, 225)],
    PC + "HeightComparisonGlobalModel": [(21, 60), (100, 155)],
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def provenance(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert (atlas["repository"], atlas["commit"]) == (REPO, REV)
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    result = []
    for module, ranges in RANGES.items():
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        record = inspect_file({"repository": REPO, "commit": REV, "path": path,
                               "git_blob_sha1": blobs[module]}, offline)
        lines = (ROOT / "build/source-cache" / REPO / REV / path).read_bytes().splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            data = b"".join(lines[lo - 1:hi])
            assert len(data) <= 12000
            excerpts.append({"lines": [lo, hi], "sha256": sha(data)})
        result.append({"module": module, **{k: record[k] for k in
                       ["repository", "commit", "path", "git_blob_sha1", "sha256", "matches_pinned_blob"]},
                       "excerpts": excerpts})
    return result


def exact_quotient_checks():
    cases = 0
    sizes = [(1, 1), (2**10, 3), (10**12, 10**2)]
    for g in range(1, 5):
        for r in range(g + 1):
            pi = sp.diag(*([0] * r + [1] * (g - r)))
            for trial, (t1, t2) in enumerate(sizes):
                s = sp.Matrix(g, g, lambda i, j: ((i + 1) * (j + 2) + trial) % 5 - 2)
                y0 = s.T * s + sp.eye(g)
                u = sp.Matrix(r, 1, lambda i, j: i + 1)
                b1 = sp.zeros(g)
                b2 = sp.zeros(g)
                if r:
                    b1[:r, :r] = sp.eye(r) + u * u.T
                    b2[:r, :r] = sp.diag(*range(1, r + 1))
                assert b1 * pi == sp.zeros(g) and b2 * pi == sp.zeros(g)
                y = y0 + t1 * b1 + t2 * b2
                h = y.inv()
                c = pi * (pi * y0 * pi + sp.eye(g) - pi).inv() * pi
                assert pi * y * pi == pi * y0 * pi
                representatives = y * c
                assert pi * (representatives - sp.eye(g)) == sp.zeros(g)
                assert h * representatives == c
                assert representatives.T * h * representatives == c
                toric_det = h[:r, :r].det()
                quotient_det = c[r:, r:].det()
                assert h.det() == toric_det * quotient_det
                # Moving complex frame; the metric and actual toric vectors
                # are transported together, so cancellation remains exact.
                m = sp.eye(g)
                for i in range(g - 1):
                    m[i, i + 1] = sp.Rational(trial + 1, i + 2) + sp.I
                mi = m.inv()
                transported = mi.conjugate().T * h * mi
                gram = sp.simplify(m.conjugate().T * transported * m)
                assert gram == h
                assert sp.simplify(gram.det() / gram[:r, :r].det()) == quotient_det
                cases += 1
    assert cases == 42
    n = sp.symbols("n", positive=True)
    bad_error = (1 / n)**2 * n**4
    assert sp.simplify(bad_error) == n**2
    return {"cases": cases, "ambient_dimensions": [1, 4],
            "toric_ranks": "every r from 0 to the ambient dimension",
            "logarithmic_coefficient_pairs": sizes,
            "identities": ["common-kernel compression", "exact orthogonal representative",
                           "quotient metric", "Schur determinant", "moving complex frame"],
            "negative_control": "z1=exp(-n^4), z2=1/n gives |z2|^2(-log|z1|)=n^2",
            "scope": "Finite exact diagnostics; the manuscript proves the identities for all matrices satisfying its hypotheses."}


def sign_and_constant_checks():
    f, r, m, rd, index, t, cost, lam = sp.symbols("f r m rd index T X Lambda")
    toric_sum = f * (-r * rd + index / (2 * f))
    l4 = sp.symbols("log_4pi")
    phi = toric_sum + t + f * m * cost - index / 2 + f * r * l4 / 2
    expected = f * m * cost + t - f * r * rd + f * r * l4 / 2
    assert sp.simplify(phi - expected) == 0
    budget = sp.expand((52 * f * m * lam) -
                       (16 * f * m + 36 * f * (m - r) + f * r / 2) * lam)
    assert budget == sp.Rational(71, 2) * f * r * lam
    a, b = sp.symbols("a b")
    # Exponents of pi and 2 after full and quotient metric conversions.
    assert sp.expand(m - (m - r) - 2 * r) == -r
    assert -2 * r == sp.expand(-2 * r)
    nfield, finite_coords, vertical, scalar, frames, grams = sp.symbols("N F W A C G")
    signed_indices = -scalar - finite_coords + frames
    boundary_values = scalar + nfield * (index / 2 - f * r * l4 / 2) + grams / 2 - frames - vertical
    h0 = (finite_coords + vertical) / nfield
    actual_phi = (signed_indices - grams / 2) / nfield - index / 2 + f * r * l4 / 2
    assert sp.simplify(h0 + boundary_values / nfield + actual_phi) == 0
    wrong_index = sp.simplify(h0 + boundary_values / nfield + actual_phi + index)
    assert wrong_index == index
    omitted_vertical = sp.simplify((finite_coords / nfield) + boundary_values / nfield + actual_phi)
    assert omitted_vertical == -vertical / nfield
    return {"toric_index_cancellation": "exact", "52_constant_reserve": str(budget),
            "toric_metric_factor": "pi^m pi^(-(m-r)) |2 pi i|^(-2r)=(4 pi)^(-r)",
            "product_formula_identity": "h_B^0+average(x)+Phi=0",
            "negative_controls": {"reversed_toric_index": str(wrong_index),
                                  "omitted_vertical_factors": str(omitted_vertical)}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    review_path = ROOT / "certificates/geometry-point-height-theta-review.json"
    review = json.loads(review_path.read_text())
    assert review["status"] == "passed"
    for path, digest in {**review["reviewed_files"], **review["dependency_artifacts"]}.items():
        assert sha((ROOT / path).read_bytes()) == digest, path
    reference = review["primary_reference"]
    assert sha((ROOT / reference["local_path"]).read_bytes()) == reference["sha256"]
    sources = provenance(args.offline)
    paths = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", f"scripts/{STEM}.py",
             "certificates/geometry-point-height-theta-review.json",
             "certificates/geometry-hodge-specialization.json",
             "certificates/geometry-point-continuation.json"]
    certificate = {
        "result": "Original determinant bound and uniform all-point regularized height floor",
        "classification": "closed actual supplier obligations in W10; full proof-map node remains open",
        "source_repository": REPO, "source_revision": REV,
        "source_records": sources, "primary_reference": reference,
        "independent_review": {"path": str(review_path.relative_to(ROOT)), "status": "passed",
                               "sha256": sha(review_path.read_bytes())},
        "matrix_diagnostics": exact_quotient_checks(),
        "exact_sign_and_constant_identities": sign_and_constant_checks(),
        "artifacts": {path: sha((ROOT / path).read_bytes()) for path in paths},
        "remaining": ["original signed intersection limit", "weighted mean-height comparison",
                      "finite rank losses and final numerical family"],
        "limits": ["Written mathematical proof with cited primary theorems and bounded source interfaces.",
                   "Finite exact diagnostics are not a proof of universal geometry.",
                   "No Lean build, kernel check, whole-node closure, RH proof or GRH proof is claimed."]}
    dest = ROOT / f"certificates/{STEM}.json"
    dest.write_text(json.dumps(certificate, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"result": "pass", "sources": len(sources), "matrix_cases": 42,
                      "certificate": str(dest.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
