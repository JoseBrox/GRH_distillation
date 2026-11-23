#!/usr/bin/env python3
"""Authenticate the exact N4 construction and check its twist normalizations.

The mathematical proof is the shared TeX, using the actual complete-pair
Mumford construction. Symbolic checks below are limited to the displayed
integral exponents; no finite example proves the geometric theorem.
"""
from __future__ import annotations

import argparse
import json
from itertools import product
from math import lcm
from pathlib import Path

import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth
import check_geometry_arithmetic_frontier_dvr_uniformization as dvr


STEM = "geometry-arithmetic-frontier-formal-arcs"
RANGES = {
    dvr.T + "UniformisationConclusion": [(43, 109), (130, 170), (182, 227)],
    dvr.T + "PushInvertible": [(29, 38), (52, 66)],
    dvr.T + "TwoWeightEqOneAddRoot": [(53, 94), (131, 160)],
    dvr.D + "ThickTransComp": [(42, 114), (164, 192)],
    dvr.D + "DegUnif": [(51, 95), (105, 131), (132, 178)],
    dvr.D + "DegExp": [(91, 144)],
    dvr.D + "DegExpF": [(94, 115)],
    dvr.D + "DegOUnif": [(21, 36)],
    dvr.D + "GtPtBridgeSt": [(29, 76), (90, 143)],
    dvr.D + "QkToAkU": [(16, 21)],
}

REFERENCES = [
    {"path": "build/reference-cache/lan-pel-revision.pdf",
     "url": "https://www.kwlan.org/articles/cpt-PEL-type-thesis-revision.pdf",
     "sha256": "a7a454f5d0735f4bf11f00a8afc14c361c5fc2cefd691d7466f7620ab4c3a079",
     "text_path": "build/reference-cache/lan-pel-revision.txt",
     "text_sha256": "f0b305b0a54e5557c5b9420526ccf79b90c42cf236e91f78e2645868f649af58",
     "ranges": [(9890, 9942), (9980, 10012), (10510, 10555),
                (10580, 10673), (10750, 10805), (10815, 10874),
                (11479, 11545), (11546, 11631), (12870, 12923),
                (13224, 13281), (13760, 13850), (14261, 14318),
                (14406, 14492)],
     "scope": ["Complete noetherian normal pairs and symmetric cubical ampleness",
               "Tensor-compatible actual Mumford equivalence and original primitive line",
               "Character-graded affine charts, period quotient and proper algebraization",
               "All-integer torsion quotient and exact unit-period rank sequence"]},
    {"path": "build/reference-cache/lan-cpt-ram-flat.pdf",
     "url": "https://www.kwlan.org/articles/cpt-ram-flat.pdf",
     "sha256": "dbe7d5c3488693bad792def9f7245bdea5657174455e15e32bef607c93d801d2",
     "text_path": "build/reference-cache/lan-cpt-ram-flat.txt",
     "text_sha256": "3619dbd1e1794c54fb7b70566cc8b3d884295de6e170ca7e95a47042432bc2de",
     "ranges": [(2693, 2775), (4195, 4235), (4227, 4290)],
     "scope": ["The specified cusp filtration, torus argument and centered-valuation cone condition",
               "Actual normal-base extension with all original and auxiliary degenerating families"]},
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
    path = "build/reference-cache/stacks-01VJ.html"
    expected = "60b0c8e841ce71071971ddaf548b95ebce51db1b05d3c5867ba8705869308311"
    assert auth.sha((auth.ROOT/path).read_bytes()) == expected
    result.append({"path": path, "sha256": expected,
                   "url": "https://stacks.math.columbia.edu/tag/01VJ",
                   "scope": "Canonical relative-Proj open immersion for every competing relatively ample line"})
    return result


def exact_twist_checks():
    x1, x2, y1, y2, z1, z2, k = sp.symbols("x1 x2 y1 y2 z1 z2 k")
    X = sp.Matrix([x1, x2])
    Y = sp.Matrix([y1, y2])
    Z = sp.Matrix([z1, z2])
    W = sp.Matrix([[0, -2], [1, 1]])
    B = sp.Matrix([[2, 1], [1, 4]])
    Wbar = sp.eye(2)-W
    assert B.det() == 7 and B[0, 0] > 0
    assert W.T*B == B*Wbar
    assert W*W-W+2*sp.eye(2) == sp.zeros(2)
    bilinear = lambda u, v: sp.expand(u.dot(B*v))
    quadratic = lambda v: sp.expand(bilinear(v, v)/2)
    identities = [
        quadratic(X+Y)-quadratic(X)-quadratic(Y)-bilinear(X, Y),
        bilinear(X, W*X)-quadratic(X),
        bilinear(X, Wbar*X)-quadratic(X),
        quadratic(X+k*Y)-quadratic(X)-k*k*quadratic(Y)-k*bilinear(X, Y),
        bilinear(Y+k*X, Z)-bilinear(Y, Z)-k*bilinear(X, Z),
        bilinear(W*X, Y)-bilinear(X, Wbar*Y),
        bilinear(X, Y)-bilinear(Y, X),
    ]
    assert all(sp.expand(expr) == 0 for expr in identities)
    assert sp.Matrix([-1, 1, 1, -1])+sp.Matrix([1, -2, -1, 2]) == sp.Matrix([0, -1, 0, 1])
    count = 0
    for M, A in [(3, 1), (3, 3), (9, 6), (15, 10), (25, 15), (21, 35)]:
        L = lcm(M, A)
        BB = 2*L*B
        for xx in product(range(-2, 3), repeat=2):
            for yy in product(range(-2, 3), repeat=2):
                xxv, yyv = sp.Matrix(xx), sp.Matrix(yy)
                value = int(xxv.dot(BB*yyv))
                assert value % (2*L) == 0
                assert value % M == value % A == 0
                assert int(xxv.dot(BB*xxv)) % 2 == 0
                count += 1
    return {
        "symbolic_identities": len(identities),
        "integral_exponent_cases": count,
        "primitive_line_exponents": [1, -2, -1, 2],
        "torus_torsion_exponent": "+b(y,chi)/k",
        "period_exponent": "+b(y,y)/2",
        "scope": "Exact algebraic normalization checks, including shared factors in M and A. The rank-two matrix is not asserted to realize an entire admissible source CM host.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    refs = references()
    checks = exact_twist_checks()
    paths = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", "scripts/"+Path(__file__).name]
    record = {
        "date": "2026-11-23", "status": "PASS", "whole_nodes_newly_closed": 0,
        "classification": "Closed original Model.N4 formal-arc construction and exact specialization",
        "proved": [
            "The actual complete-pair degeneration has exactly the prescribed original primitive line, period and selected torsion factors",
            "The original unit-period hypothesis gives one ray in the actual cusp filtration and auxiliary tuple, satisfying the normal-base toroidal criterion",
            "The abelian locus is precisely D(t), with the original generic moduli object on D(varpi*t)",
            "Literal all-thickening expansion multiplication recovers the graded section ring, origin, coefficient action and original labels of any competing source PELUnif",
            "The nonflat evaluation t to varpi commutes with the actual monomial chart algebras, period quotient and proper algebraization",
            "Every permitted evaluation homomorphism is the usual convergent evaluation, giving the complete universal specialization clause",
            "Together with the accepted N0,N2,SplitFibres,N3,N6 constructions this supplies every original PartI field",
        ],
        "essential_hypotheses": [
            "ArcIn.gen requires every original psi to be a unit generator everywhere on O-prime",
            "The positive integral form is coefficient-adjoint and takes values in 2*lcm(M,A)Z",
            "Only half-label inputs on bar(b)Lambda are constrained and used; arbitrary other eta values are not treated as linear",
            "All-power ExpBij is combined with actual common denominators, t_mul, t_unit, gt_t and w_compat",
            "The symmetric cubical generic ample line is relatively ample on every competing source SAB",
            "Specialization uses the monomial construction, not a nonexistent whole-fraction-field map or flat base-change theorem",
        ],
        "remaining": ["Arithmetic section-remainder and height estimates",
                      "Exact quantitative cusp and signed-boundary estimates",
                      "Good-cover field and integral lattice suppliers where separately required",
                      "Global theta norm and final uniform arithmetic assembly"],
        "sources": sources, "primary_references": refs, "exact_checks": checks,
        "artifacts": [{"path": p, "sha256": auth.sha((auth.ROOT/p).read_bytes())} for p in paths],
        "scope": "Written standard proof and authenticated source/reference interfaces; symbolic checks verify displayed twist normalizations only. No Lean build, quantitative arithmetic estimate, or whole proof-map node closure.",
        "reproduce": "python3 scripts/"+Path(__file__).name+" --offline",
    }
    (auth.ROOT/"certificates"/(STEM+".json")).write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "primary_references": len(refs), "exact_checks": checks}))


if __name__ == "__main__":
    main()
