#!/usr/bin/env python3
"""Authenticate the actual GalOut supplier and its infinitesimal algebra."""
from __future__ import annotations
import argparse
import gzip
import hashlib
import itertools
import json
import random
from pathlib import Path
from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
P = BASE+"PatchingModules."
S = P+"SelmerScaling."
RANGES = {
    P+"PatchedSupportCompletions": [(72, 101), (112, 157)],
    P+"PairedDualFirstOrderDualMatrixSpace": [(119, 184), (192, 274), (306, 357)],
    S+"SelmerSpannedByKappaLaurent": [(9, 50), (54, 96), (119, 171)],
    S+"OoExKer": [(106, 195)],
    S+"LocLemma": [(225, 307), (308, 356)],
    S+"LowerEntriesZeroOfCommutingTriangular": [(6, 73)],
    S+"OddDiag": [(5, 90)],
    S+"ConjConst": [(94, 203), (204, 293)],
    S+"LaInj": [(6, 82)],
    S+"InvEv": [(4, 82)],
    S+"DualEx": [(9, 92), (94, 134)],
    S+"TpDual": [(28, 108)],
    S+"PhDecDApply": [(6, 88)],
    S+"TestEx": [(46, 112)],
    S+"DefUTest": [(34, 112)],
    S+"DefULift": [(244, 327)],
    S+"DefUPush": [(11, 45)],
    S+"Claim2": [(11, 33)],
    S+"FirstOrderMatrixMemSquareZero": [(279, 388)],
    S+"FirstOrderLiftConstantPart": [(134, 244)],
    S+"AlCSmul": [(12, 80), (81, 147)],
    S+"SelmerRankBoundLaurent": [(47, 93)],
    S+"EvenCocyclesLiftLaurent": [(7, 38)],
    S+"SelmerSpannedByKappaLaurentAlt": [(6, 49)],
    S+"DiscImp": [(1, 10)],
    P+"AutomorphicDetection.GalOut": [(16, 48)],
}
DEPENDENCIES = [
    "notes/selmer-integral-frontier-polarized-model.md",
    "notes/selmer-integral-frontier-limit-comparison.md",
    "notes/selmer-integral-frontier-padded-relations.md",
    "notes/selmer-integral-frontier-incidence.md",
]


def dd_mul(x, y, modulus=None):
    a, e, f, h = x
    b, u, v, k = y
    ans = (a*b, tuple(a*j+i*b for i, j in zip(e, u)),
           tuple(a*j+i*b for i, j in zip(f, v)),
           a*k+h*b+sum(i*j+p*q for i, j, p, q in zip(e, v, f, u)))
    if modulus is None:
        return ans
    return (ans[0] % modulus, tuple(v % modulus for v in ans[1]),
            tuple(v % modulus for v in ans[2]), ans[3] % modulus)


def exact_checks():
    basis_triples = 0
    for g in (0, 1, 2, 3):
        basis = []
        for j in range(2+2*g):
            z = [int(i == j) for i in range(2+2*g)]
            basis.append((z[0], tuple(z[1:1+g]),
                          tuple(z[1+g:1+2*g]), z[-1]))
        one = (1, (0,)*g, (0,)*g, 0)
        for x in basis:
            assert dd_mul(one, x) == x
        for x, y in itertools.product(basis, repeat=2):
            assert dd_mul(x, y) == dd_mul(y, x)
        for x, y, z in itertools.product(basis, repeat=3):
            assert dd_mul(dd_mul(x, y), z) == dd_mul(x, dd_mul(y, z))
            basis_triples += 1
    # Full test-map check over R=F3[x]/x^2, N=R, N^2=0.
    # alpha extracts x in R, mu the constant in N, Phi x in N.
    p = 3
    elems = list(itertools.product(range(p), repeat=4))
    def theta(x):
        r0, r1, n0, n1 = x
        return r0, (n0,), (r1,), n1
    def mul(x, y):
        r0, r1, n0, n1 = x
        s0, s1, m0, m1 = y
        return (r0*s0 % p, (r0*s1+r1*s0) % p,
                (r0*m0+s0*n0) % p,
                (r0*m1+r1*m0+s0*n1+s1*n0) % p)
    for x, y in itertools.product(elems, repeat=2):
        assert theta(mul(x, y)) == dd_mul(theta(x), theta(y), p)
    # Rank-deficient rectangular correspondence, not an asserted ring map.
    c = [[1, 0, 1], [0, 0, 0]]
    e, g, p = 2, 3, 5
    rng = random.Random(20261123)
    def paired():
        a, h = rng.randrange(p), rng.randrange(p)
        v = [rng.randrange(p) for _ in range(g)]
        u = [rng.randrange(p) for _ in range(e)]
        old = (a, tuple(sum(c[i][j]*v[j] for j in range(g)) % p for i in range(e)),
               tuple(u), h)
        new = (a, tuple(v),
               tuple(sum(c[i][j]*u[i] for i in range(e)) % p for j in range(g)), h)
        return old, new
    def relation(old, new):
        return (old[0] == new[0] and old[3] == new[3] and
                all(old[1][i] == sum(c[i][j]*new[1][j] for j in range(g)) % p
                    for i in range(e)) and
                all(new[2][j] == sum(c[i][j]*old[2][i] for i in range(e)) % p
                    for j in range(g)))
    for _ in range(200):
        x, xx = paired()
        y, yy = paired()
        assert relation(dd_mul(x, y, p), dd_mul(xx, yy, p))
    # Three distinct characters of C2 x C2. No group element separates
    # them; g1+2g2 does, over F5.
    vals = [(1, (-1)**a, (-1)**b)
            for a, b in itertools.product(range(2), repeat=2)]
    assert all(len(set(v)) < 3 for v in vals)
    separating = tuple((vals[2][i]+2*vals[1][i]) % 5 for i in range(3))
    assert len(set(separating)) == 3
    # The ordered product alone does not force multiplicity one:
    # sigma=chi_1 Id also satisfies it. The source's prescribed residual
    # flag, kept explicitly in the theorem, is therefore necessary.
    return {
        "status": "PASS",
        "DD_basis_associativity_triples_over_Z": basis_triples,
        "DD_ranks": [0, 1, 2, 3],
        "full_second_order_test_map_pairs_over_F3": len(elems)**2,
        "rank_deficient_rectangular_correspondence_products_over_F5": 200,
        "separating_group_algebra_values_over_F5": separating,
        "negative_controls": [
            "Distinct characters need not be separated by one group element; three characters of C2 x C2 supply a counterexample.",
            "Ordered annihilation alone permits repeated constituents; the prescribed residual flag with each character once is retained.",
            "If two ordinary characters coincide, a nonzero lower matrix can commute with the scalar representation; local lower-entry rigidity needs distinct characters.",
            "Free rank zero ordinary modules have empty support; the theorem does not supply a seed.",
        ],
        "scope": "Exact finite-algebra checks supplement the general proof. They do not certify arithmetic tower existence, support nonvanishing, a uniform integral exponent, or a Lean build.",
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
    stem = "selmer-integral-frontier-local-propagation"
    artifacts = [f"notes/{stem}.md", f"paper/shared/{stem}.tex",
                 f"paper/shared/{stem}-references.tex",
                 "scripts/check_selmer_integral_frontier_local_propagation.py"]
    for path in artifacts+DEPENDENCIES:
        assert (ROOT/path).is_file(), path
        assert all(c >= 32 or c in (9, 10) for c in (ROOT/path).read_bytes())
    report = {
        "schema_version": 1, "status": "PASS",
        "classification": "closed exact GalOut local-propagation subobligation inside W04",
        "claim": "At every original supplied normalized curve, the three exact Selmer conditions imply the complete prime-inclusion GalOut contract through the actual polarized model and integral presentation.",
        "verification_kind": "Authenticated bounded source interfaces, existing theorem dependencies and exact infinitesimal algebra controls; full standard mathematical proof in the note.",
        "quantifiers": [
            "Every original OoPt datum, every odd residue characteristic, and the exact one- or two-block normalized representation.",
            "Every D0 with the original K1(D0), K2 and K3, preserving the original group, primitive modules and ordered local conditions.",
            "Every pair Z,Q of primes in the exact curve-kernel completion, with DiscSt(Z), dim(R/Z)>=1+D0 and DiscSt(Q) or original NonSS(Q).",
            "No assertion that a stable prime Z or a nonzero automorphic support point exists.",
        ],
        "decisive_interfaces": {
            "actual_coefficient_DVR": "O'=completion of O[[s]] at (pi), using the specified original s mapping to t; no perfection or Cohen-section replacement.",
            "bounded_continuity": "B/p^r is finite over O[[s]], by its finite p-adic filtration; m_B=(s)+p gives theta(m_B^j) subset t^(j-r+1) theta(B).",
            "ordinary_local_correction": "One separating group-algebra element gives Lagrange projectors; sum(P_i^1 P_i^0)=1-Y matches flags and preserves the exact parity subalgebra.",
            "even_tangent_injection": "Constancy of the conjugated representation fixes full determinant coefficients, ordered ordinary characters, all U roots, every y parameter and the original s. Exact GenBy plus bounded continuity fixes B and its completion.",
            "odd_tangent_injection": "The exact full block span tests a pure cross-corner entry, retaining all torsion in N.",
            "second_order_supplier": "The explicit DD test map from R direct_sum N uses Phi(rm)-rbar Phi(m). Orthogonal odd conjugation and a rank-deficient rectangular coefficient correspondence preserve every original equation.",
            "first_order_flag_compatibility": "Local discrepancies have upper-triangular coboundary; distinct ordinary characters force upper triangularity. Explicit first-order-flag conjugates correct all directions without dividing by g.",
            "integral_presentation": "K2 gives codim U<=g; K1 and tangent injectivity give dim W+g^2<=D0; K3 supplies N generators. Existing padding and second-order functional separation give the full original Pres.",
            "final_prime_inclusion": "Exact polarized-model DiscSt and NonSS implications feed the established incidence theorem. The one-block case follows from the regular power-series presentation.",
        },
        "limitations": [
            "The original K1/K2/K3 hypotheses remain exactly as in the source; their tower suppliers are separate authenticated prior results.",
            "This theorem does not supply localized patched support, a nonzero automorphic seed, or the global normalized curve chain.",
            "No numerical exponent for integral annihilator torsion or moving-family Selmer budget is inferred.",
            "No whole RH/GRH proof-map node or Lean project build is certified.",
        ],
        "exact_checks": exact_checks(),
        "dependencies": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
                         for p in DEPENDENCIES],
        "sources": sources,
        "artifacts": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
                      for p in artifacts],
    }
    path = ROOT/"certificates"/f"{stem}.json"
    path.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "modules": len(sources),
                      "dependencies": len(DEPENDENCIES),
                      "certificate": str(path.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
