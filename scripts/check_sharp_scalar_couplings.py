#!/usr/bin/env python3
"""Exact finite checks for the sharp-scalar reconstruction.

These check source bytes, cancellation and finite coefficient/weight algebra.
They do not prove the formal-group, theta, or global analytic theorems.
Run from any directory; output is certificates/sharp-scalar-couplings.json.
"""
from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import product
import json
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
REV = "72fead102f663d5c7a407964a13dc0cf9d977207"
CACHE = ROOT / "build/source-cache/lsernau/grh-lean" / REV / "grh/src"
SOURCES = {
    "New/Derivatives/Sharpness/OneCurve.lean": "bffd16c21bf4be8f99e4a9db98dcbfc9d6048bcb",
    "New/Derivatives/Sharpness/LeastValuation.lean": "57023e123c8d731e02af8ce58748a8648b0c5c4e",
    "New/Derivatives/Sharpness/Couplings.lean": "de96c06ef8d3c8188cf780b6387ef34e18d71d38",
    "New/Derivatives/Sharpness/NearPairs.lean": "213027e16cbb8cd0e7d982f12f7fd8dc3fcd538a",
    "New/Derivatives/Sharpness/Cases.lean": "a492b67e2c6c1c1eefec78337d5fc09b46dd6019",
    "New/Derivatives/Sharpness/BoundAttained.lean": "95fc1fb8b13805ce9c96a3fe84f8c103d6d8f2f4",
    "New/Derivatives/Vacuum/ShortVectors.lean": "836f43b9a3648434ff409824c0662bef38463071",
    "New/Reduction/Data/AdmissibleData.lean": "48f73664d37f8b5036fcff2bf642d7be5e259907",
    "New/Reduction/Data/FieldsAndPlaces.lean": "8b0a085a2f5aaa75d02863607df1dc7f304018fc",
}


def vf(n: int, p: int) -> int:
    total = 0
    while n:
        n //= p
        total += n
    return total


def vb(n: int, length: int, p: int) -> int:
    lo = max(n - length, 0)
    return vf(lo + length, p) - vf(lo, p)


def primes(n: int) -> list[int]:
    return [p for p in range(2, n + 1) if all(p % a for a in range(2, int(p**0.5) + 1))]


def source_checks() -> list[dict]:
    rows = []
    for path, expected in SOURCES.items():
        target = CACHE / path
        if target.exists():
            data = target.read_bytes()
        else:
            url = "https://raw.githubusercontent.com/lsernau/grh-lean/" + REV + "/grh/src/" + path
            with urlopen(url, timeout=30) as response:
                data = response.read()
        actual = sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert actual == expected, (path, actual, expected)
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        rows.append({"path": path, "git_blob_sha1": actual,
                     "sha256": sha256(data).hexdigest(), "bytes": len(data)})
    return rows


def cancellation_checks() -> dict:
    odd = []
    for p in primes(101)[1:]:
        a, b = next((a, b) for a in range(p) for b in range(p)
                    if (1 + a*a + b*b) % p == 0)
        assert a or b
        odd.append({"p": p, "a": a, "b": b})
    root = 1
    for n in range(3, 40):
        if (root*root + 7) % (2 ** (n + 1)):
            root += 2 ** (n - 1)
        assert (root*root + 7) % (2 ** (n + 1)) == 0
    assert (1 + root*root + 1 + 1 + 4) % (2**40) == 0
    assert all((a*a + b*b + c*c) % 8 != 7 for a, b, c in product(range(8), repeat=3))
    return {"odd_prime_residue_solutions": odd, "dyadic_precision": 40,
            "sqrt_minus_seven_residue": root, "dyadic_three_square_obstruction_mod_8": True}


def coefficient_checks() -> int:
    import sympy as sp
    count = 0
    for p, dim in product((3, 5, 7), (2, 3)):
        z = sp.symbols("z0:" + str(dim))
        xi = sum(z[i]**p * z[(i + 1) % dim] for i in range(dim)) + p*sum(z)
        # kappa=1/p. The exact normalized repeated derivative is
        # g -> g*d(xi)/dz_t + p*dg/dz_t; W=1.
        for js in product(range(3), repeat=dim):
            g = sp.Poly(1, *z)
            for i, multiplicity in enumerate(js):
                t = z[(i + 1) % dim]
                a = sp.Poly(sp.diff(xi, t), *z)
                for _ in range(multiplicity):
                    g = g*a + p*g.diff(t)
            lead = tuple(p*j for j in js)
            expected = sp.Poly(sp.prod(z[i]**lead[i] for i in range(dim)), *z)
            assert all(int(c) % p == 0 for c in (g - expected).coeffs())
            u = sp.Poly(1 + sum(z) + sum(t*t for t in z), *z)
            assert int((g*u).coeff_monomial(lead)) % p == 1
            count += 1
    return count


def large_prime_checks() -> int:
    count = 0
    for b, k in product((13, 41, 160, 1000), range(1, 31)):
        length = (6*b + k - 1)//k
        for p in primes(47):
            if p <= max(2, k):
                continue
            for weight, other_weight in product((0, 1, b//7, b), repeat=2):
                for excess in (0, min(3, length), min(b, length)):
                    ell = weight + excess
                    if ell > 2*b:
                        continue
                    i = max(ell-length, 0)//p
                    assert i <= length
                    j = min(i, other_weight)
                    assert vf(ell, p) - j <= max(F(weight, p)-other_weight, 0) + 2*vb(ell, length, p)
                    count += 1
    return count


def partner_minimum(weight: int, weights: list[int], t: int, p: int) -> F:
    dim = len(weights)
    total, e = F(0), 1
    while F(weight, p**e) > min(weights):
        total += min(F(weight, p**e), weights[(t + e) % dim])
        e += 2
    return total + F(weight, p**e) / (1 - F(1, p*p))


def sparse_checks() -> dict:
    count, nonempty, max_carry = 0, 0, 0
    b, u, eps = 100_000_000, 50, 2
    for dim in range(3, 10):
        for cutoff in range(4, min(9, dim + 2)):
            for flags in product((False, True), repeat=dim):
                B = {i for i, flag in enumerate(flags) if flag}
                if any(t in B and (t+i) % dim in B and (t+j) % dim in B
                       for t in B for i in range(1, cutoff) for j in range(i+1, cutoff)):
                    continue
                near = [(t, e) for t in B for e in range(1, cutoff, 2)
                        if 2*e < cutoff and (t+e) % dim in B]
                starts, ends = [t for t, e in near], [(t+e) % dim for t, e in near]
                assert len(starts) == len(set(starts))
                assert len(ends) == len(set(ends))
                assert not set(starts).intersection(ends)
                for t, e in near:
                    assert all((s, a) == (t, e) for s in starts for a in range(1, e+1, 2)
                               if (s+a) % dim == (t+e) % dim)
                weights = [b if t in B else u for t in range(dim)]
                ell = [w + (t % (eps + 1)) for t, w in enumerate(weights)]
                for p in (3, 5, 7, 13):
                    k = p
                    length = (6*b + k - 1)//k
                    nu1, nu2, J = [0]*dim, [0]*dim, 0
                    for t, e in near:
                        j = ell[t]//(p**e)
                        nu1[t] += p**e*j
                        nu2[(t+e) % dim] += j
                        J += j
                    assert all(a+c <= l for a, c, l in zip(nu1, nu2, ell))
                    carry = sum(vf(l, p)-vf(a, p)-vf(c, p)-vf(l-a-c, p)
                                for a, c, l in zip(nu1, nu2, ell))
                    max_carry = max(max_carry, carry)
                    gamma = F(p, p*p-1)
                    R = sum(partner_minimum(w, weights, t, p) for t, w in enumerate(weights))
                    S = gamma*sum(weights)-R
                    assert gamma*sum(ell)-J+carry <= S + sum(vb(l, length, p) for l in ell)
                    count += 1
                    nonempty += bool(near)
    return {"weight_cases": count, "with_nonempty_near_pair_family": nonempty,
            "maximum_exact_total_carry": max_carry, "weight_b": b, "off_weight": u}


def main() -> None:
    result = {
        "schema_version": 1,
        "source_revision": REV,
        "scope": "Finite exact algebra, arithmetic inequalities and pinned source bytes only; no Lean build or analytic proof verification.",
        "source_files": source_checks(),
        "cancellation": cancellation_checks(),
        "logarithmic_derivative_coefficient_cases": coefficient_checks(),
        "large_prime_weight_cases": large_prime_checks(),
        "sparse_near_pair_checks": sparse_checks(),
    }
    path = ROOT / "certificates/sharp-scalar-couplings.json"
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"source_files": len(result["source_files"]),
                      "coefficient_cases": result["logarithmic_derivative_coefficient_cases"],
                      "large_prime_cases": result["large_prime_weight_cases"],
                      "sparse_cases": result["sparse_near_pair_checks"], "output": str(path)}, indent=2))


if __name__ == "__main__":
    main()
