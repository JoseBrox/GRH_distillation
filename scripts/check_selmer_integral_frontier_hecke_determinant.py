#!/usr/bin/env python3
"""Authenticate the actual Hecke determinant and check its normalizations.

The mathematical proof is in the note. This script checks exact pinned
interfaces, primary-PDF provenance, and universal polynomial identities.
It is not a Lean build or a proof of the whole W04 obligation.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
import urllib.request

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
DENSE = "ModularityArgument.ThresholdArguments.DenseThresholdCases."
RANGES = {
    BASE+"WeilGroupCharacters.ContinuousResP": [(73, 92), (111, 130)],
    BASE+"WeilGroupCharacters.UniversalOrdinaryDeterminantRing": [
        (80, 103), (109, 176)],
    BASE+"HeckeAlgebras.IsTheta": [(40, 52), (100, 143), (147, 168)],
    BASE+DENSE+"UnitaryHeckeData": [(18, 67)],
    BASE+DENSE+"TCoreSep": [(37, 65)],
    BASE+DENSE+"HeckeOperatorPreservesPart": [(308, 336)],
    BASE+DENSE+"TCoreDet": [
        (42, 96), (191, 250), (251, 280), (291, 323)],
    BASE+DENSE+"OrdCoreH": [(20, 61)],
    BASE+DENSE+"LocOrdFlag": [(116, 169)],
    BASE+"ModularityArgument.AutomorphyLifting.GalUnitaryT": [
        (18, 50), (74, 95)],
    BASE+DENSE+"ExistsOrdinaryCharactersHeckeAlgebra": [(15, 74)],
    BASE+DENSE+"HeckeDeterminantReductionEqResidual": [(15, 35)],
    BASE+DENSE+"HeckeDeterminantSatisfiesDeformationRelations": [(15, 35)],
    BASE+DENSE+"HidaLevelX": [(62, 79), (115, 143)],
    BASE+DENSE+"PaLevel": [(24, 57)],
    BASE+DENSE+"NonemptyUnitaryHeckeParts": [(30, 84)],
    BASE+DENSE+"PTypeEx": [(29, 71), (88, 136)],
    BASE+DENSE+"TTypeEx": [(18, 21)],
    "Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange."
    "ArchimedeanBaseChangeProof.BaseChangeIsobaricNOf": [(18, 45)],
    BASE+"AlgebraTools.DeterminantRepresentations.GlueRep": [(19, 24)],
}

PRIMARY = [
    {
        "file": "bz1977.pdf",
        "url": "https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/BZ-induced-1.pdf",
        "sha256": "b379d3cb70d0fb94d9efbddd5f39a576bd2dc2b43a3f5bdc78f4ef084db10eda",
        "reference": "Bernstein-Zelevinsky, Induced representations I (1977)",
        "reviewed": "Proposition 2.3, printed p.446; geometric lemma 2.12, p.448; support and Theorem 4.2, p.454.",
        "use": "Jacquet adjunction/admissibility, Weyl filtration, uniqueness of support, and principal-series irreducibility.",
    },
    {
        "file": "labesse-cbcm.pdf",
        "url": "https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf",
        "sha256": "5df9d8fcfa158064fe362d4fdf46858648991eb32dddabc63a4a998840785865",
        "reference": "Labesse, Changement de base CM et series discretes (2011)",
        "reviewed": "Author pp.41-43: degree >=2, property (*), and Corollary 5.3.",
        "use": "Definite weight-zero base change with all discrete CSD blocks; exact split/unramified comparison and infinitesimal character.",
        "hypotheses": "Original F has degree >=2 because original CM L/F is unramified at all finite places; compact infinity gives discrete series and (*). Corollary 5.3 imposes no extra finite-place quasi-split or parity assumption.",
    },
    {
        "file": "moeglin-waldspurger1989.pdf",
        "url": "https://www.numdam.org/item/10.24033/asens.1595.pdf",
        "sha256": "a46e3549d05d2cd39f396ef326840f4484f3935ff3daa17e6339091962de9e94",
        "reference": "Moeglin-Waldspurger, Le spectre residuel de GL(n) (1989)",
        "reviewed": "Main theorem, printed pp.605-606; normalized induction, section I.1.1, pp.606-607.",
        "use": "Speh classification; repeated unramified twists would repeat inertial characters at a good ell-place, so every discrete block is cuspidal. Multiple isobaric blocks are retained.",
    },
    {
        "file": "colmez-fontaine2000.pdf",
        "url": "https://webusers.imj-prg.fr/~pierre.colmez/CF.pdf",
        "sha256": "f0b5c51191831415b39cd363cc9eb5ba759d1ea7e46d9b4c1d15cea0a7aa6490",
        "reference": "Colmez-Fontaine, Construction des representations p-adiques semi-stables (2000)",
        "reviewed": "Author section 3.4, pp.21-22; Proposition 4.2, p.23.",
        "use": "Weak admissibility, exact full faithfulness, and stability under subquotients. Rank-one characters have already been constructed, so essential surjectivity is not needed for the flag proof.",
    },
]


def polynomial_checks():
    import sympy as s

    n, j, m = s.symbols("n j m", integer=True)
    identities = {
        "U_successive_ratio": s.expand(
            ((j+1)*(n-j-1)-j*(n-j))/2-((n-1)/2-j)),
        "block_algNorm": s.expand((m-n)/2+(1-m)/2-(1-n)/2),
        "Frobenius_Hecke_exponent": s.expand(
            j*(n-1)/2-j*(n-j)/2-j*(j-1)/2),
        "ordinary_WD_exponent": s.expand((n-1)/2-j+j-(n-1)/2),
    }
    assert all(z == 0 for z in identities.values())
    # Exact universal 3-by-3 check of the primitive-cyclic-word identity.
    # Words of length <=3 on two letters are A,B,AB,AAB,ABB.
    t, u = s.symbols("t u")
    A = s.Matrix(3, 3, s.symbols("a0:9"))
    B = s.Matrix(3, 3, s.symbols("b0:9"))
    left = (s.eye(3)-t*A-u*B).det()
    def truncated_product(p, q):
        result = {}
        for (i, k), a in p.items():
            for (h, v), b in q.items():
                if i+k+h+v <= 3:
                    key = (i+h, k+v)
                    result[key] = result.get(key, 0)+a*b
        return result

    right = {(i, 0): c for i, c in enumerate(A.charpoly().all_coeffs())}
    right = truncated_product(right, {
        (0, i): c for i, c in enumerate(B.charpoly().all_coeffs())})
    for power, coefficient in [
        ((1, 1), -s.trace(A*B)),
        ((2, 1), -s.trace(A*A*B)),
        ((1, 2), -s.trace(A*B*B)),
    ]:
        right = truncated_product(right, {(0, 0): 1, power: coefficient})
    pleft = s.Poly(left, t, u)
    checked = []
    for i in range(4):
        for k in range(4-i):
            delta = s.expand(pleft.coeff_monomial(t**i*u**k)
                             - right.get((i, k), 0))
            assert delta == 0, (i, k)
            checked.append([i, k])
    return {
        "status": "PASS",
        "normalizations": list(identities),
        "normalization_scope": "Identities in the exact rational polynomial ring, with symbolic n,j,m.",
        "Amitsur": {
            "matrices": "Two universal 3x3 matrices over Z[a0,...,a8,b0,...,b8]",
            "primitive_words": ["A", "B", "AB", "AAB", "ABB"],
            "checked_bidegrees": checked,
            "scope": "Exact independent low-rank check; the all-rank integral proof is in note section 6.",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert hashlib.sha256(packed).hexdigest() == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    rows = {row[0]: row for row in atlas["modules"]}
    sources = []
    for module, ranges in RANGES.items():
        item = {
            "repository": atlas["repository"], "commit": atlas["commit"],
            "path": "lean/src/"+module.replace(".", "/")+".lean",
            "git_blob_sha1": rows[module][1],
        }
        checked = inspect_file(item, args.offline)
        cache = ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]
        lines = cache.read_bytes().splitlines(keepends=True)
        excerpts = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines) and end-start+1 <= 120
            data = b"".join(lines[start-1:end])
            assert len(data) <= 12000, (module, start, end, len(data))
            excerpts.append({"start": start, "end": end,
                             "sha256": hashlib.sha256(data).hexdigest()})
        sources.append({**item, "module": module,
                        "sha256": checked["sha256"],
                        "matches_pinned_blob": True,
                        "reviewed_excerpts": excerpts})
    refs = []
    for item in PRIMARY:
        target = ROOT/"build/selmer-determinant-sources"/item["file"]
        if not target.exists():
            if args.offline:
                raise FileNotFoundError(f"Primary PDF missing in offline mode: {target}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(urllib.request.urlopen(item["url"], timeout=60).read())
        data = target.read_bytes()
        assert data.startswith(b"%PDF"), item["file"]
        assert hashlib.sha256(data).hexdigest() == item["sha256"], item["file"]
        refs.append({**item, "bytes": len(data), "local_hash_verified": True})
    stem = "selmer-integral-frontier-hecke-determinant"
    artifacts = [
        f"notes/{stem}.md",
        f"paper/shared/{stem}.tex",
        f"paper/shared/{stem}-references.tex",
        "scripts/check_selmer_integral_frontier_hecke_determinant.py",
    ]
    dependencies = [
        "notes/selmer-integral-frontier-ordinary-diamond.md",
        "certificates/selmer-integral-frontier-ordinary-diamond.json",
        "notes/selmer-integral-frontier-classical-control.md",
        "certificates/selmer-integral-frontier-classical-control.json",
        "notes/classical-galois-substitution.md",
        "notes/galois-period-dictionary.md",
        "notes/classical-local-correspondence.md",
        "notes/local-correspondence-bridge.md",
        "notes/fixed-correspondence-reduction.md",
    ]
    for path in artifacts:
        assert all(c >= 32 or c in (9, 10) for c in (ROOT/path).read_bytes()), path
    report = {
        "schema_version": 1, "status": "PASS",
        "classification": "closed subobligation inside W04 for each original fixed type datum",
        "verification_kind": "Pinned source and primary-PDF provenance, exact symbolic normalization and universal low-rank identity checks; the standard mathematical proof is in the note.",
        "claim": "Actual original ordinary Hecke eigencharacters separate; their actual classical constituents supply Galois representations and ordinary flags; compact integral determinant descent produces the exact surjective B-to-T map and compatible auxiliary classical specialization.",
        "quantifiers": [
            "Every original fixed Hida setting, positive rank n, odd ell, original O, original integral type satisfying TypeForAlt, original torus character and residual Hecke data.",
            "Every original compact auxiliary level; a nonzero residual module has its exact finite Hecke algebra, and a zero module gets its unique action.",
            "Every nonzero vector in the smooth auxiliary union has a detecting good weight-zero classical constituent, retaining all global multiplicities.",
            "Every allowed weak local correspondence and period model is handled by the previously audited guarded comparison transport.",
        ],
        "decisive_interfaces": {
            "Jacquet_scalar_action": {
                "proof": "A kernel vector is killed by compact-unipotent averaging and hence by a power of the actual unnormalized U. Its ordinary inverse makes the map injective. Distinct compact characters give an irreducible principal series and one selected Jacquet line.",
                "normalization": "U_j=q^(j(n-j)/2)*product_(i<j) chi_i(varpi); b_i=U_(i+1)/U_i=q^((n-1)/2-i)*chi_i(varpi).",
                "multiplicity": "Only the local selected Jacquet factor is one dimensional. Every global type multiplicity space is retained.",
            },
            "base_change": {
                "input": "Labesse Corollary 5.3 in its exact definite, degree >=2 scope.",
                "discrete_blocks": "Moeglin-Waldspurger plus distinct unit characters excludes Speh lengths >1; it does not assert that the isobaric sum is cuspidal.",
                "rank_shift": "pi_alpha=Pi_alpha*|det|^((m_alpha-n)/2); algNorm_m(pi_alpha)=Pi_alpha*|det|^((1-n)/2).",
                "polarizing_character": "delta_(L/F)^m_alpha*|.|^(m_alpha-n), with real sign (-1)^m_alpha and delta trivial under norm pullback.",
                "Galois_supplier": "The already adopted W05 theorem applies separately to all regular algebraic polarized cuspidal shifted blocks; take their direct sum.",
            },
            "ordinary_characters": {
                "exact_formula": "psi_i=xi_i*epsilon^(-i), xi_i|units=theta_i^(-1), xi_i(varpi)=U_(i+1)/U_i.",
                "retained_conditions": "Continuity, full residual character, original finite torsion restriction, original inertial weight character, and original cumulative uniformizer products.",
                "cyclotomic_warning": "WD(epsilon) on geometric Frobenius is q^-1; the Galois cyclotomic character on a local uniformizer at ell is not replaced by q^-1.",
                "flag": "Weak admissibility identifies each smallest-Hodge-weight Frobenius line with the already constructed rank-one admissible character; full faithfulness with descent gives the subrepresentation, then induction.",
                "source": "ExistsOrdinaryCharactersHeckeAlgebra:15-74; UniversalOrdinaryDeterminantRing:131-146.",
            },
            "integral_determinant": {
                "compactness": "T is finite over the actual weight ring and embeds continuously as a closed subring of the product over its separating continuous eigencharacters.",
                "density": "The original split Frobenius representatives outside S' are dense; their exact characteristic polynomials put every coefficient tuple in T.",
                "polynomial_law": "The primitive-cyclic-word Amitsur identity descends all finite group-algebra determinants integrally; multiplicativity and naturality are coefficient identities detected by the separating maps.",
                "small_prime_scope": "No use of 1/n!; ell<=n is allowed.",
            },
            "Pair": {
                "fields": ["D", "psi", "cont", "red", "psi.cont/red/mu", "P", "Ord", "I"],
                "ordinary_order": "The rightmost factor lowers the last flag step, so product_(i=0)^(n-1)(rho(g_i)-psi_i(g_i))=0.",
                "type_kernel": "TypeForAlt supplies N=0 and finite diagonal Teichmuller inertia; Ip=Iu intersect all residual character kernels acts trivially.",
                "universality": "Original Pair yields B-to-T; the exact original generator formulas prove surjectivity and weight compatibility.",
            },
            "weak_local_comparison": {
                "guard": "WDT/Gd is toral with zero monodromy; outside the guard one only supplies existence of the actual WD representation.",
                "transport": "The existing full local preimage/uniqueness/injectivity argument identifies any weak guarded parameter with the classical parameter of the same local representation.",
                "scope": "Works for the whole isobaric direct sum and every auxiliary local factor; no genericity or global cuspidality is inferred from distinct inertia.",
                "source": "GalUnitaryT:18-50; PaLevel:24-42.",
            },
        },
        "limitations": [
            "The separate exact integral type-existence supplier TTypeEx/PTypeEx is retained as input and is not identified with W05's depth-zero type law.",
            "No residual module is asserted nonzero.",
            "The original auxiliary level maps with one uniform exponent, full Taylor-Wiles construction, patched support, two-sided rigidity and uniform integral Selmer bounds remain separate.",
            "No whole W04 or other proof-map node is completed.",
            "No Lean project build or complete RH/GRH proof is certified.",
        ],
        "exact_checks": polynomial_checks(),
        "primary_references": refs,
        "dependencies": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
                         for p in dependencies],
        "sources": sources,
        "artifacts": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
                      for p in artifacts],
    }
    target = ROOT/"certificates"/f"{stem}.json"
    target.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "modules": len(sources),
                      "primary_pdfs": len(refs),
                      "certificate": str(target.relative_to(ROOT)),
                      "scope": report["verification_kind"]}))


if __name__ == "__main__":
    main()
