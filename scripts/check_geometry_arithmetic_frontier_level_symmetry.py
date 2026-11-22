#!/usr/bin/env python3
"""Authenticate the exact level-action and generic-descent suppliers.

The finite checks verify the root action, not existence of a compactification.
The latter is proved in the shared text using the authenticated references.
"""
from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path
from urllib.request import Request, urlopen

import check_geometry_arithmetic_frontier_geometric_filtration as auth
import check_geometry_arithmetic_frontier_integral_pel as pel


STEM = "geometry-arithmetic-frontier-level-symmetry"
T = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry.ToroidalCompactification."
RANGES = {
    T + "TwoWeightEqOneAddRoot": [(14, 68), (72, 82)],
    T + "PushInvertible": [(68, 95), (106, 124)],
    T + "Clauses": [(105, 121), (154, 171)],
}

STACKS = {
    "01ZM": "f24dc66991adbc1a0c758cb5bf409ca15f4fbf78c306608006471fa4a3aa88ce",
    "0C0C": "cd0b5d0acd5b5f8575639b6c02c22db3feb258112f02cab8e6bdf16f51c5698b",
    "081F": "3de17126874c2a028f8a81f18f7a5ae9f6c8b08738fa16c27c57cefc429af789",
    "0E0N": "f9d1aad04b2739a97523e274106e044d74a7a66470791ca3928bc737672003a2",
    "07QS": "719094ee28bf5a8c012ab9cbac9309865bb120a3a136ef8f34c5c423a39a05a6",
    "07QV": "55fba694608fe9d0f076284dab82f15501e4502264611bce395395cc3e70e19f",
}


def approximation_references(offline):
    records = []
    for tag, expected in STACKS.items():
        url = "https://stacks.math.columbia.edu/tag/"+tag
        path = auth.ROOT/"build/reference-cache"/("stacks-"+tag+".html")
        if not path.exists() and not offline:
            with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=25) as response:
                path.write_bytes(response.read())
        data = path.read_bytes()
        assert auth.sha(data) == expected, (tag, "reference bytes changed; rereview required")
        records.append({"tag": tag, "url": url, "sha256": expected, "bytes": len(data)})
    return records


def root_actions():
    moduli = actions = 0
    for m in range(3, 100, 2):
        units = [x for x in range(m) if gcd(x, m) == 1]
        for primitive in units:
            orbit = {(r*primitive) % m for r in units}
            assert orbit == set(units)
            assert [r for r in units if (r*primitive) % m == primitive] == [1]
            actions += len(units)
        moduli += 1
    return {"odd_moduli": moduli, "exact_root_actions": actions,
            "all_stabilizers_trivial": True,
            "scope": "Exact split rank-one finite multiplier model; the general group and scheme assertions are proved in the text."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    refs = [dict(pel.REFERENCES[0]), dict(pel.REFERENCES[1]), dict(pel.REFERENCES[2])]
    refs[0]["ranges"] = [(9920, 9940), (9980, 10012), (10635, 10683)]
    refs[0]["items"] = ["Normal-base full faithfulness for semiabelian families and cubical lines", "Generic ampleness criterion after normal local completion"]
    refs[1]["ranges"] = [(290, 316), (2200, 2252), (2253, 2288)]
    refs[1]["items"] = ["Invariant projective fans under the compact normalizer", "Exact tautological-family pullback for level and Hecke maps"]
    refs[2]["ranges"] = [(5150, 5178)]
    refs[2]["items"] = ["Scope check: Proposition13.19 gives finite interior/minimal maps; it is not used as a theorem of finite toroidal transitions"]
    pel.REFERENCES = refs
    references = pel.references(args.offline)
    paths = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
             f"paper/shared/{STEM}-references.tex", "scripts/"+Path(__file__).name]
    record = {
        "date": "2026-11-22", "status": "PASS",
        "classification": "Closed original LevelActs, A=1 Descends, prime-to-p Extends and full GoodRedExt subobligations",
        "whole_nodes_newly_closed": 0,
        "exact_conditions": ["Original coefficient field and level labels", "Singleton original Tate lattice", "Invariant projective fan", "Actual primitive cubical line and rigidification", "No Galois assumption on the coefficient-field extension"],
        "valuation_scope": "Every original valuation ring with its prescribed fraction field, including both discrete and nondiscrete classes; no field enlargement. Normal finite approximation is over the original excellent arithmetic DVR.",
        "remaining": ["Simultaneous finite transitions and SiegelCompare", "Global domination", "Arithmetic height, section and global norm estimates"],
        "sources": sources, "references": references,
        "approximation_references": approximation_references(args.offline),
        "finite_root_action": root_actions(),
        "artifacts": [{"path": p, "sha256": auth.sha((auth.ROOT/p).read_bytes())} for p in paths],
        "scope": "Bounded source/reference authentication and exact finite checks supplement the standard mathematical proof. No Lean build or full node closure.",
        "reproduce": "python scripts/"+Path(__file__).name+" --offline",
    }
    (auth.ROOT/"certificates"/(STEM+".json")).write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "primary_references": len(references), **record["finite_root_action"]}))


if __name__ == "__main__":
    main()
