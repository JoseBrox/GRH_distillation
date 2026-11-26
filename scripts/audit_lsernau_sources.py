#!/usr/bin/env python3
"""Reproduce the static inventory of the pinned lsernau/grh-lean source.

This is a lexical/import inventory, not a Lean parser or a kernel checker.
Run: python scripts/audit_lsernau_sources.py /path/to/grh-lean --output audit.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

PIN = "72fead102f663d5c7a407964a13dc0cf9d977207"
MIT_MANIFEST_SHA256 = "cd537287df9d0580afa93fcf7237370967520295f38075805964e4d4bbb9f1f8"
WATCH = re.compile(
    r"\b(?:axiom|sorry|admit|unsafe|opaque|implemented_by|extern|native_decide|"
    r"ofReduceBool|sorryAx|run_meta|run_elab|run_tac|addDecl|addAndCompile|"
    r"setEnv|modifyEnv|initialize|builtin_initialize|syntax|macro|elab)\b"
)


def code_only(text: str) -> str:
    """Blank nested Lean comments and quoted strings, preserving line positions."""
    out = list(text)
    i, depth = 0, 0
    while i < len(text):
        if depth:
            if text.startswith("/-", i):
                out[i : i + 2] = "  "
                depth += 1
                i += 2
            elif text.startswith("-/", i):
                out[i : i + 2] = "  "
                depth -= 1
                i += 2
            else:
                if text[i] != "\n":
                    out[i] = " "
                i += 1
        elif text.startswith("/-", i):
            out[i : i + 2] = "  "
            depth = 1
            i += 2
        elif text.startswith("--", i):
            end = text.find("\n", i)
            if end == -1:
                end = len(text)
            out[i:end] = " " * (end - i)
            i = end
        elif text[i] == '"':
            out[i] = " "
            i += 1
            while i < len(text):
                if text[i] == "\\":
                    for j in range(i, min(i + 2, len(text))):
                        if text[j] != "\n":
                            out[j] = " "
                    i += 2
                elif text[i] == '"':
                    out[i] = " "
                    i += 1
                    break
                else:
                    if text[i] != "\n":
                        out[i] = " "
                    i += 1
        else:
            i += 1
    if depth:
        raise ValueError("unclosed comment")
    return "".join(out)


def imports(code: str) -> list[str]:
    answer = []
    for line in code.splitlines():
        m = re.match(r"\s*(?:public\s+)?import\s+(.+)$", line)
        if m:
            answer.extend(m[1].split())
    return answer


def file_record(path: Path, root: Path) -> dict:
    data = path.read_bytes()
    return {
        "path": path.relative_to(root).as_posix(),
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "lines": len(data.splitlines()),
    }


def compare_published_manifest(root: Path, path: Path) -> dict:
    """Compare the MIT source manifest captured on 2026-11-26 with this checkout."""
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != MIT_MANIFEST_SHA256:
        raise SystemExit(f"published manifest hash changed: {digest}")
    entries = {}
    for line in data.decode().splitlines():
        expected, name = line.split(None, 1)
        name = name.removeprefix("*")
        source = (root / name).resolve()
        if Path(name).is_absolute() or not source.is_relative_to(root):
            raise SystemExit(f"unsafe source-manifest path: {name}")
        if name in entries or not re.fullmatch(r"[0-9a-f]{64}", expected):
            raise SystemExit("invalid or duplicate source-manifest entry")
        if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != expected:
            raise SystemExit(f"source-manifest mismatch: {name}")
        entries[name] = expected
    tracked = set(subprocess.check_output(
        ["git", "-C", str(root), "ls-files"], text=True).splitlines())
    return {
        "url": "https://math.mit.edu/~drew/shortgrh/source-files.sha256",
        "sha256": digest,
        "entries": len(entries), "matched": len(entries),
        "mismatches": [],
        "tracked_files_not_in_manifest": sorted(tracked - entries.keys()),
        "manifest_files_not_tracked": sorted(entries.keys() - tracked),
    }


def inspect(root: Path, edition: str) -> dict:
    folder = root / edition
    files = sorted((folder / "src").rglob("*.lean"))
    mods = {p.relative_to(folder / "src").with_suffix("").as_posix().replace("/", "."): p
            for p in files}
    graph, tokens, code_lines, raw_lines = {}, [], 0, 0
    lib_to_new = []
    options = set()
    for mod, path in mods.items():
        raw = path.read_text()
        code = code_only(raw)
        raw_lines += len(raw.splitlines())
        code_lines += sum(bool(line.strip()) for line in code.splitlines())
        graph[mod] = imports(code)
        for match in WATCH.finditer(code):
            tokens.append({"path": path.relative_to(root).as_posix(),
                           "line": code[:match.start()].count("\n") + 1,
                           "token": match[0]})
        if mod.startswith("Lib."):
            lib_to_new.extend((mod, dest) for dest in graph[mod] if dest.startswith("New."))
        options.update(re.findall(r"\bset_option\s+([\w.]+)", code))
    seen, pending = set(), ["Main"]
    extern = set()
    while pending:
        mod = pending.pop()
        if mod in seen:
            continue
        if mod not in graph:
            extern.add(mod)
            continue
        seen.add(mod)
        pending.extend(graph[mod])
    manifest = json.loads((folder / "lake-manifest.json").read_text())
    key_paths = ["src/Statements.lean", "src/Main.lean", "src/New/Main.lean",
                 "src/Lib/Speed.lean", "src/Lib/General/LinearAlgebra/Base.lean",
                 "lean-toolchain", "lakefile.toml",
                 "lake-manifest.json", "scripts/PrintAxioms.lean", "Challenge.lean",
                 "comparator.json", "README.md"]
    return {
        "source_files": len(files), "source_lines": raw_lines,
        "nonblank_code_lines_lexical": code_lines,
        "watched_tokens_in_production_source": tokens,
        "local_modules_reachable_from_Main": len(seen),
        "source_modules_outside_Main_import_closure": sorted(set(mods) - seen),
        "external_imports_from_Main": sorted(extern),
        "Lib_imports_of_New": lib_to_new,
        "Challenge_imported_by_production": any("Challenge" in v for v in graph.values()),
        "Statements_imports": graph["Statements"],
        "set_option_names": sorted(options),
        "toolchain": (folder / "lean-toolchain").read_text().strip(),
        "packages": [{k: package[k] for k in ("name", "url", "rev")}
                     for package in manifest["packages"]],
        "key_files": [file_record(folder / name, root) for name in key_paths
                      if (folder / name).exists()],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--source-manifest", type=Path,
                        help="Optional MIT source-files.sha256; its captured hash is pinned.")
    args = parser.parse_args()
    root = args.source.resolve()
    revision = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    if revision != PIN:
        raise SystemExit(f"wrong source revision: {revision}; expected {PIN}")
    dirty = subprocess.check_output(["git", "-C", str(root), "status", "--porcelain", "--untracked-files=no"], text=True)
    if dirty:
        raise SystemExit("source has tracked modifications; refusing pinned inventory")
    result = {"source": "https://github.com/lsernau/grh-lean", "revision": revision,
              "scope": "Static lexical and import inventory; no Lean elaboration or kernel replay.",
              "editions": {name: inspect(root, name) for name in ("grh", "grh-compact")},
              "identical_statement_files": (root / "grh/src/Statements.lean").read_bytes()
              == (root / "grh-compact/src/Statements.lean").read_bytes()}
    if args.source_manifest:
        result["published_source_manifest"] = compare_published_manifest(root, args.source_manifest)
    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
