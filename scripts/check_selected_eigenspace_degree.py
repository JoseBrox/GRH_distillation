#!/usr/bin/env python3
"""Reproduce the signed scalar/rank reduction and pin its source contracts.

Exact algebra and bounded source integrity only. This does not supply the
logarithmic tangent estimate or replay any upstream Lean proof.
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
NOTE = "notes/selected-eigenspace-degree.md"
OUT = "certificates/selected-eigenspace-degree.json"
AS = "Development.AutomorphicSpectrum."
WB = "Development.WeilBound.CoreStatements.PlurisubharmonicCones."
SOURCES = [
    (AS+"Definitions.MetricPeriods.IsAdapted",
     "c662e60bc7ff8d80c010932874bb95d627f339a3f235c37da2e7baf928ceabb7",
     [[30,65]]),
    (AS+"Proofs.MetricProofs.AdaptedFamilyExistsOnEigenspaceStatement",
     "a03c0c52a4b238d8a5278aaa3cda83f1d2701974b96417696537be53a5664dec",
     [[1,8]]),
    (WB+"ExistsSmulMemOfEig",
     "481621dcf3883eab908020fdb580939fb4bc6ece91a7de40b902be4ae1f526b7",
     [[9,89],[156,207]]),
    (WB+"HeightComparisonGlobalModel",
     "b61f96d5d0cb9a5af7174bee7b3f081d1120278d761dace6bfffd626f80df298",
     [[21,59],[150,164],[176,238]]),
    (AS+"Proofs.MetricProofs.AbelianPartHeightLinear",
     "8bd98110d2ea81597045b6574f8b8c6c12fb0dd9b4af6937943fca4a33b0d340",
     [[201,212]]),
    (WB+"FlatSat",
     "f34edb87ca7a8196a91080cf3435510c6c33e6fc1de14c9d976d82db95f423d8",
     [[11,20]]),
    (AS+"Proofs.GeometryProofs.SlopeBoundOfLineLargeDegree",
     "6d8c7e366d54ca3fb0c62416670882b27daee46d4ba5b876c7a40f9a1ee90d09",
     [[17,19]]),
    (AS+"Proofs.GeometryProofs.SlopeBoundOfLargeDegreeLine",
     "bff503206718f3b3dcd6f4af11fc488586b49e925361aa4ac15401f12b25e7fa",
     [[94,143]]),
    (AS+"Proofs.GeometryProofs.LineOfKeyDegree",
     "f97fc5d8c9d4b47b2509219c7044e59ae324ace8c6a1518fd7998cd1a02bc91c",
     [[196,267],[269,375]]),
    (AS+"Proofs.GeometryProofs.ExistsThetaSectionsBounded",
     "18598167c7fa5870f154f53ab7e85b1e1d0cc2fb80becfcd2b48a841f16cb898",
     [[210,245],[403,468]]),
    (AS+"Definitions.GlobalGeometry.IsThetaMeanSquareNorm",
     "f8ce5066b02316caeaaa3d7438c2324d6b170c19201f240021851bd62d4bd2db",
     [[98,131]]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def check_sources():
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, expected, ranges in SOURCES:
        rel = "lean/src/"+module.replace(".","/")+".lean"
        data = (ROOT/"build/source-cache/jsmorph/rh"/REV/rel).read_bytes()
        blob = hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
        assert blob == blobs[module] and sha(data) == expected, module
        lines = data.splitlines()
        excerpts = []
        for start,end in ranges:
            assert 1 <= start <= end <= len(lines) and end-start < 120
            excerpts.append({"lines":[start,end],
                "sha256":sha(b"\n".join(lines[start-1:end])+b"\n")})
        records.append({"module":module,"path":rel,"sha256":expected,
            "git_blob_sha1":blob,"bytes":len(data),"line_count":len(lines),
            "inspected_excerpts":excerpts})
    return records


def check_algebra():
    X,Y,delta,nu = sp.symbols("X Y delta nu",real=True)
    T,b,d = X-nu,X-Y,X+Y+delta
    assert sp.expand(d-(2*T-b+delta+2*nu)) == 0
    signed_cases = 0
    for t,b0,delta0,nu0 in itertools.product(
            [F(-7,2),F(-1),F(0),F(1,3),F(2),F(10)],
            [F(-5),F(0),F(1,2),F(8)],
            [F(0),F(1,3),F(3)],[F(0),F(1,3),F(3)]):
        d0 = 2*t-b0+delta0+2*nu0
        if t > 0:
            assert max(-d0,F(0)) <= max(b0-delta0-2*nu0,F(0))
        signed_cases += 1
    rank_cases = 0
    for f,m,ca in itertools.product(range(1,6),range(12),
                                    [F(0),F(1,4),F(1,2),F(1),F(3)]):
        for r in range(m+1):
            k = m-r
            assert f*k == f*(m-r)
            assert f*ca*k+F(f*r,2) <= f*m*max(ca,F(1,2))
            rank_cases += 1
    lam,c = sp.symbols("lambda c",positive=True)
    gap = lam*sp.log(3+c)-sp.log(3+c*lam)
    assert sp.simplify(sp.diff(gap,lam)-
                       (sp.log(3+c)-c/(3+c*lam))) == 0
    return {
        "signed_identity":"d=2T-b+delta+2nu, symbolically exact",
        "rational_signed_cases":signed_cases,
        "exact_rank_and_toric_cases":rank_cases,
        "logarithmic_step":"Derivative identity checked; its positivity for lambda>=1,c>=0 follows analytically from log(3)>1 and c/(3+c*lambda)<=1. No floating-point inequality is used.",
        "scope":"Finite exact examples supplement, and do not replace, the complete algebraic proofs in Sections 1--2."
    }


def main():
    sources = check_sources()
    algebra = check_algebra()
    cert = {
        "schema_version":1,"result":"PASS","repository":"jsmorph/rh","commit":REV,
        "note":NOTE,"note_sha256":sha((ROOT/NOTE).read_bytes()),
        "script":"scripts/check_selected_eigenspace_degree.py",
        "script_sha256":sha(Path(__file__).read_bytes()),
        "source_files":sources,"algebra":algebra,
        "independent_reviews":[
            {"reviewer":"root","result":"PASS",
             "scope":"Sections 1--2: signed degree identity, two-case scalar proof, exact R=f(m-r), and maximum of the abelian and toric costs. No new upstream geometry audit."},
            {"reviewer":"rh_source_symmetry","result":"PASS",
             "scope":"Sections 1--2, including zero cases, integral-index signs, explicit logarithmic constant and toric/abelian convex combination. Independently hash-read ExistsSmulMemOfEig:156--207 and AdaptedFamilyExistsOnEigenspaceStatement:1--8. No review of the new theta-supplier implementation chain or Lean kernel replay is included in this entry."}
        ],
        "limitations":[
            "The selected logarithmic slope estimate remains a hypothesis.",
            "Section 3 records bounded source contracts; it does not certify their upstream geometric proofs.",
            "Integral torsion translates, the same prescribed metrics, finite field extension and the absolute Siegel input must still be supplied.",
            "No blueprint construction node is closed."
        ]
    }
    (ROOT/OUT).write_text(json.dumps(cert,indent=2)+"\n")
    print(json.dumps({"result":"PASS","source_files":len(sources),
        "source_excerpts":sum(len(s["inspected_excerpts"]) for s in sources),
        "algebra":algebra,"certificate":OUT},indent=2))


if __name__ == "__main__":
    main()
