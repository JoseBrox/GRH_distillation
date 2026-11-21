#!/usr/bin/env python3
"""Exact checks for the averaged geometric comparison, not a Lean replay.

Populate the two pinned sources with scripts/source_excerpt.py --atlas before
running this script. The ordinary proofs are in notes/rh-geometric-combination.md.
The finite rational cases supplement those proofs; they do not establish a
uniform arithmetic-geometric estimate for the actual growing family.
"""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REVISION = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
SOURCES = [
    {
        "path": "lean/src/Development/AbelianVarietyTheory/Definitions/Divisors/CovolXOfCovol.lean",
        "git_blob_sha1": "4ed4695093989e1f18246a3244b79102db6c548e",
        "sha256": "f40c762ed8c2b18311d604540c15613e4a5969b1395dcab59b2854584fb6d3ae",
        "inspected_ranges": [[65, 131], [133, 159]],
    },
    {
        "path": "lean/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/LowerBoundOfAllEstimates.lean",
        "git_blob_sha1": "4d30dd405b7d5b26d61d37507a095cc7ef426dc5",
        "sha256": "111bbcfa0022d90c5aebb3d52247857c8f10ff9269cc369f5d2eaae8a76637d9",
        "inspected_ranges": [[18, 51], [65, 105]],
    },
]


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def main():
    for item in SOURCES:
        paths = [ROOT / "build/lean-mirror" / item["path"],
                 ROOT / "build/source-cache/jsmorph/rh" / REVISION / item["path"]]
        path = next((path for path in paths if path.is_file()), None)
        if path is None:
            raise FileNotFoundError("Populate pinned source cache: " + item["path"])
        data = path.read_bytes()
        assert sha256(data) == item["sha256"]
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == item["git_blob_sha1"]
        count = len(data.splitlines())
        assert all(1 <= start <= end <= count for start, end in item["inspected_ranges"])
        item["bytes"] = len(data)
        item["line_count"] = count

    beta, lam, lamcap, T, C, U = sp.symbols("beta lambda Lambda T C U", real=True)
    direct = lam * (-T - C * U - 2 * beta) - 2 * (1 - lam) * lamcap - 2 * beta
    collected = -T - lam * C * U - 2 * beta * (1 + lam) - (1 - lam) * (2 * lamcap - T)
    assert sp.expand(direct - collected) == 0

    rational_descent_cases = 0
    for b in [F(1), F(2), F(3)]:
        for ratio in range(1, 11):
            cap = b * ratio
            low = cap / (cap + b)
            for frac in [F(0), F(1, 4), F(1, 2), F(1)]:
                l = low + frac * (1 - low)
                assert (1 - l) * cap <= l * b
                for t in [-cap, -cap / 2, F(0), cap / 2, cap]:
                    for c in [F(0), F(1), F(17, 3)]:
                        for u in [b, 2 * b]:
                            error = l * c * u + 2 * b * (1 + l) + (1 - l) * (2 * cap - t)
                            assert error <= c * u + 7 * u
                            rational_descent_cases += 1

    N = sp.symbols("N", positive=True, integer=True)
    nu_B = (N * (N - 2) - 2 * N) / (N + 1)
    extremal_defect = sp.simplify(N - (nu_B - 2))
    assert sp.simplify(extremal_defect - (2 + 5 * N / (N + 1))) == 0
    assert sp.limit(extremal_defect, N, sp.oo) == 7

    M, a, c, A, b = sp.symbols("M a c A b", real=True)
    phi = b * M - 2 * a * c - A * sp.log(2 + M + 2 * c)
    assert sp.simplify(sp.diff(phi, M) - (b - A / (2 + M + 2 * c))) == 0
    assert sp.simplify(sp.diff(phi, M, 2) - A / (2 + M + 2 * c) ** 2) == 0
    assert sp.simplify(sp.diff(phi, M).subs(M, A / b - 2 - 2 * c)) == 0

    moment_models = 0
    for c0 in [F(0), F(1, 5), F(1), F(9, 2)]:
        for off in [F(0), F(1, 7), F(1), F(5), F(13)]:
            m0 = -c0 + off
            z = m0 + 2 * c0
            if z == 0:
                assert c0 == m0 == 0
                continue
            minus = c0 / z
            plus = 1 - minus
            assert 0 <= minus <= 1 and 0 <= plus <= 1
            assert minus * (-z) + plus * z == m0
            assert minus * z == c0
            assert minus * z + plus * z == m0 + 2 * c0
            moment_models += 1

    x1, x2, y1, y2 = sp.symbols("x1 x2 y1 y2", real=True)
    cauchy_gap = (x1*x1 + x2*x2) * (y1*y1 + y2*y2) - (x1*y1 + x2*y2)**2
    assert sp.expand(cauchy_gap - (x1*y2 - x2*y1)**2) == 0

    u, h = sp.symbols("u h", positive=True)
    du, dh = sp.symbols("du dh", real=True)
    perspective = u * sp.log(1 + h/u)
    hessian_form = (du**2 * sp.diff(perspective, u, 2)
                    + 2*du*dh*sp.diff(perspective, u, h)
                    + dh**2 * sp.diff(perspective, h, 2))
    assert sp.simplify(hessian_form + (h*du-u*dh)**2 / (u*(u+h)**2)) == 0
    assert sp.limit(perspective, u, 0, dir="+") == 0
    assert sp.limit(sp.sqrt(u*(u+h))-u, u, 0, dir="+") == 0

    note_path = "notes/rh-geometric-combination.md"
    record = {
        "status": "PASS",
        "repository": "jsmorph/rh",
        "commit": REVISION,
        "source_files": SOURCES,
        "note": note_path,
        "note_sha256": sha256((ROOT / note_path).read_bytes()),
        "script": "scripts/check_rh_geometric_combination.py",
        "script_sha256": sha256(Path(__file__).read_bytes()),
        "exact_checks": {
            "rational_covering_descent_cases": rational_descent_cases,
            "sharp_two_moment_models": moment_models,
            "covering_rearrangement": True,
            "constant_seven_extremal_family_and_limit": True,
            "component_optimization_derivatives": True,
            "cauchy_schwarz_square_identity": True,
            "log_perspective_hessian": True,
            "zero_source_spread_limits": True,
        },
        "independent_review": {
            "status": "PASS",
            "reviewer": "rh_source_symmetry",
            "scope": "Sections 1--3: normalized-rank descent and sharpness; two-height-moment optimization, equality cases and K* <= K0; weighted refined-frame inequalities, denominators and zero cases. Refined frame statement matched to manuscript qrh-sharper-slope.",
            "limits": "The reviewer did not independently re-download the geometric source files or audit upstream geometric suppliers. Section 4 is a substitution into the separately reviewed direct-transfer result.",
        },
        "scope": "Pinned source integrity and exact symbolic/rational supplementary checks. Full ordinary proofs are in the note. No Lean build, kernel replay, geometric supplier verification, or uniform RH estimate is asserted.",
    }
    output = ROOT / "certificates/rh-geometric-combination.json"
    output.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": record["status"], "exact_checks": record["exact_checks"],
                      "certificate": str(output.relative_to(ROOT)), "scope": record["scope"]}, indent=2))


if __name__ == "__main__":
    main()
