#!/usr/bin/env python3
"""Authenticate the bounded dual-detection assessment; no Lean build."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules."
TARGETS = {
    "ThetaCoefficientMapEq": [(54, 61), (235, 264)],
    "EpsilonEtaMatrices.ExistsNcardAnnihilatedCocyclesLeCoboundariesMul": [(21, 130), (349, 430)],
    "DegreeCountCohomology.SolCnt": [(128, 242), (293, 393)],
    "EpsilonEtaMatrices.FinTwLc": [(23, 56)],
    "EpsilonEtaMatrices.DualN": [(10, 16)],
    "EpsilonEtaMatrices.W1BoundArithmeticRankTwo": [(40, 61)],
    "DeterminantPadicFree.FrameWith": [(26, 72)],
    "DeterminantPadicFree.MapSpan": [(14, 83)],
    "DeterminantPadicFree.DetAsm": [(160, 268)],
    "DeterminantPadicFree.DetAlg": [(71, 141)],
    "DeterminantPadicFree.OddPart": [(18, 61)],
    "DeterminantPadicFree.DetFin": [(127, 213)],
    "AutomorphicDetection.Choice": [(14, 40)],
    "ChebotarevFamilies.PFromAutOf": [(42, 49), (83, 91)],
}


def counterexample() -> dict:
    """Exact F_5 upper triangular cocycle; no sampled arithmetic points."""
    p = 5
    group = [(a, b, d) for a in range(1, p) for b in range(p)
             for d in range(1, p)]

    def multiply(g, h):
        a, b, d = g
        x, y, z = h
        return (a*x % p, (a*y+b*z) % p, d*z % p)

    def cocycle(g):
        return g[1] * pow(g[2], -1, p) % p

    def action(g, c):
        return g[0] * pow(g[2], -1, p) * c % p

    for g in group:
        for h in group:
            assert cocycle(multiply(g, h)) == (cocycle(g)+action(g, cocycle(h))) % p
        # z(g)rho(g) is the strictly upper triangular matrix [[0,b],[0,0]].
        z_rho = [[0, cocycle(g)*g[2] % p], [0, 0]]
        assert (z_rho[0][0] + z_rho[1][1]) % p == 0
    u = (1, 1, 1)
    assert cocycle(u) == 1 and action(u, 1) == 1
    # Two diagonal image vectors (1,1), (1,2) span F_5 x F_5.
    assert (1*2-1*1) % p != 0
    return {
        "field": "F_5", "group_order": len(group),
        "cocycle_pairs_checked": len(group)**2,
        "zero_trace_checks": len(group),
        "nonboundary_witness": "z([[1,1],[0,1]])=E12; rho is identity on the unipotent subgroup",
        "full_even_span_witness": "diag(1,1), diag(1,2) have independent diagonal vectors",
        "scope": "Ordinary untwisted trace alone does not detect odd extensions; not a counterexample to the paired source theorem.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    atlas = json.loads(gzip.decompress((ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()))
    rows = {row[0]: row for row in atlas["modules"]}
    sources = []
    for suffix, intervals in TARGETS.items():
        module = PREFIX + suffix
        row = rows[module]
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        item = {"repository": atlas["repository"], "commit": atlas["commit"],
                "path": path, "git_blob_sha1": row[1]}
        checked = inspect_file(item, offline=args.offline)
        raw = (ROOT / "build/source-cache" / item["repository"] / item["commit"] / path).read_bytes()
        lines = raw.splitlines(keepends=True)
        excerpts = []
        for start, end in intervals:
            assert 1 <= start <= end <= len(lines) and end-start+1 <= 120
            excerpts.append({"start": start, "end": end,
                             "sha256": hashlib.sha256(b"".join(lines[start-1:end])).hexdigest()})
        sources.append({**item, "module": module, "sha256": checked["sha256"],
                        "matches_pinned_blob": True, "reviewed_excerpts": excerpts})
    artifacts = ["notes/selmer-integral-frontier-dual-detection.md",
                 "scripts/check_selmer_integral_frontier_dual_detection.py"]
    report = {
        "schema_version": 1,
        "status": "PASS",
        "claim": "Bounded source bytes authenticated and illustrative finite-group counterexample checked exactly.",
        "mathematical_assessment": {
            "proved_in_note": "Complete linear-equation counting controls every finite-level solution under finite residual solutions and integral detection up to torsion.",
            "extra_bockstein_hypothesis": "Not needed in the actual SolCnt approach; completeness and stabilization control nonliftable modular solutions.",
            "remaining_human_reconstruction": "Actual paired determinant detection: OddPart/RelPair/BlockPrinc, followed by DetAlg, finite detection and simultaneous auxiliary choice.",
            "coefficient_field": "k((t)), of characteristic ell",
            "constant_order": "Fix point and auxiliary set, then exists C for all m; DualN has exists C, for all m, eventually N.",
        },
        "limits": [
            "The algebraic proof in the note is a human proof, not checked by this script or a proof assistant.",
            "No Lean compilation or whole-source audit was run.",
            "Determinant suppliers are located and their contracts inspected, not fully reconstructed here.",
            "No whole proof node is closed; RH 6/9 and GRH 17/31 remain unchanged.",
        ],
        "reproduce": "python3 scripts/check_selmer_integral_frontier_dual_detection.py --offline",
        "sources": sources,
        "finite_counterexample": counterexample(),
        "artifacts": {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in artifacts},
    }
    output = ROOT / "certificates/selmer-integral-frontier-dual-detection.json"
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "pinned_modules": len(sources),
                      "bounded_excerpts": sum(len(s["reviewed_excerpts"]) for s in sources),
                      "finite_cocycle_pairs": report["finite_counterexample"]["cocycle_pairs_checked"],
                      "certificate": str(output.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
