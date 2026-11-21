#!/usr/bin/env python3
"""Authenticate the integral RH Selmer-product reduction.

The written all-rank proof is primary. The finite exact calculations below
are supplemental group-ring/cardinality/averaging checks, not computations
of an actual Selmer group, an upstream proof replay, or a Lean build.
"""

from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PROJECT_REV = "979ac582dcb8b4d33230a45a1bd2ffaa31709d86"
NOTE = "notes/rh-selmer-product-criterion.md"
SCRIPT = "scripts/check_rh_selmer_product_criterion.py"
OUT = "certificates/rh-selmer-product-criterion.json"
AA = "Development.AutomorphicArithmetic.AutomorphicVarieties."
SOURCES = [
    ("Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.ExistsFamPOfKits",
     "5637a641fd600135f29acaf3d29a495b7029639794674f940ea24a107815ab32",
     [[56, 101], [120, 133]]),
    ("Formalism.LocalRingCardinality.Params",
     "1de4e5a1230e9d93b5ace3e4f7e112f65e3d5264d75db227476986d179881e17",
     [[6, 29]]),
    (AA + "HeightAndVanishing.CountI",
     "f2f494a5aaa5255477336c119bb6173d7017ab9b5c78b576fb1f2290b63a8e80",
     [[19, 49]]),
    (AA + "HeightAndVanishing.Counts",
     "cc00a1a2e38f8dc5a87a0cc5d79ab8100db8c59255d62be12c95931262fc53c2",
     [[24, 47], [53, 73]]),
    (AA + "UnitaryThreeGroups.CorGSumLog",
     "8fb1f7e2de2193d3f0fb8101356b00dc623e86005c101d21b23e1deb0d2b2611",
     [[1, 12], [37, 73]]),
    (AA + "UnitaryThreeGroups.CorGKOf",
     "b6642ab5bc0ff87dbfe65a21f2acb929793804f090dfb398cb727d4ae4f17513",
     [[5, 10]]),
    (AA + "ModularityArgument.ThresholdArguments.DenseThresholdCases.CountVOf",
     "4230bf1f65fb54b8e30d32a19a641b95eaa476a6043d91c184e17fbc8fc76dce",
     [[33, 61]]),
]

PREMISES = [
    ("notes/rh-selmer-residual-budget.md",
     "f901646e0f1558c0afad92717231a10b47b2da11d1fa186e5dcdd7a70a6842d4",
     [[28, 141], [258, 330]],
     "Actual host, twist, case partition, conductor threshold and weighted residual allowance."),
    ("notes/qualitative-selmer-finiteness.md",
     "2e18981627bc91d95b92f6132eb3f6c79074c435f96e1a251d9cb0eeff5b806e",
     [[20, 91], [92, 166], [168, 206]],
     "Established strict full-local finiteness and natural dual injection into K_{2e}; no fresh proof audit."),
    ("paper/sections/recovered/32-fcmp-section.tex",
     "e65c746a51b724f6425f29d553acd08254bd94901137e163f3eda66137766bb9",
     [[15, 90], [192, 237], [365, 398]],
     "Established integral Fourier comparison, coefficient normalization and preservation of local conditions."),
    ("notes/finite-twisted-place-budget.md",
     "2a73e1734e7f8493e419f396a676c75e193225507f01c7d744f2e8d310a46cfa",
     [[70, 115], [145, 188]],
     "Selected-place weights and generator coefficient one; remaining local integral comparison retained."),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def passages(data, ranges):
    lines = data.splitlines()
    out = []
    for lo, hi in ranges:
        assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
        out.append({"lines": [lo, hi],
                    "sha256": sha(b"\n".join(lines[lo - 1:hi]) + b"\n")})
    return out


def source_records():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["commit"] == REV and atlas["repository"] == "jsmorph/rh"
    blobs = {r[0]: r[1] for r in atlas["modules"]}
    records = []
    for module, expected, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        path = ROOT / "build/source-cache/jsmorph/rh" / REV / rel
        if not path.is_file():
            path = ROOT / "build/lean-mirror" / rel
        data = path.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert sha(data) == expected and blob == blobs[module], module
        records.append({"module": module, "path": rel, "sha256": expected,
                        "git_blob_sha1": blob, "line_count": len(data.splitlines()),
                        "inspected_excerpts": passages(data, ranges)})
    return records


def premise_records():
    out = []
    for path, expected, ranges, role in PREMISES:
        data = subprocess.check_output(["git", "show", PROJECT_REV + ":" + path], cwd=ROOT)
        assert sha(data) == expected, path
        out.append({"path": path, "commit": PROJECT_REV, "sha256": expected,
                    "role": role, "bounded_passages": passages(data, ranges)})
    return out


def group_checks():
    cases = cardinality_cases = compression_cases = 0
    for h in range(4):
        n = 2 ** h
        group = list(itertools.product(range(n), range(2), range(2)))
        index = {g: i for i, g in enumerate(group)}
        z = (0, 0, 0)
        j = (0, 1, 1)

        def add(g, k):
            return ((g[0] + k[0]) % n, (g[1] + k[1]) % 2, (g[2] + k[2]) % 2)

        def neg(g):
            return ((-g[0]) % n, g[1], g[2])

        def product(a, b):
            c = {g: F(0) for g in group}
            for g in group:
                for k in group:
                    c[add(g, k)] += a[g] * b[k]
            return c

        ident = {g: F(g == z) for g in group}
        avg = {g: F(1, len(group)) for g in group}
        projectors = []
        for parity in (1, -1):
            c = {g: F(g == z, 2) + parity * F(g == j, 2) for g in group}
            projectors.append(c)
            old = {g: c[g] - (avg[g] if parity == 1 else 0) for g in group}
            projectors.append(old)
            restored = {g: c[g] - old[g] for g in group}
            augmentation = {g: ident[g] - avg[g] for g in group}
            assert product(restored, augmentation) == {g: F(0) for g in group}
            if parity == -1:
                assert restored == {g: F(0) for g in group}
            compression_cases += 1
        odd = projectors[2]
        for low in range(h + 1):
            subgroup = {g for g in group if g[1:] == (0, 0) and g[0] % (2 ** low) == 0}
            ah = {g: F(g in subgroup, len(subgroup)) for g in group}
            projectors.append(product(odd, {g: ident[g] - ah[g] for g in group}))
        for pr in projectors:
            assert product(pr, pr) == pr
            assert all(pr[neg(g)] == pr[g] for g in group)
            assert all(v.denominator & (v.denominator - 1) == 0 for v in pr.values())
            rank = len(group) * pr[z]
            assert rank.denominator == 1 and 0 <= rank <= len(group)
            cases += 1
            # Exhaustive finite-module image checks. These are regular modules,
            # deliberately not presented as actual Selmer-group calculations.
            if h in (0, 1):
                modulus = 9 if h == 0 else 3
                coeff = {g: (pr[g].numerator * pow(pr[g].denominator, -1, modulus)) % modulus
                         for g in group}
                matrix = [[coeff[add(g, neg(k))] for k in group] for g in group]
                images = set()
                for v in itertools.product(range(modulus), repeat=len(group)):
                    images.add(tuple(sum(a * b for a, b in zip(row, v)) % modulus for row in matrix))
                assert len(images) == modulus ** int(rank)
                cardinality_cases += 1
    return {"exact_group_ring_projectors": cases,
            "exact_restored_trivial_summand_compression_identities": compression_cases,
            "exhaustive_regular_finite_module_image_cases": cardinality_cases}


def average_checks():
    cases = 0
    choices = [F(0), F(1, 3), F(1)]
    lengths = [[0, 2, 1], [1, 0, 4], [3, 1, 2]]
    for weights in itertools.product(choices, repeat=3):
        for ranks in itertools.product([0, 1, 3], repeat=3):
            consumers = [F(1, 2), F(2, 3), F(1)]
            mass = sum(u * d for u, d in zip(consumers, ranks))
            if not mass:
                assert all(u * d == 0 for u, d in zip(consumers, ranks))
                cases += 1
                continue
            a = [u * d / mass for u, d in zip(consumers, ranks)]
            assert sum(a) == 1
            # Each coordinate represents the coefficient of log(p) for a
            # fixed prime; equality therefore proves the formal log-product
            # identity for arbitrary prime orders without floating logs.
            for pindex in range(3):
                per_family = [weights[(i + pindex) % 3] for i in range(3)]
                wbar = sum(a[i] * per_family[i] for i in range(3))
                total_length = sum(lengths[pindex])
                left = sum(consumers[i] * ranks[i] * per_family[i] * total_length for i in range(3))
                assert left == mass * wbar * total_length
            cases += 1
    return {"exact_rank_weighted_average_cases": cases}


def file_record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "sha256": sha(data), "bytes": len(data)}


def main():
    sources = source_records()
    premises = premise_records()
    checks = {**group_checks(), **average_checks()}
    result = {
        "schema_version": 1, "result": "PASS",
        "claim": "Exact integral projectors and a resonance-free weighted product replace the RH residual character sums; equality on actual groups uses the established trivial-character vanishing. No quantitative bound is supplied.",
        "source_revision": {"repository": "jsmorph/rh", "commit": REV},
        "sources": sources,
        "established_premises": premises,
        "primary_analytic_reference": {
            "source": "NIST Digital Library of Mathematical Functions",
            "url": "https://dlmf.nist.gov/25.15",
            "equations": ["25.15.4", "25.15.5", "25.15.7", "25.15.8"],
            "consulted_date": "2026-11-21",
            "scope": "Primitive trivial-zero parity and imprimitive Euler-factor identity were consulted directly; no numerical L-value calculation is claimed."
        },
        "checks": checks,
        "review": {
            "author": "Ordinary all-rank projector, descent, duality, family-average and parity proofs completed; the bounded new source contracts were read.",
            "root": "PASS: full written ordinary mathematics, the final outside-P equality on actual groups using known Case Z, and direct primary DLMF 25.15.4/.5/.7/.8 check. Independently hash-read ExistsFamPOfKits 73-85 and 120-133, and CorGSumLog 52-73: common ranks/page/q/d/conductor/generator data, separate per-member supports and the aggregate two-integer valuation bound agree. Other source clauses remain the author's bounded audit; no upstream proof or Lean replay claimed.",
            "geometric_simplify": "PASS: all ordinary proofs in Sections 1-4, including integral projectors, exact normalized length identity, full-local prime-to-p descent, relative quotient, duality, rank-weighted average and trivial-zero parity; directly checked official DLMF 25.15.4/.5/.7/.8. Separately passed the final resonance-free equality on actual groups, retaining Case Z in its proof. Uses the already reviewed qualitative/Fourier premises; no fresh audit of the new family/CorG/CountV source contracts. Explicit d_i>=0 precision is included.",
            "transport_defect": "PASS: ordinary mathematics of the paper proposal and note Sections 1-3, including full-local prime-to-p descent at ramified places, rank-weighted averaging with zero-total handled before division, and the final outside-P restoration of the vanishing resonant even trivial-character summand. No new upstream source audit claimed."
        },
        "limitations": [
            "No bound on the weighted product or an actual Selmer-group order is proved.",
            "The source family constructor, local integral comparison and quantitative automorphy/deformation inputs remain hypotheses.",
            "Established finiteness and Fourier theorems are cited premises, not freshly replayed upstream proofs.",
            "No Lean build, proof-kernel replay or whole-source audit was performed."
        ],
        "artifacts": [file_record(NOTE), file_record(SCRIPT)]
    }
    (ROOT / OUT).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "pinned_files": len(sources),
                      "bounded_source_excerpts": sum(len(s["inspected_excerpts"]) for s in sources),
                      "established_premise_files": len(premises), **checks}))


if __name__ == "__main__":
    main()
