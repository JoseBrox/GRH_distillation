#!/usr/bin/env python3
"""Exact diagnostics and bounded source evidence for the rank-two curve.

The mathematical argument is in the accompanying note. This script
does not prove global propagation, arithmetic frame existence, or RH.
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
    "FrobeniusSmoothVectors.ContinuousCoboundaries2": [(16, 57), (109, 216)],
    "CurveDVRSpecialization.SecondThirdPrimeConditionTransferAlt": [(11, 85)],
    "CurveDVRSpecialization.PxIsCont": [(231, 289)],
    "CurveDVRSpecialization.FinLamOf": [(60, 146), (177, 258)],
    "FrobeniusSmoothVectors.LeAdicClosure": [(27, 32), (149, 249)],
    "FrobeniusSmoothVectors.MemPowSmulLe": [(14, 110)],
    "FrobeniusSmoothVectors.FrameFiberEq": [(6, 42)],
    "FrobeniusSmoothVectors.FrameExtensionOfLocallyConstant": [(11, 89)],
    "FrobeniusSmoothVectors.FinrankStructMapSRange": [(6, 53)],
    "FrobeniusSmoothVectors.AbEval": [(134, 181)],
    "FrobeniusSmoothVectors.CharpolyCoeffsInSubalgebra": [(15, 84)],
    "FrobeniusSmoothVectors.TameInertiaCondition": [(183, 280)],
    "CurveDVRSpecialization.NicePrimeEx": [(87, 125)],
    "CurveDVRSpecialization.ExistsNicePrimeAboveOfLargeDim": [(1, 69)],
    "FrobeniusSmoothVectors.HasObs": [(26, 120)],
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def exact_checks():
    a, b, c, d, x, y, alpha, beta = sp.symbols("a b c d x y alpha beta", nonzero=True)
    A = sp.Matrix([[a, b], [c, d]])
    J = sp.Matrix([[0, 1], [1, 0]])
    Ast = J*A.T*J
    D = A-Ast
    assert D == sp.diag(a-d, d-a)
    assert sp.simplify(sp.trace(A*A-A*Ast)-(a-d)**2) == 0
    e1 = sp.simplify((D+(a-d)*sp.eye(2))/(2*(a-d)))
    e2 = sp.simplify(((a-d)*sp.eye(2)-D)/(2*(a-d)))
    assert e1 == sp.diag(1, 0)
    assert e2 == sp.diag(0, 1)
    B = sp.Matrix([[x, y], [alpha, beta]])
    assert sp.trace(e1*A*e2*B) == b*alpha

    R1 = sp.Matrix([[x, 0], [a, 1/x]])
    R2 = sp.Matrix([[y, 0], [b, 1/y]])
    ordinary = sp.simplify((R1-x*sp.eye(2))*(R2-(1/y)*sp.eye(2)))
    assert sp.simplify(ordinary-sp.Matrix([[0, 0], [a*(y-1/y)-b*(x-1/x), 0]])) == sp.zeros(2)
    cocycle = sp.simplify((R1*R2)[1, 0]/(x*y))
    assert sp.simplify(cocycle-(a/x+(1/x**2)*(b/y))) == 0

    # The normalized infinitesimal gauge group is the split orthogonal Lie line.
    H = sp.diag(x, -x)
    assert H*J+J*H.T == sp.zeros(2)
    assert sp.trace(H) == 0
    gauge = A*J+J*A.T
    assert gauge == sp.Matrix([[2*b, a+d], [a+d, 2*c]])

    checked = 0
    for C0 in range(21):
        for degree in range(3*C0+8, 3*C0+28):
            assert degree+2*C0+2 < 2*degree
            for local_degree in range(6, 16):
                assert 2*degree-local_degree+3 < 2*degree
                checked += 1
    return {
        "ring_identities": [
            "J2-polarization makes the rank-two marking automatic.",
            "zeta^2=tr(A^2-A A*) and spectral projectors use only 2*zeta.",
            "The weight-zero pair is tr(e1 A e2 B).",
            "The ordinary product gives the exact strict local coboundary equation.",
            "Dividing the lower entry by Psi gives the Psi^-2 cocycle equation.",
            "The orthogonal infinitesimal gauge space is one-dimensional when 2 is invertible."
        ],
        "dimension_margin_cases": checked,
        "dimension_margin_scope": "Finite edge diagnostic only; the note proves both inequalities for every C0,d,d_v in the original ranges.",
        "excluded_claims": ["A Lean build", "A uniform bound on the original unramified exponent h", "Global component propagation", "An integral Selmer estimate"]
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert digest(packed) == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    modules = {row[0]: row for row in atlas["modules"]}
    records = []
    for name, ranges in RANGES.items():
        module = BASE+name
        item = {"repository": atlas["repository"], "commit": atlas["commit"],
                "path": "lean/src/"+module.replace(".", "/")+".lean",
                "git_blob_sha1": modules[module][1]}
        source = inspect_file(item, args.offline)
        cache = ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]
        lines = cache.read_text().splitlines()
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo+1 <= 120
        records.append({**item, "sha256": source["sha256"], "line_count": len(lines),
                        "ranges": [{"start": lo, "end": hi,
                                    "sha256": digest(("\n".join(lines[lo-1:hi])+"\n").encode())}
                                   for lo, hi in ranges]})
    note = ROOT/"notes/selmer-support-continuation-rank-two-curve.md"
    presentation = ROOT/"paper/shared/selmer-support-continuation-rank-two.tex"
    references = ROOT/"paper/shared/selmer-support-continuation-rank-two-references.tex"
    result = {
        "classification": "Closed rank-two starting-curve subobligation; independently reviewed.",
        "target": "An actual Nice type-I one-dimensional characteristic-ell prime above the original Hecke-support starting prime.",
        "proof_file": str(note.relative_to(ROOT)), "proof_sha256": digest(note.read_bytes()),
        "presentation_files": [
            {"path": str(path.relative_to(ROOT)), "sha256": digest(path.read_bytes())}
            for path in (presentation, references)
        ],
        "source_records": records,
        "exact_diagnostics": exact_checks(),
        "preserved_hypotheses": [
            "The original odd prime, rank-two Setup, universal normalized Space, TwLink and actual Hecke ideal J.",
            "The original ModIn.fin weight ring and finite Hecke quotient.",
            "Abstract curve lemma: FinLam, Ok and Big suffice without ModIn; actual ModIn.fin is used only to supply FinLam.",
            "The coefficient DVR may have equal characteristic ell; lambda_0 and the dimension cuts retain its uniformizer.",
            "The actual F.Ok strict H1_C bound, trivial H1 bound, local inertia generators and bounded unramified-character exponent.",
            "The original Big inequalities d>3*C0+7 and every d_v>5.",
            "The original finite unramified chart coefficient extension and residue embedding.",
            "The exact original N_v=I_v intersect ker(epsilon_v), and the ordered local characters."
        ],
        "decisive_dimensions": {
            "closed_coefficient_fibre": "at most C0",
            "triangular_locus": "at most d+2*C0+2 < 2*d",
            "off_triangular_character_coincidence": "at most 2*d-d_v+3 < 2*d",
            "actual_seed_chart_support": "2*d+2",
            "curve": "1"
        },
        "scope": {
            "whole_node_closed": False, "lean_build": False,
            "global_component_propagation": "Still separate; the next exact tangent/obstruction presentation is identified.",
            "rank_three": "No type-E or thick-link result is asserted.",
            "integral_selmer_budget": "No bound is asserted."
        }
    }
    out = ROOT/"certificates/selmer-support-continuation-rank-two-curve.json"
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"source_files": len(records), "exact_diagnostics": "passed",
                      "certificate": str(out.relative_to(ROOT)), "no_whole_node_completion": True}))


if __name__ == "__main__":
    main()
