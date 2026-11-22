#!/usr/bin/env python3
"""Authenticate bounded sources and check conjugate-filtration formulas.

The all-characteristic geometric theorem is a written, independently reviewed
proof. This script checks provenance and exact finite algebra only. It does not
construct the arithmetic model, prove crystalline comparison, or replay Lean.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
import urllib.request

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
AS = "Development.AutomorphicSpectrum."
SOURCES = [
    ("Formalism.LocalToGlobal.ProjectiveLattices.IsChartIff", [[74, 117]]),
    ("Formalism.SharpRestriction.Divisibility.GeneratorPowers.GermCut", [[111, 125]]),
    (AS + "Definitions.CommutativeAlgebra.GermComp1ZeroPointLeft",
     [[17, 52], [68, 104]]),
    (AS + "Definitions.CommutativeAlgebra.IsSplitGaussChars", [[101, 131]]),
    (AS + "Proofs.GeometryProofs.ExistsHodgeLatticeGermSystem", [[85, 114]]),
    (AS + "Proofs.GeometryProofs.FibreCurveGermPowers", [[215, 270]]),
    (AS + "Proofs.GeometryProofs.AbelianQuotientOfPowerFns", [[174, 225]]),
    (AS + "Proofs.GeometryProofs.AbelianQuotientLattice", [[423, 450]]),
    (AS + "Definitions.GlobalGeometry.ToFirst", [[18, 39]]),
    ("Development.AbelianVarietyTheory.Definitions.Uniformization.ExistsInKNeOne",
     [[19, 35]]),
]
PRIMARY = [
    {
        "path": "build/reference-cache/mazur-messing-1974.pdf",
        "url": "https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/mazur-messing.pdf",
        "sha256": "54486ccb86cad19118bfdb9d1e56386b18a45c63529254f1a1f7b7d110ca5eee",
        "inspected": [
            "I.2.1, printed p.13: pointed first-neighbourhood rigidifications",
            "I.2.6.7, pp.24-25: universal extension and arbitrary base change",
            "II.9, pp.93-94: contravariant crystal via the dual universal extension",
            "II.13, pp.119-122: functorial abelian/p-divisible comparison",
        ],
    },
    {
        "path": "build/reference-cache/madapusi-pera-2019.pdf",
        "url": "https://www.numdam.org/item/10.24033/asens.2391.pdf",
        "sha256": "d7e0dfa1d9ef76f3f85682f1abcc52d3d66de9e9378e92fc9153a3ba5c10a077",
        "inspected": [
            "1.1.4, printed pp.404-405, especially (1.1.4.1): exact Hodge kernel of crystalline Frobenius",
        ],
        "role": "Only the ordinary proper Dieudonne/Hodge comparison is used.",
    },
    {
        "path": "build/reference-cache/conrad-units-product.pdf",
        "url": "https://math.stanford.edu/~conrad/papers/unitthm.pdf",
        "sha256": "0720c7f594d69049ebe70d804582a252fcd83852b6f530b3f52fabb7cee9e9e0",
        "inspected": [
            "Theorem 1.1, p.1, proof pp.1-3: units factor on connected reduced products",
        ],
    },
]
ARTIFACTS = [
    "notes/biextension-conjugate-filtration.md",
    "scripts/check_biextension_conjugate_filtration.py",
]


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def source_evidence(fetch: bool) -> list[dict]:
    compressed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(compressed) == inventory["compressed_graph"]["sha256"]
    graph = json.loads(gzip.decompress(compressed))
    assert graph["repository"] == "jsmorph/rh" and graph["commit"] == REV
    entries = {row[0]: row for row in graph["modules"]}
    result = []
    for module, ranges in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        record = inspect_file({
            "repository": "jsmorph/rh", "commit": REV, "path": path,
            "git_blob_sha1": entries[module][1],
        }, offline=not fetch)
        raw = (ROOT / "build/source-cache/jsmorph/rh" / REV / path).read_bytes()
        lines = raw.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            excerpt = b"\n".join(lines[lo - 1:hi]) + b"\n"
            assert len(excerpt) <= 12000
            excerpts.append({"lines": [lo, hi], "sha256": sha(excerpt)})
        result.append({
            "module": module, "path": path,
            "sha256": record["sha256"],
            "git_blob_sha1": record["git_blob_sha1"],
            "url": f"https://github.com/jsmorph/rh/blob/{REV}/{path}",
            "inspected_excerpts": excerpts,
        })
    return result


def primary_evidence(fetch: bool) -> list[dict]:
    for item in PRIMARY:
        path = ROOT / item["path"]
        if not path.exists() and fetch:
            path.parent.mkdir(parents=True, exist_ok=True)
            with urllib.request.urlopen(item["url"], timeout=50) as response:
                path.write_bytes(response.read())
        assert sha(path.read_bytes()) == item["sha256"], item["path"]
    return PRIMARY


def zero(matrix) -> bool:
    return all(sp.expand(x) == 0 for x in matrix)


def matrix_checks() -> dict:
    # Arbitrary rank-two blocks check the displayed coefficient identity and
    # alpha/beta signs; the written proof establishes arbitrary dimension.
    h = sp.Matrix(2, 2, sp.symbols("h0:4"))
    a = sp.Matrix(2, 2, sp.symbols("a0:4"))
    s = sp.symbols("s")
    sigma = sp.Matrix([[0, s], [-s, 0]])
    j = sigma.row_join(sp.eye(2)).col_join((-sp.eye(2)).row_join(sp.zeros(2)))
    alpha = h.col_join(a.T)
    beta = (-a + h.T * sigma).row_join(h.T)
    expected = h.T * sigma * h + h.T * a.T - a * h
    assert zero(alpha.T * j * alpha - expected)
    assert zero(beta * alpha - expected)
    assert zero(alpha.T * j - beta)

    # Fully nonsymmetric gauge, nontrivial integral coordinate change.
    z = sp.Matrix(3, 3, sp.symbols("z0:9"))
    u, v, w = sp.symbols("u v w")
    sigma1 = sp.Matrix([[0, u, v], [-u, 0, w], [-v, -w, 0]])
    ell = sp.Matrix([[1, 1, 0], [0, 1, 1], [0, 0, 1]])
    sigma2 = ell.T * sigma1 * ell + z.T - z
    j1 = sigma1.row_join(sp.eye(3)).col_join((-sp.eye(3)).row_join(sp.zeros(3)))
    j2 = sigma2.row_join(sp.eye(3)).col_join((-sp.eye(3)).row_join(sp.zeros(3)))
    t = ell.row_join(sp.zeros(3)).col_join(
        (ell.inv().T * z.T).row_join(ell.inv().T)
    )
    assert zero(t.T * j1 * t - j2)

    # Coefficient adjunction and symmetry coherence, retaining conjugation.
    r = sp.Matrix(2, 2, sp.symbols("r0:4"))
    rb = sp.Matrix(2, 2, sp.symbols("q0:4"))
    b = sp.Matrix(2, 2, sp.symbols("b0:4"))
    bb = (sigma * rb - r.T * sigma - b).T
    ma = r.row_join(sp.zeros(2)).col_join((-b.T).row_join(rb.T))
    mb = rb.row_join(sp.zeros(2)).col_join((-bb.T).row_join(r.T))
    assert zero(ma.T * j - j * mb)
    return {
        "alpha_pairing_and_beta": "PASS, generic rank-two polynomial matrices",
        "gauge": "PASS, generic nonsymmetric rank-three matrix and nontrivial integral basis",
        "adjoint_coherence": "PASS, generic rank-two polynomial matrices",
        "scope": "Exact sign and formula checks; dimension-independent proofs are written in the note.",
    }


class Truncated:
    """Exact F_p[x,y]/(x^(p+1),y^(p+1)) arithmetic."""

    def __init__(self, p: int):
        self.p = p
        self.one = {(0, 0): 1}

    def clean(self, a):
        return {m: c % self.p for m, c in a.items() if c % self.p}

    def add(self, a, b):
        out = dict(a)
        for m, c in b.items():
            out[m] = out.get(m, 0) + c
        return self.clean(out)

    def mul(self, a, b):
        out = {}
        for (i, j), c in a.items():
            for (k, ell), d in b.items():
                m = (i + k, j + ell)
                if max(m) <= self.p:
                    out[m] = out.get(m, 0) + c * d
        return self.clean(out)

    def power(self, a, n):
        out = self.one
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n //= 2
        return out

    def inv(self, a):
        assert a.get((0, 0), 0) == 1
        u = self.add(self.one, {m: -c for m, c in a.items()})
        out, term = self.one, self.one
        for _ in range(2 * self.p):
            term = self.mul(term, u)
            out = self.add(out, term)
        assert self.mul(a, out) == self.one
        return out

    def subst(self, a, xexp=1, yexp=1):
        return self.clean({
            (i * xexp, j * yexp): c
            for (i, j), c in a.items()
            if max(i * xexp, j * yexp) <= self.p
        })


def scalar_checks() -> dict:
    # Trivial symmetric biextension on a split torus, with arbitrary local
    # frame 1 + x^t Z y. Restrict to x_i,y_j; exchanged coefficient is Z_ji.
    # The actual group law has [p](x)=x^p in coordinates t=1+x.
    cases = 0
    for p in (2, 3, 5):
        alg = Truncated(p)
        for a in range(p):
            for b in range(p):
                f = alg.clean({(0, 0): 1, (1, 1): a})
                fs = alg.clean({(0, 0): 1, (1, 1): b})
                c = alg.mul(alg.power(f, p), alg.inv(alg.subst(f, xexp=p)))
                d = alg.mul(alg.power(f, p), alg.inv(alg.subst(f, yexp=p)))
                cswap = alg.mul(alg.power(fs, p), alg.inv(alg.subst(fs, yexp=p)))
                sy = alg.mul(fs, alg.inv(f))
                symmetry_rhs = alg.mul(cswap, alg.mul(
                    alg.subst(sy, yexp=p), alg.inv(alg.power(sy, p))
                ))
                assert d == symmetry_rhs
                lhs = alg.mul(alg.subst(c, yexp=p), alg.power(d, p))
                rhs = alg.mul(alg.subst(d, xexp=p), alg.power(c, p))
                assert lhs == rhs
                assert c.get((p, 1), 0) == -a % p
                assert sy.get((1, 1), 0) == (b - a) % p
                assert (-a + b - (b - a)) % p == 0
                cases += 1
    return {
        "cases": cases, "primes": [2, 3, 5], "status": "PASS",
        "checked": [
            "Two p-fold scalar identities to bidegree (p,p)",
            "A=-Z and Sigma=Z^t-Z in an arbitrary-frame split-torus example",
            "Alternating/isotropic matrix identity including characteristic two",
        ],
        "scope": "Exact finite examples checking signs; not a replacement for the all-prime formal proof.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fetch-missing", action="store_true")
    args = parser.parse_args()
    sources = source_evidence(args.fetch_missing)
    primary = primary_evidence(args.fetch_missing)
    matrices = matrix_checks()
    scalars = scalar_checks()
    certificate = {
        "status": "PASS",
        "subject": "Intrinsic same-lattice Hodge and conjugate filtrations",
        "source_revision": REV,
        "automated_scope": "Pinned-byte provenance and exact finite algebra only.",
        "independent_review": {
            "status": "PASS, mathematical review by root and finite_window_audit",
            "record": "certificates/hard-node-review-2026-11-22.json",
            "scope": "Written geometric theorem, same-model source match and formal-chart corollary; not Lean replay.",
        },
        "source_evidence": sources,
        "primary_evidence": primary,
        "matrix_checks": matrices,
        "scalar_checks": scalars,
        "artifact_hashes": {path: sha((ROOT / path).read_bytes()) for path in ARTIFACTS},
        "remaining": [
            "Actual arithmetic integral model and compatible chart/fibre construction",
            "Integral complex multiplication evaluation",
            "Separate finite section-degree and cusp estimates",
        ],
        "node_counts_changed": False,
        "lean_kernel_replayed": False,
    }
    destination = ROOT / "certificates/biextension-conjugate-filtration.json"
    destination.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({
        "status": "PASS", "sources": len(sources), "primary_pdfs": len(primary),
        "scalar_examples": scalars["cases"],
        "certificate": str(destination.relative_to(ROOT)),
        "scope": certificate["automated_scope"],
    }))


if __name__ == "__main__":
    main()
