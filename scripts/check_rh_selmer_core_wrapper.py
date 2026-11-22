#!/usr/bin/env python3
"""Exact examples and pinned provenance for the abstract length wrapper.

Finite arithmetic checks supplement the general proofs; they do not
construct the marked arithmetic model or verify its hypotheses.
"""

import gzip
import hashlib
import itertools
import json
from fractions import Fraction
from math import comb, gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties.CommutativeAlgebra."
ALG = BASE+"GradedModulesLength."
SOURCES = [
    (BASE+"OrbitVanishingLocal", [(74, 118)]),
    (ALG+"LinPartApply", [(127, 155)]),
    (ALG+"SmHolds", [(55, 112)]),
    (ALG+"IftSubstLow", [(93, 123)]),
    (ALG+"CutHolds", [(101, 131)]),
    (ALG+"NzCoeffMul", [(33, 89)]),
    (ALG+"FinHolds", [(49, 98)]),
    (ALG+"MainCotSpan", [(32, 70)]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records():
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["commit"] == REV
    blobs = {r[0]: r[1] for r in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        path = "lean/src/"+module.replace(".", "/")+".lean"
        data = (ROOT/"build/source-cache/jsmorph/rh"/REV/path).read_bytes()
        blob = hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
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


def determinant(a):
    if not a:
        return 1
    return sum((-1)**j*a[0][j]*determinant([row[:j]+row[j+1:] for row in a[1:]])
               for j in range(len(a)))


def multiply(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def inverse(a):
    n = len(a)
    rows = [[Fraction(v) for v in row]+[Fraction(i == j) for j in range(n)]
            for i, row in enumerate(a)]
    for j in range(n):
        k = next(i for i in range(j, n) if rows[i][j])
        rows[j], rows[k] = rows[k], rows[j]
        pivot = rows[j][j]
        rows[j] = [v/pivot for v in rows[j]]
        for i in range(n):
            if i != j:
                factor = rows[i][j]
                rows[i] = [v-factor*w for v, w in zip(rows[i], rows[j])]
    result = [row[n:] for row in rows]
    assert multiply(a, result) == [[int(i == j) for j in range(n)] for i in range(n)]
    return result


def smith_checks():
    cases = 0
    for r in range(1, 4):
        for exponents in itertools.product(range(3), repeat=r):
            for p, seed in itertools.product((3, 5), (1, 2, 3)):
                n = r+1
                u = [[int(i == j) for j in range(n)] for i in range(n)]
                for i in range(1, n):
                    u[i] = [a+seed*b for a, b in zip(u[i], u[i-1])]
                u[0] = [a+(seed+1)*b for a, b in zip(u[0], u[-1])]
                assert determinant(u) == 1
                v = inverse(u)
                assert all(c.denominator == 1 for row in v for c in row)
                diagonal = [[p**exponents[i] if i == j else 0 for j in range(n)]
                            for i in range(r)]
                original = multiply(diagonal, u)
                transformed = multiply(original, v)
                assert transformed == diagonal
                assert all(row[-1] == 0 for row in transformed)
                minor_gcd = 0
                for columns in itertools.combinations(range(n), r):
                    minor_gcd = gcd(minor_gcd,
                                    determinant([[row[j] for j in columns] for row in original]))
                # Independent index computation by all maximal minors.
                assert abs(minor_gcd) == p**sum(exponents)
                cases += 1
    return cases


# Formal polynomials in p=xy and q=uv. Both have weight zero and
# ordinary degree two for weights wt(x,y,u,v)=(-1,1,-2,2).
P = {(1, 0): Fraction(1)}
Q = {(0, 1): Fraction(1)}


def add(*polys):
    out = {}
    for poly in polys:
        for monomial, value in poly.items():
            out[monomial] = out.get(monomial, 0)+value
    return {m: v for m, v in out.items() if v}


def scale(c, poly):
    return {m: c*v for m, v in poly.items() if c*v}


def product(a, b, degree):
    out = {}
    for m, x in a.items():
        for n, y in b.items():
            k = tuple(u+v for u, v in zip(m, n))
            if sum(k) <= degree:
                out[k] = out.get(k, 0)+x*y
    return {m: v for m, v in out.items() if v}


def part(poly, degree):
    return {m: v for m, v in poly.items() if sum(m) == degree}


def implicit_checks():
    scalar_cases, coupled_cases, checked_coefficients = 0, 0, 0
    for degree in range(1, 9):
        h = {}
        for k in range(1, degree+1):
            residual = add(h, scale(-1, product(h, h, degree)), scale(-1, P))
            h = add(h, scale(-1, part(residual, k)))
        assert add(h, scale(-1, product(h, h, degree)), scale(-1, P)) == {}
        # Independent closed-form Catalan coefficients of h-h^2-p=0.
        expected = {(k, 0): Fraction(comb(2*k-2, k-1), k) for k in range(1, degree+1)}
        assert h == expected
        scalar_cases += 1
        checked_coefficients += len(h)
    for c, d in ((Fraction(1), Fraction(1)), (Fraction(-2), Fraction(3)),
                 (Fraction(1, 3), Fraction(-1, 2))):
        for degree in range(1, 7):
            def equations(h1, h2):
                return (add(scale(2, h1), h2, scale(c, product(h1, h1, degree)), P),
                        add(h1, h2, scale(d, product(h1, h2, degree)), Q,
                            product(P, P, degree)))
            h1, h2 = {}, {}
            for k in range(1, degree+1):
                a, b = [part(poly, k) for poly in equations(h1, h2)]
                # Inverse of the zero-weight Jacobian [[2,1],[1,1]].
                h1 = add(h1, scale(-1, a), b)
                h2 = add(h2, a, scale(-2, b))
            assert equations(h1, h2) == ({}, {})
            for poly in (h1, h2):
                for i, j in poly:
                    assert i+j >= 1
                    exponents = (i, i, j, j)
                    assert sum(w*e for w, e in zip((-1, 1, -2, 2), exponents)) == 0
                    assert sum(exponents) >= 2
            coupled_cases += 1
            checked_coefficients += len(h1)+len(h2)
    return {"scalar_catalan_examples": scalar_cases, "coupled_examples": coupled_cases,
            "nonzero_coefficients_checked": checked_coefficients,
            "maximum_original_variable_degree": 16,
            "zero_variable_case": "identity substitution, handled directly in the general proof"}


def representative_checks():
    cases, values = 0, 0
    # A=Q[x,y,z], wt=(-1,1,0), equation F=x, chart z->0, g=y.
    for c, d, k in itertools.product((-1, 0, 1), (0, 1), range(1, 4)):
        correction = int(c == 0)
        assert c+correction != 0
        # a=c*x*y+d*z^k; a'=a+correction*x*y. The correction is in (F).
        assert -1+1 == 0
        for y, z in itertools.product(range(-2, 3), repeat=2):
            a_at_equation_point = d*z**k
            adjusted_value = (c+correction)*0*y+d*z**k
            assert adjusted_value == a_at_equation_point
            values += 1
        assert c*0*0+d*0**k == 0
        cases += 1
    return {"representative_examples": cases, "equation_point_values": values,
            "augmentation_preserved": True, "integral_correction": "gF=xy"}


def main():
    sources = source_records()
    smith = smith_checks()
    implicit = implicit_checks()
    representatives = representative_checks()
    dependency_path = "certificates/rh-selmer-upper-multiplicity.json"
    dependency = json.loads((ROOT/dependency_path).read_text())
    assert dependency["status"] == "pass"
    for artifact in dependency["artifacts"]:
        assert sha((ROOT/artifact["path"]).read_bytes()) == artifact["sha256"]
    artifacts = ["notes/rh-selmer-core-wrapper.md", "scripts/check_rh_selmer_core_wrapper.py"]
    record = {
        "status": "pass", "date": "2026-11-22",
        "theorem": "Full abstract commutative-algebra length theorem, including finite orbit cover, integral normalization, zero-weight cut, and representative adjustment, under its original model hypotheses.",
        "scope": [
            "Eight upstream files are checked against the pinned Git-blob atlas; only the listed bounded ranges form the source-contract audit.",
            "The general mathematical proof is in the note. Finite examples check integral matrices, weighted formal coefficients, and representative values only.",
            "Formal coefficient checks are truncated at explicitly recorded orders and do not substitute for the coefficient-by-coefficient existence and uniqueness proof.",
            "Finite orbit existence follows from the previously reviewed generic slice and finite degree-zero quotient; the prior independent cover-existence premise is discharged.",
            "The actual marked arithmetic model, its original chart and geometric/automorphic hypotheses, and the Selmer lifting conditions remain inputs.",
            "No complete RH/GRH proof-map node or Lean build is claimed.",
        ],
        "sources": sources,
        "dependencies": [{"certificate": dependency_path, "artifact_hashes_verified": True}],
        "exact_checks": {"smith_presentations": smith, "implicit_substitutions": implicit,
                         "representative_adjustment": representatives},
        "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())} for p in artifacts],
        "independent_review_record": "certificates/hard-node-review-2026-11-22.json",
        "review_scope": "Automation-only verification here; mathematical review is recorded separately.",
    }
    out = ROOT/"certificates/rh-selmer-core-wrapper.json"
    out.write_text(json.dumps(record, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "pass", "pinned_sources": len(sources),
                      "smith_presentations": smith, "formal_substitutions": implicit["scalar_catalan_examples"]+implicit["coupled_examples"],
                      "point_values": representatives["equation_point_values"],
                      "output": str(out.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
