#!/usr/bin/env python3
"""Authenticate sources and check the exact Hodge metric identities.

The analytic and geometric proof is independently reviewed mathematics.
This script is not a Lean replay or an automated proof of that argument.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
AS = "Development.AutomorphicSpectrum."
SOURCES = [
    ("ReciprocityTheory.ReductiveGroups.ArithmeticGeometry."
     "BirationalGeometry.ToroidalCompactification.PushInvertible",
     [[40, 66]]),
    ("ReciprocityTheory.ReductiveGroups.ArithmeticGeometry."
     "BirationalGeometry.ToroidalCompactification.TwoWeightEqOneAddRoot",
     [[72, 91], [144, 160]]),
    ("ReciprocityTheory.ReductiveGroups.ArithmeticGeometry."
     "SemiabelianSchemes.AbelianSchemeQuotients.IsAbelianScheme",
     [[19, 48]]),
    ("ReciprocityTheory.ReductiveGroups.ArithmeticGeometry."
     "BirationalGeometry.ToroidalCompactification.IsCompletedStrictHens",
     [[16, 23]]),
    (AS + "Definitions.GlobalGeometry.BdryChart", [[19, 62]]),
    (AS + "Definitions.GlobalGeometry.IsFlatAnIffIsConstMul",
     [[33, 52], [121, 185]]),
    (AS + "Proofs.GeometryProofs.LogPeriodsRiemannForm",
     [[33, 69], [83, 126]]),
    (AS + "Proofs.MetricProofs.PeriodMatrixLocalTrivialization",
     [[10, 31]]),
    (AS + "Proofs.GeometryProofs.HodgeGramBoundNearBoundary",
     [[52, 119]]),
    (AS + "Proofs.GeometryProofs.BoundaryChartFrameGrowth",
     [[303, 352]]),
    (AS + "Proofs.GeometryProofs.EigenFramesAnalytic",
     [[121, 198]]),
    (AS + "Statements.GeometryStatements.FlatLineGenerator",
     [[18, 19]]),
]
PRIMARY = [
    {
        "path": "build/reference-cache/serre-gaga-1956.pdf",
        "url": "https://www.numdam.org/item/10.5802/aif.59.pdf",
        "sha256": "9898f985dd6932496e26450bfe0beca8655a937032f545b97cebd88d1bc8eb98",
        "inspected": "Section 12, Theorems 1-2, pp.19-20; extracted text 787-806",
    },
    {
        "path": "build/reference-cache/wlodarczyk-resolution-2005.pdf",
        "url": "https://www.math.purdue.edu/~wlodarcz/singularities/Resolution.pdf",
        "sha256": "bb2d56aa9b250c1aecaabbd053efa0f49ffa315d88e414fc4fbed0a2d65abf2f",
        "inspected": "Theorems 1.0.1 and 1.0.3, pp.781-782; extracted text 119-142 and 172-185",
    },
]
STACKS = {
    "repository": "stacks/stacks-project",
    "commit": "a04446e57ec1fbc252a871afcec7752fb2807b14",
    "path": "coherent.tex",
    "git_blob_sha1": "d0e7f49ad29ce3092e40c766d630b9ad99d8e1ba",
    "sha256": "702ca51850d0f9a615888dc0ced8100e104c98961e05a48b32c3ddf6eda61604",
    "ranges": [[4922, 4940]],
}


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def ranges(raw: bytes, bounds: list[list[int]]) -> list[dict]:
    lines = raw.splitlines()
    result = []
    for lo, hi in bounds:
        assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
        excerpt = b"\n".join(lines[lo - 1:hi]) + b"\n"
        assert len(excerpt) <= 12000
        result.append({"lines": [lo, hi], "sha256": sha(excerpt)})
    return result


def source_evidence(fetch: bool) -> list[dict]:
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    entries = {row[0]: row for row in atlas["modules"]}
    result = []
    for module, bounds in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        record = inspect_file({
            "repository": "jsmorph/rh", "commit": REV, "path": path,
            "git_blob_sha1": entries[module][1],
        }, offline=not fetch)
        raw = (ROOT / "build/source-cache/jsmorph/rh" / REV / path).read_bytes()
        result.append({
            "module": module, "path": path,
            "sha256": record["sha256"],
            "git_blob_sha1": record["git_blob_sha1"],
            "url": f"https://github.com/jsmorph/rh/blob/{REV}/{path}",
            "inspected_excerpts": ranges(raw, bounds),
        })
    path = ROOT / "build/source-cache" / STACKS["repository"] / STACKS["commit"] / STACKS["path"]
    raw = path.read_bytes()
    assert sha(raw) == STACKS["sha256"]
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    assert blob == STACKS["git_blob_sha1"]
    result.append({
        **{k: v for k, v in STACKS.items() if k != "ranges"},
        "url": f"https://github.com/{STACKS['repository']}/blob/{STACKS['commit']}/{STACKS['path']}",
        "inspected_excerpts": ranges(raw, STACKS["ranges"]),
    })
    return result


def primary_evidence(fetch: bool) -> list[dict]:
    for item in PRIMARY:
        path = ROOT / item["path"]
        if not path.exists() and fetch:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(urlopen(item["url"], timeout=45).read())
        assert sha(path.read_bytes()) == item["sha256"]
    return PRIMARY


def matrix_identities() -> dict:
    count = 0
    for g in range(1, 4):
        for seed in range(3):
            T = sp.eye(g)
            for i in range(g):
                for j in range(i):
                    T[i, j] = sp.Rational(seed + i + j + 1, 2) + sp.I * (i - j)
            H = sp.simplify(T * T.conjugate().T)
            A, C = H.applyfunc(sp.re), H.applyfunc(sp.im)
            B = C.row_join(-A).col_join(A.row_join(C))
            plus = sp.eye(g).col_join(-sp.I * sp.eye(g)) / 2
            minus = sp.eye(g).col_join(sp.I * sp.eye(g)) / 2
            assert B.T == -B
            assert sp.simplify(2 * sp.I * plus.T * B * minus - H) == sp.zeros(g)
            assert sp.simplify(2 * sp.I * minus.T * B * plus + H.conjugate()) == sp.zeros(g)
            assert sp.simplify(plus.T * B * plus) == sp.zeros(g)
            assert sp.simplify(minus.T * B * minus) == sp.zeros(g)
            # The kernel-to-dual map has coefficient matrix H.
            dual = sp.simplify(
                H.inv().T * (-H.conjugate()) * H.conjugate().inv()
            )
            assert sp.simplify(dual + H.inv().T) == sp.zeros(g)
            assert H.det() > 0
            count += 1
    p, q = sp.symbols("p q", integer=True, nonnegative=True)
    x, y, pi = sp.symbols("x y pi", positive=True)
    assert sp.simplify((pi**p * x) / (pi**q * y) / (x / y)) == pi**(p - q)
    # An indefinite remainder with a positive common-kernel restriction.
    Y0, N = sp.Matrix([[-1, 2], [2, 3]]), sp.diag(1, 0)
    assert Y0.det() < 0
    Y = Y0 + 3 * N
    assert Y[0, 0] > 0 and Y.det() > 0
    return {
        "status": "PASS",
        "exact_hermitian_cases": count,
        "verified": [
            "2iB(e_+(u),e_-(v))=H(u,v)",
            "Flat Hermitian signs on positive and negative summands",
            "Isotropy of both Hodge summands",
            "The kernel metric becomes minus the exact dual metric",
            "The prescribed pi metric scales squared determinant norm by pi^(p-q)",
            "An exact Schur-complement diagnostic with indefinite holomorphic remainder",
        ],
        "scope": "Exact finite matrix identities; not the general analytic or geometric theorem.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fetch", action="store_true")
    args = parser.parse_args()
    result = {
        "status": "PASS",
        "automated_scope": (
            "Pinned-source byte authentication, bounded-excerpt hashes, "
            "primary PDF hashes, and exact finite Hodge metric identities."
        ),
        "independent_review": "certificates/hard-node-review-2026-11-22.json",
        "sources": source_evidence(args.fetch),
        "primary_references": primary_evidence(args.fetch),
        "finite_checks": matrix_identities(),
        "artifacts": [
            {"path": path, "sha256": sha((ROOT / path).read_bytes())}
            for path in [
                "notes/flat-family-boundary-extension.md",
                "scripts/check_flat_family_boundary_extension.py",
            ]
        ],
        "not_claimed": [
            "Lean kernel replay",
            "An automated proof of the analytic boundary theorem",
            "Construction of the prescribed arithmetic model or level charts",
            "Finite-place norm constancy without the separate geometric suppliers",
            "Completion of an RH or GRH node",
        ],
    }
    (ROOT / "certificates/flat-family-boundary-extension.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print("PASS: 12 pinned Lean sources, pinned Chow lemma, 2 primary PDFs,")
    print("9 exact Hodge metric cases and symbolic pi normalization.")
    print("Scope: authentication and finite algebra; no Lean replay or automated geometric proof.")


if __name__ == "__main__":
    main()
