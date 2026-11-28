# The link gain: congruence, torsion, and the remaining cut

## Exact scope

This note proves four ordinary ingredients of the pair-discriminant
estimate: the link graph and corank bounds, the determinant gain from
congruence, the reciprocal torsion-index cancellation, and the bound
for the gauge of a near term. It leaves one precise link-lattice cut
inequality, (15), open. The final pair gain is conditional on that
inequality; no full moment estimate is claimed.

Use the Hermitian space, frame, class lattices, and term lattices of
[the frame-fibre chapter](lsernau-corank-frame-fibres.md):
\[
 V=A\oplus(W\oplus Ez)\oplus A^*,\qquad
 h|_W=I_k,\quad h(z,z)=-N,\quad \dim A=\rho,\quad n=\rho+1.
 \tag{1}
\]
Two rational terms \(\gamma,\gamma'\) are over the same block, so
they carry the same target class lattice to the source class lattice
\(\Lambda\) and have the same reduction modulo \(M\). In particular
\[
              m=\gamma'\gamma^{-1}\equiv1\pmod {M\Lambda}.
 \tag{2}
\]
All lattice statements can be made place by place and then multiplied;
projective global lattices need not be free.

## 1. Links are graphs in a positive space

Put \(B_\gamma=A+\gamma A\) and \(J_\gamma=A\cap\gamma A\).
For \(t\in B_\gamma^\perp\), take the middle coordinates of
\(t\) and \(\gamma^{-1}t\). Their pairs form the link
\(\mathcal L_\gamma\subset (W\oplus Ez)^2\).
The kernel of this map is \(J_\gamma\). Indeed, zero middle
coordinates together with orthogonality to \(A,\gamma A\)
say that \(t\in A\) and \(\gamma^{-1}t\in A\).
Consequently
\[
 \dim_E\mathcal L_\gamma
   =\dim B_\gamma^\perp-\dim J_\gamma=k+1.                   \tag{3}
\]
The link is totally isotropic for the difference of the two middle
Hermitian forms: the pairings of \(t,t'\) and
\(\gamma^{-1}t,\gamma^{-1}t'\) agree.

Write a pair as \((w+\lambda z,w'+\lambda'z)\), and exchange
the two \(z\)-coordinates. It becomes
\[
                  (a,b)=((w,\lambda'),(w',\lambda))
\]
in the positive space \(P=W\oplus Ez^+\), where
\(\|z^+\|^2=N\). The difference form is now
\(\langle a,a'\rangle_P-\langle b,b'\rangle_P\).
Its restriction to the link is zero. The projection to the
first \(P\) is injective by positivity, and is bijective by (3).
Thus
\[
                 \mathcal L_\gamma=\operatorname{graph}(U_\gamma)
 \tag{4}
\]
for a unitary isometry of \(P\). The positive metric on a link
is the metric on this first \(P\).

Let \(i=\operatorname{codim}(\mathcal L_\gamma\cap
\mathcal L_{\gamma'})\) in either link. Let \(C\subset W\) be
the space on which the two isometries agree and have image in
\(W\). Intersecting the common graph first with zero source
\(z\)-coordinate, then with zero target \(z\)-coordinate, costs
at most two dimensions. Therefore
\[
                    \operatorname{codim}_W C\le i+1.       \tag{5}
\]
In particular equal links have corank at most one in \(W\).
If a term has a cell index \(j<n\), its shared last frame vector
has the form \(Q_\gamma y=Fx\), with \(y_{n-1}=1\).
The frame Gram identity implies \(|x_{n-1}|^2=1\).
This pair belongs to the link and has both \(W\)-coordinates
zero. Hence \(U_\gamma\) preserves the \(z^+\)-line, and so
preserves \(W\). Equal links in this case have \(C=W\), of
corank zero. The triangular tail argument in the frame-fibre
chapter proves the shared-vector assertion directly from the
actual cell condition.

Conversely, suppose \(U_\gamma\) preserves the \(z^+\)-line.
Its graph contains a pair with both \(W\)-parts zero and both
\(z\)-coordinates nonzero. A lift gives \(Fx=\gamma Fy\), and
after scaling \(y_{n-1}=1\) one has
\(x_{n-1}\overline{x_{n-1}}=1\).
If \(D_n=\det Z_\gamma\ne0\), then
\[
 Z_\gamma y=-N x_{n-1}e_{n-1},\qquad
 (Z_\gamma^{-1})_{n-1,n-1}=-\frac1{N x_{n-1}}.
\]
The complementary-minor formula therefore gives
\(D_n\overline{D_n}=N^2D_\rho\overline{D_\rho}\).
An actual top-cell term has nonzero difference of these two
quantities by its cell condition. Its \(U_\gamma\) cannot preserve
the line, so \(W\cap U_\gamma^{-1}W\) has codimension exactly one.
Thus equal links have simultaneously zero term discriminants
or simultaneously nonzero term discriminants. Their common
space \(C\) has corank respectively zero or one.

## 2. The congruence determinant gain

Let \(A_\gamma\) and \(A_{\gamma'}\) be rank-\(i\) lattices
in complements to \(\mathcal L_\gamma\cap\mathcal L_{\gamma'}\).
Suppose their basis vectors, after adding vectors in the common
link, have integral lifts in \(\Lambda\). This is the exact
lift condition used by the source's link splitting.

The difference form \(\mathcal B\) pairs the two complements
nondegenerately. To see this, a vector in the second complement
orthogonal to the first is also orthogonal to the common link,
since the latter lies in the second isotropic link. It is therefore
orthogonal to all of the first link. A maximal isotropic link is
its own orthogonal, so the vector lies in their intersection and
must be zero.

The same pairing is integral after division by \(M\). For integral
lifts \(t,t'\), it is
\[
 \mathcal B(t,t')
   =h(t,t')-h(\gamma^{-1}t,\gamma'^{-1}t')
   =h((1-m)t,t')\in M\widehat{\mathcal O}_E,                 \tag{6}
\]
by (2). Adding common-link vectors does not change this pairing.

For a positive rank-\(i\) lattice \(L\), let \(d(L)\) be the square
root of the norm of its Gram determinant ideal, with the same
normalization as in the weighted lattice chapter. Then
\[
 \boxed{\displaystyle
      d(A_\gamma)d(A_{\gamma'})
                          \ge(M/2)^{2if}.}                \tag{7}
\]
Here is a proof with all powers specified. In positive coordinates
the cross-pairing is
\[
                 a^*(1-U_\gamma^*U_{\gamma'})b.
 \tag{8}
\]
At each infinite embedding, exterior-power Cauchy–Schwarz and
\(\|1-U_\gamma^*U_{\gamma'}\|\le2\) give
\[
 |\det(8)|\le2^i
        \det(a^*a)^{1/2}\det(b^*b)^{1/2}.                   \tag{9}
\]
Take the product of squared absolute values over the \(f\)
complex places, and multiply by the finite determinant indices
of the chosen local lattice bases. Since (6) is a nondegenerate
integral pairing after division by \(M\), its determinant ideal
has positive integer norm, at least one. We obtain
\[
       1\le M^{-2if}2^{2if}
                     d(A_\gamma)d(A_{\gamma'}),
\]
which is (7). This also proves the assertion for nonfree projective
lattices: local determinant indices transform the two sides by
the same factors. For \(i=0\) all determinants are one.

## 3. The reciprocal intersection index

For \(\gamma'\), define the torsion module and its order by
\[
 T_{\gamma'}=
 \frac{\Lambda\cap(A+\gamma'A)}
      {(\Lambda\cap A)+\gamma'(\Lambda'\cap A)},\qquad
                       t_{\gamma'}=|T_{\gamma'}|.          \tag{10}
\]
Here \(\Lambda'\) is the target class lattice; its isotropic
lattice is the same standard \(\mathcal O_E^\rho\).
The quotient is finite since numerator and denominator span the
same rational subspace. Define
\[
 C_\gamma=(\Lambda\cap C)\cap L_\gamma,\qquad
 L_{12}=C_\gamma\cap L_{\gamma'} .
\]
These are full lattices in \(C\). Indeed, the common-link pair
associated to \(v\in C\) has both \(z\)-coordinates zero. Its lift
through \(\mathcal L_\gamma\) has the form \(t=v+a\), with
\(a\in A\), and is orthogonal to \(\gamma F\). Thus the rational
linear term-lattice equation \(Q_\gamma^*J(v+a)=0\) is solvable
for every \(v\in C\); the same holds for \(\gamma'\).
Choose rational linear right inverses on \(C\). Clearing their
finitely many denominators and the fixed factor \(M\) shows that
one nonzero integer multiple of \(\Lambda\cap C\) lies in both
term lattices. Hence \(C_\gamma,C_{\gamma'}\), and \(L_{12}\)
all have rank \(\dim C\). This argument uses no discriminant cut.

Then
\[
 \boxed{\displaystyle
             [C_\gamma:L_{12}]\mid t_{\gamma'}.}          \tag{11}
\]
The corresponding statement with \(\gamma,\gamma'\) exchanged
also holds.

For the index proof complete the lattices at the finite places;
their finite indices are unchanged. The same letters now denote
these completions and the corresponding rational spaces tensored
with \(\mathbb A_{E,f}\).
Write \(P'v=Q_{\gamma'}^*Jv\), and set
\(J'=P'(\Lambda\cap A)\). The homomorphism
\[
             C_\gamma\longrightarrow\mathbb A_{E,f}^n/(MJ'),\qquad
                            v\longmapsto P'v              \tag{12}
\]
has kernel \(L_{12}\), by the definition of \(L_{\gamma'}\).
We show that its image is a subgroup of a quotient of
\(T_{\gamma'}\).

Choose \(a\in\Lambda\cap A\) so that
\(y=v-Ma\) is orthogonal to \(Q_\gamma\). Since \(v\in C\),
one can also choose \(y'\in v+A\) orthogonal to \(Q_{\gamma'}\)
with the same middle image after applying the respective inverses.
Thus
\[
 my-y=(y'-y)+
            \gamma'(\gamma^{-1}y-\gamma'^{-1}y')
                       \in A+\gamma'A.                  \tag{13}
\]
This is rational linear algebra; it remains true on every finite
completion. By (2), \(w=(y-my)/M\) is an integral vector in this
span. Moreover \(P'my=0\), since \(mQ_\gamma=Q_{\gamma'}\).
Therefore \(P'v=M(P'a+P'w)\).

It follows that the image of (12) is contained in
\(MP'(\Lambda\cap(A+\gamma'A))/(MJ')\). The latter is a quotient
of (10), because \(P'\) kills \(\gamma'(\Lambda'\cap A)\).
The order of any subgroup of a quotient of a finite group divides
its order. This proves (11), including its finiteness; a chosen
lift \(a\) need not depend linearly on \(v\).

Discriminants of full lattices scale by additive indices.
Consequently (11) implies
\[
 d(L_{12})^2\le
        t_\gamma t_{\gamma'}\,d(C_\gamma)d(C_{\gamma'}).
 \tag{14}
\]
The torsion factors have deliberately exchanged positions. Losing
this cancellation would spoil the exact gauge gain.

## 4. The one remaining cut inequality

The following is the exact remaining geometric supplier.

**Open link-lattice cut.** For two actual character-compatible terms
of specified cell indices, construct complementary lattices
\(A_\gamma,A_{\gamma'}\) satisfying the integral-lift hypothesis of
§2, and prove
\[
 \begin{split}
 t_\gamma d(C_\gamma)d(A_\gamma)X&\le G_\gamma,\\
 t_{\gamma'}d(C_{\gamma'})d(A_{\gamma'})X&\le G_{\gamma'} .
 \end{split}                                               \tag{15}
\]
Here \(X=1\) except when the links are equal and have the top cell
index; in that case \(1\le X\le\operatorname{meetNorm}(s)\).
The positive scalar \(G_\gamma\) is the actual level gauge, defined
in §5. The meet norm is the product of residue-field sizes at the
specified level places where the reduced frame spans meet.

This is a statement about the precise integral link lattice and
the two forms recording its \(z\)-coordinates. It does not follow
from (7), ordinary Euclidean packing, or a generic covolume bound.
The source proof combines a bordered Jacobi identity in
\((\Lambda\cap J_\gamma^\perp)/(\Lambda\cap J_\gamma)\), the
two isotropic-row indices, and a rank-at-most-two cut by those
\(z\)-forms. Its meet-norm improvement is part of (15), not an
extra factor that may be assumed afterward.

**Conditional pair gain.** Assuming (15), equations (7), (14)
give, with no further hypothesis,
\[
 \boxed{\displaystyle
 \bigl(d(L_{12})X(M/2)^{if}\bigr)^2
                             \le G_\gamma G_{\gamma'}.}    \tag{16}
\]
Indeed multiply (15), use (14), and then use (7) to bound the
product of the complementary discriminants from below.
Thus the congruence and reciprocal-index parts of the gain are
closed; precisely the cut (15) remains.

## 5. The actual gauge and its near-term bound

Let \(Z_\gamma=F^*J\gamma F\), \(D_a\) its leading minor of order
\(a\), and let \(\Delta_*\) be the minor on the first \(j\) frame
indices together with the last index (without repeating that last
index when \(j=n\)). Put
\[
 \begin{split}
 \mathfrak d_\gamma&=D_n\overline{D_n}-N^2D_\rho\overline{D_\rho},\\
 G_\gamma&=M^{2\min(\rho,j)f}
   \max\!\left\{
     \frac{|N_{E/\mathbb Q}(\Delta_*)|}
                  {I_\gamma I_{\gamma^{-1}}N^f},
     \prod_{\sigma\in\Phi}|\sigma(\mathfrak d_\gamma)|
       \right\}.
 \end{split}                                               \tag{17}
\]
Here \(I_\gamma\) is the isotropic-row index: if \(R_a\) is the
lattice spanned by the first \(a\) rows of \(Z_\gamma\), then
\(I_\gamma=[R_\rho:R_{\min(j,\rho)}]\).
Rows are numbered from zero; the last frame row is never included.
The actual finite class coordinates give this same definition.
The distinct notation \(J_\gamma\) in §1 denotes an intersection
subspace, not this integer.

These row indices are positive. For \(j\le\rho\), the shared-tail
condition says that the first \(\rho\) rows of \(Z_\gamma Y^{-1}\)
have zero tail columns, so they are spanned by the first \(j\)
rows of \(Z_\gamma\). These first \(j\) rows are independent
because \(D_j\ne0\). For \(j=n\), the index is one. The same
argument applies to \(\gamma^{-1}\), whose shared flag pairs
are obtained by exchanging the pair and whose leading minors
are conjugates.

The bordered minor \(\Delta_*\) is nonzero. For \(j<n\), take the
shared last column \(Q_\gamma Y^{-1}e_{n-1}=Fx\).
The last coordinate of \(Y^{-1}e_{n-1}\) is one, so
\(|x_{n-1}|^2=1\). The Schur complement formula gives
\(\Delta_*=-N x_{n-1}D_j\ne0\). For \(j=n\), it is \(D_n\ne0\).
Thus \(G_\gamma>0\).

For a near term, the frame-fibre chapter proves
\(|\sigma(Z_{\gamma,ab})|\le b^{134n}\). Every square minor of
size at most \(n\) therefore has absolute norm at most
\(b^{270n^2f}\). The discriminant in (17) satisfies the
deliberately coarse estimate
\[
 \prod_\sigma|\sigma(\mathfrak d_\gamma)|
                    \le b^{(270n^2+120n+1)f},              \tag{18}
\]
using \(N\le b^{60n}\) and \(2\le b\).
Discarding denominators at least one, and using \(M\le b^{23}\),
gives
\[
 0<G_\gamma\le b^{(270n^2+166n+1)f}
                              \le b^{n^3f}=H.              \tag{19}
\]
The last inequality holds already for \(n\ge1000\), well within
the actual \(n\ge100001\). Hence this gauge bound is supplied
independently of the open cut (15).

**Conditional range corollary.** Once (15) is supplied, no further
range theorem is needed to apply the proved pair count.
The common lattice is integral in the definite class lattice, so
\(d(L_{12})\ge1\). By (16), \(X\ge1\), and (19),
\[
 d(L_{12})\le H,\qquad (M/2)^{if}\le H.
\]
The actual \(M\ge b^{19}\), \(b\ge2\), imply \(M/2\ge b^{18}\).
Since \(H=b^{n^3f}\), this gives \(i\le n^3/18\) and therefore
\(\ell=\operatorname{codim}_W C\le i+1\le n^3\).
Equal-link pairs already have \(\ell\le1\). Thus (15) supplies
both the gain and exactly the discriminant/corank range consumed
by the weighted pair-count theorem.

## 6. Immutable source and verification

All source files are at
[72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src),
attributed to Levent Alpöge's announced work.

| Source file | Role |
|---|---|
| New/Spanning/Unfolding/Terms.lean, 108–126 | Actual cell and term-discriminant definitions |
| New/Spanning/RemainingTerms/Gain.lean, 58–98, 118–347 | Graph coranks and congruence determinant estimate, proved in §§1–2 |
| New/Spanning/RemainingTerms/Gain.lean, 460–513, 622–850 | Common-link lift, reciprocal torsion index, and assembly, proved in §§3–4 |
| New/Spanning/RemainingTerms/BorderedDeterminant.lean, 404–450 | Exact gauge normalization in (17) |
| New/Spanning/RemainingTerms/Data.lean, 65–74 | Level factor in the actual gauge |
| New/Spanning/RemainingTerms/Sum.lean, 88–121 | Required pair range and the actual \(M\ge b^{19}\) bound |
| New/Spanning/RemainingTerms/LinkLattice.lean, 242–439, 787–end | Bordered Jacobi and integral link-lattice supplier still required for (15) |
| New/Spanning/RemainingTerms/Cut.lean, 154–309, 528–637 | The rank-two \(z\)-form and meet-norm cut still required for (15) |

The [exact checker](../scripts/check_link_gain_index.py) records these
immutable blobs, checks finite quotient maps by enumeration and
independent Hermite normal forms, tests graph coranks and determinant
bounds over \(\mathbb Q(i)\), and certifies the universal gauge exponent
inequality by a polynomial with nonnegative coefficients.
Its [certificate](../certificates/link-gain-index.json) records the
actual counts and the SHA-256 of this note. The status of (15) remains
open regardless of those checks.
