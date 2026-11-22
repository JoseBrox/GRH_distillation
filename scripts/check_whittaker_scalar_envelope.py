#!/usr/bin/env python3
"""Exact finite checks and pinned-source provenance, not a theta estimate."""

from __future__ import annotations

from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
REVISION = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
CACHE = ROOT / "build/source-cache/jsmorph/rh" / REVISION / "lean/src"
PREFIX = "Formalism/LocalToGlobal/SiegelLatticeTheory/"
SOURCES = [
    (PREFIX + "HaarTransversals/HidaSetting.lean",
     "20d8b16845b77d6f9cfd258f54474e742eefb34b6db851f1ee4f6617f2f30350",
     [(136, 156), (207, 231), (267, 317), (338, 363)]),
    ("Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean",
     "3be6a65abf5c2a48523ea59af7fe7356bee69cf0246a60eaf0de2c360e053fed",
     [(23, 28), (61, 66), (94, 96)]),
    (PREFIX + "HaarTransversals/PoincareInHH.lean",
     "aefc3163325ffcdb11603f7244f4449ebde4087a698c4553c6ba4b4d52e645e1",
     [(60, 75), (100, 132), (144, 199), (248, 263)]),
    (PREFIX + "SiegelMassRatios/ColsDim.lean",
     "51033a560e7b43d615dc40c32049caedc6be52c4674fc2f35d6a8b919f6da0bf",
     [(18, 96)]),
    (PREFIX + "ClosedLocalOrbits/TermOp.lean",
     "2f6b9f6b12b4c8e72eee70f0256a5cd9da07af5c70c540f13f8ce060cfdf25fa",
     [(207, 229)]),
    (PREFIX + "FlagStabilizerTensors/ParametersTermRelations.lean",
     "b47b7ccfb755e3b3e013592e6897866d52c357d7f86033ccea4923bbaeee31e7",
     [(38, 75)]),
    (PREFIX + "FlagStabilizerTensors/PoincareConstantEq.lean",
     "0c8d01b4349c6ef30f3e4b9196c98fc05d9c042e593f727bb0bbd1a50990fee0",
     [(25, 59)]),
    (PREFIX + "ClosedLocalOrbits/GaugeLatticeShifts/IdMeetVolSteps.lean",
     "fdec1c4f6e91e7f2a880f9e4285bb10e9db8758ac83635f89f1d29a2e90f95f1",
     [(24, 40)]),
    (PREFIX + "ClosedLocalOrbits/GaugeLatticeShifts/IdMeetVolEqPf.lean",
     "d53bd70064ba60d260f9adfa9a46b3c0125f9a024d2c8c2d61de1896ab7391e7",
     [(19, 58)]),
    (PREFIX + "ClosedLocalOrbits/GaugeLatticeShifts/SlabCoverPf.lean",
     "96929055ee9b086997bd97f077b4716a1be493ded9605a6339d3a1b48887a34a",
     [(17, 89)]),
    (PREFIX + "ClosedLocalOrbits/GaugeLatticeShifts/KExpCut.lean",
     "769e7b590bc95de93bdfa5a94d07d4ed7ced3fc87d18d8aa090fed2dee912040",
     [(622, 637)]),
    ("Formalism/SharpRestriction/CuspSpanNormBounds/AdmissibleBoundsFromSource.lean",
     "fdd8922dcd54badfe1a700feba89a02a8359c1bc93f839283c278f5b146b3cb8",
     [(212, 244)]),
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def provenance() -> list[dict]:
    with gzip.open(ROOT / "blueprint/lean-source-imports.json.gz", "rt") as f:
        atlas = {m[0]: m for m in json.load(f)["modules"]}
    report = []
    for path, expected, ranges in SOURCES:
        raw = (CACHE / path).read_bytes()
        assert sha(raw) == expected, path
        name = path[:-5].replace("/", ".")
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        assert blob == atlas[name][1], path
        lines = raw.splitlines(keepends=True)
        excerpts = []
        for first, last in ranges:
            assert 1 <= first <= last <= len(lines) and last - first < 120
            excerpts.append({"lines": [first, last],
                             "sha256": sha(b"".join(lines[first - 1:last]))})
        report.append({"path": "lean/src/" + path, "sha256": expected,
                       "git_blob_sha1": blob, "excerpts": excerpts})
    return report


def transpose(a):
    return list(map(list, zip(*a)))


def multiply(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), F(0))
             for col in bt] for row in a]


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def psd(a):
    """Exact Schur-complement elimination; zero pivots require a zero row."""
    a = [row[:] for row in a]
    while a:
        assert a == transpose(a)
        t = a[0][0]
        if t < 0:
            return False
        if t == 0:
            if any(a[0][j] != 0 for j in range(1, len(a))):
                return False
            a = [row[1:] for row in a[1:]]
        else:
            a = [[a[i][j] - a[i][0] * a[0][j] / t
                  for j in range(1, len(a))] for i in range(1, len(a))]
    return True


def positive_trace_le_2(a, alpha, bound):
    """Compare the 2 by 2 spectral positive trace using only rational squares."""
    tr = a[0][0] + a[1][1]
    disc = (a[0][0] - a[1][1]) ** 2 + 4 * a[0][1] ** 2
    t = tr - 2 * alpha
    if t >= 0 and disc <= t * t:
        return t <= bound
    if t <= 0 and disc <= t * t:
        return bound >= 0
    rhs = 2 * bound - t
    return rhs >= 0 and disc <= rhs * rhs


def compact_group():
    # The irreducible two-dimensional representation of the dihedral group.
    return [a for p in ((0, 1), (1, 0))
            for s in itertools.product((-1, 1), repeat=2)
            for a in [[[F(s[i] if p[i] == j else 0) for j in range(2)]
                       for i in range(2)]]]


def exact_compact_checks():
    group = compact_group()
    counts = {"schur": 0, "seed_isometry": 0, "weighted_seed_isometry": 0,
              "full_fold_majorant": 0,
              "restricted_positive_trace": 0, "radial_mass": 0,
              "haar_rescaling": 0}
    profiles = [
        [[F(1), F(0)], [F(0), F(1)], [F(6, 5), F(8, 5)]],
        [[F(3, 5), F(4, 5)], [F(-4, 5), F(3, 5)], [F(0), F(2)]],
    ]
    norms = [F(1), F(1), F(2)]
    qweight = F(1, 6)
    a = sum(norms) * qweight
    assert sum(t * t for t in norms) * qweight == 1
    for ws in profiles:
        for w in ws:
            v = [multiply(g, [[x] for x in w]) for g in group]
            avg = [[sum(z[i][0] * z[j][0] for z in v) / 8
                    for j in range(2)] for i in range(2)]
            assert avg == [[F(i == j) * sum(x * x for x in w) / 2
                            for j in range(2)] for i in range(2)]
            counts["schur"] += 1

        for m in (1, 2):
            # Exact product cells: column, a nontrivial N character, H, quotient.
            rows, radial, positions = [], [], []
            for rho, n, h, x in itertools.product(range(m), (-1, 1), group, range(3)):
                v = multiply(h, [[t] for t in ws[x]])
                row = [F(0)] * (2 * m)
                row[2 * rho:2 * rho + 2] = [n * t[0] for t in v]
                rows.append(row)
                radial.append(norms[x])
                positions.append(x)
            gram = multiply(transpose(rows), rows)
            assert gram == [[48 * F(i == j) for j in range(2 * m)]
                            for i in range(2 * m)]
            for p in (norms, [t * t for t in norms], [F(1)] * 3,
                      [F(1, 2), F(3), F(4)]):
                b = sum(norms[i] ** 2 / p[i] for i in range(3)) * qweight
                weighted = [[sum(row[i] * row[j] / p[x]
                                  for row, x in zip(rows, positions))
                             for j in range(2 * m)] for i in range(2 * m)]
                assert weighted == [[48 * b * F(i == j) for j in range(2 * m)]
                                    for i in range(2 * m)]
                counts["weighted_seed_isometry"] += 1
            # mu_cell/c = 1/48 for arbitrary v_K, v_N, v_H.
            for vk, vn, vh in itertools.product((F(1), F(3, 5)),
                                                (F(1, 2), F(7, 3)),
                                                (F(1), F(5))):
                c = vk * vn * vh / 2
                mu = vk * vn * vh / 96
                assert mu * 48 == c
                assert mu * a * sum(radial) == c * (2 * m) * a * a
                counts["seed_isometry"] += 1

            for size in (4, 6, 8, 12):
                for stride in (1, 5, 7):
                    # A full finite folding: no return term is omitted.
                    pp = [[F(0)] * (2 * m) for _ in range(size)]
                    theta = [F(0)] * size
                    for j, row in enumerate(rows):
                        y = (stride * j + j // size) % size
                        pp[y] = [x + z for x, z in zip(pp[y], row)]
                        theta[y] += a * radial[j]
                    assert all(t > 0 for t in theta)
                    # diag(theta) - PP*/48 >=0 iff this small matrix >=0.
                    small = [[F(i == j) - sum(pp[y][i] * pp[y][j] / theta[y]
                                             for y in range(size)) / 48
                              for j in range(2 * m)] for i in range(2 * m)]
                    assert psd(small)
                    counts["full_fold_majorant"] += 1

                    for rotated in (False, True):
                        jmat = identity(2 * m)
                        if rotated:
                            jmat[0][:2] = [F(3, 5), F(-4, 5)]
                            jmat[1][:2] = [F(4, 5), F(3, 5)]
                        for rank in (1, 2 * m):
                            jj = [row[:rank] for row in jmat]
                            # Two orthonormal target vectors, with a genuine cut.
                            uu = [[F(0), F(0)] for _ in range(size)]
                            uu[0][0], uu[2][0] = F(3, 5), F(4, 5)
                            uu[1][1], uu[3][1] = F(5, 13), F(12, 13)
                            assert multiply(transpose(uu), uu) == identity(2)
                            restricted = multiply(transpose(uu), multiply(pp, jj))
                            q0 = [[x / 48 for x in row]
                                  for row in multiply(restricted, transpose(restricted))]
                            assert psd(q0)
                            diag_kernel = [sum(x * x for x in row) for row in uu]
                            for alpha in (F(1, 3), F(1), F(2), F(5)):
                                bound = sum(max(theta[y] - alpha, 0) * diag_kernel[y]
                                            for y in range(size))
                                assert positive_trace_le_2(q0, alpha, bound)
                                counts["restricted_positive_trace"] += 1

        for p in (norms, [t * t for t in norms], [F(1)] * 3,
                  [F(1, 2), F(3), F(4)]):
            b = sum(norms[i] ** 2 / p[i] for i in range(3)) * qweight
            mass = sum(p) * qweight
            assert b * mass >= a * a
            if p == norms:
                assert b == a and b * mass == a * a
            counts["radial_mass"] += 1
        for sqrt_t in (F(1, 3), F(2), F(5, 2)):
            t = sqrt_t ** 2
            new_a = sum(sqrt_t * v for v in norms) * qweight / t
            assert new_a == a / sqrt_t
            assert [new_a * sqrt_t * v for v in norms] == [a * v for v in norms]
            counts["haar_rescaling"] += 1
    return counts


def determinant_checks():
    i, q = sp.I, sp.Rational
    examples = [
        (sp.Matrix([[(3 + 4 * i) / 5]]), sp.eye(1)),
        (sp.Matrix([[q(3, 5), q(4, 5)], [-q(4, 5), q(3, 5)]]), sp.eye(2)),
        (sp.diag((3 + 4 * i) / 5, i), sp.eye(2)),
        (sp.Matrix([[q(5, 3), q(4, 3)], [q(4, 3), q(5, 3)]]), sp.diag(1, -1)),
        (sp.Matrix([[q(3, 5), 4 * i / 5], [4 * i / 5, q(3, 5)]]), sp.eye(2)),
    ]
    cases = 0
    for h, form in examples:
        assert sp.simplify(h.conjugate().T * form * h - form) == sp.zeros(h.rows)
        assert sp.simplify(h.det() * sp.conjugate(h.det())) == 1
        action = h.inv().T
        real = action.applyfunc(sp.re)
        imag = action.applyfunc(sp.im)
        block = real.row_join(-imag).col_join(imag.row_join(real))
        for r in range(4):
            matrix = sp.diag(*([block] * r)) if r else sp.zeros(0)
            assert sp.simplify(matrix.det()) == 1
            cases += 1
    return cases


def main():
    sources = provenance()
    counts = exact_compact_checks()
    counts["unitary_modulus"] = determinant_checks()
    files = ["notes/whittaker-scalar-envelope.md",
             "paper/shared/whittaker-scalar-envelope.tex",
             "scripts/check_whittaker_scalar_envelope.py"]
    report = {
        "result": "PASS", "source_repository": "jsmorph/rh",
        "source_revision": REVISION,
        "scope": "Pinned source interfaces and exact finite coefficient/folding checks; the general proofs are in the note. No arithmetic smallness estimate, model existence or Lean replay is claimed.",
        "independent_review_scope": "Independent mathematical reviews are recorded separately by the parent integration; this certificate covers automated checks only.",
        "files": [{"path": p, "sha256": sha((ROOT / p).read_bytes())} for p in files],
        "source_files": sources, "exact_cases": counts,
    }
    output = ROOT / "certificates/whittaker-scalar-envelope.json"
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "source_files": len(sources),
                      "source_excerpts": sum(len(s["excerpts"]) for s in sources),
                      "exact_cases": counts, "certificate": str(output.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
