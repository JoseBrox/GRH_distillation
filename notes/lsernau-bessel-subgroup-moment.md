# Exact Bessel-subgroup contribution to the Poincare moment

Use the notation and absolute convergence of
[global cut unfolding](lsernau-global-cut-unfolding.md)
and [quantitative returns](lsernau-quantitative-returns.md).
This computes the actual part of the normalized amplitude supported
on the rational Bessel subgroup, not the full return matrix.

Source: pinned readable revision 72fead102f663d5c7a407964a13dc0cf9d977207,
New/Spanning/Unfolding/BesselLevelStructure.lean, 825--927,
AmplitudeSums.lean, 887--end, ReducedGroups.lean, 295--361,
506--end. The argument works for arbitrary free source levels
with the same block decomposition and approximation properties.

## 1. Class fibres

Write R=UH for the Bessel subgroup, H the definite middle unitary
group (rank k), and U its unipotent radical. Let K_f be the lattice
stabilizer and J the chosen principal congruence level, normal in K_f.
The source class level is J_H=J intersect H_f. Let C be the definite
class set H(F)\H_f/J_H and h_c its representatives in H_f.
Assume the class stabilizers at J_H are trivial, as in the
source free-level hypotheses.

The finite subgroup R_f intersect K_f is a semidirect product
of the corresponding U and H intersections, and the same is true
at J. This follows by reading the middle diagonal block of the
upper block-triangular matrix and its inverse in the given lattice
basis; for J the middle block is congruent to the identity.
In particular projection to H preserves the indicated level.
This is the actual source level, not an arbitrary replacement by a
smaller compact subgroup.

Put Rbar=image(R_f intersect K_f -> K_f/J).
For s in Rbar, fix k_s in R_f intersect K_f lifting it. For each c,
write h_c k_s=u h with u in U_f and h in H_f. Decompose
h=eta h_d a with eta in H(F), a in J_H. The strong approximation
of U gives x in U(F) with h^(-1)u^(-1)x h in J; here one uses the
rational root coordinates of the unipotent group and simultaneous
finite-place approximation. Thus gamma_0=x eta satisfies
\[
        h_c^{-1}\gamma_0 h_d\in k_sJ .
\]
Conversely, if a rational gamma in R has this property for some
d, projection to H identifies the same class d. The class depends
only on s and c, not on the chosen lift k_s, by projection of J.
The assignment c -> d is a permutation: the inverse class
assignment is induced by s^(-1).

For gamma another term over (c,s,d), the element
gamma gamma_0^(-1) belongs to R(F) intersect h_c J h_c^(-1).
Its projection to H is a class stabilizer, hence the identity.
Consequently all such terms are exactly the coset
Gamma_c^U gamma_0, with
Gamma_c^U=U(F) intersect h_c J h_c^(-1).
Conjugation by gamma_0 identifies Gamma_d^U with Gamma_c^U.
If s lies outside Rbar, there are no rational R-terms at all.
This proves the class-fibre assertions including their multiplicities.

## 2. Integrate the exact fibre

Use the vector W of normalized local Bessel functions in the source,
including its finite character convention. Let V_B be the tensor
product of its coordinate spaces and D_X=|C| dim V_B.
Its transformation law is W(r y)=sigma(r)W(y) with sigma unitary
on R_infinity (the U action is the prescribed character).
The full local Bessel coordinate orthonormality gives
\[
 \int_{U_\infty\backslash G_\infty}W(y)W(y)^*\,dy=I_{V_B}.
\]
Equivalently this follows from the irreducible compact type,
Schur's lemma and the source L^2 normalization, tensorized with
its quotient measures. The finite character is trivial on the
arithmetic Gamma_c^U: the principal congruence is in the local
character kernel and the rational character satisfies the product
formula. Thus W is invariant on those arithmetic orbits.

Consider the block of the rational-R contribution to equation (1)
of the global cut chapter, divided by its covolume nu.
Use the coset from section 1 and sum the cutoff beta_d over it.
The transformation law, invariance under Gamma_d^U and the cutoff
partition of unity give
\[
 A_s(c,d)=\nu^{-1}\int\beta_c(y)
                         W(y)W(\gamma_0^{-1}y)^*\,dy
         =\nu^{-1}\int\beta_c(y)W(y)W(y)^*\,dy\,\sigma(\gamma_0^{-1})^* .
\]
The product W(y)W(y)^* is U-invariant. Disintegrate over
U_infinity\G_infinity; the integral of beta_c on a U-orbit is nu.
Indeed the partition of unity integrates over the quotient by
Gamma_c^U to its covolume, the common source normalization.
Absolute convergence follows from the return theorem; for this
particular fibre the partition of unity also gives direct domination.
Therefore
\[
            A_s(c,d)=\sigma(\gamma_0^{-1})^* .
\]
The other blocks in row c are zero. With the transpose/conjugate
Gram convention of the global cut chapter the same matrix may be
written as its transpose; all norms and identity assertions here
are unchanged. For s=1 one can choose gamma_0=1 and d=c.
This yields the exact normalized Bessel-subgroup matrices:
\[
 A_1=I_{D_X},\qquad
 A_s \text{ unitary for }s\in Rbar,\qquad
 A_s=0\text{ otherwise}.
\]
In particular
\[
             \sum_s\|A_s\|_{\rm HS}^2=|Rbar|D_X.       \tag{1}
\]
The covolume in the amplitude is essential; omitting it would
square an erroneous volume factor in (1).

## 3. Count the reduced subgroup

At a chosen split place of residue size q, the U-image is the
strict upper block-unipotent subgroup with block sizes
1,...,1,k+1,1,...,1, with rho singleton blocks on either side.
It has
\[
         \binom{2\rho}{2}+2\rho(k+1)
              =\rho(2k+2\rho+1)
\]
free entries. The H-image is GL_k(F_q).
Every choice of these entries and middle invertible block lifts
integrally at the split place. At its conjugate place use the
inverse Hermitian adjoint, which has the same required block shape.
The pairs are independent; away from the chosen places take
the identity. Thus for the two split rational primes p_0,p_1,
each with f chosen places and product M, the exact cardinality is
\[
 |Rbar|=|\bar H|M^{f\rho(2k+2\rho+1)},
 \qquad |\bar H|=\prod_{w\text{ chosen}}|GL_k(\mathbf F_{q_w})|.
\]
This is the source reduced subgroup size, with no double counting
of conjugate places. The formula includes rho=0 and k=0.

## 4. Control the effect of replacing full Bessel functions by cuts

Let E_s be the normalized full-minus-cut amplitude matrix,
over all rational terms. The absolute integrated difference
bound (25)--(26) of the quantitative return chapter gives, for
each fixed source class c,
\[
 \sum_d \|E_s(c,d)\|_{\rm op}\le
 \sum_d \|E_s(c,d)\|_{\rm HS}\le b^{-k^3f}/2 .
\]
The same bound for the column sums follows by the inversion
gamma -> gamma^(-1), y -> gamma^(-1)y, which interchanges c,d and
s,s^(-1) and takes Hermitian adjoints. Hence the block Schur
test gives
\[
              \|E_s\|_{\rm op}\le b^{-k^3f}/2,\qquad
              \|E_s\|_{\rm HS}\le\sqrt{D_X}\,b^{-k^3f}/2.
 \tag{2}
\]
The proof of the block Schur test is just scalar Cauchy--Schwarz
with the nonnegative matrix of block norms. The same argument
applies to any inversion-stable family of rational terms. It
does not require summing an operator-norm error once per class.

The full return matrix is A_s plus the non-Bessel contribution.
Equation (1) computes its Bessel term exactly and (2) deals
with the truncation. No small bound on the non-Bessel contribution
at s=1, on mixed cross terms in the moment, or on the open-cell
and terminal-fixer contributions follows from these identities.
Those remain separate arithmetic estimates. Injectivity of the full
Poincare map is not asserted. Good-form multiplicities are now supplied
independently by the [two-place theorem](lsernau-good-form-multiplicities.md).
