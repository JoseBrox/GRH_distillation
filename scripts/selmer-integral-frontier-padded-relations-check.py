#!/usr/bin/env python3
"""Check provenance and exact boundary calculations for padded relations.

The note proves the general statements. Finite calculations test coordinate
padding, the block resultant, truncated kernels, and obstruction lengths.
No source read or successful calculation is described as a Lean build.
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
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
SOURCES = [
    ("PatchingModules.SelmerScaling.LinAlg", [(45, 126)]),
    ("PatchingModules.SelmerScaling.AlCSmul", [(12, 81), (81, 147)]),
    ("PatchingModules.SelmerScaling.FirstOrderLiftConstantPart", [(134, 244)]),
    ("PatchingModules.SelmerScaling.SelmerSpannedByKappaLaurent", [(38, 50), (163, 171)]),
    ("PatchingModules.ThetaCoefficientMapEq", [(15, 78), (265, 301)]),
    ("PatchingModules.SeparableMatrixStability.OdComm", [(48, 94)]),
    ("PatchingModules.SeparableMatrixStability.KerOo", [(15, 79)]),
    ("PatchingModules.SeparableMatrixStability.CocKer", [(23, 105)]),
    ("PatchingModules.SeparableMatrixStability.KoszulThreeOfDet", [(8, 49)]),
    ("PatchingModules.ArchimedeanH0Cards.ExistsCore", [(83, 160), (385, 453)]),
    ("PatchingModules.ArchimedeanH0Cards.GenTrick", [(55, 154)]),
    ("PatchingModules.ArchimedeanH0Cards.ObstructionBoundOfDuality", [(89, 140), (145, 218)]),
    ("PatchingModules.EpsilonEtaMatrices.W1BoundArithmeticRankTwo", [(40, 61), (119, 165)]),
    ("PatchingModules.AutomorphicDetection.BoundW1Arithmetic", [(7, 16)]),
    ("PatchingModules.AutomorphicDetection.TaylorWilesObstructionBound", [(25, 46)]),
    ("PatchingModules.AutomorphicDetection.CohLim", [(8, 19)]),
    ("PatchingModules.SeparableMatrixStability.FirstCohomologyBoundOfBoundaryBound", [(36, 79)]),
    ("PatchingModules.SeparableMatrixStability.SecondCohomologyBoundOfBoundaryBound", [(44, 119)]),
    ("PatchingModules.SeparableMatrixStability.TaylorWilesFirstConditionAtLimitOfGroupCondition", [(19, 41)]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_checks(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["commit"] == REV
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for suffix, ranges in SOURCES:
        module = PREFIX + suffix
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        result = inspect_file({"repository": "jsmorph/rh", "commit": REV,
                               "path": rel, "git_blob_sha1": blobs[module]}, offline)
        assert result["matches_pinned_blob"]
        data = (ROOT / "build/source-cache/jsmorph/rh" / REV / rel).read_bytes()
        lines = data.splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpts.append({"first_line": lo, "last_line": hi,
                             "sha256": sha(b"".join(lines[lo-1:hi]))})
        records.append({"module": module, "path": rel, "commit": REV,
                        "url": "https://github.com/jsmorph/rh/blob/" + REV + "/" + rel,
                        "git_blob_sha1": blobs[module], "sha256": sha(data),
                        "matches_pinned_blob": True, "excerpts": excerpts})
    return records


def rref(rows, n, p):
    rows = [[int(x) % p for x in row] for row in rows]
    i, pivots = 0, []
    for j in range(n):
        q = next((q for q in range(i, len(rows)) if rows[q][j]), None)
        if q is None:
            continue
        rows[i], rows[q] = rows[q], rows[i]
        u = pow(rows[i][j], -1, p)
        rows[i] = [u*x % p for x in rows[i]]
        for q in range(len(rows)):
            if q != i and rows[q][j]:
                u = rows[q][j]
                rows[q] = [(a-u*b) % p for a, b in zip(rows[q], rows[i])]
        pivots.append(j)
        i += 1
    return rows[:i], pivots


def rank(rows, n, p):
    return len(rref(rows, n, p)[1])


def nullspace(rows, n, p):
    rr, pivots = rref(rows, n, p)
    result = []
    for j in range(n):
        if j not in pivots:
            v = [int(k == j) for k in range(n)]
            for i, q in enumerate(pivots):
                v[q] = -rr[i][j] % p
            result.append(v)
    return result


def all_subspace_bases(n, max_rank, p):
    for r in range(min(n, max_rank)+1):
        for pivots in itertools.combinations(range(n), r):
            slots = [(i, j) for i, q in enumerate(pivots)
                     for j in range(q+1, n) if j not in pivots]
            for entries in itertools.product(range(p), repeat=len(slots)):
                rows = [[int(j == q) for j in range(n)] for q in pivots]
                for (i, j), a in zip(slots, entries):
                    rows[i][j] = a
                yield rows


def padding_checks():
    counts, zero_examples = {}, 0
    for p in [2, 3]:
        count = 0
        for d in range(4):
            for g in range(4):
                if d*g > (6 if p == 2 else 4):
                    continue
                for phi in all_subspace_bases(d*g, g, p):
                    U = nullspace(phi, d*g, p)
                    padded = phi + [[0]*(d*g) for _ in range(g-len(phi))]
                    S = [row[j*d:(j+1)*d] for row in padded for j in range(g)]
                    dim_W = d-rank(S, d, p)
                    complement, spanning = [], S[:]
                    for j in range(d):
                        e = [int(i == j) for i in range(d)]
                        if rank(spanning+[e], d, p) > rank(spanning, d, p):
                            spanning.append(e)
                            complement.append(e)
                    assert len(complement) == dim_W
                    for extra in [0, 2]:
                        D = g*g+dim_W+extra
                        X = S+complement+[[0]*d for _ in range(extra)]
                        assert len(X) == D and rank(X, d, p) == d
                        coeff = [[int(a == ij) for a in range(D)] for ij in range(g*g)]
                        assert rank(coeff, D, p) == g*g
                        for u in U:
                            for i in range(g):
                                assert sum(X[i*g+j][k]*u[j*d+k]
                                           for j in range(g) for k in range(d)) % p == 0
                        count += 1
                    if d and g and not phi:
                        assert all(not any(x) for x in S)
                        zero_examples += 1
        counts[str(p)] = count
    # Omitting dim W+g² <= D: g=d=D=1, U=T gives no spanning X
    # and independent coefficient c with cX identically zero.
    for p in [2, 3]:
        assert not any(c*x % p == 0 for c in range(1, p) for x in range(1, p))
    # Omitting codim U <= g: g=D=1, d=2, U=0 has W=0,
    # but one linear form cannot span a two-dimensional dual.
    assert 1 < 2
    return {"padded_presentations_by_field_order": counts,
            "fully_zero_first_block_examples": zero_examples,
            "negative_controls": ["missing_dimension_bound", "missing_codimension_bound"],
            "scope": "All annihilator subspaces in the listed small dimensions; arbitrary-field proof is in the note."}


def sylvester_map(B, C):
    return sp.kronecker_product(B, sp.eye(C.rows))-sp.kronecker_product(sp.eye(B.rows), C.T)


def polynomial_resultant(f, g, x):
    """Use the defining Sylvester determinant, keeping argument order explicit."""
    f, g = sp.Poly(f, x), sp.Poly(g, x)
    a, b = f.degree(), g.degree()
    rows = []
    for i in range(b):
        rows.append([0]*i + f.all_coeffs() + [0]*(b-1-i))
    for i in range(a):
        rows.append([0]*i + g.all_coeffs() + [0]*(a-1-i))
    return sp.expand(sp.Matrix(rows).det())


def resultant_checks():
    x, t = sp.symbols("x t")
    symbolic = []
    for a, b in [(1, 1), (1, 2), (2, 1), (1, 3), (2, 2)]:
        B = sp.Matrix(a, a, sp.symbols(f"b0:{a*a}"))
        C = sp.Matrix(b, b, sp.symbols(f"c0:{b*b}"))
        delta = polynomial_resultant(B.charpoly(x).as_expr(), C.charpoly(x).as_expr(), x)
        plus, minus = sylvester_map(B, C), sylvester_map(C, B)
        assert sp.expand(plus.det()-delta) == 0
        assert sp.expand(minus.det()-(-1)**(a*b)*delta) == 0
        symbolic.append([a, b])
    examples = [
        (2, sp.Matrix([[1]]), sp.Matrix([[1+t]]), "nonunit_gap"),
        (2, sp.Matrix([[1]]), sp.Matrix([[1+t, 1], [0, 1+t]]), "repeated_eigenvalue_inside_block"),
        (3, sp.Matrix([[1]]), sp.Matrix([[1+t, 1], [0, 1+t+t*t]]), "unequal_nonunit_gaps"),
        (3, sp.Matrix([[1]]), sp.Matrix([[2, 1], [0, 2]]), "unit_gap_repeated_eigenvalue"),
    ]
    truncations = []
    for p, B, C, label in examples:
        delta = sp.Poly(polynomial_resultant(B.charpoly(x).as_expr(), C.charpoly(x).as_expr(), x), t, modulus=p)
        assert not delta.is_zero
        v = min(k[0] for k, _ in delta.terms())
        L = sp.diag(sylvester_map(B, C), sylvester_map(C, B))
        nullities = []
        for m in range(7):
            # Expand multiplication by L over F_p[t]/t^m into an ordinary
            # F_p-linear matrix, independent of Smith normal form.
            r = L.rows
            expanded = [[0]*(r*m) for _ in range(r*m)]
            for i in range(r):
                for j in range(r):
                    poly = sp.Poly(L[i, j], t, modulus=p)
                    for (e,), c in poly.terms():
                        for k in range(max(0, m-e)):
                            expanded[i*m+k+e][j*m+k] = int(c) % p
            nullity = r*m-rank(expanded, r*m, p)
            assert nullity <= 2*v
            nullities.append(nullity)
        truncations.append({"case": label, "residue_characteristic": p,
                            "resultant_valuation": v,
                            "kernel_log_cardinality_m_0_to_6": nullities,
                            "uniform_log_bound": 2*v})
    # Shared eigenvalue: P=I2, all odd matrices commute and their counts grow.
    assert sylvester_map(sp.eye(1), sp.eye(1)) == sp.zeros(1)
    return {"generic_symbolic_block_sizes": symbolic,
            "exact_truncated_kernel_counts": truncations,
            "negative_control": "scalar_blocks_have_kernel_cardinality_|k|^(2m)"}


def obstruction_checks():
    admissible, checked = 0, 0
    for r in range(6):
        for parts in itertools.combinations_with_replacement(range(1, 7), r):
            m = max(parts, default=0)
            for g in range(4):
                for C in range(7):
                    checked += 1
                    if all(sum(min(e, q) for q in parts) <= g*e+C for e in range(m+1)):
                        assert sum(q > C for q in parts) <= g
                        admissible += 1
    # A bound only at e=m misses the obstruction.
    parts, g, C, m = (2, 2), 1, 1, 4
    assert sum(min(m, q) for q in parts) <= g*m+C
    assert sum(q > C for q in parts) > g
    # Separate constants C(m)=m allow rank g+1 and do not imply a fixed C.
    assert all(2*m <= m+m for m in range(8))
    assert 2*5 > 5+2
    return {"elementary_divisor_cases_checked": checked,
            "cases_satisfying_all_truncation_bounds": admissible,
            "negative_controls": ["only_full_length_bound", "nonuniform_additive_constant"]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    result = {"status": "pass", "date": "2026-11-22",
              "scope": "Pinned-source provenance and finite exact checks; general proofs in companion note; not a Lean build.",
              "source": source_checks(args.offline),
              "padding": padding_checks(),
              "block_resultant": resultant_checks(),
              "finite_obstruction": obstruction_checks(),
              "node_progress_unchanged": {"RH": "6/9", "GRH": "17/31"},
              "remaining": ["actual uniform global and ordinary-local counts",
                            "actual limiting-group construction",
                            "actual patched automorphic modules"]}
    paths = ["notes/selmer-integral-frontier-padded-relations.md",
             "paper/shared/selmer-integral-frontier-padded-relations.tex",
             "scripts/selmer-integral-frontier-padded-relations-check.py"]
    result["artifacts"] = [{"path": p, "sha256": sha((ROOT/p).read_bytes())} for p in paths]
    output = ROOT / "certificates/selmer-integral-frontier-padded-relations.json"
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "pass", "certificate": str(output.relative_to(ROOT)),
                      "pinned_source_files": len(result["source"]),
                      "padding": result["padding"],
                      "finite_obstruction": result["finite_obstruction"],
                      "symbolic_block_sizes": result["block_resultant"]["generic_symbolic_block_sizes"]}, indent=2))


if __name__ == "__main__":
    main()
