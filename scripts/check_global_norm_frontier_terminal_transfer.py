#!/usr/bin/env python3
"""Exact diagnostics for the actual terminal lift; no Lean build claim."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import sympy as s
from check_sources import inspect_file

ROOT=Path(__file__).resolve().parents[1]
REPO="jsmorph/rh"
REV="ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
STEM="global-norm-frontier-terminal-transfer"
SOURCES=[
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.CutEXMkTopCut",[(13,25)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.CutMK2",[(16,74)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.CutMKTop",[(17,50)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.CutEXMkTop",[(74,120),(178,251)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.CutEXMkTopBump",[(62,98)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.CutEX2",[(20,91),(93,114)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.CutEXAsm",[(119,222),(223,323),(324,425),(426,478)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.ExistsCompactCutoffCoefficient",[(25,57),(76,108)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.FrameTransportToLastLevel",[(11,67)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.FnValLift",[(40,80),(119,154)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.InvMemOfKappa",[(28,63)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.CutFP",[(12,25),(34,91)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.HeadTopOfRadialExhaustion",[(12,42),(48,62)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.TopUnipotentIntegralPositive",[(11,38)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.ThetaCompactSupport",[(81,130)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.HeadWeightAtOfExists",[(96,169)]),
 ("Formalism.HermitianCurvature.StatementTop",[(14,31),(80,87)]),
 ("Formalism.HermitianCurvature.StatementQ",[(956,978)]),
 ("Formalism.HermitianCurvature.StatementFr",[(219,235)]),
 ("Formalism.HermitianCurvature.StatementD",[(259,270)]),
 ("Formalism.HermitianCurvature.CompositeFormulaLevelZero",[(89,110)]),
 ("Formalism.HermitianCurvature.StatementM",[(224,229)]),
 ("Formalism.HermitianCurvature.RealInputsClosedAdmissibleSettings",[(14,16),(83,121),(228,243)]),
]


def sha(b):return hashlib.sha256(b).hexdigest()


def sources(offline):
    packed=(ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inv=json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert sha(packed)==inv["compressed_graph"]["sha256"]
    atlas=json.loads(gzip.decompress(packed));assert (atlas["repository"],atlas["commit"])==(REPO,REV)
    blobs={x[0]:x[1] for x in atlas["modules"]};ans=[]
    for module,ranges in SOURCES:
        path="lean/src/"+module.replace(".","/")+".lean"
        rec=inspect_file({"repository":REPO,"commit":REV,"path":path,"git_blob_sha1":blobs[module]},offline)
        assert rec["matches_pinned_blob"]
        lines=(ROOT/"build/source-cache"/REPO/REV/path).read_bytes().splitlines(keepends=True)
        chunks=[]
        for lo,hi in ranges:
            assert 1<=lo<=hi<=len(lines) and hi-lo<120
            text=b"".join(lines[lo-1:hi]);assert len(text)<=12288
            chunks.append({"lines":[lo,hi],"bytes":len(text),"sha256":sha(text)})
        ans.append({"module":module,**{k:rec[k] for k in ["repository","commit","path","bytes","sha256","git_blob_sha1","matches_pinned_blob"]},"excerpts":chunks})
    return ans


def clean(x):return x.applyfunc(s.simplify) if isinstance(x,s.MatrixBase) else s.simplify(x)
def eq(a,b):assert clean(a-b)==(s.zeros(*a.shape) if isinstance(a,s.MatrixBase) else 0)


def qr(z):
    n=z.rows
    q=s.zeros(n);rr=s.zeros(n)
    for j in range(n):
        v=z[:,j]
        for i in range(j):
            rr[i,j]=clean((q[:,i].H*v)[0]);v=clean(v-q[:,i]*rr[i,j])
        rr[j,j]=s.sqrt(clean((v.H*v)[0]));assert rr[j,j]>0
        q[:,j]=clean(v/rr[j,j])
    aa=s.diag(*[rr[i,i] for i in range(n)])
    return q,aa,clean(aa.inv()*rr)


def qr_checks():
    results=[]
    for n in range(1,7):
        q=s.eye(n)
        for i in range(n-1):
            rot=s.eye(n);rot[i,i]=rot[i+1,i+1]=s.Rational(3,5)
            rot[i,i+1]=-s.Rational(4,5)*s.I;rot[i+1,i]=-s.Rational(4,5)*s.I
            q=clean(q*rot)
        eq(q.H*q,s.eye(n))
        aa=s.diag(*[s.Rational(i+2,i+1) for i in range(n)])
        uu,v=s.eye(n),s.eye(n)
        for i in range(n):
            for j in range(i+1,n):
                uu[i,j]=s.Rational(i+j+1,3)+s.I*s.Rational(j-i,7)
                v[i,j]=s.Rational(2*i+j+1,5)-s.I*s.Rational(j+1,11)
        z=clean(q*aa*uu)
        q1,a1,u1=qr(z);q2,a2,u2=qr(clean(z*v))
        eq(q1,q);eq(a1,aa);eq(u1,uu)
        eq(q2,q);eq(a2,aa);eq(u2,clean(uu*v))
        results.append({"rank":n,"unitary_Q_positive_A_upper_U_and_right_covariance":"exact PASS"})
    # Dimension-zero QR and its zero-dimensional Haar factor.
    eq(s.eye(0).det(),1)
    return results


def interpolation_checks():
    x=s.Symbol("x");rows=[]
    for vals in [[2],[2,2],[-2,0,3],[-2,-2,0,3,5],[1,2,3,4,5,6]]:
        nodes=sorted(set(vals));p=s.interpolate([(a,s.Rational(1,a) if a else 0) for a in nodes],x)
        for a in vals:eq(p.subs(x,a),s.Rational(1,a) if a else 0)
        n=len(vals);u=s.eye(n)
        for i in range(n-1):u[i,i+1]=1+s.I
        aa=u*s.diag(*vals)*u.inv()
        pp=s.Poly(p,x);evalp=s.zeros(n)
        for (power,),coef in pp.terms():evalp+=coef*aa**power
        eq(evalp,u*s.diag(*[s.Rational(1,a) if a else 0 for a in vals])*u.inv())
        rows.append({"eigenvalues":vals,"degree":s.degree(p,x),"matrix_identity":"exact PASS"})
    return rows


def compositions(n):
    if n==0:return [()]
    return [(a,)+b for a in range(1,n+1) for b in compositions(n-a)]


def head_checks():
    x,y,tt=s.symbols("x y TT",real=True);z=x+s.I*y
    cases=[]
    for r in range(6):
        for blocks in compositions(r):
            mats=[]
            for j,b in enumerate(blocks):
                mats.append((j+2+s.I)*s.Matrix(b,b,lambda i,k:int(i+k==b-1)))
            head=s.diag(*mats) if mats else s.eye(0)
            big=s.diag(head,s.Matrix([[z]]))
            den=clean(big.det()*s.conjugate(big.det())-tt*head.det()*s.conjugate(head.det()))
            eq(den,head.det()*s.conjugate(head.det())*(x*x+y*y-tt))
            eq(clean(big.det()*s.conjugate(big.det())/den),(x*x+y*y)/(x*x+y*y-tt))
            cases.append({"head_size":r,"blocks":list(blocks)})
    # Both original nonzero bump integrals cancel in the compact lift.
    l,rr,a=s.symbols("kappa_L kappa_R A",nonzero=True)
    eq(l*rr*(a/(l*rr)),a)
    return cases


def hs_checks():
    rows=[]
    for n in range(1,6):
        v=s.Matrix(n,3,lambda i,j:s.Rational(i+2*j+1,3)+s.I*s.Rational(2*i-j,5))
        w=s.Matrix(n,3,lambda i,j:s.Rational(2*i+j,7)-s.I*s.Rational(i+j+1,2))
        weights=s.symbols(f"a0:{n}",real=True)
        dd=s.diag(*weights)
        lhs=s.trace((dd*v).H*w)
        rhs=0
        for i,a in enumerate(weights):
            ee=s.zeros(n);ee[i,i]=1
            rhs+=a*s.trace((ee*v).H*(ee*w))
        eq(lhs,rhs);rows.append(n)
    return rows


def main():
    p=argparse.ArgumentParser();p.add_argument("--offline",action="store_true");args=p.parse_args()
    src=sources(args.offline)
    checks={"QR":qr_checks(),"finite_spectral_inverse":interpolation_checks(),
            "all_block_heads_through_size_five":head_checks(),"weighted_HS_ranks":hs_checks()}
    paths=[f"paper/shared/{STEM}.tex",f"paper/shared/{STEM}-references.tex",f"notes/{STEM}.md",f"scripts/check_{STEM.replace('-','_')}.py"]
    cert={"status":"PASS","classification":"closed local supplier, independently reviewed",
          "claim":"Original compact top-lift and HeadTop under the unchanged place/operator/admissible-word hypotheses",
          "source_commit":REV,"sources":src,"checks":checks,
          "files":[{"path":f,"sha256":sha((ROOT/f).read_bytes())} for f in paths],
          "proof_scope":"The human proof gives unbounded-rank QR compactness, nonzero bump integrals, operator locality, exact disintegration and every-head transfer. Finite exact diagnostics do not replace these arguments.",
          "not_claimed":["arithmetic place construction","original Theta supplier","uniform differential bound construction","full kernel estimate","W06/W08 completion","Lean build"]}
    # SymPy degree is a symbolic Integer even in these exact rational tests.
    for row in checks["finite_spectral_inverse"]:row["degree"]=int(row["degree"])
    (ROOT/"certificates"/(STEM+".json")).write_text(json.dumps(cert,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"status":"PASS","sources":len(src),"QR_ranks":len(checks['QR']),
                      "spectral_cases":len(checks['finite_spectral_inverse']),
                      "heads":len(checks['all_block_heads_through_size_five']),"HS_ranks":len(checks['weighted_HS_ranks'])}))


if __name__=="__main__":main()
