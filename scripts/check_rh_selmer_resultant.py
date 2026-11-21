#!/usr/bin/env python3
"""Check the resultant supplier and corrected common divisor.

Written proofs are primary. The exact finite examples below verify
normalization, multiplicities, empty cases and exceptional-prime handling;
they do not compute actual Selmer groups or automorphic trace spectra.
Only bounded source contracts are authenticated, without a Lean build.
"""

from fractions import Fraction
import gzip
import hashlib
import itertools
import json
from math import gcd
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
SOURCES = [
    ("AutomorphicForms.Classifies", [[10, 30]],
     "Exact Galois-stable trace multiset, size bound three, scaled integrality and injective classification."),
    ("BuildingsResidueChars.FrobeniusTraceNormNonzeroLogBound", [[7, 29], [41, 57]],
     "Actual simultaneous integer construction and valuation direction."),
    ("AutomorphicForms.CongruenceNumberRankThree", [[121, 140]],
     "Normalized Eisenstein trace, conductor/twist count and coefficient-prime exclusions."),
    ("AutomorphicForms.TemperedLocalComponents.CongruenceNumberRankThree", [[14, 32], [44, 63]],
     "Conditional spectral supplier, residue norm r^f with f<=2, polynomial spectral count."),
    ("UnitaryThreeGroups.KatoUse", [[36, 42], [54, 64]],
     "Same fixed host/twist/orbit for every auxiliary integer, and surviving trace-to-length contract."),
    ("UnitaryThreeGroups.CorGSumLog", [[37, 64]],
     "Two invocations with identical K,e,N,H bound the same orbit length."),
    ("UnitaryThreeGroups.OrbEquiv", [[151, 173]],
     "Character-orbit indexing, injective classification and normalized valuation consumer."),
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def source_records():
    raw = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    prior = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert digest(raw) == prior["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(raw))
    assert atlas["commit"] == REV
    blobs = {r[0]: r[1] for r in atlas["modules"]}
    out = []
    for suffix, ranges, role in SOURCES:
        module = PREFIX + suffix
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        cache = ROOT / "build/source-cache/jsmorph/rh" / REV / path
        data = cache.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == blobs[module]
        lines = data.splitlines()
        excerpts = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines) and end - start < 120
            excerpts.append({"lines": [start, end],
                             "sha256": digest(b"\n".join(lines[start-1:end]) + b"\n")})
        out.append({"repository": "jsmorph/rh", "commit": REV,
                    "module": module, "path": path, "sha256": digest(data),
                    "git_blob_sha1": blob, "excerpts": excerpts, "role": role})
    return out


def sylvester_det(f, g, x):
    f, g = sp.Poly(f, x), sp.Poly(g, x)
    m, n = f.degree(), g.degree()
    if m == 0:
        return int(f.LC() ** n)
    if n == 0:
        return int(g.LC() ** m)
    rows = []
    for shift in range(n):
        rows.append([0] * shift + f.all_coeffs() + [0] * (n - 1 - shift))
    for shift in range(m):
        rows.append([0] * shift + g.all_coeffs() + [0] * (m - 1 - shift))
    return int(sp.Matrix(rows).det(method="bareiss"))


def resultant_examples():
    x, t = sp.symbols("x t")
    cases = []
    # Algebraic, rational, repeated and empty trace/root multisets.
    for q, e, pcode, zcode in [
        (5, 1, "quadratic", 4), (7, 1, "quadratic", 4),
        (11, 1, "quadratic", 4), (5, 1, "upper", 1),
        (5, 1, "lower", 2), (7, 2, "quadratic", 8),
        (5, 2, "repeated", 4), (7, 1, "cubic", 4),
        (5, 1, "empty", 4), (5, 1, "quadratic", 0),
        (11, 1, "zero", 4), (7, 1, "repeated", -4),
    ]:
        a = q ** e
        P = {"quadratic": t*t-2*a*a, "upper": t-3*a,
             "lower": t+3*a, "repeated": (t-a)**2,
             "cubic": t**3-2*a**3, "empty": sp.Integer(1),
             "zero": t}[pcode]
        Z = (sp.Integer(1) if zcode == 0 else
             sp.cyclotomic_poly(abs(zcode), x) ** (2 if zcode < 0 else 1))
        R, m = sp.degree(P, t), sp.degree(Z, x)
        V = sp.Poly(sp.cancel(x**R * P.subs(t, x+a+a*a/x)), x)
        assert all(c.is_Integer for c in V.all_coeffs())
        n = int(sp.resultant(Z, V.as_expr(), x))
        independent = sylvester_det(Z, V.as_expr(), x)
        assert n == independent and n != 0
        assert abs(n) <= (a*a + 4*a + 1) ** (int(R) * int(m))
        if pcode == "quadratic" and zcode == 4:
            # At z=i, the argument is a-i(a^2-1); multiply its
            # P-value by its complex conjugate using integer arithmetic.
            b = a*a - 1
            direct = (a*a + b*b)**2 + 4*a*a*b*b
            assert n == direct
        cases.append({"q": q, "e": e, "trace_case": pcode,
                      "root_case": zcode, "P": str(P), "Z": str(Z),
                      "V": str(V.as_expr()), "resultant": n,
                      "sylvester_determinant": independent})
    return cases


def val(n, p):
    assert n > 0
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def common_divisor(A, B, r, s):
    return gcd(A // r**val(A, r), B // s**val(B, s)) * r**val(B, r) * s**val(A, s)


def common_divisor_examples(cases):
    checks = 0
    r, s, l = 7, 11, 3
    # Exhaust the small valuation triples independently of any spectrum.
    for ar, br, ass, bs, al, bl in itertools.product(range(3), repeat=6):
        A, B = r**ar*s**ass*l**al, r**br*s**bs*l**bl
        G = common_divisor(A, B, r, s)
        assert val(G, r) == br and val(G, s) == ass
        assert val(G, l) == min(al, bl) and (A*B) % G == 0
        checks += 1
    chosen = {c["q"]: abs(c["resultant"]) for c in cases
              if c["trace_case"] == "quadratic" and c["root_case"] == 4 and c["e"] == 1}
    A, B = chosen[7], chosen[11]
    G = common_divisor(A, B, 7, 11)
    assert G == 1
    # A case in which ordinary gcd is invalid at both excluded primes.
    A, B = 11**3 * 3**4, 7**2 * 3
    exceptional = common_divisor(A, B, 7, 11)
    assert exceptional == 7**2 * 11**3 * 3
    return {"exact_small_valuation_cases": checks,
            "coprime_synthetic_spectra": {"n_7": chosen[7], "n_11": chosen[11], "corrected_gcd": G},
            "exceptional_prime_example": {"A": A, "B": B, "ordinary_gcd": gcd(A, B), "corrected_gcd": exceptional}}


def main():
    # The edge a=5 supplies strict separation; both polynomials below
    # increase thereafter. No floating-point transcendental check is used.
    assert 5*5-4*5-1 == 4
    assert Fraction(4, 5) + Fraction(1, 25) < 1
    cases = resultant_examples()
    artifact_paths = ["notes/rh-selmer-resultant.md", "paper/shared/selmer-resultant.tex",
                      "scripts/check_rh_selmer_resultant.py"]
    report = {
        "schema_version": 1,
        "claim": "Explicit resultant gives the conditional simultaneous integer supplier; two integers bounding the same orbit length admit a corrected gcd bound.",
        "scope": ["Written ordinary-mathematical proofs are primary.",
                  "Bounded source contracts authenticated against pinned Git blobs.",
                  "Actual trace purity, integrality, counting and Selmer comparisons are retained as inputs, not independently re-proved upstream.",
                  "Exact synthetic algebraic checks only; no actual Selmer or automorphic computation.",
                  "No Lean build and no completion of a proof-map node."],
        "sources": source_records(),
        "exact_resultant_cases": cases,
        "corrected_gcd_checks": common_divisor_examples(cases),
        "artifacts": [{"path": p, "sha256": digest((ROOT / p).read_bytes())} for p in artifact_paths],
        "independent_review_record": "certificates/continuation-review-2026-11-22.json",
        "review_scope": "This checker records only automated source-integrity and exact finite checks. Independent mathematical review is recorded separately in the referenced continuation certificate.",
    }
    out = ROOT / "certificates/rh-selmer-resultant.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "pass", "sources": len(report["sources"]),
                      "resultant_examples": len(cases),
                      "gcd_cases": report["corrected_gcd_checks"]["exact_small_valuation_cases"],
                      "output": str(out.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
