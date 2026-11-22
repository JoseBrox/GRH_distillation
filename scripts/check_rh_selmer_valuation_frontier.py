#!/usr/bin/env python3
"""Exact synthetic gcd examples and bounded deformation-contract provenance."""

import gzip
import hashlib
import json
from fractions import Fraction
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
SOURCES = [
    ("UnitaryThreeGroups.KatoUse", [[19, 34], [54, 64]]),
    ("AutomorphicCases.AutomorphyUnramifiedCoefficients", [[12, 27]]),
    ("UnitaryThreeGroups.OneCharOf", [[64, 93], [114, 140], [158, 178]]),
    ("UnitaryThreeGroups.ModelLower", [[373, 401]]),
    ("UnitaryThreeGroups.VlenLe", [[43, 67]]),
    ("UnitaryThreeGroups.PtHypOf", [[74, 89]]),
    ("UnitaryThreeGroups.ModelUpper", [[103, 120], [133, 160]]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def vp(n, p):
    assert n > 0
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def main():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    cert = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == cert["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["commit"] == REV
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    sources = []
    for suffix, ranges in SOURCES:
        module = PREFIX + suffix
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        data = (ROOT / "build/source-cache/jsmorph/rh" / REV / path).read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == blobs[module]
        lines = data.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpts.append({"lines": [lo, hi], "sha256": sha(b"\n".join(lines[lo-1:hi])+b"\n")})
        sources.append({"repository": "jsmorph/rh", "commit": REV, "path": path,
                        "sha256": sha(data), "git_blob_sha1": blob, "excerpts": excerpts})
    examples = []
    for L in range(1, 13):
        M, e = 13**L, 1
        while 7**e < M:
            e += 1
        assert 7**(e-1) < M <= 7**e
        records = {}
        for q in (7, 11):
            a = q**e
            u = (a*a+a+1) % M
            alpha = Fraction(u, a)
            n = a*a+a+1-u
            assert 0 <= alpha < 1 and n > a*a and n < 2*a*a
            assert n % M == 0 and (a*alpha).denominator == 1
            records[q] = {"u": u, "alpha": str(alpha), "integer": n}
        A, B = records[7]["integer"], records[11]["integer"]
        G = gcd(A//7**vp(A, 7), B//11**vp(B, 11))*7**vp(B, 7)*11**vp(A, 11)
        assert vp(G, 13) >= L and (A*B) % G == 0
        examples.append({"L": L, "e": e, "M": M, "traces": records,
                         "corrected_gcd": G, "gcd_13_valuation": vp(G, 13)})
    artifacts = ["notes/rh-selmer-valuation-frontier.md",
                 "scripts/check_rh_selmer_valuation_frontier.py"]
    result = {"schema_version": 1,
              "claim": "Trace-class assumptions alone allow corrected gcd with logarithm linear in twist; actual OneChar proof retains integral negative-weight deformation and automorphy inputs.",
              "scope": ["Exact synthetic integer examples only; not actual automorphic spectra or Selmer groups.",
                        "General growth and square-zero-algebra statements are proved in the note, not established by finite enumeration.",
                        "Listed pinned source contracts only; no upstream proof audit or Lean build.",
                        "No proof-map node completed."],
              "sources": sources, "examples": examples,
              "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())} for p in artifacts],
              "independent_review_record": "certificates/continuation-review-2026-11-22.json",
              "review_scope": "Automated integrity and exact finite checks only; mathematical review is recorded separately."}
    out = ROOT / "certificates/rh-selmer-valuation-frontier.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "pass", "source_files": len(sources), "exact_examples": len(examples),
                      "output": str(out.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
