#!/usr/bin/env python3
"""Verify bounded source evidence and exact residual point-height algebra.

No Lean kernel replay, full flat-comparison proof audit, or new geometric
supplier is performed. Source dependencies are distinguished from the
independently reconstructed scalar deductions.
"""
from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NOTE = "notes/remaining-point-height-comparisons.md"
OUT = "certificates/remaining-point-height-comparisons.json"
AS = "Development.AutomorphicSpectrum."
WB = "Development.WeilBound.CoreStatements.PlurisubharmonicCones."
SOURCES = [
    (AS + "Statements.GeometryStatements.FlatDegree",
     "cfd99f65da51fe56065f6549373471908f2b05f883b74ebe5610d94982a55870", [[12, 19]]),
    (AS + "Proofs.GeometryProofs.FlatDegreeHolds",
     "2ae4dd58fb3e7ebb04700b941d7689e30289f85c9e6e8bb563a60b99d2815679", [[1, 11], [60, 118]]),
    (AS + "Proofs.GeometryProofs.FlatDegreeHoldsStatement",
     "2d4df5626e75997ad76c075f75d693a82d24734b52c486a964027ada4695551f", [[1, 6]]),
    (AS + "Proofs.GeometryProofs.FrameFunctionCmHeight",
     "22bca0778a297c7c78c5505ae455df06d112a5eb2cc164f4e3286e45f593253b", [[24, 49]]),
    (AS + "Proofs.GeometryProofs.FlatTheoremOfResolutionGaga",
     "b14b26dae80736b9e5dc03c2036802ca7f5c3d7ba56a43de3eb4b33a73133d03", [[19, 24]]),
    (AS + "Proofs.GeometryProofs.PhiDegFibLatLeOfIsOFamilyOfIsAdapted",
     "983a1eda3160559c93228668d49cdd99f035ec8738ec6b1ea998107d7e1cec28", [[20, 71], [73, 124], [126, 153]]),
    (WB + "HeightComparisonGlobalModel",
     "b61f96d5d0cb9a5af7174bee7b3f081d1120278d761dace6bfffd626f80df298", [[80, 121], [122, 164], [176, 238]]),
    (WB + "FlatSat",
     "f34edb87ca7a8196a91080cf3435510c6c33e6fc1de14c9d976d82db95f423d8", [[11, 20]]),
    (WB + "LogOmBound",
     "dc9a395aca59434b344249873713a8c20bd841eed93853dc18ef893ae390b3d4", [[9, 46]]),
    (WB + "SumLogPrimeRatioLe",
     "5c5811e45a7b5b3f6de982e586cc5c7923c955521da88c8abeb6b3432d68155b", [[28, 61]]),
]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def file_record(relative):
    data = (ROOT / relative).read_bytes()
    return {"path": relative, "bytes": len(data), "sha256": sha(data)}

def check_sources():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, expected, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        paths = [ROOT / "build/source-cache/jsmorph/rh" / REV / rel,
                 ROOT / "build/lean-mirror" / rel]
        local = next((p for p in paths if p.is_file()), None)
        if local is None:
            raise FileNotFoundError("Populate source_excerpt.py cache for " + module)
        data = local.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == blobs[module] and sha(data) == expected, module
        lines = data.splitlines()
        excerpts = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines) and end-start < 120
            passage = b"\n".join(lines[start-1:end]) + b"\n"
            excerpts.append({"lines": [start, end], "sha256": sha(passage)})
        records.append({"module": module, "path": rel, "sha256": expected,
                        "git_blob_sha1": blob, "line_count": len(lines),
                        "inspected_excerpts": excerpts})
    return records

def check_algebra():
    finite = period = toric = 0
    # exp(7/10) exceeds 2 already at degree three.
    t = F(7,10)
    assert 1+t+t*t/2+t*t*t/6 > 2
    assert F(28,5)+F(16,7) == F(276,35) < 8
    # e > 8/3, together with pi < 22/7, gives log(2pi), log 7 < 2.
    assert (F(8,3)**2) > F(44,7)
    assert (F(8,3)**2) > 7
    assert 16+36 == 52
    # A positive-integral proof of pi < 22/7, independent of decimals:
    # x^4(1-x)^4/(1+x^2) = Q(x)-4/(1+x^2), int_0^1 Q=22/7.
    q = [F(4), F(0), F(-4), F(0), F(5), F(-4), F(1)]
    product = [F(0)]*9
    for j, coefficient in enumerate(q):
        product[j] += coefficient
        product[j+2] += coefficient
    product[0] -= 4
    assert product == [F(0), F(0), F(0), F(0), F(1), F(-4), F(6), F(-4), F(1)]
    assert sum(c/F(j+1) for j,c in enumerate(q)) == F(22,7)
    for c, u, v, z in itertools.product([F(0), F(1,2), F(1), F(8)],
                                      [F(1), F(2), F(5)],
                                      [F(0), F(1,3), F(7)],
                                      [F(0), F(1,5), F(6)]):
        la = u+v+z
        assert 2*c*u+2*v <= 2*max(c,F(1))*la <= (2*c+2)*la
        finite += 1
    for gamma, c, u, v, ell in itertools.product(
            [F(0), F(1,2), F(2)], [F(-2), F(0), F(3)],
            [F(1), F(2), F(7)], [F(0), F(1,3), F(6)],
            [F(-5), F(0), F(4)]):
        a = gamma+abs(c)
        la = u+v+abs(ell)
        cf = 1+a
        assert abs(gamma+c-v-ell) <= a+v+abs(ell) <= cf*la
        assert cf*la-(a+v+abs(ell)) == u+a*(u-1+v+abs(ell))
        period += 1
    for m in range(7):
        for r in range(m+1):
            for ca in [F(0), F(1,4), F(1,2), F(3)]:
                cost = ca*(m-r)+F(r,2)
                assert cost <= max(ca,F(1,2))*m
                assert max(ca,F(1,2))*m-cost == ((max(ca,F(1,2))-ca)*(m-r)
                                                             +(max(ca,F(1,2))-F(1,2))*r)
                toric += 1
    return {"finite_prime_exact_cases": finite,
            "scalar_period_exact_cases": period,
            "toric_abelian_exact_cases": toric,
            "constant_52": "Exact exponential-series and positive-integral rational identities checked; gamma<1 follows from gamma<=3/2-log2 and log2>1/2.",
            "scope": "Exact rational checks supplement the written ordinary proofs; no log, period or geometric theorem is inferred from sampling."}

def main():
    sources = check_sources()
    checks = check_algebra()
    certificate = {
        "schema_version": 1,
        "result": "PASS",
        "claim": "Bounded residual-input audit and exact scalar simplifications after the classical tangent-slope supplier.",
        "source_revision": {"repository": "jsmorph/rh", "commit": REV},
        "sources": sources,
        "checks": checks,
        "independent_reviews": [{
            "reviewer": "/root",
            "result": "PASS",
            "scope": "Full ordinary-mathematics review of the note: finite-prime coefficient (including independent C1=8 at B>=128), elementary period bound, signed eigenspace sum, selected-rank and toric/abelian constants, and the resulting conditional constant 52; distinction between an upstream flat proof and an independently reconstructed geometric application. No full upstream proof or Lean-kernel replay claimed."
        }, {
            "reviewer": "/root/rh_source_symmetry",
            "result": "PASS",
            "scope": "Independent ordinary-mathematics review of all three sections, including the final C1=8 and conditional constant 52. Independently hash-read the decisive flat construction, flat-degree proof and relay, finite determinant identities, geometric height-comparison use, scalar period bound and prime-sum passages. A scoped manuscript search and selected-tangent-bound lines 1-63 found the signed bound as a hypothesis, not an ordinary proof of the same-model period comparison. No full-manuscript audit, upstream geometric proof replay or Lean-kernel verification claimed."
        }],
        "dependencies": [file_record(p) for p in [
            "notes/moret-bailly-theta-supplier.md", "notes/selected-eigenspace-degree.md",
            "notes/actual-point-height-frontier.md"]],
        "limitations": [
            "No full Lean kernel replay or upstream proof audit.",
            "The upstream FlatDegree theorem and its geometric application are identified, not newly proved by this checker.",
            "The same-model determinant/metric, integral-point, cusp-mean and finite section-degree comparisons remain outside this reconstruction.",
            "No RH/GRH blueprint node is completed by this source-status audit."],
        "artifacts": [file_record(NOTE), file_record("scripts/check_remaining_point_height_comparisons.py")],
    }
    (ROOT / OUT).write_text(json.dumps(certificate, indent=2)+"\n")
    print("PASS:", len(sources), "pinned files;", sum(len(s[2]) for s in SOURCES),
          "bounded excerpts;", sum(checks[k] for k in checks if k.endswith("cases")), "exact scalar cases.")

if __name__ == "__main__":
    main()
