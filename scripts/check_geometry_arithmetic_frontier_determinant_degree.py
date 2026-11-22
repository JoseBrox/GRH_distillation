#!/usr/bin/env python3
"""Check pinned sources and exact examples for the section determinant proof.

The general theorem is proved in the shared mathematical text, not by
these finite computations. No Lean build or geometric construction is run.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path

import sympy as sp

from check_sources import inspect_file


ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "geometry-arithmetic-frontier-determinant-degree"
DP = "Development.AbelianVarietyTheory.Proofs.DivisorProofs."
DD = "Development.AbelianVarietyTheory.Definitions.Divisors."
RANGES = {
    DD + "HermSysHypOneLeLambdaZero": [(15, 38), (73, 99), (114, 175), (188, 240), (253, 271)],
    DD + "IntegralBound": [(34, 70)],
    DP + "ArithmeticHilbertSamuelBound": [(19, 20)],
    DP + "ExplicitArithmeticHilbertSamuelBound": [(23, 47)],
    DP + "HilbertSamuelFiltrationAtGoodSections": [(27, 76)],
    DP + "LatticeDegreeGeHeightPolynomialVectorsDet": [(39, 87), (91, 121)],
    DP + "FiniteHeightSubMeanLeDegreeFullLatticeDetIdeal": [(73, 90), (107, 119), (121, 146)],
    DP + "MultiformHeightLowerBound": [(31, 49), (107, 156)],
    DP + "ExistsShortColumnsDetNeZeroHilbertSamuel": [(99, 132)],
    DP + "PowDvdOfSpecialisations": [(44, 50), (71, 101), (103, 129)],
    DP + "SlopeLowerBoundTopLatticeOffHypersurface": [(106, 158), (161, 175), (185, 237), (251, 256)],
    DP + "ClaimSOfNumbers": [(9, 16), (56, 88)],
    DP + "HermitianSystemSlopeBoundOfDeterminantSlopeInequ": [(14, 17), (38, 88)],
    "Formalism.LocalToGlobal.IndefiniteForms.IndefiniteTree.RealCubicMeans."
    "LogMeanShares.LogMeanStatements.HSClaim": [(7, 22)],
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


def arithmetic_checks():
    count = 0
    for D in range(1, 13):
        for T in range(D + 1, D + 25):
            R = comb(T - 1, D)
            ranks = [comb(a + D - 1, D - 1) for a in range(T - D)]
            exponent = sum(r * (T - a) for a, r in enumerate(ranks))
            assert sum(ranks) == R
            assert (D + 1) * exponent == R * (T + D * (D + 1))
            count += 1

    q, D, T, y, d, c, h, lb, l0, lD, lT = sp.symbols("q D T y d c h lb l0 lD lT")
    a = D * (D + 1)
    e = y * (T - D) - q * a
    exact = q * (T + a) * h - c * e - q * (T * lb / 2 + l0) - y * ((T - D) * lb / 2 + lD) - (d - q - y) * lT
    coarse = q * (T * h - a * c - l0 - T * lb / 2) - (d - q) * (T * c + T * lb / 2 + lD + lT)
    nonnegative = q * a * (h + c) + c * (T * (d - q) - e) + ((d - q) * T - y * (T - D)) * lb / 2 + (d - q - y) * lD + y * lT
    assert sp.expand(exact - coarse - nonnegative) == 0

    cases = 0
    for Dv in range(1, 6):
        for Tv in range(Dv + 1, Dv + 8):
            qv = comb(Tv - 1, Dv)
            y0 = (qv * Dv * (Dv + 1) + Tv - Dv - 1) // (Tv - Dv)
            for yv in [y0, y0 + 1, y0 + qv]:
                for extra in [0, 1, qv]:
                    dv = qv + yv + extra
                    for hv in [Fraction(-3, 2), Fraction(0), Fraction(7, 3)]:
                        values = {D: Dv, T: Tv, q: qv, y: yv, d: dv, c: Fraction(3, 2),
                                  h: hv, lb: Fraction(2, 3), l0: Fraction(1, 5),
                                  lD: Fraction(3, 7), lT: Fraction(2, 5)}
                        assert e.subs(values) >= 0
                        assert (exact - coarse).subs(values) >= 0
                        cases += 1
    return {"monomial_count_cases": count, "symbolic_nonnegative_error_identity": True,
            "exact_signed_slope_cases": cases,
            "negative_height_boundary_included": True}


def determinant_checks():
    x, y, s, t, u, v = sp.symbols("x y s t u v")
    cases = []
    # Actual P^1 section spaces V_j=H^0(O(j+kappa)), using original
    # monomial generators, rather than synthetic diagonal determinants.
    for T in [2, 3, 4]:
        for kappa in [0, 1]:
            degree = T + kappa
            columns = [sp.expand((s*x+t*y)**a * (u*x+v*y)**(T-a) * x**kappa)
                       for a in range(T-1)]
            columns += [sp.expand((s*x+t*y)**(T-1) * x**(kappa+1-j) * y**j)
                        for j in range(kappa+2)]
            matrix = sp.Matrix([[sp.Poly(col,x,y).coeff_monomial(x**(degree-j)*y**j)
                                 for col in columns] for j in range(degree+1)])
            determinant = sp.factor(matrix.det(method="domain-ge"))
            exponent = (T-1)*(T+2)//2
            quotient = sp.cancel(determinant/(s*v-t*u)**exponent)
            polynomial = sp.Poly(quotient, s,t,u,v)
            assert polynomial.total_degree() == kappa*(T-1)
            assert determinant != 0
            assert sp.expand(determinant-(s*v-t*u)**exponent*quotient) == 0
            cases.append({"D":1,"T":T,"kappa":kappa,"rank":degree+1,
                          "Chow_exponent":exponent,"cofactor":str(quotient)})

    ideals = 0
    for diagonal in [(2,3),(2,4,5),(3,5,7),(1,2,4)]:
        r = len(diagonal)
        base = sp.Matrix(r,r,lambda i,j:(1 if i==j else 0)+(i+1)*(j+1)*u+(i-j)*v)
        columns = sp.diag(*diagonal)*base
        determinant = sp.Poly(sp.expand(columns.det()),u,v)
        index = sp.prod(diagonal)
        assert all(coeff % index == 0 for coeff in determinant.coeffs())
        ideals += 1

    # Proportionality on a principal open set does not imply divisibility
    # when the supposed Chow polynomial is reducible.
    bad_f, bad_p = s*u, u**3
    assert sp.expand(bad_p*s**3-bad_f**3) == 0
    assert sp.rem(bad_p,bad_f**3,s,u) != 0
    return {"section_space_determinants":cases,"integral_coefficient_ideal_cases":ideals,
            "negative_controls":[
                {"name":"irreducibility","f":"s*u","P":"u^3","open":"s!=0",
                 "proportional_but_not_divisible":True},
                {"name":"actual_lattice_integrality","M":"2Z","P":"1","column_bound":1,
                 "degree":"-log(2)","invalid_claim_without_integrality":"0 <= -log(2)"}]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources = provenance(args.offline)
    arithmetic = arithmetic_checks()
    determinants = determinant_checks()
    files = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
             f"paper/shared/{STEM}-references.tex", "scripts/"+Path(__file__).name]
    record = {
        "date":"2026-11-22", "status":"PASS",
        "classification":"Reconstructed arithmetic degree supplier and shorter dependency route inside an open node",
        "claim":"The polynomial determinant argument estimates the full original section lattice under its retained geometric filtration, lattice, multiplication and short-family hypotheses.",
        "sources":sources,"exact_checks":{"arithmetic":arithmetic,"determinants":determinants},
        "newly_proved_suppliers":[
            "Polynomial-height lower bound and full-lattice determinant comparison with fractional determinant ideals.",
            "Construction of nonzero polynomial columns from the original short families.",
            "Chow-form power divisibility from the good-section filtration and maximal deepest rank.",
            "Original full section-degree lower bound and its geometric-height specialization."],
        "bypassed_inputs":["Controlled integral lifts of every jet.",
                           "Separate evaluation-lattice degree estimate.",
                           "Quantitative archimedean lifts of each jet and small choices of auxiliary cutting hyperplanes."],
        "retained_inputs":["Original arithmetic model, metric, full lattices and component identifications.",
                           "Multiplication stability and the original Hermitian operator bound.",
                           "Short spanning families at levels 0,D,T.",
                           "Good-section vector-space filtration, Chow form, Bertini and height identity.",
                           "Original nef-and-big and vanishing inputs used to construct that filtration."],
        "limitations":["The general mathematical proof is in the shared TeX; finite checks do not prove it.",
                       "The determinant branch exists in the pinned source; novelty is its completed readable reconstruction and dependency simplification.",
                       "No construction of the retained geometric data or new whole-node completion.",
                       "No Lean compilation or arithmetic jet-lifting assertion.",
                       "The existing smaller J=DP(kappa/T+1) is preserved, not counted as a new result."],
        "artifacts":[{"path":p,"sha256":sha((ROOT/p).read_bytes())} for p in files],
        "reproduce":"python3 scripts/"+Path(__file__).name+" --offline"}
    (ROOT/"certificates"/(STEM+".json")).write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":"PASS","source_modules":len(sources),
                      "monomial_count_cases":arithmetic["monomial_count_cases"],
                      "slope_cases":arithmetic["exact_signed_slope_cases"],
                      "section_determinants":len(determinants["section_space_determinants"]),
                      "negative_controls":len(determinants["negative_controls"])}))


if __name__ == "__main__":
    main()
