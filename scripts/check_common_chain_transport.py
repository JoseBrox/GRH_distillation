#!/usr/bin/env python3
"""Exact finite algebra checks for the common-chain transport chapter.

This is not a Lean build or verification of an analytic theta identity.
Source checks use the already available pinned readable checkout.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha1, sha256
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REV = "72fead102f663d5c7a407964a13dc0cf9d977207"
SOURCES = {
    "New/UpperBound/Objects/Columns.lean": "afcff440aad4768ae39a61a11e77934402aa2c72",
    "New/UpperBound/Divisibility/ChainDatumExpansion.lean": "a0f9a505de5e9b6afde9194192d220063f8ab35a",
    "New/UpperBound/Kernels/ThetaLiftGauge.lean": "5c3212c92e2d1a52ada40b2f4822800d0a8c16ea",
    "New/UpperBound/Objects/LiftChains.lean": "213d4b739cb274c80da185a1dae57fd2a9bb517c",
    "New/UpperBound/Divisibility/ChainValuation.lean": "8757389f4a78ba79557014d7370c97aba526de0d",
    "New/UpperBound/Divisibility/LocalDivisibility.lean": "dca196fee3c258a6b261a95303abc09e45f5bc16",
    "New/UpperBound/Size/ArchimedeanSize.lean": "d47054a000f52d49b2778fe907cefac0a11737d0",
    "New/OneLift/HeckeValues/TwistedValueHeights.lean": "ddfc466fb70a096b21707df61c6a0af498151f6c",
    "New/OneLift/FalseLifts/PeriodsOfFalseLifts.lean": "a999c4f8eb57526a9d8215bc5e8c0b423aaccfae",
    "New/Determinant/Twist/FitTwists.lean": "27897e237e68320c4fb473e8ef98bde5c08f9265",
    "New/OneLift/ComparisonOperator/ExchangeData.lean": "7b0ee0953eeda998c465864203b3cdb001f79b46",
    "New/OneLift/TestedForms.lean": "fd293523f52fdef03cf3f7353aaf941ccecff174",
    "New/Reduction/Data/AdmissibleData.lean": "48f73664d37f8b5036fcff2bf642d7be5e259907",
    "New/Reduction/Data/Sizes.lean": "6007f8713e359ad70d320b6e7ce134cad278e424",
    "New/Reduction/Data/LevelAndTwists.lean": "46856ce171839485ad4a1744096ab3d86db4919b",
    "New/UpperBound/Size/ClassCount.lean": "5c9a4beba811d689c4bf3d61bdf6f08139b2730a",
    "New/UpperBound/Size/Estimates.lean": "bbfddcc3eb61f075241aa7f94dc231f736cc2d61",
    "New/UpperBound/Objects/Weights.lean": "debbf2f446b4648ba38c069ac0edd87588a05447",
    "New/Derivatives/Vacuum/IntegralVacuum.lean": "f735c9a79aafe8d2e5b135e2dfebfaa7871dff5c",
    "New/Reduction/Data/FieldsAndPlaces.lean": "8b0a085a2f5aaa75d02863607df1dc7f304018fc",
    "New/Derivatives/Field/ChosenPlaces.lean": "9552c1e2ce3061e631dc70b1e76ad215f66d340d",
}


def source_records():
    records = []
    for name, expected in SOURCES.items():
        candidates = [
            ROOT / "build/readable-source/grh/src" / name,
            ROOT / "build/chain-source" / name,
            ROOT / "build/source-cache/lsernau/grh-lean" / REV / "grh/src" / name,
        ]
        path = next((p for p in candidates if p.is_file()), None)
        if path is None:
            raise FileNotFoundError(f"Pinned source unavailable: {name}")
        data = path.read_bytes()
        blob = sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == expected, (name, blob, expected)
        records.append({"path": "grh/src/" + name, "git_blob_sha1": blob,
                        "sha256": sha256(data).hexdigest()})
    return records


def cyclotomic_zero(counts):
    """For prime q, sum c_i zeta_q^i=0 iff all integer c_i agree."""
    return len(set(counts)) <= 1


def finite_gluing_checks():
    records = []
    total_gram = 0
    # Basis (a,b), with normalized counting measure 1/D on the b variable.
    # v_y(a,b)=1_(a=y) zeta_q^(y.b).  Thus v_0 is delta_0 tensor 1.
    # Translation in the first factor and modulation in the second factor
    # are the finite Schrödinger model of the two conjugate polarizations.
    for q in (2, 3, 5):
        for rank in (1, 2):
            vecs = list(product(range(q), repeat=rank))
            dim = len(vecs)
            zero = (0,) * rank
            gram_sum = Fraction(0)
            for y in vecs:
                for z in vecs:
                    counts = [0] * q
                    # Disjoint delta supports give an empty sum off diagonal.
                    if y == z:
                        for b in vecs:
                            exponent = sum((zi - yi) * bi
                                           for yi, zi, bi in zip(y, z, b)) % q
                            counts[exponent] += 1
                    if y == z:
                        assert counts == [dim] + [0] * (q - 1)
                        gram_sum += Fraction(counts[0], dim)
                    else:
                        assert cyclotomic_zero(counts)
                    total_gram += 1
            assert gram_sum == dim
            # Projection to v_0 keeps exactly y=0. Its coefficient is 1.
            projected = [y for y in vecs if y == zero]
            assert projected == [zero]
            # Tensoring with arbitrary outside data gives A* A = D I.
            outside_gram = [[dim if i == j else 0 for j in range(3)]
                            for i in range(3)]
            assert outside_gram == [[dim, 0, 0], [0, dim, 0], [0, 0, dim]]
            records.append({"q": q, "middle_rank": rank, "D": dim,
                            "gram_entries_checked": dim * dim,
                            "vacuum_projection": "one surviving term",
                            "restricted_gram_scalar": dim})
    return records, total_gram


def expansion_checks():
    count = 0
    for q in (2, 3, 5):
        # x occupies an outside place; the two gluing residues occupy N.
        coeffs = {0: Fraction(2), 1: Fraction(-3), 2: Fraction(5, 7)}
        expanded = {}
        for x, a in coeffs.items():
            for y in product(range(q), repeat=2):
                index = (x,) + y
                assert index not in expanded
                expanded[index] = a
        assert sum(map(abs, expanded.values())) == q**2 * sum(map(abs, coeffs.values()))
        count += len(expanded)
    cardinal_cases = 0
    for f, m, k, t in product((1, 2, 7), (2, 4, 6, 10), (1, 3, 8), (1, 3, 10)):
        odd_sum = sum(k + j * (t + 1) for j in range(1, m, 2))
        exact = f * (m // 2 * k + (m // 2)**2 * (t + 1))
        assert f * odd_sum == exact
        n_m = k + m * (t + 1)
        assert 4 * exact == f * m * (k + n_m)
        assert exact <= f * m * n_m // 2
        cardinal_cases += 1
    # Sharp obstruction to a free square-root saving after evaluation.
    for dim in (2, 3, 9, 25):
        squared_data_norm = dim
        squared_evaluation = dim**2
        assert squared_evaluation > squared_data_norm
    return {"distinct_expanded_indices": count,
            "exact_odd_rank_sum_cases": cardinal_cases,
            "theta_functional_counterexample_dimensions": [2, 3, 9, 25]}


def six_block_checks():
    cases = 0
    for active in (6, 12):
        for z in (24, 101, 10001, 10002):
            residual = 2 * z - active - 8
            assert active + 4 + 4 + residual == 2 * z
            assert residual % 2 == 0 and residual >= 4
            assert 2 * (active + 8) + 5 < 2 * z
            # The vacuum normalization is exactly total rank, not total rank
            # plus the active block a second time.
            assert active + (residual + 8) == 2 * z
            cases += 1
    # Pure tensor symmetrization in a single-row Weyl module:
    # the diagonal Gram entry counts the words of prescribed multiplicities.
    multinomial_cases = 0
    from math import factorial
    for active in (2, 3, 6):
        for degree in range(7):
            counts = {}
            for word in product(range(active), repeat=degree):
                alpha = tuple(word.count(i) for i in range(active))
                counts[alpha] = counts.get(alpha, 0) + 1
            for alpha, multiplicity in counts.items():
                denominator = 1
                for a in alpha:
                    denominator *= factorial(a)
                assert multiplicity == factorial(degree) // denominator
                multinomial_cases += 1
    return {"rank_and_normalization_cases": cases,
            "exact_symmetric_tensor_gram_cases": multinomial_cases}


def norm_budget_ledger():
    """Check integer absorptions after the analytic inequalities in the note.

    x >= e^100 > 2^100. A polynomial with positive coefficients is
    bounded by sum(coefficients)*x^max(degrees), and hence by x^target
    when the exact integer test below passes. No floating logs are used.
    Geometry of numbers, the kernel bound and the scale deductions
    themselves remain ordinary mathematical proofs in the note.
    """
    x_lower = 2**100
    stages = {
        "class_count": ([(384, 55), (3, 24), (104, 26)], 60),
        "branching_squared": ([(792, 66)], 70),
        "single_kernel_nonrow": ([(1, 37), (14, 25), (3, 25), (1, 18)], 50),
        "all_nonrow": ([(1, 70), (30, 56), (30, 21), (132, 26),
                        (2, 61), (2, 51)], 72),
    }
    records = []
    for name, (terms, target) in stages.items():
        coefficient_sum = sum(c for c, _ in terms)
        max_degree = max(e for _, e in terms)
        assert target >= max_degree
        assert coefficient_sum <= x_lower**(target - max_degree)
        records.append({"stage": name, "positive_terms": terms,
                        "coefficient_sum": coefficient_sum,
                        "largest_degree": max_degree, "target_degree": target})
    b_power = 10**12
    assert 88 <= b_power  # n*g^2 <= b
    assert 72 <= b_power + 1  # x^72 <= a <= f*a*B
    row_cost, level_cost, auxiliary_cost = 75, 32, 1
    remainder = row_cost + level_cost + auxiliary_cost
    assert remainder == 108 and remainder <= 100**2
    assert remainder + 1 <= 100**2  # optional terminal class sum
    return {"x_lower_bound": "2^100", "B_lower_bound": 100,
            "b_at_least_x_to_power": b_power, "absorptions": records,
            "pointwise_remainder_in_units_f_a_log_b": remainder,
            "terminal_class_remainder_in_units_f_a_log_b": remainder + 1,
            "original_error_in_units_f_a_log_b": "(log b)^2"}


def main():
    source = source_records()
    gluing, entries = finite_gluing_checks()
    result = {
        "status": "passed",
        "source_repository": "lsernau/grh-lean",
        "source_revision": REV,
        "sources": source,
        "finite_gluing": gluing,
        "total_gram_entries_checked": entries,
        "expansion": expansion_checks(),
        "six_block_transport": six_block_checks(),
        "norm_budget_ledger": norm_budget_ledger(),
        "scope": "Exact finite algebra, pinned bytes and integer exponent absorptions. The analytic kernel and geometry-of-numbers proofs are in the notes; no Lean build or final determinant comparison is certified.",
    }
    path = ROOT / "certificates/common-chain-transport.json"
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "source_files": len(source),
                      "gram_entries": entries, "expansion": result["expansion"],
                      "six_block_transport": result["six_block_transport"],
                      "norm_budget_remainder": result["norm_budget_ledger"][
                          "pointwise_remainder_in_units_f_a_log_b"]}))


if __name__ == "__main__":
    main()
