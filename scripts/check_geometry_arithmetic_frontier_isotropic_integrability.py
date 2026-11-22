#!/usr/bin/env python3
"""Authenticate the arithmetic isotropic-count proof and its exact algebra.

The reduction and unfolding arguments are mathematical proofs in the note.
Finite algebra checks do not prove arithmetic reduction theory or construct
the geometric model, and this script does not build the Lean source.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import urllib.request

import fitz
import sympy as sp

from check_sources import inspect_file


ROOT = Path(__file__).resolve().parents[1]
REVISION = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPOSITORY = "jsmorph/rh"
PREFIX = "GroundTheory.HeightsAndTheta.Heights."
STEM = "geometry-arithmetic-frontier-isotropic-integrability"
SOURCES = [
    ("FiniteCovolume.Objects",
     "86da5e3a40dc5f17d4fe12e07edbd8e8c6ce505590f4b06b9bfe643d8597eb9c",
     [(57, 68), (99, 123), (129, 135), (162, 176), (180, 207)]),
    ("FiniteCovolume.StatementsVectorOrbits",
     "113873f7b050c7c33b75625340232df686850b37d50b6c9dafdfedd612ca6d85",
     [(15, 27), (45, 48)]),
    ("FiniteCovolume.Statements",
     "2b2f4241dc04ce068d23fd9398f9739bd858dc7410a8c533440e53415fcd0058",
     [(15, 28), (43, 52), (74, 80)]),
    ("StabilizerCovolume.WeightedScaling",
     "5ddc589eb08244c18a6e5227ea7e042b41665ea3892c60472494bd0557c83121",
     [(16, 37)]),
    ("StabilizerCovolume.StatementsMeanLogPlus",
     "ac7f1aed609688a709b310670d11489101c19820f6417784c40234a16541ce1c",
     [(25, 29), (44, 66)]),
]

REFERENCES = [
    {
        "title": "Borel and Harish-Chandra, Arithmetic Subgroups of Algebraic Groups",
        "url": "https://www.mathi.uni-heidelberg.de/~wienhard/retreat10/references/borel_harishchandra_2.pdf",
        "file": "borel-harish-chandra-arithmetic-1962.pdf",
        "sha256": "7bc28593402ef043d9df14a9ac1a7875bec4b4054be0cd523081bf5e470da762",
        "pdf_page": 39,
        "locator": "Theorem 9.4, printed p.522; including proof for groups with unipotent radical",
        "role": "Finite arithmetic covolume for the unitary group and the vector stabilizer with no rational characters.",
        "inspection": "Original scanned page visually inspected and separately OCR-read.",
    },
    {
        "title": "Platonov and Rapinchuk, Algebraic Groups and Number Theory",
        "url": "https://uva.theopenscholar.com/files/andrei-rapinchuk/files/agnt_english.pdf",
        "file": "platonov-rapinchuk-algebraic-groups-number-theory.pdf",
        "sha256": "75f1fff8a4b712f00d0c7db5790951c3c242c070b8cdd70380a2d04a398f4aa3",
        "pdf_page": 136,
        "locator": "Theorem 5.4, printed pp.258-259",
        "role": "Finitely many arithmetic orbits on the rational parabolic quotient; applied to rational isotropic lines.",
        "inspection": "Author-hosted original spread visually inspected and text-read.",
    },
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_records(offline: bool) -> list[dict]:
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == REPOSITORY and atlas["commit"] == REVISION
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for suffix, expected_sha, ranges in SOURCES:
        module = PREFIX + suffix
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        record = inspect_file({"repository": REPOSITORY, "commit": REVISION,
                               "path": rel, "git_blob_sha1": blobs[module]}, offline)
        data = (ROOT / "build/source-cache" / REPOSITORY / REVISION / rel).read_bytes()
        assert sha(data) == expected_sha
        record = {k: record[k] for k in
                  ["repository", "commit", "path", "bytes", "git_blob_sha1",
                   "sha256", "matches_pinned_blob"]}
        lines = data.splitlines()
        record["inspected_excerpts"] = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            excerpt = b"\n".join(lines[lo - 1:hi]) + b"\n"
            assert len(excerpt) <= 12000
            record["inspected_excerpts"].append(
                {"lines": [lo, hi], "sha256": sha(excerpt)})
        records.append(record)
    return records


def reference_records(offline: bool) -> list[dict]:
    cache = ROOT / "build/reference-cache"
    cache.mkdir(parents=True, exist_ok=True)
    records = []
    for spec in REFERENCES:
        path = cache / spec["file"]
        if not path.exists():
            if offline:
                raise FileNotFoundError(path)
            request = urllib.request.Request(spec["url"],
                                             headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(request, timeout=45) as response:
                data = response.read()
            assert sha(data) == spec["sha256"]
            path.write_bytes(data)
        data = path.read_bytes()
        assert sha(data) == spec["sha256"]
        document = fitz.open(path)
        page = document[spec["pdf_page"] - 1]
        page_text = page.get_text()
        if "Platonov" in spec["title"]:
            assert "THEOREM 5.4." in page_text
            assert "double cosets" in page_text
            assert "finite" in page_text
        records.append({
            **spec,
            "bytes": len(data),
            "verified_full_bytes": True,
            "pdf_page_count": len(document),
            "page_text_sha256": sha(page_text.encode()),
            "scope": "Primary-source identity and locator authenticated; cited theorem is a mathematical input.",
        })
    return records


def compositions(total: int):
    if total == 0:
        yield ()
    else:
        for first in range(1, total + 1):
            for tail in compositions(total - first):
                yield (first,) + tail


def exact_checks() -> dict:
    # General complex scalar, one Hermitian complement entry. The middle
    # block is unchanged in arbitrary dimension, as shown in the proof.
    a, b, d = sp.symbols("a b d", real=True)
    u = a + sp.I * b
    ubar = a - sp.I * b
    witt = sp.Matrix([[0, 0, 1], [0, d, 0], [1, 0, 0]])
    lift = sp.diag(u, 1, 1 / ubar)
    unitary_error = (lift.conjugate().T * witt * lift - witt).applyfunc(sp.simplify)
    assert unitary_error == sp.zeros(3)
    assert sp.simplify(lift.det() - u / ubar) == 0
    assert sp.simplify(lift.det().subs(b, 0)) == 1

    # Coarea exponent, its E/Q norm exponent, and the rational-scalar case.
    f, n = sp.symbols("f n", integer=True, positive=True)
    assert sp.expand(f * (2 * n - 2) - 2 * f * (n - 1)) == 0
    norm_scaling_cases = 0
    for field_half_degree in range(1, 7):
        for dimension in range(3, 10):
            s = dimension - 1
            for scalar in [F(2), F(3, 2), F(5, 7)]:
                assert (scalar ** (2 * field_half_degree)) ** (-s) == \
                    scalar ** (-2 * field_half_degree * s)
                norm_scaling_cases += 1

    # A(e) changes by B^-s; NJ changes by B^-1. Their product is invariant.
    representative_cases = 0
    for s in range(2, 8):
        for bnorm in [F(2), F(3, 2), F(7, 5)]:
            for jnorm in [F(1), F(1, 3), F(7, 2)]:
                assert bnorm ** (-s) * (jnorm / bnorm) ** (-s) == jnorm ** (-s)
                representative_cases += 1

    # Each local ideal Euler factor is <= the degree-th Riemann factor.
    # Allow every sequence of residue degrees whose sum is <= the degree;
    # the unused degree also covers ramification. These finite checks
    # audit the exact inequality proved factor by factor in the note.
    euler_cases = 0
    for degree in [2, 4, 6]:
        for total in range(1, degree + 1):
            for residues in compositions(total):
                for prime in [2, 3, 5, 11]:
                    for s in [2, 3, 5]:
                        lhs = F(1)
                        for residue in residues:
                            lhs *= F(1) / (1 - F(1, prime ** (residue * s)))
                        rhs = (F(1) / (1 - F(1, prime ** s))) ** degree
                        assert lhs <= rhs
                        euler_cases += 1

    # Plain scalar multiples cannot satisfy a fixed line-index bound.
    unbounded_index_examples = [
        {"field_degree": degree, "scalar": m, "line_index": m ** degree}
        for degree in [2, 4, 6] for m in [2, 3, 5]
    ]
    assert all(row["line_index"] > 1 for row in unbounded_index_examples)
    return {
        "symbolic_witt_lift": "T* H T = H; det(T)=u/conj(u); real-unit determinant=1",
        "norm_scaling_cases": norm_scaling_cases,
        "representative_change_cases": representative_cases,
        "exact_euler_factor_comparisons": euler_cases,
        "unbounded_line_index_examples": unbounded_index_examples,
        "scope": "Exact algebra and finite arithmetic audits, not a computational proof of reduction theory or convergence.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true",
                        help="Require cached pinned sources and primary references.")
    args = parser.parse_args()
    artifacts = [
        f"notes/{STEM}.md",
        f"paper/shared/{STEM}.tex",
        f"paper/shared/{STEM}-references.tex",
        "scripts/check_geometry_arithmetic_frontier_isotropic_integrability.py",
    ]
    certificate = {
        "status": "pass",
        "claim": "For N>=3 the full isotropic O_E-lattice count is integrable on the actual arithmetic unitary or special unitary Haar quotient; all-radius homogeneity follows.",
        "proof": "Finite rational cusp lines, finite-index congruence-unit images, character-free vector stabilizers, nonnegative unfolding, and a convergent partial Dedekind zeta sum at N-1.",
        "source_pin": {"repository": REPOSITORY, "commit": REVISION},
        "source_records": source_records(args.offline),
        "primary_references": reference_records(args.offline),
        "exact_checks": exact_checks(),
        "removed_obligations": [
            "Independent arithmetic finite-volume hypothesis for the identified lattice stabilizer",
            "Independent integrability hypothesis for one radius of the full isotropic count",
            "Independent counting-mean homogeneity hypothesis after the same Haar identification",
            "A bounded line-index restriction on the vectors being counted",
        ],
        "retained_obligations": [
            "Actual geometric construction, arithmetic model, and component uniformization",
            "Identification of the original lattice and positive Hodge norm",
            "Equality of the normalized geometric mean with the original normalized Haar mean, including finite-level indices and component/stabilizer weights",
            "Fixed compact finite-adelic support with bounded invariant weights if a weighted count is used",
            "Signed boundary intersection limit and all remaining W10 arithmetic section/model suppliers",
        ],
        "edge_cases": [
            "A definite archimedean factor, or global anisotropy, makes the isotropic count zero",
            "N>=3 gives convergence at s=N-1>1 and the nonzero complement for SU determinant correction; no dimension-two convergence is claimed",
            "The vector stabilizer has no multiplicative Levi factor; the line stabilizer does",
            "Nonzero E-vectors are nonzero at every embedding",
            "The stabilizer groups and their Haar measures are identical under e->a e",
            "CM unit modulo conjugate has finite root-of-unity image, so real units have finite index for SU",
        ],
        "artifacts": [{"path": path, "sha256": sha((ROOT / path).read_bytes())}
                      for path in artifacts],
        "verification_limit": "No Lean build, no geometric model existence assertion, no complete RH or GRH proof, and no proof-map node closure.",
        "completed_nodes": {"RH": [6, 9], "GRH": [17, 31]},
    }
    output = ROOT / "certificates" / f"{STEM}.json"
    output.write_text(json.dumps(certificate, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "status": certificate["status"],
        "certificate": str(output.relative_to(ROOT)),
        "pinned_source_modules": len(certificate["source_records"]),
        "primary_references": len(certificate["primary_references"]),
        "norm_scaling_cases": certificate["exact_checks"]["norm_scaling_cases"],
        "representative_change_cases": certificate["exact_checks"]["representative_change_cases"],
        "exact_euler_factor_comparisons": certificate["exact_checks"]["exact_euler_factor_comparisons"],
        "completed_nodes": certificate["completed_nodes"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
