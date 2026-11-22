#!/usr/bin/env python3
"""Authenticate the exact CM-point descent interface and its cited inputs.

This is a provenance checker. The pure-period isogeny, exact labelled
descent and fixed-field proof are mathematical arguments reviewed
separately. No numerical experiment or Lean kernel replay is claimed.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
TOR = ("ReciprocityTheory.ReductiveGroups.ArithmeticGeometry."
       "BirationalGeometry.ToroidalCompactification.")
GEOM = "Development.AutomorphicSpectrum.Proofs.GeometryProofs."
SOURCES = [
    (TOR + "PushInvertible", [[29, 39]]),
    (TOR + "TwoWeightEqOneAddRoot",
     [[14, 25], [30, 39], [53, 64], [72, 91], [131, 166]]),
    (TOR + "IsHolPeriods", [[16, 20], [51, 75], [84, 93]]),
    ("Development.AbelianVarietyTheory.Statements.PrincipalLattices."
     "FiniteDimensionalBase", [[16, 25]]),
    ("Development.WeilBound.CoreStatements.SesquilinearFractions.GRational",
     [[24, 48], [79, 100]]),
    (GEOM + "FamilyPurePeriodsSpan", [[8, 11]]),
    (GEOM + "CmPeriodAlgebraic", [[71, 100], [108, 137]]),
]
PRIMARY = [
    {
        "path": "build/reference-cache/milne-abelian-varieties.pdf",
        "url": "https://jmilne.org/math/CourseNotes/AV.pdf",
        "sha256": "f5ca4e63e5092a4b102daad1470e4cbed5fe8f82115e3a28c8881e3f67f6aaef",
        "inspected": [
            "Theorems 2.8-2.9, pp.14-15: complex tori and algebraic homomorphisms",
            "Remark 8.12, p.39: finite subgroup quotients",
            "Proposition 13.6, pp.58-59: line bundles and alternating Tate pairing",
            "Corollary 16.4, p.68: homomorphism descent over regular extensions",
        ],
        "scope": "Previously reviewed exact descent input; PDF integrity rechecked.",
    },
    {
        "path": "build/reference-cache/milne-modular-functions-2017.pdf",
        "url": "https://www.jmilne.org/math/CourseNotes/MF.pdf",
        "sha256": "977f06a4e838c43c77a7c9398c090789e60d67f64e013e1dcd9bcce0e0c27b8d",
        "inspected": [
            "Corollary 12.9, p.124: algebraicity of j at an imaginary quadratic period",
            "pdftotext -layout, Python splitlines 6909-6921, read in this investigation",
        ],
    },
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_evidence(fetch: bool) -> list[dict]:
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    graph = json.loads(gzip.decompress(packed))
    assert graph["repository"] == "jsmorph/rh" and graph["commit"] == REV
    entries = {row[0]: row for row in graph["modules"]}
    evidence = []
    for module, bounds in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        record = inspect_file({
            "repository": "jsmorph/rh", "commit": REV, "path": path,
            "git_blob_sha1": entries[module][1],
        }, offline=not fetch)
        raw = (ROOT / "build/source-cache/jsmorph/rh" / REV / path).read_bytes()
        lines = raw.splitlines()
        excerpts = []
        for lo, hi in bounds:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpt = b"\n".join(lines[lo-1:hi]) + b"\n"
            assert len(excerpt) <= 12000
            excerpts.append({"lines": [lo, hi], "sha256": sha(excerpt)})
        evidence.append({
            "module": module, "path": path, "sha256": record["sha256"],
            "git_blob_sha1": record["git_blob_sha1"], "inspected_excerpts": excerpts,
            "url": f"https://github.com/jsmorph/rh/blob/{REV}/{path}",
        })
    return evidence


def primary_evidence(fetch: bool) -> list[dict]:
    for item in PRIMARY:
        path = ROOT / item["path"]
        if not path.exists() and fetch:
            request = Request(item["url"], headers={"User-Agent": "Mozilla/5.0"})
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(urlopen(request, timeout=45).read())
        assert sha(path.read_bytes()) == item["sha256"]
    return PRIMARY


def previous_input() -> dict:
    path = "certificates/cm-product-period-calculation.json"
    raw = (ROOT / path).read_bytes()
    record = json.loads(raw)
    assert record["status"] == "PASS" and not record["lean_kernel_replay"]
    note = "notes/cm-product-period-calculation.md"
    expected = next(item["sha256"] for item in record["artifacts"]
                    if item["path"] == note)
    assert sha((ROOT / note).read_bytes()) == expected
    return {
        "certificate": path, "certificate_sha256": sha(raw),
        "note": note, "note_sha256": expected,
        "scope": "Section 3.1 exact symmetric rigidified line and finite-data descent; preserved mathematical review, not rerun proof.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true")
    args = parser.parse_args()
    result = {
        "status": "PASS",
        "automated_scope": "Pinned source and bounded excerpt authentication, primary PDF integrity and frozen CM descent input integrity only.",
        "lean_kernel_replay": False,
        "independent_review": "certificates/frontier-progress-review-2026-11-22.json",
        "sources": source_evidence(args.fetch),
        "primary_references": primary_evidence(args.fetch),
        "previously_reviewed_input": previous_input(),
        "mathematical_results_for_separate_review": [
            "The exact pure finite-index hypothesis gives an isogeny from an algebraic CM elliptic product to the actual universal fibre.",
            "The coefficient action, original symmetric rigidified cubical line and both finite level maps descend over Qbar.",
            "Moduli point separation makes the exact complex point invariant under Aut(C/Qbar); finite type then puts it over a number field.",
            "The original-line comparison and product maps descend after the point is algebraic, without replacing the selected component.",
            "The source's infinite Tate system is existential, not a chosen datum in ObjMap.",
        ],
        "artifacts": [{"path": path, "sha256": sha((ROOT/path).read_bytes())}
                      for path in ["notes/cm-period-point-descent.md",
                                   "scripts/check_cm_period_point_descent.py"]],
        "not_claimed": [
            "Construction of the actual arithmetic moduli model or its pointwise period presentation",
            "Descent of an infinite compatible Tate tower or arbitrary scalar adjunction witnesses",
            "A new proof of the cited classical theorems",
            "An automated mathematical proof or Lean replay",
            "Completion of any RH or GRH proof-map node",
        ],
    }
    (ROOT / "certificates/cm-period-point-descent.json").write_text(
        json.dumps(result, indent=2)+"\n")
    print("PASS: 7 pinned Lean modules, 2 primary PDFs and the frozen CM descent input authenticated.")
    print("Scope: provenance only; mathematical proof reviewed separately, no Lean replay.")


if __name__ == "__main__":
    main()
