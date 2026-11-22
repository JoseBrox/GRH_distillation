#!/usr/bin/env python3
"""Authenticate the original integral type construction and its conventions.

The all-rank proof is in the note. Exact small-rank algebra checks supplement
the proof; this script is not a Lean build or a whole-W04 certificate.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
import urllib.request

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
DENSE = "ModularityArgument.ThresholdArguments.DenseThresholdCases."
RANGES = {
    BASE+"WeilGroupCharacters.ContinuousResP": [(73, 92)],
    BASE+"WeilGroupCharacters.UniversalOrdinaryDeterminantRing": [(109, 127)],
    BASE+"WeilGroupCharacters.ArithmeticPointClassicality": [(12, 18)],
    BASE+"HeckeAlgebras.Distinct": [(103, 105)],
    BASE+DENSE+"UnitaryHeckeData": [(18, 41), (59, 67)],
    BASE+DENSE+"PTypeEx": [(29, 71), (88, 136)],
    BASE+DENSE+"TTypeEx": [(18, 21)],
    BASE+DENSE+"TypesNZeroKIface": [(16, 34)],
}

PRIMARY = [
    {
        "file": "shotton-gln.pdf",
        "url": "https://maths.dur.ac.uk/users/jack.g.shotton/papers/gln.pdf",
        "sha256": "1924aaf7f67ff68852ae8ceb4f9d0edacb36a53447cdd9411f499a4e91994372",
        "reference": "Shotton, The Breuil-Mezard conjecture when l != p (2018)",
        "reviewed": [
            "Author pp.10-12: inertial types include monodromy through the associated continuous inertia representation; partitions and dominance.",
            "Author p.13: normalized r_l and independence of the complex embedding; Theorem 3.7(1),(2).",
            "Author p.14: Example 3.8, trivial GL2 compact type versus the Steinberg parameter.",
            "Author pp.38-45: arbitrary simple characters and the local SZ construction; Corollary 6.21(1),(2).",
        ],
        "use": "An actual compact type isolates the prescribed zero-monodromy inertial parameter. No genericity, depth-zero, quasi-banal, ell>n or p>n condition is used.",
        "dependency_scope": "Only the local representation-theoretic construction in section 6, not the global patching or Breuil-Mezard theorem.",
    },
    {
        "file": "henniart2001.pdf",
        "url": "https://www.numdam.org/item/JTNB_2001__13_1_167_0.pdf",
        "sha256": "c9db009ee2f2e561d834b9e1ef07a8b27ff40d0edd19546d3351f38f39b2dac5",
        "reference": "Henniart, Sur la conjecture de Langlands locale pour GL_n (2001)",
        "reviewed": "Section 7.4, printed pp.185-186; the exact normalization is also stated in Shotton section 3.4.",
        "use": "Equivariance of normalized LLC under coefficient-field automorphisms; all conjugates introduced by restriction of scalars detect the same E0-defined type.",
    },
]


def partitions(n, largest=None):
    if n == 0:
        yield ()
        return
    if largest is None:
        largest = n
    for first in range(min(n, largest), 0, -1):
        for tail in partitions(n-first, first):
            yield (first,)+tail


def dominates(p, q):
    if sum(p) != sum(q):
        return False
    return all(sum(p[:j]) >= sum(q[:j])
               for j in range(1, max(len(p), len(q))+1))


def exact_checks():
    import sympy as s

    counts = {}
    for n in range(13):
        target = (1,)*n
        parts = list(partitions(n))
        for p in parts:
            assert dominates(p, target)
            assert dominates(target, p) == (p == target)
        counts[str(n)] = len(parts)
    assert not dominates((1, 1), (2,))
    # For a target action A and coefficient action A^(-transpose),
    # the tuple of target basis vectors satisfies the original covariance.
    # Clear det(A) to check the identity in a universal integral ring.
    a = s.Matrix(3, 3, s.symbols("a0:9"))
    cleared = a*a.adjugate()-a.det()*s.eye(3)
    assert all(s.expand(x) == 0 for x in cleared)
    # Wild rank-one control: 1+3Z_3 modulo 1+9Z_3 has a character
    # mapping 4 modulo 9 to 2 modulo 7, of exact order three.
    assert [pow(4, j, 9) for j in range(3)] == [1, 4, 7]
    assert [pow(2, j, 7) for j in range(3)] == [1, 2, 4]
    assert pow(4, 3, 9) == pow(2, 3, 7) == 1
    assert all(
        ((1+3*i)*(1+3*j)) % 9 == (1+3*((i+j) % 3)) % 9
        for i in range(3) for j in range(3)
    )
    return {
        "status": "PASS",
        "dominance": {
            "ranks": [0, 12],
            "partition_counts": counts,
            "scope": "Every partition through rank 12 checked against the all-ones minimum; the note proves this in every rank.",
        },
        "covariance": {
            "identity": "A adj(A) = det(A) I for the universal 3x3 matrix over Z[a0,...,a8]",
            "scope": "Exact polynomial check of the dual convention; the note gives the all-rank matrix argument.",
        },
        "negative_controls": [
            "GL2 partition (2) is not dominated by the N=0 partition (1,1); the primary source identifies these with the Steinberg and trivial compact-type cases.",
            "For p=3, ell=7, the order-three character of (1+3Z_3)/(1+9Z_3) is nontrivial on wild inertia and cannot be inflated from F_3^times.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert hashlib.sha256(packed).hexdigest() == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    rows = {row[0]: row for row in atlas["modules"]}
    sources = []
    for module, ranges in RANGES.items():
        item = {
            "repository": atlas["repository"], "commit": atlas["commit"],
            "path": "lean/src/"+module.replace(".", "/")+".lean",
            "git_blob_sha1": rows[module][1],
        }
        checked = inspect_file(item, args.offline)
        cache = ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]
        lines = cache.read_bytes().splitlines(keepends=True)
        excerpts = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines) and end-start+1 <= 120
            data = b"".join(lines[start-1:end])
            assert len(data) <= 12000
            excerpts.append({"start": start, "end": end,
                             "sha256": hashlib.sha256(data).hexdigest()})
        sources.append({**item, "module": module,
                        "sha256": checked["sha256"],
                        "matches_pinned_blob": True,
                        "reviewed_excerpts": excerpts})
    refs = []
    for item in PRIMARY:
        target = ROOT/"build/selmer-type-sources"/item["file"]
        if not target.exists():
            if args.offline:
                raise FileNotFoundError(f"Primary PDF missing in offline mode: {target}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(urllib.request.urlopen(item["url"], timeout=60).read())
        data = target.read_bytes()
        assert data.startswith(b"%PDF"), item["file"]
        assert hashlib.sha256(data).hexdigest() == item["sha256"], item["file"]
        refs.append({**item, "bytes": len(data), "local_hash_verified": True})
    stem = "selmer-integral-frontier-type-construction"
    artifacts = [
        f"notes/{stem}.md",
        f"paper/shared/{stem}.tex",
        f"paper/shared/{stem}-references.tex",
        "scripts/check_selmer_integral_frontier_type_construction.py",
    ]
    dependencies = [
        "notes/classical-local-correspondence.md",
        "notes/local-correspondence-bridge.md",
        "certificates/classical-local-correspondence.json",
        "certificates/local-correspondence-bridge.json",
    ]
    for path in artifacts:
        assert all(c >= 32 or c in (9, 10) for c in (ROOT/path).read_bytes()), path
    report = {
        "schema_version": 1, "status": "PASS",
        "classification": "closed integral type-existence subobligation inside W04",
        "verification_kind": "Pinned-source and primary-PDF provenance, exact finite dominance and dual-convention checks; the all-rank standard mathematical proof is in the note.",
        "claim": "The exact TTypeEx/TypeForAlt integral type exists over the original coefficient DVR, with arbitrary conductor, zero-monodromy discrimination and all weak-correspondence quantifiers.",
        "quantifiers": [
            "Every original Hida setting, positive n, original coefficient DVR O, residual datum r, and complex embedding.",
            "Every original type place, whose residue characteristic p differs from ell by St_l; repeated inertial characters and wild ramification are allowed.",
            "Every irreducible admissible local representation; no genericity or temperedness assumption.",
            "Every allowed weak local correspondence; every nonzero representation isotypic for each original group factor.",
            "Every Teichmuller lift in the source contract, handled by uniqueness in the original complete DVR.",
        ],
        "decisive_interfaces": {
            "zero_monodromy": "All-ones partitions are dominance-minimal at fixed basic support, so Shotton 3.7(1),(2) become an exact iff including N=0.",
            "original_coefficients": "Choose a finite model E/E0, take a stable O_E lattice by the finite orbit sum, restrict scalars to O, and use normalized LLC equivariance for every conjugate summand.",
            "rank": "The local O-rank is [E_u:E0] dim_Eu sigma_u; the simultaneous rank is their product. Empty type set has rank one.",
            "covariance": "The source tuple condition is Hom_K(V^dual,pi); choose V=(Res L)^dual.",
            "weak_local_laws": "Inertia characters extend to the full local Galois group; Frobenius preserves their isotypic spaces. Semisimplicity makes the parameter toral even with repeats, so the established good-preimage/restricted-uniqueness bridge applies.",
            "isotypic_product": "Successive evaluation and Schur's lemma give M=(tensor pi_u) tensor W with W nonzero, retaining all multiplicity spaces.",
            "Teichmuller": "Hensel lifts roots of X^(|k|-1)-1 uniquely and multiplicatively; the lift has exactly the residual kernel.",
            "scope_in_source": {
                "p_ne_ell": "ContinuousResP:82-83",
                "exact_type": "Distinct:103-105",
                "universal_Teichmuller_and_product": "UnitaryHeckeData:22-41",
                "frontier": "TTypeEx:18-21; PTypeEx:29-71,88-136",
                "reducibility_allowed": "UnitaryHeckeData:38-41 imposes open-kernel covariance detection, not irreducibility of tau0",
            },
        },
        "limitations": [
            "No uniform bound on the coefficient-field enlargement or compact type rank.",
            "No nonzero residual automorphic summand is asserted.",
            "No patched support, full Taylor-Wiles level comparison, two-sided rigidity or moving-family integral Selmer bound is proved.",
            "No whole proof-map node is completed, and no Lean project build is certified.",
        ],
        "exact_checks": exact_checks(),
        "primary_references": refs,
        "dependencies": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
                         for p in dependencies],
        "sources": sources,
        "artifacts": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
                      for p in artifacts],
    }
    target = ROOT/"certificates"/f"{stem}.json"
    target.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "modules": len(sources),
                      "primary_pdfs": len(refs),
                      "certificate": str(target.relative_to(ROOT)),
                      "scope": report["verification_kind"]}))


if __name__ == "__main__":
    main()
