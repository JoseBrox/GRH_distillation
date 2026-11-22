#!/usr/bin/env python3
"""Authenticate bounded sources and artifacts for the finite-selection proof.

This records provenance, not a Lean build or an automated proof of the theorem.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
PA = "Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules."
RANGES = {
    "Development.AutomorphicArithmetic.AutomorphicVarieties.CommutativeAlgebra.ResMapBijective": [(334, 338)],
    PA+"DeterminantPadicFree.PhiSub": [(5, 31)],
    PA+"DeterminantPadicFree.LocallyConstantCocyclesFiniteOfPhi": [(5, 78)],
    PA+"DeterminantPadicFree.AcConst": [(51, 81)],
    PA+"DeterminantPadicFree.CharPOfPadic": [(25, 76)],
    PA+"DeterminantPadicFree.SelSub": [(38, 105)],
    PA+"DeterminantPadicFree.MaxIndep": [(5, 54)],
    PA+"DeterminantPadicFree.DetFin": [(127, 213)],
    PA+"DeterminantPadicFree.FinSub": [(5, 33)],
    PA+"DeterminantPadicFree.OmDense": [(34, 87)],
    PA+"PairedDualFirstOrderDualMatrixSpace": [(288, 315)],
    PA+"AutomorphicDetection.Choice": [(10, 40)],
    PA+"PatchedSupportCompletions": [(215, 230)],
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    atlas = json.loads(gzip.decompress((ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()))
    rows = {row[0]: row for row in atlas["modules"]}
    sources = []
    for module, ranges in RANGES.items():
        item = {"repository": atlas["repository"], "commit": atlas["commit"],
                "path": "lean/src/"+module.replace(".", "/")+".lean",
                "git_blob_sha1": rows[module][1]}
        checked = inspect_file(item, offline=args.offline)
        lines = (ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]).read_bytes().splitlines(keepends=True)
        excerpts = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines) and end-start+1 <= 120
            raw = b"".join(lines[start-1:end])
            assert len(raw) <= 12000
            excerpts.append({"start": start, "end": end,
                             "sha256": hashlib.sha256(raw).hexdigest()})
        sources.append({**item, "module": module, "sha256": checked["sha256"],
                        "matches_pinned_blob": True, "reviewed_excerpts": excerpts})
    artifacts = ["notes/selmer-integral-frontier-finite-selection.md",
                 "paper/shared/selmer-integral-frontier-finite-selection.tex",
                 "paper/shared/selmer-integral-frontier-finite-selection-references.tex",
                 "scripts/check_selmer_integral_frontier_finite_selection.py"]
    dependencies = ["certificates/selmer-integral-frontier-integral-detection.json"]
    report = {
        "schema_version": 1, "status": "PASS",
        "claim": "Authenticated source provenance and artifact integrity for the written finite-selection theorem.",
        "results": [
            "Finite free continuous cocycle module under the original open-subgroup finiteness hypothesis.",
            "Construction of the original independent odd Selmer family with all local witnesses and generation up to powers of the uniformizer.",
            "A basis of detecting forms over the fraction field preserves the exact integral common kernel.",
            "One finite set in the original cyclotomic kernel simultaneously detects at finitely many points and has separable characteristic polynomials at all points.",
            "Under these hypotheses, one denominator exponent suffices for all integral cocycles in the detecting kernel at each fixed point."
        ],
        "sources": sources,
        "preserved_hypotheses": ["Finite coefficient fields of odd characteristic ell", "Original nontrivial residual cyclotomic character", "Original open-subgroup finiteness condition", "Original cyclotomic kernel", "Original spectral density hypothesis at every point", "Original local Selmer conditions", "Continuity of original twisted representations"],
        "limits": ["This script authenticates source bytes and proof artifacts; it does not prove the mathematical statements.", "No Lean build was run.", "The denominator and cardinality bounds depend on the fixed points and residual actions.", "Equality of integral kernels does not imply equality of their reductions modulo t^a; no modular cocycle lifting is asserted.", "Arithmetic construction of the normalized points and their global group and spectral hypotheses remain retained.", "No whole node closes: ordinary RH 6/9, Dirichlet GRH 17/31."],
        "artifacts": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in artifacts},
        "dependencies": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        "reproduce": "python3 scripts/check_selmer_integral_frontier_finite_selection.py --offline"
    }
    (ROOT/"certificates/selmer-integral-frontier-finite-selection.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "pinned_modules": len(sources),
                      "scope": "source provenance and artifact integrity; human proof separate"}))


if __name__ == "__main__":
    main()
