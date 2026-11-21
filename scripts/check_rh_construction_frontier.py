#!/usr/bin/env python3
"""Exact finite checks and pinned-source record for the RH frontier note.

The universal proofs are in the note. These checks do not run Lean, prove
the arithmetic construction, or certify upstream analytic inputs.
"""
from __future__ import annotations

import gzip
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
CACHE = ROOT / "build/source-cache/jsmorph/rh" / PIN
NOTE = "notes/rh-construction-frontier.md"
CERT = "certificates/rh-construction-frontier.json"
SOURCES = {
    "Development/AbelianVarietyTheory/Definitions/GlobalTwisting/APerTw.lean": [(23, 57)],
    "Development/AutomorphicArithmetic/CharacterBoxes/ExS.lean": [(10, 12)],
    "Development/AutomorphicArithmetic/CharacterBoxes/ExistsPageN.lean": [(12, 49)],
    "Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/LabelDatum.lean": [(91, 115)],
    "Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ExplicitFormulaErrorOfHostConditions.lean": [(144, 151)],
    "Formalism/SizeWindowBrackets/SChain.lean": [(50, 58)],
    "Formalism/LocalRingCardinality/Params.lean": [(36, 53)],
    "Formalism/LocalRingCardinality/DataParams₂.lean": [(27, 39), (73, 89), (151, 156)],
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def determinant(matrix: list[list[int]]) -> F:
    a = [[F(x) for x in row] for row in matrix]
    result = F(1)
    for j in range(len(a)):
        pivot = next(i for i in range(j, len(a)) if a[i][j])
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        result *= a[j][j]
        for i in range(j + 1, len(a)):
            ratio = a[i][j] / a[j][j]
            for k in range(j, len(a)):
                a[i][k] -= ratio * a[j][k]
    return result


def finite_checks() -> dict:
    determinants = []
    for n in range(1, 33):
        matrix = [[1] + [int(i == j) - int(i == 0) for j in range(1, n)]
                  for i in range(n)]
        det = determinant(matrix)
        assert abs(det) == n
        determinants.append({"n": n, "one_fibre_determinant": int(det),
                             "four_fibre_index": n ** 4})
    kernel_examples = 0
    for n in range(1, 7):
        for z in itertools.product((-1, 0, 1), repeat=n):
            if sum(z) % n == 0:
                k = sum(z) // n
                assert sum(value - k for value in z) == 0
            kernel_examples += 1
    hinge_examples = 0
    for lam, z, b, r in itertools.product(
        (F(5, 4), F(3, 2), F(2), F(3), F(5)),
        map(F, range(33)), (F(1, 4), F(1), F(3)),
        (F(0), F(1, 8), F(1), F(7))
    ):
        h = lambda w: max(z - w, 0) - max(z - lam * w, 0)
        assert h(b + r) >= h(b) - r * int(z >= b)
        hinge_examples += 1
    lam, z, b, r = F(2), F(2), F(3, 2), F(1, 4)
    h = lambda w: max(z - w, 0) - max(z - lam * w, 0)
    assert h(b + r) == h(b) - r
    return {"determinants": determinants,
            "kernel_decomposition_examples": kernel_examples,
            "relative_hinge_examples": hinge_examples,
            "relative_hinge_constant_one_attained": True}


def source_records() -> list[dict]:
    atlas = json.loads(gzip.decompress((ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == PIN
    modules = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for relative, ranges in SOURCES.items():
        path = "lean/src/" + relative
        data = (CACHE / path).read_bytes()
        blob = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
        assert blob == modules[relative.removesuffix(".lean").replace("/", ".")]
        lines = data.splitlines(keepends=True)
        reads = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            excerpt = b"".join(lines[lo - 1:hi])
            reads.append({"lines": [lo, hi], "sha256": sha(excerpt)})
        records.append({"path": path, "git_blob_sha1": blob,
                        "sha256": sha(data), "lines": len(lines), "excerpts": reads})
    return records


def main() -> None:
    result = {
        "schema_version": 1,
        "status": "proved_elementary_reductions_with_open_arithmetic_supplier",
        "repository": "jsmorph/rh", "commit": PIN,
        "note": {"path": NOTE, "sha256": sha((ROOT / NOTE).read_bytes())},
        "script": {"path": str(Path(__file__).relative_to(ROOT)), "sha256": sha(Path(__file__).read_bytes())},
        "source_atlas_sha256": sha((ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()),
        "source_files": source_records(),
        "finite_checks": finite_checks(),
        "proof_dependencies": [
            {"path": path, "sha256": sha((ROOT / path).read_bytes())}
            for path in ("notes/rh-direct-transfer.md", "notes/rh-specialization.md",
                         "notes/one-construction-target.md", "blueprint/full-proof-program.md",
                         "blueprint/endpoint-field-ledger.md")
        ],
        "independent_review": {
            "relative_transfer_and_dilation_criterion": "PASS: transport reviewer checked exact current Section 3, including signs, counts, domains and new supplier obligations.",
            "integral_index_proof": "ordinary quotient-map proof; exact finite determinant and kernel checks supplement it"
        },
        "scope": {
            "ordinary_math_proofs": True,
            "pinned_source_and_excerpt_hashes_recomputed": True,
            "lean_build_run": False, "kernel_replay": False,
            "full_upstream_proof_audit": False,
            "paired_arithmetic_supplier_constructed": False,
            "RH_or_GRH_claimed_proved": False,
            "completion_percentage_or_prompt_prediction": "not estimated; no defensible mathematical denominator or remaining-duration bound"
        }
    }
    (ROOT / CERT).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "source_files": len(result["source_files"]),
                      "determinants": len(result["finite_checks"]["determinants"]),
                      "hinge_cases": result["finite_checks"]["relative_hinge_examples"],
                      "certificate": CERT}))


if __name__ == "__main__":
    main()
