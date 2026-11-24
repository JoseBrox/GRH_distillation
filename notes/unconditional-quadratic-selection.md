# Unconditional two-prime selection with the original congruences

24 November 2026. **Transfer from the Hecke track to ordinary RH and
Dirichlet GRH.** The entire analytic auxiliary-prime block needed by
our averaged corrected-ramp comparison is available without the
parent's uniform Dirichlet quasi-RH (QRH) assumption. The original
two-sign field, both exponential size ranges and every prescribed
congruence are retained. This is a replacement for the *analytic
supplier* in the [averaged comparison](one-construction-target.md);
it does not prove the stronger source all-height 399/400 zero-free
clause or any missing geometric construction.

The proof is also valid over any fixed number field for a fixed
finite-order Hecke family and the growing real dyadic auxiliary
layers, so it replaces the QRH input of
[general finite-order companions](../hecke/notes/general-finite-order-companions.md).

## 1. Precise theorem

Fix a number field F (possibly Q), a finite set Xi of primitive
finite-order characters of F, a fixed integer M>=1 containing
the bad rational primes of F and the fixed character conductors,
constants A,J>=1, and 0<epsilon<1/52. Let rho run through the
characters of the real dyadic cyclotomic layers of height at
most A(1+log U). Let B_U consist of the primitive realizations
of alpha rho^N for alpha in Xi, where N denotes norm pullback
to F. The constants, F, Xi and M are fixed before U grows.

Write d_F=[F:Q], z=U^(epsilon/5), z'=z(log U)^2,
Q=exp(z) and D=exp(z'). For sufficiently large U we can select
distinct rational primes


```math
Q/2<q\le Q,\qquad D/2<d\le D,\qquad
 q\equiv3\pmod8,\qquad d\equiv7\pmod{16},
```


prime to M, with q|(d+1) and every odd prime l<=z dividing
d+1. These imply the original ranges e^(z/2)<q<e^z and
e^(z'/2)<d<e^z' (if an upper endpoint is integral, omit it).
Consistent fixed extra congruences can be imposed.

Use the true corrected ramps G_beta over F: for a nonprincipal
character F_beta=-L'/L and G_beta(y)=R_beta(y)-y F_beta(1),
where R_beta sums log norm prime-power coefficients against
(y/n-1)_+. In the principal case subtract y log y-(1+c_F)y,
where c_F is the constant term of zeta'_F/zeta_F at 1.

For every alpha in Xi, each nontrivial companion
beta=alpha (chi_q^i chi_d^j)^N, i,j in {0,1}, i+j>0,
satisfies


```math
|G_\beta(y)|\le y^{1/2+\epsilon/2},\qquad
 |F_\beta(1)|\le 2d_F\log y
          \quad(U\le y\le U^J).
\tag{1}
```


Moreover all nontrivial quadratic companions of the entire
B_U are nonprincipal and zero-free in the closed box
Re s>=1-delta, |Im s|<=Q^2 for q-only companions and <=D^2
otherwise, for a fixed delta>0. The untwisted fixed characters
are not asserted to be zero-free in any such fixed-width strip.

For all U<=x<=U^J, all gamma in the whole family B_U and
its quadratic companions, including the principal character,
and every v>=exp(x^(epsilon/3))/3, one has


```math
|G_\gamma(v)|/v\le \exp(-x^{\epsilon/8}).
\tag{2}
```


This is the original thin target, not merely a power-saving
bound. For F=Q take Xi to contain all primitive characters of
conductor dividing 8M; then (1) is stronger than qs-bounds in
[parent Section 11](../paper/sections/recovered/11-qs-section.tex),
and (2) supplies its large-scale thin estimate at the exact
consumer scales, without assuming QRH. The proof of
[selection assembly](../paper/sections/recovered/34-sec-selection-assembly.tex)
uses the same field ranges and conductor bounds. The fixed
width **at every height** in the old selection theorem is
not part of this replacement; see Section 6.

## 2. Uniform prime correlations, retaining an exceptional bias

Use Thorner--Zaman, *Refinements to the prime number theorem for
arithmetic progressions*, Math. Z. 306 (2024), article 54,
[Theorem 1.1, arXiv:2108.10878v2 p.1](https://arxiv.org/pdf/2108.10878v2).
We checked the displayed theorem, including its relative error,
exceptional threshold and short-interval parameter. For an
interval (V/2,V] and reduced class a modulo m it gives a main
term


```math
\frac{1}{\varphi(m)}
   \int_{V/2}^V(1-\chi_*(a)t^{\beta_*-1})\,dt
```


times 1+O(E), when the modulus has its indicated exceptional
real character. Without it the integrand is one. Uniformly
for the moduli below,


```math
E\ll \exp\left(-c\frac{\log V}
    {\log m+(\log V)^{2/5}(\log\log V)^{1/5}+1}\right).
\tag{3}
```


The interval has log(V/h)=log 2, which accounts for the
bounded additional term. The theorem's lower-main-term
hypothesis is satisfied here: its (1.7) and the effective
bound 1-beta_* >> m^(-1/2) give a main term at least
V exp(-O(log m+1)), whereas log m=o(log V).
In particular it eventually exceeds V^(32/37+eta_0)
for any fixed sufficiently small eta_0>0. The same reasoning
applies to every refined reduced class modulo ms below,
even if the individual class is strongly suppressed.
The constants are independent of the class. We use the
relative error in (3), not an absolute PNT error divided by
a possibly very small main term.

Fix a positive integer L (it will be the polynomial cutoff
exponent in the moment argument), and an integer h>=1.
For q-selection take V=Q, and a fixed reduced progression
modulo a fixed m_0 divisible by 8 and the fixed bad primes.
Choose residue 3 modulo 8. For d-selection take V=D, and
the prescribed reduced progression modulo


```math
m=16q\prod_{3\le p\le z,\ p\ {\rm prime}}p
```


enlarged by any fixed required factors. Here q>z at large U,
so the indicated factors are coprime; the residue is 7
modulo 16 and -1 modulo every odd displayed prime. Chebyshev
gives log m=O(z). The cutoff products s will be odd
squarefree, (s,m)=1, s<=(2U^L)^(2h).
In either stage all moduli ms are <=H for some H with
log H=O_{h,L}(log U) at q-selection and O_{h,L}(z) at
d-selection. Enlarge H to at least 3.

By the classical Landau--Page theorem, for a fixed absolute
small c_0>0, at most one primitive real character of conductor
<=H has a real zero >1-c_0/log(3H); call it chi_* if it
exists, with zero beta_*. Choose c_0 also small enough that
this zero lies in the exceptional region in Theorem 1.1
for every modulus divisible by its conductor. Any exceptional
zero of a smaller modulus not in this global region has
t^(beta-1) <= exp(-c_0 log(V/2)/log(3H)). This contribution
is absorbed into an absolute relative-to-the-primary-main-term
error of the same form as (3) (its main-term factor is then
1+o(1)). Thus the *same single* exceptional character may
be used for all refinements ms.

In both stages (3), and this absorption, have size at most


```math
E_0=O_{h,L}(\exp(-c(\log U)^2))
\tag{4}
```


with fixed c>0: for q, the quotient log V divided by the
denominator grows as a positive power of U up to logarithms;
for d, log V=z(log U)^2 and the denominator is O(z).
In particular E_0 is smaller than every fixed negative power
of U.

Give the candidate primes l in (V/2,V] in the fixed class a
modulo m weight log l, and let W be the total mass. Every
candidate is >2U^L at large U. For s>1 coprime to m as
above the correlation is the average of the Legendre product
(l/s). To evaluate it, use the asymptotics for the classes
(a,b) modulo ms as b ranges over the units modulo s.
Each main term is positive (its integrand is positive
for t>1), and its error is bounded in absolute value by
E_0 times that main term.

There are three cases.

1. If the global exceptional conductor divides m, its character
   has constant value on all the refinements. The correlation's
   main term is zero by orthogonality, even if W is suppressed.
   Summing the errors gives |E(l/s)|<=O(E_0), because the total
   error is relative to the sum of the same positive main terms.
2. If that conductor does not divide m and does divide ms,
   its local part on the s-factor is a nontrivial quadratic
   character. The sum of the exceptional terms over b vanishes.
   The signed numerator against (b/s) vanishes unless the
   local character on s is exactly the primitive quadratic
   character (b/s). This can occur for at most **one** squarefree
   s>1, namely the part of the primitive exceptional conductor
   outside m (if that part is an odd squarefree number with
   the required coprimality; otherwise none).
3. If the global conductor does not divide ms, or there is no
   global exception, there is no retained exceptional term.

Hence for every relevant s>1,


```math
|\mathbb E(l/s)|\ll E_0
```


apart from at most one exceptional odd squarefree s_*, where
the trivial bound one is used. The total weight W is at least
V exp(-O(log m+1)) by the original progression estimate,
with log m fixed at the q stage. Consequently deleting any
O(V^a) candidates, for a fixed a<1, deletes o(W) weight,
including when the progression is exceptionally suppressed.
For d the constant in the O(z) modulus bound is uniform in
the previous q.

## 3. High moments, including the exceptional product

Before choosing the primes supply at most U^C coefficient
sequences b_i(p) on rational primes p<=2U^L,
with |b_i(p)|<=C_1 log p, where C,C_1,L are fixed.
Remove the prime 2 and all primes dividing the progression
modulus. Their absolute contribution is O(1+log m)=O(z),
which is o(sqrt t) uniformly for t>=U.
For the remaining primes quadratic reciprocity expresses
chi_l(p) as (l/p) times a sign fixed by p and the prescribed
class l=3 mod4.

For real coefficients expand the 2hth moment of the sum
up to t (handle complex coefficients by real and imaginary
parts). The all-even tuples have contribution at most
(2h-1)!! (sum |b_i(p)|^2)^h. Each other tuple has a nonempty
odd squarefree product s. If s is not the exceptional s_*,
its total contribution is bounded in absolute value by
O(E_0)(sum |b_i(p)|)^(2h), negligible for fixed h,L.
If s=s_*, let r be its number of prime factors.
A tuple contributing has r<=2h and even r.
Remove one occurrence of each of those primes. All remaining
multiplicities are even and can be paired. Counting the
choices of the removed positions and the pairings by
a constant depending only on h, this contribution is at most


```math
C_h \prod_{p\mid s_*}|b_i(p)|
          \left(\sum_{p\le t}|b_i(p)|^2\right)^{h-r/2}
 \le C_h\left(\sum_{p\le t}|b_i(p)|^2\right)^h .
\tag{5}
```


No assumption on the size or number of prime factors of the
exceptional conductor is required. This also proves the
general finite-moment version of the old single-exception
second-moment argument.

Chebyshev bounds the coefficient square sum by O(t log(2t)).
Thus the 2hth moment is O_h((t log(2t))^h), uniformly in the
progression and in the supplied sequences.
Markov's inequality and the union bound over O(U^L) integer
cutoffs and U^C sequences show that for any fixed eta>0
the proportion of candidate weight failing the bound
t^(1/2+eta) at some cutoff U<=t<=2U^L tends to zero,
by taking 2h eta>L+C+2. Fixed constants from forced
primes and complex splitting are absorbed by the same loss.
One may use floor U as the initial cutoff if U is not integral.

Choose q good for this collection, even after the permitted
O(Q^a) rejections. With q fixed, choose d good for the doubled
collection b_i(p) and b_i(p)chi_q(p), even after its own permitted
O(D^a) rejections. This gives every nontrivial combination of
the two auxiliary signs on the same whole finite windows.
The full congruences and the old asymptotic sizes are unchanged.

## 4. Select true zero-free boxes and corrections

For the genuine finite-order L-functions we may reject the
density-bad primes exactly as in
[the general Hecke theorem](../hecke/notes/general-finite-order-companions.md).
Here is the needed scope. Over a fixed F use the classical
log-free Hecke density estimate (Thorner, MRL 26 (2019),
Theorem 2.3, finite-order subfamily), in the weaker form
(H^2 T^d_F)^(3(1-sigma)) times a fixed power of log(HT),
for primitive conductors of norm <=H and height <=T.
For F=Q the standard log-free density theorem for primitive
Dirichlet characters gives the same needed form with an
absolute fixed exponent C(1-sigma) in Q^2 T; its precise
exponent is immaterial. Use Jutila, *On Linnik's constant*, Math. Scand. 41 (1977), 45--62,
[Theorem 1, (1.8)](https://www.mscand.dk/article/download/11701/9717),
which for 4/5<=sigma<=1 bounds the total primitive zero count by
O_epsilon((H^2 T)^((2+epsilon)(1-sigma))). The printed p. 46 has
been checked; take its fixed auxiliary epsilon equal to one.
The only property needed here is a fixed finite exponent.
These are established density theorems, not uniform
zero-free strips for all characters.

All conductors of B_U are polynomial in U with fixed
ramified support (including the dyadic prime), and
their finite-order infinity types are bounded.
New quadratic norm twists are genuinely ramified above
the new rational prime: at an unramified extension
of local fields the norm on units is surjective.
The base is unramified there. Thus distinct q in
q-selection give disjoint sets of witnessing primitive
companions, and similarly distinct d after fixing q
give disjoint witnessing sets for the d-only and qd
companions. At V=Q or D all norms of relevant conductors
are <=V^{C_2} with fixed C_2, and the box height is V^2.
Apply the density theorem at 1-2delta, with delta fixed
sufficiently small. It excludes O(V^{1/3}) candidate
primes with a companion zero in the smaller closed box
Re s>=1-delta, |Im s|<=V^2. The estimate already counts
the witnesses over the growing dyadic base family, so
no extra cardinality factor is needed. Section 2 shows
these rejections have negligible candidate weight.

Use the moment theorem on the actual coefficients
b_i(p)=a_alpha(p) for alpha in Xi, with loss epsilon/4,
up to 2U^L where L>J is fixed large enough that
L delta/2>J+epsilon/5+3. The actual prime-power coefficient
of the twisted Hecke function is a_alpha(n)chi_q(n)^i
chi_d(n)^j, including the absent factors at new ramified
primes. The local norm observation proves this, and
the elementary sum-of-residue-degrees argument gives
|a_alpha(p^k)|<=d_F log p. Higher rational prime powers
contribute O_F(sqrt t) to partial sums, so


```math
|P_\beta(t)|\ll t^{1/2+\epsilon/4}
       \quad(U\le t\le2U^L).
```


The cutoff Mellin argument in Section 3 of the
[cubic companion note](../hecke/notes/cubic-companion-selection.md)
now applies at the selected boxes, with actual conductor
logarithm O(z') and fixed degree. In detail choose smooth
V_0 equal to one on [0,1], zero on [2,infinity), X=U^L.
Shift the Mellin integral for
sum_n a_beta(n)V_0(n/X)/n from Re w=1 to -delta/2,
at height V^2/2. The local Hadamard log-derivative
estimate is O_delta(log(C_beta(3+|t|)^d_F)) in that strip;
all nearby zeros are separated horizontally by delta/2.
The residue at zero gives F_beta(1). The vertical error
is O(X^(-delta/2)(1+log C_beta)); horizontal and initial
tails are negligible by rapid cutoff-transform decay and
the exponential heights. Hence


```math
F_\beta(1)=\sum_n\frac{a_\beta(n)}n V_0(n/X)
                       +O(U^{-J-1}).
```


For U<=y<=U^J<X, subtract this genuine linear correction
from the ramp, obtaining
G_beta(y)=-P_beta(y)-y sum_{n>y}a_beta(n)V_0(n/X)/n
+O(y U^{-J-1}). Partial summation with the proved finite
window estimates gives O(y^(1/2+epsilon/4)).
For the derivative split the cutoff at U, bound the
initial part by d_F sum_{n<=U}Lambda(n)/n
=d_F log U+O_F(1), and the tail by O(U^(-1/2+epsilon/4)).
Absorb the fixed constants at large U. This proves (1).
No artificial finite logarithmic-derivative constant
is used.

## 5. The original exponential thin estimate follows classically

For all selected companions the possible real exceptional
zero of the usual Hecke or Dirichlet zero-free region has
been excluded by its selected box. Untwisted real characters
of B_U form a fixed finite set: the group of norm pullbacks
of the real dyadic character tower is the dual of a closed
subgroup of a procyclic Z_2 group, and has at most two
characters of order dividing two. For each fixed alpha,
the equation (alpha rho^N)^2=1 has at most two solutions.
The fixed possible exceptional zeros of these finitely
many characters are handled by shrinking the region
constant once. The principal pole is allowed.

Thus the whole family has the classical region of width
c/log(C_gamma(3+|t|)^d_F), with fixed c>0. Use the
smoothed Perron contour of Section 4 of the cubic companion
note (or Section 5 of the general finite-order theorem):
for v>=3 it gives, with fixed constants,


```math
|G_\gamma(v)|/v\ll
 (1+\log C_\gamma+\log v)^{B_1}
 \exp\left(-c_1\frac{\log v}
       {1+\log C_\gamma+\sqrt{\log v}}\right).
```


This includes the principal correction, since the double
pole at one has the stated residue. The actual auxiliary
sizes give the *sharper* conductor bound
log C_gamma <= C x^(epsilon/5)(log(2x))^2 on
U<=x<=U^J; use this, not the coarse x^(epsilon/4)
substitute. Set L_v=log v>=x^(epsilon/3)-log3.
The exponent is at least a fixed positive constant times


```math
\min\left(\frac{L_v}{x^{\epsilon/5}(\log(2x))^2},
                    \sqrt{L_v}\right).
```


At the initial thin scale the first term is
>>x^(2epsilon/15)/(log x)^2, and the second is
>>x^(epsilon/6). Both dominate x^(epsilon/8)
since 2/15>1/8. This also dominates the logarithm
of the prefactor uniformly through the entire tail:
up to L_v<=x^(2epsilon/5)(log(2x))^4 that logarithm
is O(log x); beyond it the lower bound is a constant
times sqrt(L_v). Increase the threshold to absorb
all constants and the fixed prefactor. This proves
exactly (2), with the same exponent as the parent.
If an imprimitive Dirichlet realization is needed,
its finite Euler corrections are bounded by
O(log N(1+log v)) from the exact minimum formula
in the parent section, negligible after division
by v. The actual primitive host family already
satisfies (2).

## 6. Exact transfer and residual source audit

The original RH/Dirichlet two-prime choices, their common
window ordering and all field/size hypotheses in the
[selection assembly](../paper/sections/recovered/34-sec-selection-assembly.tex)
are unchanged. With F=Q and Xi the primitive characters
of conductor dividing 8M, (1) supplies the exact
corrected thick companion values and log derivative bounds.
Equation (2) supplies the thin cost at every actual
thin argument v>=exp(x^(epsilon/3))/3.
The [averaged finite-error criterion](one-construction-target.md)
requires these values and signed costs, not a proof that
an auxiliary L-function has no zeros anywhere beyond a
fixed line at unbounded height. Thus this replacement
removes QRH from that analytic block of our preferred
distillation. With F=Q(omega) and Xi={1,lambda,lambda^-1}
it simultaneously removes QRH from the two-sign Hecke
block, without the geometric alteration of the one-sign
polynomial scheme.

The original source has a stronger all-height zero-free
clause for the real characters of its conductor. We have
only proved a fixed-width box with growing finite height
and a classical shrinking region outside. Do not assert
that the old source theorem with this all-height clause
has been reproduced. Any later consumer that actually
uses it in a different way must be checked separately.
In particular this note does not show that every QRH
use in the pinned source has been eliminated. It proves
the stated numerical companion and thin suppliers
unconditionally with the classical cited inputs.

No Selmer, theta/period or final geometric budget is
deduced from auxiliary selection alone; all such
obligations in the proof map are retained.

## Implementation

The rational specialization has a complete shared TeX proof in
[unconditional-quadratic-selection.tex](../paper/shared/unconditional-quadratic-selection.tex),
now included in both parent manuscripts. The partial cohomological
window proposition sa-compatible-interval explicitly replaces its
QRH-dependent selection by that theorem. Its coarse cohomological
hypothesis is unchanged. The old stronger conditional source theorem
is retained. The new TeX sources have not been compiled in this turn.
