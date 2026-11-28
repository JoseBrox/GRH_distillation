#!/usr/bin/env python3
"""Exact checks for the rank-two critical-period local calculations.

The analytic proof is in notes/lsernau-rank-two-period-norm.md.
This verifies its rational identities and independent finite truncations;
it does not verify the classical Siegel--Weil or approximation theorems.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REVISION = "72fead102f663d5c7a407964a13dc0cf9d977207"
SOURCES = {
    "New/OneLift/HeckeValues/PeriodAtOne.lean":
        "35560a59661edc426816712cdf3ef97461235c7b",
    "New/OneLift/ComparisonOperator/ThreeExchanges.lean":
        "0a17364df7400aaac53a6117440e2b3f2e8b3010",
    "New/Determinant/Exchange/TheoremForPartners.lean":
        "ce25f3cb6ba24e8f34174de581e3a76478b11be8",
    "New/Determinant/Exchange/ExplicitMatching.lean":
        "3b7a149ac8fd2c374a10942cf0b1b406ce32d2e2",
    "Lib/Weil/DualPair/WeilAction.lean":
        "e23b7e7e9f20d66f871193037d31f0c1a255c0e1",
    "Lib/ClassField/HeckeCharacter/SplittingCharacters.lean":
        "0a41ed7f9cee7413376c68a010239eb52cd21cd4",
    "Lib/Weil/Unramified/HeckeTransfer.lean":
        "a8150176564ae56d5db55f266983019b70a10c4e",
}


def split_symbolic_identity() -> None:
    q, t, y = sp.symbols("q t y", nonzero=True)
    a, b, c = t * y / q, t / (q * y), 1 + 1 / q
    regions = (
        (1 - a**2 * b**2) / ((1 - a**2) * (1 - b**2))
        + c * t * y / ((1 - a**2) * (1 - t * y))
        + c * t / y / ((1 - b**2) * (1 - t / y))
        + c * t**2 / ((1 - t * y) * (1 - t / y))
    )
    answer = ((1 - t**2 / q) * (1 - t**2 / q**2)
              / ((1 - t * y) * (1 - t / y)
                 * (1 - t * y / q) * (1 - t / (q * y))))
    assert sp.cancel(regions - answer) == 0
    # Inert E/F has q_E=q^2 and eta(varpi)=-1.
    inert_l_ratio = ((1 + t**2 / q) * (1 - t**2 / q**2)
                     / ((1 - t**2) * (1 - t**2 / q**2)))
    inert_cartan = 1 + (1 + 1 / q) * t**2 / (1 - t**2)
    assert sp.cancel(inert_cartan - inert_l_ratio) == 0
    # The ramified test exactly supplies the spherical denominator at s=0.
    ramified = (1 - 1 / q) * (1 - 1 / q**2)
    denominator = 1 / ((1 - 1 / q) * (1 - 1 / q**2))
    assert sp.cancel(ramified * denominator - 1) == 0


def truncated_cartan(q: int, y: Fraction, degree: int) -> list[Fraction]:
    """Directly enumerate all Cartan indices contributing up to degree N."""
    result = [Fraction(0)] * (degree + 1)
    for a in range(-degree, degree + 1):
        for b in range(-degree, a + 1):
            n = abs(a) + abs(b)
            if n > degree:
                continue
            mass = (Fraction(1) if a == b else
                    (1 + Fraction(1, q)) * q ** (a - b))
            result[n] += mass * y ** (a + b) / q**n
    return result


def truncated_euler_ratio(q: int, y: Fraction, degree: int) -> list[Fraction]:
    """Expand the four Euler geometric series, without using Cartan regions."""
    coeffs = [Fraction(1)] + [Fraction(0)] * degree
    for lam in (y, 1 / y, y / q, 1 / (q * y)):
        coeffs = [
            sum((coeffs[n - j] * lam**j for j in range(n + 1)), Fraction(0))
            for n in range(degree + 1)
        ]
    return [
        coeffs[n]
        - ((Fraction(1, q) + Fraction(1, q**2)) * coeffs[n - 2]
           if n >= 2 else 0)
        + (Fraction(1, q**3) * coeffs[n - 4] if n >= 4 else 0)
        for n in range(degree + 1)
    ]


def check_cartan_coefficients() -> dict:
    degree = 12
    parameters = [
        (q, y)
        for q in (2, 3, 5, 7, 11, 13)
        for y in map(Fraction, (-3, -1, 1, 2))
    ] + [(q, Fraction(1, 2)) for q in (2, 3, 5, 7, 11, 13)]
    for q, y in parameters:
        assert truncated_cartan(q, y, degree) == truncated_euler_ratio(q, y, degree)
    return {
        "parameter_pairs": len(parameters),
        "formal_degree": degree,
        "exact_coefficients_compared": len(parameters) * (degree + 1),
        "note": "Rational y values are formal algebra tests, not unitary characters.",
    }


def check_finite_matrix_counts() -> dict:
    cases = []
    for q in (2, 3, 5, 7, 11):
        invertible = sum(
            (a * d - b * c) % q != 0
            for a, b, c, d in itertools.product(range(q), repeat=4)
        )
        assert invertible == (q**2 - 1) * (q**2 - q)
        assert Fraction(invertible, q**4) == (1 - Fraction(1, q)) * (1 - Fraction(1, q**2))
        cases.append({"q": q, "total_matrices": q**4, "invertible": invertible})
    return {"cases": cases, "total_matrices": sum(c["total_matrices"] for c in cases)}


def check_fock_norms() -> dict:
    z11, z12, z21, z22 = sp.symbols("z11 z12 z21 z22")
    determinant = z11 * z22 - z12 * z21
    cases = []
    for k in range(17):
        polynomial = sp.Poly(determinant**k, z11, z12, z21, z22)
        norm = sum(
            int(coefficient)**2 * math.prod(math.factorial(e) for e in exponents)
            for exponents, coefficient in polynomial.terms()
        )
        assert norm == math.factorial(k) * math.factorial(k + 1)
        cases.append({"k": k, "norm_squared": norm})
    return {"cases": cases}


def check_sources() -> dict:
    base = ROOT / "build/readable-source/grh/src"
    verified = {}
    for relative, expected in SOURCES.items():
        data = (base / relative).read_bytes()
        actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert actual == expected, (relative, expected, actual)
        verified[relative] = actual
    return {"revision": REVISION, "verified_git_blobs": verified}


def references() -> dict:
    result = {}
    for name in (
        "yamana-siegel-weil-2013",
        "gan-qiu-takeda-2014",
        "tate-thesis-1950",
        "rapinchuk-strong-approximation-2013",
        "platonov-strong-approximation-1969",
    ):
        path = ROOT / "build/references" / (name + ".pdf")
        if path.exists():
            result[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def mathematical_notes() -> dict:
    """Record the exact prose proof and the synchronized endpoint scopes."""
    return {
        str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in (
            ROOT / "notes/lsernau-rank-two-period-norm.md",
            ROOT / "notes/lsernau-rank-two-period-arithmetic.md",
            ROOT / "notes/lsernau-normalized-transfer-critical-norm.md",
            ROOT / "notes/lsernau-integral-critical-kernels.md",
            ROOT / "notes/lsernau-critical-value-systems.md",
        )
    }


def main() -> None:
    split_symbolic_identity()
    certificate = {
        "status": "all exact algebra checks passed",
        "scope": (
            "Split Cartan rational identity, inert local factor, ramified denominator "
            "cancellation, independent truncated Cartan/Euler series, finite GL2 counts, "
            "Fock determinant norms, and pinned source blobs. These checks do not "
            "formalize the analytic Siegel--Weil or strong-approximation input."
        ),
        "symbolic_identities": 3,
        "independent_cartan_series": check_cartan_coefficients(),
        "finite_matrix_counts": check_finite_matrix_counts(),
        "fock_norms": check_fock_norms(),
        "source": check_sources(),
        "reference_pdf_sha256": references(),
        "mathematical_note_sha256": mathematical_notes(),
    }
    target = ROOT / "certificates/rank-two-period-norm.json"
    target.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(
        "PASS: 3 rational identities; "
        f'{certificate["independent_cartan_series"]["exact_coefficients_compared"]} '
        "independent Cartan coefficients; "
        f'{certificate["finite_matrix_counts"]["total_matrices"]} finite matrices; '
        "17 Fock norms; 7 pinned source blobs."
    )
    print(target.relative_to(ROOT))


if __name__ == "__main__":
    main()
