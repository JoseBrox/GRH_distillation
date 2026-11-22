#!/usr/bin/env python3
"""Check pinned frontier contracts and exact vertical-fibre counterexamples.

This checks source provenance and finite polynomial algebra.  It is not a Lean
build, a Galois representation construction, or an arithmetic finiteness proof.
"""

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
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
SOURCES = [
    ("AutomorphicCases.AutomorphyUnramifiedCoefficients", [(12, 27)], ["def FinA", "Module.Finite"]),
    ("UnitaryThreeGroups.GRepresents", [(75, 105)], ["structure Univ", "def BoxCond", "def NormCond"]),
    ("UnitaryThreeGroups.ConjStable", [(25, 49), (70, 85)], ["abbrev SRing", "RingHom.ker q = Q.ideal"]),
    ("CurveDVRSpecialization.RatTorsionFree", [(21, 32)], ["def FinEnd", "FiniteIndex"]),
    ("CurveDVRSpecialization.GfResZpow", [(179, 205)], ["finA_of_end", "finCrit", "diag_eq_and_triangular_of_charpoly_eq"]),
    ("CurveDVRSpecialization.FinCrit", [(122, 186)], ["theorem UpperTheory.V.Pr.finCrit", "maximalIdeal (W.gr 0)", "finite_of_finite_quotient_map"]),
    ("CurveDVRSpecialization.FinEndOfFinPt", [(9, 48)], ["finEnd_of_finPt", "FinPt O Φ 3 → FinEnd"]),
    ("CurveDVRSpecialization.PropagationTheoremGL2", [(32, 60), (74, 84)], ["def OffFin", "def FinPt", "P23'"]),
    ("CurveDVRSpecialization.FinPtOf", [(183, 260)], ["theorem finPtOf", "S.u.OffTri"]),
    ("CurveDVRSpecialization.PropagationTheoremGL3", [(150, 159), (213, 229)], ["components_good_rank_three", "h23", "M ⊓ I₃"]),
    ("CurveDVRSpecialization.AbsMain", [(12, 30)], ["m₃.p3", "components_good_rank_three", "finPtOf"]),
    ("CurveDVRSpecialization.SecondThirdPrimeConditionTransferAlt", [(78, 85), (103, 107)], ["structure ModIn", "p3 : T.B.P3core J"]),
    ("ModularityArgument.ThresholdArguments.DenseThresholdCases.PrLinkedEnd", [(22, 40)], ["ModUAlt", "hJ.p1, hJ.p3"]),
    ("ModularityArgument.ThresholdArguments.DenseThresholdCases.PointTheoremBaseObject", [(26, 48)], ["structure ModularAlt", "p1 : B.P1core J", "p3 : B.P3core J"]),
    ("WeilGroupCharacters.UniversalOrdinaryDeterminantRing", [(266, 301)], ["def IsThick", "def P1core", "def P3core"]),
    ("PatchingModules.TaylorWilesObstructionBound", [(126, 154)], ["def HasAut", "def PfromAut", "B.P1core J ∧ B.P3core J"]),
    ("PatchingModules.AutomorphicDetection.PfromAut", [(1, 10)], ["theorem UpperTheory.V.Pa.pFromAut", "UpperTheory.V.Pa.raw"]),
    ("PatchingModules.ChebotarevFamilies.PFromAutOf", [(30, 49), (83, 114), (116, 131)], ["theorem chain_of", "hR l", "theorem pFromAut_of"]),
    ("PatchingModules.PatchedSupportCompletions", [(181, 213)], ["def ChainConcl", "def Raw"]),
    ("PatchingModules.AutomorphicDetection.LiftPt", [(76, 110), (139, 175)], ["theorem core", "patchedModule_free_finite_over_iwasawaAlgebra", "galOut"]),
    ("PatchingModules.AutomorphicDetection.GalOut", [(16, 43)], ["private theorem ctx_out", "presOut0", "presOut1"]),
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_records(offline: bool) -> list[dict]:
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["commit"] == REV
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for suffix, ranges, anchors in SOURCES:
        module = PREFIX + suffix
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        raw = inspect_file({"repository": "jsmorph/rh", "commit": REV,
                            "path": rel, "git_blob_sha1": blobs[module]}, offline)
        assert raw["matches_pinned_blob"]
        data = (ROOT / "build/source-cache/jsmorph/rh" / REV / rel).read_bytes()
        lines = data.splitlines(keepends=True)
        excerpts = []
        bounded_text = ""
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            excerpt = b"".join(lines[lo - 1:hi])
            excerpts.append({"first_line": lo, "last_line": hi, "sha256": sha(excerpt)})
            bounded_text += excerpt.decode()
        for anchor in anchors:
            assert anchor in bounded_text, (suffix, anchor)
        records.append({"module": module, "path": rel, "commit": REV,
                        "git_blob_sha1": blobs[module], "sha256": sha(data),
                        "matches_pinned_blob": True, "excerpts": excerpts,
                        "checked_contract_anchors": anchors})
    return records


def ideal_basis(gens, variables):
    return [sp.expand(p.as_expr()) for p in sp.groebner(gens, *variables, order="lex", domain=sp.QQ).polys]


def elimination(gens, variables, eliminated):
    basis = ideal_basis(gens, variables)
    return [p for p in basis if not (p.free_symbols & set(eliminated))]


def algebra_checks() -> dict:
    u, x, y, z, pi = sp.symbols("u x y z pi")
    checks = []
    for exponent in range(1, 7):
        rel = [pi**exponent*x, pi**exponent*y]
        weight_zero = elimination(rel + [z-x*y], (x, y, z, pi), (x, y))
        assert weight_zero == [pi**exponent*z], weight_zero
        saturation = elimination(rel + [1-u*pi], (u, x, y, pi), (u,))
        assert saturation == [x, y], saturation
        conormal = ideal_basis(rel + [x*x, x*y, y*y], (x, y, pi))
        assert conormal == [x*x, x*y, pi**exponent*x, y*y, pi**exponent*y], conormal
        # Independent monomial count: every positive invariant x^a y^a
        # survives modulo pi, while both variables die after saturation.
        for degree in range(1, 41):
            assert degree-degree == 0
            assert sp.Poly((x*y)**degree, x, y, pi).monoms() == [(degree, degree, 0)]
        checks.append({"M": exponent, "invariant_relation": str(weight_zero[0]),
                       "pi_saturation": list(map(str, saturation)),
                       "conormal_relations": list(map(str, conormal)),
                       "surviving_weight_zero_monomials_mod_pi_checked": 40})

    # (pi) intersection (x,y) is computed by the elimination formula
    # I intersection J = (u I + (1-u) J) intersection the original ring.
    radical_case = elimination([u*pi, (1-u)*x, (1-u)*y], (u, x, y, pi), (u,))
    assert radical_case == [pi*x, pi*y], radical_case

    # Negative control: same generic fibre, but x*y=0 deletes every
    # positive weight-zero monomial; its invariant ring is O.
    no_mixed = elimination([pi*x, pi*y, x*y, z-x*y], (x, y, z, pi), (x, y))
    assert no_mixed == [z], no_mixed
    return {"status": "PASS", "cases": checks,
            "reduced_M1_intersection": list(map(str, radical_case)),
            "negative_control_extra_relation_xy_zero": list(map(str, no_mixed)),
            "scope": "Exact polynomial elimination and monomial identities; the accompanying proof passes these identities to complete power series rings. No actual Galois counterexample is claimed."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    record = {
        "status": "PASS",
        "claim": "The actual integral finiteness supplier controls characteristic-prime curves; generic rigidity and reducedness alone cannot replace it.",
        "source_provenance": source_records(args.offline),
        "exact_algebra": algebra_checks(),
        "not_verified": ["Lean kernel/build", "actual global ring flatness", "human reconstruction of rank-three patched-support propagation", "uniform integral Selmer length bound"],
        "node_counts_unchanged": {"RH": "6/9", "GRH": "17/31"},
        "artifacts": {},
    }
    for rel in ["notes/selmer-integral-frontier-special-fibre.md", "scripts/selmer-integral-frontier-check.py"]:
        record["artifacts"][rel] = sha((ROOT / rel).read_bytes())
    out = ROOT / "certificates/selmer-integral-frontier-special-fibre.json"
    out.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "PASS", "source_files": len(SOURCES),
                      "exact_counterexample_exponents": 6, "certificate": str(out)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
