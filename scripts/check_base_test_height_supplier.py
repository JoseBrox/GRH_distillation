#!/usr/bin/env python3
"""Verify exact normalization algebra and pinned height-supplier evidence.

This checks source bytes and finite exact identities. It does not execute a
Lean kernel, prove any upstream geometry, or verify the actual point floor.
The two cited primary PDFs are cached under build/reference-cache; their
published URLs and inspected pages are recorded in the resulting certificate.
"""

from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NOTE = "notes/base-test-height-supplier.md"
OUT = "certificates/base-test-height-supplier.json"
HL = "GroundTheory.HeightsAndTheta.Heights.HodgeLowerBound."
AS = "Development.AutomorphicSpectrum."
SOURCES = [
    (HL + "FlagIndices",
     "8229a61265994066013cfba3d40283075be714c88a6bc13dae482cce930e9cc5",
     [[16, 43], [54, 93], [103, 108]]),
    (HL + "StatementsZhangLowerX",
     "3cec1a5cb749ab07ec8964b6c2d370eb399ba38d0e64736c43b7ef93e12eaf7f",
     [[1, 29]]),
    (HL + "PZhangLowerX",
     "af94b015e93f8fb0aa68b4efb867a74e6f1e313c0036a2b452420197aa70fa26",
     [[11, 37]]),
    (AS + "Proofs.DivisibilityProofs.SlopeLowerBaseSettings",
     "91b2a7711038280953fd65a2abd70a670bbdd6612a2d13cd61b94c8e31accf2e",
     [[16, 74], [76, 118]]),
    (AS + "Definitions.GlobalGeometry.HasBaseDegreeSettingStrict",
     "cb98a05d46d93ec16c181cd2fb9332cfbae2ea73eba12eee4fd1a2131f07749d",
     [[9, 24]]),
    (HL + "StatementsStokesGeo",
     "586897e80c74f9c79e6297b3e515ddd8dffdfe6ad4cc959ddb3250c54f422f8f",
     [[23, 49], [59, 109]]),
    (HL + "PStokesLimit",
     "cb2815ce357e5c56d1502af8f23eb0d518cb80637113addf8b09c83485d6eee9",
     [[16, 81]]),
    (HL + "FrameDefinitions.Weights",
     "539e80ecef5ef08eca3a978917697d6b39ec677ede3b7e4bbf2ccd9cfeb05bfc",
     [[122, 162]]),
    (HL + "FrameDefinitions.CpRegPhRegOfNonneg",
     "1c5861639dd75c124c17cd3d740384b940fba358530d3adff58679006a4ef965",
     [[67, 90]]),
    (HL + "FrameDefinitions.IsFrameOverLine",
     "e1496c0aa35b261840b79d8729f38ebfdd919b74bb682e88775dec67f091aea9",
     [[60, 99]]),
]

PDFS = [
    {"title": "Yuan--Zhang, Adelic Line Bundles on Quasi-projective Varieties, v9",
     "url": "https://arxiv.org/pdf/2105.13587v9",
     "path": "build/reference-cache/yuan-zhang-adelic-v9.pdf",
     "sha256": "3de89c1736979c44592447edd3bc5a14be9202fc9a07a0ea9d158e422a25145a",
     "inspected_pdf_pages": [232, 233, 234, 240, 241, 243],
     "scope": "Relative semipositivity, distinct arithmetic nefness, height normalization, Theorems A.4.2 and A.5.2; not a proof audit of the whole reference."},
    {"title": "Zhang, Positive Line Bundles on Arithmetic Varieties, JAMS 8 (1995), 187--221",
     "url": "https://archive.ymsc.tsinghua.edu.cn/pacm_download/355/9113-plav.pdf",
     "path": "build/reference-cache/zhang-positive-line-bundles-1995.pdf",
     "sha256": "9f2f38e87e1d81f05bf0ebbc714d209758563a686a7571a97705b8a99a7fda07",
     "inspected_pdf_pages": [15, 23],
     "inspected_journal_pages": [200, 208],
     "scope": "Rendered scan of relative-semiample context and Theorem 5.2; older stronger metric hypothesis retained honestly."},
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


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
        candidates = [ROOT / "build/source-cache/jsmorph/rh" / REV / rel,
                      ROOT / "build/lean-mirror" / rel]
        local = next((p for p in candidates if p.is_file()), None)
        if local is None:
            raise FileNotFoundError("Populate the pinned cache with source_excerpt.py for " + module)
        data = local.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == blobs[module] and sha(data) == expected, module
        lines = data.splitlines()
        excerpts = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines) and end - start < 120
            passage = b"\n".join(lines[start-1:end]) + b"\n"
            excerpts.append({"lines": [start, end], "sha256": sha(passage)})
        records.append({"module": module, "path": rel, "git_blob_sha1": blob,
                        "sha256": expected, "line_count": len(lines),
                        "inspected_excerpts": excerpts})
    return records


def check_pdfs():
    records = []
    for spec in PDFS:
        path = ROOT / spec["path"]
        if not path.is_file():
            raise FileNotFoundError("Cache the primary PDF from " + spec["url"] + " at " + str(path))
        data = path.read_bytes()
        assert sha(data) == spec["sha256"], spec["title"]
        records.append({**spec, "bytes": len(data), "sha256_verified": True})
    return records


def check_algebra():
    n = sp.symbols("n", integer=True, nonnegative=True)
    m = sp.symbols("m", positive=True)
    degree = sp.symbols("degree", positive=True)
    inter = sp.symbols("inter", real=True)
    scaled = (inter / m**(n+1)) / ((n+1) * degree / m**n)
    assert sp.simplify(scaled - inter / ((n+1)*degree*m)) == 0
    a, u, gap = sp.symbols("a u gap", real=True)
    limiting_intersection = (n+1)*degree*(a-u/2) + gap
    assert sp.simplify(limiting_intersection + (n+1)*u*degree/2 - (n+1)*a*degree - gap) == 0
    f, q, Ch, Cu, Lam = sp.symbols("f q Ch Cu Lam", positive=True)
    weights = sp.symbols("w0:3", positive=True)
    slacks = sp.symbols("g0:3", nonnegative=True)
    cusp_slacks = sp.symbols("t0:3", nonnegative=True)
    means = [-Ch*f*q*Lam - (Cu*f*q*Lam-cusp_slacks[i])/2 + slacks[i]
             for i in range(3)]
    beta = sum(weights[i]*means[i] for i in range(3))/(sum(weights)*f*q)
    expected_gap = sum(weights[i]*(slacks[i]+cusp_slacks[i]/2) for i in range(3))/(sum(weights)*f*q)
    assert sp.simplify(beta + (Ch+Cu/2)*Lam - expected_gap) == 0
    tensor_cases = 0
    signed_component_cases = 0
    for dim, power, raw_degree, raw_inter in itertools.product(
            range(0, 7), range(1, 8), (F(1, 3), F(2), F(9, 2)), (F(-11), F(0), F(13, 7))):
        h = raw_inter/((dim+1)*raw_degree)
        hscaled = (raw_inter/power**(dim+1))/((dim+1)*raw_degree/power**dim)
        assert hscaled == h/power
        tensor_cases += 1
    for weights0, aa, uu in itertools.product(
            ((1,), (1, 2), (2, 1, 4)), (F(-7), F(0), F(5, 2)),
            (F(-9, 2), F(0), F(8))):
        W = sum(weights0)
        d0 = F(3, 2)
        test_sum = F(0)
        signed = F(0)
        for i, w in enumerate(weights0):
            dd = d0 + i
            nn = i + 1
            ai, ui, slack = aa-i, uu+i, F(i, 3)
            Ii = (nn+1)*dd*(ai-ui/2+slack)
            si = Ii/((nn+1)*dd)
            test_sum += w*si
            signed += w*(ai-ui/2)
        assert test_sum/W >= signed/W
        signed_component_cases += 1
    return {"symbolic_tensor_power_identity": "PASS",
            "symbolic_signed_limit_identity": "PASS",
            "symbolic_three_component_normalization": "PASS",
            "exact_tensor_cases": tensor_cases,
            "exact_signed_component_cases": signed_component_cases,
            "scope": "These algebra checks supplement the written general proof; they do not verify convergence or geometric hypotheses."}


def main():
    sources = check_sources()
    references = check_pdfs()
    algebra = check_algebra()
    cert = {"schema_version": 1,
            "result": "PASS",
            "repository": "jsmorph/rh", "commit": REV,
            "note": NOTE, "note_sha256": sha((ROOT/NOTE).read_bytes()),
            "script": "scripts/check_base_test_height_supplier.py",
            "script_sha256": sha(Path(__file__).read_bytes()),
            "source_files": sources, "primary_references": references,
            "algebra": algebra,
            "independent_reviews": [{"reviewer": "root",
              "result": "PASS",
              "scope": "Note Sections 1--4 and complete TeX insertion: reciprocal limit, signs, tensor powers, exact component normalization; independently inspected modern primary PDF pp232,234,240,241,243. Finite nonempty components and finite constants made explicit after review."}],
            "limitations": ["No Lean replay or upstream proof audit.",
              "No actual point-height, regularization, cusp-mean, or test-identification supplier is proved by this certificate.",
              "The point-to-intersection step uses the modern relative-semipositive theorem, not an unqualified weakening of Zhang 1995.",
              "The limiting deduction fixes each geometric datum first; uniform numerical point-floor and cusp constants remain required."]}
    (ROOT/OUT).write_text(json.dumps(cert, indent=2)+"\n")
    print(json.dumps({"result": "PASS", "source_files": len(sources),
                      "source_excerpts": sum(len(r["inspected_excerpts"]) for r in sources),
                      "primary_pdfs": len(references), "algebra": algebra, "certificate": OUT}, indent=2))


if __name__ == "__main__":
    main()
