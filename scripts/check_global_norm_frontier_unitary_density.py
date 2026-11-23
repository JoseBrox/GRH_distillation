#!/usr/bin/env python3
"""Authenticate the actual compact transfer and test its exact frame algebra."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import sympy as s

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "global-norm-frontier-unitary-density"
SOURCES = [
    ("Formalism.FormalDegreeBessel.StatementG", [(59, 70)]),
    ("Formalism.HermitianCurvature.StatementB", [(98, 156)]),
    ("Formalism.HermitianCurvature.StatementD", [(75, 120)]),
    ("Formalism.HermitianCurvature.RealInputsClosedAdmissibleSettings",
     [(56, 58), (245, 263)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.HcoSmulRight",
     [(10, 17), (218, 283)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.ExistsMeasurableSection",
     [(206, 287), (288, 399), (400, 450)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.SupportPhiZeroSubset",
     [(39, 94), (170, 203), (218, 229)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.FlagStabilizerFixesFrame",
     [(290, 365)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.UnipotentCoordinatesMeasurePreserving",
     [(5661, 5768), (5769, 5783)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.MatExtMulVec",
     [(33, 41), (329, 428), (429, 467)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.UnipotentCharacterOneOfProduct",
     [(152, 229)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.HermitianFormRankZeroApply",
     [(759, 842)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.SubMulRight",
     [(361, 377), (382, 447)]),
    ("Formalism.HermitianCurvature.HermitianCurvatureProofs.FibreIntegralCells",
     [(25, 51), (61, 132)]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def sources(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert (atlas["repository"], atlas["commit"]) == (REPO, REV)
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    ans = []
    for module, ranges in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        rec = inspect_file({"repository": REPO, "commit": REV, "path": path,
                            "git_blob_sha1": blobs[module]}, offline)
        assert rec["matches_pinned_blob"]
        data = (ROOT / "build/source-cache" / REPO / REV / path).read_bytes()
        lines = data.splitlines(keepends=True)
        chunks = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpt = b"".join(lines[lo-1:hi])
            assert len(excerpt) <= 12288
            chunks.append({"lines": [lo, hi], "bytes": len(excerpt),
                           "sha256": sha(excerpt)})
        ans.append({"module": module, **{key:rec[key] for key in
                    ["repository", "commit", "path", "bytes", "sha256",
                     "git_blob_sha1", "matches_pinned_blob"]}, "excerpts": chunks})
    return ans


def clean(m):
    return m.applyfunc(s.simplify) if isinstance(m, s.MatrixBase) else s.simplify(m)


def eq(a, b):
    assert clean(a-b) == (s.zeros(*a.shape) if isinstance(a, s.MatrixBase) else 0)


def form(r, tp):
    h = s.zeros(2*r+2)
    for i in range(r):
        h[i, r+i] = h[r+i, i] = 1
    h[2*r, 2*r], h[2*r+1, 2*r+1] = -tp, 1
    return h


def frame(r, t, tp):
    f = s.zeros(2*r+2, r+1)
    for i in range(r):
        f[i, i] = 1
    f[2*r, r] = s.sqrt(t/tp)
    return f


def section(z, t, tp):
    n, r = z.rows, z.rows-1
    h = form(r, tp)
    f = frame(r, t, tp)
    delta = z.det()
    minor = z[:r, :r].det()
    gram = clean(delta*s.conjugate(delta)-t*tp*minor*s.conjugate(minor))
    assert gram > 0
    kap = z.adjugate()[:, r]
    nn = clean((kap.H*kap)[0])
    ph = clean(delta/s.sqrt(delta*s.conjugate(delta)))
    ss, ssp = s.sqrt(gram/t), s.sqrt(gram/tp)
    al = -z[r:r+1, :]/s.sqrt(t*tp)
    be = clean(kap.H*ss*ph/nn)
    ap = s.zeros(n)
    ap[r, r] = -tp
    rr = clean(ap+tp*al.H*al-be.H*be)
    qq = clean(kap*kap.H/nn)
    pp = s.eye(n)-qq
    kk = clean(pp*rr*pp/2+pp*rr*qq)
    mm = clean(z.inv().H*kk)
    eq((kap.H*rr*kap)[0], 0)
    eq(qq*rr*qq, s.zeros(n))
    eq(kk+kk.H, rr)
    eq(qq*kk, s.zeros(n))
    eq(mm[r:r+1, :], s.zeros(1,n))
    xx = s.Matrix.vstack(mm[:r,:], z[:r,:], al, be)
    eq(xx.H*h*xx, ap)
    eq(f.H*h*xx, z)
    y0 = f*z.inv().H[:, :r]
    # The source Hermitian form is linear in the first variable.
    hlin = lambda a,b: clean((a.T*h*b.conjugate())[0])
    yy = s.zeros(2*r+2, r)
    for i in range(r):
        yy[:,i] = clean(y0[:,i]-sum((hlin(y0[:,i],y0[:,j])*xx[:,j]
                                   for j in range(r)), s.zeros(2*r+2,1))/2)
    cc = f*z.adjugate()[r,:].conjugate().T
    p = cc.copy()
    for i in range(r):
        p -= hlin(cc,yy[:,i])*xx[:,i]+hlin(cc,xx[:,i])*yy[:,i]
    p += hlin(cc,xx[:,r])*xx[:,r]/tp
    p = clean(p)
    eq(hlin(p,p), gram/tp)
    vv = clean(ph*p/ssp)
    sig = s.Matrix.hstack(xx[:,:r], yy, xx[:,r:r+1], vv)
    eq(sig.H*h*sig, h)
    eq(sig[:, :r], xx[:,:r])
    fprime = frame(r,tp,tp)
    eq(f.H*h*sig*fprime, z)
    right = clean(sig*fprime*kap)
    left = clean(h.inv()*sig.H*h*cc)
    eq(right[2*r+1], ss*ph)
    eq(left[2*r+1], ssp/s.sympify(ph))
    pair = s.Matrix.hstack(f,xx)
    eq(clean(pair.H*h*pair).det(method="domain-ge"), (-1)**n*gram)
    return sig, gram, ph, ss, ssp


def tau(uu, tz, tp):
    """Original flag action in the (e,e*,z',nu') coordinates."""
    r = uu.rows-1
    aa = uu[:r,:r]
    # z=sqrt(tz/tp) z', so its upper column has this coordinate.
    bb = uu[:r,r:r+1]/s.sqrt(tz/tp)
    dd = aa.H.inv()
    cc = bb*bb.H*dd/(2*tp)
    alpha = bb.H*dd/tp
    ans = s.eye(2*r+2)
    ans[:r,:r], ans[:r,r:2*r] = aa, cc
    ans[r:2*r,r:2*r] = dd
    ans[:r,2*r:2*r+1], ans[2*r:2*r+1,r:2*r] = bb, alpha
    eq(ans.H*form(r,tp)*ans, form(r,tp))
    eq(ans*frame(r,tz,tp), frame(r,tz,tp)*uu)
    return ans


def frame_checks():
    cases = []
    for n in range(1,5):
        for t,tp,last in [(s.Integer(1),s.Integer(1),s.Rational(5,3)),
                          (s.Integer(4),s.Integer(9),s.Integer(10))]:
            patterns = ["diagonal"] + (["reversal","cycle"] if n > 1 else [])
            for pattern in patterns:
                perm = list(range(n)) if pattern == "diagonal" else (
                    list(reversed(range(n))) if pattern == "reversal" else list(range(1,n))+[0])
                pp = s.zeros(n)
                for j,i in enumerate(perm): pp[i,j] = 1
                diag = [s.Integer(i+2)*(3+4*s.I)/5 for i in range(n-1)]+[last]
                ll,uu = s.eye(n),s.eye(n)
                for i in range(n):
                    for j in range(i): ll[i,j] = s.Rational(i+j+1,7)+s.I*s.Rational(i-j,11)
                    for j in range(i+1,n): uu[i,j] = s.Rational(i+j+2,5)-s.I*s.Rational(j-i,13)
                zz = clean(ll*s.diag(*diag)*pp*uu)
                sig,g,ph,ss,ssp = section(zz,t,tp)
                r = n-1
                # A second independent upper pair checks actual flag/frame covariance.
                vl,vr = s.eye(n),s.eye(n)
                for i in range(n-1):
                    vl[i,i+1] = (1+2*s.I)/3
                    vr[i,i+1] = (2-s.I)/5
                left,right = tau(vl,t,tp),tau(vr,tp,tp)
                hh = form(r,tp)
                moved = clean(hh.inv()*left.H*hh*sig*right)
                zm = clean(vl.H*zz*vr)
                ff = frame(r,t,tp); ffp = frame(r,tp,tp); hh = form(r,tp)
                eq(ff.H*hh*moved*ffp,zm)
                eq(zm.det(),zz.det())
                eq(zm[:r,:r].det(),zz[:r,:r].det())
                cr = clean(moved*ffp*zm.adjugate()[:,r])
                cl = clean(hh.inv()*moved.H*hh*ff*zm.adjugate()[r,:].conjugate().T)
                eq(cr[2*r+1],ss*ph);eq(cl[2*r+1],ssp/ph)
                cases.append({"n":n,"T":str(t),"Tprime":str(tp),"pattern":pattern,
                              "top_minor_zero":zz[:r,:r].det()==0,
                              "section_gram_cofactors_and_flag_covariance":"exact PASS"})
        print(json.dumps({"frame_rank":n,"completed_cases":len(cases)}),flush=True)
    return cases


def symbolic_checks():
    # Hermitian paired-frame determinant in unbounded rank is proved in the TeX.
    # These exact instances include arbitrary diagonal-block scaling.
    tt,tt2,aa=s.symbols("T Tprime a",positive=True)
    rows=[]
    for n in range(1,5):
        zz=s.diag(*[s.Integer(i+2) for i in range(n)])
        if n>1: zz[0,n-1]=1+s.I;zz[n-1,0]=2-s.I
        ee=s.zeros(n);ee[n-1,n-1]=1
        pair=(-aa*tt*ee).row_join(zz).col_join(zz.H.row_join(-aa*tt2*ee))
        target=(-1)**n*(zz.det()*s.conjugate(zz.det())-
                    aa**2*tt*tt2*zz[:-1,:-1].det()*s.conjugate(zz[:-1,:-1].det()))
        eq(pair.det(),target);rows.append(n)
    # Rescaling either kernel Haar measure cancels its disintegration constant.
    c,d,a,b=s.symbols("c d a b",positive=True)
    eq((c/a)*(d/b)*a*b,c*d)
    x,y=s.symbols("x y",real=True)
    eq(s.re((-2*s.I)*s.conjugate(x+s.I*y)),s.re(2*s.I*(x+s.I*y)))
    eq(-s.re((-2*s.I)*(x+s.I*y)),s.re(2*s.I*(x+s.I*y)))
    return {"paired_gram_symbolic_scaling_ranks":rows,
            "haar_rescaling_and_both_original_character_signs":"symbolic PASS"}


def main():
    p=argparse.ArgumentParser();p.add_argument("--offline",action="store_true");a=p.parse_args()
    src=sources(a.offline)
    checks={"actual_frame_cases":frame_checks(),"symbolic":symbolic_checks()}
    paths=[f"paper/shared/{STEM}.tex",f"paper/shared/{STEM}-references.tex",
           f"notes/{STEM}.md",f"scripts/check_{STEM.replace('-','_')}.py"]
    cert={"status":"PASS","classification":"closed local supplier, independently reviewed",
          "claim":"Original PhiZero and DensC for compact coefficients, every relevant head",
          "source_commit":REV,"sources":src,"checks":checks,
          "files":[{"path":x,"sha256":sha((ROOT/x).read_bytes())} for x in paths],
          "proof_scope":"Unbounded-rank human algebra, paired-frame properness, exact Haar and quotient comparison are in shared TeX; finite exact checks are diagnostics only.",
          "not_claimed":["HeadTop","uniform kernel estimate","W06/W08 completion","Lean build"]}
    (ROOT/"certificates"/(STEM+".json")).write_text(json.dumps(cert,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"status":"PASS","sources":len(src),"actual_frame_cases":len(checks['actual_frame_cases']),"symbolic":checks['symbolic']}))


if __name__=="__main__":main()
