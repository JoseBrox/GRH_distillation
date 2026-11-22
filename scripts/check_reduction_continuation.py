#!/usr/bin/env python3
"""Verify the frozen reduction continuation and its publication artifacts.

This checks identities, inclusion, stable status and recorded visual scope.
It does not replace the written mathematical proofs or compile upstream Lean.
Later revisions should preserve this snapshot and make a new integration record.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEW = "certificates/reduction-continuation-review-2026-11-22.json"
INTEGRATION = "certificates/reduction-continuation-integration-2026-11-22.json"


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


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def main():
    review, integration = read(REVIEW), read(INTEGRATION)
    assert all(p["review_status"] == "PASS" for p in review["packages"])
    ids = [p["id"] for p in review["packages"]]
    assert len(ids) == len(set(ids)) == 8
    assert integration["package_ids"] == ids
    assert review["new_existing_nodes_completed"] == 0
    assert integration["node_counts"] == review["node_counts"]
    progress = read("blueprint/progress.json")
    for route, key in [("rh", "rh"), ("grh", "technical")]:
        actual = progress["maps"][key]
        assert review["node_counts"][route] == {
            "finished": actual["finished"], "total": actual["total"]
        }
    builds = {r: read(f"certificates/{r}-build.json")
              for r in ["rh", "grh", "guide"]}
    expected = {}
    for item in records([review, integration, list(builds.values())]):
        name, checksum = item["path"], item["sha256"]
        p = Path(name)
        assert not p.is_absolute() and ".." not in p.parts, name
        assert name not in expected or expected[name] == checksum, name
        expected[name] = checksum
    verified = omitted_renders = 0
    for name, checksum in sorted(expected.items()):
        p = ROOT / name
        if name.startswith("build/review-reduction-continuation/") and not p.exists():
            omitted_renders += 1
            continue
        assert digest(name) == checksum, name
        if p.suffix in {".md", ".tex", ".py", ".json", ".svg", ".dot"}:
            assert not any(c < 32 and c not in (9, 10) for c in p.read_bytes()), (
                "Unexpected control character in a text artifact", name)
        verified += 1
    for route, build in builds.items():
        assert integration["builds"][route]["pages"] == build["page_count"]
    assert builds["guide"]["page_count"] == 8
    assert (ROOT / "paper/main.pdf").read_bytes() == (ROOT / "paper/grh/main.pdf").read_bytes()
    guide = (ROOT / "paper/guide/main.tex").read_text()
    block = guide[guide.index(r"\section{A particularly short analytic route for RH}"):
                  guide.index(r"\section{The smaller final analytic target}")].encode()
    saved = integration["guide_analytic_proof_preservation"]
    assert len(block) == saved["bytes"] == 2958
    assert hashlib.sha256(block).hexdigest() == saved["sha256"]
    manifest = read("paper/shared/manifest.json")
    for fragment in manifest["fragments"]:
        included = {r for r in ["rh", "grh"]
                    if fragment["path"] in {s["path"] for s in builds[r]["sources"]}}
        assert included == set(fragment["routes"]), fragment["path"]
    assert read("certificates/concurrent-routes-check.json")["passed"]
    assert integration["visual_review"]["status"] == "PASS"
    print(json.dumps({
        "status": "PASS", "packages": len(ids), "verified_artifacts": verified,
        "uncached_renders_not_replayed": omitted_renders,
        "node_counts": review["node_counts"],
        "scope": "Frozen artifact identities, actual proof inclusion, preserved guide proof and unchanged node status; no mathematical proof or upstream Lean replay."
    }))


if __name__ == "__main__":
    main()
