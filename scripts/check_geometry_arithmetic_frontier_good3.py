#!/usr/bin/env python3
"""Authenticate the exact Good3 supplier and check its gauge normalizations.

The geometric construction is the mathematical proof in the shared TeX.
Finite exact models check the homotopy sign, separability projection,
primitive half-factor and harmonic gauge cancellation; they do not prove
the general scheme-theoretic construction or compile Lean.
"""
from __future__ import annotations

import argparse
import json
from math import factorial
from pathlib import Path

import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth


STEM = "geometry-arithmetic-frontier-good3"
P = "Formalism.LocalToGlobal.ProjectiveLattices."
G = "Formalism.SharpRestriction.Divisibility.GeneratorPowers."
A = "Development.AbelianVarietyTheory."
F = A + "Proofs.FormalGroupCharts."
J = A + "Proofs.JetHarmonics."
RANGES = {
    P + "VAtVNeBot": [(46, 83)],
    P + "ChartDirectionsIntegral": [(61, 89), (116, 151), (155, 179)],
    P + "ThGerm": [(101, 144), (158, 180), (189, 217)],
    A + "Definitions.PlaceAdaptation.AdaptStd": [(129, 150)],
    G + "IntChartSt": [(13, 32)],
    G + "GermCut": [(23, 47)],
    F + "CanonGaugeOfLog": [(21, 29)],
    F + "CanonGaugeOfSteps": [(73, 99), (100, 136)],
    F + "ExistsActionGauge": [(299, 332)],
    F + "CanonGaugeIndependenceHarmonic": [(24, 71)],
    F + "CanonGaugeNabValBaseChange": [(113, 139)],
    J + "HarmonicConnectionValueBaseChangeField": [(79, 94)],
    J + "ExistsExtensionAllModelsUniformized": [(21, 58)],
    J + "ExistsUniformisedModelIntegralChartAtPoint": [(28, 60)],
}


def references():
    refs = [
        ("04GK", "c2901bf52ad4d257630ce5634998ca6a00835a10feb5e17de2db1654ec14ae97",
         "Finite etale algebras over a henselian local ring and its residue field"),
        ("05D5", "490b6b188c82eb37fee5f470d78e7bd3e2069c0c9db4d6fd78ca59021d1a85d6",
         "Formal coordinates along a smooth section with specified free conormal basis"),
        ("02KH", "9da5d88e9ba6915ffdea0b6191750eb65dcc108799c35dc54f4f9bad1fc29777",
         "Flat H0 base change on a quasi-compact quasi-separated scheme, without properness"),
    ]
    result = []
    for tag, expected, scope in refs:
        path = f"build/reference-cache/stacks-{tag}.html"
        assert auth.sha((auth.ROOT/path).read_bytes()) == expected
        result.append({"path": path, "sha256": expected,
                       "url": f"https://stacks.math.columbia.edu/tag/{tag}",
                       "scope": scope})
    path = "build/reference-cache/lan-pel-revision.pdf"
    pdf_sha = "a7a454f5d0735f4bf11f00a8afc14c361c5fc2cefd691d7466f7620ab4c3a079"
    assert auth.sha((auth.ROOT/path).read_bytes()) == pdf_sha
    text_path = "build/reference-cache/lan-pel-revision.txt"
    raw = (auth.ROOT/text_path).read_bytes()
    text_sha = "f0b305b0a54e5557c5b9420526ccf79b90c42cf236e91f78e2645868f649af58"
    assert auth.sha(raw) == text_sha
    lines = raw.splitlines(keepends=True)
    excerpts = []
    for lo, hi in [(9890, 9942), (9980, 10012)]:
        piece = b"".join(lines[lo-1:hi])
        assert len(piece) <= 12000
        excerpts.append({"lines": [lo, hi], "sha256": auth.sha(piece)})
    result.append({"path": path, "sha256": pdf_sha, "text_path": text_path,
                   "text_sha256": text_sha,
                   "url": "https://www.kwlan.org/articles/cpt-PEL-type-thesis-revision.pdf",
                   "authenticated_text_excerpts": excerpts,
                   "scope": "Normal-base full faithfulness for semiabelian morphisms and original cubical lines; the full DVR degeneration was independently verified in its existing package"})
    return result


def gauge_checks():
    x1, x2, xp1, xp2, z, t = sp.symbols("x1 x2 xp1 xp2 z t")
    x = (x1, x2)
    xp = (xp1, xp2)
    cases = 0
    for degree in range(2, 7):
        for a in range(degree+1):
            h = (1+z+2*z*z)*x1**a*x2**(degree-a)
            c = sp.expand(h+h.subs(dict(zip(x, xp)), simultaneous=True)
                          -h.subs({x1: x1+xp1, x2: x2+xp2}, simultaneous=True))
            one_form = [-sp.diff(c, v).subs({xp1: 0, xp2: 0}) for v in xp]
            homotopy = sp.integrate(sum(v*one_form[i].subs({x1:t*x1, x2:t*x2}, simultaneous=True)
                                       for i, v in enumerate(x)), (t, 0, 1))
            assert sp.expand(homotopy-h) == 0
            cases += 1

    # The actual quadratic order Z[w], w^2-w+2=0; denominators of
    # the separability idempotent are permitted only in the fraction field.
    w = sp.Matrix([[0, -2], [1, 1]])
    wb = sp.eye(2)-w
    b00, b01, b10, b11 = sp.symbols("b00 b01 b10 b11")
    b = sp.Matrix([[b00, b01], [b10, b11]])
    assert w*w-w+2*sp.eye(2) == sp.zeros(2)
    dual = [(3*sp.eye(2)+w)/7, (sp.eye(2)-2*w)/7]
    dual_bar = [(3*sp.eye(2)+wb)/7, (sp.eye(2)-2*wb)/7]
    basis = [sp.eye(2), w]
    h3 = sp.zeros(2)
    for u, v, vb in zip(basis, dual, dual_bar):
        h3 += u.T*(v.T*b-b*vb)
    assert (w.T*h3-h3*wb-(w.T*b-b*wb)).applyfunc(sp.expand) == sp.zeros(2)
    assert (sum((u*v for u, v in zip(basis, dual)), sp.zeros(2))-sp.eye(2)) == sp.zeros(2)
    s = sp.Matrix([[0, z], [-z, 0]])
    h4 = -s/2
    assert h4.T-h4 == s
    assert w.T*h4-h4*wb == sp.zeros(2)
    balanced = sp.Matrix([[2, 1], [1, 4]])
    xx = sp.Matrix(x)
    assert w.T*balanced == balanced*wb
    assert sp.expand((xx.T*balanced*w*xx)[0]-(xx.T*balanced*xx)[0]/2) == 0
    return {"exact_cocycle_homotopies": cases,
            "parameter_dependent_cocycles": True,
            "separability_derivation_identity": True,
            "symmetry_sign_and_half_factor": True,
            "original_primitive_graph_half_factor": True}


def harmonic_checks():
    x1, y1, x2, y2, q = sp.symbols("x1 y1 x2 y2 q")
    variables = (x1, y1, x2, y2)
    f = (1+x1+2*y1+x1*y1+x1*x1+y1*y1)*(1+2*x2+y2+3*x2*y2+x2*x2)
    quadratic = q*(x1*y1+x2*y2)
    expq = sum(quadratic**i/sp.factorial(i) for i in range(5))
    expanded = sp.Poly(sp.expand(expq*f), variables)
    original = sp.Poly(f, variables)

    def at_zero(poly, ff):
        return sp.expand(sum(coeff*ff.coeff_monomial(mo)
                             *sp.prod(factorial(a) for a in mo)
                             for mo, coeff in sp.Poly(poly, variables).terms()))

    count = 0
    for a in range(5):
        for b in range(5):
            harmonic = (x1+x2)**a*(y1-y2)**b
            lap = sp.diff(harmonic, x1, y1)+sp.diff(harmonic, x2, y2)
            assert sp.expand(lap) == 0
            assert at_zero(harmonic, expanded) == at_zero(harmonic, original)
            count += 1
    # A nonharmonic derivative changes. Its invariance is deliberately
    # not part of the theorem.
    assert sp.expand(at_zero(x1*y1, expanded)-at_zero(x1*y1, original)-q) == 0
    return {"exact_harmonic_gauge_cases": count, "maximum_degree": 8,
            "nonharmonic_negative_control": True,
            "ordinary_derivatives_not_divided_powers": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    refs = references()
    checks = {"gauge": gauge_checks(), "harmonic": harmonic_checks()}
    paths = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", str(Path(__file__).relative_to(auth.ROOT)),
             "paper/shared/geometry-arithmetic-frontier-dvr-uniformization.tex",
             "paper/shared/geometry-arithmetic-frontier-discriminant-clearing.tex"]
    cert = {
        "date": "2026-11-23", "status": "PASS",
        "classification": "closed exact local Good3 supplier; independent mathematical review accepted",
        "whole_nodes_newly_closed": 0,
        "actual_suppliers": ["IntegralChartA3", "FrTrunc", "Good3",
                             "PELUnif and all-integer TorsionIso for every original IntData model",
                             "Original harmonic theta-value base change over the finite unramified extension"],
        "ramification_index": 1,
        "sources": sources, "primary_references": refs,
        "exact_diagnostics": checks,
        "artifact_hashes": {p: auth.sha((auth.ROOT/p).read_bytes()) for p in paths},
        "scope": {
            "actual_integral_frames_and_original_primitive_line": True,
            "integral_eigenspace_defects_retained": True,
            "nonproper_H0_uses_flat_base_change": True,
            "canonical_gauge_constructed_over_fraction_field_only": True,
            "new_discriminant_or_valuation_loss": False,
            "not_claimed": ["Uniform degree bound for the local unramified extension",
                            "Global sized arithmetic-cover existence",
                            "Gauge independence of arbitrary nonharmonic derivatives",
                            "Global theta-series identification and determinant-ideal comparisons",
                            "Archimedean Gram/norm bound", "Lean compilation"]},
        "diagnostics_scope": "Finite exact models check normalization and one false strengthening. General geometric and all-degree claims rest on the written proof and cited theorems."}
    target = auth.ROOT/"certificates"/(STEM+".json")
    target.write_text(json.dumps(cert, indent=2)+"\n")
    print(json.dumps({"status": cert["status"], "sources": len(sources),
                      "primary_references": len(refs), "checks": checks}))


if __name__ == "__main__":
    main()
