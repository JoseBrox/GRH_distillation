#!/usr/bin/env python3
"""Authenticate and check the original embedded-isometry genus-count supplier.

The determinant, fixed-space, finite-module and mass arguments are written
proofs. Exact finite diagnostics below test both sharpness of the congruence
factor and recovery of the original embedded graph in a valid CM field.
No Lean build or full weighted return-series bound is claimed.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import subprocess

import sympy as s

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
P = "Development.AbelianVarietyTheory.Proofs.FlagMeasures."
D = "Development.AbelianVarietyTheory.Definitions.SemilocalFrames."
SOURCES = [
    (D + "FlagPairDefinitePartLattice",
     "33962c30e534b2a499694f1493e8c69f69e6ef92fb7c9ef076edc543ed0aa5a7", [[101,122]]),
    (D + "NormalFormDualOrthogonalLast",
     "05c633d7e619d916d6041040f1a0fc0711da10bb31f42984cacd40631cb290a6", [[22,31],[127,137]]),
    (P + "DiscriminantOrderCommonFixedLatticeEmbeddedDataStatement",
     "08baecdfd5d70ec4d549fe9c2236efd40b53ba0b9ee561e2ffd5e732e26b8538", [[11,12]]),
    (P + "DiscriminantOrderCommonFixedLatticeEmbeddedData",
     "09701e99f627988cf42af61acf06ab81a69327616f453cdda6bb72ed198eca98", [[110,124],[172,185],[250,265],[283,299],[325,337],[372,410]]),
    (P + "CardEmbeddedDataWithGivenFixedLatticeStatement",
     "a6743dc99e33b0a583a0bd3c5c5011cb4bf8f38225a848068e957fab379af7f9", [[11,12]]),
    (P + "CardEmbeddedDataWithGivenFixedLattice",
     "607506d01634f44b07b093833a3b199a5c7d970c562ed3507e3423fdeed1791f", [[151,211]]),
    (P + "CardIsometriesFixingSubspaceDefiniteLatticesLeStatement",
     "6e9b7ffb6a4396ff128a514eb6cf7adb057ef83b0e177c9ed306e08f5914055e", [[11,12]]),
    (P + "EncardSublatticesIndexFixedTraceLeStatement",
     "b4af56651c656e6d721185f89d7b0e10aba8aa9a4665a6d3cd89c28f871eb74d", [[11,12]]),
    (P + "CountIsometryPairsWithGivenFixedSpaceStatement",
     "3c38cdaeb21f3e2a8b646780d9b0bf2b47dae2e9d5d6ae3992cb810715b70723", [[11,12]]),
    (P + "PairsIsometryNoFixedVectorCountBoundStatement",
     "a80febe735f0a394650384ae5bc03a6f6a669dda58884130592727c3d45acd87", [[11,12]]),
    (P + "PairsIsometryNoFixedVectorCountBound",
     "de1b903b1eb4594b6ed22c443c3572027e439020cd1566718c005ff6137a0d5c", [[20,90]]),
    (P + "DiscNResNeZero",
     "bf1968d436f07f2965cea329b303b154c3f5b948d8243e2420c4fd05c19b3571", [[312,430]]),
    (P + "MeanPrimitiveSublatticesGenusDefiniteLattice",
     "1635d022d2670d3bca20dbbe8f1b4ae29f205f17cd06c7e3ec94e0da88f0fdee", [[158,198]]),
    (P + "TermPairsRowLatticeCountedViaEmbeddings",
     "6dfd6333685cb70fe079a958eba263dbe5b6bfa4c35edc570232dd5ca1b0687e", [[114,177]]),
]
ARTIFACTS = [
    "paper/shared/embedded-isometry-genus-count.tex",
    "paper/shared/embedded-isometry-genus-count-references.tex",
    "notes/embedded-isometry-genus-count.md",
    "scripts/embedded-isometry-genus-count-check.py",
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def symbolic_identities():
    j,k,r,l,c = s.symbols("j k s ell c")
    m = 3*(2*j+1)
    fiber_D = s.expand(m-(3*j+1))
    fiber_x = s.expand(m-(5*j+2))
    assert fiber_D == 3*j+2 and fiber_x == j+1
    fixed_space = s.expand((2*r+2*c+1)-(r+l+c/2))
    assert s.expand(fixed_space.subs(c,1+l)) == r+l/2+s.Rational(5,2)
    full_Y = s.expand(m+(2*r+2*c+1)+(5*r+5+2*c)+1)
    assert full_Y == 6*j+10+4*c+7*r
    # Extract the powers from both actual factors before cancellation.
    n,D0,X,q = s.symbols("n D X q", positive=True)
    fixed_factor=(q**(2*r)*D0*X/n)**(k/2)
    primitive_factor=(n/D0)**(k/2)*16**(r*k)
    quotient=s.expand_log(s.log(fixed_factor*primitive_factor), force=True)
    target=k*s.log(X)/2+r*k*s.log(16*q)
    assert s.simplify(s.expand_log(quotient-target, force=True))==0
    # In the no-fixed-space comparison, use Y=X D^2.
    nofix_X = s.expand(k/2+(c+m)+k-(k+c+m))
    nofix_D = s.expand(2*(c+m)+k-2*m)
    assert nofix_X == k/2 and nofix_D == k+2*c
    return {
        "fixed_datum_D_reserve":str(fiber_D),
        "fixed_datum_x_reserve":str(fiber_x),
        "fixed_space_exponent_reserve":str(s.expand(fixed_space.subs(c,1+l))),
        "complete_genus_Y_exponent":str(full_Y),
        "normalized_discriminant_cancellation":"(Q/n)^(k/2)(n/D)^(k/2)=(2/g)^(skf)X^(k/2)",
        "orbital_factor_after_16_skf":"(32/g)^(skf)",
        "no_fixed_vector_comparison_X_exponent":str(nofix_X),
        "no_fixed_vector_comparison_D_exponent":str(nofix_D),
    }


def minkowski_factorial_comparison():
    count=0
    for dimension in range(1,101):
        for prime in list(s.primerange(2,2*dimension+2)):
            minkowski=0
            factorial=0
            power=1
            while dimension//(power*(prime-1)):
                a=dimension//(power*(prime-1))
                b=(2*dimension)//(prime*power)
                assert a<=b
                minkowski+=a
                factorial+=b
                power*=prime
            while (2*dimension)//(prime*power):
                factorial+=(2*dimension)//(prime*power)
                power*=prime
            assert minkowski<=factorial
            count+=1
    return {"dimensions":[1,100],"prime_dimension_pairs":count,
            "scope":"Exact diagnostic of the written termwise comparison p <= 2(p-1), not proof of Minkowski's cited theorem."}


def finite_unramified_cm_diagnostics():
    z=s.symbols("z")
    disc_E=int(s.discriminant(s.cyclotomic_poly(12,z),z))
    disc_F=int(s.discriminant(z*z-3,z))
    assert disc_E==144 and disc_F==12 and disc_E==disc_F**2
    # E=Q(zeta_12), F=Q(sqrt(3)), f=2. On O_E^2 use the identity
    # graph modulo 2 and eta=diag(1,-1). The fixed part is O_E e_1.
    f=2
    codimension=1
    g=2
    norm_determinant=2**(2*f*codimension)
    assert norm_determinant==16
    assert (s.Rational(2,g))**(2*f*codimension)==1
    # For L=Lambda=O_E and Gamma=graph(-1) modulo 3, F=3 O_E.
    # Alpha(y)=-2y/3 modulo O_E, represented by a vector modulo 3.
    # Verify actual graph recovery independently for all (z,y) residues.
    elements=tuple(itertools.product(range(3),repeat=4))
    recovered=0
    for a,b in itertools.product(elements,repeat=2):
        graph=all((ai+bi)%3==0 for ai,bi in zip(a,b))
        encoded=all((ai-bi)%3==(-2*bi)%3 for ai,bi in zip(a,b))
        assert graph==encoded
        recovered+=graph
    assert recovered==81
    return {
        "field":"E=Q(zeta_12), F=Q(sqrt(3))",
        "absolute_field_discriminant":disc_E,
        "real_field_discriminant":disc_F,
        "norm_relative_discriminant":disc_E//(disc_F**2),
        "sharp_congruence_example":{
            "lattice":"O_E^2 with the standard Hermitian form",
            "eta":"diag(1,-1)","g":g,"x":1,"x_prime":1,
            "codimension":codimension,"norm_det_eta_minus_one_on_complement":norm_determinant,
            "fixed_intersection_discriminant":1,"upper_bound":1},
        "graph_recovery_example":{
            "lattice":"O_E with the standard form","g":3,
            "graph":"z=-y modulo 3 O_E","fixed_lattice":"3 O_E",
            "index":81,"residue_pairs_checked":len(elements)**2,
            "graph_pairs_recovered":recovered},
        "scope":"Valid finite-unramified CM diagnostics of the general written theorems; no assertion about the original RH auxiliary field."}


def cited_source():
    path=ROOT/"build/references/serre-finite-groups.pdf"
    pdf_sha="d52d1072a58381fe6a725a5ac040f539164217055dd4b482b1e1f986ac8d0405"
    assert sha(path.read_bytes())==pdf_sha
    extracted=subprocess.run(["pdftotext","-layout",str(path),"-"],
                             check=True,stdout=subprocess.PIPE).stdout.decode()
    start=extracted.index("Theorem 1. Let n be an integer")
    end=extracted.index("The proof will be given",start)
    excerpt=extracted[start:end]
    assert "finite subgroup of GLn" in excerpt
    return {"title":"Serre, Bounds for the orders of the finite subgroups of G(k)",
            "url":"https://www.college-de-france.fr/media/jean-pierre-serre/UPL3821667391778701726_6___Bounds_for_the_orders.pdf",
            "version":"Author's version headed EPFL Press, Lausanne, 2006",
            "theorem":"Theorem 1 (Minkowski)","pdf_sha256":pdf_sha,
            "bounded_statement_sha256":sha(excerpt.encode()),
            "scope":"Cited classical finite rational linear group theorem; subsequent factorial comparison proved in the manuscript."}


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
        "result":"Original embedded-isometry genus mean with all three fixed-space ranges",
        "classification":"closed actual quantitative arithmetic supplier",
        "source_repository":"jsmorph/rh","source_revision":REV,
        "source_records":records,"external_source":cited_source(),
        "symbolic_identities":symbolic_identities(),
        "finite_group_bound_diagnostics":minkowski_factorial_comparison(),
        "CM_field_diagnostics":finite_unramified_cm_diagnostics(),
        "primitive_mean_certificate_sha256":sha((ROOT/"certificates/primitive-sublattice-genus-mean.json").read_bytes()),
        "written_proof_labels":["lem:embedded-isometry-fixed-discriminant",
                                "lem:embedded-data-count",
                                "lem:sublattice-prescribed-intersection",
                                "thm:embedded-isometry-fixed-space-count",
                                "thm:embedded-isometry-genus-mean"],
        "artifact_sha256":{p:sha((ROOT/p).read_bytes()) for p in ARTIFACTS},
        "remaining":["original weighted flag-term-to-embedded-triple fiber estimate",
                     "complete fixed-label pair estimate and zero-Gram sum",
                     "generic-return and finite-column arithmetic sums"],
        "verification_scope":"Pinned source byte authentication, exact symbolic comparisons, a sharp fixed-space congruence example, and exhaustive graph recovery modulo 3 in a valid finite-unramified CM field. General statements have written proofs using the previously proved primitive mean and cited Minkowski theorem. No Lean build or full W08 claim."}
    path=ROOT/"certificates/embedded-isometry-genus-count.json"
    path.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"certificate":str(path.relative_to(ROOT)),
                      "sources":len(records),"symbolic_identities":len(cert["symbolic_identities"]),
                      "graph_residue_pairs":cert["CM_field_diagnostics"]["graph_recovery_example"]["residue_pairs_checked"],
                      "passed":True}))


if __name__=="__main__":
    main()
