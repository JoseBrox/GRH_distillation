#!/usr/bin/env python3
"""Exact checks for link graphs, reciprocal indices, and gauge powers.

The universal ordinary proofs are in notes/lsernau-link-gain-index.md.
These finite examples are regression checks, not a proof of the open cut.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import deque
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form


ROOT = Path(__file__).resolve().parents[1]
REVISION = "72fead102f663d5c7a407964a13dc0cf9d977207"
SOURCES = {
    "New/Spanning/RemainingTerms/Gain.lean":
        "842a5840286b8d2cfe4b8b14a26f789c02381564",
    "New/Spanning/RemainingTerms/BorderedDeterminant.lean":
        "776e5fac77ad3e77b53aca05b63a86c7c55a9dc8",
    "New/Spanning/RemainingTerms/LinkLattice.lean":
        "052592b3aaf905d9f57a4d1961094472815438a0",
    "New/Spanning/RemainingTerms/Cut.lean":
        "15711c7929a5c71778eb45b7324584196d8f2300",
    "New/Spanning/RemainingTerms/Data.lean":
        "df72908b356a809a92d6aa16246964e7dfd8562d",
    "New/Spanning/Unfolding/Terms.lean":
        "17362bff437d81052d1735245a8054a27509e041",
    "New/Spanning/RemainingTerms/Sum.lean":
        "cc6bd2c9ce1805ac053b7e498465434273b6f1d5",
}


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


def simp(m: sp.Matrix) -> sp.Matrix:
    return m.applyfunc(sp.simplify)


def norm_sq(z: sp.Expr) -> sp.Expr:
    return sp.simplify(z * sp.conjugate(z))


def unitary_examples(d: int) -> list[sp.Matrix]:
    identity = sp.eye(d)
    phase = sp.diag(*[sp.I**a for a in range(d)])
    rotation = sp.eye(d)
    if d >= 2:
        rotation[0, 0] = sp.Rational(3, 5)
        rotation[d-1, d-1] = sp.Rational(3, 5)
        rotation[0, d-1] = -sp.Rational(4, 5)
        rotation[d-1, 0] = sp.Rational(4, 5)
    answer = [identity, -identity, phase, rotation, phase*rotation]
    for u in answer:
        assert simp(u.conjugate().T*u) == identity
    return answer


def graph_and_determinant_checks() -> dict:
    graph_cases = determinant_cases = congruence_cases = 0
    for d in range(1, 6):
        k = d-1
        examples = unitary_examples(d)
        for u, v in itertools.product(examples, repeat=2):
            i = (u-v).rank()
            equations = (u-v)[:, :k].col_join(u[d-1:d, :k])
            ell = equations.rank()
            assert ell <= i+1
            if i == 0:
                assert ell == (0 if u[d-1, :k] == sp.zeros(1, k) else 1)
            graph_cases += 1

        for i in range(d+1):
            a = sp.Matrix(d, i, lambda x, y: int(bool(x == y)) + int(bool(x > y)))
            b = sp.Matrix(d, i, lambda x, y: int(bool(x == y)) + sp.I*int(bool(x > y)))
            assert a.rank() == i and b.rank() == i
            gram_a = sp.simplify((a.conjugate().T*a).det())
            gram_b = sp.simplify((b.conjugate().T*b).det())
            for u in examples:
                cross = simp(a.conjugate().T*(sp.eye(d)-u)*b)
                actual = norm_sq(cross.det())
                bound = 4**i*gram_a*gram_b
                assert sp.simplify(bound-actual) >= 0
                determinant_cases += 1
                for modulus in (2, 3, 5):
                    aa = 5*modulus*sp.eye(d)[:, :i]
                    bb = sp.eye(d)[:, :i]
                    cross = simp(aa.conjugate().T*(sp.eye(d)-u)*bb)
                    integral = simp(cross/modulus)
                    assert all(
                        sp.re(x).is_integer and sp.im(x).is_integer for x in integral
                    )
                    if cross.det() != 0:
                        assert norm_sq(cross.det()) >= modulus**(2*i)
                        product = (aa.conjugate().T*aa).det() * (bb.conjugate().T*bb).det()
                        assert product >= sp.Rational(modulus, 2)**(2*i)
                        congruence_cases += 1
    return {
        "exact_unitary_graph_pairs": graph_cases,
        "exterior_determinant_examples": determinant_cases,
        "nondegenerate_integral_congruence_examples": congruence_cases,
        "field_for_integral_examples": "Q(i), f=1",
        "boundary_ranks": "i=0 and full rank included",
    }


def fractional_class(v: sp.Matrix) -> tuple:
    return tuple(x-sp.floor(x) for x in v)


def index_checks() -> dict:
    quotient_cases = subgroup_cases = representatives = 0
    for d in range(1, 5):
        for offset in (0, 1, 2):
            divisors = [2+(j+offset) % 3 for j in range(d)]
            denominator = sp.diag(*divisors)
            torsion_order = int(denominator.det())
            for m in range(1, d+1):
                p = sp.eye(d)[:m, :]
                for a in range(m):
                    for b in range(m, d):
                        p[a, b] = 1+(a+2*b+offset) % 5
                j_basis = hermite_normal_form(p*denominator)
                j_inverse = j_basis.inv()
                all_classes = {
                    fractional_class(j_inverse*p*sp.Matrix(coords))
                    for coords in itertools.product(*(range(a) for a in divisors))
                }
                representatives += torsion_order
                image_basis = hermite_normal_form(p)
                quotient_order = int(j_basis.det()/image_basis.det())
                assert len(all_classes) == quotient_order
                assert torsion_order % quotient_order == 0
                quotient_cases += 1
                for rank in range(d+1):
                    h = sp.Matrix(d, rank, lambda a, b: int(bool(a == b))+int(bool(a > b))*(offset+1))
                    c = p*h
                    generators = [
                        fractional_class(j_inverse*c[:, a]) for a in range(rank)
                    ]
                    zero = (sp.Integer(0),)*m
                    seen = {zero}
                    pending = deque([zero])
                    while pending:
                        x = pending.popleft()
                        for y in generators:
                            z = tuple(t-sp.floor(t) for t in map(sum, zip(x, y)))
                            if z not in seen:
                                seen.add(z)
                                pending.append(z)
                    sum_basis = hermite_normal_form(j_basis.row_join(c))
                    independent_order = int(j_basis.det()/sum_basis.det())
                    assert len(seen) == independent_order
                    assert seen <= all_classes
                    assert torsion_order % len(seen) == 0
                    subgroup_cases += 1
    reciprocal_cases = 0
    for rank in range(5):
        for offset in range(5):
            aa = [2+(j+offset) % 4 for j in range(rank)]
            bb = [2+(2*j+offset) % 5 for j in range(rank)]
            ll = [sp.ilcm(a, b) for a, b in zip(aa, bb)]
            d1 = sp.prod(aa)**2
            d2 = sp.prod(bb)**2
            common = sp.prod(ll)**2
            t1 = sp.prod(l//b for l, b in zip(ll, bb))**2
            t2 = sp.prod(l//a for l, a in zip(ll, aa))**2
            assert common**2 == t1*t2*d1*d2
            reciprocal_cases += 1
    return {
        "quotient_maps": quotient_cases,
        "subgroups_checked_by_enumeration_and_HNF": subgroup_cases,
        "finite_domain_representatives": representatives,
        "reciprocal_Gaussian_integer_index_examples": reciprocal_cases,
    }


def minor_checks() -> dict:
    cases = 0
    for j in range(5):
        a = sp.Matrix(j, j, lambda x, y: (x+1)*int(bool(x == y))+int(bool(x < y)))
        u = sp.Matrix(j, 1, lambda x, y: x+1+sp.I)
        v = sp.Matrix(1, j, lambda x, y: y+1-sp.I)
        for modulus in (5, 7, 11):
            for phase in (1, -1, sp.I, -sp.I):
                corner = (v*a.inv()*u)[0, 0]-modulus*phase
                z = a.row_join(u).col_join(v.row_join(sp.Matrix([[corner]])))
                assert sp.simplify(z.det()+modulus*phase*a.det()) == 0
                assert norm_sq(z.det()) == modulus**2*norm_sq(a.det())
                assert sp.simplify(z.inv()[j, j]+1/(modulus*phase)) == 0
                cases += 1
    return {"bordered_and_inverse_minor_examples": cases,
            "cell_zero_and_last_cell_conventions": "j=0 included"}


def exponent_checks() -> dict:
    t = sp.symbols("t", nonnegative=True)
    n = t+1000
    polynomial = sp.Poly(sp.expand(n**3-270*n**2-166*n-1), t)
    coefficients = [int(x) for x in reversed(polynomial.all_coeffs())]
    assert all(x >= 0 for x in coefficients)
    return {
        "gauge_bound_n_at_least": 1000,
        "coefficients_of_n3_minus_270n2_minus_166n_minus1_at_n_equals_t_plus1000":
            coefficients,
    }


def main() -> None:
    result = {
        "status": "all exact checks passed",
        "scope": "finite exact examples and exponent certificate; ordinary proofs in note",
        "open_obligation": "construction and exact bounds of the link-lattice cut (15)",
        "sources": source_checks(),
        "graphs_and_determinants": graph_and_determinant_checks(),
        "indices": index_checks(),
        "bordered_minors": minor_checks(),
        "gauge_exponents": exponent_checks(),
        "note_sha256": hashlib.sha256(
            (ROOT/"notes/lsernau-link-gain-index.md").read_bytes()
        ).hexdigest(),
    }
    target = ROOT/"certificates/link-gain-index.json"
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: value for key, value in result.items()
                      if key not in ("sources", "note_sha256")}, indent=2))


if __name__ == "__main__":
    main()
