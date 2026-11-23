#!/usr/bin/env python3
"""Authenticate the exact arithmetic tower interfaces; not a proof or Lean build."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    "CurveDVRSpecialization.HostFrameEx": [(22, 79)],
    "FrobeniusSmoothVectors.FrobeniusSplitPrimeDatum": [(19, 107)],
    "FrobeniusSmoothVectors.EtaleSimplicialCochainSchemeSectionExtensionNatu": [(99, 140)],
    "FrobeniusSmoothVectors.AuxwEx": [(26, 61)],
    "FrobeniusSmoothVectors.HthPlace": [(63, 111)],
    "FrobeniusSmoothVectors.HlayPlace": [(73, 132)],
    "FrobeniusSmoothVectors.Ufacts": [(78, 178), (179, 241)],
    "FrobeniusSmoothVectors.RankLeOfCardLe": [(137, 187)],
    "FrobeniusSmoothVectors.Strict": [(14, 80), (81, 174)],
    "FrobeniusSmoothVectors.StSel": [(31, 128)],
    "FrobeniusSmoothVectors.StCount": [(11, 76)],
    "FrobeniusSmoothVectors.FieldEx": [(24, 120), (121, 155)],
    "FrobeniusSmoothVectors.LinkEx": [(150, 240), (241, 308)],
    "FrobeniusSmoothVectors.FrameEx": [(52, 119), (120, 160)],
    "FrobeniusSmoothVectors.ContinuousCoboundaries2": [(167, 212)],
    "GaloisCochains.H2GaloisQuotientEq": [(87, 165)],
    "GaloisCochains.H2GaloisQuotientSurjective": [(50, 78)],
    "GaloisCochains.ConeCount": [(349, 371)],
    "GaloisCochains.CharacterH1GaloisQuotient": [(121, 150), (151, 260), (261, 310)],
    "FrobeniusSmoothVectors.SeedCl": [(23, 131)],
    "FrobeniusSmoothVectors.GenHost": [(85, 150), (151, 219), (220, 255)],
    "UnitaryThreeDeformations.IsHostFrame": [(12, 21)],
    "UnitaryThreeDeformations.DyadicCharacterPowerNeOne": [(50, 113), (202, 242)],
    "HeightAndVanishing.GdIffIndex": [(146, 220)],
    "FrobeniusSmoothVectors.SqrtDiscr": [(152, 215), (216, 284)],
    "FrobeniusSmoothVectors.HostEx": [(8, 26)],
    "FrobeniusSmoothVectors.GdEx": [(8, 25)],
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    lookup = {row[0]: row for row in atlas["modules"]}
    records = []
    for suffix, ranges in RANGES.items():
        module = PREFIX + suffix
        row = lookup[module]
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        item = {"repository": atlas["repository"], "commit": atlas["commit"],
                "path": path, "git_blob_sha1": row[1]}
        rec = inspect_file(item, args.offline)
        data = (ROOT / "build/source-cache" / atlas["repository"] /
                atlas["commit"] / path).read_bytes()
        lines = data.decode().splitlines()
        checked = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines)
            assert end - start + 1 <= 120
            excerpt = "\n".join(lines[start-1:end]).encode()
            checked.append({"start": start, "end": end, "sha256": sha(excerpt)})
        records.append({"module": module, "path": path,
                        "sha256": sha(data), "git_blob_sha1": row[1],
                        "ranges": checked, "source_check": rec})
    claims = {
        "classification": "Closed original HasFrame/HostFrameEx/GdFrameEx construction; no whole-node closure.",
        "construction": "The exact Upl fields, class-rank bound before the cyclotomic height, both strict classes, literal GalLink, all Ok/Big conditions, original seed and both original initial families.",
        "parity": "The compensated residual character is EVEN; both psi^(-a) eta are ODD for a=1,2.",
        "duality_count": "All global and real invariant terms vanish; only the auxiliary local term 2-1=1 survives.",
        "uniformity": "C0 is independent of m for one fixed initial abelian E; no uniformity in E or bound on Selmer orders.",
        "quotient_review": "Use inequality, not equality, for equivariant homomorphisms on the IMAGE of excluded inertia. No local decomposition embedding into G_{F,S'} is assumed.",
        "remaining": "Integral FinA from the now-constructed frame and uniform FinEnd, global two-sided rigidity, and moving-family weighted Selmer bound.",
        "scope": "Pinned-source authentication and source-range ledger only. Mathematical arguments are in the shared TeX file; no Lean rebuild or automated theorem proof.",
    }
    tracked = ["paper/shared/selmer-support-continuation-auxiliary-tower.tex",
               "paper/shared/selmer-support-continuation-auxiliary-frame.tex",
               "paper/shared/selmer-support-continuation-auxiliary-admission.tex",
               "paper/shared/selmer-support-continuation-auxiliary-tower-references.tex",
               "notes/selmer-support-continuation-auxiliary-tower.md"]
    output = {"source_repository": atlas["repository"], "source_commit": atlas["commit"],
              "claims": claims, "sources": records,
              "artifacts": [{"path": p, "sha256": sha((ROOT / p).read_bytes())} for p in tracked]}
    path = ROOT / "certificates/selmer-support-continuation-auxiliary-tower.json"
    path.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"certificate": str(path.relative_to(ROOT)),
                      "sources": len(records), "scope": claims["scope"]}))


if __name__ == "__main__":
    main()
