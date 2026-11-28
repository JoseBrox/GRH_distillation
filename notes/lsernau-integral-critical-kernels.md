# Integral critical kernels, with exact finite Fourier denominators

This supplies the z>=2 point-kernel integrality input of
[critical-value systems](lsernau-critical-value-systems.md), using
the already constructed scalar CM, integral vacuum, charged-jet
and gauge suppliers. In particular, it does not deduce integrality
from the Euler product norm. The
[rank-two period arithmetic](lsernau-rank-two-period-arithmetic.md)
supplies the \(z=1\) kernel integrality and exact Euler insertion with
a further radical-level saving. Its fully ramified analytic period
identity and nonzero base are proved in
[the rank-two norm chapter](lsernau-rank-two-period-norm.md).

## 1. Finite datum and its exact clearing factor

Keep the source critical pair (nu,z), n=2z>=4, M=p_0 p_1,
f=[E:Q]/2, and row-length sum L. Let m be the actual modulus
levelModulus 1: the product of the chosen split places and the
auxiliary twist places Q, with no conjugate place included.
At each chosen prime p_i there are f chosen degree-one places.
Thus

    Norm(m)=M^f N_Q.

In the self-dual finite coordinates of
[Weil normalization](lsernau-weil-normalization.md), the source
pointDatum is the integral vacuum multiplied by the residue
indicator of the specified column. At chosen places the whole
column is specified; at twist places its distinguished entry is
1. The other coordinates may be arbitrary. The datum is
independent of the tame character at fixed modulus. The factor
vacuumScale^n making the vacuum integral has already been
included; do not introduce it twice.

Expand the residue indicator Psi on (O_E/m)^n in additive
characters. By orthogonality the coefficient of a character chi is

    Norm(m)^(-n) sum_x Psi(x) overline(chi(x)).

The numerator is an algebraic integer because the indicator
takes values 0 or 1 and the character values are roots of unity.
The signed Heisenberg translations at the conjugate split
places realize these characters on the vacuum, by the
self-dual conductor pairing. Their finite coordinates have
denominators at most the local modulus; they are supported at
these split pairs. Multiplication by M makes them integral at
every place above a coefficient prime ell not dividing N_Q.
At all such coefficient embeddings the factor N_Q^n is a unit.
It follows directly that

    M^(fn) pointDatum belongs to standardData(M)              (1)

at each of those embeddings. This improves the generic bound
M^(2fn) that uses Norm((M)) rather than the norm of the actual
chosen half of the split modulus. Formula (1) holds without
a bound for the number of terms in the Fourier expansion.

## 2. Integrality of the scaled derivative and transported gauge

The kernel is the Schur jet at scale c jetScale, with
c=bar(piMBar), an algebraic integer of norm M. In rank one
the source Schur representation is trivial and the target
mixed weight has one row at each CM embedding. Its Schur entries
are homogeneous integral polynomials of total degree L:
they are the entries of the polynomial Weyl representation
in its integral tableau basis. There is no determinant
twist on this target gauge.

The [charged-jet theorem](lsernau-charged-jet-estimate.md), (4),
gives for a standard datum of level delta and a homogeneous
integral differential polynomial of degree L, in the actual
period normalization,

    v(derivative at c jetScale) >= L v(c/(bar(delta) sqrt(-d))).

For delta=M and c integral this is at least
-L(v(M)+v(d)/2). Multiplying by the integer
M^L d^ceil(L/2) therefore makes every Schur entry integral.
The required period-factor identity, the CM frame prime
to the coefficient prime, and the actual scaled vacuum are
those established in [Weil normalization](lsernau-weil-normalization.md)
and [scalar CM normal form](lsernau-cm-theta-normal-form.md).
If using only the source's coarser integral derivative
bound with d instead of sqrt(-d), the sufficient factor is
(Md)^L.

This entrywise calculation is a gauge statement at every
finite point, not just at the identity. Apply the rational
approximation and integral Weil-action argument of
[definite gauges](lsernau-split-transfer-and-level-lifts.md),
section 6 with diagonal d there equal to the identity.
For the source and target finite points g,h, choose rational
unitary multipliers gamma,epsilon making them integral above ell.
The actual theta jet is rationally equivariant by
[nonstandard transport](lsernau-nonstandard-weil-transport.md)
and the derivative construction; the transported gauge is
invariant under those rational changes of points. Integral
unitary actions above ell and arbitrary actions away from ell
preserve standardData(M) as proved in the definite-gauge
chapter. Thus (1) and the entrywise derivative estimate give

    weylGauge_ell(h, C_nu pointKernel(g,h)) <= 1,              (2)
    C_nu = M^(fn+L) d^ceil(L/2).

The larger source denominator M^(2fn)(Md)^L is divisible
by C_nu. All inequalities are for each embedding separately.
In particular the proof works at the chosen level primes
as well as away from them, provided ell does not divide N_Q.
No p-adic norm of the complex Gaussian is being taken: all
values use the specified algebraic CM period normalization.

## 3. Fixed-modulus integral measure

At fixed Q the point datum and scale are independent of
the twist xi. The latter occurs in the source-character
factor b(det g)^(-1) in the Weil action. Thus changing the
trivial character of modulus Q into xi multiplies the point
kernel by xi(g)^(-1), with g read as a norm-one idele.
The residue-unit lifts partition the full block into the
specified single-column-entry indicators; their inverse
unit convention gives exactly the class representatives
u_a in the critical-value chapter. The chosen source torus
level is free (a root of unity congruent to 1 at the prescribed
odd split level is trivial, as proved there). Consequently

    Phi_{nu,xi}(h)=sum_a xi(u_a)^(-1) K_a(h),

with K_a the untwisted point kernels at that same modulus.

For the Gram pairing take the first gauge at the coefficient
embedding composed with conjugation and the second at the
original embedding. To justify this carefully, rationally
translate h to a point integral above ell. The Weyl gauge
then reduces to the integral tableau coordinates and the
Gram pairing is unchanged by the common rational unitary
action. Its matrix has integer entries, since the Weyl
vectors are integral tensor/exterior-power combinations
with the standard tensor Gram product. Equivalently, on the
two coefficient embeddings the finite unitary matrices
satisfy the transpose-inverse law, so their two gauge actions
cancel in the pairing. Thus (2) proves integrality of
C_nu^2 gramForm(K_b(h),K_a(h)) at ell. This checks the
conjugate-side embedding rather than assuming it agrees
with the original p-adic valuation.

In the class sum over the target each stabilizer order
divides the source chosenGroupOrder G, by the established
definite-level bound (the level is contained in the standard
integral group and the rank is in the source range).
Therefore

    c_ab = G C_nu^2 N_Q^(-(n-1))
           classSum_h gramForm(K_b(h),K_a(h))

is integral at every ell prime to N_Q. Expanding the norm
square gives the group-ring element

    Theta_Q = sum_ab c_ab [u_b/u_a],

whose evaluation is
G C_nu^2 ||Phi_{nu,xi}||^2 / N_Q^(n-1).
This remains valid for imprimitive twists of the prescribed
modulus. The norm formula of
[stable-range critical norms](lsernau-normalized-transfer-critical-norm.md)
shows that this normalized squared norm is a fixed positive
constant times the partially omitted L-value, independent
of Q and xi. Hence the empty-modulus value is nonzero and
the Euler removal relations hold at every new permitted split
place. The constant changes by the same fixed factor if the
larger original source denominator is used throughout.
The original Stickelberger system normalization can thus be
retained, or the smaller integer C_nu used consistently.

This proves the integral measure and analytic norm suppliers
for the stable-range z>=2 branch on the common CM lattice.
The z=1 branch is completed by the separate rank-two arithmetic and
analytic norm chapters linked above. The remaining determinant ratios
and the global short-form/complement comparison are not consequences
of this rank-one calculation.

Source dictionary: pinned readable revision
72fead102f663d5c7a407964a13dc0cf9d977207,
New/OneLift/HeckeValues/AlgebraicPartIntegrality.lean 101–208,
257–403; New/UpperBound/Kernels/ThetaLiftGauge.lean 250–490
(blob 5c3212c92e2d1a52ada40b2f4822800d0a8c16ea);
Lib/Adelic/AutomorphicForms/PAdicGauge.lean,
gramForm_mem_embValRing.
The proof is a combination of the established local suppliers,
with the exact split-half Fourier denominator, not a Lean replay.
