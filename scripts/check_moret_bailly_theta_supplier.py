#!/usr/bin/env python3
"""Authenticate the classical same-model theta supplier and exact constants.

The algebra checks supplement the ordinary proofs and the stated classical
theorems. They are not a proof replay of Moret--Bailly or Autissier and do
not certify the full upstream Lean project.
"""
from fractions import Fraction as F
import gzip
import hashlib
import json
from math import factorial, isqrt
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NOTE = "notes/moret-bailly-theta-supplier.md"
OUT = "certificates/moret-bailly-theta-supplier.json"
TOR = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry.ToroidalCompactification."
SEMI = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.SemiabelianSchemes."
AS = "Development.AutomorphicSpectrum."
SOURCES = [
    (TOR+"TwoWeightEqOneAddRoot",
     "3646386e9cd25287a50eb1ad82456c5b26316207741b8ed7298d46aa4f9d7826",
     [[72,91]]),
    (TOR+"IsGrpPullback",
     "e27cd707ff5b70d57002a494ab607f9840c0a77375620b8cc99086003bf154fa",
     [[25,29]]),
    (SEMI+"AbelianSchemeQuotients.IsAbelianScheme",
     "93bbb87c48ab64304c325f052098ab90b761f9b77b581d9e967e24cd2d8d8f20",
     [[13,17],[41,48]]),
    ("ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.ExtensionDescent.NonzeroLocus",
     "0fb85f490332679f3fef1154ef93d5b1038be586871a9c493882150d57966cbf",
     [[26,57]]),
    (AS+"Definitions.GlobalGeometry.SlopeBoundSt",
     "cfafbde60240b4fa49e09ead297c6d14c3b3e6ee897fa1be5c982e17a4d42088",
     [[69,76]]),
    (AS+"Definitions.GlobalGeometry.IsThetaMeanSquareNorm",
     "f8ce5066b02316caeaaa3d7438c2324d6b170c19201f240021851bd62d4bd2db",
     [[26,66],[77,118],[122,131]]),
    (AS+"Proofs.GeometryProofs.LineOfKeyDegree",
     "f97fc5d8c9d4b47b2509219c7044e59ae324ace8c6a1518fd7998cd1a02bc91c",
     [[213,215],[269,299],[311,324],[348,367]]),
    (AS+"Proofs.GeometryProofs.ExistsThetaSectionsBounded",
     "18598167c7fa5870f154f53ab7e85b1e1d0cc2fb80becfcd2b48a841f16cb898",
     [[403,468]]),
    (AS+"Proofs.MetricProofs.ExistsThetaSupBoundLogMean",
     "06331ebcaf206732e91fb53bd60e38f052a0316f400d2e5b1c728554f0e9109f",
     [[452,485],[521,556]]),
]
REFERENCES = [
    {
        "title":"Theta height and Faltings height",
        "author":"Fabien Pazuki",
        "publication":"Bulletin de la Société Mathématique de France 140 (2012), 19–49",
        "url":"https://www.numdam.org/item/BSMF_2012__140_1_19_0.pdf",
        "path":"build/reference-cache/pazuki-theta-faltings-2012.pdf",
        "sha256":"9f957d234f98aee294676cc97e103a61559722ba1749c58d523bb1ca398c5206",
        "bytes":917619,
        "viewed_pdf_pages":[9,11,12,14,15,16,17,21,22],
        "used_clauses":"Definition2.1; sections2.3.1–2.3.2 and Proposition2.5; Definition3.1; Theorem3.4(i)–(v); Proposition5.1.",
    },
    {
        "title":"Semistable reduction for abelian varieties",
        "author":"Brian Conrad",
        "url":"https://math.stanford.edu/~conrad/DarmonCM/2011Notes/SemistableReduction.pdf",
        "path":"build/reference-cache/conrad-semistable-reduction.pdf",
        "sha256":"bfbad9fc883b2a6ac6e5f842abc664c2ebc84c348b9d80fa4ca6313b37e28173",
        "bytes":345935,
        "viewed_pdf_pages":[10,11],
        "bounded_text_proof_pages":[12,13,14,15,16],
        "used_clauses":"Theorem4.4 and Corollary4.5, used with explicit smoothness. Néron mapping property, quasi-finiteness and Zariski main theorem proof read in bounded extracted text.",
    },
    {
        "title":"Un lemme matriciel effectif",
        "author":"Pascal Autissier",
        "publication":"Mathematische Zeitschrift 273 (2013), 355–361",
        "url":"https://arxiv.org/pdf/1104.5644v1",
        "author_revision_url":"https://www.math.u-bordeaux.fr/~pautissi/Matrix2.pdf",
        "path":"build/reference-cache/autissier-matrix-arxiv-1104.5644.pdf",
        "sha256":"1e6ce585c6e85a10a89423132d5975a6f34e7cb356b4b19368deda06fc190779",
        "bytes":127870,
        "viewed_pdf_pages":[2,4,5],
        "used_clauses":"Corollary1.4(p2); Riemann-form period minimum(p4); Faltings norm with denominator2^g(p5). Exact used clauses also checked against the later author PDF through the web reader; direct author download returned503.",
    },
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


def check_references():
    records = []
    for ref in REFERENCES:
        data = (ROOT/ref["path"]).read_bytes()
        assert len(data) == ref["bytes"] and sha(data) == ref["sha256"]
        entry = dict(ref)
        p = Path(ref["path"])
        entry["viewed_page_images"] = []
        for page in ref["viewed_pdf_pages"]:
            img = p.with_name(p.stem+f"-p{page}.png")
            image_data = (ROOT/img).read_bytes()
            entry["viewed_page_images"].append(
                {"page":page,"path":str(img),"sha256":sha(image_data),
                 "bytes":len(image_data)})
        records.append(entry)
    return records


def check_exact_algebra():
    # For principal complex periods P=[I X;0 Y], the Riemann-form
    # real volume is det(Y) det(Y^-1)=1. The determinant dual of pi H
    # has squared norm det(Y)/pi^g, the exact Deligne Hodge norm.
    metric_cases = 0
    p = sp.Symbol("pi",positive=True)
    for g in range(1,6):
        for den in [1,2,3,5]:
            A = sp.Matrix(g,g,lambda i,j:
                sp.Rational(i+2,den) if i == j else
                (sp.Rational(i+j+1,den+1) if i < j else 0))
            Y = A.T*A
            X = sp.Matrix(g,g,lambda i,j:sp.Rational(i+j+1,den+2))
            P = sp.BlockMatrix([[sp.eye(g),X],[sp.zeros(g),Y]]).as_explicit()
            H = Y.inv()
            real_gram = P.T*sp.diag(H,H)*P
            assert sp.simplify(real_gram.det()) == 1
            assert sp.simplify((p*H).det()**-1-Y.det()/p**g) == 0
            metric_cases += 1

    # Rational affine identities in heights, written coefficientwise.
    h,g,lp,l4 = sp.symbols("h g logpi log4",real=True)
    hfa = h-g*lp/2
    shifted = sp.expand(hfa+g*(l4+2*lp)/2)
    assert sp.simplify(shifted-(h+g*(l4+lp)/2)) == 0
    for gg in range(1,31):
        for hh in [F(0),F(1,7),F(1),F(13,2),F(100)]:
            assert 1+16*hh+24*gg <= 24*(2+gg+hh)
    ball_affine_cases = 150

    level_cases = 0
    for den in range(1,13):
        for num in range(den,20*den+1):
            Z = F(num,den)
            a = isqrt(num//den)
            if a*a < Z:
                a += 1
            m,k,n = 6*a,12*a*a,36*a*a
            assert m%6 == 0 and n == m*m == 3*k
            assert 12*Z <= k <= 48*Z and n <= 144*Z
            level_cases += 1
    assert F(1)+F(1,12) == F(13,12)
    assert F(1,2)+F(1,12) == F(7,12)
    assert F(13,6)+F(91,12)+F(14,12)+1 == F(143,12) < 12
    # The elementary constants need only e>8/3 and 3<pi<22/7.
    elo = sum((F(1,factorial(j)) for j in range(5)),F(0))
    assert elo > F(8,3)
    assert F(8,3)**2 > F(44,7)   # exp2 > 2pi, hence log(2pi)<2
    assert F(8,3)**3 > F(88,7)   # exp3 > 4pi, hence log(4pi)<3
    assert F(8,3)**4 > 24        # log24<4
    assert F(8,3)**7 > 624       # log624<7
    assert F(8,3)**2 > 3         # log3<2
    assert 2+F(4,2)+F(2,4) < 5  # sup + L2 constant <5
    return {
        "rational_period_metric_cases":metric_cases,
        "exact_Faltings_shift":"hFa+(g/2)log(4pi^2)=hDeligne+(g/2)log(4pi)",
        "ball_affine_cases":ball_affine_cases,
        "exact_even_level_cases":level_cases,
        "constants":{"A0":5,"B0":1,"theta_power_upper_multiplier":144,
                     "maximal_slope_coefficient":12},
        "elementary_exponential_certificate":"Rational Taylor lower bound e>8/3; exact comparisons prove every logarithmic numerical simplification. Uses the elementary 3<pi<22/7.",
        "scope":"Exact algebra checks, not a computational proof of model existence, matrix lemma, theta irreducibility or all parameter values."
    }


def main():
    sources = check_sources()
    references = check_references()
    checks = check_exact_algebra()
    note = (ROOT/NOTE).read_bytes()
    text = note.decode()
    assert not any(ord(c)<32 and c not in "\n\t\r" for c in text)
    report = {
        "schema_version":1,
        "result":"PASS",
        "claim":"A classical same-model integral theta supplier, an elementary ball estimate plus Autissier's matrix lemma, and the prior jet/absolute-Siegel proofs imply mu_max(V)<=12 log(2+g+max(-deg_n(V),0)) for the prescribed principally polarized semistable tangent lattice.",
        "source_revision":{"repository":"jsmorph/rh","commit":REV},
        "sources":sources,
        "primary_references":references,
        "checks":checks,
        "independent_reviews":[
            {"reviewer":"root","result":"PASS",
             "scope":"Written Sections1–7, including the same-model bridge, elementary ball/Jensen and exact metric normalization argument, even level and coefficient12; independently viewed immutable Autissier PDF2,4,5. No full upstream Lean replay."},
            {"reviewer":"rh_source_symmetry","result":"PASS",
             "scope":"Written Sections1–7, including the new Autissier/ball supremum proof and coefficient12; independent Pazuki PDF9,11,12,14–17,21–22, Conrad10–11 and immutable Autissier PDF2,4,5; bounded exact source/model/metric contracts, including principal generic fibre. Explicitly no complete upstream source audit or proof replay of the cited deep theorems."}
        ],
        "dependencies":[
            "certificates/absolute-siegel-supplier.json",
            "certificates/theta-jet-slope-reduction.json",
            "certificates/selected-eigenspace-degree.json"
        ],
        "limitations":[
            "Cites the exact classical Moret–Bailly and Autissier theorems; does not reprove every deep theorem they use.",
            "The classical integral translate theorem is used only at positive even theta levels, chosen divisible by six.",
            "The restricted theta section need not be primitive in a larger section module on the identity component; that is not required.",
            "No assertion of the original local primitive determinant identity or arbitrary-trivialization torsion integrality is made.",
            "The whole W10 intersection/section construction and RH/GRH remain outside the completed subrequirement.",
            "No Lean kernel build, complete source audit or full manuscript review is claimed."
        ],
        "artifacts":{
            "note":{"path":NOTE,"sha256":sha(note),"bytes":len(note)},
            "checker":{"path":str(Path(__file__).resolve().relative_to(ROOT)),
                       "sha256":sha(Path(__file__).read_bytes())}
        }
    }
    (ROOT/OUT).write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
    print(f"PASS: {len(sources)} pinned source files; "
          f"{sum(len(s['inspected_excerpts']) for s in sources)} excerpts; "
          f"{len(references)} primary PDFs; "
          f"{checks['rational_period_metric_cases']} exact metric cases; "
          f"{checks['exact_even_level_cases']} exact even-level cases.")


if __name__ == "__main__":
    main()
