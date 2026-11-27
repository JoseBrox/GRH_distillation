# Definite base change: the trace transfer and label step

We prove the weighted class-trace comparison and extraction of a labelled
eigenvector once the actual matching roots and levels exist. We also prove
the rational descent of the norm-one cocycle and the integral local
cocycle splitting at split unramified places. The [global norm-root chapter](lsernau-global-norm-roots.md) now supplies the global matching-root existence and the general matching compact-level construction. The [specific Hecke transfer chapter](lsernau-specific-hecke-transfer.md) supplies the transfer levels and matching products. Split-case attachment and labelled local-global compatibility remain.

Throughout, E'/E is one of the source's cyclic prime-degree CM steps.
Write sigma for its generator, p for its degree, and j for the two
inclusions on rational and finite adelic unitary groups. Both rational
groups are definite. The image of j consists precisely of the
sigma-fixed elements, by Galois descent of matrix entries. Write
N_sigma(a)=a sigma(a)...sigma^{p-1}(a).

## 1. Rational descent of a locally split cocycle

Suppose s is a rational unitary matrix over E' with N_sigma(s)=1,
and is a unitary coboundary in the finite adeles. Matrix Hilbert 90
gives s=g_0 sigma(g_0)^{-1} with g_0 in GL_n(E').
The Hermitian matrix H=g_0^*g_0 is sigma-fixed, because s is unitary.
It therefore defines a nondegenerate Hermitian form over E.

At every finite place of the maximal real subfield of E,
a unitary adelic solution t gives t^{-1}g_0 sigma-fixed, and

\[
 H=(t^{-1}g_0)^*(t^{-1}g_0).
\]

Thus H is locally isometric to the standard form at every such place.
At the infinite places it is positive definite, as is clear in an
embedding of E' extending the embedding of E. By the classical
local-global theorem for Hermitian forms over quadratic extensions
(Landherr's theorem), H=r^*r for some r in GL_n(E).
Then g=g_0 r^{-1} is rational unitary and
s=g sigma(g)^{-1}. This proves exactly the rational unitary
coboundary assertion used below. It does not assume all unitary
cocycles split without the local hypothesis.

At a split place of E inert and unramified in E', the local
unitary group at the paired places is GL_n of the local field.
For its maximal integral compact K'=GL_n(O'), every norm-one
sigma-cocycle splits in K'. Indeed an integral cocycle s makes
(O')^n a module with descent datum, with semilinear action
v -> s sigma(v). The norm-one condition is precisely the descent
identity. Faithfully flat descent along the finite etale Galois
extension O'/O gives a finite projective O-module whose base
change is (O')^n. It is free of rank n because O is a DVR.
The columns of a descended basis form t in GL_n(O') with
s sigma(t)=t. Thus s=t sigma(t)^{-1}. No division by p is
involved, so this includes the unramified residue-characteristic-p
case. For a split extension of local fields use the same descent
argument for the product of the unramified rings, or choose the
basis on one component and transport cyclically; norm one makes
the last transport consistent.

The cocycle condition at more general source matching subgroups
(e.g. prescribed ramified congruence levels) is not a consequence
of this assertion.

## 2. Class traces as weighted groupoid sums

Let Gamma be the rational unitary group inside the finite adelic
group G, L an open compact subgroup, and V the finite-dimensional
coefficient representation rho of Gamma. The forms in question
are functions phi satisfying phi(a x l)=rho(a)phi(x).
Since the group is definite, the double-class set is finite
and each stabilizer Gamma_x=Gamma intersect x L x^{-1} is finite.
Evaluation at representatives identifies this form space with
the direct sum of V^{Gamma_x}. Use Haar volume one on L.

Let f be a compactly supported bi-L Hecke function and sigma an
automorphism preserving L and Gamma. Assume s on V intertwines
rho(a) with rho(sigma(a)), and let S phi(x)=s phi(sigma^{-1}x).
The trace of T_f S is

\[
 \operatorname{tr}(T_f S)=
 \sum_{x\in\Gamma\backslash G/L}
 \frac1{|\Gamma_x|}\sum_{a\in\Gamma}
 f(x^{-1}a\sigma(x))\,\operatorname{tr}(\rho(a)s).
 \tag{1}
\]

Here and below matrices of the coefficient action refer to the
source's convention, not to a new contragredient.
To verify (1), consider the diagonal block of the convolution
on the summand V^{Gamma_x}. Only cosets hL for which
sigma^{-1}(xh) is in Gamma x L contribute. They are of the
form hL=x^{-1}a sigma(x)L, and the possible a for each coset
form a right coset of sigma(Gamma_x). On V^{Gamma_x}
the action is rho(a)s, independent of this choice.
The projector onto V^{Gamma_x} is the average of rho(b)
over b in Gamma_x. Compute the trace by inserting this
projector and use s rho(b)=rho(sigma b)s to sum over all a
once, with the displayed denominator. Equivalently the trace
on the direct summand is the trace on V of that diagonal block
composed with the projector. The sum is finite because f
is compactly supported and Gamma is discrete in the finite
adeles of this definite group. The untwisted trace is (1)
with sigma=s=1.

Suppose L is contained in a compact subgroup C and f is invariant
under C-twisted conjugation. Consider pairs (x,a) modulo the
moves

\[
 (x,a)\mapsto (b x c,\ b a\sigma(b)^{-1}),
 \qquad b\in\Gamma,\quad c\in C.
\]

Their summand in (1) is invariant. The finite automorphism group
of a pair is the intersection of its twisted rational centralizer
with x C x^{-1}. Refining from C to L gives, over each such pair
class, the orbits of its automorphism group on C/L (left action
through x). The sum of reciprocal stabilizer orders is
[C:L] divided by the original automorphism order, by the ordinary
orbit-stabilizer formula. At level L, conjugation orbits of a under
Gamma_x similarly turn the inner sum of (1), divided by |Gamma_x|,
into reciprocal automorphism weights. Consequently (1) divided
by [C:L] is exactly the sum over pair classes at C with those
weights. This remains valid when C is not sigma-stable: the
equivalence relation uses right C on x and the assumed twisted
conjugation invariance of f. Only L needs sigma-stability to
define S on the form space. The trace is a finite weighted sum,
not a count of conjugacy classes without automorphism weights.

In the base-change weight, the representations at the embeddings
over one base embedding are tensor factors permuted cyclically by s.
For linear maps A_1,...,A_p on the corresponding coefficient space,
the trace of the cyclic permutation composed with their tensor
product equals tr(A_1...A_p), with the ordering induced by that
permutation. This follows directly by expanding in tensor bases.
Therefore when N_sigma(a) is conjugate to j(gamma), the twisted
coefficient trace in (1) is the original coefficient trace at
gamma. This is the actual base-change weight normalization:
there is no factor p or extra dimension factor.

## 3. Compare the pair groupoids under the matching-root input

Here is the precise remaining input from the source's global
norm-root argument. For good rational elements nu over E'
(in a conjugation-stable set containing the norms on support),
let A_nu be rational unitary and B_nu finite adelic unitary,
both equivariant under ordinary conjugation by rational
unitary matrices. The matching-root identities supply:

* A_nu and B_nu commute with nu; for eta=j(gamma) good,
  N_sigma(A_eta^{-1})=eta;
* on a supported target pair (x,delta), with nu=N_sigma(delta),
  the element A_nu delta has norm one and its twisted conjugate
  by B_nu x lies in C;
* the test functions match on
  (x_0,gamma) -> (B_{j(gamma)}^{-1}j(x_0),A_{j(gamma)}^{-1})
  for good gamma, including zero values, and a nonzero source
  summand is good.

These are the outputs of exists_isMatchingRoots and the
matching-function property in TwistedTraceIdentity.lean.
They are proved in the global norm-root chapter from the
source's IsStep and the actual matching test functions.
Assume also every norm-one cocycle in C splits in C.
Put C_0=j^{-1}(C), L_0=j^{-1}(L).

Denote the displayed pair map by m. At good pairs it gives
a map of the source pair groupoid to the target groupoid,
because A,B are conjugation-equivariant and j(C_0) lies in C.
It is fully faithful: a rational target move b from m(p)
to m(q) intertwines the twisted norm elements, hence conjugates
the corresponding eta_p,eta_q. Equivariance of A changes the
twisted conjugacy relation for A^{-1} into sigma(b)=b.
Thus b descends to a unique rational move over E.
Equivariance of B changes the condition on the finite
coordinates into exactly membership in C_0. In particular
pair automorphism groups are isomorphic.

To verify essential surjectivity on the supported pairs, let
(x,delta) be a target pair, and write nu=N_sigma(delta).
By the norm-one and C-membership assertions, choose k in C
such that

\[
 A_\nu\delta
   = B_\nu x k\,\sigma(B_\nu x k)^{-1}.
\]

The preceding rational descent gives a rational unitary g with
A_nu delta=g sigma(g)^{-1}. Thus
g^{-1} B_nu x k is fixed by sigma and descends to y.
Also g^{-1}nu g is fixed: the identity
delta sigma(nu)delta^{-1}=nu and commutation of A_nu with nu
give this by substituting the coboundary identity.
Write g^{-1}nu g=j(gamma). Then conjugation equivariance
of A,B shows

\[
 m(y,\gamma)
   =(g^{-1}xk,\ g^{-1}\delta\sigma(g)).
\]

This is equivalent to (x,delta) in the C-groupoid.
The source pair is good since its norm is conjugate to nu.
This proves essential surjectivity without an additional
assertion about uniqueness of the root polynomials.

The two weighted groupoid sums are consequently equal by
the matched test functions, the tensor trace identity, and
the automorphism group isomorphisms. Undoing the level
refinement from section 2 proves

\[
 \operatorname{tr}(T_{f'} S)
   =\frac{[C:L]}{[C_0:L_0]}\operatorname{tr}(T_f).
 \tag{2}
\]

The constant is nonzero and independent of the Hecke functions.
This is the source trace identity with its exact level scalar,
conditional only on the stated matching-root and compact-cocycle
inputs. It is not an appeal to a general base-change theorem.

## 4. Spectral extraction from the trace identity

Let W,W' be the actual finite-dimensional spaces at the
transfer levels. The source has commuting families of Hecke
operators, with a subfamily T_i,T'_i to be matched. Let B,B'
be the distinguished local operators, commuting with the
families. The matching-pair set contains (B,B') and is closed
under multiplication by (T_i,T'_i), with the common choice
of matching product. Thus (2) implies, by linearity,

\[
 \operatorname{tr}\big(P(T'_i) B' S\big)
     = c\,\operatorname{tr}\big(P(T_i)B\big)
 \tag{3}
\]

for every polynomial in finitely many generators, with the
same nonzero c. We require only this multiplicative closure,
not an assertion that arbitrary matching functions multiply
under convolution.

Even an infinite family of commuting endomorphisms on a
finite-dimensional complex space has finitely many joint
generalized characters: the commutative finite-dimensional
algebra it generates is Artinian, with primary decomposition
into its local factors. Include both spaces in this argument
via direct sum. If a prescribed character theta occurs in W,
finitely many of the named generators distinguish it from
all other characters on W or W'. For each such generator take
a polynomial equal to one modulo a sufficiently high power
of X-theta_i and zero modulo the corresponding powers at
the other eigenvalues. The Chinese remainder theorem gives
these polynomials. Their product P is the projector to the
theta block on both spaces. It is exact even with nilpotents.

If tr(B|W_theta) is nonzero, (3) shows
tr(P(T'_i)B'S) is nonzero. Decompose W' under the full spherical commuting family,
which S permutes by sigma; no corresponding assertion about
the local generators is needed. Both P' and B' preserve
these spherical blocks. A block moved by S contributes zero
to the trace. On a sigma-fixed spherical block V, P'B' must
therefore have nonzero image. That image lies in the selected
local generalized eigenspace and is invariant under the whole
commuting family. Simultaneous
triangularization supplies a common eigenvector in that image.
Its eigenvalues are the chosen character, and in particular
match theta and are constant on the sigma-orbits of the
spherical operators. This also applies when B' is not
self-adjoint or invertible.

The specific Hecke transfer chapter proves the actual
transfer-level existence and stability of matching products.
Together these arguments prove the required weak transfer
eigenvector, including the choice in the image of the
distinguished local operator. No positivity of the twisted
trace on the target is used.

## 5. The finite Shintani label step

At the split inert unramified place of section 1, reduction
on the maximal compact commutes with sigma, and the preimage
of the upstairs principal reduction kernel is the downstairs
principal reduction kernel. If an integral element a has
twisted norm conjugate to an element b of the base group,
its residue satisfies the corresponding identity in the
semidirect product GL_n(k') semidirect <sigma>:
(a_bar,sigma)^p=(N_sigma(a_bar),1).
This is just multiplication in that semidirect product.

Suppose the source supplies a common finite Shintani character
F on that semidirect product, whose value on the sigma coset
descends to the desired downstairs character Xi and whose
restriction to GL_n(k') is Xi'. We use the genuine-character
case (the source Lift Nat condition), not arbitrary class
functions or virtual differences. Inflate by reduction and
extend by zero off the compact. Twisted-conjugation invariance
follows directly from the class-function property of F.
Given matching roots for the compact indicators, their support
and norm assertions give exactly the matching value assertion
for the inflated functions by this semidirect-product identity.
Thus no new norm-root problem is needed for the labels.

On a finite-dimensional representation of GL_n(k), the
group-algebra element with coefficients conjugate(Xi(g))
acts on an irreducible type lambda by the nonnegative
scalar |GL_n(k)| m_lambda/dim(lambda), by Schur orthogonality.
If the original vector has the label Xi, this operator is
nonzero on it. On every invariant finite space containing
that vector its trace is therefore strictly positive.
This supplies the nonzero local trace condition in section 4.

Upstairs, put

\[
 a=\sum_{g\in GL_n(k')}\overline{F(g,\sigma)}\,g,\qquad
 b=\sum_{g\in GL_n(k')}\overline{\Xi'(g)}\,g.
\]

Realize F as the character of a genuine representation R of
the semidirect product. The coefficients of a are conjugates
of tr(R(g)R(sigma)), hence linear combinations of conjugate
matrix coefficients of the irreducible types occurring in
R restricted to GL_n(k'). Schur orthogonality shows that a
acts by zero on all other types. The central operator b is a
strictly positive scalar on each occurring type. Consequently
a nonzero vector in the image of a cannot be killed by b.
Apply this to the eigenvector of section 4 with B'=a:
it has the upstairs label Xi'. This proves the label extraction
from the common finite Shintani character and the matched
global trace, including the genuine-character hypothesis
needed for the positivity downstairs.

This argument does not establish Galois local-global
compatibility for the labelled form. In particular the tame
inertia polynomial and all-powers trace identities used by
the local derivative proof still require that theorem.

## Source dictionary

All references are to
[lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).

* Lib/GaloisRep/BaseChange/TwistedTraceIdentity.lean,
  221--330, 340--456, 718--end, blob
  0adf2e660e4bee51900e69cb5977f1c6f092c835.
* Lib/GaloisRep/BaseChange/PrimeDegreeTransfer.lean,
  699--890, blob 6562ac0946077ceb1e2eb1fa40b471eb82862d8a.
* Lib/GaloisRep/BaseChange/ShintaniLift.lean,
  244--414, blob c2cba274166782b15801cafda74dfef3f3f3901c.

The weighted trace and spectral/label arguments are proved
with the precise source global matching inputs retained.
The local descent and rational coboundary argument use
classical Hilbert 90, Landherr and faithfully flat descent.
Global matching roots and the matching compact family are
now supplied in the linked chapter. The specific transfer levels
and matching products are proved in the specific transfer chapter.
The actual common finite Shintani characters remain. The
subsequent local-global attachment theorem is separate.
No new Lean replay is asserted.
