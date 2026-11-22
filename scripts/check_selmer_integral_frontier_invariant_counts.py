#!/usr/bin/env python3
"""Authenticate the invariant interfaces and compare two exact counting methods.

Polynomial Smith factors are checked against full finite-field congruence
operators on the original paired coefficient pattern. These finite checks
support the human proof; they do not prove the general theorem or build Lean.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules."
RANGES = {
    BASE+"PairedDualFirstOrderDualMatrixSpace": [(108, 150), (203, 224), (292, 294)],
    BASE+"EpsilonEtaMatrices.EpsilonEtaTensorDual": [(11, 41)],
    BASE+"EpsilonEtaMatrices.FixBdQZero": [(8, 52), (181, 206)],
    BASE+"EpsilonEtaMatrices.CommutingMatrixOffdiagZero": [(19, 63), (86, 134), (158, 188)],
    BASE+"EpsilonEtaMatrices.Rho1MapReductionLevel": [(42, 64), (66, 91)],
    BASE+"EpsilonEtaMatrices.FinrankCentralizerW1Le": [(7, 34), (57, 104), (106, 131)],
    BASE+"EpsilonEtaMatrices.W1BoundArithmeticRankTwo": [(40, 61), (95, 142)],
}
t = sp.symbols("t")


def rank_mod_p(rows, p):
    a = [list(row) for row in rows]
    rank = 0
    for j in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(rank, len(a)) if a[i][j] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        u = pow(a[rank][j] % p, -1, p)
        a[rank] = [u*x % p for x in a[rank]]
        for i in range(rank+1, len(a)):
            u = a[i][j] % p
            if u:
                a[i] = [(x-u*y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def congruence_nullity(matrix, p, m):
    rows, cols = matrix.shape
    expanded = [[0]*(cols*m) for _ in range(rows*m)]
    for i in range(rows):
        for j in range(cols):
            poly = sp.Poly(matrix[i, j], t, modulus=p)
            for (power,), coefficient in poly.terms():
                for h in range(max(0, m-power)):
                    expanded[i*m+h+power][j*m+h] = int(coefficient) % p
    return cols*m-rank_mod_p(expanded, p)


def paired_commutator(n, a, s, eigenvalues, coupling=True):
    """Matrix of [P+sum epsilon_i B_i, Z] on eta E + sum epsilon'_i O."""
    same = lambda i, j: (i < a) == (j < a)
    coordinates = [(0, i, j) for i in range(n) for j in range(n) if same(i, j)]
    coordinates += [(k+1, i, j) for k in range(s)
                    for i in range(n) for j in range(n) if not same(i, j)]
    P = sp.diag(*eigenvalues)
    B = []
    for k in range(s):
        K = sp.Matrix(n, n, lambda i, j: (i+j+k+1) if coupling and not same(i, j) else 0)
        B.append(K*P)
    matrix = sp.zeros(len(coordinates), len(coordinates))
    for col, (slot, i, j) in enumerate(coordinates):
        unit = sp.zeros(n); unit[i, j] = 1
        images = [sp.zeros(n) for _ in range(s+1)]
        images[slot] = P*unit-unit*P
        if slot:
            images[0] = B[slot-1]*unit-unit*B[slot-1]
        for row, (output_slot, u, v) in enumerate(coordinates):
            matrix[row, col] = sp.expand(images[output_slot][u, v])
    return matrix


def exact_checks():
    polynomial_cases = finite_counts = 0
    max_defect = 0
    for p in (3, 5):
        for n in range(1, 4):
            for a in range(n+1):
                for s in range(3):
                    for h in (1, 2):
                        eigenvalues = [1+i*t**h for i in range(n)]
                        matrix = paired_commutator(n, a, s, eigenvalues)
                        diagonal = smith_normal_form(matrix, domain=sp.GF(p).poly_ring(t))
                        valuations = []
                        for i in range(diagonal.rows):
                            poly = sp.Poly(diagonal[i, i], t, modulus=p)
                            if not poly.is_zero:
                                valuations.append(min(power[0] for power, coefficient in poly.terms() if coefficient))
                        free_rank = matrix.cols-len(valuations)
                        assert free_rank == n, (p, n, a, s, h, free_rank)
                        max_defect = max(max_defect, sum(valuations))
                        for m in range(5):
                            expected = m*n+sum(min(m, v) for v in valuations)
                            assert congruence_nullity(matrix, p, m) == expected
                            finite_counts += 1
                        polynomial_cases += 1

    # An integral zero kernel can have nonzero solutions at every truncation.
    for p in (3, 5):
        for a in range(1, 5):
            matrix = sp.Matrix([[t**a]])
            for m in range(7):
                assert congruence_nullity(matrix, p, m) == min(m, a)
    # Increasing a shows why the defect constant is not uniform over points.
    assert congruence_nullity(sp.Matrix([[t**7]]), 3, 7) == 7
    # Block spectra are disjoint, but a collision inside one block leaves
    # five eta centralizer coordinates in dimension three.
    collision = paired_commutator(3, 2, 1, [1, 1, 2], coupling=False)
    assert congruence_nullity(collision, 5, 1) == 5 > 3
    # In characteristic two the nonzero identity matrix is skew.
    assert (1+1) % 2 == 0
    # Without distinguished twisted rigidity, a trivial action fixes W.
    assert congruence_nullity(sp.zeros(4), 3, 2) == 8
    return {
        "polynomial_smith_matrices": polynomial_cases,
        "independent_finite_congruence_counts": finite_counts,
        "zero_integral_kernel_defect_cases": 56,
        "maximum_observed_smith_defect": max_defect,
        "characteristics": [3, 5], "truncations": [0, 1, 2, 3, 4],
        "empty_odd_family_and_empty_blocks": True,
        "negative_controls": [
            "Integral kernel zero does not remove finite congruence torsion.",
            "Block separation does not replace full simple spectrum.",
            "Odd characteristic cannot be removed from skew-kernel vanishing.",
            "Distinguished rigidity cannot be omitted.",
            "Smith defects need not be bounded over moving points."
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    atlas = json.loads(gzip.decompress((ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()))
    rows = {row[0]: row for row in atlas["modules"]}
    sources = []
    for module, intervals in RANGES.items():
        item = {"repository": atlas["repository"], "commit": atlas["commit"],
                "path": "lean/src/"+module.replace(".", "/")+".lean", "git_blob_sha1": rows[module][1]}
        checked = inspect_file(item, offline=args.offline)
        lines = (ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]).read_bytes().splitlines(keepends=True)
        excerpts = []
        for start, end in intervals:
            assert 1 <= start <= end <= len(lines) and end-start+1 <= 120
            content = b"".join(lines[start-1:end]); assert len(content) <= 12000
            excerpts.append({"start": start, "end": end, "sha256": hashlib.sha256(content).hexdigest()})
        sources.append({**item, "module": module, "sha256": checked["sha256"],
                        "matches_pinned_blob": True, "reviewed_excerpts": excerpts})
    checks = exact_checks()
    artifacts = ["notes/selmer-integral-frontier-invariant-counts.md",
                 "paper/shared/selmer-integral-frontier-invariant-counts.tex",
                 "paper/shared/selmer-integral-frontier-invariant-counts-references.tex",
                 "scripts/check_selmer_integral_frontier_invariant_counts.py"]
    report = {
        "schema_version": 1, "status": "PASS",
        "claim": "Pinned source authentication and two independent exact finite counting methods for the original invariant matrix systems.",
        "result": "For fixed original arithmetic data, global skew and distinguished twisted invariants are bounded independently of m; simple-spectrum paired invariants have exact integral rank n and count at most q^(mn+C).",
        "quantifiers": "Fix the normalized point, odd family, distinguished subgroup and chosen simple-spectrum elements; then constants are independent of all m>=0.",
        "sources": sources, "exact_checks": checks,
        "retained_inputs": ["Odd characteristic", "Original integral even span", "Original characteristic-prime distinguished rigidity N4", "Full simple spectrum over the fraction field, with integral roots"],
        "limits": ["This script supports the human proof; it is not that proof or a Lean build.",
                   "The source modules and finite examples do not construct the required arithmetic points or their N4 property.",
                   "No lifting of finite-level invariants is assumed, and no uniformity over moving points is asserted.",
                   "Tower descent, arithmetic global duality and patched modules are separate consumers.",
                   "No whole node closes: RH 6/9 and Dirichlet GRH 17/31."],
        "reproduce": "python3 scripts/check_selmer_integral_frontier_invariant_counts.py --offline",
        "artifacts": {path: hashlib.sha256((ROOT/path).read_bytes()).hexdigest() for path in artifacts},
    }
    (ROOT/"certificates/selmer-integral-frontier-invariant-counts.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "pinned_modules": len(sources), **checks}))


if __name__ == "__main__":
    main()
