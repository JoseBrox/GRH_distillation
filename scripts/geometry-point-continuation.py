#!/usr/bin/env python3
"""Authenticate the actual selected-eigenlattice application.

The mathematical proof is in the shared TeX. Source-byte and exact scalar
checks do not prove that result or the still open Hodge--Tate specialization.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen
import sympy as s
from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
AS = "Development.AutomorphicSpectrum."
WB = "Development.WeilBound.CoreStatements.PlurisubharmonicCones."
RANGES = {
    AS+"Proofs.GeometryProofs.PhiDegFibLatLeOfIsOFamilyOfIsAdapted":
        [(20,71),(73,124)],
    AS+"Proofs.GeometryProofs.AbelianPartLieSignature": [(18,28)],
    WB+"HeightComparisonGlobalModel": [(21,60),(91,164),(176,238)],
    WB+"AbelianPartIntegralPointBis": [(21,66),(90,120)],
    WB+"NormBound": [(90,135)],
    AS+"Proofs.GeometryProofs.CuspHeightUpper": [(120,145),(146,223)],
    AS+"PublishedTheorems.Algebra₂.FarguesHodgeTate": [(10,20)],
    AS+"Proofs.GeometryProofs.PointHTOfFarguesHodgeTate": [(50,64)],
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--offline",action="store_true")
    args=ap.parse_args()
    packed=(ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inv=json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert digest(packed)==inv["compressed_graph"]["sha256"]
    atlas=json.loads(gzip.decompress(packed))
    assert atlas["repository"]=="jsmorph/rh" and atlas["commit"]==REV
    blobs={r[0]:r[1] for r in atlas["modules"]}
    sources=[]
    for module,ranges in RANGES.items():
        path="lean/src/"+module.replace(".","/")+".lean"
        rec=inspect_file(dict(repository="jsmorph/rh",commit=REV,
                             path=path,git_blob_sha1=blobs[module]),args.offline)
        lines=(ROOT/"build/source-cache/jsmorph/rh"/REV/path).read_bytes().splitlines(keepends=True)
        excerpts=[]
        for a,b in ranges:
            assert 1<=a<=b<=len(lines) and b-a<120
            data=b"".join(lines[a-1:b])
            assert len(data)<=12000
            excerpts.append(dict(lines=[a,b],sha256=digest(data)))
        sources.append(dict(module=module,**{k:rec[k] for k in
            ["path","git_blob_sha1","sha256","matches_pinned_blob"]},excerpts=excerpts))
    url="https://math.stanford.edu/~conrad/DarmonCM/2011Notes/SemistableReduction.pdf"
    pdf=ROOT/"build/reference-cache/conrad-semistable.pdf"
    if not pdf.is_file():
        if args.offline:
            raise FileNotFoundError(pdf)
        pdf.parent.mkdir(parents=True,exist_ok=True)
        with urlopen(Request(url,headers={"User-Agent":"GRH-distillation/1"}),timeout=45) as response:
            pdf.write_bytes(response.read())
    assert pdf.read_bytes().startswith(b"%PDF-")
    # These checks record exact signs and ranks, including both selected halves.
    p,q,r,f,pe,ld,lr,delta,nu,T=s.symbols("p q r f pe ld lr delta nu T",real=True)
    checked=[]
    for m in [p,q]:
        a=m-r
        b=p+q-m-r
        corrected=(a-b)*pe/2+b*(ld-lr)
        frame_sum=b*(ld-lr)
        assert s.expand(corrected-frame_sum-(2*m-p-q)*pe/2)==0
        g=f*(p+q-2*r)
        R=f*(m-r)
        assert s.expand(2*R-g-f*(2*m-p-q))==0
        signed=f*(2*m-p-q)*pe/2
        dV=2*T-signed+delta+2*nu
        assert s.expand(-dV-(signed-delta-2*nu-2*T))==0
        checked.append(str(m))
    # Independent toric edge cases: signatures and selected ranks, not a
    # numerical approximation to a transcendental inequality.
    rank_cases=0
    for pp in range(9):
        for qq in range(9):
            for rr in range(min(pp,qq)+1):
                for mm in [pp,qq]:
                    gg=pp+qq-2*rr
                    assert 0<=mm-rr<=gg
                    assert abs(2*mm-pp-qq)<=gg
                    rank_cases+=1
    artifacts=[]
    for path in ["paper/shared/geometry-point-continuation.tex",
                 "notes/geometry-point-continuation.md",
                 "scripts/geometry-point-continuation.py"]:
        data=(ROOT/path).read_bytes()
        artifacts.append(dict(path=path,sha256=digest(data)))
    cert=dict(claim="Actual conjugate-eigenlattice application: source authenticity and exact scalar verification",
        classification="closed obligation within W10; no whole-node completion",
        pinned_repository="jsmorph/rh",pinned_revision=REV,
        sources=sources,reference=dict(url=url,sha256=digest(pdf.read_bytes()),
            inspected="Theorem 4.4 and Corollary 4.5, printed pages 10-11: semistable identity-component and base-change comparison"),
        exact_checks=dict(selected_halves=checked,rank_edge_cases=rank_cases,
            finite_correction="The normalized integral-frame logarithmic norm subtracts the full finite flat correction",
            retained_indices="d_V=2T-b+delta+2nu"),artifacts=artifacts,
        limits=["No Lean compilation or kernel audit.",
                "No verification by finite computation of the general geometric proof.",
                "No construction of the corrected Hodge--Tate fibre lattice or all-point height floor.",
                "Prior construction proofs are used with their stated hypotheses; their historical checks are not rerun."])
    out=ROOT/"certificates/geometry-point-continuation.json"
    out.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps(dict(source_files=len(sources),rank_edge_cases=rank_cases,
                          output=str(out.relative_to(ROOT)))))


if __name__=="__main__":
    main()
