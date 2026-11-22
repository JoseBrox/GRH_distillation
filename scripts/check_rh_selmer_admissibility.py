#!/usr/bin/env python3
"""Exact monomial checks and pinned contracts for four-weight admissibility.

The general prime and field-valued-point proof is in the accompanying note.
These finite checks neither verify arithmetic model existence nor compute
an actual Selmer group.
"""

import gzip
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties.CommutativeAlgebra."
ALG = BASE + "GradedModulesLength."
SOURCES = [
    (BASE + "OrbitVanishingLocal", [(21, 48), (66, 70), (86, 105)]),
    (BASE + "ResMapBijective", [(245, 267)]),
    (ALG + "ToDegInjective", [(187, 218)]),
    (ALG + "ExistsSecNotMem", [(63, 118)]),
    (ALG + "PrimeMaximalOrKernel", [(63, 84)]),
    (ALG + "TspHolds", [(7, 77)]),
    (ALG + "SameDegreeZeroOfRestriction", [(15, 42)]),
    (ALG + "XProjZero", [(81, 113)]),
    (ALG + "AdmissibilityHolds", [(30, 77)]),
]
WEIGHTS = (-2, -1, 1, 2)


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
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            excerpts.append({"lines": [lo, hi],
                             "sha256": sha(b"\n".join(lines[lo-1:hi]) + b"\n")})
        records.append({"repository": "jsmorph/rh", "commit": REV, "path": path,
                        "sha256": sha(data), "git_blob_sha1": blob, "excerpts": excerpts})
    return records


def weight(exponents):
    return sum(a*b for a, b in zip(WEIGHTS, exponents))


def add(*vectors):
    return tuple(sum(v[i] for v in vectors) for i in range(len(vectors[0])))


def scale(n, vector):
    return tuple(n*v for v in vector)


def sum_vectors(vectors, dimension=4):
    return tuple(sum(v[i] for v in vectors) for i in range(dimension))


def even_factorization(exponents):
    """Remove zero-weight blocks and return pure blocks of signed weight two."""
    assert weight(exponents) % 2 == 0
    remaining = list(exponents)
    zero = []
    for block in ((1, 0, 0, 1), (0, 1, 1, 0),
                  (1, 0, 2, 0), (0, 2, 0, 1)):
        count = min(remaining[i]//v for i, v in enumerate(block) if v)
        zero.extend([block]*count)
        remaining = [r-count*v for r, v in zip(remaining, block)]
    assert not ((remaining[0] or remaining[1]) and (remaining[2] or remaining[3]))
    assert remaining[1] % 2 == remaining[2] % 2 == 0
    blocks = ([(1, 0, 0, 0)]*remaining[0]
              + [(0, 2, 0, 0)]*(remaining[1]//2)
              + [(0, 0, 2, 0)]*(remaining[2]//2)
              + [(0, 0, 0, 1)]*remaining[3])
    assert all(weight(z) == 0 for z in zero)
    signed_two = 2 if weight(exponents) > 0 else -2
    assert all(weight(b) == signed_two for b in blocks)
    assert len(blocks) == abs(weight(exponents))//2
    assert sum_vectors(zero+blocks) == tuple(exponents)
    return zero, blocks


def factor_checks():
    even_cases = 0
    for exponents in itertools.product(range(8), repeat=4):
        if weight(exponents) % 2 == 0:
            even_factorization(exponents)
            even_cases += 1
    half_cases = 0
    values = list(itertools.product(range(4), repeat=4))
    for u, v in itertools.product(values, repeat=2):
        j = weight(v)
        total = weight(add(u, v))
        if j <= 0 or total > 0 or total % 2:
            continue
        n = -total//2
        zero_u, negative = even_factorization(scale(2, u))
        zero_v, positive = even_factorization(scale(2, v))
        assert len(negative) == 2*n+j and len(positive) == j
        paired = [add(negative[i], positive[i]) for i in range(j)]
        leftover = negative[j:]
        assert len(paired) == j and all(weight(z) == 0 for z in paired)
        assert len(leftover) == 2*n and all(weight(z) == -2 for z in leftover)
        assert sum_vectors(zero_u+zero_v+paired+leftover) == scale(2, add(u, v))
        half_cases += 1
    return even_cases, half_cases


def identity_checks():
    """Monomial exponent equality in the commutative polynomial algebra."""
    # Coordinates F, h, n0, n2, t0, t2.
    f, h, n0, n2, t0, t2 = [tuple(int(i == j) for i in range(6)) for j in range(6)]
    identities = [
        (add(scale(2, f), t0, n2, t2), add(scale(2, f), t2, n2, t0)),
        (add(scale(2, add(h, f)), n0, t0), add(scale(2, f), t0, scale(2, h), n0)),
        (add(h, f, n0, t0), add(f, t0, h, n0)),
    ]
    assert all(left == right for left, right in identities)
    # For the basepoint case, two strictly negative integers can sum to -2
    # only as -1 + -1; they cannot sum to -1.
    basepoint_cases = 0
    for total in (-1, -2):
        for first in range(-20, 21):
            second = total-first
            assert first >= 0 or second >= 0 or (total == -2 and first == second == -1)
            basepoint_cases += 1
    return len(identities), basepoint_cases


def main():
    sources = source_records()
    even_cases, half_cases = factor_checks()
    identities, basepoint_cases = identity_checks()
    artifacts = ["notes/rh-selmer-admissibility.md", "scripts/check_rh_selmer_admissibility.py"]
    record = {
        "status": "pass",
        "date": "2026-11-22",
        "theorem": "Actual three-graded admissibility from four-weight generation, negative cotangent spanning, finite degree-zero quotient, fixed-point separation, and two-sided trace nonvanishing.",
        "scope": [
            "Nine upstream files are verified against the pinned Git-blob atlas; only the listed bounded ranges form the source-contract audit.",
            "Finite exponent checks supplement the general even-half and field-valued-point proof in the note; they are not a general algebra formalization.",
            "The radical-power condition is proved under the stated marked-model hypotheses; arithmetic construction, automorphy, and local upper multiplicity are not verified by this script.",
            "No existing RH or GRH proof-map node is declared complete.",
        ],
        "sources": sources,
        "exact_checks": {
            "four_weight_even_monomials": even_cases,
            "half_extension_square_factorizations": half_cases,
            "clearing_identities": identities,
            "basepoint_weight_cases": basepoint_cases,
            "integer_arithmetic": True,
        },
        "primary_references": [
            {"statement": "Weak Nullstellensatz", "url": "https://stacks.math.columbia.edu/tag/00FV", "checked_date": "2026-11-22"},
            {"statement": "Lying over for an integral inclusion", "url": "https://stacks.math.columbia.edu/tag/00GQ", "checked_date": "2026-11-22"},
        ],
        "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())} for p in artifacts],
        "independent_review_record": "certificates/hard-node-review-2026-11-22.json",
        "review_scope": "Automation-only verification here; mathematical review is recorded separately.",
    }
    out = ROOT / "certificates/rh-selmer-admissibility.json"
    out.write_text(json.dumps(record, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "pass", "pinned_sources": len(sources),
                      "even_monomials": even_cases, "half_factorizations": half_cases,
                      "clearing_identities": identities, "output": str(out.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
