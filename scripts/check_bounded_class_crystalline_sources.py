#!/usr/bin/env python3
"""Verify the pinned sources for the bounded-class crystalline-loss theorem.

This is a provenance check, not a proof of the theorem or a numerical
evaluation of its non-effective constant. Downloads stay in ignored build/.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
REV = "72fead102f663d5c7a407964a13dc0cf9d977207"
SOURCE = ROOT / "build/source-cache/lsernau/grh-lean" / REV / "grh/src"
ROWS = [
    ("New/Congruences/FirstOrder/RibetElement.lean",
     "7d1087d880d58b22825fddb422ab5a097a1d7734", [[147, 186], [203, 269]]),
    ("New/Congruences/LocalLoss/CrystallineDefect.lean",
     "c21212f774df81bff52003cbf8c6bf42ee2d7e95", [[383, 404]]),
    ("New/Congruences/Lifting/CupOrthogonalityBounds.lean",
     "33ff1d8099302c487eb2621acac93ce54a04dc4b", [[532, 566]]),
]
PDF_URL = "https://www.numdam.org/item/10.1016/j.ansens.2007.05.002.pdf"
PDF_SHA = "ecc6310bf65dc53ee043878631a450403d8e78631dbf40d3f79ec1ad27f2218a"


def read_or_download(path: Path, url: str) -> bytes:
    if path.is_file():
        return path.read_bytes()
    request = Request(url, headers={"User-Agent": "GRH-distillation-source-check/1"})
    with urlopen(request, timeout=45) as response:
        data = response.read()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def main() -> None:
    records = []
    for name, expected, ranges in ROWS:
        url = f"https://raw.githubusercontent.com/lsernau/grh-lean/{REV}/grh/src/{name}"
        data = read_or_download(SOURCE / name, url)
        actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if actual != expected:
            raise ValueError(f"Pinned source mismatch: {name}")
        line_count = len(data.splitlines())
        if not all(1 <= start <= end <= line_count for start, end in ranges):
            raise ValueError(f"Invalid recorded excerpt: {name}")
        records.append({"path": "grh/src/" + name, "git_blob_sha1": actual,
                        "sha256": hashlib.sha256(data).hexdigest(), "lines": line_count,
                        "inspected_ranges": ranges})
    pdf_path = ROOT / "build/crystalline-uniformity-reference/liu-fontaine-2007.pdf"
    pdf = read_or_download(pdf_path, PDF_URL)
    if hashlib.sha256(pdf).hexdigest() != PDF_SHA:
        raise ValueError("Published Liu reference differs from the recorded PDF")
    record = {
        "scope": "Pinned source and published reference bytes only; ordinary proof is in the note.",
        "note": "notes/lsernau-bounded-class-crystalline-loss.md",
        "source_revision": REV,
        "source_files": records,
        "classical_reference": {"author": "Tong Liu", "year": 2007,
            "doi": "10.1016/j.ansens.2007.05.002", "url": PDF_URL,
            "sha256": PDF_SHA, "statement_printed_page": 633,
            "crystalline_proof_printed_pages": [669, 671],
            "prime_two_proof_printed_pages": [672, 673]},
        "proof_scope": [
            "One finite actual crystalline-obstruction module for fixed K, L, target and weight interval.",
            "Uniform over all auxiliary families, their ranks and precision.",
            "Normalized bound persists under finite coefficient extension of the fixed target.",
        ],
        "limits": [
            "No numerical value of the finite obstruction length is computed.",
            "No bound as original fields, target representations and weights grow.",
            "No new Lean build, replay, or numerical automorphic Galois matrix check.",
            "Source-byte verification does not establish the mathematical proof.",
        ],
    }
    output = ROOT / "certificates/bounded-class-crystalline-loss-sources.json"
    output.write_text(json.dumps(record, indent=2) + "\n")
    print("Verified 3 pinned Lean source blobs and Liu's published PDF; no numerical loss claim.")


if __name__ == "__main__":
    main()
