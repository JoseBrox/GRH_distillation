#!/usr/bin/env python3
"""Verify provenance and exact boundary algebra for the local Selmer comparison.

This is not a Lean build or a numerical proof of p-adic Hodge theory.
Kisin's theorem, local duality, and the ordinary field-flag comparison
remain the explicitly cited inputs to the proof in the accompanying note.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import urllib.request

import fitz
import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
SOURCES = [
    ("PadicHodgeTheory.IsInertiaInfiniteCyclotomic", [(11, 45), (72, 151)]),
    ("ModularityArgument.CrystallineOrdinaryIdeals.TriangularConjOfOrdIdealEqBot", [(100, 129)]),
    ("ModularityArgument.CrystallineOrdinaryIdeals.ChosenFrobeniusIsFrobenius", [(70, 83)]),
    ("PadicHodgeTheory.RtDual", [(137, 196)]),
    ("PadicHodgeTheory.DualCr", [(30, 62)]),
    ("PadicHodgeTheory.BkAbove", [(5, 79)]),
    ("UnitaryThreeGroups.TanCocIsBK", [(187, 222)]),
    ("PublishedTheorems.KisinCrTrivial", [(9, 28)]),
    ("ModularityArgument.CrystallineOrdinaryIdeals.IsLCrystallinePointOfSaturatedOrdIdeal", [(15, 57)]),
]

REFERENCES = [
    {
        "name": "Kisin, Potentially semi-stable deformation rings, author DVI",
        "url": "https://people.math.harvard.edu/~kisin/dvifiles/def.dvi",
        "file": "kisin-potentially-semistable.dvi",
        "sha256": "ca85f74a47caf411dfb7fe0fa356ef30928d5dbd2cd518bafcc13943cf483dee",
        "locator": "Section 2.1, printed p.10; setup (2.7.5) and Corollary (2.7.7), printed p.23",
        "text_ranges": [(582, 591), (1376, 1415)],
        "anchors": ["(2.7.5)", "Corollary  (2.7.7)", "any  finite  E-", "potentially crystalline"],
        "role": "Complete coefficient ring, torsion-free setup, and universal crystalline quotient on every finite E-algebra.",
    },
    {
        "name": "Kisin, The structure of potentially semi-stable deformation rings",
        "url": "https://people.math.harvard.edu/~kisin/dvifiles/licm.pdf",
        "file": "kisin-deformation-survey.pdf",
        "sha256": "c69ede9dada816b3adfa72fa61a0b14d8a4dc171bbeef26e716493360730ff23",
        "locator": "Theorem 1.2.2 and following paragraph, printed/PDF p.7",
        "pages": [7],
        "anchors": ["Theorem 1.2.2.", "local E-algebra B", "rather than just a ﬁnite ﬁeld"],
        "role": "Independent author confirmation that finite local algebras, not only fields, occur in the theorem.",
    },
    {
        "name": "Conrad, notes by Lichtenstein, Generic fibers of deformation rings",
        "url": "https://math.stanford.edu/~conrad/modseminar/pdf/L04.pdf",
        "file": "conrad-generic-fibers.pdf",
        "sha256": "62fc1fb97b1bfa9325fb976c902d990d2dc047484b7f82f489b71ec58a0c5182",
        "locator": "Claim and its proof, printed/PDF pp.2-3",
        "pages": [2, 3],
        "anchors": ["R[1/π]", "Jacobson", "ﬁnite over the fraction ﬁeld"],
        "role": "Jacobson algebraic generic fibre; finite closed residue fields; automatic locality of field points.",
    },
    {
        "name": "Bloch and Kato, L-functions and Tamagawa numbers of motives",
        "url": "https://math.stanford.edu/~conrad/BSDseminar/refs/BKTamagawa.pdf",
        "file": "bloch-kato-tamagawa.pdf",
        "sha256": "ec89c6436c7e16580791eddd562c8c04a12442d8a8484f8ac75c5ea8dc04f5e5",
        "locator": "Corollary 3.8.4, printed p.355/PDF p.23; Example 3.9, printed p.359/PDF p.27",
        "pages": [23, 27],
        "anchors": ["Corollary 3.8.4", "Example 3.9.", "unramified"],
        "role": "Finite cohomology dimension and zero/first-twist boundary cases.",
    },
    {
        "name": "Feng, The Bloch-Kato Selmer Group",
        "url": "https://math.stanford.edu/~conrad/BSDseminar/Notes/L14.pdf",
        "file": "feng-bloch-kato-selmer.pdf",
        "sha256": "7d9eb97fe707cef3844cc02b9b95114d2f1b98efd388a6ac485bf4b3ca90c727",
        "locator": "Theorem 2.1, printed/PDF pp.4-5; Remark 4.8 and Proposition 4.10, p.12",
        "pages": [4, 5, 12],
        "anchors": ["Theorem 2.1.", "Euler characteristic formula", "−[K : Qp]", "Remark 4.8.", "Proposition 4.10."],
        "role": "Local Tate duality, correct Euler-characteristic sign, and crystalline extension interpretation.",
    },
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["commit"] == REV
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for suffix, ranges in SOURCES:
        module = PREFIX + suffix
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        record = inspect_file({"repository": "jsmorph/rh", "commit": REV,
                               "path": rel, "git_blob_sha1": blobs[module]}, offline)
        data = (ROOT / "build/source-cache/jsmorph/rh" / REV / rel).read_bytes()
        lines = data.splitlines()
        record = {k: record[k] for k in ["repository", "commit", "path", "bytes",
                                       "git_blob_sha1", "sha256", "matches_pinned_blob"]}
        record["excerpts"] = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            record["excerpts"].append({"lines": [lo, hi],
                "sha256": sha(b"\n".join(lines[lo-1:hi]) + b"\n")})
        records.append(record)
    return records


def reference_records(offline):
    cache = ROOT / "build/reference-cache"
    cache.mkdir(parents=True, exist_ok=True)
    records = []
    for spec in REFERENCES:
        path = cache / spec["file"]
        if not path.exists():
            if offline:
                raise FileNotFoundError(path)
            request = urllib.request.Request(spec["url"], headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(request, timeout=45) as response:
                data = response.read()
            assert sha(data) == spec["sha256"], spec["name"]
            path.write_bytes(data)
        data = path.read_bytes()
        assert sha(data) == spec["sha256"], spec["name"]
        record = {k: spec[k] for k in ["name", "url", "sha256", "locator", "role"]}
        record["bytes"] = len(data)
        excerpts = []
        if path.suffix == ".dvi":
            extracted = subprocess.check_output(["dvi2tty", "-w", "120", str(path)], text=True)
            lines = extracted.split("\n")
            for lo, hi in spec["text_ranges"]:
                text = "\n".join(lines[lo-1:hi])+"\n"
                excerpts.append({"dvi2tty_lines": [lo, hi], "sha256": sha(text.encode())})
        else:
            doc = fitz.open(path)
            texts = [doc[page-1].get_text() for page in spec["pages"]]
            extracted = "\n".join(texts)
            for page, text in zip(spec["pages"], texts):
                excerpts.append({"pdf_page": page, "sha256": sha(text.encode())})
        assert all(anchor in extracted for anchor in spec["anchors"]), spec["name"]
        record["excerpts"] = excerpts
        record["anchor_checks"] = "pass"
        records.append(record)
    return records


def exact_algebra():
    # Boundary e=1: inertia kills the first dual coordinate.  The second
    # is killed by the adjacent Frobenius nonresonance factor q-c.
    u, q, c, a, b, x = sp.symbols("u q c a b x")
    lam = sp.Matrix([[a, b]])
    inertia = sp.diag(u**2, u)
    frobenius = sp.Matrix([[x, sp.Symbol("z")], [0, q]])
    ei = lam*inertia-u*lam
    ef = lam*frobenius-c*lam
    assert sp.expand(ei[0]) == a*u**2-a*u
    assert ei[1] == 0
    assert sp.simplify(ef[1].subs(a, 0)-(q-c)*b) == 0
    assert sp.simplify(ef[1].subs({a: 0, q: c})) == 0

    # The density failure without saturation is visible componentwise.
    s, x, y, t = sp.symbols("s x y t")
    g = sp.groebner([x*y, 1-s*x], s, x, y, order="lex")
    elimination = [p.as_expr() for p in g.polys if not p.as_expr().has(s)]
    assert elimination == [y]
    assert sp.groebner([x*y], x, y).reduce(y)[1] == y
    assert (x*y).subs({x: 0, y: 1}) == 0
    assert y.subs({x: 0, y: 1}) == 1

    # Field-valued points kill t in E[t]/(t²), but its dual-number point
    # has a nonzero t-coordinate; the computations certify the algebra.
    gdual = sp.groebner([t**2], t)
    assert gdual.reduce(t**2)[1] == 0
    assert gdual.reduce(t)[1] == t
    return {
        "dual_invariants": "At e=1, inertia gives (u²-u)a=0; after a=0, Frobenius gives (q-c)b=0 independently of the extension entry. The proof treats e>=2 by differing inertia exponents.",
        "saturation": "Elimination computes (xy):x^infinity=(y). Without saturation, y is nonzero on the missed component x=0.",
        "nonreduced_boundary": "The class of t in E[t]/(t²) is nonzero while its square is zero; field points cannot detect this class.",
        "scope": "Exact symbolic identities and counterexample algebra; no computation substitutes for the cited p-adic theorems or the general density proof.",
    }


def ordinary_matrix_identities():
    p = sp.symbols("p0:3")
    a = sp.symbols("a0:3")
    entries = sp.symbols("m0:9")
    A = sp.Matrix(3, 3, entries)
    eye = sp.eye(3)
    D = sp.diag(*p)
    Di = [D-pi*eye for pi in p]
    ci = [sp.prod(p[i]-p[j] for j in range(3) if i != j) for i in range(3)]
    projections = [sp.diag(*[int(j == i) for j in range(3)]) for i in range(3)]
    for i in range(3):
        assert sp.simplify(Di[(i+1) % 3]*Di[(i+2) % 3]-ci[i]*projections[i]) == sp.zeros(3)
    slots = [(A-a[0]*eye)*Di[1]*Di[2],
             Di[0]*(A-a[1]*eye)*Di[2],
             Di[0]*Di[1]*(A-a[2]*eye)]
    assert sp.simplify(slots[0]-ci[0]*(A-a[0]*eye)*projections[0]) == sp.zeros(3)
    assert sp.simplify(slots[2]-ci[2]*projections[2]*(A-a[2]*eye)) == sp.zeros(3)
    assert sp.simplify(slots[1][1, 1]-ci[1]*(A[1, 1]-a[1])) == 0

    k = sp.symbols("k0:3", nonzero=True)
    z01, z02, z12, cycl = sp.symbols("z01 z02 z12 cycl")
    sigma = sp.Matrix([[k[0], z01, z02], [0, k[1], z12], [0, 0, k[2]]])
    traces = [sp.trace(Di[(i+1) % 3]*Di[(i+2) % 3]*sigma) for i in range(3)]
    for i in range(3):
        assert sp.expand(traces[i]-ci[i]*k[i]) == 0
    for i in [0, 1]:
        dd = ci[i+1]*traces[i]-cycl*ci[i]*traces[i+1]
        assert sp.simplify(dd-ci[i]*ci[i+1]*k[i+1]*(k[i]/k[i+1]-cycl)) == 0

    # Each missing slot permits its diagonal character to change when the
    # other two slots and the one distinguished characteristic polynomial
    # are retained.  These are algebraic controls, not group examples.
    controls = []
    for omitted in range(3):
        values = dict(zip(p, [1, 2, 4])) | dict(zip(a, [3, 5, 7]))
        test = sp.diag(3, 5, 7)
        test[omitted, omitted] += 1
        values |= dict(zip(entries, list(test)))
        evaluated = [slot.subs(values) for slot in slots]
        assert evaluated[omitted] != sp.zeros(3)
        assert all(evaluated[i] == sp.zeros(3) for i in range(3) if i != omitted)
        controls.append({"omitted_slot": omitted, "matrix": str(test),
                         "other_two_slots": "zero", "omitted_slot_value": "nonzero"})

    # Conversely, three correctly ordered triangular factors annihilate
    # the flag successively; this is an identity without commutativity of
    # those matrices.
    factors = []
    for i in range(3):
        diag = sp.symbols(" ".join(f"b{i}{j}" for j in range(3)))
        x, y, z = sp.symbols(f"x{i} y{i} z{i}")
        M = sp.Matrix([[diag[0], x, y], [0, diag[1], z], [0, 0, diag[2]]])
        factors.append(M-diag[i]*eye)
    assert factors[0]*factors[1]*factors[2] == sp.zeros(3)
    return {
        "spectral_projectors": "D_(i+1) D_(i+2)=c_i P_i, with c_i=product_(j!=i)(p_i-p_j).",
        "slots": "(s,t,t) fixes column0; (t,t,s) fixes row2; (t,s,t) fixes the middle diagonal. Together they force exactly the required triangular diagonal data.",
        "trace_factors": "T_i=c_i*kappa_i(sigma); d_i=c_i*c_(i+1)*kappa_(i+1)(sigma)*(kappa_i/kappa_(i+1)(sigma)-chi(sigma)).",
        "converse_product_identity": "The three ordered triangular factors have zero product by exact symbolic multiplication.",
        "omitted_slot_controls": controls,
        "scope": "Exact matrix identities supporting the field-flag proof; normality and uniqueness of the invariant line/plane are proved in the note.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    artifacts = [
        "notes/selmer-crystalline-component-comparison.md",
        "paper/shared/selmer-crystalline-component-comparison.tex",
        "paper/shared/selmer-crystalline-component-references.tex",
        "scripts/check_selmer_crystalline_component_comparison.py",
    ]
    certificate = {
        "status": "pass", "date": "2026-11-22",
        "result": "The actual coefficient-prime tangent condition follows from the displayed ordinary matrix equations, an elementary spectral-projector flag calculation, the reduced saturated locus, and Kisin's full finite-algebra theorem.",
        "artifacts": [{"path": path, "sha256": sha((ROOT/path).read_bytes())} for path in artifacts],
        "pinned_sources": source_records(args.offline),
        "primary_references": reference_records(args.offline),
        "exact_algebra": exact_algebra(),
        "ordinary_matrix_identities": ordinary_matrix_identities(),
        "proved_implications": [
            "Saturation makes delta regular and hence excludes delta from every minimal prime; the nonresonant open is dense on every surviving component.",
            "Fixed-type crystalline field points on that open force Kisin's ideal into the radical saturated ideal on the Jacobson generic fibre.",
            "The ideal inclusion supplies all finite coefficient-algebra points, including dual numbers at points where delta vanishes.",
            "The ordinary rank-three field flag is crystalline by two applications of local Tate duality and the Bloch-Kato dimension formula; the e=1 nonresonance conditions remove both possible cyclotomic quotients.",
            "The ordinary matrix equations themselves give the unique invariant field flag and exact nonresonance factors by three substitutions and spectral projectors; no additional field-flag supplier is needed.",
            "For e>=2, nonresonance follows from inertia and the local finite-condition proof applies directly to the reduced unsaturated ordinary locus.",
            "Crystalline dual-number self-extensions give finite tangent cocycles; finite-index averaging descends the condition to the actual local group.",
        ],
        "retained_inputs": [
            "A continuous actual local representation over the specified complete Noetherian coefficient ring, with the fixed residual representation and fixed parallel Hodge type.",
            "Identification of the actual local ring with the displayed ordinary equations, saturation, and a quotient containing the radical saturated ideal.",
            "The global arithmetic model's maps to the local component quotient and finite inertia quotients.",
            "Kisin's crystalline-deformation theorem for every finite E-algebra, local Tate duality/Euler characteristic, and Bloch-Kato's finite dimension formula.",
            "The other W04 frontiers: actual arithmetic models, non-diagonal global rigidity and uniform integral Selmer estimates.",
        ],
        "limits": [
            "No Lean compilation or kernel check.",
            "No proof of the stronger nonreduced saturated-ordinary-locus statement; it is unnecessary for this tangent supplier.",
            "No uniform field-degree, denominator or integral Selmer bound.",
            "No new completed RH or GRH node.",
        ],
    }
    path = ROOT / "certificates/selmer-crystalline-component-comparison.json"
    path.write_text(json.dumps(certificate, indent=2)+"\n")
    print(json.dumps({"status": "pass", "pinned_sources": len(certificate["pinned_sources"]),
                      "primary_references": len(certificate["primary_references"]),
                      "exact_boundary_algebra": "pass", "certificate": str(path.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
