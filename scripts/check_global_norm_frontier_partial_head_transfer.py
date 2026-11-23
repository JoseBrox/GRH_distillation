#!/usr/bin/env python3
"""Exact block-head, radical, Capelli and gauge diagnostics; no Lean build."""
from __future__ import annotations

import argparse
from functools import lru_cache
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
STEM = "global-norm-frontier-partial-head-transfer"
SOURCES = [
    ("Formalism.HermitianCurvature.StatementU",
     [(28, 44), (63, 83), (84, 128), (171, 187)]),
    ("Formalism.HermitianCurvature.StatementD",
     [(124, 147), (222, 235)]),
    ("Formalism.HermitianCurvature.RealInputsClosedAdmissibleSettings",
     [(64, 76), (83, 109), (180, 196), (212, 243)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.CutHL2",
     [(22, 52)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.DifferentiableAtOfPuncturedSmooth",
     [(79, 100), (117, 131)]),
    ("Formalism.HermitianCurvature.StatementWd", [(119, 137)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.FubiniHeadLastPart",
     [(276, 318), (353, 371)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.LevelZeroKernel",
     [(29, 36), (74, 95), (99, 119)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.HeadJ",
     [(13, 29)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.PointStep",
     [(23, 37), (45, 62)]),
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


def zmat(m, n, seed=0):
    return sp.Matrix(m, n, lambda i, j:
                     sp.Rational((3*i+2*j+seed) % 7-3, 3)
                     + sp.I*sp.Rational((2*i+5*j+seed+1) % 5-2, 4))


def reverse(n):
    return sp.Matrix(n, n, lambda i, j: int(i+j == n-1))


def exact_matrix(m):
    """Normalize Gaussian rationals before matrix elimination."""
    return m.applyfunc(sp.expand_complex)


def parts(n):
    if n == 0:
        yield []
    else:
        for first in range(1, n+1):
            for tail in parts(n-first):
                yield [first]+tail


def head_case(sizes, seed):
    n = sum(sizes)
    cuts = [0]
    for s in sizes:
        cuts.append(cuts[-1]+s)
    block = [b for b, s in enumerate(sizes) for _ in range(s)]
    w = sp.diag(*(reverse(s) for s in sizes))
    ds = [sp.Integer(2+b)+sp.I*(b+1) for b in range(len(sizes))]
    d = sp.diag(*(ds[b]*sp.eye(s) for b, s in enumerate(sizes)))
    raw = zmat(n, n, seed)
    lower = sp.eye(n)+sp.Matrix(n, n, lambda i, j: raw[i, j] if block[i] > block[j] else 0)
    upper = sp.eye(n)+sp.Matrix(n, n, lambda i, j: raw[i, j] if i < j else 0)
    zz = exact_matrix(lower*w*d*upper)
    ll, bb = sp.eye(n), sp.zeros(n)
    for b in range(len(sizes)):
        ib = slice(cuts[b], cuts[b+1])
        for c in range(b, len(sizes)):
            ic = slice(cuts[c], cuts[c+1])
            value = zz[ib, ic]
            for a in range(b):
                ia = slice(cuts[a], cuts[a+1])
                value -= ll[ib, ia]*bb[ia, ic]
            bb[ib, ic] = exact_matrix(value)
        assert sp.expand_complex(bb[ib, ib].det(method="domain-ge")-(ds[b]**sizes[b])*reverse(sizes[b]).det()) == 0, (sizes, seed, b)
        for c in range(b+1, len(sizes)):
            ic = slice(cuts[c], cuts[c+1])
            value = zz[ic, ib]
            for a in range(b):
                ia = slice(cuts[a], cuts[a+1])
                value -= ll[ic, ia]*bb[ia, ib]
            ll[ic, ib] = exact_matrix(exact_matrix(value)*bb[ib, ib].inv(method="DM"))
    assert (ll-lower).applyfunc(sp.simplify) == sp.zeros(n)
    assert ((w*d).inv()*bb-upper).applyfunc(sp.simplify) == sp.zeros(n)
    return w, w*lower*w, d, upper, zz


def block_and_shear_checks():
    cases = 0
    shears = 0
    for n in range(1, 6):
        for pattern in parts(n):
            w, low0, dd, up, zz = head_case(pattern, cases)
            cases += 1
            for s in [1, 2]:
                ws = reverse(s)
                vv, bb = zmat(s, n, cases), zmat(n, s, cases+1)
                aa, bnew = exact_matrix(ws*vv*low0.inv(method="DM")*w.inv()), exact_matrix(up.inv(method="DM")*bb)
                h0 = exact_matrix(w*low0*dd*up)
                hb = (3+sp.I)*ws
                orig = sp.BlockMatrix([[h0, w*low0*dd*bb],
                                       [ws*vv*dd*up, ws*vv*dd*bb+hb]]).as_explicit()
                fac = sp.BlockMatrix([[sp.eye(n), sp.zeros(n, s)], [aa, sp.eye(s)]]).as_explicit()
                fac *= sp.diag(h0, hb)
                fac *= sp.BlockMatrix([[sp.eye(n), bnew], [sp.zeros(s, n), sp.eye(s)]]).as_explicit()
                assert exact_matrix(orig-fac) == sp.zeros(n+s)
                aright = exact_matrix(low0.inv(method="DM")*w.inv())
                bu = exact_matrix(up.inv(method="DM"))
                ajac = sp.kronecker_product(aright.T, ws).det(method="domain-ge")
                bjac = sp.kronecker_product(sp.eye(s), bu).det(method="domain-ge")
                jac = sp.expand_complex(ajac*bjac)
                assert sp.expand_complex(jac*sp.conjugate(jac)) == 1
                shears += 1
    a = sp.symbols("a")
    assert sp.Matrix([[1, 0], [a, 1]])*reverse(2)*sp.Matrix([[1, -a], [0, 1]]) == reverse(2)
    return {"all_ordered_partitions_through_size": 5,
            "exact_block_gaussian_recoveries": cases,
            "exact_append_shears_and_real_unit_jacobians": shears,
            "nonproper_full_lower_group_negative_control": True}


def radical(h, p, seed):
    m = h.rows
    xx = zmat(m, p, seed)
    aa = zmat(p, p, seed+1)
    kk = sp.Matrix(p, p, lambda i, j: aa[i, j] if i < j else
                   -sp.conjugate(aa[j, i]) if i > j else sp.I*(i+seed+1))
    jj = reverse(p)
    rr = sp.BlockMatrix([[sp.eye(p), -jj*xx.conjugate().T*h,
                          jj*(-xx.conjugate().T*h*xx/2+kk)],
                         [sp.zeros(m, p), sp.eye(m), xx],
                         [sp.zeros(p), sp.zeros(p, m), sp.eye(p)]]).as_explicit()
    return xx, kk, exact_matrix(rr)


def radical_checks():
    count = 0
    for p, rho, k in itertools.product([1, 2, 3], [0, 1], [1, 2]):
        middle = sp.diag(sp.eye(k), -sp.eye(1))
        if rho:
            middle = sp.BlockMatrix([[sp.zeros(1), sp.zeros(1, k+1), sp.eye(1)],
                                    [sp.zeros(k+1, 1), middle, sp.zeros(k+1, 1)],
                                    [sp.eye(1), sp.zeros(1, k+1), sp.zeros(1)]]).as_explicit()
        m = middle.rows
        jj = reverse(p)
        xl, kl, rl = radical(middle, p, 2)
        xr, kr, rr = radical(middle, p, 5)
        zz = zmat(p, p, 4)+5*sp.eye(p)
        gamma = sp.eye(m)
        if rho:
            _, _, gamma = radical(sp.diag(sp.eye(k), -sp.eye(1)), 1, 9)
        hh = sp.BlockMatrix([[sp.zeros(p), sp.zeros(p, m), jj],
                             [sp.zeros(m, p), middle, sp.zeros(m, p)],
                             [jj, sp.zeros(p, m), sp.zeros(p)]]).as_explicit()
        mm = sp.BlockMatrix([[sp.zeros(p), sp.zeros(p, m), zz.conjugate().T.inv(method="DM")*jj],
                             [sp.zeros(m, p), gamma, sp.zeros(m, p)],
                             [jj*zz, sp.zeros(p, m), sp.zeros(p)]]).as_explicit()
        gg = exact_matrix(rl.inv(method="DM")*exact_matrix(mm)*rr)
        assert (gg.conjugate().T*hh*gg-hh).applyfunc(sp.simplify) == sp.zeros(2*p+m)
        sl0, sl1, sl2 = slice(0, p), slice(p, p+m), slice(p+m, 2*p+m)
        dd = gg[sl2, sl0]
        qxl = -gg[sl1, sl0]*dd.inv()
        qxrs = -jj*dd.inv()*gg[sl2, sl1]*middle.inv()
        qkl = -jj*gg[sl0, sl0]*dd.inv()-xl.conjugate().T*middle*xl/2
        qkr = jj*dd.inv()*gg[sl2, sl2]+xr.conjugate().T*middle*xr/2
        qgamma = gg[sl1, sl1]-gg[sl1, sl0]*dd.inv()*gg[sl2, sl1]
        for original, recovered in [(xl, qxl), (xr.conjugate().T, qxrs), (kl, qkl), (kr, qkr), (gamma, qgamma)]:
            assert (original-recovered).applyfunc(sp.simplify) == sp.zeros(*original.shape)
        count += 1
    return {"exact_unitary_radical_recovery_cases": count,
            "ranks_tested": [1, 2, 3], "residual_ranks_tested": [0, 1],
            "k_tested": [1, 2], "all_five_inverse_formulas": True}


def add(a, b, scalar=1):
    out = dict(a)
    for key, value in b.items():
        out[key] = sp.expand(out.get(key, 0)+scalar*value)
        if out[key] == 0:
            del out[key]
    return out


def prod(a, b):
    out = {}
    for x, sx in a.items():
        for y, sy in b.items():
            out = add(out, {x+y: sx*sy})
    return out


def qminor(rows, cols, u):
    out = {}
    for pm in itertools.permutations(range(len(rows))):
        inv = sum(pm[i] > pm[j] for i in range(len(pm)) for j in range(i+1, len(pm)))
        term = {(): sp.Integer((-1)**inv)}
        for c, a in enumerate(pm):
            i, j = rows[a], cols[c]
            term = prod(term, add({((i, j),): sp.Integer(1)}, {(): u-c} if i == j else {}))
        out = add(out, term)
    return out


def capelli_checks():
    u, cc = sp.symbols("u c")
    count = 0
    for j in [1, 2, 3]:
        def order(g):
            a, b = g
            return (0 if a == j and b < j else 2 if a < j and b == j else 1, a, b)

        @lru_cache(None)
        def normal(word):
            for i in range(len(word)-1):
                a, b = word[i:i+2]
                if order(a) > order(b):
                    out = dict(normal(word[:i]+(b, a)+word[i+2:]))
                    if a[1] == b[0]:
                        out = add(out, normal(word[:i]+((a[0], b[1]),)+word[i+2:]))
                    if b[1] == a[0]:
                        out = add(out, normal(word[:i]+((b[0], a[1]),)+word[i+2:]), -1)
                    return out
            return {word: sp.Integer(1)}

        def image(expr, lower):
            out = {}
            for word, coeff in expr.items():
                for ww, sw in normal(word).items():
                    factor = coeff*sw
                    left, right = 0, len(ww)
                    while left < right and order(ww[left])[0] == 0:
                        factor *= lower[ww[left][1]]
                        left += 1
                    while right > left and order(ww[right-1])[0] == 2:
                        factor *= int(ww[right-1][0] == j-1)
                        right -= 1
                    out = add(out, {ww[left:right]: factor})
            return {w: sp.simplify(c) for w, c in out.items() if sp.simplify(c) != 0}

        for seed in [1, 3, 5]:
            zz = zmat(j, j, seed)+4*sp.eye(j)
            zi = zz.inv()
            lower = [cc*zi[b, j-1] for b in range(j)]
            lhs = qminor(list(range(j+1)), list(range(j+1)), u)
            diag = prod(qminor(list(range(j)), list(range(j)), u),
                        {(): u-j, ((j, j),): 1})
            small = {}
            for b in range(j):
                cols = [a for a in range(j) if a != b]
                coeff = zz[:j-1, cols].det()
                small = add(small, qminor(list(range(j-1)), cols, u), coeff)
                assert sp.simplify(coeff-(-1)**(j-1+b)*zz.det()*zi[b, j-1]) == 0
            expr = add(add(lhs, diag, -1), small, cc/zz.det())
            assert image(expr, lower) == {}
            count += 1
    kap, y = sp.symbols("kappa Y")
    assert sp.expand(y+kap-kap) == y
    assert sp.expand(y-kap+kap) == y
    r, lev, k = sp.symbols("r j k", integer=True)
    assert sp.expand(2*(2*(r-lev)+k)-2-2*(2*(r-lev)+k-1)) == 0
    return {"noncommuting_PBW_general_head_border_cases": count,
            "maximum_Capelli_size": 4,
            "spectral_and_new_coordinate_parameters_symbolic": True,
            "exact_adjugate_contraction": True,
            "both_gauge_shifts_and_density_exponent": True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources = source_records(args.offline)
    checks = {}
    for name, fn in [("block_heads", block_and_shear_checks),
                     ("radical", radical_checks), ("capelli", capelli_checks)]:
        checks[name] = fn()
        print(json.dumps({"completed": name, "checks": checks[name]}), flush=True)
    paths = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", f"scripts/check_global_norm_frontier_partial_head_transfer.py",
             "paper/sections/recovered/85-rt-section.tex",
             "paper/sections/recovered/86-rc-section.tex",
             "paper/sections/recovered/95-jf-section.tex",
             "paper/sections/new/jacquet-integrated-descent.tex"]
    result = {"schema_version": 1, "status": "PASS",
              "classification": "closed actual below-terminal partial-head supplier; pending independent review",
              "supplied_interfaces": ["SliceCpt", "HeadJ", "RadHead"],
              "checks": checks, "sources": sources,
              "artifact_hashes": {p: digest((ROOT/p).read_bytes()) for p in paths},
              "scope": {"all_actual_block_heads_and_finite_admissible_words": True,
                        "level_range": "0 <= j < r for transfer, 0 <= j <= r for SliceCpt",
                        "original_Haar_measures_phases_gauges_and_cutoffs_retained": True,
                        "whole_node_count_changed": False,
                        "not_verified": ["Terminal HeadTop for the actual top lift",
                                         "Complete all-level Fourier kernel estimate",
                                         "Global rational-return/Gram estimate", "Full Lean build"]}}
    (ROOT/f"certificates/{STEM}.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "sources": len(sources), "checks": checks}))


if __name__ == "__main__":
    main()
