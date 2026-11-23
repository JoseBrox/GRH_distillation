#!/usr/bin/env python3
"""Authenticate the actual Core/CoreBC/Raw supplier and its exact diagnostics.

This checks provenance and finite diagnostic cases.  The accompanying note is
the standard-mathematics proof; this is not a Lean build or a proof by testing.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import urllib.request

import sympy as sp
from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
PA = BASE+"PatchingModules."
AB = PA+"AnnihilatorBaseChange."
BC = PA+"PatchingBaseChange."
SS = PA+"SeparableMatrixStability."
RANGES = {
    BASE+"CommutativeAlgebra.ResMapBijective": [(9, 33)],
    PA+"PatchedSupportCompletions": [(30, 70), (112, 157), (178, 213), (223, 230)],
    PA+"ThetaCoefficientMapEq": [(86, 141), (265, 297)],
    PA+"PairedDualFirstOrderDualMatrixSpace": [(251, 294), (352, 366)],
    SS+"SysCover": [(8, 80)],
    SS+"SelmerCocyclesLimitAndDescentProperties": [(15, 110), (111, 211)],
    AB+"SpecializationMapCompUniversalSection": [(52, 101), (103, 158)],
    AB+"FiniteOpenHomsToFiniteGroup": [(161, 224), (225, 280), (281, 328)],
    AB+"RmapsEx": [(33, 99)],
    AB+"TupNOfRep": [(33, 86)],
    AB+"SplittingAlgebraNontrivialFreeGenerated": [(41, 136), (193, 225)],
    AB+"SpoCo": [(8, 16)],
    AB+"PiSurj": [(106, 134)],
    AB+"OoFiniteHom": [(149, 196)],
    AB+"OoPair": [(65, 127)],
    AB+"InjOfProd": [(77, 110), (111, 173)],
    AB+"PatchedModuleFreeFiniteOverIwasawaAlgebra": [(7, 46)],
    AB+"EventuallyExistsPatchedModuleQuotientMaps": [(10, 46), (193, 239)],
    AB+"FreeNQuot": [(13, 44)],
    AB+"PatchedTraceSingleMulSubOneApproxAnnihilated": [(22, 78)],
    AB+"PatchedLamConjTwistApproxAnnihilated": [(39, 90)],
    AB+"PatchedTraceLocalCharPolyApproxAnnihilated": [(54, 96)],
    AB+"EventuallyTraceInertiaCongruenceOfAdapted": [(27, 53)],
    AB+"MapRingHomSingleMulCharpolyElement": [(42, 67)],
    AB+"MapRingHomSingleMulPartialCharpolyElement": [(49, 80)],
    AB+"FoCong": [(6, 40)],
    AB+"T3Of": [(7, 28)],
    AB+"LaDimArith": [(23, 73)],
    AB+"NonssT": [(69, 99)],
    AB+"PatchedModuleAnnihilatorLeComapIffIdealLe": [(6, 28)],
    AB+"ChainAbs": [(7, 70)],
    BC+"ChainLift": [(6, 75)],
    BC+"AlgebraMapEq": [(10, 33), (57, 76)],
    BC+"Oprime": [(104, 110)],
    BC+"PtLift": [(87, 134)],
    BC+"TilCo": [(8, 48)],
    BC+"AutBc": [(10, 27)],
    SS+"TwquotEx": [(19, 87)],
    SS+"RawMain": [(12, 48)],
    PA+"AutomorphicDetection.LiftPt": [(49, 110), (111, 175)],
    PA+"AutomorphicDetection.CoreBC": [(24, 100), (101, 127)],
}

PRIMARY = [
    {"file": "build/selmer-level-sources/chenevier-determinants.pdf",
     "text_file": "build/selmer-level-sources/chenevier-determinants.txt",
     "url": "https://arxiv.org/pdf/0809.0415",
     "sha256": "f3c0e0d86e803301c617d3023d425752e30da46673ed5af932647eb284286953",
     "text_ranges": [(1947, 2018)],
     "printed_pages": [42, 43],
     "interface": "Proposition 3.3 and Remark 3.5: universal continuous multiplicative polynomial law and topological generation by every characteristic-polynomial coefficient; completed scalar change gives the original O coefficient category. The previously verified multiplicity-free Cayley-Hamilton theorem retains rank-one diagonal corners."},
    {"file": "build/selmer-level-sources/wang-erickson-algfam.pdf",
     "text_file": "build/selmer-level-sources/wang-erickson-algfam.txt",
     "url": "https://arxiv.org/pdf/1501.05629",
     "sha256": "cd2f131fce547c5d9fd873751417683e904d2075b064531ddc1f5e2c13df7382",
     "text_ranges": [(1040, 1115)],
     "printed_pages": [19, 20],
     "interface": "Proposition 3.2: finite continuous H1(G,ad residual semisimplification) implies Noetherian universal determinant ring; the proof explicitly removes the hypothesis that n! is invertible. The previously verified Proposition 3.6 supplies the finite continuous Cayley-Hamilton quotient."},
]


def valuation(a, ell):
    assert a != 0
    n = 0
    while a % ell == 0:
        a //= ell
        n += 1
    return n


def exact_checks():
    binomial_cases = 0
    for ell in (3, 5, 7):
        for k in range(1, 9):
            for j in range(1, 7):
                a = k+j
                # Coefficients of degree >= k are already in (Y)^k.
                for r in range(1, k):
                    assert valuation(math.comb(ell**a, r), ell) >= j
                    binomial_cases += 1

    x, y, f, a, t, u = sp.symbols("x y f a t u")
    exponent_cases = 0
    for e in range(9):
        power = e+1
        geometric_sum = sum(x**(power-1-i)*y**i for i in range(power))
        assert sp.expand(x**power-y**power-(x-y)*geometric_sum) == 0
        # The +1 also keeps the branch rho(a')=0 valid when the input e=0.
        assert (0**power) == 0
        exponent_cases += 1

    # The actual finite free splitting algebra need not be etale or reduced
    # at the closed point.  The multiplier is nonzero on the generic curve,
    # but it is not a unit in the curve's complete coefficient DVR.
    polynomial = u*u-t*t
    multiplication_u = sp.Matrix([[0, t*t], [1, 0]])
    assert multiplication_u**2 == t*t*sp.eye(2)
    assert multiplication_u.subs(t, 0) != sp.zeros(2)
    assert multiplication_u.subs(t, 0)**2 == sp.zeros(2)
    multiplier = (u-(-u))**2*((-u)-u)**2
    assert sp.expand(multiplier) == 16*u**4
    assert sp.rem(multiplier, polynomial, u) == 16*t**4

    # Surjective maps do not admit arbitrary homomorphism lifts.  The
    # corrected local construction lifts free generators, then kills the
    # relations in the limiting kernel.
    c4_lifts = [a for a in range(4) if a % 2 == 1]
    assert c4_lifts == [1, 3]
    assert all((2*a) % 4 != 0 for a in c4_lifts)
    assert all((2*a) % 2 == 0 for a in c4_lifts)

    dimension_cases = 0
    for D in range(8):
        for n in range(1, 6):
            for q in range(6):
                weight_dimension = D+2
                curve_local_dimension = weight_dimension-1
                support_dimension = curve_local_dimension+n*q
                assert support_dimension == 1+(D+n*q)
                dimension_cases += 1
    return {
        "binomial_coefficient_cases": binomial_cases,
        "binomial_scope": "ell=3,5,7; 1<=k<=8; 1<=j<=6; a=k+j; all 1<=r<k. Universal containment is proved in the note.",
        "difference_of_powers_cases": exponent_cases,
        "exact_exponent": "Original TWAut exponent e_T retained; S5 approximate-annihilator exponent is e_T+1, including e_T=0.",
        "coalescing_root_negative_control": {
            "algebra": "k[[t]][u]/(u^2-t^2), characteristic k odd",
            "rank": 2, "generic_roots": ["t", "-t"],
            "closed_fibre": "k[u]/u^2, with nonzero nilpotent u",
            "fEl_at_one": "16*t^4, nonzero and not a unit",
            "conclusion": "Do not replace the original splitting algebra by an etale/reduced algebra or require the multiplier to be a unit at the closed curve point.",
        },
        "local_lift_negative_control": "C4 -> C2: neither lift of the nontrivial generator has order 2. Free-generator lifting and subsequent relation killing are essential.",
        "dimension_cases": dimension_cases,
        "zero_module_guard": "If M0=0 then J=B and no starting prime can contain J; the theorem does not manufacture nonvanishing from this case.",
        "scope": "Exact finite arithmetic and symbolic diagnostics. No computational test establishes the universal marked propagation theorem.",
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
        lines = text.splitlines(keepends=True)
        excerpts = []
        for lo, hi in item["text_ranges"]:
            excerpt = b"".join(lines[lo-1:hi])
            assert hi-lo+1 <= 120 and len(excerpt) <= 12000
            excerpts.append({"start": lo, "end": hi, "sha256": hashlib.sha256(excerpt).hexdigest()})
        primary.append({**item, "bytes": path.stat().st_size,
                        "text_sha256": hashlib.sha256(text).hexdigest(),
                        "reviewed_text_excerpts": excerpts, "matches_reviewed_pdf": True})

    stem = "selmer-integral-frontier-marked-propagation"
    artifacts = [f"notes/{stem}.md", f"paper/shared/{stem}.tex",
                 f"paper/shared/{stem}-references.tex",
                 "scripts/check_selmer_integral_frontier_marked_propagation.py"]
    dependencies = [
        "notes/selmer-integral-frontier-limit-comparison.md",
        "notes/selmer-integral-frontier-taylor-wiles.md",
        "notes/selmer-integral-frontier-polarized-model.md",
        "notes/selmer-integral-frontier-local-propagation.md",
        "notes/selmer-integral-frontier-patched-support.md",
        "notes/selmer-integral-frontier-first-global-bound.md",
        "notes/selmer-integral-frontier-second-global-bound.md",
    ]
    for name in artifacts+dependencies:
        data = (ROOT/name).read_bytes()
        assert all(c >= 32 or c == 10 for c in data), name
    report = {
        "schema_version": 1, "status": "PASS",
        "classification": "closed actual marked-propagation subobligation inside W04; independent review recorded separately",
        "claim": "Construct the original marked universal determinant ring, every S5 module/map/relation field, and prove the complete Core, CoreBC and Raw chain propagation contracts.",
        "verification_kind": "Authenticated pinned interfaces, primary determinant representability and Noetherianity, and exact symbolic/arithmetic diagnostic cases. Universal proofs are in the note and TeX; no Lean build is asserted.",
        "quantifiers": [
            "Every odd ell, original finite-residue complete coefficient DVR O, rank n and actual ordinary datum; n>=1 follows from existence of any NP point.",
            "Every adapted original TW tower with actual TWAut, every finite normalized-point chain and all original odd Selmer families and B1/B2 constants.",
            "Every linking NonSS prime, initial stable prime containing J, and terminal stable or NonSS prime below the last curve kernel.",
            "Every fixed relation and coefficient precision has an eventual assertion in the one ultrafilter U; U<=atTop imports the original a_j(N)>=N and norm congruences. No cofinite replacement or countable intersection is asserted.",
            "All original finite-flat splitting ranks, O'/O ranks, marked variable, ordered characters, coefficient actions, fEl factors and original auxiliary module ranks remain present.",
        ],
        "decisive_interfaces": {
            "common_cover": "One finitely generated free profinite P covers all levels; compactness of finite quotients constructs K and Gamma_infinity. Local maps use free presentations of fixed finitely generated local quotients, generator lifts, continuity of all profinite relators, and ker(pi_N)V=KV along U; no homomorphism lift to P is assumed.",
            "universal_ring": "Full multiplicative polynomial law and every ordered ordinary character, plus s,Z,Y; Chenevier 3.3 and Wang-Erickson 3.2 require no n! invertibility. All six literal source Rel families are imposed before completions.",
            "residue_field": "ResMapBijective 9-33 proves the source IsCO residue condition. Hence O' tensor_O B is local with residue O'/m_O', not an unselected semilocal tensor algebra.",
            "determinant_descent": "The trace-radical ideal in the multiplicity-free Cayley-Hamilton GMA has zero rank-one diagonal corners; every determinant cycle containing it vanishes universally. The full determinant law descends even when ell<=n.",
            "integral_modules": "X=C tensor_B M0 retains actual finite-free rank; every MN is original. Mod weight-ideal comparisons use finite quotient Nakayama and actual TWAut maps. Diamond quotient order is unchanged.",
            "relations": "Original fEl(Q_N,U) approaches fEl(1,U); fixed original e_T yields S5 e_T+1 by difference of powers. All six approximation suppliers use U, including exact original cyclotomic and mixed ordinary coefficients.",
            "equation_algebra": "OoPair.ooKer is the already closed original chBar(pairGens union qGens). NonSS transfer uses a continuous quotient onto the finite original equation algebra; no radical, saturation, generic trace algebra or unproved closure/base-change equality replaces it.",
            "support": "Finite-flat prime zigzag, GalOut K1/K2/K3 and actual S5 MOVE propagate the given starting support. Lambda curve localization has dimension D+1 and the support threshold remains 1+D+nq.",
            "raw": "Residual-kernel pro-ell quotient is justified by finite CH algebra before quotienting; coefficient actions and cocycles factor together through finite semidirect ell-groups. Exact B1/B2, odd families, discriminants and original equation algebra are preserved.",
        },
        "limitations": [
            "No whole W04 proof-map node is completed.",
            "The initial stable prime in support is a retained hypothesis, not inferred from a characteristic-zero seed.",
            "Normalization of arbitrary nice curves, arithmetic auxiliary-prime realization, and the subsequent global component argument are separate suppliers.",
            "No uniform global Selmer length, coefficient degree, splitting rank, lattice index or arithmetic height budget is claimed.",
        ],
        "sources": sources, "primary_literature": primary,
        "exact_diagnostics": exact_checks(),
        "dependencies": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in dependencies],
        "artifacts": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in artifacts],
    }
    destination = ROOT/"certificates"/(stem+".json")
    destination.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n")
    print(f"PASS: {len(sources)} pinned modules; {len(primary)} primary PDFs; "
          f"{report['exact_diagnostics']['binomial_coefficient_cases']} exact binomial cases; "
          f"{report['exact_diagnostics']['dimension_cases']} retained-dimension cases.")
    print(destination.relative_to(ROOT))


if __name__ == "__main__":
    main()
