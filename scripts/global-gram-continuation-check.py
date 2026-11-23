#!/usr/bin/env python3
"""Authenticate the arithmetic folding suppliers and test exact conventions.

The adelic and all-dimension proofs are in the accompanying TeX.
The finite-group diagnostic checks the noncommutative double-coset
orientation, stabilizer quotient, and unchanged Haar normalization.
It is not evidence for a uniform arithmetic estimate or a Lean build.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp
import check_global_norm_frontier_off_diagonal as provenance

ROOT = Path(__file__).resolve().parents[1]
STEM = "global-gram-continuation"
H = "Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals."
L = "Formalism.LocalToGlobal.SiegelLatticeTheory.ClosedLocalOrbits.GaugeLatticeShifts."
SOURCES = [
    (H + "HidaSetting", [(179, 231), (275, 321)]),
    (H + "WuDecay", [(18, 43)]),
    (H + "PoincareInHH", [(144, 177), (179, 199)]),
    (H + "UnitaryHaarProducts.InHHCut", [(315, 339)]),
    (H + "UnitaryHaarProducts.IUnfold", [(123, 177), (183, 202), (369, 408)]),
    (H + "UnitaryHaarProducts.SCompact", [(323, 370), (402, 452)]),
    (H + "FoldBound", [(10, 32), (65, 120)]),
    (H + "PoincareSeriesSquareIntegrable", [(40, 86)]),
    (H + "UnitaryHaarProducts.HermitianETransportInvariant",
     [(264, 279), (935, 967), (1029, 1057)]),
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.ClosedLocalOrbits."
     "GaugeLatticeShifts.DoubleCosetSingleUnfolding", [(31, 75), (435, 447)]),
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.FlagStabilizerTensors."
     "RootLatticeThresholds.RowFormAllOf", [(108, 182)]),
    (L + "SlabCountPfSteps", [(16, 22)]),
    (L + "SlabCountPfLeviSteps", [(16, 59), (105, 138)]),
    (L + "SlabCountPfLeviPos", [(128, 161)]),
]
DEPENDENCIES = [
    "paper/shared/global-norm-frontier-seed-decay.tex",
    "paper/shared/global-gram-continuation.tex",
    "paper/shared/global-gram-continuation-references.tex",
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def subgroup(gens, group, mul):
    out = {group[0]}
    while True:
        nxt = out | {mul(x, y) for x in out for y in gens}
        if nxt == out:
            return out
        out = nxt


def transversal(group, sub, mul):
    unused = set(group)
    ans = []
    for g in group:
        if g in unused:
            ans.append(g)
            unused.difference_update(mul(s, g) for s in sub)
    assert not unused
    return ans


def double_reps(group, left, right, mul):
    unused = set(group)
    ans = []
    for g in group:
        if g in unused:
            ans.append(g)
            unused.difference_update(mul(mul(s, g), t) for s in left for t in right)
    assert not unused
    return ans


def diagnostic():
    checked = 0
    bad_conjugation_detected = False
    bad_stabilizer_detected = False
    bad_haar_detected = False
    reports = []
    for order in (3, 4, 5):
        group = list(itertools.product(range(order), range(2)))
        identity = (0, 0)

        def mul(x, y):
            return ((x[0] + (-1)**x[1] * y[0]) % order, (x[1] + y[1]) % 2)

        def inv(x):
            return next(y for y in group if mul(x, y) == identity)

        for sg, tg in (((0, 1), (1, 1)), ((0, 1), (0, 1)), ((1, 0), (0, 1))):
            S = subgroup([sg], group, mul)
            T = subgroup([tg], group, mul)
            D, E = transversal(group, S, mul), transversal(group, T, mul)
            R = double_reps(group, S, T, mul)
            f, h = {}, {}
            for j, d in enumerate(D):
                for s in S:
                    f[mul(s, d)] = sp.Rational(2*j+1, j+2) + sp.I*sp.Rational(j+3, 2*j+1)
            for j, e in enumerate(E):
                for t in T:
                    h[mul(t, e)] = sp.Rational(j+2, 3*j+1) - sp.I*sp.Rational(2*j+1, j+4)
            Pf = {x: sp.expand(sum(f[mul(d, x)] for d in D)) for x in group}
            Ph = {x: sp.expand(sum(h[mul(e, x)] for e in E)) for x in group}
            assert len(set(Pf.values())) == len(set(Ph.values())) == 1
            # Ambient Haar measure gives each point mass c.  Gamma=G,
            # so the fundamental domain has one point, of mass c.
            for c in (sp.Rational(1, len(group)), sp.Rational(5, 7)):
                lhs = sp.expand(c * Pf[identity] * sp.conjugate(Ph[identity]))
                rhs = 0
                wrong = 0
                wrong_quotient = 0
                for r in R:
                    stabilizer = {s for s in S if mul(mul(inv(r), s), r) in T}
                    Fs = transversal(group, stabilizer, mul)
                    rhs += c * sum(f[x]*sp.conjugate(h[mul(inv(r), x)]) for x in Fs)
                    wrong += c * sum(f[x]*h[mul(inv(r), x)] for x in Fs)
                    wrong_quotient += c * sum(f[x]*sp.conjugate(h[mul(inv(r), x)]) for x in group)
                assert sp.simplify(lhs-rhs) == 0
                bad_conjugation_detected |= sp.simplify(lhs-wrong) != 0
                bad_stabilizer_detected |= sp.simplify(lhs-wrong_quotient) != 0
                bad_haar_detected |= sp.simplify(lhs-rhs/c) != 0
                # Test the return-set injection used in the actual proof.
                for Om in ({identity}, {identity, (0, 1)}, set(group)):
                    for x in group:
                        for y in group:
                            ret = [z for z in group if mul(mul(inv(x), z), y) in Om]
                            if not ret:
                                continue
                            z0 = ret[0]
                            image = {mul(z, inv(z0)) for z in ret}
                            target = {mul(mul(mul(x, a), inv(b)), inv(x)) for a in Om for b in Om}
                            assert len(image) == len(ret) and image <= target
                checked += 1
            reports.append({"ambient_group": f"dihedral order {2*order}",
                            "subgroup_sizes": [len(S), len(T)],
                            "double_cosets": len(R)})
    assert bad_conjugation_detected and bad_stabilizer_detected and bad_haar_detected
    return {"exact_gram_cases": checked, "groups": reports,
            "wrong_conjugation_rejected": bad_conjugation_detected,
            "missing_stabilizer_quotient_rejected": bad_stabilizer_detected,
            "discarded_Haar_scalar_rejected": bad_haar_detected,
            "return_injection_checked": True,
            "diagnostics_replace_no_adelic_proof": True}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    provenance.SOURCES = SOURCES
    records = provenance.source_records(args.offline)
    out = {
        "claim": "Actual arithmetic MultPoly, IUnfold and LeviFinC suppliers; exact scalar Poincare Gram identity under the retained original PhWellDef premise",
        "classification": "closed supplier obligations within W08",
        "source_verification": records,
        "dependencies": [{"path": p, "sha256": sha((ROOT/p).read_bytes())} for p in DEPENDENCIES],
        "diagnostics": diagnostic(),
        "proof_scope": {
            "all_dimensions_and_field_degrees": True,
            "actual_multiplicity_exponent": "4 n^2 in the product of original local operator norms",
            "constants_uniform_in_setting": False,
            "PhWellDef_independently_discharged_here": False,
            "LeviFinC_discharged_here": True,
            "OOLintSumC_or_SigRowsC_discharged_here": False,
            "uniform_positive_trace_budget_proved": False,
            "whole_node_closed": False,
            "lean_build_run": False,
        },
    }
    target = ROOT / "certificates" / (STEM + ".json")
    target.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({"certificate": str(target.relative_to(ROOT)),
                      "verified_sources": len(records),
                      "exact_gram_cases": out["diagnostics"]["exact_gram_cases"],
                      "uniform_budget_proved": False}))


if __name__ == "__main__":
    main()
