#!/usr/bin/env python3
"""Check bounded source provenance and exact algebra for coefficient freeness.

The written geometric/crystalline proof is independently reviewed; this script
does not prove it, reconstruct the boundary model, or run the Lean kernel.
Use --fetch-missing to retrieve only explicitly pinned missing source files.
"""
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
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
AS = "Development.AutomorphicSpectrum."
SOURCES = [
    ("Formalism.LocalToGlobal.ProjectiveLattices.IsChartIff", [[74, 117]]),
    ("Development.AbelianVarietyTheory.Definitions.Uniformization.ExistsInKNeOne",
     [[19, 35]]),
    (AS + "Definitions.GlobalGeometry.ToFirst", [[18, 42]]),
    (AS + "Definitions.GlobalGeometry.GermSys", [[47, 63]]),
    (AS + "Proofs.GeometryProofs.AbelianQuotientOfPowerFns", [[192, 225]]),
    (AS + "Proofs.GeometryProofs.AbelianQuotientLattice", [[423, 450]]),
    (AS + "Proofs.GeometryProofs.AbelianQuotientBilinear", [[27, 58]]),
    (AS + "Proofs.GeometryProofs.HeightCharFreeGeometric",
     [[29, 35], [76, 93], [230, 290]]),
    ("Development.WeilBound.CoreStatements.TorusUniformisation."
     "ChowMahlerFamilies.HodgeFreeEveryStalk", [[124, 173]]),
    (AS + "Proofs.GeometryProofs.ExistsHodgeLatticeGermSystem", [[85, 114]]),
    (AS + "Proofs.GeometryProofs.EigenLinePAdicBound", [[193, 251]]),
    (AS + "Proofs.GeometryProofs.FibreCurveGermPowers", [[215, 270]]),
]
PRIMARY = [
    {
        "path": "build/reference-cache/mazur-messing-1974.pdf",
        "url": "https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/mazur-messing.pdf",
        "sha256": "54486ccb86cad19118bfdb9d1e56386b18a45c63529254f1a1f7b7d110ca5eee",
        "inspected": [
            "I.2.1, printed p.13: pointed first-neighbourhood rigidifications",
            "I.2.6.7, pp.24-25: universal extension and arbitrary base change",
            "II.9, pp.93-94: finite locally free crystal",
            "II.13, pp.119-122: functorial abelian/p-divisible comparison",
            "II.15, pp.126-127: finite free Witt evaluation",
        ],
    },
    {
        "path": "build/reference-cache/conrad-units-product.pdf",
        "url": "https://math.stanford.edu/~conrad/papers/unitthm.pdf",
        "sha256": "0720c7f594d69049ebe70d804582a252fcd83852b6f530b3f52fabb7cee9e9e0",
        "inspected": [
            "Theorem 1.1, p.1: units factor on geometrically connected reduced products",
            "Sections 2-3, pp.1-3: proof by divisors at infinity",
        ],
    },
    {
        "path": "build/reference-cache/madapusi-pera-2019.pdf",
        "url": "https://www.numdam.org/item/10.24033/asens.2391.pdf",
        "sha256": "d7e0dfa1d9ef76f3f85682f1abcc52d3d66de9e9378e92fc9153a3ba5c10a077",
        "inspected": [
            "1.1.3-1.1.4, pp.404-405: integral one-motive realizations",
            "1.2-1.3.5, pp.405-408: exact degeneration/log-crystal hypotheses",
            "A.1.8-A.1.10, pp.500-501: monodromy construction and descent",
        ],
        "role": "Prospective next comparison; not used to claim the actual boundary construction.",
    },
]
ARTIFACTS = [
    "notes/boundary-hodge-freeness.md",
    "scripts/check_boundary_hodge_freeness.py",
]


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def check_sources(fetch: bool) -> list[dict]:
    raw_graph = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(raw_graph) == inventory["compressed_graph"]["sha256"]
    graph = json.loads(gzip.decompress(raw_graph))
    assert graph["repository"] == "jsmorph/rh" and graph["commit"] == REV
    entries = {row[0]: row for row in graph["modules"]}
    result = []
    for module, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        item = {
            "repository": "jsmorph/rh", "commit": REV, "path": rel,
            "git_blob_sha1": entries[module][1],
        }
        record = inspect_file(item, offline=not fetch)
        path = ROOT / "build/source-cache/jsmorph/rh" / REV / rel
        raw = path.read_bytes()
        lines = raw.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            excerpt = b"\n".join(lines[lo - 1:hi]) + b"\n"
            assert len(excerpt) <= 12000, (module, lo, hi)
            excerpts.append({"lines": [lo, hi], "sha256": sha(excerpt)})
        result.append({
            "module": module, "path": rel,
            "sha256": record["sha256"],
            "git_blob_sha1": record["git_blob_sha1"],
            "url": f"https://github.com/jsmorph/rh/blob/{REV}/{rel}",
            "inspected_excerpts": excerpts,
        })
    return result


def check_primary(fetch: bool) -> list[dict]:
    for item in PRIMARY:
        path = ROOT / item["path"]
        if not path.exists() and fetch:
            path.parent.mkdir(parents=True, exist_ok=True)
            with urllib.request.urlopen(item["url"], timeout=50) as stream:
                path.write_bytes(stream.read())
        assert sha(path.read_bytes()) == item["sha256"], item["path"]
    return PRIMARY


def zero(matrix):
    return all(sp.expand(x) == 0 for x in matrix)


def exact_matrix_identities() -> dict:
    # Generic blocks: torus rank 1 and abelian tangent dimension 2.
    # Entries are independent integer polynomial variables. The paper proves
    # the dimension-independent statement; this checks its signs and maps.
    ta, tb, x1, x2, y1, y2 = sp.symbols("ta tb x1 x2 y1 y2")
    ua = sp.Matrix(2, 2, sp.symbols("a0:4"))
    ub = sp.Matrix(2, 2, sp.symbols("b0:4"))
    rho = sp.zeros(3)
    rhob = sp.zeros(3)
    rho[0, 0], rhob[0, 0] = ta, tb
    rho[0, 1], rho[0, 2] = x1, x2
    rhob[0, 1], rhob[0, 2] = y1, y2
    rho[1:3, 1:3], rhob[1:3, 1:3] = ua, ub
    pmap = sp.Matrix([[0, 1, 0], [0, 0, 1]])
    c = sp.Matrix(2, 2, sp.symbols("c0:4"))
    z = sp.Matrix(3, 3, sp.symbols("z0:9"))
    pulled = pmap.T * c * pmap
    original = pulled - rho.T * z + z * rhob

    def haction(r, rb, coeff):
        d = r.rows
        return r.row_join(sp.zeros(d)).col_join((-coeff.T).row_join(rb.T))

    old = haction(rho, rhob, original)
    new = haction(rho, rhob, pulled)
    gauge = sp.eye(3).row_join(sp.zeros(3)).col_join(z.T.row_join(sp.eye(3)))
    assert zero(old * gauge - gauge * new)

    toric_projection = sp.Matrix([[0, 0, 0, 1, 0, 0]])
    assert zero(toric_projection * new - tb * toric_projection)
    kernel_inclusion = sp.zeros(6, 5)
    for column, row in enumerate([0, 1, 2, 4, 5]):
        kernel_inclusion[row, column] = 1
    kernel_action = kernel_inclusion.T * new * kernel_inclusion
    assert zero(new * kernel_inclusion - kernel_inclusion * kernel_action)
    quotient = sp.zeros(4, 5)
    for i in range(4):
        quotient[i, i + 1] = 1
    abelian = haction(ua, ub, c)
    assert zero(quotient * kernel_action - abelian * quotient)
    toric_inclusion = sp.Matrix([1, 0, 0, 0, 0])
    assert zero(kernel_action * toric_inclusion - ta * toric_inclusion)
    assert toric_projection.rank() == 1 and kernel_inclusion.rank() == 5
    assert quotient.rank() == 4 and toric_inclusion.rank() == 1
    assert zero(toric_projection * kernel_inclusion)
    assert zero(quotient * toric_inclusion)
    return {
        "ring": "Integer polynomial ring in independent matrix entries",
        "generic_block_dimensions": {"torus": 1, "abelian_tangent": 2, "hodge": 6},
        "identities_checked": [
            "Original action times gauge equals gauge times pulled-back action",
            "Equivariance of conjugate dual toric projection",
            "Stability and exact image of its kernel",
            "Equivariance and exact kernel of the abelian quotient",
            "Correct original-action toric submodule",
        ],
        "scope": "Exact polynomial sign/map checks, not a machine proof in all dimensions.",
    }


def rank_mod_p(matrix, p):
    a = [[int(x) % p for x in row] for row in matrix.tolist()]
    rank = 0
    for col in range(matrix.cols):
        pivot = next((i for i in range(rank, matrix.rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][col], -1, p)
        a[rank] = [(x * inverse) % p for x in a[rank]]
        for i in range(matrix.rows):
            if i != rank:
                factor = a[i][col]
                a[i] = [(x - factor * y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def gaussian_integer_diagnostic() -> dict:
    regular_i = sp.Matrix([[0, -1], [1, 0]])
    identity_i = sp.eye(2)
    cases = 0
    for a in range(2):
        for b in range(2):
            left = (a * sp.eye(2) + b * regular_i).charpoly().all_coeffs()
            right = (a * sp.eye(2) + b * identity_i).charpoly().all_coeffs()
            assert [int(x) % 2 for x in left] == [int(x) % 2 for x in right]
            cases += 1
    assert rank_mod_p(regular_i - sp.eye(2), 2) == 1
    assert rank_mod_p(identity_i - sp.eye(2), 2) == 0
    possible_lifts = 0
    for code in range(16):
        n = sp.Matrix(2, 2, [(code >> j) & 1 for j in range(4)])
        jlift = sp.eye(2) + 2 * n
        if all(int(x) % 4 == 0 for x in jlift * jlift + sp.eye(2)):
            possible_lifts += 1
    assert possible_lifts == 0
    return {
        "ring": "Z[i] at p=2",
        "residue_character_cases": cases,
        "nilpotent_action_rank": {"regular": 1, "diagnostic": 0},
        "all_mod4_lifts_of_identity_checked": 16,
        "mod4_lifts_squaring_to_minus_identity": possible_lifts,
        "scope": "Exact diagnostic for insufficiency of the regular character alone.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch-missing", action="store_true")
    args = parser.parse_args()
    sources = check_sources(args.fetch_missing)
    primary = check_primary(args.fetch_missing)
    matrix = exact_matrix_identities()
    diagnostic = gaussian_integer_diagnostic()
    artifacts = [{"path": rel, "sha256": sha((ROOT / rel).read_bytes())}
                 for rel in ARTIFACTS]
    certificate = {
        "result": "PASS",
        "scope": "Automated source/PDF provenance and exact algebra checks only.",
        "source_repository": "jsmorph/rh",
        "source_revision": REV,
        "source_count": len(sources),
        "sources": sources,
        "primary_references": primary,
        "exact_matrix_checks": matrix,
        "exact_ramification_diagnostic": diagnostic,
        "artifacts": artifacts,
        "written_result": (
            "The actual proper formal module is the tangent module of a rigidified "
            "universal extension. Its Witt crystal gives coefficient-factor "
            "projectivity. A same-line-bundle gauge and three-step toric filtration "
            "extend this to the semiabelian fibre. The regular character gives a "
            "common coefficient rank, which lifts to the same local stalk."
        ),
        "independent_review": {
            "record": "certificates/hard-node-review-2026-11-22.json",
            "scope": "Separate mathematical review, not performed by this checker.",
        },
        "remaining_open": [
            "Construct the prescribed boundary quotient and self-dual pullback line on the chosen model.",
            "Identify compatible Hodge and conjugate filtrations on the exact lattice on required test curves.",
            "Complete actual-model/logarithmic-crystal comparison if that alternative is used.",
            "Supply the independent integral CM evaluation, finite section and cusp inputs.",
        ],
        "not_verified": [
            "Transitive Lean source proofs or Lean kernel replay",
            "Actual boundary-model construction",
            "The full geometric hard node or RH/GRH endpoint",
        ],
        "node_counts": {"RH": [6, 9], "GRH": [17, 31]},
    }
    target = ROOT / "certificates/boundary-hodge-freeness.json"
    target.write_text(json.dumps(certificate, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "result": "PASS", "source_count": len(sources),
        "primary_pdf_count": len(primary),
        "certificate": str(target.relative_to(ROOT)),
        "scope": certificate["scope"],
    }))


if __name__ == "__main__":
    main()
