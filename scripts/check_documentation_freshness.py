#!/usr/bin/env python3
"""Sanity-check current documentation pointers and historical labels.

This checks navigation, not mathematical correctness or complete staleness.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HISTORICAL = ["notes/arithmetic-supplier-continuation-2026-11-22.md","notes/arithmetic-frontier-continuation-2026-11-22.md","notes/project-assessment.md","notes/recovery-crosswalk.md"]
LATER_NOTES = ["notes/geometry-bergman-continuation-upper.md","notes/geometry-bergman-continuation-thick.md","notes/geometry-bergman-continuation-thin.md","notes/selmer-support-continuation-type-one-rigidity.md","notes/selmer-support-continuation-relative-presentation.md","notes/global-gram-continuation-degenerate-fibres.md","notes/geometry-section-continuation.md","notes/geometry-point-continuation.md","notes/geometry-arithmetic-frontier-integral-pel.md","notes/geometry-arithmetic-frontier-discriminant-clearing.md"]

def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")

def check_links(path: str, section: str) -> int:
    count = 0
    for dest in re.findall(r"\]\(([^)]+)\)", section):
        dest = dest.split("#", 1)[0]
        if not dest or "://" in dest or dest.startswith("mailto:"):
            continue
        if not ((ROOT / path).parent / dest).exists():
            raise AssertionError(f"{path}: broken link {dest}")
        count += 1
    return count

def main() -> None:
    state = read("notes/current-state.md")
    assert "not yet proved" in state.lower(), "missing proof-status disclaimer"
    assert (ROOT / "notes/open-frontier-theorems.md").is_file()
    progress = read("blueprint/progress.md")
    for key in ("rh", "grh"):
        data = json.loads(read(f"blueprint/{key}/status.json"))
        assert f"**{data['finished']}/{data['total']}**" in progress, key
    count = 0
    for path in ("results/README.md", "certificates/README.md"):
        text = read(path)
        marker = "## Current navigation:"
        assert marker in text, path
        live = text.split(marker, 1)[1].split("\n## ", 1)[0]
        count += check_links(path, live)
        assert "historical" in text.lower(), path
    for path in HISTORICAL:
        banner = "\n".join(read(path).splitlines()[:9])
        assert "**Historical " in banner, path
        count += check_links(path, banner)
    for path in LATER_NOTES:
        banner = "\n".join(read(path).splitlines()[:9])
        assert "**Later status (23 November 2026).**" in banner, path
        count += check_links(path, banner)
    print(f"PASS: 2 current indices, {len(HISTORICAL)} historical checkpoints, "
          f"{len(LATER_NOTES)} later-status notes; {count} local links checked.")

if __name__ == "__main__":
    main()
