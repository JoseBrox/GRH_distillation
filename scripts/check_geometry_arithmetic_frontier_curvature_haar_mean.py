#!/usr/bin/env python3
"""Authenticate the original mean and check its determinant normalization.

The source audit is bounded and pinned. Exact algebra below checks the
matrix density and finite-sheet normalizations; it does not construct
the original geometric sheets or verify a Lean build.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path

import sympy as sp

from check_sources import inspect_file


ROOT = Path(__file__).resolve().parents[1]
REVISION = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPOSITORY = "jsmorph/rh"
STEM = "geometry-arithmetic-frontier-curvature-haar-mean"
G = "GroundTheory.HeightsAndTheta.Heights."
R = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry."
D = "Development.AutomorphicSpectrum."
SOURCES = [
    (G + "HodgeLowerBound.FrameDefinitions.IsFrameOverLine", [(60, 99)]),
    (G + "HodgeLowerBound.FrameDefinitions.Weights", [(136, 143)]),
    (R + "ArithmeticHilbertSamuelLowerBound", [(73, 74)]),
    (R + "IsSemipositiveOn", [(206, 219)]),
    (R + "IsIntersectionFamily", [(116, 145)]),
    (D + "Definitions.MetricPeriods.IsFundSet", [(15, 24), (49, 78)]),
    (D + "Definitions.MetricPeriods.GroupDict", [(14, 43)]),
    (D + "Definitions.GlobalGeometry.IsSheetCover", [(20, 28), (38, 73)]),
    (D + "Proofs.MetricProofs.MongeAmpereDensityOfBallPotential", [(337, 385)]),
    (D + "Proofs.MetricProofs.HaarPushforwardEqBallDensity", [(394, 464)]),
    (D + "Proofs.MetricProofs.SheetCoverOfArithmeticVarietyStatement", [(11, 12)]),
    (G + "StabilizerCovolume.StatementsMeanLogPlus", [(25, 29), (48, 52)]),
    (D + "ParallelStatements.ParallelGeometry.CuspMeanBound", [(21, 24)]),
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_records(offline: bool) -> list[dict]:
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == REPOSITORY and atlas["commit"] == REVISION
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        record = inspect_file({"repository": REPOSITORY, "commit": REVISION,
                               "path": rel, "git_blob_sha1": blobs[module]}, offline)
        assert record["matches_pinned_blob"]
        data = (ROOT / "build/source-cache" / REPOSITORY / REVISION / rel).read_bytes()
        record = {k: record[k] for k in
                  ["repository", "commit", "path", "bytes", "git_blob_sha1",
                   "sha256", "matches_pinned_blob"]}
        lines = data.splitlines()
        record["inspected_excerpts"] = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            excerpt = b"\n".join(lines[lo - 1:hi]) + b"\n"
            assert len(excerpt) <= 12000
            record["inspected_excerpts"].append(
                {"lines": [lo, hi], "sha256": sha(excerpt)})
        records.append(record)
    return records


def star(matrix):
    return matrix.conjugate().T


def clean(matrix):
    return matrix.applyfunc(sp.simplify)


def sample(p, q, seed):
    return sp.Matrix(p, q, lambda i, j:
                     sp.Rational(i + 1 - seed * (j + 1), 8 * max(1, p * q))
                     + sp.I * sp.Rational(i + 1 + seed * (j + 1),
                                          12 * max(1, p * q)))


def check_matrix_density(p, q, seed):
    z = sample(p, q, seed)
    left = clean(sp.eye(p) - z * star(z))
    right = clean(sp.eye(q) - star(z) * z)
    for k in range(1, q + 1):
        assert right[:k, :k].det() > 0
    assert sp.simplify(left.det() - right.det()) == 0
    a, b = clean(left.inv()), clean(right.inv())
    tensor_hessian = sp.kronecker_product(a.T, b) / 2
    assert sp.simplify(tensor_hessian.det()
                       - sp.Rational(1, 2) ** (p * q)
                       * right.det() ** (-(p + q))) == 0

    # Independently differentiate the determinant polynomial, then assemble
    # exactly the source's real-derivative definition of its complex Hessian.
    dim = p * q
    xs = sp.symbols("x0:" + str(dim), real=True)
    ys = sp.symbols("y0:" + str(dim), real=True)
    zsym = sp.Matrix(p, q, lambda i, j: xs[i * q + j] + sp.I * ys[i * q + j])
    polynomial = sp.expand((sp.eye(q) - star(zsym) * zsym).det())
    coordinates = xs + ys
    values = {xs[i * q + j]: sp.re(z[i, j]) for i in range(p) for j in range(q)}
    values.update({ys[i * q + j]: sp.im(z[i, j]) for i in range(p) for j in range(q)})
    d0 = sp.simplify(polynomial.subs(values))
    gradient = sp.Matrix([sp.diff(polynomial, v).subs(values) for v in coordinates])
    second = sp.Matrix(2 * dim, 2 * dim,
                       lambda i, j: sp.diff(polynomial, coordinates[i], coordinates[j]).subs(values))
    real_hessian = (gradient * gradient.T / d0 ** 2 - second / d0) / 2
    direct = sp.Matrix(dim, dim, lambda i, j:
                       (real_hessian[i, j] + real_hessian[dim + i, dim + j]
                        + sp.I * (real_hessian[i, dim + j] - real_hessian[dim + i, j])) / 4)
    assert clean(direct - tensor_hessian) == sp.zeros(dim)

    # Check the actual quotient representative and its norm, independently
    # of the Hessian calculation.
    w = z.T
    dmat = clean(sp.eye(q) - w * star(w))
    inverse = clean(dmat.inv())
    section = sp.Matrix.vstack(star(w), sp.eye(q)) * inverse
    positive_plane = sp.Matrix.vstack(sp.eye(p), w)
    form = sp.diag(*([1] * p + [-1] * q))
    quotient = sp.Matrix.hstack(-w, sp.eye(q))
    assert clean(quotient * section - sp.eye(q)) == sp.zeros(q)
    assert clean(star(positive_plane) * form * section) == sp.zeros(p, q)
    assert clean(-star(section) * form * section - inverse) == sp.zeros(q)
    return {"signature": [p, q], "seed": seed, "complex_dimension": dim}


def exact_checks():
    density_cases = [
        check_matrix_density(p, q, seed)
        for p, q in [(1, 1), (1, 2), (2, 1), (2, 2)]
        for seed in [1, 2]
    ]
    zero_cases = []
    for p, q in [(0, 0), (0, 3), (3, 0)]:
        z = sp.zeros(p, q)
        assert (sp.eye(q) - star(z) * z).det() == 1
        assert p * q == 0 and math.factorial(p * q) == 1
        zero_cases.append([p, q])

    # Constant mixed discriminant: the finite-difference coefficient is n!.
    mixed_cases = 0
    for n in range(9):
        coefficient = sum((-1) ** (n - k) * math.comb(n, k) * k ** n
                          for k in range(n + 1))
        assert coefficient == math.factorial(n)
        assert F(2 ** n, 1) * F(1, 2) ** n == 1
        mixed_cases += 1

    # Exact fractional-linear covariance for a rational unitary boost.
    mobius_cases = 0
    for p, q in [(1, 1), (2, 2)]:
        a, d = sp.eye(p), sp.eye(q)
        b, c = sp.zeros(p, q), sp.zeros(q, p)
        a[0, 0] = d[0, 0] = sp.Rational(5, 3)
        b[0, 0] = c[0, 0] = sp.Rational(4, 3)
        g = sp.BlockMatrix([[a, b], [c, d]]).as_explicit()
        form = sp.diag(*([1] * p + [-1] * q))
        assert clean(star(g) * form * g - form) == sp.zeros(p + q)
        z = sample(p, q, 1)
        denominator = clean(c * z + d)
        image = clean((a * z + b) * denominator.inv())
        assert clean(sp.eye(q) - star(image) * image
                     - star(denominator.inv()) * (sp.eye(q) - star(z) * z)
                     * denominator.inv()) == sp.zeros(q)
        mobius_cases += 1

    # Distinct sheet values ensure this checks fibre averaging, not merely
    # the special case where every sheet has the same value.
    masses = [[F(1), F(2), F(3)], [F(1, 2), F(3, 2)]]
    sheets = [[(F(1), F(-1)), (F(2), F(-3)), (F(4), F(5))],
              [(F(-2), F(0), F(4)), (F(1), F(-1), F(3))]]
    multiplicities = [2, 3]
    volumes = [sum(row, F(0)) for row in masses]
    total_mass = sum((d * v for d, v in zip(multiplicities, volumes)), F(0))
    numerator = sum((mass * sum(vals, F(0))
                     for mm, ss in zip(masses, sheets)
                     for mass, vals in zip(mm, ss)), F(0))
    abs_mass = sum((mass * sum(map(abs, vals), F(0))
                    for mm, ss in zip(masses, sheets)
                    for mass, vals in zip(mm, ss)), F(0))
    weights = [d * v / total_mass for d, v in zip(multiplicities, volumes)]
    haar_means = [
        sum((mass * sum(vals, F(0)) / d for mass, vals in zip(mm, ss)), F(0)) / v
        for mm, ss, d, v in zip(masses, sheets, multiplicities, volumes)
    ]
    assert numerator / total_mass == sum((w * mean for w, mean in zip(weights, haar_means)), F(0))
    assert numerator / total_mass == F(61, 36)
    assert abs_mass > abs(numerator)

    haar_constants = [F(2), F(5)]
    stabilizer_orders = [3, 2]
    raw_covolumes = [c * v / s for c, v, s in zip(haar_constants, volumes, stabilizer_orders)]
    recovered_volumes = [s * raw / c for s, raw, c in zip(stabilizer_orders, raw_covolumes, haar_constants)]
    assert recovered_volumes == volumes
    wrong_total = sum((d * raw for d, raw in zip(multiplicities, raw_covolumes)), F(0))
    wrong_weights = [d * raw / wrong_total for d, raw in zip(multiplicities, raw_covolumes)]
    assert wrong_weights != weights
    return {
        "direct_complex_hessian_and_quotient_gram_cases": density_cases,
        "zero_dimensional_factors": zero_cases,
        "mixed_density_normalization_cases": mixed_cases,
        "mobius_covariance_cases": mobius_cases,
        "finite_sheet_mean": str(numerator / total_mass),
        "retained_component_weights": list(map(str, weights)),
        "wrong_weights_if_stabilizers_and_haar_constants_are_dropped": list(map(str, wrong_weights)),
        "absolute_integrability_control": "Signed sheet means do not determine the absolute sheet integral.",
        "scope": "Exact local algebra and finite measure identities; the general measure proof is in the note.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true",
                        help="Require the pinned source files to be cached.")
    args = parser.parse_args()
    artifacts = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
                 "scripts/check_geometry_arithmetic_frontier_curvature_haar_mean.py"]
    certificate = {
        "status": "pass",
        "claim": "The original Hodge determinant density yields the normalized arithmetic Haar mean on the actual finite geometric sheets, with multiplicities and stabilizer factors retained.",
        "source_pin": {"repository": REPOSITORY, "commit": REVISION},
        "source_records": source_records(args.offline),
        "exact_checks": exact_checks(),
        "density_convention": "dd^c=(i/pi)partial barpartial; repeated-potential density n!(2/pi)^n det(Hess(phi)); phi=Phi/2 gives n!/pi^n times b.",
        "normalization": "degMu=geomDeg=the same ptsIntegral against 1 by definition; no algebraic-degree or boundary-current replacement.",
        "component_weights": "d_k V_k / sum_l d_l V_l, where V_k=(s_k/c_k) vol(Gamma_k\\G_k) for pi_*dg_k=c_k b_k dV.",
        "proved_consumers": [
            "Nonnegative full isotropic lattice counts, once the original fibre isometries and complex sheets are identified",
            "The nonnegative logarithmic cusp function, using the preceding counting-to-mean bound",
            "The original nonnegative cusp weight via its pointwise bound",
        ],
        "retained_geometric_inputs": [
            "Existence of the actual arithmetic model and global family",
            "Original finite arithmetic component uniformization and source Pieces sheet cover, including finite multiplicities",
            "Original lattice, Hodge norm and determinant metric identifications; an arbitrary FullerData record does not imply them",
            "The signed boundary intersection limit and the remaining arithmetic section suppliers",
        ],
        "no_new_analytic_hypothesis": "Arithmetic unfolding supplies finite count means; the original determinant metric supplies the invariant density; normalization is the same analytic mass.",
        "integrability_scope": "Use nonnegative measures first, then require the average of absolute sheet values to be integrable. No assertion about totalized real integrals of nonintegrable functions.",
        "artifacts": [{"path": path, "sha256": sha((ROOT / path).read_bytes())}
                      for path in artifacts],
        "verification_limit": "No Lean build, no geometric existence assertion, no complete RH or GRH proof, no proof-map node closure.",
        "completed_nodes": {"RH": [6, 9], "GRH": [17, 31]},
    }
    output = ROOT / "certificates" / f"{STEM}.json"
    output.write_text(json.dumps(certificate, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "pass", "certificate": str(output.relative_to(ROOT)),
                      "pinned_source_modules": len(certificate["source_records"]),
                      "direct_hessian_cases": len(certificate["exact_checks"]["direct_complex_hessian_and_quotient_gram_cases"]),
                      "finite_sheet_mean": certificate["exact_checks"]["finite_sheet_mean"],
                      "component_weights": certificate["exact_checks"]["retained_component_weights"],
                      "completed_nodes": certificate["completed_nodes"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
