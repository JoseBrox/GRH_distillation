# The cubic automorphic seed: what can be constructed and what is missing

24 November 2026. This is a supplier audit and a partial construction for
the two remaining high-dyadic point premises in
[cubic-high-dyadic-presentation.md](cubic-high-dyadic-presentation.md).
It uses the parent rank-two arithmetic seed, but does not claim a
cuspidal rank-three seed, an R=T theorem or irreducible curve exclusion.

## 1. Actual ordinary endoscopic starting data

Keep F=Q(omega), K=F(cuberoot(2)), lambda the order-three character of
G_F, eta the quadratic character of F/Q, and the normalized diagonal
(a lambda^(-1),1,a^(-1)lambda^(-1)), a=epsilon^e rho^N, of the cubic
frame. Here rho is a rational host character of 2-power order, and
N is a modulus for it. In this construction assume ell>=5 and
ell does not divide 6N. Assume the high dyadic conductor condition.

Let chi' be rho, or rho eta if necessary to achieve
chi'(c)=(-1)^e. This does not change its restriction to G_F.
Enlarge N by a factor of 3 if necessary. Choose a rational prime w
prime to 6N ell, split in the finite fields of the characters and
with w=1 mod ell. Chebotarev gives infinitely many such w (in fact
one may use a splitting prime of the compositum). Let theta be a
character of order ell and conductor w. Write L/F for the abelian CM
extension obtained by adjoining the real degree-ell field of theta.
Additional real auxiliary extensions of degree dividing 2 times
an ell-power are allowed. The degree of L/F then divides 2 ell^s
for some s. The residual square of epsilon^e chi' is nontrivial
on G_L: at inertia at 2 before restriction its order is at least
2^(b-3), where 2^b is the exact dyadic conductor. Restriction to a
group of index dividing 2 ell^s cannot kill this square.

Thus the rank-two construction in
[parent arithmetic seed, AS1--AS4 and its rank-two paragraph](../../paper/shared/selmer-integral-frontier-arithmetic-seed.tex)
applies with the imaginary quadratic field F. More precisely we
use the modular-form construction in that proof, not its assertion
about the original source's full rank-three seed. It constructs
ordinary newforms f of weight 2m+1, for sufficiently large
m=e mod (ell-1), with character chi'^2 eta theta. If r_f denotes
the arithmetic-Frobenius representation with determinant
epsilon^(2m) chi'^2 eta theta, put


```math
\sigma=r_f\varepsilon^{-m}(\chi')^{-1}.
```


Its determinant is eta theta, its residual semisimplification
is (epsilon^e chi' eta) plus (epsilon^(-e) chi'^(-1)), and its
ordered inertia exponents at ell are m,-m. The exact away inertia
is the pair chi' theta eta and chi'^(-1), in the sense of
semisimplification of its finite inertia restriction.
These are consequences of the Eisenstein congruence, ordinarity
and exact conductor argument of AS2--AS4. On G_L both eta and
theta are trivial. The parent proof establishes irreducibility
on G_L using the nontriviality of the residual square verified
above. In fact it is strongly irreducible: an imprimitive
rank-two representation would have a quadratic self-twist,
which upon reduction forces the ratio of its two distinct
residual characters to have order two. That ratio has order
greater than two on G_L. Scalar action on an open subgroup
is excluded by the two distinct infinite inertia exponents.

Set W=sigma|G_L and A=W tensor lambda^(-1)|G_L. It follows
directly that det A=lambda^(-2), A^c is isomorphic to A^vee,
and


```math
(A\oplus 1)^{\rm ss}\bmod\pi =
 (\bar a\bar\lambda^{-1})\oplus 1\oplus
 (\bar a^{-1}\bar\lambda^{-1}).
```


The statement about conjugate self-duality uses the pairing on
W from det W=1 and the rational origin of sigma. Twisting by
the anticyclotomic lambda^(-1) preserves the conjugate pairing.
The original finite inertia labels on G_L are retained:
the new outer labels are chi'^± lambda^(-1), with middle
label 1. At ell the inertia exponents of the ordered flag
on the direct sum, with the middle line inserted, are m,0,-m.
In particular no CM extension has to trivialize lambda to
construct this *reducible* automorphic datum.

Here is the automorphic interpretation with a normalization check.
Let pi_f be the unitary cuspidal GL2 representation of the
newform, and use its contragredient for the geometric-Frobenius
normalization of the parent. Its solvable base change to L
is cuspidal: cyclic base change can fail to be cuspidal only
through a self-twist trivial on the next subgroup, contrary to
the strong irreducibility just checked. Twist it by the finite
Hecke characters whose geometric Artin avatars are chi'^(-1)
and lambda^(-1) on G_L. Denote this unitary GL2 constituent
by Pi_2. For a good prime of norm Q and arithmetic eigenvalues
alpha,beta of r_f, the Satake eigenvalues before the finite
twists are Q^m(alpha^(-1),beta^(-1)). With the twists they are
exactly the geometric eigenvalues of A. Thus


```math
\Pi_{\rm end}=\Pi_2\boxplus 1
```


is an ordinary conjugate-self-dual isobaric automorphic
representation of GL3 over L, with integral, distinct infinity
parameters m,0,-m and the residual characteristic-polynomial
identity above in the parent normalization. Multiplying the
geometric eigenvalues by Q gives the algebraic GL3 normalization,
namely (A plus 1) epsilon^(-1). This is why one must not insert
the half-norm twist from the parent *GL2* algebraic normalization
into the GL3 isobaric sum.

This argument constructs the ordinary endoscopic starting packet
at auxiliary weights m, using the proved rank-two supplier.
It does not construct a cuspidal GL3 packet or a lattice whose
point lies on the desired irreducible component. In particular
it is not an irreducible point of the original fixed-weight
ring: both the auxiliary weight and the original block shape
matter. The rank-two theorem is used with its stated arithmetic
inputs, not assumed for every coefficient prime or host.

## 2. Why the original irreducible seed cannot simply be reused

The parent's other seed is an adjoint/symmetric-square lift of
a rational modular form. It is essentially orthogonal, even
after scalar twisting. For the actual cubic diagonal, every
essentially self-dual three-dimensional representation would
induce an involution chi -> mu/chi on the three residual
characters. For distinct characters this forces some
chi_i^2=chi_j chi_k, unless all three are fixed. For the three
characters here that relation says either lambda^2=1, or
a^3=lambda, or a^(-3)=lambda. All are impossible: lambda
has order three and a^c=a, whereas lambda^c=lambda^(-1).
If all three are fixed, their squared ratios are one, implying
lambda^4=1, also impossible.

The argument persists on every finite CM extension of F on
which the residual constituents remain distinct. Indeed
K/F is cyclic cubic and K is not contained in a CM field.
For a proof, any CM field has a central complex-conjugation
automorphism on its Galois closure, hence a totally imaginary
Galois subfield has central complex conjugation. The group of
K/Q is S3, with noncentral complex conjugation. Alternatively
every subfield of a CM field is CM or totally real. Thus lambda
remains nontrivial, and the conjugation calculation still works.
The symmetric-square obstruction therefore cannot be removed
by the permitted CM base change. This agrees with the full
SL3 connected monodromy theorem in
[cubic-irreducible-monodromy.md](cubic-irreducible-monodromy.md).

## 3. Audit of two published routes

* Jack A. Thorne, A p-adic approach to the existence of
  level-raising congruences, Proc. Lond. Math. Soc. 128 (2024),
  e12584, [DOI and full text](https://doi.org/10.1112/plms.12584),
  Theorem 6.11. This is relevant to replacing the 2+1 isobaric
  packet by a cuspidal ordinary representation. But it requires,
  among other conditions, Steinberg constituents at the raising
  place with a specified congruence of the unramified twists.
  In our construction the GL2 constituent at its exact
  central-character conductor is principal series, and at other
  prime-to-ell places it is unramified. No Steinberg place with
  the required congruence has been constructed. Base change and
  finite twisting of these local parameters do not create their
  missing monodromy operator. The additional CM splitting,
  parity, and generic-place hypotheses of 6.11 must also be
  checked for a genuine replacement seed. Theorem 6.11 is not
  being applied here. Even an appropriate cuspidal congruence
  at a new level would not by itself imply attachment of every
  irreducible point of the original fixed-weight, fixed-inertia ring.

* P. B. Allen, J. Newton, J. A. Thorne, Automorphy lifting for
  residually reducible l-adic Galois representations, II,
  [arXiv:1912.11269v2](https://arxiv.org/abs/1912.11269),
  Compos. Math. 156 (2020), 2399--2422, Theorem 6.1(4)--(6).
  Besides the Steinberg hypotheses, this theorem requires
  individually conjugate-self-dual residual constituents
  with the same polarizing multiplier. In the multiplier-one
  normalization the three individual conjugate products
  chi_i^c chi_i are a^2,1,a^(-2). They are not all one.
  A scalar twist multiplies all these products by the same
  scalar character and does not remove the mismatch. On a
  CM restriction where a^2 becomes trivial, the two outer
  residual constituents coincide. Thus the simultaneous
  distinctness and individual polarization hypotheses cannot
  be arranged in this way. Large connected characteristic-zero
  monodromy is not large *residual* image. Thorne 2024,
  Theorem 7.5, retains this same individual-polarization
  restriction.

The high-dyadic corner-elimination theorem is for the
original fixed-inertia ring. It does not assert the absence
of a type-E stratum of an auxiliary variable-weight
deformation ring. Hence it does not justify omitting an
auxiliary propagation step which uses that stratum.

## 4. The additional auxiliary class-rank input

The parent auxiliary tower in
[AT1--AT3](../../paper/shared/selmer-integral-frontier-auxiliary-tower.tex)
uses a fixed abelian residual splitting field E over Q and
bounds the ell-ranks of its class groups through the cyclotomic
ell-tower by Ferrero--Washington. For the actual cubic
characters the residual splitting field must also contain K.
Indeed the residual cubic character is faithful (ell>=5),
and in the two outer labels its cubic factor can be separated
from the rational characters by conjugation. Thus the analogous
field is K E_m, where E_m contains F and is abelian over Q.
Since K/F has degree three, K and E_m are disjoint over F.

The ell-primary part of Cl(K E_m) decomposes under the
cyclic order-three group, after an unramified coefficient
extension containing the third roots of unity. Norm and
extension of ideals identify its invariant summand with
Cl(E_m){ell}: their composites are multiplication by 3
and the group norm respectively, which act invertibly on
the invariant ell-primary summand. This holds for every
layer and is compatible with the norm maps. Ferrero--Washington
therefore bounds the invariant part, but supplies no bound
for either nontrivial cubic part.

A sufficient additional tower hypothesis is mu=0 for
the nontrivial cubic components of the unramified cyclotomic
Iwasawa module of K E_0 at ell. By the structure theorem
this bounds the minimal number of ell-generators of the
inverse-limit components, and hence of the class-group
components of sufficiently deep layers (norms become
surjective when the cyclotomic steps are ramified).
Conversely, bounded ranks at every layer imply finite
generation over Z_ell of the norm inverse limit by compactness
and Nakayama; in the standard torsion Iwasawa module this
excludes an elementary mu factor. This explains the precise
strength of the new rank-bound input in that proof route.
The abelian mu theorem alone cannot supply it, and the
cubic-prime 2 and 3 calculations do not concern these
varying ell>=5 towers. We leave this input open rather
than treat mu=0 for this nonabelian extension as established.

## 5. Priority

The cleanest remaining route is to obtain an irreducible
ordinary rank-three automorphic starting packet with the
actual cubic characters, and a support/propagation theorem
controlling the actual trace algebra (including the
characteristic-prime fibre). The endoscopic datum above is a
concrete candidate starting point for a new congruence
construction, not an assertion that the necessary level
raising or propagation is automatic. The direct field method
and higher-rank Euler systems remain reserved for the
lower-dyadic cross-block cases. Neither of the two original
point premises is closed by this note.

## Subsequent arithmetic alternative

The [pure-cubic descent](pure-cubic-selmer-descent.md) and [finite class-rank certificates](cubic-finite-class-rank-certificates.md) now reduce the actual cubic component to a degree-three companion and give a sufficient finite arithmetic test for the new auxiliary rank bound. The [two-negative elimination](cubic-two-negative-weight-elimination.md) discharges the point premises on sectors satisfying the finite vanishing criterion. These are partial alternatives to the seed construction, not a general cuspidal attachment or curve exclusion theorem.
