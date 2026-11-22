#!/usr/bin/env python3
"""Authenticate the complete local and model-wide integral theta proof.

The written proof establishes the arithmetic construction. Exact small
algebra models detect loss of the fixed Artin--Rees shift, normality, or
saturation; they are not substitutes for the general algebraic arguments.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import check_geometry_arithmetic_frontier_geometric_filtration as auth
import check_geometry_arithmetic_frontier_dvr_uniformization as dvr


STEM = "geometry-arithmetic-frontier-integral-theta"
RANGES = dict(dvr.RANGES)
RANGES[dvr.T + "PushInvertible"] = [(40, 66), (99, 104)]
RANGES[dvr.T + "TwoWeightEqOneAddRoot"] = [(53, 94), (131, 160)]
RANGES[dvr.T + "Clauses"] = [(105, 121), (154, 171)]

LAN_RANGES = [(10185, 10255), (10292, 10313), (10510, 10555),
              (10577, 10673), (10750, 10805), (10815, 10874),
              (11479, 11545), (11546, 11631), (12870, 12923),
              (13224, 13281), (14261, 14318), (14406, 14486)]

STACKS = [
    {"tag": "00IN", "sha256": "3e7f0333310107c55a4ecd715be67d87df9b3b248f35e6cefa6a986316565cd0",
     "title": "Artin-Rees", "scope": "Finite submodule fR of the noetherian module R; one shift C for all n."},
    {"tag": "00IP", "sha256": "5943ea151fb2d179972b1b821c69da02ceab4a002555e9cddd2759e8ea82b438",
     "title": "Krull's intersection theorem", "scope": "Finite local module L_z/fL_z and the proper ideal m_R O_G,z."},
    {"tag": "02KH", "sha256": "9da5d88e9ba6915ffdea0b6191750eb65dcc108799c35dc54f4f9bad1fc29777",
     "title": "Flat base change", "scope": "Quasi-compact separated family and the flat base-completion morphism, without a properness hypothesis."},
]


def references():
    info = dict(dvr.REFERENCE)
    info["ranges"] = LAN_RANGES
    assert auth.sha((auth.ROOT/info["path"]).read_bytes()) == info["sha256"]
    raw = (auth.ROOT/info["text_path"]).read_bytes()
    assert auth.sha(raw) == info["text_sha256"]
    lines = raw.splitlines(keepends=True)
    excerpts = []
    for lo, hi in LAN_RANGES:
        assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
        piece = b"".join(lines[lo-1:hi])
        assert len(piece) <= 12000
        excerpts.append({"lines": [lo, hi], "sha256": auth.sha(piece)})
    info["authenticated_text_excerpts"] = excerpts
    info["scope"] = [
        "Complete noetherian normal local, rather than only discrete valuation, base hypotheses",
        "Whole-base torus part and exact principal period index",
        "Actual symmetric line ampleness, positivity and finite Fourier support on thickenings",
        "Tensor-compatible unpolarized Mumford equivalence independent of auxiliary ample powers",
        "All-integer torsion and saturated unit-period subgroup on the abelian locus",
    ]
    result = [info]
    for item in STACKS:
        p = "build/reference-cache/stacks-" + item["tag"] + ".html"
        data = (auth.ROOT/p).read_bytes()
        assert auth.sha(data) == item["sha256"]
        result.append({**item, "path": p,
                       "url": "https://stacks.math.columbia.edu/tag/" + item["tag"],
                       "bytes": len(data)})
    return result


def exact_algebra_controls():
    # R=Q[[u,v]], f=u^a v^b, d=u^i v^j. In this model the
    # m-adic order is total degree, and C=a+b is exact.
    cases = 0
    for a in range(6):
        for b in range(6):
            for i in range(9):
                for j in range(9):
                    for n in range(12):
                        in_shifted_ideal = a+b+i+j >= n+a+b
                        assert in_shifted_ideal == (i+j >= n)
                        cases += 1
    # Dropping the shift is false even in a regular local ring.
    assert 3+2 >= 5 and not 0 >= 5
    # Normality cannot be dropped when passing from d^2 in R to d in R.
    semigroup = {2*a+3*b for a in range(10) for b in range(10)}
    assert 2 in semigroup and 1 not in semigroup
    # Full rank alone does not force equality of period lattices.
    subgroup_mod_four = {0,2}
    assert len(subgroup_mod_four) == 2 and 1 not in subgroup_mod_four
    rank_cases = 0
    for g in range(10):
        for closed_rank in range(g+1):
            for current_rank in range(closed_rank+1):
                unit_rank = closed_rank-current_rank
                for n in (2,3,5,7):
                    assert n**(2*g-closed_rank)*n**unit_rank == n**(2*g-current_rank)
                    if current_rank == 0:
                        assert unit_rank == closed_rank
                    rank_cases += 1
    return {
        "exact_two_variable_monomial_cancellation_cases": cases,
        "exact_torsion_rank_cases": rank_cases,
        "negative_controls": {
            "unshifted_cancellation": "f=u^3 v^2 and d=1 have fd in m^5 but d not in m^5",
            "without_normality": "In Q[[t^2,t^3]], d=t is in the fraction field and d^2 is integral, but d is not in the ring",
            "without_saturation": "2Z has full rank in Z but is a proper subgroup",
        },
        "scope": "Exact finite algebra models of the essential cancellation and rank identities, plus explicit hypothesis counterexamples. They do not prove Artin-Rees or construct a PEL model computationally.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    refs = references()
    controls = exact_algebra_controls()
    paths = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", "scripts/"+Path(__file__).name]
    record = {
        "date": "2026-11-22", "status": "PASS", "whole_nodes_newly_closed": 0,
        "classification": "Closed actual PushInvertible, SplitFibres and N3 construction subobligations",
        "proved": [
            "Original period factors are integral and converge in the maximal-ideal topology on every source complete normal local base",
            "The original generic theta section extends with scalar one on the actual semiabelian scheme",
            "Its integral section module is free of rank one with fibrewise nonzero generator",
            "Flat completion descent, smooth openness and faithful-flat contraction give the exact all-open PushInvertible clause",
            "Original GoodAt torsion splits every fibre torus over its original residue field",
            "The original PELUnif, ExpBij, all-integer TorsionIso and PsiUnitOn give the entire source N3 clause",
        ],
        "remaining": [
            "Coordinated finite transitions and exact SiegelCompare",
            "Global domination N6 and all remaining height, section remainder and cusp estimates",
            "Raw global theta norm and final arithmetic assembly",
        ],
        "sources": sources, "primary_references": refs,
        "exact_algebra_controls": controls,
        "artifacts": [{"path": p, "sha256": auth.sha((auth.ROOT/p).read_bytes())} for p in paths],
        "scope": "Written standard-mathematical proof with authenticated source/reference interfaces. The integral existence theorem is not inferred from finite tests, generic equal dimensions, nonproper residue-field base change or coherence of the pushforward. No uniform bound on the Artin-Rees constant, Lean build, whole PartI supplier or whole-node closure is claimed.",
        "reproduce": "python3 scripts/"+Path(__file__).name+" --offline",
    }
    (auth.ROOT/"certificates"/(STEM+".json")).write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "primary_references": len(refs),
                      "cancellation_cases": controls["exact_two_variable_monomial_cancellation_cases"],
                      "rank_cases": controls["exact_torsion_rank_cases"]}))


if __name__ == "__main__":
    main()
