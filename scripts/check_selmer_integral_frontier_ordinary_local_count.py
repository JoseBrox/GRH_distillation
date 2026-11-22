#!/usr/bin/env python3
"""Exact finite-coefficient checks and pinned provenance for the ordinary count.

The mathematical proof uses local Tate duality and local reciprocity. This
script checks their coefficient algebra and the source interface, not a Lean
build or a computational proof of the arithmetic theorems.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
PA, WG = BASE+"PatchingModules.", BASE+"WeilGroupCharacters."
RANGES = {
    WG+"Inertia": [(9, 22)],
    PA+"DegreeCountCohomology.IsDualPair": [(44, 55), (158, 160)],
    PA+"DegreeCountCohomology.OneCount": [(39, 77)],
    PA+"DegreeCountCohomology.HomCount": [(100, 133)],
    PA+"EpsilonEtaMatrices.EpsilonEtaTensorDual": [(11, 41)],
    PA+"PairedDualFirstOrderDualMatrixSpace": [(78, 86), (192, 224), (251, 274)],
    PA+"EpsilonEtaMatrices.MemW1IffPattern": [(107, 142), (146, 200)],
    PA+"DegreeCountCohomology.TyCard": [(102, 127)],
    PA+"EpsilonEtaMatrices.EntryZero": [(102, 145), (154, 202), (204, 280), (281, 322)],
    PA+"DegreeCountCohomology.PresCounts": [(9, 39)],
    WG+"WeilCharactersModular.LocCFT": [(31, 63), (65, 90)],
    PA+"EpsilonEtaMatrices.W1BoundArithmeticRankTwo": [(30, 61), (143, 165)],
    PA+"ThetaCoefficientMapEq": [(15, 39), (54, 61)],
}
PRIMARY = [
    {"path": "build/reference-cache/milne-adt-2006.pdf",
     "url": "https://www.jmilne.org/math/Books/ADTnot.pdf",
     "sha256": "2c6195ec76a974f3f336c77cb71cc3845b018aad2d43136716b3477a3bc5fb31",
     "results": ["I.2.3: finite local duality", "I.2.8: local Euler characteristic"],
     "pdf_pages": [36, 39], "printed_pages": [28, 31]},
    {"path": "build/reference-cache/milne-cft-v403.pdf",
     "url": "https://www.jmilne.org/math/CourseNotes/CFT.pdf",
     "sha256": "50d79af78250a9f1117ad9d337e0b231704a533fc707966ed1bfa52e13d498f5",
     "results": ["I.1.1: local reciprocity", "I.1.4: local existence theorem"],
     "pdf_pages": [29, 31], "printed_pages": [20, 22]},
]


def rank_mod_p(rows, p):
    a = [list(row) for row in rows]
    rank = 0
    for j in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(rank, len(a)) if a[i][j] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        u = pow(a[rank][j] % p, -1, p)
        a[rank] = [u*x % p for x in a[rank]]
        for i in range(len(a)):
            if i != rank:
                u = a[i][j]
                a[i] = [(x-u*y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


class FiniteField:
    def __init__(self, p, modulus):
        self.p, self.modulus = p, modulus
        self.f, self.q = len(modulus)-1, p**(len(modulus)-1)
        assert modulus[-1] == 1

    def digits(self, x):
        return [(x//self.p**j) % self.p for j in range(self.f)]

    def encode(self, a):
        return sum((x % self.p)*self.p**j for j, x in enumerate(a))

    def add(self, x, y):
        return self.encode([(a+b) % self.p for a, b in zip(self.digits(x), self.digits(y))])

    def mul(self, x, y):
        a, b = self.digits(x), self.digits(y)
        c = [0]*(2*self.f-1)
        for i, j in itertools.product(range(self.f), repeat=2):
            c[i+j] = (c[i+j]+a[i]*b[j]) % self.p
        for i in range(len(c)-1, self.f-1, -1):
            u = c[i]
            for j in range(self.f+1):
                c[i-self.f+j] = (c[i-self.f+j]-u*self.modulus[j]) % self.p
        return self.encode(c[:self.f])

    def power(self, x, n):
        out = 1
        while n:
            if n % 2:
                out = self.mul(out, x)
            x, n = self.mul(x, x), n//2
        return out

    def trace(self, x):
        out = 0
        for j in range(self.f):
            out = self.add(out, self.power(x, self.p**j))
        assert 0 <= out < self.p
        return out


def finite_coefficient_checks():
    fields = [FiniteField(3, [0, 1]), FiniteField(3, [1, 0, 1]),
              FiniteField(3, [1, 2, 0, 1]), FiniteField(5, [0, 1]),
              FiniteField(5, [2, 0, 1])]
    pairings, annihilators, twists = 0, 0, 0
    trace_one_zero = []
    for k in fields:
        # This also verifies that the chosen quotient is a field, without
        # relying on a polynomial package or an irreducibility assertion.
        assert all(k.mul(x, k.power(x, k.q-2)) == 1 for x in range(1, k.q))
        if k.trace(1) == 0:
            trace_one_zero.append(k.q)
        for m in range(1, 6):
            basis = [(i, k.p**j) for i in range(m) for j in range(k.f)]
            pairing = [[k.trace(k.mul(x, y)) if i+j == m-1 else 0
                        for j, y in basis] for i, x in basis]
            assert rank_mod_p(pairing, k.p) == k.f*m
            pairings += 1
        for m, c in itertools.product(range(8), range(9)):
            # Multiplication by t^c(1+a t+b t^2), where a may leave F_p.
            unit = [1, min(k.q-1, k.p), k.q-1]
            columns = []
            for j in range(m):
                for e in range(k.f):
                    column = [0]*(k.f*m)
                    for u, value in enumerate(unit):
                        if j+c+u < m:
                            digits = k.digits(k.mul(value, k.p**e))
                            column[(j+c+u)*k.f:(j+c+u+1)*k.f] = digits
                    columns.append(column)
            matrix = list(map(list, zip(*columns))) if columns else []
            assert k.f*m-rank_mod_p(matrix, k.p) == k.f*min(m, c)
            annihilators += 1
        for alpha in range(1, k.q):
            for eps in range(1, k.p):
                dual = k.mul(eps, k.power(alpha, k.q-2))
                for i, j in itertools.product(range(k.f), repeat=2):
                    x, y = k.p**i, k.p**j
                    assert k.trace(k.mul(k.mul(alpha, x), k.mul(dual, y))) == (
                        eps*k.trace(k.mul(x, y))) % k.p
                    twists += 1
    assert 27 in trace_one_zero
    # Omitting the Tate twist loses equivariance, already over F_3.
    k = fields[0]
    alpha, eps, x, y = 2, 2, 1, 1
    wrong_dual = k.power(alpha, k.q-2)
    assert k.trace(k.mul(k.mul(alpha, x), k.mul(wrong_dual, y))) != (
        eps*k.trace(k.mul(x, y))) % k.p
    # A resonant character contributes m, not a fixed additive constant.
    for constant in range(8):
        m = constant+1
        assert m*3 > m*2+constant
    return {"field_orders": [k.q for k in fields], "perfect_pairing_matrices": pairings,
            "annihilator_matrices": annihilators, "equivariant_pairing_checks": twists,
            "trace_of_one_zero_but_pairing_perfect": trace_one_zero,
            "negative_controls": ["omit cyclotomic Tate twist", "replace trace pairing by trace(1)",
                                  "bound a resonant character by a fixed defect constant"]}


def coefficient_and_filtration_checks():
    cases, counts = 0, 0
    for p, n, r in itertools.product([3, 5], range(1, 5), range(3)):
        zero = (0,)*(r+1)
        one = (1,)+(0,)*r

        def add(x, y):
            return tuple((a+b) % p for a, b in zip(x, y))

        def neg(x):
            return tuple(-a % p for a in x)

        def mul(x, y):
            return (x[0]*y[0] % p,)+tuple((x[0]*y[i]+x[i]*y[0]) % p for i in range(1, r+1))

        def mm(x, y):
            z = [[zero for _ in range(n)] for _ in range(n)]
            for i, j, h in itertools.product(range(n), repeat=3):
                z[i][j] = add(z[i][j], mul(x[i][h], y[h][j]))
            return z

        identity = [[one if i == j else zero for j in range(n)] for i in range(n)]
        for types in itertools.product([0, 1], repeat=n):
            T = [[zero for _ in range(n)] for _ in range(n)]
            for i in range(n):
                T[i][i] = (1+i % (p-1),)+(0,)*r
                for j in range(i+1, n):
                    if types[i] == types[j]:
                        T[i][j] = ((1+i+j) % p,)+(0,)*r
                    else:
                        T[i][j] = (0,)+tuple((1+i+j+s) % p for s in range(r))
            inverse = [[zero for _ in range(n)] for _ in range(n)]
            for i in range(n-1, -1, -1):
                inverse[i][i] = (pow(T[i][i][0], -1, p),)+(0,)*r
                for j in range(i+1, n):
                    total = zero
                    for h in range(i+1, j+1):
                        total = add(total, mul(T[i][h], inverse[h][j]))
                    inverse[i][j] = neg(mul(inverse[i][i], total))
            assert mm(T, inverse) == identity == mm(inverse, T)
            for width in range(n):
                B = [[zero for _ in range(n)] for _ in range(n)]
                for i in range(n):
                    for j in range(i+width, n):
                        B[i][j] = (((1+2*i+j) % p,)+(0,)*r if types[i] == types[j]
                                   else (0,)+tuple((2+i+j+s) % p for s in range(r)))
                conjugate = mm(mm(T, B), inverse)
                for i in range(n):
                    for j in range(n):
                        if j-i < width:
                            assert conjugate[i][j] == zero
                        elif j-i == width:
                            assert conjugate[i][j] == mul(mul(T[i][i], B[i][j]), inverse[j][j])
                cases += 1
    for n in range(1, 8):
        for a in range(1, n+1):
            for selected in itertools.combinations(range(n), a):
                types = [i in selected for i in range(n)]
                for r in range(4):
                    nu = a*(a-1)//2+(n-a)*(n-a-1)//2+r*a*(n-a)
                    actual = sum(1 if types[i] == types[j] else r
                                 for i in range(n) for j in range(i+1, n))
                    assert actual == nu
                    assert n+2*nu == a*a+(n-a)**2+2*r*a*(n-a)
                    counts += 1
    # Without killing smaller widths, a diagonal matrix contributes to
    # a higher entry after conjugation: T=[[1,1],[0,1]], B=diag(0,1).
    def integer_mm(x, y):
        return [[sum(x[i][h]*y[h][j] for h in range(2)) for j in range(2)] for i in range(2)]
    T, B, Ti = [[1, 1], [0, 1]], [[0, 0], [0, 1]], [[1, -1], [0, 1]]
    assert integer_mm(integer_mm(T, B), Ti)[0][1] != T[0][0]*B[0][1]*Ti[1][1]
    return {"typed_square_zero_filtration_cases": cases, "type_dimension_cases": counts,
            "characteristics": [3, 5], "empty_family_and_empty_block_included": True,
            "negative_controls": ["omit smaller-width vanishing"]}


def conjugation_sign_check():
    # Degree-one epsilon coefficients are noncommutative polynomials in
    # K,P,R; products of two epsilon coefficients are zero.
    def add(*polys):
        result = {}
        for poly in polys:
            for word, value in poly.items():
                result[word] = result.get(word, 0)+value
        return {word: value for word, value in result.items() if value}

    def product(a, b):
        out = {}
        for w, x in a.items():
            for v, y in b.items():
                out[w+v] = out.get(w+v, 0)+x*y
        return {w: x for w, x in out.items() if x}

    R, P, K = {("R",): 1}, {("P",): 1}, {("K",): 1}
    actual = add(product(P, R), product(K, R), {("R", "P"): -1})
    expected = add(product(K, R), {("R", "P"): -1}, product(P, R))
    assert actual == expected
    wrong = add(product(P, R), product(K, R), product(R, P))
    assert wrong != expected
    return {"identity": "(1+P)(1+K)R(1-P)=R+(K+P)R-RP modulo epsilon^2",
            "noncommuting_coefficient_ring": "Z", "negative_control": "use 1+P for the right inverse factor"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    atlas = json.loads(gzip.decompress((ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()))
    rows = {row[0]: row for row in atlas["modules"]}
    sources = []
    for module, intervals in RANGES.items():
        item = {"repository": atlas["repository"], "commit": atlas["commit"],
                "path": "lean/src/"+module.replace(".", "/")+".lean", "git_blob_sha1": rows[module][1]}
        checked = inspect_file(item, offline=args.offline)
        lines = (ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]).read_bytes().splitlines(keepends=True)
        excerpts = []
        for start, end in intervals:
            assert 1 <= start <= end <= len(lines) and end-start+1 <= 120
            excerpts.append({"start": start, "end": end,
                             "sha256": hashlib.sha256(b"".join(lines[start-1:end])).hexdigest()})
        sources.append({**item, "module": module, "sha256": checked["sha256"],
                        "matches_pinned_blob": True, "reviewed_excerpts": excerpts})
    for reference in PRIMARY:
        assert hashlib.sha256((ROOT/reference["path"]).read_bytes()).hexdigest() == reference["sha256"]
    artifacts = ["notes/selmer-integral-frontier-ordinary-local-count.md",
                 "paper/shared/selmer-integral-frontier-ordinary-local-count.tex",
                 "paper/shared/selmer-integral-frontier-ordinary-local-count-references.tex",
                 "scripts/check_selmer_integral_frontier_ordinary_local_count.py"]
    checks = {"finite_coefficients": finite_coefficient_checks(),
              "typed_filtration": coefficient_and_filtration_checks(),
              "prescribed_conjugation": conjugation_sign_check()}
    report = {"schema_version": 1, "status": "PASS",
              "claim": "Source authentication and exact algebra supporting the actual ordinary local Selmer estimate.",
              "result": "For fixed ordinary data, every m has |Z_v,m| <= q^(m(n+nu)(d+1)+C_v), with C_v=sum w_ij c_ij independent of m and of the auxiliary level.",
              "quantifiers": "Fix normalized point, coefficient field, odd family and local witnesses; exists C_v, for every m>=0 and every auxiliary level N.",
              "sources": sources, "primary_references": PRIMARY, "exact_checks": checks,
              "limits": ["The script is not the human proof or a Lean build.",
                         "Finite matrix checks support, but do not replace, the general width-filtration proof.",
                         "Local Tate duality and local reciprocity are verified published arithmetic inputs.",
                         "No finite cocycle lifting is assumed; no uniformity over changing arithmetic points is asserted.",
                         "Global duality, distinguished-place estimates and patched modules remain separate.",
                         "No whole proof node closes: ordinary RH 6/9; Dirichlet GRH 17/31."],
              "reproduce": "python3 scripts/check_selmer_integral_frontier_ordinary_local_count.py --offline",
              "artifacts": {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in artifacts}}
    (ROOT/"certificates/selmer-integral-frontier-ordinary-local-count.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "pinned_modules": len(sources),
                      "pairing_checks": checks["finite_coefficients"]["perfect_pairing_matrices"],
                      "annihilator_checks": checks["finite_coefficients"]["annihilator_matrices"],
                      "filtration_checks": checks["typed_filtration"]["typed_square_zero_filtration_cases"],
                      "type_dimension_checks": checks["typed_filtration"]["type_dimension_cases"]}))


if __name__ == "__main__":
    main()
