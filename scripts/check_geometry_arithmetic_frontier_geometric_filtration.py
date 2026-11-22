#!/usr/bin/env python3
"""Authenticate the geometric-filtration proof and check exact section models.

The general result, including vanishing and the Koszul induction, is a
mathematical proof in the shared TeX. These finite models do not prove it.
No Lean compilation, arithmetic model construction or jet norm bound is run.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from functools import lru_cache
from math import comb, factorial
from pathlib import Path

import sympy as sp

from check_sources import inspect_file


ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "geometry-arithmetic-frontier-geometric-filtration"
AP = "Development.AbelianVarietyTheory."
DP = AP + "Proofs.DivisorProofs."
DD = AP + "Definitions.Divisors."
RANGES = {
    DD + "HasBoundedPolesGlobalData": [(109, 145), (179, 218), (238, 269), (336, 350)],
    DD + "WellChosen": [(22, 30), (96, 105)],
    AP + "BlockTheory.DivisorBase.TopRankPowers": [(62, 78)],
    DP + "VanishesToOneOfStalkMap": [(21, 41), (61, 66), (133, 177)],
    DP + "FilMonoOfKerRes": [(24, 58)],
    DP + "FilSpaceVEqSpaceP": [(23, 45)],
    DP + "HilbertSamuelDegreeZeroResiduesRangeEqTop": [(23, 30)],
    DP + "HilbertSamuelVanishingFiltrationDeepestStepSpan": [(20, 39)],
    DP + "HilbertSamuelFiltrationAtGoodSections": [(27, 76)],
    DD + "HermSysHypOneLeLambdaZero": [(79, 99), (196, 224)],
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def provenance(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert (atlas["repository"], atlas["commit"]) == (REPO, REV)
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    result = []
    for module, ranges in RANGES.items():
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        record = inspect_file({"repository": REPO, "commit": REV, "path": path,
                               "git_blob_sha1": blobs[module]}, offline)
        assert record["matches_pinned_blob"]
        lines = (ROOT / "build/source-cache" / REPO / REV / path).read_bytes().splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            data = b"".join(lines[lo - 1:hi])
            assert len(data) <= 12000
            excerpts.append({"lines": [lo, hi], "sha256": sha(data)})
        result.append({"module": module, **{k: record[k] for k in
                       ["repository", "commit", "path", "git_blob_sha1", "sha256", "matches_pinned_blob"]},
                       "excerpts": excerpts})
    return result


def references():
    data = [
        {"path": "build/reference-cache/viehweg-moduli-1995.pdf",
         "url": "https://page.mi.fu-berlin.de/esnault/books/vibuch.pdf",
         "sha256": "57c4c714b7d22c05bd103fb3173643601460894da7506db10daa791de81af297",
         "reference": "E. Viehweg, Quasi-Projective Moduli for Polarized Manifolds, Springer 1995, Theorem 2.28, printed page 67 / PDF page 73.",
         "verified_scope": "Author-hosted theorem page was read and visually inspected; use N=1 and divisor zero for nef-and-big line-bundle vanishing."},
        {"path": "build/reference-cache/stacks-067M.html",
         "url": "https://stacks.math.columbia.edu/tag/067M",
         "sha256": "da297a018c3dbdc96e14c56d42c43937436f0c1276e2b46b4b62c0ec7e2bac52",
         "reference": "Stacks Project, Regular ideal sheaves, Lemmas 31.21.1 and 31.21.4.",
         "verified_scope": "Regular sequences imply Koszul regularity and the symmetric description of the associated graded ideal."},
        {"path": "build/reference-cache/stacks-02KH.html",
         "url": "https://stacks.math.columbia.edu/tag/02KH",
         "sha256": "9da5d88e9ba6915ffdea0b6191750eb65dcc108799c35dc54f4f9bad1fc29777",
         "reference": "Stacks Project, Flat base change, Lemma 30.5.2.",
         "verified_scope": "Cohomology commutes with flat extension of the base field for the projective schemes in the proof."},
    ]
    for row in data:
        actual = sha((ROOT / row["path"]).read_bytes())
        if row["sha256"] is not None:
            assert actual == row["sha256"]
        row["sha256"] = actual
    return data


@lru_cache(None)
def monomials(degree, variables):
    if variables == 1:
        return ((degree,),)
    return tuple((i,) + tail for i in range(degree + 1)
                 for tail in monomials(degree - i, variables - 1))


def projective_space_checks():
    cases = graded = 0
    for D in range(1, 5):
        for T in range(D + 1, D + 6):
            for b in range(1, 4):
                for c in range(3):
                    # Y=P^D, L=O(1), B=O(b), A=O(b+D+c), e=x_0^c.
                    # Z=[1:0:...:0], s_i=x_i and V_j=G_j.
                    A = b + D + c
                    m0 = A - D - 1
                    mD = A - 1
                    mT = A + T - D - 1
                    a0 = T - D
                    assert m0 >= 0 and min(D - i for i in range(D + 1)) == 0
                    assert min((D + 1) - i for i in range(D + 1)) >= 0
                    ambient = set(monomials(mT, D + 1))
                    deepest = {m for m in ambient if sum(m[1:]) >= a0}
                    generated = set()
                    for alpha in monomials(a0, D):
                        for beta in monomials(mD, D + 1):
                            generated.add((beta[0],) + tuple(x + y for x, y in zip(alpha, beta[1:])))
                    assert generated == deepest
                    for a in range(a0):
                        symbols = {m for m in ambient if sum(m[1:]) == a}
                        products = {(m0 + T - a,) + alpha for alpha in monomials(a, D)}
                        assert symbols == products
                        assert len(symbols) == comb(a + D - 1, D - 1)
                        graded += 1
                    cases += 1
    return {"models": cases, "graded_symbol_comparisons": graded,
            "deepest_monomial_spans_equal": True, "includes_D1_and_T_equals_D_plus_1": True,
            "scope": "Exact monomial section spaces on P^D, D=1..4; these models have delta=1."}


def multipoint_line_checks():
    t = sp.symbols("t")
    cases = graded = 0
    for ell in (2, 3):
        roots = list(range(1, ell + 1))
        s = sp.prod(t - r for r in roots)
        for b in (1, 2):
            for c in (0, 1):
                for T in (2, 3, 4):
                    # L=O(ell), B=O(b), A=O(b+ell+c), e=y^c.
                    # The good divisor is a reduced set of ell rational points.
                    m0 = b + ell + c - 2
                    mT = m0 + ell * T
                    mD = m0 + ell
                    a0 = T - 1
                    residues = sp.Matrix([[r ** j for j in range(m0 + 1)] for r in roots])
                    assert residues.rank() == ell
                    for a in range(a0 + 1):
                        jets = sp.Matrix([[sp.diff(t ** j, t, k).subs(t, r) / factorial(k)
                                           for j in range(mT + 1)]
                                          for r in roots for k in range(a)])
                        nullity = mT + 1 if a == 0 else mT + 1 - jets.rank()
                        assert nullity == mT + 1 - ell * a
                        if a == a0:
                            products = [sp.Poly(sp.expand(s ** a * t ** j), t) for j in range(mD + 1)]
                            matrix = sp.Matrix([[poly.nth(i) for poly in products] for i in range(mT + 1)])
                            assert matrix.rank() == nullity == mD + 1
                            assert jets * matrix == sp.zeros(ell * a, mD + 1)
                        else:
                            # Normalize the usual derivative by s'(r)^a to obtain
                            # the symbol in the actual local parameter s.
                            symbol = sp.Matrix([[sp.diff(s ** a * t ** j, t, a).subs(t, r)
                                                 / (factorial(a) * sp.diff(s, t).subs(t, r) ** a)
                                                 for j in range(m0 + 1)] for r in roots])
                            assert symbol == residues and symbol.rank() == ell
                            graded += 1
                    cases += 1
    return {"models": cases, "graded_symbol_comparisons": graded,
            "scope": "Exact polynomial spaces on P^1 with L=O(2) or O(3), including all local derivative symbols and deepest kernels."}


def negative_controls():
    # On y^2=x^3-x, x=2 gives two distinct points with y=+/-sqrt(6).
    # For B=O (nef but not big), V0=H0(O(2 infinity)) has basis 1,x.
    y = sp.sqrt(6)
    assert y ** 2 == 2 ** 3 - 2 and y != -y
    bad_residues = sp.Matrix([[1, 2], [1, 2]])
    assert bad_residues.rank() == 1 < 2
    # For a double point K[t]/(t^2), geometric evaluation kills t.
    geometric_evaluation = sp.Matrix([[1, 0]])
    assert geometric_evaluation.rank() == 1 < 2
    return [{"hypothesis": "B big", "example": "Elliptic curve y^2=x^3-x; L=O(2 infinity), B=O, A=L, e=1, s=x-2.",
             "exact_matrix_rank": 1, "required_residue_dimension": 2,
             "scope": "The matrix and the two distinct curve points are checked exactly; standard section-basis facts are explained in the mathematical note."},
            {"hypothesis": "Z finite etale", "example": "K[t]/(t^2)",
             "coordinate_ring_dimension": 2, "geometric_evaluation_rank": 1}]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources = provenance(args.offline)
    primary = references()
    projective = projective_space_checks()
    multipoint = multipoint_line_checks()
    controls = negative_controls()
    files = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
             f"paper/shared/{STEM}-references.tex", "scripts/" + Path(__file__).name]
    dependencies = ["paper/shared/geometry-arithmetic-frontier-determinant-degree.tex",
                    "paper/shared/finite-section-jet-bound.tex"]
    record = {
        "date": "2026-11-22", "status": "PASS",
        "classification": "Actual generic-filtration supplier reconstructed inside the open arithmetic-geometry node",
        "claim": "Original nef-and-big bundle hypotheses, the effective section e, and good finite-etale sections supply onto residues, exact graded symbols and the deepest-space equality for the original W_s=G_T+P_s.",
        "sources": sources, "primary_references": primary,
        "exact_checks": {"projective_spaces": projective, "multipoint_projective_lines": multipoint,
                         "negative_controls": controls},
        "newly_proved_suppliers": ["Onto residues from B-twisted ordinary Koszul and vanishing, with multiplication by the original e into V0=G0.",
                                   "First-order division from nonnegative A-twists and higher division by regular-sequence symbols.",
                                   "The actual deepest equality for enlarged V_D and exact graded product identities.",
                                   "Good tuples on a principal open and the exact specialized Chow factorization, using the previously proved projection construction."],
        "not_counted_as_new": ["Projection construction already in finite-section-jet-bound.",
                               "Existing smaller component coefficient J=DP(kappa/T+1)."],
        "retained_inputs": ["Original smooth projective geometric model and its nef-and-big bundles, e and open U.",
                            "Original birational linear system and Chow form with arithmetic height identity.",
                            "Actual integral lattices, metrics, multiplication bounds and short integral families."],
        "limitations": ["General proof is the shared mathematical text; finite checks do not prove vanishing or regular-sequence theorems.",
                        "No controlled integral jet lifts or their norm bounds are claimed or required by the determinant branch.",
                        "No Lean compilation, new arithmetic model construction or whole-node completion."],
        "artifacts": [{"path": p, "sha256": sha((ROOT / p).read_bytes())} for p in files],
        "dependencies": [{"path": p, "sha256": sha((ROOT / p).read_bytes())} for p in dependencies],
        "reproduce": "python3 scripts/" + Path(__file__).name + " --offline"}
    (ROOT / "certificates" / (STEM + ".json")).write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "projective_space_models": projective["models"],
                      "multipoint_line_models": multipoint["models"],
                      "graded_symbol_comparisons": projective["graded_symbol_comparisons"] + multipoint["graded_symbol_comparisons"],
                      "negative_controls": len(controls)}))


if __name__ == "__main__":
    main()
