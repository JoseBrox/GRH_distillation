#!/usr/bin/env python3
"""Pinned source contracts and exact scalar checks for the point-height frontier.

No upstream geometric hypothesis or tangent-slope supplier is established by
this checker. It does not run a Lean kernel or identify the source integral
model with a Neron model.
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
NOTE = "notes/actual-point-height-frontier.md"
OUT = "certificates/actual-point-height-frontier.json"
HL = "GroundTheory.HeightsAndTheta.Heights.HodgeLowerBound."
AS = "Development.AutomorphicSpectrum."
WB = "Development.WeilBound.CoreStatements.PlurisubharmonicCones."
SOURCES = [
    (HL + "FrameDefinitions.CpRegPhRegOfNonneg",
     "1c5861639dd75c124c17cd3d740384b940fba358530d3adff58679006a4ef965",
     [[67, 90]]),
    (HL + "FrameDefinitions.IsFrameOverLine",
     "e1496c0aa35b261840b79d8729f38ebfdd919b74bb682e88775dec67f091aea9",
     [[60, 99]]),
    (AS + "Statements.GeometryStatements.NineGeoU",
     "e60e737cadb045801254fae41cd379e356fda04268e758da2aa7f592818040d1",
     [[19, 43], [53, 67]]),
    (AS + "Proofs.GeometryProofs.BaseSettingOfGoodTower",
     "3dee535e0c62c583a55cb9b69646758b310c54f798878fbcb2e8762b9d7a8c9f",
     [[91, 103]]),
    (AS + "Proofs.MetricProofs.CorrectedWeightRegularization",
     "67d2082919c078ffa738f9da97944c238388d050bb3c739812a070e80f0c6d0c",
     [[482, 499]]),
    (AS + "Proofs.GeometryProofs.CuspHeightUpper",
     "92acda917ce886dcbe003b2d949e8ab4a0b4a7cba8a1511d2a38e1724df12912",
     [[74, 105], [120, 158], [169, 223]]),
    (AS + "Proofs.GeometryProofs.CuspIntersectionHeight",
     "4ba85e090bf97d72e7f4de0342e13590c5172e5448f791b246efb4c8a9ac436e",
     [[162, 163], [397, 426]]),
    (WB + "HeightComparisonGlobalModel",
     "b61f96d5d0cb9a5af7174bee7b3f081d1120278d761dace6bfffd626f80df298",
     [[21, 59], [80, 88], [150, 164], [176, 238]]),
    (AS + "Definitions.GlobalGeometry.SlopeBoundSt",
     "cfafbde60240b4fa49e09ead297c6d14c3b3e6ee897fa1be5c982e17a4d42088",
     [[39, 43], [69, 76]]),
    ("GroundTheory.HeightsAndTheta.Heights.HeightsOfSets.Slopes",
     "0c518cce4f9cffa8ab4bab172eabead399069a1de59ce98144ac36dfdcbfa77f",
     [[14, 36]]),
    (AS + "Definitions.GlobalGeometry.HodgeIPIffHodgeFormConj",
     "72861f75151dc99d3739bfd10ada7f766b42adf957d2328d9fc320c8714018dc",
     [[20, 34]]),
    (AS + "Proofs.GeometryProofs.PhiDegFibLatLeOfIsOFamilyOfIsAdapted",
     "983a1eda3160559c93228668d49cdd99f035ec8738ec6b1ea998107d7e1cec28",
     [[126, 158]]),
    (AS + "Proofs.GeometryProofs.ExistsGeometricHeightConstants",
     "b29e532b9c73705a4f6b6225df2da92f5c639c5f989dd78a72ced6d6dedd8709",
     [[17, 25]]),
    (WB + "FlatSat",
     "f34edb87ca7a8196a91080cf3435510c6c33e6fc1de14c9d976d82db95f423d8",
     [[11, 20]]),
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
            raise FileNotFoundError("Populate pinned cache using source_excerpt.py for " + module)
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
    f, q = sp.symbols("f q", positive=True)
    r, X, T, rd, l4, idx = sp.symbols("r X T rd l4 idx", real=True)
    labelled_sum = f*q*X-f*r*rd+idx/2+T
    phi = labelled_sum-idx/2+f*r*l4/2
    raw = f*q*X+T-f*r*rd+f*r*l4/2
    assert sp.expand(phi-raw) == 0
    Cx, Ca, La = sp.symbols("Cx Ca La", real=True)
    claimed = (Cx+Ca+sp.Rational(1, 2))*f*q*La
    positive_remainder = (f*q*(Cx*La-X)+(Ca*f*q*La-T)
                          +f*r*rd+f*(q-r)*La/2+f*r*(La-l4)/2)
    assert sp.expand(claimed-raw-positive_remainder) == 0
    ch, ka, ratio, u, v, w = sp.symbols("ch ka ratio u v w", real=True)
    # phi=ch-w, corrected archimedean average exceeds x by u,
    # and auxiliary height is -ka+v.
    height = -(ch-w)+u+ratio*(-ka+v)
    assert sp.expand(height+ch+ratio*ka-(w+u+ratio*v)) == 0
    t = sp.symbols("t", positive=True)
    assert sp.simplify(sp.exp(-2*t)*sp.exp(2*t)) == 1
    assert sp.simplify(-sp.log(sp.exp(-2*t))/2) == t
    det, rank, scale = sp.symbols("det rank scale", positive=True)
    shifted = -sp.log(scale**(2*rank)*det)/2
    assert sp.expand_log(shifted, force=True) == -sp.log(det)/2-rank*sp.log(scale)
    H = sp.symbols("H", positive=True)
    assert sp.limit(H/sp.log(3+H), H, sp.oo) == sp.oo
    cases = 0
    for ff, qq, rr0, la, xx_slack, tt_slack, rd0, l4_slack in itertools.product(
            (1, 3), (1, 2, 7), (F(0), F(1, 2), F(1)),
            (F(1), F(5)), (F(0), F(2)),
            (F(0), F(3)), (F(0), F(4)), (F(0), F(1, 2))):
        rr = rr0*qq
        cx, ca = F(3), F(4)
        xx, tt = cx*la-xx_slack, ca*ff*qq*la-tt_slack
        log4pi = la-l4_slack
        raw0 = ff*qq*xx+tt-ff*rr*rd0+ff*rr*log4pi/2
        bound0 = (cx+ca+F(1, 2))*ff*qq*la
        assert raw0 <= bound0
        cases += 1
    return {"signed_index_cancellation": "PASS",
            "selected_degree_bound_positive_remainder": "PASS",
            "regularized_point_floor_signed_identity": "PASS",
            "abstract_degree_zero_large_slope_example": "PASS",
            "norm_rescaling_degree_shift": "PASS",
            "published_numeric_envelope_not_logarithmic": "PASS",
            "exact_rational_budget_cases": cases,
            "scope": "Finite and symbolic algebra supplements the written proof; no actual geometric instance of the slope or selected-degree hypothesis is verified."}


def main():
    sources = check_sources()
    algebra = check_algebra()
    pdf = ROOT / "build/reference-cache/gaudron-arakelov-2019.pdf"
    expected = "1d8cb2c3ce8c0d948f84c603db373082083bc7f80b5422f45dd3313b186e433d"
    assert sha(pdf.read_bytes()) == expected
    reference = {
        "title": "Eric Gaudron, Some explicit computations in Arakelov geometry of abelian varieties, J. Ramanujan Math. Soc. 34 (2019), 433--447",
        "url": "https://lmbp.uca.fr/~gaudron/art19.pdf",
        "path": "build/reference-cache/gaudron-arakelov-2019.pdf",
        "sha256": expected,
        "bytes": pdf.stat().st_size,
        "visually_inspected_pdf_pages": [4, 5, 12],
        "visually_inspected_journal_pages": [436, 437, 444],
        "additional_text_inspection": "Section 4.1, journal page 443; finite extension and metric choice.",
        "scope": "Proposition 4.2 and its actual hypotheses, degree convention and metric; no complete proof audit of this paper."}
    cert = {
        "schema_version": 1, "result": "PASS",
        "repository": "jsmorph/rh", "commit": REV,
        "note": NOTE, "note_sha256": sha((ROOT/NOTE).read_bytes()),
        "script": "scripts/check_actual_point_height_frontier.py",
        "script_sha256": sha(Path(__file__).read_bytes()),
        "source_files": sources, "primary_reference": reference, "algebra": algebra,
        "independent_reviews": [{
            "reviewer": "rh_source_symmetry",
            "result": "PASS",
            "scope": "Ordinary mathematics in note Sections 1--4; HtU and SlopeBoundSt quantifiers; corrected metric and height identities; signed index cancellation and selected-degree deduction; ordinary degree and pi-times-Appell-Humbert metric; actual Gaudron journal pages 436,437,444. Independently recomputed all 14 source Git/SHA256 records and 22 excerpt hashes, primary PDF hash, and reran all 576 exact algebra cases. No upstream proof replay, actual selected-degree supplier, or Neron integral-model identification."
        }, {
            "reviewer": "root",
            "result": "PASS",
            "scope": "Full note read: scalar reductions, signs, quantified selected-sum target and carefully limited numerical non-implication. This review entry does not assert a fresh primary-PDF audit."
        }],
        "limitations": [
            "No Lean kernel replay and no audit of all upstream proofs.",
            "The universal logarithmic tangent-slope hypothesis and the smaller selected-eigenspace degree bound remain unproved here.",
            "The source integral tangent model is not identified with the Neron model in this audit.",
            "The classical estimate is insufficient for the displayed logarithmic interface; no claim of falsity or impossibility for the actual geometric family is made.",
            "Actual point uniformity, integral comparisons, regularization, cusp mean and same-data intersection limits remain geometric inputs.",
            "No blueprint construction node is closed."
        ]}
    (ROOT/OUT).write_text(json.dumps(cert, indent=2)+"\n")
    print(json.dumps({"result": "PASS", "source_files": len(sources),
                      "source_excerpts": sum(len(r["inspected_excerpts"]) for r in sources),
                      "algebra": algebra, "certificate": OUT}, indent=2))


if __name__ == "__main__":
    main()
