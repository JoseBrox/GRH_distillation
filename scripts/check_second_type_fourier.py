#!/usr/bin/env python3
"""Exact finite checks for the second-type Fourier argument.

This verifies finite models of its decisive dyadic/odd one-coordinate
identity and leakage bounds.  The all-field, all-conductor assertion is
proved in the manuscript; these finite checks are not a substitute.
Only Python integer arithmetic and fractions are used.
"""

from fractions import Fraction
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def norm(kind, p, x, y):
    if kind == "split":
        return x * y
    # Unramified quadratic models:
    # p=2: alpha^2+alpha+1=0; p=3: alpha^2+1=0.
    return x*x - x*y + y*y if p == 2 else x*x + y*y


def cyclic_convolve(a, b):
    m = len(a)
    return [sum(a[j] * b[(i-j) % m] for j in range(m))
            for i in range(m)]


def power_convolve(a, r):
    z = [1] + [0] * (len(a)-1)
    for _ in range(r):
        z = cyclic_convolve(z, a)
    return z


def squared_sum_is(p, m, counts, expected):
    """Equality in Z[zeta_m], m a power of p; no floating point."""
    c = [sum(counts[j] * counts[(j+i) % m] for j in range(m))
         for i in range(m)]
    c[0] -= expected
    d = m // p
    # Phi_{p^a}(X)=sum_{k=0}^{p-1} X^{kd}.
    return all(c[b+k*d] == c[b+(p-1)*d]
               for b in range(d) for k in range(p-1))


def main():
    cases = []
    total = 0
    for kind in ("split", "unramified"):
        for p, amax in ((2, 3), (3, 2)):
            for a in range(1, amax+1):
                m = p**a
                points = [(x, y, norm(kind, p, x, y) % m)
                          for x in range(m) for y in range(m)]
                checked = 0
                for t in range(1, m):
                    if t % p == 0:
                        continue
                    for u in range(m):
                        for v in range(m):
                            c = [0] * m
                            for x, y, n in points:
                                c[(t*n+u*x+v*y) % m] += 1
                            assert squared_sum_is(p, m, c, m*m), (
                                kind, p, a, t, u, v)
                            checked += 1
                # rho=4 is the lowest rank used in STC1--STC2.
                rho = 4
                counts = [0] * m
                first = [0] * m
                both = [0] * m
                for x, y, n in points:
                    counts[n] += 1
                    if x % p == 0:
                        first[n] += 1
                    if x % p == 0 and y % p == 0:
                        both[n] += 1
                denominator = m**(2*rho)
                density = Fraction(m * power_convolve(counts, rho)[0],
                                   denominator)
                eps = Fraction(1, p**(rho-1))
                assert abs(density-1) <= eps
                both_zero = power_convolve(both, rho)[0]
                if kind == "split":
                    # Two maximal ideals; subtract their intersection.
                    leak_count = 2*power_convolve(first, rho)[0]-both_zero
                    leak_bound = 2*(1+eps)*eps
                else:
                    leak_count = both_zero
                    leak_bound = (1+eps)*eps*eps
                leak = Fraction(m*leak_count, denominator)
                assert leak <= leak_bound
                cases.append({
                    "algebra": kind, "residue_size": p,
                    "conductor_exponent": a,
                    "primitive_quadratic_linear_sums_checked": checked,
                    "rho": rho, "scaled_density": str(density),
                    "density_error_bound": str(eps),
                    "scaled_leakage": str(leak),
                    "leakage_bound": str(leak_bound),
                })
                total += checked
    report = {
        "claim": "Exact finite one-coordinate Gauss identities and rank-four leakage checks.",
        "limits": "Only the listed finite unramified and split models; not a Lean replay or an all-field proof.",
        "method": "Integer phase histograms, exact cyclotomic reduction, cyclic convolution and fractions.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "total_gauss_sums": total,
        "cases": cases,
    }
    target = ROOT / "certificates/second-type-fourier.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Verified {total} exact Gauss sums and {len(cases)} density/leakage cases.")
    print(target.relative_to(ROOT))


if __name__ == "__main__":
    main()
