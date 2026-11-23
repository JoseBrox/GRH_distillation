#!/usr/bin/env python3
"""Authenticate the exact finite-decay interface and its algebraic diagnostics.

Finite examples test coordinate identities.  Nonnegative-coefficient
polynomial certificates verify the stated budget for all ranks/word lengths.
The analytic proof is in the accompanying TeX, not certified by finite tests.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s

from check_sources import inspect_file
from check_global_norm_frontier_unitary_density import tau, form, frame

ROOT = Path(__file__).resolve().parents[1]
REPO = "jsmorph/rh"
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
STEM = "global-norm-frontier-finite-decay"
P = "Formalism.HermitianCurvature."
H = P + "HermitianCurvatureProofs."
SOURCES = [
    (P + "RealInputsClosedAdmissibleSettings",
     [(56, 66), (90, 121), (290, 301)]),
    (P + "BigCellVanishingOfCommute", [(61, 106)]),
    (P + "StatementB", [(218, 241)]),
    (P + "StatementD", [(75, 120), (124, 147), (176, 214),
                        (222, 238), (249, 270)]),
    (P + "StatementQ", [(166, 206)]),
    (P + "StatementTop", [(80, 87)]),
    (P + "StatementU", [(28, 44), (63, 128), (171, 187), (391, 411)]),
    (P + "CompositeFormulaLevelZero", [(338, 342)]),
    (H + "SlicesFiniteRegularityBuilt", [(65, 72), (1042, 1114)]),
    (H + "FormLevLimit", [(56, 73), (138, 178)]),
    (H + "PositiveDensityModerateGrowth", [(376, 423)]),
    (H + "MatExtMulVec", [(329, 428)]),
    (H + "UnipotentCoordinatesMeasurePreserving", [(5661, 5768), (5769, 5783)]),
    (H + "ExistsMeasurableSection", [(206, 287), (288, 399), (400, 450)]),
    (H + "FibreIntegralCells", [(25, 51), (61, 132)]),
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
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpt = b"".join(lines[lo-1:hi])
            assert len(excerpt) <= 12288
            excerpts.append({"lines": [lo, hi], "bytes": len(excerpt),
                             "sha256": sha(excerpt)})
        ans.append({"module": module, **{key: rec[key] for key in
                    ["repository", "commit", "path", "bytes", "sha256",
                     "git_blob_sha1", "matches_pinned_blob"]},
                    "excerpts": excerpts})
    return ans


def clean(x):
    return x.applyfunc(s.simplify) if isinstance(x, s.MatrixBase) else s.simplify(x)


def eq(a, b):
    z = s.zeros(*a.shape) if isinstance(a, s.MatrixBase) else 0
    assert clean(a-b) == z


def zmat(n, m, seed=0):
    return s.Matrix(n, m, lambda i, j:
                    s.Rational((3*i+2*j+seed) % 7-3, 3)
                    + s.I*s.Rational((2*i+5*j+seed+1) % 5-2, 4))


def compositions(n):
    if n == 0:
        yield ()
        return
    for a in range(1, n+1):
        for tail in compositions(n-a):
            yield (a,)+tail


def cramer_checks():
    cases = []
    for n in range(1, 6):
        for blocks in compositions(n):
            bounds = [0]
            for z in blocks:
                bounds.append(bounds[-1]+z)
            lb = s.eye(n)
            ub = s.eye(n)
            hh = s.zeros(n)
            for b, size in enumerate(blocks):
                a, e = bounds[b], bounds[b+1]
                for j in range(size):
                    hh[a+j, e-1-j] = s.Rational(b+2,b+1) + s.I/3
                for c in range(b+1, len(blocks)):
                    c0,c1 = bounds[c], bounds[c+1]
                    lb[c0:c1,a:e] = zmat(c1-c0,e-a,b+c+2)
            for i in range(n):
                for j in range(i+1,n):
                    ub[i,j] = zmat(1,1,i+j)[0]
            zz = clean(lb*hh*ub)
            bb = clean(hh*ub)
            for b in range(len(blocks)):
                a,e = bounds[b],bounds[b+1]
                eq(zz[:e,:e].det(),hh[:e,:e].det())
                for c in range(b+1,len(blocks)):
                    c0,c1 = bounds[c],bounds[c+1]
                    got = clean(zz[c0:c1,:e]*zz[:e,:e].inv())[:,a:e]
                    eq(got,lb[c0:c1,a:e])
                for c in range(b,len(blocks)):
                    c0,c1 = bounds[c],bounds[c+1]
                    got = zz[a:e,c0:c1]
                    if a:
                        got = got-zz[a:e,:a]*zz[:a,:a].inv()*zz[:a,c0:c1]
                    eq(got,bb[a:e,c0:c1])
                if a:
                    eq(-zz[a:e,:a]*zz[:a,:a].inv(),lb.inv()[a:e,:a])
            eq(zz.inv()*lb*hh,ub.inv())
            cases.append({"size": n, "blocks": list(blocks)})
    return cases


def radical_checks():
    cases = []
    for j,rho,k in [(1,0,2),(1,1,2),(2,0,2),(2,1,3),(3,0,2)]:
        m=2*rho+k+1
        jj=s.zeros(j)
        for a in range(j): jj[a,j-1-a]=1
        hh=s.diag(*([1]*(m-1)+[-1]))
        xx=zmat(m,j,2)
        yy=zmat(m,j,4)
        kk0=zmat(j,j,5)
        kk1=zmat(j,j,8)
        kk0=kk0-kk0.H
        kk1=kk1-kk1.H
        def radical(x, kk):
            return s.BlockMatrix([[s.eye(j),-jj*x.H*hh,
                                   jj*(-x.H*hh*x/2+kk)],
                                  [s.zeros(m,j),s.eye(m),x],
                                  [s.zeros(j,j),s.zeros(j,m),s.eye(j)]]).as_explicit()
        z=zmat(j,j,7)+5*s.eye(j)
        gam=s.eye(m)
        mid=s.BlockMatrix([[s.zeros(j,j),s.zeros(j,m),z.H.inv()*jj],
                           [s.zeros(m,j),gam,s.zeros(m,j)],
                           [jj*z,s.zeros(j,m),s.zeros(j,j)]]).as_explicit()
        g=clean(radical(xx,kk0).inv()*mid*radical(yy,kk1))
        dd=g[j+m:, :j]
        eq(-g[j:j+m,:j]*dd.inv(),xx)
        eq(-jj*dd.inv()*g[j+m:,j:j+m]*hh.inv(),yy.H)
        eq(-jj*g[:j,:j]*dd.inv()-xx.H*hh*xx/2,kk0)
        eq(jj*dd.inv()*g[j+m:,j+m:]+yy.H*hh*yy/2,kk1)
        eq(g[j:j+m,j:j+m]-g[j:j+m,:j]*dd.inv()*g[j+m:,j:j+m],gam)
        cases.append({"head_size":j,"residual_rank":rho,"k":k})
    return cases


def eichler_checks():
    cases=[]
    for r in range(5):
        for tt,tp in [(s.Integer(1),s.Integer(1)),(s.Integer(4),s.Integer(9))]:
            uu=s.eye(r+1)
            for i in range(r+1):
                for j in range(i+1,r+1): uu[i,j]=zmat(1,1,i+2*j)[0]
            mat=tau(uu,tt,tp)
            hh=form(r,tp)
            eq(mat.H*hh*mat,hh)
            eq(mat*frame(r,tt,tp),frame(r,tt,tp)*uu)
            eq(mat.inv(),hh.inv()*mat.H*hh)
            cases.append({"r":r,"T":str(tt),"Tprime":str(tp)})
    return cases


def positive_projection_checks():
    cases=[]
    jj=s.diag(1,-1)
    phases=[s.Integer(1),s.I,s.Rational(3,5)+s.I*s.Rational(4,5)]
    for t in [s.Rational(1,4),s.Rational(1,3),s.Rational(1,2),s.Rational(2,3)]:
        c=(1+t*t)/(1-t*t)
        u=2*t/(1-t*t)
        for phase in phases:
            v=s.Matrix([c,phase*u])
            aa=clean((v.H*v)[0])
            qq=v/s.sqrt(aa)
            hh=clean(qq.H*jj*qq)
            pp=clean(qq*hh.inv()*qq.H*jj)
            eq(pp*pp,pp)
            eq(pp.H*jj,jj*pp)
            eq(hh[0],1/aa)
            # The nonzero singular value of this rank-one projection is aa.
            eq(s.trace(pp*pp.H),aa**2)
            eq((pp*pp.H).det(),0)
            eq((v.H*jj*v)[0],1)
            cases.append({"boost_parameter":str(t),"phase":str(phase)})
    return cases


def budget_certificates():
    # A nonnegative-coefficient expansion after R=u+1, k=v+2 proves
    # the inequalities for all r>=0, k>=2, N>=0 and b=|Cb|>=0.
    u,v,nn,b=s.symbols("u v N b",nonnegative=True)
    rr=u+1
    dd=2*rr+v+1
    xx=nn*dd**2+dd**3
    mm=5+3*rr*(nn+2)*dd+nn*(rr-1)
    bb=127*rr**3*xx+1
    lower=3*nn*rr**2+6*rr*mm+4*rr*(bb+2*dd**2+1)+1
    top=(b*b+5*b)*rr*nn*dd+64*rr**2*(2*dd**2+1)+1
    statements={
        "derivative_order":8*xx-mm,
        "lower_budget_600":600*rr**4*xx-lower,
        "terminal_budget_200":200*(1+b)**2*rr**4*xx-top,
        "selected_Cc":10000*(1+b)**2*rr**4*xx-lower-top,
        "flag_stripping_degree":9*rr**2-(4*rr*(rr+1)+1),
        "terminal_coordinate_degree":64*rr**2-36*rr**2,
        "pairing_derivative_reserve":mm-(5+dd*nn),
        "pairing_decay_reserve":bb-(2*(v+2+rr-1)*rr+1+2*nn),
    }
    ans=[]
    for name, expression in statements.items():
        poly=s.Poly(s.expand(expression),u,v,nn,b)
        assert all(c>=0 for c in poly.coeffs()),name
        ans.append({"name":name,"variables":[str(z) for z in poly.gens],
                    "nonnegative_coefficients":True,
                    "terms":[{"powers":list(powers),"coefficient":str(c)}
                             for powers,c in poly.terms()]})
    return ans


def fibre_credit_checks():
    cases=0
    for rr in [1,2,7,23]:
        for oo in range(9):
            for input_order in range(oo+1):
                for fibre_order in range(oo-input_order+1):
                    assert 3*rr*fibre_order+2*rr*input_order<=5*rr*oo
                    cases+=1
    return cases


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--offline",action="store_true")
    args=parser.parse_args()
    src=sources(args.offline)
    checks={"block_cramer":cramer_checks(),"radical_inverse":radical_checks(),
            "original_eichler_sections":eichler_checks(),
            "positive_complement_projections":positive_projection_checks(),
            "all_parameter_budget_certificates":budget_certificates(),
            "fibre_derivative_credit_cases":fibre_credit_checks()}
    files=[f"paper/shared/{STEM}.tex",f"paper/shared/{STEM}-references.tex",
           f"notes/{STEM}.md",f"scripts/check_{STEM.replace('-','_')}.py"]
    result={"status":"PASS","classification":"closed exact supplier; independent review recorded separately",
            "interface":"Formalism.FourierDecayAlt.KB.FormLimit",
            "scope":"Original finite decay exponent, cutoff, every level/head and original top-lift hypotheses; no W06/W08 closure.",
            "source_authentication":src,"exact_diagnostics":checks,
            "files":{p:sha((ROOT/p).read_bytes()) for p in files},
            "limitations":["No Lean build or formal verification claim.",
                           "Finite coordinate examples are diagnostics; all-rank identities are proved in the TeX.",
                           "Analytic dominated convergence and the original source-object comparisons require mathematical review.",
                           "TopLiftExists2 and the global arithmetic theta/Gram and rational-return constructions remain separate."]}
    (ROOT/f"certificates/{STEM}.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"PASS","authenticated_modules":len(src),
                      "block_cramer_cases":len(checks["block_cramer"]),
                      "radical_cases":len(checks["radical_inverse"]),
                      "eichler_cases":len(checks["original_eichler_sections"]),
                      "projection_cases":len(checks["positive_complement_projections"]),
                      "all_parameter_budget_certificates":len(checks["all_parameter_budget_certificates"]),
                      "fibre_credit_cases":checks["fibre_derivative_credit_cases"]}))


if __name__=="__main__":
    main()
