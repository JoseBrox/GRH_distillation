#!/usr/bin/env python3
"""Exact examples and source-byte certificate for finite symmetry energy.

The universal proofs are in the note. This script does not build Lean or
prove an action or energy estimate for the actual arithmetic target.
"""
from __future__ import annotations

import gzip
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
CACHE = ROOT / "build/source-cache/jsmorph/rh" / PIN
NOTE = "notes/finite-symmetry-energy.md"
CERT = "certificates/finite-symmetry-energy.json"
SOURCES = {
    "Development/AbelianVarietyTheory/Proofs/DivisorProofs/KeepsCuspLatticeNorm.lean": [(204, 236)],
    "Development/AbelianVarietyTheory/Proofs/DivisorProofs/ActCCoe.lean": [(38, 48)],
    "Development/AbelianVarietyTheory/Definitions/Divisors/IsCoprimeOfNatCast.lean": [(436, 473)],
    "Formalism/LocalToGlobal/IndefiniteReal/GramCEqTranspose.lean": [(76, 101)],
    "Development/AbelianVarietyTheory/Definitions/Divisors/NormNegCmConstantEqAtAllEmbeddings.lean": [(31, 48)],
    "Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PointRead.lean": [(24, 38)],
    "Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/LabelDatum.lean": [(91, 116)],
    "Development/AutomorphicArithmetic/TwistedTraces/IsotypicMultiplicityTensorProduct.lean": [(12, 13)],
    "Formalism/SharpRestriction/CuspSpanNormBounds/DataS.lean": [(33, 48)],
    "Formalism/HarderNarasimhan/StatementPl.lean": [(55, 62)],
    "Formalism/SizeWindowBrackets/FrameTraceRatioFinEquiv.lean": [(59, 77)],
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def zero(n: int, m: int) -> list[list[F]]:
    return [[F(0) for _ in range(m)] for _ in range(n)]


def identity(n: int) -> list[list[F]]:
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a: list[list[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*a)]


def add(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c: F, a: list[list[F]]) -> list[list[F]]:
    return [[c * x for x in row] for row in a]


def mul(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[sum((x * y for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def kron(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[a[i][j] * b[k][l] for j in range(len(a[0]))
             for l in range(len(b[0]))]
            for i in range(len(a)) for k in range(len(b))]


def trace(a: list[list[F]]) -> F:
    return sum((a[i][i] for i in range(len(a))), F(0))


def hs2(a: list[list[F]]) -> F:
    return sum((x * x for row in a for x in row), F(0))


def conjugate(u: list[list[F]], q: list[list[F]]) -> list[list[F]]:
    return mul(mul(u, q), transpose(u))


def reynolds(group: list[list[list[F]]], q: list[list[F]]) -> list[list[F]]:
    result = zero(len(q), len(q))
    for u in group:
        result = add(result, conjugate(u, q))
    return scale(F(1, len(group)), result)


def energies(maps: list[list[list[F]]]) -> tuple:
    d = len(maps[0])
    q = zero(d, d)
    delta = F(0)
    rank = 0
    for t in maps:
        r = len(t[0])
        rank += r
        delta += hs2(add(mul(transpose(t), t), scale(F(-1), identity(r))))
        q = add(q, mul(t, transpose(t)))
    mass = trace(q)
    eta = F(d) * hs2(add(q, scale(-mass / d, identity(d)))) / mass**2
    return rank, delta, q, mass, eta


def finite_checks() -> dict:
    rotation = [[F(0), F(-1)], [F(1), F(0)]]
    reflection = [[F(1), F(0)], [F(0), F(-1)]]
    powers = [identity(2)]
    for _ in range(3):
        powers.append(mul(powers[-1], rotation))
    group = powers + [mul(r, reflection) for r in powers]
    key = lambda a: tuple(tuple(row) for row in a)
    keys = {key(a) for a in group}
    assert len(keys) == 8
    for u in group:
        assert mul(u, transpose(u)) == identity(2)
        assert all(x.denominator == 1 for row in u for x in row)
        for v in group:
            assert key(mul(u, v)) in keys
    rational_examples = 0
    for m in range(1, 5):
        d = 2 * m
        lifted = [kron(u, identity(m)) for u in group]
        for seed in range(1, 6):
            maps = [[[F(((i + 2) * (j + 3) + seed * (r + 1)) % 11 - 5, 3)
                      for j in range(r)] for i in range(d)]
                    for r in (1, 2, 3)]
            rank, delta, q, mass, eta = energies(maps)
            expanded = [mul(u, t) for u in lifted for t in maps]
            rk, dk, qk, mk, etak = energies(expanded)
            rq = reynolds(lifted, q)
            assert rk == 8 * rank and dk == 8 * delta and mk == 8 * mass
            assert qk == scale(F(8), rq)
            assert dk / rk == delta / rank
            residual = add(q, scale(F(-1), rq))
            assert eta - etak == F(d) * hs2(residual) / mass**2
            assert etak <= eta
            # Schur averaging on V tensor E: A=(Tr_V Q)/dim(V).
            partial = [[(q[i][j] + q[m + i][m + j]) / 2
                        for j in range(m)] for i in range(m)]
            assert rq == kron(identity(2), partial)
            assert etak == F(d * 2) * hs2(
                add(partial, scale(-mass / d, identity(m)))) / mass**2
            assert reynolds(lifted, rq) == rq
            rational_examples += 1
    sharp_examples = []
    for m in range(1, 13):
        embed = [[F(i == a * m) for a in range(2)] for i in range(2 * m)]
        rank, delta, q, mass, eta = energies([embed for _ in range(m)])
        assert delta == 0 and rank == mass == 2 * m and eta == m - 1
        assert all(conjugate(kron(u, identity(m)), q) == q for u in group)
        sharp_examples.append({"multiplicity": m, "dimension": 2 * m,
                               "e": 0, "eta_before_and_after": m - 1})
    line = [[F(1)], [F(0)]]
    _, delta, q, _, eta = energies([line, line])
    assert delta == 0 and eta == 1
    assert reynolds([identity(2), reflection], q) == q
    assert reynolds(group, q) == identity(2)
    assert mul(reflection, line) == line
    assert mul(rotation, line) == [[F(0)], [F(1)]]
    return {
        "integral_orthogonal_group_order": 8,
        "exact_rational_orbit_replication_and_partial_trace_examples": rational_examples,
        "sharp_irreducible_type_multiplicity_examples": sharp_examples,
        "multiplicity_free_block_mass_obstruction": "e=0, eta=1 before and after",
        "whole_target_irreducible_example": "eta=1 becomes eta=0",
        "ambient_isometry_moves_the_character_eigenspace": True,
    }


def source_records() -> list[dict]:
    atlas = json.loads(gzip.decompress((ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == PIN
    modules = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for relative, ranges in SOURCES.items():
        path = "lean/src/" + relative
        data = (CACHE / path).read_bytes()
        blob = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
        assert blob == modules[relative.removesuffix(".lean").replace("/", ".")]
        lines = data.splitlines(keepends=True)
        reads = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            reads.append({"lines": [lo, hi], "sha256": sha(b"".join(lines[lo - 1:hi]))})
        records.append({"path": path, "git_blob_sha1": blob,
                        "sha256": sha(data), "lines": len(lines), "excerpts": reads})
    return records


def main() -> None:
    certificate = {
        "schema_version": 1,
        "status": "proved_finite_symmetry_reduction_with_unresolved_actual_target_and_multiplicity_supplier",
        "repository": "jsmorph/rh", "commit": PIN,
        "note": {"path": NOTE, "sha256": sha((ROOT / NOTE).read_bytes())},
        "script": {"path": str(Path(__file__).relative_to(ROOT)), "sha256": sha(Path(__file__).read_bytes())},
        "source_atlas_sha256": sha((ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()),
        "source_files": source_records(),
        "finite_checks": finite_checks(),
        "proof_dependencies": [{"path": "notes/averaged-theta-energy.md",
                                "sha256": sha((ROOT / "notes/averaged-theta-energy.md").read_bytes())}],
        "independent_review": {
            "status": "PASS",
            "reviewer": "transport_defect",
            "ordinary_mathematics": "Sections 1-3: orbit replication, commutant and partial-trace normalizations, both variance terms, sharp examples, scalar stabilizer and arithmetic compatibility.",
            "independent_source_hash_and_contract_reads": [
                "Development/AbelianVarietyTheory/Proofs/DivisorProofs/KeepsCuspLatticeNorm.lean:204-236",
                "Formalism/LocalToGlobal/IndefiniteReal/GramCEqTranspose.lean:76-101",
            ],
            "limits": "No independent audit of all remaining source-table clauses or upstream proofs; no Lean replay.",
        },
        "scope": {
            "ordinary_proofs_in_note": True,
            "exact_finite_examples": True,
            "pinned_source_bytes_and_bounded_contract_comparison": True,
            "upstream_source_proofs_audited": False,
            "lean_kernel_replay": False,
            "same_actual_target_group_action_supplied": False,
            "actual_global_energy_bound_supplied": False,
        },
    }
    (ROOT / CERT).write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "certificate": CERT,
                      "source_files": len(certificate["source_files"]),
                      "rational_examples": certificate["finite_checks"]["exact_rational_orbit_replication_and_partial_trace_examples"],
                      "sharp_examples": len(certificate["finite_checks"]["sharp_irreducible_type_multiplicity_examples"])}))


if __name__ == "__main__":
    main()
