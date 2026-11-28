#!/usr/bin/env python3
"""Exact algebraic checks for the three-quotient frame-fibre proof.

The ordinary proof is notes/lsernau-corank-frame-fibres.md. This tests
the integral Eichler and skew-solution formulas independently as matrices,
and certifies all polynomial exponent absorptions. It is not a Lean replay.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REVISION = "72fead102f663d5c7a407964a13dc0cf9d977207"
SOURCES = {
    "New/Spanning/RemainingTerms/FramesOverLattice.lean":
        "246b97446e5851ef4567d15405a4e9887dd01b81",
    "New/Spanning/RemainingTerms/FrameParts.lean":
        "36ef00fb7a1f921cbb2755a7ca2523e79b62677c",
    "New/Spanning/RemainingTerms/FrameCount.lean":
        "1de9068f3517584b16a789ae1b3bee6bbf2d0721",
    "New/Spanning/Unfolding/ReducedPoints.lean":
        "6ea7eaab5c878b31821105929f8bca43231feb39",
    "New/Spanning/Unfolding/Terms.lean":
        "17362bff437d81052d1735245a8054a27509e041",
    "New/Spanning/RemainingTerms/Count.lean":
        "1978ffd7969b8df8a3aa9a6aca15a31e69b776a4",
}


def reduce_matrix(m: sp.Matrix) -> sp.Matrix:
    return m.applyfunc(sp.expand)


def source_checks() -> dict:
    checked = {}
    for relative, expected in SOURCES.items():
        data = (ROOT / "build/readable-source/grh/src" / relative).read_bytes()
        actual = hashlib.sha1(
            b"blob " + str(len(data)).encode() + b"\0" + data
        ).hexdigest()
        assert actual == expected, (relative, expected, actual)
        checked[relative] = actual
    return {"revision": REVISION, "git_blobs": checked}


def eichler_checks() -> dict:
    tau = (1 + sp.I * sp.sqrt(3)) / 2
    assert sp.expand(tau + sp.conjugate(tau)) == 1
    assert sp.expand(tau**2 - tau + 1) == 0  # tau is integral
    cases = 0
    for rho in (1, 2, 3):
        for k in (1, 2, 3):
            size = 2*rho + k + 1
            z = rho + k
            j = sp.zeros(size)
            for i in range(rho):
                j[i, rho + k + 1 + i] = 1
                j[rho + k + 1 + i, i] = 1
            for i in range(k):
                j[rho + i, rho + i] = 1
            j[z, z] = -5
            x = sp.eye(size)[:, :rho]
            f = x.row_join(sp.eye(size)[:, z])
            eta = sp.Matrix(k, rho, lambda a, b: (a + 1) - (b + 1)*sp.I)
            v = sp.zeros(size, rho)
            v[rho:rho + k, :] = eta
            q = sp.Matrix(size, rho + 1, lambda a, b: a + 2*b + sp.I*(a - b))
            for modulus in (1, 2, 3, 5):
                u = (sp.eye(size) + modulus*(x*v.conjugate().T*j - v*x.conjugate().T*j)
                     - modulus**2*tau*x*(v.conjugate().T*j*v)*x.conjugate().T*j)
                assert reduce_matrix(u.conjugate().T*j*u) == j
                assert reduce_matrix(u*f) == f
                assert sp.expand(u.det()) == 1
                p = q[rho + k + 1:, :]
                assert reduce_matrix((u*q)[rho:rho + k, :] -
                                     q[rho:rho + k, :] + modulus*eta*p) == sp.zeros(k, rho + 1)
                skew = sp.Matrix(rho, rho, lambda a, b: a - b + sp.I*(a + b + 1))
                assert skew.conjugate().T == -skew
                move = sp.eye(size) + modulus*x*skew*x.conjugate().T*j
                assert reduce_matrix(move.conjugate().T*j*move) == j
                assert move*f == f
                assert reduce_matrix((move*q)[:rho, :] - q[:rho, :] -
                                     modulus*skew*p) == sp.zeros(rho, rho + 1)
                cases += 1
    return {"rank_and_modulus_cases": cases,
            "field": "Q(i,sqrt(3)); tau=(1+i sqrt(3))/2 integral of trace one",
            "identities_per_case": 7}


def skew_solution_checks() -> dict:
    cases = 0
    for rho in range(1, 5):
        n = rho + 1
        for cell in range(n + 1):
            y = sp.eye(n)
            for a in range(cell):
                y[a, a] = a + 2 + sp.I
                for b in range(a + 1, n):
                    y[a, b] = a + b + 1 - sp.I
            p = sp.zeros(rho, n)
            if cell == n:
                p = y[:rho, :]
            else:
                p[:cell, :] = y[:cell, :]
            delta = sp.expand(y.det())
            alpha = y.adjugate()[:, :rho]
            s = sp.Matrix(rho, rho, lambda a, b: a - b + sp.I*(a + b + 1))
            mu = s*p
            assert reduce_matrix(mu.conjugate().T*p + p.conjugate().T*mu) == sp.zeros(n)
            assert reduce_matrix(mu*alpha*p - delta*mu) == sp.zeros(rho, n)
            b = (sp.conjugate(delta)*mu*alpha
                 - delta*(mu*alpha).conjugate().T
                 - alpha.conjugate().T*p.conjugate().T*mu*alpha)
            assert reduce_matrix(b.conjugate().T + b) == sp.zeros(rho)
            assert reduce_matrix(b*p - delta*sp.conjugate(delta)*mu) == sp.zeros(rho, n)
            if cell == n:
                last = y.adjugate()[:, n - 1]
                assert reduce_matrix(p*last) == sp.zeros(rho, 1)
                assert reduce_matrix(mu*last) == sp.zeros(rho, 1)
            cases += 1
    return {"cell_and_rank_cases": cases, "isotropic_ranks": [1, 2, 3, 4],
            "all_cells_included": True}


def exponent_checks() -> dict:
    t, ell = sp.symbols("t ell", nonnegative=True)
    n = t + 1
    rho = n - 1
    expressions = {
        "frame_condition_number":
            46*n**2 - (1 + (2 + 44*n)*rho + 7*n),
        "shared_vector_bound":
            182*n**2 - (46*n**2 + (2 + 134*n)*rho + 1 + 23*rho + 37*n),
        "three_quotient_bound":
            2000*n**6*(ell + 1)
            - (2 + 270*n**3 + 366*n**4 + 2*n**3*(rho + ell*n + n*rho)),
        "fibre_square_cost":
            128000*n**9 - 4000*n**6*(n**3 + 1),
    }
    result = {}
    for name, expr in expressions.items():
        polynomial = sp.Poly(sp.expand(expr), t, ell)
        assert all(c >= 0 for c in polynomial.coeffs())
        result[name] = [
            {"powers_t_ell": list(powers), "coefficient": int(coefficient)}
            for powers, coefficient in polynomial.terms()
        ]
    big_n = t + 100000
    for name, expr in {
        "first_modulus": 2*big_n**3 - (46 + 270*big_n**2),
        "second_modulus": 2*big_n**3 - (46 + 540*big_n**2),
    }.items():
        polynomial = sp.Poly(sp.expand(expr), t)
        assert all(c >= 0 for c in polynomial.coeffs())
        result[name] = [int(c) for c in reversed(polynomial.all_coeffs())]
    assert sp.Rational(4, 5) < 1
    return result


def main() -> None:
    notes = ["notes/lsernau-corank-frame-fibres.md",
             "notes/lsernau-link-lattice-counting.md",
             "notes/lsernau-quantitative-returns.md"]
    result = {
        "status": "all exact checks passed",
        "scope": "matrix identities and exponent certificates, not a Lean replay",
        "sources": source_checks(),
        "eichler": eichler_checks(),
        "skew_solution": skew_solution_checks(),
        "exponent_certificates": exponent_checks(),
        "note_sha256": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                        for p in notes},
    }
    target = ROOT / "certificates/corank-frame-fibres.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"],
                      "source_blobs": len(SOURCES),
                      "eichler_cases": result["eichler"]["rank_and_modulus_cases"],
                      "skew_solution_cases": result["skew_solution"]["cell_and_rank_cases"],
                      "polynomial_certificates": len(result["exponent_certificates"]),
                      "certificate": str(target.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    main()
