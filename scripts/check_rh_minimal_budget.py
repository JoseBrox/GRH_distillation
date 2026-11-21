#!/usr/bin/env python3
"""Exact arithmetic and source-byte checks for the minimal RH budget.

The computations check algebra and pinned definitions, not existence of the
arithmetic-geometric constructor or a Lean kernel replay.
"""

from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
COMMIT = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
CACHE = ROOT / "build/source-cache/jsmorph/rh" / COMMIT
SOURCES = [
    ("Formalism/SharpRestriction/InertJacobiLevels/AsmIface.lean",
     "1c01d77eca74ee32a49d3ec089b799c87c0d2c25", [[120, 144]]),
    ("Formalism/LocalRingCardinality/DataParams₂.lean",
     "50914500995df91e2646d91a6c5c99a7e603a51b", [[27, 45]]),
    ("Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean",
     "7828c8b1060818fe158e23f87f1ad9e2efcf79eb", [[1070, 1070], [1390, 1396]]),
    ("Formalism/SizeWindowBrackets/SChain.lean",
     "a4bc8cecac40a1f5fd307661e151639aaf6a6efa", [[33, 58]]),
    ("Formalism/SizeWindowBrackets/ErrorFormsWeakWindowsFalse.lean",
     "1d1d179d111b5aa668893327264648558f30fdb6", [[16, 45]]),
]


def plus(*pairs):
    return tuple(sum((p[j] for p in pairs), F(0)) for j in (0, 1))


def times(coefficient, pair):
    return tuple(coefficient * x for x in pair)


def main():
    evidence = []
    for relative, blob, ranges in SOURCES:
        path = "lean/src/" + relative
        data = (CACHE / path).read_bytes()
        actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert actual == blob, path
        evidence.append({"path": path, "git_blob_sha1": actual,
                         "sha256": hashlib.sha256(data).hexdigest(), "read_ranges": ranges})

    checks = 0
    for n in (1, 2, 5):
        for t, s in product(range(1, n + 1), repeat=2):
            for m, b, rank, x, z in product((1, 3), (2, 7), (10, 17), (3, 9), (1, 2)):
                n, t, s, m, b, rank, x, z = map(F, (n, t, s, m, b, rank, x, z))
                density, tau = s / n, t / n
                normalizer = t * m * b * density / 2
                old = (t * 2 * x * b * (1 + m * m / rank)
                       + m * (2 * n * m * b * z + s * rank * b * z * z / (n * n)))
                new = (4 * x / (density * m) + 4 * x * m / (density * rank)
                       + 4 * m * z / (density * tau) + 2 * rank * z * z / (tau * n * n))
                assert old / normalizer == new
                checks += 1

    # Affine exponent pairs mean constant + epsilon_coefficient * epsilon.
    x = (F(1), F(0))
    inverse_d = (F(0), F(1))
    inverse_tau = (F(0), F(1, 8))
    m = (F(1, 2), F(-1, 16))
    rank = (F(9, 2), F(10))
    n = (F(2), F(8))
    eps = (F(0), F(1))
    exponents = [
        plus(x, inverse_d, times(-1, m)),
        plus(x, m, inverse_d, times(-1, rank)),
        plus(m, eps, inverse_d, inverse_tau),
        plus(rank, times(2, eps), inverse_tau, times(-2, n)),
    ]
    expected = [(F(1, 2), F(17, 16)), (F(-3), F(-145, 16)),
                (F(1, 2), F(33, 16)), (F(1, 2), F(-31, 8))]
    assert exponents == expected
    target = (F(1, 2), F(33, 16))
    assert all(all(a <= b for a, b in zip(pair, target)) for pair in exponents)
    assert sum((4, 8, 16, 8)) == 36
    entropy = plus(rank, inverse_tau, times(-1, n), times(-1, m), inverse_d)
    assert entropy == (F(2), F(51, 16))
    height_offset = plus(inverse_tau, times(-1, n), times(-1, m), inverse_d)
    assert height_offset == (F(-5, 2), F(-109, 16))

    frame_checks = 0
    for a, b in product((F(0), F(1, 3), F(1), F(2), F(7)), repeat=2):
        gap = (a / 3 + 5 * b / 6) ** 2 - (a * b + b * b / 4)
        assert gap == (a - 2 * b) ** 2 / 9 >= 0
        assert a / 3 + 5 * b / 6 >= 0
        frame_checks += 1
    assert (F(2) / 3 + F(5) / 6) ** 2 == F(2) + F(1, 4)

    note = ROOT / "notes/rh-minimal-budget.md"
    certificate = {
        "status": "PASS",
        "scope": "exact scalar identities, exponent arithmetic and pinned source bytes only",
        "repository": "jsmorph/rh", "commit": COMMIT, "sources": evidence,
        "normalization_cases": checks,
        "four_terms": [{"coefficient": c, "constant_exponent": str(p[0]),
                        "epsilon_coefficient": str(p[1])}
                       for c, p in zip((4, 8, 16, 8), exponents)],
        "final_multiplier": 36, "final_loss_over_C": "33/16",
        "frame_square_identity_cases": frame_checks,
        "sharp_frame_factor": "4/3 at A=2B",
        "entropy_exponent_before_exp_minus_x_epsilon": [str(v) for v in entropy],
        "normalized_height_exponent_offset": [str(v) for v in height_offset],
        "independent_frame_review": {
            "reviewer": "geometric_simplify", "result": "PASS",
            "scope": "sharp 4/3 majorant and accuracy exponents, with explicit extra allowance for log x",
        },
        "independent_scalar_and_transfer_review": {
            "reviewer": "geometric_simplify", "result": "PASS",
            "scope": "sections 1–3; independently bounded/hash-checked source rank windows and cardinality",
            "checked": [
                "exact normalization and four affine exponents",
                "factor 36 and comparison with old generic scalar loss",
                "m and K optimization with actual-source exclusion",
                "transfer thresholds, thin scale and domain",
                "source-density qualification for weaker thin accuracy",
                "normalized height exponent 109/16 and word-count exponent 51/16",
            ],
        },
        "independent_manuscript_review": {
            "reviewer": "geometric_simplify", "result": "PASS",
            "file": "paper/sections/recovered/04-sec-numerical.tex",
            "label": "prop:rh-four-term-budget",
            "scope": "integrated theorem and proof, domains, exact constants and exponents, conditional construction scope",
        },
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "note_sha256": hashlib.sha256(note.read_bytes()).hexdigest(),
        "no_new_constructor_or_lean_build": True,
    }
    path = ROOT / "certificates/rh-minimal-budget.json"
    path.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: certificate[k] for k in
                      ("status", "normalization_cases", "final_loss_over_C",
                       "frame_square_identity_cases")}, sort_keys=True))


if __name__ == "__main__":
    main()
