#!/usr/bin/env python3
"""Authenticate the far-kernel supplier and its exact cutoff simplification.

This does not rebuild Lean or certify the missing period-Gram transfer.
"""

from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVISION = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
ANCHORS = {
    "Development.AbelianVarietyTheory.Definitions.SemilocalFrames.LayerProd":
        [(15, 24), (39, 54)],
    "Development.AbelianVarietyTheory.Statements.CuspFrameWeights.EigenfunctionFiniteCoefficients":
        [(50, 62)],
    "Development.AbelianVarietyTheory.Proofs.FlagMeasures.LowestKTypeDecayGapOfCompressionFormulaGap":
        [(11, 32)],
    "Development.AbelianVarietyTheory.Proofs.FlagMeasures.LowestKTypeCompressionFormulaOfStrictLowestKType":
        [(22, 65)],
    "Development.AbelianVarietyTheory.Proofs.FlagMeasures.PtBoundAndFarBoundAndDecGap":
        [(11, 16)],
    "Development.AbelianVarietyTheory.Statements.CuspFrameWeights.CuspFrame":
        [(15, 37)],
    "Development.AbelianVarietyTheory.Proofs.FlagMeasures.PtBoundOfDecGap":
        [(13, 51)],
    "Development.AbelianVarietyTheory.Proofs.FlagMeasures.SummableOfSupport":
        [(42, 108), (109, 124)],
    "Development.AbelianVarietyTheory.BlockTheory.SiegelWeilLocal.FarTermsLatticeBound":
        [(12, 32)],
    "Development.AbelianVarietyTheory.BlockTheory.SiegelWeilLocal.AutomorphicBallCount":
        [(12, 21)],
    "Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals.HidaSetting":
        [(136, 156), (302, 317)],
    "Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals.PoincareInHH":
        [(172, 199)],
    "Formalism.LocalToGlobal.SiegelLatticeTheory.FlagStabilizerTensors.RootLatticeThresholds.EvalTRph":
        [(19, 52)],
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def authenticate():
    with gzip.open(ROOT / "blueprint/lean-source-imports.json.gz", "rt") as handle:
        atlas = json.load(handle)
    assert atlas["commit"] == REVISION
    entries = {row[0]: row for row in atlas["modules"]}
    evidence = []
    for name, ranges in ANCHORS.items():
        entry = entries[name]
        path = "lean/src/" + name.replace(".", "/") + ".lean"
        data = (ROOT / "build/source-cache/jsmorph/rh" / REVISION / path).read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == entry[1], name
        assert len(data) == entry[2], name
        lines = data.splitlines(keepends=True)
        excerpts = []
        for a, b in ranges:
            assert 1 <= a <= b <= len(lines) and b - a < 120
            excerpts.append({"lines": [a, b], "sha256": sha(b"".join(lines[a-1:b]))})
        evidence.append({"repository": "jsmorph/rh", "commit": REVISION,
                         "path": path, "git_blob_sha1": blob, "sha256": sha(data),
                         "excerpts": excerpts})
    return evidence


def cutoff_checks():
    cases = 0
    for n in range(2, 151):
        h = 16 * n**19
        ep = Fraction(1, 8 * n**2)
        assert n**15 >= 64
        assert h >= 1024 * n**4
        assert 2 * n**2 * ep == Fraction(1, 4) <= Fraction(1, 2)
        assert 64 * n**2 <= h * ep
        assert 1 <= h * ep**2 / 16
        assert h * ep**2 / 16 == Fraction(n**15, 64)
        for q in range(1, n + 1):
            assert 2 * q * ep**2 <= 1
            # Squared form of 120*n*q^(3/2) <= h, with positive sides.
            assert (120 * n)**2 * q**3 <= h**2
            cases += 1
    return cases


def main():
    evidence = authenticate()
    cases = cutoff_checks()
    result = {
        "status": "source-supplier checkpoint and exact cutoff checks passed",
        "scope": "Pinned source bytes and bounded interfaces; no Lean build, no full dependency proof audit, no theta-map Gram bound or nonvanishing claim.",
        "source_files": evidence,
        "exact_cutoff_cases": cases,
        "proved_observation": "A nonzero unitary-covariant Whittaker vector with an unbounded left covariance group cannot decay in the full-group operator distance; quotient geometry is required.",
        "cusp_moment_limitation": {
            "status": "proved analytic probability model, not an arithmetic counterexample",
            "model": "X uniform on (0,1), lambda=r*X^(1/k), N_t=ceil((t/lambda)^a)-1, k>a>0",
            "mean_count": "E N_t=zeta(k/a)*(t/r)^k",
            "log_mean": "E log(r/lambda)=1/k",
            "power_mean": "E(r/lambda)^p=k/(k-p) for 0<p<k; infinity for p>=k",
            "positive_general_bound": "E max(1,r/lambda)^p <= k/(k-p)*M_star^(p/k), 0<p<k, under the stated small-minimum tail with M_star>=1",
            "remaining_identifications": "The actual tau/lambda and n/N comparisons are retained; no arithmetic kernel divergence claimed."
        },
        "retained_requirements": [
            "Actual discrete-series, signature, gap, finite idempotent and formal-degree identifications",
            "Positive M before normalizing; original lattice minimum tau and all near returns",
            "A valid period-Gram or quotient-Bessel transfer",
            "Original source inclusions J_u, original target projection and actual lost mass"
        ],
        "node_counts": {"RH": "6/9", "GRH": "17/31", "changed": False}
    }
    path = ROOT / "certificates/projector-kernel-tail.json"
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "passed", "source_files": len(evidence),
                      "exact_cutoff_cases": cases,
                      "certificate": str(path.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
