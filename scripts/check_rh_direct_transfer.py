#!/usr/bin/env python3
"""Exact supplemental checks of the symmetry-free RH transfer.

No Lean build or proof of the remaining arithmetic construction is implied.
The general inequalities are proved in notes/rh-direct-transfer.md.
"""
from fractions import Fraction as F
from itertools import product
from math import gcd
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def cadd(z, w):
    return z[0] + w[0], z[1] + w[1]


def cmul(z, w):
    return z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0]


def ipow(e):
    return [(1, 0), (0, 1), (-1, 0), (0, -1)][e % 4]


def primitive_kernel_checks():
    # U(15) = <-1> x <2>, of orders 2 and 4. Values are Gaussian integers.
    coords = {((-1)**a * 2**b) % 15: (a, b)
              for a, b in product(range(2), range(4))}
    chars = {}
    for k, j in product(range(2), range(4)):
        val = {u: ipow(2*k*a + j*b) for u, (a, b) in coords.items()}
        conductor = next(d for d in [1, 3, 5, 15]
                         if all(val[u] == val[v]
                                for u in coords for v in coords if (u-v) % d == 0))
        def primitive(n, d=conductor, v=val):
            if gcd(n, d) != 1:
                return (0, 0)
            return v[next(u for u in coords if (u-n) % d == 0)]
        chars[k, j] = primitive
    count = 0
    for p, r, ga, gb in product([2, 3, 5, 7, 11], range(1, 5), range(2), range(4)):
        total = (0, 0)
        for (k, j), chi in chars.items():
            total = cadd(total, cmul(ipow(-2*k*ga-j*gb), chi(p**r)))
        if p == 3:
            # Quotient by U(3); coordinate residues correspond to the value mod 5.
            expected = 4 if ((-1)**ga * 2**gb - p**r) % 5 == 0 else 0
        elif p == 5:
            expected = 2 if ((-1)**ga * 2**gb - p**r) % 3 == 0 else 0
        else:
            expected = 8 if ((-1)**ga * 2**gb - p**r) % 15 == 0 else 0
        assert total == (expected, 0), (p, r, ga, gb, total, expected)
        count += 1
    return count


def quadratic(p, modulus):
    if gcd(p, modulus) != 1:
        return 0
    if modulus == 4:
        return 1 if p % 4 == 1 else -1
    return 1 if pow(p % modulus, (modulus-1)//2, modulus) == 1 else -1


def kernel(g, n):
    total = 0
    for sig, tau, lam in product(range(2), repeat=3):
        chi = 1
        for exponent, modulus in [(sig, 7), (tau, 3), (lam, 4)]:
            if exponent:
                chi *= quadratic(n, modulus)
        total += (-1)**(sig*g[0]+tau*g[1]+lam*g[2])*chi
    assert total >= 0
    return total


def thick_checks():
    # Exact checks term by term in the positive prime-power coefficients.
    # The principal logarithmic correction has a nonnegative difference.
    count = 0
    n, f, b, width = 2, 4, F(2), F(1, 2)
    subsets = [(0,), (1,), (0, 1)]
    for p, power, S, T, m in product([2, 3, 5, 7, 11, 13, 17], range(1, 4), subsets, subsets, [1, 2]):
        N = p**power
        density = F(len(S), n)
        k = len(T)*m*b*density/2
        lhs, base, psi = F(0), F(0), F(0)
        for t in T:
            a = F(12+3*t)
            kplus = (1+quadratic(N, 3))*(1-quadratic(N, 7))
            base += b*kplus*max(a/(b*N)-1, F(0))
            psi += kplus if N <= a/b else 0
            for u, i, v in product(range(n), range(m), S):
                rho = (v+u) % n
                g = (1, 0, (rho-t) % n)
                w = b + width*F((u+2*i+rho) % 4, 3)
                assert b <= w <= b+width <= a
                lhs += kernel(g, N)*max(a/N-w, F(0))/(n*f)
        rhs = k*base/(len(T)*b) - m*density*width*psi/2
        assert lhs >= rhs, (p, power, S, T, m, lhs, rhs)
        count += 1
    return count


def normalization_checks():
    count = 0
    for n in range(1, 13):
        f = 2*n
        for s in range(1, n+1):
            for m, nt in product([1, 3], [1, 4]):
                density, b, abar, theta = F(s, n), F(5), F(17), F(1, 101)
                k = nt*m*b*density/2
                exact = 2*m*(f-s)*theta*nt*abar/k
                proposed = 2*f*(2-density)*abar*theta/(density*b)
                assert exact == proposed
                count += 1
    return count


def quotient_checks():
    # G=(C2)^4, A=(C2)^2, from quadratic characters of conductors7,3,4,5.
    A = list(product(range(2), repeat=2))
    Bs = [[(0, 0)], [(0, 0), (1, 0)], [(0, 0), (0, 1)],
          [(0, 0), (1, 1)], A]
    chars = list(product(range(2), repeat=4))
    def chi(psi, N):
        ans = 1
        for exponent, modulus in zip(psi, [7, 3, 4, 5]):
            if exponent:
                ans *= quadratic(N, modulus)
        return ans
    def coefficient(g, N, chosen):
        return sum((-1)**sum(x*y for x, y in zip(psi, g))*chi(psi, N)
                   for psi in chosen)
    count = 0
    n, f, b, width = 4, 8, F(3), F(2, 3)
    for B in Bs:
        X = [psi for psi in chars if all((psi[2]*u[0]+psi[3]*u[1]) % 2 == 0 for u in B)]
        sets = {tuple(B), (B[0],), (B[-1],)}
        for S, T, p, power in product(sets, [[A[0]], A], [2, 3, 5, 7, 11, 13], [1, 2]):
            N, m = p**power, 2
            density = F(len(S), n)
            k = len(T)*m*b*density/2
            actual, frozen, loss = F(0), F(0), F(0)
            for t in T:
                a = F(15+2*t[0]+t[1])
                qcoeff = coefficient((1, 0, t[0], t[1]), N, X)
                assert 0 <= qcoeff <= F(4*n, len(B))
                frozen += qcoeff*max(a/N-b, F(0))
                loss += qcoeff if N <= a/b else 0
                for u, i, s in product(B, range(m), S):
                    g = (1, 0, (s[0]+u[0]-t[0]) % 2, (s[1]+u[1]-t[1]) % 2)
                    w = b+width*F((u[0]+u[1]+i+s[0]) % 3, 2)
                    c = coefficient(g, N, chars)
                    assert c >= 0
                    actual += c*max(a/N-w, F(0))/(len(B)*f)
                for s in S:
                    summed = sum(coefficient((1, 0, (s[0]+u[0]-t[0]) % 2,
                                              (s[1]+u[1]-t[1]) % 2), N, chars)
                                 for u in B)
                    assert summed == len(B)*qcoeff
            rhs = k*frozen/(len(T)*b) - m*len(S)*width*loss/f
            assert actual >= rhs
            count += 1
    return count


def main():
    results = {
        "primitive_fourier_cases_including_ramification": primitive_kernel_checks(),
        "one_sided_thick_freezing_cases": thick_checks(),
        "thin_normalization_cases": normalization_checks(),
        "general_subgroup_positive_transfer_cases": quotient_checks(),
    }
    paths = ["notes/rh-direct-transfer.md", "notes/positive-kernel-transfer.md",
             "scripts/check_rh_direct_transfer.py"]
    pin = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
    sources = []
    for path, expected, intervals in [
        ("lean/src/Development/AutomorphicArithmetic/DedekindLFunctions/SplitInertia.lean",
         "b5662cda1f3523fc53b547ee582a46bd3cd826d4", [(42, 48)]),
        ("lean/src/Formalism/SizeWindowBrackets/SChain.lean",
         "a4bc8cecac40a1f5fd307661e151639aaf6a6efa", [(50, 58)]),
    ]:
        data = (ROOT/"build/source-cache/jsmorph/rh"/pin/path).read_bytes()
        actual = hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
        assert actual == expected, path
        lines = data.decode().splitlines(keepends=True)
        sources.append({"repository": "jsmorph/rh", "commit": pin,
                        "path": path, "git_blob_sha1": actual,
                        "sha256": hashlib.sha256(data).hexdigest(),
                        "ranges": [{"start": start, "end": end,
                                    "sha256": hashlib.sha256("".join(lines[start-1:end]).encode()).hexdigest()}
                                   for start, end in intervals]})
    certificate = {
        "schema_version": 1,
        "claim": "Exact supplemental finite checks of primitive Fourier positivity and the RH thick/thin transfer.",
        "results": results,
        "sources": sources,
        "mathematical_review": {
            "reviewers": ["rh_source_symmetry", "transport_defect", "geometric_simplify"],
            "outcome": "PASS after relaxing the local envelope statement to b <= w <= a and w-b <= r.",
            "scope": "RH written proof and manuscript integration, primitive/ramified coefficients, signs, counts, source numerical substitutions, sampled domains, and extension to any subgroup with fixed or controlled quotient index; no new Lean build."
        },
        "limitations": ["Finite checks supplement the general written proof.",
                        "The uniform QRH input and compatible arithmetic/geometric construction are not proved by this script."],
        "files": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in paths]
    }
    output = ROOT / "certificates/rh-direct-transfer.json"
    output.write_text(json.dumps(certificate, indent=2)+"\n")
    print(json.dumps({"status": "PASS", **results}))


if __name__ == "__main__":
    main()
