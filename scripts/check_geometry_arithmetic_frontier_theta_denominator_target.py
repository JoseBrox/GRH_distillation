#!/usr/bin/env python3
"""Authenticate the exact next theta-denominator target; prove no new supplier."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import check_geometry_arithmetic_frontier_geometric_filtration as auth


STEM = "geometry-arithmetic-frontier-theta-denominator-target"
DP = "Development.AbelianVarietyTheory.Proofs.DivisorProofs."
HW = "Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights."
RANGES = {
    DP + "ExistsBoundedIntegerGoodCoverThetaSeriesIntegral": [(31, 79), (80, 118)],
    DP + "LogShortThetaSeriesDenominatorBoundLeStatement": [(16, 20)],
    HW + "ExistsGoodCoverAtMinimalLevel": [(20, 57)],
    HW + "ShortSpanCompositionClosed": [(24, 31), (68, 112)],
    HW + "ShortGeneratorNormComparison": [(23, 37)],
    HW + "ShortVectorsSpanCuspLattice": [(28, 34), (77, 85)],
    HW + "ShortVectorWeightBound": [(23, 28), (79, 85)],
    HW + "ExistsDegreeParametersBound": [(33, 76)],
    HW + "ExistsWeightHodgeBundleGenerated": [(22, 53)],
    HW + "HermitianGeometricHypothesisHolds": [(19, 47)],
    HW + "GeneratedWeightsMulStableAndBounded": [(16, 49), (50, 77)],
    HW + "ToKnownTheoremsOf": [(7, 35)],
    DP + "HeightBirationalImageEqTupleHeight": [(21, 26)],
    DP + "IsImageHeightUnique": [(403, 441), (449, 472)],
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    files = [f"notes/{STEM}.md", "scripts/" + Path(__file__).name]
    record = {
        "date": "2026-11-22", "status": "PROVENANCE_PASS_TARGET_OPEN",
        "classification": "Exact next-target card; no newly proved arithmetic supplier",
        "target": "Uniform N_A=intZ^2 with log N_A<=C(frL)^2 sizeK clearing the actual normalized theta family into the original integral cusp lattice.",
        "source_declaration": "GlobalTheory.CovInt.integral_smul_thLa",
        "three_local_cases": ["Primes outside level", "Primes dividing level without a square below the place", "Prime squares dividing level"],
        "preserved_data": ["Actual level indicator, harmonic polynomial, self-dual lattice and connection.",
                           "Original coefficient field, valuation set and determinant-ideal scalar condition.",
                           "The betaH normalization and both powers of intZ.",
                           "Theta spanning and raw theta norm as separate inputs."],
        "scope": "Pinned source bytes and bounded excerpts authenticated; no finite-place theta theorem reconstructed or Lean project built.",
        "sources": sources,
        "artifacts": [{"path": p, "sha256": auth.sha((auth.ROOT / p).read_bytes())} for p in files],
        "checker_dependency": {"path": "scripts/check_geometry_arithmetic_frontier_geometric_filtration.py",
                               "sha256": auth.sha((auth.ROOT / "scripts/check_geometry_arithmetic_frontier_geometric_filtration.py").read_bytes())},
        "reproduce": "python3 scripts/" + Path(__file__).name + " --offline"}
    out = auth.ROOT / "certificates" / (STEM + ".json")
    out.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "source_modules": len(sources), "new_supplier_count": 0}))


if __name__ == "__main__":
    main()
