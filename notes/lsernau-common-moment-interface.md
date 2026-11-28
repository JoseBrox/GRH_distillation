# The scalar moment and dimension interface on the common spaces

This proves the finite representation-theoretic part of the
spanning theorem on the exact spaces named in the Sernau
source. The actual global unfolding and arithmetic estimates
are still inputs. The source is
[SpanningTheorem.lean][s] 61–109, 118–183, 221–339 at
revision 72fead102f663d5c7a407964a13dc0cf9d977207.

## 1. Definite-space dimension

For a definite unitary group, let \(K'\lhd K\) be its chosen
principal level inside the standard maximal level, and
\(\mathcal G=K/K'\). The finite stabilizer of a double coset
at \(K\) is \(\Gamma_h\). Suppose the stabilizers at \(K'\)
are trivial. Then the fiber over \(h\) of the map of class
sets consists of the orbits of \(\Gamma_h\) on \(K/K'\).
The action is free, because a stabilizer maps to the
intersection with a conjugate of \(K'\).
Thus the fiber has cardinality \(|\mathcal G|/|\Gamma_h|\).
If \(d_\infty\) is the dimension of the prescribed compact
algebraic weight, evaluation of level \(K'\) forms at class
representatives identifies their space with one copy of
that weight space for every class. It follows that
\[
 \dim V_{\rm prin}
 =|\mathcal G|\,d_\infty
                \sum_{h\in\mathrm{Cl}(K)}|\Gamma_h|^{-1}.
 \tag{1}
\]
At the source's degree-one split chosen prime \(p>2\),
the torsion-free principal congruence calculation of the
[critical-value chapter](lsernau-critical-value-systems.md)
proves the required triviality of stabilizers.
The sum in (1) is the definite genus mass. The compact
formal degree is the Weyl dimension of this weight in the
specified Haar normalization.

For the actual source \(W_m\), take its algebraic weight
and \(K'=D.\mathrm{chosenLevel}\).
The [two-place multiplicity theorem](lsernau-good-form-multiplicities.md)
identifies its good eigensystems, including their multiplicities,
with those on \(Y_0\). Thus
\[
 D_{\rm good}=\dim(D.e_0 V_{Y_0})
     \le |\mathcal G|\,d_\infty\,\mathrm{mass}_r.       \tag{2}
\]
That theorem uses the primitive cuspidal type at one split place
above each of the two distinct level primes and the precise
Harris--Labesse comparison. Formula (1) then gives (2); no
nonvanishing of the good space is inferred from this upper bound.

## 2. A single compression for the second moment

Use the full coordinate source \(X=D.\mathrm{SourceForm}\)
of dimension \(d_X>0\). The source scaled map is
\(P=(\mathrm{vol}J\,\nu)^{-1/2}D.\mathrm{poincare}\),
in the source coordinate isometry, where \(\nu\) is the
specified unipotent covolume. Let \(\rho\) be the unitary
action of \(\mathcal G\) on the principal forms, and
\(E=D.e_0\) its central orthogonal projector onto the
good forms. The ranges of the original good translates
are the ranges of
\[
 A_g=\rho(g)EP
\]
(the scalar \(|\mathcal G|\) in the original map and the
positive Poincare scale change no ranges).

For the actual spanning estimate it suffices to prove the
following two analytic assertions from the global unfolding:
\[
 \begin{split}
 &\|EP P_U\|_{\rm HS}^2
       \ge\dim U-5b^{-4}d_X\quad(U\subset X),\\
 &\sum_{g\in\mathcal G}\|P^*\rho(g)P\|_{\rm HS}^2
       \le (1+9b^{-4})\,d_X^2/(d_\infty\mathrm{mass}_r).
 \end{split}                                             \tag{3}
\]
Here \(P_U\) denotes the orthogonal projection. The first
inequality is equivalent to
\(\operatorname{tr}(I-P^*EP)_+\le5b^{-4}d_X\):
take the subspace of eigenvalues below one for the
necessary direction and use the positive part for the
sufficient direction. It also implies \(EP\ne0\) for
\(5b^{-4}<1\), so the target is nonzero.

Define the positive operator
\[
 K_0=|\mathcal G|^{-1}\sum_g\rho(g)PP^*\rho(g)^*.
\]
Expanding its squared trace, cyclic invariance of trace
and the bijection \(g^{-1}h\) give
\[
 \operatorname{tr}K_0^2
 =|\mathcal G|^{-1}\sum_g\|P^*\rho(g)P\|_{\rm HS}^2.
\]
The good-target operator is \(K=EK_0E\) restricted
to the range of \(E\). By the orthogonal block
decomposition, \(\operatorname{tr}K^2
=\|EK_0E\|_{\rm HS}^2\le\|K_0\|_{\rm HS}^2\).
Using (2) and (3), we get
\[
 \operatorname{tr}K^2\le
  (1+9b^{-4})d_X^2/D_{\rm good}.
\]
This avoids a new unfolded moment for the projected
map: only the unprojected moment needs to be
estimated. The positive source deficit is the same
for every translate, at most \(5b^{-4}\) after
division by \(d_X\).

Apply the [two-moment spanning lemma](lsernau-moment-and-prime-reductions.md)
with \(e=19b^{-4}\) and missing share \(\eta=4b^{-2}\).
For \(b\ge3\), \(0<e<\eta<1\) and
\(\eta-e\ge b^{-2}\). The number of selected
translates is at most
\[
 \left\lceil\frac{2D_{\rm good}}{d_X}
         \log\frac{1-e}{\eta-e}\right\rceil
 \le \frac{4D_{\rm good}}{d_X}\log b+1.
\]
They span at least \((1-4b^{-2})D_{\rm good}\)
dimensions. This proves the exact desired scalar
spanning conclusion on the full source subject
to (3), since (2) is now supplied. For the actual ramified source, use the exact dimension and restricted
moment theorem in [the common finite theta chapter](lsernau-common-theta-finite.md#5-restrict-the-actual-scalar-moments-before-selecting-translates).
It proves the same rank target directly on that subspace with the
correspondingly adjusted deficit and second moment.

The outstanding analytic work is the proof of
(3) for the actual Poincare map, including
unipotent covolume, off-diagonal sums and the
good-type loss. The finite upper-chain evaluation and normalization are given in the
common finite theta chapter; the global see-saw identity and uniform
integral jet estimates remain open.
No legacy whole node is closed by these
finite-dimensional arguments.

[s]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean
