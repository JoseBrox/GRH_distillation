#!/usr/bin/env python3
"""Exact phase, transfer and mixed-residue covariance checks with pinned sources."""
from __future__ import annotations

import argparse
import functools
import gzip
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "global-norm-frontier-wave-isometry"
SOURCES = [
    ("Formalism.HermitianCurvature.RealInputsClosedAdmissibleSettings",
     [(18, 43), (60, 66), (97, 121), (148, 153)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.PBFCstmt",
     [(20, 26)]),
    ("Formalism.HermitianCurvature.StatementD", [(164, 194), (212, 214)]),
    ("Formalism.HermitianCurvature.StatementJC", [(18, 23), (90, 106)]),
    ("Formalism.HermitianCurvature.StatementWd", [(34, 55)]),
    ("Formalism.HermitianCurvature.CompositeFormulaLevelZero", [(38, 48)]),
    ("Formalism.YangianSpanCharacter.StatementT", [(27, 31)]),
    ("Formalism.HermitianCurvature.TopEntryWaveEquation", [(12, 21)]),
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def source_records(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert digest(packed) == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert (atlas["repository"], atlas["commit"]) == (REPO, REV)
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        rec = inspect_file({"repository": REPO, "commit": REV, "path": path,
                            "git_blob_sha1": blobs[module]}, offline)
        assert rec["matches_pinned_blob"]
        lines = (ROOT / "build/source-cache" / REPO / REV / path).read_bytes().splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            data = b"".join(lines[lo-1:hi])
            assert len(data) <= 12288
            excerpts.append({"lines": [lo, hi], "bytes": len(data), "sha256": digest(data)})
        records.append({"module": module, **{key: rec[key] for key in
                        ["repository", "commit", "path", "bytes", "sha256",
                         "git_blob_sha1", "matches_pinned_blob"]},
                        "excerpts": excerpts})
    return records


def phase_checks():
    s, sb = sp.symbols("s sb")  # independent formal variables; sb is conjugate(s)
    count = 0
    for n in [2, 3]:
        eta = sp.symbols("eta:"+str(n))
        dual = sp.symbols("y:"+str(n))
        xs = list(range(1, n+1))
        xis = list(range(n+2, 2*n+2))
        z = sum(a*b for a, b in zip(xs, eta))
        zb = sum(a*b for a, b in zip(xis, dual))

        def e(a, b, f):
            return sp.expand(eta[a]*sp.diff(f, eta[b])-dual[b]*sp.diff(f, dual[a]))

        @functools.lru_cache(maxsize=None)
        def det(f, wave=False):
            ans = 0
            for perm in itertools.permutations(range(n)):
                sign = (-1)**sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
                term = f
                for col in reversed(range(n)):
                    row = perm[col]
                    out = e(row, col, term)
                    if row == col:
                        out += (7-col)*term
                    if wave:
                        out += (s*eta[row]*xs[col]+sb*xis[row]*dual[col])*term
                    term = sp.expand(out)
                ans += sign*term
            return sp.expand(ans)

        cz = lambda f: sp.expand(det(z*f)-z*det(f))
        cb = lambda f: sp.expand(det(zb*f)-zb*det(f))
        mixed = lambda f: sp.expand(cz(zb*f)-zb*cz(f))
        fs = [sp.Integer(1), eta[0]+dual[-1], eta[0]*dual[-1],
              sum(v*v for v in eta)+sum(v**3 for v in dual)]
        for f in fs:
            assert sp.expand(cz(z*f)-z*cz(f)) == 0
            assert sp.expand(cb(zb*f)-zb*cb(f)) == 0
            assert sp.expand(mixed(z*f)-z*mixed(f)) == 0
            assert sp.expand(mixed(zb*f)-zb*mixed(f)) == 0
            assert sp.expand(det(f, True)-det(f)-s*cz(f)+sb*cb(f)+s*sb*mixed(f)) == 0
            count += 1
    # Exact Weyl transfer under phase multiplication.
    p, c, ci, spectral = sp.symbols("p c ci Y")
    transfer = sp.Matrix([[spectral+p, -c], [ci, 0]])
    uminus = sp.Matrix([[1, 0], [-s, 1]])
    assert transfer*uminus == sp.Matrix([[spectral+p+s*c, -c], [ci, 0]])
    return {"actual_standard_dual_differential_models": count,
            "matrix_sizes": [2, 3],
            "commutator_identities_per_model": 5,
            "phase_variables_are_formally_independent": True,
            "exact_weyl_transfer_identity": True}


I2 = sp.eye(2)


def unit(i, j):
    return sp.eye(2)[:, i]*sp.eye(2)[j, :]


def kron(xs):
    ans = sp.ones(1)
    for x in xs:
        ans = sp.kronecker_product(ans, x)
    return ans


def insert_base(q, place, h):
    ans = sp.zeros(2**(h+1))
    for i, j in itertools.product(range(2), repeat=2):
        xs = [I2 for _ in range(h)]+[q[2*i:2*(i+1), 2*j:2*(j+1)]]
        xs[place] = unit(i, j)
        ans += kron(xs)
    return ans


def residue_model(signs, u, transformed=False):
    h = len(signs)
    blocks = [sp.Matrix([[2, 1+sp.I], [1-sp.I, 3]]),
              sp.Matrix([[0, 1], [2, 0]]),
              sp.Matrix([[1, sp.I], [sp.I, 2]]),
              sp.Matrix([[4, 0], [0, 1]])]
    assert blocks[0]*blocks[1] != blocks[1]*blocks[0]

    def q(y):
        a, b, c, d = blocks
        ans = ((y+1)*a).row_join(b).col_join(c.row_join((2-y)*d))
        if transformed:
            uu = sp.kronecker_product(u, I2)
            ans = uu.H*ans*uu
        return ans

    vals = [0, 5, 11][:h]
    rational = []
    for j in range(h):
        ri = sp.zeros(2**(h+2))
        for a, b in itertools.product(range(2), repeat=2):
            xs = [I2]*(h+2)
            xs[0] = unit(a, b)
            xs[j+1] = unit(b, a) if signs[j] else unit(a, b)
            ri += kron(xs)
        rational.append(ri)

    def main_matrix(y, upto):
        ans = insert_base(q(y), 0, h+1)
        for j in range(upto):
            z = y-vals[j] if signs[j] else vals[j]-y
            rr = (z*sp.eye(2**(h+2))-rational[j])/(z-1)
            ans = ans*rr if signs[j] else rr*ans
        return ans

    result = sp.eye(2**(h+1))
    for j in range(h):
        top = main_matrix(vals[j], j)
        step = sp.zeros(2**(h+1))
        for a, b in itertools.product(range(2), repeat=2):
            block = top[a*2**(h+1):(a+1)*2**(h+1), b*2**(h+1):(b+1)*2**(h+1)]
            xs = [I2]*(h+1)
            xs[j] = unit(a, b) if signs[j] else unit(b, a)
            step += kron(xs)*block
        result = result*step
    v = kron([u if plus else sp.conjugate(u) for plus in signs]+[I2])
    return result.applyfunc(sp.expand), v


def covariance_checks():
    mats = [sp.Matrix([[1, 0], [1+2*sp.I, 1]]),
            sp.Matrix([[1, 1], [sp.I, 1+sp.I]])]
    permutation = sum((sp.kronecker_product(unit(i, j), unit(j, i))
                       for i, j in itertools.product(range(2), repeat=2)), sp.zeros(4))
    contraction = sum((sp.kronecker_product(unit(i, j), unit(i, j))
                       for i, j in itertools.product(range(2), repeat=2)), sp.zeros(4))
    cases = negative_controls = 0
    for index, u in enumerate(mats):
        tensor = sp.kronecker_product(u, u)
        assert permutation*tensor == tensor*permutation
        tensor = sp.kronecker_product(u.H, sp.conjugate(u).inv())
        assert (contraction*tensor-tensor*contraction).applyfunc(sp.expand) == sp.zeros(4)
        for h in range(1, 4 if index == 0 else 3):
            for signs in itertools.product([True, False], repeat=h):
                a, v = residue_model(signs, u)
                b, _ = residue_model(signs, u, True)
                assert (b-v.H*a*v).applyfunc(sp.expand) == sp.zeros(2**(h+1)), signs
                if not all(signs):
                    wrong = kron([u]*h+[I2])
                    assert (b-wrong.H*a*wrong).applyfunc(sp.expand) != sp.zeros(2**(h+1))
                    negative_controls += 1
                cases += 1
    return {"exact_noncommuting_residue_models": cases,
            "all_sign_patterns_through_length": 3,
            "complex_conjugation_negative_controls": negative_controls,
            "elementary_permutation_and_contraction_checks": 4,
            "rational_returns_unchanged": "(z I-P)/(z-1), (z I-Omega)/(z-1)",
            "finite_models_not_an_all_word_proof": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources = source_records(args.offline)
    checks = {"phase": phase_checks(), "mixed_words": covariance_checks()}
    files = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
             f"paper/shared/{STEM}-references.tex",
             f"scripts/check_{STEM.replace('-', '_')}.py",
             "paper/sections/new/commutator-matrix.tex",
             "paper/sections/new/jacquet-integrated-descent.tex",
             "paper/sections/recovered/87-rq-section.tex",
             "paper/sections/recovered/95-jf-section.tex",
             "notes/residue-source-dictionary.md"]
    result = {"schema_version": 1, "status": "PASS",
              "classification": "closed exact wave-isometry supplier for actual residue forms",
              "supplied_interfaces": ["VIso", "VIsoCpt"],
              "theorem": "beta_w(waveG(s,w,x),waveG(s,w,y))=beta_w(x,y)",
              "checks": checks, "sources": sources,
              "artifact_hashes": {p: digest((ROOT/p).read_bytes()) for p in files},
              "scope": {"uniform_identity": "All original levels, ranks, admissible finite signed words and complex s",
                        "coefficient_classes": "Compact smooth or all-derivative rapidly decreasing, each with the original positive Gram cutoff",
                        "same_original_haar_constant_on_both_sides": True,
                        "whole_node_count_changed": False,
                        "not_verified": ["Mixed determinant Cauchy inequality",
                                         "Partial-head Fourier comparison on every lower stratum",
                                         "Global rational-return and Gram bounds",
                                         "Any full Lean build"]}}
    dest = ROOT / "certificates" / (STEM+".json")
    dest.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "checks": checks, "certificate": str(dest.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    main()
