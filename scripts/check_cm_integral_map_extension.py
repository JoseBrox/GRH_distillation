#!/usr/bin/env python3
"""Authenticate the exact CM extension contracts and primary theorem.

This script checks provenance only. The valuative and divisor arguments
are mathematics in the note, reviewed separately. No Lean replay or
automated geometric proof is claimed.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
TOR = ("ReciprocityTheory.ReductiveGroups.ArithmeticGeometry."
       "BirationalGeometry.ToroidalCompactification.")
AS = "Development.AutomorphicSpectrum."
SOURCES = [
    (TOR + "PushInvertible", [[52, 66]]),
    (TOR + "TwoWeightEqOneAddRoot", [[72, 91]]),
    (AS + "Definitions.GlobalGeometry.IsCMFrame", [[36, 64]]),
    (AS + "Proofs.GeometryProofs.CmPackProductFrame", [[27, 42]]),
    (AS + "Proofs.GeometryProofs.LieModelExtendsOverDvr", [[1, 10]]),
]
PRIMARY = {
    "path": "build/reference-cache/faltings-finiteness-1983.pdf",
    "url": ("https://math.uchicago.edu/~drinfeld/Deligne%27s_conjecture_Manin_conf/"
            "Faltings_argument/Faltings.pdf"),
    "doi": "10.1007/BF01388432",
    "sha256": "0b7fb3e505d5d63e3e6c5913daf15bd843488e59f80f8d5176b154ac8faa3fc2",
    "inspected": ("Original 1983 paper, Section 2, Lemma 1, printed p.350; "
                  "pdftotext -layout splitlines 64-91, including statement and proof."),
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_evidence(fetch: bool) -> list[dict]:
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    graph = json.loads(gzip.decompress(packed))
    assert graph["repository"] == "jsmorph/rh" and graph["commit"] == REV
    entries = {row[0]: row for row in graph["modules"]}
    evidence = []
    for module, bounds in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        record = inspect_file({
            "repository": "jsmorph/rh", "commit": REV, "path": path,
            "git_blob_sha1": entries[module][1],
        }, offline=not fetch)
        raw = (ROOT / "build/source-cache/jsmorph/rh" / REV / path).read_bytes()
        lines = raw.splitlines()
        excerpts = []
        for lo, hi in bounds:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpt = b"\n".join(lines[lo-1:hi]) + b"\n"
            assert len(excerpt) <= 12000
            excerpts.append({"lines": [lo, hi], "sha256": sha(excerpt)})
        evidence.append({
            "module": module, "path": path, "sha256": record["sha256"],
            "git_blob_sha1": record["git_blob_sha1"], "inspected_excerpts": excerpts,
            "url": f"https://github.com/jsmorph/rh/blob/{REV}/{path}",
        })
    return evidence


def primary_evidence(fetch: bool) -> dict:
    path = ROOT / PRIMARY["path"]
    if not path.exists() and fetch:
        request = Request(PRIMARY["url"], headers={"User-Agent": "Mozilla/5.0"})
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(urlopen(request, timeout=45).read())
    assert sha(path.read_bytes()) == PRIMARY["sha256"]
    return PRIMARY


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true")
    args = parser.parse_args()
    result = {
        "status": "PASS",
        "automated_scope": "Immutable-source authentication, bounded excerpt hashes and primary PDF authentication only.",
        "independent_review": "certificates/frontier-progress-review-2026-11-22.json",
        "sources": source_evidence(args.fetch),
        "primary_reference": primary_evidence(args.fetch),
        "mathematical_results_for_separate_review": [
            "Properness extends the supplied generic point uniquely.",
            "Faltings's cited theorem extends the generic semiabelian group isomorphism and its inverse.",
            "The zero rigidification kills the vertical divisor of the given original-line isomorphism.",
            "The resulting integral isomorphism preserves coefficient actions and exact tangent eigenlattices.",
            "The generic component and original-line identification remain explicit inputs.",
        ],
        "artifacts": [{"path": path, "sha256": sha((ROOT/path).read_bytes())}
                      for path in ["notes/cm-integral-map-extension.md",
                                   "scripts/check_cm_integral_map_extension.py"]],
        "not_claimed": [
            "A new proof of Faltings's extension theorem",
            "Lean kernel replay or an automated geometric proof",
            "Construction of the actual arithmetic model or generic CM component point",
            "A generic isogeny replacing the required original-line isomorphism",
            "Completion of any RH or GRH proof-map node",
        ],
    }
    (ROOT / "certificates/cm-integral-map-extension.json").write_text(
        json.dumps(result, indent=2)+"\n")
    print("PASS: 5 pinned Lean contracts and Faltings's original PDF authenticated.")
    print("Scope: provenance only; mathematical proof reviewed separately, no Lean replay.")


if __name__ == "__main__":
    main()
