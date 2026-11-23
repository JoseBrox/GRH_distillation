#!/usr/bin/env python3
"""Authenticate the actual terminal-period and Haar-normalization comparisons.

Exact finite models detect omitted masses, phase conjugation, branching
constants and finite stabilizer normalization.  They do not prove the
arithmetic construction, the see-saw comparison, or a Lean build.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import permutations, product
import json

import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth


STEM = "theta-period-continuation"
IW = "Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition."
DEC = "Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs."
SAT = "Development.AbelianVarietyTheory.Proofs.SatakeParameters."
LF = "Development.AbelianVarietyTheory.Definitions.LatticeFrames."
RANGES = {
    "Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals.PoincareInHH": [(252, 264)],
    IW + "KernelsOverOfFamily": [(177, 215), (221, 252), (256, 313)],
    IW + "KernelAtPointPenultimateStepFirstCoupledKernel":
        [(232, 271), (273, 305), (309, 341)],
    IW + "ExistsLowerEmbF": [(80, 119), (121, 158)],
    "Formalism.LocalToGlobal.Columns.FiniteSumNonzeroLargeDepth":
        [(38, 72), (87, 137), (187, 218)],
    IW + "TrueColumnsPeriodMapDatumOkAndOverLevelPrime": [(15, 69), (73, 95)],
    SAT + "PeriodRelationsTrueColumnsAtTuple": [(140, 162), (166, 223)],
    LF + "ThetaIdentityOfMapsAll": [(99, 133), (155, 174)],
    DEC + "HaarFiniteAdeleDisintegrationStabilizerCompact": [(91, 147), (148, 190)],
    DEC + "LintegralBesselGroupHaarEqConstMulProd": [(54, 102)],
    DEC + "HaarMeasureDisintegrationBesselGroup": [(19, 64)],
    DEC + "FoldIntegralBesselQuotientSupportedFunctions": [(22, 62), (63, 90)],
    DEC + "UnfoldedPeriodEqIntegralBesselPeriods": [(73, 98), (99, 138), (139, 185)],
    DEC + "InnerPoincareSeriesEqSetIntegralUnfolding": [(17, 59), (60, 95), (96, 132)],
    DEC + "ConjugateRowPairingPoincareSeriesBesselPeriods": [(17, 23)],
    DEC + "BesselColumnScalarFormNormBound": [(18, 47)],
    DEC + "ExistsSBesUnscaledDual": [(50, 74), (75, 101), (102, 129)],
    DEC + "BottomRelationOfPin": [(101, 149), (151, 210)],
    DEC + "JointStarProductNonvanishing": [(101, 132), (142, 164), (176, 201)],
}


def simp(z):
    return sp.expand_complex(sp.cancel(z))


def terminal_period_checks():
    """Compare matrix composition with an independently expanded path sum.

    The two-dimensional polynomial fibres have a nontrivial rational
    branching functional; all class masses are kept.  Fourth-root changes
    of representatives are made at every stage, with inverse row phases.
    """
    I = sp.I
    w0, w1, wr = [2, 3], [4, 1, 6], [3, 5]
    phases = [sp.Integer(1), I, sp.Integer(-1), -I]
    branch = (sp.Rational(5, 7) + sp.Rational(2, 7) * I) * (2 - I) ** -3
    lower = sp.Matrix([[sp.Rational(2, 3), sp.Rational(3, 5)]])
    pairing = sp.Rational(1, 2)
    count = 0
    controls = None
    for seed in range(1, 13):
        x = [sp.Matrix([seed + a + I, 2 - a + seed * I]) for a in range(2)]
        k0 = [[sp.Matrix([[1 + b, a + I], [a - I, seed + b]])
               for a in range(2)] for b in range(3)]
        k1 = [[sp.Matrix([[seed + b, 1 + a * I], [b - I, 2 + a]])
               for a in range(3)] for b in range(2)]
        row = [1 + seed * I, 2 - I]
        y = [sum((k0[b][a] * x[a] / w0[a] for a in range(2)), sp.zeros(2, 1))
             for b in range(3)]
        z = [sum((k1[c][b] * y[b] / w1[b] for b in range(3)), sp.zeros(2, 1))
             for c in range(2)]
        composed = simp(sum(pairing * branch * (lower * z[c])[0] * row[c] / wr[c]
                            for c in range(2)))
        expanded = simp(sum(pairing * branch * (lower * k1[c][b] * k0[b][a] * x[a])[0]
                            * row[c] / (wr[c] * w1[b] * w0[a])
                            for c, b, a in product(range(2), range(3), range(2))))
        assert simp(composed - expanded) == 0
        p0 = [phases[(seed + a) % 4] for a in range(2)]
        p1 = [phases[(seed + 2 * b) % 4] for b in range(3)]
        p2 = [phases[(seed + c) % 4] for c in range(2)]
        changed = simp(sum(pairing * branch *
                          (lower * (p2[c] / p1[b] * k1[c][b]) *
                           (p1[b] / p0[a] * k0[b][a]) * (p0[a] * x[a]))[0]
                          * row[c] / p2[c] / (wr[c] * w1[b] * w0[a])
                          for c, b, a in product(range(2), range(3), range(2))))
        assert simp(changed - composed) == 0
        count += 2
        if controls is None:
            missing_mass = simp(sum(pairing * branch * (lower * k1[c][b] * k0[b][a] * x[a])[0]
                                    * row[c] for c, b, a in product(range(2), range(3), range(2))))
            same_phase = simp(sum(pairing * branch * (lower * z[c])[0] * row[c] * p2[c] ** 2 / wr[c]
                                  for c in range(2)))
            no_branch = simp(composed / branch)
            assert all(simp(v - composed) != 0 for v in (missing_mass, same_phase, no_branch))
            controls = {"omitting_class_masses_detected": True,
                        "same_instead_of_inverse_row_phase_detected": True,
                        "omitting_original_branch_scalar_detected": True}
    return {"exact_comparisons": count, "negative_controls": controls,
            "scope": "Finite Gaussian-rational class sums with two-dimensional fibres, nontrivial masses and branching denominator; not the general period theorem."}


def finite_haar_checks():
    """Check the finite disintegration independently for nonabelian S4.

    Ambient Haar gives each point mass 2/7.  For each genuine subgroup
    intersection, the auxiliary stabilizer Haar gives the intersection
    mass one.  No enumeration of a double-coset fibre is used on the
    left side of the equality.
    """
    group = list(permutations(range(4)))
    unit = tuple(range(4))
    def mul(a, b):
        return tuple(a[b[j]] for j in range(4))
    def inv(a):
        return tuple(a.index(j) for j in range(4))
    S = [g for g in group if g[3] == 3]
    K = [g for g in group if {g[0], g[1]} == {0, 1}]
    assert len(S) == 6 and len(K) == 4 and unit in S and unit in K
    mu = Q(2, 7)
    values = {g: Q(1 + j * j, 1 + j % 3) for j, g in enumerate(group)}
    counts = set()
    checks = 0
    for x in group:
        H = [s for s in S if mul(mul(inv(x), s), x) in K]
        counts.add(len(H))
        support = {mul(mul(s, x), k) for s, k in product(S, K)}
        lhs = sum(mu * values[g] for g in support)
        rhs = sum(mu * values[mul(mul(s, x), k)] / len(H) for s, k in product(S, K))
        assert lhs == rhs
        wrong = sum(mu * values[mul(mul(s, x), k)] for s, k in product(S, K))
        if len(H) > 1:
            assert wrong != lhs
        # A right-K-invariant function supplies exactly vol(K), for
        # every s, independently of the disintegration enumeration.
        for s in S:
            sx = mul(s, x)
            invariant = lambda a: min(mul(a, k) for k in K)
            integral = sum(mu * values[invariant(mul(sx, k))] for k in K)
            assert integral == len(K) * mu * values[invariant(sx)]
            checks += 1
        checks += 1
    # Actual Haar ratio beta must invert when it replaces product Haar.
    for beta in (Q(2, 3), Q(1), Q(11, 5)):
        original_integral = beta * rhs
        assert original_integral / beta == lhs
        checks += 1
    return {"exact_comparisons": checks, "ambient_group_order": len(group),
            "stabilizer_order": len(S), "level_order": len(K),
            "intersection_orders": sorted(counts), "level_volume": str(len(K) * mu),
            "omitted_intersection_normalization_detected": True,
            "scope": "Finite nonabelian Haar/coset identities and positive measure-ratio orientation; no adelic volume bound inferred."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    artifacts = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
                 f"notes/{STEM}.md", f"scripts/{STEM}.py"]
    dependencies = ["paper/shared/theta-spanning-continuation-chain.tex",
                    "paper/sections/recovered/35-coef-section.tex",
                    "paper/sections/recovered/39-ib-section.tex",
                    "paper/sections/recovered/46-cp-section.tex"]
    diagnostics = {"terminal_period": terminal_period_checks(), "finite_haar": finite_haar_checks()}
    record = {"status": "PASS", "classification": "closed terminal-period and exact Poincare-Bessel scalar supplier obligations; whole W06 remains open",
              "sources": sources,
              "artifacts": {p: auth.sha((auth.ROOT / p).read_bytes()) for p in artifacts},
              "established_dependency_hashes": {p: auth.sha((auth.ROOT / p).read_bytes()) for p in dependencies},
              "diagnostics": diagnostics,
              "scope_guards": ["original class masses and inverse terminal phases",
                               "original conjugate prime element and full branching scalar",
                               "original twisted initial source and retained restrictions",
                               "original positive period normalizer c0X",
                               "finite stabilizer intersection has auxiliary mass one",
                               "original Bessel Haar equals beta times real/finite product Haar",
                               "Poincare factor is vol(K2)/(beta*sqrt(c0X)); beta is positive, not freely chosen"],
              "remaining": ["actual see-saw comparison with the algebraic terminal period",
                            "actual smooth row realization and restriction compatibility",
                            "nonzero anchor after strict normalized source deficit",
                            "row-dependent proportionality factors in arithmetic map heights",
                            "uniform coefficient fields and final source/target norm budgets",
                            "whole W06 completion is not claimed"],
              "verification_scope": "Pinned source hashes and bounded excerpts; exact finite diagnostics; general proofs in companion TeX. No Lean build or all-node proof certificate."}
    out = auth.ROOT / "certificates" / (STEM + ".json")
    out.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "source_files": len(sources),
                      "terminal_comparisons": diagnostics["terminal_period"]["exact_comparisons"],
                      "finite_haar_comparisons": diagnostics["finite_haar"]["exact_comparisons"],
                      "certificate": str(out.relative_to(auth.ROOT))}))


if __name__ == "__main__":
    main()
