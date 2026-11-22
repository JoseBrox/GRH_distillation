#!/usr/bin/env python3
"""Bounded provenance and exact algebra checks for the paired odd proof.

This does not check the complete human proof or compile Lean.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.DeterminantPadicFree."
RANGES = {
    "FrameWith": [(26, 72)], "RelMove": [(70, 100)],
    "DTw": [(22, 82)], "DTwAlt": [(4, 50)], "Shapiro": [(7, 64)],
    "BlockPrinc": [(51, 112), (112, 160)],
    "RelPair": [(23, 55), (111, 176)], "OddPart": [(18, 61)],
    "MapSpan": [(14, 83)], "DetAsm": [(165, 213)],
}


def add(*terms):
    result = {}
    for term in terms:
        for word, coefficient in term.items():
            result[word] = result.get(word, 0) + coefficient
    return {word: coefficient for word, coefficient in result.items() if coefficient}


def neg(poly):
    return {word: -coefficient for word, coefficient in poly.items()}


def mul(left, right):
    result = {}
    for u, a in left.items():
        for v, b in right.items():
            result[u+v] = result.get(u+v, 0)+a*b
    return {word: coefficient for word, coefficient in result.items() if coefficient}


def paired_product():
    # Freely noncommuting integral variables. K,L are values at g;
    # A,B are conjugates of the corresponding values at h.
    K, A, L, B, P, Q = ({(v,): 1} for v in "KALBPQ")
    comm = add(mul(K, B), neg(mul(B, K)))
    lhs = add(P, Q, comm, mul(add(L, B), add(K, A)))
    rhs = add(P, mul(L, K), Q, mul(B, A), mul(K, B), mul(L, A))
    assert lhs == rhs
    no_commutator = add(P, Q, mul(add(L, B), add(K, A)))
    wrong_sign = add(P, Q, neg(comm), mul(add(L, B), add(K, A)))
    wrong_order_lhs = add(P, Q, comm, mul(add(K, A), add(L, B)))
    wrong_order_rhs = add(P, mul(K, L), Q, mul(A, B), mul(K, B), mul(L, A))
    assert no_commutator != rhs and wrong_sign != rhs
    assert wrong_order_lhs != wrong_order_rhs
    return {"coefficient_ring": "Z, free associative algebra",
            "paired_product_identity": True,
            "negative_controls_rejected": ["omit commutator", "reverse commutator sign", "reverse lambda-kappa order"]}


def unit_mul(x, y):
    if x is None or y is None or x[1] != y[0]:
        return None
    return (x[0], y[1])


def trace_extraction():
    cases = 0
    for n in range(1, 5):
        units = list(itertools.product(range(n), repeat=2))
        for u, v, a, b in itertools.product(range(n), range(n), units, units):
            product = unit_mul(unit_mul(unit_mul(a, (v, v)), b), (u, u))
            lhs = int(product is not None and product[0] == product[1])
            rhs = int(a == (u, v) and b == (v, u))
            assert lhs == rhs
            cases += 1
    return {"basis_cases": cases, "identity": "tr(A E_vv B E_uu)=A_uv B_vu",
            "scope": "Every matrix-unit basis pair in sizes 1 through 4; bilinear extension."}


def modular_rank(rows, p, columns):
    matrix = [[x % p for x in row] for row in rows]
    pivot_row = 0
    for col in range(columns):
        pivot = next((i for i in range(pivot_row, len(matrix)) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][col], -1, p)
        matrix[pivot_row] = [inverse*x % p for x in matrix[pivot_row]]
        for i in range(pivot_row+1, len(matrix)):
            if matrix[i][col]:
                factor = matrix[i][col]
                matrix[i] = [(x-factor*y) % p for x, y in zip(matrix[i], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


def corner_derivations():
    cases = []
    for a, b, reverse in itertools.product(range(1, 3), range(1, 3), [False, True]):
        n = a+b
        even = [(i, j) for i in range(n) for j in range(n) if (i < a) == (j < a)]
        corner = [(i, j) for i in range(n) for j in range(n)
                  if ((i >= a and j < a) if reverse else (i < a and j >= a))]
        index_even = {x: i for i, x in enumerate(even)}
        index_corner = {x: i for i, x in enumerate(corner)}
        q = len(corner)
        unknowns = len(even)*q
        equations = []
        for i, x in enumerate(even):
            for j, y in enumerate(even):
                rows = [[0]*unknowns for _ in corner]
                xy = unit_mul(x, y)
                if xy is not None:
                    for k in range(q):
                        rows[k][index_even[xy]*q+k] += 1
                for k, z in enumerate(corner):
                    zy = unit_mul(z, y)
                    xz = unit_mul(x, z)
                    if zy is not None:
                        rows[index_corner[zy]][i*q+k] -= 1
                    if xz is not None:
                        rows[index_corner[xz]][j*q+k] -= 1
                equations.extend(rows)
        # Each column is the derivation X -> XP-PX for one corner unit P.
        inner = [[0]*q for _ in range(unknowns)]
        for j, primitive in enumerate(corner):
            for i, x in enumerate(even):
                xp, px = unit_mul(x, primitive), unit_mul(primitive, x)
                if xp is not None:
                    inner[i*q+index_corner[xp]][j] += 1
                if px is not None:
                    inner[i*q+index_corner[px]][j] -= 1
        for p in [3, 5, 7]:
            dimension = unknowns-modular_rank(equations, p, unknowns)
            assert dimension == q and modular_rank(inner, p, q) == q
            assert all(sum(row[i]*inner[i][j] for i in range(unknowns)) % p == 0
                       for row in equations for j in range(q))
            # The chosen row-block idempotent satisfies delta(e)=P, fixing the sign.
            row_indices = range(a, n) if reverse else range(a)
            evaluation = [[sum(inner[index_even[(i, i)]*q+k][j] for i in row_indices)
                           for j in range(q)] for k in range(q)]
            assert evaluation == [[int(i == j) for j in range(q)] for i in range(q)]
            cases.append({"characteristic": p, "block_sizes": [a, b],
                          "corner": "lower" if reverse else "upper",
                          "dimension": dimension, "idempotent_sign": "delta(e)=P"})
    return cases


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    atlas = json.loads(gzip.decompress((ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()))
    rows = {row[0]: row for row in atlas["modules"]}
    sources = []
    for suffix, intervals in RANGES.items():
        module = PREFIX+suffix
        item = {"repository": atlas["repository"], "commit": atlas["commit"],
                "path": "lean/src/"+module.replace(".", "/")+".lean", "git_blob_sha1": rows[module][1]}
        checked = inspect_file(item, offline=args.offline)
        raw = (ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]).read_bytes()
        lines = raw.splitlines(keepends=True)
        excerpts = []
        for start, end in intervals:
            assert 1 <= start <= end <= len(lines) and end-start+1 <= 120
            excerpts.append({"start": start, "end": end,
                             "sha256": hashlib.sha256(b"".join(lines[start-1:end])).hexdigest()})
        sources.append({**item, "module": module, "sha256": checked["sha256"],
                        "matches_pinned_blob": True, "reviewed_excerpts": excerpts})
    artifacts = ["notes/selmer-integral-frontier-odd-detection.md",
                 "paper/shared/selmer-integral-frontier-odd-detection.tex",
                 "paper/shared/selmer-integral-frontier-odd-detection-references.tex",
                 "scripts/check_selmer_integral_frontier_odd_detection.py"]
    report = {
        "schema_version": 1, "status": "PASS",
        "claim": "Pinned source identity and exact algebra checks supporting the human proof of OddPart.",
        "mathematical_result": "Under the exact DetFr/IsKap/IsTw hypotheses, every odd lambda_i is d_chi(Y_i), with Y_i odd and s Y_i^T=Y_i.",
        "human_proof": "Central block idempotent, separation of distinct twists, vanishing of corner H-invariants, polarization, and the four-factor paired trace identity.",
        "preserved_hypotheses": ["Characteristic different from two, including F=k((t)) of odd characteristic", "Full even span of rho(H)", "Nontrivial chi, trivial on H", "Independent polarized odd kappa classes", "Exact paired cocycle and trace equations"],
        "sources": sources,
        "exact_checks": {"paired_product": paired_product(), "trace_extraction": trace_extraction(),
                         "corner_derivations": corner_derivations()},
        "limits": ["This script does not prove the complete theorem or compile Lean.",
                   "Finite-field derivation checks are finite exact validation; the note gives the general proof.",
                   "Even correction, integral denominator clearing and finite simultaneous auxiliary choice are separate suppliers.",
                   "No whole Selmer node is closed; RH 6/9 and GRH 17/31 remain unchanged."],
        "reproduce": "python3 scripts/check_selmer_integral_frontier_odd_detection.py --offline",
        "artifacts": {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in artifacts},
    }
    (ROOT/"certificates/selmer-integral-frontier-odd-detection.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "pinned_modules": len(sources),
                      "trace_basis_cases": report["exact_checks"]["trace_extraction"]["basis_cases"],
                      "finite_field_derivation_cases": len(report["exact_checks"]["corner_derivations"]),
                      "negative_controls": len(report["exact_checks"]["paired_product"]["negative_controls_rejected"])}))


if __name__ == "__main__":
    main()
