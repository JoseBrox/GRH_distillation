#!/usr/bin/env python3
"""Check the current frontier review and its integrated deliverables.

This verifies artifact identity and publication consistency. It does not
prove the mathematics or replay Lean. Earlier integration records describe
their historical Git snapshots and are not rewritten by this check.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INTEGRATION = "certificates/frontier-progress-integration-2026-11-22.json"
REVIEW = "certificates/frontier-progress-review-2026-11-22.json"


def read(path):
    return json.loads((ROOT / path).read_text())


def records(value):
    if isinstance(value, dict):
        if "path" in value and "sha256" in value:
            yield value
        for child in value.values():
            yield from records(child)
    elif isinstance(value, list):
        for child in value:
            yield from records(child)


def main():
    integration, review = read(INTEGRATION), read(REVIEW)
    assert all(p["status"] == "PASS" for p in review["packages"])
    ids = [p["id"] for p in review["packages"]]
    assert len(ids) == len(set(ids))
    assert integration["proof_package_ids"] == ids
    assert integration["node_counts"] == review["node_counts"]
    assert integration["new_existing_nodes_completed"] == 0
    progress = read("blueprint/progress.json")
    for route, key in [("rh", "rh"), ("grh", "technical")]:
        actual = progress["maps"][key]
        assert review["node_counts"][route] == {
            "finished": actual["finished"], "total": actual["total"]
        }

    expected = {}
    proof_artifacts = [p["artifacts"] for p in review["packages"]]
    build_sources = [read(f"certificates/{route}-build.json")["sources"]
                     for route in ["rh", "grh", "guide"]]
    for item in records([integration, proof_artifacts, build_sources,
                         read("certificates/guide-review.json")]):
        name, digest = item["path"], item["sha256"]
        path = Path(name)
        assert not path.is_absolute() and ".." not in path.parts, name
        assert name not in expected or expected[name] == digest, name
        expected[name] = digest
    verified = uncached_renders = 0
    for name, digest in sorted(expected.items()):
        path = ROOT / name
        if name.startswith("build/review-frontier/") and not path.is_file():
            uncached_renders += 1
            continue
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, name
        verified += 1

    assert (ROOT / "paper/main.pdf").read_bytes() == (ROOT / "paper/grh/main.pdf").read_bytes()
    assert integration["builds"]["guide"]["pages"] <= 12
    guide = (ROOT / "paper/guide/main.tex").read_text()
    start = guide.index(r"\section{A particularly short analytic route for RH}")
    stop = guide.index(r"\section{The smaller final analytic target}")
    block = guide[start:stop].encode()
    preservation = read("certificates/guide-review.json")["analytic_proof_preservation"]
    assert len(block) == preservation["bytes"]
    assert hashlib.sha256(block).hexdigest() == preservation["block_sha256"]
    print(json.dumps({
        "result": "PASS", "reviewed_packages": len(ids),
        "verified_artifacts": verified,
        "uncached_visual_artifacts_not_replayed": uncached_renders,
        "scope": "Frozen identities, stable node status and guide proof preservation; no mathematical proof or Lean replay."
    }))


if __name__ == "__main__":
    main()
