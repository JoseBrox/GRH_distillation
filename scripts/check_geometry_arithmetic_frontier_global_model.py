#!/usr/bin/env python3
"""Authenticate the original all-place arithmetic model construction.

This is a source and primary-reference interface certificate for the
written proof. There is no numerical theorem here and no finite toy
model is promoted to a proof of the geometric construction.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import check_geometry_arithmetic_frontier_geometric_filtration as auth
import check_geometry_arithmetic_frontier_dvr_uniformization as dvr


STEM = "geometry-arithmetic-frontier-global-model"
RANGES = {
    dvr.T + "TwoWeightEqOneAddRoot": [(53, 94)],
    dvr.T + "PushInvertible": [(40, 83), (114, 122)],
    dvr.T + "Clauses": [(90, 99), (154, 171)],
}

REFERENCES = [
    {"path": "build/reference-cache/lan-pel-revision.pdf",
     "url": "https://www.kwlan.org/articles/cpt-PEL-type-thesis-revision.pdf",
     "sha256": "a7a454f5d0735f4bf11f00a8afc14c361c5fc2cefd691d7466f7620ab4c3a079",
     "text_path": "build/reference-cache/lan-pel-revision.txt",
     "text_sha256": "f0b305b0a54e5557c5b9420526ccf79b90c42cf236e91f78e2645868f649af58",
     "ranges": [(5305, 5365), (9890, 9942), (9980, 10012),
                (26645, 26725), (29705, 29761)],
     "scope": ["Arbitrary sets of good primes, including a cofinite set",
               "Actual projective arithmetic toroidal scheme and tautological family",
               "Normal-base unique extension of the original group and cubical comparisons"]},
    {"path": "build/reference-cache/lan-cpt-ram-flat.pdf",
     "url": "https://www.kwlan.org/articles/cpt-ram-flat.pdf",
     "sha256": "dbe7d5c3488693bad792def9f7245bdea5657174455e15e32bef607c93d801d2",
     "text_path": "build/reference-cache/lan-cpt-ram-flat.txt",
     "text_sha256": "3619dbd1e1794c54fb7b70566cc8b3d884295de6e170ca7e95a47042432bc2de",
     "ranges": [(2520, 2625), (2693, 2775)],
     "scope": ["Canonical normalization in the original generic PEL function fields",
               "Auxiliary Siegel presentation independence for the same induced cone data"]},
]


def references():
    result = []
    for ref in REFERENCES:
        assert auth.sha((auth.ROOT/ref["path"]).read_bytes()) == ref["sha256"]
        raw = (auth.ROOT/ref["text_path"]).read_bytes()
        assert auth.sha(raw) == ref["text_sha256"]
        lines = raw.splitlines(keepends=True)
        excerpts = []
        for lo, hi in ref["ranges"]:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            piece = b"".join(lines[lo-1:hi])
            assert len(piece) <= 12000
            excerpts.append({"lines": [lo, hi], "sha256": auth.sha(piece)})
        result.append({**ref, "authenticated_text_excerpts": excerpts})
    for tag, expected, scope in [
        ("02KH", "9da5d88e9ba6915ffdea0b6191750eb65dcc108799c35dc54f4f9bad1fc29777",
         "Flat H0 base change for each graded piece of the relatively ample section algebra"),
        ("01VJ", "60b0c8e841ce71071971ddaf548b95ebce51db1b05d3c5867ba8705869308311",
         "The canonical relative-Proj open immersion associated with a relatively ample line"),
        ("0D2P", "dc5eb34e303bb0e3fa910283bf3d44ea8e5683669fbd43da9908a7b52b9b765e",
         "Faithfully flat descent of relative ampleness and the same section-algebra comparison"),
    ]:
        path = "build/reference-cache/stacks-"+tag+".html"
        data = (auth.ROOT/path).read_bytes()
        # Exact retrieved bytes are recorded. These cached primary statements
        # were read independently before the written scheme-descent argument.
        assert auth.sha(data) == expected
        result.append({"path": path, "sha256": auth.sha(data),
                       "url": "https://stacks.math.columbia.edu/tag/"+tag,
                       "scope": scope})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    refs = references()
    paths = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", "scripts/"+Path(__file__).name]
    record = {
        "date": "2026-11-22", "status": "PASS", "whole_nodes_newly_closed": 0,
        "classification": "Closed original N6 global-model construction for the coordinated canonical local models",
        "proved": [
            "Actual arithmetic family over one cofinite good-prime base agrees with canonical local models by localization of normalization",
            "A finite normalized projective graph dominates all remaining exceptional places without changing the generic compactification",
            "The original family and primitive line descend effectively as schemes using their relatively ample section algebras",
            "Every source valuation restriction is exactly the original finite-place DVR",
            "All original Model, generic Descends and universal Dominates fields are retained",
        ],
        "essential_coordination": "One fixed rational cone datum and its canonical normalization presentations; outside finitely many places the local models are localizations of one actual arithmetic model. No claim for an arbitrary infinite collection of independently chosen local blowups.",
        "remaining": ["Finite level transitions and exact SiegelCompare",
                      "Remaining formal boundary/arc compatibility and numerical height/section estimates",
                      "Raw global theta norm and final uniform assembly"],
        "sources": sources, "primary_references": refs,
        "artifacts": [{"path": p, "sha256": auth.sha((auth.ROOT/p).read_bytes())} for p in paths],
        "scope": "Written standard proof and authenticated source/reference interfaces. No Lean build, computational arithmetic estimate, finite transition assertion or whole-node closure.",
        "reproduce": "python3 scripts/"+Path(__file__).name+" --offline",
    }
    (auth.ROOT/"certificates"/(STEM+".json")).write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "primary_references": len(refs), "numerical_proof_claim": False}))


if __name__ == "__main__":
    main()
