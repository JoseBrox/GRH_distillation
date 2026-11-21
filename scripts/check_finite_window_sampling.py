#!/usr/bin/env python3
"""Exact checks for the finite sampling reduction, not its arithmetic inputs.

The general theorem is proved in the note. Fractions check endpoint cells
without floating-point rounding; a symbolic derivative verifies the error
integral. The bounded analytic dependencies are pinned to reviewed bytes.
"""
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEPENDENCIES = [
    ("paper/sections/recovered/03-sec-one-sided.tex", 337, 381,
     "ce3e87093500a6e5235d7efd687f7f8832ec60c33d8b8bce154eb4dbfeca0fcf"),
    ("paper/rh/sections/01-introduction.tex", 31, 60,
     "96606f00a60113d4b636dc162c243ed3b1c21ab0d35f87b2b692e8e97c759c63"),
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def ceil(q):
    return -(-q.numerator // q.denominator)


def cells(n, ratio):
    """Factors whose logarithms are the unnormalized averaging weights."""
    assert n >= 1 and ratio > 1
    top = ratio*n
    return [(k, min(Fraction(k+1), top)/k)
            for k in range(n, ceil(top))]


def product(items):
    value = Fraction(1)
    for item in items:
        value *= item
    return value


def main():
    dependency_records = []
    for path, first, last, expected in DEPENDENCIES:
        data = (ROOT/path).read_bytes()
        excerpt = b"".join(data.splitlines(keepends=True)[first-1:last])
        assert last-first+1 <= 120 and digest(excerpt) == expected, path
        dependency_records.append({"path": path,
                                   "ranges": [{"start": first, "end": last,
                                               "sha256": expected}]})
    cases = 0
    ratios = [Fraction(10001, 10000), Fraction(101, 100), Fraction(3, 2),
              Fraction(2), Fraction(7, 3), Fraction(4), Fraction(13, 3)]
    for n in [*range(1, 37), 100, 1000]:
        for ratio in ratios:
            row = cells(n, ratio)
            assert row and row[0][0] == n and row[-1][0] == ceil(ratio*n)-1
            assert all(factor > 1 for _, factor in row)
            assert product(factor for _, factor in row) == ratio
            # Expanded finite-table containment, including integral endpoints.
            for end in [n, n+1, 2*n, Fraction(3*n, 2)]:
                if end >= n:
                    assert row[-1][0] <= ceil(ratio*end)
            cases += 1
    cancellation_cases = 0
    for n in [*range(1, 41), 100]:
        row = cells(n, Fraction(4))
        low = product(f for k, f in row if k < 2*n)
        high = product(f for k, f in row if k >= 2*n)
        assert low == high == 2
        # Thus (-log(low)+log(high))/log(4)=0,
        # whereas log(high)/log(4)=1/2 after taking positive parts first.
        cancellation_cases += 1
    u, theta, c = sp.symbols("u theta c", positive=True)
    primitive = -sp.exp(-theta*u)*((c+u)**2/theta
                                 +2*(c+u)/theta**2+2/theta**3)
    assert sp.simplify(sp.diff(primitive, u)
                       -sp.exp(-theta*u)*(c+u)**2) == 0
    assert sp.limit(primitive, u, sp.oo) == 0
    # The finite difference of a positive part is controlled by a
    # nonnegative interpolation error, regardless of a budget's sign.
    positive_part_cases = 0
    for a in [Fraction(i, 3) for i in range(-20, 21)]:
        for error in [Fraction(i, 5) for i in range(11)]:
            assert max(a+error, 0) <= max(a, 0)+error
            positive_part_cases += 1
    note = "notes/finite-window-sampling.md"
    script = "scripts/check_finite_window_sampling.py"
    result = {
        "schema_version": 1, "status": "PASS",
        "claim": "Exact finite endpoint, signed-weight and error-integral checks supplement the written finite-table criterion.",
        "note": note, "note_sha256": digest((ROOT/note).read_bytes()),
        "script": script, "script_sha256": digest((ROOT/script).read_bytes()),
        "proof_dependencies": dependency_records,
        "checks": {"rational_averaging_rows": cases,
                   "exact_signed_cancellation_cases": cancellation_cases,
                   "positive_part_interpolation_cases": positive_part_cases,
                   "symbolic_tail_integral": "PASS",
                   "integral_and_fractional_endpoints": "PASS"},
        "mathematical_review": "The general proof is written in the note; its independent review is recorded separately in certificates/finite-window-sampling-review.json.",
        "limits": "No new arithmetic construction, spectral or geometric estimate, zero computation or Lean verification. Integer comparisons are hypotheses; an almost-everywhere comparison is not assumed to include the integers.",
    }
    (ROOT/"certificates/finite-window-sampling.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": result["status"], **result["checks"]}))


if __name__ == "__main__":
    main()
