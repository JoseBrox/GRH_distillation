#!/usr/bin/env python3
"""Exact matrix and pinned-source checks for averaged theta energy.

All matrix arithmetic is rational. These computations supplement the
ordinary proofs; they do not construct arithmetic theta maps, estimate
their global energies, or replay the Lean kernel.
"""

from fractions import Fraction as F
from pathlib import Path
from itertools import product
import hashlib
import json
import random

ROOT = Path(__file__).resolve().parents[1]
COMMIT = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
CACHE = ROOT / "build/source-cache/jsmorph/rh" / COMMIT
SOURCES = [
    ("Formalism/SharpRestriction/CuspSpanNormBounds/DataS.lean",
     "05d6c08d180bf9804c8cf33b5873fc0c43e93bb4", [[13, 48]]),
    ("Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean",
     "d008b93b66125f83b7adb112628b058dde3b1096", [[320, 376]]),
    ("Formalism/SharpRestriction/GlobalTheoremInputs.lean",
     "ba31f5120ed089d48968754ae577427912d467c5", [[65, 89], [142, 160]]),
    ("Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean",
     "cbccb968fd96afe14797b8890f4e5dc63bd11d26",
     [[679, 723], [1004, 1107], [1110, 1122], [1218, 1315], [1317, 1381]]),
    ("Formalism/SizeWindowBrackets/FrameTraceRatioFinEquiv.lean",
     "c4e727f636c40a5b922efc2458465a587c884d8d", [[59, 77]]),
    ("Formalism/SizeWindowBrackets/TraceSquareAndDiagBounds.lean",
     "9fa80554a83904eb1cf696c7dd38fa88b5d9ad5c", [[38, 78], [80, 116]]),
]


def zeros(m, n):
    return [[F(0) for _ in range(n)] for _ in range(m)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def subtract(a, b):
    return add(a, scale(F(-1), b))


def multiply(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(ar, bc)), F(0))
             for bc in bt] for ar in a]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def hs2(a):
    return sum((x * x for row in a for x in row), F(0))


def rank_one(v):
    return [[x * y for y in v] for x in v]


def householder(n, rng):
    v = [F(rng.randint(1, 4)) for _ in range(n)]
    norm2 = sum(x * x for x in v)
    a = subtract(eye(n), scale(2 / norm2, rank_one(v)))
    assert multiply(transpose(a), a) == eye(n)
    return a


def family_energy(maps, d):
    q, mass, delta, rank = zeros(d, d), F(0), F(0), 0
    for a in maps:
        if a is None:
            continue
        r = len(a[0])
        gram = multiply(transpose(a), a)
        qi = multiply(a, transpose(a))
        q = add(q, qi)
        mass += trace(gram)
        delta += hs2(subtract(gram, eye(r)))
        rank += r
    variance = hs2(subtract(q, scale(mass / d, eye(d))))
    assert variance == trace(multiply(q, q)) - mass * mass / d >= 0
    assert (mass - rank) ** 2 <= rank * delta
    return {"q": q, "m": mass, "delta": delta, "r": rank,
            "v": variance, "eta": d * variance / mass ** 2 if mass else None}


def verify_pair(full_maps, retained_maps, d):
    f, r = family_energy(full_maps, d), family_energy(retained_maps, d)
    assert r["r"] > 0 and f["m"] > 0 and r["m"] > 0
    lost_rank, lost_mass = f["r"] - r["r"], f["m"] - r["m"]
    s = subtract(f["q"], r["q"])
    assert trace(s) == lost_mass >= 0
    assert r["delta"] <= f["delta"]
    assert (lost_mass - lost_rank) ** 2 <= lost_rank * f["delta"]
    # Positivity of the mixed trace is the decisive compression step.
    assert trace(multiply(s, r["q"])) >= 0
    alpha = f["m"] / r["m"]
    lhs = r["eta"] - (alpha - 1)
    if lhs > 0:
        # Equivalent to (2.4), with no floating-point square roots.
        assert lhs ** 2 <= alpha ** 2 * f["eta"] * r["eta"]
    # Trace-square identity with the exact diagonal correction.
    omega = F(0)
    for i, a in enumerate(full_maps):
        for j, b in enumerate(full_maps):
            if i != j:
                omega += hs2(multiply(transpose(a), b))
    assert trace(multiply(f["q"], f["q"])) == omega + 2*f["m"] - f["r"] + f["delta"]
    return f, r


def main():
    evidence = []
    for path, expected_blob, ranges in SOURCES:
        relative = "lean/src/" + path
        data = (CACHE / relative).read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == expected_blob, relative
        evidence.append({"path": relative, "git_blob_sha1": blob,
                         "sha256": hashlib.sha256(data).hexdigest(), "read_ranges": ranges})

    rng = random.Random(20261121)
    matrix_cases = noncoordinate_cases = kernel_cases = 0
    for d, count, repetition in product(range(2, 6), range(2, 5), range(10)):
        maps, retained = [], []
        for i in range(count):
            rank = 1 + rng.randrange(4)
            a = [[F(rng.randint(-3, 3), 2) for _ in range(rank)] for _ in range(d)]
            # Ensure at least the first retained map is nonzero.
            if i == 0:
                a[0][0] += 5
            keep = 1 + rng.randrange(rank) if i == 0 else rng.randrange(rank + 1)
            if keep == 0:
                aj = None
            else:
                u = householder(rank, rng)
                j = [row[:keep] for row in u]
                assert multiply(transpose(j), j) == eye(keep)
                aj = multiply(a, j)
                if 0 < keep < rank:
                    noncoordinate_cases += 1
            maps.append(a)
            retained.append(aj)
        full, restricted = verify_pair(maps, retained, d)
        matrix_cases += 1

        if repetition == 0:
            # Counting measure on d+2 points; H is a proper d-dimensional
            # subspace, so its projection kernel is not the ambient identity.
            ambient = d + 2
            u = [row[:d] for row in householder(ambient, rng)]
            assert multiply(transpose(u), u) == eye(d)
            projection = multiply(u, transpose(u))
            kernels, total = [], zeros(ambient, ambient)
            delta_from_kernel = F(0)
            for a in maps:
                functions = multiply(u, a)
                ki = multiply(functions, transpose(functions))
                kernels.append(ki)
                total = add(total, ki)
                delta_from_kernel += hs2(ki) - 2*trace(ki) + len(a[0])
            assert trace(total) == full["m"]
            assert delta_from_kernel == full["delta"]
            assert hs2(subtract(total, scale(full["m"] / d, projection))) == full["v"]
            kernel_cases += 1

    sharp_cases = 0
    for d in range(2, 9):
        maps = [[[F(i == j)] for i in range(d)] for j in range(d)]
        for keep in range(1, d + 1):
            full, retained = verify_pair(maps, maps[:keep] + [None]*(d-keep), d)
            assert full["eta"] == full["delta"] == retained["delta"] == 0
            assert retained["eta"] == (full["m"] - retained["m"]) / retained["m"]
            sharp_cases += 1

    envelope_cases = 0
    for sigma, qfraction, root_theta in product(
            (F(1, 20), F(1, 100), F(1, 1000)),
            (F(0), F(1, 3), F(1, 2)),
            (F(0), F(1, 10), F(1, 4), F(1, 3), F(1, 2))):
        q = qfraction * sigma
        theta = root_theta ** 2
        lam = (theta + q*root_theta) / (1-q)
        alpha = 1 / (1-lam)
        assert lam <= F(7, 26) and alpha <= F(26, 19)
        assert alpha - 1 <= F(80, 57)*theta + F(20, 57)*sigma
        target = 11*sigma + 3*theta
        v = alpha - 1
        assert target >= v
        # The target lies beyond the positive quadratic root in (2.3).
        assert (target - v)**2 >= alpha**2 * 5*sigma * target
        envelope_cases += 1
    assert 5*F(26, 19)**2 + F(40, 57) <= 11
    assert F(160, 57) <= 3
    for sigma in (F(1, 20), F(1, 100), F(1, 1000)):
        old_numerator = (1+sigma/2)*(1+sigma/2+sigma*(1+sigma/2)**2)
        exact_gap = (1+5*sigma)*(1-sigma/2)**2 - old_numerator
        assert exact_gap == sigma*(16-52*sigma+4*sigma*sigma-sigma**3)/8 > 0

    # Explicit failure of mass/diagonal control as a supplier for isotropy.
    for d in range(2, 9):
        repeated = [[[F(i == 0)] for i in range(d)] for _ in range(d)]
        energy = family_energy(repeated, d)
        assert energy["m"] == energy["r"] == d and energy["delta"] == 0
        assert energy["eta"] == d-1
    # Exact Gram eigenvalues 0 and 2: a tight frame with e=1.
    assert (F(0)-1)**2 + (F(2)-1)**2 == 2
    # Aggregate nonvanishing and correlation counterexamples.
    for n in (2, 5, 20, 100):
        energy = family_energy([[[F(0)]]] + [[[F(1)]]]*(n-1), 1)
        assert energy["delta"] / energy["r"] == F(1, n)
        assert energy["eta"] == 0
        assert F(1, n*n) * n**3 == n

    result = {
        "status": "PASS",
        "scope": "Exact finite rational matrix and scalar algebra plus pinned source-byte checks; no global theta-energy supplier, construction, Lean build or kernel replay.",
        "source": {"repository": "jsmorph/rh", "commit": COMMIT, "files": evidence},
        "checks": {"matrix_families": matrix_cases,
                   "noncoordinate_proper_isometric_compressions": noncoordinate_cases,
                   "proper_subspace_finite_measure_kernel_models": kernel_cases,
                   "sharp_tight_frame_compressions": sharp_cases,
                   "linear_rank_loss_envelopes": envelope_cases,
                   "normalization_and_counterexamples": "PASS"},
        "comparison_scope": "The current manuscript already has the linear envelope 7*sigma+4*theta. The alternative 11*sigma+3*theta is not a new exponent improvement over that manuscript. The new statements are the aggregate energy interface and exact retained-energy quadratic, including its sharp tight-frame case. The exponent improvement is only relative to the external source's square-root envelope.",
        "independent_reviews": [
            {"reviewer": "geometric_simplify", "status": "PASS",
             "scope": "Written Sections 1-2: scalar identities, noninjective/zero-map and rank cases, compression, exact quadratic, sharp example, all linear-envelope constants and qualified exponent comparison. No source-byte or Sections 3 onward audit."},
            {"reviewer": "rh_source_symmetry", "status": "PASS",
             "scope": "Written Sections 3-4, kernel identities with finite-sum representatives, exact normalization, actual common-basis arithmetic map bridge, isometric ramified inclusion, normalizer positivity caveat, correlated scale integral. Independently checked critical pinned bounded source contracts. No upstream theorem proof or kernel replay."},
            {"reviewer": "root", "status": "PASS",
             "scope": "Independent Sections 1-2 and linear constants, mathematical coherence of finite-kernel identities and normalization. Sigma-finite measure hypothesis requested and included."}
        ]
    }
    output = ROOT / "certificates/averaged-theta-energy.json"
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": result["status"], "checks": result["checks"],
                      "certificate": str(output.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    main()
