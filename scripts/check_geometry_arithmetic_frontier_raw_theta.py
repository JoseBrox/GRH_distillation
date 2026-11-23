#!/usr/bin/env python3
"""Authenticate the actual raw theta construction and exact finite scalars.

Finite diagnostics test normalization traps, not the general geometric proof.
No Lean build, theta spanning theorem, or archimedean norm bound is claimed.
"""
from __future__ import annotations

import argparse
from itertools import product
import json
from math import gcd
import subprocess
import urllib.request

import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth

STEM = "geometry-arithmetic-frontier-raw-theta"
P = "Formalism.LocalToGlobal.ProjectiveLattices."
C = "Development.AbelianVarietyTheory.Proofs.CuspFormEvaluations."
S = "Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation."
D = "Development.AbelianVarietyTheory.Proofs.DivisorProofs."
F = "Development.AbelianVarietyTheory.Definitions.Foundations."
V = "Development.AbelianVarietyTheory.Definitions.Divisors."
FD = "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.FundamentalDomains."
RANGES = {
    P + "ThClass": [(17, 59)],
    P + "ThShort": [(45, 110), (235, 269)],
    P + "ThProps": [(20, 30)],
    P + "EmbKCoe": [(11, 21)],
    P + "AlgebraMapCAt": [(30, 54)],
    P + "AllTest": [(9, 14)],
    C + "ExistsFaithfullyFlatCoverShortThetaValueData": [(34, 95)],
    C + "InZhGeoInjStable": [(66, 119)],
    C + "TorsionIsotropicCommutatorPairing": [(30, 87), (109, 140)],
    C + "SqDvdSumAlternatingFormsOfKilledLattice": [(13, 37)],
    C + "UniversalSymLiftExistsUniqueGlobal": [(19, 44)],
    C + "ThetaGroupShiftHalfTorsionRoot": [(58, 90)],
    C + "IsotropicSumIndependentOfChoicesLocal": [(41, 104), (105, 145)],
    C + "ShortThetaSumEqOfWitnessesCommonAlgebra": [(28, 78), (88, 109)],
    C + "ShortThetaValueExistsUniqueNaturalOfLaws": [(42, 76)],
    C + "HarmonicSumTriangularFrameChange": [(113, 158), (160, 178)],
    C + "ThetaValueWeightTriangularFrame": [(261, 289)],
    C + "ThetaRuleMemSec": [(17, 46)],
    C + "ThetaRuleExistsAndEval": [(24, 39)],
    S + "ExistsEvenRepsTensorLatticeAndSum": [(106, 147), (150, 214)],
    S + "SectionsReadAsTranslatesAtScaledPoint": [(23, 72)],
    S + "HarmonicConnectionValueEqPolynomialDerivative": [(19, 30)],
    S + "ShortThetaValueComplexPointEqClassicalTheta": [(194, 264)],
    D + "HolSub0LeSpanRaw": [(108, 137), (146, 176)],
    D + "ThFamMono": [(31, 38)],
    F + "IsProbabilityMeasureMuPart": [(232, 236), (425, 440)],
    V + "NormNegCmConstantEqAtAllEmbeddings": [(49, 64), (230, 250)],
    P + "EquivariantFiniteGroup": [(20, 49)],
    S + "ExistsLetterRowWeightDictionary": [(107, 147)],
    S + "ShortThetaSeriesDominantWeightIsCuspForm": [(24, 44)],
    "Development.AbelianVarietyTheory.Definitions.ThetaValues.ExistsMemRowHighestTotalDegreeEqTwo":
        [(17, 29), (319, 387)],
    C + "IsHarmonicAndMemMinorSpan": [(19, 38), (56, 68), (82, 112), (118, 180),
                                      (189, 218), (238, 276), (291, 342), (348, 436),
                                      (437, 474), (536, 633), (663, 710)],
    C + "MatRmulUnipMulHeadProj": [(21, 51), (126, 172), (316, 381)],
    C + "FirstMinimumPrincipalTorusAtOrthonormalFrame": [(373, 483)],
    C + "FirstMinimumEqZeroOfRankZero": [(512, 550)],
    FD + "Signature": [(91, 145)],
    FD + "ModerateCoefficientPositivity": [(27, 59)],
}


def references(offline):
    stem = "miller-schmid-rapid-decay"
    url = "https://arxiv.org/pdf/1106.2149v1"
    pdf = auth.ROOT / "build/reference-cache" / f"{stem}.pdf"
    txt = pdf.with_suffix(".txt")
    if not pdf.exists():
        if offline:
            raise FileNotFoundError(pdf)
        pdf.parent.mkdir(parents=True, exist_ok=True)
        pdf.write_bytes(urllib.request.urlopen(url, timeout=60).read())
    if not txt.exists():
        subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], check=True)
    ph = "83a460ea43560fad40d630621e4078be72b4d8e14f18d85736f29f429d41a02e"
    th = "7ad0c7e5fb4be2d7875acfad1db15e5f65167da80541ed83e4ab68318a3a95c8"
    assert auth.sha(pdf.read_bytes()) == ph
    tb = txt.read_bytes()
    assert auth.sha(tb) == th
    lines = tb.decode().split("\n")
    ranges = [(82, 100), (201, 226), (310, 325), (429, 445), (1157, 1183)]
    return [{
        "reference": "Miller--Schmid, arXiv:1106.2149v1, Theorem A and equation (6.1)",
        "url": url, "pdf_path": str(pdf.relative_to(auth.ROOT)), "pdf_sha256": ph,
        "text_path": str(txt.relative_to(auth.ROOT)), "text_sha256": th,
        "line_convention": "Newline-delimited pdftotext -layout output; form-feed characters do not add lines",
        "excerpts": [{"lines": [lo, hi],
                      "sha256": auth.sha(("\n".join(lines[lo-1:hi])+"\n").encode())}
                     for lo, hi in ranges],
        "verified_statement": "Rapid decay on every Siegel set for a smooth cuspidal automorphic form of moderate growth, finite under the center of the enveloping algebra, on the stated reductive group with compact real center. The proof separately verifies all these hypotheses for the original theta reading.",
    }]


def diagnostics():
    # Odd torsion, including composite and prime-square levels.  Work with
    # exact root exponents: products of individual commutators can be one
    # while none of those individual commutators is one.
    commutators = 0
    nontrivial_column_examples = 0
    permutation_cases = 0
    for N in [1, 3, 5, 9, 15]:
        m = N*N
        assert gcd(2, m) == 1
        inv2 = pow(2, -1, m) if m > 1 else 0
        for a in range(m):
            for b in [0, 1 % m, (m-1) % m]:
                exponents = [a, b, (-a-b) % m]
                roots = [(inv2*e) % m for e in exponents]
                assert all((2*r-e) % m == 0 for r, e in zip(roots, exponents))
                assert sum(roots) % m == 0
                commutators += 1
                nontrivial_column_examples += int(any(exponents))
        # This tests the full group, not a primitive orbit or one generator.
        for modulus in sorted({1, N, m}):
            for shift in range(modulus):
                assert sorted((x+shift) % modulus for x in range(modulus)) == list(range(modulus))
                assert sorted((2*x) % modulus for x in range(modulus)) == list(range(modulus))
                permutation_cases += 1

    # Polynomial Bezout identities work over nonreduced coefficient algebras.
    x = sp.symbols("x")
    for N in [1, 3, 5, 9, 15]:
        m = N*N
        assert sp.gcd(x**2-1, x**m-1) == x-1
        # If a^2=b^m and c=a*b^{-(m+1)/2}, then c^m=a^{-1}
        # and c^2=b^{-1}; verify the exponent reductions exactly.
        assert m-2*((m+1)//2) == -1
        assert m-(m+1) == -1

    # Actual annihilator constraints in a split hyperbolic local model:
    # Lambda has exponents (a,-a); N has valuation e.  The variables v
    # represent N^2-torsion v/N^2, and v/N belongs to Lambda exactly when
    # v_1 is divisible by p^(e+a), v_2 by p^(e-a).
    subgroup_cases = 0
    unequal_indices = 0
    for p, e in [(3, 1), (3, 2), (5, 1)]:
        N = p**e
        modulus = N*N
        for a in range(-e, e+1):
            rows = [(p**(e-a), 0), (0, p**(e+a))]
            points = [(u, v) for u, v in product(range(modulus), repeat=2)
                      if all((c*u+d*v) % modulus == 0 for c, d in rows)]
            expected = [(u, v) for u, v in product(range(modulus), repeat=2)
                        if u % p**(e+a) == 0 and v % p**(e-a) == 0]
            assert points == expected
            J = p**(2*e)
            I = p**(2*e-abs(a))
            assert len(points) == J
            assert J//I == p**abs(a)
            # Pairing with the hyperbolic dual swaps the two coordinates;
            # every product is divisible by N^2 on the full subgroup.
            for u, v in points:
                for u2, v2 in points:
                    assert (u*v2+v*u2) % modulus == 0
            subgroup_cases += 1
            unequal_indices += int(I != J)

    # The representative in the Heisenberg operator is u, while the
    # corresponding abelian torsion point is u/N.  Homogeneous derivative
    # scaling cancels the one actual N^d denominator.
    z0, z1, lam = sp.symbols("z0 z1 lam", nonzero=True)
    derivative_cases = 0
    for d0, d1 in product(range(4), repeat=2):
        phi = 7*z0**d0*z1**d1 + z0**(d0+1)*z1**(d1+2)
        original = sp.diff(phi, z0, d0, z1, d1).subs({z0:0, z1:0})
        scaled = sp.diff(phi.subs({z0:lam*z0, z1:lam*z1}), z0,d0,z1,d1).subs({z0:0,z1:0})
        assert sp.expand(scaled-lam**(d0+d1)*original) == 0
        derivative_cases += 1
    I,J,C0,N0,beta,kappa,value = sp.symbols("I J C0 N beta kappa value", nonzero=True)
    degree = sp.symbols("degree", integer=True, nonnegative=True)
    assert sp.cancel(J*kappa*N0**degree*value/(I*C0*N0**degree)
                     -J*kappa*value/(I*C0)) == 0
    assert sp.cancel(beta*(J*kappa*value/(beta*I*C0))-J*kappa*value/(I*C0)) == 0

    # Source rowAdd(a,b,s), a<b, adds the EARLIER row a to LATER row b.
    # Use the last nonzero coefficient of a row relation, including zero
    # rows and rectangular matrices with fewer columns than rows.
    elimination_cases = 0
    for p in range(1, 6):
        for n in range(0, 7):
            for seed in range(3):
                A = sp.Matrix(p, p-1, lambda i,j: ((i+1)*(j+2)+seed+i*j) % 7-3)
                B = sp.Matrix(p-1, n, lambda i,j: ((i+2)*(j+1)+seed+j*j) % 11-5)
                X = A*B
                relation = X.T.nullspace()[0]
                pivot = max(i for i in range(p) if relation[i] != 0)
                U = sp.eye(p)
                for i in range(pivot):
                    U[pivot,i] = relation[i]/relation[pivot]
                assert U.det() == 1
                assert all(U[i,j] == 0 for i in range(p) for j in range(i+1,p))
                assert (U*X)[pivot,:] == sp.zeros(1,n)
                elimination_cases += 1

    # The exact rectangular Borel gauge, including both independent
    # constraints.  It is not enough to remove only one component.
    gauge_cases = 0
    for q,p in product(range(1,4), repeat=2):
        r = p+q
        for seed in range(4):
            w = sp.Matrix([i+seed+1 for i in range(r)])
            ell = sp.Matrix([(-1)**i*(i+1) for i in range(r)])
            ell[r-1] = -sum(w[i]*ell[i] for i in range(r-1))/w[r-1]
            assert (w.T*ell)[0] == 0
            d = sp.zeros(p,1)
            e = sp.zeros(q,1)
            d[0] = 1/w[q]
            e[0] = 1/ell[0]
            t = sum(w[i]*ell[i] for i in range(q))
            K = sp.Matrix(q,p,lambda a,c:w[a]*d[c]-e[a]*ell[q+c]-t*e[a]*d[c])
            assert K*w[q:r,0] == w[:q,0]
            assert K.T*ell[:q,0] == -ell[q:r,0]
            gauge_cases += 1

    # Exact c^2/4 and 4*pi frequency relation, with complex cusp linear
    # forms and real characteristics.  Q*d=0 is tested separately: without
    # it, vanishing linear frequency does not imply translation invariance.
    ar, ai, br, bi, u0,u1,ct = sp.symbols("ar ai br bi u0 u1 ct", real=True)
    ell = sp.Matrix([ar+sp.I*ai,br+sp.I*bi])
    u = sp.Matrix([u0,u1])
    CM = ct**2*sp.re(ell*sp.conjugate(ell).T)
    nu = ct**2*sp.expand_complex((u.T*ell)[0]*sp.conjugate((u.T*ell)[0]))/4
    assert sp.simplify((u.T*CM*u)[0]-4*nu) == 0
    hd = -sp.I*ct*sp.conjugate(ell[0])/2
    he = sp.I*ct*ell[0]/2
    shifted_period = sp.I*ct*ell[1]*hd-sp.I*ct*sp.conjugate(ell[1])*he
    assert sp.expand_complex(sp.expand(shifted_period-CM[0,1])) == 0
    z = sp.Matrix(sp.symbols("z0:3"))
    tau = sp.symbols("tau")
    dv = sp.Matrix([1,2,3])
    ann = sp.Matrix([[-2,1,0],[-3,0,1]])
    QQ = ann.T*sp.diag(2,5)*ann
    assert QQ*dv == sp.zeros(3,1)
    assert sp.expand(((z+tau*dv).T*QQ*(z+tau*dv))[0]-(z.T*QQ*z)[0]) == 0
    assert sp.expand(((z+tau*dv).T*(z+tau*dv))[0]-(z.T*z)[0]) != 0
    # Missing positive row degree is also a genuine obstruction: the
    # row-highest polynomial X_11 survives at a rank-one 2-by-2 matrix.
    x00,x01,x10,x11,s = sp.symbols("x00 x01 x10 x11 s")
    short_minor = x00
    assert short_minor.subs({x10:x10+s*x00,x11:x11+s*x01}) == short_minor
    assert sp.Poly(short_minor,x00,x01,x10,x11).degree(x10) == 0
    assert sp.Poly(short_minor,x00,x01,x10,x11).degree(x11) == 0
    assert sp.Matrix([[1,0],[0,0]]).rank() == 1
    assert short_minor.subs({x00:1,x01:0,x10:0,x11:0}) == 1
    return {
        "odd_commutator_models": commutators,
        "models_with_nontrivial_individual_columns": nontrivial_column_examples,
        "full_group_translation_and_even_representative_cases": permutation_cases,
        "nonreduced_cancellation": "Exact polynomial gcd and odd-lift exponent identities",
        "annihilator_subgroup_models": subgroup_cases,
        "models_with_distinct_I_and_J": unequal_indices,
        "homogeneous_derivative_models": derivative_cases,
        "exact_complex_scalar": "J/(I C) times original kappa; beta_H and N^degree cancel exactly",
        "original_triangular_row_elimination_cases": elimination_cases,
        "two_constraint_split_gauge_cases": gauge_cases,
        "exact_cusp_frequency": "u^t C_tau u=4 nu_tau, with C_tau=c_tau^2 Re(ell ell*) and real u",
        "exact_period_shift_sign": "h d=-i c conjugate(ell)/2 and h e=+i c ell/2 give precisely C_tau under the original rank-one flow",
        "cusp_negative_controls": "Rank-deficient evaluation need not vanish when a row degree is zero; zero linear frequency does not remove a quadratic term unless Q d=0",
        "scope": "Finite exact diagnostics only; arbitrary-base algebraicity and general descent are proved in the shared text.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    primary = references(args.offline)
    checks = diagnostics()
    dependencies = [
        "geometry-arithmetic-frontier-integral-theta",
        "geometry-arithmetic-frontier-good3",
        "geometry-arithmetic-frontier-level-cover",
        "geometry-arithmetic-frontier-member",
        "geometry-arithmetic-frontier-actual-theta-denominator",
    ]
    files = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", f"scripts/check_{STEM.replace('-','_')}.py"]
    rec = {
        "date":"2026-11-23", "status":"PASS",
        "classification":"Closed exact construction supplier; independent mathematical review recorded separately",
        "claim":"Original beta=1 raw theta sections over every coefficient algebra, with exact value, weight and classical scalar; actual cusp-space and integral-image membership in the original positive weight range",
        "whole_nodes_newly_closed":0,
        "sources":sources,
        "primary_references":primary,
        "dependencies":[{"path":f"paper/shared/{stem}.tex",
                         "sha256":auth.sha((auth.ROOT/f"paper/shared/{stem}.tex").read_bytes())}
                        for stem in dependencies],
        "checks":checks,
        "files":[{"path":path,"sha256":auth.sha((auth.ROOT/path).read_bytes())} for path in files],
        "preserved_quantifiers":[
            "Every original IsNab and framed point over every K-algebra, including nonreduced algebras",
            "Every original self-dual Lambda standard at M and every allowed odd N divisible by M",
            "Every original finite weight w and harmonic row-highest polynomial P",
            "Arbitrary coefficient maps and original FrMap relations",
            "All original finite theta witnesses and full torsion-group enumerations",
            "Original determinant-ideal scalars and valuation tests when the accepted denominator theorem applies",
            "Every original component and GoodEmb in the cusp target, with positive first-p row degrees from CovGmin.Hyp and definite endpoints separately checked",
        ],
        "not_claimed":["Full holomorphic cusp-space spanning", "Archimedean theta norm estimate",
                       "Nonzero image for every harmonic type", "Whole W06/W08/W10 closure", "Lean build"],
    }
    (auth.ROOT/"certificates"/f"{STEM}.json").write_text(json.dumps(rec,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"status":"PASS", "authenticated_modules":len(sources),
                      "finite_checks":checks},ensure_ascii=False))


if __name__ == "__main__":
    main()
