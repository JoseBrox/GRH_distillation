#!/usr/bin/env python3
"""Authenticate the CM supplier's sources and check exact finite algebra.

This is a provenance and algebra checker, not a proof of the geometric,
class-field-theoretic or analytic inputs, and not a Lean kernel replay.
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
AV = "Development.AbelianVarietyTheory."
SOURCES = [
    (AS + "Proofs.AlgebraProofs.PurePeriodLocalBasisExists",
     [[151, 193], [202, 237]]),
    (AS + "Proofs.AlgebraProofs.LocalBasisGramDeterminantBound",
     [[146, 162], [336, 378], [465, 505]]),
    (AS + "Definitions.GlobalGeometry.IsCMFrame",
     [[15, 30], [36, 64], [75, 88]]),
    (AS + "Proofs.GeometryProofs.CmPeriodAlgebraic",
     [[19, 45], [71, 110], [114, 164]]),
    (AS + "Proofs.GeometryProofs.CmPackProductFrame", [[27, 64]]),
    (AS + "Proofs.GeometryProofs.IsogenyDecompositionProduct", [[12, 56]]),
    (AS + "Proofs.GeometryProofs.CmPackPureNorm",
     [[129, 158], [234, 291]]),
    (AS + "Proofs.GeometryProofs.DualBasisHermitianSum",
     [[20, 34], [45, 102]]),
    ("Development.WeilBound.CoreStatements.SesquilinearFractions."
     "LieNormSquareOfFamily", [[11, 45], [73, 119]]),
    (AS + "Proofs.GeometryProofs.CmPackPeriodProduct",
     [[206, 229], [262, 331]]),
    (AS + "Proofs.GeometryProofs.CmPackPureFrameOpen",
     [[19, 24], [125, 184]]),
    (AS + "Proofs.GeometryProofs.FrameFunctionCmValue",
     [[20, 28], [43, 53]]),
    (AS + "Proofs.GeometryProofs.FrameFunctionCmNumberField",
     [[23, 59], [65, 88]]),
    (AS + "Proofs.GeometryProofs.FrameFunctionCmHeight",
     [[22, 49], [50, 114]]),
    (AS + "Proofs.GeometryProofs.FlatDegreeHolds", [[60, 118]]),
    (AS + "Definitions.GlobalGeometry.IsConstMul", [[30, 50], [59, 82]]),
    (AS + "Proofs.GeometryProofs.ChowlaSelbergPeriod", [[18, 33]]),
    (AV + "Statements.PrincipalLattices.LogHermFormOfUnitDiscriminant",
     [[28, 50]]),
    (AV + "Proofs.CubicalLineBundles.IsLieNormSqIffEqPiDivCovolume",
     [[13, 24]]),
    (AV + "Definitions.CMLattices.ExistsIsThetaDegOfIsLocalModel",
     [[23, 46]]),
]
PRIMARY = [
    {
        "path": "build/reference-cache/milne-abelian-varieties.pdf",
        "url": "https://jmilne.org/math/CourseNotes/AV.pdf",
        "sha256": "f5ca4e63e5092a4b102daad1470e4cbed5fe8f82115e3a28c8881e3f67f6aaef",
        "inspected": [
            "Theorems 2.8-2.9, pp.14-15: polarized tori and algebraic homomorphisms",
            "Remark 8.12, p.39: finite subgroup quotients",
            "Proposition 13.6, pp.58-59: line bundles and alternating Tate pairing in characteristic zero",
            "Corollary 16.4, p.68: homomorphism descent over regular extensions",
        ],
    },
    {
        "path": "build/reference-cache/milne-modular-functions-2017.pdf",
        "url": "https://www.jmilne.org/math/CourseNotes/MF.pdf",
        "sha256": "977f06a4e838c43c77a7c9398c090789e60d67f64e013e1dcd9bcce0e0c27b8d",
        "inspected": [
            "Theorem 4.21, p.57: discriminant product with (2*pi)^12",
            "Theorem 12.14, p.125: potential good reduction for elliptic CM",
            "Theorem 12.18, p.126: CM ideal-class Galois orbit",
        ],
    },
    {
        "path": "build/reference-cache/zagier-kronecker-1975.pdf",
        "url": "https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BF01343950/KroneckerLimit.pdf",
        "sha256": "df4307e4e6b61a453fa5695bd67f58c8c58624916401957f346fa59306ee8a41",
        "inspected": [
            "Section 2, pp.156-159, (2.3)-(2.5): quadratic lattice zeta and Kronecker formula",
        ],
        "normalization": "The reference's zeta_Q is 2^s times Z_tau; the constant term is rescaled too.",
    },
    {
        "path": "build/reference-cache/conrad-minimal-models-2015.pdf",
        "url": "https://math.stanford.edu/~conrad/papers/minimalmodel.pdf",
        "sha256": "1093586aee9844c3c37f518d7b241175d4a64c3912839ecdd485c4c185a8b87a",
        "inspected": [
            "Definition 5.1 and Example 5.3, p.13: Neron mapping and unit discriminant criterion",
        ],
    },
    {
        "path": "build/reference-cache/serre-tate-good-reduction-1968.pdf",
        "url": "https://wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf",
        "sha256": "93a2f4e0cd8d9e49c4d96baa76753ca8debf2d1f06e58d563fe1f30fd81dfeb7",
        "inspected": [
            "Theorem 1 and Corollary 2, printed p.493 (PDF page 3): good reduction invariant under isogeny",
        ],
        "inspection_method": "Rendered scanned page inspected directly; pdftotext is empty.",
    },
]
ARTIFACTS = [
    "notes/cm-product-period-calculation.md",
    "scripts/check_cm_product_period_calculation.py",
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
    evidence = []
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
        evidence.append({
            "module": module, "path": path,
            "sha256": record["sha256"],
            "git_blob_sha1": record["git_blob_sha1"],
            "url": f"https://github.com/jsmorph/rh/blob/{REV}/{path}",
            "inspected_excerpts": excerpts,
        })
    return evidence


def primary_evidence(fetch: bool) -> list[dict]:
    for item in PRIMARY:
        path = ROOT / item["path"]
        if not path.exists() and fetch:
            path.parent.mkdir(parents=True, exist_ok=True)
            request = urllib.request.Request(
                item["url"], headers={"User-Agent": "Mozilla/5.0",
                                      "Accept": "application/pdf"})
            with urllib.request.urlopen(request, timeout=50) as response:
                path.write_bytes(response.read())
        assert path.exists(), f"Missing primary PDF; rerun with --fetch: {path}"
        assert sha(path.read_bytes()) == item["sha256"], item["path"]
    return PRIMARY


def symbolic_identities() -> dict:
    a, b, d, w = sp.symbols("a b d w")
    modpoly = sp.Poly(w*w - w + (d+1)/4, w)
    trace = 2*a + b
    trace_w = a + b*(1-d)/2
    rhs = trace_w - trace + w*trace
    lhs = (2*w-1)*(a+b*w)
    assert sp.rem(sp.Poly(lhs-rhs, w), modpoly).is_zero

    # Discriminant and metric constants: use formal logarithms.
    lpi, ltwo, lo, ly, leta = sp.symbols("lpi ltwo lo ly leta")
    log_delta = 12*(ltwo+lpi) - 12*lo + 24*leta
    log_n = lpi - 2*lo - ly
    assert sp.expand(log_n - (-2*ltwo-lpi-ly-4*leta + log_delta/6)) == 0

    # KLF rescaling and the class-average constant.
    gamma, ld, ratio, mean = sp.symbols("gamma ld ratio mean")
    log_c = ltwo-ld/2
    const_over_residue = log_c+2*gamma-2*ltwo-mean
    mean_value = sp.solve(const_over_residue-(gamma+ratio), mean)[0]
    x = gamma+ltwo+lpi-ld/2-ratio
    assert sp.expand(mean_value+2*ltwo+lpi-x) == 0

    # Archimedean determinant formula before using any product formula.
    p, q, lr, lt, lgp, lgm, lge, np, nm = sp.symbols(
        "p q lr lt lgp lgm lge np nm")
    lphi = lr-lt+lgm
    arch = lphi + (p*(np+ld/2)+lgp-q*(nm+ld/2)-lgm)/2
    arch = sp.expand(arch.subs(lgp, 2*lt+lge-lgm))
    arch_expected = lr+p*(np+ld/2)/2-q*(nm+ld/2)/2+lge/2
    assert sp.expand(arch-arch_expected) == 0

    # Finite frame covariance and conjugation-average elimination.
    D, lrt = sp.symbols("D lrt")
    finite = lr-lt-q*D+(q-p)*(D-lrt)
    finite_mean = sp.expand(finite.subs(lt, (-(p+q)*D-lge)/2))
    expected = lr+lge/2-(p-q)*D/2+(p-q)*lrt
    assert sp.expand(finite_mean-expected) == 0

    # The product formula cancels the lr and lge sums, before this step.
    X, rd = sp.symbols("X rd")
    total = (-(p-q)*X/2+(p-q)*ld/4
             -(p-q)*(-rd)/2+(p-q)*(-ld/2))
    degree = sp.expand(-total)
    assert sp.expand(degree-(p-q)*(X+ld/2-rd)/2) == 0
    corrected = degree+q*(-rd+ld)
    assert sp.expand(corrected-((p-q)*(X+ld/2-rd)/2+q*(ld-rd))) == 0
    assert degree.subs({p: 0, q: 0}) == 0
    assert degree.subs(q, p) == 0
    return {
        "trace_identity": "PASS: linear-first quadratic trace formula",
        "metric_discriminant": "PASS: pi and (2*pi)^12 constants",
        "kronecker_mean": "PASS: normalized constant/residue comparison",
        "archimedean_gram": "PASS",
        "finite_covariance": "PASS",
        "actual_and_corrected_degrees": "PASS",
        "scope": "Formal polynomial/rational identities only; analytic inputs are cited.",
    }


def trace_dual_example() -> dict:
    # A degree-four CM field tests an absolute projector, not merely F=E.
    # Its host unramifiedness is NOT asserted or used in this diagnostic.
    ar = [(1+sp.sqrt(5))/2, (1-sp.sqrt(5))/2]
    br = [(1+sp.I*sp.sqrt(7))/2, (1-sp.I*sp.sqrt(7))/2]
    rows = [[1, a, b, a*b] for a in ar for b in br]
    U = sp.Matrix(rows)
    gram = (U.T*U).applyfunc(sp.simplify)
    assert all(entry.is_Rational for entry in gram)
    dual = (U*gram.inv()).applyfunc(sp.simplify)
    projector = (dual*U.T).applyfunc(sp.simplify)
    assert projector == sp.eye(4)
    # A generic element's four conjugates; verify the two Gram sums.
    z = [1+row[1]+2*row[2]-row[3] for row in rows]
    checks = 0
    for target in range(4):
        wt = rows[target][2]
        coefficients = [
            z[i]*(rows[i][2]-1+wt) for i in range(4)]
        H = U.T*sp.diag(*coefficients)*sp.conjugate(U)
        result = (dual[target, :]*H*sp.conjugate(dual[target, :].T))[0]
        expected = (2*wt-1)*z[target]
        assert sp.simplify(result-expected) == 0
        checks += 1
    return {
        "field": "Q(sqrt(5), sqrt(-7))",
        "basis": "1, (1+sqrt(5))/2, (1+sqrt(-7))/2, their product",
        "absolute_projector_entries": 16,
        "double_gram_collapse_cases": checks,
        "scope": "Exact trace algebra; this field is not asserted to satisfy the unramified host condition.",
    }


def f4_dyadic_examples() -> dict:
    # F_4=F_2[a]/(a^2+a+1), encoded by two-bit polynomials.
    def add(x: int, y: int) -> int:
        return x ^ y

    def mul(x: int, y: int) -> int:
        raw = 0
        for i in range(2):
            for j in range(2):
                if (x >> i) & 1 and (y >> j) & 1:
                    raw ^= 1 << (i+j)
        if raw & 4:
            raw ^= 7
        return raw

    def bar(x: int) -> int:
        return mul(x, x)

    def pairing(H: list[list[int]], v: tuple[int, int],
                w: tuple[int, int]) -> int:
        value = 0
        for i in range(2):
            for j in range(2):
                value = add(value, mul(mul(v[i], H[i][j]), bar(w[j])))
        return value

    assert add(2, bar(2)) == 1  # trace-unit dyadic anti-unit reduction
    forms = norm_vectors = orthogonal_complements = 0
    for a in [0, 1]:
        for c in [0, 1]:
            for b in range(4):
                H = [[a, b], [bar(b), c]]
                det = add(mul(a, c), mul(b, bar(b)))
                if det == 0:
                    continue
                forms += 1
                good = []
                for x in range(4):
                    for y in range(4):
                        v = (x, y)
                        if pairing(H, v, v) == 1:
                            good.append(v)
                            norm_vectors += 1
                assert good
                for v in good:
                    perpendicular = [
                        (x, y) for x in range(4) for y in range(4)
                        if pairing(H, (x, y), v) == 0]
                    assert len(perpendicular) == 4
                    assert all(pairing(H, w, w) != 0
                               for w in perpendicular if w != (0, 0))
                    orthogonal_complements += 1
    assert forms == 10
    return {
        "field": "F_4/F_2",
        "all_nondegenerate_rank_two_hermitian_forms": forms,
        "unit_norm_vectors": norm_vectors,
        "nondegenerate_orthogonal_complements": orthogonal_complements,
        "scope": "Exhaustive finite dyadic diagnostic; the all-rank/all-prime argument is the written proof.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true")
    args = parser.parse_args()
    evidence = source_evidence(args.fetch)
    primary = primary_evidence(args.fetch)
    symbolic = symbolic_identities()
    trace = trace_dual_example()
    dyadic = f4_dyadic_examples()
    output = {
        "status": "PASS",
        "scope": "Automated source authentication and exact finite algebra only.",
        "lean_kernel_replay": False,
        "independent_review": {
            "record": "certificates/hard-node-review-2026-11-22.json",
            "scope": "The separate review record covers the written mathematical proof and its retained hypotheses.",
        },
        "proved_in_written_argument": [
            "Pure local basis at every chosen prime, including dyadic places",
            "Descent of the specified symmetric rigidified CM line and good abelian model",
            "Exact prime-to-residue-characteristic product tangent basis",
            "Elliptic CM period mean in the pi-times-Appell-Humbert metric",
            "Actual and corrected flat determinant degree under the retained local norm contract",
        ],
        "retained_hypotheses": [
            "The actual arithmetic moduli space, compactification and uniformization interface",
            "Existence of the algebraic flat determinant family",
            "Equality of its prescribed local norm with the same-model norm at every allowed CM point",
            "No new assertion about the cusp or section-surplus supplier",
        ],
        "sources": evidence,
        "primary_references": primary,
        "previously_audited_input": {
            "note": "notes/moret-bailly-theta-supplier.md",
            "role": "The Moret-Bailly extension of the specified rigidified line and same-model comparison",
            "sha256": sha((ROOT / "notes/moret-bailly-theta-supplier.md").read_bytes()),
        },
        "checks": {
            "symbolic": symbolic,
            "absolute_trace_dual": trace,
            "dyadic_finite_forms": dyadic,
        },
        "artifacts": [
            {"path": path, "sha256": sha((ROOT/path).read_bytes())}
            for path in ARTIFACTS
        ],
    }
    out = ROOT / "certificates/cm-product-period-calculation.json"
    out.write_text(json.dumps(output, indent=2, ensure_ascii=False)+"\n")
    print(f"PASS: {len(evidence)} pinned sources, {len(primary)} primary PDFs, "
          f"symbolic constants/degrees, {trace['double_gram_collapse_cases']} "
          f"absolute-projector Gram cases, {dyadic['all_nondegenerate_rank_two_hermitian_forms']} "
          "dyadic Hermitian forms.")
    print("Scope: source authentication and exact finite algebra; no Lean replay.")


if __name__ == "__main__":
    main()
