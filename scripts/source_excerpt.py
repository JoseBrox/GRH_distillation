#!/usr/bin/env python3
"""Search or read one hash-verified source without printing the complete file.

Examples:
  python scripts/source_excerpt.py --source Main.lean --search theorem
  python scripts/source_excerpt.py --source lean/src/Main.lean --lines 1:12

Sources are selected from sources/manifest.json unless --manifest is supplied.
A manifest has a `files` list with repository, commit, path and git_blob_sha1.
Missing selected files are downloaded into the ignored local source cache.
No mathematical verification or compilation is implied by byte verification.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

from check_sources import ROOT, inspect_file

MAX_LINES = 120
MAX_BYTES = 12000
MAX_MATCHES = 25


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=ROOT / "sources/manifest.json")
    parser.add_argument("--source", required=True, help="Exact path, or unique path suffix")
    parser.add_argument("--repository", help="Disambiguate identical paths across repositories")
    parser.add_argument("--offline", action="store_true", help="Require an already cached file")
    query = parser.add_mutually_exclusive_group(required=True)
    query.add_argument("--search", help="Literal declaration name or other literal text")
    query.add_argument("--lines", help="Inclusive one-based range START:END (at most 120 lines)")
    args = parser.parse_args()

    if args.search is not None and not args.search:
        parser.error("--search must not be empty")
    start = end = None
    if args.lines is not None:
        if not re.fullmatch(r"[1-9][0-9]*:[1-9][0-9]*", args.lines):
            parser.error("--lines must be an inclusive range such as 30:80")
        start, end = map(int, args.lines.split(":"))
        if end < start or end - start + 1 > MAX_LINES:
            parser.error("Request an ordered range of at most 120 lines")

    manifest = json.loads(args.manifest.read_text())
    entries = [item for item in manifest["files"]
               if (not args.repository or item["repository"] == args.repository)]
    exact = [item for item in entries if item["path"] == args.source]
    matches = exact or [item for item in entries if item["path"].endswith("/" + args.source)]
    if len(matches) != 1:
        names = [item["repository"] + ":" + item["path"] for item in matches[:MAX_MATCHES]]
        raise ValueError(f"Expected one source, found {len(matches)}; candidates: {names}")
    item = matches[0]
    # Source identifiers become paths and URLs. Reject traversal and unpinned refs.
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", item["repository"]):
        raise ValueError("Expected a repository in owner/name form")
    if any(part in (".", "..") for part in item["repository"].split("/")):
        raise ValueError("Invalid repository path")
    if not re.fullmatch(r"[0-9a-fA-F]{40}", item["commit"]):
        raise ValueError("Use a pinned full commit hash")
    record = inspect_file(item, args.offline)
    cache = ROOT / "build/source-cache" / item["repository"] / item["commit"] / item["path"]
    lines = cache.read_text().splitlines()

    if args.search is not None:
        if shutil.which("rg"):
            result = subprocess.run(["rg", "--fixed-strings", "--line-number", "--no-heading",
                                     "--max-count", str(MAX_MATCHES + 1), "--", args.search,
                                     str(cache)], text=True, capture_output=True)
            if result.returncode not in (0, 1):
                raise RuntimeError(result.stderr.strip())
            found = result.stdout.splitlines()
        else:
            found = []
            for number, line in enumerate(lines, 1):
                if args.search in line:
                    found.append(f"{number}:{line}")
                    if len(found) > MAX_MATCHES:
                        break
        truncated = len(found) > MAX_MATCHES
        output = "\n".join(line[:300] + (" [line shortened]" if len(line) > 300 else "")
                           for line in found[:MAX_MATCHES])
        if truncated:
            output += "\n[More matches exist; narrow --search.]"
        if not found:
            output = "[No literal matches.]"
    else:
        if start > len(lines) or end > len(lines):
            raise ValueError(f"Source has {len(lines)} lines; choose a range within it")
        output = "\n".join(f"{number}: {lines[number - 1]}" for number in range(start, end + 1))
        if len(output.encode("utf-8")) > MAX_BYTES:
            raise ValueError("Excerpt exceeds 12,000 bytes; request a narrower range")

    print(json.dumps({"repository": item["repository"], "commit": item["commit"],
                      "path": item["path"], "sha256": record["sha256"],
                      "git_blob_sha1": record["git_blob_sha1"], "lines": len(lines),
                      "scope": "Pinned source bytes verified; no proof or build claim."}))
    print(output)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError, KeyError) as error:
        print(f"Bounded source read failed: {error}", file=sys.stderr)
        raise SystemExit(1)
