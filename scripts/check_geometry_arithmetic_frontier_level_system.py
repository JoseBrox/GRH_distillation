#!/usr/bin/env python3
"""Authenticate the exact simultaneous level and Siegel suppliers.

This is provenance and interface verification for the written proof,
not a finite test promoted to an all-level mathematical theorem.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import check_geometry_arithmetic_frontier_geometric_filtration as auth
import check_geometry_arithmetic_frontier_integral_pel as pel

STEM = "geometry-arithmetic-frontier-level-system"
T = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry.ToroidalCompactification."
RANGES = {
    T+"TwoWeightEqOneAddRoot": [(14, 68), (144, 166)],
    T+"PushInvertible": [(40, 45), (106, 112)],
    T+"Clauses": [(14, 84), (123, 164)],
    T+"UniformisationConclusion": [(223, 227)],
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    refs = [dict(x) for x in pel.REFERENCES]
    refs[0]["ranges"] = [(4008, 4067), (4250, 4340), (4394, 4480),
                          (4574, 4618), (5305, 5365), (5438, 5490),
                          (7631, 7654), (9915, 9940), (29745, 29793)]
    refs[0]["items"] = [
        "Finite presentation, rigidified Picard, exact diagonal polarization",
        "Finite Rosati-compatible endomorphism schemes and infinitesimal rigidity",
        "Fine smooth Siegel spaces and normal-base full faithfulness",
        "Same rational cones under principal level change",
    ]
    refs[1]["ranges"] = [(240, 316), (1780, 1855)]
    refs[1]["items"] = ["Invariant smooth projective fan under the full compact normalizer",
                        "Original projective model and tautological family"]
    refs[2]["ranges"] = [(1295, 1325), (1510, 1540),
                          (2520, 2608), (2693, 2775)]
    refs[2]["items"] = ["Finite actual Siegel map on the generic moduli interior",
                        "Same-lattice auxiliary construction and normalization",
                        "Independence of auxiliary presentation for fixed induced cones"]
    pel.REFERENCES = refs
    references = pel.references(args.offline)
    paths = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
             f"paper/shared/{STEM}-references.tex", "scripts/"+Path(__file__).name]
    record = {
        "date": "2026-11-22", "status": "PASS", "whole_nodes_newly_closed": 0,
        "classification": "Closed original N0 and complete N2 suppliers",
        "quantifiers": ["Every original datum and original admissible level",
                        "Every prime p and W with p nonunit",
                        "Every original Level.Dvd and coefficient-field inclusion",
                        "Every inclusion of the exact valuation subrings",
                        "One auxiliary prime for all M, using Level.fromK",
                        "Nondiscrete valuation rings in SiegelFamily.points"],
        "normalizations": ["The original primitive line and underlying abelian scheme",
                           "The exact Poincare line on A x A and factor-two commutator",
                           "The same rational cones at all levels",
                           "Finite transitions only after the original coefficient base change",
                           "All original components in the normalization",
                           "Both complete label maps and original M/A power relations"],
        "remaining": ["Model.N4 formal arcs", "Arithmetic height and section estimates",
                      "Global period norms and uniform fourth-power assembly"],
        "sources": sources, "primary_references": references,
        "artifacts": [{"path": p, "sha256": auth.sha((auth.ROOT/p).read_bytes())}
                      for p in paths],
        "scope": "Bounded source and primary-reference authentication; the standard all-level proof is in the shared text. No Lean build or numerical verification of the theorem is claimed.",
        "reproduce": "python scripts/"+Path(__file__).name+" --offline",
    }
    (auth.ROOT/"certificates"/(STEM+".json")).write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "primary_references": len(references), "numerical_proof_claim": False}))


if __name__ == "__main__":
    main()
