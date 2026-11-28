#!/usr/bin/env python3
"""Exact finite and algebraic checks for the weighted class-lattice mean.

The infinite theorem and its class-averaging argument are proved in
notes/lsernau-link-lattice-counting.md. These checks independently enumerate
row annihilators, test Gram complement/index identities, and certify the
polynomial inequalities used in the filling-scale specialization. They are
not a Lean replay or a substitute for Minkowski's second theorem.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REVISION = "72fead102f663d5c7a407964a13dc0cf9d977207"
SOURCES = {
    "New/Spanning/RemainingTerms/LatticesOfCorank.lean":
        "ccd6650e56236c42184589419c343aa1bfb63f10",
    "New/Spanning/RemainingTerms/SiegelLemma.lean":
        "ccde3d869e03bd2349c5c7455e76bad82ffae7a8",
    "New/Spanning/RemainingTerms/Discriminants.lean":
        "c7d319cc890a874a8a888d98f0fc776d37eaab37",
    "New/Spanning/RemainingTerms/Count.lean":
        "1978ffd7969b8df8a3aa9a6aca15a31e69b776a4",
    "New/Spanning/Unfolding/Setup.lean":
        "a54f7bb24f51e51913d3d164edf1ccd5656719a1",
    "New/Spanning/Unfolding/FillingAdmissible.lean":
        "ab290c97b8a4731459743f3bde8af505054f8f91",
    "New/Spanning/Bessel/FillingData.lean":
        "bcb9abdf604c8101c6d8c340476cc5b0473f9341",
}


def source_checks() -> dict:
    result = {}
    for relative, expected in SOURCES.items():
        data = (ROOT / "build/readable-source/grh/src" / relative).read_bytes()
        actual = hashlib.sha1(
            b"blob " + str(len(data)).encode() + b"\0" + data
        ).hexdigest()
        assert actual == expected, (relative, expected, actual)
        result[relative] = actual
    return {"revision": REVISION, "verified_git_blobs": result}


def annihilator_checks() -> dict:
    cases = 0
    rows_tested = 0
    for q in (2, 3, 5):
        for k in range(1, 5):
            # A nonsingular integral change of ambient coordinates.
            u = sp.eye(k)
            for a in range(k - 1):
                u.row_op(a + 1, lambda v, j, a=a: v + (a + 1) * u[a, j])
            if k > 1:
                u.row_op(0, lambda v, j: v + u[k - 1, j])
            assert abs(int(u.det())) == 1
            rows = tuple(itertools.product(range(q), repeat=k))[1:]
            for r in range(k + 1):
                for exponents in itertools.product(range(3), repeat=r):
                    columns = [
                        tuple(int(u[a, j]) * q**exponents[j] for a in range(k))
                        for j in range(r)
                    ]
                    count = sum(
                        all(sum(row[a] * col[a] for a in range(k)) % q == 0
                            for col in columns)
                        for row in rows
                    )
                    t = sum(e > 0 for e in exponents)
                    exact = q**(k - r + t) - 1
                    index = q**sum(exponents)
                    assert count == exact
                    assert count <= index * q**(k - r)
                    cases += 1
                    rows_tested += len(rows)
    return {"smith_types": cases, "nonzero_rows_enumerated": rows_tested,
            "fields": [2, 3, 5], "ambient_ranks": [1, 2, 3, 4],
            "smith_exponents": [0, 1, 2]}


def gram_checks() -> dict:
    complements = 0
    indices = 0
    for k in range(1, 6):
        for seed in range(1, 5):
            u = sp.eye(k)
            for a in range(k - 1):
                coeff = seed + (a + 1) * sp.I
                u.row_op(a + 1, lambda v, j, a=a, coeff=coeff:
                         v + coeff * u[a, j])
            if k > 1:
                u.row_op(0, lambda v, j: v + (1 - sp.I) * u[k - 1, j])
            assert sp.expand(u.det()) == 1
            dual = u.conjugate().T.inv()
            for r in range(k + 1):
                first = u[:, :r]
                last = dual[:, r:]
                d1 = sp.expand((first.conjugate().T * first).det())
                d2 = sp.expand((last.conjugate().T * last).det())
                assert d1 == d2 and d1 >= 1
                assert (first.conjugate().T * last).applyfunc(sp.expand) == sp.zeros(r, k - r)
                complements += 1
            # Over Z[i], additive index is Norm(det A), whereas a Gram
            # determinant scales by exactly this index, not its square.
            a = sp.diag(*[j + 2 + sp.I for j in range(k)])
            for j in range(k - 1):
                a[j, j + 1] = seed - sp.I
            ua = u * a
            index = sp.expand(a.det() * sp.conjugate(a.det()))
            d_base = sp.expand((u.conjugate().T * u).det())
            d_sub = sp.expand((ua.conjugate().T * ua).det())
            assert d_sub == index * d_base
            indices += 1
    return {"hermitian_complement_identities": complements,
            "gaussian_integer_index_identities": indices,
            "ranks": [1, 2, 3, 4, 5]}


def local_zeta_checks() -> dict:
    # Coefficients count triangular normal forms; compare independently with
    # the recurrence for the product of geometric local Euler factors.
    cases = 0
    coefficients = 0
    degree = 8
    for q in (2, 3, 5, 7):
        for r in range(5):
            direct = [0] * (degree + 1)
            for exponents in itertools.product(range(degree + 1), repeat=r):
                n = sum(exponents)
                if n <= degree:
                    direct[n] += q**sum(j * e for j, e in enumerate(exponents))
            euler = [1] + [0] * degree
            for j in range(r):
                euler = [
                    sum(euler[n - a] * q**(j * a) for a in range(n + 1))
                    for n in range(degree + 1)
                ]
            assert direct == euler
            cases += 1
            coefficients += degree + 1
    return {"local_series": cases, "formal_degree": degree,
            "exact_coefficients_compared": coefficients}


def exponent_checks() -> dict:
    t = sp.symbols("t", nonnegative=True)
    n = t + 1
    inequalities = {
        "first_factor_to_7n4":
            7*n**4 - (2 + n**3*(2*n + 3)),
        "7n4_to_k_over_4":
            128000*n**9 - 7*n**4,
        "k_lower_implies_2000n":
            512000*n**9 - 2000*n,
        "frame_fibre_square_to_tau":
            128000*n**9 - 4000*n**6*(n**3 + 1),
    }
    certificates = {}
    for name, difference in inequalities.items():
        polynomial = sp.Poly(sp.expand(difference), t)
        coefficients = list(reversed(polynomial.all_coeffs()))
        assert all(c >= 0 for c in coefficients)
        certificates[name] = [int(c) for c in coefficients]
    assert Fraction(32, 1000) <= Fraction(1, 4)
    assert Fraction(60, 2000) + Fraction(2, 1000) == Fraction(32, 1000)

    # Exact rational checks of the weight trade, including negative
    # mu+1-corank and both zero- and full-rank boundary cases.
    trade_cases = 0
    for k in range(1, 8):
        for ell in range(k + 1):
            r = k - ell
            for mu in (2, 3, 7):
                for d in (Fraction(1), Fraction(3, 2), Fraction(5)):
                    for index in (1, 2, 3, 8):
                        h = d * index
                        left = index * h**(-k)
                        right = h**(mu + 1) * d**(-k - 1) * Fraction(index)**(-r - mu)
                        assert left <= right
                        trade_cases += 1
    return {"nonnegative_coefficients_after_n_equals_t_plus_one": certificates,
            "weight_trade_exact_cases": trade_cases,
            "second_factor_fraction": "32/1000 <= 1/4"}


def main() -> None:
    note = ROOT / "notes/lsernau-link-lattice-counting.md"
    result = {
        "status": "all exact checks passed",
        "scope": "finite/algebraic certificate; ordinary infinite proof is in the note",
        "sources": source_checks(),
        "annihilator_rows": annihilator_checks(),
        "hermitian_discriminants": gram_checks(),
        "local_submodule_zeta": local_zeta_checks(),
        "filling_exponents": exponent_checks(),
        "note_sha256": hashlib.sha256(note.read_bytes()).hexdigest(),
    }
    target = ROOT / "certificates/link-lattice-counting.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "status": result["status"],
        "sources": len(SOURCES),
        "smith_types": result["annihilator_rows"]["smith_types"],
        "rows_enumerated": result["annihilator_rows"]["nonzero_rows_enumerated"],
        "gram_checks": result["hermitian_discriminants"],
        "local_series_coefficients":
            result["local_submodule_zeta"]["exact_coefficients_compared"],
        "weight_trade_cases":
            result["filling_exponents"]["weight_trade_exact_cases"],
        "certificate": str(target.relative_to(ROOT)),
    }, indent=2))


if __name__ == "__main__":
    main()
