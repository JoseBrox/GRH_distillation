#!/usr/bin/env python3
"""Authenticate source anchors and test exact finite section-rank formulas.

The written geometric proof is not replaced by these finite checks.  The
polynomial tests certify only the listed model evaluation matrices.
"""

from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
from math import comb, isqrt, prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVISION = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPOSITORY = "jsmorph/rh"
PREFIX = "Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts."
SOURCES = [
    (PREFIX + "HodgeBundleWeights.JetRankComplexLe",
     "0c3a10e49869394921fb8a6eb3bb08bb89337f00e6faed0981d6cab884dc13d8", [[55, 102]]),
    (PREFIX + "HodgeBundleWeights.ShareStatementOfKnownTheorems",
     "ce2fbe082c40361dd35920bc2af3495e37dd3589babc5a084e32f282708c5d8c", [[55, 91]]),
    (PREFIX + "ThirdPlaceSeries.ShareStatementOfKnownTheorems",
     "73997cc0ad2cfd623ceeff3ac2f4ceb7b6ceefea4d56d5e6ce213dd0188aa2d0", [[47, 66]]),
    ("Development.AbelianVarietyTheory.Proofs.DivisorProofs.ComponentImageDegreeBetweenOfProportionality",
     "1a46a7b6241bdf31ded295acf0822a8e490ab3f06c521651824c61a2ea733f37", [[15, 26]]),
    (PREFIX + "HodgeBundleWeights.BaseWeightLineBundleIsNef",
     "33b5c25c574e726b9d2912d78a95d97ad3cf7e2c25587b7cb81159a50dcea90b", [[21, 32]]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def sources():
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


def multiindices(d, bound):
    return [a for a in itertools.product(range(bound + 1), repeat=d) if sum(a) <= bound]


def jet_entry(exponent, derivative, point):
    # Taylor coefficient, i.e. derivative divided by its multi-factorial.
    if any(b > e for e, b in zip(exponent, derivative)):
        return 0
    return prod(comb(e, b) * x ** (e - b)
                for e, b, x in zip(exponent, derivative, point))


def independent_rows(matrix, prime):
    a = [[v % prime for v in row] for row in matrix]
    row_ids = list(range(len(a)))
    pivots = []
    for col in range(len(a[0])):
        pivot = next((r for r in range(len(pivots), len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        i = len(pivots)
        a[i], a[pivot] = a[pivot], a[i]
        row_ids[i], row_ids[pivot] = row_ids[pivot], row_ids[i]
        pivots.append(row_ids[i])
        inv = pow(a[i][col], -1, prime)
        for j in range(col, len(a[0])):
            a[i][j] = a[i][j] * inv % prime
        for r in range(i + 1, len(a)):
            scale = a[r][col]
            if scale:
                for j in range(col, len(a[0])):
                    a[r][j] = (a[r][j] - scale * a[i][j]) % prime
    return pivots


def determinant_mod(matrix, prime):
    a = [[v % prime for v in row] for row in matrix]
    determinant = 1
    for col in range(len(a)):
        pivot = next((r for r in range(col, len(a)) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            determinant = -determinant
        value = a[col][col]
        determinant = determinant * value % prime
        inv = pow(value, -1, prime)
        for r in range(col + 1, len(a)):
            scale = a[r][col] * inv % prime
            for j in range(col + 1, len(a)):
                a[r][j] = (a[r][j] - scale * a[col][j]) % prime
    return determinant % prime


def polynomial_models():
    prime = 1000003
    assert all(prime % d for d in range(2, isqrt(prime) + 1))
    for a in range(20):
        # P^1, A=O(1), B=O(a+1): at equality the proposed
        # non-strict numerical bound would give a+2 <= a+1.
        assert comb(a + 2, 1) > comb(a + 1, 1)
    records = []
    cases = [(d, k, a) for d in [1, 2] for k in [2, 3] for a in [0, 1, 2]]
    cases += [(3, 2, 0), (3, 2, 1)]
    for d, k, a in cases:
        # P^d, A=O(k).  A general-fibre model uses the k-grid
        # [x0^k : product(x_i-j*x0)] at [1:0:...:0].
        points = list(itertools.product(range(k), repeat=d))
        jets = multiindices(d, a)
        degree = k * (a + 1) - 1
        exponents = multiindices(d, degree)
        matrix = [[jet_entry(exponent, beta, point) for exponent in exponents]
                  for point in points for beta in jets]
        pivots = independent_rows(matrix, prime)
        assert len(pivots) == len(exponents)
        minor = [matrix[i] for i in pivots]
        det = determinant_mod(minor, prime)
        assert det != 0
        assert degree * k ** (d - 1) < (a + 1) * k ** d
        assert len(exponents) <= k ** d * comb(a + d, d)
        # At equality, product(x_1-j)^(a+1) is nonzero and all
        # Taylor coefficients through order a vanish on the grid.
        polynomial = [1]
        for _ in range(a + 1):
            for j in range(k):
                nxt = [0] * (len(polynomial) + 1)
                for i, c in enumerate(polynomial):
                    nxt[i] -= j * c
                    nxt[i + 1] += c
                polynomial = nxt
        assert polynomial[-1] == 1 and len(polynomial) - 1 == k * (a + 1)
        for point in points:
            for beta in jets:
                coeff = sum(c * jet_entry((i,) + (0,) * (d - 1), beta, point)
                            for i, c in enumerate(polynomial))
                assert coeff == 0
        records.append({"dimension": d, "grid_degree": k, "jet_order": a,
                        "polynomial_degree": degree, "points": len(points),
                        "section_dimension": len(exponents), "jet_dimension": len(matrix),
                        "modular_certificate": {"prime": prime, "minor_rows": pivots,
                                                "determinant": det},
                        "strict_threshold_counterexample_verified": True})
    return records


def rank_ratios():
    count = 0
    rho_values = [F(0), F(1, 1000), F(1, 100), F(1, 7), F(1, 2), F(9, 10), F(99, 100)]
    for d in range(1, 41):
        for t in sorted({d + 1, 2 * d + 3, 10 * d * d, 100 * d * d}):
            for rho in rho_values:
                n = t + d + 3
                a = int(F(n) / (1 - rho))
                assert F(n) / (1 - rho) < a + 1
                ratio = F(comb(t - 1, d), comb(a + d, d))
                eta = 1 - ratio
                theta = d * rho + F(2 * d * d + 4 * d, t)
                assert 0 <= eta < 1 and eta <= theta
                assert ratio == prod(F(t - j, a + j) for j in range(1, d + 1))
                es = [1 - (1 - rho) * (t - j) / (t + d + 3 + j * (1 - rho))
                      for j in range(1, d + 1)]
                assert all(0 <= e < 1 for e in es)
                assert eta <= 1 - prod(1 - e for e in es) <= sum(es) <= theta
                if theta < 1:
                    assert eta / (1 - eta) <= theta / (1 - theta)
                if d >= 2:
                    assert theta <= d * rho + F(4 * d * d, t)
                    assert theta <= 7 * (F(d * d, t) + d * rho)
                count += 1
    return {"cases": count, "arithmetic": "exact rational", "all_passed": True,
            "excess_rank_conversion": "eta/(1-eta), bounded by Theta/(1-Theta) only when Theta<1"}


def main():
    source_records = sources()
    result = {
        "schema_version": 1,
        "status": "written geometric implication with explicit remaining model hypotheses",
        "scope": "Pinned source authentication, exact finite algebra, and polynomial-model jet minors; no geometric construction verification or Lean replay.",
        "source_files": source_records,
        "rank_ratio_checks": rank_ratios(),
        "polynomial_models": polynomial_models(),
        "primary_references": [
            {"url": "https://stacks.math.columbia.edu/tag/01OF", "facts": "base-ideal blowup; effective exceptional divisor; projectivity"},
            {"url": "https://stacks.math.columbia.edu/tag/0AB5", "facts": "Lemma 33.17.2; finiteness in codimension one"},
            {"url": "https://stacks.math.columbia.edu/tag/0BEL", "facts": "numerical intersections, effective divisor restriction, positivity of ample classes"},
        ],
        "remaining_inputs": [
            "actual projective component model and original cusp-section realization",
            "birationality of the chosen weight system, weight nefness, and prescribed degree comparison",
            "signed cusp mean and arithmetic Hilbert-Samuel remainder estimates",
            "common arithmetic constructions, integral maps and global norms",
        ],
        "node_status_change": False,
    }
    result["artifacts"] = [{"path": p, "sha256": sha((ROOT / p).read_bytes())} for p in [
        "notes/finite-section-jet-bound.md", "paper/shared/finite-section-jet-bound.tex",
        "scripts/check_finite_section_jet_bound.py"]]
    out = ROOT / "certificates/finite-section-jet-bound.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"source_files": len(source_records),
                      "exact_rank_cases": result["rank_ratio_checks"]["cases"],
                      "certified_polynomial_models": len(result["polynomial_models"]),
                      "certificate": str(out.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
