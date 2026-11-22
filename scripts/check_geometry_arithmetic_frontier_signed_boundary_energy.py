#!/usr/bin/env python3
"""Authenticate the signed-boundary energy checkpoint and its exact scope.

This verifies provenance and small exact algebraic identities. The general
analytic proofs are in the note. It does not verify a Lean build or the open
arithmetic intersection comparison.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
import urllib.request

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
GH = "GroundTheory.HeightsAndTheta.Heights."
DP = "Development.AutomorphicSpectrum.Proofs.MetricProofs."
SOURCES = [
    (GH + "Regularisation.Statements", [(92, 125), (127, 143)]),
    (GH + "HodgeLowerBound.FrameDefinitions.Weights",
     [(39, 55), (70, 91), (140, 162)]),
    (GH + "HodgeLowerBound.FrameDefinitions.CpRegPhRegOfNonneg",
     [(19, 29), (71, 87)]),
    (DP + "RegularizedWeightPshAndBounds", [(137, 179)]),
    (DP + "RegularizedWeightPshAndBoundsStatement", [(9, 11)]),
    (DP + "RegularizedWeightTendstoC2", [(426, 430)]),
    (DP + "RegularizedWeightTendstoC2Statement", [(9, 11)]),
    (GH + "StabilizerCovolume.BRegWeightLevi", [(32, 40)]),
    ("Development.AutomorphicSpectrum.ParallelStatements.ParallelGeometry."
     "StokesLimitBound", [(33, 58), (76, 85)]),
    ("ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry."
     "InterNamed", [(10, 15), (37, 41)]),
]
PRIMARY = [
    {
        "title": "Monge-Ampere equations in big cohomology classes",
        "authors": ["Boucksom", "Eyssidieux", "Guedj", "Zeriahi"],
        "year": 2010,
        "url": "https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf",
        "path": "build/reference-cache/begz-monge-ampere-big-classes-2010.pdf",
        "sha256": "7f1f53e505113fc8856f3f364f6f565592a608e43b7743003eb2b79961cdc919",
        "printed_pages": [228, 229, 231],
        "results": ["Proposition 2.10", "Proposition 2.11", "Proposition 2.14(i)"],
        "visual_review": [{"printed_page": 229, "pdf_page": 31,
                           "image": "build/review-signed-boundary-energy/begz-31.png",
                           "sha256": "c92dc38474f7430a5f0372a27d0f7d9262a5b476168c555a04c331a4952235be"}],
    },
    {
        "title": "A variational approach to complex Monge-Ampere equations",
        "authors": ["Berman", "Boucksom", "Guedj", "Zeriahi"],
        "year": 2013,
        "url": "https://www.numdam.org/item/10.1007/s10240-012-0046-6.pdf",
        "path": "build/reference-cache/bbgz-variational-monge-ampere-2013.pdf",
        "sha256": "d4135747982e52c1ab31dacc7c2c2442cf5a0f277a5e0c9c845d001b9be99947",
        "printed_pages": [193, 195, 196],
        "results": ["Proposition 2.1", "Proposition 2.4",
                    "Lemma 2.7", "Proposition 2.8"],
        "visual_review": [
            {"printed_page": page, "pdf_page": page - 178,
             "image": f"build/review-signed-boundary-energy/bbgz-{page-178}.png",
             "sha256": digest}
            for page, digest in [
                (193, "71658c4f16f84a189ddf6cfc55d71b535c0c90161748ea0e09be600f229e91fc"),
                (195, "54cfe4d0d06504e274fa9c6e5c16a6ef8d5e672cbaf6c854653f194558f295e4"),
                (196, "d3cc1674bf35661aeb155318d45127de454eb9bcf8ddcefab1693c0abc5e591f"),
            ]
        ],
    },
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["commit"] == REV
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        result = inspect_file({"repository": "jsmorph/rh", "commit": REV,
                               "path": rel, "git_blob_sha1": blobs[module]}, offline)
        assert result["matches_pinned_blob"]
        data = (ROOT / "build/source-cache/jsmorph/rh" / REV / rel).read_bytes()
        lines = data.splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            excerpts.append({"first_line": lo, "last_line": hi,
                             "sha256": sha(b"".join(lines[lo-1:hi]))})
        records.append({"module": module, "commit": REV, "path": rel,
                        "git_blob_sha1": blobs[module], "sha256": sha(data),
                        "matches_pinned_blob": True, "excerpts": excerpts})
    return records


def exact_checks():
    # The crossing integral is evaluated before any other radial variable.
    a, s = sp.symbols("a s", positive=True)
    assert sp.integrate(1 / (a+s)**2, (s, 0, sp.oo)) == 1/a
    # Wedge-square zero of a rank-one form is the exterior-algebra fact
    # used in the proof. Check its equivalent determinant linearity here.
    z = sp.symbols("z")
    rank_one = []
    for n in [1, 2, 3]:
        base = sp.diag(*range(1, n+1))
        u = sp.Matrix(sp.symbols(f"u0:{n}"))
        v = sp.Matrix(sp.symbols(f"v0:{n}"))
        p = sp.Poly(sp.expand((base + z*u*v.T).det()), z)
        assert p.degree() <= 1
        rank_one.append(n)
    # Exact recovery of the constant coefficient from positive arguments:
    # Q(0)=sum (-1)^(j+1) binom(n+1,j) Q(j B), deg Q<=n.
    for n in range(13):
        for k in range(n+1):
            lhs = sum((-1)**(j+1)*sp.binomial(n+1, j)*j**k
                      for j in range(1, n+2))
            assert lhs == int(k == 0)
    return {
        "crossing_integral": "Integral_0^infinity (a+s)^(-2) ds = 1/a for a>0",
        "rank_one_determinant_sizes": rank_one,
        "signed_interpolation_degrees_checked": list(range(13)),
        "scope": "Finite exact algebraic checks supplement the general proofs; no numerical approximation is used.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    records = source_records(args.offline)
    primary = []
    for record in PRIMARY:
        path = ROOT / record["path"]
        if not path.exists() and not args.offline:
            with urllib.request.urlopen(record["url"], timeout=30) as response:
                data = response.read()
            assert data.startswith(b"%PDF") and sha(data) == record["sha256"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        data = path.read_bytes()
        assert data.startswith(b"%PDF") and sha(data) == record["sha256"]
        item = dict(record, bytes=len(data))
        # The rendered pages are preserved review evidence, not a new visual
        # inspection performed by this script. Their absence in a fresh
        # checkout does not affect authentication of the source PDF.
        for visual in record["visual_review"]:
            image_path = ROOT / visual["image"]
            if image_path.exists():
                assert sha(image_path.read_bytes()) == visual["sha256"]
        primary.append(item)
    artifacts = [
        "notes/geometry-arithmetic-frontier-signed-boundary-energy.md",
        "scripts/check_geometry_arithmetic_frontier_signed_boundary_energy.py",
    ]
    result = {
        "status": "checkpoint",
        "date": "2026-11-22",
        "verification_status": "pass",
        "scope": "Proved analytic substeps under exact regularization data; original signed arithmetic interface remains open. Source provenance and finite exact checks, not a Lean build.",
        "proved": [
            "Logarithmic normal-crossing barrier has finite energy and full mass",
            "Full mixed mass recovered for the original nef class using positivity of polynomial deficits",
            "Original source approximants converge in every corrected Kahler energy",
            "Signed analytic energy recovered by finite polynomial interpolation",
            "Conditional concavity assembly gives the original signed cusp coefficient",
        ],
        "remaining": [
            "Original arithmetic intersection metric-variation normalization, complex-place weights and vertical factors",
            "Full comparison of the source's bounded cusp approximants with the bounded corrected potential",
            "Original rationally twisted arithmetic polynomial and arLim identification",
            "Existence and identification of the actual arithmetic model and its regularization data",
        ],
        "source": records,
        "primary_references": primary,
        "exact_checks": exact_checks(),
        "artifacts": [{"path": p, "sha256": sha((ROOT / p).read_bytes())}
                      for p in artifacts],
        "node_progress_unchanged": {"RH": "6/9", "GRH": "17/31"},
    }
    path = ROOT / "certificates/geometry-arithmetic-frontier-signed-boundary-energy.json"
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "verification_status": "pass",
                      "source_modules": len(records), "primary_references": len(primary),
                      "certificate": str(path.relative_to(ROOT)),
                      "signed_arithmetic_interface": "open"}))


if __name__ == "__main__":
    main()
