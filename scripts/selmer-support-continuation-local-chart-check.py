#!/usr/bin/env python3
"""Authenticate the actual local-chart interfaces and check matrix identities.

This verifies source correspondence and finite algebraic identities, not
the p-adic Hodge-theoretic proof or a Lean rebuild.
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
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    "PadicHodgeTheory.IsInertiaInfiniteCyclotomic": [(11, 62), (72, 104), (110, 162)],
    "PadicHodgeTheory.RtCompl": [(22, 24)],
    "PadicHodgeTheory.RtChart": [(41, 74)],
    "PadicHodgeTheory.RtConj": [(8, 14)],
    "PadicHodgeTheory.LocGood": [(93, 124)],
    "PadicHodgeTheory.DimZ1fCrystallineDeformation": [(130, 182), (184, 219)],
    "UnitaryThreeGroups.ConjStable": [(18, 37), (54, 85)],
    "UnitaryThreeGroups.ModelOfPres": [(241, 277), (295, 329)],
    "UnitaryThreeGroups.ModelLower": [(248, 285), (296, 365), (373, 401)],
    "UnitaryThreeGroups.PtShape": [(85, 171)],
    "UnitaryThreeGroups.FreeEtaleSheafZmodExistsHomSendingGenerator": [(8, 58), (60, 120)],
    "UnitaryThreeGroups.OneCharOf": [(102, 178)],
    "UnitaryThreeGroups.KatoUse": [(54, 64)],
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def matrix_checks() -> dict:
    t, p, a, u, eps = sp.symbols("t p a u eps", nonzero=True)
    J = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    tor = sp.diag(t, 1, 1/t)
    dimensions = []
    for weight in range(-2, 3):
        basis = []
        for i in range(3):
            for j in range(3):
                eij = sp.zeros(3)
                eij[i, j] = 1
                if all(sp.simplify(v) == 0 for v in tor*eij*tor.inv()-t**weight*eij):
                    basis.append(eij)
        for eij in basis:
            reflected = -J*eij.T*J
            assert all(sp.simplify(v) == 0 for v in tor*reflected*tor.inv()-t**weight*reflected)
            assert -J*reflected.T*J == eij
        # These are the Bloch--Kato dimensions proved in the text, then
        # combined with the independently computed matrix multiplicities.
        count = len(basis)*(2 if weight > 0 else 1)
        dimensions.append({"weight": weight, "matrix_dimension": len(basis),
                           "framed_finite_cocycle_dimension": count})
    assert [item["framed_finite_cocycle_dimension"] for item in dimensions] == [1, 2, 3, 4, 2]
    assert sum(item["framed_finite_cocycle_dimension"] for item in dimensions) == 12

    # Compute the original trace-defined saturation element on the
    # unramified diagonal family directly from its matrix definition.
    inertia = sp.diag(p, 1, 1/p)
    eigen = [p, 1, 1/p]
    fr = sp.diag(a*u, 1, 1/(a*u))
    cc = [sp.prod(eigen[i]-eigen[j] for j in range(3) if j != i) for i in range(3)]
    traces = []
    for i in range(3):
        factors = [inertia-eigen[j]*sp.eye(3) for j in range(3) if j != i]
        traces.append(sp.trace(factors[0]*factors[1]*fr))
    dd = [sp.factor(cc[i+1]*traces[i]-eps*cc[i]*traces[i+1]) for i in range(2)]
    assert sp.simplify(dd[0]-cc[0]*cc[1]*(a*u-eps)) == 0
    assert sp.simplify(dd[1]-cc[1]*cc[2]*(a*u-eps)/(a*u)) == 0
    assert dd[0] != 0 and dd[1] != 0

    # Local strict-cocycle direction, with the polarized reflection retained.
    x, y, psi = sp.symbols("x y psi", nonzero=True)
    Y = sp.Matrix([[0, 0, 0], [x, 0, 0], [0, y, 0]])
    base = sp.diag(psi, 1, 1/psi)
    for sign in [1, -1]:
        action = Y if sign == 1 else -J*Y.T*J
        coboundary = Y-base*action*base.inv()
        assert all(sp.simplify(v) == 0 for v in tor*coboundary*tor.inv()-coboundary/t)
        # Differentiate (1+sY) base theta(1-sY), coefficient of s.
        s = sp.Symbol("s")
        conjugated = (sp.eye(3)+s*Y)*base*(sp.eye(3)-s*action)
        derivative = conjugated.diff(s).subs(s, 0)*base.inv()
        assert all(sp.simplify(v) == 0 for v in derivative-coboundary)

    # The two cases in the isomorphism-to-torus calculation.
    b, v = sp.symbols("b v", nonzero=True)
    full = sp.Matrix(3, 3, sp.symbols("a0:9"))
    M = sp.diag(t*b, b, b/t)
    assert all(sp.simplify(v) == 0 for v in M*full*M.inv()-tor*full*tor.inv())
    outer = sp.Matrix([[full[0, 0], 0, full[0, 2]],
                       [0, full[1, 1], 0], [full[2, 0], 0, full[2, 2]]])
    M = sp.diag(t*t*v, b, v)
    assert all(sp.simplify(v) == 0 for v in M*outer*M.inv()-tor*outer*tor.inv())
    return {"weights": dimensions, "original_adjacent_factors": [str(v) for v in dd],
            "polarized_coboundary_identity": "passed for both component signs",
            "marked_isomorphism_to_torus": "passed in both diagonal-intertwiner cases"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    lookup = {row[0]: row for row in atlas["modules"]}
    sources = []
    for suffix, ranges in RANGES.items():
        module = PREFIX+suffix
        row = lookup[module]
        path = "lean/src/"+module.replace(".", "/")+".lean"
        entry = {"repository": atlas["repository"], "commit": atlas["commit"],
                 "path": path, "git_blob_sha1": row[1]}
        checked = inspect_file(entry, args.offline)
        data = (ROOT/"build/source-cache"/atlas["repository"]/atlas["commit"]/path).read_bytes()
        lines = data.decode().splitlines()
        excerpts = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines) and end-start < 120
            excerpts.append({"start": start, "end": end,
                             "sha256": sha("\n".join(lines[start-1:end]).encode())})
        sources.append({"module": module, "path": path, "sha256": sha(data),
                        "git_blob_sha1": row[1], "ranges": excerpts,
                        "source_check": checked})
    files = ["paper/shared/selmer-support-continuation-local-chart.tex",
             "paper/shared/selmer-support-continuation-local-chart-references.tex",
             "notes/selmer-support-continuation-local-chart.md"]
    checks = matrix_checks()
    output = {
        "classification": "Closed original local-chart and integral strict-cocycle comparison subobligations; full weighted Selmer product remains open.",
        "source_repository": atlas["repository"], "source_commit": atlas["commit"],
        "scope": "Original selected component It, full integral global equation ideal, same strict-cocycle modulus, and original OneChar normalization.",
        "verification_scope": "Pinned source authentication and exact symbolic matrix identities; no automated p-adic Hodge proof, no actual Selmer-group computation and no Lean rebuild.",
        "primary_theorems": [
            {"author": "Bellovin--Gee", "theorem": "3.3.7, potentially crystalline (N=0) case", "url": "https://msp.org/ant/2019/13-2/ant-v13-n2-p03-p.pdf", "pages": "366--367"},
            {"author": "Colmez--Fontaine", "theorem": "A; exact fully faithful crystalline equivalence", "url": "https://webusers.imj-prg.fr/~pierre.colmez/CF.pdf"},
        ],
        "sources": sources, "exact_checks": checks,
        "artifacts": [{"path": path, "sha256": sha((ROOT/path).read_bytes())} for path in files],
    }
    dest = ROOT/"certificates/selmer-support-continuation-local-chart.json"
    dest.write_text(json.dumps(output, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"certificate": str(dest.relative_to(ROOT)), "sources": len(sources),
                      "exact_matrix_checks": "passed", "scope": output["verification_scope"]}))


if __name__ == "__main__":
    main()
