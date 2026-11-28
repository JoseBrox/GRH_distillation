#!/usr/bin/env python3
"""Exact checks for the finite Bessel good-type transfer.

Enumerates the two actual unipotent pattern groups over small prime fields.
Character sums are compared on every unipotent Jordan class, in Z[zeta_p].
This verifies equality of their induced characters in these finite cases,
without enumerating the ambient general linear group. Rational checks verify
the minimum probability weights. No analytic moment or Lean replay is tested.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import prod
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
REVISION = "72fead102f663d5c7a407964a13dc0cf9d977207"
SOURCES = {
    "Lib/DiscreteSeries/Bruhat/FloorGroups.lean": "a5e9f316d5195e2cf0448b371d8c596409f8ebd9",
    "Lib/DiscreteSeries/Bessel/SchurBound.lean": "bb0fd13cdf3afc0a9c4ca1e1e4691de760a8ad39",
    "New/Spanning/Unfolding/Setup.lean": "a54f7bb24f51e51913d3d164edf1ccd5656719a1",
    "New/Spanning/Unfolding/Moments.lean": "05ebe97ed1068478917a25ae4afd41be63b839a4",
    "New/Spanning/Unfolding/BesselLevelStructure.lean": "ab99374c5683ad7d416dd4baa6f52230f7047e18",
    "New/Spanning/SecondMoment/SpanningTheorem.lean": "4b47ff63873e2e0b0a349be79900a1e47e5b1933",
}


def rank(a, p):
    a = [list(row) for row in a]
    n = len(a)
    pivot = 0
    for j in range(n):
        row = next((i for i in range(pivot, n) if a[i][j] % p), None)
        if row is None:
            continue
        a[pivot], a[row] = a[row], a[pivot]
        inv = pow(a[pivot][j] % p, -1, p)
        a[pivot] = [(v * inv) % p for v in a[pivot]]
        for i in range(pivot + 1, n):
            c = a[i][j] % p
            if c:
                a[i] = [(v - c * w) % p for v, w in zip(a[i], a[pivot])]
        pivot += 1
    return pivot


def mul(a, b, p):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) % p
             for j in range(n)] for i in range(n)]


def jordan_type(nilpotent, p):
    n = len(nilpotent)
    powers = nilpotent
    nullities = [0]
    for _ in range(1, n + 1):
        nullities.append(n - rank(powers, p))
        if nullities[-1] == n:
            break
        powers = mul(powers, nilpotent, p)
    assert nullities[-1] == n
    columns = [nullities[i + 1] - nullities[i]
               for i in range(len(nullities) - 1)]
    return tuple(sum(c > j for c in columns) for j in range(columns[0]))


def class_character_sums(p, k, rho, balanced):
    m = 2 * rho + 1
    r = k + m
    composition = ([1] * rho + [k + 1] + [1] * rho
                   if balanced else [1] * (m - 1) + [k + 1])
    levels = [i for i, size in enumerate(composition) for _ in range(size)]
    positions = [(i, j) for i in range(r) for j in range(r)
                 if levels[i] < levels[j]]
    if balanced:
        # z is the first coordinate in the central block.
        chain = list(range(rho)) + [rho] + list(range(rho + k + 1, r))
    else:
        chain = list(range(m))
    edges = list(zip(chain, chain[1:]))
    assert len(positions) == rho * (2 * k + 2 * rho + 1)
    assert all(edge in positions for edge in edges)
    by_class = defaultdict(lambda: [0] * p)
    total = 0
    for values in product(range(p), repeat=len(positions)):
        a = [[0] * r for _ in range(r)]
        for (i, j), v in zip(positions, values):
            a[i][j] = v
        phase = sum(a[i][j] for i, j in edges) % p
        by_class[jordan_type(a, p)][phase] += 1
        total += 1
    assert total == p ** len(positions)
    # For prime p, Phi_p(X)=1+...+X^(p-1); coefficients below degree p-1.
    reduced = {str(part): [c - counts[-1] for c in counts[:-1]]
               for part, counts in sorted(by_class.items())}
    return total, reduced


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    maximum = n if maximum is None else min(n, maximum)
    for first in range(maximum, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def rational_checks():
    count = 0
    equality_count = 0
    for q in (2, 3, 5, 7, 11, 17):
        for r in range(2, 13):
            br = prod((1 - Fraction(1, q ** j) for j in range(1, r + 1)),
                      start=Fraction(1))
            for rho in range((r - 1) // 2 + 1):
                k = r - 2 * rho - 1
                bk = prod((1 - Fraction(1, q ** j) for j in range(1, k + 1)),
                          start=Fraction(1))
                order_u = q ** (rho * (2 * k + 2 * rho + 1))
                min_multiplicity = prod(q ** j - 1 for j in range(1, k + 1))
                assert order_u * min_multiplicity == q ** (r * (r - 1) // 2) * bk
                omega_b = bk / (q ** r * (1 - Fraction(1, q ** r)))
                omega_pl = br / (q ** r * (1 - Fraction(1, q ** r)) ** 2)
                assert omega_b >= omega_pl
                order_g = q ** (r * r) * br
                assert order_g.denominator == 1
                for degrees in partitions(r):
                    denominator = prod((1 - Fraction(1, q ** d) for d in degrees),
                                       start=Fraction(1))
                    green_degree = q ** (r * (r - 1) // 2) * br / denominator
                    # Some partitions do not occur as squarefree labels over small q.
                    # The rational inequality is valid for all degree partitions.
                    lower_weight = order_u * green_degree * min_multiplicity / order_g
                    assert denominator <= 1 - Fraction(1, q ** r)
                    assert lower_weight >= omega_b
                    if len(degrees) == 1:
                        assert lower_weight == omega_b
                        equality_count += 1
                    count += 1
    return count, equality_count


def source_checks():
    checked = []
    for name, expected in SOURCES.items():
        candidates = [ROOT / "build/readable-source/grh/src" / name,
                      ROOT / "build/source-cache/lsernau/grh-lean" / REVISION / "grh/src" / name]
        path = next((p for p in candidates if p.is_file()), None)
        if path is None:
            raise FileNotFoundError(name)
        data = path.read_bytes()
        actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert actual == expected, (name, actual, expected)
        checked.append({"path": "grh/src/" + name, "git_blob_sha1": actual,
                        "sha256": hashlib.sha256(data).hexdigest()})
    pdf = ROOT / "build/references/andrews-thiem-gggr.pdf"
    expected = "f9951669cb0b685d1428a9f78add23e2ac11b83903b887bbcb762b6a352ec30b"
    assert hashlib.sha256(pdf.read_bytes()).hexdigest() == expected
    return checked, expected


def main():
    cases = []
    total_matrices = 0
    # Includes trivial U, ordinary Whittaker, and genuinely different radicals.
    for p, k, rho in [(2, 2, 0), (2, 0, 1), (3, 0, 1), (2, 1, 1),
                      (3, 1, 1), (5, 1, 1), (2, 2, 1), (3, 2, 1),
                      (2, 3, 1), (2, 1, 2)]:
        total_left, left = class_character_sums(p, k, rho, True)
        total_right, right = class_character_sums(p, k, rho, False)
        assert total_left == total_right
        assert left == right, (p, k, rho, left, right)
        total_matrices += total_left + total_right
        cases.append({"prime": p, "k": k, "rho": rho, "r": k + 2 * rho + 1,
                      "each_subgroup_order": total_left,
                      "jordan_class_sums": left})
    rational, equalities = rational_checks()
    sources, reference_sha = source_checks()
    record = {
        "status": "passed", "source_revision": REVISION,
        "scope": "Exact finite character-class sums, rational weight inequalities, source bytes. No analytic moment, all-rank proof automation, or Lean replay.",
        "induction_comparisons": len(cases), "enumerated_subgroup_matrices": total_matrices,
        "rational_weight_checks": rational, "irreducible_weight_equalities": equalities,
        "induction_cases": cases, "sources": sources,
        "primary_reference": {"url": "https://arxiv.org/pdf/1505.00763v1",
                              "sha256": reference_sha},
        "proof_note_sha256": hashlib.sha256(
            (ROOT / "notes/lsernau-bessel-good-type-transfer.md").read_bytes()).hexdigest(),
    }
    out = ROOT / "certificates/bessel-good-type-transfer.json"
    out.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({k: record[k] for k in ["status", "induction_comparisons",
          "enumerated_subgroup_matrices", "rational_weight_checks",
          "irreducible_weight_equalities"]}))


if __name__ == "__main__":
    main()
