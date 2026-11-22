#!/usr/bin/env python3
"""Provenance and exact algebra checks for negative-weight Selmer rigidity.

This is not a computation of a Selmer group or a verification of the
classical global duality, K-theory, Baire, or Bloch--Kato theorems.
"""

import gzip
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
U = BASE + "UnitaryThreeGroups."
SOURCES = [
    (U + "BlochKatoNonpositiveWeight",
     [(194, 243), (297, 359), (363, 414)]),
    (U + "AdRepBaseLiftApply", [(18, 39)]),
    (U + "UnitaryThreeReflectionRight", [(235, 257), (277, 301)]),
    (BASE + "LevelCohomology.FdAdjoinRange", [(17, 96)]),
    ("Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues."
     "CompactGroupRepDefinedOverFiniteExtension", [(14, 53)]),
    (U + "TanCocIsBK", [(162, 190)]),
    (U + "GRepresents", [(128, 138)]),
    (U + "PtHypOf", [(52, 89)]),
    (U + "BaseRepGL3NormalisedOfPsiEqOne", [(53, 73)]),
    (U + "ZetaReducibleRepEqSubInvAndIsUnit", [(5, 20)]),
    (U + "NormCob", [(30, 49)]),
    (U + "GradedModelSpansCotOfRigidWeights", [(205, 244)]),
    (BASE + "GeneratorCountTuples.LemmaK", [(13, 17)]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads(
        (ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["commit"] == REV
    blobs = {r[0]: r[1] for r in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        data = (ROOT / "build/source-cache/jsmorph/rh" / REV / rel).read_bytes()
        blob = hashlib.sha1(
            b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == blobs[module], module
        lines = data.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpts.append({
                "lines": [lo, hi],
                "sha256": sha(b"\n".join(lines[lo-1:hi]) + b"\n"),
            })
        records.append({
            "repository": "jsmorph/rh", "commit": REV, "path": rel,
            "sha256": sha(data), "git_blob_sha1": blob, "excerpts": excerpts,
        })
    return records


def dependency_record():
    rel = "certificates/qualitative-selmer-finiteness.json"
    data = (ROOT / rel).read_bytes()
    record = json.loads(data)
    assert record["result"] == "PASS"
    assert sha((ROOT / record["note"]).read_bytes()) == record["note_sha256"]
    assert sha((ROOT / record["checker"]).read_bytes()) == record["checker_sha256"]
    for reference in record["primary_sources"]:
        assert sha((ROOT / reference["path"]).read_bytes()) == reference["sha256"]
    return {
        "path": rel, "sha256": sha(data),
        "scope": "Prior strict-Selmer theorem, note/checker hashes and all three primary PDF hashes authenticated; no new proof of the classical inputs.",
    }


def primary_record():
    rel = "build/reference-cache/bloch-kato-tamagawa.pdf"
    data = (ROOT / rel).read_bytes()
    expected = "ec89c6436c7e16580791eddd562c8c04a12442d8a8484f8ac75c5ea8dc04f5e5"
    assert sha(data) == expected
    doc = fitz.open(stream=data, filetype="pdf")
    assert len(doc) == 68
    pages = []
    for page, marker, scope in [
        (23, "3.8.4", "Printed p.355: local finite-cohomology dimension formula"),
        (27, "3.9", "Printed p.359: all negative Tate twists vanish; weight zero is unramified"),
    ]:
        text = doc[page-1].get_text()
        assert marker in text
        pages.append({
            "pdf_page": page, "scope": scope,
            "extracted_page_text_sha256": sha(text.encode()),
            "visually_inspected": True,
        })
    return {
        "title": "Bloch and Kato, L-functions and Tamagawa numbers of motives",
        "publication": "The Grothendieck Festschrift, Vol. I (1990), pp.333-400",
        "url": "https://math.stanford.edu/~conrad/BSDseminar/refs/BKTamagawa.pdf",
        "path": rel, "sha256": expected, "bytes": len(data),
        "page_count": len(doc), "inspected_pages": pages,
    }


def coefficient_field_reference():
    rel = "build/reference-cache/milne-ant-2020.pdf"
    data = (ROOT / rel).read_bytes()
    expected = "24b83c789a89f25aebffb3cbe4ae5ca29edd0075acc072de093d140770630847"
    assert sha(data) == expected
    doc = fitz.open(stream=data, filetype="pdf")
    assert len(doc) == 166
    text = doc[134].get_text()
    assert "7.64" in text and "7.65" in text
    return {
        "title": "Milne, Algebraic Number Theory, version 3.08 (2020)",
        "url": "https://www.jmilne.org/math/CourseNotes/ANT.pdf",
        "path": rel, "sha256": expected, "pdf_page": 135,
        "printed_page": 133,
        "scope": "Proposition 7.64 and Remark 7.65: finitely many extensions of a given degree up to isomorphism, hence countably many embedded finite coefficient fields.",
        "extracted_page_text_sha256": sha(text.encode()),
        "inspection": "Bounded text of the exact proposition and remark.",
    }


def valuation(x, prime):
    x = Fraction(x)
    if not x:
        return float("inf")
    numerator, denominator = abs(x.numerator), x.denominator
    out = 0
    while numerator % prime == 0:
        numerator //= prime
        out += 1
    while denominator % prime == 0:
        denominator //= prime
        out -= 1
    return out


def check_common_denominator():
    cases = 0
    for prime, r, shift, q, theta, residue in itertools.product(
            (2, 3, 5, 7), range(4), range(4), range(-2, 3),
            (1, 2, 3, 5), (-1, 0, 1)):
        if theta % prime == 0:
            continue
        d = prime**r
        t = Fraction(q, d)
        error = Fraction(residue, prime+1)
        value = prime**shift * ((theta-1)*t + error)
        assert valuation(d*t, prime) >= 0
        assert valuation(value/prime**shift - (theta-1)*t, prime) >= 0
        assert valuation(d*value, prime) >= shift
        cases += 1
    # Without d*t integral, the asserted common-denominator implication fails.
    assert valuation(3 * Fraction(1, 9), 3) == -1
    return {
        "exact_rational_valuation_cases": cases,
        "excluded_normalization_control": {
            "prime": 3, "d": 3, "t": "1/9", "v_3(d*t)": -1,
        },
        "scope": "Finite rational instances of the DVR implication only; the arbitrary finite field and limiting intersection are proved in the note.",
    }


def zero():
    return [[Fraction(0) for _ in range(3)] for _ in range(3)]


def add(a, b):
    return [[a[i][j]+b[i][j] for j in range(3)] for i in range(3)]


def scale(c, a):
    return [[c*a[i][j] for j in range(3)] for i in range(3)]


def sub(a, b):
    return add(a, scale(-1, b))


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]


def reflect(a):
    return [[a[2-j][2-i] for j in range(3)] for i in range(3)]


def basis(i, j):
    a = zero()
    a[i][j] = Fraction(1)
    return a


def diagonal(p):
    p = Fraction(p)
    return [[(p, Fraction(1), 1/p)[i] if i == j else Fraction(0)
             for j in range(3)] for i in range(3)]


def action(a, p, eta):
    middle = a if eta == 1 else scale(-1, reflect(a))
    return mm(mm(diagonal(p), middle), diagonal(1/Fraction(p)))


def check_adjoint_and_marking():
    weights = (1, 0, -1)
    dimensions = {}
    for j in range(-2, 3):
        entries = [(a, b) for a in range(3) for b in range(3)
                   if weights[a]-weights[b] == j]
        fixed = sum((a, b) == (2-b, 2-a) for a, b in entries)
        dimensions[j] = {"minus": (len(entries)-fixed)//2,
                         "plus": (len(entries)+fixed)//2}
    assert dimensions[-2] == {"minus": 0, "plus": 1}
    assert dimensions[-1] == {"minus": 1, "plus": 1}
    assert dimensions[0] == {"minus": 1, "plus": 2}
    vectors = [
        (-1, -1, sub(basis(1, 0), basis(2, 1))),
        (-1, 1, add(basis(1, 0), basis(2, 1))),
        (-2, 1, basis(2, 0)),
    ]
    scalar_cases = 0
    p_values = tuple(map(Fraction, (-3, -2, 2, 3))) + (
        Fraction(1, 2), Fraction(2, 3))
    for p, eta, (j, sign, vector) in itertools.product(p_values, (-1, 1), vectors):
        assert reflect(reflect(vector)) == vector
        assert reflect(vector) == scale(sign, vector)
        character = p**j * (eta if sign == 1 else 1)
        assert action(vector, p, eta) == scale(character, vector)
        scalar_cases += 1
    torus = [[Fraction(1), 0, 0], [0, 0, 0], [0, 0, Fraction(-1)]]
    marking_cases = 0
    for p, a, b, d in itertools.product(p_values, range(-2, 3),
                                       range(-2, 3), range(-2, 3)):
        x = [[Fraction(a), Fraction(b), 0],
             [Fraction(d), 0, Fraction(-b)],
             [0, Fraction(-d), Fraction(-a)]]
        assert reflect(x) == scale(-1, x)
        gamma = sub(x, action(x, p, 1))
        gamma_star = sub(x, action(x, 1/p, 1))
        z = sub(mm(gamma, diagonal(p)), mm(gamma_star, diagonal(1/p)))
        commutator = sub(mm(x, torus), mm(torus, x))
        assert z == scale(p-1/p, commutator)
        assert z[0][1] == -(p-1/p)*b
        assert z[1][0] == (p-1/p)*d
        normalized = (z[0][1] == 0 and z[1][0] == 0)
        assert normalized == (b == 0 and d == 0)
        if normalized:
            for eta in (-1, 1):
                assert action(x, p, eta) == x
        marking_cases += 1
    # A nonzero coboundary survives these two marked equations if p^2=1.
    x = sub(basis(0, 1), basis(1, 2))
    assert sub(x, action(x, 2, 1)) != zero()
    for p in (Fraction(1), Fraction(-1)):
        gamma = sub(x, action(x, p, 1))
        gamma_star = sub(x, action(x, 1/p, 1))
        z = sub(mm(gamma, diagonal(p)), mm(gamma_star, diagonal(1/p)))
        assert z[0][1] == z[1][0] == 0
    return {
        "involution_dimensions_by_weight": dimensions,
        "exact_negative_character_cases": scalar_cases,
        "exact_marking_cases": marking_cases,
        "separation_controls": ["p=1", "p=-1"],
        "scope": "Exact rational matrix identities, all three actual negative summands, and necessity of the separating marked coefficient.",
    }


def main():
    sources = source_records()
    checks = {
        "common_denominator": check_common_denominator(),
        "adjoint_and_marking": check_adjoint_and_marking(),
    }
    artifacts = [
        "notes/rh-selmer-negative-weight-rigidity.md",
        "scripts/check_rh_selmer_negative_weight_rigidity.py",
    ]
    record = {
        "status": "pass", "date": "2026-11-22",
        "theorem": "Negative-weight rational finite-Selmer vanishing from qualitative strict torsion finiteness, with the actual adjoint decomposition and framed base-normalization lemma.",
        "scope": [
            "The ordinary proof includes Baire coefficient descent and finite period-witness enlargement.",
            "Only the existence of an exponent killing one fixed strict torsion group is used; no quantitative cohomology or K-group bound is assumed.",
            "All finite-order twists are included, even of ell-divisible order; m=1 and ell=2 are included.",
            "Base-point coboundaries become zero normalized cocycles by the exact marked matrix calculation.",
            "The actual model's derivation lifting, local finite condition and tangent determination remain hypotheses.",
            "The source graded-model implication separately assumes ell is odd; that model restriction is retained.",
            "No integral torsion estimate, non-diagonal two-sided rigidity, full RH/GRH node, or Lean build is claimed.",
        ],
        "sources": sources,
        "prior_finiteness_dependency": dependency_record(),
        "primary_reference": primary_record(),
        "coefficient_field_reference": coefficient_field_reference(),
        "exact_checks": checks,
        "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())}
                      for p in artifacts],
        "independent_review_record": "certificates/frontier-progress-review-2026-11-22.json",
        "review_scope": "Automation-only verification here; mathematical review is recorded separately.",
    }
    path = ROOT / "certificates/rh-selmer-negative-weight-rigidity.json"
    path.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({
        "status": "pass", "sources": len(sources),
        "bounded_excerpts": sum(len(s["excerpts"]) for s in sources),
        "exact_checks": checks, "certificate": str(path.relative_to(ROOT)),
    }, indent=2))


if __name__ == "__main__":
    main()
