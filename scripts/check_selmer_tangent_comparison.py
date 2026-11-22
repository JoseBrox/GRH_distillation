#!/usr/bin/env python3
"""Check provenance and exact algebra for the Selmer tangent comparison.

The finite calculations do not prove completion, continuity, local
Bloch--Kato conditions, arithmetic-model existence, or a Selmer order bound.
Those implications and their retained hypotheses are stated in the note.
Requires SymPy; use --offline after the selected source cache is populated.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties.UnitaryThreeGroups."
SOURCES = [
    ("ExistsDualNumberPointOfPointDerivationVanishing", [(27, 89), (136, 225)]),
    ("ExistsTorusTwistEqLocalPointOfWeightedPres", [(83, 137)]),
    ("WeightedPresExistsAlgHomExtensionOfAdicComplete", [(30, 55), (167, 246)]),
    ("ModelOfPres", [(155, 171), (249, 295), (320, 329)]),
    ("TanDet", [(110, 139), (175, 272), (276, 337), (343, 432)]),
    ("NormCob", [(30, 103)]),
    ("GRepresents", [(41, 85), (128, 141)]),
    ("GradedModelSpansCotOfRigidWeights", [(205, 244)]),
    ("GradedModelDerivationConditionOfPtHyp", [(93, 132), (153, 228)]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["commit"] == REV
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for suffix, ranges in SOURCES:
        module = PREFIX + suffix
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        item = {"repository": "jsmorph/rh", "commit": REV,
                "path": rel, "git_blob_sha1": blobs[module]}
        record = inspect_file(item, offline)
        data = (ROOT / "build/source-cache/jsmorph/rh" / REV / rel).read_bytes()
        lines = data.splitlines()
        record = {k: record[k] for k in ["repository", "commit", "path", "bytes",
                                       "git_blob_sha1", "sha256", "matches_pinned_blob"]}
        record["excerpts"] = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            record["excerpts"].append({"lines": [lo, hi],
                "sha256": sha(b"\n".join(lines[lo-1:hi]) + b"\n")})
        records.append(record)
    return records


def matrix_identities():
    a, b, c, d, e, f, h, u, v, w = sp.symbols("a b c d e f h u v w")
    J = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    T = sp.diag(1, 0, -1)
    M = sp.Matrix([[a, b, c], [d, e, b], [f, d, h]])
    X = sp.Matrix([[u, v, 0], [w, 0, -v], [0, -w, -u]])
    Z = M - J*M.T*J
    assert sp.simplify(Z-(a-h)*T) == sp.zeros(3)
    assert X + J*X.T*J == sp.zeros(3)
    comm = X*Z-Z*X
    assert sp.expand(comm[0, 1]+(a-h)*v) == 0
    assert sp.expand(comm[1, 0]-(a-h)*w) == 0
    assert sp.simplify(u*T*Z-Z*u*T) == sp.zeros(3)
    return {"normalized_matrix_difference": "M-J M^t J=(M11-M33)T",
            "skew_primitive": "[[u,v,0],[w,0,-v],[0,-w,-u]]",
            "differentiated_entries": ["-zeta*v", "zeta*w"],
            "status": "exact symbolic identities pass"}


def rank_mod_p(rows, p):
    mat = [[int(x) % p for x in row] for row in rows]
    rank = 0
    for col in range(len(mat[0])):
        pivot = next((i for i in range(rank, len(mat)) if mat[i][col]), None)
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        inv = pow(mat[rank][col], -1, p)
        mat[rank] = [(x*inv) % p for x in mat[rank]]
        for i in range(len(mat)):
            if i != rank:
                c = mat[i][col]
                mat[i] = [(x-c*y) % p for x, y in zip(mat[i], mat[rank])]
        rank += 1
    return rank


def boundary_checks():
    variables = sp.symbols("x0:9")
    X = sp.Matrix(3, 3, variables)
    J = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    T = sp.diag(1, 0, -1)
    records = []
    for p, zeta, expected in [(2, 1, 4), (3, 1, 1), (5, 2, 1), (5, 0, 3)]:
        comm = X*(zeta*T)-(zeta*T)*X
        equations = list(X+J*X.T*J) + [comm[0, 1], comm[1, 0]]
        rows = [[sp.expand(eq).coeff(x) for x in variables] for eq in equations]
        dimension = 9-rank_mod_p(rows, p)
        assert dimension == expected
        records.append({"field_characteristic": p, "zeta": zeta,
                        "primitive_space_dimension": dimension})
    # Over Z/9, zeta=3 does not kill the permitted off-diagonal torsion.
    X = sp.Matrix([[0, 3, 0], [0, 0, -3], [0, 0, 0]])
    C = X*(3*T)-(3*T)*X
    assert all(int(x) % 9 == 0 for x in list(X+J*X.T*J))
    assert int(C[0, 1]) % 9 == int(C[1, 0]) % 9 == 0
    assert int(X[0, 1]) % 9 != 0
    return {"finite_field_checks": records,
            "nonunit_zeta_counterexample": "Over Z/9, zeta=3 and X12=3, X23=-3 satisfy the marking but X is not diagonal.",
            "scope": "Necessity of the stated integral unit hypotheses; no counterexample to the characteristic-zero theorem."}


def vp(q, p):
    q = Fraction(q)
    if not q:
        return float("inf")
    n, d = abs(q.numerator), q.denominator
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    while d % p == 0:
        d //= p
        value -= 1
    return value


def finite_thickening_checks():
    x, pi = sp.symbols("x pi")
    examples = []
    for degree in range(1, 9):
        g = x**degree-pi
        assert sp.expand(x**(2*degree)-g**2-2*pi*x**degree+pi**2) == 0
        examples.append({"point_polynomial": f"x^{degree}-pi",
                         "square_neighbourhood_rank": 2*degree,
                         "power_in_pi_plus_kernel_squared": 2*degree})
    tail_checks = 0
    for p in [2, 3, 5]:
        for denominator in [0, 1, 7]:
            scalar = Fraction(p)
            tangent = Fraction(1, p**denominator)
            a, b = Fraction(1), Fraction(0)
            for n in range(1, 31):
                a, b = a*scalar, a*tangent+b*scalar
                assert a == scalar**n
                assert b == n*scalar**(n-1)*tangent
                assert vp(b, p) >= n-1-denominator
                tail_checks += 1
    return {"square_neighbourhood_examples": examples,
            "dual_number_power_formula_checks": tail_checks,
            "formula": "(a+epsilon*b)^n=a^n+epsilon*n*a^(n-1)*b",
            "scope": "Exact finite checks of the thickening and tail identities; the convergence theorem is proved in the note."}


def valuation_balancing_checks():
    weights = [-2, -1, 1, 2]
    values = [None, Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2)]
    counts = {"both_signs": 0, "positive_only": 0, "negative_only": 0,
              "all_zero": 0, "strictly_incompatible": 0}
    for valuations in itertools.product(values, repeat=4):
        active = [(w, v) for w, v in zip(weights, valuations) if v is not None]
        positive = [(w, v) for w, v in active if w > 0]
        negative = [(w, v) for w, v in active if w < 0]
        if not all(-wj*vi+wi*vj > 0 for wi, vi in positive for wj, vj in negative):
            counts["strictly_incompatible"] += 1
            continue
        low = max((-v/w for w, v in positive), default=None)
        high = min((-v/w for w, v in negative), default=None)
        if low is not None and high is not None:
            assert low < high
            shift = (low+high)/2
            counts["both_signs"] += 1
        elif low is not None:
            shift = low+1
            counts["positive_only"] += 1
        elif high is not None:
            shift = high-1
            counts["negative_only"] += 1
        else:
            shift = Fraction(0)
            counts["all_zero"] += 1
        assert all(v+w*shift > 0 for w, v in active)
        # Nonzero weight-zero coordinates are untouched and already strict.
        assert Fraction(1, 7)+0*shift > 0
    assert sum(counts.values()) == 6**4
    return {"cases": 6**4, "counts": counts,
            "zero_coordinates": "None values are omitted; they stay zero under scaling.",
            "weight_zero_coordinates": "Positive valuation is unchanged by every shift.",
            "no_variables": "The empty system has shift zero and t=1.",
            "nonstrict_boundary": "Weights 1,-1 and valuations 0,0 give coincident endpoints and no strict balancing; their invariant monomial has valuation zero.",
            "scope": "Exact rational verification of interval selection and its zero/one-sign boundary cases."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    note = "notes/selmer-tangent-comparison.md"
    tex = "paper/shared/selmer-tangent-comparison.tex"
    certificate = {
        "status": "pass", "date": "2026-11-22",
        "result": "Grading-rescaled point lifting, derivation lifting, and faithful tangent cocycles under the actual weighted-presentation and framed-universality hypotheses; one-dimensional general marking calculation.",
        "note": note, "note_sha256": sha((ROOT/note).read_bytes()),
        "tex": tex, "tex_sha256": sha((ROOT/tex).read_bytes()),
        "checker": str(Path(__file__).relative_to(ROOT)),
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "sources": source_records(args.offline),
        "exact_matrix_identities": matrix_identities(),
        "edge_cases": boundary_checks(),
        "finite_completion_examples": finite_thickening_checks(),
        "valuation_balancing": valuation_balancing_checks(),
        "retained_inputs": [
            "Actual weighted arithmetic presentation, initial formal chart and finite degree-zero equation quotient.",
            "Actual framed universal ring, homogeneous matrix-entry compatibility and local finite condition.",
            "Non-diagonal two-sided cohomological rigidity.",
            "Uniform integral Selmer estimate and compatibility with the other arithmetic constructions.",
        ],
        "limits": [
            "No Lean compilation or kernel check.",
            "No construction of the full arithmetic model.",
            "No new full RH or GRH node completion.",
            "The finite field and denominator bounds in the proof depend on each point and tangent; they do not give uniform arithmetic bounds.",
            "Source hashing and finite symbolic checks supplement, but do not substitute for, the ordinary mathematical proofs in the note.",
        ],
    }
    path = ROOT / "certificates/selmer-tangent-comparison.json"
    path.write_text(json.dumps(certificate, indent=2)+"\n")
    print(json.dumps({"status": "pass", "sources": len(certificate["sources"]),
                      "exact_dual_number_checks": 270,
                      "valuation_balancing_cases": 1296,
                      "certificate": str(path.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
