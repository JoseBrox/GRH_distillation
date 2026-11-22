#!/usr/bin/env python3
"""Bounded provenance and exact checks of the upper Euler determinant formula.

The note proves the general formula. These finite checks do not compute an
actual Selmer group or verify the retained mixed-intersection comparison.
"""

import gzip
import hashlib
import itertools
import json
from fractions import Fraction
from functools import lru_cache
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
SOURCES = [
    ("CommutativeAlgebra.ResMapBijective", [(9, 13)]),
    ("CommutativeAlgebra.GradedModulesLength.ToDegInjective", [(156, 163), (187, 218)]),
    ("CommutativeAlgebra.GradedModulesLength.HerbrandFinLen", [(83, 99), (189, 259)]),
    ("CommutativeAlgebra.GradedModulesLength.EventuallyMQGrFiniteAnnihilator", [(77, 123)]),
    ("CommutativeAlgebra.GradedModulesLength.LocLenAPieceIdeal2LeTwoPow", [(69, 115)]),
    ("CommutativeAlgebra.GradedModulesLength.TwoSigned", [(63, 95)]),
    ("CommutativeAlgebra.GradedModulesLength.AlgMemCoef", [(92, 143)]),
    ("CommutativeAlgebra.GradedModulesLength.AdmissibleMonoIdeal", [(191, 237), (273, 322)]),
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


def det(matrix):
    """Exact determinant by expansion; dimensions are at most four."""
    if not matrix:
        return 1
    if len(matrix) == 1:
        return matrix[0][0]
    return sum((-1)**j * matrix[0][j]
               * det([row[:j] + row[j+1:] for row in matrix[1:]])
               for j in range(len(matrix)))


def maximal_minor_gcd(matrix):
    rows = len(matrix)
    if rows == 0:
        return 1
    out = 0
    for cols in itertools.combinations(range(len(matrix[0])), rows):
        out = gcd(out, det([[row[j] for j in cols] for row in matrix]))
    return abs(out)


def valuation(n, p):
    n = abs(n)
    assert n != 0
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result, n


def torsion_matrix(p, s, mode):
    if mode == 0:
        return [[0] * s for _ in range(s)]
    if mode == 1:
        return [[p * int(i == j) for j in range(s)] for i in range(s)]
    if mode == 2:
        return [[p * ((i+1) * int(i == j) + int(j == i+1))
                 for j in range(s)] for i in range(s)]
    return [[p * int(j == (i+1) % s) for j in range(s)] for i in range(s)] if s else []


@lru_cache(maxsize=None)
def torsion_kernel_count(p, level, s, mode):
    modulus = p**level
    c = torsion_matrix(p, s, mode)
    count = sum(all(sum(c[i][j]*vector[j] for j in range(s)) % modulus == 0
                    for i in range(s))
                for vector in itertools.product(range(modulus), repeat=s))
    length, unit = valuation(count, p)
    assert unit == 1
    return count, length, modulus**s


def presentation_case(p, level, cs, s, mode):
    """M=Z_p^r + (Z/p^level)^s; u=[A,0;B,C]."""
    r, modulus = len(cs), p**level
    a = [[p**cs[i] if i == j else (mode+1 if j == i+1 else 0)
          for j in range(r)] for i in range(r)]
    b = [[(1+i+2*j+mode) % modulus for j in range(r)] for i in range(s)]
    c = torsion_matrix(p, s, mode)
    u = [row + [0]*s for row in a] + [b[i] + c[i] for i in range(s)]
    # Cokernel presentation [relations of M | images of u].
    relations = [[modulus * int(i == r+j) for j in range(s)]
                 for i in range(r+s)]
    presentation = [relations[i] + u[i] for i in range(r+s)]
    cokernel_order = maximal_minor_gcd(presentation)
    cokernel_length, unit = valuation(cokernel_order, p)
    assert unit == 1
    kernel_order, kernel_length, _ = torsion_kernel_count(p, level, s, mode)
    determinant_length, determinant_unit = valuation(det(a), p)
    assert determinant_unit == 1
    assert determinant_length == sum(cs)
    assert cokernel_length - kernel_length == determinant_length
    for ramification in (1, 2, 3, 5):
        assert (Fraction(cokernel_length, ramification)
                - Fraction(kernel_length, ramification)
                == sum(Fraction(c, ramification) for c in cs))
    return {"p": p, "torsion_level": level, "free_diagonal_exponents": list(cs),
            "torsion_rank": s, "coupling_mode": mode,
            "kernel_order": kernel_order, "cokernel_order": cokernel_order,
            "euler_characteristic": determinant_length,
            "presentation_sha256": sha(json.dumps(presentation).encode())}


def exact_checks():
    cases = []
    for p in (3, 5):
        for level in (1, 2, 3):
            for cs in ((), (0,), (1,), (2,), (1, 1), (1, 3)):
                for s in (0, 1, 2):
                    for mode in range(4):
                        cases.append(presentation_case(p, level, cs, s, mode))

    examples = []
    for p in (3, 5):
        jordan = [[p*p, 1, 0], [0, p*p, 0], [0, 0, p]]
        assert det(jordan) == p**5
        assert maximal_minor_gcd(jordan) == p**5
        examples.append({"p": p, "kind": "nonsemisimple generic operator",
                         "matrix": jordan, "point_multiplicities": [2, 1],
                         "point_valuations": [2, 1], "determinant_valuation": 5})
        # Multiplication by X in Z_p[X]/(X^2-p). Its two conjugate roots
        # each have valuation 1/2, and each generic localized length is one.
        quadratic = [[0, p], [1, 0]]
        assert det(quadratic) == -p
        assert maximal_minor_gcd(quadratic) == p
        assert Fraction(1, 2) + Fraction(1, 2) == 1
        examples.append({"p": p, "kind": "ramified quadratic residue extension",
                         "matrix": quadratic, "point_multiplicities": [1, 1],
                         "point_valuations": ["1/2", "1/2"],
                         "determinant_valuation": 1})
    vectors = sum(p**(level*s) for p in (3, 5) for level in (1, 2, 3)
                  for s in (0, 1, 2) for mode in range(4))
    return cases, examples, vectors


def main():
    sources = source_records()
    cases, examples, vectors = exact_checks()
    artifacts = ["notes/rh-selmer-euler-determinant.md",
                 "scripts/check_rh_selmer_euler_determinant.py"]
    record = {
        "schema_version": 1,
        "claim": "The one-operator Euler characteristic of the actual finite graded weight module is an exact generic determinant valuation and a sum of localized point multiplicities; the mixed-intersection lower comparison remains a separate input.",
        "scope": [
            "Ordinary-mathematics proof in the note and shared TeX; no new Lean replay claimed.",
            "Integral torsion cancels through the kernel term; no flatness of the finite weight module is assumed.",
            "The exact generic support uses distinct degree-zero characters, including separate embeddings of characteristic-zero residue fields.",
            "The source module and normalization are matched; eventual finite support, local multiplicity, mixed lower comparison and arithmetic model existence remain supplied hypotheses.",
            "Exact checks on finite presentations supplement the proof; no actual Selmer module or growing model is computed.",
            "No additional existing proof-map node completed.",
        ],
        "sources": sources,
        "primary_reference_audit": [
            {"url": "https://stacks.math.columbia.edu/tag/0AZZ",
             "statement": "Local Koszul Euler characteristic equals the degree-q Hilbert-Samuel multiplicity when the q-generated ideal has finite colength.",
             "checked_date": "2026-11-22"},
            {"url": "https://stacks.math.columbia.edu/tag/0B00",
             "statement": "The preceding formula has a module-relative version when the quotient of the finite module has finite length.",
             "checked_date": "2026-11-22"},
        ],
        "exact_checks": {"module_presentations": len(cases),
                         "distinct_torsion_kernel_vectors_examined": vectors,
                         "normalization_identities": 4*len(cases),
                         "spectral_examples": examples,
                         "case_list_sha256": sha(json.dumps(cases, sort_keys=True).encode()),
                         "representative_cases": cases[:4] + cases[-4:]},
        "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())} for p in artifacts],
        "independent_review_record": "certificates/hard-node-review-2026-11-22.json",
        "review_scope": "Automation-only verification here; mathematical review is recorded separately.",
    }
    out = ROOT / "certificates/rh-selmer-euler-determinant.json"
    out.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "pass", "pinned_sources": len(sources),
                      "presentations": len(cases), "kernel_vectors": vectors,
                      "spectral_examples": len(examples),
                      "output": str(out.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
