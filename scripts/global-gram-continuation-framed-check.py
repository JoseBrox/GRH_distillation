#!/usr/bin/env python3
"""Authenticate exact framed-return interfaces and check the finite dictionary.

The finite diagonal-group model tests the quotient, stabilizer index and Haar
factors in the written all-rank adelic proof.  It does not establish that proof,
any uniform arithmetic estimate, or a Lean build.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path

import check_global_norm_frontier_off_diagonal as provenance

ROOT = Path(__file__).resolve().parents[1]
H = "Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals."
T = "Formalism.LocalToGlobal.SiegelLatticeTheory.ClosedLocalOrbits."
L = T + "GaugeLatticeShifts."
SOURCES = [
    (H + "HidaSetting", [(267, 282), (302, 321)]),
    (H + "WuDecay", [(18, 43)]),
    (T + "TermOp", [(60, 99), (140, 160), (207, 216)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.IsPrimitiveSub", [(272, 274)]),
    (L + "SlabCountPfSteps", [(16, 22)]),
    (L + "SlabCountPf", [(50, 142), (143, 204)]),
    (L + "DoubleCosetSingleUnfolding", [(373, 396), (435, 447), (525, 548)]),
]
DEPENDENCIES = [
    "paper/shared/global-norm-frontier-seed-decay.tex",
    "paper/shared/global-gram-continuation.tex",
    "paper/shared/global-gram-continuation-framed-returns.tex",
    "paper/shared/global-gram-continuation-framed-references.tex",
]


def finite_models():
    reports = []
    detected_index = False
    detected_haar = False
    detected_nontrivial_fibre = False
    for degree in (3, 4, 5):
        G = list(itertools.product(range(degree), range(2)))
        one = (0, 0)

        def mul(a, b):
            return ((a[0] + (-1)**a[1]*b[0]) % degree, (a[1]+b[1]) % 2)

        def inv(a):
            return next(b for b in G if mul(a, b) == one)

        def subgroup(gens):
            out = {one}
            while True:
                nxt = out | {mul(a, b) for a in out for b in gens}
                if out == nxt:
                    return out
                out = nxt

        def tr(H, candidates=G):
            unused = set(candidates)
            out = []
            for a in sorted(candidates):
                if a in unused:
                    out.append(a)
                    unused.difference_update(mul(h, a) for h in H)
            assert not unused
            return out

        def conj(a, H):
            return {mul(mul(a, h), inv(a)) for h in H}

        def dc(left, right, candidates):
            unused = set(candidates)
            out = []
            for a in sorted(candidates):
                if a in unused:
                    out.append(a)
                    unused.difference_update(mul(mul(l, a), r) for l in left for r in right)
            assert not unused
            return out

        rotation = subgroup([(1, 0)])
        reflection = subgroup([(0, 1)])
        trivial = {one}
        whole = set(G)
        cases = [
            (whole, rotation, rotation, trivial, reflection),
            (whole, trivial, whole, rotation, reflection),
            (rotation, trivial, reflection, trivial, rotation),
            (reflection, trivial, whole, trivial, reflection),
            (whole, rotation, whole, rotation, whole),
            (rotation, rotation, whole, trivial, trivial),
        ]
        for S, N, Sp, Np, K in cases:
            assert N <= S and Np <= Sp
            assert all(conj(s, N) == N for s in S)
            assert all(conj(s, Np) == Np for s in Sp)
            xu, xp = one, (1, 1)

            def rows(A, x):
                out = {}
                for s in sorted(A):
                    a = mul(s, x)
                    lattice = frozenset(mul(a, k) for k in K)
                    out.setdefault(lattice, a)
                return list(out.items())

            rows0, rows1 = rows(S, xu), rows(Sp, xp)

            def norm_seed(A, seed):
                vals = {}
                for j, a in enumerate(tr(A)):
                    for s in A:
                        vals[mul(s, a)] = Fraction(j+seed, j+2)
                return vals

            f, fp = norm_seed(S, 2), norm_seed(Sp, 3)
            support = {mul(mul(s, xu), k) for s in S for k in K}
            supportp = {mul(mul(s, xp), k) for s in Sp for k in K}
            D, Dp = tr(S), tr(Sp)

            def P(x, y, first=True):
                F, supp, reps = (f, support, D) if first else (fp, supportp, Dp)
                return sum((F[mul(d, x)] for d in reps if mul(d, y) in supp), Fraction(0))

            h0 = []
            for lattice, a in rows0:
                A = S & conj(a, K)
                NL = N & conj(a, K)
                assert len(A) % len(NL) == 0
                h0.append(len(A)//len(NL))
            Fsize = {}
            for j, (L1, a1) in enumerate(rows1):
                for k, (L2, a2) in enumerate(rows1):
                    exists = any({mul(s, x) for x in L2} == set(L1) for s in Sp)
                    A2, N2 = Sp & conj(a2, K), Np & conj(a2, K)
                    Fsize[j, k] = len(A2)//len(N2) if exists else 0
            M = sum(Fsize.values())
            for cinf, cfin in ((Fraction(1, len(G)), Fraction(2, 3)),
                               (Fraction(5, 7), Fraction(1, len(G)))):
                J = cinf*cfin*sum(P(one, b)*P(one, b, False) for b in G)
                v0 = cfin*len(K)
                total = Fraction(0)
                maxfibre = 0
                for j, (Lat, a) in enumerate(rows0):
                    A, NL = S & conj(a, K), N & conj(a, K)
                    Q = {x: f[x]*P(x, a, False) for x in G}
                    intA = cinf*sum(Q[x] for x in tr(A))
                    intN = cinf*sum(Q[x] for x in tr(NL))
                    assert intN == h0[j]*intA
                    detected_index |= intN != intA
                    Y = {b for b in G if any(mul(s, b) in Lat for s in S)}
                    slice_integral = cinf*cfin*sum(
                        f[x]*P(x, b, False) for x in D for b in Y if b in support)
                    assert slice_integral == v0*intA
                    assert slice_integral <= J
                    detected_haar |= slice_integral != len(K)*intA
                    fibres = Counter()
                    for Latp, ap in rows1:
                        NLp = Np & conj(ap, K)
                        candidates = [r for r in G if {mul(r, z) for z in Latp} == set(Lat)]
                        for r in dc(NL, NLp, candidates):
                            R = NL & conj(r, NLp)
                            orbit_integral = cinf*sum(f[x]*fp[mul(inv(r), x)] for x in tr(R))
                            unfolded = cinf*sum(
                                f[x]*sum(fp[mul(mul(inv(r), m), x)] for m in tr(R, NL))
                                for x in tr(NL))
                            assert orbit_integral == unfolded
                            total += orbit_integral
                            for m in tr(R, NL):
                                g = mul(inv(r), m)
                                coset = min(mul(s, g) for s in Sp)
                                fibres[coset] += 1
                                assert mul(g, a) in supportp
                    maxfibre = max(maxfibre, max(fibres.values(), default=0))
                    assert all(count <= M for count in fibres.values())
                assert total <= Fraction(M*sum(h0), 1)*J/v0
                detected_nontrivial_fibre |= maxfibre > 1
                reports.append({"group_order": len(G), "S": len(S), "N": len(N),
                                "Sprime": len(Sp), "Nprime": len(Np), "K0": len(K),
                                "source_rows": len(rows0), "target_rows": len(rows1),
                                "M": M, "max_fibre": maxfibre,
                                "sum": str(total), "bound": str(Fraction(M*sum(h0), 1)*J/v0)})
    assert detected_index and detected_haar and detected_nontrivial_fibre
    return {"exact_models": len(reports), "models": reports,
            "missing_stabilizer_index_detected": detected_index,
            "missing_finite_Haar_scalar_detected": detected_haar,
            "nontrivial_fibres_present": detected_nontrivial_fibre,
            "does_not_replace_adelic_proof": True}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    provenance.SOURCES = SOURCES
    records = provenance.source_records(args.offline)
    out = {
        "claim": "Full original OOLintSum and orbital absolute convergence in the established arithmetic gap regime",
        "classification": "closed actual framed-return convergence obligation within W08",
        "source_verification": records,
        "dependencies": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
                         for p in DEPENDENCIES],
        "diagnostics": finite_models(),
        "scope": {"original_framed_return_set": True,
                  "original_Haar_measures": True,
                  "PhWellDef_needed_for_positive_sum": False,
                  "K0_used_only_for_domination": True,
                  "unrestricted_FoldOK_only_OOLintSumC_claimed": False,
                  "uniform_return_bound_proved": False,
                  "complex_raw_kernel_Gram_identity_proved": False,
                  "whole_node_closed": False, "lean_build_run": False},
    }
    target = ROOT / "certificates/global-gram-continuation-framed.json"
    target.write_text(json.dumps(out, indent=2)+"\n")
    print(json.dumps({"certificate": str(target.relative_to(ROOT)),
                      "sources": len(records), "exact_models": out["diagnostics"]["exact_models"],
                      "uniform_budget_proved": False}))


if __name__ == "__main__":
    main()
