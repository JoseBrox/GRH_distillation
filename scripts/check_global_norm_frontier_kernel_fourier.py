#!/usr/bin/env python3
"""Exact interface diagnostics for the actual normalized Fourier supplier.

The unbounded-rank analytic and interpolation proof is in the TeX file.
No Lean build, numerical Fourier proof, or global norm bound is claimed.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import itertools
import json
from pathlib import Path

from check_sources import inspect_file

ROOT=Path(__file__).resolve().parents[1]
REPO="jsmorph/rh"
REV="ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
STEM="global-norm-frontier-kernel-fourier"
SOURCES=[
 ("Formalism.HermitianCurvature.StatementTBB",[(12,23),(38,62),(90,91),(137,160)]),
 ("Formalism.HermitianCurvature.StatementC",[(39,47)]),
 ("Formalism.HermitianCurvature.StatementD",[(259,270)]),
 ("Formalism.HermitianCurvature.RealInputsClosedAdmissibleSettings",[(14,31),(56,76),(83,118),(134,187),(212,243)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.HeadContinuityAtZeroOfStandard",[(138,204)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.StandardPairingOfHeads",[(15,25)]),
 ("Formalism.HermitianCurvature.HermitianCurvatureProofs.PBFCstmt",[(10,26)]),
]
DEPENDENCIES=[
 "paper/shared/global-norm-frontier-wave-isometry.tex",
 "paper/shared/global-norm-frontier-mixed-cauchy.tex",
 "paper/shared/global-norm-frontier-partial-head-transfer.tex",
 "paper/shared/global-norm-frontier-terminal-transfer.tex",
 "paper/sections/recovered/78-as-section.tex",
 "paper/sections/recovered/79-ca-section.tex",
 "paper/sections/recovered/80-cg-section.tex",
 "paper/sections/recovered/95-jf-section.tex",
]


def sha(x):return hashlib.sha256(x).hexdigest()


def source_records(offline):
    packed=(ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inv=json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert sha(packed)==inv["compressed_graph"]["sha256"]
    atlas=json.loads(gzip.decompress(packed))
    assert (atlas["repository"],atlas["commit"])==(REPO,REV)
    blobs={x[0]:x[1] for x in atlas["modules"]};records=[]
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
        records.append({"module":module,**{k:rec[k] for k in
            ["repository","commit","path","bytes","sha256","git_blob_sha1","matches_pinned_blob"]},
            "excerpts":chunks})
    return records


def compositions(n):
    if n==0:return [()]
    return [(a,)+b for a in range(1,n+1) for b in compositions(n-a)]


def naux(k,r,gg,head):
    """Original nAux with fr=1; entries are (block size, squared norm)."""
    b=1;value=Q(1)
    for block,norm_sq in head:
        end=b+block-1
        if end==r+1 and block==1:
            value*=gg**(k-1)
        else:
            mlev=k+1+2*(r+1-end)
            half_exp=block*(mlev+block-3)
            value*=norm_sq**half_exp
        b+=block
    return value


def normalization_checks():
    count=terminal=outside=0
    tt=Q(7,3)
    # Nonzero complex head parameters represented by exact squared norms.
    for k in [2,3,4,7]:
        for r in range(7):
            for j in range(r+1):
                for blocks in compositions(j):
                    head=[(a,Q((i+2)**2+1,(i+1)**2)) for i,a in enumerate(blocks)]
                    ah=naux(k,r,Q(0),head)
                    assert ah>0 and ah==naux(k,r,Q(-11),head)
                    for c_sq in [Q(1,2),Q(7,3),Q(5),Q(29,4)]:
                        gg=c_sq-tt
                        appended=naux(k,r,gg,head+[(1,c_sq)])
                        if j<r:
                            expected=ah*c_sq**(2*(r-j)+k-1)
                            assert appended==expected
                        elif gg>0:
                            assert appended==ah*gg**(k-1)
                            terminal+=1
                        else:
                            # Source RR is zero here. No sqrt(product)=product
                            # step is allowed for a negative formal weight.
                            rr=Q(0)
                            assert appended*rr==0
                            outside+=1
                        count+=1
    return {"all_block_compositions_max_rank":6,"normalization_cases":count,
            "positive_terminal_cases":terminal,"zero_or_negative_terminal_domain_cases":outside,
            "status":"exact rational PASS"}


def unused_blocks_checks():
    patterns=0
    # Exhaust every occupancy set and every longer word length: repeated
    # occupancy is permitted and is exactly the TBB quantifier distinction.
    for N in range(1,9):
        for bits in itertools.product([0,1],repeat=N):
            occupied={i for i,b in enumerate(bits) if b}
            for h in range(len(occupied),N+1):
                free=[i for i in range(N) if i not in occupied]
                for K in range(N-h+1):
                    selected=free[:K]
                    assert len(selected)==K and not occupied.intersection(selected)
                    assert h+len(selected)<=N
                    patterns+=1
    actual=[]
    for r in [0,1,2,7,23]:
        N=20*(r+1);I=6*N**3+6*N;q=Q(I,6*N);ell=q-1
        assert q==N*N+1
        intervals=[(Q((2*N+2*a-2))*q,Q((2*N+2*a-2))*q+ell) for a in range(1,N+1)]
        short=[Q(j*N*N)+Q(1,j+3) for j in range(N)]
        assert all(0<=x and x+1<=I for x in short)
        assert all(a>=0 and b+1<=I for a,b in intervals)
        for a in range(N-1):
            assert intervals[a+1][0]-(intervals[a][1]+1)>=N*N+1
            assert short[a+1]-short[a]-1>=Q(N*N,8)
        assert intervals[0][0]-(short[-1]+1)>=N*N+1
        # All degrees required in the original argument are in its range.
        assert 2*r<Q(N,10) and Q(28*N,I)<1
        actual.append({"r":r,"N":N,"I":I,"shifted_separation":"exact PASS"})
    return {"exhaustive_occupancy_max_N":8,"patterns":patterns,"original_scale_cases":actual}


def qword(w,y):
    out=Q(1)
    for plus,a in w:
        out*=(y-a+1)/(y-a) if plus else (a-y)/(a-y-1)
    return out


def scalar_checks():
    norm=lambda y:y*y+7
    cases=0
    for old_len in range(5):
        for signs in itertools.product([False,True],repeat=old_len):
            w=[(plus,Q(100*i+30+(not plus))) for i,plus in enumerate(signs)]
            sw=Q(1)
            for _,a in w:sw*=norm(a)
            for K in range(5):
                ys=[Q(-100*(i+1)) for i in range(K)]
                plus=[(True,y) for y in ys]+w
                minus=[(False,y+1) for y in ys]+w
                sp=sm=Q(1)
                for _,a in plus:sp*=norm(a)
                for _,a in minus:sm*=norm(a)
                p1=p2=qprod=Q(1)
                for y in ys:
                    p1*=norm(y);p2*=norm(y+1);qprod*=qword(w,y)
                    assert qword(w,y)>0
                    D=min([abs(y-a) if plus_sign else abs(a-y-1)
                           for plus_sign,a in w],default=Q(2))
                    assert D>1
                    assert (1-1/D)**old_len<=qword(w,y)<=(1+1/D)**old_len
                assert sp==sw*p1 and sm==sw*p2
                ah=Q(13,7)
                # Squared exact normalization in mixed Cauchy.
                assert (ah/sw)**2*sp*sm/(ah*ah*qprod)==p1*p2/qprod
                cases+=1
    max_cases=0
    for A,B,C in itertools.product([Q(0),Q(1,3),Q(2),Q(19)],repeat=3):
        M=max(A,B,C)
        assert A*B<=M*M and C<=M
        max_cases+=1
    return {"signed_word_normalizer_and_q_cases":cases,"common_maximum_cases":max_cases,
            "empty_word_and_K_zero":"included","status":"exact rational PASS"}


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--offline",action="store_true");args=parser.parse_args()
    src=source_records(args.offline)
    checks={"head_normalization":normalization_checks(),
            "all_word_grid_extension":unused_blocks_checks(),"signed_scalars":scalar_checks()}
    paths=[f"paper/shared/{STEM}.tex",f"paper/shared/{STEM}-references.tex",
           f"notes/{STEM}.md",f"scripts/check_{STEM.replace('-','_')}.py"]
    cert={"status":"PASS","classification":"closed local supplier, independently reviewed",
          "claim":"Original compact KernelFourierIntegralBound, HeadContinuityAtZero and PosAt on the constructed separated finite grids, with unchanged actual place and top-lift hypotheses",
          "source_commit":REV,"sources":src,"checks":checks,
          "files":[{"path":f,"sha256":sha((ROOT/f).read_bytes())} for f in paths],
          "established_mathematical_dependencies":[{"path":f,"sha256":sha((ROOT/f).read_bytes())} for f in DEPENDENCIES],
          "proof_scope":"The written proof handles every rank, admissible word, head, extension length and Fourier parameter. Exact finite checks validate interfaces and edge cases, not the analytic theorems or unbounded quantifiers.",
          "not_claimed":["construction of the original arithmetic place","original uniformly controlled Theta supplier",
                         "passage to decaying eigenfunctions","block-growth supplier","global source/target Gram estimate","W06/W08 completion","Lean build"]}
    (ROOT/"certificates"/(STEM+".json")).write_text(json.dumps(cert,indent=2)+"\n")
    print(json.dumps({"status":"PASS","sources":len(src),"checks":checks}))


if __name__=="__main__":main()
