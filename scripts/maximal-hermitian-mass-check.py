#!/usr/bin/env python3
"""Authenticate the maximal Hermitian mass source and its local normalization.

The global mass theorem is cited. The local structure has a written proof.
These exact counts check a genuinely nonunimodular dyadic local density;
they are not a proof of the general mass theorem or of the genus pair count.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import urllib.request

import sympy as s

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PDF_URL = "https://www.math.uni-bielefeld.de/~mkirschm/papers/herm.pdf"
PDF_SHA = "aef562cc9ea0cfcd7d82a6e325a3885c3527d367811eb39a8e8e7d544596e183"
P = "Development.AbelianVarietyTheory.Proofs.FlagMeasures."
SOURCES = [
    ("Development.AbelianVarietyTheory.PublishedTheorems.DiscreteSeriesUnitary₂.MaxMass",
     "7905d9f425626b6ba573f4e91610480233b95a09f24d08cf48688ba102cf8b0e", [[10,14]]),
    ("Development.AbelianVarietyTheory.Definitions.SemilocalFrames.ChartGen",
     "f9871c7d06667b73eb651a356b80d8edcffd368cf6971923b200c1d9d4046325", [[104,137]]),
    (P+"MaximalHermitianLatticeMassRatio",
     "9b309769132d0beb5bf6c59c954d4f987430e234ab9fb1dacc7cda285c16d62c", [[31,117]]),
    (P+"TermPairCountBoundOfSiegelMassRatios",
     "0d43b29bbeabb78957704d9e8d09ae1d2e652ba48b85ca20193642fa30127754", [[70,163]]),
    (P+"MeanPrimitiveSublatticesGenusDefiniteLattice",
     "1635d022d2670d3bca20dbbe8f1b4ae29f205f17cd06c7e3ec94e0da88f0fdee", [[158,200]]),
    (P+"MassGenusCyclicDiscriminantSplitPrimeStatement",
     "c9822751472a7095141f394e17df0d8a3f3487620a9192bdfef3425caad4d2c1", [[9,10]]),
    (P+"CyclicDiscriminantLatticesFormOneGenusStatement",
     "5ff5a44c32c82403853ebd7084afc222e2a688396e58f1f027a2e730b15d8637", [[9,10]]),
    (P+"MassIntegralLatticesDiscriminantOrderLeStatement",
     "667fb27cf89b299c85367d0a7d5323867ab088400af179033b528bc27ff2f461", [[9,10]]),
]
ARTIFACTS = [
    "paper/shared/maximal-hermitian-mass.tex",
    "paper/shared/maximal-hermitian-mass-references.tex",
    "notes/maximal-hermitian-mass.md",
    "scripts/maximal-hermitian-mass-check.py",
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def external_source(offline: bool):
    path = ROOT/"build/references/kirschmer-herm.pdf"
    if not path.exists():
        if offline:
            raise FileNotFoundError("The external PDF is not cached; rerun without --offline.")
        path.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(PDF_URL, timeout=30) as response:
            path.write_bytes(response.read())
    assert sha(path.read_bytes()) == PDF_SHA
    extracted = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"],
        check=True, stdout=subprocess.PIPE).stdout.decode()
    pieces = [
        ("Definition 3.5.1", "In Section 3.3"),
        ("Theorem 4.2.3 (Siegel)", "Theorem 4.2.4 In"),
        ("Theorem 4.2.4 In", "If p is bad,"),
    ]
    records = []
    for start, stop in pieces:
        a = extracted.index(start)
        b = extracted.index(stop, a)
        excerpt = extracted[a:b]
        assert 200 <= len(excerpt) <= 10000
        records.append({"start": start, "end_before": stop,
                        "extracted_utf8_bytes": len(excerpt.encode()),
                        "sha256": sha(excerpt.encode())})
    return {"url": PDF_URL, "sha256": PDF_SHA,
            "bytes": path.stat().st_size,
            "bounded_excerpts": records,
            "scope": "Cited classical mass and local density theorems; no new proof of these external theorems."}


def local_factor_identity():
    q, t, epsilon = s.symbols("q t epsilon", nonzero=True)
    # Here t=q^n and epsilon=(-1)^n. Standard density differs from
    # rank n-1 by 1-epsilon/t; dual index q^2 contributes t.
    result = s.factor(t*(1-epsilon/t)/(q+1))
    assert s.simplify(result-(t-epsilon)/(q+1)) == 0
    evaluated=[]
    for q0 in (2,3,4,5,7,8,9):
        for n in range(1,9):
            for eta in (-1,1):
                b=Fraction(1)
                for a in range(1,n):
                    b *= 1-Fraction(eta**a,q0**a)
                beta_bad=(q0-eta)*b
                beta_standard=b*(1-Fraction(eta**n,q0**n))
                correction=q0**n*beta_standard/beta_bad
                assert correction==Fraction(q0**n-eta**n,q0-eta)
                evaluated.append([q0,n,eta,str(correction)])
    return {"symbolic_identity":str(result),
            "rational_cases":evaluated}


def dyadic_density():
    records=[]
    for level in (1,2,3):
        m=2**level
        # The unramified quadratic extension of Z_2:
        # B/(2^level)=Z/(2^level)[w]/(w^2+w+1).
        elements=[(a,b) for b in range(m) for a in range(m)]
        size=len(elements)
        norm=[(a*a-a*b+b*b)%m for a,b in elements]
        conjugate=[((a-b)%m)+m*((-b)%m) for a,b in elements]
        multiply=[[0]*size for _ in range(size)]
        for i,(a,b) in enumerate(elements):
            for j,(c,d) in enumerate(elements):
                multiply[i][j]=(a*c-b*d)%m+m*((a*d+b*c-b*d)%m)
        for last_diagonal in (1,2):
            first=[(a,c) for a in range(size) for c in range(size)
                   if (norm[a]+last_diagonal*norm[c])%m==1]
            second=[(b,d) for b in range(size) for d in range(size)
                    if (norm[b]+last_diagonal*norm[d])%m==last_diagonal%m]
            count=0
            for a,c in first:
                for b,d in second:
                    x=elements[multiply[conjugate[a]][b]]
                    y=elements[multiply[conjugate[c]][d]]
                    if ((x[0]+last_diagonal*y[0])%m==0
                        and (x[1]+last_diagonal*y[1])%m==0):
                        count+=1
            density=Fraction(count,2**(4*level))
            expected=(Fraction(9,8) if last_diagonal==1 else
                      Fraction(3) if level==1 else Fraction(9,2))
            assert density==expected
            records.append({"residue_cardinality":2,"rank":2,
                            "Gram_diagonal":[1,last_diagonal],
                            "level":level,"congruence_isometries":count,
                            "normalized_count":str(density)})
    return {"ring":"Z/2^N Z[w]/(w^2+w+1), conjugation w -> -1-w",
            "counts":records,
            "caution":"For Gram diag(1,2), level 1 gives 3, while levels 2 and 3 give the correct stabilized value 9/2.",
            "scope":"Exact finite diagnostics, not an assertion that these cases prove stabilization in general."}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args=parser.parse_args()
    packed=(ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory=json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert sha(packed)==inventory["compressed_graph"]["sha256"]
    atlas=json.loads(gzip.decompress(packed))
    assert atlas["repository"]=="jsmorph/rh" and atlas["commit"]==REV
    rows={row[0]:row for row in atlas["modules"]}
    records=[]
    for module,expected,ranges in SOURCES:
        item={"repository":"jsmorph/rh","commit":REV,
              "path":"lean/src/"+module.replace(".","/")+".lean",
              "git_blob_sha1":rows[module][1]}
        record=inspect_file(item,args.offline)
        assert record["sha256"]==expected,(module,record["sha256"])
        records.append({"module":module,"sha256":expected,
                        "git_blob_sha1":rows[module][1],
                        "inspected_ranges":ranges})
    cert={
        "result":"Exact maximal integral Hermitian mass and cyclic-discriminant genus normalization",
        "classification":"closed actual arithmetic mass supplier",
        "source_repository":"jsmorph/rh","source_revision":REV,
        "source_records":records,
        "external_mass_theorem":external_source(args.offline),
        "local_factor":local_factor_identity(),
        "dyadic_density":dyadic_density(),
        "written_proof_labels":["thm:maximal-hermitian-mass","cor:cyclic-discriminant-mass",
                                "thm:integral-lattice-fixed-discriminant-mass"],
        "artifact_sha256":{p:sha((ROOT/p).read_bytes()) for p in ARTIFACTS},
        "remaining":["uniform primitive-sublattice genus mean",
                     "fixed-space isometry counts",
                     "actual weighted row-to-lattice correspondence",
                     "complete fixed-label pair bound and zero-Gram sum"],
        "verification_scope":"Authenticated pinned source and external PDF; symbolic local factor and exact small dyadic congruence counts. Local structure has a written proof; global mass formula is cited. No Lean build, no proof-map node completion.",
    }
    path=ROOT/"certificates/maximal-hermitian-mass.json"
    path.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"certificate":str(path.relative_to(ROOT)),
                      "sources":len(records),"dyadic_counts":len(cert["dyadic_density"]["counts"]),
                      "passed":True}))


if __name__=="__main__":
    main()
