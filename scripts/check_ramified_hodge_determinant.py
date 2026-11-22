#!/usr/bin/env python3
"""Authenticate bounded contracts and test exact ramified determinant indices.

The general theorem is a mathematical proof in the accompanying note.
These Smith/Hermite computations are finite independent lattice checks,
not an automated proof of that theorem or a Lean kernel replay.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PREFIX = "Development.AutomorphicSpectrum.Proofs."
SOURCES = [
    ("AlgebraProofs.CmTypeValuationEmbedding", [[20, 63], [291, 301]]),
    ("AlgebraProofs.ValuationLatticeMatrixReduction", [[198, 254]]),
    ("AlgebraProofs.StatementUnavailableOne", [[5, 8]]),
    ("GeometryProofs.EigenLinePAdicFrame", [[72, 88], [295, 338]]),
    ("GeometryProofs.HodgeLatticeSpanIndependent", [[8, 18]]),
    ("GeometryProofs.ExistsHodgeLatticeGermSystem", [[84, 114]]),
    ("GeometryProofs.HodgeLatticeDvrDegree", [[163, 201], [202, 237]]),
    ("GeometryProofs.EigenLinePAdicBound", [[193, 251]]),
]
GLOBAL_SOURCES = [
    ("ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry."
     "ToroidalCompactification.PushInvertible", [[52, 66]]),
    ("ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry."
     "ToroidalCompactification.TwoWeightEqOneAddRoot", [[72, 91]]),
]
PRIMARY = {
    "path": "build/reference-cache/milne-ant-2020.pdf",
    "url": "https://www.jmilne.org/math/CourseNotes/ANT.pdf",
    "sha256": "24b83c789a89f25aebffb3cbe4ae5ca29edd0075acc072de093d140770630847",
    "inspected": ("Version 3.08 (2020), Proposition 7.50, Corollary 7.51, "
                  "Proposition 7.55, Remark 7.56, pp.127-130; "
                  "pdftotext -layout splitlines ranges 6742-6810, 6863-6901."),
}


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def source_evidence(fetch: bool) -> list[dict]:
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    entries = {row[0]: row for row in atlas["modules"]}
    result = []
    full_sources = [(PREFIX + suffix, bounds) for suffix, bounds in SOURCES] + GLOBAL_SOURCES
    for module, bounds in full_sources:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        evidence = inspect_file({
            "repository": "jsmorph/rh", "commit": REV, "path": path,
            "git_blob_sha1": entries[module][1],
        }, offline=not fetch)
        raw = (ROOT / "build/source-cache/jsmorph/rh" / REV / path).read_bytes()
        lines = raw.splitlines()
        excerpts = []
        for lo, hi in bounds:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            text = b"\n".join(lines[lo-1:hi]) + b"\n"
            assert len(text) <= 12000
            excerpts.append({"lines": [lo, hi], "sha256": sha(text)})
        result.append({
            "module": module, "path": path, "sha256": evidence["sha256"],
            "git_blob_sha1": evidence["git_blob_sha1"],
            "url": f"https://github.com/jsmorph/rh/blob/{REV}/{path}",
            "inspected_excerpts": excerpts,
        })
    return result


def primary_evidence(fetch: bool) -> dict:
    path = ROOT / PRIMARY["path"]
    if not path.exists() and fetch:
        request = Request(PRIMARY["url"], headers={"User-Agent": "Mozilla/5.0"})
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(urlopen(request, timeout=45).read())
    assert sha(path.read_bytes()) == PRIMARY["sha256"]
    return PRIMARY


def integer_kernel(matrix: sp.Matrix) -> sp.Matrix:
    """A saturated integer kernel, checked using unimodular Smith matrices."""
    rows, cols = matrix.shape
    if rows == 0:
        return sp.eye(cols)
    if cols == 0:
        return sp.zeros(0, 0)
    domain = DomainMatrix.from_Matrix(matrix).convert_to(sp.ZZ)
    diagonal, left, right = smith_normal_decomp(domain)
    diagonal, left, right = (a.to_Matrix() for a in (diagonal, left, right))
    assert diagonal == left * matrix * right
    assert abs(left.det()) == 1 and abs(right.det()) == 1
    rank = sum(diagonal[i, i] != 0 for i in range(min(rows, cols)))
    kernel = right[:, rank:]
    assert matrix * kernel == sp.zeros(rows, cols-rank)
    return kernel


def vp(value: int, p: int) -> int:
    value = abs(int(value))
    assert value != 0
    exponent = 0
    while value % p == 0:
        value //= p
        exponent += 1
    return exponent


def torsion_length(matrix: sp.Matrix, p: int) -> int:
    if matrix.rows == 0:
        return 0
    diagonal, left, right = smith_normal_decomp(
        DomainMatrix.from_Matrix(matrix).convert_to(sp.ZZ))
    assert diagonal == left * DomainMatrix.from_Matrix(matrix).convert_to(sp.ZZ) * right
    diagonal = diagonal.to_Matrix()
    return sum(vp(diagonal[i, i], p) for i in range(min(diagonal.shape))
               if diagonal[i, i] != 0)


def quotient_case(p: int, roots: list[int], n: int,
                  ranks: list[int], seed: int) -> dict:
    """Build L as an actual integer image, not from the predicted index."""
    m, total = len(roots), sum(ranks)
    evaluations, maps, inverses = [], [], []
    for i, root in enumerate(roots):
        evaluation = sp.zeros(n, n*m)
        for j in range(n):
            for power in range(m):
                evaluation[j, j*m+power] = root**power
        change = sp.eye(n)
        if n > 1:
            for step in range(2*n+1):
                row = (i+step) % n
                col = (row+1+(step//n)) % n
                if col == row:
                    col = (col+1) % n
                elementary = sp.eye(n)
                elementary[row, col] = ((seed+2*i+step) % 5)-2
                change = elementary * change
        assert change.det() == 1
        rank = ranks[i]
        maps.append(change[:rank, :])
        inverses.append(change.inv()[:, :rank])
        evaluations.append(evaluation)
    projection = sp.Matrix.vstack(*[maps[i] * evaluations[i] for i in range(m)])
    assert projection.shape == (total, n*m)
    assert projection.rank() == total
    kernel = integer_kernel(projection)
    lattice = hermite_normal_form(projection) if total else sp.zeros(0, 0)
    assert lattice.shape == (total, total)
    assert lattice.det() != 0
    root_diagonal = sp.diag(*[root for root, rank in zip(roots, ranks)
                             for _ in range(rank)])
    operator = lattice.inv() * root_diagonal * lattice if total else sp.zeros(0, 0)
    assert all(entry.q == 1 for entry in operator)
    offsets = [sum(ranks[:i]) for i in range(m)]
    rows = []
    for i, root in enumerate(roots):
        eigenkernel = integer_kernel(operator-root*sp.eye(total))
        assert eigenkernel.cols == ranks[i]
        ambient = lattice * eigenkernel
        start, rank = offsets[i], ranks[i]
        eigen_block = ambient[start:start+rank, :]
        assert eigen_block.shape == (rank, rank) and eigen_block.det() != 0
        for j in range(m):
            if j != i:
                assert ambient[offsets[j]:offsets[j]+ranks[j], :] == sp.zeros(ranks[j], rank)
        lifts = inverses[i] * eigen_block
        kernel_projection = hermite_normal_form(evaluations[i] * kernel)
        assert kernel_projection.shape == (n, n-rank)
        adapted = sp.Matrix.hstack(kernel_projection, lifts)
        assert adapted.shape == (n, n) and adapted.det() != 0
        index = vp(adapted.det(), p)
        expected = sum(ranks[j] * vp(root-roots[j], p)
                       for j in range(m) if j != i)
        torsion = torsion_length(operator-root*sp.eye(total), p)
        projection_index = vp(eigen_block.det(), p)
        assert index == expected == torsion + projection_index
        rows.append({
            "root": root, "quotient_rank": rank,
            "actual_adapted_determinant": str(adapted.det()),
            "index_valuation": index, "weighted_root_difference_valuation": expected,
            "cokernel_torsion_length": torsion,
            "image_to_kernel_length": projection_index,
        })
    return {"prime": p, "roots": roots, "free_coefficient_rank": n,
            "signature": ranks, "mixing_seed": seed, "characters": rows}


def exact_lattice_checks() -> dict:
    cases = []
    configurations = [(2, [0, 2, 6]), (3, [0, 3, 12]),
                      (2, [0, 2, 4, 8]), (5, [0, 5])]
    for p, roots in configurations:
        for n in (1, 2, 3):
            m = len(roots)
            patterns = {(0,)*m, (n,)*m,
                        tuple((i+1) % (n+1) for i in range(m)),
                        tuple(n if i % 2 else 0 for i in range(m))}
            for ranks in sorted(patterns):
                cases.append(quotient_case(p, roots, n, list(ranks), len(cases)+1))
    cases.append(quotient_case(2, [0, 2], 0, [0, 0], 1))
    # The full normalization module has generic rank one but is not B-free.
    # Its zero-character image and kernel are both Z_(2), contradicting the
    # predicted factor 2 if the full-coefficient-freeness hypothesis is removed.
    normalized_operator = sp.diag(0, 2)
    actual_kernel = integer_kernel(normalized_operator)
    assert actual_kernel == sp.Matrix([[1], [0]])
    diagnostic = {"prime": 2, "roots": [0, 2], "module": "R^2, T=diag(0,2)",
                  "actual_index": 0, "incorrect_prediction_without_freeness": 1,
                  "full_coefficient_freeness_required": True}
    return {"status": "PASS", "quotient_cases": len(cases),
            "character_cases": sum(len(a["characters"]) for a in cases),
            "cases": cases, "nonfree_diagnostic": diagnostic,
            "scope": "Exact finite integer lattices localized at the stated prime; no general proof or arithmetic model construction."}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true")
    args = parser.parse_args()
    checks = exact_lattice_checks()
    result = {
        "status": "PASS",
        "automated_scope": ("Pinned-source authentication, bounded excerpt hashes, "
                            "primary PDF hash, and exact Smith/Hermite lattice computations."),
        "independent_review": "certificates/frontier-progress-review-2026-11-22.json",
        "sources": source_evidence(args.fetch),
        "primary_reference": primary_evidence(args.fetch),
        "finite_checks": checks,
        "artifacts": [{"path": path, "sha256": sha((ROOT/path).read_bytes())}
                      for path in ["notes/ramified-hodge-determinant.md",
                                   "scripts/check_ramified_hodge_determinant.py"]],
        "not_claimed": [
            "Lean kernel replay or transitive upstream proof verification",
            "Automated proof of the general determinant theorem",
            "Construction of the actual arithmetic moduli model",
            "Construction of integral CM maps to the selected component",
            "Any new completion in the RH or GRH proof maps",
        ],
    }
    (ROOT/"certificates/ramified-hodge-determinant.json").write_text(
        json.dumps(result, indent=2)+"\n")
    print(f"PASS: {len(result['sources'])} pinned Lean modules and 1 primary PDF;")
    print(f"{checks['quotient_cases']} exact quotients, {checks['character_cases']} character indices, and the nonfree diagnostic.")
    print("Scope: source authentication and finite exact lattice algebra; no Lean replay.")


if __name__ == "__main__":
    main()
