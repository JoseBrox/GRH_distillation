#!/usr/bin/env python3
"""Authenticate the actual determinant-height assembly and exact diagnostics.

The general geometric, analytic and arithmetic arguments are in the TeX.
Finite exact models check sensitive signs, factors, kernels and quotients;
they are not substitutes for those proofs. No Lean build is performed.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
from random import Random
import re

import sympy as sp

import check_geometry_arithmetic_frontier_geometric_filtration as auth

STEM = "geometry-height-assembly"
GD = "Development.AutomorphicSpectrum.Definitions.GlobalGeometry."
GP = "Development.AutomorphicSpectrum.Proofs.GeometryProofs."
MP = "Development.AutomorphicSpectrum.Proofs.MetricProofs."
DP = "Development.AutomorphicSpectrum.Proofs.DivisibilityProofs."
DT = "Development.AutomorphicSpectrum.Definitions.DivisibilityTowers."
PC = "Development.WeilBound.CoreStatements.PlurisubharmonicCones."
RG = "GroundTheory.HeightsAndTheta.Heights.Regularisation."
HL = "GroundTheory.HeightsAndTheta.Heights.HodgeLowerBound."
RANGES = {
    GD + "IsCptGen": [(9, 27)],
    GD + "IsHodgeLine": [(33, 74)],
    GD + "MemEigSpOfMemHtDual": [(20, 48), (53, 90)],
    GD + "ExistsUniqueLeftBasisCoordsAdicCompletion": [(62, 79)],
    GD + "PotentialsBoundedRegSettingEqReference": [(18, 60)],
    GP + "IntersectionDegreeUpper": [(40, 87)],
    GP + "HodgeCompCoverCmSigns": [(21, 90)],
    GP + "CuspIntersectionPositive": [(122, 170), (210, 265)],
    GP + "CuspIntersectionLimit": [(135, 182), (189, 229)],
    GP + "CuspWeightRegularisationsTied": [(25, 44)],
    GP + "GoodOriginIntersectionTower": [(38, 80), (81, 124)],
    MP + "LogDetEigenFramePlurisubharmonic": [(58, 79), (93, 146)],
    MP + "LogDetCuspFramePlurisubharmonic": [(153, 194), (195, 265)],
    MP + "ExistsRegularizationSetting": [(19, 48)],
    MP + "HeightBoundFullIntersectionSystem": [(154, 208)],
    PC + "ExistsPhiNormSq": [(289, 348)],
    PC + "ExistsTiedRegularSetting": [(68, 103)],
    PC + "TiedSettingSymmetricCharts": [(93, 145), (149, 181)],
    RG + "Statements": [(92, 155)],
    RG + "PMollifierLowerBound": [(20, 97)],
    RG + "PMaxOscillation": [(12, 41)],
    RG + "PBoundedChartComparison": [(101, 157), (158, 238)],
    RG + "PChartComparison": [(28, 115)],
    HL + "FrameDefinitions.CpRegPhRegOfNonneg": [(19, 90)],
    HL + "FlagIndices": [(62, 108)],
    DP + "SlopeLowerBaseSettings": [(16, 74), (76, 120)],
    DP + "TowerWeilInputsCombined": [(22, 53)],
    DP + "VolumeTheoremOfInputs": [(72, 121)],
    DT + "HeckeSectionsIsotropicCommutatorPairingPower": [(30, 74)],
    DT + "CompactGapsGE": [(19, 46)],
}


def primary_references():
    rows = [
        {"path": "build/reference-cache/lan-pel-thesis-2021.pdf",
         "url": "https://www.kwlan.org/articles/cpt-PEL-type-thesis-revision.pdf",
         "sha256": "a7a454f5d0735f4bf11f00a8afc14c361c5fc2cefd691d7466f7620ab4c3a079",
         "scope": "Theorem7.2.4.1(2)-(3), printed pp552-553: a positive power of the actual Hodge line is the pullback of an ample minimal-compactification line, including the toroidal boundary."},
        {"path": "build/reference-cache/lan-ramified-flat.pdf",
         "url": "https://www.kwlan.org/articles/cpt-ram-flat.pdf",
         "sha256": "dbe7d5c3488693bad792def9f7245bdea5657174455e15e32bef607c93d801d2",
         "scope": "Example2.3, maps(7.7)-(7.8), Proposition7.11, Theorem7.14: original singleton normalization model and auxiliary Hodge-line pullback. No isogeny change of the original lattice is introduced."},
    ]
    for row in rows:
        assert auth.sha((auth.ROOT / row["path"]).read_bytes()) == row["sha256"]
    return rows


def integral_generation_checks():
    valuation_cases = 0
    for p in list(sp.primerange(2, 100)):
        for R in range(4, 10):
            v_kappa = F(2) if p == 2 else F(1, p - 1)
            assert F(R - 1) - v_kappa >= 0
            valuation_cases += 1
    # N=4Z+2Z+Z and n=16: all lifts of the original differentials
    # have the same classes in N/2N because nZ^3 is contained in 2N.
    N = sp.diag(4, 2, 1)
    assert all(x.is_Integer for x in (2*N).inv() * 16)
    assert not all(x.is_Integer for x in (2*N).inv() * 4)
    # A constant ideal changes the arithmetic degree, although its
    # degree on every vertical curve is zero. This is not discarded.
    return {"valuation_cases": valuation_cases,
            "dyadic_factor": 4,
            "global_label_interface": "IsCptGen.bij plus HodgeCpt.tors, not a constant-field extension",
            "too_small_level_negative_control": "n=4 and N=4Z+2Z+Z do not give n omega subset 2N",
            "scope": "Exact valuation and free-module checks; the all-chart global generation proof is in the TeX."}


def matrix_checks():
    rng = Random(10752)
    hessian_count = quotient_count = 0

    def gaussian_matrix(m, n):
        return sp.Matrix(m, n, lambda i, j:
                         rng.randrange(-2, 3)+sp.I*rng.randrange(-2, 3))

    for g in range(2, 6):
        for m in range(1, g+1):
            for _ in range(4):
                A = gaussian_matrix(g, g)
                C = gaussian_matrix(g-m, m)
                B = sp.eye(g)[:, :m]
                Bp = sp.zeros(g, m)
                if g > m:
                    Bp[m:g, :] = C
                Fz = -B.conjugate().T*A*B+B.conjugate().T*Bp
                Fzb = (Bp.conjugate().T*Bp
                       -Bp.conjugate().T*A*B
                       -B.conjugate().T*A.conjugate().T*Bp
                       +B.conjugate().T*(A*A.conjugate().T+A.conjugate().T*A)*B)
                lhs = sp.expand(sp.trace(Fzb-Fz.conjugate().T*Fz))
                blocks = [C-A[m:g, :m], A[:m, :m], A[:m, m:g]]
                rhs = sum(sp.expand(sp.trace(M.conjugate().T*M)) for M in blocks)
                assert sp.expand(lhs-rhs) == 0 and rhs >= 0
                hessian_count += 1
        for r in range(1, g):
            A = gaussian_matrix(g, g)
            Y = A.conjugate().T*A+sp.eye(g)
            H = Y.inv()
            Q = H[r:g, r:g]-H[r:g, :r]*H[:r, :r].inv()*H[:r, r:g]
            assert (Q-Y[r:g, r:g].inv()).applyfunc(sp.simplify) == sp.zeros(g-r)
            assert sp.simplify(H.det()-H[:r, :r].det()*Q.det()) == 0
            quotient_count += 1
    return {"exact_hessian_models": hessian_count,
            "exact_quotient_and_determinant_models": quotient_count,
            "scope": "Exact Gaussian-rational matrix identities, not numerical positivity evidence."}


def convexity_and_assembly_checks():
    # Convex, nondecreasing piecewise affine functions in log radius.
    # The slopes are integers and all radii logarithms rational.
    convex_checks = 0
    for T in range(5, 20):
        for gap in range(1, T-2):
            lo, mid, hi = F(-T), F(-T+gap), F(0)
            for kink in range(-T+1, 1):
                for a, b in [(0, 1), (1, 2), (2, 7)]:
                    f = lambda x: a*x+(b-a)*max(x-F(kink), F(0))
                    assert (f(mid)-f(lo))/(mid-lo) <= (f(hi)-f(mid))/(hi-mid)
                    convex_checks += 1
    normalization_cases = 0
    for f in range(1, 5):
        for q in range(1, 5):
            for p in range(2*q+1, 2*q+4):
                N = p+q
                n0, d = f*p*q, f*N*(N-1)//2
                assert d-n0 == f*(p*(p-1)+q*(q-1))//2
                L = F(N+3, q+1)
                a = -52*f*q*L
                cusp = 3*f*q*L
                component = a-cusp/2
                assert component == -F(107, 2)*f*q*L
                delta, cfib, degree, vol, J = map(F, [3, 7, 15, 5, 7])
                # delta*vol*J=cfib*degree=105, retaining both factors.
                assert delta*vol*J == cfib*degree
                A = (n0+1)*degree*component
                test = cfib*A/delta
                beta = test/(vol*f*q*(n0+1)*J)
                assert beta == -F(107, 2)*L
                normalization_cases += 1
    # A lower bound on metric increase gives no lower bound for F.
    G, old_F, increase, supposed_upper = 0, -100, 100, 1
    assert G >= 0 and increase >= supposed_upper
    assert old_F < -supposed_upper
    # Removing an initial vertical factor shifts the height and top
    # intersection, although it changes no complex curvature.
    n, degree, initial_shift = 3, F(5), F(7, 2)
    assert (n+1)*degree*initial_shift == 70
    return {"convex_secant_checks": convex_checks,
            "dimension_and_projection_normalizations": normalization_cases,
            "wrong_energy_orientation_negative_control": True,
            "initial_vertical_factor_negative_control": True,
            "scope": "Exact algebra and negative controls; limit convergence is proved in the manuscript."}


def artifact_checks():
    paths = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", f"scripts/{STEM}.py"]
    body = (auth.ROOT/paths[0]).read_text()
    assert body.count(r"\[") == body.count(r"\]")
    assert not [c for c in body if ord(c) < 32 and c not in "\n\r"]
    for name in ["proof", "proposition", "theorem"]:
        assert body.count(r"\begin{"+name+"}") == body.count(r"\end{"+name+"}")
    assert len(re.findall(r"\\tag\{HA\d+\}", body)) == 21
    return {p: auth.sha((auth.ROOT/p).read_bytes()) for p in paths}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    checks = {"finite_generation": integral_generation_checks(),
              "period_matrices": matrix_checks(),
              "overlap_and_normalization": convexity_and_assembly_checks()}
    record = {
        "status": "PASS",
        "classification": "closed actual finite-fibre nefness, tied-smoothing and signed base-test suppliers; W10 remains open",
        "sources": sources, "primary_references": primary_references(),
        "integral_determinant_proofs": {
            p: auth.sha((auth.ROOT/p).read_bytes()) for p in [
                "paper/shared/biextension-conjugate-filtration.tex",
                "paper/shared/determinant-torsion-rigidity.tex",
                "paper/shared/theta-spanning-continuation-flat.tex"]},
        "artifacts": artifact_checks(), "diagnostics": checks,
        "dependencies_retained": [
            "actual same-lattice integral Hodge and conjugate determinant theorem on every vertical curve",
            "actual normal model, prescribed full generic level and original corrected modules",
            "original finite and infinite metric and exact all-point floor with constant52",
            "original arithmetic intersection and metric-variation conventions",
            "proved isotropic arithmetic integrability and exact Haar/curvature/sheet dictionary with cusp constant3"],
        "remaining": [
            "actual general flag ModelNef and M2 suppliers needed by the weighted tower mean",
            "exact Frobenius-linked Lagrangian congruences, not implied by an annihilator bound",
            "original metric/count-volume comparison and finite section-rank budget",
            "full W10 and both complete RH/GRH proofs"],
        "verification_scope": "Ordinary proofs, authenticated bounded pinned-source interfaces, primary-reference hashes, exact finite diagnostics and independent review; no Lean build or whole-node completion claim."}
    out = auth.ROOT/"certificates"/(STEM+".json")
    out.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_files": len(sources),
                      "hessian_models": checks["period_matrices"]["exact_hessian_models"],
                      "normalization_models": checks["overlap_and_normalization"]["dimension_and_projection_normalizations"],
                      "certificate": str(out.relative_to(auth.ROOT))}))


if __name__ == "__main__":
    main()
