#!/usr/bin/env python3
"""Synchronize the two proof routes and report genuine node-status changes.

Counts refer to stated mathematical interfaces, not fractions of a proof.
This checks organization and evidence locations; it does not prove a theorem.
"""
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "blueprint"
FINISHED = {"written", "cited"}


def relocate(text, source, destination):
    def replace(match):
        target = match[1]
        if target.startswith("#") or re.match(r"[a-zA-Z]+:", target):
            return match[0]
        path, separator, anchor = target.partition("#")
        path = os.path.relpath((source / path).resolve(), destination)
        return "](" + path + (separator + anchor if separator else "") + ")"
    return re.sub(r"\]\(([^)\s]+)\)", replace, text)


def main():
    for script in ["build_full_proof_program.py", "build_blueprint.py"]:
        subprocess.run(["python", str(ROOT / "scripts" / script)], cwd=ROOT, check=True)
    for source, destination in [("full-proof-program.md", "grh/program.md"),
                                ("endpoint-field-ledger.md", "grh/field-ledger.md")]:
        source, destination = OUT / source, OUT / destination
        text = relocate(source.read_text(), source.parent, destination.parent)
        text = text.replace("../full-proof-program.md", "program.md")
        text = text.replace("../endpoint-field-ledger.md", "field-ledger.md")
        destination.write_text(text)
    source, destination = OUT / "rh/program.md", OUT / "rh-proof-program.md"
    destination.write_text(relocate(source.read_text(), source.parent, destination.parent))

    model = json.loads((OUT / "proof-blueprint.json").read_text())
    baseline = json.loads((ROOT / "certificates/route-status-baseline.json").read_text())
    previous_path = OUT / "progress.json"
    previous = json.loads(previous_path.read_text()) if previous_path.exists() else baseline
    history_path = ROOT / "certificates/node-completions.json"
    history = json.loads(history_path.read_text()) if history_path.exists() else {
        "scope": "Changes of mathematical node status after the fixed route baseline. New nodes and reorganizations are recorded separately from closing an existing open node.",
        "baseline_commit": baseline["basis_commit"], "events": []}
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    maps, changes = {}, []
    for key, title in [("rh", "Ordinary RH"), ("technical", "Dirichlet GRH: technical map"),
                       ("overview", "Shared overview")]:
        nodes = {node["id"]: node["status"] for node in model[key]["nodes"]}
        counts = Counter(nodes.values())
        maps[key] = {"title": title, "total": len(nodes),
                     "finished": sum(n in FINISHED for n in nodes.values()),
                     "status_counts": dict(counts), "nodes": nodes}
        old = previous["maps"].get(key, {}).get("nodes", {})
        for node, status in nodes.items():
            if node in old and old[node] not in FINISHED and status in FINISHED:
                changes.append({"kind": "completed_existing_node", "map": key, "node": node,
                                "previous_status": old[node], "status": status,
                                "finished": maps[key]["finished"], "total": len(nodes),
                                "based_on_commit": head})
            elif node not in old:
                changes.append({"kind": "new_node", "map": key, "node": node, "status": status,
                                "based_on_commit": head})
            elif old[node] in FINISHED and status not in FINISHED:
                changes.append({"kind": "reopened_node", "map": key, "node": node,
                                "status": status, "based_on_commit": head})
        for node in sorted(set(old)-set(nodes)):
            changes.append({"kind": "removed_node", "map": key, "node": node,
                            "based_on_commit": head})
    history["events"].extend(changes)
    history_path.write_text(json.dumps(history, indent=2, ensure_ascii=False)+"\n")
    works = json.loads((OUT / "grh/program.json").read_text())["work_packages"]
    record = {"schema_version": 1, "semantics": baseline["semantics"],
              "finished_statuses": sorted(FINISHED), "maps": maps,
              "work_packages": {"finished": sum(w["status"] in FINISHED for w in works), "total": len(works)},
              "completion_history": "certificates/node-completions.json"}
    previous_path.write_text(json.dumps(record, indent=2, ensure_ascii=False)+"\n")
    lines = ["# Proof-node progress", "", record["semantics"], "",
             "Counts belong to different views of overlapping mathematics and must not be added together.", "",
             "| Blueprint | Finished nodes | Partial | Open | Optional alternatives |",
             "| --- | ---: | ---: | ---: | ---: |"]
    for key, data in maps.items():
        count = data["status_counts"]
        lines.append(f"| {data['title']} | **{data['finished']}/{data['total']}** | {count.get('partial',0)} | {count.get('open',0)} | {count.get('alternative',0)} |")
    lines += ["", "The eleven larger work packages remain a separate measure: "
              f"**{record['work_packages']['finished']}/{len(works)}** are written or supplied. "
              "These counts are not percentages of an RH or GRH proof.", "",
              "The [completion record](../certificates/node-completions.json) distinguishes closing an existing node from adding, removing or reopening one. "
              "The source-import and manuscript-reference atlases are navigation tools and have no mathematical completion score."]
    (OUT / "progress.md").write_text("\n".join(lines)+"\n")
    for route, key in [("rh", "rh"), ("grh", "technical")]:
        (OUT / route / "status.json").write_text(json.dumps(maps[key], indent=2, ensure_ascii=False)+"\n")
    paths = ["paper/grh/main.tex", "blueprint/rh/map.json", "blueprint/rh/program.md",
             "blueprint/grh/map.json", "blueprint/grh/program.json", "blueprint/grh/program.md",
             "blueprint/grh/field-ledger.md", "blueprint/progress.json", "blueprint/progress.md",
             "blueprint/rh/proof.svg", "blueprint/rh/proof.png", "blueprint/grh/proof.svg",
             "blueprint/grh/proof.png", "certificates/node-completions.json"]
    certificate = {"passed": True, "scope": "Route synchronization, stable node counts and status transitions. Not verification of mathematical proofs.",
                   "artifacts": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in paths],
                   "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   "changes_this_run": changes}
    (ROOT / "certificates/route-blueprint-check.json").write_text(json.dumps(certificate, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"counts": {k: f"{v['finished']}/{v['total']}" for k,v in maps.items()},
                      "changes": changes}))


if __name__ == "__main__":
    main()
