#!/usr/bin/env python3
"""Bind the actual full ordinary-family proof to its source interfaces.

Finite exact diagnostics check normalizations, integral projection and local
inertia elimination.  They do not replace the universal mathematical proof.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import urllib.request

import sympy as sp
from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
HA = BASE+"HeckeAlgebras."
BR = BASE+"BuildingsResidueChars."
DT = BASE+"ModularityArgument.ThresholdArguments.DenseThresholdCases."
RANGES = {
    BASE+"WeilGroupCharacters.ArithmeticPointClassicality":
        [(14, 37), (65, 119), (125, 144)],
    BASE+"WeilGroupCharacters.LocCFTAll": [(19, 23)],
    HA+"ContinuousTorusCharacter": [(269, 354)],
    HA+"CoefficientRepTrivialOnUnramified": [(230, 275)],
    HA+"TcAnti": [(69, 112)],
    HA+"OrdinaryHeckeCharacters.IndexNeZero": [(378, 415)],
    HA+"OrdinaryHeckeCharacters.CtrlEq": [(4, 47)],
    HA+"OrdinaryHeckeCharacters.CtrlOrd":
        [(41, 110), (111, 229), (230, 348), (349, 371)],
    BR+"ExistsAutomorphicFormWithPrescribedIwahoriValues": [(30, 106)],
    BR+"ExistsIntegralFormLiftingControlMap": [(18, 100)],
    BR+"ClassicalFormsLevelMonotoneAndUpStable": [(8, 67)],
    BR+"UpOperatorMapsLatticeOfControlValues": [(8, 63)],
    DT+"TJRing": [(47, 136), (137, 189)],
    DT+"TJDense": [(23, 50)],
    DT+"PointTheoremBaseObject": [(26, 48)],
    DT+"THidaU": [(38, 48)],
    DT+"UnifVal": [(68, 97)],
    BASE+"AutomorphicForms.BlochKatoSelmerVanishes": [(69, 85)],
    BASE+"PadicHodgeTheory.EpsArt": [(27, 42)],
    "Development.AbelianVarietyTheory.PublishedTheorems.AutomorphicForms₂.ExistsUniqueHcharOfFiniteOrder": [(50, 60)],
}

PRIMARY = [
    {"file": "build/selmer-determinant-sources/labesse-cbcm.pdf",
     "text_file": "build/selmer-determinant-sources/labesse-cbcm.txt",
     "url": "https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf",
     "sha256": "5df9d8fcfa158064fe362d4fdf46858648991eb32dddabc63a4a998840785865",
     "text_sha256": "d7f112703f8a72e80f13a32cb0f60ee7fb29ddb423012b82534902a4f29ef30d",
     "text_ranges": [(1900, 1964)], "printed_pages": [42, 43],
     "interface": "Corollary 5.3: every discrete-series constituent of the actual compact-at-infinity unitary group satisfies (*); degree F>=2 is retained. Base change is a sum of discrete CSD blocks, with matching infinity infinitesimal character and split/unramified local comparison. This is not a cuspidality assertion for the whole sum."},
    {"file": "build/selmer-determinant-sources/moeglin-waldspurger1989.pdf",
     "text_file": "build/selmer-determinant-sources/moeglin-waldspurger1989.txt",
     "url": "https://www.numdam.org/item/10.24033/asens.1595.pdf",
     "sha256": "a46e3549d05d2cd39f396ef326840f4484f3935ff3daa17e6339091962de9e94",
     "text_sha256": "46c21e3355ffcc774bb07addb6264ed66264c0a799b5afc660bf33acaa33b319",
     "text_ranges": [(40, 121)], "printed_pages": [605, 606, 607],
     "interface": "Discrete GL blocks are Speh(tau,m), with unitary cuspidal tau and normalized exponents (m-1)/2-j. All original ranks and Speh lengths remain in the arithmetic-point decomposition, including nongood points."},
    {"file": "build/selmer-pt-sources/blggt-potential.pdf",
     "text_file": "build/selmer-pt-sources/blggt-potential.txt",
     "url": "https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n2-p03-p.pdf",
     "sha256": "c9d6c7107bcde7fb26f9388abea5209f28457076bae59d70ccb6c34bbe1d621b",
     "text_sha256": "dedd0f1c1f71d44973e91c19317ea23d11470ca4a02ce2d39807f16d4770bcea",
     "text_ranges": [(1925, 1978)], "printed_pages": [538, 539],
     "interface": "Theorem 2.1.1 applies to each pi_a=tau_a|det|^((d_a+m_a-n-1)/2), verified regular algebraic and polarized with the correct real sign. It gives continuous semisimple Galois representations, exact away-from-ell normalization and purity. Pure weight n-1 is deduced only when every m_a=1; the source FrobEig includes unramifiedness."},
    {"file": "build/reference-cache/milne-cft.pdf",
     "text_file": "build/reference-cache/milne-cft.txt",
     "url": "https://www.jmilne.org/math/CourseNotes/CFT.pdf",
     "sha256": "50d79af78250a9f1117ad9d337e0b231704a533fc707966ed1bfa52e13d498f5",
     "text_sha256": "5f9250521f173b47423192f8c1b2fe05b9b38329522454f0bf93ee96cfa6547a",
     "text_ranges": [(1305, 1360), (3790, 3838), (9716, 9807)],
     "printed_pages": [20, 21, 67, 178, 179],
     "interface": "Local reciprocity, Hilbert 90 and global idele reciprocity. The proof explicitly inverts arithmetic reciprocity to match the pinned geometric convention v(art g)=-deg(g); finite-character avatars have no algebraic correction."},
]


def rank_mod(matrix, p):
    rows = [[int(x) % p for x in row] for row in matrix]
    rank = 0
    for j in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][j]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][j], -1, p)
        rows[rank] = [(inverse*x) % p for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank:
                factor = rows[i][j]
                rows[i] = [(x-factor*y) % p for x, y in zip(rows[i], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def mmul(a, b, modulus):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) % modulus
                       for j in range(2)) for i in range(2))


def mpow(a, exponent, modulus):
    value = ((1, 0), (0, 1))
    while exponent:
        if exponent % 2:
            value = mmul(value, a, modulus)
        a = mmul(a, a, modulus)
        exponent //= 2
    return value


def exact_checks():
    speh_cases = 0
    for n in range(1, 13):
        for d in range(1, n+1):
            for m in range(1, n//d+1):
                shift = Fraction(d+m-n-1, 2)
                assert shift+Fraction(1-d, 2) == Fraction(m-n, 2)
                for j in range(m):
                    assert Fraction(m-1, 2)-j+Fraction(1-n, 2) == Fraction(m-n, 2)-j
                for h in range(-5, 6):
                    top_entry = Fraction(n-1, 2)-h-Fraction(m-1, 2)
                    assert top_entry+shift == Fraction(d-1, 2)-h
                if m == 1:
                    assert shift == Fraction(d-n, 2)
                if d == n:
                    assert m == 1 and shift == 0
                speh_cases += 1

    inertia_cases = 0
    rank_degenerations = 0
    for ell, n in itertools.product((3, 5, 7, 11), range(1, 6)):
        U = sp.eye(n)
        for i in range(n-1):
            U[i, i+1] = 1
        adjoint = sp.kronecker_product(U.inv().T, U)
        assert rank_mod((adjoint-sp.eye(n*n)).tolist(), ell) < n*n
        rank_degenerations += 1
        for q in range(2, ell):
            assert rank_mod((adjoint-q*sp.eye(n*n)).tolist(), ell) == n*n
            inertia_cases += 1

    twist_cases = 0
    for ell, a in itertools.product((3, 5, 7, 11), range(1, 4)):
        order = ell**a
        half = pow(2, -1, order)
        for exponent in range(order):
            assert (half*(exponent-(-exponent))) % order == exponent
            assert (2*half*exponent) % order == exponent
            twist_cases += 1
    assert 2 % 3 != 1  # Restricting b to (u,u^-1) without the square root is wrong.

    projector_cases = 0
    for ell, depth in itertools.product((3, 5), range(1, 5)):
        modulus = ell**depth
        for unit, c, d in itertools.product(range(1, ell), range(ell), range(ell)):
            U = ((unit, 0), (c, ell*d))
            graph = c*pow(unit-ell*d, -1, modulus) % modulus
            projector = ((1, 0), (graph, 0))
            exponent = ell**(depth-1)*(ell-1)*depth
            assert mpow(U, exponent, modulus) == projector
            assert mmul(projector, projector, modulus) == projector
            assert projector[0] == (1, 0)
            assert mmul(U, projector, modulus) == tuple(
                tuple(unit*x % modulus for x in row) for row in projector)
            projector_cases += 1

    level_cases = 0
    for n in range(1, 9):
        for c in range(n, n+5):
            for i in range(n):
                for j in range(i+1, n):
                    upper_depth = c+1-(j-i)
                    lower_depth = c+1+(j-i)
                    assert upper_depth >= 0
                    assert lower_depth >= c+2
                    level_cases += 1
    nilpotent = sp.Matrix([[0, 1], [0, 0]])
    assert nilpotent != sp.zeros(2) and nilpotent**2 == sp.zeros(2)
    return {
        "speh_normalization_cases": speh_cases,
        "speh_scope": "n=1..12, d>=1, m>=1, dm<=n; exact rational half-norm shifts, all j<m, and infinity labels h=-5..5. Universal normalization is proved in the text.",
        "inertia_adjoint_cases": inertia_cases,
        "inertia_scope": "ell=3,5,7,11; ranks1..5; scalar-times-regular-unipotent residual Frobenius (scalar cancels in Ad); every nontrivial q in F_ell^*. Exact finite-field rank, including ell<=n.",
        "q_equals_one_negative_controls": rank_degenerations,
        "twist_square_root_cases": twist_cases,
        "twist_scope": "ell=3,5,7,11, exponents1..3, every value of a cyclic ell-power character. b_U(u,u^-1)=b_w(u); omitting the square root fails already for order3.",
        "integral_projector_cases": projector_cases,
        "projector_scope": "ell=3,5; coefficient depths1..4; every unit residue and every c,d residue for U=[[a,0],[c,ell*d]]. Exact invertible/nilpotent projector and integral lowest-coordinate inverse, with no division by ell.",
        "original_depth_cases": level_cases,
        "depth_scope": "Original Tc and Nbar(c) use varpi^(c+1). Ranks1..8, c=n..n+4, all roots: conjugation by z leaves positive factors integral and advances negative depth to c+2.",
        "eigencharacter_negative_control": "The faithful regular module of E[epsilon]/epsilon^2 has a nonzero nilpotent operator annihilated by every field character. Good-point scalar decomposition, not faithfulness alone, proves eigencharacter separation. Nongood-point occurrence uses support and the socle instead.",
        "scope": "Exact diagnostic cases. No computation asserts universal Hida control, global component reachability, a completed W04 node, or a final Selmer bound.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert hashlib.sha256(packed).hexdigest() == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    rows = {r[0]: r for r in atlas["modules"]}
    sources = []
    for module, ranges in RANGES.items():
        item = {"repository": atlas["repository"], "commit": atlas["commit"],
                "path": "lean/src/"+module.replace(".", "/")+".lean",
                "git_blob_sha1": rows[module][1]}
        checked = inspect_file(item, args.offline)
        path = ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]
        lines = path.read_bytes().splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo+1 <= 120
            excerpt = b"".join(lines[lo-1:hi])
            assert len(excerpt) <= 12000, (module, lo, hi, len(excerpt))
            excerpts.append({"start": lo, "end": hi, "sha256": hashlib.sha256(excerpt).hexdigest()})
        sources.append({**item, "module": module, "sha256": checked["sha256"],
                        "matches_pinned_blob": True, "reviewed_excerpts": excerpts})
    primary = []
    for item in PRIMARY:
        path = ROOT/item["file"]
        if not path.exists():
            if args.offline:
                raise FileNotFoundError(path)
            path.parent.mkdir(parents=True, exist_ok=True)
            blob = urllib.request.urlopen(item["url"], timeout=60).read()
            assert blob.startswith(b"%PDF")
            assert hashlib.sha256(blob).hexdigest() == item["sha256"]
            path.write_bytes(blob)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"]
        text = (ROOT/item["text_file"]).read_bytes()
        assert hashlib.sha256(text).hexdigest() == item["text_sha256"]
        lines = text.splitlines(keepends=True)
        excerpts = []
        for lo, hi in item["text_ranges"]:
            assert 1 <= lo <= hi <= len(lines) and hi-lo+1 <= 120
            excerpt = b"".join(lines[lo-1:hi])
            assert len(excerpt) <= 12000
            excerpts.append({"start": lo, "end": hi, "sha256": hashlib.sha256(excerpt).hexdigest()})
        primary.append({**item, "bytes": path.stat().st_size,
                        "reviewed_text_excerpts": excerpts, "matches_reviewed_pdf": True})
    stem = "selmer-integral-frontier-ordinary-families"
    artifacts = [f"notes/{stem}.md", f"paper/shared/{stem}.tex",
                 f"paper/shared/{stem}-references.tex",
                 "scripts/check_selmer_integral_frontier_ordinary_families.py"]
    dependencies = ["notes/selmer-integral-frontier-"+name+".md" for name in
                    ("ordinary-diamond", "classical-control", "hecke-determinant",
                     "type-construction", "arithmetic-point", "taylor-wiles",
                     "arithmetic-propagation")]
    for name in artifacts+dependencies:
        data = (ROOT/name).read_bytes()
        assert all(c >= 32 or c == 10 for c in data), name
    report = {
        "schema_version": 1, "status": "PASS",
        "classification": "closed actual ordinary-family subobligation inside W04; independent review recorded separately",
        "claim": "Construct every original HidaProps field for the same actual J: full integral higher-weight classical control, fixed-weight Dense, distinguished-prime unr0, all arithmetic-point decompositions and purity/classicality, and exact finite anticyclotomic TwistOk. With the existing PT, P1/P3 and HasAut, this supplies original HidaU and Modular/ModU.",
        "verification_kind": "Authenticated original contracts, primary theorem interfaces and exact finite diagnostics. The universal proofs are in the note and TeX, not inferred from the tests. No Lean build is asserted.",
        "quantifiers": [
            "Original odd ell, CM Hida setting L/F, V.S'=S, large O, every n>=1 and original residual/type/level/weight datum. HidaU/ModU retains the no-primitive-ellth-root hypothesis on L.",
            "Every strictly increasing labeled weight h; every arithmetic point killing the same J, including nongood points with repeated finite inertial characters and nonsemisimple ramified Hecke action.",
            "Every prescribed finite ell-power anticyclotomic beta with the original old-inertia and I0 kernel conditions, every given twisted point x' with the exact determinant and ordered characters.",
            "Full coefficient ranks, Speh lengths, global multiplicities, conductor depths and finite coefficient extensions are retained; no uniform bound for these quantities is inferred.",
        ],
        "decisive_interfaces": {
            "full_control": "Actual saturated exterior-tensor lattice; original depths Tc,Nbar(c) are c+1. Taking c0>=n permits explicit Gauss factorization of u^-1 y u and original unnormalized sum reindexing. Normalized U preserves the lattice and contracts evaluation kernel. Deep-level approximate lifts, level lowering, the integral ordinary projector and Nakayama give exact integral evaluation isomorphism.",
            "dense": "At each fixed h, original weight coordinates are u_j zeta_j. Finite character corrections retain residual and torsion conditions. Power-series density with finite exclusions gives distinct finite inertial characters, hence one local Jacquet line and actual Hecke eigencharacter separation.",
            "all_points": "Finite faithful T-module M has full support; localization/Nakayama gives occurrence of each y in a weight fibre, and its Artinian socle gives a joint eigenvector. Faithfulness after nonflat scalar change and semisimplicity of nongood U are not assumed.",
            "decomposition": "Labesse on the original definite group and Moeglin-Waldspurger retain all discrete blocks Speh(tau_a,m_a). The exact twist pi_a=tau_a|det|^((d_a+m_a-n-1)/2) gives algNorm_d pi_a=tau_a|det|^((m_a-n)/2). Thus rho=direct_sum r_a epsilon^-j, with full determinant law and all multiplicities.",
            "purity_classicality": "Only when all m_a=1 is common pure weight n-1 asserted; FrobEig itself requires unramifiedness. An irreducible determinant forces one block, m=1,d=n, so the rank-n cusp representation has no half-norm twist. Abstract representation continuity follows from its fixed isomorphism to the continuous semisimple one.",
            "unr0": "V0ok gives unramified residual semisimplification, scalar residual Frobenius polynomial and q mod ell !=1. Even for a nonsplit residual lattice, residual inertia is an ell-group; tame relation first kills its reduction and then Ad(barPhi)-q invertibility kills every congruence layer. Separating weight-zero points give both exact determinant-kernel relations including star.",
            "twist": "Use geometric reciprocity inverse to Milne arithmetic Artin. Source art(g_varpi)=varpi has degree -1, and finite-avatar IsLAdicOf50-60 gives b(varpi)=iota beta(g_varpi). The unique odd-order square root b_U(t)=b(t)^r on U(1) gives b_U(u,u^-1)=b_w(u). Multiplication by b_U(det g) preserves the actual group, tame type, v0 level and residual summand and multiplies U_j by beta(g_varpi)^j.",
            "starting_component": "A-torsion-freeness of finite T implies every minimal prime contracts to zero and has dimension1+n[F:Q]. Stability below an actual seed follows separately from that seed's previously proved absolute irreducibility and a nonzero trace-Gram discriminant. The normalized Space/SeedIn transfer remains distinct.",
        },
        "limitations": [
            "No whole W04 proof-map node is completed.",
            "The exact normalized Space/SeedIn transfer and global rank-two/rank-three component argument to OffFin/FinPt/FinEnd/FinA remain separate obligations.",
            "No uniform integral Selmer length, conductor, arithmetic field degree, coefficient lattice index, type rank or final W02/W11 budget is claimed.",
        ],
        "sources": sources, "primary_literature": primary,
        "exact_diagnostics": exact_checks(),
        "dependencies": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in dependencies],
        "artifacts": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in artifacts],
    }
    destination = ROOT/"certificates"/(stem+".json")
    destination.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n")
    d = report["exact_diagnostics"]
    print(f"PASS: {len(sources)} pinned modules; {len(primary)} primary PDFs; "
          f"{d['speh_normalization_cases']} exact Speh normalizations; "
          f"{d['inertia_adjoint_cases']} local adjoint checks; "
          f"{d['integral_projector_cases']} integral projector checks.")
    print(destination.relative_to(ROOT))


if __name__ == "__main__":
    main()
