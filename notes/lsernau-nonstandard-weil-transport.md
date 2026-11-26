# Exact nonstandard Weil transport and the mixed theta identity

This chapter fixes the phase of the **actual** Weil action used by the
common diagram. It proves rational unitary invariance, canonical transport
between pointed spaces, orthogonal products, the mixed zero-term laws and
absolute mixed theta summation. It does not establish a uniform estimate
for an integral over a noncompact unitary quotient, or injectivity of an
integrated theta lift.

We use the ordinary adelic Heisenberg/Weil model (Stone--von Neumann,
the Schwartz--Bruhat realization and its covariance), Fourier inversion
on the additive adelic quotient, and Landherr's local-global theorem for
Hermitian forms. These are classical inputs, not new claims about the
formal verification. We use the lattice and splitting character constructed
in [the standard normalization chapter](lsernau-weil-normalization.md).
In particular \(E/F=E/E^+\) is unramified at every finite place, and
the character \(\upsilon\) is unramified on finite units, equals \(-1\)
on an inert uniformizer, satisfies
\(\upsilon(\bar t)=\upsilon(t)^{-1}\), is trivial on principal ideles,
and has the infinity type \(z/|z|\) at each CM-type place. Write
\[
 \chi(t)=\upsilon(t)|t|_{\mathbb A_E}^{-1/2}.
\]
All references below are to the pinned revision
[lsernau/grh-lean@72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).

## 1. Identification of the model and normalization of the theta line

A pointed space is \(V=(J,x_V)\), where \(J\) is a nonsingular
rational Hermitian matrix and \(x_V^*Jx_V\) is the fixed signed
matrix at infinity and the identity at the finite places. In normalized
coordinates the rational Heisenberg vectors are
\(\Gamma_V=x_V^{-1}E^n\). The actual Weil action depends on the sign
tuple and the standard finite lattice, not separately on \(J\).
Write \(\rho\) for its Heisenberg translations and \(v\) for its
unit vacuum. The prescribed normalization is
\[
 \langle v,\omega(g)v\rangle=\overline{\Delta(g)}^{-1},\qquad
 \Delta(g)=\Delta_f(g_f)\prod_{\tau}\overline{\det d_\tau}.
 \tag{1}
\]
Here \(d_\tau\) is the negative-to-negative block and
\(\Delta_f(g)=\chi_f(\det u)\), where
\(u\widehat{\mathcal O}_E^n=\widehat{\mathcal O}_E^n
\cap g^{-1}\widehat{\mathcal O}_E^n\).
The latter is a saturation of the standard lattice in the normalized
coordinates; the common scalar fractional ideal \(\alpha\) cancels.
The determinant is well-defined modulo finite integral units.
These are the defining multipliers of the source, not an alternative
choice of a splitting. In particular the overlap in (1) is nonzero.
Its phase, together with unitarity and Heisenberg covariance, determines
the operator: two unitary intertwiners differ by a unit scalar, and
their nonzero overlaps have the same phase precisely when that scalar
is 1.

For clarity one can do the following argument on the classical
Schwartz--Bruhat subspace. Choose a rational symplectic polarization
of the underlying rational alternating space (take the trace to
\(\mathbb Q\) of the skew-Hermitian form). Its Schrödinger model is
\(\mathcal S(\mathbb A_{\mathbb Q}^{D})\), \(D=\dim_{\mathbb Q}V/2\).
The corresponding central character is the source's adelic
additive character, since the pairing includes its specified
purely imaginary coefficient \(j\). Normalize the self-dual measures;
\(\mathbb A_{\mathbb Q}^{D}/\mathbb Q^{D}\) has volume one.
In these coordinates the rational Heisenberg invariant distribution
is, up to a scalar,
\[
 \Lambda(F)=\sum_{\xi\in\mathbb Q^D}F(\xi).
 \tag{2}
\]
Here rational modulations are trivial on the summation set, including
the central half-pairing on rational vectors.

Here is a direct uniqueness and normalization argument. A
translation-invariant distribution factors through periodization
\(F\mapsto\sum_\xi F(\,\cdot+\xi)\). To see this, choose a compactly
supported smooth function \(\eta\) with periodization 1: start with
nonnegative smooth bumps positive on a finite cover of the compact
quotient, and divide their sum by its positive periodization.
For an invariant distribution the value on \(F\) equals its value
on \(\eta\sum_\xi F(\cdot+\xi)\). The equality follows by translating
the individual summands; their sums converge in the Schwartz topology,
using the finite support at finite places and rapid decrease on the
archimedean lattice of bounded denominators. Invariance under
multiplication by every rational character now makes the resulting
distribution on the compact quotient a multiple of evaluation at 0.
Indeed it has the same value on each character, and Fourier expansion
is convergent in the smooth topology (at fixed finite level it is
the ordinary Fourier expansion on a finite union of tori).
This proves uniqueness of (2).

For \(F\) in the Schrödinger space integrate the squared theta value
of its translates over the two adelic quotient coordinates \(a,b\).
For fixed \(a\), orthogonality of the rational characters in \(b\)
gives
\[
 \int_{\mathbb A^D/\mathbb Q^D}
  \left|\sum_{\xi\in\mathbb Q^D}
      \psi(b\cdot(\xi+a/2))F(\xi+a)\right|^2 db
 =\sum_{\xi}|F(\xi+a)|^2 .
\]
The half-pairing does not affect the modulus. A second integral unfolds
to \(\|F\|_2^2\). In particular a theta distribution whose vacuum
translation mean square is 1 is a unit multiple of (2), not a
multiple with an uncontrolled modulus. This also proves injectivity
of its Heisenberg realization \(F\mapsto(z\mapsto\Theta(\rho(z)F))\).
It does **not** say that evaluating a theta lift at one automorphic
vector is injective.

The calculation applies to the source's model of integrable vacuum
coefficients as well. In the Schrödinger model the normalized vacuum
has a Gaussian archimedean part and a compactly supported smooth
finite part, possibly in transformed coordinates. The map sending
its Heisenberg translates to the source vacuum translates is isometric:
their mutual inner products are obtained by the Heisenberg law from
the same specified vacuum coefficient. The span is dense by
Stone--von Neumann. The Schwartz space embeds in the data model
by the coherent-state resolution
\[
 f=\int \langle \rho(y)v,f\rangle\,\rho(y)v\,dy .
 \tag{3}
\]
The Haar measure here is normalized by the square-integrability
orthogonality for a unit vacuum. The finite part of the coefficient
of a Schwartz vector against the vacuum has compact support (both
translation and modulation variables, by compact support and local
constancy); the real part is rapidly decreasing. Hence the
integral is absolutely convergent in the data norm and this norm
is bounded by Schwartz seminorms at each finite level. Formula (3)
also makes the vacuum-translate span dense in that norm. These
observations identify the given bounded rational-invariant theta
functional with the unique distribution just calculated, and justify
passing identities of bounded maps from the smooth model to the
data space. The ordinary covariance and preservation of Schwartz
space are used here, not a putative uniform bound on the unitary
group variables.

References: AdelicRepresentation.lean, 381--421, 497--805,
808--944, 1041ff. (blob 5b6a2897be93a262dc1987879f7faef0ec3eddcd);
CanonicalTheta.lean, 108--148 (blob 64564b2cdcb6b58974d848d12f4edaabd32ce0f6).

## 2. The exact hyperbolic Levi phase

In a split hyperbolic block write its isotropic frames \(l,k\)
in this order, with \(l^*Jk=1\). The Levi \(g_a\) acts by
\(l\mapsto l a^{-*},\ k\mapsto k a\). We calculate the phase in
(1) in adapted normalized coordinates. At each real place choose
the orthonormal positive/negative axes \((l+k)/\sqrt2\) and
\((l-k)/\sqrt2\). The negative block is
\((a+a^{-*})/2\). Since
\[
 a+a^{-*}=a^{-*}(I+a^*a),
\]
its determinant has phase \(\det a/|\det a|\). The real
factor of \(\Delta(g_a)\upsilon(\det a)\) is consequently positive.

At a finite place use an integral hyperbolic frame of the
standard unimodular lattice. Such a frame exists even above 2:
in the unramified quadratic algebra the norm on units is
surjective, so \((1,u)\), \(u\bar u=-1\), is a primitive
isotropic vector of the two-dimensional unit lattice. Choose
an integral partner pairing to 1 and subtract a multiple of
the first vector to make it isotropic, using the surjectivity
of the integral trace map. The two vectors then form an integral
basis by their unimodular Gram matrix. At split places this
argument applies with the split quadratic algebra; take direct
sums for higher rank. No inversion of 2 in the ring of integers
is needed.

Let \(e_{w,i}\) be the local Smith exponents of \(a\) at \(w\).
The sum of the exponents of the determinant of the saturated
lattice in (1) is
\[
 s_w=\sum_i\max(0,-e_{w,i})+
                  \sum_i\max(0,e_{\bar w,i}).
\]
This follows from the two blocks \(a,a^{-*}\); integral factors
on either side of a Smith form preserve the index. The finite
phase of \(\Delta_f(g_a)\upsilon_f(\det a)\) is therefore the
character on an ideal of exponents
\[
 s_w+\sum_i e_{w,i}
     =\sum_i\max(0,e_{w,i})+\sum_i\max(0,e_{\bar w,i}).
\]
At an inert place this is even, so its contribution is 1.
At a split pair the exponents are equal and the two character
values are inverse. The argument uses only finitely many
nonzero exponents and proves
\[
             \Delta(g_a)\upsilon(\det a)>0.
 \tag{4}
\]

In the mixed Schrödinger realization let \(T_a\) act by
\[
             (T_aF)(z)=\chi(\det a)^{-1}F(a^*z).
 \tag{5}
\]
It is unitary by adelic change of variables and has the correct
Heisenberg covariance. The adapted vacuum on this hyperbolic
block is, up to a constant, a real positive Gaussian times
the indicator of the self-dual finite lattice. This can be
seen from its characteristic coefficient: at infinity the
two equal orthogonal isotropic axes give the standard
Gaussian; at finite places invariance under the two isotropic
lattices forces both support in one self-dual lattice and
constancy on it. On each isotropic lattice the signed vacuum
phase is trivial. Equivalently its Schrödinger value is
proportional to the squared modulus of the source's rank-\(r\)
vacuum coefficient. Its overlap with its transform by (5)
is a positive real number times \(\chi(\det a)^{-1}\):
the intersection of the two finite lattices is open and
nonempty, and the two Gaussians are positive. By (4) the
phase is exactly the phase of the overlap (1). Stone--von
Neumann and unitarity now identify (5) with the prescribed
Weil action. In particular the exponent \(-1/2\) in \(\chi\)
and the inverse of the splitting character have been fixed,
not absorbed into a proportionality constant.

On block diagonal sums, the same argument gives exact tensor
compatibility of the Weil operators: vacuum coefficients
multiply, the finite saturation is a direct sum, the real
determinants multiply, and Heisenberg covariance determines
the unitary intertwiner up to a scalar whose phase (1) fixes.
This applies also to \(g_a\oplus g_0\) in an adapted mixed
frame for any pointed middle space \(V_0\).

References: FiniteMultiplier.lean, 943--1020
(blob be310c131ec94bbd575b09d709de2c2c05e33c9f);
ThetaInvariance.lean, 299--407
(blob 9833a44aba1233e591939a242fdd23d2829aa1d9).

## 3. Mixed zero terms, summation and the radical

Use a rational Witt decomposition
\(V=lE^r\oplus V_0\oplus kE^r\). Write
\(\operatorname{ev} f\) for the zero term, defined as the
probability Haar mean along \(k(\mathbb A_E^r/E^r)\) of
the theta function, and
\(f[z]=\operatorname{ev}\rho(lz)f\). In the mixed
Schrödinger realization the hyperbolic coordinates give a
Schwartz function of \(z\in\mathbb A_E^r\) with values
in the middle representation. Averaging the \(k\)-translations
in (2) selects \(z=0\) by character orthogonality. Thus
\(\operatorname{ev}\) is a nonzero scalar times evaluation
at 0; the scalar is the ratio of the two normalized theta
phases. The same scalar occurs in every slice. In particular
the definition by the mean, rather than an independently
normalized restriction, proves the exact identity
\[
                 \Theta_V(f)=\sum_{\xi\in E^r}\Theta_{V_0}(f[\xi]).
 \tag{6}
\]
One can see it without choosing either theta phase: the
terms are exactly the Fourier coefficients of the function
\(b\mapsto\Theta_V(\rho(kb)f)\), by the Heisenberg
commutation relation and rational invariance. Fourier
inversion at zero gives (6).

Here is a useful uniform-in-translation bound for this
Fourier summation. Fix a splitting and adapted unit vacuum
\(u\). Its mixed function is \(C\phi(z)v_0\) for a constant
\(C\ne0\), with \(\phi\ge0\) a Gaussian times a finite
lattice indicator; \(v_0\) is the middle vacuum. Under an
arbitrary translation by \(y=la+i w+kb\), the mixed
law is
\[
 (\rho(y)u)[z]=\beta(2z+a,b)\rho_0(w)u[z+a].
\]
The scalar \(\beta\) has absolute value 1. The sum of
\(\phi(\xi+a)\) over \(\xi\in E^r\) is bounded independently
of \(a\): reduce \(a\) modulo the rational lattice to a compact
set, use the compact finite support to bound the denominators
of the rational vectors by one fractional ideal, and use
Gaussian summability on its archimedean lattice. The same
argument bounds the integral of \(\phi(z+a)\) independently
of \(a\). Applying (3) with the adapted vacuum, and the
boundedness of the fixed adapted Weil operator and its
inverse on the data model, gives constants depending on
the splitting with
\[
 \sum_{\xi\in E^r}\|f[\xi]\|_{\rm data}
       \le C_D\|f\|_{\rm data},\qquad
 \int_{\mathbb A_E^r}\|f[z]\|_{\rm data}\,dz
       \le C'_D\|f\|_{\rm data}.
 \tag{7}
\]
For each translation the zero-term map is also bounded by
\(|C|\sup\phi\,\|v_0\|_{\rm data}\); (3) proves its
boundedness on the full data space. These estimates extend
(6) by continuity and absolute convergence. They do not
assert uniform bounds on \(C_D,C'_D\) as the diagram varies.
A mixed Schwartz realization also gives ordinary pointwise
absolute convergence directly.

By (5) and exact tensor compatibility,
\[
 \begin{split}
 \operatorname{ev}\omega(g_a,g_0)
   &=\chi(\det a)^{-1}\omega_0(g_0)\operatorname{ev},\\
 (\omega(g_a,g_0)f)[z]
   &=\chi(\det a)^{-1}\omega_0(g_0)f[a^*z].
 \end{split} \tag{8}
\]
The unknown constant in the evaluation map cancels.

For an element \(n\) of the unipotent radical of the
\(k\)-parabolic, Heisenberg covariance makes
\(\operatorname{ev}\omega(n)\) a scalar multiple of
\(\operatorname{ev}\). Indeed \(n\) fixes \(k\) and acts as
the identity on \(k^\perp/k\). In the mixed model, a continuous
map invariant under the modulations in the \(z\)-variable
factors through evaluation at \(z=0\): this is the distribution
supported at zero with no derivatives. At infinity the assertion
follows by differentiating modulation invariance, so multiplication
by each coordinate annihilates the distribution; at the finite
places local constancy and characters separating points give
the assertion. After evaluation, covariance with the middle
Heisenberg group and irreducibility makes the map scalar.
The scalar is nonzero and multiplicative since the radical
acts by invertible operators. Equation (8) shows its invariance
under conjugation by the Levi. The scalar Levi \(a=2I\) grades
the radical's abelian first quotient and its central subgroup
by weights \(2,4\) (or their inverses, according to the
choice of opposite parabolic). A conjugation-invariant
character on the center is trivial since multiplication by
\(4-1=3\) on its additive adelic vector space is onto. After
passing to the abelian quotient the same proof with \(2-1\)
gives triviality. This also covers the zero-middle case.
Hence for all elements preserving \(k\) the first formula
in (8) holds with the actual determinant on \(k\) and induced
middle action. In particular the central radical element
\(l\mapsto l-k j^{-1}Z\), \(Z=Z^*\), acts on the slices by
\(\psi_E(-z^*Zz/2)\); this follows by commuting the
translation by \(lz\) through the element and then applying
the mixed law to the additional \(k j^{-1}Zz\) term.
All scalar statements are with the prescribed normalization.

References: ZeroTerm.lean, 684--798
(blob 381b7d1fdd689c2729c9cae8bc0187c05404c4ab);
ThetaInvariance.lean, 407--487.

## 4. Rational unitary invariance, including anisotropic spaces

First suppose \(V\) is split. A rational Levi has
\(\chi(\det a)=1\) by the product formula and triviality
of the character on principal ideles, and \(a^*\) permutes
\(E^r\). Its rational radical acts by a character trivial
on rational points. Thus (6)--(8) give exact invariance
of \(\Theta_V\) under the Siegel parabolic. The same proof
with the opposite frame gives the opposite Siegel parabolic.
They generate the split rational unitary group: the relative
Bruhat decomposition for the stabilizer of a maximal isotropic
space has double cosets represented by interchanges of
hyperbolic pairs. Such interchanges are in the generated
group, since for any \(\lambda\in E^\times\) with
\(\bar\lambda=-\lambda\),
\[
 \begin{pmatrix}0&\lambda\\-\lambda^{-1}&0\end{pmatrix}
 =
 \begin{pmatrix}1&\lambda\\0&1\end{pmatrix}
 \begin{pmatrix}1&0\\-\lambda^{-1}&1\end{pmatrix}
 \begin{pmatrix}1&\lambda\\0&1\end{pmatrix}.
\]
Each upper/lower matrix preserves the hyperbolic Hermitian
form, and permutations of pairs belong to the Levi.
So the whole rational group fixes the theta functional.

For arbitrary \(V\), double to \(W=V\oplus(-V)\).
The diagonal and anti-diagonal give rational complementary
isotropic subspaces, with dual frames obtained by inserting
\(J^{-1}/2\) in the latter. The rank-zero case is trivial.
The theta distribution on \(W\) is a nonzero scalar times
the product of the theta distributions on \(V,-V\),
by Heisenberg uniqueness (the product is itself invariant
and nonzero). This assertion does not require any choice
of the relative phase. Choose a second-factor vector \(h\)
on which that distribution is nonzero. For \(\gamma\) a
rational unitary point on \(V\), use split invariance of
\((\gamma,1)\) and exact tensor compatibility of the
Weil action:
\[
 \Theta_W((\omega_V(\gamma)f)\otimes h)
     =\Theta_W(f\otimes h).
\]
Cancel the nonzero scalar and second-factor theta value.
This proves
\[
          \Theta_V\omega_V(\gamma)=\Theta_V
 \tag{9}
\]
without importing rational unitary invariance of the
nonstandard model as a hypothesis. In normalized coordinates
the action is by \(x_V^{-1}\gamma x_V\).
Heisenberg covariance immediately gives the substitution law
on theta functions,
\[
  \Theta_V(\rho(z)\omega_V(\gamma)f)
       =\Theta_V(\rho((x_V^{-1}\gamma x_V)^{-1}z)f).
 \tag{10}
\]
The computation is valid on the smooth model and hence by
boundedness on the data model. References: ThetaInvariance.lean,
496--637.

## 5. Canonical phases, moved spaces, and the common diagram

For two pointed spaces of the same signatures, their
given points identify the two local forms at every place.
Landherr's theorem therefore gives a rational isometry \(A\)
with \(A^*J_VA=J_W\); the normalized isometry
\(g=x_V^{-1}Ax_W\) maps \(\Gamma_W\) onto \(\Gamma_V\).
If \(g\) merely maps \(\Gamma_W\) into \(\Gamma_V\) and is
invertible adelic linear, its rational matrix has columns
in \(E^n\), is nonsingular, and is therefore a rational
isomorphism. No index of rational lattices is introduced.

For the signed standard space fix the product of the
specified rank-one functionals, with their given phases.
Its mean square normalization follows from the product
quotient. For \(V\), choose any \(g_V\) taking \(\Gamma_V\)
onto the signed standard rational lattice, and put
\(\Theta_V=\Theta_{\rm std}\omega(g_V)\). Two choices differ
by a rational unitary operator on the standard lattice,
which fixes \(\Theta_{\rm std}\) by (9). Thus this is
precisely the choice-independent canonical phase of the
source. For any \(g\) carrying \(\Gamma_W\) to \(\Gamma_V\),
\[
            \Theta_W=\Theta_V\omega(g).
 \tag{11}
\]
In particular \(\Theta_{(J,x_Vg)}=\Theta_V\omega(g)\).
For an orthogonal sum with block-diagonal point the
product of the two maps to the standard signed spaces
is such a map for the sum. Exact tensor compatibility and
the standard choice of the product phase therefore give
\[
        \Theta_{V_1\oplus V_2}(f_1\boxtimes f_2)
                 =\Theta_{V_1}(f_1)\Theta_{V_2}(f_2).
 \tag{12}
\]
Permutations of compatible sign coordinates preserve the
chosen product phase as well (the corresponding permutation
is an integral unitary with positive real vacuum multiplier
in the signed standard product realization; equivalently
use the canonical tensor identification carrying the vacuum
and the translates, and reorder the product of the line
functionals). No analogous exact phase is asserted for an
arbitrary semilinear complex conjugation without its separate
comparison. Its invariant functional is at least a unit
multiple, by uniqueness and the quotient-mean normalization.

Equations (9)--(12) provide the rational and pointed-space
transport required for forming common kernels, including
their nonstandard lower-chain spaces. They are identities
of theta functionals and do not require a choice of new
period on each edge. Inserting a fixed rational
isometry on the hom space of a dual pair consequently
introduces no arbitrary unit scalar beyond the prescribed
Weil operator and the dual-pair determinant characters.
The common arithmetic jet identities still require
the full Galois-semilinear comparison and their sharp local
tests; the global integral see-saw still needs its
unfolding, absolute majorants on the unitary quotient,
and nonvanishing. In particular (7), which concerns
rational additive lattice summation for a fixed splitting,
must not be substituted for those missing estimates.

References: Landherr.lean, 433--478
(blob 61e6be188613eaef2b0ce1a5f23b1994fa969731);
CanonicalTheta.lean, 90--213;
ProductsAndTransport.lean
(blob e22509ab3a679872a8efc8c7501fb9a1b39a9f03).
