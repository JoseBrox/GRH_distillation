#!/usr/bin/env python3
"""Check the exact Low identities and pinned GL3 propagation interfaces.

This is an identity/source certificate, not a numerical proof of the
dimension, connectedness, cohomology, or arithmetic transfer arguments.
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
    "CurveDVRSpecialization.PropagationTheoremGL2": [(16, 60)],
    "CurveDVRSpecialization.PropagationTheoremGL3": [(80, 120), (150, 229)],
    "CurveDVRSpecialization.LocProp": [(1, 75)],
    "FrobeniusSmoothVectors.StrSMul": [(13, 71)],
    "FrobeniusSmoothVectors.ExistsNonzeroLowCocycle": [(14, 78), (121, 194)],
    "FrobeniusSmoothVectors.KrullDimLtOfNotLeTriangular": [(36, 58)],
    "FrobeniusSmoothVectors.Integral": [(71, 103)],
    "CurveDVRSpecialization.SecondThirdPrimeConditionTransferAlt": [(38, 57), (78, 107)],
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def exact_checks():
    p, q, u, v, d, alpha = sp.symbols("p q u v d alpha", nonzero=True)
    Y = lambda p, u: u+d*(p-1)
    A = lambda p, u: d*d-d*d*(p+1/p)/2-d*(1+1/p)*u+u*u/(2*p)
    gamma = alpha*alpha/2-d*alpha-d*d/2
    identities = {
        "first_lower_product": Y(p*q, q*u+v)-q*Y(p, u)-Y(q, v),
        "corner_product": A(p*q, q*u+v)-q*A(p, u)-Y(1/p, u/p)*Y(q, v)-A(q, v)/p,
        "corner_star": A(1/p, u/p)-A(p, u),
        "first_local": Y(p, (p-1)*alpha)-(p-1)*(alpha+d),
        "second_local": Y(1/p, (p-1)*alpha/p)-(1-1/p)*(alpha-d),
        "corner_local": A(p, (p-1)*alpha)-(p-1/p)*gamma+(1-1/p)*(alpha+d)*(alpha-d),
        "marking": Y(p, u)-Y(1/p, u/p)-(p-1)*(d*(p+1)+u)/p,
    }
    for name, expression in identities.items():
        assert sp.factor(expression) == 0, name
    return {
        "exact_rational_identities": list(identities),
        "local_parameters": "alpha'=alpha+delta, beta'=alpha-delta, gamma'=alpha^2/2-delta*alpha-delta^2/2",
        "allowed_denominators": "2, Psi(g), Psi(g0)^2-1 are units under the retained original hypotheses.",
        "scope": "These identities verify the proposed non-E Low family in all odd characteristics. They do not replace the standard-mathematics topological and arithmetic proofs."
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
    note = ROOT/"notes/selmer-support-continuation-rank-three-propagation.md"
    result = {
        "classification": "Closed literal normalized PropagationTheoremGL3; independently reviewed.",
        "proof_file": str(note.relative_to(ROOT)), "proof_sha256": digest(note.read_bytes()),
        "source_records": records, "exact_diagnostics": exact_checks(),
        "dependencies": [{"file": name, "sha256": digest((ROOT/name).read_bytes())}
                         for name in ["notes/selmer-support-continuation-type-e.md",
                                      "notes/selmer-support-continuation-rank-three-sharp.md"]],
        "decisive_interfaces": {
            "nice_curves": "The exact N_v ordered coincidences and uniformizer cut are retained; completed-chart dimension uses algebraization, not fraction-field transcendence.",
            "coefficient_fibre": "Low polynomial families map into the original A3 through a homogeneous universal algebra. Evaluation occurs only in that polynomial algebra, never in arbitrary completed series.",
            "seed": "The literal weaker SeedIn I subset Z subset xi intersect B3 is used, with dim(B3/Z)=3d+1.",
            "thick_chains": "Intermediate type-E components are supplied by I3 and actual Thick; they are not assumed Hecke-good.",
            "output": "AllGood(I); OffFin is witnessed by I intersect I3 with the exact FinLam inclusion."
        },
        "scope": {"whole_node_closed": False, "lean_build": False,
                  "remaining": "Actual arithmetic Nice/Thick transfer is supplied by its companion reviewed package; finite-point/endomorphism transfer and the moving-family integral Selmer estimate remain separate."}
    }
    result["presentation_files"] = [
        {"file": name, "sha256": digest((ROOT/name).read_bytes())}
        for name in ["paper/shared/selmer-support-continuation-rank-three.tex",
                     "paper/shared/selmer-support-continuation-rank-three-references.tex"]]
    out = ROOT/"certificates/selmer-support-continuation-rank-three-propagation.json"
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"source_files": len(records), "exact_diagnostics": "passed",
                      "certificate": str(out.relative_to(ROOT)), "no_whole_node_completion": True}))


if __name__ == "__main__":
    main()
