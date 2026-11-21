#!/usr/bin/env python3
"""Pinned evidence and exact finite checks for the two-primary Selmer reduction.

The ordinary proofs are in the note. No Selmer group is computed and no Lean
proof, global construction, or analytic estimate is certified by this script.
"""

from fractions import Fraction
import gzip
import hashlib
import json
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NOTE = "notes/two-primary-selmer-reduction.md"
OUT = "certificates/two-primary-selmer-reduction.json"
HV = "Development.AutomorphicArithmetic.AutomorphicVarieties.HeightAndVanishing."
TH = "Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases."
SOURCES = [
    (HV + "DirichletPrimeToLPartMulLPowerPart",
     "581296043e4d3e868e1530db3aa8d36f0af6e95a7345a67967b8508dd54592c0",
     [[148, 192], [204, 225]]),
    (HV + "HostComp",
     "96947e65f39891fa39aa40a42ac7c78ae86d6b12b7b40c964ed308a182cb65e4",
     [[21, 34]]),
    (HV + "Cases",
     "106cac91fddb7abbd3f3234bbf986446c631ae0a9d64ae18be415ea901890102",
     [[8, 48]]),
    (HV + "Counts",
     "cc00a1a2e38f8dc5a87a0cc5d79ab8100db8c59255d62be12c95931262fc53c2",
     [[49, 73]]),
    (HV + "SumOut",
     "4cb9dc9c0dca0804fcb4cb68deeb0cacb0b47c32f8fec59084d240646754bc28",
     [[50, 118], [119, 166], [167, 231]]),
    (HV + "JointWinOfCounts",
     "3c71cf0dabc617e3d1ab9fc04939c311e4242912407cdfbc71c8e0764563d558",
     [[16, 33]]),
    (HV + "BchiFacts",
     "6304725e9256d25463272315823562e7875bf5eb31d21f30b651173116cfa1de",
     [[7, 10], [75, 85]]),
    ("Development.AutomorphicArithmetic.CharacterBoxes.ExistsPageN",
     "732c3347fb02e410cf9af8831afdbba1d230fc522c3dbbccdb4b708e5dde73db",
     [[12, 49]]),
    ("Development.AutomorphicArithmetic.CharacterBoxes.SupplyChi",
     "70a11ba909e03b9153a6beacce24da22f3224b8192ec6980b7f27018961be81b",
     [[8, 16]]),
    ("Formalism.SharpRestriction.GlobalSchurBounds.MainSup",
     "0a317908f73e9deed3a39ab3056c5531567d849633b2c65615190dfd55e0701d",
     [[88, 94]]),
    ("Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.LitThin",
     "a135fd9de91e2a9306f67e83ed1de431fa787b3c46e15df92db9fb191338671b",
     [[8, 9]]),
    (TH + "VwinOfRow",
     "d2df45a5cf337190ae6f885e8e43056ae4e804ae8da250a2ab0abd64b1ca7080",
     [[1, 5]]),
    (TH + "TopMainZj",
     "f824d3f7873a493432bdfcbdc279fa82d70a6a9dbaac44c2a30316cada2eae3e",
     [[18, 58], [59, 74]]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, expected, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        path = ROOT / "build/source-cache/jsmorph/rh" / REV / rel
        if not path.is_file():
            path = ROOT / "build/lean-mirror" / rel
        data = path.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert sha(data) == expected and blob == blobs[module], module
        lines = data.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpt = b"\n".join(lines[lo-1:hi]) + b"\n"
            excerpts.append({"lines": [lo, hi], "sha256": sha(excerpt)})
        records.append({"module": module, "path": rel, "sha256": expected,
                        "git_blob_sha1": blob, "bytes": len(data),
                        "line_count": len(lines), "inspected_excerpts": excerpts})
    return records, sha(packed)


def order_checks():
    cases = 0
    for a in range(13):
        for h in range(11):
            exponent = h + 1 + a
            for k in range(exponent + 1):
                order = 2**k
                assert 2**exponent % order == 0
                assert order % 2 == 0 or order == 1
                cases += 1
    # The order constraint alone does not exclude a nontrivial odd order
    # when the target itself has such an order.
    assert all((3 * 2**h) % 3 == 0 for h in range(12))
    return cases


def prime(n):
    return n >= 2 and all(n % k for k in range(2, isqrt(n) + 1))


def harmonic_pair_checks():
    cases = 0
    for t in range(2, 302):
        m = t - 1
        primes = [p for p in range(3, 2*m+2, 2) if prime(p)]
        direct = sum(1 for p in primes for e in range(1, t) if 2*e % (p-1) == 0)
        grouped = sum(m // ((p-1)//2) for p in primes)
        divisor_sum = sum(m // j for j in range(1, m+1))
        harmonic = sum((Fraction(1, j) for j in range(1, m+1)), Fraction())
        assert direct == grouped <= divisor_sum <= m * harmonic
        cases += 1
    return cases


def polynomial_checks():
    cases = 0
    for N in (1, 2, 5, 17):
        for t in (2, 3, 7, 20):
            m, M = t-1, N*t
            harmonic = sum((Fraction(1, j) for j in range(1, m+1)), Fraction())
            for CI in range(5):
                for C in range(5):
                    lhs = m * M**CI + N*m*harmonic*((2*m+1)*N*m)**C
                    first = M**(CI+1)
                    second = 2**C * M**(2*C+2)
                    rhs = (1+2**C)*M**max(CI+1, 2*C+2)
                    assert lhs <= first + second <= rhs
                    cases += 1
    return cases


def main():
    records, atlas_hash = source_records()
    exact = {
        "power_of_two_order_cases": order_checks(),
        "prime_twist_harmonic_counts": harmonic_pair_checks(),
        "rational_polynomial_budget_cases": polynomial_checks(),
        "odd_target_order_counterexample": "order 3 divides 3 times every positive power of 2",
    }
    report = {
        "schema_version": 1,
        "result": "PASS",
        "repository": "jsmorph/rh",
        "commit": REV,
        "note": NOTE,
        "note_sha256": sha((ROOT / NOTE).read_bytes()),
        "checker": str(Path(__file__).relative_to(ROOT)),
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "atlas_compressed_sha256": atlas_hash,
        "mathematical_results": [
            "Case III is empty for actual host characters when the fixed target has power-of-two order.",
            "The restricted SumOut proof omits CountIII; the universal theorem is not changed.",
            "Resonant prime-twist pairs are at most m H_m, with m=t-1.",
            "The conditional outside-prime budget is at most (1+2^C)(Nt)^max(C_I+1,2C+2).",
            "LitThin is an analytic thin-prime input, distinct from VWin/cohomological inputs.",
        ],
        "exact_checks": exact,
        "sources": records,
        "review": {
            "author": "Ordinary proofs and bounded source-consumer audit completed.",
            "root": "PASS: complete note ordinary mathematics and pinned HostComp 21-34, Cases 8-48, SumOut 85-123, MainSup 88-94. Root requested the explicit weighted sum and retention of C_Z in the default assembly; both are now included.",
            "transport_defect": "PASS: Sections 1-2 ordinary proofs; independently hash-read HostComp 21-34, DirichletPrimeToLPartMulLPowerPart 208-215 and SumOut 85-123. Earlier review allowed the explicitly assumed zero Case Z; the final statement instead includes C_Z in the same per-character majorant, with unchanged proof. No cohomological supplier or upstream replay claimed.",
        },
        "limitations": [
            "Finite checks supplement, rather than prove, the universal ordinary-mathematics arguments.",
            "No actual Selmer length, congruence index, or nonzero theta map is computed.",
            "Cases I/II, fixed bad primes, prime 2, other parity, integral comparison, and window quantifiers remain.",
            "No complete source proof dependency closure or Lean kernel build was performed.",
            "No W04/W06 or other construction-node completion follows.",
        ],
    }
    (ROOT / OUT).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "source_files": len(records),
                      "source_excerpts": sum(len(r["inspected_excerpts"]) for r in records),
                      "exact_checks": exact, "certificate": OUT}))


if __name__ == "__main__":
    main()
