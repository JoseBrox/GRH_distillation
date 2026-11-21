#!/usr/bin/env python3
"""Build the full-source work program and a complete namespace atlas.

Coverage checks are structural. They do not certify mathematical hypotheses.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "blueprint"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    model_path = OUT / "full-proof-program.json"
    endpoint_path = ROOT / "certificates/lean-endpoint-backbone.json"
    inventory_path = ROOT / "certificates/lean-source-inventory.json"
    model = json.loads(model_path.read_text())
    endpoint = json.loads(endpoint_path.read_text())
    inventory = json.loads(inventory_path.read_text())
    works = model["work_packages"]
    ids = {w["id"] for w in works}
    assert len(ids) == len(works)
    fields = model["coherent_fields"]
    names = [f["name"] for f in fields]
    expected = [f["name"] for f in endpoint["coherent_package_fields"]]
    assert len(names) == len(set(names)) and set(names) == set(expected)
    assert all(f["owner"] in ids for f in fields)
    assert all((ROOT / path).is_file() for path in model.get("evidence", []))
    assert sum(inventory["root_groups"].values()) == inventory["local_modules"]
    assert sum(inventory["subject_groups"].values()) == inventory["local_modules"]
    assert inventory["main_reachable_modules"] == inventory["local_modules"]
    graph_file = ROOT / inventory["compressed_graph"]["path"]
    assert sha(graph_file) == inventory["compressed_graph"]["sha256"]

    lines = ["# Full proof program", "", model["scope"], "",
             "## Preferred target", "", model["preferred_target"], "", model["source_supplier"], "",
             "The eleven work packages below are responsibilities in a research program, not eleven already proved theorems or a claim of minimal logical independence.", "",
             "## What is now covered", "",
             f"The complete local source atlas contains **{inventory['local_modules']:,} pinned modules** and **{inventory['unique_local_import_edges']:,} import edges**. Every local module is reachable from Main. External package internals remain explicit boundaries; imports do not identify the indispensable declarations of a proof term.", "",
             f"All **{len(fields)} fields** of the endpoint's coherent construction are assigned in the [field ledger](endpoint-field-ledger.md). The [endpoint review](../notes/lean-endpoint-backbone.md) also inventories the final literature-assembly declarations and distinguishes lexical references from elaborated proof dependencies.", "",
             "The outer inputs are: " + "; ".join(model["outer_inputs"]) + ".", "",
             "## Structural simplifications", "",
             "| Change | Status |", "| --- | --- |"]
    lines += [f"| {s['name']} | {s['status']} |" for s in model["simplifications"]]
    lines += ["", "## Work packages", "",
              "| Package | Goal | Status |", "| --- | --- | --- |"]
    lines += [f"| [{w['id']}](#{w['id'].lower()}) | {w['title']} | {w['status']} |" for w in works]
    for w in works:
        lines += ["", f"<a id=\"{w['id'].lower()}\"></a>", f"### {w['id']}: {w['title']}", "",
                  "**Required result.** " + w["goal"], "", "**Quantifiers and uniformity.** " + w["uniformity"], "",
                  "**Source interface.** " + "; ".join(f"`{s}`" for s in w["source_contracts"]) + ".", "",
                  "**Existing manuscript coverage.** " + (", ".join(w["manuscript_sections"]) or "No matching complete conventional theorem yet") + ". Stable section ids are in the [inventory](module-inventory.md).", "",
                  "**Next concrete task.** " + w["next_step"], "", "**Acceptance conditions:**", ""]
        lines += ["- " + x for x in w["acceptance"]]
    lines += ["", "## Compatibility is part of the theorem", "", model["coherence"], "", model["nonvacuity"], "",
              "A separately proved bound for some lattice, some theta map, or some measure does not discharge a field that refers to a different selected object. Every proposed substitution needs the relevant equality, transport or compatibility statement.", "",
              "The [classical-input review](../notes/lean-global-inputs.md), [weak-to-classical comparison](../notes/fixed-correspondence-reduction.md), and [local preimage proofs](../notes/local-correspondence-bridge.md) record the current conditional reduction of the Galois construction. Both local preimage lemmas are proved under the full correspondence laws, and the conventional depth-zero type formula has passed independent review. The exact full local-law and global period-model dictionaries remain gates; the original source supplier is retained.", "",
              "## Execution order", "",
              "Read " + " → ".join(model["reading_order"][:3]) + " first to fix the final target, then work on the suppliers. The immediate research priorities are:", ""]
    lines += ["1. " + x for x in model["recommended_next"]]
    lines += ["", "After each result, update its precise status and loss/normalization ledger, run the coverage checks, and commit a coherent checkpoint to main. A candidate shortcut is not adopted until its hypotheses and all surviving branches are accounted for.", "",
              "## Reproduce the maps", "", "```sh", "python scripts/build_full_proof_program.py", "python scripts/build_blueprint.py", "```", "",
              "The [source atlas](lean-source-atlas.md), [namespace diagram](source-subject-atlas.svg), [complete subject inventory](source-subjects.md), and [technical interface graph](technical.svg) serve different purposes. Namespace containment and imports are not mathematical proof arrows."]
    (OUT / "full-proof-program.md").write_text("\n".join(lines) + "\n")

    ledger = ["# Endpoint construction field ledger", "", model["coherence"], "", model["nonvacuity"], "",
              "All 46 fields are accounted for. Some are data and choices, some are propositions, and many reference the same selected objects; they are not 46 independent assumptions. Ownership indicates where a proof obligation is tracked, not permission to construct incompatible inputs.", "",
              "| Source field | Source group | Responsible work package |", "| --- | --- | --- |"]
    ledger += [f"| `{f['name']}` | {f['source_group'].replace('_', ' ')} | [{f['owner']}](full-proof-program.md#{f['owner'].lower()}) |" for f in fields]
    ledger += ["", "Source types and bounded evidence are in [lean-endpoint-backbone.json](../certificates/lean-endpoint-backbone.json). The first-line type inventory locates the declarations; it does not replace reading the complete type when implementing a field."]
    (OUT / "endpoint-field-ledger.md").write_text("\n".join(ledger) + "\n")

    # A containment atlas, deliberately without misleading aggregated import
    # arrows: contracting arbitrary namespace groups can introduce cycles.
    groups = inventory["subject_groups"]
    major = {name: n for name, n in groups.items() if n >= 1000 and "." in name}
    partition = dict(major)
    for root, count in inventory["root_groups"].items():
        remainder = count - sum(n for name, n in major.items() if name.startswith(root + "."))
        if remainder:
            partition[root + (".Other" if any(k.startswith(root + ".") for k in major) else "")] = remainder
    assert sum(partition.values()) == inventory["local_modules"]
    quote = lambda s: json.dumps(s, ensure_ascii=False)
    dot = ['digraph source {', 'graph [rankdir=LR, bgcolor="white", pad=0.25, nodesep=0.20, ranksep=0.55, fontname="DejaVu Sans", labelloc=t, label="Complete local source atlas — namespace containment, not proof dependencies"];',
           'node [shape=box, style="rounded,filled", fillcolor="#EEF1F4", color="#64748B", fontname="DejaVu Sans", fontsize=10];',
           'edge [color="#A5AFBC", arrowhead=none];',
           f'"all" [label="Pinned local Lean source\\n{inventory["local_modules"]:,} files", fillcolor="#E8F0FC", color="#3267B2"];']
    families = ["Development", "Formalism", "GroundTheory", "Other families"]
    for family in families:
        members = {k: n for k, n in partition.items() if (k.split('.')[0] == family if family != 'Other families' else k.split('.')[0] not in families[:3])}
        dot.append(f'{quote(family)} [label={quote(family + chr(10) + format(sum(members.values()), ",") + " files")}, fillcolor="#E3F3E8", color="#267047"];')
        dot.append(f'"all" -> {quote(family)};')
        for name, count in members.items():
            label = name.replace(".", " / ") + "\n" + format(count, ",") + (" file" if count == 1 else " files")
            dot.append(f'{quote("leaf:"+name)} [label={quote(label)}];')
            dot.append(f'{quote(family)} -> {quote("leaf:"+name)};')
    dot.append("}")
    (OUT / "source-subject-atlas.dot").write_text("\n".join(dot) + "\n")
    subprocess.run(["dot", "-Tsvg", str(OUT / "source-subject-atlas.dot"), "-o", str(OUT / "source-subject-atlas.svg")], check=True)
    subject_lines = ["# Complete source subject inventory", "", f"All {len(groups)} two-component source groups are listed. Counts sum to {inventory['local_modules']:,} local files. These are namespace groups, not independent mathematical modules.", "", "| Source group | Files |", "| --- | ---: |"]
    subject_lines += [f"| `{name}` | {count:,} |" for name, count in groups.items()]
    (OUT / "source-subjects.md").write_text("\n".join(subject_lines) + "\n")

    outputs = [OUT / n for n in ["full-proof-program.md", "endpoint-field-ledger.md", "source-subject-atlas.dot", "source-subject-atlas.svg", "source-subjects.md"]]
    record = {"scope": "Coverage of work-package ids, exact endpoint-field allocation, and complete source namespace partition. Not mathematical proof verification.",
              "work_packages": len(works), "endpoint_fields": len(fields), "source_modules": inventory["local_modules"],
              "source_groups": len(groups), "displayed_source_groups": len(partition), "passed": True,
              "inputs": {str(p.relative_to(ROOT)): sha(p) for p in [model_path, endpoint_path, inventory_path]},
              "evidence_checkpoints": {path: sha(ROOT / path) for path in model.get("evidence", [])},
              "outputs": {str(p.relative_to(ROOT)): sha(p) for p in outputs}, "script_sha256": sha(Path(__file__))}
    (ROOT / "certificates/full-proof-program-check.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({k: record[k] for k in ["passed", "work_packages", "endpoint_fields", "source_modules", "source_groups"]}))


if __name__ == "__main__":
    main()
