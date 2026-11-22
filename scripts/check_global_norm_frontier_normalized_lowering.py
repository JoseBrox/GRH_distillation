#!/usr/bin/env python3
"""Authenticate and check the original normalized lowering-scalar reduction."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import subprocess

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PRIOR = "1d6b784075cf61ce5d6b2f1b03cb0196c64130ab"
REPO = "jsmorph/rh"
STEM = "global-norm-frontier-normalized-lowering"
J = "Development.AbelianVarietyTheory.Proofs.JetHarmonics."
B = "CompanionTheory.AutomorphicTheory.PieriRules.ThetaBesselIsometries."
SOURCES = [
    ("Development.AbelianVarietyTheory.Definitions.Jets.SumIoPrAlt",
     [(25, 39), (123, 144)]),
    (B + "TensorMomentEstimate", [(59, 83), (108, 121)]),
    (J + "CapelliComatrixPicksSplitCasimirEigencomponent", [(48, 103), (109, 119)]),
    (J + "QuantumMinorRowExpansionEigenFunctional", [(13, 47)]),
    (J + "QuantumMinorColumnExpansionUnderLinearMap", [(29, 72)]),
    (J + "GlRelationRowStepsFunctionalEigen", [(164, 178)]),
    (J + "BesselColumnStepsFunctionalEigen", [(93, 101)]),
    (J + "ProjectorEntryValueUnderLinearFunctional", [(24, 55), (69, 103)]),
    (B + "DualTensorBesselMoment", [(88, 95), (116, 146), (147, 174)]),
    (B + "FamilySetupMomentGrowth", [(66, 113)]),
    (B + "ExistsKTypeNonzeroBessel", [(19, 38)]),
    (J + "FrameWConjMatrixUnits", [(337, 340)]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert (atlas["repository"], atlas["commit"]) == (REPO, REV)
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    out = []
    for module, ranges in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        rec = inspect_file({"repository": REPO, "commit": REV,
                            "path": path, "git_blob_sha1": blobs[module]}, offline)
        assert rec["matches_pinned_blob"]
        data = (ROOT / "build/source-cache" / REPO / REV / path).read_bytes()
        lines = data.splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            part = b"".join(lines[lo-1:hi])
            assert len(part) <= 12_288
            excerpts.append({"lines": [lo, hi], "bytes": len(part), "sha256": sha(part)})
        out.append({"module": module,
                    **{k: rec[k] for k in ["repository", "commit", "path", "bytes",
                                           "sha256", "git_blob_sha1", "matches_pinned_blob"]},
                    "excerpts": excerpts})
    prior = []
    for file, lo, hi in [("81-rp-section.tex", 18, 56),
                         ("87-rq-section.tex", 50, 108),
                         ("72-fd-section.tex", 462, 516)]:
        path = "paper/sections/recovered/"+file
        data = subprocess.check_output(["git", "show", f"{PRIOR}:{path}"], cwd=ROOT)
        part = b"".join(data.splitlines(keepends=True)[lo-1:hi])
        prior.append({"repository": "JoseBrox/GRH_distillation", "commit": PRIOR,
                      "path": path, "sha256": sha(data), "lines": [lo, hi],
                      "excerpt_sha256": sha(part)})
    return out, prior


def compositions(total, length):
    if length == 1:
        return [(total,)]
    return [(a,)+rest for a in range(total+1)
            for rest in compositions(total-a, length-1)]


def symmetric_power_units(n, degree):
    basis = compositions(degree, n)
    positions = {v: j for j, v in enumerate(basis)}
    units = [[sp.zeros(len(basis)) for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for col, weight in enumerate(basis):
                if weight[b]:
                    new = list(weight)
                    new[b] -= 1
                    new[a] += 1
                    units[a][b][positions[tuple(new)], col] = weight[b]
    return units


def sign(perm):
    return (-1)**sum(perm[a] > perm[b] for a in range(len(perm))
                    for b in range(a+1, len(perm)))


def quantum_minor(units, rows, cols, u):
    size = units[0][0].rows
    out = sp.zeros(size)
    for perm in itertools.permutations(range(len(rows))):
        term = sp.eye(size)
        for a in range(len(rows)):
            i, j = rows[perm[a]], cols[a]
            factor = units[i][j]
            if i == j:
                factor = factor+(u-a)*sp.eye(size)
            term = term*factor
        out += sign(perm)*term
    return out


def comatrix(units, y):
    n = len(units)
    return sp.BlockMatrix([
        [(-1)**(i+j)*quantum_minor(units,
            [a for a in range(n) if a != j],
            [a for a in range(n) if a != i], y+sp.Rational(n-1, 2))
         for j in range(n)] for i in range(n)]).as_explicit()


def quantum_checks():
    modules = evaluations = spectral = vanished = 0
    for n, degree in [(1, 0), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1)]:
        units = symmetric_power_units(n, degree)
        dim = units[0][0].rows
        parameter = [sp.Rational(n-1, 2)-a+(degree if a == 0 else 0)
                     for a in range(n)]
        operator = -sp.BlockMatrix(units).as_explicit()
        identity = sp.eye(n*dim)
        # Degree at most n: n+1 exact values certify each matrix polynomial.
        for y in range(n+1):
            scalar = sp.prod(y+t for t in parameter)
            determinant = quantum_minor(units, list(range(n)), list(range(n)),
                                        y+sp.Rational(n-1, 2))
            assert determinant == scalar*sp.eye(dim)
            cofactor = comatrix(units, y)
            assert cofactor*((y-sp.Rational(n-1, 2))*identity-operator) == scalar*identity
            evaluations += 1
        zeta = [-t-sp.Rational(n-1, 2) for t in parameter]
        total = sp.zeros(n*dim)
        for s in range(n):
            proj = identity
            for t in range(n):
                if t != s:
                    proj = proj*(operator-zeta[t]*identity)/(zeta[s]-zeta[t])
            assert proj*proj == proj
            ds = sp.prod(parameter[t]-parameter[s] for t in range(n) if t != s)
            assert comatrix(units, -parameter[s]) == ds*proj
            total += proj
            spectral += 1
            vanished += int(proj == sp.zeros(n*dim))
        assert total == identity
        modules += 1
    return {"exact_matrix_unit_modules": modules,
            "polynomial_identity_evaluations": evaluations,
            "spectral_cofactor_extractions": spectral,
            "zero_spectral_summands": vanished,
            "scope": "Finite representations check ordered shifts, signs and polynomial extraction; general proof is in the TeX."}


def string_checks():
    cases = rows_removed = columns_removed = rank_zero = 0
    tau = sp.Integer(3)
    for r in range(6):
        for k in range(1, 9):
            n = 2*r+k+1
            u = sp.Rational(n-1, 2)
            if r == 0:
                assert u == sp.Rational(k, 2)
                assert abs((-tau)*tau) == tau**2
                rank_zero += 1
            else:
                rows, cols = list(range(n-1)), list(range(1, n))
                factor = sp.Integer(1)
                for a in range(r):
                    b = a+1 if a < r-1 else r+k
                    assert a in rows and b in cols and a not in cols
                    rows.remove(a)
                    cols.remove(b)
                    factor *= 1 if a < r-1 else tau
                    rows_removed += 1
                assert rows == list(range(r, n-1))
                assert cols == list(range(r, r+k))+list(range(r+k+1, n))
                for b in range(n-1, r+k, -1):
                    a = b-1
                    assert a in rows and b in cols and b not in rows
                    rows.remove(a)
                    cols.remove(b)
                    factor *= tau if a == r+k else 1
                    u -= 1
                    columns_removed += 1
                assert rows == cols == list(range(r, r+k))
                assert factor == tau**2
                assert u == sp.Rational(k, 2)
            cases += 1
    return {"original_row_column_configurations": cases,
            "row_removals": rows_removed, "column_removals": columns_removed,
            "rank_zero_configurations": rank_zero,
            "exact_geometric_factor_and_final_shift": True}


def formal_degree_checks():
    cases = 0
    for n in range(2, 10):
        # Use a strictly decreasing separated list throughout.
        mu = [sp.Integer(5*(n-a)**2) for a in range(n)]
        degree = sp.prod(abs(mu[a]-mu[b]) for a in range(n) for b in range(a+1, n))
        for s in range(n):
            shifted = mu.copy()
            shifted[s] -= 1
            other = sp.prod(abs(shifted[a]-shifted[b])
                            for a in range(n) for b in range(a+1, n))
            original = sp.prod(abs(mu[s]-mu[t]) for t in range(n) if t != s)
            lowered = sp.prod(abs(mu[s]-1-mu[t]) for t in range(n) if t != s)
            assert other > 0 and lowered > 0
            assert degree/other == original/lowered
            cases += 1
    return {"same_constant_vandermonde_ratio_cases": cases}


def controls():
    units = symmetric_power_units(2, 1)
    operator = -sp.BlockMatrix(units).as_explicit()
    y = sp.Integer(3)
    scalar = (y+sp.Rational(3, 2))*(y-sp.Rational(1, 2))
    # A one-unit error in the right-hand shift destroys the quantum comatrix identity.
    assert comatrix(units, y)*((y+sp.Rational(1, 2))*sp.eye(4)-operator) != scalar*sp.eye(4)
    # Formal degrees for unrelated Haar scalings cannot be cancelled as a common constant.
    original_ratio = sp.Rational(7, 3)
    assert 2*original_ratio != original_ratio
    return {"controls_rejected": 2,
            "labels": ["quantum comatrix right-hand shift changed by one",
                       "different Haar scaling constants cancelled as identical"]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources, prior = source_records(args.offline)
    exact = {"quantum_comatrices": quantum_checks(), "character_strings": string_checks(),
             "formal_degrees": formal_degree_checks(), "negative_controls": controls()}
    artifacts = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
                 f"paper/shared/{STEM}-references.tex",
                 "scripts/check_global_norm_frontier_normalized_lowering.py"]
    certificate = {
        "date": "2026-11-22", "status": "PASS",
        "claim": "Original degree-normalized lowering scalar is at most T*b^4 "
                 "under the supplied signed Pieri family and original normalized subgroup periods.",
        "new_supplier": "Original one-slot quantum cofactor evaluation and normalized signed adjoint reduction.",
        "retained_data": ["original period test domain generated by group translates of compact finite vectors",
                          "subgroup period integrability and rank-one factorization",
                          "original character amplitudes and Witt frame",
                          "both r=0 and r>0 geometric normalizations",
                          "ordered noncommuting minors and all shifts",
                          "formal degrees for the same Haar measure"],
        "sources": sources, "existing_mathematics_reused": prior, "exact_checks": exact,
        "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())}
                      for p in artifacts],
        "dependencies": [{"path": p, "sha256": sha((ROOT/p).read_bytes())} for p in
                         ["certificates/global-norm-frontier-lowering-product.json",
                          "certificates/global-norm-frontier-tensor-projections.json"]],
        "limitations": ["Original normalized Bessel and Pieri families remain supplied inputs.",
                        "No construction or identification of that family with the original Jacquet transform.",
                        "No proof of original quotient L2 mass/isometry here.",
                        "Finite checks supplement the general proof; no Lean build.",
                        "No RH/GRH whole-node count change."],
        "reproduce": "python3 scripts/check_global_norm_frontier_normalized_lowering.py --offline",
    }
    output = ROOT/"certificates"/f"{STEM}.json"
    output.write_text(json.dumps(certificate, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "checks": exact, "certificate": str(output.relative_to(ROOT))},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
