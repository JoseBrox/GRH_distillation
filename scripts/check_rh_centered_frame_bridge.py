#!/usr/bin/env python3
"""Verify bounded source evidence for the RH centered-frame bridge.

This checks bytes and dependency snapshots, not Lean or the open
arithmetic suppliers. Mathematical proofs are in the linked notes.
"""
from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
CACHE = ROOT / "build/source-cache/jsmorph/rh" / PIN
NOTE = "notes/rh-centered-frame-bridge.md"
CERT = "certificates/rh-centered-frame-bridge.json"
SOURCES = {
    "Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean": [(474, 504)],
    "Formalism/LocalRingCardinality/DataArith.lean": [(127, 135)],
    "Formalism/SizeWindowBrackets/FrameTraceRatioFinEquiv.lean": [(59, 90)],
    "Formalism/HarderNarasimhan/StatementPl.lean": [(55, 65)],
    "Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean": [(519, 568), (638, 645), (679, 689), (740, 744)],
    "Formalism/SharpRestriction/GlobalSchurBounds/Chosen.lean": [(53, 57), (75, 77)],
    "Formalism/RankGapBounds/MeanBoundSecondForm.lean": [(84, 95), (118, 129), (139, 167)],
    "Formalism/SizeWindowBrackets/QuotientSlopeBoundsWith.lean": [(15, 65)],
    "Formalism/SizeWindowBrackets/SChain.lean": [(33, 36)],
    "Formalism/SizeWindowBrackets/ErrorFormsWeakWindowsFalse.lean": [(16, 45)],
    "Formalism/LocalToGlobal/IndefiniteForms/IndefSide.lean": [(284, 316)],
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    atlas_bytes = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    atlas = json.loads(gzip.decompress(atlas_bytes))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == PIN
    modules = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for relative, ranges in SOURCES.items():
        path = "lean/src/" + relative
        data = (CACHE / path).read_bytes()
        blob = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
        assert blob == modules[relative.removesuffix(".lean").replace("/", ".")]
        lines = data.splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            excerpts.append({"lines": [lo, hi],
                             "sha256": sha(b"".join(lines[lo - 1:hi]))})
        records.append({"path": path, "git_blob_sha1": blob,
                        "sha256": sha(data), "lines": len(lines),
                        "excerpts": excerpts})
    result = {
        "schema_version": 1,
        "status": "conditional_same_map_centered_frame_substitution_with_explicit_nonframe_residual",
        "repository": "jsmorph/rh", "commit": PIN,
        "note": {"path": NOTE, "sha256": sha((ROOT / NOTE).read_bytes())},
        "script": {"path": str(Path(__file__).relative_to(ROOT)), "sha256": sha(Path(__file__).read_bytes())},
        "source_atlas_sha256": sha(atlas_bytes),
        "source_files": records,
        "proof_dependencies": [
            {"path": path, "sha256": sha((ROOT / path).read_bytes())}
            for path in ("notes/frame-degree-compatibility.md", "notes/one-construction-target.md",
                         "notes/rh-minimal-budget.md", "notes/averaged-theta-energy.md")
        ],
        "independent_review": {
            "centered_slope_input": "The originating geometric note's Sections 2-3 were independently checked by rh_source_symmetry; proof passed.",
            "new_source_bridge": "PASS by transport_defect: Sections 1-2, including source-unit conversion, same-map substitution, exact residual, weighted signs and all four surviving normalized shapes.",
            "independent_source_hash_and_contract_reads": [
                "Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean:474-504",
                "Formalism/SizeWindowBrackets/QuotientSlopeBoundsWith.lean:15-65",
                "Formalism/RankGapBounds/MeanBoundSecondForm.lean:118-167",
            ],
            "limits": "No whole upstream proof audit or Lean replay; remaining source-table clauses were not independently re-audited by this reviewer.",
            "second_review": {
                "reviewer": "geometric_simplify",
                "status": "PASS",
                "scope": "Sections 1-3 and hash-verified model, height/slope, LatGeom, scalar-error, density-size, word-count and isotropy contracts; additionally TopDensity568-608 and DataParams2:27-29.",
                "limits": "Ordinary mathematics and source contracts; no upstream proof replay or Lean build.",
            },
        },
        "scope": {
            "bounded_pinned_source_contracts_compared": True,
            "all_source_bytes_match_pinned_atlas": True,
            "ordinary_same_map_substitution_proof_in_note": True,
            "lean_kernel_replay": False,
            "upstream_source_proofs_audited": False,
            "new_arithmetic_supplier_proved": False,
            "any_entire_four_term_envelope_summand_removed": False,
            "current_rank_or_word_constructor_weakened": False,
        },
    }
    (ROOT / CERT).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "certificate": CERT,
                      "source_files": len(records),
                      "bounded_excerpts": sum(len(r["excerpts"]) for r in records),
                      "scope": "source bytes and dependency hashes; not a Lean build"}))


if __name__ == "__main__":
    main()
