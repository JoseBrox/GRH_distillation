#!/usr/bin/env python3
"""Exact finite Laurent-action checks for the fused transfer congruence.

This is supplementary evidence, not a proof for arbitrary word length.
The terminal matrix entries act on C^2 and do not commute.  The transposed
full matrix is evaluated directly from L A T, independently of its W factor.
Only the Python standard library is required.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import json


def add(out, key, value):
    out[key] += value
    if not out[key]:
        del out[key]


def scalar_entry(kind, row, col, y, m, n):
    """Return coefficient, holomorphic shift, antiholomorphic shift."""
    if kind == "T":
        return {(0, 0): (y + m, 0, 0), (0, 1): (-1, 1, 0),
                (1, 0): (1, -1, 0)}.get((row, col), (0, 0, 0))
    if kind == "L":
        return {(0, 0): (y - n, 0, 0), (0, 1): (1, 0, -1),
                (1, 0): (-1, 0, 1)}.get((row, col), (0, 0, 0))
    if kind == "W":
        return scalar_entry("L", col, row, y, m, n)
    if kind == "Ws":
        return scalar_entry("T", col, row, y, m, n)
    raise ValueError(kind)


def terminal_entry(row, col, y):
    return {
        (0, 0): ((y + 1, 1), (0, y - 1)),
        (0, 1): ((0, 1), (2, 0)),
        (1, 0): ((1, 0), (0, -1)),
        (1, 1): ((2, y), (1, 3)),
    }[row, col]


def change(bits, i, a):
    return bits[:i] + (a,) + bits[i + 1:]


def transfer(vector, i, y, kind):
    out = defaultdict(F)
    for (m, n, bits, z), value in vector.items():
        for a in (0, 1):
            c, dm, dn = scalar_entry(kind, a, bits[i], y, m, n)
            if c:
                add(out, (m + dm, n + dn, change(bits, i, a), z), value * c)
    return dict(out)


def apply_a(vector, i, y, transpose=False):
    out = defaultdict(F)
    for (m, n, bits, z), value in vector.items():
        for a in (0, 1):
            row, col = (bits[i], a) if transpose else (a, bits[i])
            matrix = terminal_entry(row, col, y)
            for zz in (0, 1):
                c = matrix[zz][z]
                if c:
                    add(out, (m, n, change(bits, i, a), zz), value * c)
    return dict(out)


def apply_q(vector, i, y, transpose=False):
    """Compute each Q_ab = sum L_ak A_kl T_lb; transpose auxiliary indices."""
    out = defaultdict(F)
    for (m, n, bits, z), value in vector.items():
        for a in (0, 1):
            row, col = (bits[i], a) if transpose else (a, bits[i])
            for k, ell in product((0, 1), repeat=2):
                ct, dm, dn = scalar_entry("T", ell, col, y, m, n)
                if not ct:
                    continue
                matrix = terminal_entry(k, ell, y)
                cl, dm2, dn2 = scalar_entry("L", row, k, y, m + dm, n + dn)
                if not cl:
                    continue
                for zz in (0, 1):
                    c = matrix[zz][z]
                    if c:
                        add(out, (m + dm + dm2, n + dn + dn2,
                                  change(bits, i, a), zz), value * ct * c * cl)
    return dict(out)


def rational_factor(vector, i, j, delta, kind):
    """(delta I - permutation/contraction)/(delta - 1)."""
    out = defaultdict(F)
    for key, value in vector.items():
        m, n, bits, z = key
        add(out, key, value * F(delta, delta - 1))
        if kind == "P":
            new = change(change(bits, i, bits[j]), j, bits[i])
            add(out, (m, n, new, z), -value / (delta - 1))
        elif kind == "Q":
            if bits[i] == bits[j]:
                for a in (0, 1):
                    new = change(change(bits, i, a), j, a)
                    add(out, (m, n, new, z), -value / (delta - 1))
        else:
            raise ValueError(kind)
    return dict(out)


def residue(vector, signs, parameters, full, wrong_minus=False):
    for i in reversed(range(len(signs))):
        # Right product: old equal signs in increasing written order.
        for j in reversed(range(i)):
            if signs[j] == signs[i]:
                delta = parameters[i] - parameters[j]
                if signs[i] == "-" and not wrong_minus:
                    delta = -delta
                vector = rational_factor(vector, i, j, delta, "P")
        vector = (apply_q if full else apply_a)(
            vector, i, parameters[i], transpose=signs[i] == "-")
        # Left product: old opposite signs in decreasing written order.
        for j in range(i):
            if signs[j] != signs[i]:
                minus = parameters[i] if signs[i] == "-" else parameters[j]
                plus = parameters[j] if signs[j] == "+" else parameters[i]
                vector = rational_factor(vector, i, j, minus - plus, "Q")
    return vector


def conjugated(vector, signs, parameters, reverse=False, wrong_minus=False):
    order = list(range(len(signs)))
    if reverse:
        order.reverse()
    for i in order:
        vector = transfer(vector, i, parameters[i], "T" if signs[i] == "+" else "W")
    vector = residue(vector, signs, parameters, full=False, wrong_minus=wrong_minus)
    for i in reversed(order):
        vector = transfer(vector, i, parameters[i], "L" if signs[i] == "+" else "Ws")
    return vector


def main():
    parameters = (-3, 2, 7)
    powers = ((-2, -1), (0, 0), (1, 2), (3, -2))
    checked = 0
    by_length = {}
    for h in (1, 2, 3):
        subtotal = 0
        for signs in product(("+", "-"), repeat=h):
            for m, n in powers:
                for bits in product((0, 1), repeat=h):
                    for z in (0, 1):
                        vector = {(m, n, bits, z): F(1)}
                        left = residue(vector, signs, parameters[:h], full=True)
                        right = conjugated(vector, signs, parameters[:h])
                        assert left == right, (h, signs, m, n, bits, z)
                        checked += 1
                        subtotal += 1
        by_length[str(h)] = subtotal

    controls = {}
    for label, signs, reverse, wrong_minus in (
        ("reversed_transfer_order", ("+", "+"), True, False),
        ("wrong_minus_difference", ("-", "-"), False, True),
    ):
        failures = 0
        for bits in product((0, 1), repeat=2):
            vector = {(1, 2, bits, 0): F(1)}
            left = residue(vector, signs, parameters[:2], full=True)
            wrong = conjugated(vector, signs, parameters[:2], reverse, wrong_minus)
            failures += left != wrong
        assert failures
        controls[label] = {"detected_failures": failures, "cases": 4}
    import hashlib
    from pathlib import Path
    root = Path(__file__).resolve().parents[1]
    report = {
        "source_sha256": {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in [Path(__file__).resolve(), root / "paper/sections/new/jacquet-integrated-descent.tex"]},
        "method": "exact rational action on Laurent monomials with noncommuting terminal 2-by-2 coefficients",
        "claim": "supplementary finite cases; universal proof is in ji-fused-congruence",
        "parameters": parameters,
        "laurent_exponents": powers,
        "word_sign_patterns": "all patterns of lengths 1, 2, 3",
        "passed_basis_cases": checked,
        "by_length": by_length,
        "negative_controls": controls,
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
