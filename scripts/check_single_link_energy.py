#!/usr/bin/env python3
"""Source hashes and exact scale checks for the single-link frontier.

This does not certify the unsupplied orbit, link-lattice cut, or
zero-term classification theorems. The frame-fibre, lattice count,
and other pair-gain ingredients are proved in their own notes.
The infinite summation implication
is proved in the accompanying ordinary-mathematics note.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha1, sha256
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVISION = "72fead102f663d5c7a407964a13dc0cf9d977207"
SOURCES = {
    "New/Spanning/RemainingTerms/Size.lean":
        "a61c50a82101c059bea19d4bb3028de6feba3a93",
    "New/Spanning/RemainingTerms/Count.lean":
        "1978ffd7969b8df8a3aa9a6aca15a31e69b776a4",
    "New/Spanning/RemainingTerms/SchurOrbit.lean":
        "02c749d1e6fc4ee0fdb8132bc24ccdfb9f084201",
    "New/Spanning/RemainingTerms/Sum.lean":
        "cc6bd2c9ce1805ac053b7e498465434273b6f1d5",
    "New/Spanning/Unfolding/SquareExpansion.lean":
        "35ae555cd8125cc2e39b22d54e18e57051aaab20",
    "New/Spanning/Unfolding/Terms.lean":
        "17362bff437d81052d1735245a8054a27509e041",
    "New/Spanning/RemainingTerms/Gain.lean":
        "842a5840286b8d2cfe4b8b14a26f789c02381564",
}


def shifted_coefficients(coefficients: list[int], shift: int) -> list[int]:
    """Ascending coefficients of P(x+shift), using the binomial theorem."""
    out = [0] * len(coefficients)
    for degree, coefficient in enumerate(coefficients):
        for power in range(degree + 1):
            out[power] += coefficient * comb(degree, power) * shift**(degree-power)
    return out


def main() -> None:
    records = []
    for relative, expected in SOURCES.items():
        path = ROOT / "build/readable-source/grh/src" / relative
        data = path.read_bytes()
        actual = sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert actual == expected, (relative, actual, expected)
        records.append({"path": relative, "git_blob": actual})

    # Exponents are coefficients of t=kf in log_b units.
    assert Fraction(8, 4) + 1 - 6 == -3   # Same-link gain on either strip.
    assert Fraction(8, 4) + 1 - 6 == Fraction(-12, 4)  # Mixed-link budget.
    assert Fraction(-12, 4) <= Fraction(-10, 4)
    assert Fraction(1 - 10, 4) <= -1     # Sum over at most tau coranks.
    assert Fraction(-3, 2) * 40 <= -20
    assert Fraction(-1, 2) * 40 <= -20
    assert 9 <= 2**28                   # 9 b^-40 <= b^-12 for b>=2.
    assert 9 <= 2**11                   # 9 b^-20 +4 b^-9 <=5 b^-9.

    # Uniform tail comparison for all k>=100, r<=2k, f>=1.
    # 2k^3-22r^2-40 >= 2k^3-88k^2-40.
    shifted = shifted_coefficients([-40, 0, -88, 2], 100)
    assert shifted == [1119960, 42400, 512, 2]
    assert all(coefficient >= 0 for coefficient in shifted)

    # The square of the separately proved frame-fibre bound fits one
    # tau: ell<=n^3, n>=1, k>=1000(2n)^9.
    assert 2 * 2000 * 2 <= 1000 * 2**9 // 4

    note = ROOT / "notes/lsernau-single-link-energy-frontier.md"
    result = {
        "status": "passed",
        "scope": "Pinned source identity and universal exact exponent comparisons only",
        "revision": REVISION,
        "note_sha256": sha256(note.read_bytes()).hexdigest(),
        "sources": records,
        "tail_polynomial": {
            "expression": "2(x+100)^3 -88(x+100)^2 -40",
            "ascending_coefficients": shifted,
            "domain": "x>=0",
        },
        "conditional_results": [
            "both strips <=9 b^-40 |R| d_X",
            "source deficit <=5 b^-9 d_X",
        ],
        "not_certified": [
            "gauge-specific orbit size",
            "integral link-lattice cut inequality (15) in the gain note",
            "classification and cancellation of zero-discriminant terms",
            "Lean replay or actual Poincare restricted moments",
        ],
    }
    destination = ROOT / "certificates/single-link-energy-frontier.json"
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print("Passed: 7 pinned source blobs and exact universal exponent comparisons.")
    print(destination.relative_to(ROOT))


if __name__ == "__main__":
    main()
