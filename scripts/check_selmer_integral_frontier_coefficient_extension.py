#!/usr/bin/env python3
"""Authenticate extension sources and check the ramified recombination exactly.

The written proof covers arbitrary complete DVRs. Finite polynomial examples
below are checks of its sensitive unit and ramification factors, not a proof
by sampling or a Lean build.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
PA = "Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules."
RANGES = {
    PA+"PairedDualFirstOrderDualMatrixSpace": [(232, 274), (306, 315)],
    PA+"PatchedSupportCompletions": [(220, 230)],
    PA+"DeterminantPadicFree.FrameWith": [(78, 79)],
    PA+"DeterminantPadicFree.ExtFree": [(5, 57)],
    PA+"DeterminantPadicFree.CompSel": [(18, 91)],
    PA+"DeterminantPadicFree.PushSel": [(21, 79)],
    PA+"DeterminantPadicFree.KapPush": [(8, 71)],
    PA+"DeterminantPadicFree.DetPush": [(77, 167)],
    PA+"DeterminantPadicFree.CharPOfPadicAlt": [(26, 59)],
    PA+"DeterminantPadicFree.PadicHomUnique": [(84, 140), (142, 163)],
    PA+"AutomorphicDetection.Choice": [(10, 40)],
}


def ramification_checks():
    cases = 0
    omitted_unit_rejections = 0
    omitted_ramification_rejections = 0
    for p in (3, 5):
        for e in (1, 2, 3):
            for v in range(1, p):
                # Exact polynomials in F_p[u]; t maps to v*u^e.
                y = {j: (j*j+j+1) % p for j in range(5*e+3)}
                y = {j: a for j, a in y.items() if a}
                projections = [{(j-i)//e: a*pow(v, -(j-i)//e, p) % p
                                for j, a in y.items() if j % e == i}
                               for i in range(e)]
                reconstructed = {}
                for i, coord in enumerate(projections):
                    for j, a in coord.items():
                        reconstructed[e*j+i] = a*pow(v, j, p) % p
                assert reconstructed == y
                for exponents in itertools.product(range(3), repeat=e):
                    N = max(exponents)
                    combined = {}
                    wrong_unit = {}
                    for i, (coord, s) in enumerate(zip(projections, exponents)):
                        coefficient = pow(v, -N, p)*pow(v, N-s, p) % p
                        shift = i+e*(N-s)
                        for j, a in coord.items():
                            degree = shift+e*(s+j)
                            value = coefficient*a*pow(v, s+j, p) % p
                            combined[degree] = (combined.get(degree, 0)+value) % p
                            bad = pow(v, N-s, p)*a*pow(v, s+j, p) % p
                            wrong_unit[degree] = (wrong_unit.get(degree, 0)+bad) % p
                    combined = {j: a for j, a in combined.items() if a}
                    wrong_unit = {j: a for j, a in wrong_unit.items() if a}
                    target = {j+e*N: a for j, a in y.items()}
                    assert combined == target
                    if pow(v, N, p) != 1:
                        assert wrong_unit != target
                        omitted_unit_rejections += 1
                    if e > 1 and N > 0:
                        wrong_power = {j+N: a for j, a in y.items()}
                        assert combined != wrong_power
                        omitted_ramification_rejections += 1
                    # The projection continuity exponent: degrees >= e*N
                    # have coordinate t-orders >= N, regardless of v.
                    for i in range(e):
                        assert all((j-i)//e >= N for j in range(e*N, e*N+3*e)
                                   if j % e == i)
                    cases += 1
    assert omitted_unit_rejections and omitted_ramification_rejections
    return {"cases": cases, "characteristics": [3, 5], "ramification_indices": [1, 2, 3],
            "identities": ["Finite free coordinate reconstruction", "Projection continuity with exponent e*N", "Maximum-exponent polarized-boundary recombination, including the unit v^(-N)"],
            "omitted_unit_rejections": omitted_unit_rejections,
            "omitted_ramification_rejections": omitted_ramification_rejections,
            "scope": "Exact finite polynomial checks over prime fields; the general proof is written separately."}


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
    artifacts = ["notes/selmer-integral-frontier-coefficient-extension.md",
                 "paper/shared/selmer-integral-frontier-coefficient-extension.tex",
                 "paper/shared/selmer-integral-frontier-coefficient-extension-references.tex",
                 "scripts/check_selmer_integral_frontier_coefficient_extension.py"]
    dependencies = ["certificates/selmer-integral-frontier-integral-detection.json",
                    "certificates/selmer-integral-frontier-finite-selection.json"]
    report = {
        "schema_version": 1, "status": "PASS",
        "claim": "Authenticated source provenance and exact ramified coefficient checks supporting the written simultaneous-choice proof.",
        "result": "The original odd Selmer family and paired detection survive a finite ramified coefficient extension; splitting and common residue-field extension finish the original simultaneous auxiliary choice.",
        "sources": sources, "exact_checks": ramification_checks(),
        "primary_references": [{"url": "https://stacks.math.columbia.edu/tag/09E8", "role": "Finite integral closure in a separable extension; one prime over a complete DVR."}, {"url": "https://stacks.math.columbia.edu/tag/0C0S", "role": "Equal-characteristic complete regular local ring as power series over its residue field."}],
        "preserved_hypotheses": ["Original normalized points and local Selmer conditions", "Original cyclotomic kernel and nontrivial residual cyclotomic character", "Original open-subgroup finiteness condition", "Original spectral density hypothesis", "Finite injective local extensions, including ramification", "Distinct roots need not have unit differences"],
        "limits": ["These checks support the written mathematical proof; no Lean build was run.", "The local normalized-point construction is transported; construction of the original arithmetic points is retained.", "No modular cocycle lifting or uniformity over moving arithmetic families is asserted.", "No whole node closes: ordinary RH 6/9, Dirichlet GRH 17/31."],
        "artifacts": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in artifacts},
        "dependencies": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        "reproduce": "python3 scripts/check_selmer_integral_frontier_coefficient_extension.py --offline"
    }
    (ROOT/"certificates/selmer-integral-frontier-coefficient-extension.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "pinned_modules": len(sources),
                      "ramified_recombination_cases": report["exact_checks"]["cases"],
                      "scope": "source provenance and exact coefficient checks; human proof separate"}))


if __name__ == "__main__":
    main()
