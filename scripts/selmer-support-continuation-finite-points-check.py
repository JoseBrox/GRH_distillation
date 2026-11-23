#!/usr/bin/env python3
"""Authenticate literal GoodPt/FinPt/AbsMain interfaces and proof records.

This is a source and review certificate, not a Lean build or a numerical
substitute for the general ring-theoretic and arithmetic arguments.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    "CurveDVRSpecialization.IsUnitOrIsUnitOfAddOne": [(107, 122)],
    "FrobeniusSmoothVectors.LeAdicClosure": [(140, 181)],
    "CurveDVRSpecialization.PropagationTheoremGL2": [(41, 84)],
    "CurveDVRSpecialization.SecondThirdPrimeConditionTransferAlt": [(71, 85), (103, 107)],
    "CurveDVRSpecialization.GoodPtOf": [(60, 88)],
    "CurveDVRSpecialization.FinPtOf": [(29, 120), (121, 181), (183, 284), (285, 344)],
    "CurveDVRSpecialization.AbsMain": [(12, 30)],
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert digest(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    modules = {row[0]: row for row in atlas["modules"]}
    records = []
    for name, ranges in RANGES.items():
        module = BASE+name
        item = {"repository": atlas["repository"], "commit": atlas["commit"],
                "path": "lean/src/"+module.replace(".", "/")+".lean",
                "git_blob_sha1": modules[module][1]}
        source = inspect_file(item, args.offline)
        lines = (ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]).read_text().splitlines()
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo+1 <= 120
        records.append({**item, "sha256": source["sha256"], "line_count": len(lines),
                        "ranges": [{"start": lo, "end": hi,
                                    "sha256": digest(("\n".join(lines[lo-1:hi])+"\n").encode())}
                                   for lo, hi in ranges]})
    note = ROOT/"notes/selmer-support-continuation-finite-points.md"
    files = ["paper/shared/selmer-support-continuation-finite-points.tex",
             "paper/shared/selmer-support-continuation-finite-points-references.tex"]
    result = {
        "classification": "Closed literal GoodPt/FinPt/AbsMain subobligation; independently reviewed.",
        "proof_file": str(note.relative_to(ROOT)), "proof_sha256": digest(note.read_bytes()),
        "source_records": records,
        "presentation_files": [{"file": name, "sha256": digest((ROOT/name).read_bytes())} for name in files],
        "decisive_interfaces": {
            "all_DVR_lifts": "The actual pullback C=A times_{k(A)} k(O) is complete Noetherian local with residue k(O); m_C^n=m_A^n and A is a finite C-module. IsLiftA includes the required diagonal residual matrix.",
            "GoodPt": "Every original complete DVR, every injective field map, and the original MatIrr hypothesis; full determinant law and ordered characters over the same A.",
            "FinPt": "Exact O-k(O)-A scalar tower and fixed inertia intersect ker(Psi). OffFin plus the balanced product u^b v^a forces global triangularity in the DVR domain.",
            "diagonal": "Original local ordered equations, polarization, finite ell-group continuity, and the original nonzero class-group exponent. No division by 3.",
            "output": "The three literal AbsMain conclusions under the same actual ModIn inputs.",
        },
        "scope": {"whole_node_closed": False, "lean_build": False,
                  "computation_claim": "Authenticated interfaces and proof hashes only; the note and TeX prove the general statements.",
                  "remaining": "Actual GalLink/FinEnd transfer, global two-sided finite-ring criterion, and moving-family integral Selmer estimate remain separate; actual ModIn suppliers are retained."}
    }
    out = ROOT/"certificates/selmer-support-continuation-finite-points.json"
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"source_files": len(records), "source_authentication": "passed",
                      "certificate": str(out.relative_to(ROOT)), "no_whole_node_completion": True}))


if __name__ == "__main__":
    main()
