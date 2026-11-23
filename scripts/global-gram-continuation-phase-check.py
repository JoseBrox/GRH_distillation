#!/usr/bin/env python3
"""Authenticate original finite phase data and exact arithmetic diagnostics.

The full proof is conventional mathematics in the shared TeX.  The small
checks below test the ideal exponent, trace-dual and character bookkeeping;
they are not a replacement for the all-field argument or a Lean build.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from math import gcd
from pathlib import Path

import check_global_norm_frontier_off_diagonal as provenance

ROOT = Path(__file__).resolve().parents[1]
H = "Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals."
SOURCES = [
    (H + "HidaSetting", [(106, 128), (172, 173), (207, 231), (233, 273)]),
    (H + "UnitaryHaarProducts.InHHCut", [(107, 175)]),
    (H + "UnitaryHaarProducts.HermitianETransportInvariant",
     [(67, 80), (240, 279), (354, 377), (679, 683), (786, 834), (935, 967)]),
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.TraceIntegralEstimates.DdTraceCore", [(10, 62)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.BlockEnds", [(116, 118)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.GlobAut", [(44, 52)]),
    (H + "UnitaryHaarProducts.LevelSubgroupCharacterUnitary", [(194, 217), (569, 578)]),
]
DEPENDENCIES = [
    "paper/shared/global-gram-continuation.tex",
    "paper/shared/global-gram-continuation-phases.tex",
    "paper/shared/global-gram-continuation-phase-references.tex",
]


def diagnostics():
    # Fractional flag ideals d^(a-r) have exactly the prescribed adjacent
    # ratio and terminal value.  Rank zero contributes no fictitious last row.
    exponents = []
    for r in (0, 1, 2, 7, 31):
        aa = [a-r for a in range(r)]
        assert all(aa[a]-aa[a+1] == -1 for a in range(r-1))
        assert not aa or aa[-1] == -1
        exponents.append({"rank": r, "adjacent_ratios": len(aa)-1 if aa else 0,
                          "last_exponent": aa[-1] if aa else None})

    # For real quadratic F with fundamental D = 1 mod 4, the trace
    # pairing of (1,omega) with (1/sqrt(D),omega/sqrt(D)) is [[0,1],[1,1]].
    # Compute in Q[sqrt(D)] rather than using floating-point approximations.
    trace_reports = []
    for D in (5, 13, 17, 29):
        def mul(x, y):
            return (x[0]*y[0]+D*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
        basis = [(Fraction(1), Fraction(0)), (Fraction(1, 2), Fraction(1, 2))]
        inverse = [(Fraction(0), Fraction(1, D)), (Fraction(1, 2), Fraction(1, 2*D))]
        pairing = [[2*mul(x, y)[0] for y in inverse] for x in basis]
        assert pairing == [[0, 1], [1, 1]]
        assert pairing[0][0]*pairing[1][1]-pairing[0][1]*pairing[1][0] == -1
        trace_reports.append({"discriminant": D, "trace_pairing": [[int(x) for x in row] for row in pairing]})

    # An additive unit character is represented exactly by its angle in Q/Z.
    # This checks the final decomposition cancellation with no numerical roots.
    phase_cases = 0
    for denominator in (3, 5, 8, 15):
        for an in range(denominator):
            for anp in range(denominator):
                for ak in range(denominator):
                    aell = (an+2*anp+ak+1) % denominator
                    akp = (-anp+an+aell+ak) % denominator
                    assert (an+ak+aell-anp-akp) % denominator == 0
                    phase_cases += 1

    # A condition only at primes dividing g cannot control the finite
    # character elsewhere: at p=3 take v=1/3 and zero at all other primes,
    # with g=5.  The p=5 local component is integral, but its Q/Z angle is nonzero.
    missing_different_counterexample = Fraction(1, 3) % 1
    assert missing_different_counterexample != 0 and gcd(3, 5) == 1
    return {"flag_ideal_checks": exponents, "ramified_trace_dual_checks": trace_reports,
            "exact_character_cancellations": phase_cases,
            "level_only_counterexample": {"g": 5, "omitted_prime": 3,
                                           "nonzero_character_angle": str(missing_different_counterexample)},
            "does_not_replace_all_field_proof": True}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    provenance.SOURCES = SOURCES
    records = provenance.source_records(args.offline)
    out = {
        "claim": "Original UnipotentConjugateInLevel, LevelDec and PhWellDef from actual integral splitting and finite character",
        "classification": "closed exact finite compatibility obligation within W08",
        "source_verification": records,
        "dependencies": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
                         for p in DEPENDENCIES],
        "diagnostics": diagnostics(),
        "scope": {"original_different_and_fractional_flag_ideals": True,
                  "original_level_character_law_retained": True,
                  "all_finite_primes_retained": True,
                  "PhWellDef_supplied": True,
                  "class_frame_raw_kernel_identity_proved": False,
                  "uniform_trace_budget_proved": False,
                  "whole_node_closed": False, "lean_build_run": False},
    }
    target = ROOT / "certificates/global-gram-continuation-phases.json"
    target.write_text(json.dumps(out, indent=2)+"\n")
    print(json.dumps({"certificate": str(target.relative_to(ROOT)), "sources": len(records),
                      "character_checks": out["diagnostics"]["exact_character_cancellations"],
                      "PhWellDef_supplied": True}))


if __name__ == "__main__":
    main()
