#!/usr/bin/env python3
"""Authenticate local Pieri/period interfaces and check exact proof identities."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
import subprocess
import urllib.request
from collections import Counter
from fractions import Fraction
from math import ceil
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
REPO = "jsmorph/rh"
STEM = "global-norm-frontier-pieri-family"
J = "Development.AbelianVarietyTheory."
T = "CompanionTheory.AutomorphicTheory.PieriRules.ThetaBesselIsometries."
SOURCES = [
    (J+"Definitions.Jets.SumIoPrAlt", [(18, 61), (77, 100), (125, 169)]),
    (J+"Definitions.Jets.SideFam", [(19, 21), (30, 45)]),
    (J+"PublishedTheorems.DiscreteSeries₂.Zuckerman", [(13, 19)]),
    (J+"Proofs.JetHarmonics.PieriTensorDecomposition", [(112, 191), (232, 275)]),
    (J+"Proofs.JetHarmonics.FamilyThroughDiscreteSeries", [(10, 35)]),
    (J+"Proofs.JetHarmonics.ExistsFamilyFunctionals", [(10, 41)]),
    (J+"Proofs.JetHarmonics.NumericalFamilyShapeGaps", [(73, 115)]),
    ("Formalism.PeriodIntegrals.UpqRep", [(228, 235), (296, 331)]),
    ("Formalism.HermitianCurvature.StatementB", [(224, 234)]),
    ("Formalism.HermitianCurvature.BesselNonvanishingReduction",
     [(22, 54), (122, 143)]),
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.BesselDiscreteSeries.DecInfPf",
     [(59, 126)]),
    ("ReciprocityTheory.ReductiveGroups.DiscreteSeries.InfinitesimalDecay."
     "DecBoundOfCompact", [(80, 126)]),
    (T+"BesselGapExistsFunctional", [(25, 45)]),
    (T+"TensorMomentEstimate", [(59, 123)]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.OnePlaceEstimates",
     [(57, 64)]),
]
REFERENCES = [
    {
        "file": "knapp-vogan-preview.pdf",
        "url": "https://api.pageplace.de/preview/DT0400.9781400883936_A26869474/preview-9781400883936_A26869474.pdf",
        "sha256": "40edacda4fb8e9d3758f5d34c74867a792735159de79d638dedb3a9ce8e9ff3c",
        "pages": [10, 53],
        "used_for": "Good-range Theorems 0.50--0.51, printed page 34; table of contents identifies induction-in-stages chapter. The unavailable full chapter is cited, not claimed locally inspected.",
    },
    {
        "file": "harris-kobayashi-speh-2025.pdf",
        "url": "https://www.ms.u-tokyo.ac.jp/~toshi/texpdf/tk2025l-HKS_250921.pdf",
        "sha256": "be28805b969fa0bb72fddd253d9b33afd9734bd2c3242dbcb9d37df9b88067be",
        "pages": [15, 16, 20, 21, 48, 49],
        "used_for": "Parameter classification; Lemmas 2.18--2.19 on cohomological induction and tensoring; Proposition 5.5 on standard/dual tensor shifts.",
    },
    {
        "file": "bernstein-krotz-2014.pdf",
        "url": "https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/Bern-Kroetz-2014.pdf",
        "sha256": "afa09e43f1bc8c6e5323da3a23c34735d9972434d370922c951cd8bb5dcce695",
        "pages": [2],
        "used_for": "Casselman--Wallach equivalence between smooth admissible moderate-growth Frechet representations and Harish-Chandra modules.",
    },
    {
        "file": "jiang-sun-zhu-bessel-v2.pdf",
        "url": "https://arxiv.org/pdf/0908.1728v2",
        "sha256": "4eb27d5be576b980cf6fd49bc59df7c0a961f465f26299b314e608fa97d1c36b",
        "pages": [1, 2, 3, 4],
        "used_for": "Theorem A and exact Bessel subgroup/generic-character conventions, including r=0.",
    },
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def source_records(offline):
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert digest(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert (atlas["repository"], atlas["commit"]) == (REPO, REV)
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        path = "lean/src/"+module.replace(".", "/")+".lean"
        rec = inspect_file({"repository": REPO, "commit": REV, "path": path,
                            "git_blob_sha1": blobs[module]}, offline)
        assert rec["matches_pinned_blob"]
        lines = (ROOT/"build/source-cache"/REPO/REV/path).read_bytes().splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            data = b"".join(lines[lo-1:hi])
            assert len(data) <= 12288
            excerpts.append({"lines": [lo, hi], "bytes": len(data), "sha256": digest(data)})
        records.append({"module": module, **{key: rec[key] for key in
                        ["repository", "commit", "path", "bytes", "sha256",
                         "git_blob_sha1", "matches_pinned_blob"]},
                        "excerpts": excerpts})
    return records


def reference_records(offline):
    cache = ROOT/"build/reference-cache"
    cache.mkdir(parents=True, exist_ok=True)
    records = []
    for item in REFERENCES:
        path = cache/item["file"]
        if not path.exists():
            if offline:
                raise FileNotFoundError(path)
            with urllib.request.urlopen(item["url"], timeout=60) as response:
                data = response.read()
            assert digest(data) == item["sha256"]
            path.write_bytes(data)
        data = path.read_bytes()
        assert digest(data) == item["sha256"]
        pages = []
        for page in item["pages"]:
            text = subprocess.run(
                ["pdftotext", "-q", "-layout", "-f", str(page), "-l", str(page),
                 str(path), "-"], capture_output=True, check=True).stdout
            assert text.strip()
            pages.append({"pdf_page": page, "text_bytes": len(text),
                          "text_sha256": digest(text)})
        records.append({**{k: v for k, v in item.items() if k != "pages"},
                        "bytes": len(data), "bounded_page_excerpts": pages})
    return records


def compact_wall_paths():
    cases = transitions = walls = repeated_endpoints = 0
    example = None
    for n in range(2, 7):
        for signs in itertools.product([-1, 1], repeat=n):
            # Adjacent compact gaps one; every noncompact gap at least four.
            mu = [0]*n
            for j in range(n-2, -1, -1):
                mu[j] = mu[j+1]+(1 if signs[j] == signs[j+1] else 4)
            paths = [(tuple(mu), ())]
            for depth in range(1, 4):
                new_paths = []
                for param, path in paths:
                    for j in range(n):
                        target = list(param)
                        target[j] += 1
                        transitions += 1
                        ties = [a for a in range(n-1) if target[a] == target[a+1]]
                        assert all(target[a] >= target[a+1] for a in range(n-1))
                        for a, b in itertools.combinations(range(n), 2):
                            if signs[a] != signs[b]:
                                assert abs(target[a]-target[b]) >= 4-depth > 0
                        if ties:
                            assert ties == [j-1] and signs[j-1] == signs[j]
                            walls += 1
                            continue
                        new_paths.append((tuple(target), path+(j,)))
                paths = new_paths
                multiplicities = Counter(param for param, path in paths)
                repeated_endpoints += sum(v > 1 for v in multiplicities.values())
                if example is None:
                    for param, mult in multiplicities.items():
                        if mult > 1:
                            example = {"signs": signs, "initial": mu, "final": param,
                                       "distinct_paths": [path for p, path in paths if p == param]}
                            break
                cases += 1
    assert walls > 0 and repeated_endpoints > 0 and example is not None
    return {"parameter_depth_cases": cases, "one_step_transitions": transitions,
            "compact_wall_factors": walls, "repeated_final_parameters": repeated_endpoints,
            "repeated_parameter_example": example,
            "scope": "Combinatorial checks; the cohomological zero and actual splitting are proved in the written argument."}


def tensor_coordinate_checks():
    count = 0
    matrices = []
    for t in [sp.Rational(1, 3), sp.Rational(1, 2)]:
        c, s = (1+t*t)/(1-t*t), 2*t/(1-t*t)
        matrices.append((sp.diag(1, -1), sp.diag(sp.I, 1)*sp.Matrix([[c, s], [s, c]])))
    swap = sp.Matrix([[0, 1], [1, 0]])
    for t in [sp.Rational(2, 3), sp.Rational(3, 2)]:
        g = sp.diag(2, sp.Rational(1, 2))*sp.Matrix([[1, sp.I*t], [0, 1]])*sp.Matrix([[1, 0], [sp.I/3, 1]])
        matrices.append((swap, g))
    for gamma, g in matrices:
        assert sp.simplify(g.H*gamma*g-gamma) == sp.zeros(2)
        for m in range(5):
            gm, hm = sp.ones(1), sp.ones(1)
            for _ in range(m):
                gm = sp.kronecker_product(gm, g)
                hm = sp.kronecker_product(hm, gamma)
            for i, j in itertools.product(range(2), repeat=2):
                row = next(a for a in range(2) if gamma[a, i] != 0)
                sign = gamma[row, i]
                ii = sum(row*2**a for a in range(m))
                jj = sum(j*2**a for a in range(m))
                actual = (hm*gm)[ii, jj]
                assert sp.simplify(actual-sign**m*g[i, j]**m) == 0
                count += 1
    return {"signed_coordinate_power_identities": count,
            "original_signed_permutation_forms_included": True}


def decay_reserve_checks():
    count = 0
    for r in range(16):
        for k in range(1, 21):
            n, q = 2*r+k+1, r+1
            ag = 4*(k+r)*q
            dn = r*(r-1)+2*r*(k+1)+r*r
            a_s = (2*r+k)*dn
            mexp = 2*(r*r+r+1)
            gate1 = 2*mexp*(a_s+ag)+ag+3
            gate2 = 9*q*n*n+3*ag+3
            for fraction in [Fraction(0), Fraction(1, 3), Fraction(7, 8)]:
                a = Fraction(120*n**3+gate1+gate2+1)+fraction
                m = ceil(a-1)
                # h*=8 sqrt(2r+2) a >=8a; use rational lower bounds.
                assert a > 1 and a-1 <= m <= a < 8*a
                assert 8*a >= 120*n**3
                assert a >= gate1 and a >= gate2
                assert a-1 > 2*n*n
                count += 1
    return {"exact_rational_gap_and_ceiling_cases": count,
            "family_effective_gap": "h_*=h/4, giving a=h/(32 sqrt(2r+2))",
            "nonuniform_seminorm_constants_used_only_for_convergence": True}


def compose(p, q):
    return tuple(p[q[j]] for j in range(len(p)))


def inverse(p):
    return tuple(p.index(j) for j in range(len(p)))


def norm_sq(x):
    return sp.expand((x.H*x)[0])


def folner_checks():
    group = list(itertools.permutations(range(3)))
    index = {p: j for j, p in enumerate(group)}
    regular = {}
    for p in group:
        mat = sp.zeros(6)
        for j, q in enumerate(group):
            mat[index[compose(p, q)], j] = 1
        regular[p] = mat
    vectors = [sp.Matrix([1, sp.I, 2-sp.I, 3, 1+2*sp.I, -2]),
               sp.Matrix([0, 2, 1+sp.I, -1, 3*sp.I, 4])]
    count = wrong_inverse_cases = 0
    wrong_example = None
    for subset in itertools.combinations(group, 3):
        a_set = set(subset)
        for x in vectors:
            for haar in [sp.Rational(3, 2), sp.Rational(7, 3)]:
                lhs = 0
                for p in group:
                    pa = {compose(p, a) for a in subset}
                    overlap = sp.Rational(len(a_set & pa), len(subset))
                    lhs += haar*(x.H*regular[p]*x)[0]*overlap
                avg = sum((haar*regular[inverse(a)]*x for a in subset), sp.zeros(6, 1))
                rhs = norm_sq(avg)/(haar*len(subset))
                assert sp.simplify(lhs-rhs) == 0 and sp.simplify(rhs).is_nonnegative
                wrong_avg = sum((haar*regular[a]*x for a in subset), sp.zeros(6, 1))
                wrong = norm_sq(wrong_avg)/(haar*len(subset))
                if sp.simplify(lhs-wrong) != 0:
                    wrong_inverse_cases += 1
                    if wrong_example is None:
                        wrong_example = {"subset": subset, "haar_mass_per_element": str(haar),
                                         "left_overlap": str(sp.simplify(lhs)),
                                         "wrong_average_without_inverse": str(sp.simplify(wrong))}
                count += 1
    assert wrong_inverse_cases and wrong_example is not None
    full_averages = 0
    for haar in [sp.Rational(3, 2), sp.Rational(7, 3)]:
        gram = sum((haar*regular[p] for p in group), sp.zeros(6))
        factor = sp.sqrt(haar)*sp.ones(1, 6)
        assert gram == factor.H*factor and gram.rank() == 1
        full_averages += 1
    return {"noncommutative_S3_overlap_identities": count,
            "nonunit_Haar_positive_rank_one_factorizations": full_averages,
            "wrong_inverse_negative_controls": wrong_inverse_cases,
            "first_wrong_inverse_example": wrong_example}


def zero_base_compatibility_checks():
    count = 0
    a = sp.Matrix([[0, 0], [1, 0], [0, 1]])
    sigma = [sp.eye(2), -sp.eye(2)]
    shifted = [sp.eye(3), sp.diag(1, -1, -1)]
    for haar, sign in itertools.product([sp.Rational(3, 2), sp.Integer(2)], [1, -1]):
        b = sp.zeros(1, 2)
        bi = sp.sqrt(2*haar)*sp.Matrix([[1, 0, 0]])
        c = sign*a.H
        assert sum((haar*g for g in sigma), sp.zeros(2)) == b.H*b
        assert sum((haar*g for g in shifted), sp.zeros(3)) == bi.H*bi
        for g, gi in zip(sigma, shifted):
            assert a*g == gi*a and g*c == c*gi
        assert bi != sp.zeros(1, 3) and a != sp.zeros(3, 2)
        assert bi*a == sp.zeros(1, 2)
        assert b*c == sp.zeros(1, 3)
        count += 1
    return {"zero_base_nonzero_shifted_period_models": count,
            "nonzero_intertwining_A_and_both_tensor_signs": True,
            "logical_supplier": "Exact period comparison before scalar construction; no inference that a zero period form implies zero Bessel Hom space."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources = source_records(args.offline)
    references = reference_records(args.offline)
    checks = {"compact_walls_and_paths": compact_wall_paths(),
              "tensor_coordinates": tensor_coordinate_checks(),
              "decay_reserve": decay_reserve_checks(),
              "folner_positivity": folner_checks(),
              "zero_base_pieri_compatibility": zero_base_compatibility_checks()}
    files = [f"notes/{STEM}.md", f"paper/shared/{STEM}.tex",
             f"paper/shared/{STEM}-references.tex",
             f"scripts/check_{STEM.replace('-', '_')}.py",
             "paper/shared/global-norm-frontier-jacquet-gram.tex",
             "paper/shared/global-norm-frontier-normalized-lowering.tex",
             "paper/shared/global-norm-frontier-quotient-mass.tex",
             "paper/shared/global-norm-frontier-first-length.tex"]
    result = {
        "schema_version": 1, "status": "PASS",
        "classification": "closed local representation/Pieri, smooth-decay, exact period-normalization and leading-minor subobligations",
        "theorem": "Original BesselLeadingMinorBound follows with Cq>=200, Cg>=10^6, Cb>=Ch+5, including both original character scales.",
        "checks": checks, "sources": sources, "primary_references": references,
        "artifact_hashes": {p: digest((ROOT/p).read_bytes()) for p in files},
        "scope": {
            "written_proof": "Shared TeX and mathematical note; classical representation theorems are explicitly cited.",
            "computation": "Exact identities and bounded edge-case checks supplement, and do not replace, the written proof.",
            "not_verified": ["Weighted orbital estimate", "Global rational-return/Gram assembly",
                             "Integral theta maps and global nonvanishing", "Any full Lean build"],
            "whole_node_count_changed": False,
        },
    }
    dest = ROOT/"certificates"/(STEM+".json")
    dest.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "source_modules": len(sources),
                      "primary_references": len(references), "checks": checks,
                      "certificate": str(dest.relative_to(ROOT))}, indent=2))


if __name__ == "__main__":
    main()
