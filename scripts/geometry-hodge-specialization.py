#!/usr/bin/env python3
"""Authenticate the actual finite Hodge--Tate specialization proof.

Finite exact diagnostics test coset cocycles, the original pairing,
nonflat specialization, the different, and the quotient-image index.
They supplement the general proof; no Lean build is run.
"""
from __future__ import annotations

import argparse
from itertools import product
import json

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

import check_geometry_arithmetic_frontier_geometric_filtration as auth


STEM = "geometry-hodge-specialization"
GD = "Development.AutomorphicSpectrum.Definitions.GlobalGeometry."
GP = "Development.AutomorphicSpectrum.Proofs.GeometryProofs."
HP = "Development.WeilBound.CoreStatements.HodgeTatePoints."
PC = "Development.WeilBound.CoreStatements.PlurisubharmonicCones."
RANGES = {
    GD + "MemEigSpOfMemHtDual": [(20, 48), (53, 90)],
    GD + "IsHodgeLine": [(19, 29), (33, 74), (83, 91)],
    GD + "IntegralClosureHeightEqOneOfLiesOver": [(14, 27), (44, 47)],
    GP + "HtatLinkOf": [(25, 53), (55, 89)],
    HP + "WeilfunCore": [(26, 59), (67, 79), (115, 161)],
    HP + "Weilfun": [(10, 19)],
    HP + "TwhopfMain": [(47, 92)],
    HP + "TwpairAlg": [(117, 147)],
    HP + "GcChart": [(18, 67), (71, 111)],
    HP + "GhModelAlg": [(27, 73), (75, 110), (135, 216)],
    HP + "GhModel": [(53, 89), (93, 144)],
    PC + "AevalCyclotomic": [(81, 101), (230, 292)],
    PC + "InFibreLoc": [(59, 120), (121, 178)],
    PC + "AbelianPartIntegralPointBis": [(21, 66), (67, 120)],
    PC + "NormBound": [(50, 88), (90, 135)],
    GP + "HodgeTateOmegaCoherent": [(17, 80)],
    GP + "HodgeTateWeilPullback": [(145, 198), (201, 265)],
    GP + "HodgeCptProjectiveModel": [(173, 214), (270, 312), (317, 376)],
}


def references():
    rows = [
        {"path": "build/reference-cache/fargues-2011-canonical-torsion.pdf",
         "url": "https://www.numdam.org/item/10.24033/asens.2157.pdf",
         "sha256": "2fdb96d0c9c9d8a23fb90f0542d32f86155c6179ad494d925e7fe70e5a7b9888",
         "verified_scope": "Printed p.911: complete rank-one valuation, not necessarily discrete, arbitrary residue field. Printed p.933 Remark2: dyadic qualification. Printed p.935, section5.4 Theorem3: finite-flat Hodge--Tate cokernel annihilated at v>=1/(p-1), no p=2 exclusion. Applied to the Cartier dual of the induced finite model, retaining dyadic 4."},
        {"path": "build/reference-cache/stacks-04GJ.html",
         "url": "https://stacks.math.columbia.edu/tag/04GJ",
         "sha256": "1c6900b8ca02830ef8209a43529ca7a18f190dba5fc99c75d274aca8eb406119",
         "verified_scope": "Finite-type algebra over a henselian local ring decomposes into finite local pieces and a piece without quasi-finite points on its closed fibre."},
        {"path": "build/reference-cache/stacks-05K0.html",
         "url": "https://stacks.math.columbia.edu/tag/05K0",
         "sha256": "c54998016d99597d7a5223352bc0b33b0a21ea287ab6a800c1c545e400576f18",
         "verified_scope": "A separated quasi-finite scheme over a quasi-compact quasi-separated base is a quasi-compact open in a finite scheme. With the henselian decomposition this gives the finite open part containing the closed fibre."},
        {"path": "build/reference-cache/stacks-0ESN.html",
         "url": "https://stacks.math.columbia.edu/tag/0ESN",
         "sha256": "66a6d71d7debb3295adf5dffc3f7a258d1dbe870f0119866eaf56f14beacbfe0",
         "verified_scope": "Blowing up the r-th Fitting ideal of a finitely presented module, locally free of rank r on a schematically dense open, makes its strict transform locally free. The modification is an isomorphism where the module was already locally free."},
    ]
    for row in rows:
        assert auth.sha((auth.ROOT / row["path"]).read_bytes()) == row["sha256"]
    return rows


def coset_checks():
    """Use T=(Z/p^2)^2 and H=pZ/p^2 x Z/p^2.

    The quotient does not admit the chosen representatives as a subgroup;
    the nonzero H-valued carry is essential. Pairing values are exponents
    of a primitive p^2-th root, so all comparisons are exact integers.
    """
    comparisons = associative = 0
    controls = {"omitted_cocycle": False, "omitted_mixed_character": False,
                "omitted_H_pairing": False, "omitted_constant_pairing": False}
    models = []
    for p in (2, 3):
        n = p * p
        T = list(product(range(n), repeat=2))
        H = [x for x in T if x[0] % p == 0]

        def add(x, y):
            return ((x[0] + y[0]) % n, (x[1] + y[1]) % n)

        def sub(x, y):
            return ((x[0] - y[0]) % n, (x[1] - y[1]) % n)

        # A nonisotropic choice exposes the otherwise invisible constant.
        reps = [(c, c * c % n) for c in range(p)]

        def decompose(x):
            c = x[0] % p
            return c, sub(x, reps[c])

        def cocycle(c, d):
            return sub(add(reps[c], reps[d]), reps[(c + d) % p])

        def induced_sum(x, y):
            c, h = decompose(x)
            d, k = decompose(y)
            return add(reps[(c + d) % p], add(add(h, k), cocycle(c, d)))

        def e(x, y):
            return (x[0] * y[1] - x[1] * y[0]) % n

        assert all(cocycle(c, d) in H for c, d in product(range(p), repeat=2))
        assert any(cocycle(c, d) != (0, 0)
                   for c, d in product(range(p), repeat=2))
        for x, y in product(T, repeat=2):
            c, h = decompose(x)
            d, k = decompose(y)
            assert induced_sum(x, y) == add(x, y)
            no_carry = add(reps[(c + d) % p], add(h, k))
            controls["omitted_cocycle"] |= no_carry != add(x, y)
            factors = [e(reps[c], reps[d]), e(reps[c], k), e(h, reps[d]), e(h, k)]
            assert sum(factors) % n == e(x, y)
            controls["omitted_constant_pairing"] |= sum(factors[1:]) % n != e(x, y)
            controls["omitted_mixed_character"] |= (factors[0] + factors[2] + factors[3]) % n != e(x, y)
            controls["omitted_H_pairing"] |= sum(factors[:3]) % n != e(x, y)
            comparisons += 2
        for c, d, f in product(range(p), repeat=3):
            assert add(cocycle(c, d), cocycle((c + d) % p, f)) == \
                   add(cocycle(d, f), cocycle(c, (d + f) % p))
            associative += 1
        # Directly verify perfectness of the original pairing, not only
        # alternatingness or a possibly degenerate subgroup pairing.
        chars = {tuple(e(x, y) for y in T) for x in T}
        assert len(chars) == len(T)
        assert all(e(x, x) == 0 for x in T)
        models.append({"p": p, "n": n, "full_torsion_order": len(T),
                       "finite_part_generic_order": len(H), "cosets": p,
                       "distinct_pairing_characters": len(chars)})
    assert all(controls.values())
    return {"models": models, "exact_comparisons": comparisons,
            "coset_cocycle_associativity_checks": associative,
            "negative_controls": controls,
            "scope": "Finite group/cocycle/pairing formula only; finite flat representability and the Fargues estimate are proved/cited in the TeX."}


def gaussian_polynomial(expr, var=None):
    expr = sp.expand(expr)
    coeffs = sp.Poly(expr, var).all_coeffs() if var is not None else [expr]
    return all(sp.re(c).is_Integer and sp.im(c).is_Integer for c in coeffs)


def specialization_checks():
    """An actual ramified coefficient action over Z[i,t], specialized t->a.

    N has a free basis whose restricted image is 4A. The different of
    Q(i) is (2i). The quotient image has a nontrivial index in saturation.
    """
    t = sp.Symbol("t", real=True)
    I = sp.I
    action = sp.Matrix([[0, -1], [1, 0]])
    eig = sp.Matrix([1, -I])
    N = sp.Matrix([[4 + I * t, I], [t, 1]])
    assert action * eig == I * eig
    assert sp.expand(N.det()) == 4
    assert eig.T * N == sp.Matrix([[4, 0]])
    assert all(gaussian_polynomial(x, t) for x in N)
    assert all(gaussian_polynomial(x, t) for x in N.inv() * 4)
    D = eig / 4
    different = 2 * I
    F = D / different
    annihilator = 4 * different
    assert annihilator * F == eig
    assert 4 * D == eig
    assert not all(gaussian_polynomial(x) for x in 4 * F)
    # The actual quotient map is integral and its image is 2Z[i],
    # whereas the full quotient lattice is Z[i].
    q = sp.Matrix([[2, 0]])
    Vgen = (q * eig)[0]
    Fgen = (q * F)[0]
    assert Vgen == 2
    assert sp.simplify(annihilator * Fgen - Vgen) == 0
    index = sp.expand(Vgen * sp.conjugate(Vgen))
    assert index == 4 and index != 1
    norm_a = sp.expand(annihilator * sp.conjugate(annihilator))
    assert norm_a == 4 * 16 == 64
    count = 0
    for value in range(-5, 6):
        Nv = N.subs(t, value)
        assert eig.T * Nv == sp.Matrix([[4, 0]])
        assert Nv.det() == 4
        assert all(gaussian_polynomial(x) for x in Nv.inv() * 4)
        count += 1
    return {"specializations_with_kernel": count,
            "coefficient_field": "Q(i)", "different_generator": "2i",
            "kappa": 4, "restricted_image_generator": 4,
            "annihilator": "8i", "annihilator_absolute_norm": int(norm_a),
            "full_quotient_lattice": "Z[i]", "original_quotient_image": "2 Z[i]",
            "quotient_image_index": int(index),
            "omitted_different_detected": True,
            "saturation_replacement_loses_nonzero_index": True,
            "scope": "Exact module specialization over Z[i,t], with free N and restricted image Q; not a numerical construction of the general semiabelian family."}


def nonprojective_negative_control():
    # I=(3,t) in Z[t], presentation with relation (-t,3).
    # At t=0 the pullback is Z + Z/3, and its image is 3Z.
    t, s = sp.symbols("t s")
    relation = sp.Matrix([[-t], [3]])
    smith = smith_normal_form(relation.subs(t, 0), domain=sp.ZZ)
    nonzero = [abs(int(x)) for x in smith if x != 0]
    assert nonzero == [3]
    assert (sp.Rational(1, 3) * t).subs(t, 0) == 0
    assert not sp.Poly(t / 3, t).all_coeffs()[0].is_Integer
    # On the blowup chart t=3s, the actual image is generated by 3;
    # the torsion relation is 3 times the kernel generator (-s,1).
    generators = sp.Matrix([[3, 3 * s]])
    kernel = sp.Matrix([[-s], [1]])
    assert generators * kernel == sp.zeros(1, 1)
    assert relation.subs(t, 3 * s) == 3 * kernel
    return {"module": "I=(3,t) in Z[t]", "specialization": "t=0",
            "tensor_pullback": "Z direct_sum Z/3Z", "coherent_image": "3Z",
            "dual_then_specialize": "Z", "image_then_dual": "(1/3)Z",
            "naive_image_dual_base_change_fails": True,
            "blowup_chart": "t=3s", "strict_transform": "3 Z[s]",
            "actual_image_equals_strict_transform": True,
            "scope": "Exact counterexample to omitting projectivity and exact local model of the allowed flattening."}


def norm_checks():
    x = sp.Symbol("x")
    tested = []
    for p in (3, 5, 7, 11, 13, 17, 19):
        f = sp.cyclotomic_poly(p, x)
        assert sp.resultant(f, x - 1, x) == p
        assert sp.degree(f, x) == p - 1
        tested.append(p)
    return {"odd_primes": tested, "cyclotomic_norms_verified": len(tested),
            "dyadic_factor_retained": 4,
            "general_norm_identity": "log(rd(E)) + sum_odd log(p)/(p-1) + 2*1_(2 in S)*log(2)",
            "scope": "Exact cyclotomic norm checks in finite examples; the all-prime and extended-different formulas are proved in the TeX."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    auth.RANGES = RANGES
    sources = auth.provenance(args.offline)
    artifacts = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
                 f"notes/{STEM}.md", f"scripts/{STEM}.py"]
    checks = {"induced_finite_model": coset_checks(),
              "actual_specialization_model": specialization_checks(),
              "projectivity_negative_control": nonprojective_negative_control(),
              "ideal_norms": norm_checks()}
    record = {
        "status": "PASS",
        "classification": "closed actual corrected-fibre comparison and compatible local-freeness construction suppliers; whole W10 remains open",
        "sources": sources, "primary_references": references(),
        "artifacts": {p: auth.sha((auth.ROOT / p).read_bytes()) for p in artifacts},
        "diagnostics": checks,
        "scope_guards": [
            "original cubical Weil pairing and full generic torsion at the prescribed finite level",
            "finite induced model has the original identity cotangent module",
            "Fargues finite theorem is applied to the Cartier dual, with target omega(B)",
            "complete rank-one valuations and dyadic 4 retained",
            "height-one test extensions are injective and retain generic abelianity",
            "boundary specialization uses projective original restricted images and exact kernels",
            "one original different ideal; no projector denominator added",
            "full quotient eigenlattice, original quotient image and corrected image remain distinct",
            "actual differential modules commute with dominant normal-model pullback",
            "simultaneous Fitting modifications are vertical and retain the full characteristic-zero fibre",
            "old fields, levels, labels, coordinates and metrized line bundles are retained",
            "original arithmetic points lift uniquely without a field extension"],
        "remaining": [
            "regularized actual boundary point-height identity and uniform averaged height bound",
            "separate exact Lagrangian congruences and flag numerical records",
            "remaining W10 rank and map-height budgets",
            "whole W10 and both RH/GRH proofs remain open"],
        "verification_scope": "Authenticated bounded pinned-source excerpts, checked primary theorem interfaces, exact finite diagnostics, and ordinary-mathematics proofs in the TeX. No Lean build or complete-node certificate."}
    out = auth.ROOT / "certificates" / (STEM + ".json")
    out.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "source_files": len(sources),
                      "finite_comparisons": checks["induced_finite_model"]["exact_comparisons"],
                      "specializations": checks["actual_specialization_model"]["specializations_with_kernel"],
                      "negative_controls": "all passed", "certificate": str(out.relative_to(auth.ROOT))}))


if __name__ == "__main__":
    main()
