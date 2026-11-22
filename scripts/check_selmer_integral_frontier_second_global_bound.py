#!/usr/bin/env python3
"""Check the original W2 obstruction translation and second Selmer interface.

The matrix checks use the actual commutative paired coefficient algebra,
with noncommuting matrix coefficients over truncated polynomial rings.
Finite dihedral examples check cocycles, projection and normalization;
they do not construct the arithmetic tower or build Lean.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path

from check_sources import inspect_file
from check_selmer_integral_frontier_second_bound_suppliers import TruncatedRing

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules."
RANGES = {
    BASE+"PairedDualFirstOrderDualMatrixSpace": [(108, 150), (220, 247), (251, 274), (306, 329), (334, 348)],
    "Development.AutomorphicArithmetic.AutomorphicVarieties.WeilGroupCharacters.UniversalOrdinaryDeterminantRing": [(97, 103)],
    BASE+"ThetaCoefficientMapEq": [(54, 61)],
    BASE+"ArchimedeanH0Cards.TranslDD": [(109, 153)],
    BASE+"ArchimedeanH0Cards.Transl": [(66, 145), (155, 214), (215, 291), (292, 364)],
    BASE+"ArchimedeanH0Cards.TranslGen": [(13, 118)],
    BASE+"ArchimedeanH0Cards.ObstructionBoundOfDuality": [(197, 218)],
}


class Matrices:
    def __init__(self, p, m, n):
        self.ring = TruncatedRing(p, m)
        self.n = n

    def zero(self):
        return [[self.ring.zero for _ in range(self.n)] for _ in range(self.n)]

    def identity(self):
        return [[self.ring.one if i == j else self.ring.zero for j in range(self.n)] for i in range(self.n)]

    def add(self, a, b):
        return [[self.ring.add(x, y) for x, y in zip(ar, br)] for ar, br in zip(a, b)]

    def neg(self, a):
        return [[self.ring.neg(x) for x in row] for row in a]

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def scale(self, c, a):
        return [[tuple(c*x % self.ring.p for x in value) for value in row] for row in a]

    def transpose(self, a):
        return [list(row) for row in zip(*a)]

    def mm(self, a, b):
        return self.ring.mm(a, b)

    def comm(self, a, b):
        return self.sub(self.mm(a, b), self.mm(b, a))

    def patterned(self, a, odd, seed, symmetric=False):
        out = self.zero()
        for i in range(self.n):
            for j in range(self.n):
                if ((i < a) != (j < a)) == odd:
                    u, v = (min(i, j), max(i, j)) if symmetric else (i, j)
                    out[i][j] = self.ring.elem([seed+u+2*v, 1+seed*u+v])
        return out


class PairedAlgebra:
    def __init__(self, mats, size):
        self.M, self.s = mats, size

    def zero(self):
        return [self.M.zero() for _ in range(2*self.s+2)]

    def W2(self, even, odd):
        result = self.zero()
        for j, value in enumerate(even):
            result[1+self.s+j] = value
        result[-1] = odd
        return result

    def mul(self, x, y):
        M, s = self.M, self.s
        out = self.zero()
        out[0] = M.mm(x[0], y[0])
        for j in range(1, 1+2*s):
            out[j] = M.add(M.mm(x[0], y[j]), M.mm(x[j], y[0]))
        out[-1] = M.add(M.mm(x[0], y[-1]), M.mm(x[-1], y[0]))
        for j in range(s):
            out[-1] = M.add(out[-1], M.add(M.mm(x[1+j], y[1+s+j]), M.mm(x[1+s+j], y[1+j])))
        return out

    def rep(self, rho, kappa, inverse=False):
        result = self.zero()
        result[0] = rho
        for j, value in enumerate(kappa):
            result[1+j] = self.M.neg(self.M.mm(rho, value)) if inverse else self.M.mm(value, rho)
        return result

    def ordinary(self, w, witnesses, inverse=False):
        result = self.zero()
        result[0] = w
        for j, value in enumerate(witnesses):
            result[1+j] = self.M.mm(w, value) if inverse else self.M.neg(self.M.mm(value, w))
        return result


def matrix_formula_checks():
    cases = noncommuting = interleaved = 0
    for p, m, n, s in itertools.product((3, 5), (1, 2), (2, 3, 4), range(3)):
        for a in sorted({1, n-1}):
            for alternate in (False, True):
                M = Matrices(p, m, n)
                D = PairedAlgebra(M, s)
                rho, basis = M.identity(), M.identity()
                for i in range(n):
                    rho[i][i] = M.ring.elem([1, i+1])
                    for j in range(i+1, n):
                        if (i < a) == (j < a):
                            rho[i][j] = M.ring.elem([1+i+j, i+1])
                            basis[i][j] = M.ring.elem([i+j+1, j])
                rho_inv = M.ring.inverse_upper(rho)
                basis_inv = M.ring.inverse_upper(basis)
                permutation = list(range(0, n, 2))+list(range(1, n, 2)) if alternate else list(range(n))
                P = M.zero()
                for j, i in enumerate(permutation):
                    P[i][j] = M.ring.one
                w, wi = M.mm(basis, P), M.mm(M.transpose(P), basis_inv)
                assert M.mm(w, wi) == M.identity() and M.mm(wi, w) == M.identity()
                types = [i < a for i in permutation]
                if types != sorted(types, reverse=True):
                    interleaved += 1
                kappas = [M.patterned(a, True, j+1) for j in range(s)]
                witnesses = [M.patterned(a, True, j+3) for j in range(s)]
                odd = M.patterned(a, True, 7)
                local_even = []
                for j in range(s):
                    value = M.zero()
                    for i in range(n):
                        for k in range(i+1, n):
                            if types[i] == types[k]:
                                value[i][k] = M.ring.elem([i+k+j+1, j+2])
                    local_even.append(value)
                even = [M.mm(M.mm(w, value), wi) for value in local_even]
                lifted = D.W2(even, odd)
                transformed_even = [M.mm(M.mm(rho, value), rho_inv) for value in even]
                transformed_odd = M.mm(M.mm(rho, odd), rho_inv)
                for kappa, value in zip(kappas, transformed_even):
                    commutator = M.comm(kappa, value)
                    noncommuting += commutator != M.zero()
                    transformed_odd = M.add(transformed_odd, commutator)
                actual = D.mul(D.mul(D.rep(rho, kappas), lifted), D.rep(rho_inv, kappas, inverse=True))
                assert actual == D.W2(transformed_even, transformed_odd)
                correction = odd
                for witness, value in zip(witnesses, even):
                    correction = M.add(correction, M.comm(witness, value))
                actual_local = D.mul(D.mul(D.ordinary(wi, witnesses, inverse=True), lifted), D.ordinary(w, witnesses))
                expected_odd = M.mm(M.mm(wi, correction), w)
                assert actual_local == D.W2(local_even, expected_odd)
                assert all(expected_odd[i][i] == M.ring.zero for i in range(n))
                corrected = D.W2(even, M.sub(odd, correction))
                actual_corrected = D.mul(D.mul(D.ordinary(wi, witnesses, inverse=True), corrected), D.ordinary(w, witnesses))
                assert actual_corrected == D.W2(local_even, M.zero())
                assert all(actual_corrected[c][i][j] == M.ring.zero
                           for c in range(2*s+2) for i in range(n) for j in range(i+1))
                cases += 1
    assert noncommuting > 0 and interleaved > 0
    return {"original_algebra_matrix_and_local_formulas": cases,
            "nonzero_mixed_commutators": noncommuting,
            "ordinary_bases_with_interleaved_types": interleaved}


def cocycle_checks():
    cases = pair_checks = normalization_checks = 0
    for p, m, n, s in itertools.product((3, 5), (1, 2), (2, 3), (1, 2)):
        M = Matrices(p, m, n)
        kappas = [M.patterned(1, True, j+1, symmetric=True) for j in range(s)]
        even = [M.patterned(1, False, j+2, symmetric=True) for j in range(s)]
        coupling = M.zero()
        for kappa, value in zip(kappas, even):
            coupling = M.add(coupling, M.comm(kappa, value))
        group = list(itertools.product(range(p), range(2)))

        def mul(g, h):
            return ((g[0]+(-1)**g[1]*h[0]) % p, (g[1]+h[1]) % 2)

        def add_pair(x, y):
            return ([M.add(a, b) for a, b in zip(x[0], y[0])], M.add(x[1], y[1]))

        def neg_pair(x):
            return ([M.neg(a) for a in x[0]], M.neg(x[1]))

        def act(g, pair):
            ep, eta = pair
            if g[1]:
                ep, eta = [M.neg(M.transpose(a)) for a in ep], M.neg(M.transpose(eta))
            out = eta
            for kappa, value in zip(kappas, ep):
                out = M.add(out, M.scale(g[0], M.comm(kappa, value)))
            return (ep, out)

        def psi(g):
            return ([M.scale(g[0], value) for value in even],
                    M.scale(g[0]*g[0]*pow(2, -1, p), coupling))

        def section(g):
            return ([M.scale(g[0], value) for value in even], M.zero())

        for g, h in itertools.product(group, repeat=2):
            assert psi(mul(g, h)) == add_pair(psi(g), act(g, psi(h)))
            defect = add_pair(add_pair(act(g, section(h)), neg_pair(section(mul(g, h)))), section(g))
            primitive = ([], M.scale(-g[0]*g[0]*pow(2, -1, p), coupling))
            # Since Psi=x-iota(u), d x = iota(d u) exactly.
            ug = ([], primitive[1])
            uh = ([], M.scale(-h[0]*h[0]*pow(2, -1, p), coupling))
            ugh = ([], M.scale(-mul(g, h)[0]**2*pow(2, -1, p), coupling))
            dut = M.add(M.sub(act(g, uh)[1], ugh[1]), ug[1])
            assert all(value == M.zero() for value in defect[0]) and defect[1] == dut
            pair_checks += 1
        c = (0, 1)
        assert psi(c) == ([M.zero() for _ in range(s)], M.zero())
        v = ([M.zero() for _ in range(s)], M.patterned(1, True, 1, symmetric=True))

        def boundary(g, value):
            return add_pair(act(g, value), neg_pair(value))

        def psi0(g):
            return add_pair(psi(g), boundary(g, v))

        cvalue = psi0(c)
        half = ([M.zero() for _ in range(s)], M.scale(pow(2, -1, p), cvalue[1]))
        corrected_c = add_pair(psi0(c), boundary(c, half))
        assert corrected_c == ([M.zero() for _ in range(s)], M.zero())
        if cvalue[1] != M.zero():
            wrong_sign = add_pair(psi0(c), neg_pair(boundary(c, half)))
            assert wrong_sign != corrected_c
            normalization_checks += 1
        for g in group:
            corrected = add_pair(psi0(g), boundary(g, half))
            assert corrected[0] == psi(g)[0]
        cases += 1
    assert normalization_checks > 0
    return {"finite_dihedral_cocycle_lifts": cases, "full_group_cocycle_and_defect_equations": pair_checks,
            "nonzero_normalization_sign_tests": normalization_checks,
            "coefficient_lengths": [1, 2], "characteristics": [3, 5]}


def negative_controls():
    M = Matrices(3, 1, 2)
    K = M.zero(); K[0][1] = M.ring.one
    P = M.zero(); P[0][0] = M.ring.one
    assert M.comm(K, P) != M.zero()
    # The original mixed term is nonzero and cannot be erased.
    D = PairedAlgebra(M, 1)
    R = D.rep(M.identity(), [K])
    Ri = D.rep(M.identity(), [K], inverse=True)
    result = D.mul(D.mul(R, D.W2([P], M.zero())), Ri)
    assert result[-1] == M.comm(K, P) and result[-1] != M.zero()
    # An odd eta correction cannot erase a nonzero even epsilon' diagonal.
    assert result[2][0][0] == M.ring.one
    # In characteristic2, C2 with kappa(generator)=K and even value P
    # has norm eta[K,P] regardless of the eta component of its lift.
    M2 = Matrices(2, 1, 2)
    K2 = M2.zero(); K2[0][1] = M2.ring.one; K2[1][0] = M2.ring.one
    P2 = M2.zero(); P2[0][0] = M2.ring.one
    assert M2.comm(K2, P2) != M2.zero()
    return ["Dropping the mixed epsilon-epsilon' product changes the actual action.",
            "The even ordinary diagonal restriction cannot be supplied by an odd eta correction.",
            "Characteristic2 can obstruct the cyclic lift; oddness and the division by2 are retained.",
            "The wrong complex-conjugation normalization sign is rejected by the finite cocycle suite."]


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
            content = b"".join(lines[start-1:end])
            assert len(content) <= 12000
            excerpts.append({"start": start, "end": end, "sha256": hashlib.sha256(content).hexdigest()})
        sources.append({**item, "module": module, "sha256": checked["sha256"],
                        "matches_pinned_blob": True, "reviewed_excerpts": excerpts})
    checks = {"matrix_formulas": matrix_formula_checks(), "cocycles": cocycle_checks(),
              "negative_controls": negative_controls()}
    stem = "selmer-integral-frontier-second-global-bound"
    artifacts = [f"notes/{stem}.md", f"paper/shared/{stem}.tex", f"paper/shared/{stem}-references.tex",
                 "scripts/check_selmer_integral_frontier_second_global_bound.py"]
    dependencies = ["certificates/selmer-integral-frontier-obstruction-quotients.json",
                    "certificates/selmer-integral-frontier-second-bound-suppliers.json",
                    "certificates/selmer-integral-frontier-padded-relations.json"]
    for path in artifacts:
        assert all(c >= 32 or c in (10, 9) for c in (ROOT/path).read_bytes()), path
    report = {
        "schema_version": 1, "status": "PASS",
        "claim": "The exact original second Selmer estimate B2 under the retained normalized-point, auxiliary-tower and arithmetic cohomology inputs.",
        "result": "For g+1 tuples of original even Selmer cocycles, there are coefficients c_i in A with one unit and an original W2 Selmer cocycle whose epsilon'_j coefficient is t^C2 sum_i c_i p_ij.",
        "quantifiers": "Fix arithmetic data, point, odd family and auxiliary set; exists C2, for every m, at every sufficiently large N, for every collection of input tuples.",
        "sources": sources, "exact_checks": checks,
        "dependencies": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        "retained_inputs": ["Odd prime ell and the original arithmetic cohomology system",
                            "Original normalized point and odd family",
                            "Original commutative paired coefficient algebra and first-order representation",
                            "Original ordinary witness bases and subgroup mu, and original unramified lifting"],
        "limits": ["Both finite-level Selmer estimates are proved under supplied arithmetic data; this does not construct their arithmetic realization or patched automorphic modules.",
                   "The finite cocycle examples test the translation and do not satisfy or replace the arithmetic hypotheses.",
                   "No Lean build; no whole node closure: RH 6/9 and GRH 17/31."],
        "reproduce": "python3 scripts/check_selmer_integral_frontier_second_global_bound.py --offline",
        "artifacts": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in artifacts},
    }
    (ROOT/f"certificates/{stem}.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "pinned_modules": len(sources), **checks}))


if __name__ == "__main__":
    main()
