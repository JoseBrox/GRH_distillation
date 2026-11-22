#!/usr/bin/env python3
"""Authenticate the actual ordinary/classical specialization interfaces.

This checks pinned source and artifact provenance, not a Lean build
or a numerical substitute for the mathematical proof.
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
    "HeckeAlgebras.ContinuousTorusCharacter": [(118, 145), (151, 230), (245, 246)],
    "HeckeAlgebras.CoefficientRepTrivialOnUnramified": [(145, 176), (216, 249)],
    "HeckeAlgebras.Distinct": [(51, 66)],
    "HeckeAlgebras.IsTheta": [(123, 159)],
    "HeckeAlgebras.OrdinaryHeckeCharacters.UOpLevel": [(20, 93)],
    "HeckeAlgebras.OrdinaryHeckeCharacters.OrdFree": [(357, 413), (441, 445)],
    "HeckeAlgebras.OrdinaryHeckeCharacters.HiComm": [(194, 230)],
    "HeckeAlgebras.OrdinaryHeckeCharacters.SpecIntIff": [(100, 145), (146, 201)],
    "WeilGroupCharacters.LamFree": [(45, 78), (150, 190)],
    "HeckeAlgebras.OrdinaryHeckeCharacters.WeightVariablesExist": [(13, 46)],
    "ModularityArgument.ThresholdArguments.DenseThresholdCases.TDenseU": [(374, 457)],
    "ModularityArgument.ThresholdArguments.DenseThresholdCases.ExistsHeckeIdeal": [(70, 83)],
    "ModularityArgument.ThresholdArguments.DenseThresholdCases.VLPiPts": [(179, 207), (226, 277)],
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
        item = {
            "repository": atlas["repository"],
            "commit": atlas["commit"],
            "path": "lean/src/"+module.replace(".", "/")+".lean",
            "git_blob_sha1": rows[module][1],
        }
        checked = inspect_file(item, args.offline)
        cache = ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]
        lines = cache.read_bytes().splitlines(keepends=True)
        excerpts = []
        for start, end in intervals:
            assert 1 <= start <= end <= len(lines) and end-start+1 <= 120
            data = b"".join(lines[start-1:end])
            assert len(data) <= 12000
            excerpts.append({
                "start": start, "end": end,
                "sha256": hashlib.sha256(data).hexdigest(),
            })
        sources.append({
            **item, "module": module, "sha256": checked["sha256"],
            "matches_pinned_blob": True, "reviewed_excerpts": excerpts,
        })
    stem = "selmer-integral-frontier-classical-control"
    artifacts = [
        f"notes/{stem}.md",
        f"paper/shared/{stem}.tex",
        f"paper/shared/{stem}-references.tex",
        "scripts/check_selmer_integral_frontier_classical_control.py",
    ]
    for path in artifacts:
        assert all(c >= 32 or c in (9, 10) for c in (ROOT/path).read_bytes()), path
    dependency_paths = [
        "notes/selmer-integral-frontier-ordinary-diamond.md",
        "certificates/selmer-integral-frontier-ordinary-diamond.json",
    ]
    report = {
        "schema_version": 1,
        "status": "PASS",
        "verification_kind": "Pinned source provenance and artifact hashes; standard mathematical proofs are in the note.",
        "classification": "closed subobligation inside W04: exact actual ordinary base change and faithful good weight-zero classical specialization",
        "claim": "The original ordinary modules commute with every continuous local coefficient map; finite-order torus weights supply the full weight-zero specialization interface, and principal-cyclotomic-shifted torsion points with distinct local characters detect every nonzero vector.",
        "quantifiers": [
            "Fix the original Hida datum, type, weight ring A, auxiliary set Q and original Hecke family.",
            "For every original compact auxiliary level K and every continuous local O-algebra map A to complete Noetherian local B with finite residue field, pointwise ordinary base change is an isomorphism.",
            "For every finite coefficient field E and every such map A to O_E with finite-order torus character, one congruence depth c0 depending on the character works for all K.",
            "For every nonzero element of A, at least one good weight-zero specialization has nonzero value; the same holds for each nonzero original ordinary vector.",
        ],
        "proved_steps": [
            "At a common finite coefficient precision and congruence level, the original double-coset coordinate modules and actual U matrices base change exactly.",
            "Split invertible/nilpotent Fitting decompositions survive nonflat coefficient maps and give the exact finite-level ordinary module.",
            "The compatible finite-precision isomorphisms give ordinary base change over complete coefficient rings.",
            "The original residual joint Hecke idempotent, all fixed Hecke operators, diamond actions, traces and auxiliary translations are preserved.",
            "A finite-order torus character gives one exact opposite-unipotent congruence level for every integral ordinary vector.",
            "The integral ordinary lattice equals the unit-slope classical space after extending scalars.",
            "Weight zero has trivial algebraic representation and lowW=0, so all original Hecke normalization factors are exactly one.",
            "Principal-cyclotomic twists preserve both residual and prescribed torsion character restrictions and produce actual finite-order torus specializations.",
            "The least-unit-coefficient valuation argument proves multivariable torsion density with the required distinct-character exclusions.",
        ],
        "decisive_source_interfaces": {
            "ordinary_module": {
                "dependency": "selmer-integral-frontier-ordinary-diamond",
                "retained_objects": "The same original arithmetic double cosets, type lattice, U sum and uniformizers, congruence groups, tame levels, and residual summand.",
                "sources": [
                    "HeckeAlgebras.ContinuousTorusCharacter:118-230",
                    "HeckeAlgebras.OrdinaryHeckeCharacters.UOpLevel:20-93",
                    "HeckeAlgebras.OrdinaryHeckeCharacters.OrdFree:357-413",
                ],
            },
            "coefficient_change": {
                "hypotheses": "A to B is continuous and local; both are complete Noetherian local O-algebras with finite residue fields. Choose N mapping m_A^N into m_B^k and c making theta(T_c)=1 modulo m_A^N.",
                "mechanism": "Tensor the actual split finite Fitting decomposition; then take the compatible inverse limit of finite free ordinary modules.",
                "nonflatness": "No flatness and no general commutation of invariants with base change are assumed.",
            },
            "weight_zero": {
                "identity": "lowW(lambda,i)=lambda(i.rev), hence lowW(0,i)=0; algPow and lowVal are one, so original unnormalized Hecke operators remain unchanged.",
                "full_specification": "Trivial algebraic representation, one exact torus depth, finite-dimensional classical space, stable integral Hecke operators, integral eigenvalues, semilinearity, spanning, independence, Hecke equivariance and auxiliary equivariance.",
                "sources": [
                    "HeckeAlgebras.Distinct:51-66",
                    "HeckeAlgebras.CoefficientRepTrivialOnUnramified:167-176",
                    "HeckeAlgebras.CoefficientRepTrivialOnUnramified:216-249",
                    "HeckeAlgebras.OrdinaryHeckeCharacters.SpecIntIff:100-201",
                ],
            },
            "original_weight_coordinates": {
                "identity": "1+X_(v,i,j)=psi0_(v,i)(gamma_(v,j))^-1*kappa_(v,i)(gamma_(v,j)).",
                "dimension": "D=n*sum_v [F_v:Q_ell]=n*[F:Q]; no conductor-one reduction in D is assumed.",
                "sources": [
                    "WeilGroupCharacters.LamFree:45-78",
                    "WeilGroupCharacters.LamFree:150-190",
                    "HeckeAlgebras.OrdinaryHeckeCharacters.WeightVariablesExist:13-46",
                ],
            },
            "arithmetic_specializations": {
                "construction": "kappa_x=psi0*<epsilon>^(-i)*chi, where psi0 is the finite-order lift retaining the original torsion character and chi is any finite-order character of the free pro-ell inertial quotient.",
                "exact_normalization": "kappa(g)*epsilon(g)^i*theta(e_(v,i)(Art(g)))=1, hence theta_x=(psi0*omega_epsilon^i*chi)^-1.",
                "torsion": "ell is odd, so 1+ell Z_ell is torsion-free; the principal cyclotomic twist is trivial on the prescribed finite local torsion subgroup.",
                "density": "Use the invertible substitution X=u(1+T)-1 and the least-unit-coefficient valuation argument at T=zeta-1, permitting the finite exclusions that force local characters to be distinct.",
                "sources": [
                    "HeckeAlgebras.IsTheta:143-159",
                    "HeckeAlgebras.CoefficientRepTrivialOnUnramified:167-176",
                    "ModularityArgument.ThresholdArguments.DenseThresholdCases.TDenseU:374-457",
                ],
            },
            "actual_consumer": {
                "fact": "The source construction of the original Hecke ideal chooses the identically zero algebraic weight.",
                "source": "ModularityArgument.ThresholdArguments.DenseThresholdCases.ExistsHeckeIdeal:70-83",
            },
        },
        "cited_external_theorem": {
            "author": "J. S. Milne",
            "title": "Class Field Theory",
            "version": "4.03, 2020-08-06",
            "location": "Chapter I, Theorems 1.1 and 1.4 and paragraphs 1.10-1.11, printed pages 20,22-24",
            "url": "https://www.jmilne.org/math/CourseNotes/CFT.pdf",
            "verification": "Author's primary PDF opened and exact statements checked through web retrieval; not a local external-PDF byte-hash claim.",
            "use": "Local reciprocity identifies the abelianized Galois inertia quotient with local units. The local rank and all density assertions are proved separately in the note.",
        },
        "limitations": [
            "No whole W04 or other proof-map node is completed.",
            "No bound is claimed for specialization conductors, finite coefficient extensions, arithmetic dimensions or module ranks.",
            "Classical functions detect vectors; classical Hecke eigencharacters separating the Hecke algebra is not inferred.",
            "The original continuous ordinary Galois determinant action, exact Galois-compatible classical constituents, full TWAut datum, patched support and uniform integral Selmer bounds remain separate obligations.",
            "Neither the source Lean project nor the full RH/GRH proof is certified by this script.",
        ],
        "dependencies": [
            {"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
            for p in dependency_paths
        ],
        "sources": sources,
        "artifacts": [
            {"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
            for p in artifacts
        ],
    }
    target = ROOT/"certificates"/f"{stem}.json"
    target.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({
        "status": "PASS", "modules": len(sources),
        "certificate": str(target.relative_to(ROOT)),
        "scope": report["verification_kind"],
    }))


if __name__ == "__main__":
    main()
