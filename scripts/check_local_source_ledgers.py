#!/usr/bin/env python3
"""Check cached source bytes and note tables against the pinned Git tree.

Example (the cache and tree JSON must be supplied separately):
  python3 scripts/check_local_source_ledgers.py \
    --cache-root /path/to/source-cache --tree-json /path/to/tree.json \
    --note notes/lsernau-discrete-series-suppliers.md \
    --output certificates/local-real-galois-integral-source-checks.json

This checks source integrity and attribution, not a Lean build or a theorem.
The optional LF repair is appropriate only for the documented fetch helper:
it removes one appended LF only if the resulting complete Git hash agrees.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re

REVISION = "72fead102f663d5c7a407964a13dc0cf9d977207"


def git_blob(data):
    prefix = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(prefix + data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-root", type=Path, required=True)
    parser.add_argument("--tree-json", type=Path, required=True)
    parser.add_argument("--note", type=Path, action="append", default=[])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--normalize-appended-lf", action="store_true")
    args = parser.parse_args()

    raw_tree = json.loads(args.tree_json.read_text())
    if raw_tree.get("truncated"):
        raise SystemExit("Refusing a truncated source tree.")
    tree = {
        item["path"]: item["sha"]
        for item in raw_tree["tree"]
        if item["type"] == "blob"
    }
    errors, sources, normalized = [], [], []
    for path in sorted(args.cache_root.rglob("*.lean")):
        relative = path.relative_to(args.cache_root).as_posix()
        expected = tree.get(relative)
        if expected is None:
            errors.append(f"Not in supplied tree: {relative}")
            continue
        data = path.read_bytes()
        actual = git_blob(data)
        if actual != expected and args.normalize_appended_lf:
            if data.endswith(b"\n") and git_blob(data[:-1]) == expected:
                data = data[:-1]
                path.write_bytes(data)
                actual = git_blob(data)
                normalized.append(relative)
        if actual != expected:
            errors.append(f"Source-byte mismatch: {relative}")
        else:
            sources.append(
                {"path": relative, "git_blob_sha1": actual, "bytes": len(data)}
            )

    checked = {row["path"] for row in sources}
    ledgers = []
    for note in args.note:
        hash_column = None
        for number, line in enumerate(note.read_text().splitlines(), start=1):
            if not line.startswith("|"):
                hash_column = None
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            headers = [cell.strip("`").lower() for cell in cells]
            hash_headers = {"blob", "blob sha", "git blob sha", "git blob sha-1"}
            columns = [i for i, cell in enumerate(headers) if cell in hash_headers]
            if columns:
                if len(columns) != 1:
                    errors.append(f"Ambiguous hash header: {note}:{number}")
                hash_column = columns[0]
                continue
            if hash_column is None:
                # A revision SHA inside a source URL is not a blob-ledger cell.
                continue
            if all(re.fullmatch(r":?-+:?", cell) for cell in cells):
                continue
            cell = cells[hash_column] if hash_column < len(cells) else ""
            match = re.fullmatch(r"`?([0-9a-f]{40})`?", cell)
            hashes = [match.group(1)] if match else []
            paths = re.findall(
                r"(?<![A-Za-z0-9_./])((?:\.\./)*[A-Za-z0-9_]"
                r"[A-Za-z0-9_./-]*\.lean)", line
            )
            if len(paths) != 1 or len(hashes) != 1:
                errors.append(f"Ambiguous source ledger: {note}:{number}")
                continue
            suffix = paths[0]
            while suffix.startswith("../"):
                suffix = suffix[3:]
            candidates = [
                path for path, sha in tree.items()
                if (path == suffix or path.endswith("/" + suffix))
                and sha == hashes[0]
            ]
            if len(candidates) != 1:
                source = paths[0]
                errors.append(f"Ledger/tree mismatch: {note}:{number}: {source}")
                continue
            source = candidates[0]
            if source not in checked:
                errors.append(f"Ledger source not byte-verified: {source}")
            else:
                ledgers.append(
                    {
                        "note": note.as_posix(),
                        "line": number,
                        "path": source,
                        "git_blob_sha1": hashes[0],
                    }
                )

    result = {
        "schema_version": 2,
        "source_repository": "lsernau/grh-lean",
        "revision": REVISION,
        "supplied_git_tree_sha": raw_tree.get("sha"),
        "verification": "Full Git blob SHA-1 of bytes equals the supplied tree entry. Each row in the selected notes' tables with a Blob or Git blob SHA column identifies exactly one pinned tree entry by path suffix and SHA, and that source is byte-verified. Revision SHAs inside ordinary source links are not blob-ledger entries.",
        "scope": "Integrity and attribution only. The caller supplies the tree for the pinned revision. No Lean replay or mathematical theorem verification.",
        "normalization": "Optional removal of exactly one final LF, only when the corrected full Git blob hash matches the tree.",
        "normalized_files_this_run": normalized,
        "verified_source_count": len(sources),
        "verified_ledger_rows": len(ledgers),
        "sources": sources,
        "ledgers": ledgers,
        "errors": errors,
        "status": "passed" if not errors else "failed",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in
                      ("status", "verified_source_count",
                       "verified_ledger_rows", "errors")}, indent=2))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
