#!/usr/bin/env python3
"""Check arithmetic normalizations used by the integral-minor proof.

The general ideal divisibility, infinite packing sum and operator-product
argument are written proofs. These exact checks do not constitute a Lean
build or prove the remaining fixed-label genus mean.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import random

import sympy as s

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
F = "Formalism.SharpRestriction.CuspSpanNormBounds."
R = "Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts."
P = "Development.AbelianVarietyTheory.Proofs.FlagMeasures."
SOURCES = [
    (F + "FlagEEqHyperbolic", "f2bd94d759cda5036cef38b6093c3b471feb6e17be2f9fb43b33f1bec3b16e08", [[93,120]]),
    (F + "BlockEnds", "c28c1978046dd5717cb64b8e30de695628b5c7f944e2cede36bbd63b3ab9d9cf", [[92,121]]),
    (F + "MinorIntegralityTorus", "591307ec05cd5bae7c3fb5b7c5d671ff16217eadd31fa2eea7c8a32e3357e801", [[110,170]]),
    (F + "KappaEndpoints", "aeaa6920dfd0f47c0bb8f636132307c7fe37fc1bd9bbe0c3cae64974c04ef2b5", [[2905,2916],[2965,2987]]),
    (R + "DimFormC", "66e794f63209a48bcc50261d84aab6a3fb72aa55f9d02fe08ea679dc46d0b7c3", [[42,79]]),
    (R + "KloostermanCosetSumLe", "3209a15a6245185b9fabe353dabd35b6f6e8f50b28bc9a5cc2366a16ad7b0bce", [[150,212]]),
    (R + "RelevantSetZeroGNotIdentity", "6b3dc2644b1ad76b4efa594fa8a3d228137bf10e886e9480463416813a92166b", [[60,146]]),
    (P + "LocalBoundProductOverPlacesLabel", "0e40863afd1866ee8674dbbc4406803df13b2500a97978c8db98a4ec8163533e", [[21,88],[100,146],[154,259]]),
    ("Development.AbelianVarietyTheory.Definitions.SemilocalFrames.PerRowC", "4f0286f8d2a7752d7d3faa5034369ce15434db7c75fa8d9a82d6b49bdff42f78", [[19,45],[56,77]]),
    (P + "DiscNResNeZero", "bf1968d436f07f2965cea329b303b154c3f5b948d8243e2420c4fd05c19b3571", [[312,430]]),
]
ARTIFACTS = [
    "paper/shared/global-gram-continuation-integral-minors.tex",
    "paper/shared/global-gram-continuation-integral-minors-references.tex",
    "notes/global-gram-continuation-integral-minors.md",
    "scripts/global-gram-continuation-integral-minors-check.py",
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def positive_polynomial(expr, variables):
    poly = s.Poly(s.expand(expr), *variables)
    assert all(c >= 0 for c in poly.coeffs()), poly.as_expr()
    return str(poly.as_expr())


def polynomial_reserves():
    t, c = s.symbols("t c", nonnegative=True)
    r = t + 1
    m = 2*r + 2
    # r=t+1, CH=c. All coefficients are nonnegative, so these
    # checks establish the polynomial comparisons for the full range.
    checks = {
        "height_budget": positive_polynomial(
            2*(c+1)*m**2 - 4*r*(1+c*m), (t,c)),
        "label_log_budget": positive_polynomial(
            (17+4*c)*m**2 - (13+4*r+4*c*m*r), (t,c)),
        "original_Cc_budget": positive_polynomial(
            (21+4*c)**2-(17+4*c), (c,)),
        "local_constant_budget": positive_polynomial(
            80*r**4-(16*r**4+32*r**3+8*r**2+8*r+3), (t,)),
        "moment_exponent_budget_after_multiplying_by_r": positive_polynomial(
            80*r**5-(8*r**4+24*r**3+2*r**2+6*r+1), (t,)),
        "minimum_moment": positive_polynomial(
            80*r**5-(16*r**3+4*r+2), (t,)),
        "a_at_least_k_over_two_at_k_5r": positive_polynomial(5*r-2*(r+1),(t,)),
    }
    l, rr = s.symbols("l rr", integer=True)
    e = l*rr-l*(l-1)/2
    assert s.expand(2*e-(2*l*rr-l*(l-1))) == 0
    checks["minor_ideal_exponent"] = "2 a_l = 2lr-l(l-1)"
    return checks


def gaussian_example():
    # O=Z[i], d=(5), r=3. This tests the general star-stable-ideal
    # argument; Q(i)/Q does not satisfy the source's finite-unramified
    # hypothesis, and is not presented as an actual RH field.
    r=3
    J=s.zeros(6)
    J[:3,3:]=s.eye(3)
    J[3:,:3]=s.eye(3)
    wt=s.diag(5**3,5**2,5)
    E=s.eye(6)[:,:3]*wt
    B=s.Matrix([[0,1+s.I],[1-s.I,2]])
    Ep=s.zeros(6,3)
    Ep[3:5,:2]=B*s.diag(5**3,5**2)
    Ep[2,2]=5
    assert E.H*J*E==s.zeros(3)
    assert Ep.H*J*Ep==s.zeros(3)
    assert E.rank()==Ep.rank()==3
    gram=s.simplify(Ep.H*J*E)
    ideals=[]
    for l in range(4):
        e=sum(r-a for a in range(l))
        d=s.expand(gram[:l,:l].det())
        normalized=s.simplify(d/5**(2*e))
        assert s.re(normalized).is_Integer and s.im(normalized).is_Integer
        norm=s.expand(normalized*s.conjugate(normalized))
        assert norm==0 or norm>=1
        ideals.append({"l":l,"a_l":e,"raw_minor":str(d),
                       "minor_divided_by_5_power":str(normalized),
                       "normalized_ideal_norm":str(norm)})
    assert ideals[1]["normalized_ideal_norm"]=="0"
    assert ideals[2]["normalized_ideal_norm"]=="4"
    # Deleting the weighted-lattice hypothesis invalidates normalized
    # norm integrality: delta=1 is integral but not in (5)^(2r).
    false_norm=Fraction(1,25**(2*r))
    assert false_norm<1
    return {"field":"Q(i), an illustrative field for the general ideal lemma only",
            "ideal":"(5)","r":r,"minors":ideals,
            "unweighted_integrality_counterexample_norm":str(false_norm)}


def reciprocal_products():
    rng=random.Random(72961123)
    cases=0
    for f in range(1,6):
        for r in range(1,6):
            for _ in range(8):
                cols=[]
                for l in range(r+1):
                    if l>0 and rng.randrange(4)==0:
                        cols.append([Fraction(0)]*f)
                        continue
                    col=[Fraction(rng.randrange(1,10),rng.randrange(1,10)) for _ in range(f-1)]
                    prod=Fraction(1)
                    for x in col:prod*=x
                    col.append(1/prod)
                    cols.append(col)
                M=Fraction(2)**(2*r)
                left=Fraction(1); S=Fraction(1)
                for v in range(f):
                    left*=max([Fraction(1)]+[1/col[v] for col in cols if col[v]])
                    S*=max([Fraction(1)]+[col[v]/M for col in cols])
                assert left<=M**(f*(r+1))*S**(r+1)
                cases+=1
    return {"exact_rational_cases":cases,
            "zero_columns":"permitted only simultaneously across embeddings",
            "scope":"finite diagnostics of the proved reciprocal-product inequality"}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline",action="store_true")
    args=parser.parse_args()
    packed=(ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory=json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert sha(packed)==inventory["compressed_graph"]["sha256"]
    atlas=json.loads(gzip.decompress(packed))
    assert atlas["repository"]=="jsmorph/rh" and atlas["commit"]==REV
    rows={row[0]:row for row in atlas["modules"]}
    records=[]
    for module,expected,ranges in SOURCES:
        row=rows[module]
        item={"repository":"jsmorph/rh","commit":REV,
              "path":"lean/src/"+module.replace(".","/")+".lean",
              "git_blob_sha1":row[1]}
        record=inspect_file(item,args.offline)
        assert record["sha256"]==expected,(module,record["sha256"])
        records.append({"module":module,"git_blob_sha1":row[1],"sha256":expected,
                        "inspected_ranges":ranges})
    certificate={
        "result":"Exact different-ideal divisibility, normalized label sum and local product",
        "classification":["closed actual arithmetic supplier","stronger field-uniform label bound"],
        "source_repository":"jsmorph/rh","source_revision":REV,
        "source_records":records,
        "polynomial_reserves":polynomial_reserves(),
        "exact_gaussian_example":gaussian_example(),
        "reciprocal_diagnostics":reciprocal_products(),
        "written_proof_labels":["thm:actual-minor-ideal","thm:actual-normalized-minor-sum",
                                "thm:actual-degenerate-product"],
        "artifact_sha256":{p:sha((ROOT/p).read_bytes()) for p in ARTIFACTS},
        "remaining":["fixed-label genus pair count with exact stabilizer weights",
                     "global finite-place and row-mass assembly","complete zero-Gram sum",
                     "generic returns and finite-column sums","final map comparison and positive traces"],
        "verification_scope":"Pinned bytes, exact polynomial reserves and finite arithmetic diagnostics; full ideal, packing and product proofs in TeX. No Lean build or kernel audit. No proof-map node completion.",
    }
    target=ROOT/"certificates/global-gram-continuation-integral-minors.json"
    target.write_text(json.dumps(certificate,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"certificate":str(target.relative_to(ROOT)),"sources":len(records),
                      "polynomial_reserves":len(certificate["polynomial_reserves"]),
                      "rational_diagnostics":certificate["reciprocal_diagnostics"]["exact_rational_cases"],
                      "passed":True}))


if __name__=="__main__":
    main()
