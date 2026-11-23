# Arithmetic degree of the original component cusp lattice

> **Later status (23 November 2026).** Independent mathematical review and manuscript integration are recorded in the [joint review](../certificates/rigidity-section-orbital-review.json). This theorem supplies the component degree estimate, **not** the all-point height/rank budget. The [corrected tangent-fibre theorem](geometry-hodge-specialization.md) is also now supplied; consult [current state](current-state.md).

## Frontier theorem and status

The smallest remaining section-degree supplier was the original
component estimate HSClaimS26, with its actual lattice, component
Petersson norm, divided weights, image height and coefficient
J=DP(kappa/T+1). The proof in
paper/shared/geometry-section-continuation.tex supplies it by applying
the existing polynomial determinant theorem to the actual geometric
spaces. Its stronger conclusion is linear in the signed image height.

Classification: **closed obligation: the actual component arithmetic
section estimate**, independently reviewed and integrated; see
[the joint review](../certificates/rigidity-section-orbital-review.json). This is a supplier inside W10, not completion of W10.
The all-point corrected-height comparison, final mean-height/rank
comparisons and any still unconstructed numerical family remain.

The route does not construct integral lifts of arbitrary jets or
algebraic points of controlled height. Those stronger assertions are
unnecessary for this component section estimate.

## Construction on the same spaces

Let X be the original smooth projective toroidal full flag component
over its original totally complex field K, with reduced boundary B.
Its prescribed canonical identity is omega_X(B)=L(kappa_can).
The exact cusp space is H0(X,L(a)(-B)); analytic-algebraic toroidal
comparison identifies the subcanonical extension with the original
holomorphic cusp reading. Dominance, finite infinitesimal character,
moderate growth and compact center are retained in the rapid-decay
comparison. Generic boundary divisors suffice for extension because
X is smooth and hence normal.

Resolve the two ORIGINAL cusp base ideals over K, by a smooth
projective modification pi:Y→X which is an isomorphism on the
interior. If F1,F2 are their exact fixed divisors, set

~~~
L = pi*L(u1)(-F1),
L2 = pi*L(u2)(-F2),
A = pi*L(u2 + D u1),
div(e) = F2 + D F1.
~~~

The first two lines are generated and birational, hence nef and big.
The already proved strict-gap positivity gives the same for A.
The section e belongs to A L2^(-1)L^(-D) and is nonzero on the
interior. No height or norm of e is needed.

The equality pi_*omega_Y=omega_X is proved directly: pi is an
isomorphism at every codimension-one generic point of smooth X;
regular top forms extend across codimension at least two on X.
Their pullbacks are regular on smooth Y because the Jacobian has
regular coefficients. Thus the original spaces
V_j inside sections of omega_Y A L^j contain all global sections,
with equality at j=0. Multiplication by the fixed-divisor section
at level j proves the inclusion for j>0. This supplies exactly the
previous geometric-filtration theorem.

The original integral lattice and each Petersson norm are transported
by the prescribed canonical identification; a different lattice of
integral global sections on Y is never substituted. Products stay
integral at every original integral test object, and pointwise
metric multiplication plus the actual upper Bergman bound gives
the original multiplication operator norm sqrt(beta).

## Height and degree normalizations

For the irreducible Chow form f of the original image, let H(f) be
its normalized finite Gauss height after substitution by the entire
integral frame, plus its intrinsic Hermitian spherical mean. Then

~~~
h = H(f)/((D+1)delta) + (1/2) sum_{i=1}^{N-1} 1/i.
~~~

This is the ORIGINAL component height definition. It requires no
point-height estimate. Two full integral frames express one another
by integral matrices, giving equality of their finite Gauss norms.
Coordinate changes with their transported Gram matrices preserve
the same Hermitian spheres. The product formula cancels the scalar
ambiguity of the Chow form.

For a=[K:Q] and rank d, the original degree is

~~~
deg_n M = -log(covol M)/a - (d/2)log2 + (d/2)log rd(K).
~~~

The covolume takes one complex embedding per conjugate pair and its
underlying real Euclidean measure. Equivalently this is the normalized
negative logarithm of the determinant ideal and Gram determinants.
The source's squared-norm slope is twice deg_n M/d.

## Literal downstream bound

Put q=binom(T-1,D)delta, theta=q/d,
c=log(n Lambda)+(log n+1)/2 and a_n=(log n+1)/2. The supplied result is

~~~
deg_n M(a_T)/d
 >= theta [T h - T a_n - D(D+1)c - log Lambda0 - T log beta/2]
    -(1-theta)[T c + T log beta/2 + log LambdaD + log LambdaT].
~~~

The original component constants are
Lambda0=exp(DP(kappa/T+1)) and LambdaD=LambdaT=exp(Pkappa).
The direct degree bound therefore retains J=DP(kappa/T+1).

With rho=log Lambda+26 log(n D delta(2+|h|+log Lambda)),
one has c≤rho. The elementary inequalities displayed in the proof
give the exact HSClaimS26 consumer with z=1-theta, including every
rank factor and the factor one-half on log beta. The stronger
bound also sums over components with only their original signed
weighted mean height; no separate absolute-height moment appears.

## Pinned source interfaces

Every module is pinned to
jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.
The certificate records full source and bounded-range hashes.

* Definitions.Divisors.BarCompSubsetClosure86–121:
  exact u1,u2 and a_j=kappa_can+u2+(D+j)u1.
* Definitions.Divisors.ExistsResolProjSpace181–220,231–264:
  exact two base ideals, lines A,L,L2, section e and product transport.
* Definitions.Divisors.NonemptyCuspFrame118–194:
  actual global inclusions, equality at zero, lattice membership and
  every original Petersson norm under the same section identification.
* Definitions.Divisors.PointHeight27–35:
  frameNorm(A,x)=||A^(-1)x|| and the original spherical/finite
  formHeight with the harmonic correction.
* Definitions.Divisors.AevalEqZeroOfMemConeIdeal220–269:
  full-frame, image-height and presentation definitions.
* Definitions.Divisors.IsHomogeneousCompIdeal152–165:
  original component degree and height are precisely those definitions.
* Proofs.DivisorProofs.FormHeightEqHt16–25,41–77 and
  IsImageHeightUnique403–472: exact height equality and frame invariance.
* Proofs.DivisorProofs.DegreeSupLatticeComponentEq17–109:
  original real covolume, squared slope and lattice/metric degree transport.
* HodgeBundleWeights.ExistsWeightHodgeBundleGenerated22–53,
  HodgeBundleSandwichBound24–53,
  HermitianGeometricHypothesisHolds19–47:
  actual smooth models, canonical identity and supplied nef/big data.
* HodgeBundleWeights.ExistsDegreeParametersBound33–76 and
  ThirdPlaceSeries.ExistsDegreeParametersBound34–70:
  exact h0,hsh and original component consumer.
* LogMeanStatements.HSClaim7–22 and
  Proofs.DivisorProofs.HermitianSystemSlopeBoundOfDeterminantSlopeInequ14–88:
  literal constants and rank factors.

The source's quoted theorem package is not invoked as a black box.
The generic filtration and determinant inequality were already proved
in standard mathematics; the present proof constructs their actual
inputs and checks their exact output.

## Reproduction and limits

~~~sh
python3 scripts/geometry-section-continuation.py --offline
~~~

The checker authenticates the source interfaces and two primary PDFs,
and verifies the Picard-class identities, determinant/covolume
normalization and literal numerical weakening exactly. These checks
supplement the general mathematical proof. They do not build Lean or
construct the still separate numerical family and all-point heights.
