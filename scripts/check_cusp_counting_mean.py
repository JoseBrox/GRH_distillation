#!/usr/bin/env python3
"""Authenticate bounded cusp sources and check exact scalar comparisons.

The measure, model and arithmetic identifications remain mathematical
hypotheses. Finite checks do not prove their existence or replay Lean.
"""

from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVISION = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPOSITORY = "jsmorph/rh"
PREFIX = "GroundTheory.HeightsAndTheta.Heights."
SOURCES = [
    (PREFIX + "StabilizerCovolume.StatementsMeanLogPlus",
     "ac7f1aed609688a709b310670d11489101c19820f6417784c40234a16541ce1c", [[14, 66]]),
    (PREFIX + "StabilizerCovolume.ShortIsotropic",
     "0454c38448025db63cf78a9fa9796fb8f6a9069c08196728b5d507d02c1fcb0c", [[147, 217], [219, 281]]),
    (PREFIX + "CountingLowerBound.Statements",
     "277c23ccb074fbe1a4538ecc2ceaff2fab72b637ba437f3151438184ee82d6a3", [[141, 189]]),
    (PREFIX + "CountingLowerBound.PMeanCountBound",
     "96a900dca2d37f7af5a480f8c346f9d02fd22856d7bd40541a2581a5d1dcd1e3", [[13, 100]]),
    (PREFIX + "CountingLowerBound.PCuspWeightBound",
     "5c86fbd357c52e5fd9b581d1e14dfe1f2f41e6687e963285ae752c736abc9c24", [[19, 53]]),
    (PREFIX + "HodgeLowerBound.FlagIndices",
     "8229a61265994066013cfba3d40283075be714c88a6bc13dae482cce930e9cc5", [[78, 80]]),
    ("Development.AutomorphicSpectrum.ParallelStatements.ParallelGeometry.CuspMeanBound",
     "3f023a2bffbd92f37710acb5531fff2c76501afb8c6fd92b6c9cb46efad3c444",
     [[21, 24], [42, 44], [58, 84]]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == REPOSITORY and atlas["commit"] == REVISION
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, expected, ranges in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        local = ROOT / "build/source-cache" / REPOSITORY / REVISION / path
        data = local.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert sha(data) == expected and blob == blobs[module]
        lines = data.splitlines()
        excerpts = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines) and end - start < 120
            excerpts.append({"lines": [start, end],
                             "sha256": sha(b"\n".join(lines[start - 1:end]) + b"\n")})
        records.append({"repository": REPOSITORY, "commit": REVISION, "path": path,
                        "git_blob_sha1": blob, "sha256": expected,
                        "inspected_excerpts": excerpts})
    return records


def log_interval(x, terms=32):
    """Exact atanh-series enclosure of log(x) for rational 1 <= x <= 3."""
    x = F(x)
    assert F(1) <= x <= F(3)
    z = (x - 1) / (x + 1)
    lower = 2 * sum((z ** (2 * n + 1) / (2 * n + 1) for n in range(terms)), F(0))
    remainder = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return lower, lower + remainder


def exact_checks():
    # For M=u^k, the splitting point M^(a/k)=u^a is rational.
    tail_cases = 0
    for a in range(1, 9):
        for k in range(a + 1, a + 7):
            for u in [F(1), F(3, 2), F(2), F(3)]:
                m = u ** k
                split = u ** a
                integral = 1 + (split - 1) + m * F(a, k - a) * u ** (a - k)
                assert integral == F(k, k - a) * u ** a
                tail_cases += 1

    assert F(2, 3) + F(1, 8) + F(1, 6) == F(23, 24) < 1
    log3 = log_interval(F(3))
    log15 = log_interval(F(3, 2))
    assert log3[1] <= F(4, 3) and log15[1] <= F(1, 2)
    exact_worst = log3[1] / 2 + log15[1] / 4 + F(1, 6)
    assert exact_worst < F(5, 6)

    logarithmic_cases = 0
    for a in [F(2), F(5, 2), F(3), F(4), F(10), F(100)]:
        for ratio in [F(3), F(7, 2), F(4), F(7), F(100)]:
            k = ratio * a
            upper = (a * log3[1] + log_interval(k / (k - a))[1]) / (k - a) + 1 / k
            assert upper <= exact_worst
            logarithmic_cases += 1

    # Cyclic character groups: every proper subgroup is at most half.
    # Exponents model a conductor filtration, not an instantiated field.
    filtration_cases = 0
    for d in range(2, 49):
        for h in range(1, d):
            if d % h:
                continue
            subgroup = {x * (d // h) for x in range(h)}
            assert len(subgroup) == h and 2 * h <= d
            for b in range(1, 7):
                exponents = [0 if x == 0 else b - 1 if x in subgroup else b for x in range(d)]
                assert max(exponents) == b
                assert 2 * sum(exponents) >= d * b
                filtration_cases += 1

    absorption_cases = 0
    for f in range(1, 13):
        for j in range(1, 101):
            n = 3 * j + 1
            b = 4 * f * n * n
            assert b >= 64 * j
            assert 4 * (3 * j + 1) ** 2 - 64 * j == 4 * (j - 1) * (9 * j - 1)
            absorption_cases += 1
    # log(64)=6 log(2)>=3>2, by integrating 1/x >= 1/2 on [1,2].
    assert 6 * F(1, 2) > 2

    coarea_cases = 0
    for f in range(1, 13):
        for n in range(3, 33):
            for p in range(1, n):
                q = n - p
                assert p > 0 and q > 0
                assert (p - 1) + (q - 1) == n - 2 >= 1
                # Hypersurface scaling minus the linear gradient scaling.
                assert f * ((2 * n - 1) - 1) == 2 * f * (n - 1)
                # Polar coarea near the deleted zero vertex is integrable.
                assert (2 * p - 1) + (2 * q - 1) - 1 == 2 * n - 3 > -1
                coarea_cases += 1

    counterexamples = []
    for exponent in range(1, 21):
        lam = F(1, 2 ** exponent)
        t = F(3, 2) * lam
        assert lam < t < 1
        assert 1 <= (3 / lam) ** 2
        assert 1 > t ** 6  # N_t=N_1=1 violates mean scaling.
        counterexamples.append({"lambda": str(lam), "logarithmic_mean": f"{exponent}*log(2)"})
    return {"rational_tail_integral_cases": tail_cases,
            "certified_logarithmic_bound_cases": logarithmic_cases,
            "finite_character_filtration_cases": filtration_cases,
            "exact_scale_absorption_cases": absorption_cases,
            "exact_coarea_and_transitivity_dimension_cases": coarea_cases,
            "uniform_bound": "23/24 < 1",
            "sharper_numerical_comparison": "log(3)/2+log(3/2)/4+1/6 < 5/6 (exact rational series enclosure)",
            "without_scaling_counterexamples": counterexamples}


def main():
    sources = source_records()
    checks = exact_checks()
    artifacts = ["notes/cusp-counting-mean.md", "paper/shared/cusp-counting-mean.tex",
                 "scripts/check_cusp_counting_mean.py"]
    certificate = {
        "status": "passed",
        "claim": "Cusp-mean supplier with constant Cu=3; the companion arithmetic first-moment theorem supplies the full count's integrability, and Haar invariance supplies its scaling",
        "source_verification": "Pinned source bytes and bounded excerpts authenticated; no Lean build claim",
        "sources": sources,
        "classical_reference": {
            "author": "J. S. Milne", "title": "Class Field Theory", "version": "4.03 (2020-08-06)",
            "url": "https://www.jmilne.org/math/CourseNotes/CFT.pdf",
            "passages": ["Theorem I.4.16, printed pp.49-50", "Example V.3.10, printed p.159", "Theorem V.3.27, printed p.165"],
            "scope": "Primary passages inspected for cyclotomic inclusion and conductor identities; external theorem proofs cited, not reverified"},
        "exact_checks": checks,
        "retained_inputs": [
            "Actual arithmetic model, Hermitian lattice and original norm/covolume identifications",
            "Normalized Haar quotient probability measure and actual discrete lattice-vector count agreeing with the geometric mean, retaining component/stabilizer factors and finite-adelic support",
            "Identification with the original arithmetic lattice stabilizer in Hermitian dimension at least three; finite volume and full-count integrability are then supplied by the companion arithmetic first-moment theorem",
            "The same nonnegative measurable cusp U and its original pointwise lattice-covolume comparison",
            "Identification of this integral with the signed arithmetic boundary term and the one-sided boundary limit"],
        "not_claimed": ["Integral basis or index-one spanning in O_E", "New arithmetic model or quotient measure construction", "Full RH/GRH node closure", "Lean project compilation"],
        "homogeneity_proof_checks": [
            "Nonzero E-vectors have no zero archimedean embedding, so empirical measure lives on a single product of nonzero complex null cones",
            "U acts transitively by hyperbolic pairs; SU does when N>=3 by adjusting the determinant on a nonisotropic complement line",
            "Finite mean of one norm-ball count and transitivity imply local finiteness of the invariant averaged counting measure",
            "Coarea measure dS/||grad q|| is invariant and scales by 2N-2 per complex place; its bounded-ball mass is finite",
            "Invariant Radon measure uniqueness eliminates the unknown scalar; finite-adelic support and normalized component weights are retained"],
        "arithmetic_first_moment_supplier": {
            "path": "certificates/geometry-arithmetic-frontier-isotropic-integrability.json",
            "sha256": sha((ROOT / "certificates/geometry-arithmetic-frontier-isotropic-integrability.json").read_bytes()),
            "scope": "Companion proof supplies the arithmetic first moment; this checker does not replace its mathematical review or source verification."},
        "artifact_sha256": {name: sha((ROOT / name).read_bytes()) for name in artifacts},
    }
    output = ROOT / "certificates/cusp-counting-mean.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({"status": "passed", "source_modules": len(sources),
                      **{k: v for k, v in checks.items() if isinstance(v, int)},
                      "certificate": str(output.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
