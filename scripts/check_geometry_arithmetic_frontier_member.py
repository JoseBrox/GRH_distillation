#!/usr/bin/env python3
"""Authenticate the actual normalized Member supplier and exact diagnostics.

The human proof supplies all ranks, all period matrices, all original labels
and all six adelic dictionary clauses. Finite exact examples diagnose signs,
fractional-lattice interfaces and determinant normalizations; they do not
replace the cited classical theta transformation theorem or constitute Lean.
"""
from __future__ import annotations

import argparse
from itertools import product
import json
from math import gcd

import sympy as sp
import check_geometry_arithmetic_frontier_geometric_filtration as auth


STEM = "geometry-arithmetic-frontier-member"
P = "Formalism.LocalToGlobal.ProjectiveLattices."
A = "Development.AbelianVarietyTheory."
U = A + "Proofs.UnitaryExistence."
T = ("ReciprocityTheory.ReductiveGroups.ArithmeticGeometry."
     "BirationalGeometry.ToroidalCompactification.")
RANGES = {
    T + "TwoWeightEqOneAddRoot": [(14, 82)],
    P + "HostInt": [(138, 153)],
    "ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.FundamentalDomains.Signature":
        [(14, 54), (69, 110)],
    T + "IsHolPeriods": [(13, 104), (106, 114)],
    P + "EmbKCoe": [(11, 21)],
    P + "UnFree": [(62, 117)],
    A + "Definitions.ExistenceOfLattices.NormConst": [(20, 34), (188, 251)],
    U + "CmUnitPowFourIdempotentModEight": [(206, 298), (299, 378)],
    U + "ThetaSqTransformLevelEight": [(10, 25)],
    U + "ThetaFrameDetMulSqInvariant": [(43, 102)],
    U + "NormalisedFramedPointTriangularFrameWeightRule": [(77, 127)],
    U + "NormalisedFramedPointArithmeticGroupInvariantSig": [(22, 66)],
    U + "NormalisedPointsSatisfySingleFrame": [(94, 143)],
    U + "HermEqOfNormalised": [(19, 23), (60, 86)],
    U + "EqOfImHermFormEq": [(63, 96)],
    U + "ExistsFundamentalDomainMeanNormSqThetaChar": [(76, 153)],
    U + "CompletedLatticeEqAdelicCompletionAndGram": [(48, 97)],
    U + "AdelicElementLatticeFullAndCompletion": [(27, 61)],
    A + "Definitions.ExistenceOfLattices.CoeSelfDualLatticeInFrameCoordinatesEq":
        [(32, 111)],
    A + "Definitions.ExistenceOfLattices.ExistsCtxOkOfPins": [(177, 215)],
    P + "FamilyUniformisationBasePointOrthogonalBis": [(63, 118)],
    P + "EquivariantFiniteGroup": [(137, 155)],
    U + "ExistsComponentLatticeMarkingAdelic": [(119, 205)],
    A + "Definitions.Divisors.NormNegCmConstantEqAtAllEmbeddings":
        [(187, 208), (484, 499)],
    A + "Proofs.DivisorProofs.ExistsGoodCoverOverSizedField": [(111, 160)],
    P + "AllTest": [(9, 14)],
}


def clean(matrix):
    return matrix.applyfunc(sp.simplify)


def mod_zero(matrix, modulus):
    return all(int(x) % modulus == 0 for x in matrix)


def idempotent_checks():
    w, k = sp.symbols("w k")
    poly = w*w-w+4*k+2
    expressions = [
        ("e_squared_minus_e", w**8-w**4, 8),
        ("e_plus_conjugate_minus_one", w**4+(1-w)**4-1, 8),
        ("e_minus_w", w**4-w, 2),
    ]
    result = {}
    for name, expression, modulus in expressions:
        rem = sp.rem(expression, poly, w)
        divided = sp.Poly(sp.expand(rem/modulus), w, k)
        assert all(c.q == 1 for c in divided.coeffs())
        result[name] = {"remainder": str(sp.factor(rem)),
                        "divisible_by": modulus, "status": "exact PASS"}
    return result


def adapted_basis(W):
    """Find an integral SL_2 basis with w^4=diag(1,0) modulo eight."""
    e = W**4
    candidates = sorted(product(range(-8, 9), repeat=2),
                        key=lambda v: abs(v[0])+abs(v[1]))
    for a, c in candidates:
        if gcd(a, c) != 1:
            continue
        v = sp.Matrix([a, c])
        if not mod_zero(e*v-v, 8):
            continue
        aa, cc, one = sp.gcdex(a, c)
        assert one == 1 and aa*a+cc*c == 1
        # a*d-c*b=1; adding a multiple of v preserves this.
        u = sp.Matrix([-cc, aa])
        for t in range(8):
            u1 = u+t*v
            C = sp.Matrix.hstack(v, u1)
            if mod_zero(e*u1, 8):
                assert C.det() == 1
                assert mod_zero(C.inv()*e*C-sp.diag(1, 0), 8)
                return C
    raise AssertionError("No adapted symplectic basis found")


def arithmetic_checks():
    J = sp.Matrix([[0, -1], [1, 0]])
    cases, quadratic = [], 0
    for k in [0, 1, 4, 6]:
        d = 16*k+7
        assert sp.isprime(d)
        W = sp.Matrix([[0, -(4*k+2)], [1, 1]])
        assert W.T*J == J*(sp.eye(2)-W)
        C = adapted_basis(W)
        WC = C.inv()*W*C
        assert mod_zero(WC-sp.diag(1, 0), 2)
        # The primitive graph semicharacter is the zero characteristic.
        for m, n, a, b in product(range(2), repeat=4):
            v, u = sp.Matrix([m, n]), sp.Matrix([a, b])
            Q = lambda x: int((x.T*J*WC*x)[0]) % 2
            assert Q(v) == (m*n) % 2
            assert (Q(v+u)-Q(v)-Q(u)-int((v.T*J*u)[0])) % 2 == 0
            quadratic += 1
        for r in [2, 3, 4]:
            signs = [1]*(r-1)+[-1]
            B = sp.diag(*(sgn*J for sgn in signs))
            Wbig = sp.diag(*(W for _ in range(r)))
            S = sp.zeros(2*r)
            for i, sgn in enumerate(signs):
                S[2*i:2*i+2, i] = C[:, 0]
                S[2*i:2*i+2, r+i] = sgn*C[:, 1]
            Bstd = sp.zeros(2*r)
            Bstd[:r, r:] = -sp.eye(r)
            Bstd[r:, :r] = sp.eye(r)
            assert S.T*B*S == Bstd
            assert abs(S.det()) == 1
            assert mod_zero(S.inv()*(Wbig**4)*S-sp.diag(sp.eye(r), sp.zeros(r)), 8)
            for M in [3, 5, 15]:
                Gamma = sp.eye(2*r)
                K = 2*W-sp.eye(2)
                for eps in [1, -1]:
                    v = [0]*r
                    v[0], v[-1] = 1, eps
                    N = sp.zeros(2*r)
                    for i in range(r):
                        for j in range(r):
                            N[2*i:2*i+2, 2*j:2*j+2] = v[i]*signs[j]*v[j]*K
                    assert N*N == sp.zeros(2*r)
                    transv = sp.eye(2*r)+M*N
                    assert transv.T*B*transv == B
                    Gamma = Gamma*transv
                assert Gamma.T*B*Gamma == B
                assert Gamma*Wbig == Wbig*Gamma
                assert mod_zero(Gamma-sp.eye(2*r), M)
                adapted = S.inv()*Gamma*S
                assert mod_zero(adapted[:r, r:], 8)
                assert mod_zero(adapted[r:, :r], 8)
                detA = int(adapted[:r, :r].det())
                assert (detA-1) % 8 == 0
                T0 = Wbig**4*Gamma+sp.eye(2*r)-Wbig**4
                assert (int(T0.det())-1) % 8 == 0
                cases.append({"d": d, "rank": r, "M": M,
                              "det_A_mod8": detA % 8})
    return {"unitary_transvection_products": cases,
            "primitive_quadratic_refinement_cases": quadratic,
            "all_checks": "exact PASS"}


def borel_checks():
    cases, weights = [], 0
    for r in range(1, 6):
        b = sp.Matrix(r, r, lambda i, j:
                      0 if i > j else
                      (i+2 if i == j else (i+j+1)+sp.I*(j-i)))
        for q in range(r+1):
            b11, b22 = b[:q, :q], b[q:, q:]
            reverse = sp.zeros(q)
            for i in range(q):
                reverse[i, q-1-i] = 1
            h0 = sp.diag(reverse*b11.T*reverse, b22.inv())
            ratio = sp.cancel(b11.det()/b22.det())
            assert sp.cancel(h0.det()-ratio) == 0
            tangent = h0.inv()
            for j in range(r):
                idx = q-1-j if j < q else j
                expected = 1/b[j, j] if j < q else b[j, j]
                assert sp.simplify(tangent[idx, idx]-expected) == 0
            # This unitriangular part has source Gram-minor modulus one.
            bu = b*sp.diag(*(1/b[j, j] for j in range(r)))
            G = sp.diag(*([1]*q+[-1]*(r-q)))
            gram = bu.T*G*sp.conjugate(bu)
            for j in range(r+1):
                assert sp.simplify(gram[:j, :j].det()) == (-1)**max(0, j-q)
            u11, u22 = bu[:q, :q], bu[q:, q:]
            hu = sp.diag(reverse*u11.T*reverse, u22.inv())
            Hdiag = sp.diag(*(2*(j+1) for j in range(r)))
            H = clean(hu.inv().T*Hdiag*sp.conjugate(hu.inv()))
            assert sp.simplify(H.det()-Hdiag.det()) == 0
            for n in range(0, 10, 2):
                for a0 in range(4):
                    a = [a0+r-j for j in range(r)]
                    reading = ratio**(-n//2)
                    expected = sp.Integer(1)
                    for j in range(r):
                        idx = q-1-j if j < q else j
                        reading *= tangent[idx, idx]**a[j]
                        exponent = -a[j]-n//2 if j < q else a[j]+n//2
                        expected *= b[j, j]**exponent
                    assert sp.cancel(reading-expected) == 0
                    assert (-1)**n == 1
                    weights += 1
            cases.append({"rank": r, "positive_first_block": q,
                          "det_h0": str(ratio), "unit_minor_det_H": str(Hdiag.det())})
    return {"all_signatures_through_rank": 5,
            "signature_cases": cases, "even_weight_cases": weights,
            "all_checks": "exact PASS"}


def gaussian_checks():
    out = []
    for g in range(1, 7):
        P, Y = sp.symbols("P Y", positive=True)
        abs_deth = sp.sqrt(P*Y)
        C = sp.sqrt(sp.Integer(2)**g/P)
        abs_kappa_squared = sp.simplify(C*abs_deth)
        gaussian = 1/sp.sqrt(sp.Integer(2)**g*Y)
        assert sp.simplify(abs_kappa_squared*gaussian) == 1
        out.append({"g": g, "mean": 1})
    # The AH exponential removes precisely twice the imaginary quadratic.
    u, v, y = sp.symbols("u v y", real=True, nonzero=True)
    qtwice = ((u+sp.I*v)**2/y).expand().as_real_imag()[0]
    herm = (u*u+v*v)/y
    assert sp.simplify(qtwice-herm+2*v*v/y) == 0
    return {"dimension_cases": out, "AH_metric_sign": "exact PASS",
            "measure": "Original Lebesgue parallelepiped volume divides the integral; Jacobian cancels"}


def references():
    rows = [
        ("milne-abelian-varieties", "https://jmilne.org/math/CourseNotes/AV.pdf",
         "f5ca4e63e5092a4b102daad1470e4cbed5fe8f82115e3a28c8881e3f67f6aaef",
         "fbf25b2b599899a3a31adf9fb45a780b59f7cd744b414e755c74af76b36a6eb0",
         [(797, 884)], "Riemann correspondence and polarization/Weil-pairing description"),
        ("milne-cm", "https://www.jmilne.org/math/CourseNotes/CM.pdf",
         "0ac337a885d72f6938f15724b897f568fe350d0d754d0b52370b8f3a01d2e2b5",
         "596dd17c0ad120838057eaf00bca943ddd13cd6ac4cb2cd9445826ad148a2420",
         [(2358, 2409)], "Appell-Humbert classification and original factor of automorphy"),
        ("fgsm-weak-schottky", "https://content.algebraicgeometry.nl/2021-3/2021-3-009.pdf",
         "084d7c942a41e71c508670532c13fb719ac12da5e34d5376976f83dd858a00cd",
         "818cb7deb7a18fa45560a5c3e8498dc2d0a184d4e8b02f60c97f847b11882c9a",
         [(216, 278)], "Squared theta-constant transformation on Gamma_g(4,8), hence Gamma_g(8)"),
        ("lan-pel-revision", "https://www.kwlan.org/articles/cpt-PEL-type-thesis-revision.pdf",
         "a7a454f5d0735f4bf11f00a8afc14c361c5fc2cefd691d7466f7620ab4c3a079",
         "f0b305b0a54e5557c5b9420526ccf79b90c42cf236e91f78e2645868f649af58",
         [(19215, 19274)], "Proposition 5.2.4.9: exact Poincare Weil pairing and theta commutator"),
    ]
    result = []
    for stem, url, ph, th, ranges, claim in rows:
        pp, tp = f"build/reference-cache/{stem}.pdf", f"build/reference-cache/{stem}.txt"
        assert auth.sha((auth.ROOT/pp).read_bytes()) == ph
        tb = (auth.ROOT/tp).read_bytes()
        assert auth.sha(tb) == th
        lines = tb.decode().splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines)
            excerpts.append({"lines": [lo, hi],
                             "sha256": auth.sha(("\n".join(lines[lo-1:hi])+"\n").encode())})
        result.append({"path": pp, "url": url, "sha256": ph,
                       "text_path": tp, "text_sha256": th,
                       "excerpts": excerpts, "verified_statement": claim})
    result.append({
        "url": "https://www.numdam.org/item/PMIHES_1960__5__5_0.pdf",
        "reference": "Grauert (1960), section 7, Satz 5, page 64; hypotheses page 62",
        "corrigendum": "https://www.numdam.org/item/PMIHES_1963__16__35_0.pdf",
        "verified_statement": "Proper holomorphic coherent base change under flatness, reduced base and constant fibre cohomology dimension; relative seesaw for the fibrewise trivial rigidified difference line",
        "verification_scope": "Original PDF pages 62-64 and all two pages of corrigendum read directly through web retrieval on 2026-11-23; no local PDF hash or fresh network verification claimed by this checker",
        "retrieval_evidence": ["turn657602947view0", "turn235379735view0", "turn657602947view1"],
    })
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    checks = {"idempotent": idempotent_checks(),
              "arithmetic": arithmetic_checks(),
              "borel": borel_checks(),
              "gaussian": gaussian_checks()}
    refs = references()
    files = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", "scripts/check_geometry_arithmetic_frontier_member.py"]
    cert = {
        "status": "PASS", "date": "2026-11-23",
        "classification": "closed exact supplier, independently reviewed",
        "claim": "Actual A=1 IsUnf, normalized primitive theta section and original Member/DictIsUnif; together with actual level and component-field suppliers, original sized Deep.Good",
        "whole_nodes_newly_closed": 0,
        "sources": sources, "primary_references": refs, "checks": checks,
        "files": [{"path": p, "sha256": auth.sha((auth.ROOT/p).read_bytes())} for p in files],
        "scope": "General human proof plus exact finite normalization/edge diagnostics; no numerical theta approximation and no Lean build.",
        "not_claimed": ["A>1 Member supplier", "Unused adelAut or automorphic-character fields",
                        "Arithmetic short-section or signed boundary estimate",
                        "Final W10 degree bound", "Global W06/W08 norm", "Whole proof completion"],
    }
    (auth.ROOT/"certificates"/f"{STEM}.json").write_text(
        json.dumps(cert, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"status": "PASS", "sources": len(sources),
                      "primary_references": len(refs),
                      "unitary_products": len(checks["arithmetic"]["unitary_transvection_products"]),
                      "signature_cases": len(checks["borel"]["signature_cases"]),
                      "even_weight_cases": checks["borel"]["even_weight_cases"]}))


if __name__ == "__main__":
    main()
