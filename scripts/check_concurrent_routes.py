#!/usr/bin/env python3
"""Check the two built manuscripts, common proof inputs and current node counts.

This validates files, synchronization and documented reviews. It does not
infer mathematical completion from compilation or from the number of nodes.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def read(path):
    return json.loads((ROOT/path).read_text())


def main():
    builds = {route: read(f"certificates/{route}-build.json") for route in ["rh", "grh"]}
    for route, data in builds.items():
        assert data["route"] == route
        assert data["output"]["path"] == f"paper/{route}/main.pdf"
        assert sha(data["output"]["path"]) == data["output"]["sha256"]
        assert (ROOT/data["output"]["path"]).stat().st_size == data["output"]["bytes"]
        paths = {item["path"] for item in data["sources"]}
        assert f"paper/{route}/main.tex" in paths and "paper/preamble.tex" in paths
        for source in data["sources"]:
            assert sha(source["path"]) == source["sha256"], source["path"]
    assert (ROOT/"paper/main.pdf").read_bytes() == (ROOT/"paper/grh/main.pdf").read_bytes()
    assert r"\input{grh/main}" in (ROOT/"paper/main.tex").read_text()
    common = sorted(set(s["path"] for s in builds["rh"]["sources"]) &
                    set(s["path"] for s in builds["grh"]["sources"]))
    fragments = [p for p in common if p.startswith("paper/shared/")]
    for route in ["rh", "grh"]:
        for fragment in (ROOT/"paper/shared").glob("*.tex"):
            name = str(fragment.relative_to(ROOT))
            assert name in common, ("A declared common proof is missing from a route", route, name)
    aggregate = read("blueprint/proof-blueprint.json")
    progress = read("blueprint/progress.json")
    for route, key in [("rh", "rh"), ("grh", "technical")]:
        canonical = read(f"blueprint/{route}/map.json")
        assert aggregate[key] == canonical
        actual = Counter(node["status"] for node in canonical["nodes"])
        record = progress["maps"][key]
        assert record["total"] == len(canonical["nodes"])
        assert record["finished"] == actual["written"] + actual["cited"]
        assert read(f"blueprint/{route}/status.json") == record
        old_name = "rh" if route == "rh" else "technical"
        assert (ROOT/f"blueprint/{route}/proof.svg").read_bytes() == (ROOT/f"blueprint/{old_name}.svg").read_bytes()
    assert read("blueprint/grh/program.json") == read("blueprint/full-proof-program.json")
    for record in read("certificates/route-blueprint-check.json")["artifacts"]:
        assert sha(record["path"]) == record["sha256"], record["path"]
    # Validate all local links in the newly organized public entry documents.
    docs = ["README.md", "paper/README.md", "paper/rh/README.md", "paper/grh/README.md",
            "blueprint/rh/README.md", "blueprint/grh/README.md", "blueprint/shared/README.md",
            "blueprint/rh/program.md", "blueprint/grh/program.md", "blueprint/progress.md"]
    links = 0
    for path in docs:
        text = (ROOT/path).read_text()
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            if target.startswith("#") or re.match(r"[a-zA-Z]+:", target):
                continue
            file = target.partition("#")[0]
            assert (ROOT/path).parent.joinpath(file).exists(), (path, target)
            links += 1
    result = {"passed": True, "scope": "Actual source/PDF hashes, distinct routes, common proof inclusion, stable node counts and public local links. No mathematical theorem is inferred from these checks.",
              "pages": {k: v["page_count"] for k,v in builds.items()},
              "counts": {k: {x:v[x] for x in ["finished","total"]} for k,v in progress["maps"].items()},
              "common_tex_inputs": common, "common_proof_fragments": fragments,
              "local_links_checked": links,
              "build_certificates": {route:sha(f"certificates/{route}-build.json") for route in builds},
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/"certificates/concurrent-routes-check.json").write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({k:result[k] for k in ["passed", "pages", "counts", "common_proof_fragments", "local_links_checked"]}))


if __name__ == "__main__":
    main()
