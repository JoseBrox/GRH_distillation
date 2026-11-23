#!/usr/bin/env python3
"""Exact algebra diagnostics and source contracts for the type-E supplier.

The accompanying standard-mathematics proof is the argument. These
diagnostics do not prove the remaining rank-three thick-link theorem.
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
    "FrobeniusSmoothVectors.QuotientHomNonvanishingBound": [(1, 120), (140, 236)],
    "FrobeniusSmoothVectors.ExistsFrobeniusCorner": [(1, 88)],
    "FrobeniusSmoothVectors.FrobeniusCornerOrderSkips": [(1, 30)],
    "FrobeniusSmoothVectors.FrobeniusCornerMiddleMem": [(1, 94)],
    "FrobeniusSmoothVectors.ContinuousCoboundaries2": [(167, 212)],
    "FrobeniusSmoothVectors.Integral": [(1, 103)],
    "CurveDVRSpecialization.PropagationTheoremGL3": [(80, 120), (213, 229)],
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def exact_checks():
    a, b, c, d, x, y, z, w, s, t = sp.symbols("a b c d x y z w s t")
    A = sp.Matrix([[a, b], [c, d]])
    B = sp.Matrix([[x, y], [z, w]])
    A3 = sp.Matrix([[a, 0, b], [0, s, 0], [c, 0, d]])
    B3 = sp.Matrix([[x, 0, y], [0, t, 0], [z, 0, w]])
    J2 = sp.Matrix([[0, 1], [1, 0]])
    J3 = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    corner = lambda M: M.extract([0, 2], [0, 2])
    assert corner(A3*B3) == A*B
    assert (A3*B3)[1, 1] == s*t
    assert corner(J3*A3.T*J3) == J2*A.T*J2
    assert sp.simplify(A*(sp.trace(A)*sp.eye(2)-A)-A.det()*sp.eye(2)) == sp.zeros(2)
    # Formal identity used to delete the middle factor after P M^2=gamma P M.
    gamma = sp.symbols("gamma")
    P = B
    lhs = A.det()*P-(sp.trace(A)-gamma)*P*A
    rhs = -P*A*A+gamma*P*A
    assert sp.simplify(lhs-rhs) == sp.zeros(2)
    psi = sp.symbols("psi", nonzero=True)
    assert sp.expand((psi-1)*(1/psi-1)) == 2-psi-1/psi
    return {
        "corner_multiplication_and_polarization": "Exact polynomial identities passed.",
        "middle_character_multiplication": "Exact block-matrix identity passed.",
        "middle_factor_deletion": "Exact Cayley-Hamilton identity checked; the proof separately uses all ordered-product equations and a unit determinant, not noncentral cancellation.",
        "excluded_claims": ["A Lean build", "Parity-split rank-three presentation", "Determinant-section connectedness", "Thick links", "Uniform integral Selmer estimate"]
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
    note = ROOT/"notes/selmer-support-continuation-type-e.md"
    result = {
        "classification": "Closed original type-E finite-weight support supplier l53; independently reviewed.",
        "proof_file": str(note.relative_to(ROOT)), "proof_sha256": digest(note.read_bytes()),
        "target": "Rank-two FinLam plus AllGood supplies an original rank-three FinLam ideal contained in every type-E coefficient contraction.",
        "source_records": records, "exact_diagnostics": exact_checks(),
        "decisive_interfaces": {
            "same_frame": "The original S2 and S3 share O and F; no conductor-one or fixed-field substitution.",
            "ideal": "I3=p^-1(C beta(I2)), with C=B3/(E intersect B3) and the original odd-entry ideal E.",
            "ordered_corner": "The corner indices are 0,2 and the characters psi_0,psi_2; deleting the middle factor uses Cayley-Hamilton.",
            "integral_map": "Degree-zero C and fixed graded pieces are closed in the vertex completion; A2 maps into K=A3/E itself.",
            "middle_character": "Triviality is proved only after the original fixed-weight uniformizer cut, using the exact cl exponent on each finite ell-group quotient.",
            "FinLam": "The original radical inclusion is retained, so the unit ideal is allowed when the type-E locus is empty."
        },
        "scope": {"whole_node_closed": False, "lean_build": False,
                  "rank_three_propagation": "The parity presentation, determinant section and thick links remain a separate frontier.",
                  "integral_selmer": "No weighted length or nilpotence estimate is asserted."}
    }
    result["presentation_files"] = [
        {"file": name, "sha256": digest((ROOT/name).read_bytes())}
        for name in ["paper/shared/selmer-support-continuation-rank-three.tex",
                     "paper/shared/selmer-support-continuation-rank-three-references.tex"]]
    out = ROOT/"certificates/selmer-support-continuation-type-e.json"
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"source_files": len(records), "exact_diagnostics": "passed",
                      "certificate": str(out.relative_to(ROOT)), "no_whole_node_completion": True}))


if __name__ == "__main__":
    main()
