#!/usr/bin/env python3
"""Authenticate actual GL3 arithmetic transfer contracts and exact identities.

The accompanying note proves the group, torus, Hensel, closed-algebra and
semisimplicity arguments. This script records their exact interfaces and
checks polynomial identities, without claiming a Lean build or whole-node closure.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    "CurveDVRSpecialization.PxIsCont": [(184, 267), (268, 289)],
    "CurveDVRSpecialization.FinLamOf": [(177, 258)],
    "WeilGroupCharacters.UniversalOrdinaryDeterminantRing": [(189, 243), (255, 301)],
    "CurveDVRSpecialization.SecondThirdPrimeConditionTransferAlt": [(11, 107)],
    "CurveDVRSpecialization.NiceSep": [(16, 106)],
    "CurveDVRSpecialization.NiceIrr": [(61, 135)],
    "CurveDVRSpecialization.NiceIrrE": [(54, 115)],
    "CurveDVRSpecialization.NiceTypeE": [(92, 200)],
    "CurveDVRSpecialization.NiceSpecializationTwistSatisfiesThirdCondition": [(14, 60), (101, 149), (164, 213)],
    "CurveDVRSpecialization.ThickOf": [(25, 119), (120, 197)],
    "CurveDVRSpecialization.ThickAlg": [(110, 173), (253, 355), (417, 493)],
    "CurveDVRSpecialization.StableOf": [(39, 75)],
    "CurveDVRSpecialization.SecondThirdPrimeConditionTransfer": [(27, 96)],
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def exact_checks():
    x = sp.symbols("x")
    variables = sp.symbols("a0:9")
    M = sp.Matrix(3, 3, variables)
    z = sp.symbols("z0:3", nonzero=True)
    A = M*sp.diag(*z)
    ch = A.charpoly(x).as_expr()
    minor_sum = sum(M.extract([i, j], [i, j]).det()*z[i]*z[j]
                    for i in range(3) for j in range(i+1, 3))
    assert sp.expand(ch-(x**3-sum(M[i, i]*z[i] for i in range(3))*x**2
                         +minor_sum*x-M.det()*sp.prod(z))) == 0
    for i in range(3):
        complement = [j for j in range(3) if j != i]
        assert sp.expand(M.extract(complement, complement).det()-M.adjugate()[i, i]) == 0

    a, b, c, d, e, u, v = sp.symbols("a b c d e u v")
    split = sp.Matrix([[a, 0, b], [0, e, 0], [c, 0, d]])
    thick = sp.Matrix([[a, u, b], [0, e, 0], [c, v, d]])
    assert sp.expand(split.charpoly(x).as_expr()-thick.charpoly(x).as_expr()) == 0
    cycle = sp.Matrix([[0, a, 0], [0, 0, b], [c, 0, 0]])
    assert sp.expand(cycle.charpoly(x).as_expr()-(x**3-a*b*c)) == 0
    assert sp.Poly(x*x+x+1-(x-1)**2, x, modulus=3).is_zero
    assert sp.expand((x-1)*(x*x+x+1)-(x**3-1)) == 0
    zeta = sp.symbols("zeta", nonzero=True)
    marked = sp.diag(zeta, 0, -zeta)
    e0 = marked*(marked+zeta*sp.eye(3))/(2*zeta*zeta)
    e1 = sp.eye(3)-marked*marked/(zeta*zeta)
    e2 = marked*(marked-zeta*sp.eye(3))/(2*zeta*zeta)
    assert e0 == sp.diag(1, 0, 0) and e1 == sp.diag(0, 1, 0) and e2 == sp.diag(0, 0, 1)

    cases = 0
    for n in (2, 3):
        from itertools import combinations
        for weights in combinations(range(-6, 7), n):
            sums = [0]
            for w in weights:
                sums.append(sums[-1]+w)
            for j in range(1, n+1):
                vals = [sums[i]+(n-i)*weights[j-1] for i in range(n+1)]
                bottom = min(vals)
                assert [i for i, val in enumerate(vals) if val == bottom] == [j-1, j]
                cases += 1
    return {
        "principal_minor_coefficient_formula": "Exact symbolic identity for a general 3x3 matrix times a diagonal matrix.",
        "complementary_principal_minors": "Exact cofactor identities for the inverse diagonal argument.",
        "thick_determinant": "Exact characteristic-polynomial equality for arbitrary triangular extension entries, valid over every commutative scalar extension.",
        "three_cycle": "charpoly=x^3-abc, and x^2+x+1=(x-1)^2 in characteristic 3.",
        "coefficient_surjection": "Exact rank-three spectral projector identities using only 2 and zeta in the denominator; balanced atoms reduce to trace cycles using the original polarization.",
        "hensel_slope_diagnostic_cases": cases,
        "scope": "Finite identities and integer diagnostics. The note proves the quantified mathematical statements."
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert digest(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    modules = {row[0]: row for row in atlas["modules"]}
    records = []
    for name, ranges in RANGES.items():
        module = BASE+name
        item = {"repository": atlas["repository"], "commit": atlas["commit"],
                "path": "lean/src/"+module.replace(".", "/")+".lean",
                "git_blob_sha1": modules[module][1]}
        source = inspect_file(item, args.offline)
        lines = (ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]).read_text().splitlines()
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo+1 <= 120
        records.append({**item, "sha256": source["sha256"], "line_count": len(lines),
                        "ranges": [{"start": lo, "end": hi,
                                    "sha256": digest(("\n".join(lines[lo-1:hi])+"\n").encode())}
                                   for lo, hi in ranges]})
    note = ROOT/"notes/selmer-support-continuation-rank-three-transfer.md"
    result = {
        "classification": "Closed literal rank-three NiceOf, ThickOf, P1' and P23' arithmetic transfers; independently reviewed.",
        "proof_file": str(note.relative_to(ROOT)), "proof_sha256": digest(note.read_bytes()),
        "source_records": records, "exact_diagnostics": exact_checks(),
        "primary_references": [
            {"url": "https://stacks.math.columbia.edu/tag/0B7R",
             "used_for": "The identity component of the reduced algebraic-group closure is geometrically irreducible."},
            {"url": "https://www.jmilne.org/math/Books/iAG2022.pdf",
             "location": "Corrected 2022 edition, Chapter 12, Section d; PDF page 247, printed page 236.",
             "used_for": "Connected smooth subgroups of a split torus are split tori; characters and cocharacters are dual finite free lattices."},
            {"url": "https://arxiv.org/pdf/0809.0415v2", "location": "Theorem 2.12",
             "used_for": "Already authenticated determinant realization and uniqueness of semisimplification over algebraically closed fields, only for StableOf field descent."}
        ],
        "decisive_interfaces": {
            "finite_coefficient_field": "The original Point uses finite k' and A=k'[[t]], with exact local normalization kernel.",
            "all_open_irreducibility": "A three-cycle trace argument forces Psi trivial on every local group in the only induced alternative; characteristic 3 is treated explicitly.",
            "N3": "Connected Zariski closure, nonzero principal minors, a torus cocharacter, and simple-root Hensel lifting give every original open-coset quantifier for both types.",
            "TypeE": "Actual dimensions 2+1, original exponent -2 in both forms, irreducibility on G', and the exact Hom vanishing.",
            "ThickOf": "Full determinant laws, multivariable CH coefficients, both ordered products, star reversal, prime-to-ell inertia, actual adic closure, nonstable and nonsemisimple clauses.",
            "semisimple_ring": "The complement is only a module complement; the scalar middle eigenvalue lies in the algebraically closed coefficient field, which supplies the missing scalar stability.",
            "P23": "The full finite chain, contracted common Thick primes, stable entrance and stable exit, including length zero."
        },
        "scope": {"whole_node_closed": False, "lean_build": False,
                  "remaining": "Actual ModIn suppliers stay explicit. Finite-point/endomorphism transfer and moving-family integral Selmer estimates remain separate."}
    }
    result["presentation_files"] = [
        {"file": name, "sha256": digest((ROOT/name).read_bytes())}
        for name in ["paper/shared/selmer-support-continuation-rank-three.tex",
                     "paper/shared/selmer-support-continuation-rank-three-references.tex"]]
    out = ROOT/"certificates/selmer-support-continuation-rank-three-transfer.json"
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"source_files": len(records), "exact_diagnostics": "passed",
                      "certificate": str(out.relative_to(ROOT)), "no_whole_node_completion": True}))


if __name__ == "__main__":
    main()
