# The one-lift comparison and its signed ratio

This chapter reconstructs the finite linear-algebra and height parts of
the comparison for the actual descent pair at step \(j\).
The upper chain has separate proved [finite transport](lsernau-common-chain-transport.md)
and [norm bounds](lsernau-common-chain-norm-budget.md). The general
product-form gluing operator below still requires its stated first-factor,
integral product-form and analytic pairing inputs. The
[six-copy test](lsernau-six-copy-test-transport.md) and
[rank-one false-lift periods](lsernau-rank-one-false-lift-periods.md)
supply the sharp critical comparison; they do not supply the general
higher-rank gluing periods. Products spanning and the numerical
congruence budget also remain inputs. A short Selmer group alone does
not bound an arbitrary projection denominator.

## 1. Integral frames in the actual coefficient representation

At one complex place let \(b_i\) be the standard basis of minor
products in the polynomial representation dual to the Weyl module
of the source diagram. The coordinate vector in the Weyl module
is a functional on these \(b_i\). Use the column-filling matrix
\(A\): the row indexed by a filling gives the expansion of its
minor product in the \(b_i\). Its entries are integers by
integral straightening of minors. Its rows include the standard
basis rows, so it has full column rank and the coordinate embedding
into the tensor of exterior powers is saturated. The target metric
in these coordinates is
\[
 G=A^T A .
\]
Indeed the standard wedge tensors form an orthonormal basis,
and Cauchy--Binet gives the coefficient of
\(\prod_h\det(x_h^Ty_h)^{\kappa(h)}\) as this matrix.
Use the product of these constructions at all complex places,
equivalently the tensor product of the matrices. This is
the precise rational Gram matrix in the source, not an arbitrary
integral change of metric.

For the same basis put
\(F_{ij}=b_i(\partial)b_j(0)\). It is integral and real
symmetric positive definite: on monomials the Fock metric
is diagonal with entries the multi-index factorials.
Both \(G\) and \(F^{-1}\) are invariant Hermitian forms on
the same dual representation of the product of compact unitary
groups. For \(G\), this follows from its exterior-tensor
realization; for \(F^{-1}\), from invariance of the Fock
metric under unitary substitution, which follows from the
Gaussian integral for the monomial metric (or the chain rule
for the Fock pairing). The Weyl representation is the
irreducible highest-weight representation with the prescribed
diagram. Schur's lemma gives \(GF=hI\).
To determine the scalar, evaluate at the highest array,
so that the coordinate functional \(v_0\) has tensor image
\(Av_0\) the tensor of the first \(h'\) basis vectors in
each column of height \(h'\). Hence \(v_0^*Gv_0=1\).
The polynomial with coefficients \(Gv_0\) is the product
\(b_{\rm top}\) of the leading minors, by the kernel identity
above. Its Fock norm is therefore \(h\); this is exactly the
source integer \(\mathrm{hookNumber}\). In particular \(h>0\).
We use the source definition of that integer as a Fock norm;
no alternative convention for a hook product is needed.

Now the columns \(f_a=FA^Te_a=hG^{-1}A^Te_a\) are integral
coordinate vectors. They are the orthogonal projections of
the unit tensor vectors, multiplied by \(h\). Thus
\[
 \sum_a f_af_a^*G=h^2 I,\qquad \|f_a\|_G^2\le h^2.           \tag{1}
\]
This gives a short construction of the precise frame, including
its denominator, rather than a generic inverse-Gram estimate.
The only representation-theoretic inputs here are the classical
minor-product straightening and highest-weight realization used
to identify the source basis; the frame calculation uses
integral matrices and the invariant metrics.

At the chosen level the source's space of second-factor tuples
is the direct sum, with this metric, over pairs consisting of
a gluing choice and a definite class representative. Take the
frame (1) in each summand separately. One may move a class
representative to an integral one at the places above \(\ell\):
the rational unitary group is dense in the product of its
local groups at a finite set of places. Here is the needed
elementary weak-approximation proof. The Cayley transform
\(A\mapsto(1-A)(1+A)^{-1}\) identifies an open dense subset of
the vector space of skew-Hermitian matrices with the unitary
elements for which \(1+g\) is invertible. In each local group
the latter subset is dense: multiply by arbitrarily small
norm-one scalar perturbations avoiding the finitely many
forbidden eigenvalues. Weak approximation on the vector
space over the totally real ground field then gives a
single rational approximation at all these places. The
condition of moving the representative into the chosen
integral open compact subgroup is open, so it can be
achieved.

Move the coordinate frame by the inverse of the appropriate
rational unitary weight action, with complex conjugation on
the two sides as in [2]. All its conjugates remain isometries:
the matrix entries of a rational unitary element are algebraic
CM entries, and any embedding of that CM field commutes with
its CM involution. Thus (1) is unchanged, the moved frame
has squared norms at most \(h^2\) after every complex
automorphism, and its prescribed transported coordinates
are integral. The frame can depend on \(\ell\), but the
operator it represents below does not.

## 2. The actual gluing operator and the determinant identity

Use the notation of the finite theta chapter. For a fixed \(j\)
write \(W\) for the good forms on \(W_j\), of dimension \(d\),
\(V_\xi\) for the target forms of the descent pair at twist
\(\xi\), and \(L_\xi=\mathrm{goodLift}(\xi,j)\).
Let \(T\) be the fixed space of second-factor tuples described
above. In the source the actual gluing map \(G_\xi:T\to V_\xi\)
is the finite class sum of product forms
\[
 G_\xi u=M^{l_1}\sum_{i,c,h}
 \mathrm{productForm}_{i,\xi}\big((h,c),\,
                   \mathrm{firstFactor}_{i,\xi}(h),\,u_{i,c}\big).
                                                               \tag{2}
\]
Here \(i\) is a matrix/row choice at the source gluing level,
\(c\) a second-factor class at level \(J(\pi_M^2)\),
and \(h\) a first-factor class at \(J_{\Lambda(i)}\).
The product form is supported on the class of the block point
times the specified divided-lattice point, with the Cartan
product value; \(l_1\) is the denominator exponent of that
divided splitting. These are exactly the data in
\(\mathrm{GluingMaps}\), not freely chosen product forms.
The levels of the first-factor sums are free, as in the source.
The pairing of a product form with an arbitrary form is evaluation
at its supporting class paired with its specified value, with
the normalization of the product form included. Inserting this
in the finite sum proves the adjoint slice formula: the pairing
with \(G_\xi^*v\) is \(M^{l_1}\) times the sum of the Cartan
product values paired with \(v((h,c)g_{i,\xi})\).
This identifies precisely the finite quantity to unfold.

The finite gluing estimates themselves admit the following
more direct uniform calculation. At a coefficient embedding
away from the twist, suppose the divided-splitting gauge
estimate of the source holds: the Cartan product value
of a product form costs at most \(|M|_\ell^{-l_1}\) times
the product of the two transported gauges. Suppose the
first factor has gauge at most one and the tuple is
integral. The multiplier \(M^{l_1}\) in (2) cancels this
cost exactly. The integral character on the supporting
class takes unit values and every first-factor stabilizer
is trivial. Thus every term of the scaled sum has gauge
at most one; ultrametricity proves the gluing-integrality
assertion, with no factor for the number of classes.
It suffices to prove the divided-splitting and first-factor
estimates, not a further uniform integral theorem on the
completed gluing map.

For the untwisted archimedean estimate put
\(A=fmb(\log b)^2\). Let \(I\) index the pairs \((i,c)\),
\(H_i\) be the number of first-factor classes for \(i\),
and \(H_V\) the number of target classes.
Use the pointwise first-factor estimate
\(\|\sigma\mathrm{firstFactor}\|^2\le e^A\),
and the source's pointwise product-form bound:
its norm is at most \(g_0\) times the product of
the norms of the first factor and \(u_{i,c}\).
Both are the actual weight norms, at every
\(\sigma\). The latter is the exact Cartan norm
on the two disjoint blocks followed by the
class-support bound. For a target class \(x\),
triangle inequality followed by Cauchy--Schwarz,
*on the tuple index*, gives
\[
 \|(\sigma G_1)(\sigma u)(x)\|
 \le M^{l_1}g_0e^{A/2}
       \sum_{(i,c)\in I}H_i\|\sigma u_{i,c}\|
 \le M^{l_1}g_0e^{A/2}
       \Big(\sum_{(i,c)\in I}H_i^2\Big)^{1/2}
       \|\sigma u\|.
\]
Summing the squares with class weights at most one proves
\[
 \|\sigma G_1\|_{\rm op}^2
 \le M^{2l_1}g_0^2 H_V e^A
                     \sum_{(i,c)\in I}H_i^2.              \tag{2a}
\]
Here the domain is the direct sum tuple metric, and
the target metric is the class sum of the rational
Weyl Gram forms. Compared with bounding each tuple
entry by the whole tuple norm before summing, this
saves a factor \(|I|\) when the \(H_i\) are equal,
and at least that factor in the corresponding
worst-case bound. The source class bounds are
\(H_i,H_V\le e^b\), so it suffices that
\(2l_1\log M+2\log g_0+3b+\log|I|\le A\)
to recover \(\|\sigma G_1\|\le e^A\).

There is also no need to count frame vectors to estimate
\(U_1\) at infinity. Work in the ambient finite value
coordinates at target classes and the full space of tuples.
Both metrics have rational Gram matrices, using the
class weights on the target. Thus for \(c\) complex
conjugation and \(\sigma^c=c\sigma c\),
\[
 \sigma(G_1^*)=(\sigma^c G_1)^*,\qquad
 \|\sigma U_1\|_{\rm op}
 \le g_0h^2\|\sigma G_1\|_{\rm op}\|\sigma^c G_1\|_{\rm op}.
                                                               \tag{2b}
\]
For the adjoint formula on target forms, restrict
the ambient adjoint to that form subspace; the tuple
space is the full finite direct sum. The identity follows
by transposing the value matrix and inserting the two
rational metric matrices. It does not assume that
\(\sigma\) commutes with \(c\).
If (2a) gives the source bound \(\|\sigma G_1\|\le e^A\),
then \(2A+\log g_0+2\log h\) is a valid value of \(A_j\)
in Section 4. The source's \(3A\) follows whenever
\(\log g_0+2\log h\le A\). This separates the
analytic first-factor input from the finite operator
estimates and preserves the small hook and class
losses without counting the tight frame. The full
source estimates for the first factor, the local
divided splitting, and the class and scale bounds
are still required.

The analytic suppliers for (2) are now the first-factor,
product-form and divided-splitting estimates used above,
the numerical class bounds, and the first-factor period identity. After the latter and the common kernel identity,
the source has a map \(P^\circ:W\to T\) such that
\[
 c_\xi G_\xi^*L_\xi=P^\circ                                \tag{3}
\]
with one twist-independent \(P^\circ\) (its definition is
the untwisted period). The products-spanning statement
implies \(P^\circ\) injective: a vector in its kernel
pairs to zero with every choice and every second-factor
test, so is orthogonal to the spanning products.
If \(d>0\), (3) itself then implies \(c_\xi\ne0\) and
\(L_\xi\) injective; these are not independent
nonvanishing assumptions once (3) and spanning are proved.

Let \(g_0=\mathrm{chosenGroupOrder}\), the integer clearing
all the definite class stabilizers. Form the actual operator
\(U_\xi=g_0h^2G_\xi G_\xi^*\).
By (1),
\[
 U_\xi v=\sum_a g_0\langle G_\xi f_a,v\rangle\,G_\xi f_a,    \tag{4}
\]
with the inner product linear in the second argument.
If the actual gluing-integrality estimate holds for the
transported integral frames at every embedding away from
the auxiliary level, this operator preserves the integral
lattice. In fact the coefficients in (4) are integral:
\(G_\xi f_a\) is integral also at the conjugate embedding,
\(v\) is integral at the original embedding, the rational
Weyl Gram pairing preserves integrality after transporting
both vectors, and the sole class-weight denominators divide
\(g_0\). Formula (4) then gives the assertion without
introducing the number of frame vectors in the finite-place
error. The class-weight assertion follows from the faithful
reduction of a finite stabilizer at a split odd prime,
as proved in the critical-value chapter. This argument
does not prove the gluing-integrality estimate itself.

Put \(Z_\xi=L_\xi W\), \(P_\xi=\operatorname{pr}_{Z_\xi}\),
\(C_\xi=P_\xi U_\xi|_{Z_\xi}\), and
\[
 \Delta_\xi=\det C_\xi,\qquad V_\xi^{\rm vol}
                  =\det(L_\xi^*L_\xi).
\]
The adjoint equation (3) gives
\(L_\xi^*U_\xi L_\xi=g_0h^2|c_\xi|^{-2}P^{\circ*}P^\circ\).
Choose orthonormal bases in \(W,Z_\xi\); in these bases
\(L_\xi\) is a square invertible matrix, and the determinant
on the left is \(V_\xi^{\rm vol}\Delta_\xi\).
The source's three-exchange scalar identity reads
\[
 |c_1|^2/|c_\xi|^2=\Gamma_\xi/\Gamma_1,\qquad
 \Gamma_\xi=\mathrm{heckeValueProd}(j,\xi).
\]
Once this identity and (3) hold, both determinants are
positive and the exact comparison is
\[
 \frac{V_1^{\rm vol}}{V_\xi^{\rm vol}}
   =\frac{\Delta_\xi}{\Delta_1}
                         \left(\frac{\Gamma_1}{\Gamma_\xi}\right)^d .
                                                               \tag{5}
\]
This is the squared-volume identity, with no extra factor
of 2. All statements of the uniform kernel and period
inputs here refer to the exact gluing formula (2).

## 3. Projection on true lifts, at all conjugates

Use the source's central projection \(E_0\) and a split
off-level Hecke polynomial operator \(A_w\) evaluated at
the lift root. The true lifts satisfy
\(Z_\xi\subset\operatorname{im} E_0\cap\ker A_w\).
A false lift at \(w\) lies in
\[
 F_w=\operatorname{im}E_0\cap\ker A_w\cap Z_\xi^\perp.
\]
The last orthogonality uses the original Petersson metric.
Suppose \(v\perp F_w\). We prove that the original projection
\(P_\xi v\) does not increase the squared norm at any
automorphism \(\sigma\), not just at the identity.

In this calculation the transported \(\sigma\)-metric is
defined on the actual finite value coordinates with the
rational Gram matrix, as in the source. The spherical
double coset adjoint formula holds in this metric. One
way to see the formula is to use the finite correspondence
of pairs of classes linked by the double coset:
reversing a pair replaces the double coset by its inverse,
and the class-stabilizer weights count the same correspondence.
Each rational transition action on a weight fiber preserves
its transported metric by the CM unitary identity. Level
characters are roots of unity and remain unitary after
\(\sigma\). Thus reversing the correspondence and conjugating
the coefficients *after* \(\sigma\) gives the adjoint.
The spherical algebra is commutative, so \(A_w\) commutes
with this adjoint, and is normal in every \(\sigma\)-metric.
Likewise the central type projector stays an orthogonal
projector: after coefficient conjugation it projects
onto the conjugate character types. These adjoint
statements require the actual spherical unramified level
and finite group action, not a general Hecke operator
at an arbitrary level.

For the original metric,
\((\ker E_0+\operatorname{im}A_w)^\perp
=\operatorname{im}E_0\cap\ker A_w\).
Consequently
\(v=P_\xi v+x\) for some \(x\in\ker E_0+\operatorname{im}A_w\);
this sum is orthogonal to \(Z_\xi\) in the original metric.
In every transported metric the same algebraic kernel and
image relation gives the corresponding orthogonality,
since \(E_0\) stays self-adjoint and \(A_w\) normal.
Pythagoras proves
\[
 \|P_\xi v\|_\sigma^2\le\|v\|_\sigma^2 .                   \tag{6}
\]
The source must still establish that (4) sends true lifts
into the vectors orthogonal to every false-lift space.
It does this through vanishing of the actual periods.
Without this condition, (6) cannot be invoked merely
because \(P_\xi\) is orthogonal for the original metric.

## 4. Projection denominators: exact lattice cost and simultaneous separator

At an embedding over \(\ell\), an integral form on the definite
target can be tested at finitely many class representatives
integral above \(\ell\), by the weak approximation argument
of Section 1. At these points its transported coordinates
are integral in the prescribed Weyl lattice. Values elsewhere
are determined by rational and level equivariance; rational
transport is accounted for by the gauge and the level
weight acts integrally. In particular every nonzero form
can be scaled to an integral form having at least one
unit coordinate. This assertion is valid over
\(\overline{\mathbf Q}_\ell\), since there are finitely
many coordinates and the scaling can have the exact
valuation of the largest one.

Here is a useful exact interpretation when all spaces
are written over a finite coefficient field. Let
\(\mathcal O\) be its DVR, \(L\) the integral lattice,
and \(Z\) the true-lift subspace. Assume the test
subspace \(T_{\rm test}\) contains \(Z\).
Set \(L_Z=L\cap Z\), \(N=P_Z(L\cap T_{\rm test})\).
If \(P_Z\) is defined over this coefficient field,
\(N,L_Z\) are lattices of the same rank, with \(L_Z\subset N\).
If also a prescribed pairing condition requires output
in a smaller full lattice \(L_Z'\subset L_Z\),
the least valuation of the determinant of a clearing
map \(N\to L_Z'\) is exactly
\[
 \operatorname{len}(N/L_Z)+\operatorname{len}(L_Z/L_Z'),
                                                               \tag{7}
\]
where lengths are normalized by the ramification degree.
Indeed relative to bases of the two lattices the
matrix must be integral; choosing an isomorphism
between their bases attains equality. The difference
of their determinant valuations is the stated length.
This equality concerns arbitrary clearing endomorphisms,
not necessarily diagonal ones; nor does it assert
the existence of a uniform bound for this length.

The source actually supplies diagonal clearing maps through
the first-order Selmer argument. The exact input for each
basis element \(z_i\) of \(Z_\xi\) is a map \(T_i\) on \(Z_\xi\)
diagonal on a common basis of lift generators (chosen in
the relevant Hecke eigenspaces), which takes the projections
of all integral test forms into integral forms, and whose
eigenvalue at \(z_i\) has valuation at most
\[
 b_i=\mathrm{sel}_i+2t'\mathrm{ram}+r'\mathrm{loc}
                                     +\mathrm{err}.           \tag{8}
\]
Here \(r'\) is the rank of the smaller Hermitian space,
\(t'\) the rank difference, and \(\mathrm{loc},\mathrm{err}\)
are precisely the local defect and denominator error
of the source (not a Selmer dimension).
The \(g_0^2\) type/projection and diagonal-operator
clearing multiplier is already included in (8).
The existence of the individual maps with this bound
is the substantive first-order congruence theorem.

The simultaneous separator now has a simple proof.
Write the \(i\)-th diagonal entries of all the maps \(T_a\)
as \(\lambda_{ai}\), and choose a nonzero entry of smallest
valuation in each column. Divide that column by this
entry. It has integral entries and at least one nonzero
reduction. Over the infinite algebraic residue field choose
a tuple of coefficients avoiding the finitely many
hyperplanes defined by the reduced columns. Lift to
integral coefficients and form their linear combination
\(\Lambda\) of the \(T_a\). It still clears all projected
integral test forms, and its \(i\)-th eigenvalue has valuation
exactly \(\min_a v_\ell(\lambda_{ai})\le b_i\).
In particular
\[
 v_\ell(\det\Lambda)\le\sum_i b_i .                         \tag{9}
\]
A sufficiently large finite residue-field extension also
suffices. This proves the sharper sum-of-individual-defects
version of the source's worst-case bound. It does not
add an extra ramification error for passing to a common
separator. If the mixed pairing with every all-embedding
integral form is required, multiply once by \(g_0\):
the class weights are cleared and the test form is
integral at the conjugate embedding. The determinant
cost then increases by \(d\,v_\ell(g_0)\).

Apply this to (4) on the common analytic datum, assuming its
higher-rank false-lift orthogonality. The separate rank-one period
proof supplies the sharp critical test, not this general implication.
Together with the stated integral product-form gluing inputs, that
hypothesis makes \(\Lambda C_\xi\) preserve
the integral true lifts. Scale an eigenvector to primitive
integral coordinates as above: its eigenvalue is integral
because its image is integral and one coordinate is a unit.
Taking the product of eigenvalues, without requiring
semisimplicity of \(\Lambda C_\xi\), yields
\[
 \log|\iota(\Delta_\xi)|
       \le (\log\ell)\sum_i b_i.                           \tag{10}
\]
The additional factor for mixed pairings may be included
if that stronger denominator condition is used.
If the source's untwisted operator-norm estimate
\(\|U_1 v\|_\sigma\le e^{A_j}\|v\|_\sigma\) holds, (6)
applied to eigenvectors of \(C_1\) yields
\(\log|\sigma(\Delta_1)|\le d A_j\).
Here \(A_j=3fmb(\log b)^2\) in the source.
Thus the multiplier \(\Delta_1\) in (5) gives a
height bound for its first factor of
\[
 dA_j+\sum_\ell(\log\ell)\sum_i b_{i,\ell},                 \tag{11}
\]
provided the individual bounds are uniform over embeddings
and summable. This uses (10) only at the selected twists.

## 5. The indispensable negative main term

Use the source notion of a bound \(\operatorname{HeightLe}(c)\)
for a family over coefficient embeddings: one nonzero common
multiplier has conjugate log bound \(\alpha\); the products
with the family have local log bounds \(h_\ell\log\ell\)
with \(h_\ell\ge0\); their sum with \(\alpha\) is at most
\(c\). The cost can be negative. Costs add under products,
and prime-to-\(\ell\) rational powers of the twist norm
cost zero at \(\ell\).

Write \(B=\mathrm{denominatorBudget}\),
\(J=\sum_\tau\mathrm{jetSize}(\kappa_\tau)\),
\(P=\sum_\tau\mathrm{primeSum}(\kappa_\tau,\tau)\);
the source's direction amount is \(J-P\).
For a main critical pair the desired signed bound cannot
be obtained just from the constant small-twist ratio estimate.
It uses the following three further arithmetic inputs.

* The untwisted squared norm \(s_1=\|\phi_1\|^2\) has height
  at most \(B-J\). This is the empty-row comparison of
  \(\mathrm{AlgebraicPartSize}\).
* On the rank-one lift line, two integral test forms
  \(u_\iota,u'_\iota\), orthogonal to the false lifts,
  have projected pairing of height at most \(B\).
  This is the mixed-pairing conclusion of the projection
  denominator on that line.
* There is one \(c_0\ne0\) with conjugate absolute value
  at most \(e^B\), such that these tests, selected at the
  embedding and its conjugate for the **same** twist,
  satisfy
  \[
  |\iota(\langle u,\phi_\xi\rangle
                 \langle\phi_\xi,u'\rangle)|
      \ge |\iota(c_0\bar c_0 \rho_\xi^2)|
                     \ell^{-2P_\ell},\qquad
  \sum_\ell 2P_\ell\log\ell\le P .
  \]
  Here \(\rho_\xi\) is the source empty-row auxiliary
  critical ratio for the second block of rank 4,
  and \(P_\ell=\mathrm{localPrimeSumTotal}(\ell)\).
  This is the actual sharp jet/test-form input in
  \(\mathrm{TwistedValueHeights}\), not a generic
  existence of a test vector.

For any nonzero \(\phi_\xi\) the line projection satisfies
\[
 \langle P_\xi u,P_\xi u'\rangle
   =\frac{\langle u,\phi_\xi\rangle
           \langle\phi_\xi,u'\rangle}{\|\phi_\xi\|^2}.
\]
The test estimate makes its numerator nonzero. The inverse
main critical ratio is \(s_1/\|\phi_\xi\|^2\) times
a prime-to-\(\ell\) power of the auxiliary twist norm,
by the precise critical-value norm formula. Thus, up to
that unit, factor it as
\[
 s_1\ \langle P_\xi u,P_\xi u'\rangle\
       \rho_\xi^{-2}\
       \frac{\rho_\xi^2}
       {\langle u,\phi_\xi\rangle\langle\phi_\xi,u'\rangle}.
\]
The four heights are bounded by \(B-J\), \(B\), \(10\),
and \(2B+P\), respectively; the last multiplier is
\(c_0\bar c_0\). The third bound uses the improved
[constant ratio theorem](lsernau-critical-value-systems.md)
and requires that the empty-row rank-four pair be included
in the selected common system. That pair is ramified
in the source (tame character \(\chi_M\)).
Hence the main inverse ratio has the conditional
signed height bound
\[
                  4B+10-(J-P).                            \tag{12}
\]
This improves \(6B-(J-P)\) whenever \(B>5\), and retains
exactly the necessary negative main term.
No such improvement is claimed without the three
arithmetic suppliers or the critical-value norm formula.

For \(\Gamma_\xi/\Gamma_1\) the source's three-exchange
factorization gives the square of the product of \(k/2\)
main ratios and \(5m\) other ramified ratios, times a
rational power of the twist norm. This gives the
conditional bound
\[
 \operatorname{HeightLe}\big(50m+k(4B+10-(J-P))\big)
                  \text{ for }\Gamma_1/\Gamma_\xi.        \tag{13}
\]
In (5), insert (11) plus \(d\) times (13), or use
the original source uniform denominator bound if sharper.
This is an explicit improvement to the positive errors
in the signed single-lift determinant budget, not a
completed arithmetic lower bound.

## References and remaining obligations

Readable source [72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207):

1. Lib/GLn/SchurModule/TensorModel (183--323) and GramMatrix
   (56--188, 447ff.), SchurNorm: actual minor coordinates,
   Fock pairing, integral frame and CM weight isometries.
2. [LiftVolumeHeight](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/LiftVolumeHeight.lean)
   (179--443, 625--803; blob 7773d1334443460b5c920472da37b9e4b77ddb99).
3. OneLift/ComparisonOperator/GluingMaps (330--380, 542--624,
   731--802, 999--1084;
   blob e162c6d6d22870776e550830ae808f0f04abdc4c).
4. OneLift/TestedForms (373--426, 519--635).
5. [DenominatorBound](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/DenominatorBound.lean)
   (179--187, 533--647, 1030--1113, 1156--1320;
   blob 18ef2367394d9b813ecac7cfd92e9bbcc84237ca).
6. [TwistedValueHeights](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/TwistedValueHeights.lean)
   (700--859, 860--969, 1025--1110;
   blob ddfc466fb70a096b21707df61c6a0af498151f6c);
   AlgebraicPartSize, heightLe_norm_trivialLift_sq.

Remaining: first-factor and integral product-form estimates for (2),
the compatible full analytic datum and (3), higher-rank
false-lift periods for the general gluing map, products spanning,
and the numerical local comparison, congruence and
extraction costs for each separator in (8). Their exact required
sum is isolated in the [aggregate budget](lsernau-exact-cyclotomic-loss-and-budget.md),
§4. The definite finite-chain norm, rank-two analytic endpoint and
actual rank-one false-lift period are now supplied by their separate
proofs; those closures do not prove the full signed arithmetic bound.
