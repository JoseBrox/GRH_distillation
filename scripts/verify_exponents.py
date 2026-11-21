#!/usr/bin/env python3
"""Reproduce the paper's finite exponent checks with exact rational arithmetic.

The universal minimization is proved algebraically in the paper. This script
checks the listed rational instances, the sextic substitutions, and the signs
needed in that proof. It contains no numerical approximation or arithmetic
claim about zeros of L-functions.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import sys


def rational(value: Fraction) -> str:
    """Return a canonical exact rational, with no decimal conversion."""
    return str(value)


def certificate() -> dict:
    optimizations = []
    for m in (2, 3, 4, 6, 12):
        increasing_slope = Fraction(m - 1, 2 * m)
        decreasing_slope = Fraction(-1, m)
        assert increasing_slope > 0 > decreasing_slope
        intersection = Fraction(1, 2) / (
            increasing_slope - decreasing_slope
        )
        expected_intersection = Fraction(m, m + 1)
        assert intersection == expected_intersection
        increasing_value = Fraction(1, 2) + increasing_slope * intersection
        decreasing_value = 1 + decreasing_slope * intersection
        assert increasing_value == decreasing_value == expected_intersection
        assert Fraction(1, 2) < increasing_value < 1
        restricted_value = Fraction(1, 2) + increasing_slope
        assert restricted_value == 1 - Fraction(1, 2 * m)
        assert restricted_value >= 1 + decreasing_slope
        optimizations.append(
            {
                "m": m,
                "increasing_slope": rational(increasing_slope),
                "decreasing_slope": rational(decreasing_slope),
                "optimal_alpha": rational(intersection),
                "optimal_exponent": rational(increasing_value),
                "minimum_for_alpha_at_least_one": rational(restricted_value),
            }
        )

    sextic = []
    for theta in (Fraction(0), Fraction(1, 100), Fraction(1, 20), Fraction(1, 10)):
        alpha = 1 + theta
        mean_square = 2 + theta
        prime_count = alpha / 6
        squared_main = mean_square - prime_count
        squared_error = 2 - 2 * prime_count
        assert squared_main == Fraction(11, 6) + Fraction(5, 6) * theta
        assert squared_error == Fraction(5, 3) - theta / 3
        assert squared_main > squared_error
        main = squared_main / 2
        error = squared_error / 2
        assert main == Fraction(11, 12) + Fraction(5, 12) * theta
        assert error == Fraction(5, 6) - theta / 6
        sextic.append(
            {
                "theta": rational(theta),
                "H_exponent": rational(alpha),
                "prime_count_exponent_without_logarithm": rational(prime_count),
                "squared_main_exponent_without_epsilon": rational(squared_main),
                "squared_error_exponent": rational(squared_error),
                "main_exponent_without_epsilon": rational(main),
                "error_exponent": rational(error),
                "main_term_dominates": True,
            }
        )

    return {
        "arithmetic": "Python fractions.Fraction; no floating-point arithmetic",
        "scope": (
            "Exact checks for the listed rational instances. The universal "
            "minimization is proved in the paper. Theta=0 is a limiting "
            "exponent calculation, not an asserted mean-square input."
        ),
        "optimizations": optimizations,
        "sextic_substitutions": sextic,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        type=Path,
        metavar="EXPECTED_JSON",
        help="compare the calculated certificate with a saved JSON file",
    )
    args = parser.parse_args()
    actual = certificate()
    if args.check is not None:
        try:
            expected = json.loads(args.check.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            print(f"Could not read the expected certificate: {exc}", file=sys.stderr)
            return 2
        if actual != expected:
            print("Exact exponent certificate does not match.", file=sys.stderr)
            return 1
        print("Exact exponent certificate verified.")
        return 0
    print(json.dumps(actual, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
