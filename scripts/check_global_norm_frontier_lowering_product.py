#!/usr/bin/env python3
"""Authenticate and exactly check the interlacing lowering-product supplier."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "global-norm-frontier-lowering-product"
J = "Development.AbelianVarietyTheory.Proofs.JetHarmonics."
B = "CompanionTheory.AutomorphicTheory.PieriRules.ThetaBesselIsometries."
SOURCES = [
    (J + "LoweringBound", [(12, 25), (43, 89)]),
    (B + "FamilySetupMomentGrowth", [(66, 113)]),
    (B + "DualTensorBesselMoment", [(88, 95), (116, 146)]),
    (J + "ProjectorEntryValueUnderLinearFunctional", [(24, 55), (69, 103)]),
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
    return out


def polynomials(cloud, roots):
    y = sp.Symbol("y")
    p = sp.prod(y-v for v in cloud)
    q = sp.prod(y-v for v in roots)
    a = sum(roots)-sum(cloud)
    residues = [-sp.cancel(q.subs(y, t)/sp.diff(p, y).subs(y, t)) for t in cloud]
    assert all(w > 0 for w in residues)
    assert sp.cancel(q/p-y+a+sum((w/(y-t) for t, w in zip(cloud, residues)), sp.Integer(0))) == 0
    # Rational arrowhead, diagonally similar to the symmetric arrowhead with sqrt(w).
    arrow = sp.diag(*(cloud+[a]))
    for i, w in enumerate(residues):
        arrow[i, len(cloud)] = 1
        arrow[len(cloud), i] = w
    assert sp.expand(arrow.charpoly(y).as_expr()-q) == 0
    return a, residues


def family_checks():
    families = cases = zeros = partial_fractions = 0
    for k in range(1, 7):
        for extra in (1, 2, 3):
            n = k+extra
            gamma = sp.Integer(8 if extra % 2 else 32)
            for large in (False, True):
                bound = sp.Integer(10**6*n**7 if large else 64*gamma*k)
                outer = 3*bound
                cloud = [gamma*(k-1-a) for a in range(k-1)]
                lam = cloud+[-bound-8*a for a in range(extra+1)]
                for endpoints in (False, True):
                    if endpoints and k > 1:
                        roots = [v+sp.Rational(1, 2) for v in cloud]+[cloud[-1]-sp.Rational(1, 2)]
                    else:
                        roots = [gamma*(k-i+sp.Rational(1, 2)) for i in range(1, k+1)]
                    assert len(lam) == n and len(roots) == k
                    assert all(roots[a] > cloud[a] > roots[a+1] for a in range(k-1))
                    assert all(abs(t) <= outer for t in lam+roots)
                    assert all(0 <= t <= bound/8 for t in cloud)
                    assert all(-2*bound <= t <= -bound for t in lam[k-1:])
                    a, residues = polynomials(cloud, roots)
                    assert a*a+sum(residues) <= outer*outer
                    partial_fractions += 1
                    reserve = gamma/8
                    shifts = [[sp.Integer(0)]*n]
                    for position in range(n):
                        for amount in (-reserve, -1, 1, reserve):
                            delta = [sp.Integer(0)]*n
                            delta[position] = amount
                            shifts.append(delta)
                    for delta in shifts:
                        assert sum(abs(t) for t in delta) <= reserve
                        assert reserve <= min(gamma/8, bound/4, outer)
                        mu = [u+v for u, v in zip(lam, delta)]
                        if any(mu[j]-mu[j+1] < 2 for j in range(n-1)):
                            continue
                        for s in range(n):
                            den = sp.prod(abs(mu[s]-1-mu[t]) for t in range(n) if t != s)
                            assert den >= 1
                            num = sp.prod(abs(mu[s]-sp.Rational(1, 2)-u) for u in roots)
                            ratio = num/den
                            if s < k-1:
                                # e>2, so this is stronger than 8e sqrt(k) b^2.
                                assert ratio**2 <= 256*k*outer**4
                            else:
                                # Again a stronger rational bound, using e>2.
                                assert ratio <= 12*outer**2
                            if large:
                                assert ratio <= outer**4
                            zeros += int(num == 0)
                            cases += 1
                    families += 1
    assert zeros > 0
    return {"interlacing_parameter_families": families,
            "exact_partial_fractions_and_arrowhead_polynomials": partial_fractions,
            "exact_product_inequalities": cases,
            "zero_numerator_cases": zeros,
            "includes_k_one": True,
            "includes_original_large_parameter_range": True,
            "scope": "Finite rational checks supplement the general theorem."}


def constants():
    x, y = sp.symbols("x y", nonnegative=True)
    n = x+1
    b = 10**6*n**7+y
    checks = [b*b-24*n, b*b-18]
    for expression in checks:
        assert all(z >= 0 for z in sp.Poly(sp.expand(expression), x, y).coeffs())
    assert sp.Rational(3, 2)*sp.Rational(7, 2)+1 == sp.Rational(25, 4)
    assert sp.Rational(7, 2)+sp.Rational(4, 3) < 6
    assert sp.Rational(1, 4)+sp.Rational(1, 2) == sp.Rational(3, 4)
    return {"large_parameter_polynomial_certificates": 2,
            "exact_coarse_constants": 3}


def controls():
    # Without interlacing the residues need not be positive.
    y = sp.Symbol("y")
    p, q = y, (y-1)*(y-2)
    wrong_residue = -q.subs(y, 0)/sp.diff(p, y).subs(y, 0)
    assert wrong_residue == -2
    # Without the shifted denominator gap the quotient may have a pole.
    mu, roots = [sp.Integer(1), sp.Integer(0)], [sp.Integer(2)]
    assert mu[0]-1-mu[1] == 0
    assert mu[0]-sp.Rational(1, 2)-roots[0] != 0
    return {"controls_rejected": 2,
            "labels": ["interlacing removed from positive-residue argument",
                       "shifted denominator gap removed"]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources = source_records(args.offline)
    exact = {"parameter_families": family_checks(), "constants": constants(),
             "negative_controls": controls()}
    artifacts = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
                 f"paper/shared/{STEM}-references.tex",
                 "scripts/check_global_norm_frontier_lowering_product.py"]
    certificate = {
        "date": "2026-11-22", "status": "PASS",
        "claim": "The original lowering product is at most b^4, with sharper "
                 "8e*sqrt(k)*b^2 and 6e*b^2 bounds in its two parameter regions.",
        "new_supplier": "Positive interlacing residues controlled together by a symmetric arrowhead matrix.",
        "retained_data": ["actual original numerator and shifted denominator",
                          "original compact and negative parameter regions",
                          "cloud reserve gamma/8 and negative-parameter reserve B0/4",
                          "same spectral scale and maximum parameter bound"],
        "sources": sources, "exact_checks": exact,
        "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())}
                      for p in artifacts],
        "limitations": ["Bessel scalar identification and normalized adjoint identity remain explicit inputs.",
                        "Original quotient mass/isometry and Pieri existence are not supplied by this estimate.",
                        "Finite checks supplement the general proof; no Lean build.",
                        "No whole-node RH/GRH count change."],
        "reproduce": "python3 scripts/check_global_norm_frontier_lowering_product.py --offline",
    }
    output = ROOT/"certificates"/f"{STEM}.json"
    output.write_text(json.dumps(certificate, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "checks": exact, "certificate": str(output.relative_to(ROOT))},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
