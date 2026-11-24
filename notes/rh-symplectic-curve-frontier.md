# RH rank-four point arithmetic: exact curve and endpoint targets

**Status:** unconditional reductions of the remaining point premises. No proof of Fin0, NoEnd or irreducible attachment is claimed.

The [curve and endpoint theorems](../paper/shared/rh-symplectic-curve-frontier.tex) show that the full invariant algebra of the actual complete normalized ring is finite over the coefficient DVR if and only if each characteristic-ell local DVR curve has constant base trace, equivalently finite-image semisimplification. This is also equivalent to the exclusion of precisely two types of curves: absolutely irreducible rank-four curves and block-diagonal curves with an absolutely irreducible first block. No common finite-index subgroup for all curves is necessary.

The proof retains the entire characteristic-prime fibre: the flag extends to field-valued specializations by properness of the closed flag incidence scheme over the selected local domain, including the labelled Frobenius action. The two marks still give integral coordinate projectors. The XVan argument for a cross-block isolated pair works over the curve DVR. If the traces agree with the base, the trace pairing on the four distinct residual characters gives a quotient of the image algebra onto the full diagonal algebra, mapping every coordinate projector to itself. This excludes opposite arrows in every coefficient characteristic, including 3. For diagonal type, class field theory makes the diagonal characters constant and a reflection-invariant linear functional makes every nonzero off-diagonal entry have strictly positive weight. Hence all nonconstant balanced monomials vanish. The curve/radical criterion then controls even the torsion and nilpotents of the invariant algebra.

For the characteristic-zero block endpoints the two determinant magnitudes are exactly p^(e+2) and p^e at every good arithmetic Frobenius. Thus a strict half-power interval p^(c-1/2)<|lambda|<p^(c+1/2), even at just one good prime with unknown c, excludes an endpoint. After twisting the first block by alpha^(-1), the representation is even, ordinary, has distinct weights -e,0 and residual characters barPsi and 1. It is not in the odd residually reducible ordinary modularity theorem. A large-residual-image even Fontaine--Mazur theorem also does not apply to this split residual representation. The equal-characteristic curve block is even as well, with finite determinant, and if irreducible must have infinite image.

## Precise residual arithmetic

1. Exclude the two characteristic-prime types in the exact model (or prove finite-image semisimplification for every curve).
2. Give the strict half-power window at one good prime for every irreducible-block characteristic-zero endpoint (or another valid NoEnd argument).
3. Supply the common-coefficient fixed-field cuspidal attachments for all actual irreducible characteristic-zero points.

By the integral comparison theorem these suffice for the remaining RH Case II bound. The source's route to the first two is the actual rank-four mixed seed and promodularity tower. Rank-two/rank-three propagation alone, generic local smoothness, and number-field analogies of function-field deformation results do not establish these targets.

The accompanying exact combinatorial check in `scripts/check-rh-sp4-support.py` enumerates all 4096 off-diagonal patterns. After transitivity, reflection symmetry and exclusion of cross-block two-element components, 41 remain: 37 diagonal-type, three two-block and one full. The two allowed labelled permutations and an explicit strictly positive antisymmetric functional on every diagonal-type support are also checked. This finite calculation does not prove the arithmetic exclusion of cross-block pairs (proved separately in the manuscript), finiteness, or automorphy.

No TeX or Lean build or independent referee review is claimed.
