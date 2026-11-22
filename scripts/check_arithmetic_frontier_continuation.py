#!/usr/bin/env python3
"""Verify the frozen arithmetic continuation and its manuscript integration.

This checks artifact identities, original route status, proof inclusion and
the retained short RH argument. It is not a mathematical or Lean proof check.
Historical integration records are intentionally not rewritten by this check.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORD = "certificates/arithmetic-frontier-integration-2026-11-22.json"


def read(path: str):
    return json.loads((ROOT / path).read_text())


def digest(path: str) -> str:
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def main() -> None:
    record = read(RECORD)
    assert record["status"] == "PASS"
    assert record["new_existing_nodes_completed"] == 0
    ids = [p["id"] for p in record["packages"]]
    assert len(ids) == len(set(ids))
    assert all(p["review_status"] == "PASS" for p in record["packages"])

    progress = read("blueprint/progress.json")
    for route, key in [("rh", "rh"), ("grh", "technical")]:
        actual = progress["maps"][key]
        assert record["node_counts"][route] == {
            "finished": actual["finished"], "total": actual["total"]
        }

    seen = set()
    for item in record["artifacts"]:
        name = item["path"]
        path = Path(name)
        assert not path.is_absolute() and ".." not in path.parts
        assert name not in seen, name
        seen.add(name)
        assert digest(name) == item["sha256"], name
        assert (ROOT / name).stat().st_size == item["bytes"], name
        if path.suffix in {".md", ".tex", ".py", ".json", ".svg", ".dot"}:
            assert not any(c < 32 and c not in (9, 10)
                           for c in (ROOT / name).read_bytes()), name

    builds = {r: read(f"certificates/{r}-build.json")
              for r in ["rh", "grh", "guide"]}
    for route, build in builds.items():
        assert record["builds"][route]["pages"] == build["page_count"]
        assert digest(build["output"]["path"]) == build["output"]["sha256"]
        for source in build["sources"]:
            assert digest(source["path"]) == source["sha256"], source["path"]
    assert builds["guide"]["page_count"] == 8
    assert (ROOT / "paper/main.pdf").read_bytes() == (
        ROOT / "paper/grh/main.pdf").read_bytes()

    guide = (ROOT / "paper/guide/main.tex").read_text()
    block = guide[guide.index(r"\section{A particularly short analytic route for RH}"):
                  guide.index(r"\section{The smaller final analytic target}")].encode()
    saved = record["guide_analytic_proof_preservation"]
    assert len(block) == saved["bytes"] == 2958
    assert hashlib.sha256(block).hexdigest() == saved["sha256"]

    for fragment in read("paper/shared/manifest.json")["fragments"]:
        included = {r for r in ["rh", "grh"]
                    if fragment["path"] in
                    {s["path"] for s in builds[r]["sources"]}}
        assert included == set(fragment["routes"]), fragment["path"]
    assert read("certificates/concurrent-routes-check.json")["passed"]
    assert record["visual_review"]["status"] == "PASS"
    missing_renders = 0
    for item in record["visual_review"]["renders"]:
        if (ROOT / item["path"]).exists():
            assert digest(item["path"]) == item["sha256"]
        else:
            missing_renders += 1
    print(json.dumps({
        "status": "PASS", "packages": len(ids),
        "verified_artifacts": len(seen),
        "uncached_renders_not_replayed": missing_renders,
        "node_counts": record["node_counts"],
        "scope": "Artifact identity, source inclusion, preserved guide proof and unchanged node status; no mathematical proof or upstream Lean replay."
    }))


if __name__ == "__main__":
    main()
