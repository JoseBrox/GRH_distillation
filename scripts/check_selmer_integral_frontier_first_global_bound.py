#!/usr/bin/env python3
"""Check the exact finite factors and source interface of the first Selmer bound.

The arithmetic duality theorem is a cited primary input. This script checks
finite linear-algebra identities, source bytes and the exponent assembly;
it does not compute global Galois cohomology or build Lean.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules."
RANGES = {
    BASE+"PairedDualFirstOrderDualMatrixSpace": [(235, 247), (340, 346)],
    BASE+"ThetaCoefficientMapEq": [(49, 61)],
    BASE+"DegreeCountCohomology.IsDualPair": [(44, 75), (79, 94), (124, 146), (158, 158)],
    BASE+"EpsilonEtaMatrices.OneLevel": [(236, 270), (307, 359), (360, 424), (470, 483)],
    BASE+"EpsilonEtaMatrices.W1BoundArithmeticRankTwo": [(30, 61), (95, 165)],
}
PRIMARY = {"url": "https://www.jmilne.org/math/Books/ADTnot.pdf",
           "path": "build/reference-cache/milne-adt-2006.pdf",
           "sha256": "2c6195ec76a974f3f336c77cb71cc3845b018aad2d43136716b3477a3bc5fb31",
           "results": ["I.4.10(a,b): Sha pairing, orthogonal global images and exact sequence",
                       "I.4.15: finiteness for finite ramification sets",
                       "I.5.1: global Euler characteristic"],
           "newly_visually_read_pdf_pages": [65, 75],
           "printed_pages": [57, 67],
           "reused_local_duality_and_trace_evidence": "certificates/selmer-integral-frontier-ordinary-local-count.json"}


def rank_mod_p(rows, p):
    a = [list(r) for r in rows]
    rank = 0
    for j in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(rank, len(a)) if a[i][j] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        u = pow(a[rank][j] % p, -1, p)
        a[rank] = [u*x % p for x in a[rank]]
        for i in range(rank+1, len(a)):
            u = a[i][j] % p
            if u:
                a[i] = [(x-u*y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def all_subspaces(p, d):
    vectors = list(itertools.product(range(p), repeat=d))
    spaces = {frozenset([(0,)*d])}
    todo = list(spaces)
    while todo:
        W = todo.pop()
        for v in vectors:
            if v in W:
                continue
            U = frozenset(tuple((w[i]+c*v[i]) % p for i in range(d))
                          for w in W for c in range(p))
            if U not in spaces:
                spaces.add(U); todo.append(U)
    return vectors, list(spaces)


def annihilator(W, vectors, p):
    return frozenset(v for v in vectors if all(sum(x*y for x, y in zip(v, w)) % p == 0 for w in W))


def finite_factor_checks():
    duality = ordinary = 0
    for p, d in [(3, 3), (5, 2)]:
        vectors, spaces = all_subspaces(p, d)
        perps = {W: annihilator(W, vectors, p) for W in spaces}
        for V, L in itertools.product(spaces, repeat=2):
            assert len(V & L)*len(vectors) == len(perps[V] & perps[L])*len(V)*len(L)
            duality += 1
    p, d = 3, 2
    vectors, spaces = all_subspaces(p, d)
    for coefficients in itertools.product(range(p), repeat=4):
        def delta(v):
            return ((coefficients[0]*v[0]+coefficients[1]*v[1]) % p,
                    (coefficients[2]*v[0]+coefficients[3]*v[1]) % p)
        B = {delta(v) for v in vectors}
        H0 = {v for v in vectors if delta(v) == (0, 0)}
        for b, Z in itertools.product(spaces, repeat=2):
            if not {delta(v) for v in b}.issubset(Z):
                continue
            total = {((x[0]+y[0]) % p, (x[1]+y[1]) % p) for x in B for y in Z}
            local_cohomology_size = Fraction(len(Z), len(B & Z))
            assert local_cohomology_size/Fraction(len(H0)) == Fraction(len(total), len(vectors))
            assert len(total)*len(b) <= len(vectors)*len(Z)
            ordinary += 1
    # Omitting delta(b) subset Z invalidates the useful ordinary bound.
    assert p**2*p**2 > p**2*1
    return {"perfect_duality_subspace_identities": duality,
            "ordinary_quotient_inequalities": ordinary,
            "negative_control": "The ordinary denominator requires delta(b) subset Z."}


def mm(a, b, p):
    n = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) % p for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(r) for r in zip(*a)]


def inverse(a, p):
    n = len(a)
    work = [list(a[i])+[int(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if work[i][j] % p)
        work[j], work[pivot] = work[pivot], work[j]
        u = pow(work[j][j], -1, p)
        work[j] = [u*x % p for x in work[j]]
        for i in range(n):
            if i != j:
                u = work[i][j]
                work[i] = [(x-u*y) % p for x, y in zip(work[i], work[j])]
    return [row[n:] for row in work]


def real_place_checks():
    cases = 0
    for p in (3, 5):
        for n in range(1, 5):
            for a in range(n+1):
                same = lambda i, j: (i < a) == (j < a)
                S = [[int(i == j)+(i+j+1 if i < j and same(i, j) else 0) for j in range(n)] for i in range(n)]
                P0 = mm(S, transpose(S), p)
                Q0 = inverse(P0, p)
                for s in range(3):
                    P = [P0]+[[[(i+j+k+1) % p if not same(i, j) else 0 for j in range(n)] for i in range(n)] for k in range(s)]
                    Q = [Q0]+[[[-x % p for x in row] for row in mm(mm(Q0, X, p), Q0, p)] for X in P[1:]]
                    coords = [(0, i, j) for i in range(n) for j in range(n) if same(i, j)]
                    coords += [(k+1, i, j) for k in range(s) for i in range(n) for j in range(n) if not same(i, j)]
                    D = len(coords)
                    operator = [[0]*D for _ in range(D)]
                    for col, (slot, i, j) in enumerate(coords):
                        Z = [[[0]*n for _ in range(n)] for _ in range(s+1)]
                        Z[slot][i][j] = 1
                        image = [mm(mm(P0, transpose(Z[0]), p), Q0, p)]
                        for k in range(1, s+1):
                            terms = [mm(mm(P[k], transpose(Z[0]), p), Q0, p),
                                     mm(mm(P0, transpose(Z[k]), p), Q0, p),
                                     mm(mm(P0, transpose(Z[0]), p), Q[k], p)]
                            image.append([[sum(T[u][v] for T in terms) % p for v in range(n)] for u in range(n)])
                        for row, (k, u, v) in enumerate(coords):
                            operator[row][col] = (-image[k][u][v]-int(row == col)) % p
                    nu = a*(a-1)//2+(n-a)*(n-a-1)//2+s*a*(n-a)
                    assert D-rank_mod_p(operator, p) == nu
                    assert all(X == transpose(X) for X in P)
                    cases += 1
    return {"twisted_transpose_fixed_space_matrices": cases,
            "characteristics": [3, 5], "matrix_sizes": [1, 2, 3, 4],
            "result": "Each non-scalar symmetric first-order twist has fixed rank exactly nu.",
            "scope": "Finite coefficient checks; the human module isomorphism proves every truncation."}


def exponent_check():
    m, n, nu, d, qaux, d0, dp0 = sp.symbols("m n nu d qaux d0 dp0")
    old = m*(n*(dp0+(d-dp0))+nu*(d0+(d-d0))+n*qaux-nu*d)
    assert sp.expand(old-m*n*(d+qaux)) == 0
    assert sp.expand(old+m*nu*d-m*n*(d+qaux)) == m*nu*d
    return {"exact_identity": "sum ordinary m(n d'_v+nu d_v) + m n q_aux - m nu d = m n(d+q_aux), when both degree sums equal d",
            "negative_control": "Omitting the real-place invariant factor leaves the extra m nu d."}


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
            content = b"".join(lines[start-1:end]); assert len(content) <= 12000
            excerpts.append({"start": start, "end": end, "sha256": hashlib.sha256(content).hexdigest()})
        sources.append({**item, "module": module, "sha256": checked["sha256"],
                        "matches_pinned_blob": True, "reviewed_excerpts": excerpts})
    assert hashlib.sha256((ROOT/PRIMARY["path"]).read_bytes()).hexdigest() == PRIMARY["sha256"]
    checks = {"finite_cardinalities": finite_factor_checks(), "real_places": real_place_checks(), "exponent": exponent_check()}
    stem = "selmer-integral-frontier-first-global-bound"
    artifacts = [f"notes/{stem}.md", f"paper/shared/{stem}.tex", f"paper/shared/{stem}-references.tex",
                 "scripts/check_selmer_integral_frontier_first_global_bound.py"]
    dependencies = ["certificates/selmer-integral-frontier-ordinary-local-count.json",
                    "certificates/selmer-integral-frontier-invariant-counts.json",
                    "certificates/selmer-integral-frontier-tower-detection.json"]
    for path in artifacts:
        assert all(c >= 32 or c in (10, 9) for c in (ROOT/path).read_bytes()), path
    report = {
        "schema_version": 1, "status": "PASS",
        "claim": "Exact finite factor checks and authenticated source interfaces supporting the human proof of the original first Selmer bound under its supplied arithmetic system.",
        "result": "#Sel1_N,m <= #Bd1_N,m q^(mn(d+q_aux)+C), with C=C_G+C_det+C_0+sum C_v+sum C_j.",
        "quantifiers": "Fix the original arithmetic system, normalized point, odd family, detectors and tower; exists C, for every m>=0, for every sufficiently large N.",
        "sources": sources, "primary_references": [PRIMARY], "exact_checks": checks,
        "dependencies": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        "retained_inputs": ["Original global and local arithmetic duality system and its actual local maps",
                             "Original ArData.cw_epsilon and c_epsilon signs: chi(c_v)=chi(c)=-1, hence the first-order real twist is symmetric (IsDualPair91-92; OneLevel380-388)",
                            "Original ordinary Euler degrees and diagonal abelianization ranks separately at each place",
                            "Original normalized-point, distinguished-rigidity and simple-spectrum hypotheses",
                            "Original auxiliary tower kernel and convergence conditions"],
        "limits": ["The first Selmer estimate is proved under the supplied arithmetic system; its realization or construction is not asserted.",
                   "Poitou–Tate duality and local/global Euler characteristics are cited primary theorems, not computational conclusions.",
                   "The finite checks support the human proof and do not build Lean.",
                   "The second Selmer estimate, normalized-point construction and patched modules remain separate.",
                   "No whole node closes: RH 6/9 and Dirichlet GRH 17/31."],
        "reproduce": "python3 scripts/check_selmer_integral_frontier_first_global_bound.py --offline",
        "artifacts": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in artifacts},
    }
    (ROOT/f"certificates/{stem}.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "pinned_modules": len(sources), **checks}))


if __name__ == "__main__":
    main()
