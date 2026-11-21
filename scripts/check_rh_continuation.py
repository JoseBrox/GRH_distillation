#!/usr/bin/env python3
"""Verify the current RH continuation's recorded artifacts and pinned sources.

Run offline after populating the ignored source cache with source_excerpt.py.
This checks bytes, source ranges and integration records. It does not repeat
the mathematical reviews or prove the remaining arithmetic construction.
The five exact-check scripts are separate, explicitly reproducible evidence.
"""
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NAMES = [
    "rh-direct-transfer", "rh-direct-source-applicability",
    "rh-weight-symmetry", "rh-geometric-combination",
    "transport-symmetry-defect", "rh-minimal-budget",
]
SCRIPTS = {
    name: "scripts/check_" + name.replace("-", "_") + ".py"
    for name in NAMES if name != "rh-direct-source-applicability"
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    return json.loads((ROOT / path).read_text())


def check_file(path, expected):
    data = (ROOT / path).read_bytes()
    assert digest(data) == expected, f"SHA-256 mismatch: {path}"
    return data


def ranges_of(entry):
    for r in entry.get("ranges", []):
        yield r["start"], r["end"], r.get("sha256")
    for r in entry.get("excerpts", []):
        first, last = r["lines"]
        yield first, last, r.get("sha256")
    for r in entry.get("reads", []):
        yield r["first_line"], r["last_line"], r.get("sha256")
    for key in ["inspected_ranges", "read_ranges"]:
        for a, b in entry.get(key, []):
            yield a, b, None


def main():
    atlas_path = "blueprint/lean-source-imports.json.gz"
    atlas_bytes = (ROOT / atlas_path).read_bytes()
    atlas = json.loads(gzip.decompress(atlas_bytes))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == PIN
    # Only a local lookup is built; no source file is printed.
    atlas_blobs = {m[0]: m[1] for m in atlas["modules"]}
    source_paths, source_ranges, hashed_ranges = set(), set(), set()
    artifact_paths, certificate_hashes = set(), {}
    for name in NAMES:
        cert_path = f"certificates/{name}.json"
        cert = read_json(cert_path)
        certificate_hashes[name] = digest((ROOT / cert_path).read_bytes())
        note = cert.get("note", f"notes/{name}.md")
        if isinstance(note, dict):
            check_file(note["path"], note["sha256"])
            artifact_paths.add(note["path"])
        elif "note_sha256" in cert:
            check_file(note, cert["note_sha256"])
            artifact_paths.add(note)
        if "script_sha256" in cert:
            script = cert.get("script", SCRIPTS[name])
            check_file(script, cert["script_sha256"])
            artifact_paths.add(script)
        if "source_atlas_sha256" in cert:
            assert digest(atlas_bytes) == cert["source_atlas_sha256"]
        for key in ["files", "source_files", "sources"]:
            for entry in cert.get(key, []):
                path = entry["path"]
                if "git_blob_sha1" not in entry:
                    check_file(path, entry["sha256"])
                    artifact_paths.add(path)
                    continue
                assert entry.get("repository", cert.get("repository", "jsmorph/rh")) == "jsmorph/rh"
                assert entry.get("commit", cert.get("commit", cert.get("source_pin", PIN))) == PIN
                cache = f"build/source-cache/jsmorph/rh/{PIN}/{path}"
                data = check_file(cache, entry["sha256"])
                blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
                assert blob == entry["git_blob_sha1"], f"Git blob mismatch: {path}"
                assert path.startswith("lean/src/") and path.endswith(".lean")
                module = path[len("lean/src/"):-len(".lean")].replace("/", ".")
                assert atlas_blobs[module] == blob, f"Pinned atlas mismatch: {module}"
                if "bytes" in entry:
                    assert len(data) == entry["bytes"]
                lines = data.splitlines(keepends=True)
                for key_count in ["lines", "line_count"]:
                    if key_count in entry:
                        assert len(lines) == entry[key_count]
                for first, last, expected in ranges_of(entry):
                    assert 1 <= first <= last <= len(lines), (path, first, last)
                    assert last - first + 1 <= 120, ("Unbounded recorded excerpt", path)
                    excerpt = b"".join(lines[first-1:last])
                    if expected:
                        assert digest(excerpt) == expected, ("Excerpt mismatch", path, first, last)
                        hashed_ranges.add((path, first, last))
                    source_ranges.add((path, first, last))
                source_paths.add(path)

    build_sources = set()
    for name in ["paper-build", "guide-build"]:
        cert = read_json(f"certificates/{name}.json")
        for entry in cert["sources"]:
            check_file(entry["path"], entry["sha256"])
            build_sources.add(entry["path"])
        out = cert["output"]
        data = check_file(out["path"], out["sha256"])
        assert len(data) == out["bytes"]
    guide = read_json("certificates/guide-review.json")
    for key in ["source", "pdf"]:
        check_file(guide[key]["path"], guide[key]["sha256"])
    assert guide["pdf"]["pages"] == read_json("certificates/guide-build.json")["page_count"] == 7
    assert guide["visual_review"]["pages_inspected"] == list(range(1, 8))

    review_path = "certificates/rh-continuation-review.json"
    review = read_json(review_path)
    for entry in review["artifacts"]:
        check_file(entry["path"], entry["sha256"])
    for name in ["blueprint-check", "full-proof-program-check"]:
        assert read_json(f"certificates/{name}.json")["passed"]
    tex = (ROOT / "paper/sections/recovered/10-cs-section.tex").read_text()
    for label in ["geometric-cover-improved", "geometric-two-moments",
                  "cs-positive-quotient-transfer", "rh-direct-budget",
                  "cs-refined-average-frame", "cs-refined-combined-budget"]:
        assert tex.count("\\label{" + label + "}") == 1, label
    scalar = (ROOT / "paper/sections/recovered/04-sec-numerical.tex").read_text()
    assert scalar.count("\\label{prop:rh-four-term-budget}") == 1
    result = {
        "schema_version": 1, "status": "PASS",
        "repository": "jsmorph/rh", "commit": PIN,
        "source_atlas_sha256": digest(atlas_bytes),
        "distinct_pinned_source_files": len(source_paths),
        "distinct_bounded_ranges": len(source_ranges),
        "distinct_ranges_with_recorded_hashes": len(hashed_ranges),
        "current_note_and_script_files": len(artifact_paths),
        "current_build_sources": len(build_sources),
        "reviewed_artifacts": len(review["artifacts"]),
        "guide_pages": 7,
        "certificate_sha256": certificate_hashes,
        "review_sha256": digest((ROOT / review_path).read_bytes()),
        "script_sha256": digest(Path(__file__).read_bytes()),
        "scope": "Current recorded bytes, bounded source ranges, atlas membership, build inputs, and review/artifact alignment. Mathematical reviews and finite exact calculations are separate evidence.",
        "limits": "No new complete source traversal, Lean build, kernel replay, or proof of the remaining compatible arithmetic construction. Earlier certificates retain their historical snapshot scopes.",
    }
    target = ROOT / "certificates/rh-continuation-integrity.json"
    target.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({k: result[k] for k in ["status", "distinct_pinned_source_files",
        "distinct_bounded_ranges", "distinct_ranges_with_recorded_hashes",
        "current_note_and_script_files", "current_build_sources", "reviewed_artifacts"]}))


if __name__ == "__main__":
    main()
