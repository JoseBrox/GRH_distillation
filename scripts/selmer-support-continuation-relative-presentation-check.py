#!/usr/bin/env python3
"""Authenticate the original relative-presentation interface and its weights."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    "UnitaryThreeGroups.IsLocPres": [(15, 39)],
    "UnitaryThreeGroups.BoxPresOf": [(63, 145), (149, 164)],
    "UnitaryThreeGroups.BoxCount": [(46, 129)],
    "UnitaryThreeGroups.BoxAbs": [(61, 117)],
    "UnitaryThreeGroups.ExistsGaloisCyclotomicNegOneTrivialOnEtaPsi": [(43, 77)],
    "CommutativeAlgebra.LemmaP": [(256, 306)],
    "UnitaryThreeGroups.ULocEx": [(24, 51)],
    "UnitaryThreeGroups.RingEx": [(109, 153)],
    "UnitaryThreeGroups.ModelOfPres": [(241, 277)],
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def weights() -> list[dict]:
    result = []
    for weight in range(-2, 3):
        basis = [(i, j) for i in range(3) for j in range(3) if j-i == weight]
        action = sp.zeros(len(basis))
        for col, (i, j) in enumerate(basis):
            action[basis.index((2-j, 2-i)), col] = -1
        assert action**2 == sp.eye(len(basis))
        fixed = len(basis) - (action-sp.eye(len(basis))).rank()
        assert fixed == int(abs(weight) <= 1)
        # Only exchange blocks and scalar -1 blocks occur, so the same
        # dimensions hold over every field in which 2 is invertible.
        assert all(value in [-1, 0] for value in action)
        result.append({"weight": weight, "dimension": len(basis),
                       "complex_conjugation": [list(action.row(i)) for i in range(len(basis))],
                       "fixed_dimension": fixed})
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    lookup = {row[0]: row for row in atlas["modules"]}
    sources = []
    for suffix, ranges in RANGES.items():
        module = PREFIX+suffix
        row = lookup[module]
        path = "lean/src/"+module.replace(".", "/")+".lean"
        entry = {"repository": atlas["repository"], "commit": atlas["commit"],
                 "path": path, "git_blob_sha1": row[1]}
        checked = inspect_file(entry, args.offline)
        data = (ROOT/"build/source-cache"/atlas["repository"]/atlas["commit"]/path).read_bytes()
        lines = data.decode().splitlines()
        excerpts = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines) and end-start < 120
            excerpts.append({"start": start, "end": end,
                             "sha256": sha("\n".join(lines[start-1:end]).encode())})
        sources.append({"module": module, "path": path, "sha256": sha(data),
                        "git_blob_sha1": row[1], "ranges": excerpts,
                        "source_check": checked})
    files = ["paper/shared/selmer-support-continuation-relative-presentation.tex",
             "paper/shared/selmer-support-continuation-relative-presentation-references.tex",
             "notes/selmer-support-continuation-relative-presentation.md"]
    output = {
        "classification": "Closed original good-data BoxPres subobligation; local chart and final integral budget remain separate.",
        "source_repository": atlas["repository"], "source_commit": atlas["commit"],
        "scope": "Actual original local ring, all original finite inertia quotients and literal integral relation ideal; exact entry-coordinate and relation-weight counts.",
        "cohomology_scope": "H0 and H3 of the exact relative cone vanish; finite Poitou-Tate and Euler identities give Ob_j-Tang_j=dim M_j^(c=1).",
        "verification_scope": "Pinned source authentication and exact polarized matrix invariant dimensions; no Lean rebuild or automated arithmetic proof.",
        "sources": sources,
        "weights": [{**item, "complex_conjugation": [[int(v) for v in row] for row in item["complex_conjugation"]]} for item in weights()],
        "artifacts": [{"path": path, "sha256": sha((ROOT/path).read_bytes())} for path in files],
    }
    dest = ROOT/"certificates/selmer-support-continuation-relative-presentation.json"
    dest.write_text(json.dumps(output, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"certificate": str(dest.relative_to(ROOT)), "sources": len(sources),
                      "weight_counts": "passed", "scope": output["verification_scope"]}))


if __name__ == "__main__":
    main()
