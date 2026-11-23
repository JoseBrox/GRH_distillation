#!/usr/bin/env python3
"""Check exact original projector interfaces and finite return/convolution models.

The infinite Poincare/convolution interchange is proved in the TeX by
the positive L2 majorant, not by these finite diagnostics.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import json
from pathlib import Path

import check_global_norm_frontier_off_diagonal as provenance

ROOT = Path(__file__).resolve().parents[1]
H = "Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals."
SOURCES = [
    (H+"HidaSetting", [(203, 205), (228, 245), (264, 265), (357, 363)]),
    (H+"PoincareInHH", [(172, 215)]),
    (H+"ProjRows", [(25, 42), (106, 120)]),
    (H+"RowsDef", [(17, 20), (129, 131)]),
    (H+"UnitaryHaarProducts.InHHCut", [(345, 412)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.GlobAut",
     [(48, 72), (93, 101), (125, 137), (227, 255)]),
]
PROOF_FILES = [
    "paper/shared/global-gram-continuation-projectors.tex",
    "paper/shared/global-gram-continuation-projector-references.tex",
    "notes/global-gram-continuation-projectors.md",
    "scripts/global-gram-continuation-projector-check.py",
]
DEPENDENCIES = [
    "paper/shared/global-gram-continuation.tex",
    "paper/shared/global-gram-continuation-framed-returns.tex",
    "paper/shared/global-gram-continuation-phases.tex",
    "paper/shared/global-gram-continuation-period-identity.tex",
    "paper/shared/global-norm-frontier-seed-decay.tex",
]
ZERO = (Q(0), Q(0))
ROOTS = [(Q(1), Q(0)), (Q(0), Q(1)), (Q(-1), Q(0)), (Q(0), Q(-1))]


def add(x, y):
    return (x[0]+y[0], x[1]+y[1])


def mul(x, y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])


def scale(a, x):
    return (a*x[0], a*x[1])


def conj(x):
    return (x[0], -x[1])


def total(vals):
    out = ZERO
    for x in vals:
        out = add(out, x)
    return out


def sq(x):
    return x[0]**2+x[1]**2


def finite_model(phase, sign, use_central_source, base_a):
    # G=D8 x C4; Gamma is the diagonal subgroup of G_infinity x G_finite.
    G = [(a, b, c) for a in range(4) for b in range(2) for c in range(4)]
    one = (0, 0, 0)

    def times(x, y):
        a, b, c = x
        d, e, f = y
        return ((a+(-1)**b*d) % 4, (b+e) % 2, (c+f) % 4)

    def inv(x):
        a, b, c = x
        return ((-(-1)**b*a) % 4, b, (-c) % 4)

    S = [one, (2, 0, 0) if use_central_source else (0, 1, 0)]
    K = [(0, b, c) for b in range(2) for c in range(4)]
    Kset = set(K)
    reps, used = [], set()
    for x in G:
        if x not in used:
            reps.append(x)
            used |= {times(t, x) for t in S}
    assert len(reps)*len(S) == len(G)

    # An exact two-dimensional unitary irreducible representation is
    # rotation^a reflection^b i^(phase*c); its e_1 coefficient is below.
    def coef(x):
        a, _, c = x
        return scale((1, 0, -1, 0)[a], ROOTS[(phase*c) % 4])

    def chi(x):
        assert x in Kset
        # Diagonal rational central invariance pairs inverse characters
        # at the two factors. Keeping the same character would give zero.
        return scale(sign**x[1], ROOTS[(-phase*x[2]) % 4])

    haar_inf, haar_fin = Q(3, 16), Q(5, 7)
    formal_degree = Q(2, len(G))/haar_inf
    volK = len(K)*haar_fin
    assert formal_degree == Q(1, 3) and volK == Q(40, 7)

    def p(x):
        return scale(formal_degree, conj(coef(x)))

    def e(x):
        return scale(1/volK, conj(chi(x))) if x in Kset else ZERO

    # Start with a point mass, apply the two original right projectors,
    # then the left diagonal-S average. All three operations commute.
    @lru_cache(None)
    def phi(x, y):
        z = total(mul(p(times(inv(x), times(t, base_a))),
                      e(times(inv(y), t))) for t in S)
        return scale(haar_inf*haar_fin/len(S), z)

    @lru_cache(None)
    def period(x, y):
        return total(phi(times(t, x), times(t, y)) for t in reps)

    P = {h: period(one, h) for h in G}
    assert any(z != ZERO for z in P.values())
    # Every rational return is kept; independently check quotient invariance.
    for x in G:
        for h in G:
            assert period(x, h) == P[times(inv(x), h)]

    finite_checks = infinite_checks = 0
    dropped_volume = dropped_degree = wrong_phase = False
    for h in G:
        re = scale(haar_fin, total(mul(e(t), P[times(h, t)]) for t in K))
        rp = scale(haar_inf, total(mul(p(t), P[times(inv(t), h)]) for t in G))
        assert re == rp == P[h]
        finite_checks += 1
        infinite_checks += 1
        if P[h] != ZERO:
            dropped_volume |= scale(volK, re) != P[h]
            dropped_degree |= scale(1/formal_degree, rp) != P[h]
            bad = scale(Q(1, len(K)), total(mul(chi(t), P[times(h, t)]) for t in K))
            wrong_phase |= bad != P[h]

    # The positive absolute-return majorant and Minkowski inequality are
    # checked on the same quotient and both original Haar scalars.
    A = {}
    for h in G:
        terms = [phi(t, times(t, h)) for t in reps]
        assert all(a == 0 or b == 0 for a, b in terms)
        A[h] = sum((abs(a)+abs(b) for a, b in terms), Q(0))
        assert sq(P[h]) <= A[h]**2
    pabs = {t: abs(p(t)[0])+abs(p(t)[1]) for t in G}
    assert all(p(t)[0] == 0 or p(t)[1] == 0 for t in G)
    B = {h: haar_inf*sum((pabs[t]*A[times(inv(t), h)] for t in G), Q(0)) for h in G}
    quotient_weight = haar_inf*haar_fin
    left_sq = quotient_weight*sum((v*v for v in B.values()), Q(0))
    p_l1 = haar_inf*sum(pabs.values(), Q(0))
    right_sq = p_l1**2*quotient_weight*sum((v*v for v in A.values()), Q(0))
    assert left_sq <= right_sq
    assert dropped_volume and dropped_degree and wrong_phase
    return {"group": "D8 x C4", "group_order": len(G), "source_order": len(S),
            "source_central": use_central_source, "level_order": len(K),
            "rational_return_cosets": len(reps), "infinite_central_phase": phase,
            "finite_central_phase": (-phase) % 4, "level_sign": sign,
            "base": list(base_a), "haar_inf_point_weight": str(haar_inf),
            "haar_fin_point_weight": str(haar_fin), "formal_degree": str(formal_degree),
            "level_volume": str(volK), "finite_projector_checks": finite_checks,
            "infinite_projector_checks": infinite_checks,
            "majorant_L2_bound_squares": [str(left_sq), str(right_sq)],
            "negative_controls": {"missing_level_volume": dropped_volume,
                                  "missing_formal_degree": dropped_degree,
                                  "wrong_finite_conjugation": wrong_phase}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    provenance.SOURCES = SOURCES
    sources = provenance.source_records(args.offline)
    models = [finite_model(phase, sign, central, base)
              for phase, sign, central, base in [
                  (1, -1, True, (1, 0, 0)),
                  (3, -1, True, (1, 1, 2)),
                  (1, 1, False, (0, 0, 0)),
                  (3, 1, False, (2, 1, 1)),
              ]]
    def hashes(paths):
        return [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
                for p in paths]
    cert = {
        "status": "PASS: exact pinned interfaces and finite projector/return diagnostics",
        "source_files": sources,
        "proof_files": hashes(PROOF_FILES),
        "dependencies": hashes(DEPENDENCIES),
        "exact_models": models,
        "classification": "closed actual InHH/PuLinear and finite-level normalization suppliers, not W08 closure",
        "proved_target_effect": "The actual Q_H=Re*Rph fixes every original period image, so its Gram target loss is zero.",
        "remaining": ["Any additional retained target projection", "Actual integral/metric arithmetic chain dictionary",
                      "Uniform positive-trace budget and normalized weighted seed moment"],
        "conventional_analytic_proof": "The existing positive Poincare L2 majorant and p in L1 justify every rational-return/convolution interchange by Tonelli and Minkowski.",
        "Lean_build_performed": False,
        "uniform_budget_proved": False,
        "node_counts_changed": False
    }
    out = ROOT/"certificates/global-gram-continuation-projectors.json"
    out.write_text(json.dumps(cert, indent=2)+"\n")
    print(json.dumps({"certificate": str(out.relative_to(ROOT)), "sources": len(sources),
                      "models": len(models),
                      "projector_equalities": sum(m["finite_projector_checks"]+m["infinite_projector_checks"] for m in models),
                      "all_negative_controls_detected": True,
                      "uniform_budget_proved": False}))


if __name__ == "__main__":
    main()
