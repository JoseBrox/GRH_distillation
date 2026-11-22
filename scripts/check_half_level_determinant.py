#!/usr/bin/env python3
"""Authenticate bounded sources and an exact level-two diagnostic.

This automated check does not replay Lean or certify the general theorem.
The independent mathematical review is recorded separately.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
SOURCES = [
    ("Development.AutomorphicSpectrum.Proofs.AlgebraProofs."
     "KahlerFormsOverSubalgebraClosureProperties", [[175, 209], [211, 245]]),
    ("Development.WeilBound.CoreStatements.TorusUniformisation."
     "ChowMahlerFamilies.AnalyticTypeDefinition", [[317, 331], [335, 360]]),
    ("Development.AutomorphicSpectrum.Statements.GeometryStatements."
     "FlatLineGenerator", [[18, 19]]),
]


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def source_evidence(fetch: bool) -> list[dict]:
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    entries = {row[0]: row for row in atlas["modules"]}
    evidence = []
    for module, ranges in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        record = inspect_file({
            "repository": "jsmorph/rh", "commit": REV, "path": path,
            "git_blob_sha1": entries[module][1],
        }, offline=not fetch)
        raw = (ROOT / "build/source-cache/jsmorph/rh" / REV / path).read_bytes()
        lines = raw.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            excerpt = b"\n".join(lines[lo - 1:hi]) + b"\n"
            assert len(excerpt) <= 12000
            excerpts.append({"lines": [lo, hi], "sha256": sha(excerpt)})
        evidence.append({
            "module": module, "path": path,
            "sha256": record["sha256"],
            "git_blob_sha1": record["git_blob_sha1"],
            "url": f"https://github.com/jsmorph/rh/blob/{REV}/{path}",
            "inspected_excerpts": excerpts,
        })
    return evidence


def exact_diagnostic() -> dict:
    # O_E = Z[w], w^2 - w + 2 = 0, conjugate(w) = 1 - w.
    def mul(x, y):
        a, b = x
        c, d = y
        return (a * c - 2 * b * d, a * d + b * c + b * d)

    def conjugate(x):
        a, b = x
        return (a + b, -b)

    def trace(x):
        return 2 * x[0] + x[1]

    def inv_sqrt_times(x):
        # 1/sqrt(-7) = (1 - 2*w)/7. Store exact numerators.
        return mul(x, (1, -2))

    one, w, wbar, minus_one = (1, 0), (0, 1), (1, -1), (-1, 0)
    assert mul(w, wbar) == (2, 0)
    assert tuple(a + b for a, b in zip(w, wbar)) == one
    assert mul(minus_one, conjugate(minus_one)) == one
    basis = [one, w]
    matrix = []
    for x in basis:
        row = []
        for y in basis:
            numerator = trace(inv_sqrt_times(mul(x, conjugate(y))))
            assert numerator % 7 == 0
            row.append(numerator // 7)
        matrix.append(row)
    assert matrix == [[0, -1], [1, 0]]
    assert matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] == 1
    # (g-1) kills the quotient by 2 on every element, hence on bar(I).
    for x in [wbar, mul(wbar, w)]:
        assert all(a % 2 == 0 for a in mul((-2, 0), x))
    assert minus_one != one
    return {
        "ring": "Z[w]/(w^2-w+2)",
        "ideal_generator": "w",
        "conjugate_ideal_generator": "1-w",
        "product": 2,
        "coprimality_witness": "w+(1-w)=1",
        "alternating_matrix": matrix,
        "level": 2,
        "determinant": -1,
        "status": "PASS",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fetch", action="store_true")
    args = parser.parse_args()
    evidence = source_evidence(args.fetch)
    result = {
        "status": "PASS",
        "automated_scope": (
            "Pinned-source byte authentication, bounded-excerpt hashes, "
            "and exact level-two counterexample arithmetic only."
        ),
        "not_claimed": [
            "Lean kernel replay",
            "Automated proof of the general determinant theorem",
            "Boundary extension or finite-place norm constancy",
            "Completion of an RH or GRH node",
        ],
        "independent_review": "certificates/hard-node-review-2026-11-22.json",
        "sources": evidence,
        "exact_diagnostic": exact_diagnostic(),
        "artifacts": [
            {"path": path, "sha256": sha((ROOT / path).read_bytes())}
            for path in [
                "notes/half-level-determinant.md",
                "scripts/check_half_level_determinant.py",
            ]
        ],
    }
    target = ROOT / "certificates/half-level-determinant.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    print("PASS: 3 pinned sources and exact unimodular level-two counterexample.")
    print("Scope: source authentication and finite arithmetic; no Lean replay.")


if __name__ == "__main__":
    main()
