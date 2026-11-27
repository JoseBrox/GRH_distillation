# Actual auxiliary-prime root-chain selectors

This proves the allowed-Frobenius and common polynomial suppliers of
the tied extraction, **relative to actual spherical attachment and the
main-summand scalar inertia property**. The construction does not use a
classification of the unramified unitary dual, and needs no bound on
the number of congruent eigensystems in its valuation estimate.

Sources throughout: [readable revision 72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src),
New/Congruences/FirstOrder/HeckeStrings.lean 142–248, 286–432;
DenominatorBound.lean 146–391 and its subsequent determinant
selector construction. The local spherical inequality is proved in
[local tied derivatives](lsernau-local-tied-derivatives.md).

## 1. The exact chain from one root

Use a split spherical place with residue cardinality q and the
rank N unitary representation and polynomial P of Section 1 of
the local derivative chapter. The adjoint of the unnormalized
minuscule Hecke operator of colength i is the minuscule operator
of colength N-i followed by inverse central uniformizer translation:
the inverse double coset of diag(pi I_i,I_{N-i}) is
pi^{-1} times the double coset of diag(pi I_{N-i},I_i).
The Haar normalization is unchanged by inversion.
On the common spherical eigenvector this gives
t_{N-i}=t_N conjugate(t_i), with |t_N|=1.
Writing a_i=(-1)^i q^{i(i-1)/2} t_i, we obtain
a_{N-i}=a_N conjugate(a_i) q^{-i(N-1)}.
Consequently the polynomial identity
\[
 P(X)=a_N q^{-N(N-1)}X^N
       \overline{P(q^{N-1}/\bar X)}
\]
holds (the conjugated expression denotes a polynomial after
multiplication by X^N). In particular the roots, including
multiplicities, are stable under c -> q^{N-1}/conjugate(c).

Suppose c is a root with |c|^2=q^{N-t}, 1<=t<=N.
The strict top-root inequality in the local derivative chapter
says that P(qz) cannot be nonzero if P(z)=0 and
|z|^2<=q^{N-2}. Thus every successive root q^i c forces
q^{i+1}c as long as 2i<=t-2. The reflection above sends
q^i c exactly to q^{t-1-i}c. The forced first half and its
reflection cover all i=0,...,t-1, including the middle index
when t is odd; for t=1 no forcing is needed. Hence
\[
             \prod_{i=0}^{t-1}(X-q^ic)\mid P(X).          \tag{1}
\]
The roots in this string are distinct since q>1 and c!=0.
Other roots need not be distinct.

In the source notation N=card n, r=card r, t=N-r.
Let H_x be the actual spherical polynomial of a base eigensystem
x, rho_x its attached representation, and b the value of the
normalizing avatar at geometric Frobenius F. In the fixed
coefficient isomorphism, b is the inverse of the complex
frobValue c, and |c|^2=q^r by the stated character normalization.
Its ell-adic absolute value is one: a continuous character of a
compact group has bounded positive and negative powers.

Call x weak if det(1-N_x(g))=0 for every g, where N_x is the
normalized representation. Spherical local compatibility says
H_x(rho_x(F))=0 after applying the coefficient isomorphism.
Since 1 is an eigenvalue of N_x(F)=b rho_x(F), H_x(c)=0.
The preceding argument gives
\[
  H_x(b^{-1}X)= B_q(X) A'_x(X),\qquad
  B_q(X)=\prod_{i<t}(X-q^i).                               \tag{2}
\]
The equality is over the chosen complex coefficient field;
we also use its image in the ell-adic field. It is an exact
polynomial factorization, not a residual factorization.
The unitarity needed for (1) is that of the spherical local
representation, with the global Petersson pairing.

## 2. A unit-value polynomial simultaneously for all weak lifts

All normalized representations are continuous. For any group
element g and eigenvalue lambda of N_x(g), the entries of all
positive and negative powers of N_x(g) are bounded by compactness
of the image. On an eigenvector, this implies |lambda|=1 in the
ell-adic norm. Therefore their characteristic coefficients
are integral. The same reasoning applies to the twisted main
summand T=theta.invAvatar times R. This elementary proof does
not require a simultaneous choice of a stable lattice.

At places satisfying the source attachment approximation
(modulo the maximal ideal), the monic polynomial
b^N H_x(b^{-1}X) is congruent to charpol(N_x(F)).
It follows first that its coefficients are integral, even if
the original unnormalized quotient was not known integral.
Since B_q is monic integral, monic polynomial division shows
that A_x=b^N A'_x is monic integral.

If the characteristic polynomial at F is congruent to
S(X) B_q(X), with |S(1)|>=1, then S is integral as well:
S B_q is integral by the congruence, and divide by B_q.
Cancellation in the residue polynomial ring gives
A_x congruent to S, and A_x(1) is a unit. In particular
A_x/A_x(1) is an integral polynomial equal to one at 1
and divisible by A'_x over the coefficient field.

For the selected base system x_0, the exact trace identity
HasLiftTrace at every g and every power of g gives, by Newton
identities in characteristic zero,
\[
 \operatorname{charpol}N_{x_0}(g)
  =\operatorname{charpol}T(g)
       \prod_{i<t}(X-\chi(g)^{-i}).                       \tag{3}
\]
At geometric F the product is B_q. Let Near be all weak
base systems whose characteristic polynomials are congruent to
those of x_0 at every g. If det(1-T(F)) is a unit, (2)–(3)
give the unit-value property for every member of Near.

There is a useful degree refinement. Take the monic least
common multiple A of the finitely many A_x, x in Near,
over their common coefficient field, and put
\[
                         e=A/A(1).                        \tag{4}
\]
A is integral: over an algebraic closure its roots are the
union of the integral roots with maximum multiplicities, and
its coefficients belong to the original field. All these
roots have unit distance from 1, because the product of their
distances for each A_x is a unit and every distance is at most
one. Thus A(1) is a unit. If Near is empty use e=1.
This proves the required HasRootChain simultaneously for
all x in Near, with e(1)=1 and no valuation loss. The degree
of A is at most the sum of the degrees of the A_x, and may be
strictly smaller than the source product construction.
Transport back by the fixed coefficient isomorphism to
EllAdicIntegers[X]. Formula (4) supplies precisely the H
in the derivative construction (X-q^{t-1})H. No bound
on the number of roots of e is used in its integrality.

## 3. The allowed Frobenius condition

Retain the actual IsMainSummandLike scalar inertia input:
at a chosen place away from ell there is gamma in inertia
with R(gamma)=y I, and the residual order of y is greater
than 4r+2. This is the property proved in the
[main-summand datum chapter](lsernau-main-summand-data.md)
conditional on the attached local-type-compatible representations.
The twist is unramified at that place by IsAuxTwist; the
ell-adic cyclotomic character is unramified there as well.
Thus T(gamma)=y I and chi(gamma)=1.

For any g and any m=ell^nu, consider
T(gamma^{im}g)=y^{im}T(g), 0<=i<=r.
All eigenvalues of T(g) are units. The residual scalars
y^{im} in this list are distinct, since raising a root of
unity in characteristic ell to an ell-power preserves its
order (and the supplied residual order exceeds r).
Each eigenvalue excludes at most one i from the condition
that the normalized eigenvalue is not 1. Hence at least one
i gives det(1-T(gamma^{im}g)) a unit. Put delta=gamma^i.
This is the source replacement by delta^m g with delta
in the exact cyclotomic kernel, and the unit-value condition
holds throughout an open neighborhood by continuity.

Intersect the resulting neighborhood with the source
mostFrobeniiAt filter: we exclude the fixed bad-place set,
places in the base level, and require the good spherical
polynomials and their coefficientwise attachment approximation
for the finitely many base systems. These are eventual
properties of the actual attached systems as specified in
HeckeStrings.lean and DenominatorBound.lean; no additional
density assertion about labelled ramified polynomials is used.
Chebotarev with the specified Frobenius lift gives a prime
in every sufficiently small prescribed open set. Prime-norm
places suffice: in a number field the prime ideals of
residue degree greater than one contribute a bounded series
to Dirichlet density at 1, and can be omitted in a positive
density Chebotarev condition. We also avoid the finitely
many places and their conjugates excluded by the previous
triangle rows. For prime norm and a CM field, the
prime is split over the maximal real subfield.

This is exactly the allowed-Frobenius condition used in
[triangle detection](lsernau-triangle-detection.md).
Combine it with the proved [Kummer relation supply](lsernau-kummer-relations.md),
the fixed detector and the triangle construction. For each
nu choose the resulting family of places, all with
q congruent to 1 modulo ell^nu, and at each place take
(4). The number of places is independent of nu;
the polynomial is allowed to depend on nu and the place.
This proves the actual Taylor–Wiles prime and root-chain
supplier under the attachment/main-summand hypotheses,
including the source small-prime/zero-cyclotomic-loss case.

## 4. The finite weak-lift selector

At the fixed base level, for every nonweak system z choose
a g_z with a_z=det(1-N_z(g_z))!=0. On the finite set of
systems form the diagonal polynomial in integral Hecke
operators
\[
 \delta_0(x)=\prod_{z\ {\rm nonweak}}
        (a_z-\det(1-N_x(g_z))),\qquad
 n_0=\prod_{z\ {\rm nonweak}}a_z .
\]
The coefficients are integral by the characteristic-polynomial
argument and the integral trace algebra of the local derivative
chapter. This operator vanishes on nonweak systems and equals
the nonzero scalar n_0 on every weak system. The empty product
is 1. Multiply it by the previously constructed residual-block
indicator A_0 to get delta'=A_0 delta_0. This is exactly the
selector needed in the derivative factorization: on base
invariants where delta' is nonzero, all the complementary
polynomials divide e and (1) applies.

The valuation v_ell(n_0) is finite, independent of nu.
Choose nu sufficiently large *after* this fixed selector,
so that the modulus in integral extraction is divisible by
the required power of the nonzero scalar c^2 n_0.
The fixed number of auxiliary places and the logarithmic
derivative loss allow this. The cancellation in equation
(8) of the extraction chapter means that v_ell(n_0) is
not charged to the final separator valuation.

Thus all root-chain and residual-block selectors used in
the integral extraction have now been constructed relative
to the actual attached representations and their scalar
inertia property. The labelled all-powers local-global
input and the arithmetic lengths and local crystalline
defect estimates are still necessary to construct and bound
individual congruence separators. This is not an unconditional
attachment theorem, a proof of the local defect estimates,
or a claim of a new Lean replay.
