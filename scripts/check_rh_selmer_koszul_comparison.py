#!/usr/bin/env python3
"""Exact nonregular Koszul examples and bounded provenance for the lower chain.

This supplements the general proof. It does not verify the remaining
admissibility supplier for the growing arithmetic deformation model.
"""

import gzip
import hashlib
import itertools
import json
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
CALC = "Formalism.SharpRestriction.ValuationFrobeniusEpsilon.LeastPrimeTwists.QuotientShiftIrreducible.NoetherianQuotientCalc."
ALG = "Development.AutomorphicArithmetic.AutomorphicVarieties.CommutativeAlgebra.GradedModulesLength."
SOURCES = [
    (CALC + "EulerVanishingBelowDimension", [(66, 107), (113, 167)]),
    (CALC + "VanishingBelowDimensionRule", [(309, 336)]),
    (CALC + "RulePos", [(24, 45)]),
    (CALC + "RuleMono", [(11, 22)]),
    (CALC + "RuleUB", [(25, 42)]),
    (CALC + "EulerRuleProductZero", [(17, 66)]),
    (ALG + "LaDifPerm", [(49, 124)]),
    (ALG + "AdmissibleMonoIdeal", [(111, 130), (191, 237), (273, 322)]),
    (ALG + "AdmissibilityHolds", [(30, 77)]),
    (ALG + "AlgMemCoef", [(22, 43), (113, 143)]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["commit"] == REV
    blobs = {r[0]: r[1] for r in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        data = (ROOT / "build/source-cache/jsmorph/rh" / REV / path).read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == blobs[module]
        lines = data.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            excerpts.append({"lines": [lo, hi],
                             "sha256": sha(b"\n".join(lines[lo-1:hi]) + b"\n")})
        records.append({"repository": "jsmorph/rh", "commit": REV, "path": path,
                        "sha256": sha(data), "git_blob_sha1": blob, "excerpts": excerpts})
    return records


def det(a):
    if not a:
        return 1
    if len(a) == 1:
        return a[0][0]
    return sum((-1)**j*a[0][j]*det([row[:j]+row[j+1:] for row in a[1:]])
               for j in range(len(a)))


def minors_gcd(a, size):
    if size == 0:
        return 1
    out = 0
    for rows in itertools.combinations(range(len(a)), size):
        for cols in itertools.combinations(range(len(a[0])), size):
            out = gcd(out, det([[a[i][j] for j in cols] for i in rows]))
    return abs(out)


def valuation(n, p):
    n = abs(n)
    assert n
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value, n


def koszul_matrices(f1, f2, degree):
    """Homogeneous degree-d complex for two linear forms in Z[x,y]."""
    d = degree
    differential1 = [[0]*(2*d) for _ in range(d+1)]
    for j in range(d):
        differential1[j][j], differential1[j+1][j] = f1
        differential1[j][d+j], differential1[j+1][d+j] = f2
    differential2 = [[0]*(d-1) for _ in range(2*d)]
    for j in range(d-1):
        differential2[j][j], differential2[j+1][j] = -f2[0], -f2[1]
        differential2[d+j][j], differential2[d+j+1][j] = f1
    assert all(sum(differential1[i][k]*differential2[k][j] for k in range(2*d)) == 0
               for i in range(d+1) for j in range(d-1))
    return differential1, differential2


def koszul_checks():
    cases, enumerated, congruence_cases, positive_higher_homology = [], 0, 0, 0
    for p in (3, 5):
        pairs = [((1, 0), (0, 1)), ((1, 1), (0, 1)),
                 ((1, 0), (1, p)), ((1, p), (1, 2*p)),
                 ((p, 0), (0, 1)), ((p, 0), (0, p))]
        for pair_id, (y1, y2) in enumerate(pairs):
            base_length, base_unit = valuation(det([list(y1), list(y2)]), p)
            assert base_unit == 1
            for a, b, d in itertools.product(range(3), range(3), range(1, 4)):
                f1, f2 = [p**a*x for x in y1], [p**b*x for x in y2]
                differential1, differential2 = koszul_matrices(f1, f2, d)
                h0_order = minors_gcd(differential1, d+1)
                h0_length, h0_unit = valuation(h0_order, p)
                assert h0_unit == 1
                content = gcd(gcd(*f1), gcd(*f2))
                common_power, content_unit = valuation(content, p)
                assert content_unit == 1
                primitive = [[x//content for x in row] for row in differential2]
                assert all(x % content == 0 for row in differential2 for x in row)
                # Primitive columns have gcd of maximal minors one, so form
                # a saturated sublattice. They have the full rational kernel
                # rank d-1 of differential1, and are an integral kernel basis.
                assert minors_gcd(primitive, d-1) == 1
                h1_length = common_power*(d-1)
                euler = h0_length-h1_length
                assert euler == base_length+a+b
                assert euler >= 0
                positive_higher_homology += h1_length > 0

                modulus = p**(common_power+1)
                if modulus**(d-1) <= 20000:
                    kernel_order = 0
                    for vector in itertools.product(range(modulus), repeat=d-1):
                        enumerated += 1
                        if all(sum(row[j]*vector[j] for j in range(d-1)) % modulus == 0
                               for row in differential2):
                            kernel_order += 1
                    assert kernel_order == p**h1_length
                    congruence_cases += 1

                # Adjugate identities give det(f1,f2)*x and *y in (f1,f2).
                # Hence these examples satisfy the exact admissibility shape.
                determinant_value = f1[0]*f2[1]-f1[1]*f2[0]
                assert [f2[1]*f1[i]-f1[1]*f2[i] for i in range(2)] == [determinant_value, 0]
                assert [-f2[0]*f1[i]+f1[0]*f2[i] for i in range(2)] == [0, determinant_value]
                cases.append({"p": p, "base_pair": pair_id, "scalar_exponents": [a, b],
                              "degree": d, "H0_length": h0_length,
                              "H1_length": h1_length, "euler_characteristic": euler,
                              "unscaled_euler_characteristic": base_length,
                              "admissibility_power": max(1, base_length+a+b)})
    return {"koszul_complexes": len(cases),
            "cases_with_nonzero_H1": positive_higher_homology,
            "congruence_kernel_cases": congruence_cases,
            "congruence_vectors_examined": enumerated,
            "case_list_sha256": sha(json.dumps(cases, sort_keys=True).encode()),
            "sample_cases": [cases[i] for i in (0, 26, 53, 80, 134, 161, 242, 323)]}


def rank_mod_p(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    rank = 0
    for j in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(rank, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][j], -1, p)
        a[rank] = [(x*inverse) % p for x in a[rank]]
        for i in range(len(a)):
            if i != rank:
                factor = a[i][j]
                a[i] = [(x-factor*y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def zero_section_checks():
    cases = []
    for p in (3, 5):
        for d in range(1, 7):
            multiplication_x = [[int(i == j) for j in range(d)] for i in range(d+1)]
            rank = rank_mod_p(multiplication_x, p)
            assert rank == d
            # After the regular pi factor, C/pi C is F_p[x,y].
            zero_euler = (d+1)-d
            replacement_euler = (d+1-rank)-(d-rank)
            assert zero_euler == replacement_euler == 1
            cases.append({"p": p, "degree": d, "chi_zero_pi": zero_euler,
                          "chi_x_pi": replacement_euler})
        assert valuation(det([[1]]), p)[0] == 0
        assert valuation(det([[p]]), p)[0] == 1
    return cases


def main():
    sources = source_records()
    checks = koszul_checks()
    checks["zero_first_section_examples"] = zero_section_checks()
    artifacts = ["notes/rh-selmer-koszul-comparison.md",
                 "scripts/check_rh_selmer_koszul_comparison.py"]
    record = {
        "schema_version": 1,
        "claim": "Under the exact admissibility power containment, graded Koszul positivity, quotient comparisons and exact scalar extraction prove the actual mixed lower chain without global flatness or regular-sequence hypotheses.",
        "scope": [
            "Ordinary general proof in the note and shared TeX; no new Lean replay claimed.",
            "Induction is on section count, with finite graded prime filtration and finite common eventual bounds.",
            "A first section is changed only when the tail already has finite-length graded Koszul homology.",
            "Product additivity retains torsion kernels; scalar extraction uses regularity of pi only on the proved leading quotient.",
            "Exact integer Koszul matrices include nonzero higher homology and verify a primitive integral kernel basis by maximal minors.",
            "Actual admissibility from point classification, arithmetic model existence, eventual support and local generic multiplicity remain supplied inputs.",
            "No actual growing Selmer group or deformation model is computed; no existing proof-map node is completed.",
        ],
        "sources": sources,
        "exact_checks": checks,
        "primary_reference_scope_check": {
            "doi": "https://doi.org/10.2206/kyushujm.69.393",
            "pages": [394, 402],
            "checked_date": "2026-11-22",
            "finding": "Viet-Thanh Theorem 3.7 assumes an Artinian local base and does not directly supply the actual Noetherian-local-base comparison; it is not used in the proof.",
        },
        "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())} for p in artifacts],
        "independent_review_record": "certificates/hard-node-review-2026-11-22.json",
        "review_scope": "Automation-only verification here; mathematical review is recorded separately.",
    }
    out = ROOT / "certificates/rh-selmer-koszul-comparison.json"
    out.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "pass", "pinned_sources": len(sources),
                      "koszul_complexes": checks["koszul_complexes"],
                      "nonzero_H1_cases": checks["cases_with_nonzero_H1"],
                      "kernel_vectors": checks["congruence_vectors_examined"],
                      "output": str(out.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
