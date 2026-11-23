#!/usr/bin/env python3
"""Bind the proposed full rank-two propagation proof to exact contracts.

Finite algebra diagnostics complement the standard-mathematics proof;
they are not a Lean build or a global Selmer computation.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    "CurveDVRSpecialization.PropagationTheoremGL2": [(16, 60), (91, 110)],
    "FrobeniusSmoothVectors.ContinuousCoboundaries2": [(16, 97), (167, 212)],
    "FrobeniusSmoothVectors.LeAdicClosure": [(27, 32), (149, 249)],
    "FrobeniusSmoothVectors.DefIso": [(34, 126)],
    "FrobeniusSmoothVectors.PresDefs": [(176, 185)],
    "FrobeniusSmoothVectors.HasObs": [(26, 120), (121, 124)],
    "FrobeniusSmoothVectors.ChainedBot": [(51, 86)],
    "CurveDVRSpecialization.FirstPrimeConditionTransfer": [(1, 19)],
    "CurveDVRSpecialization.NiceSep": [(59, 106)],
    "CurveDVRSpecialization.NiceIrr": [(61, 135)],
    "CurveDVRSpecialization.NiceSpecializationTwistSatisfiesFirstCondition": [(1, 16)],
    "CurveDVRSpecialization.NiceSpecializationTwistSatisfiesThirdCondition": [(46, 60), (164, 213)],
    "CurveDVRSpecialization.PointEx": [(330, 439)],
    "CurveDVRSpecialization.ComponentsGoodRankTwo": [(33, 106), (107, 163)],
    "FrobeniusSmoothVectors.LocDim": [(110, 178)],
    "FrobeniusSmoothVectors.Seedpt": [(9, 30)],
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def exact_checks():
    p, u = sp.symbols("p u", nonzero=True)
    a, b, c, d, z = sp.symbols("a b c d z")
    J = sp.Matrix([[0, 1], [1, 0]])
    R = sp.Matrix([[p, 0], [u, 1/p]])
    E21 = sp.Matrix([[0, 0], [1, 0]])
    H = sp.diag(1, -1)
    E12 = sp.Matrix([[0, 1], [0, 0]])
    basis = [E21, H, E12, sp.eye(2)]

    def coords(M):
        return sp.Matrix([M[1, 0], (M[0, 0]-M[1, 1])/2,
                          M[0, 1], sp.trace(M)/2])

    adjoint = sp.Matrix.hstack(*(coords(sp.simplify(R*X*R.inv())) for X in basis))
    target = sp.Matrix([[p**-2, 2*u/p, -u*u, 0],
                        [0, 1, -p*u, 0],
                        [0, 0, p*p, 0],
                        [0, 0, 0, 1]])
    assert sp.simplify(adjoint-target) == sp.zeros(4)
    conjugation = sp.Matrix.hstack(*(coords(-J*X.T*J) for X in basis))
    assert conjugation == sp.diag(-1, 1, -1, -1)

    M = sp.Matrix([[a, b], [c, d]])
    scaled = M*sp.diag(z, 1)
    discriminant = sp.expand(sp.trace(scaled)**2-4*scaled.det())
    expected = a*a*z*z+(2*a*d-4*M.det())*z+d*d
    assert sp.expand(discriminant-expected) == 0
    assert sp.Poly(discriminant, z).all_coeffs() == [a*a, -2*a*d+4*b*c, d*d]

    counts = {}
    for ell in (3, 5, 7):
        count = 0
        for aa, bb, cc, dd in itertools.product(range(ell), repeat=4):
            determinant = (aa*dd-bb*cc) % ell
            if not determinant:
                continue
            coefficients = [aa*aa % ell, (2*aa*dd-4*determinant) % ell, dd*dd % ell]
            assert any(coefficients)
            count += 1
        assert count == (ell*ell-1)*(ell*ell-ell)
        counts[ell] = count

    gauge = M*J+J*M.T
    assert gauge == sp.Matrix([[2*b, a+d], [a+d, 2*c]])
    assert M-J*M.T*J == sp.diag(a-d, d-a)
    return {
        "adjoint_filtration": {
            "basis": ["E21", "diag(1,-1)", "E12", "I"],
            "G0_graded_characters": ["Psi^-2", "1", "Psi^2", "1"],
            "c_signs": [-1, 1, -1, -1],
            "Gamma_constituents": ["Psi^-2 delta", "1", "Psi^2 delta", "delta"]
        },
        "gauge_and_marking": "Exact identities verify a one-dimensional orthogonal Lie algebra when 2 is invertible and an automatic rank-two marking.",
        "regular_coset_polynomial": str(expected),
        "all_invertible_matrices_checked_over": counts,
        "regular_coset_scope": "The polynomial is nonzero for every invertible matrix in these finite diagnostics; the proof gives the universal odd-characteristic argument and separately requires an infinite eigenvalue ratio.",
        "prohibited_inferences": [
            "No proof from bounded computation alone.",
            "No residual absolute irreducibility assumption.",
            "No evaluation of arbitrary vertex-completed series at t=1.",
            "No bound on completed fraction-field transcendence degree.",
            "No integral Selmer length or uniform nilpotence estimate."
        ]
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
    note = ROOT/"notes/selmer-support-continuation-rank-two-propagation.md"
    presentation = ROOT/"paper/shared/selmer-support-continuation-rank-two.tex"
    references = ROOT/"paper/shared/selmer-support-continuation-rank-two-references.tex"
    result = {
        "classification": "Closed original rank-two component-propagation subobligation; independently reviewed.",
        "target": "The literal PropagationTheoremGL2 (FinLam, P1', SeedIn imply AllGood), plus the actual arithmetic P1-to-P1' transfer in rank two.",
        "proof_file": str(note.relative_to(ROOT)), "proof_sha256": digest(note.read_bytes()),
        "presentation_files": [
            {"path": str(path.relative_to(ROOT)), "sha256": digest(path.read_bytes())}
            for path in (presentation, references)
        ],
        "source_records": records,
        "primary_reference": {
            "url": "https://stacks.math.columbia.edu/tag/0ECR",
            "result": "Complete-local connectedness bound in terms of cohomological dimension.",
            "checked_application": "Ambient O'[[X_1,...,X_N]] is a complete regular local domain of dimension N+1; r relations have cohomological dimension at most r; N-r>=2d+1. No regular-sequence hypothesis is imposed."
        },
        "exact_diagnostics": exact_checks(),
        "decisive_interfaces": {
            "actual_chart_functor": "Constructed by the Laurent Rees vertex C[t^-1,U t], finite unramified coefficient base change, a closed degree-zero subring, and evaluation only on the finite Laurent algebra.",
            "tangent": "h1+1 for the original ordinary adjoint cone; the original residual representation remains a nontrivial reducible extension.",
            "obstruction": "The full original ordinary adjoint H2 cone, with no cyclotomic quotient verified from F.Ok.f2a/f2c.",
            "presentation": "N-r>=2d+1 from the exact global Euler inequality.",
            "abstract_seed_quantifier": "Z need only lie below the stable point's coefficient contraction. The exact localization A_a=B_a[u,u^-1] produces a stable prime over Z.",
            "abstract_curve_hypotheses": "The curve lemma uses FinLam, Ok and Big only; it does not require an arithmetic Hecke ideal or ModIn.",
            "coefficient_characteristic": "Both mixed and equal characteristic are covered. The coefficient uniformizer remains in lambda_0 and the counted cuts even if ell is zero in O.",
            "arithmetic_P1": "The same curve, TwLink, ordered characters and original N4 condition are used; N1, TypeI on G', and the full N3 open-set quantifier are checked."
        },
        "scope": {"whole_node_closed": False, "lean_build": False,
                  "rank_three": "Type-E components and thick links remain separate.",
                  "integral_selmer": "No weighted length bound or uniform nilpotence exponent is asserted."}
    }
    out = ROOT/"certificates/selmer-support-continuation-rank-two-propagation.json"
    out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"source_files": len(records), "exact_diagnostics": "passed",
                      "certificate": str(out.relative_to(ROOT)), "no_whole_node_completion": True}))


if __name__ == "__main__":
    main()
