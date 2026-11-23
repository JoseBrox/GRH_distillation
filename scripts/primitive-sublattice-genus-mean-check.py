#!/usr/bin/env python3
"""Check the actual primitive-sublattice genus-mean interfaces and identities.

General finite-module, ideal-count, mass, and weighted graph arguments
are written proofs. The finite module here checks a nonsemisimple case.
No Lean build or final return-sum proof is claimed.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import subprocess

import sympy as s

from check_sources import inspect_file

ROOT=Path(__file__).resolve().parents[1]
REV="ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
P="Development.AbelianVarietyTheory.Proofs.FlagMeasures."
SOURCES=[
    (P+"MassIntegralLatticesDiscriminantOrderLeStatement",
     "667fb27cf89b299c85367d0a7d5323867ab088400af179033b528bc27ff2f461", [[9,10]]),
    (P+"FewOrbitsSubspacesHermitianLatticeDiscriminantStatement",
     "c82b30e9454ac337c7280357ee434ca61d5e0794d04c68c6ec64b5a11c70346e", [[9,10]]),
    (P+"OrbitStabilizerMassSubspaceCyclicDiscriminantLeStatement",
     "0464db8d3b21bce73faf2c32d88a378e01931bf9df5775aa39c7b2c52cfc482e", [[9,10]]),
    (P+"PrimitiveSublatticeMeanCountBoundStatement",
     "67f9131c55c343db6cc67ba51c67f7c6d8ff24e7c0a6a1fe5218de319873ad17", [[9,10]]),
    (P+"PrimitiveSublatticeMeanCountBound",
     "04ee3656f662d82c2c3659f48842c4ec409451a066e05b71f0e9e12af9e2f773", [[139,214]]),
    (P+"MeanPrimitiveSublatticesGenusDefiniteLattice",
     "1635d022d2670d3bca20dbbe8f1b4ae29f205f17cd06c7e3ec94e0da88f0fdee", [[158,198]]),
    (P+"UnimodularHermitianMassMulLeMassStatement",
     "82d5d801bf23a51116fe085dbe0ad3a1dae935cd958e7870508d505c2e89fc86", [[11,12]]),
    ("Formalism.HermitianLattices.StatementMass",
     "ddcd9f431c350be9c1b40e38ffe734153cf5401c9a10c84dc388574c9775a3d1", [[20,42]]),
    ("Development.AbelianVarietyTheory.Definitions.SemilocalFrames.NormalFormDualOrthogonalLast",
     "05c633d7e619d916d6041040f1a0fc0711da10bb31f42984cacd40631cb290a6", [[22,31]]),
]
ARTIFACTS=[
    "paper/shared/primitive-sublattice-genus-mean.tex",
    "paper/shared/primitive-sublattice-genus-mean-references.tex",
    "notes/primitive-sublattice-genus-mean.md",
    "scripts/primitive-sublattice-genus-mean-check.py",
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def identities():
    j,r,l=s.symbols("j r l")
    k=j+r
    rho_power=s.expand((j*j+r*r-k*k-1)/2)
    pi_power=s.expand((k*(k+1)-j*(j+1)-r*(r+1))/2+1)
    assert s.expand(rho_power+j*r+s.Rational(1,2))==0
    assert s.expand(pi_power-j*r-1)==0
    extra_n=1+l+l/2+r
    extra_x=1+(r+l)/2+r
    assert s.expand(extra_n+extra_x-(5*r+4+4*l)/2)==0
    target=(9*r+8+4*l)/2
    assert s.expand(target-(extra_n+extra_x))==2*r+2
    source_c=1+l
    desired=5*r+5+2*source_c
    norm_n=s.expand(k/2+desired-((k-r)/2+target))
    norm_d=s.expand(-k/2+desired-(-(k-1)/2+target))
    assert norm_n==r+3
    assert norm_d==(r+5)/2
    x,y=s.symbols("x y",nonnegative=True)
    reserve=s.expand((4*r*k+1-(3*j*r+3+2*r)).subs({j:x+1,r:y+1}))
    assert all(c>=0 for c in s.Poly(reserve,x,y).coeffs())
    return {"mass_rho_power":str(rho_power),
            "mass_two_pi_power":str(pi_power),
            "raw_mean_exponent_reserve":str(2*r+2),
            "rank_mass_power_of_two_reserve_after_j=x+1_s=y+1":str(reserve),
            "normalized_n_exponent_reserve":str(norm_n),
            "normalized_D0_exponent_reserve":str(norm_d)}


def nonsemisimple_module():
    # Every additive subgroup of (Z/4Z)^2 is a Z/4Z-submodule.
    mod=4
    elements=tuple(itertools.product(range(mod),repeat=2))
    zero=(0,0)
    def add(x,y):
        return tuple((a+b)%mod for a,b in zip(x,y))
    def scale(a,x):
        return tuple((a*b)%mod for b in x)
    def extend(H,g):
        return frozenset(add(h,scale(a,g)) for h in H for a in range(mod))
    all_subgroups={frozenset([zero])}
    queue=list(all_subgroups)
    while queue:
        H=queue.pop()
        for g in elements:
            K=extend(H,g)
            if K not in all_subgroups:
                all_subgroups.add(K)
                queue.append(K)
    # Independent enumeration by ordered pairs of generators.
    by_pairs=Counter()
    for a,b in itertools.product(elements,repeat=2):
        by_pairs[extend(extend(frozenset([zero]),a),b)]+=1
    assert set(by_pairs)==all_subgroups
    assert len(all_subgroups)<=len(elements)**2
    assert sum(by_pairs.values())==len(elements)**2
    orders=Counter(len(H) for H in all_subgroups)
    return {"module":"(Z/4Z)^2",
            "submodules":len(all_subgroups),
            "submodules_by_order":dict(sorted(orders.items())),
            "ordered_pairs_of_generators":sum(by_pairs.values()),
            "all_submodules_generated_by_two":True,
            "scope":"Exact finite nonsemisimple diagnostic, not proof of the general Dedekind-module theorem."}


def submodule_index_counts():
    checked=[]
    for q in (2,3,4,5):
        for a in range(1,7):
            coeff=[1]+[0]*6
            for i in range(a):
                for e in range(1,7):
                    coeff[e]+=q**i*coeff[e-1]
            for e,value in enumerate(coeff):
                assert value<=q**(a*e)
            checked.append({"residue_size":q,"rank":a,"colengths_0_through_6":coeff})
    return checked


def cited_sources():
    path=ROOT/"build/references/kirschmer-herm.pdf"
    pdf_sha="aef562cc9ea0cfcd7d82a6e325a3885c3527d367811eb39a8e8e7d544596e183"
    assert sha(path.read_bytes())==pdf_sha
    extracted=subprocess.run(["pdftotext","-layout",str(path),"-"],
                             check=True,stdout=subprocess.PIPE).stdout.decode()
    a=extracted.index("Theorem 2.4.1 (Local-Global Principle)")
    b=extracted.index("In particular, the classification",a)
    excerpt=extracted[a:b]
    return [
        {"title":"Kirschmer, Definite quadratic and hermitian forms with small class number",
         "url":"https://www.math.uni-bielefeld.de/~mkirschm/papers/herm.pdf",
         "pdf_sha256":pdf_sha,"theorem":"2.4.1, printed page 20",
         "bounded_excerpt_sha256":sha(excerpt.encode()),
         "scope":"Cited Hermitian local-to-global principle."},
        {"title":"Milne, Algebraic Number Theory",
         "url":"https://www.jmilne.org/math/CourseNotes/ANT.pdf",
         "version":"3.08, 19 July 2020",
         "theorems":["4.3, printed page 70 (Minkowski ideal-class representatives)",
                     "5.1, printed page 85 (Dirichlet units)"],
         "scope":"Statements verified through the primary author's PDF via web retrieval; no local PDF byte hash asserted."},
    ]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline",action="store_true")
    args=parser.parse_args()
    packed=(ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inv=json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert sha(packed)==inv["compressed_graph"]["sha256"]
    atlas=json.loads(gzip.decompress(packed))
    assert atlas["repository"]=="jsmorph/rh" and atlas["commit"]==REV
    rows={r[0]:r for r in atlas["modules"]}
    records=[]
    for module,expected,ranges in SOURCES:
        item={"repository":"jsmorph/rh","commit":REV,
              "path":"lean/src/"+module.replace(".","/")+".lean",
              "git_blob_sha1":rows[module][1]}
        record=inspect_file(item,args.offline)
        assert record["sha256"]==expected
        records.append({"module":module,"sha256":expected,
                        "git_blob_sha1":rows[module][1],"inspected_ranges":ranges})
    cert={
        "result":"Original normalized primitive-sublattice genus mean",
        "classification":"closed actual quantitative arithmetic supplier",
        "source_repository":"jsmorph/rh","source_revision":REV,
        "source_records":records,
        "external_sources":cited_sources(),
        "symbolic_identities":identities(),
        "finite_module":nonsemisimple_module(),
        "local_index_count_diagnostics":submodule_index_counts(),
        "mass_certificate_sha256":sha((ROOT/"certificates/maximal-hermitian-mass.json").read_bytes()),
        "written_proof_labels":["thm:primitive-sublattice-genus-mean",
                                "thm:normalized-primitive-sublattice-genus-mean"],
        "artifact_sha256":{p:sha((ROOT/p).read_bytes()) for p in ARTIFACTS},
        "remaining":["isometries with prescribed fixed space",
                     "pairs of isometries with no fixed vector",
                     "original weighted row-to-lattice correspondence",
                     "full fixed-label pair bound and zero-Gram sum"],
        "verification_scope":"Pinned source bytes, exact symbolic comparisons and finite nonsemisimple-module diagnostics. General arguments are written proofs using cited classical theorems. No Lean build, no complete W08 claim.",
    }
    path=ROOT/"certificates/primitive-sublattice-genus-mean.json"
    path.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"certificate":str(path.relative_to(ROOT)),
                      "sources":len(records),"symbolic_identities":len(cert["symbolic_identities"]),
                      "finite_submodules":cert["finite_module"]["submodules"],
                      "passed":True}))


if __name__=="__main__":
    main()
