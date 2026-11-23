#!/usr/bin/env python3
"""Authenticate the literal period Gram interface and exact finite diagnostics.

The arithmetic theorem is proved conventionally in the companion TeX.
These finite noncommutative Gaussian-integer computations check the
phase, stabilizer, complete-return and Haar bookkeeping independently.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import check_global_norm_frontier_off_diagonal as provenance

ROOT = Path(__file__).resolve().parents[1]
P = "Formalism.LocalToGlobal.SiegelLatticeTheory."
SOURCES = [
    (P+"HaarTransversals.HidaSetting", [(172, 173), (207, 277)]),
    (P+"HaarTransversals.PoincareInHH", [(144, 170), (179, 215), (248, 263)]),
    (P+"HaarTransversals.UnitaryHaarProducts.InHHGamUnipKuGlob", [(470, 532)]),
    (P+"FlagStabilizerTensors.PoincareConstantEq", [(25, 59), (118, 128)]),
    (P+"FlagStabilizerTensors.ParametersTermRelations", [(38, 75), (83, 99)]),
    (P+"SiegelMassRatios.ColsDim", [(18, 39), (63, 69), (87, 96)]),
    (P+"ClosedLocalOrbits.TermDef", [(142, 154)]),
    (P+"ClosedLocalOrbits.TermOp", [(22, 33), (60, 99), (194, 229), (244, 266), (276, 292)]),
    (P+"ClosedLocalOrbits.GaugeLatticeShifts.RegroupPfTermCar", [(75, 143)]),
    (P+"ClosedLocalOrbits.GaugeLatticeShifts.RegroupPf", [(24, 92), (263, 269), (341, 351)]),
    (P+"ClosedLocalOrbits.GaugeLatticeShifts.KExpCut", [(109, 113), (622, 648)]),
    (P+"ClosedLocalOrbits.GaugeLatticeShifts.SlabCoverPf", [(17, 89)]),
]
PROOF_FILES = [
    "paper/shared/global-gram-continuation-period-identity.tex",
    "paper/shared/global-gram-continuation-period-references.tex",
    "notes/global-gram-continuation-period-identity.md",
    "scripts/global-gram-continuation-period-check.py",
]
DEPENDENCIES = [
    "paper/shared/global-gram-continuation.tex",
    "paper/shared/global-gram-continuation-framed-returns.tex",
    "paper/shared/global-gram-continuation-phases.tex",
]

# Gaussian integers are represented by integer pairs, with no floating point.
ZERO = (0, 0)
ONE = (1, 0)
ROOTS = [ONE, (0, 1), (-1, 0), (0, -1)]


def plus(a, b):
    return (a[0]+b[0], a[1]+b[1])


def times(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def conj(a):
    return (a[0], -a[1])


def scale(c, v):
    return [times(c, z) for z in v]


def addvec(a, b):
    return [plus(x, y) for x, y in zip(a, b)]


def matrix_zero(d, e):
    return [[ZERO for _ in range(e)] for _ in range(d)]


def add_outer(out, a, b, c=ONE):
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i][j] = plus(out[i][j], times(c, times(x, conj(y))))


def mulmat_integer(out, a):
    return [[(a*x, a*y) for x, y in row] for row in out]


def model(m, refl_source, refl_target, central_source, central_target, phase_index):
    # D_(2m) x C4, with the literal diagonal rational subgroup in G x G.
    G = [(a, b, c) for a in range(m) for b in range(2) for c in range(4)]

    def mul(x, y):
        return ((x[0]+(-1 if x[1] else 1)*y[0]) % m,
                (x[1]+y[1]) % 2, (x[2]+y[2]) % 4)

    def inv(x):
        return (((1 if x[1] else -1)*x[0]) % m, x[1], -x[2] % 4)

    def chi(x):
        rotation_sign = x[0] if m % 2 == 0 else 0
        return ROOTS[(2*(rotation_sign+x[1])+phase_index*x[2]) % 4]

    def subgroup(refl, central):
        return [(a, b, c) for a, b, c in G
                if ((b == 0 and a == 0) or (b == 1 and a == refl))
                and (central or c == 0)]

    N = subgroup(refl_source, central_source)
    Np = subgroup(refl_target, central_target)
    assert all(mul(x, y) in N for x in N for y in N)
    assert all(mul(x, y) in Np for x in Np for y in Np)
    assert all(chi(mul(x, y)) == times(chi(x), chi(y)) for x in G for y in G)

    def left_transversal(H):
        unseen = set(G)
        reps = []
        while unseen:
            r = min(unseen)
            reps.append(r)
            unseen.difference_update(mul(h, r) for h in H)
        assert len(reps)*len(H) == len(G)
        return reps

    def seed(H, dim, twist):
        out = {}
        for j, r in enumerate(left_transversal(H)):
            v = [((j+1)*(i+1)+twist*(i+2),
                  (j*j+2*i+twist) % (7+i)-3) for i in range(dim)]
            for h in H:
                out[mul(h, r)] = scale(conj(chi(h)), v)
        assert len(out) == len(G)
        assert all(out[mul(h, g)] == scale(conj(chi(h)), out[g]) for h in H for g in G)
        return out

    W = seed(N, 2, 1)
    Wp = seed(Np, 3, 4)

    def period(H, values, x):
        ans = [ZERO for _ in values[x]]
        for delta in left_transversal(H):
            ans = addvec(ans, scale(chi(delta), values[mul(delta, x)]))
        return ans

    # Fundamental domain G x {1} for diagonal Gamma in G x G.
    raw_gram = matrix_zero(2, 3)
    for x in G:
        add_outer(raw_gram, period(N, W, x), period(Np, Wp, x))

    unseen = set(G)
    reps = []
    while unseen:
        r = min(unseen)
        reps.append(r)
        unseen.difference_update(mul(mul(n, r), np) for n in N for np in Np)

    rhs = matrix_zero(2, 3)
    wrong_phase = matrix_zero(2, 3)
    wrong_stabilizer = matrix_zero(2, 3)
    diagonal_only = matrix_zero(2, 3)
    sizes = []
    representative_changes = 0
    for j, r in enumerate(reps):
        Rp = {mul(mul(r, np), inv(r)) for np in Np}
        R = sorted(set(N).intersection(Rp))
        sizes.append(len(R))
        orbital = matrix_zero(2, 3)
        for x in left_transversal(R):
            y = mul(inv(r), x)
            add_outer(orbital, W[x], Wp[y])
            add_outer(rhs, W[x], Wp[y], chi(r))
            add_outer(wrong_phase, W[x], Wp[y], conj(chi(r)))
            if j == 0:
                add_outer(diagonal_only, W[x], Wp[y], chi(r))
        for x in G:
            add_outer(wrong_stabilizer, W[x], Wp[mul(inv(r), x)], chi(r))

        # Verify the full weighted orbital term after independent left/right
        # representative changes, with the newly conjugated stabilizer.
        weighted = [[times(chi(r), z) for z in row] for row in orbital]
        for n, np in ((N[-1], Np[0]), (N[0], Np[-1]), (N[-1], Np[-1])):
            rr = mul(mul(n, r), np)
            RR = sorted(set(N).intersection(mul(mul(rr, x), inv(rr)) for x in Np))
            changed = matrix_zero(2, 3)
            for x in left_transversal(RR):
                add_outer(changed, W[x], Wp[mul(inv(rr), x)], chi(rr))
            assert changed == weighted
            representative_changes += 1

    # Infinite Haar atom 2/7; finite Haar atom 3/5; c_u=4,c_u'=9.
    # Their exact common scalar is 1/35. vol(K)=(3/5)|G|, not 1.
    assert Fraction(2, 7)*Fraction(3, 5)/6 == Fraction(1, 35)
    assert Fraction(2, 7)*(Fraction(3, 5)*len(G))/6 == Fraction(len(G), 35)
    assert raw_gram == mulmat_integer(rhs, len(G))
    # A nonzero test value is necessary for the dropped-volume control.
    assert any(z != ZERO for row in raw_gram for z in row)
    return {
        "m": m, "group_order": len(G), "source_unipotent_order": len(N),
        "target_unipotent_order": len(Np), "double_cosets": len(reps),
        "stabilizer_orders": sorted(set(sizes)), "phase_index": phase_index,
        "representative_changes": representative_changes,
        "negative_controls_detected": {
            "dropped_finite_Haar_volume": raw_gram != rhs,
            "conjugated_wrong_phase": raw_gram != mulmat_integer(wrong_phase, len(G)),
            "dropped_stabilizer_quotient": raw_gram != mulmat_integer(wrong_stabilizer, len(G)),
            "discarded_noninitial_returns": raw_gram != mulmat_integer(diagonal_only, len(G)),
        },
        "exact_complex_entry_00_before_common_factor": list(raw_gram[0][0]),
    }


def diagnostics():
    reports = []
    for m in (3, 4, 5, 6):
        for shift in (0, 1):
            for central in (False, True):
                for phase in (1, 3):
                    reports.append(model(m, 0, shift, central, central, phase))
    controls = {key:sum(r["negative_controls_detected"][key] for r in reports)
                for key in reports[0]["negative_controls_detected"]}
    assert all(n > 0 for n in controls.values())
    return {"models": reports, "model_count": len(reports),
            "representative_changes": sum(r["representative_changes"] for r in reports),
            "negative_control_detection_counts": controls,
            "arithmetic": "Exact integer pairs for Gaussian integers; exact Fraction Haar scalars.",
            "scope": "Finite algebraic diagnostics, not an arithmetic convergence proof or a uniform norm estimate."}


def records(paths):
    return [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in paths]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    provenance.SOURCES = SOURCES
    src = provenance.source_records(args.offline)
    checks = diagnostics()
    out = {
        "classification": "closed actual period-expansion supplier within W08",
        "claim": "Original NeatKu and exact EntryUnfold/KExpansion for every existing original arithmetic setting in the established seed-decay gap regime",
        "source_revision": "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de",
        "source_verification": src,
        "proof_files": records(PROOF_FILES), "dependencies": records(DEPENDENCIES),
        "diagnostics": checks,
        "scope": {"actual_Poincare_periods": True, "all_original_GTerm_returns_retained": True,
                  "original_stabilizers_phases_Haar_volumes": True,
                  "Riesz_antilinearity_retained": True,
                  "source_and_target_restrictions_explicit": True,
                  "raw_KgsOf_pair_dictionary_proved": False,
                  "different_arithmetic_chain_map_identified": False,
                  "uniform_positive_trace_budget_proved": False,
                  "whole_W08_closed": False, "lean_build_run": False},
    }
    target = ROOT/"certificates/global-gram-continuation-period.json"
    target.write_text(json.dumps(out, indent=2)+"\n")
    print(json.dumps({"certificate": str(target.relative_to(ROOT)), "sources": len(src),
                      "exact_models": checks["model_count"],
                      "representative_changes": checks["representative_changes"],
                      "negative_controls": checks["negative_control_detection_counts"],
                      "uniform_budget_proved": False}))


if __name__ == "__main__":
    main()
