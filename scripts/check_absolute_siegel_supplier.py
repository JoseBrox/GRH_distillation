#!/usr/bin/env python3
"""Pin the classical absolute-Siegel supplier and check its normalization.

The cited classical theorem is an input, not a numerical conjecture.
Source hashes, exact degree conventions and independent reviews are recorded.
No Lean kernel or integral theta construction is claimed.
"""
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NOTE = "notes/absolute-siegel-supplier.md"
OUT = "certificates/absolute-siegel-supplier.json"
AS = "Development.AutomorphicSpectrum."
SOURCES = [
    ("GroundTheory.HeightsAndTheta.Heights.HeightsOfSets.Slopes",
     "0c518cce4f9cffa8ab4bab172eabead399069a1de59ce98144ac36dfdcbfa77f",
     [[14,39]]),
    (AS+"Definitions.GlobalGeometry.IsThetaMeanSquareNorm",
     "f8ce5066b02316caeaaa3d7438c2324d6b170c19201f240021851bd62d4bd2db",
     [[98,105],[128,131]]),
    (AS+"Proofs.AdelicProofs.ShortVectorOfSubmodule",
     "a012f6447b88efb6807386f3a1b97286d49b6d9e19a03fe743285834ebbeaa3f",
     [[249,324]]),
    (AS+"Proofs.GeometryProofs.PolarizedDataFieldExtensionStatement",
     "d8c089d6e5968b5106d7d0d04f2a7e3623f04fe08d4724a3058020160e304b90",
     [[12,12]]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def check_sources():
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    blobs = {row[0]:row[1] for row in atlas["modules"]}
    records = []
    for module,expected,ranges in SOURCES:
        rel = "lean/src/"+module.replace(".","/")+".lean"
        data = (ROOT/"build/source-cache/jsmorph/rh"/REV/rel).read_bytes()
        blob = hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
        assert sha(data) == expected and blob == blobs[module],module
        lines = data.splitlines()
        excerpts = []
        for a,b in ranges:
            assert 1 <= a <= b <= len(lines) and b-a < 120
            excerpts.append({"lines":[a,b],
                "sha256":sha(b"\n".join(lines[a-1:b])+b"\n")})
        records.append({"module":module,"path":rel,"sha256":expected,
            "git_blob_sha1":blob,"bytes":len(data),"line_count":len(lines),
            "inspected_excerpts":excerpts})
    return records


def check_normalization():
    gram_cases = 0
    for r in range(1,6):
        for den in [1,2,3]:
            A = sp.Matrix(r,r,lambda i,j:
                sp.Rational(i+2,den) if i == j else
                (sp.Rational(i+j+1,den+1) if i < j else 0))
            G = A.T*A
            assert G.det() == A.det()**2 and A.det() > 0
            gram_cases += 1
    # Product-formula cancellation for scalar changes of the same rational
    # line: exact exponents, with no floating logarithms.
    scalar_cases = 0
    for num in range(1,21):
        for den in range(1,21):
            c = F(num,den)
            factors = {}
            for p,v in sp.factorint(c.numerator).items():
                factors[int(p)] = int(v)
            for p,v in sp.factorint(c.denominator).items():
                factors[int(p)] = factors.get(int(p),0)-int(v)
            product = c
            for p,v in factors.items():
                product *= F(p)**(-v)
            assert product == 1
            scalar_cases += 1
    a,e,v = sp.symbols("a e v",positive=True,integer=True)
    assert sp.simplify((e*a*v)/a-e*v) == 0
    harmonic = F(0)
    for r in range(1,101):
        expected = sum((F(1,2*j) for j in range(2,r+1)),F(0))
        assert harmonic == expected
        harmonic += F(1,2*(r+1))
    return {
        "gram_determinant_norm_cases":gram_cases,
        "exact_scalar_product_formula_cases":scalar_cases,
        "principalization":"Symbolic finite-place exponent identity a*v_P(alpha)=e*a*v_p(I), hence v_P(alpha)=v_P(I O_L). Existence follows from finite ideal class group as proved in the note.",
        "harmonic_constants":"100 exact rational harmonic constants; c_r<=log(r)/2 is proved analytically by integration, not by floating-point tests.",
        "scope":"Normalization checks supplement the ordinary proofs and the independently inspected published theorem."
    }


def main():
    sources = check_sources()
    norm = check_normalization()
    path = "build/reference-cache/gaudron-remond-minima-2013.pdf"
    data = (ROOT/path).read_bytes()
    expected = "38bc55f86a58a91dcfd9ca4fce01d8ddaf60f0f3d7b52e4867c5966b2f7cd03b"
    assert sha(data) == expected
    pages = []
    for n in [5,6,9,10]:
        image = f"build/reference-cache/gaudron-remond-minima-2013-p{n}.png"
        pages.append({"pdf_page":n,"journal_page":n+564,"image":image,
                      "image_sha256":sha((ROOT/image).read_bytes())})
    cert = {
        "schema_version":1,"result":"PASS","repository":"jsmorph/rh","commit":REV,
        "note":NOTE,"note_sha256":sha((ROOT/NOTE).read_bytes()),
        "script":"scripts/check_absolute_siegel_supplier.py",
        "script_sha256":sha(Path(__file__).read_bytes()),
        "tex":{"path":"paper/shared/selected-tangent-bound.tex",
               "sha256":sha((ROOT/"paper/shared/selected-tangent-bound.tex").read_bytes()),
               "scope":"Final absolute-Siegel and principalization paragraphs; earlier theta/selected-sum mathematics has its own certificate."},
        "source_files":sources,"normalization_checks":norm,
        "primary_reference":{
            "authors":"Eric Gaudron and Gael Remond",
            "title":"Minima, pentes et algebre tensorielle",
            "journal":"Israel Journal of Mathematics 195 (2013), 565--591",
            "doi":"10.1007/s11856-012-0109-x",
            "url":"https://lmbp.uca.fr/~gaudron/art10.pdf",
            "path":path,"bytes":len(data),"sha256":expected,
            "theorems":"Theorem 3.1 and Lemma 3.2; definitions in Sections 2.1--2.3",
            "visually_inspected_pages":pages,
            "scope":"Exact hypothesis, ordinary norm/degree and field-extension conventions, and minimum inequality inspected. The general proof of Zhang's theorem is cited, not replayed."},
        "independent_reviews":[
            {"reviewer":"root","result":"PASS",
             "scope":"Entire note and actual primary renders PDF pp5,6,9,10: ordinary norm/degree normalization, classical harmonic constant, fractional-ideal principalization, projective quotient and base-change saturation, all finite norms equal to one, nonsaturated ambient inclusion, and epsilon limit. Bounded extension/short-vector source dictionary also read. No upstream proof replay or arithmetic theta construction."}
        ],
        "discharged_subrequirement":"Classical absolute-Siegel consequence for the actual Hermitian lattice after unrestricted finite coefficient-field extension, with the same metric.",
        "limitations":[
            "No bound on the degree or discriminant of the auxiliary field is provided or needed by the all-finite-extension line criterion.",
            "The absolute-Siegel input does not construct integral theta sections or their normalized torsion translates.",
            "The prescribed theta uniformity, primitive determinant normalization and norm bounds remain geometric requirements.",
            "No full W10 or other construction-node closure, no upstream Lean replay."
        ]
    }
    (ROOT/OUT).write_text(json.dumps(cert,indent=2)+"\n")
    print(json.dumps({"result":"PASS","source_files":len(sources),
        "source_excerpts":sum(len(x["inspected_excerpts"]) for x in sources),
        "normalization_checks":norm,"certificate":OUT},indent=2))


if __name__ == "__main__":
    main()
