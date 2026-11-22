#!/usr/bin/env python3
"""Pinned contracts and exact finite checks for diagonal arithmetic rigidity.

These checks verify formulas and provenance, not global class field theory,
the local ordinary deformation theorem, or existence of the arithmetic model.
"""

import gzip
import hashlib
import itertools
import json
from fractions import Fraction
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
U = BASE + "UnitaryThreeGroups."
SOURCES = [
    (BASE + "HeightAndVanishing.Counts", [(9, 22)]),
    (U + "RhoKApply", [(16, 33), (61, 83)]),
    (U + "DatFacts", [(68, 105), (130, 133)]),
    (U + "PtInertiaAway", [(54, 109)]),
    (U + "PtIneL", [(80, 116)]),
    (U + "RootOfCharpoly", [(126, 154), (189, 225)]),
    (U + "PowEqOneOfUnr", [(71, 129)]),
    (U + "IsPtOf", [(124, 166)]),
    (U + "ModelSigns", [(140, 186)]),
    (U + "GradedModelPointConditionOfPtHyp", [(53, 90)]),
    (U + "BlochKatoNonpositiveWeight",
     [(122, 153), (244, 289), (297, 340)]),
    (U + "TanCocIsBK", [(162, 190)]),
    (U + "PtHypOf", [(64, 89)]),
    (U + "Rigid0", [(16, 20)]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads(
        (ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["commit"] == REV
    blobs = {r[0]: r[1] for r in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        data = (ROOT / "build/source-cache/jsmorph/rh" / REV / path).read_bytes()
        blob = hashlib.sha1(
            b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == blobs[module], module
        lines = data.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpts.append({
                "lines": [lo, hi],
                "sha256": sha(b"\n".join(lines[lo-1:hi]) + b"\n"),
            })
        records.append({
            "repository": "jsmorph/rh", "commit": REV, "path": path,
            "sha256": sha(data), "git_blob_sha1": blob,
            "excerpts": excerpts,
        })
    return records


def identity():
    return [[int(i == j) for j in range(3)] for i in range(3)]


def mm(a, b, modulus):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) % modulus
             for j in range(3)] for i in range(3)]


def det3(a):
    return (a[0][0] * (a[1][1]*a[2][2] - a[1][2]*a[2][1])
            - a[0][1] * (a[1][0]*a[2][2] - a[1][2]*a[2][0])
            + a[0][2] * (a[1][0]*a[2][1] - a[1][1]*a[2][0]))


def permutation_matrix(g):
    return [[int(i == g[j]) for j in range(3)] for i in range(3)]


def inverse_permutation(g):
    return tuple(g.index(i) for i in range(3))


def averaging_case(prime, exponent, parameters):
    modulus = prime ** exponent
    a, b, c = parameters
    n = [[0, a, b], [0, 0, c], [0, 0, 0]]
    n2 = mm(n, n, modulus)
    s = [[(int(i == j) + prime*n[i][j]) % modulus
          for j in range(3)] for i in range(3)]
    si = [[(int(i == j) - prime*n[i][j] + prime**2*n2[i][j]) % modulus
           for j in range(3)] for i in range(3)]
    assert mm(s, si, modulus) == identity()
    group = list(itertools.permutations(range(3)))
    rho0 = {g: permutation_matrix(g) for g in group}
    rho = {g: mm(mm(si, rho0[g], modulus), s, modulus) for g in group}
    for g in group:
        assert all((rho[g][i][j]-rho0[g][i][j]) % prime == 0
                   for i in range(3) for j in range(3))
        for h in group:
            gh = tuple(g[h[i]] for i in range(3))
            assert mm(rho[g], rho[h], modulus) == rho[gh]
    summands = [mm(rho0[h], rho[inverse_permutation(h)], modulus) for h in group]
    m = [[sum(t[i][j] for t in summands)*pow(len(group), -1, modulus) % modulus
          for j in range(3)] for i in range(3)]
    assert all(m[i][j] % prime == int(i == j)
               for i in range(3) for j in range(3))
    assert gcd(det3(m), modulus) == 1
    for g in group:
        assert mm(rho0[g], m, modulus) == mm(m, rho[g], modulus)
    return m


def check_averaging():
    cases = reductions = 0
    parameters = [(0, 0, 0), (1, 1, 1), (1, -1, 2),
                  (2, 3, -1), (0, 1, 1), (1, 0, 1)]
    for prime in [5, 7, 11]:
        for abc in parameters:
            previous = None
            for exponent in [1, 2, 3]:
                m = averaging_case(prime, exponent, abc)
                cases += 1
                if previous is not None:
                    assert [[a % prime**(exponent-1) for a in row]
                            for row in m] == previous
                    reductions += 1
                previous = m
    return {"finite_S3_representations": cases,
            "compatible_coefficient_reductions": reductions,
            "intertwining_equalities": 6*cases,
            "coefficient_rings": "Z/ell^k, ell in {5,7,11}, k in {1,2,3}"}


def reduce_polynomial(coefficients, monic):
    p = list(coefficients)
    while p and p[-1] == 0:
        p.pop()
    degree = len(monic)-1
    while len(p) > degree:
        coefficient = p[-1]
        shift = len(p)-len(monic)
        for i, a in enumerate(monic):
            p[shift+i] -= coefficient*a
        while p and p[-1] == 0:
            p.pop()
    return tuple(p + [0]*(degree-len(p)))


def check_characters():
    cyclotomic = {
        3: [1, 1, 1], 4: [1, 0, 1], 5: [1, 1, 1, 1, 1],
        6: [1, -1, 1], 8: [1, 0, 0, 0, 1],
    }
    fourier = triples = matched = 0
    for order, polynomial in cyclotomic.items():
        def value(exponent):
            return reduce_polynomial(
                [0]*(exponent % order) + [1], polynomial)

        for i in range(order):
            for j in range(order):
                total = [0]*order
                for g in range(order):
                    total[((i-j)*g) % order] += 1
                expected = [order if i == j else 0]
                assert reduce_polynomial(total, polynomial) == reduce_polynomial(
                    expected, polynomial)
                fourier += 1
        target = [0, 1, order-1]
        for triple in itertools.product(range(order), repeat=3):
            trace_equal = all(
                tuple(sum(value(i*g)[k] for i in triple)
                      for k in range(len(polynomial)-1))
                == tuple(sum(value(i*g)[k] for i in target)
                         for k in range(len(polynomial)-1))
                for g in range(order))
            assert trace_equal == (sorted(triple) == target)
            triples += 1
            matched += int(trace_equal)
    residual = 0
    for prime in [5, 7, 11, 13, 17, 19]:
        for unit in range(1, prime):
            if unit*unit % prime == 1:
                continue
            values = [unit, 1, pow(unit, -1, prime)]
            assert len(set(values)) == 3
            matches = [p for p in itertools.permutations(range(3))
                       if [values[i] for i in p] == values]
            assert matches == [(0, 1, 2)]
            residual += 1
    return {"exact_cyclotomic_Fourier_pairs": fourier,
            "exact_character_triples": triples,
            "matching_trace_triples": matched,
            "residual_ordered_match_cases": residual,
            "scope": "Exact cyclotomic arithmetic; no floating-point roots."}


def check_unramified_torsion():
    tested = surviving = 0
    for prime in [3, 5, 7]:
        for exponent in range(1, 5):
            modulus = prime**exponent
            for order in range(1, 13):
                if gcd(order, prime) != 1:
                    continue
                for unit in range(1, modulus, prime):
                    geometric = sum(pow(unit, j, modulus)
                                    for j in range(order)) % modulus
                    assert geometric % prime == order % prime
                    assert gcd(geometric, modulus) == 1
                    assert (pow(unit, order, modulus) == 1) == (unit == 1)
                    tested += 1
                    surviving += int(unit == 1)
    # The coprimality assumption is essential even in a finite coefficient ring.
    assert 4 != 1 and 4 % 3 == 1 and pow(4, 3, 9) == 1
    return {"principal_unit_power_tests": tested,
            "trivial_solutions": surviving,
            "excluded_prime_control": {"modulus": 9, "unit": 4, "power": 3}}


def check_weight_zero():
    cases = 0
    # Complex conjugation on diagonal adjoint matrices: minus reversed entries.
    def action(v):
        return tuple(-x for x in reversed(v))

    for a, b in itertools.product(range(-4, 5), repeat=2):
        v = (Fraction(a), Fraction(b), Fraction(a))
        assert tuple(x+y for x, y in zip(v, action(v))) == (0, 0, 0)
        m = tuple(-x/2 for x in v)
        assert tuple(x-y for x, y in zip(action(m), m)) == v
        assert action(action(m)) == m
        cases += 1
    return {"exact_involution_cocycle_primitives": cases,
            "primitive": "-gamma(c)/2",
            "scope": "Explicit C2 calculation; the global class-field step is a proof, not a finite check."}


def main():
    sources = source_records()
    checks = {
        "integral_averaging": check_averaging(),
        "character_matching": check_characters(),
        "principal_unit_torsion": check_unramified_torsion(),
        "weight_zero_cocycles": check_weight_zero(),
    }
    artifacts = ["notes/rh-selmer-diagonal-rigidity.md",
                 "scripts/check_rh_selmer_diagonal_rigidity.py"]
    record = {
        "status": "pass", "date": "2026-11-22",
        "theorem": "Diagonal-point uniqueness and the weight-zero global rigidity argument for the actual marked character family, under the stated local conditions and good-prime restrictions.",
        "scope": [
            "Pinned source bytes and bounded source contracts are checked against the atlas.",
            "The integral averaging, character-independence, class-field, point-transfer and cocycle arguments are proved in the note.",
            "Exact finite computations check the averaging orientation and coefficient compatibility, cyclotomic trace matching, prime-to-ell torsion elimination, and the involution coboundary formula.",
            "The local ordinary inertia-trace theorem and the local finite-to-unramified tangent comparison are retained inputs, not consequences of these finite checks.",
            "Model existence, point lifting and density, finite weight-zero algebra, negative-weight rigidity, two-sided automorphic rigidity, and uniform Selmer bounds remain separate inputs.",
            "Characteristic-zero point or tangent rigidity does not assert absence of integral torsion.",
            "No full RH/GRH node or Lean build is claimed.",
        ],
        "sources": sources,
        "classical_reference": {
            "author": "J. S. Milne", "title": "Class Field Theory",
            "version": "4.03, 6 August 2020",
            "url": "https://www.jmilne.org/math/CourseNotes/CFTc.pdf",
            "location": "Chapter V, section 3, Theorems 3.5-3.6 and Example 3.9",
            "claim": "The maximal everywhere-unramified abelian extension is the Hilbert class field, with Galois group the ideal class group.",
            "checked": "2026-11-22; official PDF, bounded Hilbert-class-field passage",
        },
        "exact_checks": checks,
        "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())}
                      for p in artifacts],
        "independent_review_record": "certificates/hard-node-review-2026-11-22.json",
        "review_scope": "Automation-only verification here; mathematical review is recorded separately.",
    }
    output = ROOT / "certificates/rh-selmer-diagonal-rigidity.json"
    output.write_text(json.dumps(record, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "pass", "pinned_sources": len(sources),
                      "exact_checks": checks, "output": str(output.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
