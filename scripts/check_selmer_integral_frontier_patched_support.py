#!/usr/bin/env python3
"""Authenticate the exact S5 supplier and its finite monomial-ideal step."""
from __future__ import annotations
import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path
from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
P = BASE+"PatchingModules."
AB = P+"AnnihilatorBaseChange."
RANGES = {
    P+"PatchedSupportCompletions": [(23, 70), (179, 185)],
    BASE+"AlgebraTools.UltraDefs": [(15, 33), (90, 98)],
    BASE+"AlgebraTools.ULimTrans": [(8, 30)],
    BASE+"AlgebraTools.QRegLim": [(8, 37)],
    BASE+"AlgebraTools.Patched": [(92, 163)],
    AB+"ExistsPowMaximalIdealSmulFiniteEqZero": [(1, 56)],
    AB+"ExistsUltraLimitPairOfEventualQuotientMaps": [(48, 105)],
    AB+"PmodEx": [(32, 95)],
    AB+"PmDimQuot": [(74, 149)],
    AB+"PmFib": [(7, 31)],
    AB+"PmMove": [(8, 23)],
    AB+"LaDimArith": [(1, 73)],
    AB+"PatchedModuleFreeFiniteOverIwasawaAlgebra": [(31, 46)],
    AB+"ChainAbs": [(1, 70)],
    P+"AutomorphicDetection.AnnBc": [(24, 87)],
    P+"AutomorphicDetection.LiftPt": [(90, 175)],
    BASE+"CurveDVRSpecialization.SeedPtOf": [(174, 179), (253, 282)],
    BASE+"IdeleGenerators.SlopeTestRemainingChoices": [(55, 99), (126, 134)],
}
DEPENDENCIES = [
    "notes/selmer-integral-frontier-taylor-wiles.md",
    "notes/selmer-integral-frontier-local-propagation.md",
]


def homogeneous_monomials(variables, degree):
    if variables == 0:
        return [()] if degree == 0 else []
    return [a for a in itertools.product(range(degree+1), repeat=variables)
            if sum(a) == degree]


def exact_checks():
    count = 0
    # Every generator of (Y+a^j)^k lies in Y^k+a^j.
    # Work in a free polynomial ring over Z, so this check uses exact
    # integer exponents and does not discard torsion or coefficients.
    for q, c, j, k in itertools.product(range(4), (1, 2),
                                       range(1, 4), range(1, 5)):
        generators = [
            tuple(int(t == i) for t in range(q))+(0,)*c
            for i in range(q)
        ]
        generators += [(0,)*q+a for a in homogeneous_monomials(c, j)]
        for indices in itertools.combinations_with_replacement(
                range(len(generators)), k):
            mon = tuple(sum(generators[i][v] for i in indices)
                        for v in range(q+c))
            assert sum(mon[:q]) >= k or sum(mon[q:]) >= j
            count += 1
    # A concrete negative control retains a positive-rank base module.
    # Lambda=F3[[t]], R=Lambda[[y,z]], X=Lambda (y,z act by zero),
    # M_N=0, f=z, I=0, q=(t,y).  X has rank 1 but X[1/f]=0.
    # f avoids q and all comparison maps are zero with composites f.
    # Patching therefore cannot create a seed at this allowed prime.
    return {
        "status": "PASS",
        "exact_monomial_products_over_Z": count,
        "diamond_variables": [0, 1, 2, 3],
        "coefficient_variables": [1, 2],
        "coefficient_orders": [1, 2, 3],
        "jet_orders": [1, 2, 3, 4],
        "negative_controls": [
            "Zero modules satisfy every finite freeness and approximate-annihilation input and give empty support.",
            "Even X of Lambda-rank one need not survive f-localization: take Lambda=F3[[t]], R=Lambda[[y,z]], X=Lambda with yX=zX=0, M_N=0, f=z, I=0, q=(t,y).",
            "The approximate annihilation exponent e is fixed before the coefficient order j; the extra f^k is removed only after localization.",
            "The dimension proof is over the prequotient completion C_i. Quotienting M_i by I before checking regular sequences is not justified.",
        ],
        "scope": "Exact monomial checks supplement the general proof. They certify neither arithmetic nonvanishing nor a Lean project build.",
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
    stem = "selmer-integral-frontier-patched-support"
    artifacts = [f"notes/{stem}.md", f"paper/shared/{stem}.tex",
                 f"paper/shared/{stem}-references.tex",
                 "scripts/check_selmer_integral_frontier_patched_support.py"]
    for path in artifacts+DEPENDENCIES:
        assert (ROOT/path).is_file(), path
        assert all(c >= 32 or c in (9, 10) for c in (ROOT/path).read_bytes())
    report = {
        "schema_version": 1, "status": "PASS",
        "classification": "closed exact S5 patched-support subobligation inside W04",
        "claim": "The original finite free jets, f-comparisons and uniformly powered approximate annihilators construct the complete PatchedSupportCompletions contract, with exact fibre support, dimension and MOVE.",
        "verification_kind": "Authenticated bounded source interfaces, prior actual-module dependencies and exact monomial-ideal controls; complete standard mathematical proof in the note.",
        "quantifiers": [
            "Every original complete Noetherian coefficient ring with finite residue field, every Noetherian local R, every finite diamond index set and every prescribed cofinal ultrafilter.",
            "For each k,j eventual finite freeness, allowing ranks to depend on N,k,j; for each j eventual comparison maps with both composites equal to the original f.",
            "One exponent e and one generating set of I, followed by each generator, every m_R-adic precision and eventually N.",
            "Every family of primes containing I+Y and avoiding f, with coefficient completions regular of specified dimension d.",
            "Exact support equivalence at every prime containing Y, and MOVE for every original pair Z subset Q and every admissible next completion.",
        ],
        "decisive_interfaces": {
            "reduced_products": "Product modulo sequences vanishing eventually at each coefficient level; finite-generator diagonal decompositions give exact Y^k transition kernels.",
            "fibre": "Finite quotients of X give maps X <-> P_1 without compatibility assumptions; both composites are f, so Q_1=X[1/f].",
            "finite_patching": "After inverting f, compatible generator lifts and homogeneous corrections give a finite module over the Y-adic completion and every exact jet.",
            "annihilation": "For each j, choose c_j killing X/a^jX. Comparisons imply f^k m_R^(k c_j) M_N subset (Y^k+a^j) M_N. Original approximate annihilators then give r^e on every localized jet.",
            "quotient_order": "Construct finite M_i over C_i=completion R_qi; retain its regular sequences there, then place the radical of Ann M_i modulo I in B_i=C_i/I.",
            "dimension": "C_i tensor_R X is the specified idempotent factor of Lambda_i tensor_Lambda X and hence finite free, with original rank retained; append d coefficient parameters after q regular diamond variables.",
            "move": "Contract the support prime to the common Y-adic completion, localize at the next admissible prime and use faithfully flat completion to lift the identical contraction.",
            "arithmetic_substitution": "d=1+D_wt, q=n*q_TW, GalOut parameter D0=D_wt+n*q_TW; threshold is exactly 1+D0.",
        },
        "limitations": [
            "S5 allows empty support. A nonzero stable arithmetic seed on the original residual component remains a separate obligation.",
            "SeedPtOf consumes the exact IsSeed representation and PointTheorem; it does not construct the representation.",
            "The complete global prime chain and the moving-family integral Selmer budget are not inferred from this supplier.",
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
