#!/usr/bin/env python3
"""Verify the bytes of the selected, pinned source files.

This checks provenance of the listed files, not any mathematical proof or Lean
build. Downloaded third-party files stay in build/source-cache (gitignored).
Only Python's standard library is required.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.request import Request, urlopen
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]


def git_blob_hash(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def inspect_file(item: dict, offline: bool) -> dict:
    relative = Path(item["path"])
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"Invalid source path: {relative}")
    cache = ROOT / "build/source-cache" / item["repository"] / item["commit"] / relative
    if cache.is_file():
        data = cache.read_bytes()
    elif offline:
        raise FileNotFoundError(f"Not cached: {relative}")
    else:
        url = (f"https://raw.githubusercontent.com/{item['repository']}/"
               f"{item['commit']}/{quote(item['path'], safe='/')}")
        request = Request(url, headers={"User-Agent": "GRH-distillation-source-check/1"})
        with urlopen(request, timeout=45) as response:
            data = response.read()
        # Do not cache a response until its expected identity has been checked.
        actual = git_blob_hash(data)
        if actual != item["git_blob_sha1"]:
            raise ValueError(f"Blob mismatch for {relative}: {actual}")
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_bytes(data)
    actual = git_blob_hash(data)
    if actual != item["git_blob_sha1"]:
        raise ValueError(f"Cached blob mismatch for {relative}: {actual}")
    result = {
        "repository": item["repository"],
        "commit": item["commit"],
        "path": item["path"],
        "bytes": len(data),
        "git_blob_sha1": actual,
        "sha256": hashlib.sha256(data).hexdigest(),
        "matches_pinned_blob": True,
    }
    if relative.suffix == ".lean":
        text = data.decode("utf-8")
        result["lines"] = len(text.splitlines())
        result["imports_on_single_lines"] = [
            line.strip()[7:] for line in text.splitlines()
            if line.strip().startswith("import ")
        ]
        # This is deliberately a lexical inventory, not a parser or axiom audit.
        words = r"\b(?:sorry|admit|sorryAx|native_decide|implemented_by|axiom)\b"
        result["lexical_hits_including_comments"] = [
            {"line": i, "tokens": re.findall(words, line)}
            for i, line in enumerate(text.splitlines(), 1) if re.search(words, line)
        ]
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true", help="Read only cached bytes")
    parser.add_argument("--output", type=Path, help="Write JSON to this path")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "sources/manifest.json").read_text())
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(lambda item: inspect_file(item, args.offline), manifest["files"]))
    certificate = {
        "schema_version": 1,
        "claim": "The listed file bytes match their pinned Git blob hashes.",
        "limits": [
            "Selected files only; not the complete source dependency graph.",
            "No Lean compilation, kernel check, or axiom-dependency audit.",
            "Lexical hits include comments and do not decide proof validity.",
            "Mirror-file checks do not authenticate the original author's archive.",
        ],
        "files_checked": len(results),
        "lean_files_checked": sum(r["path"].endswith(".lean") for r in results),
        "files": results,
    }
    output = json.dumps(certificate, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
        print(f"Verified {len(results)} pinned files; wrote {args.output}.")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        print(f"Source verification failed: {error}", file=sys.stderr)
        raise SystemExit(1)
