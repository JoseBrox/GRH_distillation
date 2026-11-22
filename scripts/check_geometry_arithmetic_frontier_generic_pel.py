#!/usr/bin/env python3
"""Authenticate the exact generic PEL supplier and finite local norm checks.

Representability is proved in the shared mathematics using Lan's theorems.
These checks do not construct a global integral model or compile Lean.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.request import urlopen

import check_geometry_arithmetic_frontier_geometric_filtration as auth

STEM = "geometry-arithmetic-frontier-generic-pel"
G = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry."
RANGES = {
    G + "BirationalGeometry.ToroidalCompactification.TwoWeightEqOneAddRoot":
        [(14, 68), (72, 82), (132, 166)],
    G + "BirationalGeometry.ToroidalCompactification.PushInvertible":
        [(12, 38), (52, 66)],
    G + "ExtensionDescent.ConstGen": [(18, 56)],
    G + "ExtensionDescent.NonzeroLocus": [(33, 57)],
}
REFERENCE = {
    "path": "build/reference-cache/lan-pel-revision.pdf",
    "url": "https://www.kwlan.org/articles/cpt-PEL-type-thesis-revision.pdf",
    "sha256": "a7a454f5d0735f4bf11f00a8afc14c361c5fc2cefd691d7466f7620ab4c3a079",
    "version": "Author's revision, 14 March 2021",
    "items": ["Definition 1.2.1.2", "Definition 1.3.7.6", "Definition 1.4.1.4",
              "Theorem 1.4.1.11", "Lemma 2.3.3.1", "Definition 5.2.4.6",
              "Proposition 5.2.4.9", "Corollary 7.2.3.10"],
}


def finite_norm_checks():
    """Norm of x+y*w for unramified quadratic rings at 2 and 3.

    w^2+w+1 at 2, w^2+1 at 3. Exhaustion is exact and small;
    the all-prime proof in the text uses residue norm and trace lifting.
    """
    cases = []
    for p, trace, norm in [(2, -1, 1), (3, 0, 1)]:
        for depth in range(1, 5):
            modulus = p**depth
            residues = {(x*x+trace*x*y+norm*y*y) % modulus
                        for x in range(modulus) for y in range(modulus)}
            units = {a for a in range(modulus) if a % p}
            assert units <= residues
            pair = next((x, y) for x in range(modulus) for y in range(modulus)
                        if (x*x+trace*x*y+norm*y*y+1) % modulus == 0)
            cases.append({"prime": p, "depth": depth, "norm_minus_one_witness": pair})
    return cases


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    refpath = auth.ROOT / REFERENCE["path"]
    if not refpath.exists() and not args.offline:
        refpath.parent.mkdir(parents=True, exist_ok=True)
        with urlopen(REFERENCE["url"], timeout=30) as response:
            refpath.write_bytes(response.read())
    assert auth.sha(refpath.read_bytes()) == REFERENCE["sha256"]
    paths = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", "scripts/" + Path(__file__).name]
    record = {
        "status": "PASS", "date": "2026-11-22", "whole_nodes_newly_closed": 0,
        "classification": "Closed exact generic Moduli construction subobligation of W10",
        "proved": ["Canonical primitive rigidified cubical line",
                   "Half-level automorphism rigidity using the perfect integral pairing",
                   "Exact full-Tate and finite-label comparison, including the pairing sign",
                   "Generic smooth quasi-projective fine moduli scheme over the original K_A"],
        "remaining": ["Integral normal flat projective Model and original semiabelian line extension",
                      "Good3 charts and prescribed level transitions",
                      "Metric, height, section, cusp and global theta estimates"],
        "sources": sources, "primary_reference": REFERENCE,
        "finite_norm_models": finite_norm_checks(),
        "artifacts": [{"path": p, "sha256": auth.sha((auth.ROOT/p).read_bytes())} for p in paths],
        "scope": "Pinned byte checks and finite models supplement the written proof; no Lean build or integral-model construction.",
        "reproduce": "python scripts/" + Path(__file__).name + " --offline",
    }
    (auth.ROOT / "certificates" / (STEM + ".json")).write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "authenticated_sources": len(sources),
                      "finite_norm_cases": len(record["finite_norm_models"])}))


if __name__ == "__main__":
    main()
