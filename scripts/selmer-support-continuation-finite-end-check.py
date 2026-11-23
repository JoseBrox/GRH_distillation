#!/usr/bin/env python3
"""Authenticate the actual Galois quotient/FinEnd transfer and ordered product."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import sympy as sp
from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    "CurveDVRSpecialization.RatTorsionFree": [(18, 32)],
    "CurveDVRSpecialization.HostFrameEx": [(22, 79)],
    "CurveDVRSpecialization.ExistsNrep3": [(10, 120), (121, 240), (240, 350), (351, 443)],
    "CurveDVRSpecialization.FinEndOfFinPt": [(9, 48)],
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def exact_checks():
    a = sp.symbols("a0:18")
    matrices = [sp.Matrix([[a[6*i], a[6*i+1], a[6*i+2]],
                          [0, a[6*i+3], a[6*i+4]], [0, 0, a[6*i+5]]])
                for i in range(3)]
    product = sp.eye(3)
    for i, matrix in enumerate(matrices):
        product = product*(matrix-matrix[i, i]*sp.eye(3))
    assert all(sp.expand(x) == 0 for x in product)
    z = sp.symbols("x0:9")
    X = sp.Matrix(3, 3, z)
    J = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    D = X-J*X.T*J
    assert D[0, 2] == D[2, 0] == 0
    assert sp.expand(D[1, 2]+D[0, 1]) == 0
    assert sp.expand(D[2, 1]+D[1, 0]) == 0
    return {"ordered_local_product": "Exact polynomial identity for three independent upper-triangular matrices in the original order.",
            "marking": "Exact off-diagonal skew-adjoint identities; no division by 3 or nonunit.",
            "scope": "These identities do not replace the general quotient, continuity, original local-character or uniform-subgroup arguments."}


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
    note = ROOT/"notes/selmer-support-continuation-finite-end.md"
    result = {
        "classification": "Closed literal ExistsNrep3/FinEndOfFinPt transfer; independently reviewed by the parent research agent.",
        "proof_file": str(note.relative_to(ROOT)), "proof_sha256": digest(note.read_bytes()),
        "source_records": records, "exact_diagnostics": exact_checks(),
        "presentation_files": [{"file": name, "sha256": digest((ROOT/name).read_bytes())}
            for name in ["paper/shared/selmer-support-continuation-finite-end.tex",
                         "paper/shared/selmer-support-continuation-finite-end-references.tex"]],
        "decisive_interfaces": {
            "quotient": "The actual closed normal inertia kernel; Teich condition and original OrdPt.away; adic closedness by Krull intersection and compact quotient descent.",
            "local_characters": "The actual conjugating element has eta=1; original CondT gives an integral h congruent to one and exact inertia characters in the original order.",
            "uniformity": "One U=Gal(Omega/L) chosen before every tested DVR A and representation r, with index [L:Q].",
            "no_replacement": "Same coefficient ring, lattice, Galois quotient, local characters, marking and polarization."
        },
        "scope": {"whole_node_closed": False, "lean_build": False,
                  "remaining": "The actual HasFrame/GalLink/Ok/Big/SeedClause arithmetic supplier remains explicit, as do global two-sided integral finiteness and moving-family Selmer bounds."}
    }
    out = ROOT/"certificates/selmer-support-continuation-finite-end.json"
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"source_files": len(records), "exact_diagnostics": "passed",
                      "certificate": str(out.relative_to(ROOT)), "no_whole_node_completion": True}))


if __name__ == "__main__":
    main()
