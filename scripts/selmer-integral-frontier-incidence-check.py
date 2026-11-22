#!/usr/bin/env python3
"""Verify provenance and boundary algebra of the local incidence proof.

Finite computations check chart identities and negative controls.  The note
proves the regular-local result for every size and every residue field.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import urllib.request

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
SOURCES = [
    ("AlgebraTools.CotInd", [(7, 14)]),
    ("AlgebraTools.DetLocus", [(18, 20)]),
    ("AlgebraTools.CaDetLocus", [(10, 58)]),
    ("AlgebraTools.CaDetCore", [(9, 48)]),
    ("PatchingModules.SelmerScaling.Ired", [(6, 7), (84, 96)]),
    ("PatchingModules.SelmerScaling.CotangentIndependentOfResidues", [(30, 73), (74, 158), (158, 211)]),
    ("PatchingModules.SelmerScaling.SelmerSpannedByKappaLaurent", [(163, 171)]),
    ("PatchingModules.AutomorphicDetection.GalOut", [(16, 43)]),
]
REFERENCES = {
    "00NP": ("5e8fc76f202b603711e5dcd02dbfe673b7452a02be4fed0320e35468e5a60ccd", "Regular local rings are domains."),
    "00NQ": ("28e8c01c12a52b05820c32d5a1dfc3f5f8d4e79776d2507b5588bcee0f4ffeac", "Independent parameters give regular quotients of the expected dimension."),
    "02IL": ("87a068f5985b50eb948fc31bb7e4f5852622e71f251b4cfe42e026fa1e30d52f", "Every point of a locally Noetherian scheme specializes to a closed point."),
    "02IT": ("2647b4a100e10c20d9dc7419d1b7681723f991b353856fb68763f983d417b2ab", "Regularity is detected at closed local rings."),
    "01W1": ("84b986dca418f3a7d39d05bb44d0d7a2320cc793997848253c3281dbb8c8e5da", "Proper morphisms are universally closed."),
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def sources(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["commit"] == REV
    blobs = {r[0]: r[1] for r in atlas["modules"]}
    out = []
    for suffix, ranges in SOURCES:
        name = PREFIX + suffix
        rel = "lean/src/" + name.replace(".", "/") + ".lean"
        r = inspect_file({"repository": "jsmorph/rh", "commit": REV,
                          "path": rel, "git_blob_sha1": blobs[name]}, offline)
        assert r["matches_pinned_blob"]
        data = (ROOT / "build/source-cache/jsmorph/rh" / REV / rel).read_bytes()
        lines = data.splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpts.append({"first_line": lo, "last_line": hi,
                             "sha256": sha(b"".join(lines[lo-1:hi]))})
        out.append({"module": name, "path": rel, "commit": REV,
                    "git_blob_sha1": blobs[name], "sha256": sha(data),
                    "matches_pinned_blob": True, "excerpts": excerpts})
    return out


def references(offline):
    cache = ROOT / "build/reference-cache/selmer-integral-frontier-incidence"
    cache.mkdir(parents=True, exist_ok=True)
    out = []
    for tag, (expected, role) in REFERENCES.items():
        path = cache / (tag + ".html")
        url = "https://stacks.math.columbia.edu/tag/" + tag
        if not path.exists():
            if offline:
                raise FileNotFoundError(path)
            path.write_bytes(urllib.request.urlopen(url, timeout=30).read())
        data = path.read_bytes()
        assert sha(data) == expected, (tag, "Primary snapshot changed; inspect before repinning.")
        assert tag.encode() in data
        out.append({"url": url, "tag": tag, "sha256": expected,
                    "bytes": len(data), "role": role,
                    "checked_on": "2026-11-22"})
    return out


def chart_checks():
    records = []
    for g in range(1, 6):
        z = sp.Matrix(g, g, sp.symbols(f"z0:{g*g}"))
        y = sp.Matrix(sp.symbols(f"y0:{g}"))
        for c in range(g):
            u = {j: sp.Symbol(f"u{j}") for j in range(g) if j != c}
            line = sp.Matrix([1 if j == c else u[j] for j in range(g)])
            equations = list(z*line) + [y[j]-u[j]*y[c] for j in u]
            pivot_vars = [z[i, c] for i in range(g)] + [y[j] for j in u]
            pivot = sp.Matrix(equations).jacobian(pivot_vars)
            assert pivot == sp.eye(2*g-1)
            substitution = {z[i, c]: -sum(u[j]*z[i, j] for j in u) for i in range(g)}
            substitution.update({y[j]: u[j]*y[c] for j in u})
            z1 = z.subs(substitution, simultaneous=True)
            y1 = y.subs(substitution, simultaneous=True)
            assert all(sp.expand(a) == 0 for a in z1*line)
            assert all(sp.expand(a) == 0 for a in z1*y1)
            if g <= 4:
                assert sp.expand(z1.det()) == 0
            records.append({"g": g, "chart": c, "pivot_determinant": 1,
                            "equations": 2*g-1, "auxiliary_variables": g-1,
                            "dimension_drop": g,
                            "determinant_expanded": g <= 4})
    return records


def determinant_mod(matrix, p):
    a = [list(row) for row in matrix]
    n = len(a)
    det = 1
    for c in range(n):
        pivot = next((i for i in range(c, n) if a[i][c] % p), None)
        if pivot is None:
            return 0
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            det = -det
        value = a[c][c] % p
        det = det*value % p
        inverse = pow(value, -1, p)
        for i in range(c+1, n):
            factor = a[i][c]*inverse % p
            for j in range(c, n):
                a[i][j] = (a[i][j]-factor*a[c][j]) % p
    return det % p


def finite_fields():
    records = []
    for p, g in [(2, 1), (3, 1), (2, 2), (3, 2), (5, 2), (2, 3)]:
        vectors = list(itertools.product(range(p), repeat=g))
        lines = [v for v in vectors if any(v) and next(a for a in v if a) == 1]
        span = {v: {tuple(a*b % p for b in v) for a in range(p)} for v in lines}
        count = total = 0
        for entries in itertools.product(range(p), repeat=g*g):
            z = [entries[i*g:(i+1)*g] for i in range(g)]
            det = determinant_mod(z, p)
            kernels = [v for v in lines if all(sum(z[i][j]*v[j] for j in range(g)) % p == 0 for i in range(g))]
            for y in vectors:
                algebraic = det == 0 and all(sum(z[i][j]*y[j] for j in range(g)) % p == 0 for i in range(g))
                incidence = any(y in span[v] for v in kernels)
                assert algebraic == incidence
                count += algebraic
                total += 1
        gl = 1
        for j in range(g):
            gl *= p**g-p**j
        formula = (p**g-1)*p**(g*(g-1)) + p**(g*g)-gl
        assert count == formula
        records.append({"field_order": p, "matrix_size": g,
                        "matrix_vector_pairs_checked": total,
                        "determinantal_incidence_pairs": count,
                        "independent_count_formula": formula})
    return records


def negative_controls():
    a, b, c = sp.symbols("a b c")
    # Without independent cotangent entries: g=1, z=a*b, y=c;
    # primes (a), (b) violate the claimed inclusion at the threshold.
    assert sp.rem(a*b*c, a, a, b, c) == 0
    assert sp.rem(a*b, b, b, a, c) == 0
    assert sp.rem(a, b, b, a, c) != 0
    # Without dimension: z=a, y=b, primes (a,c), (a), with dimensions 1,2.
    assert sp.groebner([a, c], a, b, c).reduce(a*b)[1] == 0
    assert sp.groebner([a], a, b, c).reduce(c)[1] != 0
    return {"dropped_cotangent_independence": "z=a*b, y=c, primes (a) and (b), d=3, g=1",
            "dropped_dimension_threshold": "z=a, y=b, primes (a,c) and (a), d=3, g=1",
            "dropped_determinant_equation": "Z=identity, y=zero has no projective kernel line",
            "size_zero": "empty determinant is one; there is no determinant prime"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    record = {"status": "PASS", "source_provenance": sources(args.offline),
              "primary_reference_snapshots": references(args.offline),
              "symbolic_charts": chart_checks(), "finite_field_incidence": finite_fields(),
              "negative_controls": negative_controls(),
              "proved_in_note": "Exact regular-local prime inclusion used by presOut1, with its full application to the stated B plus N presentation.",
              "not_verified": ["Lean build", "arithmetic construction of independent coefficient rows", "patched automorphic dimension supplier", "whole Selmer node"],
              "node_counts_unchanged": {"RH": "6/9", "GRH": "17/31"}, "artifacts": {}}
    for rel in ["notes/selmer-integral-frontier-incidence.md", "paper/shared/selmer-integral-frontier-incidence.tex", "scripts/selmer-integral-frontier-incidence-check.py"]:
        record["artifacts"][rel] = sha((ROOT / rel).read_bytes())
    target = ROOT / "certificates/selmer-integral-frontier-incidence.json"
    target.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "PASS", "source_files": len(SOURCES),
                      "primary_snapshots": len(REFERENCES), "symbolic_charts": len(record["symbolic_charts"]),
                      "finite_field_pairs": sum(x["matrix_vector_pairs_checked"] for x in record["finite_field_incidence"]),
                      "certificate": str(target)}))


if __name__ == "__main__":
    main()
