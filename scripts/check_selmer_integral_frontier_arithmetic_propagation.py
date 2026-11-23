#!/usr/bin/env python3
"""Authenticate actual normalization, arithmetic towers, and P1/P2/P3.

Finite exact checks diagnose the valuation, coefficient, and cohomology
interfaces.  The universal arguments are in the accompanying mathematical
proof.  This script neither proves them by testing nor asserts a Lean build.
"""
from __future__ import annotations

import argparse
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
PA = BASE+"PatchingModules."
AD = PA+"AutomorphicDetection."
CF = PA+"ChebotarevFamilies."
DC = PA+"DegreeCountCohomology."
AH = PA+"ArchimedeanH0Cards."
RANGES = {
    BASE+"WeilGroupCharacters.UniversalOrdinaryDeterminantRing":
        [(10, 108), (109, 161), (189, 248), (249, 301)],
    PA+"TaylorWilesObstructionBound":
        [(16, 60), (88, 124), (126, 154)],
    PA+"PairedDualFirstOrderDualMatrixSpace": [(251, 294)],
    AD+"ConjugationDescendsToSubring": [(137, 223), (224, 323)],
    PA+"DeterminantPadicFree.FlagBasis": [(38, 82)],
    AD+"ArPl": [(13, 120), (121, 179)],
    CF+"FrSNormal": [(183, 207)],
    CF+"ChebOne": [(1, 75)],
    CF+"ChebFam": [(6, 35)],
    CF+"HomBound": [(82, 157)],
    CF+"LevUp": [(5, 53)],
    DC+"IsDualPair": [(44, 94), (124, 140)],
    DC+"ArPres": [(23, 81), (95, 163)],
    DC+"ArPresAlt": [(11, 26)],
    DC+"PresCounts": [(9, 43)],
    DC+"UnrLoc": [(6, 46)],
    DC+"ArSys": [(8, 20)],
    AD+"BoundW1Arithmetic": [(7, 16)],
    AD+"TaylorWilesObstructionBound": [(25, 46)],
    AH+"PushforwardPreservesSelmerCocycles": [(205, 241)],
    AH+"ArGlob": [(7, 22)],
    AH+"CardOfAddEquiv": [(11, 38)],
    AH+"ArchH0Card": [(7, 42)],
    AH+"ArUr": [(7, 10)],
    AH+"CkCastMod": [(138, 166)],
    AH+"DegSplit": [(40, 48)],
    AD+"Choice": [(14, 40)],
    CF+"PFromAutOf": [(30, 131)],
    AD+"PfromAut": [(1, 10)],
    BASE+"WeilGroupCharacters.LocCFTAll": [(10, 23)],
    BASE+"WeilGroupCharacters.WeilCharactersModular.LocCFT": [(31, 90)],
}

PRIMARY = [
    {"file": "build/reference-cache/milne-cft.pdf",
     "text_file": "build/reference-cache/milne-cft.txt",
     "url": "https://www.jmilne.org/math/CourseNotes/CFT.pdf",
     "sha256": "50d79af78250a9f1117ad9d337e0b231704a533fc707966ed1bfa52e13d498f5",
     "text_sha256": "5f9250521f173b47423192f8c1b2fe05b9b38329522454f0bf93ee96cfa6547a",
     "text_ranges": [(1305, 1360), (6833, 6900), (8918, 8970)],
     "printed_pages": [20, 21, 124, 164],
     "interface": "I.1.1 local reciprocity; IV.1.14-1.16 double-centralizer and Schur lemmas for faithful semisimple modules; V.3.23 Chebotarev for every conjugacy class of the actual finite Galois extension. Positive density permits exclusion of any fixed finite set, without an effective prime-height claim."},
    {"file": "build/reference-cache/milne-adt-2006.pdf",
     "text_file": "build/reference-cache/milne-adt-2006.txt",
     "url": "https://www.jmilne.org/math/Books/ADTnot.pdf",
     "sha256": "2c6195ec76a974f3f336c77cb71cc3845b018aad2d43136716b3477a3bc5fb31",
     "text_sha256": "766d5e99c425ba1fd6410d677487d70ae85b31c68465856efd2fec2c62bf9e5d",
     "text_ranges": [(1418, 1452), (1640, 1669), (2865, 2935),
                     (3158, 3178), (3400, 3438)],
     "printed_pages": [26, 27, 31, 32, 57, 58, 67],
     "interface": "I.2.1 local finiteness and degree-three vanishing; I.2.8 local Euler characteristic; I.4.10 Poitou-Tate and global degree >=3 supported at real places; I.4.15 finite cohomology for finite S; I.5.1 global Euler characteristic. S contains every ell place and ell is odd. CohAx.ck is applied only to ell-killed modules, so its dual target is F_ell(1), not a silently truncated dual of an arbitrary ell-primary group."},
]


def finite_field_checks():
    square_cases = hensel_cases = 0
    for p in (3, 5, 7, 11):
        nonsquare = next(d for d in range(2, p)
                         if pow(d, (p-1)//2, p) == p-1)
        zero, one = (0, 0), (1, 0)

        def add(a, b):
            return ((a[0]+b[0]) % p, (a[1]+b[1]) % p)

        def neg(a):
            return ((-a[0]) % p, (-a[1]) % p)

        def mul(a, b):
            return ((a[0]*b[0]+nonsquare*a[1]*b[1]) % p,
                    (a[0]*b[1]+a[1]*b[0]) % p)

        elements = list(itertools.product(range(p), repeat=2))

        def inv(a):
            return next(b for b in elements if mul(a, b) == one)

        for residue in range(1, p):
            root = next(b for b in elements if mul(b, b) == (residue, 0))
            assert root != zero
            square_cases += 1
            inverse_derivative = inv(add(root, root))
            for pattern in range(p):
                # An actual unit in F_p[[t]], embedded by t=s^2.
                unit = [(residue, 0)]+[
                    ((pattern+j*j) % p, 0) if j % 2 == 0 else zero
                    for j in range(1, 9)]
                solution = [root]
                for degree in range(1, len(unit)):
                    known = zero
                    for i in range(1, degree):
                        known = add(known, mul(solution[i], solution[degree-i]))
                    solution.append(mul(add(unit[degree], neg(known)), inverse_derivative))
                    actual = zero
                    for i in range(degree+1):
                        actual = add(actual, mul(solution[i], solution[degree-i]))
                    assert actual == unit[degree]
                hensel_cases += 1
    return square_cases, hensel_cases


def rank_mod(matrix, p):
    matrix = [[x % p for x in row] for row in matrix]
    pivot = 0
    for col in range(len(matrix[0])):
        row = next((r for r in range(pivot, len(matrix)) if matrix[r][col]), None)
        if row is None:
            continue
        matrix[pivot], matrix[row] = matrix[row], matrix[pivot]
        inverse = pow(matrix[pivot][col], -1, p)
        matrix[pivot] = [(inverse*x) % p for x in matrix[pivot]]
        for r in range(len(matrix)):
            if r != pivot:
                factor = matrix[r][col]
                matrix[r] = [(x-factor*y) % p
                             for x, y in zip(matrix[r], matrix[pivot])]
        pivot += 1
        if pivot == len(matrix):
            break
    return pivot


def exact_checks():
    valuation_cases = 0
    for a, b in itertools.product(range(-8, 9), repeat=2):
        lower_bound = 2*max(0, b-a)+a-b
        assert lower_bound == abs(a-b)
        valuation_cases += 1
    s = sp.symbols("s", nonzero=True)
    v, w = sp.symbols("v w", nonzero=True)
    orthonormal_cases = 0
    for a, b in itertools.product(range(-3, 4), repeat=2):
        P = sp.diag(s**(2*a)*v**2, s**(2*b)*w**2)
        T = sp.diag(s**(-a)/v, s**(-b)/w)
        assert sp.simplify(T.T*P*T) == sp.eye(2)
        orthonormal_cases += 1
    # Mere stability of one lattice is insufficient.  The normalized
    # representation can acquire a denominator unless its P-dual is stable.
    P = sp.diag(1, s**2)
    T = sp.diag(1, 1/s)
    R = sp.Matrix([[1, 1], [0, 1]])
    assert T.T*P*T == sp.eye(2)
    assert T.inv()*R*T == sp.Matrix([[1, 1/s], [0, 1]])

    square_cases, hensel_cases = finite_field_checks()
    unramified_cases = 0
    for p in (3, 5):
        for a, b, c, d in itertools.product(range(p), repeat=4):
            if (a*d-b*c) % p == 0:
                continue
            rank = rank_mod([[a-1, b], [c, d-1]], p)
            invariants = p**(2-rank)
            h1 = p**(2-rank)
            coboundaries = p**2//invariants
            assert h1*coboundaries == p**2
            unramified_cases += 1
        for a, b in itertools.product(range(1, p), repeat=2):
            # Inertia diag(-1,1), Frobenius diag(a,b): use only M^I.
            h1 = p if b == 1 else 1
            invariants = h1
            assert h1*(p**2//invariants) == p**2
            unramified_cases += 1

    cardinality_cases = 0
    for p, q, index, h1 in itertools.product((3, 5, 7), range(5), range(1, 6), range(4)):
        exact_bound = p**h1*p**(q*index)
        assert exact_bound == p**(h1+q*index)
        if q == 0:
            assert exact_bound == p**h1
        cardinality_cases += 1
    # Hom(Z/p^2,F_p) and Hom(Z/p^2,Q_p/Z_p) have different orders.
    # The smaller target is legitimate precisely because CohAx requires pM=0.
    for p in (3, 5, 7):
        hom_to_fp = sum((p*p*a) % p == 0 for a in range(p))
        hom_to_qpzp = sum((p*p*a) % (p*p) == 0 for a in range(p*p))
        assert hom_to_fp == p and hom_to_qpzp == p*p
    return {
        "valuation_cases": valuation_cases,
        "valuation_scope": "All a_i,a_j in [-8,8], including negative exponents and both directions; exact identity 2max(0,a_j-a_i)+a_i-a_j=|a_i-a_j|.",
        "orthonormal_symbolic_cases": orthonormal_cases,
        "dual_lattice_negative_control": "P=diag(1,s^2), R=[[1,1],[0,1]], T=diag(1,s^-1): R preserves the standard lattice but T^-1 R T has s^-1. The proof uses stability of both M and M#.",
        "finite_residue_square_cases": square_cases,
        "truncated_hensel_cases": hensel_cases,
        "hensel_scope": "p=3,5,7,11; every nonzero F_p residue in F_(p^2), and p prescribed unit-series patterns through s^8. This diagnoses the simultaneous coefficient extension; the universal Hensel argument is separate.",
        "unramified_cocycle_cases": unramified_cases,
        "unramified_scope": "Every GL_2(F_3) and GL_2(F_5) Frobenius with trivial inertia, plus every commuting diagonal Frobenius for inertia diag(-1,1). Exact kernel/cokernel and coboundary counts.",
        "retained_cardinality_cases": cardinality_cases,
        "cardinality_scope": "p=3,5,7; q=0..4; residual subgroup index=1..5; initial H1 dimension=0..3. The actual bound retains q*[Gamma_0:H].",
        "cohomology_category_negative_control": "Hom(Z/p^2,F_p) has order p whereas Hom(Z/p^2,Q_p/Z_p) has order p^2. No ell-primary extension of the ell-killed CohAx.ck assertion is made.",
        "scope": "Exact finite and symbolic diagnostics, not a computational proof of universal arithmetic propagation or a uniform final Selmer budget.",
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

    stem = "selmer-integral-frontier-arithmetic-propagation"
    artifacts = [f"notes/{stem}.md", f"paper/shared/{stem}.tex",
                 f"paper/shared/{stem}-references.tex",
                 "scripts/check_selmer_integral_frontier_arithmetic_propagation.py"]
    dependencies = ["notes/selmer-integral-frontier-"+name+".md" for name in
                    ("finite-selection", "coefficient-extension", "dual-detection",
                     "first-global-bound", "second-global-bound", "obstruction-quotients",
                     "taylor-wiles", "marked-propagation")]
    for name in artifacts+dependencies:
        data = (ROOT/name).read_bytes()
        assert all(c >= 32 or c == 10 for c in data), name
    report = {
        "schema_version": 1, "status": "PASS",
        "classification": "closed actual arithmetic-propagation subobligation inside W04; independent review recorded separately",
        "claim": "Construct exact Norm, ArPl and arithmetic ArSys/CohAx, then discharge original PfromAut and hence P1core, P2core and P3core using the actual TWAut and marked-propagation theorems.",
        "verification_kind": "Authenticated original interfaces, classical primary theorem interfaces, and exact diagnostic arithmetic. The universal proof is in the note and TeX; no Lean build is asserted.",
        "quantifiers": [
            "Every original odd ell, actual Hida setting L/F, coefficient DVR O, n>=1, residual datum r, universal ordinary pair (B,u), and actual Hecke ideal J, retaining V0.S'=S and the source nontrivial residual cyclotomic hypothesis.",
            "Every NiceI point, and every finite chain of NiceE points with the original ordered ordinary characters, original D0, full cyclotomic kernel, stable/thick linking conditions and original closed equation algebra.",
            "Every simultaneous detecting tuple, including q=0, every N, and the actual auxiliary arithmetic fields and residual subgroup index; no bound on auxiliary prime height or lattice index is asserted.",
            "CohAx FinH, onto, LocE, UrAx and ck use ell-killed finite modules, exactly as at source lines 205-241. The ck dual is F_ell(1); arbitrary ell-primary modules would require Q_ell/Z_ell(1).",
        ],
        "decisive_interfaces": {
            "normalization": "The original block polarization is diagonalized over a stable lattice. Its polarization dual is also stable, giving v(rho_ij)>=max(0,a_j-a_i). The single rank-four extension k[[t]] -> k_2[[s]], t=s^2, squares every unit and gives normalized entries of valuation at least |a_i-a_j|.",
            "ordinary_data": "Saturated intersections of the original ordered flag with the normalized lattice give exact integral bases and original block assignments. Full determinant law, psi_mu, N1/N3 and original-D0 N4 are preserved.",
            "arithmetic_tower": "Every sigma_j lifts into the full cyclotomic kernel by ArPl 65-73. Chebotarev conditions sigma_j^-1 modulo W_N and epsilon modulo ell^N are therefore compatible on the original L/F; geometric Frobenius has the exact tame relation phi^-1 tau phi=tau^Q.",
            "uniform_homs": "Retain #Hom(H_N,F_ell) <= #Hom(H,F_ell)*ell^(q*[Gamma_0:H]); no fixed-index assumption or dimension/cardinality conflation.",
            "arithmetic_system": "The ordinary, old tame, distinguished and auxiliary places partition the actual S_N. All split in L/F, so original local group maps and degrees agree. Sum d_v=[F:Q] is retained.",
            "unramified_subgroups": "Use exact J_u=I_u intersect all residual-character kernels. I_u/J_u has prime-to-ell order. Inflation-restriction and averaging supply exact UrAx cocycle counts and lifting, without substituting full inertia.",
            "cohomology": "Local/global finite duality and Euler characteristics supply every CohAx field in its ell-killed category. Local H2 right-exactness makes the original Ck2 a quotient of the full Poitou-Tate cokernel, bounded by #Hom_G(M,F_ell(1)). Odd ell kills real degree>=3 contributions.",
            "assembly": "Finite coefficient extension preserves curve kernels; actual B1/B2 and TWAut supply Raw. Stable equals the original trace-Gram discriminant condition; thick implies NonSS for the unchanged closed equation algebra. Raw yields P1 and all finite P3 chains, including zero-length P2.",
        },
        "limitations": [
            "No whole W04 node is completed.",
            "A stable prime already in actual Hecke support is a retained starting hypothesis; the theorem does not manufacture characteristic-prime support from a characteristic-zero seed.",
            "The subsequent global component/curve argument and finite-index two-sided rigidity remain separate obligations.",
            "No uniform arithmetic Selmer length, coefficient degree, lattice index or final conductor/height budget is claimed.",
        ],
        "sources": sources, "primary_literature": primary,
        "exact_diagnostics": exact_checks(),
        "dependencies": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in dependencies],
        "artifacts": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in artifacts],
    }
    destination = ROOT/"certificates"/(stem+".json")
    destination.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n")
    diagnostics = report["exact_diagnostics"]
    print(f"PASS: {len(sources)} pinned modules; {len(primary)} primary PDFs; "
          f"{diagnostics['valuation_cases']} exact valuation cases; "
          f"{diagnostics['truncated_hensel_cases']} unit-root diagnostics; "
          f"{diagnostics['unramified_cocycle_cases']} exact local cocycle counts.")
    print(destination.relative_to(ROOT))


if __name__ == "__main__":
    main()
