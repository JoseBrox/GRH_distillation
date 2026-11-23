#!/usr/bin/env python3
"""Pinned provenance and exact diagnostics for the original arithmetic seeds.

The TeX proves the Lie-group theorem.  Diagnostics independently check
its signed gap, all-rank bounds, and projection/convolution conventions;
they do not replace the analytic proof or assert a Lean build.
"""
from __future__ import annotations

import argparse
from collections import deque
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s

import check_global_norm_frontier_off_diagonal as provenance

ROOT = Path(__file__).resolve().parents[1]
STEM = "global-norm-frontier-seed-decay"
H = "Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals."
SOURCES = [
    (H+"HidaSetting", [(132, 156), (185, 200), (275, 321)]),
    (H+"ProjRows", [(108, 120)]),
    (H+"WuDecay", [(18, 43)]),
    (H+"ConcreteSettingExists", [(13, 19)]),
    ("Formalism.PeriodIntegrals.BesselPeriodGGP", [(20, 53)]),
    ("Formalism.PeriodIntegrals.UpqRep", [(296, 331)]),
    ("Formalism.HermitianCurvature.BesselNonvanishingReduction", [(22, 34)]),
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.FlagStabilizerTensors."
     "RootLatticeThresholds.WuDecayAll", [(42, 75), (95, 138)]),
]
DEPENDENCIES = [
    "paper/shared/global-norm-frontier-pieri-family.tex",
    "paper/shared/global-norm-frontier-pieri-family-references.tex",
    "paper/shared/global-norm-frontier-quotient-mass.tex",
    "scripts/check_global_norm_frontier_off_diagonal.py",
]
REFERENCES = [
    ("yamashita-associated-varieties-1993.pdf",
     "https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/0826-03.pdf",
     "6997c06da7adec75c7e3fa1f2f296cfa86b566cd46013725b12c14f61d719123",
     "Proposition 2.1(a), printed page 31: lowest compact type has multiplicity one; compact central extension explained in the proof."),
    ("harris-kobayashi-speh-2025.pdf",
     "https://www.ms.u-tokyo.ac.jp/~toshi/texpdf/tk2025l-HKS_250921.pdf",
     "be28805b969fa0bb72fddd253d9b33afd9734bd2c3242dbcb9d37df9b88067be",
     "Definition 2.7 and formula (2.24): actual U(p,q) minimal compact-type parameter; previously authenticated signed tensor theorem."),
    ("jiang-sun-zhu-bessel-v2.pdf", "https://arxiv.org/pdf/0908.1728v2",
     "4eb27d5be576b980cf6fd49bc59df7c0a961f465f26299b314e608fa97d1c36b",
     "Theorem A, exact generic Bessel subgroup and irreducible compact target, as checked in the established Pieri package."),
    ("bernstein-krotz-2014.pdf",
     "https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/Bern-Kroetz-2014.pdf",
     "afa09e43f1bc8c6e5323da3a23c34735d9972434d370922c951cd8bb5dcce695",
     "Smooth admissible globalization; previously authenticated primary reference."),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def budgets():
    z = s.symbols("z", integer=True, nonnegative=True)
    n = z+1801
    polynomials = {
        "first_gap_budget": s.expand(79*n**5-(24*n**5+48*n**4+4*n**2+3)),
        "second_gap_budget": s.expand(79*n**5-(9*n**3+12*n**2+3)),
        "reserve_dominates_gap_budgets": s.expand(2*n**6-79*n**5),
        "weighted_Haar_reserve": s.expand(2*n**6-1-4*n**3-4*n**2),
        "cubic_gap": s.expand(16*n**4-120),
    }
    out = {}
    for name, p in polynomials.items():
        coeffs = s.Poly(p, z).all_coeffs()
        assert all(c >= 0 for c in coeffs) and p.subs(z, 0) > 0
        out[name] = {"degree": int(s.degree(p, z)),
                     "nonnegative_coefficients": [str(c) for c in coeffs]}
    p, q, i = s.symbols("p q i", integer=True, positive=True)
    assert s.simplify(2*s.summation(p+q-2*i+1, (i, 1, q))-2*p*q) == 0
    return {"all_rank_certificates": out, "Cartan_density_sum": "2 sum_i(n-2i+1) = 2pq"}


def signed_gaps():
    count = 0
    for k in (1, 2, 4, 9, 17):
        for r in range(8):
            h = 16*(2*r+k+1)**19
            tail = [-j*h for j in range(2*r+2)]
            vals = list(range(k-1, 0, -1))+tail
            signs = [True]*(k-1)+[j % 2 == 0 for j in range(2*r+2)]
            assert all(vals[j] > vals[j+1] for j in range(len(vals)-1))
            for a, b in itertools.combinations(range(len(vals)), 2):
                if signs[a] != signs[b]:
                    assert abs(vals[a]-vals[b]) >= h
                    count += 1
    return {"opposite_sign_pairs_checked": count, "signature_cases": 40,
            "proof_not_replaced_by_samples": True}


def group_diagnostics():
    """Exact induced-model checks on D3=S3, with both characters of C2."""
    group = list(itertools.product(range(3), range(2)))
    ident = (0, 0)
    def mul(g, h):
        return ((g[0]+(-1)**g[1]*h[0]) % 3, (g[1]+h[1]) % 2)
    def inv(g):
        return next(h for h in group if mul(g, h) == ident)
    a = s.Matrix([[-s.Rational(1, 2), -s.sqrt(3)/2], [s.sqrt(3)/2, -s.Rational(1, 2)]])
    b = s.diag(1, -1)
    rho = {g: a**g[0]*b**g[1] for g in group}
    m = {g: s.simplify(rho[g][0, 0]) for g in group}
    kernel = {g: 2*m[g] for g in group}  # degree 2 for probability Haar
    def conv(f, h):
        return {x: s.simplify(sum(f[t]*h[mul(inv(t), x)] for t in group)/6) for x in group}
    assert conv(kernel, kernel) == kernel
    assert all(kernel[inv(g)] == kernel[g] for g in group)
    corner_count = 0
    for g in group:
        delta = {x: 6*s.Integer(x == g) for x in group}
        assert conv(conv(kernel, delta), kernel) == {x: m[g]*kernel[x] for x in group}
        corner_count += 1
    dist = {ident: 0}
    pending = deque([ident])
    gens = [(1, 0), (2, 0), (0, 1)]
    while pending:
        x = pending.popleft()
        for h in gens:
            y = mul(x, h)
            if y not in dist:
                dist[y] = dist[x]+1
                pending.append(y)
    weight = {g: 2**dist[g] for g in group}
    assert all(weight[mul(g, h)] <= weight[g]*weight[h] for g in group for h in group)
    assert all(weight[inv(g)] == weight[g] for g in group)
    nu = [min(weight[(a, 0)], weight[((-a) % 3, 1)]) for a in range(3)]
    projection_count = majorant_count = 0
    for char in (-1, 1):
        trans = {}
        for g in group:
            mat = s.zeros(3)
            for x in range(3):
                mat[x, ((-1)**g[1]*(x+g[0])) % 3] = char**g[1]
            trans[g] = mat
        proj = sum((kernel[g]*trans[g]/6 for g in group), s.zeros(3))
        assert proj == proj.T and proj**2 == proj and proj.rank() == 1
        for g in group:
            assert proj*trans[g]*proj == m[g]*proj
        f = next(proj[:, j] for j in range(3) if proj[:, j] != s.zeros(3, 1))
        norm2 = s.Rational(1, 3)*sum(v*v for v in f)
        assert norm2 > 0
        projection_count += 1
        for subset in range(1, 8):
            beta = s.Matrix([f[i] if subset & (1 << i) else 0 for i in range(3)])
            mass = sum(f[i]*beta[i] for i in range(3))/3
            if mass == 0:
                continue
            assert proj*beta == mass/norm2*f
            for exponent in range(7):
                left = mass/norm2*sum(nu[i]**exponent*abs(f[i]) for i in range(3))/3
                middle = sum(nu[i]**exponent*abs(kernel[g])*
                             abs((trans[g]*beta)[i]) for i in range(3) for g in group)/18
                right = (sum(nu[i]**exponent*abs(beta[i]) for i in range(3))/3)*(
                    sum(abs(kernel[g])*weight[g]**exponent for g in group)/6)
                assert left <= middle <= right
                majorant_count += 1
    return {"nonabelian_group_order": 6, "exact_coefficient_corner_identities": corner_count,
            "induced_rank_one_models": projection_count,
            "exact_weighted_Tonelli_majorants": majorant_count,
            "Haar_normalizations": "group 1/6, subgroup 1/2, quotient 1/3, formal degree 2"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    provenance.SOURCES = SOURCES
    sources = provenance.source_records(args.offline)
    refs = []
    for filename, url, digest, scope in REFERENCES:
        path = ROOT/"build/reference-cache"/filename
        assert path.exists(), f"Missing previously read primary reference: {path}"
        assert sha(path.read_bytes()) == digest
        refs.append({"file": str(path.relative_to(ROOT)), "url": url, "sha256": digest, "scope": scope})
    checks = {"budgets": budgets(), "signed_gaps": signed_gaps(), "convolution": group_diagnostics()}
    files = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", f"scripts/check_{STEM.replace('-', '_')}.py"]
    cert = {
        "status": "PASS", "classification": "closed supplier, independent mathematical review recorded separately",
        "claim": "Original WuDecay and coefficient integrability for every existing HidaSetting under its exact GapHyp",
        "source_commit": provenance.REV, "sources": sources, "primary_references": refs, "checks": checks,
        "files": [{"path": p, "sha256": sha((ROOT/p).read_bytes())} for p in files],
        "established_mathematical_dependencies": [{"path": p, "sha256": sha((ROOT/p).read_bytes())} for p in DEPENDENCIES],
        "retained_hypotheses": ["actual existing HidaSetting, including unit quotient L2 norm and exact coefficient reproduction",
            "n>=1801 and every original adjacent tail gap >=16 n^19",
            "all arithmetic words, original generic characters and irreducible compact types",
            "exact formal degrees, original real Haar measures and Weil quotient measures",
            "original N1=4 n^2 sqrt(2 max q_v)",
            "finiteness constants may depend on the full arithmetic setting"],
        "not_claimed": ["construction or nonvanishing of an arithmetic setting",
            "uniform weighted-L1, compact-reproducer or return bound", "absolute global rational-return summation without its separate arithmetic folding proof",
            "actual mass-row identity", "completion of W06 or W08", "a Lean build",
            "finite diagnostics as an all-rank analytic proof"],
    }
    (ROOT/"certificates"/(STEM+".json")).write_text(json.dumps(cert, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources), "primary_references": len(refs),
                      "signed_gap_pairs": checks["signed_gaps"]["opposite_sign_pairs_checked"],
                      **checks["convolution"]}))


if __name__ == "__main__":
    main()
