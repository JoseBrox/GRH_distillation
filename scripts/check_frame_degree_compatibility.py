#!/usr/bin/env python3
"""Exact checks for centered frames, slope deductions and degree obstructions.

This checks selected pinned source bytes and finite algebraic models.
It does not establish the upstream theta, height or geometric hypotheses.
"""

from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NOTE = "notes/frame-degree-compatibility.md"
OUT = "certificates/frame-degree-compatibility.json"
SOURCES = [
    ("Formalism.SizeWindowBrackets.FrameTraceRatioFinEquiv",
     "8487d2f1b12227416fe72c5e1f70f4b41e8518d908f8ae00d81c236fe8cfa2a2",
     [[59, 90]]),
    ("Formalism.SharpRestriction.GlobalTheoremInputs",
     "4d51ccc0586441a159ad6d09ebc0a46b3c462e3c5b296d5a5bd7613266e17bfb",
     [[65, 89]]),
    ("Formalism.SharpRestriction.GlobalSchurBounds.TopDensityNGeSixteen",
     "f952a3ad11b8a3e5ae77f196fa3c434780eea7db9905f9a6941148d8e2d299b7",
     [[679, 689], [1004, 1015], [1218, 1258]]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.RelevantZeroGramTerms",
     "3be6a65abf5c2a48523ea59af7fe7356bee69cf0246a60eaf0de2c360e053fed",
     [[335, 344]]),
    ("Formalism.HarderNarasimhan.StatementPl",
     "16766730a8dd781538ca5035ff73ddf7612decae9f293bbd995679093d9adc39",
     [[55, 65]]),
    ("Development.AbelianVarietyTheory.Definitions.Divisors.NormNegCmConstantEqAtAllEmbeddings",
     "d07c8d791d45bd5f9a8b4e9fd99192dd1a0b8fc61c0471e06c98fc5f96da98c1",
     [[276, 288]]),
    ("Development.AbelianVarietyTheory.Definitions.Divisors.CovolXOfCovol",
     "f40c762ed8c2b18311d604540c15613e4a5969b1395dcab59b2854584fb6d3ae",
     [[92, 96]]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def check_sources():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    blobs = {r[0]: r[1] for r in atlas["modules"]}
    out = []
    for module, expected, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        candidates = [ROOT / "build/source-cache/jsmorph/rh" / REV / rel,
                      ROOT / "build/lean-mirror" / rel]
        local = next((p for p in candidates if p.is_file()), None)
        if local is None:
            raise FileNotFoundError("Populate the pinned cache for " + module)
        data = local.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == blobs[module] and sha(data) == expected
        lines = data.splitlines()
        excerpts = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines) and end-start < 120
            passage = b"\n".join(lines[start-1:end]) + b"\n"
            excerpts.append({"lines": [start, end], "sha256": sha(passage)})
        out.append({"module": module, "path": rel, "git_blob_sha1": blob,
                    "sha256": expected, "bytes": len(data),
                    "inspected_excerpts": excerpts})
    return out


def hs2(A):
    return sp.trace(A.T*A)


def range_projection(A):
    cols = A.columnspace()
    if not cols:
        return sp.zeros(A.rows)
    B = sp.Matrix.hstack(*cols)
    return B*(B.T*B).inv()*B.T


def matrix_checks():
    count = 0
    P_options = [sp.zeros(2), sp.eye(2), sp.diag(1, 0),
                 sp.Matrix([[1, 2], [2, 4]])/5]
    for D, seed in itertools.product([2, 3], range(1, 17)):
        T0 = sp.Matrix(D, 2, lambda i, j: (seed + 2*i + 3*j) % 5 - 2)
        T1 = sp.Matrix(D, 1, lambda i, j: (2*seed + i) % 5 - 2)
        S = sp.diag(T0.T*T0, T1.T*T1)
        Q = T0*T0.T + T1*T1.T
        R = sp.Integer(3)
        M = sp.trace(S)
        assert M > 0 and M == sp.trace(Q)
        U = sp.trace(S*S)
        Vs, Vt = hs2(S-M/R*sp.eye(3)), hs2(Q-M/D*sp.eye(D))
        Delta = hs2(S-sp.eye(3))
        assert Vs == Delta-(M-R)**2/R and Vs >= 0 and Vt >= 0
        e_opt = 1-M*M/(R*U)
        a2 = R*Vs/(M*M)
        assert 0 <= e_opt < 1 and e_opt == a2/(1+a2)
        assert Delta/R-e_opt == U/R*(1-M/U)**2
        assert (M/U)*M/R == 1-e_opt
        for P0, p1 in itertools.product(P_options, [0, 1]):
            P = sp.diag(P0, sp.Matrix([[p1]]))
            C = T0*P0*T0.T + p1*T1*T1.T
            PW = range_projection(C)
            k, r = sp.trace(P), sp.trace(PW)
            p, q = k/R, r/D
            assert P*P == P and PW*PW == PW
            assert sp.trace(C) == sp.trace(P*S)
            assert sp.trace(PW*Q)-sp.trace(C) >= 0
            assert (sp.trace(P*S)-M*p)**2 <= Vs*R*p*(1-p)
            assert (sp.trace(PW*Q)-M*q)**2 <= Vt*D*q*(1-q)
            count += 1
    return count


def obstruction_checks():
    kernel_models = 0
    for N in range(2, 13):
        T0 = sp.zeros(N, 2)
        T0[0, 1] = 1
        others = [sp.eye(N)[:, j] for j in range(1, N)]
        Q = T0*T0.T + sum((T*T.T for T in others), sp.zeros(N))
        S = sp.diag(T0.T*T0, *[T.T*T for T in others])
        R, M, U = N+1, sp.trace(Q), sp.trace(S*S)
        assert Q == sp.eye(N) and M == U == N
        assert hs2(S-sp.eye(R)) == 1
        assert 1-M*M/(R*U) == sp.Rational(1, N+1)
        Vs = hs2(S-M/R*sp.eye(R))
        a2 = R*Vs/(M*M)
        p = sp.Rational(1, N+1)
        assert a2 == sp.Rational(1, N)
        assert p*p == a2*p*(1-p)
        source_log_norms = [-N, 1] + [1]*(N-1)
        assert sum(source_log_norms) == 0
        assert -(-N) == N and -sum([1]*N) == -N
        kernel_models += 1

    T = sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5), 0],
                   [0, 0, 1],
                   [-sp.Rational(4, 5), sp.Rational(3, 5), 0]])
    assert T.T*T == T*T.T == sp.eye(3)
    A = T[:2, :]
    arithmetic = sp.Matrix([[1, 1, 0], [0, 0, 1]])
    Y = sp.diag(sp.Rational(3, 5), sp.Rational(4, 5), 1)
    assert A == arithmetic*Y
    assert all(A[:, j].rank() == 1 for j in range(3))
    assert A[:, :2].rank() == 1 and sp.Rational(2, 3) > sp.Rational(1, 2)
    assert 1+1-2 == 0 and -(F(-1)+F(2))/2 == F(-1, 2)

    cut_models = 0
    for D in range(2, 11):
        for n in range(1, D):
            delta, nu = F(D-n, D), F(n, D)
            for u in [F(0), F(1), F(7, 3)]:
                retained = -delta*u/nu
                mean_source = (n*retained+(D-n)*u)/D
                assert mean_source == 0
                assert -retained == delta*u/nu
                cut_models += 1
    return kernel_models, cut_models


def scalar_checks():
    t, Us, M, R = sp.symbols("t Us M R", positive=True)
    e = (t*t*Us-2*t*M+R)/R
    completed = Us/R*(t-M/Us)**2 + 1-M*M/(R*Us)
    assert sp.expand(e-completed) == 0
    u, H, delta, aI, bI = sp.symbols("u H delta aI bI", real=True)
    lower = -H+(H-delta*(u+H)-aI-bI)/(1-delta)
    wanted = -(delta*u+aI+bI)/(1-delta)
    assert sp.cancel(lower-wanted) == 0

    phi_models = 0
    for u0, H0 in itertools.product([F(0), F(1), F(3), F(10)], repeat=2):
        W = u0+H0
        phi2 = u0*H0 if u0 <= H0 else W*W/4
        for f in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]:
            x = u0*f
            assert 0 <= x <= W and x*(W-x) <= phi2
            phi_models += 1

    gap_models = 0
    for n in range(1, 9):
        for rtot in range(1, 10):
            for k, r in itertools.product(range(rtot+1), range(n+1)):
                difference = F(k, rtot)-F(r, n)
                if difference > 0:
                    assert difference >= F(1, n*rtot)
                    gap_models += 1
    return phi_models, gap_models


def main():
    sources = check_sources()
    matrix_cases = matrix_checks()
    kernels, cuts = obstruction_checks()
    phi, gaps = scalar_checks()
    cert = {
        "schema_version": 1,
        "status": "PASS: exact algebra, countermodels and selected pinned sources",
        "upstream": {"repository": "jsmorph/rh", "commit": REV},
        "note": NOTE, "note_sha256": sha((ROOT/NOTE).read_bytes()),
        "script": str(Path(__file__).relative_to(ROOT)),
        "script_sha256": sha(Path(__file__).read_bytes()),
        "source_files": sources,
        "checks": {
            "source_files": len(sources),
            "bounded_passages": sum(len(x["inspected_excerpts"]) for x in sources),
            "exact_centered_projection_cases": matrix_cases,
            "kernel_degree_countermodels": kernels,
            "perfect_frame_target_cut_countermodel": True,
            "sharp_centered_slope_cut_models": cuts,
            "phi_maximization_rational_cases": phi,
            "positive_integer_rank_gaps": gaps,
            "symbolic_optimal_scaling_and_target_cut_cancellation": True,
        },
        "independent_reviews": [
            {"reviewer": "/root/transport_defect", "status": "PASS",
             "scope": "Exact rank-expansion slope theorem; centered projections; actual-cut integer threshold; optimal normalization; full centered slope proof and sharp cut example. No source-rate or upstream proof audit."},
            {"reviewer": "/root/rh_source_symmetry", "status": "PASS",
             "scope": "Centered projection input, optimal common normalization, centered slope bound, truncated integrals, zero cases, target-cut cancellation and sharpness. Source-chain tracing remains separate."},
            {"reviewer": "/root/geometric_simplify", "status": "PASS",
             "scope": "Independent review of root's centered rank estimate, optimal common scalar and centered slope bound, including limits and sharpness. The separate determinant and short-image derivations are written proofs by this reviewer, not an independent review of themselves."},
        ],
        "proved_results": [
            "Exact proportional rank expansion yields a zero-penalty relative slope comparison.",
            "Centered rank comparison retains source and target variance around their actual trace masses.",
            "Optimal common comparison-matrix scaling minimizes the raw diagonal error.",
            "Centered slope bound costs [delta0*u+a*Phi(u,H)+sqrt(eta)*(H+u)/2]/(1-delta0).",
            "Stacked determinant and controlled integral image criteria identify missing arithmetic data.",
            "Exact frames do not give absolute degrees; small frame defects can hide unbounded kernel degrees.",
            "A perfect full frame can fail proportional expansion after a target cut.",
        ],
        "limits": [
            "No Lean compilation, kernel replay or full dependency audit.",
            "No proof that the source ranks and errors meet the integer-gap threshold.",
            "No identification of the final frame target with intermediate W10 cuspidal cores.",
            "No new uniform mean-volume, kernel-degree, short-generator or global theta estimate.",
            "Finite exact examples supplement the written universal proofs.",
        ],
    }
    (ROOT/OUT).write_text(json.dumps(cert, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "PASS", **cert["checks"], "certificate": OUT}))


if __name__ == "__main__":
    main()
