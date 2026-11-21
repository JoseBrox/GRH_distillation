#!/usr/bin/env python3
"""Exact algebra and pinned source-byte checks for the tower reduction.

This does not verify upstream geometry or run a Lean kernel.
Populate a missing pinned cache entry with scripts/source_excerpt.py --atlas.
"""

from fractions import Fraction as F
import gzip
import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NOTE = "notes/tower-intersection-reduction.md"
OUT = "certificates/tower-intersection-reduction.json"
AS = "Development.AutomorphicSpectrum."
AV = "Development.AbelianVarietyTheory."
TP = "Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts."
SOURCES = [
    (AS + "Definitions.DivisibilityTowers.CompactGapsGE",
     "f0b3cc3288c790783c6fad76f990b07dfd3cfc0ffa03c68ed08f6353b57fda2a",
     [[19, 46], [73, 81]]),
    (AS + "Definitions.DivisibilityTowers.HeckeSectionsIsotropicCommutatorPairingPower",
     "85cedea0294499d45b9fb5e3fa3cf151a72d69fe2e8d08ee920719e5d02a33ac",
     [[30, 42], [57, 74], [84, 93]]),
    (AS + "Definitions.DivisibilityTowers.Proportional",
     "346bea775b0a21f67b2f05719c3b3c68481c64e06a1225f094c08815be3aa0d4",
     [[114, 137]]),
    (AS + "Proofs.DivisibilityProofs.TowerT2",
     "b67fe4341820c7b4b4688292740789e05830562b1bd4ebea8166cb2add0264bc",
     [[69, 72], [98, 108], [118, 164]]),
    (AS + "Proofs.DivisibilityProofs.FlagShiftTotalLinRootPower",
     "26b7912c4c76dc2846236b92f586bc38c5ceca55ab263c9858782b4b9b860942",
     [[15, 23]]),
    (AS + "Proofs.DivisibilityProofs.TestPolynomialShiftTotal",
     "85bd2ecdb0707781ff39298280a1aac98946f0f975e66f628ed51868dcd2156e",
     [[13, 14]]),
    (AS + "Proofs.DivisibilityProofs.TestPolynomialRemainderBound",
     "6324f279e17f7de18bf88537d9fcaa423a19d4c19fbd555a4bd82a2f272824a4",
     [[417, 442]]),
    (AS + "Proofs.DivisibilityProofs.TestHeightBound",
     "786f130d0af2fdf7436284fcc94b8285f535665e72dc1791f87260e60f1f8f57",
     [[17, 41], [80, 110]]),
    (AS + "Proofs.DivisibilityProofs.FlagHeightTestBound",
     "d0df79cd4d4a23870774f7b45c178a7e77cf141aaeb5a7341ff3525e74f8eef4",
     [[344, 372]]),
    (AS + "Proofs.DivisibilityProofs.LinRootRemainderBound",
     "27b667324f69e862d07042dcb0685cc5b370e572a7f487289a60e3d5bf434690",
     [[15, 16]]),
    (AS + "Proofs.DivisibilityProofs.CutoffCoefficientsBound",
     "99903c96c1997de8813c897f6146f57f84de4a514a871f7412d29025c9cf0860",
     [[37, 80]]),
    (AS + "Proofs.GeometryProofs.PropFTopHolds",
     "73da1d9fea7f4adc95dd51dc3e3dd75b6cc990afb7f14a0903286a8dedbed00f",
     [[13, 46], [47, 97]]),
    (AS + "Statements.GeometryStatements.PropFTop",
     "21f1ca96c78c495b62966e0c191d632b9a62a046f8377eb5b4dc98bf99942e3a",
     [[10, 15]]),
    (AS + "Proofs.DivisibilityProofs.SlopeLowerBaseSettings",
     "91b2a7711038280953fd65a2abd70a670bbdd6612a2d13cd61b94c8e31accf2e",
     [[16, 24], [39, 74], [76, 118]]),
    (AS + "Proofs.DivisibilityProofs.TowerWeilInputsCombined",
     "a19e8370d09e027bef3ddc933d2e3ad9561c42b706cd36e7d16498054e41d25a",
     [[22, 29], [35, 53]]),
    (AS + "Proofs.DivisibilityProofs.VolumeTheoremOfInputs",
     "09db5866be363a45ac474678ec8d3ee73c25d643bfdf20a609a782218f696706",
     [[72, 121]]),
    (AS + "Statements.TowerExistence.GoodTowerExistsX",
     "778f974a5479f60d2e31cb368454f05a1d76407d07bda93b6055443b47031f99",
     [[28, 36]]),
    (AV + "Definitions.Divisors.BarCompSubsetClosure",
     "d459dee0ab36f33cfc7778c516e00dd564fb2a3a48008fa9dd92fa1805a1e71a",
     [[39, 57], [86, 114], [124, 148]]),
    (AV + "Definitions.Divisors.IsHomogeneousCompIdeal",
     "869c29522255ffbe00e08da3fd346a808e7b1dfc2dddbb9718869517d8df5102",
     [[109, 116]]),
    (AV + "Definitions.Divisors.NormNegCmConstantEqAtAllEmbeddings",
     "d07c8d791d45bd5f9a8b4e9fd99192dd1a0b8fc61c0471e06c98fc5f96da98c1",
     [[59, 76], [292, 295]]),
    (AV + "Definitions.Divisors.CovolXOfCovol",
     "f40c762ed8c2b18311d604540c15613e4a5969b1395dcab59b2854584fb6d3ae",
     [[26, 49], [133, 159]]),
    (AV + "Definitions.Foundations.IsProbabilityMeasureMuPart",
     "3951bad4542aa62738d56c1f31d93348ca8578bffc940aaafba74e395973645d",
     [[174, 197], [235, 236]]),
    (AV + "Definitions.Foundations.ExistsFlatSecRankZero",
     "dec3647f1e33f03c8a814b7d8f41a6c093d3fb22eb4ff11353ecd8754cd5f468",
     [[730, 754], [783, 790]]),
    (TP + "ThirdPlaceSeries.WeightsAtPoint",
     "47988690dd9d4347811bf04be0d24f01da3cfe79cef617fef38a9562fc5c24f1",
     [[27, 27]]),
    (AV + "Proofs.DivisorProofs.AnchoredWeightIndefiniteLiftGaps",
     "55a620ae5058ec75cbfd3bf0b44c748e8c160155a05346597837dc74b9a31000",
     [[102, 106], [135, 136]]),
    (TP + "HodgeBundleWeights.HeightAddLogNonneg",
     "3dff82e5e34f65ff304d29b0c1ca692d6a76942063c0f76b07813cf5a2da6a09",
     [[44, 65], [66, 105]]),
    (TP + "HodgeBundleWeights.TwistedBundleDegreeLowerBound",
     "b7ea44293582c5bbc9512ad941daa2e1a1aff6141a6344fc2584023903ed4cc0",
     [[19, 44]]),
    (TP + "ThirdPlaceSeries.HeightOfSteps",
     "204e2b46811828454a1f517799425f9af798c465f106e803e9338136f260b253",
     [[19, 38]]),
    (AV + "Proofs.DivisorProofs.LowerBoundOfAllEstimates",
     "111bbcfa0022d90c5aebb3d52247857c8f10ff9269cc369f5d2eaae8a76637d9",
     [[65, 105]]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def check_sources():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, expected, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        candidates = [ROOT / "build/source-cache/jsmorph/rh" / REV / rel,
                      ROOT / "build/lean-mirror" / rel]
        local = next((p for p in candidates if p.is_file()), None)
        if local is None:
            raise FileNotFoundError("Populate the pinned cache for " + module)
        data = local.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == blobs[module] and sha(data) == expected, module
        lines = data.splitlines()
        excerpts = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines) and end - start < 120, module
            passage = b"\n".join(lines[start-1:end]) + b"\n"
            excerpts.append({"lines": [start, end], "sha256": sha(passage)})
        records.append({"module": module, "path": rel, "git_blob_sha1": blob,
                        "sha256": expected, "line_count": len(lines), "bytes": len(data),
                        "inspected_excerpts": excerpts})
    return records


def sign(perm):
    return (-1) ** sum(perm[i] > perm[j] for i in range(len(perm))
                      for j in range(i+1, len(perm)))


def weight_statistics(u, p):
    N = len(u[0])
    q = N-p
    S = sum(sum(row[:p]) for row in u)
    T = sum(map(sum, u))
    C = F(S) - F(p, N)*T
    W = sum(row[0]-row[-1] for row in u)
    L = sum(abs(x) for row in u for x in row)
    cross = sum(row[a]-row[b] for row in u
                for a in range(p) for b in range(p, N))
    assert C == F(cross, N) and 0 <= C <= F(p*q, N)*W
    assert C <= F(p, N)*L
    return S, T, C, W, L


def statistic_checks():
    count = 0
    for N in range(2, 9):
        for p in range((N+1)//2, N):
            for f in range(1, 4):
                for seed in range(1, 13):
                    u = [sorted([F((seed*(j+3)+t*t+7*j*j)%37-18, 3)
                                 for j in range(N)], reverse=True) for t in range(f)]
                    S, T, C, W, L = weight_statistics(u, p)
                    shifted = [[x+F(t-2*seed, 5) for x in row]
                               for t, row in enumerate(u)]
                    S1, T1, C1, W1, _ = weight_statistics(shifted, p)
                    assert C1 == C and W1 == W
                    assert T1-T == N*sum(F(t-2*seed, 5) for t in range(f))
                    Z, flat = F(seed, 7), F(seed+1, 11)
                    K = max(Z, F(N-p, p)*Z+F(N, p)*flat)
                    assert F(N, p)*(C*Z+flat*abs(S)) <= K*L
                    count += 1
    return count


def degree_alternating(u):
    N, f = len(u[0]), len(u)
    d = f*N*(N-1)//2
    total = F(0)
    for perms in itertools.product(itertools.permutations(range(N)), repeat=f):
        exps = [[N-1-perm[j] for j in range(N)] for perm in perms]
        denominator = math.prod(math.factorial(k) for row in exps for k in row)
        coeff = F(math.factorial(d), denominator)
        coeff *= math.prod((-u[t][j])**exps[t][j] for t in range(f) for j in range(N))
        total += (-1)**d * math.prod(sign(perm) for perm in perms)*coeff
    return total


def degree_product(u):
    N, f = len(u[0]), len(u)
    d = f*N*(N-1)//2
    return F(math.factorial(d), math.prod(math.factorial(i) for i in range(N))**f) * math.prod(
        row[a]-row[b] for row in u for a in range(N) for b in range(a+1, N))


def degree_checks():
    count = 0
    for N, f in [(2, 1), (3, 1), (4, 1), (5, 1), (2, 2), (3, 2), (4, 2)]:
        for seed in range(1, 5):
            u = [[F((N-j)*(seed+t+j+N), 3) for j in range(N)] for t in range(f)]
            assert all(row[j] > row[j+1] for row in u for j in range(N-1))
            D = degree_alternating(u)
            assert D == degree_product(u) > 0
            shifted = [[x+F(t-seed, 2) for x in row] for t, row in enumerate(u)]
            assert degree_alternating(shifted) == D
            count += 1
    return count


def flag_degree(poly, variables, N, f):
    coeff = sp.Poly(sp.expand(poly), *variables)
    d = f*N*(N-1)//2
    out = 0
    for perms in itertools.product(itertools.permutations(range(N)), repeat=f):
        exps = tuple(N-1-perms[t][j] for t in range(f) for j in range(N))
        out += math.prod(sign(perm) for perm in perms)*coeff.coeff_monomial(exps)
    return (-1)**d*out


def test_polynomial_checks():
    count = 0
    for N, p, f in [(2, 1, 1), (3, 2, 1), (4, 2, 1), (4, 3, 1),
                    (2, 1, 2), (3, 2, 2)]:
        q, d0 = N-p, f*p*(N-p)
        variables = sp.symbols("x0:"+str(N*f))
        rows = [variables[t*N:(t+1)*N] for t in range(f)]
        mu = sum(row[j] for row in rows for j in range(p, N))
        V = sp.prod(row[b]-row[a] for row in rows
                    for a in range(N) for b in range(a+1, N)
                    if (a < p) == (b < p))
        F0 = sp.expand(mu**(d0+1)*V)
        assert sp.Poly(F0, *variables).total_degree() == f*N*(N-1)//2+1
        J = flag_degree(mu**d0*V, variables, N, f)
        assert J > 0
        for row in rows:
            Sh = sum(sp.diff(F0, x) for x in row[:p])
            Tot = sum(sp.diff(F0, x) for x in row)
            assert sp.expand(Sh) == 0
            assert flag_degree(Tot, variables, N, f) == q*(d0+1)*J
        count += 1
    return count


def scalar_checks():
    A, b, p, N, S, T, hu, h0, ru, r0 = sp.symbols(
        "A b p N S T hu h0 ru r0", nonzero=True)
    C, c, beta = S-p*T/N, (p*A+N*b)/N, h0-b+r0
    lhs = hu+A*C+c*T+ru
    rhs = hu+N/p*(C*(beta-h0-r0)+c*S)+ru
    assert sp.factor(lhs-rhs) == 0
    z = sp.symbols("z")
    assert sp.factor(lhs.subs({S:S+p*z, T:T+N*z}, simultaneous=True)-lhs-N*c*z) == 0
    size = sp.symbols("size", positive=True)
    specialization = {A:-size, b:p*size/N, hu:0, h0:0, ru:0, r0:0}
    assert sp.factor(lhs.subs(specialization, simultaneous=True)+size*C) == 0
    assert sp.factor(beta.subs(specialization, simultaneous=True)+p*size/N) == 0
    assert c.subs(specialization, simultaneous=True) == 0
    growth = []
    for q in range(1, 100):
        for extra in range(1, 5):
            p0, N0 = 2*q+extra, 3*q+extra
            assert F(N0, p0) < F(3, 2)
            growth.append((N0, p0))
    return {"symbolic_two_polynomial_identity": True,
            "symbolic_determinant_translation": True,
            "symbolic_base_input_countermodel": True,
            "source_rank_ratio_cases": len(growth)}


def anchored_weight_checks():
    count = 0
    for N in range(2, 11):
        for p in range((N+1)//2, N):
            for anchor in range(N):
                for seed in range(1, 5):
                    gaps = [((r+1)*seed)%11-4 for r in range(N-1)]
                    u1 = [sum(gaps[:anchor])-sum(gaps[:i]) for i in range(N)]
                    up = [u1[i]+(3*N if i >= p else 0) for i in range(N)]
                    total = sum((r+1)*gaps[r] for r in range(anchor)) - sum(
                        (N-1-r)*gaps[r] for r in range(anchor, N-1)) + 3*N*(N-p)
                    assert u1[anchor] == 0 and sum(up) == total
                    contrast = lambda u: F(sum(u[:p]))-F(p, N)*sum(u)
                    assert contrast(up) == contrast(u1)-3*p*(N-p)
                    count += 1
    N, p, anchor = 14, 12, 10
    u1 = [56*(anchor-i) for i in range(N)]
    up = [u1[i]+(3*N if i >= p else 0) for i in range(N)]
    assert sum(up) == 2828 and all(up[i] > up[i+1] for i in range(N-1))
    original = [F(10), F(9), F(-10)]
    centered = [x-sum(original)/3 for x in original]
    assert max(map(abs, centered)) == 13 > max(map(abs, original))
    return {"finite_cases": count,
            "strict_anchored_countermodel": {"N":N,"p":p,"q":N-p,"anchor":anchor,
                                           "gaps":56,"total_per_embedding":sum(up)},
            "mean_centering_increases_max_norm": True}


def main():
    sources = check_sources()
    results = {
        "weight_statistic_cases": statistic_checks(),
        "flag_degree_vandermonde_cases": degree_checks(),
        "test_polynomial_cases": test_polynomial_checks(),
        "scalar_identities": scalar_checks(),
        "anchored_weights": anchored_weight_checks(),
    }
    cert = {
        "status": "PASS",
        "repository": "jsmorph/rh", "commit": REV,
        "note": NOTE, "note_sha256": sha((ROOT/NOTE).read_bytes()),
        "script": str(Path(__file__).relative_to(ROOT)),
        "script_sha256": sha(Path(__file__).read_bytes()),
        "source_verification": {
            "files": len(sources),
            "bounded_passages": sum(len(r["inspected_excerpts"]) for r in sources),
            "records": sources,
        },
        "exact_checks": results,
        "mathematical_scope": [
            "Exact two-polynomial scalar elimination with the same intersection functional.",
            "Contrast and signed determinant weight retained with N/p and f*q factors.",
            "Flat translation identity conditional on the stated same-metric flat-direction contract.",
            "Anchored weights are not forced to have total zero.",
            "Base-test lower bound remains an explicit unproved geometric supplier.",
        ],
        "not_verified": [
            "No Lean build or kernel verification.",
            "No independent proof of the growing-family tower or metric geometry.",
            "No numerical lower bound for the actual selected Grassmannian test intersection.",
            "No cancellation of the cutoff determinant term with later flat section twists.",
            "No actual automorphic counterexample to the geometric theorem.",
        ],
        "independent_review": {
            "status": "PASS",
            "reviews": [
                {"reviewer": "rh_source_symmetry",
                 "scope": "Note Sections 1-5 mathematics; decisive source contracts; independently recomputed all 29 file hashes and all 47 excerpt hashes.",
                 "limitations": "No upstream geometry proof audit or Lean replay."},
                {"reviewer": "root",
                 "scope": "Note Sections 1-5 and the complete standard-mathematics TeX insertion: signs, normalized degree, exact scalar elimination, determinant translation and selected anchored sums.",
                 "limitations": "No claim here about an audit of the remaining geometric suppliers."},
            ],
        },
    }
    (ROOT/OUT).write_text(json.dumps(cert, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status":"PASS","source_files":len(sources),
                      "bounded_passages":cert["source_verification"]["bounded_passages"],
                      "exact_checks":results,"certificate":OUT}, ensure_ascii=False))


if __name__ == "__main__":
    main()
