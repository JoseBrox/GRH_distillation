# A general finite-order Hecke companion supplier

24 November 2026. This extends the analytic companion block of the
Dirichlet transfer from the cubic benchmark to arbitrary *fixed* number
fields and finite-order target characters. It uses the stated Dirichlet
QRH input of the parent moment argument, and a classical Hecke
zero-density theorem. No Hecke GRH assumption, arithmetic map or
estimate for the fixed untwisted target is supplied.

## 1. Statement and conventions

Fix a number field F of degree n >= 2, a finite nonempty set Xi of
primitive finite-order Hecke characters of F, and constants A_0,J >= 1,
0 < epsilon < 1/52. Put eta=epsilon/5, z=U^eta,
z'=z(log U)^2, Q=exp(z), D=exp(z'). For each sufficiently large U let
B_U be the family of primitive characters induced by

    xi rho^N,  xi in Xi,

where rho runs through characters of the real dyadic cyclotomic fields
of levels h <= A_0(1+log U). The superscript N means pullback along
the idelic norm F/Q. This includes the case with no dyadic factor.
Repeated characters are treated as one character. The field F, Xi
and all constants are fixed before U varies.

Use the true corrected ramps G_alpha, prime coefficients a_alpha(n),
and F_alpha=-L'/L of the
[cubic companion theorem](cubic-companion-selection.md), now over F.
For the trivial character, the correction is
R_1(v)-v log v+(1+c_F)v, where c_F is the constant term of zeta'_F/zeta_F
at one. For nonprincipal characters it is R_alpha(v)-v F_alpha(1).
Characters always mean their primitive realizations, so ramified local
Euler factors are absent.

**Theorem.** Under the parent's uniform Dirichlet QRH hypothesis
(no Dirichlet zeros in Re s>11/12), choose primes


```math
Q/2<q<Q,\qquad D/2<d<D,\quad q\equiv3\bmod8,\quad d\equiv7\bmod16,
```


with q|(d+1), and every odd prime l<=z dividing d+1. They avoid
the rational primes ramified in F or dividing the fixed conductors.
Consistent additional fixed congruence conditions as in the cubic
moment theorem are allowed. Write chi_l=(./l). For every alpha in B_U
and each (i,j) in {0,1}^2 other than (0,0), set


```math
\beta=\alpha(\chi_q^i\chi_d^j)^N.
```


All these characters are nonprincipal. There is a fixed delta>0
depending on F such that their L-functions are zero-free in
Re s>=1-delta, |Im s|<=Q^2 for q-only twists and |Im s|<=D^2 otherwise.
Uniformly over the indicated growing family,


```math
|G_\beta(y)|\le y^{1/2+\epsilon/2},\qquad
 |F_\beta(1)|\le 2n\log y\qquad(U\le y\le U^J).
 \tag{1}
```


Moreover, for every fixed A_1>0, every character gamma in the
*whole* family (including the untwisted ones, i=j=0) obeys


```math
\frac{|G_\gamma(v)|}{v}\le y^{-A_1}
 \quad(v\ge \exp(y^{\epsilon/3})/3,\ U\le y\le U^J)
 \tag{2}
```


for sufficiently large U. Constants and thresholds may depend on
the fixed field, Xi, A_0,J,epsilon,A_1. There is no uniformity over
changing fields or fixed infinite-order archimedean characters.

## 2. The one additional classical input

Use Jesse Thorner, *Bounded gaps between primes in multidimensional
Hecke equidistribution problems*, Math. Res. Lett. 26 (2019), 875–901,
Theorem 2.3, p. 885
([published PDF](https://intlpress.com/api/bgcloud-front/resource/pdf/volume/1806602455200722945-1806602455200722945-806c05b858e3cdd21f784b79edae3766.pdf);
[arXiv:1509.04378](https://arxiv.org/abs/1509.04378)).
We only use the subfamily with all archimedean exponents m=0 in that
theorem. For primitive finite-order narrow ray class characters over
fixed F, the consequence is


```math
\sum_{N\mathfrak f\le H}\sum_{\xi\bmod\mathfrak f}^{*}
 N(\sigma,T;\xi)
 \ll_F (H^2T^n)^{3(1-\sigma)}(\log(HT))^{C_F},
 \tag{3}
```


for H>=1, T>=2, 1/2<=sigma<=1. The zero count includes zeros with
real part at least sigma and height at most T; using a slightly
larger box makes any boundary convention irrelevant. The published
displayed statement and arXiv theorem were inspected. In particular
this estimate is uniform over primitive moduli up to H, and does
not require a fixed cusp form being twisted.

The standard finite-order Hecke zero-free region, with at most
a real exceptional zero for a real character, is also used below,
as in [Thorner–Zaman, Theorem 3.1](https://msp.org/ant/2019/13-5/ant-v13-n5-p02-p.pdf).
Applying it to the abelian extension cut out by an individual
character bounds its region in terms of its conductor and fixed F.
Indeed all characters of that extension are powers of it and their
conductor norms are no larger than its conductor norm.

## 3. Simultaneous exclusion of bad auxiliary primes

There are at most U^c base characters for a fixed c: the dyadic
fields are nested with degrees polynomial in U, and Xi is fixed.
Their conductor norms are polynomial in U, because a norm pullback
of a rational modulus m has conductor dividing m O_F, and
conductor ideals of products divide the product of the respective
moduli. The infinity types are finite-order sign types, hence bounded.

Every candidate q is unramified in F and outside the base conductors.
Local norms of units for an unramified extension are surjective.
The new quadratic character at q is therefore genuinely ramified
at all primes above q. The same applies to d, and q and d are
distinct and outside the original fixed ramification. A twisted
character is nonprincipal and its Euler coefficients are exactly


```math
a_\beta(k)=a_\alpha(k)\chi_q(k)^i\chi_d(k)^j
```


including the zero coefficients at new ramified primes. If an
exponent is zero the corresponding character is omitted.

For q-selection take V=Q; for d-selection after fixing q take V=D.
All relevant twisted conductors have norm <= V^{3n} for sufficiently
large U. This follows from the polynomial base bound, the factor
V^n for each new prime, and Q<=D. Their heights of interest are
T=V^2. Choose delta=1/(400n). By (3), the number of primitive
characters having a zero with Re s>=1-delta and |Im s|<=V^2
among these conductors is O_F(V^{1/4}), even using (3) at
sigma=1-2delta: its power exponent is at most 48n delta=0.12,
and the logarithmic factor is absorbed.

Reject a q if any of its q-only companions is bad. Every rejected
q has a witnessing primitive character with genuine ramification
above q; no such witness can belong to a different candidate q,
because the other base conductors involve only the fixed primes
and two. Hence there are O(V^{1/4}) rejected q. Similarly, for fixed q,
the d-only and qd companions of different d have distinct primitive
witnesses, by their ramification at d. Thus the same rejection bound
works uniformly for the second selection. There is no union-bound
factor equal to the size of the base family in this argument:
the density sum already counts all the distinct witnesses.

## 4. Moment selection and the genuine correction

Choose B>J fixed with B delta/2>J+eta+3. Apply the
[coefficient-independent high-moment lemma](cubic-companion-selection.md#2-finite-window-companion-selection-for-arbitrary-coefficients)
to the polynomially many sequences a_alpha(p), alpha in B_U, up
to 2U^B. Enlarge its fixed modulus to include ramification of F
and all fixed conductors. Use loss epsilon/4 and permit the above
density-bad primes to be rejected. The bound |a_alpha(p^k)|<=n log p
holds for every character, since the sum of residue degrees over
p is at most n. Chebyshev's higher-prime-power bound therefore
gives, simultaneously for every selected companion,


```math
|P_\beta(t)|=\left|\sum_{k\le t}a_\beta(k)\right|
       \ll t^{1/2+\epsilon/4}\quad(U\le t\le2U^B).
```


The true correction argument of
[§3 of the cubic theorem](cubic-companion-selection.md#3-select-genuine-zero-free-boxes-for-the-cubic-companions)
uses only this estimate, the zero-free box, the conductor bound,
and the local partial-fraction estimate for fixed degree. The last
estimate follows from the same order-one Hadamard product proof in
§4 there: the bounded finite-order archimedean parameters replace
the degree-two gamma factors, and the fixed degree n replaces 2.
In particular, for C_beta=|D_F|Nf_beta and Re s>=1-delta/2,
|Im s|<=T/2 in the bounded real strip used in the contour,
F_beta(s)=O_delta,F(log(C_beta(3+|Im s|)^n)).
The conductor logarithm is O(z').

Take the same smooth cutoff V_0, equal to one on [0,1] and zero
on [2,infinity), and X=U^B. The Mellin contour shift in the cited
argument gives, uniformly over the entire companion family,


```math
F_\beta(1)=\sum_k \frac{a_\beta(k)}k V_0(k/X)+O(U^{-J-1}).
```


Indeed the vertical error is O(X^{-delta/2}(1+log C_beta))
and the horizontal/tail errors are bounded by
O(X T^{-2}(1+log(C_beta(T+3)^n))). Both are O(U^{-J-1})
by the choices and the exponential sizes of T. Partial summation
from y to 2X proves G_beta(y)=O(y^{1/2+epsilon/4}).
Splitting the same approximation for F_beta(1) at U gives
n log U+O_F(1)+O(U^{-1/2+epsilon/4}), by rational Mertens and the
proved bound on P_beta. Enlarging the fixed threshold gives (1).

## 5. Thin scales including real characters

For the entire family the analytic conductor logarithm is
O(z'+log U), hence <=y^{epsilon/4} for large U. For selected
companions the only possible real exceptional zero of the
classical zero-free region is excluded by the density box:
shrink the classical region constant so its width is less
than delta everywhere.

The untwisted real characters form a finite set independent
of U. To see this, fix xi in Xi. The group of all norm-pullbacks
of real dyadic cyclotomic-layer characters is a quotient of the
character group of a procyclic Z_2-extension. Its subgroup killed
by 2 has at most two elements (equivalently use the image of
G_F in that procyclic group and its finite layer characters).
The equation (xi rho^N)^2=1 therefore has at most two solutions
for rho^N. The union over Xi is finite. For these fixed real
characters, shrink the zero-free constant once more to exclude
any fixed exceptional zero. Nonreal untwisted characters need
no such adjustment.

Thus the whole family has a uniform classical region of width
c/(log(C_gamma(3+|t|)^n)), with the principal pole allowed.
Apply the smoothed Perron contour of §4 of the cubic companion
note with fixed degree n in place of 2. The nonprincipal residue
is v F_gamma(1); the principal double pole gives
v log v-(1+c_F)v. Both are cancelled by the respective true
correction. The same initial-tail, vertical-line and horizontal
bounds give


```math
|G_\gamma(v)|/v\ll
 (1+\log C_\gamma+\log v)^{B_1}
 \exp\left(-c_1\frac{\log v}
 {1+\log C_\gamma+\sqrt{\log v}}\right).
```


All constants are fixed independent of the family size. As in
the earlier proof, when log v>=y^{epsilon/3}-log 3 and
log C_gamma<=y^{epsilon/4}, this is <=y^{-A_1} uniformly
through the whole indicated tail. This proves (2).

## 6. Scope

The analytic auxiliary block is now available for all fixed-field
finite-order target families, not just the cubic example, including
polynomially growing real dyadic auxiliary layers. It replaces the
special GL2 automorphic-induction density argument if desired.
It neither bounds the fixed target at the thick scale nor produces
the geometric arithmetic supplier for its relative host. The
genuinely infinite-order problem and uniform estimates in varying
base fields are not included. The proof imports the explicit
Dirichlet QRH input from the parent reconstruction, not Hecke GRH
or any conclusion of the crowdsourced Masullo project.
