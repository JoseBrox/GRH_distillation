#!/usr/bin/env python3
"""Authenticate the quotient-mass proof and check exact normalization models."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import subprocess

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PRIOR = "1d6b784075cf61ce5d6b2f1b03cb0196c64130ab"
REPO = "jsmorph/rh"
STEM = "global-norm-frontier-quotient-mass"
F = "Development.AbelianVarietyTheory.Proofs.FlagMeasures."
SOURCES = [
    ("Formalism.HermitianCurvature.BesselNonvanishingReduction", [(20, 54)]),
    ("Formalism.PeriodIntegrals.BesselMapUniq", [(32, 46)]),
    ("Formalism.PeriodIntegrals.BesselPeriodGGP", [(59, 83)]),
    ("Development.AbelianVarietyTheory.Definitions.Jets.SumIoPrAlt",
     [(29, 37), (123, 144)]),
    ("Development.AbelianVarietyTheory.Definitions.SemilocalFrames.MatrixOfBesselTwoSidedAction",
     [(40, 75)]),
    (F + "BesselOpNormPowerIntegralLtTopClosedSubgroup",
     [(56, 104), (197, 237)]),
    (F + "BesselSubgroupsClosedUnitaryWCompact", [(16, 33)]),
    (F + "UnimodularBesselSubgroupsUWN", [(79, 100)]),
    (F + "BesselFormCoeffProductFubiniIntegrable", [(24, 47), (72, 110)]),
    ("CompanionTheory.AutomorphicTheory.PieriRules.ThetaBesselIsometries.GapCoefficientDerivativeBound",
     [(35, 58)]),
    ("CompanionTheory.AutomorphicTheory.PieriRules.ThetaBesselIsometries.FamilySetupBesselGrowth",
     [(31, 60)]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert (atlas["repository"], atlas["commit"]) == (REPO, REV)
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        path = "lean/src/"+module.replace(".", "/")+".lean"
        rec = inspect_file({"repository": REPO, "commit": REV,
                            "path": path, "git_blob_sha1": blobs[module]}, offline)
        assert rec["matches_pinned_blob"]
        data = (ROOT/"build/source-cache"/REPO/REV/path).read_bytes()
        lines = data.splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpt = b"".join(lines[lo-1:hi])
            assert len(excerpt) <= 12_288
            excerpts.append({"lines": [lo, hi], "bytes": len(excerpt),
                             "sha256": sha(excerpt)})
        records.append({"module": module,
                        **{key: rec[key] for key in
                           ["repository", "commit", "path", "bytes", "sha256",
                            "git_blob_sha1", "matches_pinned_blob"]},
                        "excerpts": excerpts})
    path = "paper/sections/recovered/73-amb-section.tex"
    data = subprocess.check_output(["git", "show", f"{PRIOR}:{path}"], cwd=ROOT)
    excerpt = b"".join(data.splitlines(keepends=True)[784:823])
    prior = {"repository": "JoseBrox/GRH_distillation", "commit": PRIOR,
             "path": path, "sha256": sha(data), "lines": [785, 823],
             "excerpt_sha256": sha(excerpt)}
    return records, prior


def scalar(matrix):
    return sp.simplify(matrix[0])


def equal(a, b):
    if isinstance(a, sp.MatrixBase):
        return all(sp.simplify(x) == 0 for x in a-b)
    return sp.simplify(a-b) == 0


def finite_symmetric_group_models():
    matrices = []
    for permutation in itertools.permutations(range(3)):
        m = sp.zeros(3)
        for j, i in enumerate(permutation):
            m[i, j] = 1
        matrices.append(m)
    ident = sp.eye(3)
    switch = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    subgroup = [ident, switch]
    reps, covered = [], set()
    for g in matrices:
        if tuple(g) not in covered:
            reps.append(g)
            covered.update(tuple(s*g) for s in subgroup)
    assert len(reps) == 3
    basis = [sp.Matrix([1, -1, 0]), sp.Matrix([1, 0, -1])]
    vectors = basis + [sp.Matrix([2, 1, -3]),
                       sp.Matrix([1+sp.I, 1-sp.I, -2])]
    count = truncations = period_checks = weil_checks = negative = 0
    for character, row in [([1, 1], sp.Matrix([[1, 1, -2]])),
                           ([1, -1], sp.Matrix([[1, -1, 0]]))]:
        for rho, haar_g in itertools.product(
                [sp.Rational(1, 2), sp.Integer(1), sp.Integer(2)],
                [sp.Rational(1, 3), sp.Integer(1), sp.Integer(2)]):
            B = rho*row
            haar_s = scalar(B*B.H)/2
            quotient_weight = haar_g/haar_s
            degree = sp.Rational(2, 6)/haar_g
            for u, v in itertools.product(basis, repeat=2):
                period = haar_s*sum(scalar(v.H*s*u)*sp.conjugate(ch)
                                    for s, ch in zip(subgroup, character))
                assert equal(period, scalar(B*u)*sp.conjugate(scalar(B*v)))
                period_checks += 1
            # Source quotient measures may distribute mass among representatives.
            measure = {}
            for g in reps:
                for s, prob in zip(subgroup, [sp.Rational(1, 4), sp.Rational(3, 4)]):
                    measure[tuple(s*g)] = quotient_weight*prob
            for target in matrices:
                rhs = sum(measure[tuple(h)]*haar_s
                          for h in matrices for s in subgroup if s*h == target)
                assert rhs == haar_g
                weil_checks += 1
            for v in vectors:
                norm = scalar(v.H*v)
                alpha = degree/norm
                p = {tuple(g): sp.simplify(alpha*sp.conjugate(scalar(v.H*g*v)))
                     for g in matrices}
                for x in matrices:
                    convolution = haar_g*sum(p[tuple(t)]*p[tuple(t.T*x)]
                                             for t in matrices)
                    assert equal(convolution, p[tuple(x)])
                    assert equal(sp.conjugate(p[tuple(x.T)]), p[tuple(x)])
                f = sp.Matrix([scalar(B*g*v) for g in reps])
                kernel = sp.Matrix([
                    [haar_s*sum(p[tuple(g.T*s*h)]*ch
                                for s, ch in zip(subgroup, character))
                     for h in reps] for g in reps])
                assert equal(kernel, alpha*f*f.H)
                projection = quotient_weight*kernel
                assert equal(projection.H, projection)
                assert equal(projection*projection, projection)
                assert equal(projection*f, f)
                assert projection.trace() == 1
                mass = quotient_weight*scalar(f.H*f)
                assert equal(degree*mass, norm)
                distributed_mass = sum(measure[tuple(g)]*
                                       sp.conjugate(scalar(B*g*v))*scalar(B*g*v)
                                       for g in matrices)
                assert equal(distributed_mass, mass)
                for flags in itertools.product([0, 1], repeat=3):
                    A = sp.simplify(quotient_weight*sum(
                        keep*sp.conjugate(f[i])*f[i] for i, keep in enumerate(flags)))
                    assert sp.simplify(A-alpha*A*A) >= 0
                    truncations += 1
                if count == 0:
                    # Rescaling B alone violates the fixed period and mass bound.
                    assert sp.simplify(degree*4*mass-norm) > 0
                    negative += 1
                    # Replacing the given quotient measure by probability changes P.
                    wrong = kernel/3
                    assert not equal(wrong*wrong, wrong)
                    negative += 1
                count += 1
    # A zero period is also allowed: the standard representation has
    # no invariants under S=G, with the trivial one-dimensional lambda.
    for u, v in itertools.product(basis, repeat=2):
        assert sum(scalar(v.H*g*u) for g in matrices) == 0
    v = vectors[-1]
    norm = scalar(v.H*v)
    assert equal(sum(sp.conjugate(scalar(v.H*g*v)) for g in matrices)/(3*norm), 0)
    return {"models": count, "period_identities": period_checks,
            "compact_truncations": truncations, "representative_weil_checks": weil_checks,
            "zero_bessel_period_model": True, "negative_controls": negative}


def complex_character_models():
    zeta = -sp.Rational(1, 2)+sp.I*sp.sqrt(3)/2
    count = negative = 0
    for rho, haar_g, v in itertools.product(
            [sp.Rational(1, 2), sp.Integer(2)],
            [sp.Rational(1, 3), sp.Integer(2)],
            [sp.Integer(2), 1+sp.I]):
        haar_s = rho*rho
        quotient_weight = haar_g/haar_s
        degree = 1/(3*haar_g)
        norm = sp.simplify(v*sp.conjugate(v))
        f = sp.Matrix([sp.expand_complex(rho*zeta**g*v) for g in range(3)])
        p = [sp.expand_complex(degree*sp.conjugate(zeta**g)) for g in range(3)]
        kernel = sp.Matrix([[haar_s*p[(h-g) % 3] for h in range(3)]
                            for g in range(3)])
        assert equal(kernel, degree/norm*f*f.H)
        projection = quotient_weight*kernel
        assert equal(projection*projection, projection)
        assert equal(projection.H, projection)
        assert equal(projection*f, f)
        assert equal(degree*quotient_weight*scalar(f.H*f), norm)
        if count == 0:
            wrong = sp.conjugate(projection)
            assert equal(wrong*f, sp.zeros(3, 1))
            assert not equal(wrong*f, f)
            negative += 1
        count += 1
    return {"models": count, "nonreal_orientation_negative_controls": negative}


def algebraic_checks():
    t, c = sp.symbols("t c", real=True, positive=True)
    assert sp.expand(t*t-t/c+1/(4*c*c)-(t-1/(2*c))**2) == 0
    r, extra = sp.symbols("r extra", nonnegative=True)
    k, n, q = extra+1, 2*r+extra+2, r+1
    margin = sp.Poly(sp.expand((9*q-2)*n*n+12*(k+r)*q+3), r, extra)
    assert all(value > 0 for value in margin.coeffs())
    jacobians = 0
    for n in [2, 3]:
        J = sp.diag(1, -1, *([1]*(n-2)))
        for u in [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(2, 3)]:
            boost = sp.eye(n)
            boost[0, 0] = boost[1, 1] = (1+u*u)/(1-u*u)
            boost[0, 1] = boost[1, 0] = 2*u/(1-u*u)
            phase = sp.diag(sp.I, -sp.I, *([1]*(n-2)))
            g = phase*boost
            assert equal(g.H*J*g, J)
            assert g.det() == 1
            complex_left_jacobian = sp.kronecker_product(sp.eye(n), g).det()
            assert equal(complex_left_jacobian*sp.conjugate(complex_left_jacobian), 1)
            jacobians += 1
    return {"decay_square_completion": True,
            "gap_margin_nonnegative_polynomial": str(margin.as_expr()),
            "ambient_volume_jacobians": jacobians}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources, prior = source_records(args.offline)
    exact = {"symmetric_group": finite_symmetric_group_models(),
             "complex_characters": complex_character_models(),
             "algebraic": algebraic_checks()}
    artifacts = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
                 f"paper/shared/{STEM}-references.tex",
                 "scripts/check_global_norm_frontier_quotient_mass.py"]
    certificate = {
        "date": "2026-11-22", "status": "PASS",
        "claim": "The original subgroup-period normalized Bessel map satisfies "
                 "d*integral_Q ||B sigma(g)v||^2 <= ||v||^2 on every smooth vector, "
                 "with equality if B is nonzero on smooth vectors.",
        "new_supplier": "An integrable matrix-coefficient projection and compact "
                        "quotient truncation replace the double-integrability norm identity.",
        "sources": sources, "credited_prior_result": prior, "exact_checks": exact,
        "proof_obligations_addressed": [
            "One integrable cyclic vector follows from existing lowest-type decay, "
            "original gap, and equal-volume ambient ellipsoid packing.",
            "The cyclic translate span is dense in the smooth topology by compact "
            "smoothing and a smooth approximate identity.",
            "Original Bessel continuity and allowed translated compact-finite domain are retained.",
            "Induced covariance, right action, inverse and conjugate in the period kernel are explicit.",
            "Compact quotient support need not be compact group support; bounded sections suffice.",
            "Original matrix-representative quotient measure pushes forward to the same Weil measure.",
            "Zero vector, zero Bessel map, and zero truncated mass require no division."
        ],
        "artifacts": [{"path": path, "sha256": sha((ROOT/path).read_bytes())}
                      for path in artifacts],
        "limitations": [
            "Discrete-series existence, formal-degree Schur orthogonality and the "
            "classical lowest compact-type formula are retained inputs.",
            "Existence and original subgroup-period normalization of Bessel maps "
            "are retained inputs; equivariance alone does not supply the period.",
            "The exact-isometry corollary requires B nonzero; the upper bound does not.",
            "Weighted orbital estimates, original Gram identification and whole-node "
            "closure require further assembly.",
            "Finite exact models supplement the general analytic proof; no Lean build."
        ],
        "reproduce": "python3 scripts/check_global_norm_frontier_quotient_mass.py --offline"
    }
    output = ROOT/"certificates"/f"{STEM}.json"
    output.write_text(json.dumps(certificate, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "exact_checks": exact, "certificate": str(output.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
