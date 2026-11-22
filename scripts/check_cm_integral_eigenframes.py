#!/usr/bin/env python3
"""Authenticate bounded CM contracts and check exact trace-dual examples.

The general integral-eigenlattice proof is in the accompanying note. Finite
examples do not construct a CM model, prove a period formula, or run Lean.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

import sympy as sp

from check_determinant_torsion_rigidity import inspect, digest, LEAN_REV, STACKS_REV

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Development.AutomorphicSpectrum.Proofs."
SOURCES = [
    ("AlgebraProofs.EigenLocalBasisLogNorm", [[38, 80], [174, 226]]),
    ("AlgebraProofs.DifferentTwistedGeneratorExists", [[46, 57]]),
    ("GeometryProofs.CmPackProductFrame", [[27, 42]]),
    ("GeometryProofs.CmPackPureNorm", [[129, 158], [160, 193], [234, 291]]),
    ("GeometryProofs.FrameFunctionCmHeight", [[24, 49], [50, 114]]),
    ("GeometryProofs.FlatDegreeHolds", [[60, 118]]),
]


def exact_projectors():
    """Compare trace-dual and polynomial-division formulas in Q[t]/(P)."""
    x, t = sp.symbols("x t")
    polynomials = [
        x**2 + 1, x**2 - 2, x**2 - x - 1, x**2 + x + 1,
        x**3 - 2, x**3 - x - 1, x**3 + x**2 - 1,
        x**4 + 1, x**4 - x - 1, x**5 - x - 1,
    ]
    rows = []
    for expr in polynomials:
        f = sp.Poly(expr, x, domain=sp.QQ)
        n = f.degree()
        assert f.is_irreducible
        ft = sp.Poly(f.as_expr().subs(x, t), t, domain=sp.QQ)

        def rem(expr):
            return sp.rem(sp.Poly(sp.expand(expr), t, domain=sp.QQ), ft).as_expr()

        C = sp.Matrix(n, n, lambda i, j:
                      sp.rem(sp.Poly(x**(j+1), x), f).nth(i))
        G = sp.Matrix(n, n, lambda i, j: sp.trace(C**(i+j)))
        assert G.det() == sp.discriminant(f.as_expr(), x) != 0
        dual = G.inv()
        e = sp.Matrix([sum(dual[j, i]*t**j for j in range(n))
                       for i in range(n)])
        assert (C*e - t*e).applyfunc(rem) == sp.zeros(n, 1)
        E = sp.zeros(n)
        for i in range(n):
            E += e[i]*C**i
        E = E.applyfunc(rem)
        assert (E*E-E).applyfunc(rem) == sp.zeros(n)
        assert rem(sp.trace(E)) == 1
        quotient, remainder = sp.div(f.as_expr()-f.as_expr().subs(x, t), x-t, x)
        assert sp.expand(remainder) == 0
        v = sp.Matrix([sp.expand(quotient).coeff(x, i) for i in range(n)])
        derivative = sp.diff(f.as_expr(), x).subs(x, t)
        assert (derivative*e-v).applyfunc(rem) == sp.zeros(n, 1)
        assert v[n-1] == 1
        assert all(sp.Poly(a, t).domain == sp.ZZ for a in v)
        rows.append({"polynomial": str(f.as_expr()), "degree": n,
                     "discriminant": str(G.det()),
                     "ramified_rational_primes": sorted(sp.factorint(abs(int(G.det())))),
                     "trace_dual_projection": True, "idempotent_trace_one": True,
                     "derivative_scaled_primitive_vector": True})
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert digest(packed) == inventory["compressed_graph"]["sha256"]
    graph = json.loads(gzip.decompress(packed))
    assert graph["repository"] == "jsmorph/rh" and graph["commit"] == LEAN_REV
    blobs = {a[0]: a[1] for a in graph["modules"]}
    sources = []
    for suffix, ranges in SOURCES:
        module = PREFIX + suffix
        sources.append(inspect("jsmorph/rh", LEAN_REV,
                               "lean/src/" + module.replace(".", "/") + ".lean",
                               blobs[module], ranges, args.offline))
    sources.append(inspect("stacks/stacks-project", STACKS_REV, "discriminant.tex",
                           "4f85f71aafcf602e18d0f665bbcb79064d1f8026",
                           [[1417, 1438], [1477, 1494]], args.offline))
    examples = exact_projectors()
    t, y = sp.symbols("t y")
    cyclo = sp.Poly(t**4+1, t)
    bar_t = sp.invert(t, cyclo.as_expr())
    unit = sp.rem(bar_t*sp.invert(t, cyclo.as_expr()), cyclo.as_expr(), t)
    assert unit == -t**2
    assert sp.rem(unit*(-unit)-1, cyclo.as_expr(), t) == 0
    assert (2*t)*(2*t**2) == 4*t**3
    absolute_disc = int(sp.discriminant(cyclo.as_expr(), t))
    real_disc = int(sp.discriminant(y**2-2, y))
    assert absolute_disc == 256 and real_disc == 8
    assert absolute_disc // real_disc**2 == 4
    shifted = sp.Poly((t+1)**4+1, t)
    assert all(int(shifted.nth(i)) % 2 == 0 for i in range(4))
    assert int(shifted.nth(0)) % 4 != 0
    paths = ["notes/cm-integral-eigenframes.md",
             "scripts/check_cm_integral_eigenframes.py",
             "scripts/check_determinant_torsion_rigidity.py"]
    result = {
        "schema_version": 1, "result": "PASS",
        "scope": "Immutable source provenance and exact algebra examples; the universal proof and geometric hypotheses are separate.",
        "written_results": [
            "The exact integral character line is the relative different times the generic primitive idempotent.",
            "Conjugation invariance and a semilocal generator give equal conjugate finite norms without finite unramifiedness of E/E+.",
            "Regular integral product blocks give the prescribed different-scaled CM eigenframes.",
        ],
        "sources": sources, "exact_examples": examples,
        "ramified_cm_example": {
            "field": "Q(zeta_8)", "quadratic_subfield": "Q(i)",
            "relative_different_generator": "2*zeta_8",
            "conjugate_generator_ratio": "-i",
            "absolute_discriminant": absolute_disc,
            "real_subfield_discriminant": real_disc,
            "relative_real_discriminant_norm": absolute_disc // real_disc**2,
            "maximality_at_two": "The polynomial of zeta_8-1 is Eisenstein; other primes do not divide the order discriminant.",
            "scope": "Local algebra example only; not an admissible replacement for the prescribed host."
        },
        "example_scope": "Polynomial identities hold for the indicated monogenic orders. Maximality at every prime is not asserted or needed for these identity checks.",
        "artifacts": [{"path": p, "sha256": digest((ROOT/p).read_bytes())} for p in paths],
        "independent_review_record": "certificates/hard-node-review-2026-11-22.json",
        "limits": [
            "The actual integral product frame, original CM point and archimedean period evaluation remain model inputs.",
            "Removing unramifiedness from this local algebra lemma removes no separate global host condition.",
            "No Lean kernel rebuild is performed.",
        ],
    }
    out = ROOT / "certificates/cm-integral-eigenframes.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "sources": len(sources),
                      "exact_polynomial_examples": len(examples),
                      "certificate": str(out.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
