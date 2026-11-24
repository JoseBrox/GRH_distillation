# The moving 3-primary cubic sectors: exact local lifting defects

24 November 2026. This supplements the
[fixed-conductor window](cubic-fixed-conductor-selmer-window.md)
and [high-dyadic vanishing](cubic-three-primary-vanishing.md).
It removes the high-conductor restriction from the *local*
finite-modulus comparison at 3, with a uniformly bounded loss,
and gives an aggregate bound on residual generator ranks in the
actual moving host. It does not prove the remaining uniform
3-primary lengths.

## 1. The exact conductor at 3

Let F=Q(omega), K=F(cuberoot(2)), and lambda the cubic character
of K/F. Its conductor divides 6 O_F, and it is ramified of order
three at the unique prime above 3 (see
[cubic two-primary window](cubic-two-primary-window.md)).
The conductor exponent there is exactly two: 3 O_F is the square
of that prime, and a nontrivial cubic character on inertia cannot
factor through the residue unit group of order two.

By contrast, the unique order-three cyclotomic extension at this
local field is F_v(mu_9), and its nontrivial characters have
conductor exponent three. Indeed the discriminant of Q(mu_9)
is 3^9 and that of F has absolute value 3. The relative
discriminant at the unique prime of F is therefore of exponent
six. The abelian conductor-discriminant identity and equality
of the two inverse character conductors give exponent three.
These computations also show that K_v and F_v(mu_9) are
different cyclic cubic extensions. All cyclotomic layers here
are totally ramified.

Let epsilon denote the 3-adic cyclotomic character. Its image
on inertia at v is 1+3 Z_3, and its unique nontrivial quotient
of order three is the one just described. If lambda on inertia
were trivial on the kernel of epsilon, it would factor through
that image. It would agree on inertia with one of the two
order-three cyclotomic characters, giving conductor exponent
three instead of two. Thus there is an inertia element g with
epsilon(g)=1 and lambda(g) a primitive cube root. This element
is independent of the Tate exponent and the auxiliary characters.

## 2. Local comparison at every finite coefficient modulus

Let rho be any actual host character from a real dyadic
cyclotomic layer and at most two moving quadratic fields of
odd prime conductors q,d>3. It has 2-power order and is
unramified at 3. Use its norm pullback rho^N to F. Let O be
a finite 3-adic coefficient DVR containing all character
values, with fraction field E, uniformizer pi, and put


```math
c=v_O(\omega-1)=v_O(3)/2,\qquad
 D=(E/O)(\varepsilon^{-e}(\rho^N)^{-1}\lambda^{\pm1}),
 \qquad e\ge1 .
```


The integer c depends on the choice of coefficient normalization
only. At the prime above 2, epsilon is unramified and lambda
has inertia image of order three. By raising a suitable inertia
element to a power of two one can kill the entire rho^N value
while retaining a primitive cubic value. At the prime above 3
use the element of Section 1; rho^N is unramified there.
It follows that the invariants of D under either of these two
groups (inertia at 2, full decomposition group at 3), and its
global invariants, are killed by omega-1.

More precisely, the residual character on G_F is just
the reduction of (rho^N)^(-1), because F contains mu_3.
On any of the three indicated groups, if the residual character
is nontrivial, the invariants are zero. If it is trivial, the
entire 2-power character is trivial there (reduction is injective
on prime-to-3 roots). All cyclotomic values on G_F are 1 modulo
3, so all values of the remaining character differ from 1 by
multiples of omega-1. The invariant group is exactly D[omega-1],
of length c, since we have exhibited an element attaining that
valuation. At all other inertia groups away from 3 the
coefficient action is prime-to-3 finite and the invariants are
either zero or the entire divisible module D.

For r>=1 write S(D[pi^r]) for the strict group on the finite
coefficient module, with exactly the same local restriction
conditions as S(D): unramified away from 3 and zero at the
full group at 3. Write s_r for its length. The exact sequence
of multiplication by pi^r gives


```math
s_r-\min(r,c)
 \ \le\ \operatorname{length}_O S(D)[\pi^r]
 \ \le\ s_r+2\min(r,c).
 \tag{1}
```


Here is the full kernel calculation. The global map
H^1(D[pi^r]) -> H^1(D) surjects onto its killed-by-pi^r
subgroup, with kernel D^{G_F}/pi^r D^{G_F}.
The inverse image of S(D)[pi^r] in this cohomology maps
by localization into the direct sum of the local kernels
D^H/pi^r D^H. Its kernel is S(D[pi^r]).
Only the two places just computed can contribute nonzero
local kernels, each of length at most min(r,c). The global
kernel is of length at most min(r,c) and is contained in
that inverse image. Taking lengths proves (1). These
bounds retain the integral torsion and do not assume the
local maps are injective in the low-dyadic range.

If rho has exact even dyadic conductor 2^b with b>=4, the
comparison is an isomorphism for every r. At 2 its residual
character is nontrivial on inertia because F is unramified
there. At 3, Frobenius on F_v has rational residue norm 3;
the value rho_2(3) of a primitive even character has exact
order 2^(b-2). Indeed 3 generates the units modulo sign in
the real dyadic cyclotomic group (the valuation of 3^(2^k)-1
is k+2 for k>=1). This order is at least four and cannot be
cancelled by an odd quadratic factor. Thus the local and
global invariant kernels vanish. This exact lifting range
does not require the larger conductor threshold of the
Bernoulli vanishing theorem.

In particular at every conductor and every r the *normalized*
possible loss in (1) is at most 1 (divide length by v_O(3)).
It does not grow with the number of dyadic characters.

## 3. An aggregate bound on the number of cubic generators

Put M=F R_h(sqrt(-q),sqrt(-d)), omitting any unused quadratic
field, with R_h the degree-2^h real dyadic layer. M/F is an
abelian 2-extension. Choose a coefficient residue field k
containing its characters. Let g_M denote the 3-rank
dim_F3 Cl(M)/3 Cl(M).

For each rho, D[pi] is k with character
theta_rho=(bar rho^N)^(-1). This statement is independent
of e and of the cubic sign. By restriction to G_M,
inflation--restriction (degree prime to 3) and class field
theory identify its unramified H^1 subgroup with a subspace
of the theta_rho-isotypic part of the k-valued unramified
additive characters of G_M. The strict condition at 3
is an additional restriction. The sum of the dimensions
of these subspaces over all distinct actual rho is at
most g_M: distinct characters of Gal(M/F) give distinct
isotypic components, and the 3-primary character module
is semisimple for this 2-group.

For b>=4 the preceding local comparison is exact. For b<=3
the correction at r=1 costs at most two dimensions per rho.
There are at most eight such rho (at most two even dyadic
characters of conductor dividing 8, times four quadratic
choices). Thus for each of the two cubic signs, and every e,


```math
\sum_\rho \dim_k S(D_\rho)[\pi]\le g_M+16.
 \tag{2}
```


These groups are finite by the qualitative K-theory finiteness
in the parent program after finite extension killing the
character, together with the finite inflation kernel.
For finite modules over a DVR the dimension killed by
pi is the minimal number of generators. Therefore (2) is
an actual uniform aggregate generator estimate for the
moving 3-primary cubic components, not an estimate of
their exponents or lengths.

An elementary numerical upper bound is
g_M <= log h(M)/log 3. For D_M=[M:Q], Minkowski gives
a representative of every class of norm at most
2^D_M sqrt(|disc M|); counting integral ideals up to that
bound by the Euler product at s=2 yields
h(M)<=8^D_M |disc M|. The cyclotomic discriminant bound
log|disc M| <= D_M log(3*2^(h+2)*qd) consequently gives


```math
g_M+16\ll 2^h(1+h+\log(qd)).
 \tag{3}
```


Constants are absolute (omit unused quadratic factors).
This bound is polynomial in the actual sizes of the
moving host and is independent of the twist exponent.
It cannot replace the common-window rank bound, which
must be fixed before the host degree and primes vary.

## 4. Unconditional vanishing of the completely untwisted sector

There is a useful small exception to the remaining length problem.
When rho^N=1, S(D)=0 at 3 for either cubic sign and every e>=1.

Restriction to K sends it into the strict negative Tate-twist
group of K, with scalar-extended coefficients. That group
vanishes by the fixed cyclotomic 3-primary tower calculation
in the two-primary window note. Inflation--restriction
therefore places S(D) inside
H^1(Gal(K/F),D^{G_K}). At the unique prime above 3 the local
extension K_w/F_v has the same degree-three Galois group.
Moreover D^{G_K}=D^{G_{K_w}}: on both groups the cubic
character is killed and the cyclotomic image is exactly
1+3 Z_3, since the cyclic cubic extension K_w/F_v is
not the first cyclotomic layer (Section 1). Its intersection
with the procyclic cyclotomic extension is trivial over
F_v, and hence so is the global intersection.
The local inflation--restriction map on this H^1 of the
degree-three quotient is injective. The strict full-local
condition at 3 then makes the inflated class zero.
This proves the assertion with integral coefficients.

## 5. Remaining problem

The moving low-dyadic sectors with auxiliary odd
conductors now have an exact local error bound and
the aggregate generator estimate (2). The missing
quantitative assertion is a bound on their integral
exponents or total lengths that fits the parent's
fixed-ratio common windows. A bounded residual rank
alone does not supply that assertion. In particular
we have not eliminated those moving exceptional
sectors by the fixed-field cyclotomic argument.

## Later actual nonvanishing example

The [q=139 construction](cubic-three-primary-nonvanishing-example.md) proves nonzero integral strict torsion at 3 for the two cubic signs of the quadratic sector of that admissible host, at every positive twist weight. Thus the remaining moving length problem cannot be replaced by a blanket zero assertion based only on the progression and cubic Frobenius conditions.
