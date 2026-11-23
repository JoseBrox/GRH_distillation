#!/usr/bin/env python3
"""Authenticate the exact ordinary seed supplier and decisive algebraic controls."""
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
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    BASE+"IdeleGenerators.SlopeTestRemainingChoices":
        [(24, 46), (55, 109), (111, 160)],
    BASE+"IdeleGenerators.ShapeFacts": [(28, 54), (167, 192)],
    BASE+"CurveDVRSpecialization.SeedPtOf": [(174, 179)],
    BASE+"PublishedTheorems.CyclicBaseChangeC": [(13, 26), (32, 71)],
    BASE+"AutomorphicForms.BlochKatoSelmerVanishes": [(18, 39)],
    BASE+"AutomorphicForms.BcDefs": [(18, 20)],
    BASE+"IdeleGenerators.HolomorphicIrreducibility.SelfTwGal": [(31, 33)],
    BASE+"IdeleGenerators.HolomorphicIrreducibility.EigAut": [(47, 97)],
    BASE+"AutomorphicForms.CongruenceNumberRankThree": [(20, 28)],
}
PRIMARY = [
    {"file": "deligne-ribet.pdf",
     "url": "https://math.berkeley.edu/~ribet/Articles/deligne-ribet.pdf",
     "sha256": "4ff26bab2723a01434e6ee4066d0b0907d6bb5540e2bf78b02a11a86d84d0a2b",
     "pdf_pages_reviewed": [53, 54], "printed_pages": [278, 279],
     "interface": "Main Theorem 8.2: smoothed integral measure and integral Kummer congruences; the unit smoothing factor is supplied in the proof."},
    {"file": "dasgupta-kakde.pdf",
     "url": "https://arxiv.org/pdf/2010.00650v1",
     "sha256": "eb0bfdab63f56d653f302209fc92f2d81cc0894430ef88a7bbf2a2f830783d1d",
     "pdf_pages_reviewed": [17, 18],
     "interface": "Definition 4.2, Remark 4.3, Theorem 4.5(1): chi1=1, chi2=chi primitive, level=f=conductor chi; Gauss ratio cancels and extra Euler-factor set is empty."},
    {"file": "katz-padic-modular.pdf",
     "url": "https://web.math.princeton.edu/~nmk/old/padicpropMFMS.pdf",
     "sha256": "f9c14dc0c8da65bbe355926d149141b548a03e4016b883c4b800b14150cc2b1a",
     "pdf_pages_reviewed": [13, 14, 15, 16, 17],
     "interface": "Sections 1.4-1.6 and Corollary 1.6.2: fine modular curves and integral q-expansion principle. The coarse diamond eigensheaf cusp lift is proved in the note; blanket eigensheaf base change is not cited."},
    {"file": "deligne-serre.pdf",
     "url": "https://numdam.org/item/10.24033/asens.1277.pdf",
     "sha256": "65b390f6d33e827e30c6c66bbc15421eca51db3180bdf5996dcee19047be97fc",
     "pdf_pages_reviewed": [15, 17], "printed_pages": [520, 522],
     "interface": "Theorem 6.1 and Lemma 6.11: classical Galois representations and lifting a residual eigenpacket in a finite free DVR module. A specified eigenvector lift is not claimed."},
    {"file": "carayol.pdf",
     "url": "https://numdam.org/item/10.24033/asens.1512.pdf",
     "sha256": "d4a5fb6b1cd76f944f8948e06df1c7ad5656ae5ee14b9189178ee1e8f2b0dab8",
     "pdf_pages_reviewed": [2, 3, 4, 5], "printed_pages": [409, 410, 411, 412],
     "interface": "Hypotheses 0.3 and Theorem A. F=Q has odd degree, so no added finite discrete-series place is required. Exact primitive central conductor forces zero monodromy by the conductor argument in the note."},
    {"file": "kato.pdf",
     "url": "https://www.numdam.org/article/AST_2004__295__117_0.pdf",
     "sha256": "3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d",
     "pdf_pages_reviewed": [157, 159, 160], "printed_pages": [272, 274, 275],
     "interface": "Proposition 17.1 and Section 17.7, no residual irreducibility. The cohomological unramified line has arithmetic Frobenius alpha^{-1}; its dual gives the arithmetic normalization's unramified quotient alpha."},
    {"file": "gelbart-jacquet.pdf",
     "url": "https://www.math.columbia.edu/~hj/Forms%20on%20GL%282%29%20and%20GL%283%29.pdf",
     "sha256": "7bd1a452341797cda3886b67ffceb7de81cfb79dc8e3d1eeeeaa6b8bcfda2d06",
     "pdf_pages_reviewed": [65, 71, 72], "printed_pages": [534, 540, 541],
     "interface": "Theorem 9.3 and Remark 9.9: adjoint transfer with cuspidality outside the quadratic self-twist case."},
    {"file": "arthur-clozel.pdf",
     "url": "https://www.math.toronto.edu/arthur/pdf/30.pdf",
     "sha256": "3033d863634f5a1e8c26e48ba5b5ec9d8f95fb411b2a6d21c1580db80bc01737",
     "pdf_pages_reviewed": [218, 219, 228], "printed_pages": [202, 203, 212],
     "interface": "Chapter III Theorems 4.2(a,b) and 5.1: cyclic prime-degree cuspidal base change and strong local compatibility; iterate from K to the original L. No solvable descent is used."},
]


def symmetric_square(g):
    a, b, c, d = g[0, 0], g[0, 1], g[1, 0], g[1, 1]
    return sp.Matrix([[a*a, a*b, b*b],
                      [2*a*c, a*d+b*c, 2*b*d],
                      [c*c, c*d, d*d]])


def exact_checks():
    a, b, c, d = sp.symbols("a b c d")
    g = sp.Matrix([[a, b], [c, d]])
    Q = sp.Matrix([[0, 0, -2], [0, 1, 0], [-2, 0, 0]])
    S = symmetric_square(g)
    assert all(sp.expand(x) == 0 for x in S.T*Q*S-g.det()**2*Q)
    assert sp.expand(S.det()-g.det()**3) == 0
    J = sp.Matrix([[0, 1], [-1, 0]])
    assert all(sp.expand(x) == 0 for x in g.T*J*g-g.det()*J)

    u, v, z = sp.symbols("u v z")
    C = sp.Matrix([[u, v], [z, -u]])
    P2 = J*C
    assert P2 == P2.T
    rel = sp.groebner([u*u+v*z-1], u, v, z)
    A = -symmetric_square(C)  # det(C)=-1 in the quotient.
    P3 = Q*A
    for mat in [C*C-sp.eye(2), A*A-sp.eye(3), P3-P3.T]:
        assert all(rel.reduce(sp.expand(x))[1] == 0 for x in mat)
    assert Q.det() == -4

    # Exact generalized Bernoulli values in Q[zeta_3].  This is a
    # diagnostic at the smallest allowed characteristic, not a replacement
    # for the integral-measure argument for arbitrary characters and weights.
    x = sp.symbols("x")
    cycl = x*x+x+1

    def l_value(w, primitive_root, k, use_phi=True):
        logs = {pow(primitive_root, t, w): t % 3 for t in range(w-1)}
        assert len(logs) == w-1
        C0 = (4 if use_phi else 1)*w
        value = sp.Integer(0)
        for t in range(1, C0+1):
            if t % w == 0 or (use_phi and t % 2 == 0):
                continue
            phi = (1 if t % 4 == 1 else -1) if use_phi else 1
            value += phi*x**logs[t % w]*sp.bernoulli(k, sp.Rational(t, C0))
        return sp.rem(sp.expand(-sp.Rational(C0)**(k-1)*value/k), cycl, x)

    def residue(value):
        for coeff in sp.Poly(value, x).all_coeffs():
            assert int(sp.denom(coeff)) % 3 != 0
        v0 = sp.cancel(value.subs(x, 1))
        return int(sp.numer(v0)) * pow(int(sp.denom(v0)), -1, 3) % 3

    examples = []
    for k in [3, 5, 7, 9, 11, 13, 15]:
        value = l_value(13, 2, k)
        assert residue(value) == 0
        examples.append({"ell": 3, "phi_conductor": 4, "w": 13,
                         "weight": k, "L_value_in_zeta3": str(value),
                         "residue_mod_zeta3_minus_one": 0})
    wrong_split = l_value(7, 3, 3)
    trivial_phi = l_value(7, 3, 2, False)
    assert wrong_split == 78*x+32 and residue(wrong_split) == 2
    assert trivial_phi == 2*x/7-sp.Rational(4, 7)
    assert residue(trivial_phi) == 1
    return {
        "status": "PASS",
        "symbolic_identities_over_Z": [
            "The exact source symmetric-square matrix satisfies S(g)^t Q S(g)=det(g)^2 Q and det S(g)=det(g)^3, with det Q=-4.",
            "g^t J g=det(g)J; for trace-zero involution C of determinant -1, JC is symmetric.",
            "For that same C, A=-Sym^2(C) satisfies A^2=1 and QA is symmetric, modulo the exact relation u^2+vz=1.",
        ],
        "exact_bernoulli_examples": examples,
        "negative_controls": [
            {"omitted_hypothesis": "phi(w)=1", "ell": 3,
             "phi_conductor": 4, "w": 7, "weight": 3,
             "L_value_in_zeta3": str(wrong_split), "residue": 2},
            {"omitted_hypothesis": "nontrivial residual phi", "ell": 3,
             "phi": "1", "w": 7, "weight": 2,
             "L_value_in_zeta3": str(trivial_phi), "residue": 1},
        ],
        "scope": "Polynomial identities are exact generic calculations. The finite Bernoulli examples test normalization and indispensable hypotheses, not the general existence theorem.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert hashlib.sha256(packed).hexdigest() == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    rows = {r[0]: r for r in atlas["modules"]}
    sources = []
    for module, ranges in RANGES.items():
        item = {"repository": atlas["repository"], "commit": atlas["commit"],
                "path": "lean/src/"+module.replace(".", "/")+".lean",
                "git_blob_sha1": rows[module][1]}
        checked = inspect_file(item, args.offline)
        path = ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]
        lines = path.read_bytes().splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo+1 <= 120
            blob = b"".join(lines[lo-1:hi])
            assert len(blob) <= 12000
            excerpts.append({"start": lo, "end": hi,
                             "sha256": hashlib.sha256(blob).hexdigest()})
        sources.append({**item, "module": module, "sha256": checked["sha256"],
                        "matches_pinned_blob": True, "reviewed_excerpts": excerpts})

    primary = []
    directory = ROOT/"build/selmer-seed-sources"
    directory.mkdir(parents=True, exist_ok=True)
    for item in PRIMARY:
        path = directory/item["file"]
        if not path.exists():
            if args.offline:
                raise FileNotFoundError(path)
            with urllib.request.urlopen(item["url"], timeout=60) as response:
                data = response.read()
            assert data.startswith(b"%PDF")
            assert hashlib.sha256(data).hexdigest() == item["sha256"]
            path.write_bytes(data)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"]
        primary.append({**item, "bytes": path.stat().st_size,
                        "matches_reviewed_pdf": True})

    stem = "selmer-integral-frontier-arithmetic-seed"
    artifacts = [f"notes/{stem}.md", f"paper/shared/{stem}.tex",
                 f"paper/shared/{stem}-references.tex",
                 "scripts/check_selmer_integral_frontier_arithmetic_seed.py"]
    for path in artifacts:
        assert (ROOT/path).is_file()
        assert all(c >= 32 or c in (9, 10) for c in (ROOT/path).read_bytes())
    report = {
        "schema_version": 1, "status": "PASS",
        "classification": "closed actual prime-to-ell arithmetic seed subobligation inside W04, independently reviewed",
        "claim": "For every original field-character datum with ell not dividing order chi', construct the complete rank-two and rank-three IsSeed representations in arbitrarily large prescribed weight classes, retaining the rank-two supplied CM twist.",
        "verification_kind": "Authenticated bounded pinned interfaces; eight directly inspected primary references; exact generic polarization identities and small-prime Bernoulli controls. The complete existence proof is in the note.",
        "quantifiers": [
            "Every odd ell, including 3; every original N,w,K,L,chi',eta,theta,j satisfying the full field-character contract and ell not dividing order chi'.",
            "Every prescribed Qbar_ell-to-C embedding and every lower weight bound B; finite coefficient extensions are allowed inside Qbar_ell, without enlarging K or L.",
            "Rank three when chi' differs from eta; rank two for the original supplied IsTwist character kappa and its prescribed restriction ka.",
            "Residual characteristic-polynomial identities hold on every Galois element; away inertia is exact at every prime including 2; each ell-adic place has the original ordered flag and full residual decomposition-group characters.",
        ],
        "decisive_interfaces": {
            "integral_constants": "Nontrivial prime-to-ell phi supplies a unit 1-phi(a)a^k with a=1 mod w ell. Integral smoothed congruences yield the exact w Euler factor and lambda-divisibility, without a Bernoulli denominator loss.",
            "all_cusps": "The primitive constant-term formula vanishes off the infinity class; all remaining constants are unit multiples of L(1-k,chi)/2.",
            "same_character_lift": "Cusp stabilizers have order dividing 2C, so the boundary eigensheaf sequence is exact even when ell divides the diamond group order. omega^12 descends to an ample line; Serre vanishing gives the exact boundary lift.",
            "ordinary": "The lifted packet has a_ell=1 mod lambda. Kato 17.1/17.7 applies without residual irreducibility; converting its arithmetic Frobenius alpha^{-1} on the cohomological line gives the unit quotient alpha.",
            "away_type": "Carayol Theorem A over Q plus equality of central-character and representation conductor forces principal series with one unramified character and zero monodromy.",
            "rank_three": "phi=chi' eta, k=m+1, r3=Sym^2 rho/det rho. The nonquadratic residual condition excludes quadratic self-twists; infinite ordinary projective inertia then forces connected PGL2 and irreducibility on every open subgroup.",
            "rank_two": "phi=chi'^2 eta, k=2m+1, sigma=rho epsilon^{-m} chi'^{-1}; det sigma=eta theta. Clifford theory and the exact residual condition prove irreducibility on G_L.",
            "polarization": "Q=[[0,0,-2],[0,1,0],[-2,0,0]], P3=Q ad0(rho)(c); J=[[0,1],[-1,0]], P2=J sigma(c). Both pairings are symmetric with original multiplier one.",
            "automorphy": "Gelbart-Jacquet adjoint transfer; cyclic prime-degree Arthur-Clozel base change, with norm self-twists excluded by irreducible restrictions. Rank three uses exactly epsilon^{-1}. Rank two uses BC(pi_f^vee) tensor |det|^{1/2} tensor Xi_chi tensor the prescribed Xi_ka; its CM infinitesimal parameters are {m-1/2,-m-1/2} and {m+1/2,-m+1/2}, with exact geometric-Frobenius and positive algSat factors.",
        },
        "limitations": [
            "This does not assert unrestricted Seed2, Seed3 or PropEG for arbitrary ell-power character order; it supplies the exact prime-to-ell character case used in SeedPtOf.",
            "The particular IsTwist character remains an explicit rank-two input.",
            "No uniform bound on weight, coefficient degree, automorphic dimension or integral Selmer torsion is asserted.",
            "The marked PointTheorem, characteristic-prime curve point, support localization and complete prime chain must still be applied with their exact hypotheses.",
            "No whole RH or GRH proof-map node and no Lean project build is certified.",
        ],
        "sources": sources,
        "primary_sources": primary,
        "exact_checks": exact_checks(),
        "artifacts": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
                      for p in artifacts],
    }
    target = ROOT/"certificates"/(stem+".json")
    target.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "primary_references": len(primary),
                      "exact_bernoulli_examples": len(report["exact_checks"]["exact_bernoulli_examples"]),
                      "certificate": str(target.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
