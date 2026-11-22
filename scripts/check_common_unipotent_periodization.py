#!/usr/bin/env python3
"""Exact supplementary checks for the common-unipotent period reduction.

The general group, measure and convergence proofs are in the note.
Finite groups check quotient conventions and every orbital contribution;
they are not models for the unsupplied arithmetic norm estimate.
"""

from fractions import Fraction
import gzip
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NOTE = "notes/common-unipotent-periodization.md"
OUT = "certificates/common-unipotent-periodization.json"
SOURCES = [
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals.HidaSetting",
     "20d8b16845b77d6f9cfd258f54474e742eefb34b6db851f1ee4f6617f2f30350",
     [[24, 46], [59, 66], [106, 115], [136, 156], [207, 231],
      [267, 317], [338, 347]]),
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals.PoincareInHH",
     "aefc3163325ffcdb11603f7244f4449ebde4087a698c4553c6ba4b4d52e645e1",
     [[60, 75], [144, 199], [248, 263]]),
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals.PoincareSeriesSquareIntegrable",
     "7f36e2d9043e37d10a3281c2a102ba106e107aabf56516363fe639e57fa0f08d",
     [[15, 25], [50, 81]]),
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.FlagStabilizerTensors.PoincareConstantEq",
     "0c8d01b4349c6ef30f3e4b9196c98fc05d9c042e593f727bb0bbd1a50990fee0",
     [[50, 59]]),
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.FlagStabilizerTensors.ParametersTermRelations",
     "b47b7ccfb755e3b3e013592e6897866d52c357d7f86033ccea4923bbaeee31e7",
     [[38, 75], [213, 255], [286, 294], [319, 342]]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.AdmissibleBoundsFromSource",
     "fdd8922dcd54badfe1a700feba89a02a8359c1bc93f839283c278f5b146b3cb8",
     [[212, 244]]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, expected, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        path = ROOT / "build/source-cache/jsmorph/rh" / REV / rel
        data = path.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert sha(data) == expected and blob == blobs[module], module
        lines = data.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            excerpt = b"\n".join(lines[lo - 1:hi]) + b"\n"
            excerpts.append({"lines": [lo, hi], "sha256": sha(excerpt)})
        records.append({"module": module, "path": rel, "sha256": expected,
                        "git_blob_sha1": blob, "bytes": len(data),
                        "line_count": len(lines), "inspected_excerpts": excerpts})
    return records, sha(packed)


def exact_geometry():
    x, y, a, b, t = sp.symbols("x y a b t", real=True)
    eta, z = x + sp.I*y, a + sp.I*b
    # Basis (e,w,f), h(w,w)=-1, h(e,f)=1.
    H = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
    U = sp.Matrix([[1, sp.conjugate(eta), (x*x+y*y)/2],
                   [0, 1, eta], [0, 0, 1]])
    E, Z = sp.Matrix([1, 0, 0]), sp.Matrix([0, z, 0])
    assert sp.simplify(U.conjugate().T*H*U-H) == sp.zeros(3)
    assert U*E == E
    assert (U*Z-Z)[1:] == [0, 0]
    # The last simple-root coefficient is -h(eta*w,z*w).
    assert sp.expand((U*Z)[0] - sp.conjugate(eta)*z) == 0
    O = sp.Matrix([[1, 0, 0], [0, 1, 0], [sp.I*t, 0, 1]])
    assert sp.simplify(O.conjugate().T*H*O-H) == sp.zeros(3)
    assert O*E-E == sp.Matrix([0, 0, sp.I*t])
    s = sp.symbols("s", real=True)
    assert sp.simplify(O.subs(t, t)*O.subs(t, s)-O.subs(t, t+s)) == sp.zeros(3)
    c, scale = sp.symbols("c scale", positive=True)
    assert sp.simplify((1/sp.sqrt(scale))/sp.sqrt(c/scale)-1/sp.sqrt(c)) == 0
    assert sp.simplify(scale*(1/sp.sqrt(scale))**2-1) == 0
    return {"symbolic_identities": 9,
            "scope": "Unitary and opposite-root formulas; character coordinate and exact Haar scaling."}


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a):
    return tuple(a.index(i) for i in range(len(a)))


def left_reps(group, subgroup):
    unseen, reps = set(group), []
    while unseen:
        g = min(unseen)
        reps.append(g)
        unseen -= {compose(h, g) for h in subgroup}
    return reps


def double_reps(group, left, right):
    unseen, reps = set(group), []
    while unseen:
        g = min(unseen)
        reps.append(g)
        unseen -= {compose(compose(a, g), b) for a in left for b in right}
    return reps


def finite_quotients():
    G = list(itertools.permutations(range(4)))
    ident = (0, 1, 2, 3)
    Gamma = [g for g in G if g[3] == 3]
    swap = (1, 0, 2, 3)
    cycle = (1, 2, 0, 3)
    subgroups = [[ident, swap], [ident, cycle, compose(cycle, cycle)], [ident]]
    Y = left_reps(G, Gamma)
    assert len(Y) == 4
    square_roots = [1, 2, 3]
    source_dims = [2, 1, 2]
    seeds, periods, cover_indices = [], [], []
    for u, Delta in enumerate(subgroups):
        X = left_reps(G, Delta)
        fibre = left_reps(Gamma, Delta)
        cover_indices.append(len(fibre))
        coset_number = {compose(d, r): j for j, r in enumerate(X) for d in Delta}
        word_seeds, word_periods = [], []
        for col in range(source_dims[u]):
            vals = {g: sp.Integer((coset_number[g]+1)*(u+1))
                       + sp.I*((coset_number[g]+col+2) % 5-2) for g in G}
            for d in Delta:
                assert all(vals[compose(d, g)] == vals[g] for g in G)
            lhs = sum(sp.expand_complex(vals[g]*sp.conjugate(vals[g])) for g in X)
            rhs = sum(sp.expand_complex(vals[compose(d, y)]*sp.conjugate(vals[compose(d, y)]))
                      for y in Y for d in fibre)
            assert sp.expand(lhs-rhs) == 0
            word_seeds.append(vals)
            word_periods.append([sum(vals[compose(d, y)] for d in fibre) for y in Y])
        seeds.append(word_seeds)
        periods.append(word_periods)

    orbital_checks, orbital_terms = 0, 0
    for u, Du in enumerate(subgroups):
        for v, Dv in enumerate(subgroups):
            doubles = double_reps(Gamma, Du, Dv)
            for i, fu in enumerate(seeds[u]):
                for j, fv in enumerate(seeds[v]):
                    lhs = sum(periods[u][i][k]*sp.conjugate(periods[v][j][k]) for k in range(len(Y)))
                    rhs = 0
                    for g in doubles:
                        conjugate = {compose(compose(g, d), inverse(g)) for d in Dv}
                        intersection = [d for d in Du if d in conjugate]
                        rhs += sum(fu[x]*sp.conjugate(fv[compose(inverse(g), x)])
                                   for x in left_reps(G, intersection))
                        orbital_terms += 1
                    assert sp.expand_complex(lhs-rhs).expand() == 0
                    orbital_checks += 1

    # The pullback norm is exactly the covering index, with no renormalization.
    base = {g: j+1 for j, r in enumerate(Y) for g in [compose(h, r) for h in Gamma]}
    for Delta, index in zip(subgroups, cover_indices):
        assert sum(base[g]**2 for g in left_reps(G, Delta)) == index*sum(base[g]**2 for g in Y)

    # Common packet matrix, exact positive normalizers, and actual-form cuts.
    columns = [sp.Matrix([x/square_roots[u] for x in p])
               for u in range(len(subgroups)) for p in periods[u]]
    S = sp.Matrix.hstack(*columns)
    J0 = sp.Matrix([[sp.Rational(3, 5)], [sp.Rational(4, 5)]])
    J = sp.diag(J0, sp.ones(1), sp.eye(2))
    assert J.conjugate().T*J == sp.eye(4)
    Pi = sp.diag(1, 0, 1, 1)
    S0 = Pi*S*J
    JJ = J*J.conjugate().T
    Q0 = S0*S0.conjugate().T
    assert sp.simplify(Q0-Pi*S*JJ*S.conjugate().T*Pi) == sp.zeros(4)
    assert sp.simplify(Q0.trace()-(S0.conjugate().T*S0).trace()) == 0
    # The weighted fibre inequality is checked with cancellation still present.
    weighted_checks = 0
    for y in Y:
        vector = [seeds[u][0][compose(d, y)]/square_roots[u]
                  for u, Delta in enumerate(subgroups) for d in left_reps(Gamma, Delta)]
        weights = [sp.Integer(i % 3+1) for i in range(len(vector))]
        L = sum(weights)
        lhs = L*sum(z*sp.conjugate(z)/w for z, w in zip(vector, weights))
        lhs -= sum(vector)*sp.conjugate(sum(vector))
        rhs = sum(weights[i]*weights[j]*(vector[i]/weights[i]-vector[j]/weights[j])
                  *sp.conjugate(vector[i]/weights[i]-vector[j]/weights[j])
                  for i in range(len(vector)) for j in range(i))
        assert sp.expand_complex(lhs-rhs).expand() == 0
        assert sp.expand_complex(lhs).expand() >= 0
        weighted_checks += 1
    return {"ambient_group": "S4", "arithmetic_subgroup": "S3", "target_cosets": len(Y),
            "word_cover_indices": cover_indices, "seed_columns": sum(source_dims),
            "double_coset_inner_products": orbital_checks, "orbital_terms_retained": orbital_terms,
            "weighted_fibre_checks": weighted_checks,
            "normalizers": [r*r for r in square_roots],
            "restricted_trace_exact": str(sp.simplify(Q0.trace()))}


def spectral_checks():
    cases = [[0, 0, 3], [1, 1, 1], [0, 2, 3, 7], [1, 4]]
    records = []
    for vals in cases:
        n, mass, alpha = len(vals), sum(vals), max(vals)
        mean = Fraction(mass, n)
        beta = sum(max(Fraction(v)-mean, 0) for v in vals)/mass
        epsilon = Fraction(alpha*n, mass)-1
        assert beta <= epsilon/(1+epsilon)
        for v in vals:
            assert max(Fraction(v)-mean, 0) <= (1-mean/alpha)*v
        records.append({"spectrum": vals, "positive_trace_fraction": str(beta),
                        "upper_bound": str(epsilon/(1+epsilon))})
    return records


def main():
    sources, atlas_hash = source_records()
    report = {
        "schema_version": 1,
        "status": "PASS",
        "repository": "jsmorph/rh",
        "commit": REV,
        "scope": "Pinned provenance and exact supplementary algebra/finite quotient checks only; no arithmetic norm estimate or Lean replay.",
        "independent_mathematical_reviews": "Recorded separately by the project continuation review; not asserted by this script.",
        "source_inventory_sha256": atlas_hash,
        "sources": sources,
        "exact_geometry": exact_geometry(),
        "finite_quotients": finite_quotients(),
        "spectral_checks": spectral_checks(),
        "primary_reference_read": {
            "author": "Brian Conrad", "title": "A lattice in the adele ring",
            "url": "https://virtualmath1.stanford.edu/~conrad/248APage/handouts/adelelattice.pdf",
            "location": "Section 2, Theorem 2.0.1 and Remark 2.0.2",
            "scope": "Manually inspected primary statement of compactness of the additive adelic quotient; not authenticated by this script."
        },
        "artifacts": {NOTE: sha((ROOT/NOTE).read_bytes()),
                      "scripts/check_common_unipotent_periodization.py": sha(Path(__file__).read_bytes())},
        "unproved": ["Calibrated arithmetic periodization bound on the actual finite seed spaces",
                     "Integral period-map construction and arithmetic height bounds",
                     "Any RH or GRH node completion"]
    }
    (ROOT/OUT).write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": report["status"], "source_files": len(sources),
                      "source_excerpts": sum(len(x["inspected_excerpts"]) for x in sources),
                      "exact_geometry": report["exact_geometry"],
                      "finite_quotients": report["finite_quotients"], "certificate": OUT}, indent=2))


if __name__ == "__main__":
    main()
