#!/usr/bin/env python3
"""Bind the normalized-seed transfer proof to its exact source interfaces.

The finite diagnostics are exact algebra. They do not prove arithmetic
component reachability, a uniform Selmer estimate, or a Lean kernel build.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import subprocess
import urllib.request

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    "CurveDVRSpecialization.SecondThirdPrimeConditionTransferAlt": [(11, 85)],
    "CurveDVRSpecialization.PropagationTheoremGL2": [(16, 60)],
    "CurveDVRSpecialization.SeedOf": [(215, 334), (384, 455), (500, 546)],
    "FrobeniusSmoothVectors.OfTrace": [(25, 39), (108, 172)],
    "FrobeniusSmoothVectors.OfForm": [(41, 115), (249, 359)],
    "FrobeniusSmoothVectors.Integral": [(15, 44)],
    "FrobeniusSmoothVectors.PointField": [(53, 113), (115, 180), (181, 249), (254, 257)],
    "FrobeniusSmoothVectors.AlgVring": [(11, 74)],
    "FrobeniusSmoothVectors.LeAdicClosure": [(27, 32), (149, 213), (217, 249)],
    "FrobeniusSmoothVectors.SpaceEx": [(131, 244)],
    "CurveDVRSpecialization.SeedPtOf": [(174, 282)],
    "FrobeniusSmoothVectors.Seedpt": [(9, 30)],
    "FrobeniusSmoothVectors.MonMemPow": [(81, 112)],
    "FrobeniusSmoothVectors.LocDim": [(110, 178)],
    "CurveDVRSpecialization.ComponentsGoodRankTwo": [(107, 163)],
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def exact_checks():
    a, b, c, d, x = sp.symbols("a b c d x")
    A = sp.Matrix([[a, b], [c, d]])
    J2 = sp.Matrix([[0, 1], [1, 0]])
    Alt = sp.Matrix([[0, 1], [-1, 0]])
    alternating = sp.simplify(A + Alt.inv() * A.T * Alt - sp.trace(A) * sp.eye(2))
    assert alternating == sp.zeros(2)
    symmetric = A + J2 * A.T * J2 - sp.trace(A) * sp.eye(2)
    assert symmetric == sp.Matrix([[0, 2*b], [2*c, 0]])
    J3 = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    D3 = sp.Matrix([[a, b, 0], [c, 0, -b], [0, -c, -a]])
    assert D3.T * J3 + J3 * D3 == sp.zeros(3)
    assert sp.factor(D3.charpoly(x).as_expr()) == x * (x**2-a**2-2*b*c)
    assert sp.expand(sp.trace(D3*D3)) == 2*(a*a+2*b*c)
    D2 = sp.diag(a, -a)
    assert D2.T * J2 + J2 * D2 == sp.zeros(2)
    assert sp.expand(D2.charpoly(x).as_expr()) == x*x-a*a

    # All minimal balanced multisets of the actual nonzero weights.
    degrees = (-2, -1, 1, 2)
    expected = {(1, 0, 0, 1), (0, 1, 1, 0), (1, 0, 2, 0), (0, 2, 0, 1)}
    balanced = []
    atoms = set()
    for v in itertools.product(range(11), repeat=4):
        if not 0 < sum(v) <= 10 or sum(a*b for a, b in zip(v, degrees)):
            continue
        balanced.append(v)
        proper = any(all(a<=b for a,b in zip(u,v)) and u != v for u in expected)
        if not proper:
            atoms.add(v)
    assert atoms == expected
    for v in balanced:
        remain = list(v)
        blocks = 0
        while any(remain):
            u = next(u for u in expected if all(a<=b for a,b in zip(u,remain)))
            remain = [a-b for a,b in zip(remain,u)]
            blocks += 1
        assert 3*blocks >= sum(v)

    # Characteristic-zero irreducibility does not imply a stable special fibre.
    ell = sp.Integer(5)
    G0 = sp.diag(2, sp.Rational(1,2))
    G1 = sp.eye(2)+ell*sp.Matrix([[0,1],[0,0]])
    G2 = sp.eye(2)+ell*sp.Matrix([[0,0],[1,0]])
    basis = [sp.eye(2), G0, G1, G2]
    gram = sp.Matrix([[sp.trace(u*v) for v in basis] for u in basis])
    determinant = sp.factor(gram.det())
    assert determinant != 0
    assert sp.numer(determinant) % 5 == 0
    def reduce5(M):
        return [[(int(sp.numer(z))*pow(int(sp.denom(z)), -1, 5)) % 5 for z in M.row(i)]
                for i in range(M.rows)]
    reductions = [reduce5(M) for M in (G0,G1,G2)]
    assert reductions[1] == [[1,0],[0,1]] == reductions[2]
    assert reductions[0] == [[2,0],[0,3]]
    return {
        "polarization_sign": "Exact symbolic rank-two alternating and symmetric identities verified.",
        "normalized_mark": "Exact characteristic-polynomial identities in ranks two and three verified; no division by 3.",
        "balanced_monomials": {
            "degrees": degrees, "atoms": sorted(expected),
            "all_multisets_through_length": 10, "balanced_cases": len(balanced),
            "scope": "Finite diagnostic; the proof's opposite-pair/triple decomposition covers every length."
        },
        "special_fibre_obstruction": {
            "prime": 5, "trace_gram_determinant": str(determinant),
            "reduced_generators": reductions,
            "scope": "Exact constant-family example; not a counterexample to the arithmetic frame hypotheses."
        }
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert digest(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    modules = {row[0]:row for row in atlas["modules"]}
    records = []
    for name,ranges in RANGES.items():
        module = BASE+name
        item = {"repository":atlas["repository"],"commit":atlas["commit"],
                "path":"lean/src/"+module.replace(".","/")+".lean",
                "git_blob_sha1":modules[module][1]}
        record = inspect_file(item, args.offline)
        cache = ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]
        lines = cache.read_text().splitlines()
        records.append({**item,"sha256":record["sha256"],"line_count":len(lines),
            "ranges":[{"start":a,"end":b,"sha256":digest(("\n".join(lines[a-1:b])+"\n").encode())}
                      for a,b in ranges]})
    note = ROOT/"notes/selmer-support-continuation-seed-transfer.md"
    primary_pdf = ROOT/"build/selmer-support-continuation-sources/chenevier-determinants-v2.pdf"
    primary_text = primary_pdf.with_suffix(".txt")
    if not primary_pdf.exists():
        if args.offline:
            raise FileNotFoundError(primary_pdf)
        primary_pdf.parent.mkdir(parents=True, exist_ok=True)
        primary_pdf.write_bytes(urllib.request.urlopen("https://arxiv.org/pdf/0809.0415v2", timeout=60).read())
    assert digest(primary_pdf.read_bytes()) == "f3c0e0d86e803301c617d3023d425752e30da46673ed5af932647eb284286953"
    if not primary_text.exists():
        subprocess.run(["pdftotext", "-layout", str(primary_pdf), str(primary_text)], check=True)
    result = {
        "classification":"Closed normalized-seed transfer and original local-chart starting-support subobligations; standard-mathematics proof reviewed independently by the root agent.",
        "target":"Literal Setup.CurveSpecializationHypothesis and SeedIn, plus the actual Seedpt starting prime, ranks two and three, original setup.",
        "proof_file":str(note.relative_to(ROOT)), "proof_sha256":digest(note.read_bytes()),
        "manuscript_file":"paper/shared/selmer-support-continuation-seed-transfer.tex",
        "manuscript_sha256":digest((ROOT/"paper/shared/selmer-support-continuation-seed-transfer.tex").read_bytes()),
        "source_records":records,
        "primary_reference": {
            "author":"Gaetan Chenevier", "url":"https://arxiv.org/pdf/0809.0415v2",
            "pdf_sha256":digest(primary_pdf.read_bytes()),
            "text_sha256":digest(primary_text.read_bytes()),
            "theorem":"2.12; Definition-Proposition 2.18",
            "printed_pages":[28,32,33],
            "text_ranges":[[1320,1348],[1520,1552]],
            "checked_hypotheses":"An n-dimensional determinant over an algebraically closed field K; no matrix realization over the whole coefficient ring C is inferred."
        },
        "commutative_algebra_references":[
            {"url":"https://stacks.math.columbia.edu/tag/02JU", "result":"Dimension formula, equality for a universally catenary base", "checked_application":"C is a complete Noetherian local domain; D_C is a finite-type domain containing C; q is closed over m_C with finite residue extension; generic relative transcendence degree is one."},
            {"url":"https://stacks.math.columbia.edu/tag/07QS", "result":"Complete Noetherian local rings are excellent; finite type and localization preserve excellence"},
            {"url":"https://stacks.math.columbia.edu/tag/0AW1", "result":"Ratliff's equivalence of universal and formal catenarity", "checked_application":"The local domain (D_C)_q and its finite etale local extension have equidimensional completions; dimensions and contractions are preserved as stated."}
        ],
        "exact_diagnostics":exact_checks(),
        "decisive_scope":{
            "residual_irreducibility":"Not assumed; the original residual characters remain reducible.",
            "matrix_integrality":"Not asserted over C. Fractional entry modules are retained in a graded Laurent vertex construction.",
            "dimension":"The exact surjection beta:S.B->C has C=B_det/Z and beta Phi=q, so its kernel quotient has dimension 1+n[F:Q].",
            "starting_chart":"A closed point x over m_(S.B) has a nonzero original lower entry. Every original chart, with its prescribed finite unramified coefficient extension and residue map, contains an actual Hecke-support absolutely irreducible prime P with contraction Z_S and quotient dimension n[F:Q]+2.",
            "chart_characteristic":"The constructed prime P is characteristic zero; no characteristic-ell stable curve follows without the separate bad-locus and propagation arguments.",
            "uniformity":"No uniform bound on the trace discriminant, normalization basis, fractional module denominators or rank is asserted.",
            "still_open":["Original characteristic-prime component/curve reachability", "Global two-sided rigidity", "Moving-family weighted integral Selmer product bound"],
            "lean_build":False,"proof_map_node_closed":False
        }
    }
    out = ROOT/"certificates/selmer-support-continuation-seed-transfer.json"
    out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"source_files":len(records),"exact_diagnostics":"passed", "certificate":str(out.relative_to(ROOT)),
                      "no_lean_build":True,"no_whole_node_completion":True}))


if __name__ == "__main__":
    main()
