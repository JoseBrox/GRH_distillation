#!/usr/bin/env python3
"""Authenticate the RH specialization and its exact threshold arithmetic.

The Selmer groups and the remaining resonant estimate are not computed.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    "HeightAndVanishing.DirichletPrimeToLPartMulLPowerPart":
        [(75, 106), (116, 120), (148, 219)],
    "HeightAndVanishing.BchiFacts": [(7, 10), (22, 41)],
    "HeightAndVanishing.Counts": [(9, 22), (60, 73)],
    "UnitaryThreeGroups.KatoUse": [(36, 64)],
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    lookup = {row[0]: row for row in atlas["modules"]}
    sources, texts = [], {}
    for suffix, ranges in RANGES.items():
        module = PREFIX + suffix
        row = lookup[module]
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        entry = {"repository": atlas["repository"], "commit": atlas["commit"],
                 "path": path, "git_blob_sha1": row[1]}
        checked = inspect_file(entry, args.offline)
        data = (ROOT / "build/source-cache" / atlas["repository"] / atlas["commit"] / path).read_bytes()
        texts[suffix] = data.decode()
        lines = data.decode().splitlines()
        excerpts = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines) and end-start < 120
            excerpts.append({"start": start, "end": end,
                             "sha256": sha("\n".join(lines[start-1:end]).encode())})
        sources.append({"module": module, "path": path, "sha256": sha(data),
                        "git_blob_sha1": row[1], "ranges": excerpts,
                        "source_check": checked})

    family = texts["HeightAndVanishing.DirichletPrimeToLPartMulLPowerPart"]
    assert "2 * t + 1 < h.q1 ∧ 2 * t + 1 < h.d" in family
    assert "h.q1 % 4 = 3" in family and "h.d % 4 = 3" in family
    assert "16 * h.o * (l * h.q) ^ 2 * 4 ^ n0 l ψ" in family
    assert "Even (orderOf (chiP l ψ))" in family
    assert "2 ≤ e ∧ EV l ψ" in family
    counts = texts["HeightAndVanishing.Counts"]
    assert "∀ χ : PChar, ∃ C : ℕ, ∀ h : Host" in counts
    assert "h.R1 l ψ ≤ 2 ^ c2 ψ" in counts
    assert "2 ^ c2 ψ < h.R1 l ψ" in counts

    # For the conductor-one host, th1 has order 1 or 2, so lcm(4,ord(th1))=4.
    assert all(sp.ilcm(4, o) == 4 for o in [1, 2])
    f3 = int(sp.n_order(3, 4))
    n3 = int(sp.factorint(3**f3 - 1)[2])
    threshold = 16 * 3**2 * 4**n3
    assert (f3, n3, threshold) == (2, 3, 9216)
    assert 2**13 < threshold <= 2**14
    for p in [13, 17]:
        assert sp.isprime(p) and p % 4 == 1 and sp.gcd(p, 90) == 1

    e = sp.Symbol("e", integer=True, positive=True)
    # N >= 2 and ell <= 2e+1 imply ell*N*e <= [N(e+1)]^2.
    gap = sp.expand(2*(e+1)**2-e*(2*e+1))
    assert gap == 3*e+2
    # The converse conversion uses ell >= 3 and e >= 1.
    converse_gap = sp.expand(3*e-(e+1))
    assert converse_gap == 2*e-1

    artifacts = ["paper/shared/rh-selmer-nonresonant.tex",
                 "paper/shared/rh-selmer-nonresonant-references.tex",
                 "notes/rh-selmer-nonresonant.md"]
    all_tex = "\n".join(p.read_text() for p in (ROOT / "paper").rglob("*.tex"))
    labels = set(re.findall(r"\\label\{([^}]+)\}", all_tex))
    tex = (ROOT / artifacts[0]).read_text()
    assert all(x in labels for x in re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", tex))
    output = {
        "classification": "Closed nonresonant RH Selmer obligations; the resonant frontier and full W04 remain open.",
        "source_repository": atlas["repository"], "source_commit": atlas["commit"],
        "verification_scope": "Pinned source authentication and exact elementary arithmetic; no Selmer computation, automated arithmetic proof, or Lean rebuild.",
        "sources": sources,
        "exact_checks": {
            "auxiliary_field": "Q(sqrt(-3)), discriminant -3, norm-Euclidean class number one proved in text",
            "fixed_auxiliary_primes": [13, 17],
            "coefficient_prime_3_excluded_from_nonresonant_theorem": True,
            "prime_3_order_modulo_4": f3,
            "prime_3_two_adic_exponent": n3,
            "original_threshold_at_3": threshold,
            "largest_lower_layer_exponent": 13,
            "polynomial_bound_conversion": {
                "source_to_combined_frontier": "C -> 2C+1",
                "combined_frontier_to_source": "B -> B",
                "forward_gap_at_N_equals_2": str(gap),
                "reverse_gap_at_ell_equals_3": str(converse_gap),
            },
        },
        "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())} for p in artifacts],
    }
    dest = ROOT / "certificates/rh-selmer-nonresonant.json"
    dest.write_text(json.dumps(output, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"certificate": str(dest.relative_to(ROOT)),
                      "sources": len(sources), "exact_checks": "passed",
                      "scope": output["verification_scope"]}))


if __name__ == "__main__":
    main()
