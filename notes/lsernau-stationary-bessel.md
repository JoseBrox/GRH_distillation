# Stationary Bessel period: interpolation and quantitative positivity

We supply the actual stationary point and its lower period for the
normalized filling system of [Bessel majorants](lsernau-bessel-majorants.md).
We use the classical lowest-K-type matrix-coefficient formula
identified there, including its holomorphic continuation near the
identity, and ordinary finite-dimensional unitary representation
theory. The arithmetic Poincare return and Sobolev estimates are
separate; the result here is a local real supplier.

## 1. A bounded stationary frame

At one real place the large group has sign frame with a common
positive summand X and 2n remaining coordinates, with alternating
signs +,-,...,+,-. Write d=n-1. Its lowest K-type has weight zero on
X and strictly decreasing integral weights
\(\mu_0>\cdots>\mu_{2n-1}\) in \([-3B,-B]\), \(B\ge1\).
The smaller compact group has the same X and one positive
coordinate of weight \(a\ge0\). These are the source's steep
parameters in FillingData.lean and LargeFunction.lean.

Set \(L=2n,\ p(t)=\prod_i(t-\mu_i),\ q(t)=t-a\). For a real
polynomial \(F\) let
\[
 [F]_i=\frac{F(\mu_i)}{\sqrt{|p'(\mu_i)q(\mu_i)|}},
\]
extended by zero on X. The Hermitian pairing on these real
vectors satisfies
\[
 ([F],[G])_J=-\sum_i
       \frac{F(\mu_i)G(\mu_i)}{p'(\mu_i)q(\mu_i)}.
 \tag{1}
\]
Indeed the sign of \(p'(\mu_i)\) is \((-1)^i\), whereas
\(q(\mu_i)<0\). Let \(v_j=[t^j q]\) for \(0\le j\le 2d\).
For \(i+j\le2d\), (1) gives
\[
 (v_i,v_j)_J=-\mathbf1_{i+j=2d}.
 \tag{2}
\]
This is the Lagrange interpolation identity
\(\sum_i H(\mu_i)/p'(\mu_i)=[t^{L-1}]H(t)\)
for \(\deg H<L\), applied to \(H=t^{i+j}q\).
The vectors \(v_0,\ldots,v_d\) are independent: a combination
vanishing at the \(L\) distinct \(\mu_i\) is a polynomial of
degree at most \(d+1<L\) divisible by \(p\), hence zero.
In particular the first \(d\) span a totally isotropic space A,
and \(v_d\) has norm -1. This also includes \(d=0\).

The last column of the smaller space's embedding is
\(w=\sqrt{p(a)}[1]\). Here \(p(a)>0\), and partial fractions of
\(1/(p(t)(t-a))\) give
\(\sum_i 1/(p'(\mu_i)(\mu_i-a))=-1/p(a)\).
Thus \(w\) has norm 1 and is orthogonal to all \(v_j\) with
\(j\le 2d\), again by interpolation. Take \(i_0\) equal to
the identity on X and with last column w. It is an isometry.
Let M and M' denote the two diagonal lowest weights. Then
\[
 Mv_j=v_{j+1}\quad(j<d),\qquad
 Mw=aw+\sqrt{p(a)}v_0,\qquad
 i_0^\dagger M i_0=M'.
 \tag{3}
\]
Here the dagger is the Hermitian-form adjoint, not the
positive Euclidean adjoint. The last equality follows from
the preceding formula and orthogonality (also for \(d=0\)).
This is exactly the stationary frame with no approximation.

Put \(D_0=3B+a\ge1\). All the distinct integral nodes are
separated by at least 1, so \(|p'(\mu_i)|\ge1\),
\(|q(\mu_i)|\le D_0\), and \(p(a)\le D_0^L\).
For \(j\le2d\),
\[
 |(v_j)_i|\le D_0^{j+1/2}\le D_0^L,\quad
 |w_i|\le D_0^{L/2}\le D_0^L.
\]
In particular all the triangular dual vectors in (2) have
Euclidean norm at most \(M_0=\sqrt r D_0^L\), where r is
the rank of the large group.

The source shape has a standard orthonormal definite block,
hyperbolic pairs \(e_i,e_i^*\), and the last negative line z.
The fixed change from the sign frame to this shape is
Euclidean unitary. Witt extension over C gives x taking the
frame \(i_0,v_0,\ldots,v_d\), after that change of coordinates,
to the standard definite block and \(e_1,\ldots,e_d,z\).
Its Bessel length (the infimum of \(\|s x\|+1\) over
the left Bessel subgroup) is at most \(8nM_0\), as follows.
Euclidean Gram--Schmidt on \(v_0,\ldots,v_d\) uses a triangular
matrix with diagonal 1, realized by the unipotent radical
on this isotropic flag and the last line. Explicitly the
unitriangular changes of the e's extend with inverse
adjoint on their duals; adding a combination of e's to z
extends by correcting the duals by z and the e's to keep
their Gram matrix (solve the Hermitian correction by taking
half of it). The new Euclidean-orthogonal vectors \(f_j\)
have norms at most \(M_0\). Pairing \(f_j\) with \(v_{2d-j}\)
still gives -1 by (2), so each has norm at least \(M_0^{-1}\).

For \(j<d\) choose the dual \(J f_j/\|f_j\|^2\), using the
Hermitian involution J of the shape. These duals are mutually
isotropic, pair to identity with the f's, and are orthogonal
to \(f_d\) (Euclidean orthogonality). The span of the f's and
these duals is J-stable; the pair of columns for each plane
has operator norm at most \(M_0\) and the planes are
Euclidean orthogonal. On its orthogonal complement, of
signature (dim smaller space,1), \(f_d\) is a negative
unit vector of Euclidean norm at most \(M_0\).
A compact change of coordinates and one hyperbolic boost
complete it to a frame of operator norm at most \(2M_0\):
write its positive and negative lengths as \(\sinh t,\cosh t\),
then \(e^t\le 2\|f_d\|\). The resulting isometry has the
required initial flag columns. Any two completions of those
columns differ by the Bessel subgroup, which is precisely
the isometries acting unitriangularly on the flag and fixing
the last line modulo it. Taking inverses preserves the
operator norm. This proves the length bound (in fact
\(2M_0+1\) suffices after these choices).
Under the source inequalities \(3B+a\le b^2,\ 8nr\le b\),
\[
                       L_B(x)\le b^{5n}.
 \tag{4}
\]

## 2. Exact phase and localization

In the sign frame of the stationary position write
\((g,g')\) for the Bessel group element and its induced
compact isometry on the definite smaller space. The matrix
\(Y=g-1\) lowers the flag of \(v_0,\ldots,v_d\); let
\(\sigma(g)\) be the sum of its adjacent lowering coefficients.
It induces \(Y'=g'-1\) on the smaller space modulo A.
The same statements for \(Y^\dagger=g^{-1}-1\) have adjacent
sum \(-\sigma(g)\). The adjacent sum is additive under
multiplication, since products of two strictly lowering
matrices have no adjacent terms. We claim
\[
 \operatorname{tr}Y=\operatorname{tr}Y',\qquad
 \operatorname{tr}(MY)-\operatorname{tr}(M'Y')
                 =\sigma(g)-\overline{\sigma(g)}.
 \tag{5}
\]
For the first, use the filtration \(A\subset A^\perp\).
The induced action on \(A^\perp/A\) is \(Y'\) together with
zero on \(v_d\), and the traces on A and on the dual quotient
vanish by flag lowering of Y and its adjoint.
For the second choose a left inverse Z to the columns
\(v_0,\ldots,v_{d-1}\), killing \(i_0\) and \(v_d\)
(which is possible by independence). Put
\(M_1=M(v_0,\ldots,v_{d-1})Z\).
Its adjoint vanishes on A, \(v_d\), and the smaller image.
The self-adjoint remainder \(M-M_1-M_1^\dagger\) kills A
and has image in \(A^\perp\). Its induced action on
\(A^\perp/A\) compresses to M' on the smaller space;
its value on the last line need not be zero, but Y's
induced matrix has zero row and column there. The trace
of its product with Y is therefore \(\operatorname{tr}M'Y'\).
The trace of \(M_1Y\), by cyclicity and (3), is precisely
\(\sigma(g)\); the trace of \(M_1^\dagger Y\) is the
conjugate of the adjacent sum for \(Y^\dagger\).
This proves (5) without choosing a dual frame that
diagonalizes M.

Use the lowest-type coefficients \(c_l,c_k\) of the two
groups, in the common source Haar convention. The period
integrand is
\[
 \theta(g)=c_l(g)\overline{c_k(g')}
           \exp[-\phi(g)],\quad
 \phi(g)=\sigma(g)-\overline{\sigma(g)}.
 \tag{6}
\]
In the source frame this is the simpleRootSum character
of the Bessel average, because the flag is mapped to
the ordered standard frame, not just its subspaces.
The group contains \(U(X)\) diagonally, and its action
fixes both highest vectors (all weights there are zero).
Hence translating by it leaves \(\theta\) unchanged.

Here and below use the Frobenius norm unless a subscript
op is displayed. Put \(C=g-\operatorname{blockdiag}_Jg\).
For a row i of g the unitary relation gives
\[
 2\operatorname{Re}(g_{ii}-1)=
  2\sum_{\epsilon_j\ne\epsilon_i}|g_{ij}|^2
                  -\sum_j|(g-1)_{ij}|^2.
\]
Since M is zero on X and negative between -3B and -B
elsewhere, and since M' is nonnegative and g' compact,
(5) bounds the sum of squared row norms of \(g-1\) off X
by \(6\|C\|^2\). Apply it to \(g^{-1}\) to get the same
bound on column norms. If \(\|C\|\le\rho\le1/6\), the
X block \(u\) of g consequently satisfies
\(\|u^*u-1\|\le6\rho^2\); this follows from its column
Gram identity and the off-X column/row bound.
It is invertible, and multiplying by the inverse of
its unitary polar factor on X preserves (6).
The new X block has distance at most \(6\rho^2\le\rho\)
from 1, by the positive square-root eigenvalue inequality.
Combining the other rows and columns gives
\(\|g-1\|^2\le13\rho^2\) at this translated element.
Summing the row identity without weights and using
\(\operatorname{tr}(g-1)=\operatorname{tr}(g'-1)\) gives
\(\|g'-1\|^2=\|g-1\|^2-2\|C\|^2\). In particular both
distances are at most \(4\rho\). This is the actual
localization statement for the compact smaller group;
it does not bound the initial element near identity
without the compact translation.

## 3. A dimension-independent minor expansion

We give the short analytic estimate underlying the Gaussian
shape. For an orthogonal projection P, let
\(A_1,A_2,A_3\) be matrices of Frobenius norm at most \(\delta\),
\(\delta\le1/20\), and put \(B=\prod_{j=1}^3\exp A_j\).
Use the analytic logarithm of \(\det(1+P(B-1))\)
given by the trace-log series at the identity. Then
\[
 \log\det(1+P(B-1))=
 \operatorname{tr}P\sum A_j+
 \frac12\sum_j C_P(A_j,A_j)+\sum_{i<j} C_P(A_i,A_j)+R,
 \quad C_P(A,B)=\operatorname{tr}PA(1-P)B.
 \tag{7}
\]
The bound is \(|R|\le10^3\delta^3\) for
\(\delta\le1/10\). In fact introduce a formal scalar t,
expand each exponential and the trace-log series.
The coefficients of degrees one and two are the displayed
ones, by cyclicity of trace. In every monomial of degree
\(j\ge2\), the absolute trace is bounded by \(\delta^j\):
use the Hilbert--Schmidt inequality for two matrix factors,
and operator norm at most \(\delta\) for the others;
projections have operator norm at most one. In absolute
value the sum of numerical coefficients of such monomials
is bounded by the corresponding coefficient of
\[
                       -\log(2-e^{3s}).
\]
This scalar power series has nonnegative coefficients and
its value at \(s=1/10\) is less than 1. Thus the series
of terms of degree at least three is bounded by
\((10\delta)^3\) there and for smaller \(\delta\).
This proves (7) uniformly in the dimension, including
the choice of branch (the norm of \(B-1\) is less than 1).

If \(\|[P,A_j]\|\le\zeta\) for all j, the stronger bound is
\[
                         |R|\le 8000\delta\zeta^2. \tag{8}
\]
For \(\zeta\ge\delta\) use the previous bound. Otherwise
replace each crossing part \(PA_j(1-P)+(1-P)A_jP\) by t
times that part. Its Frobenius norm equals the commutator
norm. On \(|t|<\delta/\zeta\) the new matrices have norms
at most \(2\delta\); their remainder is holomorphic and
bounded by \(1000(2\delta)^3\). It vanishes at zero because
block-diagonal determinants multiply and their logarithms
are exactly the traces. Conjugation by \(2P-1\) makes this
remainder even in t. The maximum modulus principle applied
to \(R(t)/t^2\) gives (8). For \(\zeta=0\) the matrices
are block diagonal and the remainder is zero. This avoids
differentiation of high-weight products of determinants.

For \(Z=\log g\) near zero, let \(A_1=-U,A_2=Z,A_3=-V\)
where U,V are the strictly triangular compact parts of Z
in the two opposite orders of the Harish-Chandra parameter
l. They are ordered as in source reducedExp: for a threshold
projection P of \(-\lambda-\rho_G\), U has the crossings
from its complement into P and V the reverse.
The local holomorphic Flensted--Jensen formula is
\[
 c_l(g)=h_\Lambda^{-1}\int_K
   |m_\Lambda(k)|^2/m_{-\lambda-\rho_G}(k^*
                         e^{-U}e^Ze^{-V}k)\,dk .
 \tag{9}
\]
Here \(\rho_G\) is the half sum of all positive roots,
\(\Lambda=\lambda+\rho_G-2\rho_c\),
and \(h_\Lambda=\int_K|m_\Lambda(k)|^2\,dk\).
To check the input in (9), use the local analytic extension
of the Flensted--Jensen formula on accretive matrices with
left argument 1 (source CasimirEigenfunction.lean).
The left and right compact highest-type matrix coefficient
covariance extends holomorphically to the complexified
compact group near identity. The left opposite and right
highest-weight triangular unipotents therefore act
trivially. All three exponentials and their products are
accretive for \(\|Z\|\le1/20\), so this gives exactly (9);
no polar decomposition of a nonunitary matrix as a unitary
matrix is assumed. We retain the classical coefficient and
its local analytic continuation as representation-theoretic
inputs, rather than deriving existence of discrete series.

Use (7)--(8) with \(Q=kPk^*\). Set \(x=\|[P,Z]\|\),
\(\kappa=\|[P,k]\|=\|Q-P\|\), \(\delta=\|Z\|\).
All commutators with P of the three A's have norm at most x,
so their Q-commutators are at most \(\zeta=x+2\delta\kappa\).
The first trace at Q differs from \(\operatorname{tr}PZ\)
by at most \(\delta\kappa^2\): the compact block of the sum
of the A's is diagonal, and the sum of absolute diagonal
differences of the two projections is \(\|Q-P\|^2\).
For each crossing trace the change from P to Q has size
at most \(2\delta\kappa(x+\zeta)\). To see this, telescope
\(\operatorname{tr}QA(1-Q)B\) first in its first Q, then
in its second Q, and insert the crossing projection in
the factor paired with the difference; or write
\(C_Q(A,B)=\operatorname{tr} (QA(1-Q))((1-Q)BQ)\),
and use
\(\|QA(1-Q)-PA(1-P)\|\le2\delta\kappa\)
and Hilbert--Schmidt Cauchy--Schwarz.
The sum with the weights in (7) thus costs at most
\(9\delta\kappa(x+\zeta)\le18\delta\kappa\zeta\).
At P, expand the six terms entrywise. On opposite-sign
crossings \(Z_{ij}Z_{ji}=|Z_{ji}|^2\) and the only term is
the self term of Z, with factor 1/2. On equal-sign
crossings \(Z_{ij}Z_{ji}=-|Z_{ji}|^2\); the four surviving
coefficients are \(-1/2,+1,-1,+1\), also totaling 1/2.
Thus the second-order sum is \(x^2/4\). Combining (8)
with the trace errors, and using
\(\zeta\le x+\kappa\), proves
\[
 \log m_P(k^*e^{-U}e^Ze^{-V}k)
 =\operatorname{tr}PZ+\tfrac14\|[P,Z]\|^2+R_P,\quad
 |R_P|\le10^5\delta(x^2+\kappa^2).          \tag{10}
\]
Here \(m_P\) means the principal minor on P.
The formula is an equality after exponentiation; the
logarithm is the branch coming from (7).

Multiply (10) over the threshold projections of the
integral weight \(-\lambda-\rho_G\), using determinant
normalizations at negative levels. The determinant of
the reduced exponential is \(e^{\operatorname{tr}Z}\)
since U,V are strictly triangular. With
\[
 Q_w(A)=\sum_{i,j}|w_i-w_j|\,|A_{ij}|^2,\quad
 q=Q_{-\lambda-\rho_G}(Z)/4 ,
\]
the denominator in (9) is
\[
 e^{q-\operatorname{tr}(\Lambda Z)-R_k},
 \qquad |R_k|\le 5\cdot10^5\delta
                  (q+Q_\Lambda(k)+r^2).             \tag{11}
\]
Indeed \(\sum_P\|[P,A]\|^2=Q_w(A)\) by counting thresholds,
the compact root correction changes the diagonal trace
by at most \(r^2\delta\), and
\(Q_{-\lambda-\rho_G}(k)\le Q_\Lambda(k)+2r^2\)
since \(\|k\|^2=r\) and the compact correction has entries
bounded by r.

The compact probability weight \(m=|m_\Lambda(k)|^2\)
satisfies \(m\le e^{-Q_\Lambda(k)/2}\).
For one threshold use the determinant of
\((PkP)^*(PkP)\) on P, which is \(1-Pk^*(1-P)kP\).
Its determinant is at most the exponential of minus
the trace of the positive matrix being subtracted.
The two crossing squared norms of a unitary k are equal,
so that trace is \(\|[P,k]\|^2/2\). Multiplication proves
the claimed bound. Also \(h_\Lambda^{-1}\) is the compact
type dimension by Schur orthogonality. Weyl's dimension
formula bounds it by \((2(r+L_0)+1)^{r^2}\) when the
doubled parameters have entries bounded by \(L_0\).

Let \(R=r+k_0\) be the sum of the two group ranks, put
\(T=R^2\log\beta\), with \(\beta\ge10^{12}\) and
\(r+k_0+L_0\le\beta\).
If \(\|g-1\|\le\eta,\ \eta T\le10^{-12}\),
then \(\|Z\|\le2\eta\). Put \(s=q+Q_\Lambda(k)+r^2\).
For \(s\le50000T\) the bound (11) gives \(|R_k|\le1/20\),
and \(|e^{R_k}-1|\le1/10\). Otherwise
\[
 m e^{-q}|e^{R_k}-1|
 \le \exp(-q-Q_\Lambda(k)/2+s/4)
 \le e^{-5100T}.
\]
The last inequality uses \(s>50000T,\ r^2\le T\).
The reciprocal compact type dimension bound above gives
\(h_\Lambda\ge e^{-2T}\).
Integrating (11) in (9) proves
\[
 |c_l(g)e^{-\operatorname{tr}\Lambda Z}-e^{-q}|
                  \le e^{-q}/10+e^{-100T}.          \tag{12}
\]
The same proof holds on the smaller compact group and
on negating its parameter. All norms in this argument
were Frobenius norms; using the operator norm at this
stage without adjusting the radius would lose a rank
factor.

## 4. Cone estimate and lower period

Let \(\rho=10^{-13}/T\). If the noncompact part of g has
Frobenius norm at most \(\rho\), use localization from
section 2 and (12) in the two groups. The phase in the
matrix logarithms is exactly \(\phi(g)\).
For this assertion expand \(\log(1+Y)\): the functional
\(\operatorname{tr}M Y-\operatorname{tr}M'Y'\)
on \(Y^j,(Y')^j\) vanishes for \(j\ge2\).
Indeed they induce the stated powers on the quotient,
lower the flag by at least two, as do their adjoints,
and the trace computation of section 2 applies with
adjacent sums zero. Thus the phase of the logarithms
equals the first term (5). Both phases are imaginary.
Multiplying the two approximations (12), their product
differs from a nonnegative real number \(t\) by at most
\(0.21t+4e^{-100T}\). It follows that
\[
                         |\theta|\le2\operatorname{Re}\theta
                                              +12e^{-100T}.
 \tag{13}
\]
For example \(|\theta|-2\operatorname{Re}\theta
\le -t+3(0.21t+4e^{-100T})\).
In the other case use the determinant decay proved in
Bessel majorants. The squared determinant of the
block-diagonal part of g is
\(\det(1+C^*C)\ge1+\|C\|^2\), by the unitary identities.
Thus \(|c_l(g)|\le(1+\|C\|^2)^{-h/4}\) for the
excess gap h. With \(h\ge10^{30}T^3\) and
\(\|C\|\ge\rho\), this is at most \(e^{-100T}\)
(use \(\log(1+\rho^2)\ge\rho^2/2\)).
The smaller coefficient has modulus at most one.
This proves (13) on the whole Bessel group.

We also have
\(|\theta|\le(2/\|g\oplus g'\|_{\rm op})^{18R^2}\):
apply the coefficient decay with this exponent to the
larger of the two operator norms, bounding the other
coefficient by 1. The required exponent is below h.
Set \(N=R^2\) and \(G=(2/\|g\oplus g'\|_{\rm op})^{9N}\).
Combining the cone error with
\(|\theta|-2\operatorname{Re}\theta\le3|\theta|\le3G^2\)
gives the weighted cone
\[
              |\theta|\le2\operatorname{Re}\theta+
                                  6\beta^{-50N}G.   \tag{14}
\]
The graph of the real Bessel group is a closed embedded
subgroup in this direct sum of sign groups; its Haar
measure is the actual right invariant Bessel graph
measure. Apply the covering bound (4) of Bessel majorants
in rank R, with unit ball \(V=\nu\{\|g\oplus g'-1\|_{\rm op}
\le1\}\). It gives \(\int G\le\beta^N V\)
since \(3^{2N}2^{9N}(9/5)\le\beta^N\).
In particular the integral of (6) is absolutely convergent.

Set \(\delta_0=(128R\beta)^{-1}\) and let \(V_0\) be the
ball of this radius about identity in the same operator
norm. The near-identity estimate in Bessel majorants,
applied separately in each rank, shows
\(|\theta|\ge1/4\) there. The covering calculation at
norm radius 2 gives
\[
 V\le(3/\delta_0)^{2N}2^{4N}V_0\le\beta^{7N}V_0 .
\]
This inequality uses \(384R\beta\le\beta^3\);
\(V_0\) is positive and finite by properness.
Integrate (14), writing \(I=\int\theta\):
\[
 V_0/4\le2\operatorname{Re}I+
                   6\beta^{-42N}V_0.
\]
Hence \(\operatorname{Re}I\ge V_0/16>0\), and
\[
                  V\le\beta^{8N}|I|.                \tag{15}
\]
For the actual Bessel graph the second component is
compact, but the unit ball in (15) includes the second
component's distance to identity. To bound the source
ball, which restricts only g, apply the very same covering
bound at operator norm radius 2 for the whole direct sum:
the compact component has norm one. It gives at most
\(\beta^{7N}V_0\), so (15) holds for the source ball
as well. For the larger ball of norm radius \(\beta+1\)
the corresponding bound is \(\beta^{12N}|I|\).
This improves the source's exponent \(20N\) in both cases.

The source filling uses \(B=\mathrm{liftWeight}(0)\),
\(a=\mathrm{columnCount}(1)\), \(L_0=3\,\mathrm{Data.a}\),
\(\beta=b^3\), and excess gap at least \(r_{\rm Data}^7\).
The parameter inequalities used here are exactly
FillingData.lean 222--308:
\(3B+a\le b^2,\ 8nr\le b,\ R+L_0\le b^3\),
\(b^3\ge10^{12}\), \(10^{30}(R^2\log(b^3))^3\le r_{\rm Data}^7\).
They are explicit large-parameter assumptions of the
source admissible scale; this chapter does not choose
that scale anew. The steep sign and weight identities
are the source filling identities (one positive weight
at the special coordinate and zero on the rest).
The normalized average from the previous chapter has
\(d_l\|W\|_2^2=I\). Thus (4),(15) prove its stationary
lower bound with \(m=24(r+k_0)^2\le96r^2\).
Substituting in the previous chapter's sharpened majorant
gives
\[
 a_{\rm maj}\int w_{\rm maj}\le b^{119r^2}\dim I_{\rm val},
 \qquad
 \|F^\flat-F\|_2^2
      \le b^{119r^2-6r^3 f}\dim I_{\rm val}.          \tag{16}
\]
Here \(I_{\rm val}\) is the value space, not the period I.
This supplies the nonzero local Bessel average and its
normalization under the stated filling inequalities,
with improved exponents. It does not imply a lower
bound for the full global Poincare moment before the
arithmetic return estimates.

## Source dictionary and classical input

Pinned revision
[72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).
The residue frame is StationaryPosition.lean 47--268,
309--382,626--752 (blob 83bed2af7e2289243f93844501ee22ae5ac2586b).
The trace and phase are Positions.lean 289--344,432--485
and PositionGroup.lean 309--372. Frame length:
New/Spanning/Bessel/Basic.lean 479--574,
LargeFunction.lean 228--465. The minor expansion compares
MinorSecondOrder.lean 216--305,493--586,
OneMinor.lean 497--629 and GaussianShape.lean 129--393.
The short trace-series estimate in (7) replaces the
individual cubic expansion bounds. Localization.lean
522--721 and Periods.lean 235--549 give the corresponding
source localization and Laplace theorem.
FillingData.lean 222--431 gives the precise filling input.
For the local coefficient continuation see
Lib/DiscreteSeries/FlenstedJensen/CasimirEigenfunction.lean
637ff, and its preceding splitCoeff and accretive formulas.
Classical input: B. Sun, *Matrix coefficients of
cohomologically induced representations*, Compos. Math.
143 (2007), 201--221,
[doi:10.1112/S0010437X06002508](https://doi.org/10.1112/S0010437X06002508),
and the Flensted--Jensen lowest-type coefficient theorem
specified in Bessel majorants. The manuscript uses their
coefficient realization with the normalization read from
the pinned source, not a general quantitative stationary
phase theorem as a black box.

The noncompact oscillator arrows, formal-degree/volume
dictionary where required in the global moment, Sobolev
and quantitative Poincare return bounds remain separate
tasks. No new Lean replay is asserted.
