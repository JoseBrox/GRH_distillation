#!/usr/bin/env python3
"""Exact algebra/source checks for the shorter theta-and-jet argument.

This checks a proved conditional reduction. It does not construct the theta
sections, audit all upstream geometry, or replay a Lean kernel.
"""
from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NOTE = "notes/theta-jet-slope-reduction.md"
OUT = "certificates/theta-jet-slope-reduction.json"
AS = "Development.AutomorphicSpectrum."
AV = "Development.AbelianVarietyTheory."
SOURCES = [
    (AS+"Definitions.GlobalGeometry.IsThetaMeanSquareNorm",
     "f8ce5066b02316caeaaa3d7438c2324d6b170c19201f240021851bd62d4bd2db",
     [[17,24],[51,66],[77,87],[98,131]]),
    (AS+"Definitions.GlobalGeometry.SlopeBoundSt",
     "cfafbde60240b4fa49e09ead297c6d14c3b3e6ee897fa1be5c982e17a4d42088",
     [[69,76]]),
    (AV+"PublishedTheorems.RelativeAmpleness.RelAmpleAndKTrivIff",
     "867395382178cb226fdf6ee71f332a8a2ba98544a8fc247583fc3c1b20c98cd6",
     [[17,23]]),
    (AS+"Proofs.GeometryProofs.ExistsIntegralJetBasis",
     "9876cc5188b6f04e76119b216ba433d212ab734ec0f2838fcdd4abc1045802c6",
     [[102,174],[239,276]]),
    (AS+"Proofs.AdelicProofs.IntegralFlagEmbeddingCriterion",
     "26daac5bd59937845d4fbb6de000c66fd714154ffb0de87704d04212ac196478",
     [[263,351]]),
    (AS+"Proofs.GeometryProofs.LineOfKeyDegree",
     "f97fc5d8c9d4b47b2509219c7044e59ae324ace8c6a1518fd7998cd1a02bc91c",
     [[196,267],[269,375]]),
    (AS+"Proofs.GeometryProofs.ExistsThetaSectionsBounded",
     "18598167c7fa5870f154f53ab7e85b1e1d0cc2fb80becfcd2b48a841f16cb898",
     [[403,468]]),
    (AS+"Proofs.AdelicProofs.ShortVectorOfSubmodule",
     "a012f6447b88efb6807386f3a1b97286d49b6d9e19a03fe743285834ebbeaa3f",
     [[249,324]]),
    (AS+"Proofs.GeometryProofs.SlopeBoundOfLargeDegreeLine",
     "bff503206718f3b3dcd6f4af11fc488586b49e925361aa4ac15401f12b25e7fa",
     [[117,142]]),
    (AS+"Proofs.GeometryProofs.PolarizedDataFieldExtensionStatement",
     "d8c089d6e5968b5106d7d0d04f2a7e3623f04fe08d4724a3058020160e304b90",
     [[12,12]]),
    (AS+"Proofs.GeometryProofs.KeyDegreeOfBadReduction",
     "fe9d0a9f7a7e9fe7debea2b1748dcda19149d783d96e52e0b27558bafe73432f",
     [[223,302]]),
    (AS+"Proofs.GeometryProofs.KeyBadReductionHolds",
     "4020395ba9bb52fa810327d8c70eba2fac2f39b8b685ac8c9c85d3c06bce9abd",
     [[18,18]]),
    ("Development.WeilBound.CoreStatements.HodgeTatePoints.LieMultComp",
     "489ec24a9a800b82411fb8582328d0e2cd468cdb2e9533ae8f7598f4032a6d4e",
     [[80,117],[139,160]]),
    (AS+"Proofs.GeometryProofs.TorsionValueIntegral",
     "962bef6ac223d652b52fde1a279662c2a97324abe6d77d38997f90415fc0dbc8",
     [[476,510],[679,732]]),
    (AV+"Proofs.DegenerationProofs.ExistsWeightZeroSectionUnitIntegralTorsionPoint",
     "4bdae7671f2107298f95dbab280e27d1b28b43c927f96a7b3a52cbf2fff664ac",
     [[39,63]]),
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
    for module,expected,ranges in SOURCES:
        rel = "lean/src/"+module.replace(".","/")+".lean"
        data = (ROOT/"build/source-cache/jsmorph/rh"/REV/rel).read_bytes()
        blob = hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
        assert blob == blobs[module] and sha(data) == expected,module
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


def check_flag_examples():
    """Rational rows need not be integral; leading restrictions are integral."""
    cases = 0
    for r in range(2,7):
        for k in range(1,r):
            for p in [2,3,5]:
                J = sp.zeros(k+1,r)
                for i in range(k+1):
                    J[i,i] = p+i
                    for j in range(i):
                        J[i,j] = sp.Rational((-1)**(i+j)*(i+j+1),p**(i-j))
                # A unimodular integral domain-basis change hides the flag.
                U = sp.eye(r)
                for j in range(r-1):
                    E = sp.eye(r)
                    E[j,j+1] = j+2
                    U = U*E
                J = J*U
                gram = J*J.T
                residuals = []
                prod = sp.Integer(1)
                for i in range(k+1):
                    v = J.row(i)
                    for w in residuals:
                        v -= (v.dot(w)/w.dot(w))*w
                    assert v.dot(v) > 0
                    prod *= v.dot(v)
                    residuals.append(v)
                assert sp.simplify(prod-gram.det()) == 0
                for cols in itertools.combinations(range(r),k+1):
                    minor = J[:,cols].det()
                    assert minor.q == 1
                cases += 1
    return cases


def check_jets():
    t = sp.symbols("t")
    cases = 0
    for k in range(1,9):
        for a,b in [(1,1),(2,-3),(-1,2)]:
            u0 = a+2*t-t**2
            u1 = b*t+t**2-t**3
            funcs = [sp.Poly(sp.expand(u0**(k-i)*u1**i),t)
                     for i in range(k+1)]
            J = sp.Matrix([[math.factorial(j)*funcs[i].nth(j)
                            for i in range(k+1)] for j in range(k+1)])
            for i in range(k+1):
                for j in range(i):
                    assert J[j,i] == 0
                assert J[i,i] == math.factorial(i)*a**(k-i)*b**i
            target = math.prod(math.factorial(i) for i in range(k+1))
            target *= (a*b)**(k*(k+1)//2)
            assert J.det() == target and target != 0
            cases += 1
    # The factorial estimate is exact; Cauchy's analytic theorem is not a
    # numerical assertion of this script.
    for k in range(1,61):
        for i in range(1,k+1):
            assert math.factorial(i)**2 <= i**(2*i)
            assert i**i <= k**i
    return cases


def ceil_sqrt_fraction(z):
    a = math.isqrt(z.numerator//z.denominator)
    while F(a*a) < z:
        a += 1
    return a


def check_parameters():
    cases = 0
    for g,h,A,B,L in itertools.product(range(1,8),
            [F(0),F(1,3),F(2),F(100)],
            [F(0),F(1,2),F(3)],[F(0),F(1,4),F(2)],
            [F(1),F(3,2),F(4)]):
        Y = 2+g+h
        V = h/2+A*g+B*g*L
        Z = 1+g+2*V
        a = ceil_sqrt_fraction(Z)
        m,n,k = 3*a,9*a*a,3*a*a
        assert n == m*m == 3*k
        assert 3*Z <= k <= 12*Z and n <= 36*Z
        assert Z <= (1+2*A+2*B)*Y*L
        for U in [-V-F(1),F(0),V/2,V]:
            assert g+2*max(U,F(0)) <= Z
            # L0 stands for log(3k), known analytically to exceed one.
            for L0 in [F(1),F(2),F(7)]:
                assert F(g*L0+2*U,k) <= Z*L0/k <= L0/3
        cases += 1
    g,h,A,B,L = sp.symbols("g h A B L",real=True)
    Y = 2+g+h
    Z = 1+g+h+2*A*g+2*B*g*L
    positive_form = Y*(L-1)+1+2*A*(g*(L-1)+(2+h)*L)+2*B*(2+h)*L
    assert sp.expand((1+2*A+2*B)*Y*L-Z-positive_form) == 0
    k,U,lr,lb,ll = sp.symbols("k U lr lb ll",real=True)
    total = (k+1)*(lr/2+U)+k*(k+1)*(lb+ll)/2
    assert sp.simplify(2*total/(k*(k+1))-
                       (lb+ll+(lr+2*U)/k)) == 0
    return cases


def check_quadratic_completion():
    n,x1,x2,y1,y2,a,b,c = sp.symbols("n x1 x2 y1 y2 a b c")
    Q = lambda x,y: a*x*x+2*b*x*y+c*y*y
    polar = 2*(a*x1*y1+b*x1*y2+b*x2*y1+c*x2*y2)
    assert sp.expand(Q(n*x1+y1,n*x2+y2)-
                     (n*n*Q(x1,x2)+n*polar+Q(y1,y2))) == 0
    cases = 0
    for B in [((0,0),(0,0)),((1,0),(0,1)),((1,1),(0,0)),((2,-1),(1,3))]:
        q = lambda v: sum(sum(row[i]*v[i] for i in range(2))**2 for row in B)
        for x,y,n0 in itertools.product(itertools.product(range(-2,3),repeat=2),
                itertools.product(range(-2,3),repeat=2),range(1,5)):
            pol = q((x[0]+y[0],x[1]+y[1]))-q(x)-q(y)
            left = F(q(x))+F(pol,n0)+F(q(y),n0*n0)
            right = F(q((n0*x[0]+y[0],n0*x[1]+y[1])),n0*n0)
            assert left == right and right >= 0
            cases += 1
    return cases


def main():
    sources = check_sources()
    algebra = {"rational_flag_examples":check_flag_examples(),
               "exact_jet_matrices":check_jets(),
               "exact_parameter_cases":check_parameters(),
               "exact_quadratic_completion_cases":check_quadratic_completion(),
               "scope":"Exact algebra and finite examples supplement the complete conditional proofs; no floating-point estimate is decisive."}
    refpath = "build/reference-cache/genestier-ngo-shimura.pdf"
    data = (ROOT/refpath).read_bytes()
    expected = "c307cf42b5c263839e973c18929e0c034b7273fdb3a086f681b1d30444ccb2f0"
    assert sha(data) == expected
    imagepath = "build/reference-cache/genestier-ngo-shimura-p13.png"
    cert = {
        "schema_version":1,"result":"PASS","repository":"jsmorph/rh","commit":REV,
        "note":NOTE,"note_sha256":sha((ROOT/NOTE).read_bytes()),
        "script":"scripts/check_theta_jet_slope_reduction.py",
        "script_sha256":sha(Path(__file__).read_bytes()),"source_files":sources,
        "tex":{"path":"paper/shared/selected-tangent-bound.tex",
               "sha256":sha((ROOT/"paper/shared/selected-tangent-bound.tex").read_bytes()),
               "scope":"Shared ordinary-mathematics presentation, with its final absolute-Siegel passage now supplied by the companion classical theorem. Build and visual review are recorded separately.",
               "classical_supplier_certificate":"certificates/absolute-siegel-supplier.json"},
        "primary_reference":{"authors":"A. Genestier and B.-C. Ngo",
            "title":"Lectures on Shimura varieties","theorem":"2.2.3",
            "url":"https://www.math.uchicago.edu/~ngo/Shimura.pdf",
            "path":refpath,"bytes":len(data),"sha256":expected,
            "visually_inspected_pdf_pages":[13],
            "rendered_image":imagepath,
            "rendered_image_sha256":sha((ROOT/imagepath).read_bytes()),
            "scope":"Verified the very-ampleness theorem's exact hypothesis and its neighboring explanation; no complete audit of the lectures or Mumford's cited proof."},
        "algebra":algebra,
        "independent_reviews":[
            {"reviewer":"transport_defect","result":"PASS",
             "scope":"Ordinary mathematics in Sections 1--3: localized flag integrality, product formula, Gram--Schmidt, generic jet rank, Gaussian Cauchy/factorial constants, principal generator count, rounding and all explicit logarithmic constants. No independent primary-PDF or source-byte audit and no arithmetic theta construction is included in this review."},
            {"reviewer":"transport_defect","result":"PASS",
             "reviewed_tex_sha256":"1d1cc7311be04997507b9730047cec50a3ac08414b62f94ddb03ecfa60decb74",
             "scope":"The shared presentation before the final classical-Siegel addition: signed selected degrees, exact ranks, undivided jets, section count, constants, same-metric field extension and the then-conditional absolute-Siegel passage. The new classical supplier is separately reviewed in certificates/absolute-siegel-supplier.json. No new primary-PDF or upstream-source proof audit."},
            {"reviewer":"root","result":"PASS",
             "scope":"Ordinary mathematics in Sections 1--5: flag, Cauchy, level choice, absolute-Siegel consequence and quadratic completion, conditional on the explicitly supplied arithmetic inputs. No upstream Lean replay or independent arithmetic theta construction is claimed."}
        ],
        "limitations":[
            "No actual integral theta construction or uniform finite-prime supplier is proved by this checker.",
            "The prescribed principal polarization, ordinary pi-times-Appell--Humbert norm, rigidification and isometric field-extension data are retained.",
            "Absolute Siegel is now supplied by the independently audited classical theorem and principalization argument in certificates/absolute-siegel-supplier.json; the theta construction remains open.",
            "The exact generator count r is retained; nonprincipal polarizations require the extra log h0(L) term.",
            "No Lean kernel replay, whole-source audit, or blueprint node closure."
        ]
    }
    (ROOT/OUT).write_text(json.dumps(cert,indent=2)+"\n")
    print(json.dumps({"result":"PASS","source_files":len(sources),
        "source_excerpts":sum(len(s["inspected_excerpts"]) for s in sources),
        "algebra":algebra,"certificate":OUT},indent=2))


if __name__ == "__main__":
    main()
