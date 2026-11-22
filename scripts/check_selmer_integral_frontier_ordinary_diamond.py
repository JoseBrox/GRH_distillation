#!/usr/bin/env python3
"""Authenticate the original ordinary module and diamond trace interfaces.

This checks source provenance and artifact hashes. The mathematical
proofs are in the note; this is neither a finite numerical proof nor a
Lean build.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    "WeilGroupCharacters.ContinuousResP": [(73, 110)],
    "HeckeAlgebras.IsTheta": [(60, 143)],
    "HeckeAlgebras.TcAnti": [(68, 112)],
    "HeckeAlgebras.ContinuousTorusCharacter": [(118, 145), (151, 230), (245, 246)],
    "HeckeAlgebras.CoefficientRepTrivialOnUnramified": [(122, 165)],
    "HeckeAlgebras.OrdinaryHeckeCharacters.IndexNeZero": [(378, 429)],
    "HeckeAlgebras.OrdinaryHeckeCharacters.NtExpand": [(412, 487)],
    "BuildingsResidueChars.ExistsFiniteIwahoriDoubleCosetRepresentatives": [(23, 48)],
    "BuildingsResidueChars.ExistsIwahoriTorusProjection": [(5, 55)],
    "BuildingsResidueChars.ExistsLinearSectionAutomorphicFunctionsOfFree": [(5, 48)],
    "BuildingsResidueChars.ExistsSectionAutomorphicSpaceWithPrescribedValue": [(8, 103)],
    "BuildingsResidueChars.UOperatorPowEventuallyInvariantModPow": [(5, 65)],
    "HeckeAlgebras.OrdinaryHeckeCharacters.UOpLevel": [(20, 93)],
    "HeckeAlgebras.OrdinaryHeckeCharacters.OrdFree": [(295, 303), (357, 413), (441, 445)],
    "HeckeAlgebras.OrdinaryHeckeCharacters.OrdProj": [(117, 188), (298, 375), (379, 380), (445, 499)],
    "HeckeAlgebras.OrdinaryHeckeCharacters.HiComm": [(194, 230)],
    "HeckeAlgebras.OrdinaryHeckeCharacters.PiBasic": [(197, 260), (379, 398)],
    "HeckeAlgebras.OrdinaryHeckeCharacters.LevelUR2Faith": [(14, 41)],
    "HeckeAlgebras.OrdinaryHeckeCharacters.LevelUR2IwLev": [(18, 56)],
    "PatchingModules.NilpotentLevelLowering.DelIso": [(202, 218)],
    "PatchingModules.NilpotentLevelLowering.FreeSummand": [(93, 100)],
    "PatchingModules.NilpotentLevelLowering.OpToTW": [(19, 50), (53, 80)],
    "PatchingModules.ThetaCoefficientMapEq": [(163, 236)],
    "ModularityArgument.ThresholdArguments.DenseThresholdCases.HidaLevelX": [(145, 190)],
    "ModularityArgument.ThresholdArguments.DenseThresholdCases.PaLevel": [(24, 57)],
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
    for suffix, intervals in RANGES.items():
        module = BASE+suffix
        item = {"repository": atlas["repository"], "commit": atlas["commit"],
                "path": "lean/src/"+module.replace(".", "/")+".lean",
                "git_blob_sha1": rows[module][1]}
        checked = inspect_file(item, args.offline)
        cache = ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]
        lines = cache.read_bytes().splitlines(keepends=True)
        excerpts = []
        for start, end in intervals:
            assert 1 <= start <= end <= len(lines) and end-start+1 <= 120
            data = b"".join(lines[start-1:end])
            assert len(data) <= 12000
            excerpts.append({"start": start, "end": end,
                             "sha256": hashlib.sha256(data).hexdigest()})
        sources.append({**item, "module": module, "sha256": checked["sha256"],
                        "matches_pinned_blob": True, "reviewed_excerpts": excerpts})
    stem = "selmer-integral-frontier-ordinary-diamond"
    artifacts = [f"notes/{stem}.md", f"paper/shared/{stem}.tex",
                 f"paper/shared/{stem}-references.tex",
                 "scripts/check_selmer_integral_frontier_ordinary_diamond.py"]
    for path in artifacts:
        assert all(c >= 32 or c in (10, 9) for c in (ROOT/path).read_bytes()), path
    report = {
        "schema_version": 1,
        "status": "PASS",
        "verification_kind": "Pinned source provenance and artifact hashes; mathematical proofs are in the note.",
        "classification": "closed obligation inside W04: original ordinary modules, projectivity, exact trace; no whole proof-map node completed",
        "claim": "The original ordinary Hida function modules are finite free over the original weight ring, projective over the actual finite diamond group ring, and have surjective unnormalized trace with exactly the augmentation kernel, including prescribed residual Hecke localization and commuting spectral summands.",
        "quantifiers": "Fix the original Hida datum, weight ring, auxiliary set Q and Hecke eigenvalues. The conclusions hold for every compact open auxiliary level and every finite normal pair; every a_j>=0 is allowed. No uniform bound on ranks or nonvanishing of absent residual factors is asserted.",
        "proved_steps": [
            "Actual fixed odd unramified principal level gives trivial stabilizers for every compact auxiliary level.",
            "Finite congruence-level weighted function spaces are finite free by original double-coset representatives.",
            "The actual unnormalized U operator has compatible invertible Fitting summands at every coefficient precision.",
            "The inverse limit constructs the original finite-free ordinary module, exact reduction and factorial-power projector.",
            "A genuine double-coset transversal gives a group-ring-linear splitting without division by the diamond order.",
            "The actual unnormalized trace is onto and its kernel is exactly augmentation.",
            "The fixed original Hecke family and later commuting spectral idempotents preserve the splitting.",
            "The prescribed diagonal residue quotient gives the exact local group ring and its original power-series variables."
        ],
        "decisive_source_interfaces": {
            "operator": {
                "definition": "U_z=sum over q in N/(zNz^-1) of right translation by q*z; no normalization factor",
                "sources": ["HeckeAlgebras.ContinuousTorusCharacter:120-121",
                            "HeckeAlgebras.TcAnti:94-112"]
            },
            "level_lowering": {
                "hypotheses": [
                    "Coefficient character reduced modulo m^k is trivial on the original T_c.",
                    "Input vector is N-fixed, transforms by the original inverse torus character, and is fixed by Nbar(d+1), d>=c.",
                    "The source z satisfies z^-1*Nbar(d)*z subset Nbar(d+1)."
                ],
                "conclusion": "U_z preserves the same torus character and produces Nbar(d)-invariance; its powers send E_(k,c') into E_(k,c) for c'>=c.",
                "sources": ["HeckeAlgebras.OrdinaryHeckeCharacters.UOpLevel:20-93",
                            "BuildingsResidueChars.UOperatorPowEventuallyInvariantModPow:5-65"]
            },
            "integral_sections": {
                "formula": "s(v)(gamma*x_i*(u,b))=theta(tt(b))^-1*tau(u^-1)*v_i, with original representatives and b in I(c)",
                "torus_projection": "tt(b*n)=tt(b); tt(b*t)=tt(b)*t; tt(b*y)=tt(b)*s for y in Nbar(d), s in T_d",
                "conclusion": "Arbitrary representative values have an integral original Sp lift, exactly N/T/tame-equivariant and uniformly continuous; if theta(T_c)=1 mod m^k, its mod-m^k reduction is Nbar(c)-invariant.",
                "sources": ["BuildingsResidueChars.ExistsIwahoriTorusProjection:5-55",
                            "BuildingsResidueChars.ExistsLinearSectionAutomorphicFunctionsOfFree:5-48",
                            "BuildingsResidueChars.ExistsSectionAutomorphicSpaceWithPrescribedValue:8-103"]
            },
            "fixed_hecke_family": {
                "definition": "H.Op=(H.Wp x Fin n) disjoint union (H.V x Fin n), where H.Wp consists of original split places outside fixed S union Q; the second factor gives the original positive diagonal operators above ell.",
                "retention": "Q, theta, tau and all residual eigenvalues remain fixed while compact auxiliary levels vary.",
                "sources": ["HeckeAlgebras.CoefficientRepTrivialOnUnramified:122-165",
                            "HeckeAlgebras.OrdinaryHeckeCharacters.HiComm:194-230",
                            "HeckeAlgebras.OrdinaryHeckeCharacters.PiBasic:197-260",
                            "HeckeAlgebras.OrdinaryHeckeCharacters.PiBasic:379-398"]
            },
            "faithful_diamond_quotient": {
                "retention": "U_Q projects trivially at each original auxiliary place; the original product section projects to each specified local coordinate, so no diamond factor is absorbed.",
                "sources": ["HeckeAlgebras.IsTheta:117-139",
                            "HeckeAlgebras.OrdinaryHeckeCharacters.LevelUR2Faith:14-41",
                            "PatchingModules.NilpotentLevelLowering.DelIso:202-218"]
            }
        },
        "external_cited_theorems": [{
            "author": "Armand Borel",
            "title": "Some finiteness properties of adele groups over number fields",
            "journal": "Publications Mathematiques de l'IHES 16 (1963), 5-30",
            "theorem": "Theorem 5.1, printed page 19",
            "doi": "10.1007/BF02684289",
            "primary_url": "https://www.numdam.org/item/PMIHES_1963__16__5_0.pdf",
            "reviewed_pdf_pages_zero_based": [3, 15],
            "use": "Finite double-coset set for the original definite unitary group, with compact-open level changed by commensurability.",
            "verification": "Primary PDF theorem and notation inspected with web retrieval; cited classical input, not reproved here."
        }],
        "sources": sources,
        "computation_scope": "No numerical sampling used; no Lean compilation or kernel verification.",
        "remaining": [
            "Original universal ordinary determinant action, compatible with weight characters and change of level",
            "Separation of every nonzero vector by original classical automorphic specializations with exact local Galois compatibility",
            "Original spherical/Iwahori comparison maps and their single uniform nilpotence exponent",
            "Full TWAut with original base support, patched support dimension, characteristic-prime propagation and final uniform integral Selmer bound"
        ],
        "reproduce": "python3 scripts/check_selmer_integral_frontier_ordinary_diamond.py --offline",
        "artifacts": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in artifacts},
    }
    (ROOT/f"certificates/{stem}.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "pinned_modules": len(sources),
                      "scope": report["verification_kind"]}))


if __name__ == "__main__":
    main()
