# Divisor upper order from monodromy and the shortest period

This replaces the Hilbert--Samuel jet estimate in the *horizontal*
normalized-blow-up certificate by an elementary inequality on the
monodromy lattice and the already established thin Bergman theorem.
It does not assert the corresponding vertical valuation theorem.

## 1. A dimension-free inequality for the actual phi_C

Let X be a nonzero finite torsion-free O_E-module, E a CM field of
degree 2f and root discriminant R. Let beta be a positive definite
real symmetric bilinear form on X_R with the conjugate-adjoint
O_E action. Let phi_C(beta) be the infimum over linear functionals
l that are integral on integral conjugate-adjoint symmetric forms
and strictly positive on the nonzero positive semidefinite cone,
as in the source. For the ordinary Z-dual X^* put

    mu^2 = min_{0 != eta in X^*} beta^(-1)(eta,eta).

Then

    2f/(R^2 mu^2) <= phi_C(beta).                     (DA1)

In particular no rank-dependent transference factor is needed.
This is a direct alternative to the successive-minima argument
in PhiCMinK for this particular consequence.

Proof. Fix an admissible l. The subspace of conjugate-adjoint
symmetric forms is rational in integral coordinates: its defining
linear equations have integer coefficients. Its integral lattice
is saturated in the full lattice of integer matrices. Therefore
l extends to an integer linear functional on all integer matrices
(extend a basis of the saturated lattice), hence can be written

    l(G) = sum_i G(x_i,x'_i)

for x_i,x'_i in X, absorbing integer coefficients and signs in
the first variable. This is the elementary content of PhiCTie.

For a nonzero eta in X^*, trace duality gives a unique E-linear
h:X_Q -> E with eta(x)=Tr_E/Q h(x). Indeed, for each x use the
functional a -> eta(ax) on E; nondegeneracy of the trace makes
its representative unique and E-linear. For x in X and a in
O_E this trace is integral, so h(X) is contained in the
codifferent d^(-1).

Write eta_sigma(x)=sigma(h(x)) and extend these covectors real
linearly. Set

    P_eta(x,y) = sum_sigma Re(eta_sigma(x) conjugate(eta_sigma(y))).

Every summand is a nonzero positive semidefinite conjugate-adjoint
form (choose x with h(x) != 0); hence l is positive on each one.
For the element

    z = sum_i [h(x_i) conjugate(h(x'_i))
                 + conjugate(h(x_i)) h(x'_i)]

we have z in d^(-2), and every sigma(z) is twice the positive
value of l on the corresponding summand. Thus z is totally
positive in the real subfield and nonzero. The fractional-ideal
norm bound and AM--GM imply

    2 l(P_eta) = Tr_E/Q z
        >= 2f |N_E/Q(z)|^(1/(2f)) >= 2f/R^2.          (DA2)

This is exactly the lower_bound mechanism of PhiCMinI, where
Pm(eta,eta)=2P_eta.

Now decompose X_R into its real CM embedding blocks using beta:
distinct conjugate pairs are mutually orthogonal and on each
block the complex structure J is orthogonal. The real covector
eta restricted to a block is eta_sigma+eta_barsigma. If its real
restriction is alpha, then eta_sigma=(alpha-i alpha∘J)/2.
Consequently the contribution of that pair to P_eta is

    (alpha ⊗ alpha + (alpha∘J) ⊗ (alpha∘J))/2.

The two representing vectors of alpha and alpha∘J are
orthogonal and of equal beta-length. Bessel's inequality on
each block, and then the orthogonal direct sum, give

    P_eta <= (beta^(-1)(eta,eta)/2) beta

in the cone of conjugate-adjoint forms. Applying l and (DA2)
gives l(beta) >= 2f/[R^2 beta^(-1)(eta,eta)].
Choose a shortest nonzero dual covector and take the infimum
over l. This proves (DA1). The argument uses the ordinary
integral dual, not an E-dual with an unspecified different.

## 2. Shortest periods on an actual logarithmic arc

Use the principally polarized period normalization of
geometry-bergman-continuation-thin.tex. Consider a transverse
complex arc with parameter t, nonzero toric rank a, and put
L=log(1/|t|). Its adapted integral symplectic period coordinates
are u+tau(t)v for integral vectors u,v in Z^g. The real-period
lattice in the vanishing directions is the ordinary integral
dual of the torus character/monodromy lattice X, and in that
basis the log-period matrix is

    Y(t)=Im tau(t)
        = (L/(2pi)) diag(beta,0) + O(1).              (DA3)

The finite residual imaginary block is positive definite.
Here beta is the actual monodromy form in the same normalization
as HasPhi, not a matrix chosen up to rational isogeny.

Recall the normalization check. In the toroidal character chart
the multiplicative pairing has entries q_ij=t^(beta_ij) times
holomorphic units. They have logarithms tau_ij=(log q_ij)/(2pi i)
up to bounded choices of the abelian part and a fixed period
branch. The quadratic exponent in the source is Q, with
Q(x)=beta(x,x)/2; polarization of the quadratic generator
psi gives the pairing tauVal(x,y)=psiVal(x+y)/(psiVal(x)psiVal(y)).
Thus the exponent is beta(x,y), not Q(x) and not 2beta(x,y).
This is also the content of q_eq_of_hasArcData on a trait,
with the positive ramification factor w if the arc parameter
has valuation w. Principal polarization identifies the
vanishing real periods with Hom_Z(X,Z); using a finite-index
isogeny instead would invalidate the shortest-period conclusion.
The hypotheses here are the exact toroidal chart/period
identifications, with the actual algebraic character lattice.

In this normalization the squared Hermitian period length is

    (u+Re(tau)v)^T Y^(-1) (u+Re(tau)v) + v^T Y v.

The uniform positive lower bound for Y from the fixed-reference
metric argument shows that periods with v != 0 have a fixed
positive lower length. A fixed nonzero integral u supported
in the vanishing block has length squared O(1/L), so a shortest
period for small t must have v=0.

For u=(u_T,u_A) with u_A != 0, the block inverse inequality

    u^T Y^(-1) u >= u_A^T (Y_AA)^(-1) u_A

follows by minimizing the left side over u_T. The finite block
Y_AA is uniformly bounded above, so these vectors again have
a fixed positive lower length. For the remaining u=(eta,0),
the Schur complement of the finite residual block is

    (L/(2pi)) beta + O(1).

Its inverse equals (2pi/L) beta^(-1) with relative error O(1/L),
in Loewner order. This last estimate is simultaneous for *all*
integral eta; it is not just pointwise convergence for a
preselected period. Taking the minimum therefore proves

    L lambda(t)^2 -> 2pi mu^2,                        (DA4)

where lambda is the original shortest period and mu is as in
(DA1). If a=g, omit the finite block. If a=0, all period lengths
are bounded below and the needed normalized limit is zero.

The actual thin Bergman parameter is
Phi(x)=2f/(R^2 lambda(x)^2) in the thin region and zero in the
thick region. By (DA1)--(DA4),

    limsup Phi(x(t))/L <= phi_C(beta)/(2pi).            (DA5)

In particular this implies the factor-six bound requested in
LW8, with a much stronger constant. It also gives an upper
bound stronger than the original phi/2500 after applying LW8.
The 2pi in (DA5) corresponds to the standard symplectic
normalization in which Im H is integral unimodular and the
multiplicative period is exp(2pi i tau); one must not insert
an unrelated rescaling of the Hermitian metric.

## 3. Application to the finite divisor certificate

At a general smooth complex point of a prime divisor D of the
normalized blow-up, choose a transverse disk. In a toroidal
chart, after an etale splitting if necessary, the finitely
many monomial generators have exactly their generic divisorial
orders on the disk: write each as a power of the divisor's
local equation times a unit and avoid the zero loci of those
units. The same holds for their multiplicative polarization
pairings. Thus the divisor and disk monodromy forms agree.
A ramified change of parameter multiplies both beta and the
section orders by the same ramification factor; phi_C is
positively homogeneous. This verifies the specialization
argument whenever the actual toroidal trait and analytic
period data are linked by the above identifications.

The extending tangent metric has eigenvalues and inverse
eigenvalues bounded by powers of 1+L, by (DA3), its uniform
positive lower bound and the extending invertible tangent
frame. Its exterior powers and induced metrics on an extending
flag or quotient, and the fixed powers of their determinants,
have the same property: compare the positive forms in a fixed
smooth local frame before taking exterior powers or quotients.
Consequently logarithms of the actual weight-line norms in
nonvanishing extending frames are O(log(1+L)), also for
negative fixed weights. The fixed flat factors have the same
property under their original extending metric pins. This
is the sublogarithmic metric requirement of LW8.

Let b_D be the base-ideal order, phi_D=phi_C(beta) in the
normalized divisorial parameter. The full original Bergman
lower bound exp(-Phi/625) and the transverse-arc calculation
in LW8 now imply

    b_D <= phi_D/(2500 pi) <= phi_D/2500.              (DA6)

Thus, combined with the section of
geometry-reference-metric-and-theta-divisor.md having
ord_D theta >= 8 phi_D/625, the divisor inequality is

    div(theta^3) >= 8 E_base.

At interior divisors use the established thick/interior
nonvanishing theorem. No additional cusp jet-count estimate
is required for the horizontal comparison. The weight
calculation remains exactly the one in that note. All estimates
are on one fixed component and model; there is no appeal to
uniform compactness over the moving arithmetic family.

## Pinned source and remaining application checks

The CM functional argument is independently derived above from
the source PhiCTie and PhiCMinI. Its precise trace and different
constants agree with those files. The same monodromy
normalization is visible in the following pinned files at
jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de
(all relative to lean/src/):

- Formalism/SharpRestriction/Divisibility/GeneratorPowers/
  PhiCTie.lean, PhiCMinI.lean and PhiCMinK.lean.
- Development/AbelianVarietyTheory/Definitions/Foundations/
  NonnegOfMemCStarSet.lean (HasPhi).
- Development/AbelianVarietyTheory/Proofs/DegenerationProofs/
  ArcDataPsiValuationEqHalfForm.lean
  (psi_value and q_eq_of_hasArcData: Q(e y)=w*a.be(y,y)/2).
- Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/
  ExistsRingHomLift.lean (tauVal, logarithm with 2pi i);
  ExistsSymplecticCoordinatesOfIsPeriod.lean (symplectic
  integral periods); EqZeroOfSumSq.lean (tt_eq_im_mul,
  with rank-one hypothesis only).
- Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/
  PullbackModelArcPeriod.lean (q_eq, exists_form, order_of_arcWit);
  PhiDivisorBaseChangeBlowup.lean (trait lifting to the blow-up).

This proves the numerical monodromy comparison and the divisor
certificate implication on a compatible principally polarized
toroidal arc. The remaining verification is that *every* actual
horizontal base divisor admits the source-linked toroidal
character chart, integral dual period identification and unit
flag frames used here, and that the lower theta product's
key/flat/centered pins hold on those same models. The source
rank-one tt_eq_im_mul alone would not prove the all-rank
claim; (DA1)--(DA4) are the all-rank replacement. No assertion
about vertical residue-characteristic cusp orders, full W10,
or Lean replay is made.
