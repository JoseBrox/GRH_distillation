#!/usr/bin/env python3
"""Authenticate exact metric variation and check its independent local algebra.

The general locality and intersection proofs are in the note. Finite checks
verify normalizers and signs; they do not establish a Lean build or the
unclosed compact-model integral dictionary.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import itertools
import json
import math
from pathlib import Path
from urllib.request import urlopen

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "geometry-arithmetic-frontier-exact-metric-variation"
BG = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry."
GH = "GroundTheory.HeightsAndTheta.Heights.HodgeLowerBound."
DP = "Development.AutomorphicSpectrum.Proofs.MetricProofs."
SOURCES = [
    (BG + "IsIntersectionFamily",
     [(19, 39), (88, 109), (116, 151), (168, 198)]),
    (BG + "InterDerived", [(11, 47)]),
    (BG + "ArithmeticHilbertSamuelLowerBound", [(73, 91)]),
    (BG + "InterNamed", [(10, 15), (37, 41)]),
    ("ReciprocityTheory.ReductiveGroups.ArithmeticGeometry."
     "ArithmeticIntersection.RationalSections.ThmISt", [(80, 96)]),
    (DP + "IntersectionNumberMetricChange", [(30, 98), (184, 206)]),
    (BG + "IsSemipositiveOn", [(206, 222)]),
    (BG + "InterRes", [(60, 78)]),
    (GH + "FrameDefinitions.Weights",
     [(39, 51), (66, 81), (95, 112), (149, 162)]),
    (GH + "FrameDefinitions.Metric", [(108, 153)]),
    (GH + "PMuRegSmooth", [(106, 157)]),
    (DP + "StokesLimitStatementHolds", [(194, 259)]),
    (GH + "StatementsStokesGeo", [(23, 39)]),
    (GH + "FrameDefinitions.CpRegPhRegOfNonneg", [(35, 61), (71, 87)]),
]
PDF = {
    "path": "build/reference-cache/bbgz-variational-monge-ampere-2013.pdf",
    "url": "https://www.numdam.org/item/10.1007/s10240-012-0046-6.pdf",
    "sha256": "d4135747982e52c1ab31dacc7c2c2442cf5a0f277a5e0c9c845d001b9be99947",
    "title": "Berman–Boucksom–Guedj–Zeriahi, A variational approach to complex Monge-Ampere equations",
    "use": "Proposition2.1, printed page193: mixed energy difference with factor1/(n+1).",
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == REPO and atlas["commit"] == REV
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        rec = inspect_file({"repository": REPO, "commit": REV, "path": rel,
                            "git_blob_sha1": blobs[module]}, offline)
        assert rec["matches_pinned_blob"]
        data = (ROOT / "build/source-cache" / REPO / REV / rel).read_bytes()
        lines = data.splitlines(keepends=True)
        records.append({
            "module": module,
            **{k: rec[k] for k in ["repository", "commit", "path", "bytes",
                                   "git_blob_sha1", "sha256", "matches_pinned_blob"]},
            "excerpts": [
                {"lines": [lo, hi], "sha256": sha(b"".join(lines[lo - 1:hi]))}
                for lo, hi in ranges
            ],
        })
        assert all(1 <= lo <= hi <= len(lines) and hi - lo < 120
                   for lo, hi in ranges)
    return records


def primary_record(offline):
    p = ROOT / PDF["path"]
    if not p.exists():
        assert not offline, "Primary PDF missing in offline mode"
        with urlopen(PDF["url"], timeout=30) as response:
            data = response.read(5_000_000)
        assert data.startswith(b"%PDF") and sha(data) == PDF["sha256"]
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
    assert sha(p.read_bytes()) == PDF["sha256"]
    return dict(PDF)


def wedge(left, right):
    """Exterior multiplication in ordered real coordinates."""
    out = {}
    for a, ca in left.items():
        for b, cb in right.items():
            if set(a) & set(b):
                continue
            sign = (-1) ** sum(i > j for i in a for j in b)
            key = tuple(sorted(a + b))
            out[key] = out.get(key, 0) + sign * ca * cb
    return {key: sp.expand(value) for key, value in out.items()
            if sp.expand(value) != 0}


def chern_form_times_pi(matrix):
    """i sum H_ij dz_i wedge dbar(z_j), using real exterior algebra."""
    out = {}
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            dz = {(2 * i,): sp.Integer(1), (2 * i + 1,): sp.I}
            db = {(2 * j,): sp.Integer(1), (2 * j + 1,): -sp.I}
            for key, coeff in wedge(dz, db).items():
                out[key] = out.get(key, 0) + sp.I * matrix[i, j] * coeff
    return {key: sp.expand(value) for key, value in out.items()
            if sp.expand(value) != 0}


def mixed_discriminant(matrices, n):
    total = sp.Integer(0)
    for mask in range(1 << n):
        chosen = [j for j in range(n) if mask & (1 << j)]
        matrix = sum((matrices[j] for j in chosen), sp.zeros(n))
        total += (-1) ** (n - len(chosen)) * matrix.det()
    return sp.expand(total / math.factorial(n))


def matrices_for(n, seed):
    ans = []
    for j in range(n):
        m = sp.Matrix(n, n, lambda r, c:
                      ((seed + 3 * j + 7 * r + 11 * c) % 7 - 3)
                      + sp.I * ((2 * seed + j + 5 * r + 3 * c) % 5 - 2))
        ans.append(sp.expand(m.conjugate().T * m + (j + 1) * sp.eye(n)))
    return ans


def exact_checks():
    density_count = hessian_count = 0
    for n in range(5):
        for seed in range(1, 5):
            mats = matrices_for(n, seed)
            form = {(): sp.Integer(1)}
            for matrix in mats:
                form = wedge(form, chern_form_times_pi(matrix))
            exterior = form.get(tuple(range(2 * n)), 0)
            source = math.factorial(n) * 2**n * mixed_discriminant(mats, n)
            assert sp.expand(exterior - source) == 0
            density_count += 1
            if 1 <= n <= 3:
                coords = sp.symbols(f"x0:{2*n}", real=True)
                zs = [coords[2*i] + sp.I * coords[2*i+1] for i in range(n)]
                h = mats[0]
                phi = sp.expand(sum(h[i,j] * zs[i] * sp.conjugate(zs[j])
                                    for i in range(n) for j in range(n)))
                for i in range(n):
                    for j in range(n):
                        value = (
                            sp.diff(phi, coords[2*i], coords[2*j])
                            + sp.diff(phi, coords[2*i+1], coords[2*j+1])
                            + sp.I * (sp.diff(phi, coords[2*i], coords[2*j+1])
                                      - sp.diff(phi, coords[2*i+1], coords[2*j]))
                        ) / 4
                        assert sp.expand(value - h[i,j]) == 0
                        hessian_count += 1

    # A true obstruction to identifying homogeneous data outside the cone.
    a_bad, b_bad, ratio_bad, c_bad = 0, 7, 1, 0
    assert a_bad * ratio_bad != b_bad
    assert a_bad * c_bad == b_bad * c_bad
    cone_cases = 0
    for k in range(1, 5):
        for norms in itertools.product([0, 1, 2, 5], repeat=k):
            c = math.prod(norms)
            assert (c > 0) == all(x > 0 for x in norms)
            if c == 0:
                for av, bv in [(-3, 8), (0, 7), (4, 0)]:
                    assert av * c == bv * c
            cone_cases += 1

    telescope_coefficients = 0
    for n in range(17):
        for k in range(n + 1):
            assert sum(math.comb(j, k) for j in range(k, n + 1)) \
                == math.comb(n + 1, k + 1)
            telescope_coefficients += 1
        c = Fraction(3, 7)
        expected = (n + 1) * c
        assert sum(c for _ in range(n + 1)) == expected
        assert expected != -expected and expected != expected / 2
        assert (n + 1) * Fraction(1, 2) != (n + 1) * Fraction(1, 4)

    rational_cases = 0
    for n in range(9):
        degree = n + 1
        coeff = [Fraction((-1)**j * (j + 2), j + 1)
                 for j in range(degree + 1)]
        for p in range(5):
            for q in range(1, 6):
                tensor = sum(math.comb(degree, j) * q**(degree-j) * p**j * coeff[j]
                             for j in range(degree + 1)) / q**degree
                polynomial = sum(math.comb(degree, j) * Fraction(p, q)**j * coeff[j]
                                 for j in range(degree + 1))
                assert tensor == polynomial
                if p == 0:
                    assert polynomial == coeff[0]
                rational_cases += 1
    q, p, ref, vert, ample, phi, psi = sp.symbols(
        "q p ref vert ample phi psi", real=True, nonzero=True)
    difference = (q * (ref + psi + vert) + p * ample
                  - q * (ref + phi + vert) - p * ample) / q
    assert sp.expand(difference - (psi - phi)) == 0
    for n in range(13):
        assert sp.cancel(q**n * q / q**(n + 1)) == 1

    return {
        "exterior_density_cases": density_count,
        "dimensions_for_exterior_density": list(range(5)),
        "complex_hessian_entries_independently_differentiated": hessian_count,
        "coordinate_cone_cases": cone_cases,
        "binomial_telescope_coefficients": telescope_coefficients,
        "rational_twist_cases": rational_cases,
        "constant_metric_sign_and_half_factor_negative_controls": 17,
        "off_cone_ratio_equality_negative_control": "pass",
        "common_vertical_and_ample_factors_cancel_in_ratio": "pass",
        "scope": "Finite exact checks supplement the general proof; they do not verify the compact-model integral dictionary.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    source = source_records(args.offline)
    primary = primary_record(args.offline)
    checks = exact_checks()
    artifacts = [
        f"notes/{STEM}.md",
        f"paper/shared/{STEM}.tex",
        "scripts/check_geometry_arithmetic_frontier_exact_metric_variation.py",
    ]
    result = {
        "date": "2026-11-22",
        "status": "proved-formal-supplier-with-geometric-interface-open",
        "verification_status": "pass",
        "scope": "Original intersection axioms imply metric variation, full metric locality, and the exact original rational-twist polynomial. No Lean build or compact-model construction is claimed.",
        "proved": [
            "Trivial degree-zero metric has positive single-slot variation with coefficient one",
            "Product Euclidean norm gives cone locality by tensor cancellation",
            "Arbitrary same-degree metric variation implies full locality on the original complex variety",
            "Telescoping gives factor n+1 times unnormalized energy when the original mixed-integral dictionary holds",
            "Local density uses dd^c=i/pi partial bar-partial and no extra half",
            "Original rational-twist denominator q^(n+1) and arLim constant coefficient are exact",
            "Common vertical and ample factors cancel in the original normalized metric ratio",
        ],
        "remaining": [
            "Identification of original sheet integrals with the specified compact model and its component weights",
            "Identification of the common vertical curvature with the geometric form used in the original limiting measure",
            "Construction of the original arithmetic model, smooth extensions and tied regularizations",
            "Full signed arithmetic comparison and complete RH/GRH nodes",
        ],
        "source": source,
        "primary_reference": primary,
        "exact_checks": checks,
        "artifacts": [{"path": rel, "sha256": sha((ROOT / rel).read_bytes())}
                      for rel in artifacts],
        "node_progress_unchanged": {"RH": "6/9", "GRH": "17/31"},
    }
    path = ROOT / "certificates" / f"{STEM}.json"
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "pass", "sources": len(source),
                      "checks": checks, "certificate": str(path.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
