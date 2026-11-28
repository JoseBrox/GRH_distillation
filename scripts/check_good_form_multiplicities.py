#!/usr/bin/env python3
"""Exact checks of the sign and finite cuspidal-projector conventions.

No analytic trace formula or automorphic multiplicity is computed. The proof
of comparison is in notes/lsernau-good-form-multiplicities.md. This script
checks its elementary sign and projector normalizations independently, using
all regular degree-two Green characters for GL_2(F_2) and GL_2(F_3).
Only Python's standard library is required; cyclotomic arithmetic is exact.
"""
from __future__ import annotations

from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Cyclotomic:
    """Z[zeta_3] or Z[zeta_8], represented in the power basis."""

    def __init__(self, order: int):
        assert order in (3, 8)
        self.order = order
        self.degree = 2 if order == 3 else 4
        self.zero = (0,) * self.degree
        self.one = (1,) + (0,) * (self.degree - 1)
        self.powers = [self.reduce([0] * j + [1]) for j in range(order)]

    def reduce(self, a):
        a = list(a) + [0] * self.degree
        for j in range(len(a) - 1, self.degree - 1, -1):
            c = a[j]
            if self.order == 3:
                a[j - 1] -= c
                a[j - 2] -= c
            else:
                a[j - 4] -= c
        return tuple(a[:self.degree])

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def scale(self, k, a):
        return tuple(k * x for x in a)

    def mul(self, a, b):
        ans = [0] * (2 * self.degree - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                ans[i + j] += x * y
        return self.reduce(ans)

    def conjugate(self, a):
        ans = self.zero
        for j, x in enumerate(a):
            ans = self.add(ans, self.scale(x, self.powers[-j % self.order]))
        return ans


def group_check(q):
    ring = Cyclotomic(q * q - 1)
    # F_4 = F_2[t]/(t^2+t+1), F_9 = F_3[t]/(t^2+1).
    def fm(x, y):
        a, b = x
        c, d = y
        return ((a*c + (1 if q == 2 else 2)*b*d) % q,
                (a*d + b*c + (b*d if q == 2 else 0)) % q)

    def fp(x, n):
        ans = (1, 0)
        for _ in range(n):
            ans = fm(ans, x)
        return ans

    gen = (0, 1) if q == 2 else (1, 1)
    logs = {fp(gen, j): j for j in range(q*q - 1)}
    assert len(logs) == q*q - 1
    assert fp(gen, q*q - 1) == (1, 0)

    def mul(g, h):
        a, b, c, d = g
        e, f, j, k = h
        return ((a*e+b*j) % q, (a*f+b*k) % q,
                (c*e+d*j) % q, (c*f+d*k) % q)

    def inv(g):
        a, b, c, d = g
        t = pow((a*d-b*c) % q, -1, q)
        return (t*d % q, -t*b % q, -t*c % q, t*a % q)

    group = [g for g in product(range(q), repeat=4)
             if (g[0]*g[3]-g[1]*g[2]) % q]
    identity = (1, 0, 0, 1)
    order = len(group)
    assert order == (q*q-1)*(q*q-q)
    assert all(mul(g, inv(g)) == identity for g in group)
    reps = [m for m in range(q*q-1)
            if m != q*m % (q*q-1) and m < q*m % (q*q-1)]
    chars = []
    rows = []
    for m in reps:
        def theta(x):
            return ring.powers[m*logs[x] % ring.order]

        def character(g):
            a, b, c, d = g
            tr, det = (a+d) % q, (a*d-b*c) % q
            roots = [x for x in range(q) if (x*x-tr*x+det) % q == 0]
            if len(roots) == 2:
                return ring.zero
            if roots:
                scalar = b == c == 0 and a == d
                return ring.scale(q-1 if scalar else -1, theta((roots[0], 0)))
            roots2 = [x for x in logs
                      if tuple((u+v) % q for u, v in zip(x, fp(x, q))) == (tr, 0)
                      and fm(x, fp(x, q)) == (det, 0)]
            assert len(roots2) == 2
            alpha = roots2[0]
            return ring.scale(-1, ring.add(theta(alpha), theta(fp(alpha, q))))

        chi = {g: character(g) for g in group}
        assert chi[identity] == ring.scale(q-1, ring.one)
        assert all(chi[inv(g)] == ring.conjugate(chi[g]) for g in group)
        # Cuspidality: every translated unipotent sum has zero character.
        for g in group:
            for upper in (False, True):
                total = ring.zero
                for t in range(q):
                    u = (1, t, 0, 1) if upper else (1, 0, t, 1)
                    total = ring.add(total, chi[mul(g, u)])
                assert total == ring.zero
        # With counting convolution, e(g) = dim(tau)/|G| chi(g^-1).
        # Clear denominators to check e*e=e entirely in the integer ring.
        raw = {g: chi[inv(g)] for g in group}
        for g in group:
            total = ring.zero
            for h in group:
                total = ring.add(total, ring.mul(raw[h], raw[mul(inv(h), g)]))
            assert ring.scale(q-1, total) == ring.scale(order, raw[g])
        chars.append(chi)
        rows.append({"character_exponent": m, "dimension": q-1,
                     "projector_regular_rank": (q-1)**2,
                     "unipotent_cosets_checked": 2*order,
                     "convolution_coefficients_checked": order})
    for i, chi in enumerate(chars):
        for j, other in enumerate(chars):
            total = ring.zero
            for g in group:
                total = ring.add(total, ring.mul(chi[g], ring.conjugate(other[g])))
            assert total == ring.scale(order if i == j else 0, ring.one)
    return {"q": q, "group_order": order, "cuspidal_characters": rows,
            "character_inner_products_checked": len(chars)**2}


def main():
    sign_cases = 0
    for n in range(1, 13):
        for degree in range(1, 5):
            by_parity = {}
            for signatures in product(range(n+1), repeat=degree):
                det_parity = sum(signatures) % 2
                sign = sum(q*(n-q) for q in signatures) % 2
                assert sign == (n-1)*det_parity % 2
                assert by_parity.setdefault(det_parity, sign) == sign
                sign_cases += 1
    result = {
        "status": "passed",
        "scope": "Finite sign and cuspidal-projector conventions only; not an analytic trace-formula or multiplicity proof.",
        "signature_tuples_checked": sign_cases,
        "finite_groups": [group_check(q) for q in (2, 3)],
    }
    path = ROOT / "certificates/good-form-multiplicity-conventions.json"
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Passed {sign_cases} signature tuples and all regular GL2(F2), GL2(F3) cuspidal projectors.")
    print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
