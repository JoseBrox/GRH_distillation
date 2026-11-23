#!/usr/bin/env python3
"""Authenticate the actual Hermitian class-mass Siegel--Weil bridge.

Finite diagnostics detect normalization and CRT traps. The all-place
construction and cited convergent formula are proved/audited in the TeX;
no Lean build or uniform period-Gram estimate is claimed.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import gcd

import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth

STEM = "geometry-arithmetic-frontier-siegel-weil"
D = "Development.AbelianVarietyTheory.Definitions.SpanningFamilies."
S = "Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation."
RANGES = {
    "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry.ToroidalCompactification.TwoWeightEqOneAddRoot": [(14, 24)],
    D + "FirstCoordinateAdmissible": [(24, 84), (103, 150)],
    D + "IMemSiegel": [(14, 32)],
    D + "IsHeatZero": [(13, 19)],
    S + "SiegelWeilDefiniteHermitianOfFourMulLt": [(1, 21)],
    S + "KernelIdentity": [(181, 224)],
}


def references():
    rows = [
        ("gan-qiu-takeda-2014", "https://arxiv.org/pdf/1207.4709v3",
         "cde6b7ad22b974d4159f8cedd1e14a00bf4b05ec977ab750b54fdceb067adac5",
         "e01ee524edec3299a30b356a42b774bb792060a88faa14def27ea8282e8ba921",
         [(553, 586), (658, 691), (733, 754), (1831, 1854)],
         "Sections 2.5, 2.8, 3.1 and Theorem 7.1: measures, exact Weil action, probability integral and exact unitary factor"),
        ("milne-cft", "https://www.jmilne.org/math/CourseNotes/CFT.pdf",
         "50d79af78250a9f1117ad9d337e0b231704a533fc707966ed1bfa52e13d498f5",
         "5f9250521f173b47423192f8c1b2fe05b9b38329522454f0bf93ee96cfa6547a",
         [(5435, 5495)],
         "III.1.2: unramified unit norms, including the dyadic case"),
        ("hofmann-morris-compact-groups-preview",
         "https://api.pageplace.de/preview/DT0400.9783110695991_A40357843/preview-9783110695991_A40357843.pdf",
         "536d39efa97835b3ba33d8dbb7a1184d7e40f75d85e069d76a483e43213b8064",
         "9e51fd92e336536ee42ed4643bf6046392f75d96da44275aaff8361b03095456",
         [(3351, 3383)],
         "Corollary 2.33(ii): extension of a character from a closed subgroup of a compact abelian group"),
    ]
    out = []
    for name, url, ph, th, ranges, claim in rows:
        pdf = auth.ROOT / "build/reference-cache" / f"{name}.pdf"
        txt = pdf.with_suffix(".txt")
        assert auth.sha(pdf.read_bytes()) == ph
        data = txt.read_bytes()
        assert auth.sha(data) == th
        lines = data.split(b"\n")
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpt = b"\n".join(lines[lo-1:hi])
            assert len(excerpt) < 12288
            excerpts.append({"text_lines": [lo, hi], "sha256": auth.sha(excerpt)})
        out.append({"url": url, "pdf_path": str(pdf.relative_to(auth.ROOT)),
                    "pdf_sha256": ph, "text_path": str(txt.relative_to(auth.ROOT)),
                    "text_sha256": th, "excerpts": excerpts,
                    "verified_statement": claim})
    return out


def diagnostics():
    unit_norms = []
    for p, c, max_k in [(2, 1, 4), (3, 2, 3), (5, 1, 2), (7, 3, 2)]:
        assert all((a*a+a+c) % p for a in range(p))
        for k in range(1, max_k+1):
            m = p**k
            norms = {(a*a-a*b+c*b*b) % m
                     for a in range(m) for b in range(m)
                     if gcd(a*a-a*b+c*b*b, p) == 1}
            units = {a for a in range(m) if gcd(a, p) == 1}
            assert norms == units
            unit_norms.append({"p": p, "power": k, "units": len(units)})

    phases = 0
    z = sp.Rational(3, 5)+sp.I*sp.Rational(4, 5)
    assert sp.simplify(z*sp.conjugate(z)) == 1
    for n in [2, 4, 6, 10]:
        for N in [1, 2, 3, 5]:
            a = (2*z)**N
            chi = sp.conjugate(z)**(n*N)
            scalar = sp.expand(chi * sp.Integer(2)**(n*N))
            assert sp.simplify(scalar-sp.conjugate(a)**n) == 0
            rational_finite_phase = sp.expand(1/(sp.conjugate(z)**(n*N)))
            assert sp.simplify(rational_finite_phase-z**(n*N)) == 0
            phases += 1
    assert sp.simplify(z**2-1) != 0  # trivial splitting would miss this phase

    masses = []
    for orders, values in [([1, 2], [3, 7]), ([2, 3, 5], [2, -1, 6]),
                           ([4, 8, 12, 24], [0, 3, 5, -2])]:
        weights = [Fraction(1, a) for a in orders]
        mass = sum(weights)
        mean = sum(w*v for w, v in zip(weights, values))/mass
        assert sum(w*(v-mean) for w, v in zip(weights, values)) == 0
        assert sum(v-mean for v in values) != 0
        masses.append({"automorphism_orders": orders, "mass": str(mass),
                       "probability_mean": str(mean)})

    replacements = 0
    for R in [2, 3, 5, 7]:
        for M in [1, 3, 11]:
            q = 1+R*R*M
            x, y = Fraction(1, R), Fraction(q, R)
            assert (y-x)/R == M
            assert (R*y)/q == 1
            assert Fraction(R*x, q).denominator != 1
            assert (y/q-x) == 0
            replacements += 1
    return {"unramified_unit_norm_models": unit_norms,
            "exact_levi_and_central_phase_cases": phases,
            "class_mass_models": masses, "crt_replacements": replacements,
            "negative_controls": ["trivial splitting character loses the central determinant phase",
                                  "unweighted class average differs from the prescribed mass average",
                                  "weak approximation need not put the original point in both global lattices"],
            "scope": "Finite diagnostics only; the general theorem is proved in the shared TeX and uses the authenticated primary Siegel--Weil theorem."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--output", default=f"certificates/{STEM}.json")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    proof = f"paper/shared/{STEM}.tex"
    refs = f"paper/shared/{STEM}-references.tex"
    note = f"notes/{STEM}.md"
    script = f"scripts/check_geometry_arithmetic_frontier_siegel_weil.py"
    record = {
        "status": "PASS", "classification": "closed exact supplier, independent review recorded separately",
        "frontier": "Original SWAt for every actual everywhere-finite-unramified Host, every even n with 4N<n, and every original M,R,admitted family,Z",
        "artifacts": {p: auth.sha((auth.ROOT/p).read_bytes()) for p in [proof, refs, note, script]},
        "sources": sources, "primary_references": references(), "diagnostics": diagnostics(),
        "scope": {"ordinary_rh_and_dirichlet_grh": True, "same_field_and_levels": True,
                  "original_class_mass_retained": True, "original_TransH_operator": True,
                  "no_lean_build": True, "no_full_jacobi_SW_claim": True,
                  "no_uniform_period_gram_bound": True, "whole_node_closed": False},
    }
    out = auth.ROOT / args.output
    out.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "sources": len(sources),
                      "primary_references": len(record["primary_references"]),
                      "phase_cases": record["diagnostics"]["exact_levi_and_central_phase_cases"],
                      "output": args.output}))


if __name__ == "__main__":
    main()
