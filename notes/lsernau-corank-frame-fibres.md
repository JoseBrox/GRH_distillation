# Frames above a lattice: three finite quotients

## Scope

This chapter supplies the frame-fibre estimate left as (24) in
[the weighted lattice count](lsernau-link-lattice-counting.md).
The proof uses explicit unipotent matrices and three finite quotients.
It does not require a new theta or spectral theorem. Together with that
lattice count, it proves the weighted near-pair count used by
[the single-link energy reduction](lsernau-single-link-energy-frontier.md).
The gauge-dependent orbit size and discriminant gains remain separate.

The objects are the actual admissible filling objects. To make the
scope checkable, the finite lattice and archimedean conditions needed
below are stated explicitly and their roles are proved. No imported
frame-counting theorem is being used as a proof.

Let \(E/E^+\) be CM of degree \(2f\), containing a primitive third root
of unity. The actual field contains the 5040th roots, which is more
than needed here. Set
\[
 V=A\oplus(W\oplus Ez)\oplus A^*,\quad
 \dim A=\rho,\quad \dim W=k,\quad n=\rho+1,
 \qquad h(z,z)=-N .
\]
The Gram matrix is
\[
 J=\begin{pmatrix}0&0&I_\rho\\0&I_k\oplus(-N)&0\\
                   I_\rho&0&0\end{pmatrix},
 \qquad F=(e_1,\ldots,e_\rho,z).
 \tag{1}
\]
Put \(Q_\gamma=\gamma F\) and \(Z_\gamma=F^*JQ_\gamma\). In blocks write
\(Q_\gamma=(a_\gamma,x_\gamma,z_\gamma,p_\gamma)^t\), where \(x_\gamma\)
has its rows in \(W\). Thus
\[
 p_\gamma=\text{first \(\rho\) rows of }Z_\gamma,\qquad
 z_\gamma=-N^{-1}\text{last row of }Z_\gamma .
 \tag{2}
\]

For a definite class \(c\), let \(\Lambda_c\) be its full integral
unimodular Hermitian lattice in \(V(\mathbb A_f)\). Its isotropic
blocks are the standard integral blocks; write
\(\Lambda_{W,c}=\Lambda_c\cap W(\mathbb A_f)\).
A term from \(c'\) to \(c\) is integral between these prescribed
lattices. The standard frame is integral in every \(\Lambda_{c'}\).
Consequently \(a_\gamma\) and \(Z_\gamma\) are integral, and, if two
terms have the same \(Z\), every column of
\(x_\gamma-x_{\gamma'}\) belongs to \(\Lambda_{W,c}\).
These assertions follow by applying the integral isometry to the
frame, pairing with its integral vectors, and then using (2).
They do not assert that the projection of an arbitrary vector of
\(\Lambda_c\) to \(W\) is integral.

The moves are the rational isometries congruent to one modulo \(M\)
in \(\Lambda_c\) and fixing every vector of \(F\). We count sets of
terms whose frames are distinct modulo these moves.

For a term set
\[
 L_\gamma=\{v\in\Lambda_{W,c}:
       v+Mw\perp Q_\gamma\text{ for some }w\in\widehat{\mathcal O}_E^\rho
                  \text{ in }A\}.
 \tag{3}
\]
Suppose \(L\subset\Lambda_{W,c}\) has rank \(r=k-\ell\) and
\[
 d(L)\le H=b^{n^3f},\qquad L\subset L_\gamma .
 \tag{4}
\]
Here \(d\) is exactly the normalized discriminant in the lattice
chapter, so the Gram discriminant quotient has order \(d(L)^2\).

A cell index \(j\in\{0,\ldots,n\}\) means the following two properties.
The matrix \(Y\) formed from the first \(j\) rows of \(Z_\gamma\) and
the remaining rows of \(I_n\) has determinant
\(\delta\ne0\); and every column of \(Q_\gamma Y^{-1}\) with index
at least \(j\) lies in the span of \(F\). Indices for this condition
are \(0,\ldots,n-1\). These are precisely the properties of the
source cell index needed here. For such an index define the shared
matrix \(S_\gamma\) by taking the \(A\)-coordinates of
\(Q_\gamma\operatorname{adj}Y\) in columns at least \(j\), and zero
in the other columns. Both \(Z_\gamma\) and \(S_\gamma\) are unchanged
by moves.

Here is the passage from the actual cell definition to these
properties. The determinant of the padded \(Y\) is the nonzero
leading minor \(D_j\). If \(j\le\rho\), the source's norm-one
flag-pair condition supplies, for each \(a\ge j\), vectors
\(Fx_a=Q_\gamma y_a\), with \((y_a)_a=1\) and all later coordinates
zero. Pairing with the first \(j\) vectors of \(F\) shows that
the first \(j\) coordinates of \(Z_\gamma y_a\) vanish, since
these vectors are in the radical of the form on the span of \(F\).
The vectors \(Yy_a\) are therefore a triangular basis of
\(\operatorname{span}(e_j,\ldots,e_{n-1})\). It follows that
every tail column of \(Q_\gamma Y^{-1}\) lies in the span of \(F\).
For \(j=n\), there are no tail columns. This proves the precise
cell property used here directly from the flag condition.

**Frame-fibre theorem.** Under the actual admissible conditions
\[
 b\ge1000,\quad 10^5+1\le n\le b,\quad N\ge5,\quad
 N\le b^{60n},\quad M\le b^{23},
 \tag{5}
\]
the number of near terms, separated modulo moves, satisfying (4)
and possessing a cell index is at most
\[
                         b^{2000n^6(\ell+1)f}.             \tag{6}
\]
The near condition is the boxed-point condition described and
quantified in §1. The proof of (6) is completed in §§2–5.

## 1. The two small matrices

At every infinite place use the normalized real basis with Gram
matrix of operator norm one. Let \(c_i\) be the reciprocal of the
source's basis-scale factor at the \(i\)-th frame vector. Then
\[
 |c_i|\le\sqrt N,\qquad |c_i/c_l|\le b^{23\rho}.
 \tag{7}
\]
Thus these reciprocals are
\(\sqrt N/\kappa_v^{\,\rho-i}\), up to a unit phase, with
\(1\le|\kappa_v|\le b^{23}\). A near term has a point \(y\) such
that both \(y\) and \(\gamma^{-1}y\) have normalized frame vectors
of norm at most \(b^{37n}\). Moreover the Bessel length of \(y\)
is at most \(b^{7n}\). These are the explicit boxed-point bounds:
the reduced Gram–Schmidt coefficients give the frame bound, and
the cutoff length \(b^{6n+2}\) is at most \(b^{7n}\).
Their elementary reduction is given in
[quantitative returns](lsernau-quantitative-returns.md), §5.

Pair the frame at these two points, and use (7). Cauchy–Schwarz gives
\[
                 |\sigma(Z_{\gamma,il})|\le b^{134n}.
 \tag{8}
\]
Indeed the bound is \(N b^{74n}\). Every entry is an algebraic
integer. The number of possible \(Z_\gamma\) is therefore at most
\[
                            b^{270n^3f}.                 \tag{9}
\]
To justify this count without a discriminant factor, distinct
algebraic-integer tuples have maximum conjugate distance at least
one: otherwise the norm of a nonzero differing entry would be a
positive integer below one. Pack disjoint balls of radius \(1/2\)
for the maximum of the complex absolute values. In \(d\) complex
coordinates at \(f\) places the count in radius \(B\) is at most
\((1+2B)^{2df}\). Apply this with \(d=n^2\) and
\(1+2b^{134n}\le b^{135n}\).

Here is the corresponding bound for the shared matrix, including
the condition-number estimate. Let \(F_y\) be the normalized frame
at \(y\). By the definition of Bessel length, there is a Bessel
unipotent \(u\) with \(\|uy\|\le b^{7n}\); the compact definite
factor may be removed without changing the norm. Its action on the
frame is an upper unitriangular \(n\)-square matrix \(T\). Thus
\[
 |T_{il}|\le b^{44n},\qquad
 |\operatorname{adj}(T)_{il}|
       \le b^{(2+44n)\rho}.
 \tag{10}
\]
The adjugate bound follows by expanding a minor into at most
\(\rho!\le\rho^\rho\le b^{2\rho}\) products. Since \(\det T=1\),
Cramer's rule shows, for any coefficients \(v\),
\[
              |v_i|\le b^{46n^2}\|F_yv\|.
 \tag{11}
\]
The exponent before weakening is
\(1+(2+44n)\rho+7n\le46n^2\).

For a shared column write \(Q_\gamma\operatorname{adj}(Y)e_l=Fw\).
Every entry of \(\operatorname{adj}(Y)\) has modulus at most
\(b^{(2+134n)\rho}\), by (8). Apply \(y^{-1}\) to this equality in
the normalized basis. The left side is a combination of the boxed
frame at \(\gamma^{-1}y\); the right is a combination of \(F_y\)
with coefficients \(c_iw_i\). The left coefficients are
\(c_l\operatorname{adj}(Y)_{l a}\). Apply (11) to bound
\(|c_iw_i|\), and then use \(|c_l/c_i|\le b^{23\rho}\).
Equations (7), (11), and the triangle
inequality imply
\[
 |w_i|\le
 b^{46n^2+(2+134n)\rho+1+23\rho+37n}
                         \le b^{182n^2}.
 \tag{12}
\]
The entries of \(S_\gamma\) are integral because those of
\(a_\gamma\) and \(\operatorname{adj}Y\) are integral. The same
packing argument, now in \(\rho n\) entries, bounds its possibilities by
\[
                           b^{366n^4f}.                  \tag{13}
\]

Finally the determinant expansion in (8) gives
\[
 |\sigma(\delta)|^2\le b^{270n^2}.
 \tag{14}
\]
Write \([a]=|N_{E/\mathbb Q}(a)|\) for an integral nonzero \(a\).
For the two moduli
\[
                 d=M\delta,\qquad d'=M\delta\bar\delta
\]
we obtain from (5), (14), and \(n\ge10^5\)
\[
                    [d],[d']\le b^{2n^3f}.               \tag{15}
\]
The precise exponents to absorb are respectively
\((46+270n^2)f\) and \((46+540n^2)f\).

## 2. The integral moves

An algebraic integer \(\tau\) with \(\tau+\bar\tau=1\) exists:
take minus a primitive third root of unity. Let \(X\) be the matrix
whose columns are the standard vectors of \(A\). For any rational
matrix \(\eta\) with \(\rho\) columns in \(\Lambda_{W,c}\), embed
it in \(V\) as \(v\). The matrix
\[
 u_\eta=I+M(Xv^*J-vX^*J)
                 -M^2\tau X(v^*Jv)X^*J                  \tag{16}
\]
preserves \(J\), fixes \(F\), and is congruent to one modulo \(M\)
in \(\Lambda_c\). These assertions follow by multiplication:
\(X^*JX=X^*Jv=0\), and the remaining quadratic terms cancel by
\(\tau+\bar\tau=1\). Integrality follows from the integral pairing
on \(\Lambda_c\). It is upper unipotent in the decomposition (1).
Its effect on a frame is
\[
                   x_{u_\eta\gamma}=x_\gamma-M\eta p_\gamma .
 \tag{17}
\]
For any integral skew-Hermitian \(\rho\)-square matrix \(B\), there
is also the move
\[
                   u_B=I+MXBX^*J,                       \tag{18}
\]
which adds \(MBp_\gamma\) to the \(A\)-block of the frame and fixes
the other blocks.

These explicit formulas prove the required integral moves; they
are not just rational transitivity statements. No division by two
has been introduced at the dyadic places.

## 3. The first quotient: lifting the lattice

Fix \(j,Z\), and choose a rational basis matrix \(y:E^r\to W\)
for the span of \(L\). Write its finite local bases as \(m=ya\),
where \(a\in GL_r(\mathbb A_{E,f})\). From (3), every frame admits
a rational matrix \(w_\gamma:E^r\to E^\rho\) with
\[
 w_\gamma a\text{ integral},\qquad
                x_\gamma^*y+Mp^*w_\gamma=0.              \tag{19}
\]
Here rationality is legitimate even when \(L\) is not globally
free. First solve this rational linear system over the finite
adeles using (3). Gaussian elimination shows its rational affine
solution space is nonempty; rational points in its kernel are
dense in the finite adelic kernel by additive approximation
(equivalently, the Chinese remainder theorem). The condition
\(wa\) integral is open, so a rational solution satisfying it exists.

Colour each row of \(w_\gamma a\) modulo the lattice of rows of
\(m^*m\). This quotient has order \(d(L)^2\): its determinant
index is the norm of the Hermitian Gram determinant, precisely the
square of the normalized discriminant. There are therefore at most
\[
                              d(L)^{2\rho}                \tag{20}
\]
colours. If \(w'-w\) has zero colour, put
\[
                  \eta=y(y^*y)^{-1}(w'-w)^*.
 \tag{21}
\]
Then \(\eta^*y=w'-w\). The colour condition says locally that
\(\eta\) is an integral combination of columns of \(m\), so its
columns belong to \(L\), hence to \(\Lambda_{W,c}\). Formula (17)
then replaces the right side of (19) by the one for the fixed lift
\(w'\). After these moves, all \(x_\gamma^*y\) in one colour are
equal.

## 4. The second quotient: the corank complement

Fix one first colour and make these moves. Let \(x_0\) be one of
the resulting \(W\)-parts, and put
\[
                P_L=\Lambda_{W,c}\cap(\operatorname{span}_E L)^\perp .
 \tag{22}
\]
This is a projective lattice of rank \(\ell\). All columns of
\(x_\gamma-x_0\) lie in \(P_L\), by (19) and the finite integrality
observation following (2). Colour their \(n\) columns modulo
\(dP_L\), \(d=M\delta\). The number of colours is exactly
\[
                                [d]^{\ell n}.             \tag{23}
\]
Multiplication by \(d\) on a rank-\(\ell\) projective lattice has
this index; local free bases prove it without a global basis.

Suppose \(v=x_\gamma-x_{\gamma'}\) has zero colour. Then
\[
 vY^{-1}=M\eta',\qquad
                \eta'=(M\delta)^{-1}v\operatorname{adj}Y
 \tag{24}
\]
has columns in \(\Lambda_{W,c}\). All columns of \(vY^{-1}\) of
index at least \(j\) are zero by the shared-frame property. If
\(j=n\), its last column is also zero, for the following reason.
For \(q=Q_\gamma Z^{-1}e_{n-1}\), equations (1)–(2) give
\[
 q_{A^*}=0,\qquad q_z=-N^{-1},\qquad
 \|q_W\|^2=N^{-1}-N\,|(Z^{-1})_{n-1,n-1}|^2\le N^{-1}
 \tag{25}
\]
at every infinite embedding. The same holds for \(\gamma'\);
the squared norm of their \(W\)-difference is at most \(4/N<1\).
This difference is an integral vector of \(\Lambda_{W,c}\) by
(24). Its Hermitian norm is an algebraic integer with every
conjugate below one in absolute value, and hence is zero. Positivity
forces the vector to vanish.

Thus the last column of \(\eta'\), and all its columns of index
at least \(j\), vanish. Multiplying (24) by \(Y\) gives
\[
                             v=M\eta p                    \tag{26}
\]
using only the first \(\rho\) columns of \(\eta'\).
The move (16) removes this difference. Within each second colour
we may therefore make the whole \(W\)-part identical.

The strict inequality in (25) is why the actual condition \(N\ge5\)
is retained. Rational congruence alone would not suffice to remove
the last column.

## 5. The third quotient: the isotropic part

Once \(Z\) and \(x_\gamma\) agree, two frames differ only in their
\(A\)-blocks, by (2). First colour by the shared matrix; (13) bounds
this cost. Its value is unchanged by all the preceding moves.
Then colour the \(\rho n\) integral entries of \(a_\gamma\) modulo
\(d'=M\delta\bar\delta\). This costs
\[
                                [d']^{\rho n}.             \tag{27}
\]
We prove that one such colour contains at most one frame modulo
moves.

Let \(a_{\gamma'}-a_\gamma=d'X_0\) with \(X_0\) integral.
Equality of the frame Gram matrices gives
\[
                           X_0^*p=-p^*X_0.                \tag{28}
\]
Let \(\alpha\) be the first \(\rho\) columns of
\(\operatorname{adj}Y\). Equality of shared matrices shows
that all columns of \(X_0\operatorname{adj}Y\) of index at least
\(j\) vanish. When \(j=n\), its last column vanishes as well:
for \(v=\operatorname{adj}(Z)e_{n-1}\), one has \(pv=0\);
(28) gives \(p^*X_0v=0\); and \(p^*\) is injective since the
first \(\rho\) rows of the invertible \(Z\) are independent.
Therefore in all cases
\[
                             X_0\alpha p=\delta X_0.      \tag{29}
\]
The integral matrix
\[
 B=\bar\delta X_0\alpha-\delta(X_0\alpha)^*
                         -\alpha^*p^*X_0\alpha             \tag{30}
\]
satisfies \(B^*=-B\), by (28), and
\[
                                Bp=\delta\bar\delta X_0.
 \tag{31}
\]
For (31), the first term gives the claimed answer by (29);
the second and third cancel using (28) and (29).
The move (18) consequently adds exactly \(d'X_0\) to the
\(A\)-block and identifies the two frames. This proves the claim.

Combining the three quotients, for fixed \(j,Z\), the count is at most
\[
          d(L)^{2\rho}[M\delta]^{\ell n}
                      b^{366n^4f}[M\delta\bar\delta]^{\rho n}.
 \tag{32}
\]
Use (4), (15), and then count \(Z\) by (9). There are \(n+1\le b^{2f}\)
cell indices. The resulting exponent of \(b\), divided by \(f\), is
\[
 2+270n^3+366n^4+2n^3(\rho+\ell n+n\rho)
       =2+268n^3+366n^4+2n^5+2\ell n^4
       \le2000n^6(\ell+1).
 \tag{33}
\]
This proves (6), including rank-zero and full-rank \(L\). Empty
matrices and rank-zero quotients have determinant and index one.

## 6. Labels and the weighted pair count

The pair family here is the actual family whose members satisfy
the source's *IsNearTermAt*: it includes a cell index as part of
its definition. We are not asserting that every arbitrary near
term has such an index. Reducing an unrestricted moment to this
family by the character-compatibility and zero-term arguments is
a separate obligation.

For the actual near representatives, fixing the source label
makes their frames separated modulo moves. Here is the finite
reason. Equal frames put their reductions in the same coset of
the reduced Bessel group \(R\) in the reduction group \(G_{\rm red}\).
Choose a section \(\sigma:G_{\rm red}/R\to G_{\rm red}\) and define
the label of \(s\) as \(\sigma(sR)^{-1}s\in R\).
Equal cosets and equal labels force the reductions to agree.
This explains why the number of labels is \(|R|\), rather than
\(|G_{\rm red}|\). Their rational quotient now
fixes the standard frame and has principal-level reduction.
Its Levi component identifies the two definite target classes,
so those classes agree. It is then a rational stabilizer of the
free definite level and is the identity. The remaining quotient
is the frame-fixing congruence unipotent. Double-coset
representatives are consequently equal. This is the same block
argument proved in the quantitative-return chapter, §5, now with
the label used to recover equality of the reductions.

Attach to each ordered near pair its common label and its
intersection lattice \(L\). For a fixed \(L\) of corank
\(\ell\le n^3\), (6) bounds each component, hence the fibre by
\(b^{4000n^6(\ell+1)f}\). The actual admissibility inequality
\[
                  k\ge1000(2n)^9=512000n^9
\]
implies
\[
 b^{4000n^6(\ell+1)f}
      \le b^{8000n^9f}\le b^{kf/4}=\tau .
 \tag{34}
\]
Combining (34) with Corollary 2 of the weighted lattice chapter
therefore proves
\[
 \boxed{\displaystyle
 \sum_{\substack{\text{near pairs of corank }\ell\\d(L)\le H}}
                 d(L)^{-k}
       \le \tau^{\ell+2}\,
             \frac{|\mathcal C|\,|\operatorname{red}(S_{\rm Bessel})|}
                  {N^{kf}} .}
 \tag{35}
\]
There is one class factor and one label factor. There is no
additional factor for the target class: it was included in the
separated frame family and removed by the free-level argument.

Thus the entire weighted near-pair **count** is supplied in
ordinary mathematics. Equation (35) does not by itself establish
the gauge-dependent orbit integral or the link-discriminant gain
needed by the analytic moment reduction.

## 7. Source and verification ledger

All source references are to the immutable readable revision
[72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src),
attributed to Levent Alpöge's announced work.

| Source | Interface independently proved above |
|---|---|
| New/Spanning/RemainingTerms/FramesOverLattice.lean, 128–217, 275–606 | Counts of products/shared vectors; the three quotient factors; near representative specialization |
| New/Spanning/RemainingTerms/FrameParts.lean, 229–295, 356–626, 640–706 | Integral moves; rational lifts; discriminant quotient; corank complement; modulus norms |
| New/Spanning/RemainingTerms/FrameCount.lean, 60–155, 196–238, 394–444, 470–505, 679–737 | The short final column; class separation; condition number; shared-vector bound; skew solution |
| New/Spanning/Unfolding/ReducedPoints.lean, 134–205 | The integral Eichler formula, here using only a third root of unity |
| New/Spanning/Unfolding/Terms.lean, 541–581 | Frame-product and leading-minor bounds |
| New/Spanning/RemainingTerms/Count.lean, 137–211 | Fibre squaring and weighted pair count |

The [checker](../scripts/check_corank_frame_fibres.py) and
[certificate](../certificates/corank-frame-fibres.json) record six pinned
source blobs, 36 exact Eichler/central-move cases, 18 skew-solution cases
including every cell for isotropic ranks one through four, and six
universal exponent certificates. These checks support the algebraic
formulas and normalizations; the finite computations are not the proof
of (6) or (35).
