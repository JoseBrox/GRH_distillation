# Normalized theta Hecke transfer and the stable-range critical norm

## Scope and dependencies

The local split calculation of [split transfer](lsernau-split-transfer-and-level-lifts.md)
applies to the actual mixed Weil datum, with the normalization of
[Weil transport](lsernau-nonstandard-weil-transport.md). Here we complete
the passage to the normalized Galois trace on any occurring good
eigensystem, strengthen it to a representation identity, and evaluate
the stable-range rank-one critical norm. We use the classical
stable-range Siegel–Weil input with the measures fixed in
[Rallis inversion](lsernau-rallis-sharp-inversion.md).
The occurrence of an eigensystem in the definite comparison space is
a separate multiplicity input; the present proof does not assume an
attachment theorem for the indefinite group.

## 1. Transfer to the actual theta integral

Write the two ranks as r and n=r+t. At a split finite place w outside
the chosen and twist places and their conjugates, put q=Norm(w),
let a=charW, b=charV, and let

    alpha = a^BC(varpi) upsilon(varpi)^(-r) q^(r/2),
    beta  = b^BC(varpi) upsilon(varpi)^(-n) q^(n/2).

Here BC is composition with x/bar(x); both characters are unramified
at w. These are precisely the source frobValue normalizations. In the
Schrodinger coordinates the finite vector is the integral matrix
vacuum, tensored with the remaining datum. Let

    H_d(X) = sum_i (-X)^i q^(i(i-1)/2) T_{w,i}

for rank d, with unnormalized double-coset sums, and
P_s(X)=prod_{j=0}^{s-1}(1-q^j X).

For a subspace U of k^d, choose an integral matrix A_U with kernel U
modulo varpi and elementary divisors 1 and varpi. Then Y A_U^(-1)
is integral if and only if Y is integral and bar(Y) kills U.
Indeed A_U^(-1) O^d is the preimage of U in varpi^(-1)O^d:
multiply by varpi to check this from elementary divisors. This
also proves the necessity of integrality of Y, without evaluating
a residue matrix for a nonintegral Y. If the dimension of U is i,
its Weil scalar is alpha^i on the transposed target representative
and beta^i on the inverse source representative. This follows by
substituting determinant order i in the split multiplier of the
normalization chapter. Transposes enumerate the target right cosets;
inverse representatives are the source cosets at bar(w), since the
conjugate-place component of a unitary matrix is its inverse transpose.

Summing over U contained in the respective residue kernels therefore
gives, on a datum with integral matrix argument of residue rank h,
P_{n-h}(alpha X) for the target and P_{r-h}(beta X) for the source
at bar(w). The identity used here is

    sum_{U <= k^s} (-X)^dim(U) q^(dim(U)(dim(U)-1)/2)
      = P_s(X).

It follows by counting subspaces relative to a fixed hyperplane:
the Gaussian coefficients satisfy
[s choose i]_q=[s-1 choose i]_q+q^(s-i)[s-1 choose i-1]_q;
substitution gives multiplication by 1-q^(s-1)X.
Both sums vanish off the integral matrix box. Since
P_{n-h}(X)=P_t(X)P_{r-h}(q^t X), the local equality is an equality
of actual Weil vectors, not only of their vacuum matrix coefficients.

For the global theta pairing write B(f,y) for the integral of the
theta kernel with the rapid source vector y, with the fixed real
arrow projection and any fixed scalar normalization. The finite
equivariance is
rho(h)B(f,y)=B(omega(g,h)f, pi(g)y).
This is a change of source integration variable; the character
factors are those already included in omega. In particular
B(omega(g,1)f,y)=B(f,pi(g^(-1))y).
Right and left cosets are interchanged by inversion. On spherical
vectors the transpose of the Hecke sum at bar(w) is the sum at w:
inverse transpose interchanges the conjugate-place matrices, and
the two double-coset decompositions have the same number of cosets.
Equivalently this follows by integrating the compact-bi-invariant
indicator of the double coset, with compact mass one, and replacing
g by g^(-1) in the invariant bilinear pairing. No complex conjugation
of the polynomial coefficients occurs in this bilinear step.
The finite Hecke sums can be taken inside the absolutely convergent
integral. The real arrow projection commutes with them. Consequently

    H_n(X) B(f,y) = P_t(alpha X) B(f,H_r(q^t alpha X/beta)y).       (1)

This proves the actual normalized-lift Hecke identity. It also applies
if the theta image is zero, but then it does not identify an attached
eigensystem. In the subsequent applications only nonzero images are
used.

## 2. Global normalized representation identity

Suppose the source eigenvalues occur on the definite comparison group,
with attached semisimple representation R, and the nonzero image has
attached semisimple representation S. Use the normalization in
[spherical attachment](lsernau-split-galois-attachment.md).
At geometric Frobenius the reciprocal characteristic polynomial is
det(1-X R(Frob_w)); its coefficient of -X is b(w,1). Formula (1)
therefore gives the reciprocal characteristic polynomial of
alpha^(-1) S(Frob_w) as

    prod_{j<t}(1-q^j X) det(1-(q^t/beta) X R(Frob_w)).             (2)

The scalars in (2) are global characters, not placewise choices.
In the source descent data r and t are odd, n even, and
b=mu xi upsilon_U1^(n/2), where xi is the auxiliary tame twist.
Since upsilon_U1^BC=upsilon^2, we obtain
beta=(mu xi)^BC(varpi) q^(n/2). Hence q^t/beta is the geometric
Frobenius value of the algebraic avatar of

    (mu xi)^(-BC) |.|^((r-t)/2).

Write this avatar as theta xi_av^(-1), where theta does not depend on
xi. Likewise alpha^(-1) is the value of the source normalizing
avatar (inverse of the rank-r space character with its absolute
value factor). Its infinity type is algebraic by the prescribed
weight of charW. With epsilon the cyclotomic character, geometric
Frobenius has epsilon^(-1)=q.

All excluded places form a finite set. Equality (2) thus extends to
every Galois element by Chebotarev and continuity of characteristic
polynomials. Brauer–Nesbitt, applied to the two semisimple
characteristic-zero representations, gives the stronger identity

    S tensor normalizingAvatar
      ~= (R tensor theta tensor xi_av^(-1))
                direct-sum (direct-sum_{j=0}^{t-1} epsilon^(-j)). (3)

In particular its trace is
xi_av^(-1) tr(R tensor theta) + sum_{j<t} epsilon^(-j).
This is the normalized trace hypothesis of the
[main-summand construction](lsernau-main-summand-data.md).
The equality is valid on the full Galois group, and in particular on
inertia, with no additional twisting ambiguity. It is not a new
integral splitting of the chosen lattices: semisimple rational
identification does not split a congruence lattice.
The labelled local and Hodge constraints on R are supplied separately
by the previous attachment chapters. The missing global occurrence
of the good eigensystems and their common multiplicities is not
deduced from (3).

## 3. Exact mass for all rectangular sharp blocks

At each chosen split place of residue order q, let the datum be the
indicator of the specified inclusion matrix I_{n,r} modulo q.
At an auxiliary split twist place it is the prescribed tame
determinant character of the top r by r block, extended by zero
on singular blocks, with the remaining t rows free. Write K_M for
the source principal level at the chosen places. In the integral
Schrodinger normalization the squared finite norm is

    F_M = prod_{w in M} q_w^(-nr),
    F_Q = prod_{w in Q} |GL_r(k_w)| q_w^(-r^2).

The finite sharp coefficient has mass c=F_M F_Q/[K_0:K_M],
where [K_0:K_M]=prod_M |GL_r(k_w)|. To see sharpness at chosen
places, an integral source matrix must preserve the specified
inclusion, hence be the identity modulo varpi. At twist places
the transformation of the top block determinant cancels the
source character. In either case nonintegral source matrices
give disjoint primitive supports: every supported matrix X has
an integral left inverse, so integrality of Xg or Xg^(-1)
forces the corresponding source matrix to be integral. Applying
this to both support matrices forces both g and g^(-1) integral.
This proof includes the trivial character extended by zero on
singular blocks. Off these places the datum is the vacuum.

The target index at a chosen place is the number of ordered
independent r-frames, I(q)=prod_{i=0}^{r-1}(q^n-q^i).
At a twist place it is the number of r-planes, I(q)/|GL_r(k)|.
The equivariant character on the stabilizer at the twist place
does not change that index. Thus the product of the target level
index and sharp mass is exactly

    C_M C_Q,
    C_M = prod_{w in M} [prod_{i=t+1}^n(1-q_w^(-i))]/|GL_r(k_w)|,
    C_Q = prod_{w in Q} q_w^(rt) prod_{i=t+1}^n(1-q_w^(-i)).       (4)

Every factor is positive. The real type and its chosen Fock vector
are independent of the weight-zero twist. Formula (10) of Rallis
inversion, with the source algebraic norm conversion (target level
index times target type dimension), now gives the one-lift Gram
operator with exactly this finite factor times the fixed real
factor and the unramified Rallis operator. The real integral has
to be the actual nonzero edge integral of that lift; the preceding
noncompact projection work supplies the local representation but
does not by itself identify every global lift normalization.
Thus (4) fixes the twist-dependent finite normalization and
reduces the remaining one-lift metric matching to that real
identification. It is not yet a full-chain volume formula.

## 4. Rank-one critical norm, including the precise omitted factors

Take r=1, n=2z with integer z>=2, the actual definite torus and
definite target, and mu=nu xi of the critical lift. In the source
the lifted function is the constant 1 on U(1); the character is
in the Weil action. Its highest Fock polynomial is a single
coordinate to the specified nonnegative row length at each
infinite place. It has nonzero squared Fischer norm H, the hook
number in the source convention. Its U(1) transformation is
cancelled by the source determinant character, so the real integral
is exactly H vol[U(1)], with probability compact Haar. There is
no noncompact-real hypothesis in this rank-one calculation.

Let J_M=prod_M(q_w-1) be the torus level index; let d_tau be the
target weight dimension. For the unscaled theta lift with the
source algebraic norm, stable-range Rallis gives

    ||Theta 1||^2 = vol[U(n)] vol[U(1)] H d_tau C_M C_Q V,        (5)

where V is the sum of the unramified finite vacuum coefficients.
The source trivialLift is J_M times this lift; the point-kernel
version also multiplies by
s=vacuumScale^n (bar(pi_M) jetScale)^rowLengthSum,
which is independent of xi and Q.

Compute V directly. At an unramified nonsplit place the rank-one
unitary group is integral, so its contribution is 1. At a split
pair w,bar(w) the valuation of the component at w parametrizes the
cosets by j in Z. Put a_w=mu^BC(varpi_w), |a_w|=1. The source
vacuum multiplier on the saturating ideal of (varpi^j,varpi^(-j))
has absolute value q^(-z|j|); its splitting-character phase cancels
the upsilon_U1^z factor of charV. More explicitly, saturation
has determinant ideal of norm q^|j| at w for j negative, at
bar(w) for j positive. Formula vacuumCoeff_eq_spaceChar reads
charV^BC(c) upsilon(c)^(-2z) Norm(c)^(-z).
Since charV=mu upsilon_U1^z, this is a_w^(-j) q^(-z|j|).
Summing the two geometric series (counting j=0 once) gives

    (1-q^(-2z))/[(1-a_w q^(-z))(1-a_w^(-1) q^(-z))].              (6)

At an inert place the unramified BC character is trivial on a
uniformizer from the real field, and the residue order is the
square of that of the real place. Its L factor therefore cancels
the real-field zeta factor. The source CM extension is unramified
at finite places (i and the third roots of unity rule out
conjugation in inertia). Since z>1, both Euler products converge
absolutely and no denominator vanishes. All split factors in (6)
are positive real. Thus, writing S=M union Q for the set of
removed split pairs,

    V = L^S(z,mu^(-BC))/zeta_{E^+}(2z)
                      prod_{w in S}(1-q_w^(-2z))^(-1).

For r=1, (4) has C_M=prod_M(1-q_w^(-2z))/(q_w-1)
and C_Q=prod_Q q_w^(2z-1)(1-q_w^(-2z)).
Substitute into (5) and multiply by J_M^2 |s|^2. The exact norm is

    ||Phi_{nu,xi}||^2
       = C_nu N_Q^(2z-1) L^S(z,(nu xi)^(-BC)),                  (7)
    C_nu = |s|^2 vol[U(n)] vol[U(1)] H d_tau J_M
                                       /zeta_{E^+}(2z) > 0.

The constant is common to all twists, including characters whose
actual conductor is a proper divisor of the stated modulus. The
positive Euler product proves nonvanishing at the empty modulus.
Adjoining an unused split place removes precisely its two Euler
factors, with no additional scalar after the N_Q normalization.
This supplies the z>=2 analytic norm and norm-relation inputs of
the [critical-value systems](lsernau-critical-value-systems.md).
It does not use a bound for an L-value in the critical strip.
The boundary z=1 has n=2, outside this convergent stable range;
its determinant-period identity remains a separate problem.
The integrality of the point kernels and conjugated Gram pairings
is also separate from (7).

## 5. One Rallis operator for a finite collection of spaces

For any finite collection of principal-level spaces with the same
off-level group and compact K, compress translation by gamma
to the K-fixed vectors. The compression is the normalized
double-coset operator:
P_K pi(gamma) P_K on K-invariants equals
[K:K intersect gamma K gamma^(-1)]^(-1)
times sum pi(k gamma), over the corresponding k cosets. This follows
by integrating over K; the right stabilizer makes the integrand
constant on each coset. Thus each vacuum-series term, including
at nonsplit places, is the action of one element of the common
spherical Hecke algebra (the full algebra of compact-bi-invariant
finite support functions off level). The scalar vacuum coefficient
is the same on every space. The image of this algebra in the
finite direct sum of endomorphism spaces is finite dimensional
and closed. By absolute convergence in operator norm the limit
lies in that same image. There is therefore one finite-support
Hecke element inducing the Rallis operator on the whole finite
collection, not merely an approximation on each individual space.
There is no assertion of a single finite-support representative
for infinitely many varying spaces.

This observation removes the analytic series from the subsequent
finite trace comparison. If the common Hecke traces on the good
subspaces agree for every algebra element, their multiplicities
of joint eigensystems agree: interpolate on the finite set of
distinct joint characters using products of linear polynomials in
operators that separate each pair of characters. The resulting
projector has trace the multiplicity. For the possibly
noncommutative full algebra, use the semisimple image and its
central simple-factor idempotents; equality of all traces gives
equal multiplicities of simple modules, hence equal determinants
for each common element. The required automorphic trace
comparison itself remains to be proved. This argument does not
replace it with equality of total dimensions.

## Source correspondence

All paths are relative to grh/src of the pinned readable revision
72fead102f663d5c7a407964a13dc0cf9d977207.

* Lib/Weil/Unramified/HeckeTransfer.lean, 56, 101–138, 161–459,
  460–662: local finite subspace identity and its bilinear transfer
  (blob a8150176564ae56d5db55f266983019b70a10c4e).
* New/Congruences/GaloisRepresentations/RowsFromEigensystems.lean,
  288–438: first coefficient, normalized avatar and global limit.
  Here (3) strengthens that trace calculation.
* New/Determinant/Norms/AdjointThetaLift.lean, 441–665, 837–1047:
  one-lift mass, Gram and Hecke normalization.
* Lib/SiegelWeil/RallisInner/SharpData.lean, 663–985: saturated
  determinant vacuum coefficients and rank-one Euler product.
* New/OneLift/HeckeValues/CharacterLiftNorm.lean, 338–601:
  block mass, real polynomial, local level indices and critical norm
  (blob 04db66d13a867f8fe1869c61a43d49312a14c994).
* New/OneLift/HeckeValues/AlgebraicPartIntegrality.lean, 101–208,
  250–392: normalized scalar and fixed-modulus measure
  (blob dd5a60fe20d181d6c04d714a497cf394b2d42c5b).
* New/Spanning/Multiplicities/EqualMultiplicities.lean, 69–210:
  common Hecke operator for the Rallis series.

This is an ordinary proof using the existing classical stable-range
and attachment suppliers, not a fresh formal replay.
