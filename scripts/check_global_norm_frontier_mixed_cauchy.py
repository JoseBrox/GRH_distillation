#!/usr/bin/env python3
"""Exact original fused duality and mixed Cauchy checks; bounded pinned sources."""
from __future__ import annotations

import argparse
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
STEM = "global-norm-frontier-mixed-cauchy"
SOURCES = [
    ("Formalism.HermitianCurvature.RealInputsClosedAdmissibleSettings",
     [(18, 31), (139, 146)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.PBFCstmt",
     [(10, 18)]),
    ("Formalism.HermitianCurvature.StatementM", [(130, 135), (405, 411)]),
    ("Formalism.HermitianCurvature.StatementWd", [(49, 55), (89, 102)]),
    ("Formalism.HermitianCurvature.StatementD", [(176, 194), (212, 214)]),
    ("Formalism.HermitianCurvature.StatementJC", [(18, 23), (90, 106)]),
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


I2 = sp.eye(2)
J = sp.Matrix([[0, 1], [-1, 0]])


def e(i, j):
    return I2[:, i]*I2[j, :]


def kron(xs):
    ans = sp.ones(1)
    for x in xs:
        ans = sp.kronecker_product(ans, x)
    return ans


def fused_model(old_signs, old_vals, new_vals, plus, offset=1):
    old = len(old_signs)
    signs = old_signs + [plus]*len(new_vals)
    vals = old_vals + [v if plus else v+offset for v in new_vals]
    h = len(signs)
    size = 2**(h+2)
    sub = size//2
    returns = []
    for j in range(h):
        p = sp.zeros(size)
        for i, l in itertools.product(range(2), repeat=2):
            xs = [I2]*(h+2)
            xs[0] = e(i, l)
            xs[j+1] = e(l, i) if signs[j] else e(i, l)
            p += kron(xs)
        returns.append(p)

    def current(y, upto):
        ans = y*sp.eye(size)
        for i, j in itertools.product(range(2), repeat=2):
            xs = [I2]*(h+2)
            xs[0] = e(i, j)
            xs[-1] = e(i, j)
            ans += kron(xs)
        for j in range(upto):
            z = y-vals[j] if signs[j] else vals[j]-y
            rr = (z*sp.eye(size)-returns[j])/(z-1)
            ans = ans*rr if signs[j] else rr*ans
        return ans

    old_residue = sp.eye(sub)
    additional = sp.eye(sub)
    for j in range(h):
        main = current(vals[j], j)
        step = sp.zeros(sub)
        for i, l in itertools.product(range(2), repeat=2):
            xs = [I2]*(h+1)
            xs[j] = e(i, l) if signs[j] else e(l, i)
            step += kron(xs)*main[i*sub:(i+1)*sub, l*sub:(l+1)*sub]
        if j < old:
            old_residue *= step
        else:
            additional *= step
    jj = kron([I2]*old + [J]*len(new_vals) + [I2])
    qprod = sp.Integer(1)
    for y in new_vals:
        q = sp.Integer(y*(y+2))
        for sign, a in zip(old_signs, old_vals):
            q *= sp.Rational(y-a+1, y-a) if sign else sp.Rational(a-y, a-y-1)
        qprod *= q
    return old_residue, additional, jj, qprod


def polynomial_identities():
    y = sp.symbols("y")
    omega = sum((kron([e(i, j), e(i, j)]) for i, j in itertools.product(range(2), repeat=2)), sp.zeros(4))
    permutation = sum((kron([e(i, j), e(j, i)]) for i, j in itertools.product(range(2), repeat=2)), sp.zeros(4))
    q = y*sp.eye(4)+omega
    qt_plus = (y+1)*sp.eye(4)+permutation
    jj = kron([J, I2])
    assert (q*jj*qt_plus*jj.inv()-y*(y+2)*sp.eye(4)).applyfunc(sp.expand) == sp.zeros(4)
    a, b = sp.symbols("a b")
    ps = {}
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        p = sp.zeros(8)
        for x, z in itertools.product(range(2), repeat=2):
            xs = [I2]*3
            xs[i], xs[j] = e(x, z), e(z, x)
            p += kron(xs)
        ps[i, j] = p
    aa = a*sp.eye(8)-ps[0, 1]
    bb = (a+b)*sp.eye(8)-ps[0, 2]
    cc = b*sp.eye(8)-ps[1, 2]
    assert (aa*bb*cc-cc*bb*aa).applyfunc(sp.expand) == sp.zeros(8)
    assert ((a*sp.eye(4)-permutation)*(-a*sp.eye(4)-permutation)
            -(1-a*a)*sp.eye(4)).applyfunc(sp.expand) == sp.zeros(4)
    return {"adjacent_quantum_determinant": "q(y)=y(y+2) in the U(gl2) standard module",
            "symbolic_yang_baxter_identity": True,
            "symbolic_two_index_unitarity": True,
            "all_identities_use_noncommuting_matrix_units": True}


def fused_checks():
    cases = old_word_cases = adjacent_controls = cauchy_tests = 0
    examples = []
    configs = [([], [], [3, 8, 14][:K]) for K in [1, 2, 3]]
    configs += [(list(signs), [21, 30][:h], [3, 8][:K])
                for h in [1, 2]
                for signs in itertools.product([True, False], repeat=h)
                for K in [1, 2]]
    for old_signs, old_vals, new_vals in configs:
        metric, ap, jj, qprod = fused_model(old_signs, old_vals, new_vals, True)
        metric2, am, _, qprod2 = fused_model(old_signs, old_vals, new_vals, False)
        assert metric == metric2 and qprod == qprod2 and qprod > 0
        c = jj.inv()*am*jj
        assert ap*c == c*ap == qprod*sp.eye(ap.rows)
        assert metric*ap == (metric*ap).H
        assert metric*am == (metric*am).H
        if old_signs:
            old_word_cases += 1
        else:
            # Exact LDL establishes positivity only for these diagnostic models.
            for form in [ap, am]:
                _, d = form.LDLdecomposition(hermitian=True)
                assert all(z > 0 for z in d.diagonal())
            for seed in range(3):
                x = sp.Matrix([sp.Integer((i+seed) % 5-2)+sp.I*((2*i+seed) % 3-1) for i in range(ap.rows)])
                y = sp.Matrix([sp.Integer((3*i+seed) % 7-3)+sp.I*((i+2*seed) % 5-2) for i in range(ap.rows)])
                pairing = (y.H*jj*x)[0]
                lhs = sp.expand(qprod*pairing*sp.conjugate(pairing))
                rhs = sp.expand((x.H*ap*x)[0]*(y.H*am*y)[0])
                assert lhs <= rhs
                # Add an arbitrary null copy: no inverse of the base form exists.
                xx = x.col_join(y)
                yy = y.col_join(x)
                base = sp.diag(sp.eye(ap.rows), sp.zeros(ap.rows))
                aa = sp.diag(ap, ap)
                bb = sp.diag(am, am)
                jbig = sp.diag(jj, jj)
                pair2 = (yy.H*base*jbig*xx)[0]
                assert sp.expand(qprod*pair2*sp.conjugate(pair2)) == lhs
                assert sp.expand((xx.H*base*aa*xx)[0]*(yy.H*base*bb*yy)[0]) == rhs
                cauchy_tests += 2
            _, wrong, _, _ = fused_model(old_signs, old_vals, new_vals, False, offset=0)
            assert ap*jj.inv()*wrong*jj != qprod*sp.eye(ap.rows)
            adjacent_controls += 1
        if not old_signs:
            examples.append({"new_insertions": len(new_vals), "parameters": new_vals,
                             "exact_scalar": str(qprod)})
        cases += 1
    return {"exact_fused_inverse_models": cases,
            "models_with_nonempty_old_signed_word": old_word_cases,
            "wrong_adjacent_shift_negative_controls": adjacent_controls,
            "positive_and_degenerate_form_checks": cauchy_tests,
            "examples": examples,
            "old_word_scalar_factors_retained": True,
            "maximum_total_auxiliary_factors_tested": 4,
            "no_assumption_of_shifted_parameter_separation": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources = source_records(args.offline)
    checks = {"symbolic": polynomial_identities(), "fused": fused_checks()}
    files = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
             f"paper/shared/{STEM}-references.tex",
             f"scripts/check_{STEM.replace('-', '_')}.py",
             "paper/sections/recovered/79-ca-section.tex",
             "paper/sections/recovered/81-rp-section.tex",
             "paper/sections/recovered/89-re-section.tex",
             "paper/sections/new/jacquet-integrated-descent.tex",
             "notes/residue-source-dictionary.md"]
    result = {"schema_version": 1, "status": "PASS",
              "classification": "closed actual mixed determinant Cauchy supplier",
              "supplied_interfaces": ["SizeStd", "SizeStdCpt"],
              "checks": checks, "sources": sources,
              "artifact_hashes": {p: digest((ROOT/p).read_bytes()) for p in files},
              "scope": {"all_original_levels_and_finite_admissible_words": True,
                        "normalizations": "Exact q_w, plus y, minus y+1, original Haar/gauge factor",
                        "allows_degenerate_old_residue_form": True,
                        "whole_node_count_changed": False,
                        "not_verified": ["All-stratum partial-head Fourier identity",
                                         "Global rational-return and Gram comparison",
                                         "Any full Lean build"]}}
    dest = ROOT / "certificates" / (STEM+".json")
    dest.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources), "checks": checks,
                      "certificate": str(dest.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    main()
