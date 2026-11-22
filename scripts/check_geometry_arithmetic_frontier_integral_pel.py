#!/usr/bin/env python3
"""Authenticate the actual local Model supplier and exact finite level checks.

The shared proof and cited construction theorems establish the Model.
The finite calculations check cyclotomic completion and principal-unit
normalizations; no Lean build or full PartI proof is claimed.
"""
from __future__ import annotations

import argparse
import json
from math import gcd, lcm
from pathlib import Path
from urllib.request import urlopen

import check_geometry_arithmetic_frontier_geometric_filtration as auth


STEM = "geometry-arithmetic-frontier-integral-pel"
T = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry.ToroidalCompactification."
RANGES = {
    T + "TwoWeightEqOneAddRoot": [(14, 68), (72, 82), (125, 166)],
    T + "PushInvertible": [(29, 66)],
    T + "Clauses": [(90, 121), (154, 171)],
    T + "UniformisationConclusion": [(83, 128), (223, 229)],
    "Development.AbelianVarietyTheory.Definitions.PlaceAdaptation.AdaptStd": [(140, 150)],
}

REFERENCES = [
    {"path": "build/reference-cache/lan-pel-revision.pdf",
     "url": "https://www.kwlan.org/articles/cpt-PEL-type-thesis-revision.pdf",
     "sha256": "a7a454f5d0735f4bf11f00a8afc14c361c5fc2cefd691d7466f7620ab4c3a079",
     "text_path": "build/reference-cache/lan-pel-revision.txt",
     "text_sha256": "f0b305b0a54e5557c5b9420526ccf79b90c42cf236e91f78e2645868f649af58",
     "ranges": [(5440, 5470), (9980, 10012), (21411, 21448), (24900, 24936)],
     "items": ["Remark 1.4.1.9: full prime-to-p congruence level at least three is neat",
               "Proposition 3.3.2.2: cubical extension is fully faithful over a normal base",
               "Theorem 3.3.2.3(2): symmetric cubical generic line extends",
               "Definition 5.3.2.1: tautological semiabelian and coefficient structure",
               "Section 6.2.5: boundary torus has its cusp character group"]},
    {"path": "build/reference-cache/lan-cpt-ram-nbl.pdf",
     "url": "https://www.kwlan.org/articles/cpt-ram-nbl.pdf",
     "sha256": "ff2229d32fc6dd99174d8ff392ebdf6c93c3a455118bd7d54f54a74a967d31ac",
     "text_path": "build/reference-cache/lan-cpt-ram-nbl.txt",
     "text_sha256": "f48dd9b464405c1782674ad064af347e34a566249cf03dd4668b258be54487d5",
     "ranges": [(290, 316), (1780, 1835), (1870, 1930)],
     "items": ["Proposition 2.8: projective compatible cone decompositions exist",
               "Theorem 6.1: actual normal projective flat ramified model and semiabelian family",
               "Theorem 6.1(3)-(4): boundary strata and formal Mumford identifications"]},
    {"path": "build/reference-cache/lan-cpt-ram-flat.pdf",
     "url": "https://www.kwlan.org/articles/cpt-ram-flat.pdf",
     "sha256": "dbe7d5c3488693bad792def9f7245bdea5657174455e15e32bef607c93d801d2",
     "text_path": "build/reference-cache/lan-cpt-ram-flat.txt",
     "text_sha256": "3619dbd1e1794c54fb7b70566cc8b3d884295de6e170ca7e95a47042432bc2de",
     "ranges": [(330, 345), (380, 420), (4195, 4235)],
     "items": ["Example 2.3: singleton original lattice with no isogeny twist",
               "Prime-to-p neatness standing hypothesis",
               "Theorem 11.2: exact family over formal charts"]},
]


def references(offline):
    records = []
    for ref in REFERENCES:
        path = auth.ROOT/ref["path"]
        if not path.exists() and not offline:
            path.parent.mkdir(parents=True, exist_ok=True)
            with urlopen(ref["url"], timeout=30) as response:
                path.write_bytes(response.read())
        assert auth.sha(path.read_bytes()) == ref["sha256"]
        data = (auth.ROOT/ref["text_path"]).read_bytes()
        assert auth.sha(data) == ref["text_sha256"]
        lines = data.splitlines(keepends=True)
        excerpts = []
        for lo, hi in ref["ranges"]:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            bounded = b"".join(lines[lo-1:hi])
            assert len(bounded) <= 12000
            excerpts.append({"lines": [lo, hi], "sha256": auth.sha(bounded)})
        records.append({**ref, "authenticated_text_excerpts": excerpts})
    return records


def finite_level_checks():
    """Exact split rank-one checks, including shared level prime powers."""
    roots = glue = shared = 0
    for M in range(3, 32, 2):
        for A in range(1, 25):
            L, d = lcm(M,A), gcd(M,A)
            # The torsion gluing map is injective with the exact image.
            image = {(x % M, x % A) for x in range(L)}
            target = {(x,y) for x in range(M) for y in range(A)
                      if (x-y) % d == 0}
            assert len(image) == L and image == target
            glue += 1
            shared += d > 1
            # In the split model a Tate multiplier r fixing full A has
            # u=(1,r); fixed half + fixed root uniquely forces u=(1,1)
            # modulo M. Count all possible finite cyclotomic adjustments.
            for r in range(L):
                if gcd(r,L) != 1 or (r-1) % A:
                    continue
                assert (r-1) % d == 0
                assert 1*r % L == r
                assert (r % A) == (1 % A)
                if (r-1) % M == 0:
                    assert (r-1) % L == 0
                roots += 1
    # Without the fixed M-root the missing marking is genuinely not unique.
    M, A, r = 9, 3, 4
    assert r % A == 1 and r % M != 1 and gcd(r,M) == 1
    negative = {"M": M, "A": A, "half_factor": 1,
                "other_factor": r,
                "reason": "Same half and full-A labels, different full-M marking and M-root; fixed original cyclotomic component is essential."}
    return {"torsion_gluing_cases": glue, "shared_level_factor_cases": shared,
            "compatible_cyclotomic_multipliers": roots,
            "negative_control_without_fixed_root": negative}


def principal_norm_checks():
    """Exact unramified norm at two and three on principal units.

    Use w^2+w+1 at 2 and w^2+1 at 3. The theorem for every
    unramified local extension is the trace-lifting proof in the text.
    """
    cases = []
    for p, trace, norm in [(2,-1,1), (3,0,1)]:
        for depth in range(2,6):
            modulus = p**depth
            for order in range(1,depth):
                step = p**order
                image = {(x*x+trace*x*y+norm*y*y) % modulus
                         for x in range(1,modulus,step)
                         for y in range(0,modulus,step)}
                wanted = {x for x in range(modulus) if (x-1) % step == 0}
                assert image == wanted
                cases.append({"prime": p, "depth": depth,
                              "principal_unit_order": order,
                              "image_cardinality": len(image)})
    return cases


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    refs = references(args.offline)
    level = finite_level_checks()
    norms = principal_norm_checks()
    paths = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", "scripts/"+Path(__file__).name]
    record = {
        "date": "2026-11-22", "status": "PASS", "whole_nodes_newly_closed": 0,
        "classification": "Closed actual individual integral Model supplier at every original GoodAt prime",
        "proved": ["Half-M/full-A is equivalent to prescribed-root full-lcm level over the original Coeff field",
                   "Exact full-Tate liftability with all common M,A prime powers retained",
                   "Actual principal prime-to-p neatness",
                   "Normal flat projective local model with original semiabelian coefficient family",
                   "Unique extension of the exact primitive cubical line and generic abelian locus"],
        "remaining": ["PushInvertible and coordinated LevelStructureConditions",
                      "Full literal PELUnif and TorsionIso supplier",
                      "Global domination and coordinated finite level transitions",
                      "Good-cover, height, section, cusp and raw global theta estimates"],
        "sources": sources, "references": refs,
        "finite_level_models": level, "principal_unit_norm_models": norms,
        "artifacts": [{"path": p, "sha256": auth.sha((auth.ROOT/p).read_bytes())} for p in paths],
        "scope": "Source/reference byte authentication and finite exact checks supplement the standard proof and cited Lan construction theorems. No Lean build; no full PartI or whole-node closure.",
        "reproduce": "python3 scripts/"+Path(__file__).name+" --offline",
    }
    (auth.ROOT/"certificates"/(STEM+".json")).write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "primary_references": len(refs), "gluing_cases": level["torsion_gluing_cases"],
                      "shared_level_cases": level["shared_level_factor_cases"],
                      "principal_unit_norm_cases": len(norms)}))


if __name__ == "__main__":
    main()
