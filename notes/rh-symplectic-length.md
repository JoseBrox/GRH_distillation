# RH rank-four integral comparison: exact three-premise reduction

**Status:** proved the conditional comparison on the actual integral model. The three remaining arithmetic premises are not established by this result. Neither the W04 node nor RH is closed.

The [proof](../paper/shared/rh-symplectic-length.tex) replaces the remaining two-torus, graph, tangent and integral comparison work for RH Case II by a single precise implication:

* (F) the entire degree-(0,0) algebra of the actual complete normalized ring is finite over the coefficient DVR (equivalent to original Fin0 on this universal ring);
* (E) the original NoEnd condition on block-diagonal characteristic-zero points;
* (A) cuspidal attachment over the fixed quadratic field of the fixed-field spectrum theorem, for all actual irreducible points, with common coefficient isomorphism.

Under exactly these three premises, the normalized strict Selmer length obeys

    log(ell) length_norm <= (ell N (e+1))^C

with an absolute exponent. In particular the abstract integral comparison is no longer an independent missing supplier.

## Main proof details

1. Bezout projectors at the marked finite-order Frobenius, followed by the compressed marked H(g0), put each coordinate projector in the integral representation algebra. The support graph is transitive and self-reflecting. An isolated cross-block pair would give a two-dimensional subquotient with a local invariant coordinate line (the two Frobenius eigenvalues are disjoint). Divide a nonzero off-diagonal entry vanishing locally by its minimum valuation. The residual XVan cocycle vanishes globally, since its primitive vanishes at the marked Frobenius. This excludes the pair. A three-element component is impossible by reflection. The only reducible alternatives are diagonal type and the two prescribed irreducible blocks with one interblock direction absent. For diagonal type, cover arrows violating the local ordering would be negative-weight finite classes, hence split by qualitative Selmer vanishing. The coordinate projectors contradict a nonzero split arrow. The inertia corner distinguishes the two allowed orderings. This supplies the original sign and fixed-point separation conditions.

2. On the ambient slice of first weight zero, invariant monomials factor into first-zero variables and opposite first-weight pairs. Integral augmentation filtrations are cofinal, with ordinary orders differing by at most a factor two. The rational chart adds exactly the two independent products of weights (0,1),(0,2). Its dimensions at second weights (-2,-1,0,1,2) are (0,r,m,r'+1,1); the actual relation lists are unchanged. Negative/zero spanning follows from rational finite cohomology and the normalization, not from a torsion-free approximation of the quotient.

3. A slice point lifts using the projection onto first weight zero. Two-torus rescaling is a finite rational linear inequality problem; positive valuations of nonconstant invariant monomials give its feasibility. Finiteness of the full invariant algebra bounds the tails of homogeneous series, so rescaling and dual-number lifting preserve the complete original ideal. At irreducible points the localized first grading is a Laurent-polynomial extension of the slice, giving a lift of every slice tangent. Rigidity and the two marks leave precisely the diagonal torus; only one direction survives on the slice. An actual conjugacy between irreducible marked points is diagonal by the two marks and a similitude by Schur, hence the original torus action. Distinct slice orbits give distinct isomorphism classes.

4. Every two-sided slice point is irreducible: diagonal type has one sign zero, and the block-triangular alternative has an actual block-diagonal torus limit, excluded by (E). The abstract integral length theorem applies to this precise slice. Qualitative finiteness of the strict group allows choosing a common annihilator b, then enlarging it to b*(Psi^(-1)(s0)-1) so even local coboundary primitives lie in the same finite coefficient module. The original finite-modulus derivation injects the strict group into the dual of the saturated negative cotangent quotient. Ramification normalization cancels the change of uniformizer, and the fixed-field spectrum bounds the sum of actual trace valuations.

## Next attack

Prove (F), (E), (A) on this same model. The pinned source derives these using characteristic-prime and characteristic-zero promodularity, including the genuine rank-four mixed seed. Residual irreducibility is not present here; ordinary automorphy-lifting results requiring it do not discharge (A). The source's entire `WitA` interface is no longer necessary for the final RH quantitative comparison.

No independent referee review or Lean build is asserted. See the source-interface record in the certificate.
