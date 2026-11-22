#!/usr/bin/env python3
"""Pinned contracts and exact checks of the leading-piece mixed count.

The general proofs are in the note. Admissibility and Euler-characteristic
comparison are not verified by these finite computations.
"""

import gzip
import hashlib
import itertools
import json
from fractions import Fraction
from functools import lru_cache
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
SOURCES = [
    ("CommutativeAlgebra.OrbitVanishingLocal", [(86, 105)]),
    ("CommutativeAlgebra.GradedModulesLength.ToDegInjective", [(149, 154), (187, 218), (222, 248)]),
    ("CommutativeAlgebra.GradedModulesLength.LkHolds", [(8, 79)]),
    ("CommutativeAlgebra.GradedModulesLength.ReesGradedPieceSurjection", [(199, 270)]),
    ("CommutativeAlgebra.GradedModulesLength.FrobeniusInclusionXEqMulQ", [(198, 283)]),
    ("CommutativeAlgebra.GradedModulesLength.AdmissibleMonoIdeal", [(273, 322)]),
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
    for suffix, ranges in SOURCES:
        module = PREFIX + suffix
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


def compositions(count, degree):
    if degree < 0:
        return 0
    if count == 0:
        return int(degree == 0)
    return comb(degree+count-1, count-1)


@lru_cache(maxsize=None)
def weighted_count(ones, twos, degree):
    """Independent product-series dynamic programming."""
    if degree < 0:
        return 0
    coefficients = [1] + [0]*degree
    for weight in [1]*ones + [2]*twos:
        for n in range(weight, degree+1):
            coefficients[n] += coefficients[n-weight]
    closed = sum(compositions(twos, j)*compositions(ones, degree-2*j)
                 for j in range(degree//2+1))
    assert coefficients[degree] == closed
    return closed


def count(r, s, rp, sp, a, b):
    return weighted_count(r, s, a)*weighted_count(rp+1, sp+1, b)


def mixed_difference(r, s, rp, sp, a, b):
    m, n = r-1+s, rp+sp
    return sum((-1)**(i+j)*comb(m, i)*comb(n, j)
               * (count(r, s, rp, sp, a-2*i, b-2*j)
                  - count(r, s, rp, sp, a-2*i-4, b-2*j-2))
               for i in range(m+1) for j in range(n+1))


def split_series_coefficient(r, rp, a, b):
    first = (sum(comb(r-1, i) for i in range(min(r-1, a)+1))
             * sum(comb(rp, j) for j in range(min(rp, b)+1)))
    correction_x = sum(comb(r-1, i) for i in range(r) if 0 <= a-i <= 3)
    correction_y = sum(comb(rp, j)*((b-2-j)//2+1)
                       for j in range(rp+1) if b-2-j >= 0)
    return first + correction_x*correction_y


def count_checks():
    parameter_sets = coefficient_cases = tail_cases = degree_boxes = 0
    for r, s, rp, sp in itertools.product(range(1, 5), range(4), range(4), range(3)):
        parameter_sets += 1
        for a, b in itertools.product(range(r+6), range(rp+5)):
            assert mixed_difference(r, s, rp, sp, a, b) == split_series_coefficient(r, rp, a, b)
            coefficient_cases += 1
        for da, db in itertools.product((0, 1, 2, 7), repeat=2):
            a, b = r+3+da, rp+db
            assert mixed_difference(r, s, rp, sp, a, b) == 2**(r-1+rp)
            tail_cases += 1
        m, n = r-1+s, rp+sp
        for extra in itertools.product((0, 1), repeat=3):
            d = (m+extra[0], n+extra[1], 1+extra[2])
            a, b = 2*d[0]+4*d[2], 2*d[1]+2*d[2]
            assert a >= r+3 and b >= rp
            for i, j, k in itertools.product(range(m+1), range(n+1), (0, 1)):
                shifted = (d[0]-i, d[1]-j, d[2]-k)
                assert min(shifted) >= 0
                assert (2*shifted[0]+4*shifted[2], 2*shifted[1]+2*shifted[2]) == (a-2*i-4*k, b-2*j-2*k)
            assert mixed_difference(r, s, rp, sp, a, b) == 2**(r-1+rp)
            degree_boxes += 1
    return {"parameter_sets": parameter_sets,
            "full_series_coefficient_checks": coefficient_cases,
            "explicit_tail_checks": tail_cases,
            "multidegree_boxes_checked": degree_boxes,
            "weighted_counts_checked_by_two_methods": weighted_count.cache_info().currsize}


def block_checks():
    valid_monomials = examined = 0
    for ones in range(1, 4):
        for twos in range(3):
            for degree in (0, 2, 4, 6):
                count_found = 0
                for exponents in itertools.product(range(degree+1), repeat=ones+twos):
                    examined += 1
                    if sum(exponents[:ones])+2*sum(exponents[ones:]) != degree:
                        continue
                    one_factors = [i for i in range(ones) for _ in range(exponents[i])]
                    assert len(one_factors) % 2 == 0
                    blocks = [one_factors[i:i+2] for i in range(0, len(one_factors), 2)]
                    blocks += [[i] for i in range(ones, ones+twos) for _ in range(exponents[i])]
                    assert len(blocks) == degree//2
                    recovered = [0]*(ones+twos)
                    for block in blocks:
                        assert sum(1 if i < ones else 2 for i in block) == 2
                        for i in block:
                            recovered[i] += 1
                    assert tuple(recovered) == exponents
                    count_found += 1
                assert count_found == weighted_count(ones, twos, degree)
                valid_monomials += count_found
    return {"exponent_vectors_examined": examined,
            "even_weight_monomials_factored": valid_monomials}


def determinant(matrix):
    """Exact Gaussian elimination, for the leading-lattice examples."""
    a = [[Fraction(x) for x in row] for row in matrix]
    out = Fraction(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            out *= -1
        out *= a[j][j]
        for i in range(j+1, len(a)):
            ratio = a[i][j]/a[j][j]
            for k in range(j, len(a)):
                a[i][k] -= ratio*a[j][k]
    return out


def lattice_checks():
    cases = []
    for p, ones, twos in itertools.product((3, 5), range(1, 4), range(3)):
        quadratics = ones*(ones+1)//2
        rank = quadratics+twos
        matrix = [[0]*rank for _ in range(rank)]
        for i in range(quadratics):
            matrix[i][i] = p*p
            for j in range(twos):
                matrix[i][quadratics+j] = (i+2*j+1) % p
        for j in range(twos):
            matrix[quadratics+j][quadratics+j] = p**(j+1)
        determinant_value = determinant(matrix)
        assert determinant_value == p**(2*quadratics+twos*(twos+1)//2)
        cases.append({"p": p, "weight_one_variables": ones,
                      "weight_two_variables": twos, "lattice_rank": rank,
                      "lattice_index": int(determinant_value)})
    return cases


def main():
    sources = source_records()
    exact = count_checks()
    exact.update(block_checks())
    exact["leading_lattice_cases"] = lattice_checks()
    artifacts = ["notes/rh-selmer-mixed-count.md",
                 "scripts/check_rh_selmer_mixed_count.py"]
    record = {
        "schema_version": 1,
        "claim": "The actual leading quotient has finite free graded pieces of the stated monomial rank, and the three backward differences equal 2^(r-1+r') in an explicit multidegree box.",
        "scope": [
            "General ordinary-mathematics proofs are in the note and shared TeX; finite checks supplement them.",
            "The marked graded model, its rational chart and finite weight-two modules remain stated inputs.",
            "Only the leading quotient is proved free; no flatness of the original deformation or global equation quotient is asserted.",
            "Admissibility, Euler positivity, quotient comparison and scalar extraction remain separate lower-comparison suppliers.",
            "Pinned source bytes and bounded contracts verified; no Lean replay, actual Selmer computation or completed existing map node claimed.",
        ],
        "sources": sources,
        "exact_checks": exact,
        "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())} for p in artifacts],
        "independent_review_record": "certificates/hard-node-review-2026-11-22.json",
        "review_scope": "Automation-only verification here; mathematical review is recorded separately.",
    }
    out = ROOT / "certificates/rh-selmer-mixed-count.json"
    out.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "pass", "pinned_sources": len(sources),
                      "parameter_sets": exact["parameter_sets"],
                      "series_coefficients": exact["full_series_coefficient_checks"],
                      "tail_cases": exact["explicit_tail_checks"],
                      "degree_boxes": exact["multidegree_boxes_checked"],
                      "factored_monomials": exact["even_weight_monomials_factored"],
                      "leading_lattices": len(exact["leading_lattice_cases"]),
                      "output": str(out.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
