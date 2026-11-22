#!/usr/bin/env python3
"""Bounded provenance and exact algebra for the strict Selmer conormal pairing.

The general pairing is proved in ordinary mathematics, not by these finite tests.
No actual growing deformation model or Selmer group is computed here.
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
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
SOURCES = [
    ("CommutativeAlgebra.ResMapBijective", [(231, 267)]),
    ("CommutativeAlgebra.OrbitVanishingLocal", [(21, 25), (86, 128)]),
    ("CommutativeAlgebra.GradedModulesLength.Mprime", [(38, 80)]),
    ("UnitaryThreeGroups.ConjStable", [(22, 37), (54, 90)]),
    ("UnitaryThreeGroups.ExistsBasePointDerivationOfWeightHomogeneous", [(48, 80), (81, 134)]),
    ("UnitaryThreeGroups.ModelOfPres", [(145, 153), (174, 211), (221, 258), (295, 317)]),
    ("UnitaryThreeGroups.BaseRepGL3NormalisedOfPsiEqOne", [(45, 73)]),
    ("UnitaryThreeGroups.UnitaryThreeReflectionRight", [(44, 77), (151, 158), (235, 240), (281, 301)]),
    ("UnitaryThreeGroups.ShaInjGen", [(30, 99), (101, 131), (145, 187), (325, 361)]),
    ("UnitaryThreeGroups.ShaInj", [(29, 37)]),
    ("UnitaryThreeGroups.ModelLower", [(210, 218), (248, 285), (296, 301), (310, 365), (373, 401)]),
    ("UnitaryThreeGroups.VlenLe", [(13, 41), (52, 67)]),
    ("CommutativeAlgebra.GradedModulesLength.SmHolds", [(55, 62)]),
    ("CommutativeAlgebra.GradedModulesLength.MainCotSpan", [(32, 70)]),
    ("CommutativeAlgebra.GradedModulesLength.AlgMemCoef", [(92, 143)]),
    ("UnitaryThreeGroups.ModelUpper", [(103, 160)]),
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
    for suffix, ranges in SOURCES:
        module = PREFIX + suffix
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        data = (ROOT / "build/source-cache/jsmorph/rh" / REV / path).read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == blobs[module]
        lines = data.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            excerpts.append({"lines": [lo, hi],
                             "sha256": sha(b"\n".join(lines[lo-1:hi]) + b"\n")})
        records.append({"repository": "jsmorph/rh", "commit": REV, "path": path,
                        "sha256": sha(data), "git_blob_sha1": blob, "excerpts": excerpts})
    return records


def det(a):
    """Exact determinant by expansion; the tested ranks are at most four."""
    if not a:
        return 1
    if len(a) == 1:
        return a[0][0]
    return sum((-1)**j * a[0][j] * det([r[:j] + r[j+1:] for r in a[1:]])
               for j in range(len(a)))


def minor_gcd(a, k):
    out = 0
    for rows in itertools.combinations(range(len(a)), k):
        for cols in itertools.combinations(range(len(a[0])), k):
            out = gcd(out, det([[a[i][j] for j in cols] for i in rows]))
    return abs(out)


def changed_presentation(p, exponents):
    r = len(exponents)
    a = [[p**exponents[i] if i == j else 0 for j in range(r+1)] for i in range(r)]
    for k in range(7):
        i, j = k % (r+1), (k+1) % (r+1)
        for row in a:
            row[j] += (-1 if k % 2 else 2)*row[i]
        if r > 1:
            i, j = k % r, (k+1) % r
            a[j] = [x + (-1 if k % 2 else 1)*y for x, y in zip(a[j], a[i])]
    return a


def matrix_checks():
    cases = []
    vector_count = 0
    exponents = [(0,), (1,), (3,), (0, 2), (1, 5), (2, 4), (1, 2, 3), (0, 1, 2)]
    for p in (3, 5):
        for cs in exponents:
            a = changed_presentation(p, cs)
            r = len(cs)
            cs_sorted = sorted(cs)
            divisors = [minor_gcd(a, k) for k in range(1, r+1)]
            assert divisors == [p**sum(cs_sorted[:k]) for k in range(1, r+1)]
            stabilized = [row + [0] for row in a] + [[0]*(r+1) + [1]]
            assert minor_gcd(stabilized, r+1) == divisors[-1]
            levels = []
            for k in range(1, 4):
                modulus = p**k
                if modulus**r > 25000:
                    continue
                count = 0
                for x in itertools.product(range(modulus), repeat=r):
                    vector_count += 1
                    if all(sum(a[i][j]*x[i] for i in range(r)) % modulus == 0
                           for j in range(r+1)):
                        count += 1
                length = sum(min(k, c) for c in cs)
                assert count == p**length
                levels.append({"k": k, "hom_order": count, "hom_length": length})
            cases.append({"prime": p, "elementary_exponents": list(cs),
                          "maximal_minor_gcd": divisors[-1], "finite_levels": levels,
                          "matrix_sha256": sha(json.dumps(a).encode())})
    example = [[9, 3, 0], [0, 81, 243]]
    assert minor_gcd(example, 1) == 3 and minor_gcd(example, 2) == 3**6
    return cases, vector_count


def coefficient_checks():
    count = 0
    for p in (3, 5, 7):
        for k in range(1, 4):
            a = p**k
            for u in range(min(a, 13)):
                z = Fraction(u, a)
                for b in (1, 2, p, p*p, 2*p):
                    old = int(a*z) % a
                    new = int(a*b*z) % (a*b)
                    assert new == b*old % (a*b)
                    assert Fraction(old, a) % 1 == Fraction(new, a*b) % 1
                    for shift in (-2, 0, 3):
                        assert int(a*(z+shift)) % a == old
                    count += 1
            # The normalized representative is unchanged by any coboundary.
            alpha_mark = 2
            inverse = pow(alpha_mark-1, -1, a)
            for alpha_g in range(1, min(a, 11)):
                if gcd(alpha_g, a) != 1:
                    continue
                for zg, zd, m in itertools.product(range(min(a, 4)), repeat=3):
                    normal = (zg-(alpha_g-1)*inverse*zd) % a
                    changed = (zg+(alpha_g-1)*m-(alpha_g-1)*inverse*(zd+(alpha_mark-1)*m)) % a
                    assert changed == normal
                    count += 1
    return count


def mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def intertwiner_checks():
    J = [[int(i+j == 2) for j in range(3)] for i in range(3)]
    count = 0
    for psi in (Fraction(2), Fraction(3), Fraction(-2), Fraction(5, 3)):
        d = [[(psi, 1, 1/psi)[i] if i == j else 0 for j in range(3)] for i in range(3)]
        di = [[(1/psi, 1, psi)[i] if i == j else 0 for j in range(3)] for i in range(3)]
        for t in (Fraction(0), Fraction(1), Fraction(-2), Fraction(3, 5)):
            L = [[0, 0, 0], [t, 0, 0], [0, -t, 0]]
            transposed = [list(row) for row in zip(*L)]
            involuted = [[-v for v in row] for row in mul(mul(J, transposed), J)]
            assert involuted == L
            for component in (L, involuted):
                assert mul(mul(d, component), di) == [[v/psi for v in row] for row in L]
                count += 1
    return count


def main():
    sources = source_records()
    cases, vectors = matrix_checks()
    coefficient_cases = coefficient_checks()
    matrix_actions = intertwiner_checks()
    artifacts = ["notes/rh-selmer-conormal-pairing.md",
                 "scripts/check_rh_selmer_conormal_pairing.py"]
    record = {
        "schema_version": 1,
        "claim": "For the fixed marked deformation model with the stated inputs, the strict Selmer module embeds linearly in the dual of the negative conormal quotient; finite-level, exponent and elementary-divisor bounds follow.",
        "scope": [
            "Ordinary-mathematics proof in the note and shared TeX; no claim of a new Lean replay.",
            "Canonicity is relative to the fixed marking and ambient pair, not arbitrary model replacement.",
            "The source contracts and modulus equality are authenticated; uninspected suppliers are retained.",
            "Exact linear algebra and coefficient examples are supplementary finite checks, not the proof of compatibility for all data.",
            "No actual growing deformation family or Selmer group is computed; the upper graded-intersection and automorphy suppliers remain.",
            "No additional existing proof-map node completed.",
        ],
        "sources": sources,
        "exact_checks": {"module_presentations": len(cases), "finite_hom_vectors_examined": vectors,
                         "coefficient_and_normalization_cases": coefficient_cases,
                         "matrix_intertwining_cases": matrix_actions,
                         "module_cases": cases},
        "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())} for p in artifacts],
        "independent_review_record": "certificates/hard-node-review-2026-11-22.json",
        "review_scope": "Automation-only verification here; mathematical review is recorded separately.",
    }
    out = ROOT / "certificates/rh-selmer-conormal-pairing.json"
    out.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "pass", "pinned_sources": len(sources),
                      "presentations": len(cases), "finite_hom_vectors": vectors,
                      "coefficient_cases": coefficient_cases, "matrix_actions": matrix_actions,
                      "output": str(out.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
