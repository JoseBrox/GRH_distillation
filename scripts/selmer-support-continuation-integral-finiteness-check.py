#!/usr/bin/env python3
"""Check pinned interfaces and the finite rank-three zero-pattern argument."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    "AutomorphicCases.AutomorphyUnramifiedCoefficients": [(9, 27)],
    "UnitaryThreeGroups.GRepresents": [(111, 138)],
    "CurveDVRSpecialization.RatTorsionFree": [(21, 32)],
    "PadicHodgeTheory.IsInertiaInfiniteCyclotomic": [(12, 35), (72, 138)],
    "PadicHodgeTheory.CommutingUpperTriangularDistinct": [(113, 167)],
    "PadicHodgeTheory.ValuationRingClearLastRowEntry": [(150, 246)],
    "CurveDVRSpecialization.TriangularOfReducibleRankThree": [(88, 143), (190, 233)],
    "CurveDVRSpecialization.ConstOfAlg": [(7, 16)],
    "CurveDVRSpecialization.ConstOfChar": [(185, 294)],
    "UnitaryThreeGroups.ExistsCoordOfNotMatIrr": [(45, 123)],
    "CommutativeAlgebra.CoordGrading": [(29, 93)],
    "CurveDVRSpecialization.FinCrit": [(45, 121), (122, 186)],
    "CurveDVRSpecialization.GfResZpow": [(67, 138), (139, 205)],
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def pattern_check() -> dict:
    """Matrix-unit support is transitive and invariant under anti-transpose."""
    off = [(i, j) for i in range(3) for j in range(3) if i != j]
    diagonal = {(i, i) for i in range(3)}
    patterns = []
    for bits in itertools.product((0, 1), repeat=6):
        edges = diagonal | {edge for edge, bit in zip(off, bits) if bit}
        if any((2-j, 2-i) not in edges for i, j in edges):
            continue
        if any((i, j) in edges and (j, k) in edges and (i, k) not in edges
               for i, j, k in itertools.product(range(3), repeat=3)):
            continue
        full = len(edges) == 9
        outer_irreducible = ((0, 2) in edges and (2, 0) in edges)
        upper = all(i <= j for i, j in edges)
        lower = all(j <= i for i, j in edges)
        block = not any((i, j) in edges for i, j in ((0, 1), (1, 0), (1, 2), (2, 1)))
        assert full or upper or lower or (block and outer_irreducible)
        if not full and not outer_irreducible:
            assert upper or lower
        patterns.append({"entries": sorted(edges), "full": full,
                         "upper": upper, "lower": lower,
                         "outer_irreducible": outer_irreducible})
    assert patterns
    return {"candidate_off_diagonal_patterns": 64,
            "symmetric_multiplicatively_closed_patterns": len(patterns),
            "all_patterns": patterns,
            "scope": "Exact finite enumeration of possible matrix-unit support. It does not prove the trace, flag, curve or finiteness theorems."}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    lookup = {row[0]: row for row in atlas["modules"]}
    sources = []
    for suffix, ranges in RANGES.items():
        module = PREFIX + suffix
        row = lookup[module]
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        entry = {"repository": atlas["repository"], "commit": atlas["commit"],
                 "path": path, "git_blob_sha1": row[1]}
        checked = inspect_file(entry, args.offline)
        data = (ROOT / "build/source-cache" / atlas["repository"] /
                atlas["commit"] / path).read_bytes()
        lines = data.decode().splitlines()
        excerpt_records = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines), (module, start, end, len(lines))
            assert end - start + 1 <= 120
            excerpt_records.append({"start": start, "end": end,
                                    "sha256": sha("\n".join(lines[start-1:end]).encode())})
        sources.append({"module": module, "path": path, "sha256": sha(data),
                        "git_blob_sha1": row[1], "ranges": excerpt_records,
                        "source_check": checked})
    files = ["paper/shared/selmer-support-continuation-integral-finiteness.tex",
             "paper/shared/selmer-support-continuation-integral-finiteness-references.tex",
             "notes/selmer-support-continuation-integral-finiteness.md"]
    output = {
        "source_repository": atlas["repository"], "source_commit": atlas["commit"],
        "classification": "Closed original FinA subobligation, with all original U/S quantifiers.",
        "integral_scope": "The actual unsaturated, possibly nonreduced global ring is retained; weight-zero projection gives exact pi-ideal contraction.",
        "local_scope": "A decomposition-group mark with distinct residual eigenvalues gives universal Hensel spectral projectors. Specialization to the characteristic-zero base point fixes the order on each selected component; the equations survive their intersection, also at ell=3. No distinct residual inertia mark is assumed.",
        "remaining": "Two-sided characteristic-zero global rigidity and the moving-family weighted integral Selmer bound. No effective nilpotence or torsion exponent is supplied.",
        "verification_scope": "Pinned-source authentication and finite matrix-support enumeration only; mathematical proofs are in the shared TeX, with no Lean rebuild.",
        "pattern_check": pattern_check(), "sources": sources,
        "artifacts": [{"path": path, "sha256": sha((ROOT / path).read_bytes())} for path in files],
    }
    dest = ROOT / "certificates/selmer-support-continuation-integral-finiteness.json"
    dest.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"certificate": str(dest.relative_to(ROOT)), "sources": len(sources),
                      "patterns": output["pattern_check"]["symmetric_multiplicatively_closed_patterns"],
                      "scope": output["verification_scope"]}))


if __name__ == "__main__":
    main()
