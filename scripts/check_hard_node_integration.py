#!/usr/bin/env python3
"""Verify the frozen hard-node review and its integrated deliverables.

This checks artifact identity, not mathematical truth or Lean compilation.
Recorded visual checks are historical; cached renders are checked if present.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INTEGRATION = "certificates/hard-node-integration-2026-11-22.json"
REVIEW = "certificates/hard-node-review-2026-11-22.json"


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
    integration = read(INTEGRATION)
    review = read(REVIEW)
    assert len(review["packages"]) == 16
    assert all(p["status"] == "PASS" for p in review["packages"])
    assert integration["proof_package_ids"] == [p["id"] for p in review["packages"]]
    assert integration["node_counts"] == review["node_counts"]
    assert integration["new_existing_nodes_completed"] == 0

    expected = {}
    proof_artifacts = [p["artifacts"] for p in review["packages"]]
    for item in records([integration, proof_artifacts, read("certificates/guide-review.json")]):
        name, digest = item["path"], item["sha256"]
        path = Path(name)
        assert not path.is_absolute() and ".." not in path.parts, name
        assert name not in expected or expected[name] == digest, name
        expected[name] = digest
    verified, uncached_renders = 0, 0
    for name, digest in sorted(expected.items()):
        path = ROOT / name
        if name.startswith("build/review-hard-nodes/") and not path.is_file():
            uncached_renders += 1
            continue
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, name
        verified += 1
    assert (ROOT / "paper/main.pdf").read_bytes() == (ROOT / "paper/grh/main.pdf").read_bytes()
    assert integration["builds"]["guide"]["pages"] <= 12
    print(json.dumps({
        "result": "PASS", "reviewed_packages": len(review["packages"]),
        "verified_artifacts": verified,
        "uncached_visual_artifacts_not_replayed": uncached_renders,
        "scope": "Frozen artifact identities and integration consistency; no mathematical proof or Lean replay."
    }))


if __name__ == "__main__":
    main()
