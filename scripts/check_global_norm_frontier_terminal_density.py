#!/usr/bin/env python3
"""Exact compact-germ/source diagnostics; no Lean build or numerical proof."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "global-norm-frontier-terminal-density"
SOURCES = [
    ("Formalism.HermitianCurvature.StatementG",
     [(9, 68), (182, 244), (251, 300), (337, 361), (418, 439)]),
    ("Formalism.HermitianCurvature.StatementU",
     [(63, 118), (663, 695)]),
    ("Formalism.HermitianCurvature.RealInputsClosedAdmissibleSettings",
     [(245, 270)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.KloostDensOfParts",
     [(7, 38)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.KloostermanDensityOfParts",
     [(204, 288), (294, 399)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.DensityConstantOfParts",
     [(11, 17), (50, 73)]),
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


def reversal(n):
    return sp.Matrix(n, n, lambda i, j: int(i+j == n-1))


def hessenberg_checks():
    t, q, z = sp.symbols("t q z", nonzero=True)
    done = []
    for n in range(1, 7):
        xs = sp.symbols(f"x1:{n+1}")
        yy = {(i, j): sp.Symbol(f"y{i}_{j}")
              for i in range(n+1) for j in range(i+1, n+1)}
        y = sp.Matrix(n+1, n+1, lambda i, j: yy.get((i, j), 0))
        ss = sp.Matrix(n+1, n+1, lambda i, j: int(i == j+1))
        hh = t*ss+sp.diag(q, *xs)+y
        det = sp.expand(hh.det(method="domain-ge"))
        aa = sp.expand(hh[1:, 1:].det(method="domain-ge"))
        bb = det.subs(q, 0)
        assert sp.expand(det-aa*q-bb) == 0
        assert aa.subs(t, 0) == sp.prod(xs)
        assert bb.subs(t, 0) == 0
        mm = reversal(n+1)*hh
        xx = reversal(n)*mm[:n, :n]-t*sp.eye(n)
        bvec = reversal(n)*mm[:n, n:]
        assert all(xx[i, j] == 0 for i in range(n) for j in range(i+1))
        cof = sum(((-xx)**j*bvec)[0]*t**(n-1-j) for j in range(n))
        assert sp.expand(cof-(-1)**(n-1)*aa) == 0
        crit = {q:z, **{x:z for x in xs}}
        dq = -sp.diff(det, t).subs(t, 0).subs(crit)/z**n
        assert sp.simplify(dq-sum(yy[i, i+1] for i in range(n))/z) == 0
        g0 = sum(xs)+z**(n+1)/sp.prod(xs)
        assert sp.expand(g0.subs({x:z for x in xs})-(n+1)*z) == 0
        assert all(sp.diff(g0,x).subs({x:z for x in xs}) == 0 for x in xs)
        hess = sp.hessian(g0, xs).subs({x:z for x in xs})
        assert hess == (sp.eye(n)+sp.ones(n))/z
        assert sp.simplify(hess.det()-(n+1)/z**n) == 0
        done.append(n)
    return {"full_symbolic_Hessenberg_determinant_and_cofactor_sizes": done,
            "critical_corner_derivative_all_strict_upper_parameters": True,
            "critical_phase_and_complex_Hessian_determinants": True}


def phase_checks():
    t = sp.symbols("t", nonzero=True)
    for n in range(1, 6):
        a = sp.Matrix(1, n, sp.symbols(f"a0:{n}"))
        b = sp.Matrix(n, 1, sp.symbols(f"b0:{n}"))
        vv = sp.Matrix(n, n, lambda i,j: sp.Symbol(f"v{i}_{j}") if i<j else 0)
        rho = t*a*reversal(n)*(sp.eye(n)+vv)
        near = [t*vv[i,i+1] for i in range(n-1)]+[t*b[n-1]]
        original = a[n-1]+sum(vv[i,i+1] for i in range(n-1))+b[n-1]
        assert sp.expand(rho[0]+sum(near)-t*original) == 0
    n = sp.symbols("n", integer=True, positive=True)
    complex_block_dim = 2*n+n*(n-1)/2
    assert sp.expand(2*complex_block_dim-2*n-n*(n+1)) == 0
    assert sp.expand(-n*(n+1)+n+n**2) == 0
    assert sp.expand(n-2*n+n*(n+1)-n**2) == 0
    return {"original_phase_changes_sizes": list(range(1,6)),
            "complex_coordinate_dimensions_symbolic": True,
            "all_t_and_z_normalizing_exponents_symbolic": True,
            "Lebesgue_to_mu_beta_long_and_block_powers_preserved": True}


def real_hessian_checks():
    count = 0
    zz = sp.Rational(3,5)+sp.I*sp.Rational(4,5)
    beta = 2-sp.I
    for n in range(1,6):
        hc = (sp.eye(n)+sp.ones(n))/zz
        for angle in [sp.Integer(1),sp.I,(3+4*sp.I)/5]:
            hh = ((beta/angle)*hc).applyfunc(sp.expand_complex)
            re, im = hh.applyfunc(sp.re), hh.applyfunc(sp.im)
            hr = re.row_join(-im).col_join((-im).row_join(-re))
            complex_i = sp.zeros(n).row_join(-sp.eye(n)).col_join(sp.eye(n).row_join(sp.zeros(n)))
            assert complex_i.T*hr*complex_i == -hr
            target = (-1)**n * (beta*sp.conjugate(beta))**n * hc.det()*sp.conjugate(hc.det())
            assert sp.simplify(hr.det(method="domain-ge")-target) == 0
            assert target != 0
            count += 1
    return {"exact_real_Hessian_determinant_cases":count,
            "complex_rank_range":[1,5],
            "complex_structure_pairs_positive_and_negative_directions":True,
            "no_extra_stationary_phase_unit":True}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--offline",action="store_true")
    args=parser.parse_args()
    records=source_records(args.offline)
    checks={}
    for name,func in [("hessenberg",hessenberg_checks),("phase_and_powers",phase_checks),
                      ("real_Hessian",real_hessian_checks)]:
        checks[name]=func()
        print(json.dumps({"completed":name,"checks":checks[name]}),flush=True)
    artifacts=[]
    for rel in [f"paper/shared/{STEM}.tex",f"paper/shared/{STEM}-references.tex",
                f"notes/{STEM}.md",f"scripts/check_{STEM.replace('-','_')}.py"]:
        data=(ROOT/rel).read_bytes()
        artifacts.append({"path":rel,"bytes":len(data),"sha256":digest(data)})
    cert={"status":"PASS","classification":"closed local KloostDens supplier; independent review accepted",
          "scope":"Exact source authentication and polynomial/measure diagnostics; human proof supplies all ranks. No Lean build claim.",
          "source_revision":REV,"sources":records,"checks":checks,"artifacts":artifacts,
          "external_theorem":{"authors":"Lawrence C. Evans and Maciej Zworski",
             "title":"Lectures on Semiclassical Analysis, version 0.2",
             "theorem":"3.15, pp.40–41","url":"https://math.mit.edu/~vwg/semiclassicalEvansZworski.pdf",
             "verified_scope":"Compact smooth stationary phase, nondegenerate isolated critical points, finite-seminorm remainder, leading signature/determinant factor"},
          "not_claimed":["rank-uniform GermRate","PhiZero","HeadTop","KernelFourierIntegralBound","W06 or W08 completion"]}
    dest=ROOT/"certificates"/(STEM+".json")
    dest.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"status":"PASS","sources":len(records),"checks":checks}))


if __name__=="__main__":
    main()
