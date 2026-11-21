#!/usr/bin/env python3
"""Check the direct geometric degree reductions, not the deep input theorems.

Only cached pinned sources are read. Populate missing files using
scripts/source_excerpt.py --atlas. No complete source is printed.
Finite logarithmic checks use exact rational enclosing intervals.
"""

from fractions import Fraction as F
from functools import lru_cache
import gzip
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REVISION = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPOSITORY = "jsmorph/rh"
NOTE = "notes/geometric-degree-frontier.md"
OUT = "certificates/geometric-degree-frontier.json"
PREFIX = "Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts."
DIV = "Development.AbelianVarietyTheory.Proofs.DivisorProofs."
SOURCES = [
    (PREFIX + "HodgeBundleWeights.HeightAddLogNonneg",
     "3dff82e5e34f65ff304d29b0c1ca692d6a76942063c0f76b07813cf5a2da6a09",
     [[18, 28], [29, 65], [66, 105]]),
    (DIV + "ComponentImageDegreeBetweenOfProportionality",
     "1a46a7b6241bdf31ded295acf0822a8e490ab3f06c521651824c61a2ea733f37",
     [[15, 26]]),
    (PREFIX + "HodgeBundleWeights.CompactificationTopChernEqVolume",
     "1e2f08709fc28040e9dad2d4c45921d99c67e92a3c9c044d946ec990aec7b421",
     [[19, 35]]),
    (PREFIX + "ThirdPlaceSeries.CoveringDegreeMultiplicative",
     "9de93cf7b89c05b91c6b6a7320c9369b5d915b566080c52e2ebff20fd3d0b0e8",
     [[25, 55]]),
    (PREFIX + "ThirdPlaceSeries.ShortVectorWeightBound",
     "4fa39ba348157012a76a537baafaf61b262bf46f7cfc4df35f6848158947fd2b",
     [[23, 47]]),
    ("Development.AbelianVarietyTheory.Definitions.Foundations.IsProbabilityMeasureMuPart",
     "3951bad4542aa62738d56c1f31d93348ca8578bffc940aaafba74e395973645d",
     [[20, 50], [149, 164], [787, 826]]),
    ("Development.AbelianVarietyTheory.Definitions.Divisors.NormNegCmConstantEqAtAllEmbeddings",
     "d07c8d791d45bd5f9a8b4e9fd99192dd1a0b8fc61c0471e06c98fc5f96da98c1",
     [[250, 267]]),
    ("Formalism.HarderNarasimhan.StatementPl",
     "16766730a8dd781538ca5035ff73ddf7612decae9f293bbd995679093d9adc39",
     [[27, 42], [64, 71]]),
    ("Formalism.LocalToGlobal.IndefiniteForms.IndefiniteTree.RealCubicMeans.LogMeanShares.LogMeanStatements.HSClaim",
     "764e30159e21ec507075f04acd0c24e680bcb7e17ede5cfafedeb77657661c9b",
     [[7, 22]]),
    (PREFIX + "ThirdPlaceSeries.ExistsDegreeParametersBound",
     "8b74e19ec6b9fc30604c6cc6fe86c18cfc3a4583ead3fc2b56ed1d0228af5949",
     [[34, 43]]),
    (PREFIX + "ThirdPlaceSeries.SizesOfCoverStatement",
     "f57fd315cc5fa2dfed0d48f275221c6aded22719ca2ef88758ebc91c0d0f6310",
     [[19, 20]]),
    (DIV + "DegBoundOfClaimNumbers",
     "f75edbc033237ad2ce2112681011dda4092ceff7ab0680c47852fb387d19e4b6",
     [[9, 28]]),
    (DIV + "HilbertSamuelALogALe",
     "e2df2b438a98154312cc666f520a68fb129c4d24580dc997b76ce10763eb0dcb",
     [[5, 15]]),
    (PREFIX + "ThirdPlaceSeries.HilbertSamuelLowerBoundOfComponents",
     "8f952800c424367f1c8961e71b610a9cf0ac39e9f6b9958b7591199e48ddfdee",
     [[48, 54], [89, 113]]),
    ("Development.AbelianVarietyTheory.Definitions.Divisors.CovolXOfCovol",
     "f40c762ed8c2b18311d604540c15613e4a5969b1395dcab59b2854584fb6d3ae",
     [[42, 47], [140, 159]]),
    ("Development.AbelianVarietyTheory.Definitions.Divisors.SemiposAtOfPositive",
     "7fc2c91a3f3d0bc130bb65b092eb1761feb10701036ee8dff304e5ee91e1cb2e",
     [[88, 105]]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def verified_sources():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == REPOSITORY and atlas["commit"] == REVISION
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, expected_sha, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        paths = [ROOT / "build/source-cache" / REPOSITORY / REVISION / rel,
                 ROOT / "build/lean-mirror" / rel]
        local = next((p for p in paths if p.is_file()), None)
        if local is None:
            raise FileNotFoundError("Populate pinned cache for " + module)
        data = local.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == blobs[module] and sha(data) == expected_sha
        lines = data.splitlines()
        excerpts = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines) and end - start < 120
            passage = b"\n".join(lines[start - 1:end]) + b"\n"
            excerpts.append({"lines": [start, end], "sha256": sha(passage)})
        records.append({
            "module": module, "path": rel, "git_blob_sha1": blob,
            "sha256": expected_sha, "bytes": len(data), "line_count": len(lines),
            "inspected_excerpts": excerpts,
        })
    return records


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def scale(q, x):
    values = (q * x[0], q * x[1])
    return min(values), max(values)


def scalar(q):
    return F(q), F(q)


def atanh_log_interval(x, terms=20):
    """For 1<=x<=2, enclose log(x) by an exact positive series and tail."""
    assert F(1) <= x <= F(2)
    z = (x - 1) / (x + 1)
    partial = 2 * sum((z ** (2 * k + 1) / (2 * k + 1)
                       for k in range(terms)), F(0))
    tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return partial, partial + tail


@lru_cache(maxsize=None)
def log_interval(x):
    """Certified rational interval; no floating-point logarithms."""
    x = F(x)
    assert x > 0
    exponent = 0
    while x > 2:
        x /= 2
        exponent += 1
    while x < 1:
        x *= 2
        exponent -= 1
    return add(atanh_log_interval(x), scale(F(exponent), atanh_log_interval(F(2))))


def hs_interval(t, a, A, b, R0, h):
    return add(scalar(t * h - a * abs(h) - R0),
               scale(-A, log_interval(b + abs(h))))


def max_lower_interval(x, y):
    return max(x[0], y[0]), max(x[1], y[1])


def exact_pointwise_checks():
    count = 0
    parameters = itertools.product(
        [F(0), F(3)], [F(1), F(4)], [F(1), F(5)],
        [F(0), F(7)], [F(-11), F(0), F(13)],
        [F(1, 2), F(3)], [F(1), F(2)],
        [F(-50), F(-3, 2), F(0), F(3, 2), F(50)],
        [F(0), F(1, 2)])
    for a, gap, ratio, L, R0, A, b0, h, fraction in parameters:
        t = a + gap
        lam = fraction * gap
        s = t - a - lam
        beta = t + a
        P = max(ratio * L - R0, F(0))
        K = max(b0, A / s)
        lhs = max_lower_interval(scalar(-ratio * L),
                                 hs_interval(t, a, A, b0, R0, h))
        rhs = add(scalar(lam * h - R0 - (1 - lam / beta) * P),
                  scale(-A, log_interval(K + P / beta)))
        assert lhs[0] >= rhs[1], (a, t, ratio, L, R0, A, b0, h, lam)
        count += 1
    return count


def exact_aggregate_checks():
    count = 0
    for a, gap, L, A, R0, h1, h2 in itertools.product(
            [F(0), F(6)], [F(1), F(5)], [F(0), F(17)],
            [F(1, 2), F(3), F(676)], [F(0), F(4)],
            [F(-40), F(0), F(12)], [F(-7), F(0), F(40)]):
        t = a + gap
        lam = gap - 1
        weights, ranks, heights = [F(1), F(2)], [F(2), F(5)], [h1, h2]
        W, Rt = sum(weights), sum(ranks)
        theta = W / Rt
        M = sum(w * h for w, h in zip(weights, heights)) / W
        H = max(F(0), -M)
        actual_sum = scalar(0)
        for w, r, h in zip(weights, ranks, heights):
            d = max_lower_interval(scalar(-r * L),
                                   scale(w, hs_interval(t, a, A, F(2), R0, h)))
            actual_sum = add(actual_sum, d)
        lhs = scale(1 / Rt, actual_sum)
        rhs = scalar(-lam * theta * H - theta * R0
                     - (2 * a + 2) * L / (t + a))
        rhs = add(rhs, scale(-theta * A, log_interval(max(A, F(1)))))
        if A < 2:
            rhs = add(rhs, scale(F(-2), log_interval(F(2))))
        assert lhs[0] >= rhs[1], (a, t, L, A, R0, h1, h2)
        count += 1
    return count


def symbolic_checks():
    t, a, lam, P, y = sp.symbols("t a lam P y", real=True)
    beta = t + a
    assert sp.cancel((-beta*y) - (-lam*y - (1-lam/beta)*P)
                     - (beta-lam)*(P/beta-y)) == 0
    assert sp.cancel((-P) - (-lam*y-(1-lam/beta)*P)
                     - lam*(y-P/beta)) == 0
    assert sp.simplify((1 - (t-a-1)/(t+a)) + 1/(t+a)
                       - (2*a+2)/(t+a)) == 0
    D = sp.symbols("D", real=True)
    assert sp.expand(14*D**2 - 6*D - 8 - (D-1)*(14*D+8)) == 0

    C, alpha, J, h, habs, logLambda, logN, logB, logt, logbeta, g, log2, lD, lT = (
        sp.symbols("C alpha J h habs logLambda logN logB logt logbeta g log2 lD lT",
                   real=True))
    ell = logLambda + C * (logN + logB)
    raw = (t*h - 3*(D+1)*habs - J - C*D**2*(ell+logt)
           - (t+D+1)*logbeta - (t+D**2)*(g+2)
           - alpha*(t*(log2+ell+logbeta/2)+lD+lT))
    V = C*D**2+t*alpha
    A = C*V
    R0 = (J+C*D**2*logt+(t+D+1)*logbeta+(t+D**2)*(g+2)
          +V*(logLambda+C*logN)+alpha*(t*(log2+logbeta/2)+lD+lT))
    assert sp.expand(raw - (t*h-3*(D+1)*habs-A*logB-R0)) == 0

    # Countermodel: the signed lower-bound gap is manifestly positive at t>=15.
    L = sp.symbols("L", positive=True)
    w = t-1
    ell0 = 26*sp.log(2)
    core = 26*(ell0+sp.log(t))+4*(t+1)
    surplus = 27*t*sp.log(2)+2*L
    raw_lower = -w*(core+surplus)
    degree = -2*w*L
    gap = w*((676+27*t)*sp.log(2)+26*sp.log(t)+4*(t+1))
    assert sp.expand(degree-raw_lower-gap) == 0
    assert sp.simplify((1-7/t)*2*w-w-w*(1-14/t)) == 0

    # Equal top degrees remove the weight conversion exactly.
    q, sbar, c, gamma, W, NN, B, delta = sp.symbols(
        "q sbar c gamma W NN B delta", real=True)
    collected = (B*delta*NN*(sbar+c)-W*(c+gamma))/W
    assert sp.simplify(collected.subs(B*delta*NN, q*W)
                       - (q*sbar-(1-q)*c-gamma)) == 0
    return 8


def exact_volume_models():
    count = 0
    for rho, c, gamma, s1, s2 in itertools.product(
            [F(0), F(1, 4), F(3, 4)], [F(0), F(2)],
            [F(0), F(1, 3)], [F(-7), F(0), F(5)], [F(-1), F(0), F(9)]):
        delta_star = F(3)
        deltas = [delta_star, delta_star/(1-rho)]
        weights = [2*d for d in deltas]
        heights = [delta_star*(s+c)/d-c-gamma
                   for s, d in zip([s1, s2], deltas)]
        W = sum(weights)
        q = 2*2*delta_star/W
        M = sum(w*h for w, h in zip(weights, heights))/W
        sbar = (s1+s2)/2
        assert 1-rho <= q <= 1
        assert M == q*sbar-(1-q)*c-gamma
        X = max(F(0), -sbar)
        Hq = q*X+(1-q)*c+gamma
        assert M >= -Hq and Hq <= X+rho*c+gamma
        count += 1
    return count


def main():
    sources = verified_sources()
    symbolic = symbolic_checks()
    volumes = exact_volume_models()
    pointwise = exact_pointwise_checks()
    aggregate = exact_aggregate_checks()
    cert = {
        "schema_version": 1,
        "status": "PASS: pinned-source and exact algebra/interval checks",
        "upstream": {"repository": REPOSITORY, "commit": REVISION},
        "note": NOTE,
        "note_sha256": sha((ROOT / NOTE).read_bytes()),
        "script": str(Path(__file__).relative_to(ROOT)),
        "script_sha256": sha(Path(__file__).read_bytes()),
        "source_files": sources,
        "checks": {
            "source_files": len(sources),
            "bounded_passages": sum(len(s["inspected_excerpts"]) for s in sources),
            "symbolic_identities": symbolic,
            "exact_equal_volume_models": volumes,
            "certified_rational_log_pointwise_cases": pointwise,
            "certified_rational_log_aggregate_cases": aggregate,
            "logarithm_method": "atanh series with exact rational geometric-tail enclosure",
            "raw_surplus_countermodel": "symbolic strict gap for t>=15 and L>0",
        },
        "proved_results": [
            "Exact top-degree cancellation supplies the Hilbert-Samuel-weighted mean.",
            "A same-lattice short-section degree floor removes the separate negative-height moment.",
            "The added floor cost is at most 2*b0 at the source scalar scales.",
            "Raw Hilbert-Samuel plus the degree floor gives a signed height-free surplus expression.",
            "Raw scalar contracts without rank/surplus control admit an unbounded normalized loss.",
        ],
        "independent_reviews": [
            {
                "reviewer": "/root",
                "status": "PASS of Sections 1-2 and the Section 3 proof mechanism",
                "scope": "Ordinary algebra, signs, rank weights, Jensen, constants and source-scale absorption; requested separate source normalization and raw substitution audit.",
            },
            {
                "reviewer": "/root/rh_source_symmetry",
                "status": "PASS of Sections 1-3, including the bounded source bridge",
                "scope": "Exact degree cancellation, one-mean theorem and zero cases, same Cusp/latOn short vectors at the final weight, arithmetic-degree normalization, untwisted numerical Hilbert-Samuel substitution, 10002*b0, positive ranks, flat twist, and raw signed-cost collection. No upstream proof or kernel audit.",
            },
        ],
        "limits": [
            "No Lean build, kernel replay or full dependency audit.",
            "The actual mean-volume and quantitative Hilbert-Samuel construction remain inputs.",
            "The 10002*b0 supplier retains the original upper rank-share input.",
            "The raw height-free variant needs a new bound for its explicit rank-dependent cost.",
            "Finite interval cases supplement the written proofs; they are not universal proofs.",
            "No integrated geometric supplier or completion-time estimate is claimed.",
        ],
    }
    (ROOT / OUT).write_text(json.dumps(cert, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "PASS", **cert["checks"], "certificate": OUT},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
