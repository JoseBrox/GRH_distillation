#!/usr/bin/env python3
"""Render the public roadmap, technical interfaces and complete section atlas.

The work-interface arrows are curated mathematical obligations. The separate
section atlas shows documentary references, including forward pointers; it is
explicitly not a logical proof DAG. No source is downloaded by this script.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import textwrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "blueprint"
BUILD = ROOT / "build/blueprint"
MODEL = OUT / "proof-blueprint.json"
ALLOCATION = ROOT / "certificates/proof-architecture-allocation.json"


def q(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def title_plain(value: str) -> str:
    value = re.sub(r"\\texorpdfstring\{\$K\$\}\{K\}", "K", value)
    return value.replace("\\", "").replace("{", "").replace("}", "").replace("$", "")


def graph_header(title: str, *, size: float = 12) -> list[str]:
    return ["digraph proof {",
            'graph [rankdir=TB, bgcolor="white", pad="0.24", nodesep="0.30", ranksep="0.48",',
            f'  fontname="DejaVu Sans", fontsize={size}, labelloc=t, label={q(title)}, splines=polyline];',
            'node [shape=box, style="rounded,filled", fontname="DejaVu Sans", fontsize=11,',
            '  margin="0.18,0.12", penwidth=1.3];',
            'edge [color="#64748B", penwidth=1.1, arrowsize=0.65];']


def render(name: str, lines: list[str]) -> None:
    dot = OUT / (name + ".dot")
    dot.write_text("\n".join(lines + ["}"]) + "\n")
    subprocess.run(["dot", "-Tsvg", str(dot), "-o", str(OUT / (name + ".svg"))], check=True)
    if name != "module-atlas":
        subprocess.run(["dot", "-Tpng", "-Gdpi=125", str(dot), "-o", str(BUILD / (name + ".png"))], check=True)


def interface_graph(spec: dict, colors: dict) -> list[str]:
    """Render the curated arrows; invisible edges only order layout rows."""
    ids = {n["id"] for n in spec["nodes"]}
    assert len(ids) == len(spec["nodes"]), "Duplicate work-interface id"
    lines = graph_header(spec["title"])
    layout = spec.get("layout", {})
    if layout:
        lines.append(f'graph [nodesep={q(str(layout["nodesep"]))}, ranksep={q(str(layout["ranksep"]))}];')
    for node in spec["nodes"]:
        c = colors[node["status"]]
        title = node["title"]
        if layout.get("wrap_columns"):
            title = "\n".join(textwrap.fill(part, width=layout["wrap_columns"],
                                           break_long_words=False, break_on_hyphens=False)
                              for part in title.split("\n"))
        label = title + "\n" + c["label"]
        lines.append(f'{q(node["id"])} [label={q(label)}, fillcolor={q(c["fill"])}, color={q(c["border"])}, fontcolor={q(c["text"])}];')
    for source, target in spec["edges"]:
        assert source in ids and target in ids, "Missing edge endpoint"
        lines.append(f"{q(source)} -> {q(target)};")
    rows = spec.get("ranks", [])
    for row in rows:
        assert all(n in ids for n in row)
        lines.append("{rank=same; " + "; ".join(q(n) for n in row) + ";}")
    if layout.get("ordered_ranks"):
        assigned = [node for row in rows for node in row]
        assert len(assigned) == len(set(assigned)) and set(assigned) == ids
        assert max(map(len, rows)) <= layout["max_nodes_per_rank"] <= 5
        rank_of = {node: i for i, row in enumerate(rows) for node in row}
        assert all(rank_of[a] < rank_of[b] for a, b in spec["edges"]), "A mathematical arrow goes against the ordered layout"
        lines.append('// Invisible edges below control layout only; they are not proof interfaces.')
        for row in rows:
            for left, right in zip(row, row[1:]):
                lines.append(f'{q(left)} -> {q(right)} [style=invis, weight=50];')
        for upper, lower in zip(rows, rows[1:]):
            lines.append(f'{q(upper[0])} -> {q(lower[0])} [style=invis, weight=50];')
    return lines


def main() -> None:
    OUT.mkdir(exist_ok=True)
    BUILD.mkdir(parents=True, exist_ok=True)
    model = json.loads(MODEL.read_text())
    allocation = json.loads(ALLOCATION.read_text())
    colors = model["statuses"]
    for name in ["overview", "technical"]:
        render(name, interface_graph(model[name], colors))

    modules = [dict(n) for n in allocation["nodes"]]
    known = {n["path"] for n in modules}
    main_tex = (ROOT / "paper/main.tex").read_text()
    input_matches = list(re.finditer(r"\\input\{(sections/[^}]+)\}", main_tex))
    actual = {"paper/" + m[1] + ".tex" for m in input_matches}
    for path in sorted(actual - known):
        if path == "paper/sections/new/jacquet-integrated-descent.tex":
            text = (ROOT / path).read_text()
            modules.append({"id": "n-integrated-descent", "path": path,
                            "title_tex": re.search(r"\\section\{([^}]+)\}", text)[1],
                            "package": "radial_jacquet", "role": "primary", "status": "new"})
        else:
            raise ValueError("Unallocated new mathematical section: " + path)
    assert actual == {n["path"] for n in modules}, "Section inventory differs from actual manuscript inputs"
    assert len({n["id"] for n in modules}) == len(modules)
    appendix_at = main_tex.find(r"\appendix")
    labels = {}
    for n in modules:
        text = (ROOT / n["path"]).read_text()
        n["source_sha256"] = hashlib.sha256(text.encode()).hexdigest()
        n["labels"] = re.findall(r"\\label\{([^}]+)\}", text)
        for label in n["labels"]:
            assert label not in labels, "Duplicate manuscript label: " + label
            labels[label] = n["id"]
        match = next(m for m in input_matches if "paper/" + m[1] + ".tex" == n["path"])
        n["placement"] = "alternative appendix" if appendix_at >= 0 and match.start() > appendix_at else "preferred exposition"
        if n["role"] == "alternative":
            assert n["placement"] == "alternative appendix", "Alternative remains in preferred flow"
    for name in ["overview", "technical"]:
        for node in model[name]["nodes"]:
            for evidence in node.get("evidence", []):
                assert evidence in labels or (ROOT / evidence).is_file(), ("Missing mathematical evidence target", name, node["id"], evidence)
    documentary_edges = set()
    for n in modules:
        text = (ROOT / n["path"]).read_text()
        for label in re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", text):
            target = labels.get(label)
            if target and target != n["id"]:
                documentary_edges.add((n["id"], target))
    inventory = {"scope": model["scope"], "edge_semantics": "Documentary citations, not certified proof premises.",
                 "module_count": len(modules), "alternative_count": sum(n["role"] == "alternative" for n in modules),
                 "preferred_exposition_count": sum(n["placement"] == "preferred exposition" for n in modules),
                 "modules": modules, "documentary_edges": sorted(documentary_edges)}
    (OUT / "module-inventory.json").write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n")

    atlas = graph_header("Complete manuscript section-reference atlas\nArrows mean cites; this is not a proof DAG", size=16)
    atlas += ['graph [nodesep="0.15", ranksep="0.32"];', 'node [fontsize=9, margin="0.12,0.08"];',
              'edge [color="#B2BBC5", penwidth=0.6, arrowsize=0.4];']
    for package in allocation["packages"]:
        atlas.append("subgraph " + q("cluster_" + package["id"]) + " {")
        atlas.append('style="rounded"; color="#CBD5E1"; label=' + q(package["title"]) + ";")
        for n in modules:
            if n["package"] != package["id"]:
                continue
            status = "alternative" if n["role"] == "alternative" else ("open" if n["status"] == "open" else "context")
            if n["status"] == "new" and n["role"] != "alternative":
                status = "written"
            c = colors[status]
            label = n["id"] + "\n" + title_plain(n["title_tex"])
            atlas.append(f'{q(n["id"])} [label={q(label)}, fillcolor={q(c["fill"])}, color={q(c["border"])}, fontcolor={q(c["text"])}];')
        atlas.append("}")
    for source, target in sorted(documentary_edges):
        atlas.append(f"{q(source)} -> {q(target)};")
    render("module-atlas", atlas)

    rows = ["# Complete manuscript section inventory", "", model["scope"], "",
            "Stable identifiers refer to recovered source sections, not the renumbered PDF. 'Recovered' means a proof text is present; it does not report a fresh audit of every argument.", "",
            f"Coverage: **{len(modules)} section files**, **{inventory['preferred_exposition_count']} in the preferred exposition**, **{inventory['alternative_count']} in the alternative appendix**.", "",
            "The preferred exposition still contains mixed sections and context. This is not a count of minimal independent lemmas. In particular, only the early class-number, cyclotomic-degree and unit arguments of r16/r17 are used by the shortened coarse route.", "",
            "| Stable id | Mathematical section | Package | Role | Record | Placement | References to sections |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for n in modules:
        targets = sorted(b for a, b in documentary_edges if a == n["id"])
        rows.append("| " + " | ".join([n["id"], "[" + title_plain(n["title_tex"]) + "](../" + n["path"] + ")", n["package"], n["role"], n["status"], n["placement"], ", ".join(targets) or "—"]) + " |")
    (OUT / "module-inventory.md").write_text("\n".join(rows) + "\n")
    certificate = {"scope": "Structural coverage, valid graph endpoints and deterministic diagram generation; no mathematical proof certification.",
                   "module_count": len(modules), "alternative_count": inventory["alternative_count"],
                   "preferred_exposition_count": inventory["preferred_exposition_count"], "documentary_edges": len(documentary_edges),
                   "input_hashes": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in [MODEL, ALLOCATION, ROOT / "paper/main.tex"]},
                   "outputs": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.glob("*")) if p.suffix in {".svg", ".dot", ".json"}},
                   "passed": True}
    (ROOT / "certificates/blueprint-check.json").write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({k: certificate[k] for k in ["passed", "module_count", "alternative_count", "preferred_exposition_count", "documentary_edges"]}))


if __name__ == "__main__":
    main()
