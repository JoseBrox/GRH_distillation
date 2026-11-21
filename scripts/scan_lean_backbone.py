#!/usr/bin/env python3
"""Verify and index the complete pinned local Lean source import graph.

Large source and graph data stay local or in a compressed repository artifact.
This is an import inventory, never a theorem dependency or kernel certificate.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict, deque
import gzip
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PIN = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
EXTERNAL_ROOTS = {"Aesop", "Batteries", "Cli", "ImportGraph", "Init", "Lake",
                  "Lean", "LeanSearchClient", "Mathlib", "Plausible",
                  "ProofWidgets", "Qq", "Std"}
IMPORT = re.compile(r"^(?:public\s+)?import\s+(?:all\s+)?(.+?)\s*$")


def git(mirror: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(mirror), *args])


def header_imports(data: bytes) -> tuple[list[str], list[str]]:
    """Parse the import header, respecting nested block and line comments.

    Lean permits imports only in the module header. Stop at its first ordinary
    command; mathematical strings and comments in the body are never imports.
    """
    imports, unsupported = [], []
    depth = 0
    for raw in data.decode("utf-8-sig").splitlines():
        clean, at = [], 0
        while at < len(raw):
            if raw.startswith("/-", at):
                depth += 1
                at += 2
            elif depth and raw.startswith("-/", at):
                depth -= 1
                at += 2
            elif not depth and raw.startswith("--", at):
                break
            elif depth:
                at += 1
            else:
                clean.append(raw[at])
                at += 1
        line = "".join(clean).strip()
        if not line or line in {"prelude", "module"}:
            continue
        m = IMPORT.fullmatch(line)
        if m:
            names = m[1].split()
            if not all(re.fullmatch(r"[\w'.]+", name) for name in names):
                unsupported.append(line)
            imports.extend(names)
        else:
            if "import" in line.split()[:2]:
                unsupported.append(line)
            break
    return imports, unsupported


def scan(mirror: Path) -> dict:
    assert git(mirror, "rev-parse", "HEAD").decode().strip() == PIN
    tree = git(mirror, "ls-tree", "-r", "-z", "--full-tree", PIN, "lean/src")
    sources = []
    for line in tree.decode().split("\0"):
        if not line:
            continue
        meta, path = line.split("\t", 1)
        mode, kind, blob = meta.split()
        if not path.endswith(".lean"):
            raise ValueError("Unexpected source entry: " + path)
        assert mode == "100644" and kind == "blob"
        name = path.removeprefix("lean/src/").removesuffix(".lean").replace("/", ".")
        sources.append((name, path, blob))
    sources.sort()
    ids = {name: i for i, (name, _, _) in enumerate(sources)}
    rows, all_imports, unknown, unsupported = [], [], [], []
    content_digest = hashlib.sha256()
    total_bytes = total_lines = import_occurrences = 0
    for number, (name, path, blob) in enumerate(sources):
        data = (mirror / path).read_bytes()
        actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if actual != blob:
            raise ValueError("Source byte mismatch: " + path)
        content_digest.update(path.encode() + b"\0" + hashlib.sha256(data).digest())
        imports, bad = header_imports(data)
        unsupported.extend({"module": name, "line": x} for x in bad)
        unknown.extend({"module": name, "import": x} for x in imports
                       if x not in ids and x.split(".")[0] not in EXTERNAL_ROOTS)
        local = sorted({ids[x] for x in imports if x in ids})
        external = sorted({x for x in imports if x not in ids})
        rows.append([name, blob, len(data), data.count(b"\n"), local, external])
        all_imports.append(local)
        total_bytes += len(data)
        total_lines += data.count(b"\n")
        import_occurrences += len(imports)
    if unknown or unsupported:
        target = ROOT / "build/lean-import-parser-issues.json"
        target.write_text(json.dumps({"unknown": unknown, "unsupported": unsupported}, indent=2))
        raise ValueError(f"Unresolved import syntax or root; inspect {target}")

    reverse = [[] for _ in rows]
    remaining = [len(x) for x in all_imports]
    for node, deps in enumerate(all_imports):
        for dep in deps:
            reverse[dep].append(node)
    queue = deque(i for i, n in enumerate(remaining) if n == 0)
    depth, ordered = [1] * len(rows), []
    while queue:
        node = queue.popleft()
        ordered.append(node)
        for caller in reverse[node]:
            depth[caller] = max(depth[caller], depth[node] + 1)
            remaining[caller] -= 1
            if remaining[caller] == 0:
                queue.append(caller)
    if len(ordered) != len(rows):
        raise ValueError("Import cycle or cycle-dependent source modules")
    reached, queue = set(), [ids["Main"]]
    while queue:
        node = queue.pop()
        if node not in reached:
            reached.add(node)
            queue.extend(all_imports[node])
    groups = Counter(".".join(row[0].split(".")[:2]) for row in rows)
    root_groups = Counter(row[0].split(".")[0] for row in rows)
    external = sorted({x for row in rows for x in row[5]})
    edges_by_group = Counter()
    for node, deps in enumerate(all_imports):
        a = ".".join(rows[node][0].split(".")[:2])
        for dep in deps:
            b = ".".join(rows[dep][0].split(".")[:2])
            if a != b:
                edges_by_group[a, b] += 1
    graph = {
        "schema_version": 1, "repository": "jsmorph/rh", "commit": PIN,
        "scope": "All local Lean source imports; not term-level proof dependencies. External package internals are boundary nodes, not inventoried here.",
        "module_fields": ["name", "git_blob_sha1", "bytes", "newlines", "local_import_ids", "external_import_names"],
        "module_ids": "Zero-based positions in the modules array, ordered by full module name.",
        "modules": rows,
    }
    target = ROOT / "blueprint/lean-source-imports.json.gz"
    raw = json.dumps(graph, ensure_ascii=False, separators=(",", ":")).encode()
    target.write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))
    report = {
        "schema_version": 1, "repository": graph["repository"], "commit": PIN,
        "source_tree_sha1": git(mirror, "rev-parse", PIN + ":lean/src").decode().strip(),
        "scope": graph["scope"], "verification": "Every indexed checkout file recomputed as a Git blob and matched against the pinned source tree. Header parser accepts nested comments; all import endpoints classified. DAG and Main reachability recomputed locally.",
        "local_modules": len(rows), "source_bytes": total_bytes, "newlines": total_lines,
        "source_content_sha256": content_digest.hexdigest(),
        "import_occurrences": import_occurrences,
        "unique_local_import_edges": sum(len(x) for x in all_imports),
        "external_import_names": external,
        "unknown_imports": 0, "unsupported_import_headers": 0,
        "acyclic": True, "main_reachable_modules": len(reached),
        "unreachable_modules": [rows[i][0] for i in range(len(rows)) if i not in reached],
        "main_import_depth_including_main": depth[ids["Main"]],
        "root_groups": dict(sorted(root_groups.items())),
        "subject_groups": dict(sorted(groups.items())),
        "cross_subject_import_edges": [[a, b, count] for (a, b), count in sorted(edges_by_group.items())],
        "compressed_graph": {"path": str(target.relative_to(ROOT)), "bytes": target.stat().st_size,
                             "sha256": hashlib.sha256(target.read_bytes()).hexdigest()},
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "limits": ["Imports can include unused theorems; all-source reachability does not show every declaration is needed by the five target proofs.",
                   "External Mathlib and compiler/package declarations are not traversed.",
                   "No Lean build, kernel replay, theorem-type comparison or full mathematical verification is performed by this script."]}
    out = ROOT / "certificates/lean-source-inventory.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    return {k: report[k] for k in ["local_modules", "source_bytes", "unique_local_import_edges",
                                  "main_reachable_modules", "main_import_depth_including_main", "acyclic"]}


def query(module: str) -> None:
    graph = json.loads(gzip.decompress((ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()))
    rows = graph["modules"]
    matches = [row for row in rows if row[0] == module]
    if len(matches) != 1:
        raise ValueError("Use one exact full module name")
    row = matches[0]
    print(json.dumps({"module": row[0], "git_blob_sha1": row[1], "bytes": row[2],
                      "local_imports": [rows[i][0] for i in row[4]][:30],
                      "local_import_count": len(row[4]), "external_imports": row[5][:30]}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mirror", type=Path, default=ROOT / "build/lean-mirror")
    parser.add_argument("--module", help="Query one exact module in the stored graph instead of rescanning")
    args = parser.parse_args()
    if args.module:
        query(args.module)
    else:
        print(json.dumps(scan(args.mirror)))
