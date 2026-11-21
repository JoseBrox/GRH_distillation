#!/usr/bin/env python3
"""Exact finite checks for the transport/symmetry-defect identities.

No floating point is used. Logarithms of primes and the correction constants
are formal symbols; all their coefficients are rational. The character
family is the full eight-character multiquadratic quotient of modulus 105.
This exercises primitive values at the ramified primes 3, 5 and 7.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GROUP = list(product(range(2), repeat=3))
PHI = [g for g in GROUP if g[0] == 0]
PRIMES = (3, 5, 7)
C = (1, 1, 0)


def add(g, h):
    return tuple((x + y) % 2 for x, y in zip(g, h))


def pair(chi, g):
    return (-1) ** sum(x * y for x, y in zip(chi, g))


def primitive_value(chi, n):
    value = 1
    for bit, p in zip(chi, PRIMES):
        if bit:
            r = n % p
            if not r:
                return 0
            value *= 1 if pow(r, (p - 1) // 2, p) == 1 else -1
    return value


def factor(n):
    result = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            result[d] = result.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def prime_power(n):
    f = factor(n)
    return next(iter(f)) if len(f) == 1 else None


def clean(polynomial):
    return {k: v for k, v in polynomial.items() if v}


def combine(target, source, scalar=F(1)):
    for symbol, value in source.items():
        target[symbol] += scalar * value


def logarithm(q):
    q = F(q)
    out = defaultdict(F)
    for p, k in factor(q.numerator).items():
        out[f"log({p})"] += k
    for p, k in factor(q.denominator).items():
        out[f"log({p})"] -= k
    return clean(out)


def h(chi, a, w):
    out = defaultdict(F)
    for n in range(2, int(a / w) + 1):
        p = prime_power(n)
        if p is not None:
            out[f"log({p})"] += primitive_value(chi, n) * (a / n - w)
    if chi == (0, 0, 0):
        combine(out, logarithm(w), a)
        combine(out, logarithm(a), -a)
        out["1"] += a
        out["gamma"] += a
    else:
        out[f"Lprime/L:{chi}"] += a
    return clean(out)


def kappa(g, n, characters=GROUP):
    return sum(pair(chi, g) * primitive_value(chi, n) for chi in characters)


def cumulative(measure, r):
    return sum((p for w, p in measure if w <= r), F(0))


def arithmetic_balance(measures, orders, characters=GROUP):
    out = defaultdict(F)
    for t, a in orders.items():
        for rho in PHI:
            g = add(add(C, (0, 0, t)), rho)
            for chi in characters:
                coefficient = F(pair(chi, g), len(PHI))
                for w, p in measures[rho]:
                    combine(out, h(chi, a, w), coefficient * p)
    return clean(out)


def difference(left, right):
    out = defaultdict(F)
    combine(out, left)
    combine(out, right, -1)
    return clean(out)


def radial_residual(mu, nu, orders):
    out = defaultdict(F)
    weights = {w for measure in mu.values() for w, _ in measure}
    ell, upper = min(weights), max(weights)
    for t, a in orders.items():
        cuts = weights | {
            a / n for n in range(2, int(a / ell) + 1)
            if prime_power(n) is not None and ell < a / n < upper
        }
        cuts = sorted(cuts)
        for left, right in zip(cuts, cuts[1:]):
            r = (left + right) / 2
            for rho in PHI:
                delta = cumulative(mu[rho], r) - cumulative(nu[rho], r)
                g = add(add(C, (0, 0, t)), rho)
                for n in range(2, int(a / r) + 1):
                    p = prime_power(n)
                    if p is not None:
                        out[f"log({p})"] += (
                            (right - left) * delta * kappa(g, n) / len(PHI)
                        )
    return clean(out)


def encode(polynomial):
    return {k: str(v) for k, v in sorted(polynomial.items())}


def main():
    kernel_count = 0
    ramified_count = 0
    xchars = [chi for chi in GROUP if chi[2] == 0]
    for n in range(2, 201):
        p = prime_power(n)
        if p is None:
            continue
        values = [kappa(g, n) for g in GROUP]
        assert min(values) >= 0 and sum(values) == len(GROUP)
        for g in GROUP:
            projected = F(kappa(g, n) + kappa(add(g, (0, 0, 1)), n), 2)
            assert projected == kappa(g, n, xchars)
            kernel_count += 1
            ramified_count += int(p in PRIMES)
        for shift in GROUP:
            assert sum(kappa(add(shift, rho), n) for rho in PHI) <= len(GROUP)

    profiles = {
        (0, 0, 0): (1, 2), (0, 0, 1): (4, 8),
        (0, 1, 0): (2, 4), (0, 1, 1): (1, 8),
    }
    mu = {rho: [(F(w), F(1, 2)) for w in ws] for rho, ws in profiles.items()}
    nu = {
        rho: [(w, p / 2) for v in (0, 1)
              for w, p in mu[add(rho, (0, 0, v))]] for rho in PHI
    }
    orders = {0: F(8), 1: F(16)}
    full = arithmetic_balance(mu, orders)
    symmetrized = arithmetic_balance(nu, orders)
    projected = arithmetic_balance(mu, orders, xchars)
    assert symmetrized == projected
    residual = difference(full, projected)
    assert residual and residual == radial_residual(mu, nu, orders)
    assert all(symbol.startswith("log(") for symbol in residual)

    cuts = sorted({w for measure in mu.values() for w, _ in measure})
    delta_star = defaultdict(F)
    individual = {rho: defaultdict(F) for rho in PHI}
    for left, right in zip(cuts, cuts[1:]):
        r = (left + right) / 2
        ds = {rho: abs(cumulative(mu[rho], r) - cumulative(nu[rho], r))
              for rho in PHI}
        combine(delta_star, logarithm(right / left), max(ds.values()))
        for rho in PHI:
            combine(individual[rho], logarithm(right / left), ds[rho])
    assert clean(delta_star) == {"log(2)": F(1)}

    b, radius = F(5), F(1, 3)
    stop_loss = ((b - (b - radius)) + 0) / 2
    assert stop_loss == radius / 2
    assert sum(w * p for w, p in [(b - radius, F(1, 2)),
                                  (b + radius, F(1, 2))]) == b

    # On the separated source-like band [U,L], tau=1/4.
    tau = F(1, 4)
    ds_top, ds_outer = -(1 - tau), tau
    assert max(abs(ds_top), abs(ds_outer)) == F(3, 4)
    assert tau * abs(ds_top) + (1 - tau) * abs(ds_outer) == F(3, 8)

    note = ROOT / "notes/transport-symmetry-defect.md"
    certificate = {
        "status": "all exact finite checks passed",
        "scope": "finite rational/formal-log checks; not a theta construction or Lean build",
        "character_family": "eight primitive quadratic products at conductors dividing 105",
        "kernel_character_checks": kernel_count,
        "ramified_kernel_checks": ramified_count,
        "projection_identity": True,
        "signed_radial_identity": True,
        "nonzero_residual": encode(residual),
        "logarithmic_cumulative_cost": encode(clean(delta_star)),
        "sharp_equal_mean_hinge_factor": "1/2",
        "separated_band_maximum_factor_at_density_1_over_4": "3/4",
        "separated_band_average_factor_at_density_1_over_4": "3/8",
        "independent_review": {
            "reviewer": "geometric_simplify",
            "result": "PASS",
            "scope": "sections 2–3 and section 1 dependencies; mathematical proof, not source realization",
            "checked": [
                "primitive conductor and inertia including ramified primes",
                "positive kernel and total mass at most 2f",
                "symmetrization equals character projection",
                "constant and principal-log cancellation",
                "signed hinge/CDF integral and finite interchange",
                "2C_Psi and normalized 4C_Psi/d factors",
                "positive-weight support and endpoint cases",
            ],
        },
        "note_sha256": hashlib.sha256(note.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    path = ROOT / "certificates/transport-symmetry-defect.json"
    path.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: certificate[k] for k in
                      ("status", "kernel_character_checks", "ramified_kernel_checks",
                       "projection_identity", "signed_radial_identity")}, sort_keys=True))


if __name__ == "__main__":
    main()
