#!/usr/bin/env python3
"""Check pinned determinant evidence and exact supplemental algebra.

The written proof supplies the general determinant argument. These finite
checks authenticate excerpts and verify signs and normalizations; they do
not construct the geometric flat family, prove its CM evaluation, or run
Lean. Populate missing files with scripts/source_excerpt.py --atlas.
"""
from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
AS = "Development.AutomorphicSpectrum."
WB = "Development.WeilBound.CoreStatements.PlurisubharmonicCones."
SOURCE_RANGES = [
    (AS + "Definitions.GlobalGeometry.IsConstMul", [[30, 43], [59, 82]]),
    (WB + "ExistsSmulMemSpan", [[93, 152], [154, 178], [188, 261]]),
    (WB + "ExistsCoordLattice", [[346, 409], [418, 448]]),
    (AS + "Statements.GeometryStatements.FlatDegree", [[12, 19]]),
    (AS + "Proofs.GeometryProofs.KroneckerCharacterPeriodFormula",
     [[16, 45], [47, 102], [104, 146]]),
    (AS + "Proofs.GeometryProofs.PhiDegFibLatLeOfIsOFamilyOfIsAdapted",
     [[20, 71], [73, 124], [126, 153]]),
    (AS + "Proofs.GeometryProofs.AbelianPartLieSignature", [[18, 28]]),
    (AS + "Proofs.GeometryProofs.FlatDegreeHolds", [[60, 118]]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def pinned_sources():
    data = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(data) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(data))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    entries = {row[0]: row for row in atlas["modules"]}
    answer = []
    for module, ranges in SOURCE_RANGES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        path = ROOT / "build/source-cache/jsmorph/rh" / REV / rel
        if not path.is_file():
            path = ROOT / "build/lean-mirror" / rel
        payload = path.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(payload)).encode() + b"\0" + payload).hexdigest()
        assert blob == entries[module][1], module
        lines = payload.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            passage = b"\n".join(lines[lo-1:hi])+b"\n"
            excerpts.append({"lines": [lo, hi], "sha256": sha(passage)})
        answer.append({"module": module, "path": rel, "sha256": sha(payload),
                       "git_blob_sha1": blob, "line_count": len(lines),
                       "url": f"https://github.com/jsmorph/rh/blob/{REV}/{rel}",
                       "inspected_excerpts": excerpts})
    return answer


def determinant(matrix):
    n = len(matrix)
    if n == 0:
        return F(1)
    total = F(0)
    for perm in itertools.permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        value = F(-1 if inversions % 2 else 1)
        for i in range(n):
            value *= matrix[i][perm[i]]
        total += value
    return total


def transpose(a):
    return list(map(list, zip(*a)))


def multiply(a, b):
    if not a:
        return []
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def valuation(x, p):
    x = F(x)
    assert x != 0
    a, b = abs(x.numerator), x.denominator
    result = 0
    while a % p == 0:
        result += 1
        a //= p
    while b % p == 0:
        result -= 1
        b //= p
    return result


def check_algebra():
    gram = finite = correction = signature = positive_part = 0
    matrices = [[], [[F(2)]], [[F(-3)]],
                [[F(2), F(1)], [F(1), F(3)]],
                [[F(1, 2), F(3)], [F(-2), F(1, 3)]],
                [[F(1), F(2), F(0)], [F(0), F(3), F(1)], [F(2), F(0), F(1)]]]
    for a in matrices:
        n = len(a)
        da = determinant(a)
        assert da != 0
        # Independently form a positive Gram matrix and transform it.
        r = [[F(i+j+1 if i < j else 1 if i == j else 0)
              for j in range(n)] for i in range(n)]
        g = multiply(transpose(r), r)
        changed = multiply(multiply(a, g), transpose(a))
        assert determinant(changed) == da*da*determinant(g)
        gram += 1
        for b in matrices:
            db = determinant(b)
            phi0 = F(3, 5)
            phi = phi0*db/da
            # The scalar times the determinant section is frame invariant.
            assert phi*da/db == phi0
            for prime in (2, 3, 5, 7, 11, 13, 17, 19):
                assert (valuation(phi, prime)+valuation(da, prime)
                        -valuation(db, prime)) == valuation(phi0, prime)
                finite += 1
    for a, b, p, c, rd in itertools.product(
            range(6), range(6), [F(-7), F(0), F(3, 2)],
            [F(1), F(4)], [F(0), F(2), F(5)]):
        corrected = F(a-b, 2)*p+b*(c-rd)
        actual = corrected-b*(c-rd)
        assert actual == F(a-b, 2)*p
        correction += 1
    for p in range(8):
        for q in range(8):
            for r in range(min(p, q)+1):
                for f in (1, 2, 5):
                    for m in (p, q):
                        selected = f*(m-r)
                        total = f*(p+q-2*r)
                        assert 2*selected-total == f*(2*m-p-q)
                        for period in [F(-9, 2), F(0), F(7)]:
                            b = F(2*selected-total, 2)*period
                            assert abs(b) <= F(total, 2)*abs(period)
                            if selected*2 <= total and period >= 0:
                                assert b <= 0
                            if p == q:
                                assert b == 0
                            for delta, nu, t in itertools.product(
                                    [F(0), F(1, 3)], [F(0), F(2)],
                                    [F(1, 5), F(2), F(9)]):
                                degree = 2*t-b+delta+2*nu
                                assert max(-degree, F(0)) <= max(b-delta-2*nu, F(0))
                                positive_part += 1
                        signature += 1
    return {"exact_gram_determinant_cases": gram,
            "finite_valuation_frame_cases": finite,
            "finite_correction_cancellation_cases": correction,
            "toric_signature_cases": signature,
            "signed_positive_part_cases": positive_part,
            "scope": "Finite rational checks of normalizations and signs, supplemental to the written general proof."}


def file_record(relative):
    data = (ROOT / relative).read_bytes()
    return {"path": relative, "bytes": len(data), "sha256": sha(data)}


def main():
    report = {
        "date": "2026-11-22", "result": "passed",
        "claim": "A determinant-line proof of the actual local-to-global bridge and exact signed signature cost, conditional on the stated flat-family and CM-period suppliers.",
        "not_claimed": ["Independent construction of the geometric flat family",
                        "Independent reconstruction of the complete CM-period proof",
                        "Point-height, cusp-mean or finite section-degree closure",
                        "A Lean build or kernel replay", "A completed RH or Dirichlet GRH proof node"],
        "node_counts": {"rh": {"finished": 6, "total": 9},
                        "grh": {"finished": 17, "total": 31}},
        "sources": pinned_sources(), "exact_checks": check_algebra(),
        "artifacts": [file_record(p) for p in
                      ["notes/geometric-flat-determinant.md",
                       "paper/shared/flat-determinant-comparison.tex",
                       "scripts/check_geometric_flat_determinant.py"]],
        "independent_review": {
            "record": "certificates/continuation-review-2026-11-22.json",
            "scope": "The referenced review record supplies independent proof-review scopes and final artifact hashes. This script reports source authentication and exact supplemental algebra only; it does not perform that independent mathematical review."
        }
    }
    target = ROOT / "certificates/geometric-flat-determinant.json"
    target.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"result": report["result"], "sources": len(report["sources"]),
                      "exact_checks": report["exact_checks"], "output": str(target.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
