#!/usr/bin/env python3
"""Exact scalar-return and restriction checks; no arithmetic estimate."""

from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def tr(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def transpose(a):
    return list(map(list, zip(*a)))


def multiply(a, b):
    return [[sum((x * y for x, y in zip(row, col)), F(0))
             for col in transpose(b)] for row in a]


def gram(a, scale):
    return [[scale * x for x in row] for row in multiply(transpose(a), a)]


def positive_trace_le(a, threshold, bound):
    """Exact rational comparison in dimensions one and two."""
    if len(a) == 1:
        return max(a[0][0] - threshold, 0) <= bound
    assert len(a) == 2 and a[0][1] == a[1][0]
    t = tr(a) - 2 * threshold
    d = (a[0][0] - a[1][1]) ** 2 + 4 * a[0][1] ** 2
    if t >= 0 and d <= t * t:
        return t <= bound
    if t <= 0 and d <= t * t:
        return bound >= 0
    rhs = 2 * bound - t
    return rhs >= 0 and d <= rhs * rhs


def deficit_le(k, bound):
    a = [[F(i == j) - k[i][j] for j in range(len(k))] for i in range(len(k))]
    return positive_trace_le(a, F(0), bound)


def return_energy(rows, norms, labels, mu, size):
    a = [F(0)] * size
    b = [F(0)] * size
    folded = [[F(0)] * len(rows[0]) for _ in range(size)]
    for row, w, y in zip(rows, norms, labels):
        a[y] += w
        b[y] += w * w
        folded[y] = [x + z for x, z in zip(folded[y], row)]
    e = mu * sum(a[y] ** 2 - b[y] for y in range(size))
    assert e >= 0
    return folded, a, b, e


def scalar_cases():
    cases = 0
    for length in range(2, 6):
        for values in itertools.product((-2, -1, 0, 1, 2), repeat=length):
            if not any(values):
                continue
            mu = F(1, sum(v * v for v in values))
            rows = [[F(v)] for v in values]
            norms = [abs(F(v)) for v in values]
            for size in (1, 2, 3):
                labels = [j % size for j in range(length)]
                folded, a, b, e = return_energy(rows, norms, labels, mu, size)
                k = gram(folded, mu)
                assert mu * sum(b) == 1
                assert deficit_le(k, min(F(1), e))
                cases += 1
    return cases


def restricted_cases():
    cases = 0
    group = [[[F(s[i] if p[i] == j else 0) for j in range(2)] for i in range(2)]
             for p in ((0, 1), (1, 0)) for s in itertools.product((-1, 1), repeat=2)]
    source_cuts = [
        [[F(1)], [F(0)]], [[F(3, 5)], [F(4, 5)]],
        [[F(5, 13)], [F(12, 13)]], [[F(1), F(0)], [F(0), F(1)]],
    ]
    for w in ([F(1), F(0)], [F(3, 5), F(4, 5)], [F(5, 13), F(12, 13)]):
        original = [[v[0] for v in multiply(g, [[x] for x in w])] for g in group]
        for signs in ([1] * 8, [1, -1] * 4, [1, 1, -1, -1] * 2):
            rows = [[s * x for x in row] for row, s in zip(original, signs)]
            assert gram(rows, F(1, 4)) == [[F(1), F(0)], [F(0), F(1)]]
            for size, stride in itertools.product((2, 4, 8), (1, 3, 5)):
                labels = [(stride * j + j // size) % size for j in range(8)]
                _, full_a, _, full_e = return_energy(rows, [F(1)] * 8, labels, F(1, 4), size)
                # The compact Schur model has p=1 and b=1, hence F=full_a.
                envelope = full_a
                targets = []
                axis = [[F(i == 0)] for i in range(size)]
                targets.append(axis)
                rotated = [[F(0)] for _ in range(size)]
                rotated[0][0], rotated[1][0] = F(3, 5), F(4, 5)
                targets.append(rotated)
                plane = [[F(0), F(0)] for _ in range(size)]
                if size == 2:
                    plane[0][0], plane[1][1] = F(1), F(1)
                else:
                    plane[0][0], plane[2][0] = F(3, 5), F(4, 5)
                    plane[1][1], plane[3][1] = F(5, 13), F(12, 13)
                targets.append(plane)
                for jmat in source_cuts:
                    rank = len(jmat[0])
                    restricted = multiply(rows, jmat)
                    norms = ([abs(row[0]) for row in restricted]
                             if rank == 1 else [F(1)] * 8)
                    folded, a, b, energy = return_energy(restricted, norms, labels, F(1, 4), size)
                    assert F(1, 4) * sum(b) == rank
                    assert energy <= full_e
                    before = gram(folded, F(1, 4))
                    assert deficit_le(before, min(F(rank), energy))
                    for umat in targets:
                        n = len(umat[0])
                        orth = multiply(transpose(umat), umat)
                        assert orth == [[F(i == j) for j in range(n)] for i in range(n)]
                        final = multiply(transpose(umat), folded)
                        source = gram(final, F(1, 4))
                        target = gram(transpose(final), F(1, 4))
                        lost = tr(before) - tr(source)
                        assert lost >= 0
                        diag = [sum(x * x for x in row) for row in umat]
                        lost_bound = sum(envelope[y] * (1 - diag[y]) for y in range(size))
                        assert lost <= lost_bound
                        assert deficit_le(source, min(F(rank), energy) + lost)
                        excess = sum(max(envelope[y] - F(rank, n), 0) * diag[y]
                                     for y in range(size))
                        assert positive_trace_le(target, F(rank, n), excess)
                        cases += 1
    return cases


def sharp_examples():
    records = []
    for values, expected in (([1, -1], F(1)), ([1, 1], F(0))):
        rows = [[F(t)] for t in values]
        folded, a, b, energy = return_energy(rows, [F(1), F(1)], [0, 0], F(1, 2), 1)
        k = gram(folded, F(1, 2))[0][0]
        assert F(1, 2) * sum(t * t for t in values) == 1
        assert energy == 1 and max(1 - k, 0) == expected
        records.append({"seed_values": values, "source_deficit": str(expected),
                        "absolute_return_bound": str(energy)})
    return records


def main():
    dependency_path = ROOT / "certificates/whittaker-scalar-envelope.json"
    dependency = json.loads(dependency_path.read_text())
    assert dependency["result"] == "PASS"
    for row in dependency["files"]:
        assert sha((ROOT / row["path"]).read_bytes()) == row["sha256"], row["path"]
    cache = ROOT / "build/source-cache/jsmorph/rh" / dependency["source_revision"]
    for row in dependency["source_files"]:
        assert sha((cache / row["path"]).read_bytes()) == row["sha256"], row["path"]
    cases = {"scalar_returns": scalar_cases(), "both_restrictions": restricted_cases()}
    sharp = sharp_examples()
    names = ["notes/seed-return-deficit.md", "paper/shared/seed-return-deficit.tex",
             "scripts/check_seed_return_deficit.py"]
    report = {
        "result": "PASS",
        "scope": "Exact finite scalar/vector returns, genuine source and target cuts, and frozen dependency hashes. No arithmetic return estimate or Lean replay.",
        "independent_review_scope": "Independent mathematical reviews are recorded separately by the parent integration; automated checks only here.",
        "dependency": {"path": str(dependency_path.relative_to(ROOT)),
                       "sha256": sha(dependency_path.read_bytes()),
                       "source_files_rechecked": len(dependency["source_files"])},
        "files": [{"path": name, "sha256": sha((ROOT / name).read_bytes())} for name in names],
        "exact_cases": cases, "sharp_examples": sharp,
    }
    output = ROOT / "certificates/seed-return-deficit.json"
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "exact_cases": cases,
                      "sharp_examples": len(sharp), "certificate": str(output.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
