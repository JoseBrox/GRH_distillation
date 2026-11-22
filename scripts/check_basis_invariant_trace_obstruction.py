#!/usr/bin/env python3
"""Exact checks for the basis-invariant square-root trace obstruction.

The universal incidence proof, including every invertible comparison
basis and every linear restriction, is in the note. Finite sparse matrix
checks supplement that proof; they neither establish its quantifiers nor
identify a model with the actual arithmetic period maps. No Lean replay.
"""

from collections import Counter
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NOTE = "notes/basis-invariant-trace-obstruction.md"
OUT = "certificates/basis-invariant-trace-obstruction.json"
SOURCES = [
    ("Formalism.SizeWindowBrackets.TraceSquareAndDiagBounds",
     "f1baa428bebdc0d62dce1f5bf29a4960f26e8ad02ceea3033198b76f752b346f",
     [[20, 42], [64, 78]]),
    ("Formalism.SharpRestriction.GlobalSchurBounds.TopDensityNGeSixteen",
     "f952a3ad11b8a3e5ae77f196fa3c434780eea7db9905f9a6941148d8e2d299b7",
     [[658, 672], [1004, 1066], [1090, 1122]]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.DataS",
     "1077247c0b4ac5977e00b6d234f92e82498ec5f31830504f3251e4117a260849",
     [[33, 48], [50, 84]]),
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals.HidaSetting",
     "20d8b16845b77d6f9cfd258f54474e742eefb34b6db851f1ee4f6617f2f30350",
     [[179, 205], [217, 225], [267, 317]]),
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals.PoincareInHH",
     "aefc3163325ffcdb11603f7244f4449ebde4087a698c4553c6ba4b4d52e645e1",
     [[60, 75], [144, 155], [156, 215], [248, 263]]),
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals.PoincareSeriesSquareIntegrable",
     "7f36e2d9043e37d10a3281c2a102ba106e107aabf56516363fe639e57fa0f08d",
     [[50, 81]]),
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
        if not path.is_file():
            path = ROOT / "build/lean-mirror" / rel
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


def symbolic_checks():
    m, q = sp.symbols("m q", integer=True, positive=True)
    a = m*m + 1
    kp, km = a + m, a - m
    ell = q*(q - 1)
    D, r = 2*q*ell, 2*a*ell
    R = q*r
    delta = m/(2*a)
    eta = m*m/(a*a)
    tau, nu, gap = sp.symbols("tau nu gap", real=True)
    p = kp/(2*a)
    claims = {
        "redundancy": R - a*D,
        "pair_double_count": q*(kp*(kp-1) + km*(km-1)) - 2*q*(a*a-1),
        "pair_margin": r*r/D - 2*q*(a*a-1) - 2*(q-a*a),
        "incidence_defect": p - sp.Rational(1, 2) - delta,
        "positive_trace": (D/2)*m/R - delta,
        "variance": D*(D*m*m)/(R*R) - eta,
        "trace_variance_equality": 4*delta*delta - eta,
        "sharp_asymptotic_formula_squared": 4*delta*delta - (D/R)*(1-D/R),
        "basis_whitening_source_defect": q*ell*kp*(1/a - 1/kp)/D - delta,
        "slope_realization": (p-sp.Rational(1, 2))*gap - delta*gap,
        "source_cut_bound": (p-tau)/(1-tau) - sp.Rational(1, 2)
                               - (delta-tau/2)/(1-tau),
        "source_cut_threshold": (2*m*ell)/r - 2*delta,
        "retained_rank": q*(r-2*m*ell) - km*D,
    }
    for name, expression in claims.items():
        assert sp.cancel(expression) == 0, name
    assert sp.limit(m/(2*sp.sqrt(m*m+1)), m, sp.oo) == sp.Rational(1, 2)
    assert sp.cancel(delta/(D/R)) == m/2
    # The retained-rank formula uses an actual count of all remaining
    # source columns, including any columns killed by the target cut.
    return {"identities": list(claims), "limits": 1,
            "unbounded_ratio": "(inf(gamma+beta))/(D/R)=m/2"}


def prime(q):
    return q >= 2 and all(q % j for j in range(2, int(q**0.5) + 1))


def sparse_model(m, q):
    """Store each 0/1 embedding by its column-to-row map, with no floats."""
    a = m*m + 1
    assert m >= 1 and prime(q) and q >= a*a
    kp, km = a+m, a-m
    group = [(u, v) for u in range(1, q) for v in range(q)]
    ell = len(group)
    D, r, R = 2*q*ell, 2*a*ell, 2*q*a*ell
    maps = []
    for i in range(q):
        rows = []
        for g, (u, v) in enumerate(group):
            b = (u*i+v) % q
            for sign, size in enumerate([kp, km]):
                rows.extend((2*g+sign)*q+(s+b) % q for s in range(size))
        assert len(rows) == r and len(set(rows)) == r
        maps.append(rows)
    multiplicity = Counter(row for rows in maps for row in rows)
    assert len(multiplicity) == D
    assert all(multiplicity[row] == (kp if (row//q) % 2 == 0 else km)
               for row in range(D))
    assert sum(multiplicity.values()) == R
    sets = [set(rows) for rows in maps]
    pair_values = [len(sets[i] & sets[j])
                   for i in range(q) for j in range(i)]
    assert all(value == 2*q*(a*a-1) for value in pair_values)
    assert all(value <= F(r*r, D) for value in pair_values)
    beta = sum(max(F(count)-F(R, D), 0) for count in multiplicity.values())/R
    eta = F(D, R*R)*sum((F(count)-F(R, D))**2 for count in multiplicity.values())
    assert beta == F(m, 2*a) and eta == F(m*m, a*a)
    # Exact incidence bound and nonunitary target-balancing alternative.
    k = q*ell*kp
    assert F(k, R)-F(1, 2) == beta
    gamma_after_balancing = F(q*ell*kp, D)*(F(1, a)-F(1, kp))
    assert gamma_after_balancing == beta
    # Trim every plus block to km source coordinates. This is an exact
    # family of retained maps, not an inference from the spectral formula.
    retained = []
    for rows in maps:
        retained.append([row for j, row in enumerate(rows)
                         if j % (2*a) < km or j % (2*a) >= kp])
    counts = Counter(row for rows in retained for row in rows)
    assert len(counts) == D and set(counts.values()) == {km}
    R1 = sum(map(len, retained))
    assert F(R-R1, R) == 2*beta and R1 == km*D
    record = {"m": m, "q": q, "a": a, "D": D, "r": r, "R": R,
              "nonzero_entries": R, "distinct_pairs_checked": len(pair_values),
              "pair_value": pair_values[0], "pair_bound": str(F(r*r, D)),
              "optimal_trace_sum": str(beta), "eta": str(eta),
              "source_cut_fraction_to_balance": str(2*beta),
              "whitened_target_beta": "0",
              "whitened_source_gamma": str(gamma_after_balancing)}
    return record, maps


def restriction_checks():
    record, maps = sparse_model(1, 5)
    D, R, r = record["D"], record["R"], record["r"]
    p = F(3, 4)
    checks = []
    for source_mod in [5, 7, 11, 17]:
        for target_mod in [5, 7, 13]:
            target = {row for row in range(D) if row % target_mod != 0}
            retained = [[row for j, row in enumerate(rows)
                         if (3*j+i) % source_mod != 0]
                        for i, rows in enumerate(maps)]
            Rp, n = sum(map(len, retained)), len(target)
            counts = Counter(row for rows in retained for row in rows if row in target)
            M = sum(counts.values())
            assert M > 0 and Rp > 0 and n > 0
            # Source Gram diagonal entries are 1 for surviving columns
            # and 0 for columns sent to zero by the target projection.
            gamma = F(Rp-M, Rp)
            beta = sum(max(F(counts[row])-F(M, n), 0) for row in target)/M
            tau, nu = F(R-Rp, R), F(n, D)
            bound = max((p-tau)/(1-tau)-min(F(1), F(1, 2)/nu), 0)
            assert gamma+beta >= bound
            checks.append({"source_modulus": source_mod, "target_modulus": target_mod,
                           "tau": str(tau), "nu": str(nu),
                           "gamma_plus_beta": str(gamma+beta), "lower_bound": str(bound)})
    return checks


def main():
    sources, atlas_sha = source_records()
    symbolic = symbolic_checks()
    models = [sparse_model(m, q)[0] for m, q in [(1, 5), (1, 7), (1, 11), (2, 29), (2, 31)]]
    cuts = restriction_checks()
    result = {
        "status": "PASS",
        "note": {"path": NOTE, "sha256": sha((ROOT/NOTE).read_bytes())},
        "checker": {"path": str(Path(__file__).relative_to(ROOT)),
                    "sha256": sha(Path(__file__).read_bytes())},
        "source": {"repository": "jsmorph/rh", "commit": REV,
                   "atlas_sha256": atlas_sha, "files": sources},
        "exact_checks": {"symbolic": symbolic, "sparse_integral_models": models,
                         "source_and_target_coordinate_cuts": cuts},
        "review_scope": "This report covers automated exact checks and source-byte provenance only; independent mathematical review is recorded separately by the project.",
        "scope": [
            "The universal incidence and all-bases lower bounds are proved in the note, not by finite matrix enumeration.",
            "Gram matrices use standard Euclidean comparison spaces; the arithmetic metrics and map heights remain fixed separately.",
            "Finite tests use exact integer incidence matrices and rational traces, with no floating-point eigenvalues.",
            "The examples satisfy the stated matrix contract but are not identified with the actual period family or its constructor.",
            "Pinned source bytes and bounded excerpts were checked; no Lean replay or complete upstream audit was performed.",
            "No actual global theta trace supplier, RH theorem, GRH theorem, or blueprint-node completion is established."
        ]
    }
    (ROOT/OUT).write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "certificate": OUT,
                      "source_files": len(sources),
                      "excerpts": sum(len(row["inspected_excerpts"]) for row in sources),
                      "symbolic_identities": len(symbolic["identities"]),
                      "integral_models": len(models),
                      "nonzero_entries_checked": sum(row["nonzero_entries"] for row in models),
                      "distinct_pairs_checked": sum(row["distinct_pairs_checked"] for row in models),
                      "restriction_models": len(cuts)}, sort_keys=True))


if __name__ == "__main__":
    main()
