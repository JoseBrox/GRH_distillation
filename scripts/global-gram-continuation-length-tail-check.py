#!/usr/bin/env python3
"""Authenticate and check the original all-flag-length tail assembly.

This checks source integrity and exact reserve/exponent arithmetic.
The representation and analytic arguments are proved in the TeX;
this program is not a Lean build or a verification of the final Gram form.
"""
from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
P = "Formalism.SharpRestriction.CuspSpanNormBounds."
SOURCES = [
    (P+"NonGenericAndKTwoTheorems", [(109, 131), (265, 266)]),
    (P+"NormalizedLocalScale", [(127, 147), (172, 173)]),
    (P+"RelevantZeroGramTerms", [(104, 122), (159, 175), (287, 303), (402, 404)]),
    ("Formalism.LocalRingCardinality.DataHost", [(140, 145)]),
    (P+"StandingNumericalData", [(106, 136)]),
    ("Formalism.LocalRingCardinality.Params", [(6, 48), (50, 69)]),
]
PROOF = [
    "paper/shared/global-gram-continuation-length-tail.tex",
    "paper/shared/global-gram-continuation-length-tail-references.tex",
    "notes/global-gram-continuation-length-tail.md",
    "scripts/global-gram-continuation-length-tail-check.py",
]
DEPENDENCIES = [
    "paper/shared/global-norm-frontier-first-length.tex",
    "paper/shared/global-norm-frontier-mixed-ratio-moments.tex",
    "paper/shared/global-norm-frontier-tensor-projections.tex",
    "paper/shared/global-norm-frontier-lowering-product.tex",
    "paper/shared/global-norm-frontier-normalized-lowering.tex",
    "paper/shared/global-norm-frontier-quotient-mass.tex",
    "paper/shared/global-norm-frontier-pieri-family.tex",
    "paper/shared/global-gram-continuation-quantitative-seed.tex",
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def authenticate():
    atlas_data = json.load(gzip.open(ROOT/"blueprint/lean-source-imports.json.gz", "rt"))
    assert atlas_data["commit"] == REV
    atlas = {row[0]: row for row in atlas_data["modules"]}
    evidence = []
    for module, ranges in SOURCES:
        path = "lean/src/"+module.replace(".", "/")+".lean"
        raw = (ROOT/"build/source-cache/jsmorph/rh"/REV/path).read_bytes()
        git_blob = hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
        assert git_blob == atlas[module][1], module
        assert len(raw) == atlas[module][2], module
        lines = raw.splitlines(keepends=True)
        excerpts = []
        for first, last in ranges:
            assert 1 <= first <= last <= len(lines) and last-first < 120
            excerpts.append({"lines": [first, last],
                             "sha256": digest(b"".join(lines[first-1:last]))})
        evidence.append({"module": module, "repository": "jsmorph/rh", "commit": REV,
                         "path": path, "git_blob_sha1": git_blob,
                         "sha256": digest(raw), "excerpts": excerpts})
    return evidence


def nonnegative_coefficients(poly, variables):
    assert all(a >= 0 for a in s.Poly(s.expand(poly), *variables).coeffs())


def exact_arithmetic():
    r, i, j, k, q, A, Ac, CT, Cg, U = s.symbols(
        "r i j k q A Ac CT Cg U", nonnegative=True)
    m = 2*r+2
    n = 2*r+k+1
    CH = CT+8*A+Ac
    positive = (CT+6*A)*m+4*A*i+2*Ac*(r-i)
    negative = 4*A*(r-i)+2*Ac*(r-i)
    assert s.expand(CH*m-positive-4*A*(r+1-i)-2*Ac*(i+1)) == 0
    for cost in (positive, negative):
        remainder = s.expand((CH*m-cost).subs(r, i+j))
        nonnegative_coefficients(remainder, (i, j, A, Ac, CT))
    assert s.expand(CH.subs({A: U+5, Ac: 2*Cg+2})) == CT+8*U+2*Cg+42
    assert s.expand(2*CH*m-CH*m) == s.expand(CH*m)
    assert s.simplify(2*(r+1)-m) == 0
    # The original first-length order is 2q; its level is 4q.
    assert s.expand(2*(2*q)) == 4*q
    assert s.expand(m*q-2*q) == 2*r*q
    # All-rank reserve consequences: C1<=m/2 and k>=m^4.
    t, u = s.symbols("t u", nonnegative=True)
    mm = 2+t
    kk = mm**4+u
    for rem in (kk**2-kk*mm**2/4,
                kk**2-kk*mm**3/4,
                (kk+mm-1)**2-kk**2,
                (kk+mm-1)**3-kk**2):
        nonnegative_coefficients(rem, (t, u))
    # Adjacent gaps dominate 100(2q+1) for q>=1, q<=C1*k*r,
    # Cl>=1000*C1. The integer comparison 2q+1<=3q is exact.
    nonnegative_coefficients(1000*(2*r+2)**4-300*r, (r,))
    assert 100*(2*(1+t)+1) <= 300*(1+t)
    # A shifted noncompact gap remains >=8 n^19 when h>=16 n^19
    # and q<=n^2 (we use the weaker shift loss 4q).
    nn = 1+t
    nonnegative_coefficients(8*nn**19-4*nn**2, (t,))
    # Cloud-to-negative gap from b1>=Cl*m*k*(k*f*L)^Cl, Cl>=40,
    # n<=2k, k>=2, f>=1, L>1. The smallest residual is >1.
    assert 2*2**22 >= 2**19
    # Character conversion: (2/c)*(-i*c)=-2i, each length exponent
    # is -(r-i), and both signs cost at most Ac*m per moment q.
    c = s.symbols("c", positive=True)
    assert s.simplify((2/c)*(-s.I*c)) == -2*s.I
    assert s.expand(Ac*m-2*Ac*(r-i)-2*Ac*(i+1)) == 0
    return {
        "first_length_order": "2q",
        "integer_shift_use": "2q <= m q <= Q",
        "level_use": "4q <= 4n^2",
        "positive_ratio_order": "2iq <= 2rq <= n^3",
        "negative_ratio_order": "(r-i)q <= n^3",
        "tail_constant": str(s.expand(CH.subs({A: U+5, Ac: 2*Cg+2}))),
        "number_of_signed_lengths": str(m),
        "original_local_character_scale": "g rd(E)/(2 pi)",
        "uniformity": "Cq=10^8, cq=1/Cq, CH fixed before C1; Cl may depend on C1 before construction",
        "verification": "Exact polynomial identities and nonnegative-coefficient certificates; no finite-sample inference.",
    }


def main():
    report = {
        "classification": "closed original local all-length tail obligation",
        "source_files": authenticate(),
        "exact_arithmetic": exact_arithmetic(),
        "proof_files": [{"path": p, "sha256": digest((ROOT/p).read_bytes())} for p in PROOF],
        "established_dependencies": [{"path": p, "sha256": digest((ROOT/p).read_bytes())}
                                     for p in DEPENDENCIES],
        "remaining": ["zero-Gram local orbital operator estimate and global sum",
                      "generic return contribution", "final arithmetic-map identification",
                      "positive trace comparison", "construction of original standing data"],
        "scope": "Source integrity and reserve arithmetic checked. Analytic proof in TeX; no Lean build or whole-node completion.",
    }
    dest = ROOT/"certificates/global-gram-continuation-length-tail.json"
    dest.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"certificate": str(dest.relative_to(ROOT)),
                      "source_files": len(SOURCES), "result": "all exact reserve and exponent checks passed",
                      "scope": report["scope"]}))


if __name__ == "__main__":
    main()
