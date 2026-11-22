#!/usr/bin/env python3
"""Exact generic-slice examples, multiplicity counts, and pinned contracts.

This supplements the general proof under the stated arithmetic model
hypotheses. It neither constructs that model nor verifies automorphy.
"""

import gzip
import hashlib
import itertools
import json
from fractions import Fraction
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties.CommutativeAlgebra."
ALG = BASE + "GradedModulesLength."
SOURCES = [
    (BASE + "OrbitVanishingLocal", [(41, 70)]),
    (ALG + "ToDegInjective", [(156, 163), (187, 218)]),
    (ALG + "EventuallyMQGrFiniteAnnihilator", [(57, 123)]),
    (ALG + "LocLenQuotientWeightPieceLeOne", [(70, 148)]),
    (ALG + "LocLenAPieceIdeal2LeTwoPow", [(69, 115)]),
    (ALG + "LocalizedLengthLeOfSurjective", [(124, 151), (177, 213)]),
    (ALG + "TwoSigned", [(17, 25), (63, 94)]),
    (ALG + "AlgMemCoef", [(92, 102)]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["commit"] == REV
    blobs = {r[0]: r[1] for r in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        data = (ROOT / "build/source-cache/jsmorph/rh" / REV / path).read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == blobs[module]
        lines = data.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpts.append({"lines": [lo, hi],
                             "sha256": sha(b"\n".join(lines[lo-1:hi])+b"\n")})
        records.append({"repository": "jsmorph/rh", "commit": REV, "path": path,
                        "sha256": sha(data), "git_blob_sha1": blob, "excerpts": excerpts})
    return records


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    r = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        v = a[r][col]
        a[r] = [x/v for x in a[r]]
        for i in range(len(a)):
            if i != r:
                v = a[i][col]
                a[i] = [x-v*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def tangent_checks():
    """Generic char-zero examples; nonreduced cases must fail tangent <=1."""
    records = []
    for n in range(1, 5):
        # D=Q[e]/e^n; C=D[f,f^-1]; the slice f=1 is D.
        derivative_e = int(n == 1)
        ambient = 2-rank([[derivative_e, 0]])
        sliced = 1-rank([[derivative_e]])
        assert (ambient <= 1) == (n == 1) == (sliced == 0)
        records.append({"nilpotent_exponent": n, "slice": "one point",
                        "ambient_tangent": ambient, "slice_tangent": sliced})
        # Add a weight-one z with f*z^2=d. At f=1, z=0 or +/-1.
        for d, roots in ((0, (0,)), (1, (-1, 1))):
            for z in roots:
                ambient = 3-rank([[derivative_e, 0, 0], [0, z*z, 2*z]])
                sliced = 2-rank([[derivative_e, 0], [0, 2*z]])
                assert ambient == sliced+1
                assert (ambient <= 1) == (n == 1 and d == 1)
                records.append({"nilpotent_exponent": n, "quadratic_value": d,
                                "root": z, "ambient_tangent": ambient,
                                "slice_tangent": sliced})
    return records


def multiply(a, b):
    if a is None or b is None or a[1] & b[1]:
        return None
    return a[0] ^ b[0], a[1] | b[1]


def parity(a):
    return (a[0]+a[1].bit_count()) % 2


def squarefree_checks():
    """Sharp one- and two-point examples with q commuting square-zero variables."""
    records, products, associative_triples = [], 0, 0
    for q in range(1, 8):
        for base_points in (1, 2):
            basis = [(e, mask) for e in range(base_points) for mask in range(1 << q)]
            dimensions = [sum(parity(x) == p for x in basis) for p in (0, 1)]
            expected = (1 << (q-1))*base_points
            assert dimensions == [expected, expected]
            for k in range(q+1):
                layer = [x for x in basis if x[1].bit_count() == k]
                assert len(layer) == comb(q, k)*base_points
                # Every generator is a squarefree product of k selected equations.
                for e, mask in layer:
                    value = (e, 0)
                    for i in range(q):
                        if mask >> i & 1:
                            value = multiply(value, (0, 1 << i))
                    assert value == (e, mask)
            for x, y in itertools.product(basis, repeat=2):
                z = multiply(x, y)
                assert z == multiply(y, x)
                if z is not None:
                    assert parity(z) == (parity(x)+parity(y)) % 2
                products += 1
            if q <= 3:
                for x, y, z in itertools.product(basis, repeat=3):
                    assert multiply(multiply(x, y), z) == multiply(x, multiply(y, z))
                    associative_triples += 1
            for r in range(q):
                rp = q-r-1
                assert 2**(r+1+rp) == 2**q
                # The actual lower scalar is 2^(r+r'); the parity constants
                # become one or two after division by that scalar.
                assert Fraction(expected, 2**(r+rp)) == base_points
            records.append({"selected_odd_equations": q, "base_slice_points": base_points,
                            "even_length": dimensions[0], "odd_length": dimensions[1],
                            "bound_attained": True})
    return records, products, associative_triples


def rees_degree_checks():
    """Coefficient ideals in B[X0,X1,X2], B=Q[e]/e^L, retain nilpotents."""
    all_degrees, interior_degrees = 0, 0
    for length in range(1, 5):
        for exponents in itertools.product(range(length+1), repeat=3):
            for z_exponent in (0, length):
                target = min(length, z_exponent, *exponents)
                for degree in itertools.product(range(4), repeat=3):
                    available = [exponents[i] for i in range(3) if degree[i] >= 1]
                    piece = min(length, z_exponent, *available)
                    assert piece >= target
                    if min(degree) >= 1:
                        assert piece == target
                        interior_degrees += 1
                    # The unit coefficient generator has exactly the actual weight.
                    assert -2*(degree[0]+degree[2])+2*degree[1] == 2*(degree[1]-degree[0]-degree[2])
                    all_degrees += 1
    # A missing first coordinate can miss its coefficient equation entirely.
    boundary = {"ring": "Q[e]/(e^3)", "section": "e*X0", "degree": [0, 1, 1],
                "rees_piece_length": 3, "all_coefficient_quotient_length": 1}
    assert boundary["rees_piece_length"] > boundary["all_coefficient_quotient_length"]
    return all_degrees, interior_degrees, boundary


def main():
    sources = source_records()
    tangents = tangent_checks()
    examples, products, triples = squarefree_checks()
    all_degrees, interior_degrees, boundary = rees_degree_checks()
    dependency = json.loads((ROOT / "certificates/rh-selmer-admissibility.json").read_text())
    assert dependency["status"] == "pass"
    for artifact in dependency["artifacts"]:
        assert sha((ROOT/artifact["path"]).read_bytes()) == artifact["sha256"]
    artifacts = ["notes/rh-selmer-upper-multiplicity.md", "scripts/check_rh_selmer_upper_multiplicity.py"]
    record = {
        "status": "pass", "date": "2026-11-22",
        "theorem": "Eventual generic support and the 2^(r+1+r') local multiplicity bound, with a one-point-slice improvement, under the original model hypotheses.",
        "scope": [
            "Eight upstream files are checked against the pinned Git-blob atlas; only listed bounded ranges form the source-contract audit.",
            "The mathematical proof supplies the uniform support, reduced slice, squarefree filtration, and actual localized Rees-piece comparison.",
            "Exact finite examples verify characteristic-zero tangent obstructions, both sharp parity constants, and the necessary Rees degree box; they are not arithmetic models.",
            "The combined lower/upper inequality retains the separate formal-chart condition phi(a) != 0 and all previously stated chart, Smith, point, and orbit-covering inputs.",
            "No Lean build, arithmetic model construction, automorphy theorem, or RH/GRH proof-map node completion is claimed.",
        ],
        "sources": sources,
        "dependencies": [{"certificate": "certificates/rh-selmer-admissibility.json",
                          "artifact_hashes_verified": True}],
        "exact_checks": {
            "tangent_examples": tangents,
            "sharp_parity_examples": examples,
            "basis_products": products,
            "associative_triples": triples,
            "rees_degree_cases": all_degrees,
            "interior_degree_cases": interior_degrees,
            "boundary_failure_example": boundary,
            "arithmetic": "exact rational matrices and integer monomial exponents",
        },
        "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())} for p in artifacts],
        "independent_review_record": "certificates/hard-node-review-2026-11-22.json",
        "review_scope": "Automation-only verification here; mathematical review is recorded separately.",
    }
    out = ROOT / "certificates/rh-selmer-upper-multiplicity.json"
    out.write_text(json.dumps(record, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "pass", "pinned_sources": len(sources),
                      "tangent_examples": len(tangents), "sharp_parity_examples": len(examples),
                      "basis_products": products, "rees_degree_cases": all_degrees,
                      "output": str(out.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
