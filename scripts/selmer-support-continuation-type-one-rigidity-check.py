#!/usr/bin/env python3
"""Authenticate the exact source and primary theorem used for type-I rigidity."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
import urllib.request

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    "UnitaryThreeDeformations.IrrOpen": [(258, 279), (299, 338), (340, 382)],
    "UnitaryThreeDeformations.IrrCyc": [(38, 91)],
    "CurveDVRSpecialization.RatTorsionFree": [(21, 44)],
    "CurveDVRSpecialization.RankTwoAutomorphyDescendsFromAbelianCMToRat": [(16, 40)],
    "CurveDVRSpecialization.EveryPointSatisfiesFrameCondition": [(124, 131)],
    "WeilGroupCharacters.ArithmeticPointClassicality": [(82, 101)],
    "AutomorphicForms.BlochKatoSelmerVanishes": [(66, 98), (130, 148)],
    "UnitaryThreeGroups.GRepresents": [(123, 141)],
    "UnitaryThreeGroups.PtHypOf": [(64, 89)],
    "UnitaryThreeGroups.TanCocIsBK": [(187, 222)],
    "PadicHodgeTheory.DualCr": [(36, 62)],
}
PRIMARY_URL = "https://arxiv.org/pdf/2207.04925v1"
PRIMARY_SHA = "3bfd478657a9f38c79580bcf7d4cb64dfd071fe25f18d99b752a12c370d0d3cd"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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
        excerpts = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines)
            assert end - start + 1 <= 120
            excerpts.append({"start": start, "end": end,
                             "sha256": sha("\n".join(lines[start-1:end]).encode())})
        sources.append({"module": module, "path": path, "sha256": sha(data),
                        "git_blob_sha1": row[1], "ranges": excerpts,
                        "source_check": checked})

    primary = ROOT / "build/source-cache/primary/Thorne-2207.04925v1.pdf"
    if not primary.exists():
        if args.offline:
            raise RuntimeError("The authenticated Thorne manuscript is not cached.")
        primary.parent.mkdir(parents=True, exist_ok=True)
        request = urllib.request.Request(PRIMARY_URL, headers={"User-Agent": "GRH-distillation-source-audit/1"})
        with urllib.request.urlopen(request, timeout=60) as response:
            primary.write_bytes(response.read())
    assert sha(primary.read_bytes()) == PRIMARY_SHA

    files = ["paper/shared/selmer-support-continuation-type-one-rigidity.tex",
             "paper/shared/selmer-support-continuation-type-one-rigidity-references.tex",
             "notes/selmer-support-continuation-type-one-rigidity.md"]
    output = {
        "classification": "Closed original type-I rigidity subobligation; type-II and moving-family integral estimates remain separate.",
        "source_repository": atlas["repository"], "source_commit": atlas["commit"],
        "scope": "Actual ordinary points, actual auxiliary CM field and Hecke quotient, full polarized adjoint, all original dual-number lifts.",
        "local_distinction": "The residual mark lies in the multiplier-one decomposition group; the infinite-order character element lies in inertia. They need not coincide.",
        "local_finite_condition": "The previously proved crystalline-component comparison, including its exponent-one nonresonance and finite-extension descent, is retained.",
        "verification_scope": "Source authentication and primary-paper hash verification only. Mathematical proofs are in the shared TeX; no Lean rebuild or automated arithmetic proof is claimed.",
        "sources": sources,
        "primary": {"url": PRIMARY_URL, "version": "2207.04925v1", "sha256": PRIMARY_SHA,
                    "bytes": primary.stat().st_size, "pages_inspected": [3, 4, 24, 25],
                    "theorem": "Theorem 6.1 (also Theorem A)",
                    "journal_doi": "10.4310/PAMQ.2022.v18.n5.a5"},
        "artifacts": [{"path": path, "sha256": sha((ROOT / path).read_bytes())} for path in files],
    }
    dest = ROOT / "certificates/selmer-support-continuation-type-one-rigidity.json"
    dest.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"certificate": str(dest.relative_to(ROOT)), "sources": len(sources),
                      "primary_verified": True, "scope": output["verification_scope"]}))


if __name__ == "__main__":
    main()
