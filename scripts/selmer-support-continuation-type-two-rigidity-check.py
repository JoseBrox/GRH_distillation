#!/usr/bin/env python3
"""Authenticate type-II sources and check its exact matrix identities."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
import urllib.request

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    "UnitaryThreeGroups.CoboundaryLemmaNoColumn": [(135, 215)],
    "UnitaryThreeGroups.PowEqOneOfUnr": [(71, 129)],
    "UnitaryThreeGroups.DatFacts": [(66, 120)],
    "UnitaryThreeGroups.AdmissibleOfTypeII": [(110, 130)],
    "CurveDVRSpecialization.AutEnd2OfAutPt": [(273, 374)],
    "CurveDVRSpecialization.RankTwoAutomorphyDescendsFromAbelianCMToRat": [(16, 54)],
    "CurveDVRSpecialization.RatTorsionFree": [(46, 68)],
    "AutomorphicForms.Newform": [(21, 51)],
    "UnitaryThreeGroups.ReducibleThreeDim": [(263, 322), (323, 379)],
    "UnitaryThreeGroups.KatoUse": [(13, 34)],
    "UnitaryThreeGroups.PtHypOf": [(64, 89)],
}
PRIMARY = [
    {"file": "Kato-2004-p-adic-hodge-zeta.pdf",
     "url": "https://www.numdam.org/item/AST_2004__295__117_0.pdf",
     "sha256": "3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d",
     "pages_inspected": [234, 235, 240],
     "statements": "Section 14.1, Theorem 14.2(1), equations 14.10.2 and 14.10.3"},
    {"file": "BLGGT-potential-automorphy-change-weight.pdf",
     "url": "https://virtualmath1.stanford.edu/~rltaylor/pa3.pdf",
     "sha256": "0a3a56fb7ea2f598ef6c97edb64bffb7b4dcf80fb8a47ce67a8d567b9026a568",
     "pages_inspected": [35], "statements": "Lemmas 2.2.1 and 2.2.2",
     "journal_doi": "10.4007/annals.2014.179.2.3"},
    {"file": "Thorne-2207.04925v1.pdf",
     "url": "https://arxiv.org/pdf/2207.04925v1",
     "sha256": "3bfd478657a9f38c79580bcf7d4cb64dfd071fe25f18d99b752a12c370d0d3cd",
     "pages_inspected": [3, 4, 24, 25], "statements": "Theorem 6.1 and adjoint convention",
     "journal_doi": "10.4310/PAMQ.2022.v18.n5.a5"},
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def matrix_checks() -> dict:
    a, b, c, y, z, t, u0, u1, v0, v1 = sp.symbols("a b c y z t u0 u1 v0 v1")
    # The dense chart a!=0 of SL2 suffices for the polynomial identities.
    A = sp.Matrix([[a, b], [c, (1+b*c)/a]])
    J = sp.Matrix([[0, 1], [1, 0]])
    C = sp.diag(-1, 1)
    omega = sp.Matrix([[0, 1], [-1, 0]])
    Y = sp.Matrix([[y, z], [t, -y]])
    assert (J*A.inv().T*J - C*A*C).applyfunc(sp.simplify) == sp.zeros(2)
    assert -J*Y.T*J == C*Y*C
    assert -J*sp.eye(2)*J == -sp.eye(2)
    assert (omega*A.inv().T - A*omega).applyfunc(sp.simplify) == sp.zeros(2)
    u = sp.Matrix([u0, u1])
    v = sp.Matrix([[v0, v1]])
    w = omega*v.T
    assert -J*v.T == C*w
    assert -omega*J*u == C*u
    assert (u+w + u-w)/2 == u
    assert (u+w - (u-w))/2 == w
    alpha, beta = sp.symbols("alpha beta")
    assert sp.expand((alpha**2*beta**2+1)-beta**2*(alpha**2+1)) == 1-beta**2
    return {"polarization_on_SL2": True, "traceless_and_scalar_actions": True,
            "mixed_summands": True, "rank_two_trace_contradiction": True,
            "scope": "Exact symbolic identities; no arithmetic or analytic theorem is automated."}


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
            assert 1 <= start <= end <= len(lines) and end-start < 120
            excerpts.append({"start": start, "end": end,
                             "sha256": sha("\n".join(lines[start-1:end]).encode())})
        sources.append({"module": module, "path": path, "sha256": sha(data),
                        "git_blob_sha1": row[1], "ranges": excerpts,
                        "source_check": checked})
    primary = []
    for item in PRIMARY:
        path = ROOT / "build/source-cache/primary" / item["file"]
        if not path.exists():
            if args.offline:
                raise RuntimeError(f"The authenticated primary paper is not cached: {path.name}")
            path.parent.mkdir(parents=True, exist_ok=True)
            request = urllib.request.Request(item["url"], headers={"User-Agent": "GRH-distillation-source-audit/1"})
            with urllib.request.urlopen(request, timeout=60) as response:
                path.write_bytes(response.read())
        assert sha(path.read_bytes()) == item["sha256"]
        primary.append({**item, "bytes": path.stat().st_size})
    files = ["paper/shared/selmer-support-continuation-type-two-rigidity.tex",
             "paper/shared/selmer-support-continuation-type-two-rigidity-references.tex",
             "notes/selmer-support-continuation-type-two-rigidity.md"]
    output = {
        "classification": "Closed original good-data type-II rational rigidity subobligation; no whole-node completion.",
        "source_repository": atlas["repository"], "source_commit": atlas["commit"],
        "scope": "Every original Dat.gd, chosen local/global ring pair, type-II characteristic-zero point and algebra-valued dual-number lift.",
        "family_scope": "HostEnd requests only FinEnd and AutEnd3; GdEnd and PtHypOf quantify Dat and request the rank-two and two-sided conclusions. No HostData is silently strengthened.",
        "normalization": "W=V_g(e), weight(g)=2e+1; geometric Frobenius and determinant match Kato 14.10.2-3.",
        "remaining_frontier": "The moving-family integral congruence comparison and weighted Selmer budget are not bounded by rational rigidity.",
        "verification_scope": "Source and primary-paper authentication plus exact symbolic matrix checks. No Lean rebuild or automated arithmetic proof is claimed.",
        "sources": sources, "primary": primary, "matrix_checks": matrix_checks(),
        "artifacts": [{"path": path, "sha256": sha((ROOT/path).read_bytes())} for path in files],
    }
    dest = ROOT / "certificates/selmer-support-continuation-type-two-rigidity.json"
    dest.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"certificate": str(dest.relative_to(ROOT)), "sources": len(sources),
                      "primary_verified": len(primary), "matrix_checks": "passed",
                      "scope": output["verification_scope"]}))


if __name__ == "__main__":
    main()
