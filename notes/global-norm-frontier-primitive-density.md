# A signed refinement of the original primitive local densities

## Result and scope

The finite-place density used in the global norm argument is a count of
**primitive residue-field frames**, with its original normalization. The
exact count and dyadic lifting were already proved in
`paper/sections/recovered/70-md-section.tex`, Theorem `md-frame-count`
and Proposition `md-lifting`; its closing paragraph explicitly applies
the count to the source density for all coranks. They are not newly
closed suppliers. A short independent proof is recorded below to make
the sharper signed estimate auditable.

The new refinement identifies the sign of the local error and, in the
original even ranks, improves the uniform positive-error exponent by one.
The source dictionary also confirms the existing count supplies
`ExactLocalDensityAllModels` and the first estimate in
`FamilyVolumeFourth` with constant one. The separate equality of densities
for the source's scalar pairs is not claimed here. Nor does this prove
the global period norm estimates: the
archimedean orbital bounds, their assembly, the source and target cuts,
and the common normalizers are still required. Whole-node counts are
unchanged: RH **6/9**, GRH **17/31**.

The quantitative improvement is a finite-place saving. Positive density
errors occur only at inert places with odd residue corank. This is not a
new leading exponent in the final height contradiction.

All source references below use
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

## 1. Exact normalized count

Let \(K\) be a finite field of order \(q\ge2\). Let \(L\) be its
quadratic extension, or the split algebra \(K\times K\), with its usual
involution. Write \(\eta=-1\) in the field case and \(\eta=1\) in the
split case. Let \(V\) be a nondegenerate Hermitian space of rank \(N\)
over \(L\). Fix a Hermitian matrix \(A\) of size \(m\), of corank
\(c\), where \(m+c\le N\). In the split case, its two components
are transposes and have the same rank.

Count the injective \(L\)-linear maps \(X:L^m\to V\) with Gram
matrix \(A\). Over the split algebra, injectivity is required on both
components. Normalize the count by \(q^{2Nm-m^2}\), and call the result
\(\delta(A)\). Then, with \(d=N-m-c+1\),

\[
 \boxed{\displaystyle
 \delta(A)=\prod_{j=d}^{N}(1-\eta^j q^{-j}).}
 \tag{1}
\]

The empty case \(m=0\) gives one. The matrix need not be nonsingular.

### Split case

Choose dual coordinates in which the two components of \(X\) are
\(N\)-by-\(m\) matrices \(X_1,X_2\), and their pairing is
\(X_1^{\mathsf t}X_2=A\). There are
\(\prod_{i=0}^{m-1}(q^N-q^i)\) possibilities for the full-rank matrix
\(X_1\). After a change of dual coordinates, fixing \(X_1\) fixes
the first \(m\) rows of \(X_2\) to be \(A\). If \(B\) denotes
its remaining \(N-m\) rows, \(X_2\) is injective exactly when
\(B|_{\ker A}\) is injective. There are therefore

\[
 q^{(N-m)(m-c)}\prod_{i=0}^{c-1}(q^{N-m}-q^i)
\]

possibilities for \(B\). Multiplication and division by the prescribed
normalizer give (1).

### Quadratic-field case, including characteristic two

Hermitian diagonalization gives \(A\) as a nondegenerate block of rank
\(s=m-c\) followed by a zero block. No division by two is needed:
the trace \(L\to K\) is onto, so a nonzero off-diagonal entry of a
Hermitian form with zero diagonal produces a vector of nonzero norm.
Norm surjectivity then scales each nonzero diagonal entry as needed.

In a nondegenerate Hermitian space of dimension \(D\), the numbers of
vectors of any specified nonzero norm and of norm zero are respectively

\[
 V_D=q^{2D-1}-(-1)^Dq^{D-1},\qquad
 Z_D=q^{2D-1}+(q-1)(-1)^Dq^{D-1}.
 \tag{2}
\]

For completeness, for a nontrivial additive character \(\psi\) of
\(K\), the norm map has one zero fibre and \(q+1\) elements in
each nonzero fibre. Hence
\(\sum_{z\in L}\psi(z\bar z)=-q\).
Additive-character orthogonality in each coordinate gives (2). This
argument includes characteristic two.

Choose the \(s\) nonzero-norm, mutually orthogonal vectors successively.
Their count is \(\prod_{i=0}^{s-1}V_{N-i}\). Their orthogonal
complement has dimension \(D=N-s\). Having chosen an independent
isotropic frame spanning \(R\) of dimension \(i\), the next vector
must project to a nonzero isotropic vector in
\(R^\perp/R\), of dimension \(D-2i\). Each such vector has
\(q^{2i}\) lifts. Thus the remaining count is

\[
 \prod_{i=0}^{c-1}q^{2i}(Z_{D-2i}-1).
\]

The identity
\(Z_e-1=(q^e-(-1)^e)(q^{e-1}+(-1)^e)\)
makes the factors consecutive. Their powers of \(q\) total
\(2Nm-m^2\), proving (1).

## 2. Signed estimates without a rank multiplier

In the split case, all the factors lie in \((0,1)\). Consequently

\[
 0\le1-\delta(A)\le\sum_{j=d}^{N}q^{-j}
       \le\frac{q^{-d}}{1-q^{-1}}\le2q^{-d}.
 \tag{3}
\]

In the quadratic-field case the stronger signed statement is

\[
 \begin{array}{ll}
 1-q^{-d}\le\delta(A)\le1,& d\text{ even},\\[2pt]
 1\le\delta(A)\le1+q^{-d},& d\text{ odd}.
 \end{array}
 \tag{4}
\]

Indeed, an adjacent pair starting at an odd index has product at least
one, and a pair starting at an even index has product at most one.
An unmatched last factor has the same sign of deviation as the first.
This proves the side of one on which the whole product lies. Removing
the first factor leaves a product on the other side of one, which gives
the stated endpoint bound. Explicitly, the odd pair is
\((1+t)(1-t/q)=1+t(1-q^{-1}-t/q)\ge1\), since
\(0<t\le q^{-1}\) and \(q\ge2\). The even pair is
\((1-t)(1+t/q)\le1\).

For the original parameters,

\[
 m=2r+2,\quad N=2r+k+1=k+m-1,\quad
 d=k-c,\quad d_0=k-m.
 \tag{5}
\]

Both \(k\) and \(m\) are even. Thus a positive error is possible
only in the quadratic-field case with \(c\) odd; then
\(c\le m-1\) and \(d\ge d_0+1\). For every original local
matrix, therefore,

\[
 |\delta(A)-1|\le2q^{-d_0},\qquad
 0<\delta(A)\le\exp(q^{-(d_0+1)}),
 \tag{6}
\]

and the split density is at most one. Since \(m\ge2\), the first
bound implies the source's \(m q^{-d_0}\) bound, with constant one.
The second is stronger than its required \(\exp(4q^{-d_0})\).

## 3. Original lattice and finite-level dictionary

Let \(F_v\) be an original nonarchimedean local field and let
\(E_v/F_v\) be the quadratic unramified algebra specified by the
source. Let \(\Lambda\) be its original self-dual Hermitian lattice.
It is free over the maximal integral algebra; its reduced Hermitian
form is nondegenerate. A tuple is primitive in the source's sense
exactly when its residue classes are independent over the quadratic
residue field, or independent in both split components. This follows
from the elementary-divisor theorem over a discrete valuation ring,
applied separately to the two split components. Every independent
residue tuple lifts to a primitive tuple by completing it to a basis.
Self-duality supplies the nondegeneracy of the reduced form.

The source density counts precisely these residue tuples and divides
by \(q^{2Nm-m^2}\). Thus (1) evaluates that exact density. No Haar
rescaling, primitivity deletion, or replacement of the integral lattice
is involved. Its convention \(h(v_b,v_a)\) for a Gram entry agrees
after transposition with the count above and leaves the corank unchanged.

At a designated split level, keep the actual modified tuple

\[
 \bigl(f_a,\;\varpi^{-1}(f'_a-f_a)\bigr)_{0\le a\le r}.
 \tag{7}
\]

At the other places use \((f_a,f'_a)_a\). The source's generic
condition asserts primitivity of exactly this tuple, and all its Gram
entries are therefore integral. Formula (1) is applied to its full
residue Gram matrix; it does not replace (7) by the unmodified pair.
In particular, it retains every possible residue corank, including
\(c=m\). The possibly nonmaximal split order used elsewhere in the
kernel construction does not replace the maximal integral algebra in
this density definition.

The actual rank assumptions imply \(k\ge m+4\), so \(d_0\ge4\)
and \(m+c\le N\). The stronger condition
\(k\ge4r+8\) in `ExactLocalDensityAllModels` also suffices. This
proves its entire displayed density bound, including its split clause.
It does not prove the separate scalar-pair invariance in
`FamilyVolumeFourth`, the local kernel decomposition, or the
archimedean Bessel estimates.

## 4. Effect on an actual finite-place product

Suppose these local densities occur over a number field of degree
\(f\), with the same \(k,m\) and \(d_0\ge4\). The product
\(\mathcal D=\prod_v\delta_v\) converges absolutely to a positive
number: (6) bounds the sum of absolute deviations, and every local
factor is positive. Only inert places with odd corank can increase it.
Writing \(s=d_0+1\),

\[
 \log\mathcal D
 \le\sum_{\substack{v\text{ inert}\\c_v\text{ odd}}}q_v^{-(k-c_v)}
 \le f\sum_{p\text{ rational prime}}p^{-s}
 \le f\,2^{-s}\left(1+\frac{2}{s-1}\right).
 \tag{8}
\]

The first inequality retains the signed local information. For the
second, at most \(f\) places lie over a rational prime and
\(q_v\ge p\). The last follows by including all integers at least
two and comparing the tail with an integral. It is an upper bound on
the actual product, not on the product of the absolute local errors.

When the inert Gram matrices come from one nondegenerate integral
global matrix, positive factors can occur only at the finitely many
primes dividing its determinant. This observation requires that global
matrix identification; it is not silently imposed on arbitrary locally
specified data. Inequality (8) needs no such identification.

This improves the finite-place coefficient already isolated by the
source's positive local-kernel majorant. It does not bound the original
period Gram operator by itself. In particular, it supplies neither
archimedean decay relative to the prescribed period mass, nor a bound
for the high inverse-minimum factor in the projector tail.

## 5. Verification evidence

The accompanying checker authenticates the following bounded excerpts
against the pinned source inventory and records their hashes. It also
checks finite-field counts independently by exhaustive enumeration,
including characteristic two, exact products and signed endpoints,
the original parity improvement, and negative controls which remove
primitivity or alter the normalization. These finite checks support the
general proof above; they are not a Lean build or a computational proof
of the global norm estimate.

| Pinned module | Ranges | Exact role |
|---|---|---|
| `Formalism.LocalRingCardinality.Params` | 6–46 | Even \(k,m\), original ranks and \(r=m/2-1\). |
| `Formalism.SharpRestriction.CuspSpanNormBounds.FractionFieldToGenericStalkAlgebraMapEq` | 10–26, 31–59, 71–80 | Quadratic unramified local algebra, split order, original local-field assumptions. |
| `Formalism.SharpRestriction.CuspSpanNormBounds.LinQRawRange` | 43–52, 105–120, 165–174 | Self-dual lattice, primitivity, original modified tuple, density and denominator. |
| `Formalism.LocalToGlobal.SiegelLatticeTheory.SiegelMassRatios.DensExact` | 9–39 | Independent source statement of the finite counts and consecutive product. |
| `Formalism.PeriodIntegrals.UnitaryGroupMassFormula.LocalDensityCorank.CongruenceDensity` | 43–52 | Exact original density as a residue-class count. |
| `Formalism.SharpRestriction.CuspSpanNormBounds.LocalBesselAndTopKernel` | 87–96, 139–167, 577–578 | Original local inequalities and their global-norm supplier. |
