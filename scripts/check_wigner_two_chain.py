#!/usr/bin/env python3
"""Exact finite audit of WC2--WC9; this is not a representation-theory proof.

Enumerate strictly decreasing integral labels of width at most 9, with
last label zero, for U(k), 2 <= k <= 6. Check all interlacing branches,
all nonzero one-step bounds, and every adjacent two-chain comparison
allowed by the stated gap. Fractions retain exact equality and zero tests.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from math import prod
from pathlib import Path


def coefficient(labels, branch, index, raising):
    shift = 1 if raising else 0
    numerator = prod(abs(m - labels[index] - shift) for m in branch)
    denominator = prod(abs(x - labels[index]) for j, x in enumerate(labels)
                       if j != index)
    return Fraction(numerator, denominator)


def update(labels, index, delta):
    return tuple(x + (delta if j == index else 0)
                 for j, x in enumerate(labels))


def interlaces(labels, branch):
    return all(labels[j + 1] < m <= labels[j]
               for j, m in enumerate(branch))


def main():
    counts = dict(label_sets=0, branches=0, one_step_bounds=0,
                  chain_cases=0, raising_success=0, lowering_success=0,
                  one_chain_zero=0, zero_length=0)
    for rank in range(2, 7):
        for positive in itertools.combinations(range(1, 10), rank - 1):
            labels = tuple(reversed(positive)) + (0,)
            counts["label_sets"] += 1
            ranges = [range(labels[j + 1] + 1, labels[j] + 1)
                      for j in range(rank - 1)]
            for branch in itertools.product(*ranges):
                counts["branches"] += 1
                for index in range(rank):
                    diameter = max(1, labels[0] - labels[index], labels[index])
                    distances = [max(1, abs(x - labels[index])) for x in labels]
                    neighbor_product = prod(
                        distances[j + 1] if j < index else distances[j]
                        for j in range(rank - 1))
                    assert prod(distances[j] for j in range(rank)
                                if j != index) == (
                        distances[0] * distances[-1] * neighbor_product)
                    for raising in (False, True):
                        value = coefficient(labels, branch, index, raising)
                        if value:
                            assert value >= Fraction(1, diameter**2)
                            counts["one_step_bounds"] += 1
                for index in range(rank - 1):
                    max_length = (labels[index] - labels[index + 1] - 1) // 2
                    for length in range(max_length + 1):
                        b = max(Fraction(1), Fraction(length),
                                Fraction(labels[0], 2))
                        threshold = (3 * b) ** (-2 * length)
                        wp = prod(coefficient(update(labels, index + 1, t),
                                              branch, index + 1, True)
                                  for t in range(length))
                        wm = prod(coefficient(update(labels, index, -t),
                                              branch, index, False)
                                  for t in range(length))
                        assert max(wp, wm) >= threshold
                        counts["chain_cases"] += 1
                        counts["one_chain_zero"] += (wp == 0 or wm == 0)
                        counts["zero_length"] += (length == 0)
                        if branch[index] >= labels[index + 1] + length + 1:
                            assert all(interlaces(update(labels, index + 1, t), branch)
                                       for t in range(length + 1))
                            assert wp >= threshold
                            counts["raising_success"] += 1
                        else:
                            assert all(interlaces(update(labels, index, -t), branch)
                                       for t in range(length + 1))
                            assert wm >= threshold
                            counts["lowering_success"] += 1
    root = Path(__file__).resolve().parents[1]
    result = {
        "status": "passed",
        "scope": "Exact finite arithmetic audit of WC2--WC9, not a proof of the classical Clebsch--Gordan formulas or AP6.",
        "range": {"rank_min": 2, "rank_max": 6,
                  "label_width_max": 9, "last_label": 0,
                  "branches": "all integral interlacings",
                  "lengths": "all N >= 0 with 2*N+1 <= adjacent gap"},
        "counts": counts,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    target = root / "certificates" / "wigner-two-chain.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
