# Bessel averaging, reproduction and sharper uniform majorants

We use the actual lowest-K-type coefficient and Bessel quotient
measures of the source, not an arbitrary rapidly decreasing kernel.
The stationary-point lower bound that supplies a nonzero normalized
Bessel system, and the arithmetic return estimates, remain distinct
obligations. The results here establish the coefficient decay,
absolute integration, reproducing identity, norm/period identity and
the quantitative majorant and cut-tail argument from that lower
bound. They reduce the exponent 99 in the source covering/degree
product to 23.

## 1. The discrete-series coefficient

At one infinite place let G=U(J), J diagonal with entries +/-1,
of rank r>=1, and K its maximal compact group. Use the operator norm
in this sign frame and probability Haar measure on K. Write
l=2 lambda for the source doubled Harish-Chandra parameter,
mu=lambda+rho and Lambda=lambda+rho-2rho_c for the two integral
weights in its Flensted-Jensen formula. Here rho is half the sum
of roots positive for lambda, and rho_c is the half-sum of their
compact subset. Let m_w be the product of principal minors
for integral weight w (including division by the determinant
at negative levels).

For g=k z with k in K and z positive definite, the actual
coefficient is
\[
 c_\lambda(kz)=
 {1\over h_\Lambda}\int_K
 {m_\Lambda(ku)\overline{m_\Lambda(u)}
                 \over m_{-\mu}(u^*zu)}\,du,\qquad
 h_\Lambda=\int_K|m_\Lambda(u)|^2\,du.
 \tag{1}
\]
For k_1 z k_2 use the two-sided version with the numerator
m_Lambda(k_1 u) times the conjugate of m_Lambda(k_2^{-1}u).
This is the source dsCoeff_polar formula, and its normalization
c_lambda(1)=1. We use the classical Flensted-Jensen matrix
coefficient theorem for the lowest K-type of the discrete series,
with this formula and its Schur orthogonality. The parameters
have the source regular integral parity and opposite-sign gap
(at least 500 r^3+A); thus they lie in the discrete-series
range. In particular the idempotent is
e_lambda=d_lambda conjugate(c_lambda), with
d_lambda=(integral_G |c_lambda|^2)^{-1}>0 for the very same Haar
measure on G. There is no normalization of d_lambda by the
compact volume of G when G is noncompact.
Alternatively the source proves the coefficient and idempotent
theorems directly; our estimates below use (1) and its
reproducing identity as the classical coefficient input.

Here is a useful direct decay proof. Suppose the gap is h,
and 0<=m<=h is an integer. Set a=(z+z^{-1})/2, the positive
block diagonal part of z. For each integer t consider
S={i: mu_i>=t}, B={i: mu_i<t<=mu_i+m},
C={i: mu_i+m<t}. Since the difference between mu entries
of opposite signs is at least h, B has only one sign.
Fischer's inequality for positive Hermitian matrices,
followed by Jacobi's complementary-minor identity, gives
\[
 \det a_{S\cup B}\le \det a_S\det z_B
                 \le \det a_S\det z_S\det z_C .
\]
For the second inequality, z^{-1}=JzJ and det z=1 imply
det z_B=det z_{B^c}; apply Fischer to S and C.
Multiply over the levels t, including the determinant
normalizations of the negative levels. Since
m_{mu+m}(a)=m_mu(a)(det a)^m, this gives
\[
 (\det a)^m\le m_\mu(z)m_{\mu+m}(z^{-1})
                       =m_{-\mu}(z)^2 .
\]
All factors are positive, and the same bound holds at
u^*zu for u in K. Use Cauchy-Schwarz in the numerator
of (1) and invariance of K-Haar to conclude
\[
 |c_\lambda(g)|^2(\det a)^m\le1 .
\]
The singular values of z are pairs exp(t_i), exp(-t_i),
with possible ones, by z^{-1}=JzJ (or the usual hyperbolic
polar decomposition). Its block diagonal part has the
corresponding pairs cosh(t_i),cosh(t_i); all other entries
in its spectrum are one. Hence det a >= (||g||/2)^2.
We have proved
\[
 |c_\lambda(g)|\le(2/\|g\|)^m,\qquad |c_\lambda(g)|\le1.
 \tag{2}
\]
The compact case has no opposite-sign restriction and
satisfies the same inequalities. This proves the source
decay by principal minors without estimating any derivatives.

## 2. A smaller near-identity ball

Assume |l_i|<=L, and put beta=r+L+1 and
\[
                         \delta=(128r\beta)^{-1}.
\]
We claim
\[
                  \|g-1\|\le\delta
                      \quad\Longrightarrow\quad |c_\lambda(g)|\ge1/2.
 \tag{3}
\]
In the ordinary polar decomposition g=kz, one has
||z-1||<=delta by the singular-value perturbation inequality,
and ||k-1||<=2delta/(1-delta)<=4delta. Both mu and
Lambda have entries of absolute value at most beta:
each half-root sum has coordinate size at most (r-1)/2,
and the compact and noncompact terms in Lambda have disjoint
root supports.

Every principal submatrix of u^* z u has eigenvalues in
[1-delta,1+delta]. The absolute logarithm of its determinant
is at most twice delta times its size. For a negative weight
level use the complementary minor of the inverse, which has
the same logarithmic bound. The sum of the sizes of all
minors used for weight -mu, with this negative-level
convention, is sum_i |mu_i|. Thus for every u
\[
 |\log m_{-\mu}(u^*zu)|\le2r\beta\delta .
\]
The reciprocal denominator differs from 1 by at most
exp(2r beta delta)-1.

The compact highest vector coefficient m_Lambda restricted
to K is the coefficient of a unit highest vector in its
irreducible representation. Each compact sign block has a
dominant integral highest weight of entries bounded by beta.
Write it as a tensor of exterior powers with nonnegative
multiplicities and a determinant character, allowing a
negative determinant exponent. The total number of
standard or dual tensor slots is at most 3r beta
(the sum of row lengths after subtracting the smallest entry
is at most 2r beta; the determinant twist costs at most
r beta). The irreducible is a unitary subrepresentation of
this tensor. Telescoping the tensor products of unitary
operators shows
\[
 \|\rho_\Lambda(k)-1\|\le3r\beta\|k-1\|.
\]
In (1) replace the denominator by one. The resulting integral
is m_Lambda(k) by compact Schur orthogonality. The error of
the replacement is at most exp(2r beta delta)-1 by
Cauchy-Schwarz. Consequently
\[
 |c_\lambda(g)-1|
 \le12r\beta\delta+\exp(2r\beta\delta)-1<1/2 .
\]
This proves (3), including negative determinant weights
and compact sign blocks of dimension one.
Unlike the global Lipschitz estimate in the source this
argument is only a near-identity estimate, which suffices
for all the volume bounds below. It does not replace a
global derivative bound where one is separately required.

## 3. The general covering argument

Let H be a closed subgroup of G, or a group mapping
properly and injectively into G, with right Haar measure nu.
All its norms are read in the same sign frame. For x,y in G
put f(s)=||x^{-1}s y||, so f>=1 and
||g^{-1}||=||g|| for g in G. Define
\[
 V_x(\eta)=\nu\{s:\|x^{-1}sx-1\|\le\eta\},
                          \quad 0<\eta\le1.
\]
This volume is finite by properness, and positive for
nonzero Haar measure. In the real normed vector space
M_r(C), dimension D=2r^2, take a maximal eta/R-separated
set among x^{-1}s y of norm at most R>=1.
The disjoint norm balls of radius eta/(2R) around those
points lie in the ball of radius R+eta/(2R).
Comparing Lebesgue volumes bounds the number by
(1+2R^2/eta)^D. Maximality covers the whole set by balls
of radius eta/R; a greedy selection terminates by the same
packing bound. If s_i is the point of H at a covering centre,
then
\[
 \|x^{-1}ss_i^{-1}x-1\|
 =\|(x^{-1}s y-x^{-1}s_i y)(x^{-1}s_i y)^{-1}\|
 \le\eta .
\]
Right invariance therefore gives, uniformly in y,
\[
 \nu\{s:f(s)\le R\}\le(3/\eta)^D R^{2D} V_x(\eta).
\]
For M>2D the layer-cake formula, proved by Tonelli from
f^{-M}=M integral_f^infty R^{-M-1} dR, yields the stronger
uniform covering estimate
\[
 \int_H (2/f(s))^M\,d\nu(s)
 \le (3/\eta)^D\,2^M\,{M\over M-2D}\,V_x(\eta).
 \tag{4}
\]
This proof is independent of the Haar normalization.

Take M=9r^2, eta=1, H the actual Bessel graph embedded by
its first projection. It is a closed subgroup of G (the
second component is its Levi part), so that projection is
proper, also after conjugation by x. Use its du dh measure,
which is right invariant: U is unimodular and the compact
Levi H acts on it with modulus one. Put
\[
 C_R=3^{2r^2}2^{9r^2}\,9/5,\qquad V_x=V_x(1).
\]
Then (4) is precisely the uniform Bessel average majorant,
with C_R in place of 16^{9r^2}.

Apply (4) again with H=G,x=y=1,eta=delta from (3).
Schur normalization gives
\[
 V_1(\delta)\le 4/d_\lambda.
\]
It follows that
\[
 d_\lambda\int_G(2/\|g\|)^M\,dg
    \le 8(3/\delta)^{2r^2}2^M.                     \tag{5}
\]
In the actual source range b>=2000, beta<=b^4,
3/delta<=384 beta^2<=b^9 and 2^M<=b^{r^2}.
Also 8<=b^{r^2}, and
C_R=(9/5)4608^{r^2}<=b^{3r^2}.
Thus the product of (5) and C_R is at most
\[
                             b^{23r^2},            \tag{6}
\]
instead of b^{99r^2}. The same sublevel calculation gives
d_lambda vol{||g||<=T} <= 4(3/delta)^{2r^2} T^{4r^2}
for T>=1. All constants use exactly the same Haar measure
as d_lambda.

## 4. Averaging and the normalized Bessel system

Let R=U H be the source real Bessel subgroup, U the
unipotent radical and H its compact definite Levi. Its
representation on the value space is
pi(s)=wave(simpleRootSum(s)) rep(h). It is unitary;
simpleRootSum is additive on R and the wave has
absolute value one. For a unit vector v and x in G set
\[
 W(y)=\int_R c_\lambda(x^{-1}s y)\pi(s)^{-1}v\,ds .
 \tag{7}
\]
Equations (2),(4) give absolute convergence and a bound
uniform in y. They also give continuity: on a compact
neighborhood of y_0, the norm of x^{-1}s y is bounded
below by ||x^{-1}s y_0|| times a positive fixed constant,
and (4) bounds the resulting majorant. Right invariance
of the R measure yields W(s_0 y)=pi(s_0) W(y)
by substituting s s_0^{-1}.

Use the quotient measure on U\G obtained by Weil
integration with the source unipotent measure, and the
probability Haar measure on H. Then for nonnegative phi
\[
 \int_{U\backslash G}\int_R \phi(x^{-1}s y)\,ds\,d\dot y
                        =\int_G\phi(g)\,dg .       \tag{8}
\]
This is first the U-unfolding and then the compact
H-translation of the quotient. It is valid for the
source besselQuotMeasure as an integration of
left-U-invariant functions. By (2),(5),(8), W is
integrable on this quotient; boundedness implies L^2.
The coefficient reproducing identity is
\[
 \int_G d_\lambda c_\lambda(a^{-1})c_\lambda(g a)\,da
                      =c_\lambda(g).
\]
Insert (7). Fubini is justified by the uniform absolute
bound C_R V_x and the L^1-norm of the kernel, so
\[
 \int_G e_\lambda(a)W(y a)\,da=W(y).
 \tag{9}
\]
For the norm-period identity, unfold using (8) and
W(s y)=pi(s)W(y). With Hermitian pairing linear in the
second argument,
\[
 \begin{aligned}
 d_\lambda\int_{U\backslash G}\|W(y)\|^2\,d\dot y
 &=d_\lambda\int_G
       \overline{c_\lambda(x^{-1}g)}\langle v,W(g)\rangle\,dg\\
 &=\langle v,W(x)\rangle .
 \end{aligned}                                             \tag{10}
\]
The unfolded integrand is absolutely integrable by the
boundedness of W and integrability of c_lambda.
The last equality is (9). In particular the period on
the right is real and nonnegative, and strictly positive
if and only if W is nonzero. This does not prove a
quantitative lower bound on that period.

To get the actual source majorant, suppose the stationary
point supplier gives x and v such that the source length
L_B(x)<=b^{5n}, n=varrho+1, and
\[
                 V_x\le b^m d_\lambda \|W\|_2^2,\quad W\ne0 .
 \tag{11}
\]
Here L_B is the source Bessel frame length; it is left
R-invariant and satisfies L_B(xg)<=L_B(x)||g||.
These identities are the length properties used in
CutTailBound.lean (the definition uses the transported
frame columns, whose norms after right multiplication
increase by at most the operator norm).
Set F=cW with |c|^2||W||_2^2=dim I, where I is the value
space, and define
\[
 \Phi(y)=\int_R(2/\|x^{-1}s y\|)^M ds,\quad
 w(y)=|c|\Phi(y),\quad a=|c| C_R V_x .
\]
Then w<=a and for every i<=A
\[
 \max(1,L_B(y)/b^{6n})^i\,\|F(y)\|\le w(y).
 \tag{12}
\]
Indeed for large scaled length it is at most
(||x^{-1}s y||/2)^i; apply (2) with exponent M+i
and integrate. For small length use (2) with M.
Both exponents are within the given gap.
The majorant is left R-invariant by right Haar invariance.
Its integral is (8). Equations (5),(6),(11) give
\[
                    a\int w\le b^{m+23r^2}\dim I.         \tag{13}
\]
In the source m<=301r^2, this is b^{324r^2} dim I
in place of b^{400r^2} dim I.

For the source cutoff of radius B=b^{6n+2}, multiply F
by max(0,min(1,2-2 L_B/B)). The difference vanishes
unless L_B>B/2. On that set the scaled length in (12)
is at least b^2/2>=b. Taking i=3r^3 f<=A gives
\[
 \|F^\flat-F\|_2^2\le
          b^{-6r^3 f}\,a\int w
       \le b^{324r^2-6r^3 f}\dim I .
 \tag{14}
\]
This implies the source bound b^{-2r^3 f} dim I for
r>=100 and f>=1 and improves its excess exponent.
All statements in this subsection requiring (11) remain
conditional on the stationary-point period lower bound.

## 5. The real Bessel formula in the adelic frame

Take the tensor of the local averages (7) at the
infinite places, with their respective nonzero rescalings
c_v, points x_v, and vectors v_v as in (11).
The rational Bessel grading identifies its real group
with the product of the Bessel graphs by its frame
isometries, and the two Haar measures differ by a fixed
positive scalar h. The global real point g is the
preimage of the tuple x_v under the filling frame
homeomorphism. The source simple-root character
is psi_E(-(M delta_E)^{-1} times simpleRootSum).
In the real coordinates of the filling,
simpleRootSum_local=-2 pi i times the corresponding
adelic character argument. Hence on the real
Bessel group its inverse is exactly the product of
wave(-simpleRootSum_local): indeed z-conjugate(z)
for z=2 pi i a equals 2 pi i times 2 Re(a).
This gives the sign and the factor of two; no
independent local character is chosen.

Let B be the actual linear isomorphism from the
Weyl coefficient module to the row coordinates of
the tensor value space (the transposed Schur
representation). For a vector z in that module
the action of a Levi element k is
B(rho_conj(k)z)=B(z) rep(k^{-1}), in row coordinates:
this follows from k^{-t}=conjugate(k) and the
Schur composition law. The conjugate of the type
kernel at g^{-1}s y is the product of the positive
formal degrees times c_lambda(x_v^{-1}s_v y_v);
the left frame factor cancels in the relative argument.
Pair the tensor product of (7) with B(z).
Absolute convergence at each place and finitely many
tensor factors justify Fubini componentwise.
The result is exactly
\[
 \langle B(z),F_{\mathrm{full}}(y)\rangle_{\rm bil}
   =\int_{R_\infty}
      \overline{e(g^{-1}s y)}\,\psi_R(s)^{-1}
                 t(\rho_{\rm conj}(k(s))z)\,ds,
 \tag{15}
\]
where the pairing on the left is the row-column
bilinear pairing and the single linear functional is
\[
 t(z)=h\,{\prod_v c_v\over\prod_v d_{\lambda_v}}\,
                      B(z)\cdot\bigotimes_v v_v.
\]
The Haar ratio h is taken in the direction
product integral = h times global integral.
This is the actual BesselFormula.lean construction,
including the fixed common scalar and the inverse Levi
action. Its reproducing property is (9), tensorized
under the same absolute convergence. Formula (15)
requires the actual local normalized systems from (11)
and the stated filling frame identification.
It is not a proof of the stationary-point supplier,
the local Sobolev derivative bounds, nor the arithmetic
Poincare class-return estimates.

## References and scope

All source references are pinned to
[lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).

* Lib/DiscreteSeries/FlenstedJensen/Defs.lean 126--201,
  blob 06079adda3122542487f75c50b256a3fb98b326c;
  PsiKTypes.lean, dsCoeff_polar; SquareIntegrability.lean
  170--329, 870--956, blob d6cc5f4a9f2831f12a22e272581732bb436688b9.
  Classical coefficient input: M. Flensted-Jensen, Ann. of Math.
  111 (1980), 253--311; B. Sun, Compos. Math. 143 (2007),
  matrix coefficients of cohomologically induced representations,
  Theorem 1.1 (arXiv:math/0403440). We have matched the source
  formula (1), not independently reproduced the classical
  discrete-series existence theorem.
* New/Spanning/Bessel/LargeFunction.lean 478--735,
  blob 29296c8227e564ce43a8ac5b6581031d8958bdb5;
  CutTailBound.lean 61--186, 214--380,
  blob a06560c397138b3a42de7cc3186bd8f39029f770.
* New/Spanning/Unfolding/BesselFormula.lean 259--436,
  blob a77c1c5dbb1bd9c3bfdb475fd1a608c0760d4d7b.

The near-identity and covering constants (3)--(6) are new
ordinary estimates. The Bessel majorant and tail estimates
(12)--(14) follow with the exact source hypothesis (11).
The remaining stationary nonvanishing/period lower bound,
local Sobolev estimates, Poincare return and open-cell
estimates must still be proved to obtain the full moments.
No fresh Lean replay is asserted.
