#!/usr/bin/env python3
"""Exact scalar checks and pinned-source evidence for the mean-volume note.

This checks source bytes and finite algebra. It does not run Lean or verify
the tower construction, arithmetic intersection theorem, or upstream proofs.
Missing source files can be cached with scripts/source_excerpt.py --atlas.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMIT = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
ATLAS = ROOT / "blueprint/lean-source-imports.json.gz"
CACHE = ROOT / "build/source-cache/jsmorph/rh" / COMMIT
NOTE = "notes/mean-volume-supplier.md"
CERT = ROOT / "certificates/mean-volume-supplier.json"

SOURCES = {
    "Development/AbelianVarietyTheory/Definitions/Divisors/SemiposAtOfPositive.lean": [(72, 105)],
    "Development/AbelianVarietyTheory/Definitions/Divisors/IsHomogeneousCompIdeal.lean": [(220, 286)],
    "Development/AbelianVarietyTheory/Definitions/Divisors/IsLatBasisHtLatIffSpanEq.lean": [(515, 541)],
    "Development/AbelianVarietyTheory/Definitions/Foundations/IsProbabilityMeasureMuPart.lean": [(664, 681), (730, 734), (787, 826)],
    "Development/AutomorphicSpectrum/Definitions/GlobalGeometry/ModelSmall.lean": [(50, 66)],
    "Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/CompactGapsGE.lean": [(73, 81)],
    "Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/HeckeSectionsIsotropicCommutatorPairingPower.lean": [(76, 93)],
    "Development/WeilBound/CoreStatements/FlagImmersions/MeanSlopeOfProportionalVolume.lean": [(13, 39)],
    "Development/AutomorphicSpectrum/Proofs/GeometryProofs/CostTwoLogBound.lean": [(48, 84)],
    "Development/AutomorphicSpectrum/Proofs/GeometryProofs/UniformAllNormHeightBound.lean": [(300, 372)],
    "Development/AutomorphicSpectrum/Proofs/GeometryProofs/AbelianCmCompLawsBound.lean": [(54, 116), (117, 139)],
    "Development/AutomorphicSpectrum/Proofs/GeometryProofs/DeepStROfVolume.lean": [(21, 58)],
    "Development/AutomorphicSpectrum/Proofs/GeometryProofs/FinalTheoremOfInputsRight.lean": [(28, 39)],
    "Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/DeepStROfHyp.lean": [(47, 58)],
    "Development/AutomorphicSpectrum/Statements/TowerExistence/GoodTowerExistsX.lean": [(22, 36)],
    "Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/HeightAddLogNonneg.lean": [(66, 105)],
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def exact_checks() -> dict:
    # e^(3/4) exceeds its positive Taylor polynomial and hence exceeds two.
    exp_lower = 1 + F(3, 4) + F(3, 4) ** 2 / 2 + F(3, 4) ** 3 / 6
    assert exp_lower > 2
    assert 4 * 2 * 4**2 == 128
    assert F(128, 127) <= F(8, 7)
    assert 6 + F(9, 7) + F(8, 7) == F(59, 7) < 9 < 40
    assert 2 * 40 == 80 < 120
    # Equal component volume permits division before averaging, including
    # signed arithmetic intersection numbers and fractional positive volumes.
    examples = 0
    for count in range(1, 8):
        for dim in range(0, 5):
            for denom in range(1, 6):
                volume, degree = F(count + 1, denom), F(denom + 2, count)
                values = [F((-1) ** i * (i + 2), denom + i) for i in range(count)]
                lhs = sum(v / ((dim + 1) * volume * degree) for v in values) / count
                rhs = sum(values) / ((dim + 1) * count * volume * degree)
                assert lhs == rhs
                examples += 1
    # Universal constant absorption after the mean-volume comparison.
    absorption = 0
    for ct in [F(0), F(1, 3), F(7)]:
        for logb in [F(1), F(5), F(10)]:
            for logrd in [F(0), F(1, 7), F(8)]:
                for lval in [F(0), F(2)]:
                    for mass in [F(0), F(1, 2), F(9)]:
                        for spread in [F(0), F(7, 3)]:
                            err = (logb + logrd + lval) * mass + spread
                            cost = F(59, 7) * logb + 40 * logrd
                            assert ct * err + 2 * cost * mass <= (ct + 80) * err
                            absorption += 1
    return {
        "exp_three_quarters_lower_polynomial": str(exp_lower),
        "logarithmic_coefficient": "59/7",
        "universal_finite_place_increment": 80,
        "equal_volume_exact_examples": examples,
        "constant_absorption_exact_examples": absorption,
        "proof_not_replaced_by_finite_examples": True,
    }


def source_records() -> list[dict]:
    atlas = json.loads(gzip.decompress(ATLAS.read_bytes()))
    fields = atlas["module_fields"]
    names = {row[fields.index("name")]: row for row in atlas["modules"]}
    records = []
    for path, ranges in SOURCES.items():
        raw = (CACHE / "lean/src" / path).read_bytes()
        module = path.removesuffix(".lean").replace("/", ".")
        row = names[module]
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        assert blob == row[fields.index("git_blob_sha1")], path
        assert len(raw) == row[fields.index("bytes")], path
        lines = raw.splitlines(keepends=True)
        excerpts = []
        for first, last in ranges:
            assert 1 <= first <= last <= len(lines) and last - first < 120
            excerpts.append({"lines": [first, last], "sha256": sha(b"".join(lines[first - 1:last]))})
        records.append({"path": "lean/src/" + path, "git_blob_sha1": blob,
                        "sha256": sha(raw), "lines": len(lines), "excerpts": excerpts})
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write the reproducible certificate")
    args = parser.parse_args()
    old = json.loads(CERT.read_text()) if CERT.exists() else {}
    result = {
        "schema_version": 1,
        "status": "conditional_mean_volume_reduction_and_proved_finite_place_improvement",
        "repository": "jsmorph/rh", "commit": COMMIT,
        "note": {"path": NOTE, "sha256": sha((ROOT / NOTE).read_bytes())},
        "script": {"path": "scripts/check_mean_volume_supplier.py", "sha256": sha(Path(__file__).read_bytes())},
        "source_atlas_sha256": sha(ATLAS.read_bytes()),
        "source_files": source_records(),
        "exact_checks": exact_checks(),
        "independent_review": old.get("independent_review", {
            "finite_place_lemma": "rh_source_symmetry: PASS; checked Chebyshev, monotone large-prime bound, coefficient59/7 and increment80.",
            "written_note_and_source_bridge": "Requested; not yet recorded.",
        }),
        "scope": {
            "all_source_bytes_match_pinned_atlas": True,
            "bounded_source_statements_and_selected_proof_passages_read": True,
            "new_elementary_finite_place_proof": True,
            "new_uniform_tower_intersection_proof": False,
            "new_same_data_geometric_construction": False,
            "lean_kernel_replay": False,
            "complete_upstream_proof_audit": False,
            "uniform_finite_hilbert_samuel_threshold_claimed": False,
        },
    }
    if args.write:
        CERT.write_text(json.dumps(result, indent=2) + "\n")
    else:
        assert old == result, "Certificate differs; inspect changes and rerun with --write."
    print(json.dumps({"status": "PASS", "source_files": len(result["source_files"]),
                      "bounded_excerpts": sum(len(r["excerpts"]) for r in result["source_files"]),
                      "exact_checks": result["exact_checks"]}))


if __name__ == "__main__":
    main()
