#!/usr/bin/env python3
"""Authenticate the exact finite-to-limiting Selmer source interfaces.

This is provenance and artifact verification. The infinite-level result
is proved in the mathematical note; no finite computation proves it and
no Lean build is claimed.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules."
RANGES = {
    "PairedDualFirstOrderDualMatrixSpace": [(10, 42), (220, 247)],
    "ThetaCoefficientMapEq": [(265, 301)],
    "PatchedSupportCompletions": [(18, 24)],
    "SeparableMatrixStability.CocFin": [(5, 56)],
    "SeparableMatrixStability.EventuallyLocallyConstantCompTowerEq": [(6, 39)],
    "SeparableMatrixStability.EventuallyFactorThroughTowerIffLimit": [(64, 91)],
    "SeparableMatrixStability.EventuallyFactorizationCompatibleWithLocalMaps": [(37, 51)],
    "SeparableMatrixStability.LcOfAdic": [(64, 120), (122, 208)],
    "SeparableMatrixStability.SecondSelmerSpanBoundAtAllLevels": [(150, 165)],
    "SeparableMatrixStability.TaylorWilesFirstConditionAtLimitOfGroupCondition": [(19, 41)],
    "SeparableMatrixStability.TaylorWilesSecondConditionAtLimitOfGroupConditio": [(7, 26)],
    "SeparableMatrixStability.CoefficientsBoundedOfSelmerBoundary": [(64, 99), (101, 141)],
    "SeparableMatrixStability.FirstCohomologyBoundOfBoundaryBound": [(36, 79)],
    "SeparableMatrixStability.SecondCohomologyBoundOfBoundaryBound": [(44, 119)],
    "SeparableMatrixStability.SelmerSecondClosedUnderLimits": [(228, 345)],
    "SeparableMatrixStability.KoszulThreeOfDet": [(8, 49)],
    "SelmerScaling.SelScale": [(39, 75)],
    "SelmerScaling.SelmerRankBoundLaurent": [(47, 93)],
    "SelmerScaling.EvenCocyclesLiftLaurent": [(7, 38)],
    "SelmerScaling.SelmerSpannedByKappaLaurentAlt": [(6, 49)],
    "AutomorphicDetection.CohLim": [(12, 19)],
    "AutomorphicDetection.GalOut": [(16, 43)],
    "AutomorphicDetection.LiftPt": [(139, 175)],
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert hashlib.sha256(packed).hexdigest() == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    rows = {row[0]: row for row in atlas["modules"]}
    sources = []
    for suffix, intervals in RANGES.items():
        module = BASE+suffix
        item = {"repository": atlas["repository"], "commit": atlas["commit"],
                "path": "lean/src/"+module.replace(".", "/")+".lean",
                "git_blob_sha1": rows[module][1]}
        checked = inspect_file(item, args.offline)
        lines = (ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]).read_bytes().splitlines(keepends=True)
        excerpts = []
        for start, end in intervals:
            assert 1 <= start <= end <= len(lines) and end-start+1 <= 120
            data = b"".join(lines[start-1:end])
            assert len(data) <= 12000
            excerpts.append({"start": start, "end": end, "sha256": hashlib.sha256(data).hexdigest()})
        sources.append({**item, "module": module, "sha256": checked["sha256"],
                        "matches_pinned_blob": True, "reviewed_excerpts": excerpts})
    stem = "selmer-integral-frontier-limit-comparison"
    artifacts = [f"notes/{stem}.md", f"paper/shared/{stem}.tex",
                 f"paper/shared/{stem}-references.tex",
                 "scripts/check_selmer_integral_frontier_limit_comparison.py"]
    dependencies = ["certificates/selmer-integral-frontier-first-global-bound.json",
                    "certificates/selmer-integral-frontier-second-global-bound.json",
                    "certificates/selmer-integral-frontier-padded-relations.json"]
    for path in artifacts:
        assert all(c >= 32 or c in (10, 9) for c in (ROOT/path).read_bytes()), path
    report = {
        "schema_version": 1,
        "status": "PASS",
        "verification_kind": "Pinned source provenance and artifact hashes; mathematical proofs are in the note.",
        "classification": "closed obligation inside W04; no whole proof-map node completed",
        "claim": "The original finite-level B1/B2 bounds imply K1/K2/K3 on the supplied original limiting auxiliary group, and their bounded Laurent versions.",
        "quantifiers": "Fix the normalized point, odd family, arithmetic tower and original Lim object. Constants C1/C2 precede every truncation. Good auxiliary levels may depend on that truncation. No uniformity over moving points.",
        "proved_steps": [
            "Exact finite Selmer quotient identification through the original common cover, retaining all local witness conditions.",
            "Integral rank bound from the finite Smith defect of cocycle-versus-boundary equations.",
            "Second-order integral lifting from nonempty finite compatible solution sets, retaining the original t^C2 loss and a unit coefficient.",
            "K3 by the previously proved original odd resultant descent.",
            "The original bounded continuous Laurent comparisons by common integral scaling."
        ],
        "sources": sources,
        "computation_scope": "No numerical sampling used; no Lean compilation or kernel verification.",
        "dependencies": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        "retained_inputs": [
            "Original normalized characteristic-prime point and odd Selmer family",
            "Original arithmetic tower and its Lim object with kernel, base-map, local-map and auxiliary-element convergence",
            "Original coefficient modules, polarized boundaries, ordinary bases, diagonal subgroup and unramified inertia conditions",
            "Nonzero block resultants and topological normal generation of the limiting kernel"
        ],
        "remaining": [
            "Actual arithmetic construction of the normalized models and tower",
            "Patched automorphic module and its support dimension at least 1+D",
            "Full characteristic-prime propagation and the final uniform integral Selmer bound"
        ],
        "reproduce": "python3 scripts/check_selmer_integral_frontier_limit_comparison.py --offline",
        "artifacts": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in artifacts},
    }
    (ROOT/f"certificates/{stem}.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "pinned_modules": len(sources),
                      "scope": report["verification_kind"]}))


if __name__ == "__main__":
    main()
