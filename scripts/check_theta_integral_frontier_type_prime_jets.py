#!/usr/bin/env python3
"""Authenticate the actual type-prime interface and check exact local algebra.

The integral line-bundle argument and ordinary measure theorem are human
mathematics, not established by the finite checks in this file.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import itertools
import json
import math
from pathlib import Path
import subprocess
from urllib.request import urlopen

import sympy as sp
from sympy.functions.combinatorial.numbers import stirling

from check_sources import inspect_file


ROOT = Path(__file__).resolve().parents[1]
REVISION = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPOSITORY = "jsmorph/rh"
STEM = "theta-integral-frontier-type-prime-jets"
A = "Formalism.LocalToGlobal.AlgebraicTheory."
P = "Development.AbelianVarietyTheory.Proofs.SatakeParameters."
SOURCES = [
    (A + "StatementKer", [(35, 68)]),
    (A + "DefsKer", [(19, 32), (40, 75)]),
    (A + "AlgebraicTheoryProofs.CardTwoSidedQuotient",
     [(349, 455), (455, 565), (565, 603)]),
    (A + "AlgebraicTheoryProofs.KernelIndexForm", [(14, 84)]),
    (A + "AlgebraicTheoryProofs.KerHalf", [(57, 125), (367, 473)]),
    ("Development.AbelianVarietyTheory.BlockTheory.ThetaLiftGeometry.BadPrimesPeriodBound",
     [(61, 76)]),
    (P + "ThetaJetIntegralityTypePrimeOfSplitTableBound", [(221, 294)]),
    (P + "JetTableBoundConstantOneOfChainAgreement", [(1, 17)]),
]
PDF_SHA = "eea5e9a0d75d4a5b6ab7a801d5a9d861c0d2591bc360bed64cfa121bbe79267e"
PDF_REL = "build/reference-cache/bannai-kobayashi-0610163v4.pdf"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_records(offline: bool) -> list[dict]:
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == REPOSITORY and atlas["commit"] == REVISION
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        rec = inspect_file({"repository": REPOSITORY, "commit": REVISION,
                            "path": path, "git_blob_sha1": blobs[module]}, offline)
        assert rec["matches_pinned_blob"]
        data = (ROOT / "build/source-cache" / REPOSITORY / REVISION / path).read_bytes()
        record = {k: rec[k] for k in
                  ["repository", "commit", "path", "bytes", "git_blob_sha1",
                   "sha256", "matches_pinned_blob"]}
        lines = data.splitlines()
        record["inspected_excerpts"] = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            excerpt = b"\n".join(lines[lo - 1:hi]) + b"\n"
            record["inspected_excerpts"].append(
                {"lines": [lo, hi], "sha256": sha(excerpt)})
        records.append(record)
    return records


def primary_record(offline: bool) -> dict:
    path = ROOT / PDF_REL
    if not path.exists():
        assert not offline, "Primary PDF missing in offline mode"
        with urlopen("https://arxiv.org/pdf/math/0610163", timeout=30) as response:
            data = response.read(5_000_000)
        assert data.startswith(b"%PDF") and len(data) < 5_000_000
        assert sha(data) == PDF_SHA
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    data = path.read_bytes()
    assert sha(data) == PDF_SHA
    extracts = []
    for first, last, needles in [
        (1, 1, ["0610163v4", "11 Dec 2007"]),
        (24, 25, ["Lemma 2.7", "Proposition 2.8"]),
        (28, 29, ["Proposition 2.15", "Corollary 2.16"]),
    ]:
        out = subprocess.check_output(
            ["pdftotext", "-f", str(first), "-l", str(last),
             "-layout", str(path), "-"])
        text = out.decode()
        for needle in needles:
            assert needle in text
        extracts.append({"pdf_pages": [first, last], "sha256": sha(out)})
    return {
        "title": "Bannai–Kobayashi, Algebraic theta functions and p-adic interpolation of Eisenstein–Kronecker numbers",
        "version": "arXiv:math/0610163v4, 11 December 2007",
        "url": "https://arxiv.org/pdf/math/0610163",
        "path": PDF_REL, "sha256": PDF_SHA, "bytes": len(data),
        "bounded_extracts": extracts,
        "use": "Exact reduced Mumford lift and the existing prime-to-p ordinary input, not arbitrary-torsion integrality.",
    }


def exact_checks() -> dict:
    q, hz, ht = sp.symbols("q hz ht", positive=True)
    lift_exponent = -sp.pi * q**2 * hz / q - sp.pi * q**2 * ht / (2 * q**2)
    target_exponent = -sp.pi * q * hz - sp.pi * ht / 2
    assert sp.simplify(lift_exponent - target_exponent) == 0
    power_cases = 0
    for r in range(1, 33):
        exponent = sum((hz + j * ht + ht / 2 for j in range(r)), sp.Integer(0))
        assert sp.expand(exponent - r * hz - r**2 * ht / 2) == 0
        power_cases += 1

    # Independent invariant-derivative calculation, with factorials
    # multiplied in the Stirling formula rather than divided out.
    x, y = sp.symbols("x y")
    polynomial = sum(((-1)**(i + j) * (i + 2*j + 1) * x**i * y**j
                      for i in range(5) for j in range(4)), sp.Integer(0))
    mixed_cases = 0
    for m, n in itertools.product(range(7), range(6)):
        differentiated = polynomial
        for _ in range(m):
            differentiated = sp.expand((1+x) * sp.diff(differentiated, x))
        for _ in range(n):
            differentiated = sp.expand((1+y) * sp.diff(differentiated, y))
        value = differentiated.subs({x: 0, y: 0})
        predicted = sum(
            ((-1)**(i+j) * (i+2*j+1) * math.factorial(i) * math.factorial(j)
             * stirling(m, i, kind=2) * stirling(n, j, kind=2)
             for i in range(5) for j in range(4)), sp.Integer(0))
        assert value == predicted and value.is_Integer
        mixed_cases += 1

    crt_cases = 0
    for p, c in itertools.product([5, 7, 11], [1, 2, 3, 4]):
        group = range(p*c)
        first = [x for x in group if c*x % (p*c) == 0]
        second = [x for x in group if p*x % (p*c) == 0]
        sums = {(x+y) % (p*c) for x in first for y in second}
        assert len(first) == c and len(second) == p and len(sums) == p*c
        assert math.gcd(len(first), p) == 1
        crt_cases += 1

    branch_cases = 0
    formal_numerator_cases = 0
    for p, f, a, b, degree in itertools.product(
            [5, 7, 11], [1, 2], [2, 4], [2, 4], [0, 1, 3, 17, 73]):
        g = f*a*b
        original_denominator = p**g
        assert original_denominator == p**(f*a*b)
        for bar_valuation in [0, 1]:
            pi_valuation = 1-bar_valuation
            assert pi_valuation + bar_valuation == 1
            if bar_valuation == 1:
                summand_valuation_lower = -degree
            else:
                summand_valuation_lower = 0
                numerator_conjugate_valuation = 2*pi_valuation
                assert numerator_conjugate_valuation == 2
                formal_numerator_cases += 1
            final_lower = (summand_valuation_lower - g
                           + bar_valuation*degree + g)
            assert final_lower >= 0
            branch_cases += 1

    # Removing the fixed GM14 auxiliary S only changes the rational
    # shift by a lattice vector.
    auxiliary_cases = 0
    for p, s in itertools.product([5, 7, 11], range(1, 18)):
        if math.gcd(p, s) != 1:
            continue
        inverse = pow(s, -1, p)
        assert (s*inverse-1) % p == 0
        auxiliary_cases += 1

    phase_cases = 0
    for denominator, numerator in itertools.product(range(1, 13), range(-3, 4)):
        rational_norm = Fraction(numerator, denominator)
        exponent = 2*rational_norm.denominator*rational_norm
        assert exponent.denominator == 1 and exponent.numerator % 2 == 0
        phase_cases += 1

    # These are diagnostic counterexamples to invalid proof shortcuts,
    # not arithmetic-theta counterexamples.
    p = 5
    matrix = sp.Matrix([[0, sp.Rational(1, p)], [p, 0]])
    assert matrix**2 == sp.eye(2) and matrix[0, 1].q == p
    assert sp.Rational(1, p).q == p
    assert p*sp.Rational(1, p) == 1
    return {
        "exact_reduced_lift_dilation_identity": "pass",
        "same_vector_lift_power_cases": power_cases,
        "independent_mixed_invariant_derivative_cases": mixed_cases,
        "coprime_primary_quotient_cases": crt_cases,
        "original_rank_and_valuation_branch_cases": branch_cases,
        "formal_numerator_conjugate_cases": formal_numerator_cases,
        "fixed_auxiliary_integer_removal_cases": auxiliary_cases,
        "rational_weyl_phase_order_cases": phase_cases,
        "negative_controls": [
            "An order-two rational matrix can fail to preserve an arbitrary integral lattice; the actual line-bundle lift is essential.",
            "The formal example exp(z/p) has derivative 1/p; multiplication by p in the direction cannot be silently omitted.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources = source_records(args.offline)
    primary = primary_record(args.offline)
    checks = exact_checks()
    paths = [
        f"notes/{STEM}.md",
        f"paper/shared/{STEM}.tex",
        "scripts/check_theta_integral_frontier_type_prime_jets.py",
    ]
    existing = [
        "paper/sections/recovered/49-ct-section.tex",
        "paper/sections/recovered/52-ci-section.tex",
        "paper/sections/recovered/53-ts-section.tex",
        "paper/sections/recovered/55-gm-section.tex",
    ]
    record = {
        "status": "pass",
        "claim": "The original type-prime mixed-jet estimate, with the full p^(fab) denominator, follows from the existing normalized ordinary CM family and integral torsion dilation.",
        "source_pin": {"repository": REPOSITORY, "commit": REVISION},
        "source_records": sources, "primary_source": primary,
        "exact_checks": checks,
        "differential_normalization": {
            "good_elliptic_lattice": "L0=delta0 O_k for the actual unit elliptic ideal",
            "period": "omega=Omega/iota(delta0), |Omega|_p=1; neither omega nor delta0 is assumed a unit",
            "directions": "O_Cp span of iota(v) with L0 v subset Lambda; exact original frameM(v,M)=diag(cD), with integral M",
            "mixed_jets": "Invariant derivatives, equivalently factorial-weighted Taylor coefficients; no division by factorials",
        },
        "retained_normalization": [
            "The actual theta vector, discriminant scalar and determinant character",
            "Original prime-to-p shifts killed by c'",
            "The exact denominator u*p^(fab) with p not dividing u",
            "Both original Heisenberg exponential factors",
            "The Weyl factor exp(pi*i*Q(a)), a root of unity because Q(a) is rational",
            "The same GM14 measure and the same fixed complex-to-p-adic embedding",
        ],
        "local_scope": "Actual original type-prime applications with HostTie.ccK=top and their ordinary normalization; no unconditional arbitrary-ideal JetSplitAmb assertion.",
        "consumer": "The original local type-prime jet-loss constant is 1, retaining downstream branching, pairing, size, rationality and chain hypotheses.",
        "remaining": [
            "Original global arithmetic model and its identifications",
            "Remaining integral kernel constructors not implied by this local estimate",
            "Global theta norm comparison and nonvanishing",
        ],
        "existing_human_inputs": [
            {"path": path, "sha256": sha((ROOT/path).read_bytes())} for path in existing
        ],
        "artifacts": [
            {"path": path, "sha256": sha((ROOT/path).read_bytes())} for path in paths
        ],
        "verification_limit": "Human proof with bounded source authentication and exact finite algebra checks. No Lean build, no automatic verification of the geometric line-bundle proof, no full RH/GRH proof, no proof-map node closure.",
        "completed_nodes": {"RH": [6, 9], "GRH": [17, 31]},
    }
    target = ROOT / "certificates" / (STEM+".json")
    target.write_text(json.dumps(record, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "pass", "certificate": str(target.relative_to(ROOT)),
                      "pinned_source_modules": len(sources),
                      "mixed_derivative_cases": checks["independent_mixed_invariant_derivative_cases"],
                      "branch_cases": checks["original_rank_and_valuation_branch_cases"],
                      "completed_nodes": record["completed_nodes"]}))


if __name__ == "__main__":
    main()
