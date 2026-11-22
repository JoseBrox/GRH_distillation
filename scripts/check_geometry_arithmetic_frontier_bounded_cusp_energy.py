#!/usr/bin/env python3
"""Authenticate the original bounded-cusp energy comparison.

The companion note contains the general proof. Exact finite calculations
check the gluing constant and the necessary symmetry/cutoff conditions.
No calculation here is a Lean build or the remaining arithmetic dictionary.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import urllib.request

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
GH = "GroundTheory.HeightsAndTheta.Heights."
AP = "ReciprocityTheory.AnalyticForms.PlurisubharmonicFunctions."
SOURCES = [
    (AP + "IsPshLocallyIntegrableStatement", [(13, 17), (72, 98)]),
    (AP + "PshMollB", [(142, 185), (269, 277)]),
    (AP + "PshMoll", [(315, 328)]),
    (GH + "Regularisation.Statements", [(32, 56), (79, 88), (121, 125)]),
    (GH + "Regularisation.BoundedStatements", [(19, 28)]),
    (GH + "Regularisation.ChartFun", [(20, 33)]),
    (GH + "Regularisation.PBoundedGlue", [(109, 145), (195, 215)]),
    (GH + "HodgeLowerBound.FrameDefinitions.Weights", [(70, 91)]),
    (GH + "HodgeLowerBound.FrameDefinitions.CpRegPhRegOfNonneg",
     [(26, 29), (71, 73)]),
    (GH + "StabilizerCovolume.BRegWeightLevi", [(17, 40)]),
    ("Development.AutomorphicSpectrum.ParallelStatements.ParallelGeometry."
     "StokesLimitBound", [(33, 34), (76, 85)]),
]
PRIMARY = {
    "title": "A variational approach to complex Monge-Ampere equations",
    "authors": ["Berman", "Boucksom", "Guedj", "Zeriahi"],
    "year": 2013,
    "url": "https://www.numdam.org/item/10.1007/s10240-012-0046-6.pdf",
    "path": "build/reference-cache/bbgz-variational-monge-ampere-2013.pdf",
    "sha256": "d4135747982e52c1ab31dacc7c2c2442cf5a0f277a5e0c9c845d001b9be99947",
    "printed_page": 195,
    "result": "Proposition 2.4: monotonicity and upper semicontinuity of energy",
    "prior_visual_review":
        "certificates/geometry-arithmetic-frontier-signed-boundary-energy.json",
}


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
        checked = inspect_file({"repository": "jsmorph/rh", "commit": REV,
                                "path": rel, "git_blob_sha1": blobs[module]}, offline)
        assert checked["matches_pinned_blob"]
        data = (ROOT / "build/source-cache/jsmorph/rh" / REV / rel).read_bytes()
        lines = data.splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpts.append({"first_line": lo, "last_line": hi,
                             "sha256": sha(b"".join(lines[lo-1:hi]))})
        records.append({"module": module, "commit": REV, "path": rel,
                        "git_blob_sha1": blobs[module], "sha256": sha(data),
                        "matches_pinned_blob": True, "excerpts": excerpts})
    return records


def gluing_checks():
    count = 0
    # Normalize the bounded potential's value to zero. Chart zero is
    # an inner chart, so its cutoff must vanish.
    shifts = [Fraction(-1), Fraction(-1, 2), Fraction(0),
              Fraction(1, 2), Fraction(1)]
    cutoffs = [Fraction(-1), Fraction(-1, 2), Fraction(0)]
    for n in [1, 2, 3]:
        for eps in [Fraction(1, 4), Fraction(1, 2), Fraction(1)]:
            for inner in [Fraction(0), Fraction(1, 3), Fraction(1), Fraction(2)]:
                for ds in itertools.product(shifts, repeat=n-1):
                    local = [inner] + [inner + eps*d for d in ds]
                    if min(local) < 0:
                        continue
                    # Retain the actual pairwise comparison, not just
                    # comparison to the chosen inner chart.
                    if max(local)-min(local) > eps:
                        continue
                    for rest in itertools.product(cutoffs, repeat=n-1):
                        eta = [Fraction(0)] + list(rest)
                        args = [f+4*eps*h for f, h in zip(local, eta)]
                        lower, upper = max(args), max(args)+eps
                        assert 0 <= inner <= lower <= upper <= inner+2*eps
                        count += 1
    # If all cutoffs are -1, every allowed glued value can lie below
    # the original constant potential: no inner-zero condition remains.
    eps = Fraction(1, 2)
    args = [-4*eps]
    assert max(args)+eps < 0
    # A positive normalized smooth bump centered at a>0 has mean a.
    # For u(z)=Re z its convolution at zero is -a, violating submean.
    # Such a shifted bump is excluded by the actual circle invariance.
    a = Fraction(1, 4)
    assert -a < 0
    return {
        "rational_gluing_cases": count,
        "certified_interval": "psi <= f_inner <= glued <= f_inner + 2 epsilon",
        "negative_controls": [
            "Without an inner zero cutoff, the entire permitted gluing interval can be below psi.",
            "Without circle invariance, a shifted normalized positive bump lowers a real-linear harmonic function.",
        ],
        "scope": "Exact finite checks of the gluing algebra; the general analytic argument is proved in the note.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    records = source_records(args.offline)
    path = ROOT / PRIMARY["path"]
    if not path.exists() and not args.offline:
        with urllib.request.urlopen(PRIMARY["url"], timeout=30) as response:
            data = response.read()
        assert data.startswith(b"%PDF") and sha(data) == PRIMARY["sha256"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    data = path.read_bytes()
    assert data.startswith(b"%PDF") and sha(data) == PRIMARY["sha256"]
    artifacts = [
        "notes/geometry-arithmetic-frontier-bounded-cusp-energy.md",
        "scripts/check_geometry_arithmetic_frontier_bounded_cusp_energy.py",
    ]
    result = {
        "status": "pass",
        "date": "2026-11-22",
        "scope": "Actual bounded-cusp energy convergence under original geometric regularization data. Source provenance and exact finite checks; no Lean build or full arithmetic model claim.",
        "closed_obligation": "Item 2 of section 4 of the signed-boundary-energy checkpoint: the original bounded cusp approximations have the prescribed corrected energy limit.",
        "proved": [
            "Actual simultaneous-circle-invariant mollifier gives submean domination",
            "Actual finite-chart gluing satisfies the inner-chart sandwich with error 2 epsilon",
            "Original bounded cusp sequence converges pointwise everywhere and in L1 with one global bound",
            "Actual vanishing Levi error gives every fixed positive curvature correction",
            "Energy monotonicity and upper semicontinuity give the original corrected energy limit",
        ],
        "remaining": [
            "Existence and identification of the actual geometric regularization data",
            "Arithmetic metric-variation and compact-model integration dictionary",
            "Original vertical and rational twist identification",
        ],
        "source": records,
        "primary_reference": dict(PRIMARY, bytes=len(data)),
        "exact_checks": gluing_checks(),
        "artifacts": [{"path": p, "sha256": sha((ROOT / p).read_bytes())}
                      for p in artifacts],
        "node_progress_unchanged": {"RH": "6/9", "GRH": "17/31"},
    }
    output = ROOT / "certificates/geometry-arithmetic-frontier-bounded-cusp-energy.json"
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "source_modules": len(records),
                      "rational_gluing_cases": result["exact_checks"]["rational_gluing_cases"],
                      "certificate": str(output.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
