#!/usr/bin/env python3
"""Verify the recorded structural-simplification snapshot, not its mathematics.

Run the individual scripts listed in the review to reproduce the exact
algebraic checks. This verifier detects stale proof, checker and PDF hashes
and broken local links in the active dependency documents.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "certificates/structural-simplification-review.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    report = json.loads(REVIEW.read_text())
    records = report["artifacts"]
    assert len({r["path"] for r in records}) == len(records)
    for record in records:
        path = ROOT / record["path"]
        assert path.is_file(), record["path"]
        assert digest(path) == record["sha256"], f"Changed: {record['path']}"
    for name in ("rh", "grh", "guide"):
        build = json.loads((ROOT / f"certificates/{name}-build.json").read_text())
        for record in build["sources"] + [build["output"]]:
            assert digest(ROOT / record["path"]) == record["sha256"], record["path"]
        assert build["page_count"] == report["manuscript_pages"][name]
    assert (ROOT / "paper/main.pdf").read_bytes() == (ROOT / "paper/grh/main.pdf").read_bytes()
    assert len((ROOT / "notes/current-state.md").read_text().splitlines()) < 200
    links = 0
    for relative in report["link_checked_documents"]:
        path = ROOT / relative
        content = path.read_text()
        if path.suffix == ".tex":
            targets = [(ROOT, x) for x in re.findall(r"\\prooflink\{([^}]+)\}", content)]
        else:
            targets = [(path.parent, x) for x in re.findall(r"\]\(([^\s)]+)\)", content)
                       if not re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", x)]
        for base, target in targets:
            filename = target.split("#", 1)[0]
            if filename:
                assert (base / filename).is_file(), (relative, target)
                links += 1
    print(json.dumps({"status": "snapshot hashes and local links passed",
                      "artifacts": len(records), "links": links,
                      "manuscript_pages": report["manuscript_pages"],
                      "limits": "No theorem proof or Lean replay is certified."}))


if __name__ == "__main__":
    main()
