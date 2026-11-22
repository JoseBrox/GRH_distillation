#!/usr/bin/env python3
"""Authenticate and check the coarse harmonic discriminant denominator.

The general proof is in the shared TeX. Exact models below test trace
projectors, stable graph lattices, harmonic normal ordering and scaling.
They do not construct the original charts, prove normalized theta traces,
or compile the Lean project.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from math import comb, factorial, gcd, lcm
from pathlib import Path

import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth


STEM = "geometry-arithmetic-frontier-discriminant-clearing"
WV = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.TaylorDiscriminants.WickVanishing."
HF = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.PullbackSections.HolomorphicFamilies."
RI = "Development.AbelianVarietyTheory.Proofs.RingsOfIntegers."
DP = "Development.AbelianVarietyTheory.Proofs.DivisorProofs."
RANGES = {
    WV + "HStable": [(270, 302), (304, 334)],
    WV + "GaugeBilinearTermEqNegDoubleSum": [(157, 163), (223, 240)],
    HF + "BiextCoeffSecondLinear": [(154, 179), (181, 238)],
    WV + "SigCancel": [(121, 147), (149, 200)],
    WV + "ExpConjConnectionIntegral": [(40, 90)],
    WV + "LemmaH": [(34, 67)],
    WV + "LemmaHCols": [(223, 238)],
    WV + "HarmonicValueIntegral": [(89, 113), (123, 147)],
    HF + "ChartValJ": [(31, 55), (95, 158)],
    RI + "IntegralChartFormalBiextensionGaugeBound": [(50, 108)],
    RI + "HarmonicValueIntegralOfUnitDiscriminant": [(168, 203), (204, 234)],
    RI + "HarmonicValueBoundOfColumnProducts": [(18, 22)],
    HF + "ChartValueRamifiedOfLifts": [(110, 125)],
    DP + "IsIntegralFourierCoeffClassIndicatorLevelPoint": [(23, 30)],
}


class Quadratic:
    """Q[theta], theta^2-tr*theta+norm=0, exact integral-basis coordinates."""
    def __init__(self, tr, norm):
        self.tr, self.norm = F(tr), F(norm)
        self.zero, self.one, self.theta = self.q(0), self.q(1), (F(0), F(1))

    def q(self, x):
        return x if isinstance(x, tuple) else (F(x), F(0))

    def add(self, x, y):
        a, b = self.q(x); c, d = self.q(y)
        return a + c, b + d

    def neg(self, x):
        a, b = self.q(x)
        return -a, -b

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        a, b = self.q(x); c, d = self.q(y)
        return a*c - self.norm*b*d, a*d + b*c + self.tr*b*d

    def conjugate(self, x):
        a, b = self.q(x)
        return a + self.tr*b, -b

    def integral(self, x):
        return all(a.denominator == 1 for a in self.q(x))

    def matrix(self, rows):
        return [[self.q(x) for x in row] for row in rows]

    def matadd(self, A, B):
        return [[self.add(x, y) for x, y in zip(a, b)] for a, b in zip(A, B)]

    def scale(self, t, A):
        return [[self.mul(t, x) for x in a] for a in A]

    def matmul(self, A, B):
        return [[self.sum(self.mul(A[i][k], B[k][j]) for k in range(len(B)))
                 for j in range(len(B[0]))] for i in range(len(A))]

    def mv(self, A, v):
        return [self.sum(self.mul(x, y) for x, y in zip(a, v)) for a in A]

    def sum(self, xs):
        z = self.zero
        for x in xs:
            z = self.add(z, x)
        return z


def projector_graph_checks():
    fields = [-1, -2, -3, -5, -6, -7, -10, -11, -15, -19, -23, -31]
    graph_lifts = projector_identities = 0
    for t in fields:
        tr, norm = (1, (1-t)//4) if t % 4 == 1 else (0, -t)
        Q = Quadratic(tr, norm)
        Delta = abs(tr*tr - 4*norm)
        G = sp.Matrix([[2, tr], [tr, tr*tr-2*norm]])
        assert abs(int(G.det())) == Delta
        Gi = G.inv()
        dual = [(F(Gi[0, i]), F(Gi[1, i])) for i in range(2)]
        assert all(Q.integral(Q.mul(Delta, x)) for x in dual)
        I = Q.matrix([[1, 0], [0, 1]])
        Z = Q.matrix([[0, 0], [0, 0]])
        A = Q.matrix([[0, -norm], [1, tr]])
        Abart = list(map(list, zip(*Q.matadd(Q.scale(tr, I), Q.scale(-1, A)))))
        e = [Q.matadd(Q.scale(dual[0], I), Q.scale(dual[1], A)),
             Q.matadd(Q.scale(Q.conjugate(dual[0]), I), Q.scale(Q.conjugate(dual[1]), A))]
        assert Q.matadd(*e) == I
        assert Q.matmul(e[0], e[1]) == Z
        for j, eigenvalue in enumerate([Q.theta, Q.conjugate(Q.theta)]):
            assert Q.matmul(e[j], e[j]) == e[j]
            assert Q.matmul(A, e[j]) == Q.scale(eigenvalue, e[j])
            assert all(Q.integral(x) for row in Q.scale(Delta, e[j]) for x in row)
            projector_identities += 3
        # Stable graph with a genuinely nonintegral balanced part and an
        # integral, non-equivariant perturbation: S=H/Delta+C.
        H = Q.matrix([[2, tr], [tr, 2*norm]])
        C = Q.matrix([[1, 2], [0, 1]])
        S = Q.matadd(Q.scale(F(1, Delta), H), C)
        defect = Q.matadd(Q.matmul(S, A), Q.scale(-1, Q.matmul(Abart, S)))
        assert all(Q.integral(x) for row in defect for x in row)
        assert any(not Q.integral(x) for row in S for x in row)
        for j, theta in enumerate([Q.theta, Q.conjugate(Q.theta)]):
            u = [Q.sub(theta, tr), Q.one]
            assert Q.mv(A, u) == [Q.mul(theta, x) for x in u]
            v0 = [Q.neg(x) for x in Q.mv(S, u)]
            dj = dual if j == 0 else [Q.conjugate(x) for x in dual]
            es = Q.matadd(Q.scale(dj[0], I), Q.scale(dj[1], Abart))
            up = Q.mv(Q.scale(Delta, e[j]), u)
            vp = Q.mv(Q.scale(Delta, es), v0)
            assert up == [Q.mul(Delta, x) for x in u]
            phi = [Q.add(a, b) for a, b in zip(vp, Q.mv(S, up))]
            assert all(Q.integral(x) for x in up + phi)
            assert Q.mv(Abart, vp) == [Q.mul(theta, x) for x in vp]
            # Same CM type is not conjugate: the horizontal pairing vanishes.
            assert Q.sum(Q.mul(x, y) for x, y in zip(up, vp)) == Q.zero
            graph_lifts += 1
    return {"quadratic_fields": len(fields), "projector_identities": projector_identities,
            "integral_graph_eigenlifts": graph_lifts,
            "scope": "Exact integral-basis field arithmetic, including dyadic discriminants; these algebraic tests do not assert existence of a trace-one geometric datum in every field."}


def basis(a, b):
    return [(i, a-i, j, b-j) for i in range(a+1) for j in range(b+1)]


def harmonic_basis(a, b):
    mons = basis(a, b)
    target = basis(a-1, b-1) if min(a, b) else []
    row = {m: i for i, m in enumerate(target)}
    M = sp.zeros(len(target), len(mons))
    for j, m in enumerate(mons):
        for col in range(2):
            p, q = m[col], m[col+2]
            if p and q:
                dest = list(m); dest[col] -= 1; dest[col+2] -= 1
                M[row[tuple(dest)], j] += p*q
    out = []
    for v in M.nullspace():
        den = lcm(*(int(x.q) for x in v))
        z = [int(den*x) for x in v]
        common = gcd(*z)
        z = [x//common for x in z]
        assert M * sp.Matrix(z) == sp.zeros(len(target), 1)
        out.append([(m, c) for m, c in zip(mons, z) if c])
    assert len(out) == a+b+1
    return out


def derivative_value(p, q, col, scale=1):
    # f_b=1/(1-A_b*x-B_b*y), an integral formal power series.
    A, B = [(2, 3), (5, -1)][col]
    return factorial(p+q) * A**p * B**q * scale**(p+q)


def ordered_value(p, q, col, c, scale=1):
    # Exact normal-ordering coefficient: choose(p,r)*choose(q,r)*r!.
    return sum(F(comb(p, r)*comb(q, r)*factorial(r))*c**r*
               scale**(2*r)*derivative_value(p-r, q-r, col, scale)
               for r in range(min(p, q)+1))


def harmonic_word_checks():
    spaces = polynomials = identities = scaling = 0
    for a in range(5):
        for b in range(5):
            spaces += 1
            for P in harmonic_basis(a, b):
                polynomials += 1
                ordinary = sum(k*derivative_value(m[0], m[2], 0)*
                               derivative_value(m[1], m[3], 1) for m, k in P)
                for c in [F(-3), F(1, 2), F(1), F(2)]:
                    actual = sum(k*ordered_value(m[0], m[2], 0, c)*
                                 ordered_value(m[1], m[3], 1, c) for m, k in P)
                    assert actual == ordinary
                    identities += 1
                    for Delta in [3, 4, 8]:
                        value = sum(k*ordered_value(m[0], m[2], 0, c, Delta)*
                                    ordered_value(m[1], m[3], 1, c, Delta) for m, k in P)
                        assert value == Delta**(a+b)*ordinary
                        scaling += 1
    # For nonharmonic X_1 Y_1 and constant input, directly evaluate the
    # first-order words (d_x+d_z)(d_y+z/2)1 at the origin.
    x, y, z = sp.symbols("x y z")
    word = sp.diff(sp.Integer(1), y) + z/2
    word = sp.diff(word, x) + sp.diff(word, z)
    ordinary = sp.diff(sp.Integer(1), x, y)
    assert word.subs({x: 0, y: 0, z: 0}) == sp.Rational(1, 2)
    assert ordinary == 0
    # The trace-one obstruction holds symbolically for all integers a,b.
    a, b = sp.symbols("a b", integer=True)
    trace_gaussian = sp.expand((a+b*sp.I) + (a-b*sp.I))
    assert trace_gaussian == 2*a
    assert sp.Poly(trace_gaussian, a, b, modulus=2).is_zero
    assert not sp.Poly(1, a, b, modulus=2).is_zero
    # A split finite flat algebra already disproves arbitrary normalized
    # trace integrality; this is not a statement about the special theta sum.
    multiplication_matrix = sp.diag(1, 0)
    assert sp.trace(multiplication_matrix)/2 == sp.Rational(1, 2)
    # Ordinary monomial contractions never need divided integral words.
    integer_coefficients = 0
    for p in range(10):
        for q in range(10):
            for r in range(min(p, q)+1):
                c = F(factorial(p)*factorial(q),
                      factorial(p-r)*factorial(q-r)*factorial(r))
                assert c.denominator == 1
                assert c == comb(p, r)*comb(q, r)*factorial(r)
                integer_coefficients += 1
    return {"bidegree_spaces": spaces, "integral_harmonic_basis_polynomials": polynomials,
            "normal_ordering_identities": identities, "scaling_identities": scaling,
            "integer_contraction_coefficients": integer_coefficients,
            "contraction_parameters": ["-3", "1/2", "1", "2"],
            "negative_controls": ["Nonharmonic X_1 Y_1 retains contraction 1/2 on constant input.",
                                  "Z[i] has trace( a+b*i )=2a, so no integral trace-one element.",
                                  "The normalized trace of (1,0) in Z_2 x Z_2 is 1/2."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    projections = projector_graph_checks()
    words = harmonic_word_checks()
    reference_path = "build/reference-cache/stacks-0BVH.html"
    reference_hash = "630dbff7bdf6921bb43701a2d288b37192f171c0e2369a8ff94222aed130ef16"
    assert auth.sha((auth.ROOT / reference_path).read_bytes()) == reference_hash
    paths = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
             f"paper/shared/{STEM}-references.tex", "scripts/" + Path(__file__).name]
    record = {
        "date": "2026-11-22", "status": "PASS",
        "classification": "Written proof of a coarse local harmonic chart supplier under the original integral chart and trace-one hypotheses, with authenticated source identities and exact finite models.",
        "claim": "Delta^d H(P;f) is integral for integral pluriharmonic P of total degree d and the actual integral formal-biextension data.",
        "new_local_supplier_count": 1, "whole_nodes_newly_closed": 0,
        "retained_hypotheses": ["Actual integral formal group, biextension, rigidifications, symmetry and adjoint identifications.",
                                "Original integral trace-one element w+bar(w)=1.",
                                "Integral CM eigen-directions, polynomial coefficients and column sections.",
                                "Original pluriharmonicity and total degree."],
        "remaining_global_inputs": ["Normalized primary-torsion trace and index cancellation.",
                                    "Determinant-ideal scalar comparison and global model data.",
                                    "Actual theta spanning and independent raw theta norm."],
        "scope": "No Lean build and no global theta denominator closure. Finite checks supplement, not replace, the general proof and actual formal identities.",
        "projector_and_graph_checks": projections, "harmonic_word_checks": words,
        "sources": sources,
        "primary_reference": {"url": "https://stacks.math.columbia.edu/tag/0BVH",
                              "reference": "The Stacks Project, Discriminant of a finite locally free morphism, Section 49.3.",
                              "local_path": reference_path, "sha256": reference_hash,
                              "verified_scope": "Trace-pairing determinant is the discriminant; the adjugate proof is written in the shared theorem."},
        "artifacts": [{"path": p, "sha256": auth.sha((auth.ROOT / p).read_bytes())} for p in paths],
        "checker_dependency": {"path": "scripts/check_geometry_arithmetic_frontier_geometric_filtration.py",
                               "sha256": auth.sha((auth.ROOT / "scripts/check_geometry_arithmetic_frontier_geometric_filtration.py").read_bytes())},
        "reproduce": "python3 scripts/" + Path(__file__).name + " --offline",
    }
    out = auth.ROOT / "certificates" / (STEM + ".json")
    out.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "quadratic_fields": projections["quadratic_fields"],
                      "graph_lifts": projections["integral_graph_eigenlifts"],
                      "harmonic_polynomials": words["integral_harmonic_basis_polynomials"],
                      "normal_ordering_identities": words["normal_ordering_identities"],
                      "scaling_identities": words["scaling_identities"],
                      "negative_controls": len(words["negative_controls"])}))


if __name__ == "__main__":
    main()
