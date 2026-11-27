# Quantitative real restrictions and arithmetic Poincare returns

This chapter supplies ordinary proofs of the derivative-filtration estimate,
the Schur-to-section estimate, arithmetic frame separation, weighted return
summation, and the resulting absolute Poincare convergence and truncation
bound. The estimates use the actual Bessel frame and cutoff geometry of the
preferred construction. They do not supply the identity, terminal-fixer or
open-cell *second-moment* bounds, or good-form multiplicities.

Two improvements are useful. The local convolution restriction costs
`P^(268 n^2)`, in place of the source's `P^(2000 n^2)`. The arithmetic return
count retains `(1 + 4 N b^(74n))^(2nrf)`, instead of enlarging it to
`b^(12 n^3 r f)`. Neither improvement is needed to change the main proof
architecture.

The normalized discrete-series coefficient is a classical input, as in
[Bessel majorants](lsernau-bessel-majorants.md). All uses of that input are
specified below. In particular, this chapter does not replace the
noncompact Casimir-rigidity argument needed for a theta lift by a Sobolev
estimate.

## 1. Normalizations and precise inputs

Write

\[
 n=\rho+1,\qquad r=k+2\rho+1,\qquad f=[E^+:\mathbf Q].
\]

Here `k>=1`. At a real place the hermitian basis is
`e_1,...,e_rho; x_1,...,x_k; z; e_1^*,...,e_rho^*`.
The `e_a,e_a^*` are hyperbolic pairs, the `x_i` are orthonormal positive
vectors, and `z` has norm minus one. Denote this hermitian involution by
`J`, its unitary group by `G`, and the frame `(e_1,...,e_rho,z)` by `F`.
Let `U` be the Bessel unipotent group, `U_0` its subgroup fixing `F`, and
`H=U(k)` the compact group on the positive middle space. Its Haar measure
is probability measure. The frame fixer is `R_0=U_0 H`.

For a complex `n` by `n` matrix `Z`, put

\[
 \xi(Z)=(Z^{-1})_{nn},\quad
 \nu(Z)^2=1-|\xi(Z)|^2,\quad
 \Delta(Z)=|\det Z|^2-|\det Z_{<n,<n}|^2.
\]

The open cell is `Omega={det Z != 0, |xi(Z)|<1}`. On it,
`Delta(Z)=|det Z|^2 nu(Z)^2`.
Call `Z` bounded by `P` when

\[
 \|Z\|,\ \|Z^{-1}\|,\ \nu(Z)^{-1}\le P.
 \tag{1}
\]

Use the compact-dual Haar normalization in the coefficient and
formal-degree formulas. Define the explicit geometric constants

\[
 \operatorname{vol}U(j)=\prod_{a=0}^{j-1}\frac{2\pi^{a+1}}{a!}.
\]

These constants are not the total masses under the normalized Haar
measures: the compact group `U(j)` has Haar mass one. More precisely,
at the identity of `U(J)`, write `S=Jg^{-1}dg` in skew-hermitian
coordinates, using its imaginary diagonal entries and the real and
imaginary parts of its entries above the diagonal. The Haar density
there is `dS / vol U(r)`. The source rotates each pair of real
off-diagonal coordinates orthogonally, which preserves this volume.
Set

\[
 c_G=\frac{\operatorname{vol}U(k)}{\operatorname{vol}U(r)}
          \frac{2\pi^k}{(k-1)!},\qquad
 d\mu_c(h,u)=c_G c^{k-1}\,dh\,du.
 \tag{2}
\]

All restriction estimates below use exactly this measure. Rescaling Haar
measure requires rescaling the formal degree and (2) together.

The coefficient input is an irreducible unitary discrete series `pi` of
`G`, a unit lowest-`K`-type vector `v`, its normalized coefficient `c`, and
formal degree `d_pi`, with the following familiar normalization:

\[
 c(1)=1,\quad e=d_\pi c,\quad e=e^*=e*e,\quad
 \int_G|c(g)|^2dg=d_\pi^{-1}.
 \tag{3}
\]

Fix the inner product to be linear in its second argument and put
`c(g)=<v,pi(g)v>`. Our convolution and right translation conventions are

\[
 (F*e)(x)=\int_G F(xy^{-1})e(y)\,dy,\qquad
 R(g)F(x)=F(xg).
\]

Thus, with `p(g)=e(g^{-1})=d_pi overline{c(g)}`, one has
`F*e=R(p)F`. We require `e` to be integrable. The large-gap coefficient
decay in the majorant chapter is the intended supplier. A Bessel function
`W:G -> V` is bounded, transforms on the left by the fixed unitary
character of `U` and unitary representation of `H`, belongs to
`L^1(U\G)`, and is fixed by right convolution with `e`. These assumptions
give `W in L^2(U\G)`. This notation means the Hilbert space of equivariant
`V`-valued sections over `U\G`, with the prescribed unitary character;
their squared norms descend to the quotient. Right translation is a
unitary representation on this Hilbert space.

## 2. A direct filtration and Schur estimate

Let `l` be the doubled Harish--Chandra parameter, with `|l_i|<=L`.
The lowest compact highest weight `lambda` then satisfies
`|lambda_i|<=L+r`. Put `L_0=L+r`. Let `M_s` be the span obtained from the
lowest compact type by at most `s` applications of the complexified Lie
algebra `gl_r`.

### Proposition 1: derivative norm

For `w in M_s` and any complex matrix `X`,

\[
 \|d\pi(X)w\|
 \le (r+1)^4(L_0+1+s)\|X\|_{\rm op}\|w\|.
 \tag{4}
\]

**Proof.** The compact group is `K=U(p) x U(q)`. The space `M_s` is a
quotient of a finite sum of
`gl_r^{tensor j} tensor tau`, `0<=j<=s`, where `tau` is the lowest compact
type. Every weight of `tau` is in the convex hull of the compact Weyl
orbit of its highest weight. Every weight of `gl_r` is zero or a root
`e_i-e_j`. Consequently every compact highest weight occurring in `M_s`
has coordinates of absolute value at most `N=L_0+s`. In particular `M_s`
is finite dimensional and stable under `K`.

Let `C_K=sum_{epsilon_i=epsilon_j} E_ij E_ji` and
`C=sum_{i,j} E_ij E_ji`. The compact Casimir on a highest weight `mu`
has eigenvalue `sum_i mu_i(mu_i+2rho_K,i)`, at most `r N(N+r)`.
The full Casimir has eigenvalue

\[
 \kappa_l=\frac14\sum_i(l_i^2-(2\rho_i)^2)\ge-r^3/4.
\]

Unitarity gives `d pi(E_ij)^*=epsilon_i epsilon_j d pi(E_ji)`.
Therefore

\[
 \sum_{i,j}\|d\pi(E_{ij})w\|^2
 =\langle w,(2C_K-C)w\rangle
 \le\{2rN(N+r)+r^3/4\}\|w\|^2.
 \tag{5}
\]

Expand `X` in matrix units and apply Cauchy--Schwarz. Using the weaker
but convenient bound `sum|X_ij|^2 <= r^2 ||X||_op^2`, (4) follows from

\[
 r^2\{2rN(N+r)+r^3/4\}
 \le(r+1)^8(N+1)^2.
\]

For example, the left side is at most
`(2r^3+2r^4+r^5/4)(N+1)^2`, whose coefficient is at most `(r+1)^8` for
every integer `r>=1`. This proves the estimate without the noncompact
Casimir-rigidity theorem. The same proof works under the lower bound
`<w,Cw> >= kappa_l ||w||^2`, rather than a scalar Casimir. QED.

It follows, for a word of `s` matrix units, that the differentiated
lowest vector has norm at most

\[
 \{(r+1)^4(L+r+1+s)\}^s.
 \tag{6}
\]

A unitary change of frame does not alter the matrix-unit operator norm.

### Proposition 2: Schur estimate with derivatives

Suppose

\[
 P\ge (r+1)^4(L+r+1+2n^2).
 \tag{7}
\]

There is a smooth derivative family `W_w`, indexed by words in the
matrix units, with `W_empty=W`, the same left Bessel transformation
law, and, for `|w|<=2n^2` and `phi in L^1(G) cap L^2(G)`,

\[
 \int_{U\backslash G}
 \left\|\int_G\phi(y)W_w(gy)dy\right\|^2dg
 \le P^{2|w|}\frac{\|W\|_{L^2(U\backslash G)}^2}{d_\pi}
                   \|\phi\|_{L^2(G)}^2.
 \tag{8}
\]

**Proof.** In the conventions just fixed, Schur orthogonality gives
the rank-one convolution identities

\[
 e*\delta_g*e=c(g^{-1})e,\qquad
 p*\delta_g*p=c(g)p.
\]

Since `R(p)` is an orthogonal projection and `R(p)W=W`,
`<W,R(g)W>=||W||_2^2 c(g)`. If `W=0` the assertion is immediate.
Otherwise the map `pi(g)v -> R(g)W/||W||_2` preserves all inner
products, hence extends to a unitary equivalence from `pi` onto the
cyclic right-translation representation generated by `W`. The chosen
lowest vector is multiplied by `||W||_2`.

For a vector `a` in this copy, Schur orthogonality says that the functions
`g -> <b_j,pi(g)a>`, for an orthonormal basis `b_j`, are pairwise
orthogonal in `L^2(G)` and have squared norm `||a||^2/d_pi`.
Bessel's inequality applied to `phi` gives
`||integral phi(g) pi(g)a dg||^2 <= ||a||^2 ||phi||_2^2/d_pi`.
Now use (6) and (7).

The differentiability and boundedness can also be established directly
in the original function model. For the contragredient representation,
sandwich a smooth approximate identity between the compact
matrix-coefficient projector for the multiplicity-one lowest compact
type, and divide by its nonzero matrix coefficient. This produces
`beta in C_c^infty(G)` with `e*beta=beta*e=e`.
Then `W=W*beta`, and differentiation moves to a compactly supported
derivative of `beta`. Each resulting function is bounded and continuous;
dominated differentiation is justified by boundedness of `W` and the
compact support. The representation calculation (6), rather than a
bound for derivatives of `beta`, supplies the quantitative constant.
Thus no uniform approximate-identity seminorm is being assumed. QED.

## 3. The actual Gram section and its measure

Here is an explicit section, so that a qualitative smooth-section
argument does not hide a parameter-dependent constant. Write
`D(t)=diag(1,...,1,t)` and let `F'=(e_1^*,...,e_rho^*,x_1)`.
For independent complex matrices `Z,T`, define

\[
 \begin{split}
 A(Z,T)&=D(0)-I-D(0)T^{-1}(I-D(1/2))Z^{-1}D(2),\\
 s(Z,T)&=(1-\xi(Z)\xi(T))^{1/2},\\
 B(Z,T)&=(F A(Z,T)+F'D(s(Z,T)))Z,\\
 \Gamma(Z,T)&=I+(B(Z,T)-F)F^*
  +\{(FT^{-1}-B(Z,T)A(T,Z))D(s(Z,T)^{-1})-F'\}F'^*.
 \end{split}
 \tag{9}
\]

The square root is the branch on the right half-plane. For `Z,T in
Omega` its argument has positive real part. Put `gamma_Z=Gamma(Z,Z*)`.
Multiplying (9) by `F` and by its dual frame verifies
`gamma_Z* J gamma_Z=J` and `F* J gamma_Z F=Z`. In this multiplication one
uses `F*JF=D(0)-I`, `F*JF'=D(0)`, and the definition of `A`; the remaining
positive middle vectors are fixed.

For matrices bounded by `P>=8`, the following estimates follow directly
from (9):

\[
 \|A(Z,T)\|\le2+8P^2,\quad |s|\le2,\quad |s^{-1}|\le2P,
 \quad\|\Gamma(Z,T)\|\le P^{12}.
 \tag{10}
\]

For clarity, `||F||,||F'||<=1`, `||B||<=(5+8P^2)P`, and substitution
gives
`3+(5+8P^2)P+(P+(5+8P^2)P(2+8P^2))(1+2P)` as an upper bound for
`||Gamma||`; it is at most `P^12` for `P>=8`.

If `Y` is within `P^-6` of a matrix bounded by `P>=4`, the inverse
identity gives `||Y^-1||<=2P` and
`|xi(Y)-xi(Z)|<=2P^-4`. Hence `nu(Y)^2>=nu(Z)^2/2`, and `Y` is bounded
by `2P`. Apply Cauchy's inequality to the holomorphic function
`Gamma(Z,T)` on the product of these balls. After restricting to
`T=Z*`, this gives the convenient bounds

\[
 \|\gamma_Z\|\le P^{18},\qquad \|D\gamma_Z\|\le P^{25}.
 \tag{11}
\]

In particular, if a real coordinate curve `p(t)` has speed at most
`P^2/4` and `||a||<=P^20`, then `g(t)=gamma_{p(t)}a` has right
logarithmic derivative of norm at most `P^85`. Indeed,
`||g^-1||<=P^(18+20)` and `||g'||<=P^(25+2+20)`. Here
`||g^-1||=||g||` because `J` is a hermitian involution.

The measure comparison required below is

\[
 \int_\Omega c_G\Delta(Z)^{k-1}
   \int_{R_0}\int_{R_0} h(s'\gamma_Zs)\,ds\,ds'\,dZ
 \le\int_G h(g)dg\qquad(h\ge0).
 \tag{12}
\]

Its density can be checked by elementary coarea, not by an appeal to an
unspecified open-cell constant. A full-rank frame `Y` has Gram matrix
`T=Y*JY`; the differential of this Gram map is surjective. On the open
set where `Z=F*JY` is invertible, write `Y=Y'Z` with `F*JY'=I`.
The free variables in a dual frame `Y'` are a `rho` by `n` block and a
`k` by `n` positive block. The hermitian part of the first `rho` columns
is determined by `T`, leaving the unipotent variables and a vector in
`C^k` whose squared norm is `1+(Z^{-*}TZ^{-1})_nn`.
The diagonal hermitian equations contribute `2^-rho`. Radial
integration in `C^k` contributes
`(pi^k/(k-1)!) t^(k-1) dt`. The change of columns by `Z` and change of
Gram matrix by congruence contribute
`|det Z|^(2(k+rho))/|det Z|^(2n)=|det Z|^(2(k-1))`.
At `T=F*JF` the resulting frame-fibre density is therefore

\[
 \frac{2\pi^k}{2^n(k-1)!}\Delta(Z)^{k-1}\,dZ\,dR_0.
\]

Here fibre measure means the measure obtained from ordinary Lebesgue
measure and the stated real Gram coordinates on the full-rank locus,
where the Gram map is a submersion. The coordinates above and their
densities vary continuously with `T` near `F*JF`; thus the calculation
holds on this particular regular fibre, not just for almost every
Gram matrix.

The conversion from frame fibres to Haar measure has three explicit
factors. On full bases, at `Y=I`, write
`J dY=S+dT/2`, with `S` skew-hermitian. Each diagonal real coordinate
contributes `1/2`; for each off-diagonal pair the map from the four
real entries of `dY` to the hermitian and skew-hermitian coordinates
has determinant of absolute value one. Left multiplication by `J`
also preserves real volume. By the Haar normalization above, the
full-basis fibre measure is therefore

\[
 a_r\,dg,\qquad a_j=\frac{\operatorname{vol}U(j)}{2^j}.
\]

This identity holds along the entire fibre: left multiplication by
`g in U(J)` preserves both the Gram map and ambient Lebesgue measure.
For a frame-fibre measure, first append the `rho` dual isotropic
columns. After fixing their products with `F`, they are
`e^*+eA+xC`. Write
`C=-B^*` and `A=S+T/2-BB^*/2`, where `S` is skew-hermitian.
Translation by `BB^*/2` and conjugate transposition preserve real
volume, and the hermitian/skew-hermitian split contributes `2^-rho`.
At the specified Gram matrix this is exactly `2^-rho du`, with `du`
the chosen Haar measure of `U_0`.

The resulting `2rho+1` columns have a positive definite orthogonal
complement of dimension `k`. Append an orthonormal basis of that
complement. The same full-basis calculation in dimension `k` gives
`a_k dh`, where `dh` is probability Haar measure on `H`. Fubini in
these successive Gram blocks now gives, for any measure `m` on `G`
whose frame law is bounded by the frame-fibre measure,

\[
 m*(2^{-\rho}du)*(a_k\,dh)\le a_r\,dg.
\]

Equivalently,

\[
 m*dR_0\le 2^\rho\frac{a_r}{a_k}\,dg
       =\frac{\operatorname{vol}U(r)}
              {2^{\rho+1}\operatorname{vol}U(k)}\,dg,
\]

because `r=k+2rho+1`. Apply this to the open-cell frame law calculated
above. Dividing its factor `2pi^k/(2^n(k-1)!)` by the displayed ratio
gives exactly `c_G` in (12). Restricting to the open cell accounts for
the inequality; Tonelli extends the result from compactly supported
functions to all nonnegative measurable functions.

If `Q` consists of matrices bounded by `P` with `Delta>=c>0`, (12)
implies, for left-`UH`-invariant `h>=0`,

\[
 \int_Q\int_{H\times U_0}h(\gamma_Z(uh)^{-1})d\mu_c\,dZ
 \le(2P^2)^{2n^2}\int_{U\backslash G}h(g)dg.
 \tag{13}
\]

To see the additional factor, insert a measurable cutoff whose integral
along `U_0` is one, apply (12), and unfold along `U`. If `Z` and its
translate by `u in U` both lie in `Q`, the matrix induced by `u` on the
frame has entries bounded by `||Z|| ||Z'^{-1}||<=P^2`. Its strictly
upper triangular complex entries parameterize `U_0\U`. Their box
volume is at most `(2P^2)^(n(n-1))`, which is no larger than the factor
in (13). This also explains why no finite volume for the full
noncompact frame fixer is being asserted.

## 4. A sharper Sobolev restriction

The following elementary version keeps the length of the interval in
the derivative term. If `g:[0,epsilon]->H` is continuously differentiable
with values in a Hilbert space, then

\[
 \|g(0)\|^2\le \frac2\varepsilon\int_0^\varepsilon\|g(t)\|^2dt
                +2\varepsilon\int_0^\varepsilon\|g'(t)\|^2dt.
 \tag{14}
\]

This follows from `g(0)=g(t)-integral_0^t g'`, Cauchy--Schwarz, and
integration in `t`. Smoothness, or absolute continuity with the stated
square-integrable derivative, is required; no unjustified fundamental
theorem of calculus for an arbitrary everywhere differentiable
function is used.

Suppose functions `V_w` are indexed by words over `A` letters, and each
coordinate derivative has norm at most `Lambda sum_a ||V_aw||`.
Iterating (14) in `d` coordinates and using Cauchy--Schwarz on the
letters gives

\[
 \int\|V_\varnothing(0,\omega)\|^2d\omega
 \le\{2/\varepsilon+2\varepsilon(A\Lambda)^2\}^{d}K,
 \tag{15}
\]

provided the integral over the cube and `omega` of every squared norm
with word length at most `d` is bounded by `K`. Each iteration either
keeps the word or appends one letter, so exactly `d` derivative orders
suffice.

Apply this to a family on `G` whose derivative along a curve with
right logarithmic speed `C` has norm at most
`Lambda C sum_a ||V_aw||`. Suppose `A Lambda<=P^44`, `P>=8r`, and that
the entire ball `B(Z,P^-6)` satisfies (1) and `Delta>=c>0`.
Use ordinary real and imaginary matrix-entry coordinates, in which
the coordinate vectors have norm at most `P^2/4`. Put

\[
 d=2n^2,\qquad\varepsilon=P^{-129}.
\]

This cube lies inside `B(Z,P^-6)`: the coordinate map has norm at most
`2n^2`, and `P>=8r`. On `||u||<=P^20`, (11) changes the derivative
constant to `Lambda P^85`, so that `A Lambda P^85<=P^129`.
The one-coordinate factor in (15) is at most `4P^129`.
By (13), the cube integral is bounded by `(2P^2)^d K_0` if
`||V_w||_{L^2(U\G)}^2<=K_0` for `|w|<=d`. Therefore

\[
 \int_{\|u\|\le P^{20}}
   \|V_\varnothing(\gamma_Z(uh)^{-1})\|^2d\mu_c(h,u)
 \le P^{264n^2}K_0,
 \tag{16}
\]

because `(4P^129)(2P^2)=8P^131<=P^132`.

### Theorem 3: restriction of a Bessel convolution

Assume (7), `P>=8r`, and the ball hypotheses just stated. If `phi` is
integrable, square-integrable, and supported on `||y||<=P^20`, then

\[
 \int_{\|u\|\le P^{20}}
 \left\|\int_G\phi(y)W(\gamma_Z(uh)^{-1}y)dy\right\|^2d\mu_c(h,u)
 \le P^{268n^2}\frac{\|W\|_{L^2(U\backslash G)}^2}{d_\pi}
                  \|\phi\|_{L^2(G)}^2.
 \tag{17}
\]

**Proof.** Set `R=P^20`. For a letter `((a,b),c,d)` multiply the weight
`phi(y)` by `(y^-1)_ad y_cb/R^2`, and for a word take the product of
these factors. Each factor has absolute value at most one on the
support, since `||y^-1||=||y||`. Pair that weight with the derivative
`W_w` using the matrix-unit subword. Differentiating `g -> W_w(gy)`
conjugates the right logarithmic derivative by `y`; its entries are
exactly the four-index factors above. Thus the family has `r^4` letters
and derivative constant `R^2=P^40`, with `r^4 P^40<=P^44`.

Every weight has `L^2` norm at most `||phi||_2`. Proposition 2 bounds
the squared quotient norm of every word of length at most `2n^2` by
`K_0=P^(4n^2) ||W||_2^2 ||phi||_2^2/d_pi`. Equation (16) proves (17).
Boundedness of the original derivative functions and domination by
`|phi|` justify differentiating these weighted integrals. QED.

The exponent improvement is an analytic argument, not a numerical
experiment. It preserves the source measure, support radius, derivative
order and parameter hypotheses. It does not estimate the inverse of a
theta projection.

## 5. Integral frame rigidity and weighted packing

We now list the arithmetic data used by the return argument. This
separates those data from a claim about arbitrary discrete subgroups.
Let `E` be CM and let the rational middle space be positive definite off
the negative vector `z`. Class representatives act in the positive
middle space. A term over classes `(c,d)` is a rational isometry whose
matrix between their prescribed lattice bases is integral with a fixed
finite reduction. The following quantitative conditions are used:

1. `b>=1000`, `n>=23`, `N<=b^(60n)` and `n<=b`.
2. The frame products `<f_a,g f_b>` and upper-frame entries of a term
   are algebraic integers. The normalized real basis has frame-scale
   ratios bounded below by `b^(-23rho)`.
3. The rational unipotent congruence group acts on the frame through
   the full upper unitriangular group with off-diagonal entries in
   `M O_E`; its kernel is the subgroup fixing the frame. The scaled
   residue representatives can be chosen so that reduced
   Gram--Schmidt triangular coefficients have modulus at most `b^26`.
4. The cutoffs `beta_d` are nonnegative, have sum one over that
   rational unipotent group, and are supported on these reduced
   points.
5. The definite class level is the pullback of the same principal
   congruence level, and its rational class stabilizers are trivial.
   This is the free-level condition proved in
   [the finite theta chapter](lsernau-common-theta-finite.md): at the
   chosen odd degree-one prime the principal congruence subgroup is
   torsion free, whereas a definite rational class stabilizer is
   finite.
6. The product of the real Bessel characters is trivial on each
   rational class-unipotent congruence subgroup. In the specified
   automorphic data this follows from the global additive character
   being trivial on `E` and the finite-character compatibility at the
   principal level. Thus the full product Bessel function, with its
   prescribed finite indicator, is invariant under that rational
   subgroup. A left transformation law by an arbitrary character
   would not suffice for the grouping argument below.

These are the explicit finite-level and reduction hypotheses used in
the source's admissible filling system. Existence of the whole common
family of scales is still a separate global construction. In
particular, we do not infer condition 3 from discreteness alone.

Here is the reduction behind conditions 3 and 4. An integral element
`tau` with `tau+bar(tau)=1` exists when `E` contains the third roots of
unity. For an isotropic `x` and `u perpendicular x`, the Eichler map

\[
  I+x u^*J-u x^*J-\tau\langle u,u\rangle x x^*J
 \tag{18}
\]

preserves `J`; expanding the product uses `x*Jx=x*Ju=0` and cancels
the remaining terms by `tau+bar(tau)=1`. Taking appropriate multiples
of lattice vectors makes (18) congruent to the identity and gives the
elementary upper-frame operations. Reducing the triangular coefficients
in succession by a half-open fundamental domain of `M O_E` gives
exactly one coset of the frame-fixing kernel. A measurable partition
for that kernel, multiplied by the reduced-point indicator, gives
`beta_d`. The numerical radius of the fundamental domain is the
quantitative part of condition 3; it must be checked for the chosen
field and level.

Let `ell(g)=inf_{s in UH}(||s g||+1)`. Gram--Schmidt diagonal lengths
are unchanged by upper unitriangular frame operations and bounded by
`ell(g)`. The reduced triangular coefficients give
`||g^-1 f_a||<=n b^26 ell(g)<=b^27 ell(g)`. Thus if `beta_d(g)!=0` and
`ell(g)<=b^(6n+2) R`, the frame is in the ball of radius

\[
 \rho_R=b^{37n}R.
 \tag{19}
\]

### Proposition 4: separation

Two distinct rational frame images contributing to the same fixed
source class, with both transformed points satisfying (19) and the
length bound, differ in the product norm over the real places by at
least `(N rho_R)^-1`.

**Proof.** Compare the two points using their quotient isometry `g`.
If every frame displacement is smaller than `(N rho_R)^-1`, each
embedded difference
`<f_b,g f_a>-<f_b,f_a>` has modulus below one, by Cauchy--Schwarz and
the frame normalization; the bound is `N rho_R` times the displacement.
The difference is an algebraic integer. A nonzero algebraic integer
cannot have modulus below one at every archimedean place, because its
nonzero integral norm has absolute value at least one. All these Gram
differences are therefore zero.

The dual-isotropic and `z` coordinates of `g f_a-f_a` vanish. Its
positive middle part has norm zero by unitarity, and hence vanishes.
Only its coordinates along `e_1,...,e_rho` remain. Descend through
those rows. Once later rows vanish, an upper unitriangular reduction
isolates the current row. Its integral coefficient has, at every
embedding, absolute value at most

\[
 b^{23\rho}b^{6n+2}R\cdot\text{frame displacement}
 \le b^{37n}R\cdot\text{frame displacement}<1.
\]

It too is zero. Thus `g` fixes the entire frame, a contradiction. QED.

Give the tuple space the maximum of the Euclidean column norms over
all frame columns and all archimedean places. The estimates above use
this norm; no conversion to a summed Euclidean norm introduces a
factor depending on the number of places. The volume-packing argument
works for the balls of any fixed norm, since their volumes scale by
the `D`-th power of the radius.
The real dimension of the full tuple space is `D=2nrf`. More generally
use `D=dim_R V` if all differences lie in a subspace `V`. Translate
one frame tuple to the origin. The tuples have norm at most `2rho_R`
and separation at least `(N rho_R)^-1`. Disjoint balls of half the
separation fit in the ball enlarged by that half-radius. Hence their
number is at most

\[
 (1+4N\rho_R^2)^D
 \le (K R^2)^D,\qquad K=1+4N b^{74n}.
 \tag{20}
\]

This is valid also for `D=0`, when there is at most one frame image.
It does not count all rational elements: those with the same frame may
be infinite in number. Here is the class-fibre argument. Two terms of
the same finite reduction and source class have quotient in the
principal congruence relation between their target classes. If their
frame images agree, that quotient fixes `F`; its Levi component is an
isometry of the positive middle space and its other component lies in
`U_0`. Reading the middle diagonal block of the integral level relation
shows that this Levi component identifies the two definite class
representatives modulo the definite class level. Thus the target
classes agree. The Levi component is now a rational class stabilizer,
so condition 5 makes it the identity. The quotient therefore belongs
to the frame-fixing congruence subgroup of that one target class.
Fixing one term identifies all terms in this fibre with a subset of
one coset of that subgroup. Their cutoff weights sum to at most one,
by condition 4. Thus (20) also bounds the *weighted* number of terms.
This argument is the ordinary block-matrix proof of the source's
`eq_and_mem_classUnipotent_of_besselS` in
`BesselLevelStructure.lean`, lines 825--855, followed by the frame-fixer
condition. An unweighted packing assertion for all rational elements
would be false; without condition 5 a stabilizer multiplicity would
also have to be retained.

Since `N<=b^(60n)` and `b>=5`,

\[
 K\le5b^{134n}\le b^{134n+1}\le b^{6n^2}\quad(n\ge23).
 \tag{21}
\]

Keeping the middle bound avoids the unnecessary quadratic exponent in
the last expression.

## 6. Layer summation, absolute returns and the cutoff error

For each term let

\[
 L(g)=\prod_{v\mid\infty}
       \max\{1,\ell(g_v)/b^{6n}\},\qquad i=r^3 f.
\]

The preceding argument says that the total cutoff weight with `L<=R`
is at most `K^D R^(2D)`, uniformly in the point being returned and in
the chosen subset of rational terms. For any `a>2D`, Tonelli gives the
exact useful estimate

\[
 \sum_t\beta_t L_t^{-a}
 =a\int_1^\infty R^{-a-1}
                 \sum_{L_t\le R}\beta_t\,dR
 \le\frac{a}{a-2D}K^D.
 \tag{22}
\]

There is no extra atom at `L=1`: the displayed integral representation
already includes it. With `a=i` and `r^2>8n`, the right side is at most

\[
 C_{\rm ret}=2K^{2nrf}
 \le2b^{(268n^2+2n)rf}.
 \tag{23}
\]

The source's weaker `2b^(12n^3rf)` follows from the last bound in (21).

Suppose each real Bessel function `W_v` and its archimedean truncation
`W_v^cut` have a left-invariant majorant `w_v`, bounded by `A_v`, such that

\[
 \max(1,\ell(g)/b^{6n})^{3i}\|W_v(g)\|\le w_v(g),
 \qquad
 A_v\int_{U\backslash G}w_v\le b^{400r^2}\dim V_v.
 \tag{24}
\]

The same weighted inequality is required for `W_v^cut`. Require also
`W_v^cut(g)=W_v(g)` whenever `ell(g)<=b^(6n+1)`. This is the source
cut-pair support condition and is a separate hypothesis from (24).
It supplies the length gain whenever one of the two kernels differs
from its truncation.

The earlier Bessel and stationary-period chapters give this majorant
with their stated coefficient hypotheses; their sharper exponent can
be retained, but is not needed here. Let `nu_U` be the actual
unipotent covolume. Equations (22)--(24) imply:

* The sum of the norms of the cut Bessel seeds over rational translates
  is bounded uniformly in the adelic point, by
  `C_ret product_v A_v`.
* For each fixed source class and finite reduction, the sum over target
  classes and rational terms of the absolute two-seed amplitude
  integrals is at most
  `nu_U C_ret b^(400r^2 f) product_v dim V_v`.

For the first statement at an arbitrary finite adelic point, if no
rational translate meets the specified finite-level support the sum
is zero. Otherwise choose one such translate `delta`. Express every
other contributing translate relative to it as `gamma^-1 delta`.
The quotient `gamma` belongs to the fixed relation `termsOver(c,1,c)`;
apply (22) at `y=delta_infinity g_infinity`. The prescribed finite
character factor has absolute value at most one. This reduces the
uniform bound to the already proved fixed-class return estimate,
without an extra number of finite cosets.

For the second statement, reserve the target length power `i` for
(22), bound its majorant by `product A_v`, and unfold the source
cutoff against `product w_v`. Its integral is `nu_U product integral
w_v`, so (24) gives the displayed bound. All sums are nonnegative;
Tonelli justifies each interchange.

For the difference between the full kernel and the truncated kernel,
at least one argument lies outside the cut. Consequently
`L(y)L(gamma^-1 y)>=b`. Reserve powers `2i` at these two arguments and
use their product to obtain `b^(-2i)`. The tensor difference has two
terms. The absolute integrated difference is therefore at most

\[
 2\nu_U C_{\rm ret}\,
 b^{400r^2f-2r^3f}\prod_v\dim V_v.
 \tag{25}
\]

For the source numerical range

\[
 k\ge12n^3+500,\quad r\ge k+1,\quad n\ge23,\quad
 \prod_v\dim V_v\le b^{2kf},
 \tag{26}
\]

(25) is at most `nu_U b^(-k^3 f)/2`. Here is a direct check of the
margin. Set `A=268n^2+2n`. For `n>=23`, `A<=12n^3<=k`, so
`Ar<=r^2`. Since `r>=501`,

\[
 Ar+400r^2+2k+1\le401r^2+2r+1\le r^3.
\]

Together with `k^3<=r^3`, this gives
`Ar+400r^2+2k+k^3+1<=2r^3`. Finally `8<=b` absorbs the factor eight
arising from (23), (25), and the desired half. All field factors are
multiplied by the same positive integer `f`; `f>=1` suffices for this
last absorption.

## 7. Poincare series and the boundary of the result

For a class-coordinate pair `a=(c,i)`, define its arithmetic cut seed
by `F_a(g)=beta_c(g_infinity) W_i(g_infinity)` times the prescribed
finite-level indicator and its specified finite character factor.
Here `W_i` is the **full** product Bessel function, not its
archimedean truncation. The first consequence of
(24) proves absolute pointwise convergence and a uniform bound for

\[
 P_a(g)=\sum_{\gamma\in G(E)}F_a(\gamma g).
\]

Because the adelic quotient has finite volume,
`integral_G |F_a| = integral_[G] sum_gamma |F_a(gamma g)| < infinity`.
Hence the usual unfolding against bounded automorphic forms is
absolutely justified. Group the sum by the rational Bessel unipotent
subgroup. By condition 6 the full Bessel function and finite factor
are invariant under this subgroup, whereas the cutoffs sum to one.
Consequently the cutoff disappears from each grouped term, which is reproduced
by the integrable kernel `e`. The uniform bound permits convolution
to pass through this grouped sum, so `P_a*e=P_a`. It has the prescribed
finite level and is in `L^2([G])`.

If `e` is a cuspidal kernel, convolving with it gives zero constant
term along every proper rational parabolic. Its smoothness follows
from the compact reproducing bump. Thus these are the required smooth
cuspidal forms in the finite-level discrete-series type. The
class-return Petersson identity in the
[global cut chapter](lsernau-global-cut-unfolding.md) now has the
absolute convergence it needs, under the explicit coefficient and
filling hypotheses above. The same domination proves its translated
versions and finite linear combinations.

This is an absolute return theorem and a small *truncation error*.
It is not the main second-moment theorem. It does not prove that the
return operator is close to the identity, that the Poincare map is
injective, or that its image has the desired multiplicities. Those
questions require the separate identity, open-cell, terminal-fixer and
remaining-orbit estimates. Likewise, supplying an actual noncompact
theta edge still requires the normalized projection/rigidity package
identified in [noncompact real edges](lsernau-noncompact-real-edges.md).

## Source correspondence and verification scope

All source references below use readable revision
`72fead102f663d5c7a407964a13dc0cf9d977207` of
[lsernau/grh-lean](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).

| Ordinary argument | Source file and bounded range | Blob |
| --- | --- | --- |
| Filtration/Casimir norm | `Lib/DiscreteSeries/Rigidity/HighestVectorsAndFiltration.lean`, 387--468 | `e9814b21cc102732e5840c7d160de1cce92df4cc` |
| Derivative kernels and Schur | `New/Spanning/Bessel/SchurBound.lean`, 74--102, 160--235, 290--343 | `8a82cd08e213dd8f2b223a783540f244a643207b` |
| Explicit section and derivative | `New/Spanning/Bessel/GramSection.lean`, 54--109, 214--335, 337--474 | `7381aac703e8ed68c835668815e92a77293b294b` |
| Full-basis Gram-fibre normalization | `Lib/DiscreteSeries/Haar/GramPolar.lean`, 175--265, 395--423 | `bc00b082dac2e2ed2eadd0bc668b00380bfff209` |
| Compact geometric constants and probability Haar | `Lib/DiscreteSeries/Haar/TotalMass.lean`, 258--337 | `4289dee7a570390e9eb602cca41c1cf43731c4c3` |
| Appending dual and definite columns | `Lib/DiscreteSeries/Bessel/FrameFibre.lean`, 80--153, 199--326 | `f81bfa5ab77ea641c82fe2854a1f57a575a3f46e` |
| Gram-cell density | `New/Spanning/Bessel/MeanValue.lean`, 224--374, 482--618 | `41a4e2433549dd8ac7c6cc6331522fb182752308` |
| Source restriction estimate | `New/Spanning/Bessel/SobolevBound.lean`, 137--470, 471--end | `fca27bc6b132edb9304a806935ee50dc4b1e2ba3` |
| Reduced unipotent representatives | `New/Spanning/Unfolding/ReducedPoints.lean`, 60--78, 308--390, 470--end | `6ea7eaab5c878b31821105929f8bca43231feb39` |
| Frame rigidity and weighted packing | `New/Spanning/Unfolding/Packing.lean`, 147--514 | `53f793ccd01b0d3bbf28694c2a2be1ba1307b269` |
| Layer sums and absolute amplitudes | `New/Spanning/Unfolding/AmplitudeSums.lean`, 178--279, 317--631 | `5c7c88d7c976f2362a00b87e69b7957e104efe80` |
| Poincare construction | `New/Spanning/Unfolding/PoincareSeries.lean`, 255--587, 711--797 | `add48906ac75b2c9935dcf0bbb70ec843ae67150` |

The proofs above are mathematical reconstructions with explicit input
boundaries. No new Lean replay is claimed. In particular, neither an
ordinary proof of the general large-gap discrete-series package nor
the full spanning moment theorem is being claimed by listing their
source files.
