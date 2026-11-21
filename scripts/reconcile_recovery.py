#!/usr/bin/env python3
"""Check recovery preservation and index the modular mathematical manuscript.

This is a structural check, not a mathematical proof checker. It never reads
or downloads the large original Lean archive. Run from any directory:
    python3 scripts/reconcile_recovery.py
The immutable attachments are identified by SHA-256 below. The 621 entries
of the supplied bundle manifest are verified without extracting the bundle.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "archive/recovered-2026-11-21"
CERTIFICATE = ROOT / "certificates/recovery-integration.json"
EXPECTED = {
    "grh_audit_v2.tex": "9e709162aa204a1133d395e3387fd067f319ab88f549f86859a5dd4f8e111ddc",
    "grh_reconstruction_v2.tex": "3226beb21817d4f19f56a275f58988ad5d3c13368d5f701714633c4df66a0fad",
    "grh_audit_reproducibility.zip": "0dc8aa1c765fdc7577b55a67171c500e567390897e0a97f34b83a59b2e72fa78",
}
LABEL = re.compile(r"\\label\{([^}]+)\}")
REFERENCE = re.compile(r"\\(?:eqref|ref|autoref|pageref)\{([^}]+)\}")
INPUT = re.compile(r"\\(?:input|include)\{([^}]+)\}")
RESULT = re.compile(
    r"\\begin\{(theorem|lemma|proposition|corollary|example|remark)\}"
    r"(?:\[([^\]]*)\])?(.*?)\\end\{\1\}", re.S
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def uncomments(text: str) -> str:
    return "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0]
                     for line in text.splitlines())


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", uncomments(text)).strip()


def title(text: str) -> str:
    at = text.index("{")
    depth, end = 1, at + 1
    while depth and end < len(text):
        if text[end] == "{" and text[end - 1] != "\\":
            depth += 1
        elif text[end] == "}" and text[end - 1] != "\\":
            depth -= 1
        end += 1
    if depth:
        raise ValueError("Unbalanced section title")
    return text[at + 1:end - 1]


def results(text: str, start: int = 1) -> list[dict]:
    out = []
    for index, match in enumerate(RESULT.finditer(text), 1):
        out.append({
            "ordinal": index,
            "kind": match.group(1),
            "title_tex": match.group(2),
            "line_start": start + text[:match.start()].count("\n"),
            "line_end": start + text[:match.end()].count("\n"),
            "labels": LABEL.findall(match.group(3)),
            "statement_sha256_normalized": digest(normalized(match.group(0)).encode()),
        })
    return out


def expansion(main: Path) -> tuple[str, list[str]]:
    """Expand fixed-name inputs with the same working directory as the build."""
    working = main.parent
    visited: list[str] = []
    active: set[Path] = set()

    def read(path: Path) -> str:
        path = path.resolve()
        if path in active:
            raise ValueError(f"Recursive input: {relative(path)}")
        if not path.is_relative_to(ROOT):
            raise ValueError(f"Input outside repository: {path}")
        active.add(path)
        visited.append(relative(path))
        text = uncomments(path.read_text())

        def include(match: re.Match) -> str:
            name = match.group(1)
            child = Path(name if Path(name).suffix else name + ".tex")
            primary = working / child
            if not primary.exists():
                primary = path.parent / child
            return read(primary)

        text = INPUT.sub(include, text)
        active.remove(path)
        return text

    return read(main), visited


def main() -> int:
    errors: list[str] = []
    attachment_files = []
    for name, expected in EXPECTED.items():
        path = ARCHIVE / name
        actual = digest(path.read_bytes())
        matches = actual == expected
        if not matches:
            errors.append(f"Immutable attachment changed: {name}")
        attachment_files.append({"path": relative(path), "bytes": path.stat().st_size,
                                 "sha256": actual, "matches_attachment_pin": matches})

    zip_path = ARCHIVE / "grh_audit_reproducibility.zip"
    fragments: list[tuple[str, str, set[str]]] = []
    with zipfile.ZipFile(zip_path) as bundle:
        members = bundle.infolist()
        names = [entry.filename for entry in members]
        if len(names) != len(set(names)):
            errors.append("Duplicate ZIP member names")
        files = [entry for entry in members if not entry.is_dir()]
        for entry in members:
            member = PurePosixPath(entry.filename)
            if member.is_absolute() or ".." in member.parts:
                errors.append(f"Unsafe ZIP path: {entry.filename}")
            if ((entry.external_attr >> 16) & 0o170000) == 0o120000:
                errors.append(f"ZIP symlink: {entry.filename}")
        prefix = "grh_audit_reproducibility/"
        manifest = json.loads(bundle.read(prefix + "bundle_manifest.json"))
        manifest_bad = []
        for item in manifest["files"]:
            data = bundle.read(prefix + item["path"])
            if len(data) != item["bytes"] or digest(data) != item["sha256"]:
                manifest_bad.append(item["path"])
        crc_bad = bundle.testzip()
        if manifest_bad or crc_bad:
            errors.append("ZIP content integrity failure")
        duplicates_match = {}
        for archive_name, zipped_name in [
            ("grh_audit_v2.tex", "grh_audit.tex"),
            ("grh_reconstruction_v2.tex", "grh_reconstruction.tex"),
        ]:
            same = (ARCHIVE / archive_name).read_bytes() == bundle.read(prefix + zipped_name)
            duplicates_match[archive_name] = same
            if not same:
                errors.append(f"Separate TeX differs from ZIP: {archive_name}")
        for entry in files:
            name = entry.filename.removeprefix(prefix)
            if name.startswith("mathematics/") and name.endswith(".tex"):
                text = bundle.read(entry).decode()
                fragments.append((name, text, set(LABEL.findall(text))))
        zip_report = {
            "bundle_created_utc": manifest["created_utc"],
            "regular_files": len(files),
            "uncompressed_bytes": sum(item.file_size for item in files),
            "manifest_entries_verified": len(manifest["files"]),
            "manifest_mismatches": manifest_bad,
            "first_bad_crc_member": crc_bad,
            "unlisted_regular_files": sorted(set(names) -
                {prefix + item["path"] for item in manifest["files"]}),
            "separate_tex_equals_bundled_tex": duplicates_match,
        }

    original_path = ARCHIVE / "grh_reconstruction_v2.tex"
    original = original_path.read_text()
    lines = original.splitlines(keepends=True)
    starts = [i for i, line in enumerate(lines) if line.startswith(r"\section{")]
    bibliography = next(i for i, line in enumerate(lines)
                        if line.startswith(r"\begin{thebibliography}"))
    close = "".join(lines[starts[-1]:bibliography])
    # Bounded evidence excerpts; no duplicated 235-line status paragraph.
    closing_sentences = re.split(r"(?<=\.)\s+(?=[A-Z\\])", close)
    modular_paths = sorted((ROOT / "paper/sections/recovered").glob("*.tex"))
    modular_by_number = {}
    for path in modular_paths:
        match = re.match(r"(\d+)-", path.name)
        if match:
            number = int(match.group(1))
            if number in modular_by_number:
                errors.append(f"Duplicate recovered section number: {number}")
            modular_by_number[number] = path
    sections = []
    for index, start in enumerate(starts, 1):
        end = starts[index] if index < len(starts) else bibliography
        text = "".join(lines[start:end])
        labels = LABEL.findall(text)
        heading = lines[start].strip()
        first_paragraph = text.split("\n\n", 1)[0]
        section_labels = LABEL.findall(first_paragraph)
        targets = set(section_labels)
        statement_records = results(text, start + 1)
        part = modular_by_number.get(index)
        revised = part.read_text() if part else ""
        revised_records = results(revised)
        kind_counts = Counter(x["kind"] for x in statement_records)
        revised_counts = Counter(x["kind"] for x in revised_records)
        missing_counts = dict(kind_counts - revised_counts)
        missing_labels = sorted(set(labels) - set(LABEL.findall(revised)))
        lost_proofs = text.count(r"\begin{proof}") > revised.count(r"\begin{proof}")
        if not part or missing_labels or missing_counts or lost_proofs:
            errors.append(f"Incomplete recovered section {index}")
        evidence = []
        for sentence in closing_sentences:
            if targets.intersection(REFERENCE.findall(sentence)):
                excerpt = normalized(sentence)
                evidence.append(excerpt[:900] + (" ..." if len(excerpt) > 900 else ""))
        source_modules = [name for name, fragment, fragment_labels in fragments
                          if targets.intersection(fragment_labels) or heading in fragment]
        for old, new in zip(statement_records, revised_records):
            old["working_statement_sha256_normalized"] = new["statement_sha256_normalized"]
            old["statement_unchanged"] = (
                old["statement_sha256_normalized"] == new["statement_sha256_normalized"])
        sections.append({
            "original_number": index,
            "title_tex": title(text),
            "original_line_start": start + 1,
            "original_line_end": end,
            "original_sha256": digest(text.encode()),
            "working_path": relative(part) if part else None,
            "working_sha256": digest(revised.encode()) if part else None,
            "byte_identical": revised == text,
            "section_labels": section_labels,
            "labels": labels,
            "missing_labels": missing_labels,
            "missing_result_counts": missing_counts,
            "original_result_counts": dict(kind_counts),
            "working_result_counts": dict(revised_counts),
            "original_proof_count": text.count(r"\begin{proof}"),
            "working_proof_count": revised.count(r"\begin{proof}"),
            "results": statement_records,
            "bundle_source_fragments": source_modules,
            "latest_recovered_status_evidence": evidence,
            "references": sorted(set(REFERENCE.findall(text))),
        })
    label_owner = {label: section["original_number"]
                   for section in sections for label in section["labels"]}
    for section in sections:
        section["referenced_sections"] = sorted({
            label_owner[label] for label in section.pop("references")
            if label in label_owner and label_owner[label] != section["original_number"]
        })

    assembled, inputs = expansion(ROOT / "paper/main.tex")
    assembled_labels = LABEL.findall(assembled)
    label_counts = Counter(assembled_labels)
    missing = sorted(set(LABEL.findall(original)) - set(assembled_labels))
    duplicate_labels = sorted(label for label, count in label_counts.items() if count > 1)
    unresolved = sorted(set(REFERENCE.findall(assembled)) - set(assembled_labels))
    absent_inputs = [section["working_path"] for section in sections
                     if section["working_path"] not in inputs]
    if missing or duplicate_labels or unresolved or absent_inputs:
        errors.append("Main manuscript inclusion/reference failure")

    baseline_path = ROOT / "certificates/restart-paper-baseline.json"
    baseline = json.loads(baseline_path.read_text())
    companion, companion_inputs = expansion(ROOT / "paper/companion/main.tex")
    old_labels = {label for file in baseline["files"] for label in file["labels"]}
    companion_labels = set(LABEL.findall(companion))
    companion_missing = sorted(old_labels - companion_labels)
    companion_files = []
    for old in baseline["files"]:
        path = ROOT / "paper/companion" / old["path"]
        current = digest(path.read_bytes()) if path.exists() else None
        companion_files.append({"path": relative(path), "baseline_sha256": old["sha256"],
                                "current_sha256": current,
                                "byte_identical_to_restart": current == old["sha256"]})
    if companion_missing:
        errors.append("Missing restart companion labels")
    source_labels = LABEL.findall(original)
    bib_pattern = r"\\bibitem(?:\[[^\]]+\])?\{([^}]+)\}"
    original_bib = re.findall(bib_pattern, original)
    current_bib = re.findall(bib_pattern, assembled)
    missing_bib = sorted(set(original_bib) - set(current_bib))
    if missing_bib:
        errors.append("Missing recovered bibliography entries")
    report = {
        "schema_version": 1,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Preservation, inclusion, cross-reference and structural reconciliation only; no complete independent mathematical or Lean verification is claimed.",
        "baseline_repository_commit": baseline["commit"],
        "attachments": attachment_files,
        "bundle": zip_report,
        "original_reconstruction": {
            "path": relative(original_path), "lines": len(lines),
            "sections": len(sections), "unique_labels": len(set(source_labels)),
            "result_environments": sum(len(section["results"]) for section in sections),
            "proof_environments": original.count(r"\begin{proof}"),
            "bibliography_entries": len(original_bib),
            "frontmatter_lines": [1, starts[0]],
            "bibliography_and_end_lines": [bibliography + 1, len(lines)],
        },
        "main_inclusion": {
            "inputs": inputs, "missing_recovered_labels": missing,
            "duplicate_labels": duplicate_labels, "unresolved_references": unresolved,
            "recovered_sections_not_included": absent_inputs,
            "missing_bibliography_entries": missing_bib,
            "byte_identical_recovered_sections": sum(s["byte_identical"] for s in sections),
            "edited_recovered_sections": [s["original_number"] for s in sections if not s["byte_identical"]],
            "interpretation": "All original sections and result environments must remain represented. Hash differences identify editorial or mathematical revisions; they are not certified as mathematically equivalent by this script.",
        },
        "restart_companion": {
            "baseline": relative(baseline_path), "baseline_unique_labels": len(old_labels),
            "missing_labels": companion_missing, "inputs": companion_inputs,
            "files": companion_files,
        },
        "sections": sections,
        "errors": errors,
        "passed": not errors,
    }
    CERTIFICATE.parent.mkdir(parents=True, exist_ok=True)
    CERTIFICATE.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "passed": report["passed"], "bundle_files": len(files),
        "manifest_entries_verified": len(manifest["files"]),
        "recovered_sections": len(sections), "recovered_labels": len(set(source_labels)),
        "result_environments": report["original_reconstruction"]["result_environments"],
        "companion_labels": len(old_labels), "errors": errors,
        "certificate": relative(CERTIFICATE),
    }, indent=2))
    return 0 if not errors else 1


def inspect(section_number: int | None, label: str | None) -> int:
    """Print one bounded resumption card instead of the complete registry."""
    report = json.loads(CERTIFICATE.read_text())
    matching = [section for section in report["sections"]
                if (section_number == section["original_number"] or
                    label is not None and label in section["labels"])]
    if not matching:
        print("No recovered section matches the requested number or label.", file=sys.stderr)
        return 1
    section = matching[0]
    selected_results = [result for result in section["results"]
                        if label is None or label in result["labels"]]
    card = {key: section[key] for key in [
        "original_number", "title_tex", "original_line_start", "original_line_end",
        "working_path", "section_labels", "referenced_sections",
        "bundle_source_fragments", "latest_recovered_status_evidence",
    ]}
    card["results"] = [{key: result[key] for key in [
        "kind", "title_tex", "line_start", "line_end", "labels",
    ]} for result in selected_results]
    card["scope"] = "Recovered structural record, not a new independent proof audit."
    print(json.dumps(card, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    query = parser.add_mutually_exclusive_group()
    query.add_argument("--section", type=int, help="Print one recovered section's resumption card.")
    query.add_argument("--label", help="Find one label without printing the whole registry.")
    args = parser.parse_args()
    sys.exit(inspect(args.section, args.label)
             if args.section is not None or args.label is not None else main())
