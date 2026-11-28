#!/usr/bin/env python3
"""Authenticate the source ledgers for five ordinary proof suppliers.

This checks exact source bytes, not Lean elaboration or mathematical truth.
With --offline, every listed source and reference must already be cached.
Without it, missing files are fetched from the pinned URLs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REVISION = "72fead102f663d5c7a407964a13dc0cf9d977207"
CACHE = ROOT / "build/source-cache/lsernau/grh-lean" / REVISION / "grh/src"
NOTES = [
    "notes/lsernau-sharp-scalar-couplings.md",
    "notes/lsernau-good-form-multiplicities.md",
    "notes/lsernau-finite-good-type-density.md",
    "notes/lsernau-rank-two-period-arithmetic.md",
    "notes/lsernau-bounded-class-crystalline-loss.md",
]
REFERENCES = [
    ("build/references/harris-labesse.pdf",
     "https://webusers.imj-prg.fr/~michael.harris/harlab.pdf",
     "ad415daf2d3c7faa317c6d9957cca191557f70df25fea69dffb8fd59774e3610"),
    ("build/crystalline-uniformity-reference/liu-fontaine-2007.pdf",
     "https://www.numdam.org/item/10.1016/j.ansens.2007.05.002.pdf",
     "ecc6310bf65dc53ee043878631a450403d8e78631dbf40d3f79ec1ad27f2218a"),
]


def read_cached(path: Path, url: str, offline: bool) -> bytes:
    if path.is_file():
        return path.read_bytes()
    if offline:
        raise FileNotFoundError(f"Missing offline cache: {path.relative_to(ROOT)}")
    request = Request(url, headers={"User-Agent": "GRH-distillation-source-check/1"})
    with urlopen(request, timeout=45) as response:
        data = response.read()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    expected = {}
    notes = []
    pattern = re.compile(r"\|\s*`?((?:New|Lib)/[^|`\n]+?\.lean)`?\s*\|[^\n]*?\b([0-9a-f]{40})\b")
    for name in NOTES:
        data = (ROOT/name).read_bytes()
        rows = pattern.findall(data.decode())
        if not rows:
            raise ValueError(f"No source ledger found: {name}")
        for path, blob in rows:
            if path in expected and expected[path] != blob:
                raise ValueError(f"Conflicting hashes: {path}")
            expected[path] = blob
        notes.append({"path": name, "sha256": hashlib.sha256(data).hexdigest(),
                      "ledger_rows": len(rows)})
    files = []
    for name, blob in sorted(expected.items()):
        url = f"https://raw.githubusercontent.com/lsernau/grh-lean/{REVISION}/grh/src/{name}"
        data = read_cached(CACHE/name, url, args.offline)
        actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if actual != blob:
            raise ValueError(f"Pinned source mismatch: {name}: {actual} != {blob}")
        files.append({"path": "grh/src/"+name, "git_blob_sha1": actual,
                      "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
    references = []
    for path, url, expected_sha in REFERENCES:
        data = read_cached(ROOT/path, url, args.offline)
        actual = hashlib.sha256(data).hexdigest()
        if actual != expected_sha:
            raise ValueError(f"Classical-reference checksum mismatch: {url}")
        references.append({"url": url, "sha256": actual, "bytes": len(data)})
    record = {"status": "passed", "source_revision": REVISION,
              "scope": "Source-ledger and classical-reference bytes only; no Lean replay or mathematical-proof certification.",
              "notes": notes, "source_files": files, "classical_references": references}
    output = ROOT/"certificates/supplier-closure-source-checks.json"
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(f"Verified {sum(n['ledger_rows'] for n in notes)} ledger rows, "
          f"{len(files)} distinct source blobs and {len(references)} primary PDFs.")
    print(output.relative_to(ROOT))


if __name__ == "__main__":
    main()
