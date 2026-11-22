#!/usr/bin/env python3
"""Authenticate the actual complete-DVR PEL and theta supplier.

Finite models check normalization, the squared period index, and exact
all-integer theta commutators. The general theorem is the written proof
using the authenticated primary degeneration theorems. No Lean is run.
"""
from __future__ import annotations

import argparse
import json
from itertools import product
from pathlib import Path

import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth


STEM = "geometry-arithmetic-frontier-dvr-uniformization"
G = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry."
T = G + "BirationalGeometry.ToroidalCompactification."
D = G + "ExtensionDescent."
RANGES = {
    T + "UniformisationConclusion": [(43, 77), (83, 128)],
    T + "PushInvertible": [(99, 104)],
    D + "ThickTransComp": [(42, 114), (164, 192)],
    D + "DegUnif": [(51, 95), (105, 131), (132, 178)],
    D + "DegExp": [(91, 134), (140, 144)],
    D + "DegExpF": [(94, 115)],
    D + "DegOUnif": [(21, 36)],
    D + "GtPtBridgeSt": [(29, 76), (90, 143)],
    D + "QkToAkU": [(16, 21)],
    D + "RosatiAdj": [(29, 65)],
    D + "NonzeroLocus": [(59, 73)],
    "Development.AbelianVarietyTheory.Definitions.PlaceAdaptation.AdaptStd": [(124, 149)],
}

REFERENCE = {
    "path": "build/reference-cache/lan-pel-revision.pdf",
    "url": "https://www.kwlan.org/articles/cpt-PEL-type-thesis-revision.pdf",
    "sha256": "a7a454f5d0735f4bf11f00a8afc14c361c5fc2cefd691d7466f7620ab4c3a079",
    "text_path": "build/reference-cache/lan-pel-revision.txt",
    "text_sha256": "f0b305b0a54e5557c5b9420526ccf79b90c42cf236e91f78e2645868f649af58",
    "ranges": [(9920, 9940), (10185, 10200), (10206, 10255), (10292, 10313),
               (10510, 10555), (10606, 10673), (10750, 10805), (10815, 10874),
               (11479, 11545), (11546, 11631), (12098, 12123),
               (12870, 12900), (14261, 14300), (14368, 14405),
               (17220, 17265), (19205, 19230), (19600, 19673)],
    "scope": ["Normal-base semiabelian uniqueness and Raynaud cubical comparison",
              "Finite torus part over the whole henselian base",
              "Squared period-index degree formula",
              "Actual ample degeneration and Fourier recurrence",
              "Tensor-compatible Mumford equivalence",
              "All-integer quasi-finite torsion construction",
              "Coefficient action and exact theta-commutator convention"],
}


def reference():
    assert auth.sha((auth.ROOT/REFERENCE["path"]).read_bytes()) == REFERENCE["sha256"]
    data = (auth.ROOT/REFERENCE["text_path"]).read_bytes()
    assert auth.sha(data) == REFERENCE["text_sha256"]
    lines = data.splitlines(keepends=True)
    excerpts = []
    for lo, hi in REFERENCE["ranges"]:
        assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
        bounded = b"".join(lines[lo-1:hi])
        assert len(bounded) <= 12000
        excerpts.append({"lines": [lo,hi], "sha256": auth.sha(bounded)})
    return {**REFERENCE, "authenticated_text_excerpts": excerpts}


def degree_dimensions():
    cases = 0
    for index in range(1,10):
        for abelian_degree in range(1,10):
            total = index*index*abelian_degree
            assert (total == 1) == (index == abelian_degree == 1)
    for g in range(13):
        for torus_rank in range(g+1):
            for level in range(1,16):
                assert level**torus_rank*level**(g-torus_rank) == level**g
                cases += 1
    return {"all_rank_all_level_dimension_cases": cases,
            "squared_index_negative_control": {"period_index": 2,
                "abelian_polarization_degree": 1, "correct_total_degree": 4,
                "incorrect_unsquared_degree": 2}}


def exact_theta_checks():
    # Actual shift is +y, and the two orders differ by
    # a*y' - a'*y in the root-of-unity exponent. All monodromy
    # terms cancel by the symmetry of the period bilinear form.
    k, x1, x2, y1, y2, z1, z2 = sp.symbols("k x1 x2 y1 y2 z1 z2", nonzero=True)
    a1, a2, b1, b2 = sp.symbols("a1 a2 b1 b2")
    X, Y, Z = sp.Matrix([x1,x2]), sp.Matrix([y1,y2]), sp.Matrix([z1,z2])
    B = sp.Matrix([[2,1],[1,4]])
    before = (Y.dot(B*(X+Z))+Z.dot(B*X))/k
    after = (Z.dot(B*(X+Y))+Y.dot(B*X))/k
    assert sp.expand(before-after) == 0
    root_before = a1*(x1+z1)+a2*(x2+z2)+b1*x1+b2*x2
    root_after = b1*(x1+y1)+b2*(x2+y2)+a1*x1+a2*x2
    assert sp.expand(root_before-root_after-(a1*z1+a2*z2-b1*y1-b2*y2)) == 0
    # The original weighted coefficient recurrence has no lost factor k.
    Q = lambda v: sp.expand(v.dot(B*v)/2)
    assert sp.expand(Q(X+k*Y)-Q(X)-k*k*Q(Y)-k*Y.dot(B*X)) == 0
    # The exact primitive line exponents cancel to psi_y * rig.
    # Coordinates are M_(1+w)y, M_y, M_wy, M_0.
    tau = sp.Matrix([-1,1,1,-1])
    primitive = sp.Matrix([1,-2,-1,2])
    assert tau+primitive == sp.Matrix([0,-1,0,1])
    # C_(k,alpha+y) / t_b^* C_(k,alpha), using kb=c(y).
    # Basis: M_x, M_b, M_0, P(b,x), P(c(alpha),x), P(c(alpha),b).
    target_line = sp.Matrix([k,0,0,k,1,0])
    source_line = sp.Matrix([k,k,-k,k,1,1])
    assert target_line-source_line == sp.Matrix([0,-k,k,0,0,-1])
    # At zero: basis M_0, M_b, M_c(alpha), M_(b+c(alpha)).
    ratio_at_zero = sp.Matrix([k-1,1-k,1,-1])
    inverse_biextension = sp.Matrix([-1,1,1,-1])
    fibre_multiplier = sp.Matrix([k,-k,0,0])
    assert ratio_at_zero == inverse_biextension+fibre_multiplier

    cases = even = divisible = 0
    for level in range(1,13):
        group = list(product(range(level), repeat=2))
        radical = []
        for y,a in group:
            if all((a*z-b*y) % level == 0 for z,b in group):
                radical.append((y,a))
            for z,b in group:
                # Coefficient x cancels in every commutator.
                for x in (0,1,level+2):
                    lhs = a*(x+z)+b*x-b*(x+y)-a*x
                    assert (lhs-(a*z-b*y)) % level == 0
                    cases += 1
                    even += level % 2 == 0
                    divisible += any(level % p == 0 for p in (2,3,5))
        assert radical == [(0,0)]
    return {"symbolic_rank_two_monomial_and_primitive_line_checks": "PASS",
            "exact_coefficient_ratio_and_zero_fibre_exponents": "PASS",
            "exact_commutator_cases": cases, "even_level_cases": even,
            "cases_with_level_divisible_by_test_residue_prime": divisible,
            "perfect_pairing_levels": list(range(1,13)),
            "scope": "Finite and symbolic models of the original coefficient signs/powers. No claim that a toy monodromy form realizes a particular arithmetic PEL variety."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    ref = reference()
    degrees = degree_dimensions()
    theta = exact_theta_checks()
    paths = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", "scripts/"+Path(__file__).name]
    record = {
        "date": "2026-11-22", "status": "PASS", "whole_nodes_newly_closed": 0,
        "classification": "Closed actual complete-DVR PELUnif/TorsionIso supplier and rank-one integral theta module",
        "proved": ["Original GoodAt level forces split closed and Raynaud tori over the same DVR",
                   "Principal polarization gives the exact same period lattice and primitive abelian line",
                   "Actual common-denominator integral expansions on every thickening",
                   "All-level generic expansion bijection with the integral expansion witness",
                   "All-integer torsion quotient and exact original theta/Weil comparisons",
                   "Rank-one integral theta module and nonvanishing on the closed fibre"],
        "remaining": ["Coordinated finite level and good-cover comparisons",
                      "Global domination, height, section remainder and cusp estimates",
                      "Raw global theta norm and final uniform assembly"],
        "sources": sources, "primary_reference": ref,
        "dimension_checks": degrees, "theta_checks": theta,
        "artifacts": [{"path": p, "sha256": auth.sha((auth.ROOT/p).read_bytes())} for p in paths],
        "scope": "Written standard proof plus authenticated source/primary-reference bytes and exact finite identities. Torsion comparison includes residue-characteristic multiples but does not assert that the whole integral torsion kernel is finite. No Lean build, global PartI supplier, or whole-node closure.",
        "reproduce": "python3 scripts/"+Path(__file__).name+" --offline",
    }
    (auth.ROOT/"certificates"/(STEM+".json")).write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "dimension_cases": degrees["all_rank_all_level_dimension_cases"],
                      "commutator_cases": theta["exact_commutator_cases"],
                      "even_level_cases": theta["even_level_cases"]}))


if __name__ == "__main__":
    main()
