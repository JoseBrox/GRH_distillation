# The cubic coefficient interface: exact Selmer reduction without a new CM field

24 November 2026. This note identifies the reusable integral
cohomological part of the Dirichlet program for the proposed cubic
comparison. It is a genuine decomposition for the fields in
[cubic-relative-comparison](cubic-relative-comparison.md), not a
uniform Selmer bound or a construction of the required theta maps.

## 1. The CM field and the non-CM extension

Write F=Q(omega), K=F(cuberoot(2)), and retain the actual fields
L_0=F R_h(sqrt(-q),sqrt(-d)) and L=K L_0 of the relative comparison.
The first is a CM field abelian over Q; the second is not CM.
The former is exactly the parent Dirichlet character host with fixed
base character chi_{-3} (order two, conductor three) and the same
dyadic real field and auxiliary quadratic factors, as in
[selection-assembly](../../paper/sections/recovered/34-sec-selection-assembly.tex).
The field also meets the key CM/unramified field condition: complex
conjugation is nontrivial on each of F, Q(sqrt(-q)) and Q(sqrt(-d)),
whereas at a finite rational prime at most one of these three factors
is ramified (their discriminants are pairwise coprime). At two the
inertia can act on the real dyadic field but on none of the three
imaginary quadratic factors. Thus complex conjugation is not in any
finite inertia group of L_0/Q; its relative CM extension over the
maximal real field is unramified at every finite prime. This proves
the field-level condition, not all original geometric/local hypotheses.

Over F the extension L/F is abelian, with G=C3 x B' where
B'=Gal(L_0/F)=C_{2^h} x C2^2. Its characters are lambda^r rho^N,
r=0,1,2, with rho the corresponding norm-pullback Dirichlet family.
Complex conjugation sends lambda to lambda^{-1} and fixes each
rho^N. The cubic character is still nontrivial on G_{L_0}.
It has conductor supported above 2 and 3.

## 2. Exact decomposition of the strict negative-twist groups

Fix a coefficient prime ell>=5 and an integer e>=1. Let O be the
integers of a finite unramified extension of Q_ell containing
all roots of unity of order |G|. Such an extension exists since
|G|=3*2^{h+2} is prime to ell. Write M=Frac(O)/O(-e),
with the negative cyclotomic Tate twist.
For a number field E and a Galois module N of this type define


```math
\mathcal S_E(N)=\ker\left[
 H^1(G_E,N)\longrightarrow
 \prod_{v\nmid\ell}H^1(I_v,N)\ \times\
 \prod_{v\mid\ell}H^1(G_{E_v},N)\right].
 \tag{1}
```


Here v runs over finite places, I_v is inertia, and the maps use
fixed embeddings of decomposition groups. This is the strict
condition unramified away from ell and zero at ell. One can
equivalently work with a maximal Galois group unramified outside
a finite set containing ell and the ramification of every module
and extension. All fields here are totally imaginary.
The analogous argument works for any additional zero or
unramified local conditions imposed compatibly at the corresponding
places. Do not identify it with a different Selmer condition
without the exact local check.

**Lemma.** Let E'/E be finite Galois abelian of order prime to ell,
let N be an ell-primary O-module with continuous G_E action, and
suppose O contains all character values of Gal(E'/E).
For the strict local conditions (1),


```math
\mathcal S_{E'}(N)=
 \bigoplus_{\psi\in\widehat{\operatorname{Gal}(E'/E)}}
 \mathcal S_E(N\otimes O(\psi^{-1})).
 \tag{2}
```


In this equality each summand is identified with the psi-eigenspace
by restriction, after trivializing the character on G_{E'}.

**Proof.** Inflation--restriction for 1 -> G_{E'} -> G_E ->
Gal(E'/E) -> 1 gives the invariant isomorphism on H^1:
both group-cohomology terms H^1 and H^2 of the finite quotient
vanish because its order is invertible on the ell-primary module.
Twisting by psi^{-1} changes the quotient action on the restricted
H^1 by the factor psi^{-1}; hence invariants are exactly the
psi-eigenspace of the untwisted H^1.

The same inflation--restriction argument gives injectivity of
restriction on the decomposition groups and on inertia at each
place: their local indices divide [E':E] and hence are prime
to ell. The strict zero conditions, including inertia restrictions,
therefore descend and ascend under these identifications. In
particular, an originally ramified twist is not silently called
unramified; its local restriction must actually vanish.
For a zero condition at a chosen base place it is enough to check
one place above it for an invariant class; its conjugates satisfy
the same zero condition. The Fourier idempotents
|G|^{-1}sum_g psi(g)^{-1}g are integral over O, orthogonal and
sum to one. They preserve the strict subgroup because the
conditions are equivariant. This proves (2). QED.

**Application.** Use (2) for L/F, and separately for L_0/F.
All character twists of the O-module M which occur are the
actual finite characters of these fields. In particular,


```math
\begin{aligned}
\mathcal S_L(M)&\cong
 \bigoplus_{r=0}^2\bigoplus_\rho
   \mathcal S_F(M\otimes O((\lambda^r\rho^N)^{-1})),\\
\mathcal S_{L_0}(M)&\cong
 \bigoplus_\rho\mathcal S_F(M\otimes O((\rho^N)^{-1})).
\end{aligned}
\tag{3}
```


Conjugation of F interchanges r=1 and r=2, fixes the
norm-pullback and cyclotomic characters, and permutes the local
conditions in (1). Thus the two nontrivial cubic sectors have
the same lengths, character by character.

Use finite coefficient extension from Z_ell to O.
Cohomology and the strict kernels commute with it because O is
finite free over Z_ell; on finite modules, normalized lengths
are preserved (ell is a uniformizer of O). Hence whenever the
groups are finite, for the original Z_ell-coefficient strict
negative-twist groups S(E,ell,e) we obtain the exact identity


```math
\begin{aligned}
\operatorname{length}_{\mathbf Z_\ell} S(L,\ell,e)
&=\operatorname{length}_{\mathbf Z_\ell} S(L_0,\ell,e)\\
&\quad+2\sum_\rho
 \operatorname{length}_O
 \mathcal S_F(M\otimes O(\lambda(\rho^N)^{-1})).
\end{aligned}
\tag{4}
```


We used inversion of the cubic label to write lambda rather
than lambda^{-1}; the equal-length assertion justifies it.
Qualitative finiteness for the strict negative-twist groups in
the finite fields is available from the parent's
[coarse Selmer budget](../../notes/coarse-selmer-budget.md)
with its stated K-theory/duality hypotheses. Equation (2) also
holds before invoking finiteness.

This isolates exactly the **already studied abelian part**:
the r=0 term is the negative-twist group over the Dirichlet
host L_0 with base character chi_{-3}. The genuinely new
part is a sum of rank-one twisted groups over the single
fixed Eisenstein field F, with two equal cubic sectors.
No growing base-field degree appears in the new Selmer
coefficient problem. This is not yet a bound for that sum;
nor do we claim the parent program has finished its entire
uniform bound for the abelian term.

Via Shapiro one may instead express each new group over Q
with coefficient representation


```math
\operatorname{Ind}_{G_F}^{G_\mathbf Q}O(\lambda)
       \otimes O(\rho^{-1})\otimes \operatorname{Frac}(O)/O(-e).
\tag{5}
```


The induction has rank two and fixed finite monodromy S3.
The equality of the zero and inertia-kernel conditions follows
from local Mackey decomposition, or explicitly by restricting
cochains to the two G_F cosets: at each rational place the
induced local module is a direct sum of the modules induced
from the decomposition groups of its primes in F. The
unramified condition follows by the same decomposition on
inertia; equivalently it is the kernel of the restrictions to
the inertia subgroups in those Mackey factors.
Thus (5) is a fixed-rank formulation, not a replacement of
the nonabelian representation by Dirichlet characters.

The ell=2 and ell=3 components are **not** covered by (4).
They require separate integral estimates. Even in the
prime-to-three decomposition, the parent uniform weighted
Selmer bound remains a serious problem. The source's fixed-field
rank-three automorphic trace argument already uses F=Q(sqrt(-3))
in its nonresonant RH case
([nonresonant note](../../notes/rh-selmer-nonresonant.md),
[fixed-field spectrum](../../notes/selmer-support-continuation-spectrum.md)).
This motivates trying to extend that actual local/model/count
theorem to the new rank-one coefficients over F.
The source hypotheses involve explicit diagonal characters,
polarizations and point conditions: they have not been verified
for the cubic-twisted groups in (4).

## 3. Fixed cubic character projectors have only a fixed denominator

Here is a separate integral lattice supplier for a possible
geometric realization by a cubic local system. Let O now be any
DVR of characteristic zero containing omega, and let V be a finite
free O-module with an integral order-three action u.
Write V_j=ker(u-omega^j) for j=0,1,2. Over the fraction field
the three projectors are


```math
e_j=\frac13\sum_{k=0}^2\omega^{-jk}u^k .
```


Their images are the three eigenspaces. Each 3e_j V lies in
V_j, and their sum is 3V. Thus


```math
3V\subset V_0\oplus V_1\oplus V_2\subset V .
```


Consequently the integral splitting quotient is killed by 3,
and its length is at most rank(V) times v_O(3).
This is exact splitting at every coefficient prime except 3,
and a bounded per-rank index cost at 3. For a Hermitian lattice
over the integers of a number field containing omega, with
invariant positive metric, the eigenspaces are orthogonal at
each embedding, and the log index is at most
[field:Q] rank(V) log 3. This follows simply from the
inclusion above. All lattice statements use the actual
integral action, not a chosen rational splitting.

This is unlike the growing dyadic projection cost of the
parent program: the new cubic factor itself has fixed order.
It supplies no bound on the growing dyadic factor or the
actual ranks. Any arithmetic map must intertwine the action
before its restriction to these eigenspaces can be used.

## 4. A unitary coefficient twist preserves the adjoint input

A rank-one lattice O(lambda) with root-of-unity action
exists over the actual CM field L_0, without adding K to the
field of endomorphisms. The action is unitary for the standard
positive Hermitian metric and has finite monodromy. At primes
above ell>=5 it is unramified, since lambda is ramified only
above 2 and 3. Thus a scalar twist of a Galois representation
over L_0 changes no local Hodge--Tate weights and preserves
crystalline conditions at those coefficient primes.

More generally, let Gamma have an involution c and a finite
order character tau with tau^c=tau^{-1}. If
r^c is isomorphic to r^vee tensor mu, then r tensor tau
has the same conjugate-self-dual multiplier mu.
The endomorphism module is literally unchanged:
conjugation by tau(g)r(g) acts on End(V) by conjugation
by r(g). The same applies to its polarized adjoint
if the polarization is transported by the unitary twist.
For a framed deformation problem over O, twisting
r(g) -> tau(g)r(g) and untwisting by tau^{-1} give inverse
natural transformations on every coefficient algebra.
Ordered flags stay the same, and each specified diagonal
character is multiplied by tau; ratios are unchanged.
For transported conditions, the tangent and relation
modules, and hence their integral lengths, are unchanged.
At ell=2,3 the original local conditions must be checked
rather than assuming an unramified twist.

This supplies an elementary preservation theorem for a
*common* scalar twist of a prescribed polarized deformation
problem. It is not a construction of the new Selmer
groups (4) from the old ones. In particular, the fact
that a common twist cancels in the adjoint means that
it cannot by itself introduce a new cubic eigencharacter
into the relative diagonal ratios. A tensor twist also
preserves existing integral map norms but does not by
itself change their arithmetic divisor count to the
required prime-ideal count (4) of the relative comparison.

## 5. The next construction obligation

Retain the CM host L_0 and use an actual finite unitary
coefficient system with cubic monodromy, rather than
adjoining the non-CM splitting field to its endomorphism
field. The fixed cubic denominator, exact prime-to-six
cohomological decomposition and common-twist adjoint
identification above are available for that construction.

The first missing input is an equivariant integral
theta/divisor map whose Frobenius contribution is the
relative kernel (1) in cubic-relative-comparison.
Only after that identification may one transfer the
parent section, degree and frame inequalities or decide
which exact strict Selmer condition enters its denominator.
If it uses the negative-twist groups in (1), their new
prime-to-six part is exactly (4), over fixed F.
The integral special primes and uniform bound for
the new cubic sectors are open. No conclusion about
the cubic prime discrepancy follows merely from
these module identities.

Proof scope: finite group cohomology, restriction,
local Mackey decomposition, integral idempotents and
transport of deformation problems are proved or stated
with their exact classical inputs. No new source
automorphy lift, integral theta map or Selmer length
bound has been obtained. The arithmetic and geometric
compatibility is still the decisive open obligation.
