#!/usr/bin/env python3
"""Authenticate the original component-field contract and exact local edges.

The component action and all-rank assertions are proved in the shared TeX.
Finite ring calculations below diagnose the dyadic and congruence edges;
they do not prove class field theory or an unbounded-rank assertion.
"""
from __future__ import annotations

import argparse
import json

import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth


STEM = "geometry-arithmetic-frontier-component-field"
A = "Development.AbelianVarietyTheory."
P = "Formalism.LocalToGlobal.ProjectiveLattices."
RANGES = {
    "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry.ToroidalCompactification.TwoWeightEqOneAddRoot": [(14, 68)],
    P + "CompHt": [(86, 101)],
    P + "IsGenFrGenFr": [(9, 35)],
    A + "Proofs.DivisorProofs.ExistsGoodCoverOverSizedField": [(111, 162)],
    A + "Proofs.UnitaryExistence.HermitianFormsSameSignatureSameSpace": [(34, 100), (145, 218)],
    A + "Proofs.UnitaryExistence.FnAlgClosedOfCurveOverLcm": [(9, 29)],
    A + "Proofs.UnitaryExistence.GeometricallyIrreducibleComponentsWeberValues": [(9, 29)],
    A + "Proofs.UnitaryExistence.CoeffFieldAlgClosedInFunctionFieldOfAutFixPeriodStatement": [(1, 10)],
    A + "Definitions.Divisors.NormNegCmConstantEqAtAllEmbeddings": [(132, 137), (187, 208), (484, 499)],
}


def references():
    rows = [
        ("milne-shimura-introduction", "https://www.jmilne.org/math/xnotes/svi.pdf",
         "f637e61735ff9cf9730c43d978d8f05185685a37d5e1920fc3347061c83d7c7e",
         "cc65db22c9cc7bda0268c062730a86ae5c197215ed1e3a963983a67a54ff384f",
         [(3100, 3175), (4690, 4795), (6390, 6465)],
         "Theorem 5.17, Theorem 8.17 and Lemma 8.20, formula (64): actual components, rational PEL class and canonical reciprocity"),
        ("milne-cft", "https://www.jmilne.org/math/CourseNotes/CFT.pdf",
         "50d79af78250a9f1117ad9d337e0b231704a533fc707966ed1bfa52e13d498f5",
         "5f9250521f173b47423192f8c1b2fe05b9b38329522454f0bf93ee96cfa6547a",
         [(5435, 5495), (8990, 9020), (12715, 12750)],
         "III.1.2 unit and principal-unit norms, V.3.27 conductor-discriminant formula, VIII.3.1 cyclic Hasse norm theorem"),
        ("milne-cm", "https://www.jmilne.org/math/CourseNotes/CM.pdf",
         "0ac337a885d72f6938f15724b897f568fe350d0d754d0b52370b8f3a01d2e2b5",
         "596dd17c0ad120838057eaf00bca943ddd13cd6ac4cb2cd9445826ad148a2420",
         [(4120, 4185)],
         "Theorem 9.10 and Remark 9.11: CM algebras, exact Tate-module quasi-isogeny and rational polarization multiplier"),
        ("lan-pel-revision", "https://www.kwlan.org/articles/cpt-PEL-type-thesis-revision.pdf",
         "a7a454f5d0735f4bf11f00a8afc14c361c5fc2cefd691d7466f7620ab4c3a079",
         "f0b305b0a54e5557c5b9420526ccf79b90c42cf236e91f78e2645868f649af58",
         [(5795, 5838)],
         "Remark 1.4.3.12: characteristic-zero PEL moduli and canonical Shimura models, including the rational-class caveat"),
    ]
    answer = []
    for name, url, pdf_hash, text_hash, ranges, claim in rows:
        pdf_path = f"build/reference-cache/{name}.pdf"
        text_path = f"build/reference-cache/{name}.txt"
        assert auth.sha((auth.ROOT/pdf_path).read_bytes()) == pdf_hash
        data = (auth.ROOT/text_path).read_bytes()
        assert auth.sha(data) == text_hash
        # split on literal newline to match the displayed sed line numbering.
        lines = data.split(b"\n")
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpt = b"\n".join(lines[lo-1:hi])
            assert len(excerpt) <= 12288
            excerpts.append({"text_lines": [lo, hi], "sha256": auth.sha(excerpt)})
        answer.append({"path": pdf_path, "url": url, "sha256": pdf_hash,
                       "text_path": text_path, "text_sha256": text_hash,
                       "verified_statement": claim, "excerpts": excerpts})
    return answer


def local_ring_checks():
    cases = []
    for prime, c, max_k in [(2, 1, 4), (3, 2, 3), (5, 1, 2)]:
        # t^2+t+c is irreducible over the residue field.
        assert all((t*t+t+c) % prime for t in range(prime))
        for k in range(1, max_k+1):
            modulus = prime**k
            norm = lambda a, b: (a*a-a*b+c*b*b) % modulus
            units = [(a, b) for a in range(modulus) for b in range(modulus)
                     if norm(a, b) % prime]
            assert {norm(a, b) for a, b in units} == {
                u for u in range(modulus) if u % prime}
            depths = []
            for e in range(1, k+1):
                pe = prime**e
                principal = [(a, b) for a, b in units
                             if (a-1) % pe == 0 and b % pe == 0]
                assert {norm(a, b) for a, b in principal} == {
                    u for u in range(modulus) if (u-1) % pe == 0}
                for a, b in principal:
                    # bar(u)=(a-b)-bt; v=bar(u)/u has exact norm one
                    # and remains 1 modulo the very same principal ideal.
                    invnorm = pow(norm(a, b), -1, modulus)
                    aa, bb = (a-b) % modulus, -b % modulus
                    v0 = (aa*aa-c*bb*bb)*invnorm % modulus
                    v1 = (2*aa*bb-bb*bb)*invnorm % modulus
                    assert norm(v0, v1) == 1
                    assert (v0-1) % pe == 0 and v1 % pe == 0
                depths.append(e)
            cases.append({"prime": prime, "precision": k,
                          "unit_count": len(units), "principal_depths": depths})
    ramified_odd_norms = {(a*a+b*b) % 4 for a in range(4) for b in range(4)
                          if (a*a+b*b) % 2}
    assert ramified_odd_norms == {1} and 3 not in ramified_odd_norms
    return {"unramified_quadratic_ring_cases": cases,
            "unit_norm_and_every_principal_depth": "exact PASS",
            "norm_one_quotient_preserves_same_depth": "exact PASS",
            "ramified_negative_control": "Z[i]/4: odd norms are only 1 mod 4; unramified hypothesis is essential"}


def reflex_checks():
    u, ub = sp.symbols("u ub", nonzero=True)
    cases = 0
    for n in range(1, 9):
        for q in range(n+1):
            p = n-q
            v = (ub/u)**q
            assert sp.simplify(v*(u/ub)**q) == 1
            assert sp.simplify(u**n*v-u**p*ub**q) == 0
            assert sp.simplify((u**p*ub**q)*(ub**p*u**q)-(u*ub)**n) == 0
            cases += 1
    a = sp.symbols("a", integer=True, positive=True)
    assert sp.expand(3*a*a-(a*a+2*a)-2*a*(a-1)) == 0
    return {"exact_reflex_determinant_cases": cases,
            "ranks": [1, 8], "all_signatures_including_endpoints": True,
            "class_number_count_difference": "3A^2-(A^2+2A)=2A(A-1)>=0 for A>=1",
            "scope": "Exact bounded diagnostics; shared TeX proves general rank and field-size inequalities"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    refs = references()
    checks = {"local_rings": local_ring_checks(), "reflex_map": reflex_checks()}
    paths = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", "scripts/check_geometry_arithmetic_frontier_component_field.py"]
    cert = {
        "status": "PASS", "date": "2026-11-23",
        "classification": "closed exact supplier, independently reviewed",
        "claim": "Original FnAlgClosed over C R_m, relative normality and original fieldSz bound in all ranks and signatures",
        "whole_nodes_newly_closed": 0, "source_commit": auth.REV,
        "sources": sources, "primary_references": refs, "checks": checks,
        "files": [{"path": p, "sha256": auth.sha((auth.ROOT/p).read_bytes())} for p in paths],
        "proof_scope": "Human proof verifies local integral determinant lifts, rational PEL class, canonical component reciprocity and definite CM endpoints. Exact finite checks are supplementary.",
        "not_claimed": ["Full Deep.Good or Member supplier", "Uniform section or height bound",
                        "Uniform global period norm", "W10 completion", "Lean build"],
    }
    (auth.ROOT/"certificates"/(STEM+".json")).write_text(
        json.dumps(cert, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "PASS", "sources": len(sources),
                      "primary_references": len(refs),
                      "local_ring_cases": len(checks["local_rings"]["unramified_quadratic_ring_cases"]),
                      "reflex_cases": checks["reflex_map"]["exact_reflex_determinant_cases"]}))


if __name__ == "__main__":
    main()
