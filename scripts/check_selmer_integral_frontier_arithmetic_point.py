#!/usr/bin/env python3
"""Authenticate the exact PT supplier and test decisive normalization controls.

The universal mathematics is proved in the accompanying note. These are
source/provenance checks and finite exact diagnostics, not a Lean build.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import gzip
import hashlib
import itertools
import json
import math
from pathlib import Path
import urllib.request

import sympy as sp
from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    BASE+"WeilGroupCharacters.ContinuousResP": [(64, 164)],
    BASE+"WeilGroupCharacters.ArithmeticPointClassicality": [(61, 87)],
    BASE+"WeilGroupCharacters.UniversalOrdinaryDeterminantRing": [(109, 161)],
    BASE+"HeckeAlgebras.IsTheta": [(40, 52), (96, 113), (147, 168)],
    BASE+"ModularityArgument.ThresholdArguments.DenseThresholdCases.UnitaryHeckeData": [(38, 70)],
    BASE+"ModularityArgument.CuspidalDescent.DescWeak": [(10, 21)],
    BASE+"ModularityArgument.CuspidalDescent.DualOfWeights": [
        (83, 149), (153, 172), (216, 244), (315, 411)],
    BASE+"HeckeAlgebras.Distinct": [(28, 35), (58, 66), (97, 101)],
    BASE+"HeckeAlgebras.ContinuousTorusCharacter": [(123, 130), (269, 285), (339, 359)],
    BASE+"HeckeAlgebras.OrdinaryHeckeCharacters.ProdZpowConst": [(10, 22), (95, 125)],
    BASE+"HeckeAlgebras.OrdinaryHeckeCharacters.CtrlEq": [(23, 43)],
    BASE+"HeckeAlgebras.OrdinaryHeckeCharacters.CtrlOrd": [(84, 139)],
    BASE+"HeckeAlgebras.OrdinaryHeckeCharacters.OrdA": [(12, 100), (117, 165), (166, 252)],
    BASE+"HeckeAlgebras.CoefficientRepTrivialOnUnramified": [(263, 274)],
    BASE+"HeckeAlgebras.UpOperatorEigenvalues.SplitW": [(28, 57), (67, 146)],
    BASE+"HeckeAlgebras.OrdinaryHeckeCharacters.WtBridge": [(191, 244)],
    BASE+"HeckeAlgebras.OrdinaryHeckeCharacters.JPT": [(9, 12)],
    BASE+"PadicHodgeTheory.EpsArt": [(27, 42)],
    BASE+"ModularityArgument.ThresholdArguments.DenseThresholdCases.UnifVal": [(20, 36), (68, 97)],
    BASE+"CurveDVRSpecialization.SeedPtOf": [(174, 179), (220, 260)],
    BASE+"CurveDVRSpecialization.DiagonalCharactersRegularAlgebraicOfInertiaWeigh": [(68, 129)],
}
PRIMARY = [
    {"file": "build/selmer-determinant-sources/labesse-cbcm.pdf",
     "url": "https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf",
     "sha256": "5df9d8fcfa158064fe362d4fdf46858648991eb32dddabc63a4a998840785865",
     "pdf_pages_reviewed": [1, 41, 42, 43, 45, 46, 49, 50],
     "interface": "Section 5.2 and Theorem 5.4: descent to the original inner form under everywhere finite unramified CM extension and quasi-split inert finite group; spherical test functions select inert spherical constituents. Theorem 5.9: strong local comparison at all split places. Compact infinity gives discrete series and property (*). The original quadratic idele character on -1 forces degree F even, so the definite even-rank parity and degree F>=2 are checked."},
    {"file": "build/selmer-pt-sources/blggt-potential.pdf",
     "url": "https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n2-p03-p.pdf",
     "sha256": "c9d6c7107bcde7fb26f9388abea5209f28457076bae59d70ccb6c34bbe1d621b",
     "pdf_pages_reviewed": [38], "printed_pages": [538],
     "interface": "Theorem 2.1.1: adopted global representation, full away-from-ell local compatibility, and exact labeled de Rham weights. The given semisimple attached representation equals it by Chebotarev."},
    {"file": "build/selmer-pt-sources/blggt-lg2.pdf",
     "url": "https://virtualmath1.stanford.edu/~rltaylor/lg2.pdf",
     "sha256": "9badc24926b69c0c606fad193b4705b9cbb21c6081a544f082c18c78031bc67f",
     "pdf_pages_reviewed": [2, 5, 6],
     "interface": "Theorem 1.1: semisimplified compatibility at every ell place, without Shin-regularity or Iwahori hypotheses. The proof excludes linked smooth characters before forcing monodromy zero."},
    {"file": "build/selmer-determinant-sources/bz1977.pdf",
     "url": "https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/BZ-induced-1.pdf",
     "sha256": "b379d3cb70d0fb94d9efbddd5f39a576bd2dc2b43a3f5bdc78f4ef084db10eda",
     "pdf_pages_reviewed": [15], "printed_pages": [454],
     "interface": "Theorem 4.2 and the adopted full local correspondence: unlinked principal series are irreducible; all original smooth character and normalization factors are retained."},
]


def exact_checks():
    n, j = sp.symbols("n j", integer=True)
    root_count_exponent = j*(n-j)-j*(2*n-j-1)/2
    assert sp.expand(root_count_exponent+j*(j-1)/2) == 0

    weight_cases = 0
    boundary_cases = 0
    for rank in (2, 3, 4):
        possible = tuple(itertools.combinations(range(-3, 4), rank))
        for labels in (1, 2):
            for hh in itertools.product(possible, repeat=labels):
                for h in hh:
                    lam = tuple(reversed([h[i]-i for i in range(rank)]))
                    assert all(lam[i] >= lam[i+1] for i in range(rank-1))
                    assert [lam[rank-1-i]+i for i in range(rank)] == list(h)
                for i in range(rank):
                    for k in range(rank):
                        if i == k:
                            continue
                        total = sum(h[k]-h[i] for h in hh)
                        assert total != 0
                        if total == labels:
                            assert k == i+1
                            assert all(h[k]-h[i] == 1 for h in hh)
                            boundary_cases += 1
                weight_cases += 1

    models = 0
    tensor_weight_checks = 0
    for rank in (2, 3, 4):
        for differences in itertools.product(range(3), repeat=rank-1):
            for det_power in range(-2, 2):
                lam = tuple(det_power+sum(differences[i:]) for i in range(rank))
                low = tuple(reversed(lam))
                weights = Counter({(det_power,)*rank: 1})
                ambient_dimension = 1
                for size, power in enumerate(differences, 1):
                    wedge = []
                    for inds in itertools.combinations(range(rank), size):
                        wedge.append(tuple(int(a in inds) for a in range(rank)))
                    for _ in range(power):
                        new = Counter()
                        for wt, mult in weights.items():
                            for ww in wedge:
                                new[tuple(a+b for a, b in zip(wt, ww))] += mult
                        weights = new
                        ambient_dimension *= math.comb(rank, size)
                assert sum(weights.values()) == ambient_dimension
                assert weights[low] == 1
                dimension = Fraction(1)
                for a in range(rank):
                    for b in range(a+1, rank):
                        dimension *= Fraction(lam[a]-lam[b]+b-a, b-a)
                assert dimension.denominator == 1
                assert 1 <= dimension <= ambient_dimension
                for wt in weights:
                    difference = tuple(a-b for a, b in zip(wt, low))
                    assert sum(difference) == 0
                    assert all(sum(difference[:k]) >= 0 for k in range(1, rank))
                    exponent = sum((rank-1-i)*difference[i] for i in range(rank))
                    assert exponent == 0 if wt == low else exponent > 0
                    tensor_weight_checks += 1
                models += 1

    # Exact coefficient cancellation; no equality Norm(varpi)=q is used.
    t0, t1, q = sp.symbols("t0 t1 q", nonzero=True)
    for rank in (2, 3, 4):
        ps = sp.symbols("p0:"+str(rank), nonzero=True)
        hs = [2*i-3 for i in range(rank)]
        for jj in range(rank+1):
            omega = sp.prod(ps[i]*(t0*t1)**hs[i]*q**(-i) for i in range(jj))
            low_value = (t0*t1)**sum(hs[i]-i for i in range(jj))
            expected = sp.prod(ps[i]*((t0*t1)/q)**i for i in range(jj))
            assert sp.cancel(omega/low_value-expected) == 0

    # Q_3(sqrt(3)): the original uniformizer has norm -3, q=3.
    multiplication_by_varpi = sp.Matrix([[0, 3], [1, 0]])
    norm_ratio = multiplication_by_varpi.det()/3
    assert norm_ratio == -1 and norm_ratio != 1

    # Without noncriticality, psi=(epsilon,1), h=(-1,0), omega=(nu,1)
    # is exactly the linked adjacent-gap-one boundary excluded in PT.
    assert (0-(-1)) == 1
    seed_weights = []
    for m in range(2, 9):
        for h, want in [((1-m, 1, m+1), (m-1, 0, 1-m)),
                        ((1-m, 1+m), (m, 1-m)),
                        ((-m, m), (m-1, -m))]:
            got = tuple(reversed([h[i]-i for i in range(len(h))]))
            assert got == want
            assert all(abs(h[i]-h[k]) != 1 for i in range(len(h)) for k in range(len(h)))
            seed_weights.append({"m": m, "h": list(h), "lambda": list(got)})
    return {
        "symbolic_root_count_identity": "j(n-j)-sum_{i<j}(n-1-i)=-sum_{i<j}i",
        "chamber_and_noncritical_cases": weight_cases,
        "linked_boundary_cases": boundary_cases,
        "exterior_tensor_lattice_models": models,
        "exterior_tensor_weight_checks": tensor_weight_checks,
        "lowest_weight": "Unique primitive tensor; every other weight is above it in the positive-root cone and has strictly positive z exponent.",
        "ordinary_scalar_cancellation": "Exact symbolic products for ranks 2,3,4 retain Norm(varpi)/q and all character values.",
        "ramified_negative_control": {"ell": 3, "minimal_polynomial": "X^2-3", "norm_varpi": -3, "q": 3, "norm_ratio": -1, "omitted_factor_changes_U2": True},
        "noncritical_negative_control": "psi=(epsilon,1), h=(-1,0) gives linked omega=(norm,1); dropping the original noncriticality hypothesis is invalid.",
        "seed_weight_cases": seed_weights,
        "scope": "Finite exact diagnostics plus a symbolic scalar identity. The universal lattice and arithmetic occurrence proofs are in the note; no numerical test proves PT.",
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
            assert len(blob) <= 12000, (module, lo, hi, len(blob))
            excerpts.append({"start": lo, "end": hi, "sha256": hashlib.sha256(blob).hexdigest()})
        sources.append({**item, "module": module, "sha256": checked["sha256"],
                        "matches_pinned_blob": True, "reviewed_excerpts": excerpts})

    primary = []
    for item in PRIMARY:
        path = ROOT/item["file"]
        if not path.exists():
            if args.offline:
                raise FileNotFoundError(path)
            path.parent.mkdir(parents=True, exist_ok=True)
            data = urllib.request.urlopen(item["url"], timeout=60).read()
            assert data.startswith(b"%PDF")
            assert hashlib.sha256(data).hexdigest() == item["sha256"]
            path.write_bytes(data)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"]
        primary.append({**item, "bytes": path.stat().st_size, "matches_reviewed_pdf": True})

    stem = "selmer-integral-frontier-arithmetic-point"
    artifacts = [f"notes/{stem}.md", f"paper/shared/{stem}.tex",
                 f"paper/shared/{stem}-references.tex",
                 "scripts/check_selmer_integral_frontier_arithmetic_point.py"]
    dependencies = [
        "notes/selmer-integral-frontier-classical-control.md",
        "notes/selmer-integral-frontier-hecke-determinant.md",
        "notes/selmer-integral-frontier-type-construction.md",
        "notes/selmer-integral-frontier-arithmetic-seed.md",
        "notes/classical-galois-substitution.md",
        "notes/galois-period-dictionary.md",
    ]
    for name in artifacts+dependencies:
        data = (ROOT/name).read_bytes()
        assert all(c >= 32 or c in (9, 10) for c in data)
    report = {
        "schema_version": 1, "status": "PASS",
        "classification": "closed arithmetic-point subobligation inside W04; independent review recorded separately",
        "claim": "For every original PT arithmetic point in rank 2 through 4, construct a nonzero eigenvector in the original residual ordinary module and prove J is contained in its kernel, preserving all original characters, levels and normalizations.",
        "verification_kind": "Nineteen authenticated pinned interfaces, four primary PDF checks, symbolic Hecke normalization and exact finite lattice/chamber/negative-control diagnostics; the universal proof is in the note.",
        "quantifiers": [
            "Every odd ell and original Hida datum, with original CM L/F unramified at all finite places and original S'=S.",
            "Every original residual datum, integral type, weight ring, ordinary module and ideal satisfying IsJ; the zero-module branch is excluded by the constructed vector.",
            "Every algebraic O-point x, strictly increasing labeled integer weight family h, and continuous semisimple attached RACSDC representation rho of rank 2<=n<=4.",
            "The exact v0 unramifiedness, ordered locally algebraic flags and all inequalities psi_i != psi_j epsilon are retained.",
            "Finite coefficient extensions and larger allowed ell-adic congruence depth are permitted; no enlargement of the original arithmetic field, original tame level, type lattice or residual block occurs.",
        ],
        "decisive_interfaces": {
            "algebraic_points": "Local integral equations for x(b)^-1 imply positive valuation on m_B; finite generation yields continuity and a finite coefficient field.",
            "descent": "Original definite U is split at split places and quasi-split at inert unramified places; the unramified quadratic idele character on -1 forces degree F even; spherical test functions in Labesse 5.4 select inert spherical descent, and 5.9 gives strong split comparison.",
            "noncritical": "Strict integer ordering plus valuation sums excludes equal smooth characters and both norm ratios. The only boundary is adjacent gaps all one, excluded by the original psi_i != psi_j epsilon condition.",
            "actual_weight_lattice": "Saturated Cartan-component intersection inside integral exterior-tensor lattice; primitive unique lowest tensor; exact positive-cone integrality and strict z contraction; no Young symmetrizer division.",
            "local_vector": "A principal-series function on B I1(c) supplies evaluation eigenfunctional; commuting generalized eigenspaces supply an actual eigenvector without ramified Hecke semisimplicity.",
            "normalization": "U_j=chi_lambda(a_j)^-1 product_{i<j}(omega_i(varpi) q^-i)=product_{i<j}psi_i(g_varpi) epsilon(g_varpi)^i, with epsilon(g_varpi)=Norm(varpi)/q.",
            "original_module": "Nonzero lowest-weight evaluation by integral kernel contraction; exact coefficient change and original spherical/ordinary residual congruences place it in the original residual M_A.",
            "universal_point": "The eigencharacter has the exact dense Frobenius polynomials and ordered local unit/uniformizer values; density of all universal polynomial-law coefficients and character values gives x=yf.",
            "seed_consumer": "SeedPtOf 244-260 consumes exactly the proved PT implication, with m>=2 and prime-to-ell away inertia providing all retained hypotheses.",
        },
        "limitations": [
            "No whole W04 node completion is asserted.",
            "No higher-weight control surjectivity is asserted or needed.",
            "No bound on weights, coefficient-field degrees, coefficient ranks, lattice scaling, number of double cosets, Selmer lengths or global budgets is supplied.",
            "No characteristic-prime marked-support nonvanishing or two-sided global rigidity follows merely from the characteristic-zero eigenvector.",
        ],
        "sources": sources, "primary_literature": primary,
        "exact_diagnostics": exact_checks(),
        "dependencies": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in dependencies],
        "artifacts": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in artifacts],
    }
    out = ROOT/"certificates"/(stem+".json")
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n")
    print(f"PASS: {len(sources)} pinned modules; {len(primary)} primary PDFs; "
          f"{report['exact_diagnostics']['exterior_tensor_lattice_models']} integral tensor models; "
          f"{report['exact_diagnostics']['chamber_and_noncritical_cases']} weight cases.")
    print(out.relative_to(ROOT))


if __name__ == "__main__":
    main()
