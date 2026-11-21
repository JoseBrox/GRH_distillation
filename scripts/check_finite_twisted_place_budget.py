#!/usr/bin/env python3
"""Pinned-source and exact finite checks for the selected-place budget.

The checks supplement the ordinary proof. They construct no number field,
Selmer group or integral theta map and do not run a Lean kernel.
"""

from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NOTE = "notes/finite-twisted-place-budget.md"
OUT = "certificates/finite-twisted-place-budget.json"
SOURCES = [
    ("Development.AutomorphicArithmetic.ResidueCharacters.TwistedPlaces",
     "439691fcc175a0014f490085272a463a1b0a987a855bff85b9d4421d2fb52436",
     [[133, 157], [218, 241], [276, 323]]),
    ("Formalism.SharpRestriction.LevelLetterCocycles.MemPrimesOverOfMem",
     "36f4345f5366bac2cbd81a9c014e5d664cce47305a59d234039e6f4ca791be46",
     [[45, 118], [513, 554], [558, 603], [605, 647]]),
    ("Formalism.SharpRestriction.LevelLetterCocycles.ExportBoundOfAdmissible",
     "bdfc98f88029b0046557d06ae9223905e3c4b4048114a676072820d150905534",
     [[888, 895], [1023, 1053]]),
    ("Formalism.SharpRestriction.GlobalTheoremInputs",
     "4d51ccc0586441a159ad6d09ebc0a46b3c462e3c5b296d5a5bd7613266e17bfb",
     [[25, 63], [91, 95]]),
    ("Development.AutomorphicArithmetic.CharacterBoxes.DivinNOfHypV",
     "cefdce360890e26405199ef8db01d6b0c7e044c4ebebeb6bbcfd23de6148bde0",
     [[76, 129]]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, expected, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        path = ROOT / "build/source-cache/jsmorph/rh" / REV / rel
        if not path.is_file():
            path = ROOT / "build/lean-mirror" / rel
        data = path.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert sha(data) == expected and blob == blobs[module], module
        lines = data.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpt = b"\n".join(lines[lo-1:hi]) + b"\n"
            excerpts.append({"lines": [lo, hi], "sha256": sha(excerpt)})
        records.append({"module": module, "path": rel, "sha256": expected,
                        "git_blob_sha1": blob, "bytes": len(data),
                        "line_count": len(lines), "inspected_excerpts": excerpts})
    return records, sha(packed)


def weighted_models():
    """The logarithmic prime weights can be any nonnegative reals.

Use exact rational weights and integer decompositions of the field degree.
These are models of the finite inequality, not constructed number fields.
Generator loss is allowed to attain only its aggregated, not local, bound.
"""
    count = strict = 0
    for degree in range(1, 7):
        for masses in itertools.product(range(degree+1), repeat=3):
            kappa = [F(m, degree) for m in masses]
            for generator in ((), (0,), (0, 2)):
                for d in (0, 1, 3):
                    for variant in range(4):
                        weights = [F(2), F(3), F(5)]
                        residual = [F((i+variant) % 4) for i in range(3)]
                        lengths = [F((2*i+variant+1) % 5) for i in range(3)]
                        effective = [F(1) if i in generator and masses[i] else kappa[i]
                                     for i in range(3)]
                        loss = sum((d*effective[i]*weights[i]*(residual[i]+lengths[i])
                                    for i in range(3)), F())
                        ordinary = sum((weights[i]*residual[i] for i in range(3)
                                        if masses[i]), F())
                        selected = sum((effective[i]*weights[i]*lengths[i]
                                        for i in range(3)), F())
                        unweighted = sum((weights[i]*lengths[i] for i in range(3)
                                          if masses[i]), F())
                        assert loss <= d*(ordinary+selected)
                        assert selected <= unweighted
                        strict += selected < unweighted
                        count += 1
    # A generator bound alone does not permit an extra place-fraction factor.
    kappa, rank, residual, length = F(1, 4), F(1), F(0), F(1)
    local_loss = F(4)
    actual = kappa*local_loss
    assert actual == rank*(residual+length) == 1
    assert actual > rank*kappa*(residual+length)
    return count, strict


def normalization_models():
    count = 0
    for f, m, b, y, nc, cn, cv, rank in itertools.product(
            (1, 2, 5), (1, 3), (1, 4), (F(1), F(3, 2), F(4)),
            (0, 1, 7), (0, 2), (0, 3), (0, 1, 4)):
        B0 = f*m*b*y
        selected = cv*y*(B0+nc)
        actual_bound = rank*(cn*f*m*b*y*y+selected)
        final_bound = rank*(cn+cv)*y*(B0+nc)
        assert f*m*b*y*y == y*B0
        assert actual_bound <= final_bound
        assert b <= y*(B0+nc)
        count += 1
    return count


def main():
    records, atlas_hash = source_records()
    weighted, strict = weighted_models()
    checks = {"finite_weighted_models": weighted,
              "strictly_smaller_weighted_budgets": strict,
              "rank_normalization_models": normalization_models(),
              "generator_fraction_counterexample": {
                  "selected_fraction": "1/4", "local_loss": 4,
                  "actual_aggregate": 1, "incorrect_extra_fraction_bound": "1/4"}}
    report = {
        "schema_version": 1,
        "result": "PASS",
        "repository": "jsmorph/rh",
        "commit": REV,
        "note": NOTE,
        "note_sha256": sha((ROOT / NOTE).read_bytes()),
        "checker": str(Path(__file__).relative_to(ROOT)),
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "atlas_compressed_sha256": atlas_hash,
        "mathematical_results": [
            "The congruence consumer needs only the finite Selmer sum on actual twisted residue primes.",
            "Away from generator primes, retain the actual ramification-inertia fraction of twisted places.",
            "The source numerical congruence conclusion follows if that weighted budget is O(x^eps(B0+Nc)).",
            "Global finiteness in the current local-admissibility supplier is retained explicitly.",
        ],
        "exact_checks": checks,
        "sources": records,
        "review": {
            "author": "Ordinary proof and bounded source-consumer audit completed.",
            "root": "PASS: complete ordinary weighted-sum proof/downstream algebra and independently hash-read MemPrimesOverOfMem 45-118, 513-603, 605-647; ExportBoundOfAdmissible 888-895. Verified where kappa is dropped, generator aggregate, finite S before tsum, R_p decomposition and numerical allowance. No upstream proof replay.",
            "geometric_simplify": "PASS: Sections 1-4 ordinary mathematics, including generator coefficients, exact normalization, empty support/rank zero, and finiteness caveat. No additional source audit of the R_p estimate or upstream proofs claimed.",
        },
        "limitations": [
            "Finite rational models supplement the proof and are not actual number-field constructions.",
            "No Selmer length, local congruence estimate, theta map, or uniform selected-family supplier is proved.",
            "Global cohomological finiteness remains in the existing admitted interface.",
            "No removal of an entire final arithmetic-envelope summand is inferred.",
            "No full dependency replay, Lean build, or construction-node completion is claimed.",
        ],
    }
    (ROOT / OUT).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "source_files": len(records),
                      "source_excerpts": sum(len(r["inspected_excerpts"]) for r in records),
                      "exact_checks": checks, "certificate": OUT}))


if __name__ == "__main__":
    main()
