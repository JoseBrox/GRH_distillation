# Compact real edges and nonzero odd-rank theta lifts

Source: [readable revision 72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src),
Lib/Weil/CompactLift/ThetaKernelDefs.lean, 230–370,
DefiniteThetaLift.lean, 71–193, Lib/Weil/Lift.lean (IsHalfEdge,
IsEdge), Lib/Adelic/AutomorphicForms/AutomorphicAsAlgebraic.lean,
and Lib/GaloisRep/Main/ThetaLift.lean, 303–end.

We supply the compact-real case needed in all-rank attachment by
ordinary Cauchy decomposition and compact Schur orthogonality,
rather than the general noncompact local correspondence.

## Actual weights, polynomial and covariance

Let \(M=n+s,\ s>n\). At each infinite place let \(\kappa_h\)
(\(h<n\)) and \(e\) be the original column numbers and determinant
exponent. Take a tame-trivial character \(b\) of infinity weight
\(c\le e\). The source target weight has last entry zero and
column numbers
\[
 k_h=\kappa_h\ (h<n),\qquad k_n=e-c,\qquad k_h=0\ (n<h<M).
\]
All are nonnegative. Its row lengths are
\(\lambda_i=\sum_{h=i}^n k_h\), padded by zeros. The original
source rows including the determinant shift are \(\lambda_i+c\).
The joint highest polynomial at this place is
\[
 P(Z)=\prod_{h=1}^n\det Z_{[1,h],[1,h]}^{k_h}.
\]
It is nonzero, by evaluation at the rectangular identity, even
in degree zero. Its diagonal weights are the row lengths, and
the triangular raising operators annihilate it by the
elementary row and column addition rule for determinants.
Take the product over infinite places.

Use the source conjugate Weyl representations
\(\pi=\mathrm{conjWeylRep}(\kappa,e)\) and
\(\pi'=\mathrm{conjWeylRep}(k,0)\). For the rectangular
Schur matrix \(S_k(Z)\) and coefficient polynomial
\(P_{A,\xi}=A S_k(Z)\xi\), the actual Weil action is
\[
 \Omega(x,y)P_{A,\xi}=P_{A\pi'(y^{-1}),\,\pi(x)\xi}.           \tag{1}
\]
Indeed in positive Fock coordinates substitution is
\(Z\mapsto y^tZ(x^{-1})^t\) with the source determinant
factor \((\det x)^{-c}\).
The full-height minors contribute \((\det x)^{-(e-c)}\);
the remaining minors give the conjugate Weyl representation
since \(x^{-t}=\bar x\), and \(y^t=\overline{y^{-1}}\).
This is the composition law of ThetaKernelDefs.lean,
not a change to the contragredient convention.

By the classical Cauchy identity (equivalently Schur–Weyl
duality and diagonal symmetric-group invariants in each
homogeneous degree), the polynomial representation of
the two compact groups is the multiplicity-free sum of
the pairs of Schur modules indexed by partitions with
at most \(n\) rows. The determinant twist on the source
is fixed. Therefore the \(\pi\)-isotypic polynomial
subspace is precisely this single pair \(\pi\otimes(\pi')^*\).
No other degree can contribute to it.

For a direct check of the compact parameter rule, the
source doubled HC entry in decreasing position \(p<n\) is
\[
 l_p=2e+2\sum_{p<h<n}\kappa_h+n-1-2p.
\]
Subtracting \(2c\) and adding \(M\) gives exactly the
first \(n\) target HC entries shifted by \(n\);
the remaining target shifted entries are
\(M-n-1,M-n-3,\ldots,-(M-n-1)\).
The source shifted entries all exceed this block.
The required distinctness and parity hold, and the
opposite-sign gap restriction is vacuous for compact groups.

## Nonzero zeta integrals and real convolution

Take unit highest vectors \(u,u'\) in the invariant Gram
forms of \(\pi,\pi'\), respectively. The source compact
kernels are
\[
 e_S(x)=d_S\langle u,\pi(x)u\rangle,\quad
 e_T(y)=d_T\langle u',\pi'(y)u'\rangle
\]
with \(d_S=e_S(1)>0,d_T=e_T(1)>0\) their formal
degrees for the actual Haar measures (dimension divided
by compact volume). Choose \(v\) to be the Fock vector
of \(P_{\langle u',-\rangle,u}\). It is a nonzero
multiple of the nested-minor vector, after ordering the
coordinates by the highest vectors: this follows from
the highest Schur coefficient, or evaluation on the
rectangular identity in the compatible highest coordinates.
By irreducibility of the tensor pair in (1), the invariant
Fock pairing is a positive multiple of the product pairing.
Thus its source matrix coefficient is
\(\|v\|^2e_S(x)/d_S\), and its target coefficient is
\(\|v\|^2\overline{e_T(y)}/d_T\).
Schur orthogonality gives the exact zeta integral
\[
 Z_v=\int\langle v,\Omega(x,1)v\rangle
                       \overline{e_S(x)}/e_S(1)\,dx
                  =\|v\|^2/d_S>0.                            \tag{2}
\]
The swapped integral is \(\|v\|^2/d_T>0\).

For a form of type \(e_S\), the identity
\(y=\operatorname{realConv}_{e_S}y\) replaces an arbitrary
polynomial datum \(w\) in the lift by
\(\int e_S(x)\Omega(x^{-1},1)w\,dx\), by changing the
source integral variable. This is the projection onto
the \(u\)-line, with surviving polynomial space
\(u\otimes(\pi')^*\). Our \(v\) belongs to that space.
On the target, \(\int e_T(y)\Omega(1,y)\,dy\) is the
highest dual-line projection, so the lift of \(v\) has
type \(e_T\). It has an open finite level by smoothness
of the finite datum. Every projected polynomial \(w_0\)
is a target convolution of \(v\); the Schur frame formula is
\[
 w_0=\frac{d_T}{\|v\|^2}\int
      \langle\Omega(1,y)v,w_0\rangle\,\Omega(1,y)v\,dy .
\]
The coefficient is continuous with compact support since
the group is compact. Inserting this under the theta
integral proves the full compact half-edge convolution
property, and the swapped statement uses the dual kernels.
All integrations here are justified by compact quotient
convergence. This verifies the source IsEdge conditions
without a noncompact formal-degree integral.

The scalar form associated to a vector-valued algebraic
form \(\phi\) is \(\langle u,\pi(x^{-1})\phi(g)\rangle\).
Its vanishing for all \(x\) detects \(\phi(g)\), since
the orbit of \(u\) spans the representation. Conversely
compact matrix-coefficient projection identifies every
form of type \(e_S\) with such a vector-valued form:
on each finite variable recover the vector by Schur
orthogonality in the real variable. The two constructions
respect rational covariance and finite level. Consequently
the nonzero scalar lift gives a nonzero algebraic form.

## Nonzero odd-rank lifts

Use [sharp data and Rallis inversion](lsernau-rallis-sharp-inversion.md)
with the open stabilizer of a given nonzero definite form
and its tame-trivial character \(b\). The rank is in the
strict stable range, all doubled rational Lagrangians are
graphs, (2) supplies the real scalar, and the constructed
sharp finite datum is vacuum at every spherical place
of the source. Hence the actual lift is nonzero. The
target compact fixes the datum at each such place,
preserving sphericity. At a split spherical place apply the
general-rank, unramified-character identity of
[split Weil transfer](lsernau-split-transfer-and-level-lifts.md),
Sections 1–2, under the compact source integral.

Write \(\theta_{b;k,j}=b^{\mathrm{BC}}\upsilon^{-k}|\cdot|^{j-k/2}\).
For the reciprocal polynomial of ThetaLift.lean the two
scalar relations (lines 326–354) are
\[
 \frac{q^s f_1(n)}{f_b(M)}\theta_{b;s,s}(\varpi)=1,\qquad
 \theta_{b;M,s-a}(\varpi)=q^a f_1(n)\theta_{b;s,s}(\varpi).
\]
They follow directly from the source Frobenius scalar
\(f_b(M)=q^{M/2}b^{\mathrm{BC}}(\varpi)\upsilon(\varpi)^{-M}\)
and \(|\varpi|=q^{-1}\). The monic normalized polynomial
is therefore
\[
 P_w(X)\prod_{a=0}^{s-1}(X-\theta_{b;M,s-a}(\varpi_w)).
\]
Taking \(s=n+1\) and the two characters of the
[two-string chapter](lsernau-galois-two-string.md) gives
both required nonzero lifts to odd rank \(2n+1\) with
their exact spherical identities. The nonzero-lift
supplier is thus discharged relative to the convergent
classical Siegel–Weil input and earlier local constructions.
The odd-rank Galois representation construction, weak base
change and Iwahori/Shintani comparison remain separate.
The noncompact real edges of the determinant chain are
not proved by this compact argument. No Lean replay is
asserted.
