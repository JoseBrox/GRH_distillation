#!/usr/bin/env python3
"""Exact coefficient-algebra checks and pinned provenance for integral Detects.

The mathematical proof is in the companion note. This is not a Lean build.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path

from check_sources import inspect_file
from check_selmer_integral_frontier_odd_detection import add, mul, neg

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
PA = BASE+"PatchingModules."
RANGES = {
    BASE+"WeilGroupCharacters.UniversalOrdinaryDeterminantRing": [(66, 80), (101, 103)],
    PA+"PairedDualFirstOrderDualMatrixSpace": [(108, 150), (203, 224), (240, 264), (306, 322)],
    PA+"DeterminantPadicFree.W1sMem": [(5, 45)],
    PA+"DeterminantPadicFree.ConstantAndLinearPartsZeroOfMem": [(157, 246)],
    PA+"DeterminantPadicFree.MapSpan": [(14, 90), (96, 150)],
    PA+"DeterminantPadicFree.DetAsm": [(9, 20), (110, 171), (176, 212), (213, 268)],
    PA+"ThetaCoefficientMapEq": [(244, 258)],
}


def basis_product(i, j, r):
    if i is None or j is None:
        return None
    if i == 0:
        return j
    if j == 0:
        return i
    if (1 <= i <= r and r+1 <= j <= 2*r and j-i == r) or (
            1 <= j <= r and r+1 <= i <= 2*r and i-j == r):
        return 2*r+1
    return None


def algebra_checks():
    triples, families, negative_controls = 0, [], []
    one_poly = {(): 1}
    for r in range(4):
        d = 2*r+2
        eta = d-1
        for i, j, k in itertools.product(range(d), repeat=3):
            assert basis_product(basis_product(i, j, r), k, r) == basis_product(i, basis_product(j, k, r), r)
            assert basis_product(i, j, r) == basis_product(j, i, r)
            triples += 1

        def product(x, y):
            out = [{} for _ in range(d)]
            for i, a in enumerate(x):
                for j, b in enumerate(y):
                    k = basis_product(i, j, r)
                    if k is not None:
                        out[k] = add(out[k], mul(a, b))
            return out

        one = [{} for _ in range(d)]
        one[0] = one_poly
        B = [{} for _ in range(d)]
        B2 = [{} for _ in range(d)]
        Z = [{} for _ in range(d)]
        Z[eta] = {("P",): 1}
        for i in range(r):
            B[1+i] = {(f"K{i}",): 1}
            B2[1+i] = {(f"U{i}",): 1}
            Z[1+r+i] = {(f"L{i}",): 1}
        plus = [add(x, y) for x, y in zip(one, B)]
        minus = [add(x, neg(y)) for x, y in zip(one, B)]
        assert product(B, B) == [{} for _ in range(d)]
        assert product(plus, minus) == one
        assert product(plus, [add(x, y) for x, y in zip(one, B2)]) == [add(x, y, z) for x, y, z in zip(one, B, B2)]
        action = product(product(plus, Z), minus)
        expected = [dict(x) for x in Z]
        for i in range(r):
            expected[eta] = add(expected[eta], {(f"K{i}", f"L{i}"): 1,
                                                (f"L{i}", f"K{i}"): -1})
        assert action == expected
        constant_rho = [{} for _ in range(d)]
        constant_rho[0] = {("R",): 1}
        detected_matrix = product(product(Z, plus), constant_rho)[eta]
        expected_detected = {("P", "R"): 1}
        for i in range(r):
            expected_detected = add(expected_detected, {(f"L{i}", f"K{i}", "R"): 1})
        assert detected_matrix == expected_detected
        if r:
            assert product(product(plus, Z), plus) != expected
            wrong_order = {("P", "R"): 1}
            for i in range(r):
                wrong_order = add(wrong_order, {(f"K{i}", f"L{i}", "R"): 1})
            assert detected_matrix != wrong_order
            invisible = [{} for _ in range(d)]
            invisible[1] = one_poly
            assert invisible != [{} for _ in range(d)]
            assert invisible[eta] == {} and all(invisible[1+r+i] == {} for i in range(r))
        families.append({"r": r, "algebra_rank": d, "action": "PASS",
                         "eta_trace_order": "Z_i K_i rho", "inverse": "1-B"})
    negative_controls = ["replace inverse 1-B by 1+B", "reverse detected Z_i K_i order",
                         "drop the condition that constant/unprimed coordinates vanish"]
    return {"coefficient_ring": "Z with freely noncommuting matrix variables",
            "basis_associativity_triples": triples, "families": families,
            "negative_controls_rejected": negative_controls}


def laurent_checks():
    cases, zero_cases, lower_exponent_failures = 0, 0, 0
    for p, a, b, r, s in itertools.product([3, 5, 7], [1, 2], [0, 1, 2], range(3), [1, -1]):
        n = a+b
        matrices = []
        for family in range(r+1):
            matrix = [[{} for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(i, n):
                    same_block = (i < a) == (j < a)
                    allowed = same_block if family == 0 else not same_block
                    if not allowed or (i == j and s == -1):
                        continue
                    exponent = -(1+(i+2*j+family) % 4)
                    value = {exponent: 1, 1: (i+j+family+1) % p}
                    value = {e: c for e, c in value.items() if c}
                    matrix[i][j] = value
                    matrix[j][i] = {e: s*c % p for e, c in value.items() if s*c % p}
            matrices.append(matrix)
        exponents = [e for matrix in matrices for row in matrix for value in row for e in value]
        N = max([0]+[-e for e in exponents])
        if not exponents:
            zero_cases += 1
            assert N == 0
        cleared = [[[{e+N: c for e, c in value.items()} for value in row] for row in matrix]
                   for matrix in matrices]
        for family, matrix in enumerate(cleared):
            for i, j in itertools.product(range(n), repeat=2):
                assert all(e >= 0 for e in matrix[i][j])
                assert matrix[i][j] == {e: s*c % p for e, c in matrix[j][i].items() if s*c % p}
                same_block = (i < a) == (j < a)
                if (family == 0 and not same_block) or (family > 0 and same_block):
                    assert matrix[i][j] == {}
        if N:
            assert any(e+N-1 < 0 for e in exponents)
            lower_exponent_failures += 1
        # Integral assembly and both projections, entry by entry.
        for i, j in itertools.product(range(n), repeat=2):
            entry = [{} for _ in range(2*r+2)]
            entry[-1] = cleared[0][i][j]
            for family in range(r):
                entry[1+r+family] = cleared[family+1][i][j]
            assert entry[0] == {} and all(entry[1+family] == {} for family in range(r))
            assert entry[-1] == cleared[0][i][j]
            assert all(entry[1+r+family] == cleared[family+1][i][j] for family in range(r))
        cases += 1
    return {"cases": cases, "characteristics": [3, 5, 7],
            "empty_or_zero_primitive_cases": zero_cases,
            "insufficient_common_exponent_rejections": lower_exponent_failures,
            "checks": "Common t-denominator, prescribed even/odd support, s-transpose polarization, and exact integral coefficient assembly."}


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
        raw = (ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]).read_bytes()
        lines = raw.splitlines(keepends=True)
        excerpts = []
        for start, end in intervals:
            assert 1 <= start <= end <= len(lines) and end-start+1 <= 120
            excerpts.append({"start": start, "end": end,
                             "sha256": hashlib.sha256(b"".join(lines[start-1:end])).hexdigest()})
        sources.append({**item, "module": module, "sha256": checked["sha256"],
                        "matches_pinned_blob": True, "reviewed_excerpts": excerpts})
    artifacts = ["notes/selmer-integral-frontier-integral-detection.md",
                 "paper/shared/selmer-integral-frontier-integral-detection.tex",
                 "paper/shared/selmer-integral-frontier-integral-detection-references.tex",
                 "scripts/check_selmer_integral_frontier_integral_detection.py"]
    dependencies = ["certificates/selmer-integral-frontier-odd-detection.json",
                    "certificates/selmer-integral-frontier-even-detection.json",
                    "scripts/check_selmer_integral_frontier_odd_detection.py"]
    report = {
        "schema_version": 1, "status": "PASS",
        "claim": "Exact coefficient-algebra, integral assembly and source-provenance checks supporting the human proof of original Detects(H).",
        "result": "Every integral paired cocycle annihilated by the eta-trace on the original cyclotomic kernel has a polarized integral boundary after one power of t.",
        "quantifiers": "Fix normalized point and odd family; for every integral paired cocycle z, there exist N>=0 and integral Y, such that t^N z(g)=chi(g)rho1(g)Yrho1(g)^(-1)-Y for every g.",
        "preserved_hypotheses": ["Original full cyclotomic kernel H", "Odd characteristic", "Original integral normalized-point span", "Independent integral polarized odd Selmer family", "Exact eta/epsilon-prime projections and source polarization s=-chi(c)"],
        "sources": sources,
        "exact_checks": {"coefficient_algebra": algebra_checks(), "common_denominator": laurent_checks()},
        "limits": ["The human theorem is not proved by this script; no Lean build was run.",
                   "Laurent-polynomial examples are finite exact checks; the proof covers arbitrary Laurent series.",
                   "No exponent uniform over all cocycles or points is asserted.",
                   "Finite simultaneous auxiliary choice and construction of the original arithmetic inputs are separate tasks.",
                   "No whole proof node closes; RH 6/9 and GRH 17/31 remain unchanged."],
        "reproduce": "python3 scripts/check_selmer_integral_frontier_integral_detection.py --offline",
        "artifacts": {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in artifacts},
        "dependencies": {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in dependencies},
    }
    (ROOT/"certificates/selmer-integral-frontier-integral-detection.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "pinned_modules": len(sources),
                      "basis_associativity_triples": report["exact_checks"]["coefficient_algebra"]["basis_associativity_triples"],
                      "denominator_cases": report["exact_checks"]["common_denominator"]["cases"],
                      "zero_primitive_cases": report["exact_checks"]["common_denominator"]["empty_or_zero_primitive_cases"],
                      "negative_controls": len(report["exact_checks"]["coefficient_algebra"]["negative_controls_rejected"])}))


if __name__ == "__main__":
    main()
