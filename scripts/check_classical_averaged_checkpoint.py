#!/usr/bin/env python3
"""Verify the recorded files of the classical/averaged checkpoint, offline.

This checks integrity and recorded source ranges, not mathematical truth or
Lean kernel acceptance. It needs the ignored pinned source and paper caches.
The source cache can be populated with scripts/source_excerpt.py --atlas.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERTS = [
    "classical-local-correspondence", "galois-period-dictionary",
    "lean-global-inputs", "local-correspondence-bridge",
    "fixed-correspondence-reduction", "one-construction-target",
    "covolume-defect-budget",
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def check_file(path, expected):
    data = (ROOT / path).read_bytes()
    assert sha(data) == expected, f"SHA-256 mismatch: {path}"
    return data


def main():
    sources, ranges, notes, papers = set(), 0, 0, set()
    cached_papers = {}
    for directory in ["build/galois-period", "build/global-inputs",
                      "build/classical-local-correspondence"]:
        for path in (ROOT / directory).rglob("*.pdf"):
            cached_papers[sha(path.read_bytes())] = path
    for name in CERTS:
        record = json.loads((ROOT / f"certificates/{name}.json").read_text())
        if record.get("note_sha256"):
            check_file(f"notes/{name}.md", record["note_sha256"])
            notes += 1
        for entry in record.get("files", []):
            source = ROOT / "build/lean-mirror" / entry["path"]
            data = source.read_bytes()
            assert sha(data) == entry["sha256"], f"Source SHA-256: {source}"
            git = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
            assert git == entry["git_blob_sha1"], f"Git blob: {source}"
            if "bytes" in entry:
                assert len(data) == entry["bytes"], f"Source size: {source}"
            lines = len(data.splitlines())
            inspected = entry.get("inspected_ranges", [])
            for start, end in inspected:
                assert 1 <= start <= end <= lines, f"Range: {source}:{start}-{end}"
                ranges += 1
            for read in entry.get("reads", []):
                if isinstance(read, dict) and "lines" in read:
                    start, end = map(int, read["lines"].split(":"))
                    assert 1 <= start <= end <= lines, f"Range: {source}:{start}-{end}"
                    ranges += 1
            sources.add(entry["path"])
        references = record.get("primary_references", record.get("primary_literature", []))
        if isinstance(references, dict):
            references = references.values()
        for reference in references:
            digest = reference.get("sha256", reference.get("pdf_sha256"))
            if digest:
                if reference.get("local_path"):
                    check_file(reference["local_path"], digest)
                else:
                    assert digest in cached_papers, f"Missing primary paper: {reference['id']}"
                papers.add(digest)
    composition = json.loads((ROOT / "certificates/classical-galois-substitution.json").read_text())
    check_file(composition["note"], composition["note_sha256"])
    for dependency in composition["dependencies"]:
        check_file(dependency["note"], dependency["note_sha256"])
        check_file(dependency["certificate"], dependency["certificate_sha256"])
    global_record = json.loads((ROOT / "certificates/galois-period-dictionary.json").read_text())
    for dependency in global_record["adoption_dependencies"]:
        check_file(dependency["note"], dependency["note_sha256_at_adoption"])
        check_file(dependency["certificate"], dependency["certificate_sha256_at_adoption"])
    for manuscript in composition["manuscript_files"]:
        check_file(manuscript["path"], manuscript["sha256"])
    for name in ["one-construction-target", "covolume-defect-budget"]:
        record = json.loads((ROOT / f"certificates/{name}.json").read_text())
        manuscript = record.get("manuscript_file", record.get("manuscript_integration"))
        check_file(manuscript["path"], manuscript["sha256"])
    result = {
        "status": "PASS", "source_files": len(sources),
        "recorded_ranges_checked": ranges, "notes_checked": notes + 1,
        "distinct_primary_pdfs": len(papers),
        "composition_dependencies": len(composition["dependencies"]),
        "script_sha256": sha(Path(__file__).read_bytes()),
        "certificate_sha256": {
            name: sha((ROOT / f"certificates/{name}.json").read_bytes())
            for name in CERTS + ["classical-galois-substitution"]
        },
        "scope": "Offline file integrity and range validation; no proof or kernel verification",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
