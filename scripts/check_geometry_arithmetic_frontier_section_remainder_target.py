#!/usr/bin/env python3
"""Authenticate the next arithmetic section obligation; no supplier closure."""
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
STEM = "geometry-arithmetic-frontier-section-remainder-target"
TP = "Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts."
DP = "Development.AbelianVarietyTheory.Proofs.DivisorProofs."
DD = "Development.AbelianVarietyTheory.Definitions.Divisors."
RANGES = {
    TP+"ThirdPlaceSeries.ExistsDegreeParametersBound": [(34, 70)],
    TP+"HodgeBundleWeights.ExistsDegreeParametersBound": [(33, 76)],
    DP+"HilbertSamuelComponentShortBasisBound": [(26, 37)],
    DP+"ArithmeticHilbertSamuelBound": [(4, 8), (19, 20)],
    DD+"HermSysHypOneLeLambdaZero": [(253, 271)],
    DD+"IntegralBound": [(34, 70)],
    "Formalism.LocalToGlobal.IndefiniteForms.IndefiniteTree.RealCubicMeans."
    "LogMeanShares.LogMeanStatements.HSClaim": [(7, 22)],
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == REPO and atlas["commit"] == REV
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    sources = []
    for module, ranges in RANGES.items():
        rel = "lean/src/"+module.replace(".", "/")+".lean"
        result = inspect_file({"repository": REPO, "commit": REV, "path": rel,
                               "git_blob_sha1": blobs[module]}, args.offline)
        assert result["matches_pinned_blob"]
        lines = (ROOT/"build/source-cache"/REPO/REV/rel).read_bytes().splitlines(keepends=True)
        assert all(1 <= a <= b <= len(lines) and b-a < 120 for a, b in ranges)
        sources.append({"module": module,
                        **{k: result[k] for k in ["repository", "commit", "path",
                            "git_blob_sha1", "sha256", "matches_pinned_blob"]},
                        "excerpts": [{"lines": [a, b], "sha256": sha(b"".join(lines[a-1:b]))}
                                     for a, b in ranges]})
    D, T, P, kap, B, delta, rank = sp.symbols("D T P kap B delta rank", positive=True)
    exact = D*P*(kap/T+1)
    allowance = 4*(exact+T*P)+2*D*P*kap/T
    difference = 3*exact+4*T*P+2*D*P*kap/T
    assert sp.expand(allowance-exact-difference) == 0
    z = 1-B*delta/rank
    assert sp.expand(-(1-z)*exact+(1-z)*allowance-B*delta/rank*difference) == 0
    artifacts = [f"notes/{STEM}.md", "scripts/"+Path(__file__).name]
    certificate = {
        "date": "2026-11-22", "status": "PASS", "classification": "Open frontier and existing source refinement",
        "scope": "Pinned dependency audit and exact constant identities; no new geometric supplier is proved.",
        "sources": sources,
        "exact_checks": {"symbolic_identities": 2,
                         "actual_J": "D P (kap/T+1)",
                         "allowance_minus_actual": "3 D P (kap/T+1)+4 T P+2 D P kap/T",
                         "slope_improvement": "(B delta/rank) times allowance_minus_actual"},
        "retained_obligations": [
            "Actual arithmetic models, canonical line identification, frames and component lattice/metric dictionary.",
            "Birationality, two nef and big line bundles, multiplication and norm estimates, and integral short families.",
            "Exact finite jet kernels and integral product-lattice lifts, archimedean lifting bounds and deep-jet short sections.",
            "Arithmetic Bertini, point-height control, evaluation-lattice degree and the geometric height identity.",
            "HSShort.GeoBound and its actual quoted arithmetic hypotheses remain to be reconstructed."
        ],
        "limitations": ["No Lean compilation.", "No whole proof node closes.",
                        "The smaller J is already in the pinned source; it is not a new proof of its hypotheses."],
        "artifacts": {p: sha((ROOT/p).read_bytes()) for p in artifacts},
        "reproduce": "python3 scripts/"+Path(__file__).name+" --offline"
    }
    (ROOT/"certificates"/(STEM+".json")).write_text(json.dumps(certificate, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources), "symbolic_identities": 2,
                      "new_suppliers_proved": 0}))


if __name__ == "__main__":
    main()
