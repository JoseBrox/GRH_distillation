#!/usr/bin/env python3
"""Exact sharp return-envelope checks; no uniform arithmetic estimate."""

from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import random

from check_seed_return_deficit import (
    deficit_le, gram, multiply, positive_trace_le, return_energy, tr, transpose,
)

ROOT = Path(__file__).resolve().parents[1]
REVISION = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def envelope(norms):
    a = sum(norms, F(0))
    b = sum((w * w for w in norms), F(0))
    m = max(norms, default=F(0))
    h = b - max(2 * m - a, F(0)) ** 2
    assert 0 <= h <= b
    assert h <= a * a - b
    return h


def outer_sum(rows):
    return gram(rows, F(1))


def loss_matrix(rows):
    d = len(rows[0])
    total = [sum((row[j] for row in rows), F(0)) for j in range(d)]
    a = outer_sum(rows)
    return [[a[i][j] - total[i] * total[j] for j in range(d)] for i in range(d)]


def monotonicity_cases():
    count = 0
    for n in range(1, 6):
        for original in itertools.product((F(0), F(1), F(2), F(3)), repeat=n):
            for j in range(n):
                raised = list(original)
                raised[j] += F(3, 2)
                assert envelope(original) <= envelope(raised)
                count += 1
    return count


def positive_trace_cases():
    rng = random.Random(20261122)
    units = [(F(1), F(0)), (F(0), F(1)), (F(3, 5), F(4, 5)),
             (F(-3, 5), F(4, 5)), (F(5, 13), F(-12, 13))]
    count = 0
    for _ in range(1600):
        n = rng.randrange(1, 9)
        norms = [F(rng.randrange(7), rng.randrange(1, 5)) for _ in range(n)]
        rows = [[w * x for x in rng.choice(units)] for w in norms]
        assert all(sum(x * x for x in row) == w * w for row, w in zip(rows, norms))
        assert positive_trace_le(loss_matrix(rows), F(0), envelope(norms))
        for v in units:
            restricted = [[sum(x * y for x, y in zip(row, v))] for row in rows]
            cut_norms = [abs(row[0]) for row in restricted]
            assert envelope(cut_norms) <= envelope(norms)
            assert positive_trace_le(loss_matrix(restricted), F(0), envelope(cut_norms))
            count += 1
        count += 1
    return count


def folding_cases():
    count = 0
    group = [[[F(s[i] if p[i] == j else 0) for j in range(2)] for i in range(2)]
             for p in ((0, 1), (1, 0)) for s in itertools.product((-1, 1), repeat=2)]
    source_cuts = [
        [[F(1)], [F(0)]], [[F(3, 5)], [F(4, 5)]],
        [[F(5, 13)], [F(12, 13)]], [[F(1), F(0)], [F(0), F(1)]],
    ]
    for w in ([F(1), F(0)], [F(3, 5), F(4, 5)]):
        original = [[v[0] for v in multiply(g, [[x] for x in w])] for g in group]
        for signs in ([1] * 8, [1, -1] * 4, [1, 1, -1, -1] * 2):
            rows = [[s * x for x in row] for row, s in zip(original, signs)]
            assert gram(rows, F(1, 4)) == [[F(1), F(0)], [F(0), F(1)]]
            for size, stride in itertools.product((2, 4, 8), (1, 3, 5)):
                labels = [(stride * j + j // size) % size for j in range(8)]
                _, full_a, _, full_e = return_energy(rows, [F(1)] * 8, labels, F(1, 4), size)
                full_h = F(1, 4) * sum(envelope([F(1) for y in labels if y == k]) for k in range(size))
                target_cuts = []
                axis = [[F(i == 0)] for i in range(size)]
                target_cuts.append(axis)
                rotated = [[F(0)] for _ in range(size)]
                rotated[0][0], rotated[1][0] = F(3, 5), F(4, 5)
                target_cuts.append(rotated)
                plane = [[F(0), F(0)] for _ in range(size)]
                if size == 2:
                    plane[0][0], plane[1][1] = F(1), F(1)
                else:
                    plane[0][0], plane[2][0] = F(3, 5), F(4, 5)
                    plane[1][1], plane[3][1] = F(5, 13), F(12, 13)
                target_cuts.append(plane)
                for jmat in source_cuts:
                    rank = len(jmat[0])
                    restricted = multiply(rows, jmat)
                    norms = [abs(row[0]) for row in restricted] if rank == 1 else [F(1)] * 8
                    folded, _, b, energy = return_energy(restricted, norms, labels, F(1, 4), size)
                    h = F(1, 4) * sum(envelope([w for w, y in zip(norms, labels) if y == k])
                                       for k in range(size))
                    assert F(1, 4) * sum(b) == rank
                    assert h <= min(F(rank), energy, full_h)
                    before = gram(folded, F(1, 4))
                    assert deficit_le(before, h)
                    for umat in target_cuts:
                        n = len(umat[0])
                        assert multiply(transpose(umat), umat) == [
                            [F(i == j) for j in range(n)] for i in range(n)]
                        final = multiply(transpose(umat), folded)
                        source = gram(final, F(1, 4))
                        target = gram(transpose(final), F(1, 4))
                        lost = tr(before) - tr(source)
                        assert lost >= 0
                        diag = [sum(x * x for x in row) for row in umat]
                        lost_bound = sum(full_a[y] * (1 - diag[y]) for y in range(size))
                        assert lost <= lost_bound
                        assert deficit_le(source, min(F(rank), h + lost))
                        assert tr(source) >= rank - h - lost
                        excess = sum(max(full_a[y] - F(rank, n), F(0)) * diag[y]
                                     for y in range(size))
                        assert positive_trace_le(target, F(rank, n), excess)
                        count += 1
    return count


def sharp_examples():
    dominant = [F(4), F(-1), F(-2)]
    h = envelope([abs(x) for x in dominant])
    assert h == sum(x * x for x in dominant) - sum(dominant) ** 2 == 20
    # Scalar complex rows 3, 4i, -3-4i close a 3-4-5 triangle.
    complex_rows = [(F(3), F(0)), (F(0), F(4)), (F(-3), F(-4))]
    assert all(sum(x[j] for x in complex_rows) == 0 for j in range(2))
    assert envelope([F(3), F(4), F(5)]) == 50
    bad_norms = [F(1)] * 100
    c = F(81) + F(1, 100) * 100
    actual = 1 - F(81, 1) / c
    new_bound = F(1, 100) * envelope(bad_norms) / c
    old_bound = min(F(1), F(1, 100) * (100 ** 2 - 100) / c)
    assert actual == new_bound == F(1, 82) and old_bound == 1
    return {
        "dominant_lengths_4_1_2": {"positive_trace": "20", "envelope": "20"},
        "closed_complex_3_4_5_triangle": {"positive_trace": "50", "envelope": "50"},
        "crowded_small_region": {"normalizer": str(c), "actual_deficit": str(actual),
                                 "new_bound": str(new_bound), "old_bound": str(old_bound)},
    }


def source_records():
    original = json.loads((ROOT / "certificates/whittaker-scalar-envelope.json").read_text())
    chosen = {
        "lean/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/PoincareInHH.lean": [(144, 199)],
        "lean/src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/TermOp.lean": [(207, 229)],
    }
    result = []
    for row in original["source_files"]:
        path = row["path"]
        if path not in chosen:
            continue
        raw = (ROOT / "build/source-cache/jsmorph/rh" / REVISION / path).read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        assert sha(raw) == row["sha256"] and blob == row["git_blob_sha1"]
        lines = raw.decode().splitlines(keepends=True)
        result.append({"path": path, "sha256": sha(raw), "git_blob_sha1": blob,
                       "excerpts": [{"lines": [a, b], "sha256": sha("".join(lines[a-1:b]).encode())}
                                    for a, b in chosen[path]]})
    assert len(result) == len(chosen)
    return result


def main():
    cases = {"coordinate_monotonicity": monotonicity_cases(),
             "positive_trace_and_source_projections": positive_trace_cases(),
             "finite_foldings_with_both_restrictions": folding_cases()}
    records = source_records()
    files = ["notes/dominant-return-deficit.md", "paper/shared/dominant-return-deficit.tex",
             "scripts/check_dominant_return_deficit.py"]
    certificate = {
        "result": "PASS", "source_repository": "jsmorph/rh", "source_revision": REVISION,
        "scope": "Exact rational finite-dimensional positive-trace and folding checks, sharp examples, and two freshly reread pinned source interfaces. Countable proof is in the note. No uniform arithmetic smallness, model existence, node closure or Lean build claimed.",
        "general_mathematics": "Projection variational formula, coordinatewise monotonicity and reverse triangle inequality prove the sharp envelope H=B-(2m-A)_+^2 for arbitrary complex rows. Integrable seed and period quadratic terms justify the arithmetic integration without an off-diagonal L1 assumption.",
        "tests": cases, "sharp_examples": sharp_examples(),
        "source_files": records,
        "files": [{"path": path, "sha256": sha((ROOT / path).read_bytes())} for path in files],
        "dependencies": [{"path": path, "sha256": sha((ROOT / path).read_bytes()),
                          "scope": "Existing written proof/certificate retained; its entire upstream check was not rerun by this script."}
                         for path in ("notes/seed-return-deficit.md", "certificates/whittaker-scalar-envelope.json",
                                      "scripts/check_seed_return_deficit.py")],
        "independent_review": "Root independently reconstructed the projection and monotonicity proof; final integration records any completed review separately.",
    }
    output = ROOT / "certificates/dominant-return-deficit.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "tests": cases, "certificate": str(output.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
