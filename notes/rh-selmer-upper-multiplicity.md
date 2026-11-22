# Generic support and multiplicity from a two-point slice

## Result and scope

The remaining commutative-algebra upper comparison has a short proof on
the actual three-direction Rees algebra. Relevant-prime classification
first confines the generic support to two-sided equation points. On
that support the Rees algebra becomes a polynomial algebra over the
localized degree-zero ring. An invertible weight-minus-two element then
gives a finite slice with an involution. The one-dimensional tangent
hypothesis forces that slice to be reduced, and its invariant part
forces it to have at most two geometric points.

This proves the eventual support and multiplicity suppliers under the
stated model hypotheses. It does not construct the marked arithmetic
model or prove its automorphy, rigidity, or Selmer comparison inputs.
No regular sequence or flatness of the original equation quotient is
assumed. The slice is taken only in characteristic zero; residue
characteristic two causes no division-by-two issue.

## 1. Objects and statement

Use the data of [the admissibility theorem](rh-selmer-admissibility.md):
an augmented four-weight algebra \(A\), its Noetherian local
degree-zero ring \(B\), the homogeneous equation ideal \(Q\), and the
three modules

\[
N_0=A_{-2},\qquad N_1=A_2,\qquad
N_2=BF_*^2+A_{-2}^2A_2.
\]

The equations are \(F_1,\ldots,F_r,F_*\) of weight \(-1\),
\(G_j\) of weight \(-2\), \(E_1,\ldots,E_{r'}\) of weight \(1\),
\(E'_l\) of weight \(2\), and \(Z_i\in B\cap\ker x\).
Put

\[
Q_0=Q\cap B,\quad \mathfrak d=A_{-2}A_2\subset B,\quad
q=r+1+r'\ge1,
\]

\[
Q_{\mathrm{sq}}=(F_i^2,F_*^2,G_j,E_k^2,E'_l,Z_i)\subset A.
\]

Assume the finite quotient, negative cotangent spanning, and fixed-point
separation hypotheses of that theorem. The element \(a\) and its
nonvanishing condition are not needed until the final Euler bound.
Assume in addition that at every two-sided \(K\)-point of \(A/Q\)
the space of \(\mathcal O\)-linear tangent derivations has dimension
at most one. Here \(K\) is an algebraically closed extension of the
fraction field \(F\) of \(\mathcal O\).

Let \(\mathcal R=\bigoplus_{\boldsymbol d\ge0}
N_0^{d_0}N_1^{d_1}N_2^{d_2}t^{\boldsymbol d}\), and let
\(J\subset\mathcal R\) be homogeneous and contain the sections

\[
F_i^2t_0,\ G_jt_0,\ E_k^2t_1,\ E'_lt_1,\ F_*^2t_2
\]

and all \(Z_i\). Write \(M_{\boldsymbol d}=(\mathcal R/J)_{\boldsymbol d}\).
The actual application is \(J=J_\varphi+(\boldsymbol s)\).

**Theorem.** In all sufficiently large multidegrees:

1. \(M_{\boldsymbol d}\) and \(B/\operatorname{Ann}_B M_{\boldsymbol d}\)
   are finite over \(\mathcal O\).
2. If a prime \(P\subset B\) with \(P\cap\mathcal O=0\) supports
   \(M_{\boldsymbol d}\), then \(Q_0\subset P\) and
   \(\mathfrak d\not\subset P\). Every embedding of its residue
   field into \(K\) is the restriction of a two-sided point of \(A/Q\).
3. At each such prime,

   \[
   \ell_{B_P}\bigl((M_{\boldsymbol d})_P\bigr)\le 2^q. \tag{1}
   \]

The local comparison leading to (1) already holds when all \(d_i\ge1\).
Only the support exclusion requires a further uniform eventual bound.
At a prime whose finite slice has a single geometric point, the stronger
bound \(2^{q-1}\) holds. No assertion that all actual points have that
type is made.

## 2. Uniform eventual support

Let \(I_{\mathrm{irr}}\) be the product of the three coordinate-degree
ideals. The universal clearing identities in the admissibility proof
show that every relevant prime over \(J\) contains \(Q_0\mathcal R\).
Thus

\[
Q_0\mathcal R I_{\mathrm{irr}}\subset\sqrt J.
\]

Noetherianity gives an integer \(n\) such that
\((Q_0\mathcal R I_{\mathrm{irr}})^n\subset J\). By standardness,
every sufficiently large piece of the finite graded module
\(M=\mathcal R/J\) equals the corresponding piece of
\(I_{\mathrm{irr}}^n M\). Therefore

\[
Q_0^nM_{\boldsymbol d}=0 \quad\text{eventually}. \tag{2}
\]

The ring \(B/Q_0^n\) is finite over \(\mathcal O\): filter it by the
powers of \(Q_0\), whose successive quotients are finite modules over
the finite \(\mathcal O\)-algebra \(B/Q_0\). This proves the first
assertion and excludes primes not containing \(Q_0\).

The same point-classification proof, now applied to \(J+\mathfrak d\mathcal R\),
shows that every relevant prime over this ideal contracts to
\(\mathfrak m_B\). Its characteristic-zero case has
\(\sigma(\mathfrak d)=0\), so the half-point construction, fixed-point
separation, and two-degree cotangent argument give the contradiction.
No trace nonvanishing is needed for this case. Hence for some \(n'\),

\[
(\mathfrak m_B\mathcal R I_{\mathrm{irr}})^{n'}
\subset J+\mathfrak d\mathcal R.
\]

In a common eventual degree range this implies
\(\mathfrak m_B^{n'}M_{\boldsymbol d}\subset\mathfrak dM_{\boldsymbol d}\).
At a prime \(P\) containing \(\mathfrak d\) with
\(P\cap\mathcal O=0\), a uniformizer belongs to
\(\mathfrak m_B\setminus P\). Localizing gives
\((M_{\boldsymbol d})_P=\mathfrak d_P(M_{\boldsymbol d})_P\).
Nakayama's lemma makes this module zero.

For each remaining generic prime \(P\), the fraction field of \(B/P\)
is finite over \(F\). Given an embedding into \(K\), write the resulting
character as \(\sigma:B\to K\). The nonzero graded finite-type algebra
\((A/Q)\otimes_{B,\sigma}K\) has degree-zero part \(K\). A \(K\)-point
exists by the weak Nullstellensatz; since \(\sigma(\mathfrak d)\ne0\),
it is two-sided. This proves the support assertion for every embedding,
not just one chosen representative.

## 3. A finite slice and its two parity spaces

Fix a generic prime \(P\supset Q_0\) with
\(\mathfrak d\not\subset P\). Choose
\(f\in A_{-2},g\in A_2\) with \(fg\notin P\), and localize at \(P\).
Both \(f,g\) are units in \(A_P\). Put

\[
D=(B/Q_0)_P,\qquad C=(A/Q)_P,\qquad S=C/(f-1).
\]

The ring \(D\) is local Artinian and finite over \(F\).
Multiplication by \(f\) identifies weights differing by two in \(C\),
so \(C_{2j}=f^{-j}D\), \(C_{2j+1}=f^{-j}C_1\).
The grading gives the direct sum decomposition into these pieces;
imposing \(f=1\) therefore gives an actual \(D\)-module decomposition

\[
S=D\oplus C_1. \tag{3}
\]

One way to check injectivity of this normal form is to regard \(C\),
as a module, as the direct sum of the Laurent powers of \(f\) with
coefficients in \(D\oplus C_1\); evaluation at \(f=1\) has precisely
the relations generated by \(f-1\). In particular, \(D\hookrightarrow S\).
The ring \(S\) is finite over \(D\). After normalizing the finitely
many generators by powers of \(f\), its even generators lie in \(D\),
and each odd generator \(z\) has \(z^2\in D\). Successively adjoining
these integral quadratic generators proves finiteness.

The parity action \(c_j\mapsto(-1)^j c_j\) descends to an involution
of \(S\); by (3), its invariant subring is exactly \(D\).
This uses characteristic zero, so \(2\) is invertible.

At every \(K\)-point of \(S\otimes_F K\), the corresponding point
of \(A/Q\) is two-sided, since \(f\) and \(g\) are units. Its tangent
space has dimension at most one. The Euler derivation

\[
c_j\longmapsto j\,\xi(c_j)
\]

annihilates \(Q\) and takes \(f\) to \(-2\xi(f)=-2\ne0\).
Every tangent derivation of the slice annihilates \(f-1\), hence \(f\).
It would be independent of that Euler derivation unless it were zero.
Thus every tangent space of the finite \(K\)-algebra \(S\otimes_F K\)
is zero. Each of its local maximal ideals has \(\mathfrak m/\mathfrak m^2=0\);
Nakayama implies \(\mathfrak m=0\). The algebra is reduced, a product
of copies of \(K\).

As \(D\otimes_F K\hookrightarrow S\otimes_F K\), the ring \(D\)
is reduced. A reduced local Artinian ring is a field, necessarily
\(L=\kappa(P)\). For each embedding \(L\hookrightarrow K\), the
finite reduced algebra \(S\otimes_{L}K\) has invariant subring \(K\).
An involution on a finite product of copies of \(K\) permutes its
factors, and its invariant algebra has one factor per orbit. There is
therefore a single orbit of size one or two. Its parity dimensions are

\[
(m_0,m_1)=(1,0)\quad\text{or}\quad(1,1). \tag{4}
\]

The decomposition (3) and scalar extension now give, for every weight,

\[
\ell_{B_P}\bigl((A/Q)_{j,P}\bigr)=m_{j\bmod2}\le1. \tag{5}
\]

Lengths here are over \(B_P\), whose residue field is \(L\); no residue
degree multiplies (5). All nilpotents in \(D\) have been excluded by
the tangent argument, not discarded by replacing a ring with its
reduction. This is the step that retains the integral multiplicity
relevant to the generic length.

## 4. Squaring the selected odd equations

In \(A_P/Q_{\mathrm{sq}}\), let \(U\) be the ideal generated by the
\(q\) selected equations \(F_i,F_*,E_k\). Their squares are zero, so
\(U^{q+1}=0\). For every \(k\), the module \(U^k/U^{k+1}\) is a
quotient of the sum of copies of \(A_P/Q\), shifted by the weights of
the squarefree products of \(k\) selected equations. Repeated factors
vanish; this gives \(\binom qk\) copies, without asserting their
linear independence. The filtration by powers of \(U\), together
with (5), proves

\[
\ell_{B_P}\bigl((A/Q_{\mathrm{sq}})_{w,P}\bigr)
\le\sum_{I\subset\{1,\ldots,q\}}m_{(w-|I|)\bmod2}
=2^{q-1}(m_0+m_1)\le2^q. \tag{6}
\]

The middle equality uses \(q\ge1\) and the fact that all selected
weights are odd. Thus the one-point slice gives the sharper
\(2^{q-1}\) bound for every weight. Arbitrary additional relations
or kernels only reduce lengths; no sequence is assumed regular.

## 5. The exact localized Rees comparison

The same units \(f,g\) give

\[
(A_{-2})_P=fB_P,\qquad (A_2)_P=gB_P,\qquad (N_2)_P=fB_P.
\]

For example \(h/f=hg/(fg)\in B_P\) for \(h\in(A_{-2})_P\),
and \(N_2\) contains \(f^2g=(fg)f\). Hence the three independent
Rees variables give an isomorphism

\[
\mathcal R_P=B_P[X_0,X_1,X_2],\qquad
X_0=ft_0,\quad X_1=gt_1,\quad X_2=ft_2. \tag{7}
\]

This is a polynomial algebra even if \(B_P\) has nilpotents:
the monomials have distinct Rees degrees, and their coefficients are
units times elements of the embedded degree-zero ring.
Let \(H\subset B_P\) be generated by

\[
F_i^2/f,\ G_j/f,\ E_k^2/g,\ E'_l/g,\ F_*^2/f,\ Z_i.
\]

When every \(d_i\ge1\), quotienting the degree-\(\boldsymbol d\)
piece of (7) by just the specified sections and \(Z_i\) gives
\(B_P/H\): each coordinate-degree equation can be multiplied to that
degree. The further ideal \(J\) gives a quotient of this module.
Meanwhile \(Q_{\mathrm{sq}}A_P=HA_P\). The even weight

\[
w(\boldsymbol d)=2(d_1-d_0-d_2)
\]

has the unit generator \(f^{d_0+d_2}g^{d_1}\), so its quotient piece
is also \(B_P/H\). This gives the actual surjection

\[
(A/Q_{\mathrm{sq}})_{w(\boldsymbol d),P}
\twoheadrightarrow (M_{\boldsymbol d})_P\qquad(d_i\ge1). \tag{8}
\]

Combining (6) and (8) proves (1). This is a localized comparison in
the stated degree range. It does not assert an injection before
localization, a comparison on the irrelevant boundary, or equality
after the additional chart equations.

## 6. Consequence for the Euler bound and source correspondence

Suppose \(a\in B\) has augmentation zero and is nonzero at every
two-sided equation point. Let \(\Sigma\) be the set of distinct
degree-zero characters obtained from a finite set of torus-orbit
representatives covering those points. The support result, (1), and
the previously proved determinant–Euler identity give, eventually,

\[
\chi_B(a;M_{\boldsymbol d})
=\sum_{\sigma\in\Sigma}m_{\sigma,\boldsymbol d}
     v_\pi(\sigma(a))
\le2^q\sum_{\sigma\in\Sigma}v_\pi(\sigma(a)). \tag{9}
\]

The valuations are nonnegative because each \(\sigma(a)\) lies in
the image of the finite \(\mathcal O\)-algebra \(B/Q_0\). Terms with
zero localized length may be retained. The distinct embedding
convention and ramification normalization are those of
[the determinant calculation](rh-selmer-euler-determinant.md).
At single-point slices one may replace the corresponding coefficient
\(2^q\) by \(2^{q-1}\). The construction of the arithmetic model and
its tangent and orbit-covering hypotheses remain inputs.

For clarity, the combined conclusion also requires all the chart and
Smith data of the leading-quotient and Koszul lower comparisons: in
particular \(r\ge1\), the stated chart-weight multiplicities, vanishing
of the chart on the \(Z_i\), and the **separate assumption**
\(\varphi(a)\ne0\). Neither two-sided point nonvanishing nor this upper
comparison proves that formal-chart condition. With those hypotheses,
the lower and upper inequalities give

\[
2^{r+r'}\sum_i c_i
\le\chi_B(a;M_{\boldsymbol d})
\le2^{r+1+r'}\sum_{\sigma\in\Sigma}v_\pi(\sigma(a)),
\qquad
\boxed{\sum_i c_i\le2\sum_{\sigma\in\Sigma}v_\pi(\sigma(a)).} \tag{10}
\]

The right side can be refined to coefficient one at single-point
slices and coefficient two at two-point slices. In the coarser bound,
replacing distinct characters by the original orbit representatives
can only increase the nonnegative sum. Thus the actual abstract
commutative-algebra core is supplied under its original chart,
spanning, finiteness, point-separation, tangent, nonvanishing, and
covering assumptions; none of those model conditions is proved by
the numerical argument.

The proof supplies the following exact contracts at
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

| Contract | File under `CommutativeAlgebra/` | Lines |
|---|---|---:|
| Finite quotient, two-sided tangent dimension, finite orbit cover | `OrbitVanishingLocal.lean` | 41--70 |
| Localized length normalization; actual Rees modules and squared ideal | `GradedModulesLength/ToDegInjective.lean` | 156--163, 187--218 |
| Eventual finite annihilator and exclusion of other generic characters | `GradedModulesLength/EventuallyMQGrFiniteAnnihilator.lean` | 57--123 |
| Localized unsquared weight length at most one | `GradedModulesLength/LocLenQuotientWeightPieceLeOne.lean` | 70--148 |
| Squaring the actual \(r+1+r'\) equations | `GradedModulesLength/LocLenAPieceIdeal2LeTwoPow.lean` | 69--115 |
| Localized Rees-piece comparison | `GradedModulesLength/LocalizedLengthLeOfSurjective.lean` | 124--151, 177--213 |
| Upper Euler comparison and distinct degree-zero characters | `GradedModulesLength/TwoSigned.lean` | 17--25, 63--94 |
| Combined core, including independent formal-chart nonvanishing | `GradedModulesLength/AlgMemCoef.lean` | 92--102 |

The reproducible checker passes eight pinned source contracts, sixteen
exact tangent examples (including nonreduced cases rejected by the tangent
hypothesis), fourteen sharp parity examples, 109,220 basis products, and
28,672 degree cases over finite rings with nilpotents. A boundary example
shows why the condition that every coordinate is positive cannot be omitted. The general support and slice proofs above are mathematical
arguments, not consequences of finite sample computation.
