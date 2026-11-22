#!/usr/bin/env python3
"""Authenticate bounded source evidence for the finite-place frontier.

This checks immutable source bytes and excerpt bounds only. The general
Frobenius/Artin-length argument is a written proof reviewed separately.
No source theorem, actual boundary identification, or Lean build is
verified by this script.
"""
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
AS = "Development.AutomorphicSpectrum."
SOURCES = [
    (AS + "Statements.GeometryStatements.FinConstFor", [[13, 28]]),
    (AS + "Proofs.GeometryProofs.FlatTheoremOfResolutionGaga", [[19, 22]]),
    (AS + "Proofs.GeometryProofs.FlatTheoremOfParts", [[106, 145]]),
    (AS + "Proofs.GeometryProofs.FiniteConstantAllHolds", [[137, 195]]),
    (AS + "Proofs.GeometryProofs.EigenLinePAdicBound", [[170, 255]]),
    (AS + "Proofs.GeometryProofs.HodgeLatticeDvrDegree",
     [[117, 176], [177, 237]]),
    (AS + "Proofs.GeometryProofs.ValuationBoundedFrame", [[279, 363]]),
    (AS + "Proofs.AlgebraProofs.SplitHermitianGeneratorsExist",
     [[210, 289], [318, 390]]),
    (AS + "Proofs.GeometryProofs.HodgeLatticeValuationAgree", [[12, 43]]),
    (AS + "Proofs.GeometryProofs.LineDegreeSpecialFibre", [[1, 14]]),
    ("ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry."
     "ToroidalCompactification.UniformisationConclusion", [[101, 128]]),
    (AS + "Proofs.GeometryProofs.GermSystemHeightFree", [[1, 22]]),
    (AS + "Proofs.GeometryProofs.FrameFunctionCmHeight",
     [[24, 49], [50, 114]]),
    (AS + "Proofs.GeometryProofs.CmPackPureNorm", [[160, 206], [207, 291]]),
    (AS + "Proofs.AlgebraProofs.DifferentTwistedGeneratorExists", [[38, 57]]),
    (AS + "Proofs.AlgebraProofs.ExistsRealDifferentGenerator", [[1, 9]]),
    (AS + "Proofs.GeometryProofs.FlatDegreeHolds", [[60, 118]]),
]
ARTIFACTS = [
    "notes/flat-family-finite-place-frontier.md",
    "paper/shared/frobenius-character-degree.tex",
    "scripts/check_flat_family_finite_place_frontier.py",
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def check_sources():
    graph_bytes = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(graph_bytes) == inventory["compressed_graph"]["sha256"]
    graph = json.loads(gzip.decompress(graph_bytes))
    assert graph["repository"] == "jsmorph/rh" and graph["commit"] == REV
    entries = {row[0]: row for row in graph["modules"]}
    evidence = []
    for module, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        path = ROOT / "build/source-cache/jsmorph/rh" / REV / rel
        if not path.is_file():
            path = ROOT / "build/lean-mirror" / rel
        raw = path.read_bytes()
        blob = hashlib.sha1(
            b"blob " + str(len(raw)).encode() + b"\0" + raw
        ).hexdigest()
        assert blob == entries[module][1], module
        lines = raw.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            excerpt = b"\n".join(lines[lo - 1:hi]) + b"\n"
            assert len(excerpt) <= 12000, (module, lo, hi)
            excerpts.append({"lines": [lo, hi], "sha256": sha(excerpt)})
        evidence.append({
            "module": module,
            "path": rel,
            "sha256": sha(raw),
            "git_blob_sha1": blob,
            "line_count": len(lines),
            "url": f"https://github.com/jsmorph/rh/blob/{REV}/{rel}",
            "inspected_excerpts": excerpts,
        })
    return evidence


def main():
    evidence = check_sources()
    artifacts = [
        {"path": rel, "sha256": sha((ROOT / rel).read_bytes())}
        for rel in ARTIFACTS
    ]
    certificate = {
        "result": "PASS",
        "scope": "Automated pinned-source provenance and bounded-excerpt checks only.",
        "repository": "jsmorph/rh",
        "revision": REV,
        "source_count": len(evidence),
        "sources": evidence,
        "artifacts": artifacts,
        "written_mathematical_result": (
            "Under the two A-linear Hodge/conjugate filtrations on a smooth "
            "projective curve over a finite field, every idempotent part has "
            "degree zero. Local freeness of its character's Artin factor "
            "then gives degree zero for the character quotient, with the "
            "exact composition-length multiplicity."
        ),
        "independent_review": {
            "record": "certificates/continuation-review-2026-11-22.json",
            "scope": "Separate mathematical review; not performed by this checker.",
        },
        "remaining_open": [
            "Identify the actual boundary Hodge lattice with the two filtered bundles.",
            "Establish coefficient-factor freeness on the actual ramified-prime lattices.",
            "Supply same-model generic determinant identification and finite-place rigidity.",
            "Evaluate actual integral CM frames with the prescribed different and conductor.",
        ],
        "not_verified": [
            "Transitive source theorem proofs",
            "Lean kernel replay or build",
            "Actual geometric flat-family or CM-degree construction",
            "RH or GRH endpoint",
        ],
        "node_counts": {"RH": [6, 9], "GRH": [17, 31]},
    }
    target = ROOT / "certificates/flat-family-finite-place-frontier.json"
    target.write_text(json.dumps(certificate, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "result": "PASS",
        "source_count": len(evidence),
        "certificate": str(target.relative_to(ROOT)),
        "scope": certificate["scope"],
    }))


if __name__ == "__main__":
    main()
