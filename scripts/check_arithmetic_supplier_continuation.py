#!/usr/bin/env python3
"""Verify the frozen arithmetic-supplier integration, without replaying Lean.

Mathematical proofs and finite exact checks have separate reviewed records.
This checks their identities, actual manuscript inclusion, current builds,
unchanged node counts and the protected short analytic proof in the guide.
Earlier integration records retain their historical snapshots.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECORD = "certificates/arithmetic-supplier-integration-2026-11-22.json"


def read(path):
    return json.loads((ROOT / path).read_text())


def artifact_pairs(value):
    if isinstance(value, dict):
        for path, digest in value.items():
            yield path, digest["sha256"] if isinstance(digest, dict) else digest
    else:
        for item in value:
            yield item["path"], item["sha256"]


def main():
    record = read(RECORD)
    assert record["status"] == "PASS"
    assert record["new_existing_nodes_completed"] == 0
    assert record["lean_build_run"] is False
    expected = {}

    def add(pairs):
        for name, digest in pairs:
            path = Path(name)
            assert not path.is_absolute() and ".." not in path.parts, name
            assert name not in expected or expected[name] == digest, name
            expected[name] = digest

    add(artifact_pairs(record["artifacts"]))
    for package in record["packages"]:
        check, review = read(package["check"]), read(package["review"])
        assert check.get("status") == "PASS", package["id"]
        assert review.get("status", review.get("verdict")) == "PASS", package["id"]
        add(artifact_pairs(check["artifacts"]))
        add(artifact_pairs(review["artifacts"]))
        assert all(s["commit"] == record["source_pin"]
                   and s["matches_pinned_blob"] for s in check["sources"])

    scope = read(record["scope_review"])
    assert scope["status"] == "PASS" and not scope["remaining_findings"]
    add(artifact_pairs(scope["reviewed_snapshot_sha256"]))
    builds = {r: read(f"certificates/{r}-build.json")
              for r in ("rh", "grh", "guide")}
    for route, build in builds.items():
        add(artifact_pairs(build["sources"]))
        add(artifact_pairs([build["output"]]))
        assert build["page_count"] == record["builds"][route]["pages"]
    visual = read(record["visual_review"])
    assert visual["verdict"] == "PASS"
    add(artifact_pairs(visual["documents"]))
    for document in visual["documents"]:
        assert all(page["actually_viewed"] and page["verdict"] == "PASS"
                   for page in document["page_reviews"])
    assert (ROOT / "paper/main.pdf").read_bytes() == (ROOT / "paper/grh/main.pdf").read_bytes()

    manifest = {f["path"]: f for f in read("paper/shared/manifest.json")["fragments"]}
    for route in ("rh", "grh"):
        source_paths = [s["path"] for s in builds[route]["sources"]]
        texts = [(ROOT / p).read_text() for p in source_paths]
        inputs = [name for text in texts
                  for name in re.findall(r"\\input\{([^}]+)\}", text)]
        for package in record["packages"]:
            for fragment in package["fragments"]:
                assert fragment in source_paths, (route, fragment)
                assert sorted(manifest[fragment]["routes"]) == ["grh", "rh"]
                stem = Path(fragment).stem
                count = sum(Path(name).stem == stem for name in inputs)
                assert count == 1, (route, fragment, count)
        nodes = read(f"blueprint/{route}/map.json")["nodes"]
        counts = Counter(n["status"] for n in nodes)
        actual = {"finished": counts["written"] + counts["cited"], "total": len(nodes)}
        reviewed = scope["node_counts"][route]
        assert actual == record["node_counts"][route]
        assert actual == {"finished": reviewed["written_or_cited"], "total": reviewed["total"]}

    guide = (ROOT / "paper/guide/main.tex").read_text()
    start = guide.index(r"\section{A particularly short analytic route for RH}")
    stop = guide.index(r"\section{The smaller final analytic target}")
    block = guide[start:stop].encode()
    protected = record["guide_analytic_proof"]
    assert len(block) == protected["bytes"]
    assert hashlib.sha256(block).hexdigest() == protected["sha256"]
    assert builds["guide"]["page_count"] == 8
    assert read("certificates/concurrent-routes-check.json")["passed"] is True

    for name, digest in sorted(expected.items()):
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    print(json.dumps({
        "result": "PASS", "reviewed_packages": len(record["packages"]),
        "verified_artifacts": len(expected), "guide_pages": 8,
        "node_counts": record["node_counts"],
        "scope": "Frozen artifact identity, manuscript inclusion and build consistency; no mathematical proof or Lean replay."
    }, sort_keys=True))


if __name__ == "__main__":
    main()
