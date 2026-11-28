#!/usr/bin/env python3
"""Exact finite checks for the cyclotomic crystalline-loss theorem.

No p-adic approximation is used. The integral cyclic basis and its
companion matrix are checked over Z, with a unit (N-1)-minor certifying
that the coinvariants have a single nonunit invariant factor. This
supplements the ordinary proof; it does not compute an automorphic
crystalline-loss constant or replay Lean.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from math import factorial, isqrt, prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMMIT = "72fead102f663d5c7a407964a13dc0cf9d977207"
SOURCES = {
    "New/Reduction/Data/AdmissibleData.lean":
        "48f73664d37f8b5036fcff2bf642d7be5e259907",
    "New/Determinant/Twist/FitTwists.lean":
        "27897e237e68320c4fb473e8ef98bde5c08f9265",
    "New/Determinant/Twist/LongForms.lean":
        "bc473640e088d1977bf33b0aa377d60540f4e66c",
    "New/OneLift/LiftVolumeHeight.lean":
        "7773d1334443460b5c920472da37b9e4b77ddb99",
    "New/OneLift/HeckeValues/TwistedValueHeights.lean":
        "ddfc466fb70a096b21707df61c6a0af498151f6c",
    "New/Congruences/LocalLoss/CrystallineDefect.lean":
        "c21212f774df81bff52003cbf8c6bf42ee2d7e95",
}
BK_SHA256 = "ec89c6436c7e16580791eddd562c8c04a12442d8a8484f8ac75c5ea8dc04f5e5"


def valuation(n: int, p: int) -> int:
    n = abs(n)
    assert n
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def determinant(matrix: list[list[int]]) -> int:
    """Exact rational elimination, with integral output checked."""
    n = len(matrix)
    if not n:
        return 1
    a = [[Fraction(x) for x in row] for row in matrix]
    answer = Fraction(1)
    for j in range(n):
        k = next((k for k in range(j, n) if a[k][j]), None)
        if k is None:
            return 0
        if k != j:
            a[j], a[k] = a[k], a[j]
            answer = -answer
        pivot = a[j][j]
        answer *= pivot
        for k in range(j + 1, n):
            scale = a[k][j] / pivot
            for t in range(j + 1, n):
                a[k][t] -= scale * a[j][t]
            a[k][j] = 0
    assert answer.denominator == 1
    return answer.numerator


def polynomial_with_roots(roots: list[int]) -> list[int]:
    """Ascending coefficients of the monic polynomial."""
    out = [1]
    for r in roots:
        new = [0] * (len(out) + 1)
        for i, c in enumerate(out):
            new[i] -= r * c
            new[i + 1] += c
        out = new
    return out


def check_cyclic_case(p: int, n: int) -> dict:
    a = 3 if p == 2 else 1
    weight_step = 2 if p == 2 else p - 1
    q = 1 + p**a
    roots = [q**j for j in range(1, n + 1)]
    coeff = polynomial_with_roots(roots)
    basis = [[(r - 1) * r**i for i in range(n)] for r in roots]
    companion = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        companion[i + 1][i] = 1
    for i in range(n):
        companion[i][-1] = -coeff[i]
    for i in range(n):
        for j in range(n):
            assert sum(basis[i][k] * companion[k][j] for k in range(n)) == (
                roots[i] * basis[i][j]
            )
    basis_det = determinant(basis)
    vandermonde = prod(r - 1 for r in roots) * prod(
        roots[j] - roots[i] for i in range(n) for j in range(i + 1, n)
    )
    assert basis_det == vandermonde != 0
    coinvariant = [
        [companion[i][j] - int(i == j) for j in range(n)] for i in range(n)
    ]
    coinvariant_det = determinant(coinvariant)
    p_at_one = sum(coeff)
    assert p_at_one == prod(1 - r for r in roots)
    assert coinvariant_det == (-1)**n * p_at_one
    unit_minor = determinant([row[: n - 1] for row in coinvariant[1:]])
    assert unit_minor == 1
    observed = valuation(coinvariant_det, p)
    expected = a * n + valuation(factorial(n), p)
    assert observed == expected
    for j, r in enumerate(roots, 1):
        assert valuation(r - 1, p) == a + valuation(j, p)
    return {
        "prime": p,
        "N": n,
        "q": q,
        "weight_width": weight_step * n,
        "exact_limiting_loss": observed,
        "relation_lattice_index_valuation": valuation(basis_det, p),
        "unit_maximal_minor": unit_minor,
        "precision_lengths": {
            str(k): min(k, observed)
            for k in sorted({1, max(1, observed - 1), observed, observed + 1})
        },
        "cyclic_basis_and_companion_verified": True,
    }


def divisors(n: int) -> list[int]:
    low = [d for d in range(1, isqrt(n) + 1) if n % d == 0]
    return sorted(set(low + [n // d for d in low]))


def primes_to(n: int) -> list[int]:
    prime = [True] * (n + 1)
    if n >= 0:
        prime[0] = False
    if n >= 1:
        prime[1] = False
    for p in range(2, isqrt(n) + 1):
        if prime[p]:
            for j in range(p * p, n + 1, p):
                prime[j] = False
    return [p for p in range(2, n + 1) if prime[p]]


def check_sparse_set(values: list[int]) -> dict:
    s = sorted(set(values) - {0})
    if not s:
        return {"weights": [], "Q": "1", "prime_power_bound": "1", "divides": True}
    count = len(s)
    width = max(abs(t) for t in s)
    exponents = {"2": 1 + sum(2 + valuation(t, 2) for t in s)}
    for p in primes_to(width + 1):
        if p == 2:
            continue
        a = sum(1 + valuation(t, p) for t in s if t % (p - 1) == 0)
        if a:
            exponents[str(p)] = a
    prime_power = prod(int(p)**a for p, a in exponents.items())
    q = 2**(1 + 2 * count) * prod(
        abs(t) * prod(d + 1 for d in divisors(abs(t))) for t in s
    )
    assert q % prime_power == 0
    return {
        "weights": s,
        "Q": str(q),
        "prime_power_bound": str(prime_power),
        "prime_exponents": exponents,
        "divides": True,
    }


def check_sources(source_root: Path) -> list[dict]:
    records = []
    for path, expected in SOURCES.items():
        local = source_root / path
        if not local.is_file():
            records.append({"path": path, "status": "unavailable"})
            continue
        data = local.read_bytes()
        actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert actual == expected, (path, actual, expected)
        records.append({"path": path, "git_blob_sha1": actual, "status": "verified"})
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-root", type=Path, default=ROOT / "build/readable-source/grh/src"
    )
    parser.add_argument(
        "--output", type=Path, default=ROOT / "certificates/exact-cyclotomic-loss.json"
    )
    args = parser.parse_args()
    cases = [check_cyclic_case(p, n) for p in [2, 3, 5, 7] for n in range(1, 9)]
    sparse = [
        check_sparse_set(s)
        for s in [
            [], [1], [2], [-2, 2], [-5, 7], list(range(1, 13)),
            [1, 2, 3, 97, 98, 99], [-1200, -1199, 1, 1199, 1200],
        ]
    ]
    pdf = ROOT / "build/crystalline-budget-reference/bloch-kato-tamagawa.pdf"
    bk = {"status": "unavailable", "expected_sha256": BK_SHA256}
    if pdf.is_file():
        actual = hashlib.sha256(pdf.read_bytes()).hexdigest()
        assert actual == BK_SHA256
        bk = {"status": "verified", "sha256": actual, "checked_statement": "Example 3.9, p. 359"}
    result = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed",
        "scope": "Exact finite algebra and source-byte checks; ordinary proof is in the linked note.",
        "not_claimed": [
            "Uniform effective loss for the actual nonabelian enlarged automorphic family",
            "A completed signed arithmetic budget",
            "A Lean replay",
        ],
        "source_commit": COMMIT,
        "ordinary_proof_note": {
            "path": "notes/lsernau-exact-cyclotomic-loss-and-budget.md",
            "sha256": hashlib.sha256(
                (ROOT / "notes/lsernau-exact-cyclotomic-loss-and-budget.md").read_bytes()
            ).hexdigest(),
        },
        "source_interfaces": check_sources(args.source_root),
        "bloch_kato_primary_pdf": bk,
        "cyclic_cases": cases,
        "sparse_weight_certificates": sparse,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "status": "passed",
        "cyclic_cases": len(cases),
        "sparse_weight_certificates": len(sparse),
        "source_files_verified": sum(r["status"] == "verified" for r in result["source_interfaces"]),
        "output": str(args.output.relative_to(ROOT)),
    }))


if __name__ == "__main__":
    main()
