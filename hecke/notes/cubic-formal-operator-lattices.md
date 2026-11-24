# All-order local integral theta operators and their cubic factorials

24 November 2026. This strengthens the actual
[cubic differential maps](cubic-differential-theta-maps.md):
at each ordinary degree-one good prime, the complete local
integral operator lattice, including denominators and every
power of the prime, is a characteristic-polynomial lattice
of an explicit union of p-adic lines. The result also applies
to the local normalized multiplicative theta expansions of
the parent construction. It is a local-to-global arithmetic
description, not the sharp collective degree estimate.

## 1. Formal-group reduction, with the actual section test

Put F=Q(omega), alpha^3=2, E_j: y^2=x^3+2^(2j), j=0,1,2,
and let D_j be the invariant derivative from the differential
map note. Fix a prime v of F above p>3, p=1 mod 3.
Thus F_v=Q_p, and all three curves have ordinary good
reduction, as follows from their nonzero Hasse invariants.
Let R be the complete DVR of the completed maximal
unramified extension of F_v, with uniformizer p and
algebraically closed residue field. View alpha as a unit
of R: the cubic extension is unramified at v.

The ordinary height-one elliptic formal group over R is
isomorphic to the formal multiplicative group over R.
For a reference see Mazur, *Rational points of abelian
varieties with values in towers of number fields*,
Invent. Math. 18 (1972), Lemma 4.27; the same application
is recalled in the proof of Proposition 3.1 of
*Zero-cycles on products of elliptic curves over p-adic
fields*, Acta Arith.,
https://www.impan.pl/shop/publication/transaction/download/product/83414 .
One can also see the assertion by taking the Cartier dual
of its connected height-one p-divisible group: the dual is
étale of height one and becomes the constant p-divisible
group over the strictly henselian complete base. Dualizing
gives the multiplicative p-divisible group and the induced
formal-group identification. We only use the ordinary
height-one case.

Choose this isomorphism on E_0 and transport it by the
actual isomorphism phi_j of the torsor note. In its integral
formal coordinate t the invariant derivative is


```math
D_j=c_j(1+t)\partial_t,\qquad
c_j=\alpha^j c_0,\quad c_0\in R^\times.
\tag{1}
```


Indeed pullback of the invariant differential by phi_j is
alpha^(-j) times the old differential. This gives (1) in
the transported frame; no assumption that the unit period
c_0 is in Q_p is needed. Translating the formal neighborhood
to any R-point of E_j gives the same derivative.

Write V_{j,m,R}=H^0(E_j/R,O(m[0])), using the actual good-place
section lattice. Fix n>=0 and m>=n+2. For a polynomial P of
degree at most n over Frac(R) the following are equivalent:

* P(D_j) maps V_{j,m,R} to V_{j,m+n,R};
* P(c_j k) belongs to R for every integer k>=0;
* P(c_j Z_p) is contained in R.

**Proof.** First suppose the second condition holds.
Every monomial t^a is an integral linear combination of the
functions (1+t)^k, k<=a. These functions are eigenfunctions
of c_j(1+t)partial_t with eigenvalues c_j k. Consequently
P(D_j) preserves R[t] and, by t-adic continuity (it loses
at most n orders and has bounded coefficient denominators),
R[[t]]. Pick an R-point away from the origin and use its
translated formal neighborhood. Every integral section
has a regular integral function expansion there, hence so
does its image. The image already has horizontal pole order
at most m+n, by the derivation formulas. If its section
had a vertical denominator, multiply by the least positive
power of p clearing it in the actual target lattice. Its
nonzero reduced section would have zero entire formal germ
at that point. On the integral smooth special fiber a
nonzero section cannot have zero germ. This contradiction
proves integrality of the target section.

Conversely, at the same point the evaluation map onto its
jets through order n is onto over R: the kernel line bundle
has degree m-(n+1)>0 on the genus-one fibers, so its H^1
vanishes by Riemann--Roch and relative cohomology/base
change. Prescribe the jet of (1+t)^k, lift it to an actual
section, and evaluate P(D_j) there. This value is exactly
P(c_j k), since the differential order is at most n.
The first condition makes it integral. Finally nonnegative
integers are dense in Z_p and evaluation is continuous,
so the second and third conditions are equivalent. QED.

All operations here are on the same global section
lattices and their completions. A choice of a point or a
formal coordinate is used to prove the equivalence, not
to change the global map.

For several twists J subset {0,1,2}, the simultaneous
operator lattice is therefore


```math
\operatorname{Int}_{\le n}(S_J,R),\qquad
 S_J=\bigcup_{j\in J}c_0\alpha^j\mathbb Z_p.
\tag{2}
```


The corresponding lattice over O_{F_v} base changes
exactly to (2). Indeed it is the integral preimage of
the finite block of actual operator matrices, which
has full column rank in characteristic zero. Smith
normal form and flat base change give the assertion.
Unramified base change preserves normalized elementary
divisors, so one may compute them over R.

If the cubic Frobenius label is zero, alpha belongs to
Z_p^times and all three lines coincide. Otherwise its
reduction has degree three over F_p, so the three nonzero
residue directions are distinct. In particular the
operator lattices coincide locally at split cubic primes
to **all powers**, not just modulo p.

## 2. Exact local characteristic exponents for the union of lines

Multiplication of all nodes by the common unit c_0
does not change leading coefficient valuations. In the
nonsplit case let S_m denote a union of m of these lines,
1<=m<=3, with one line chosen as base (m=1).
Let w_m(k) be the negative valuation of the kth
characteristic leading coefficient ideal of
Int_{<=k}(S_m,R). For m=1,


```math
w_1(k)=\sum_{a\ge1}\lfloor k/p^a\rfloor=v_p(k!).
\tag{3}
```


For m=2,3 there is a simple exact recursive computation.
There are M=m(p-1)+1 residue classes meeting S_m.
The zero class is p S_m, and each other class is a
translate of p times a single unit multiple of Z_p.
A p-ordering is constructed by choosing at each step
a new node minimizing the valuation of the product of
its differences from the previous nodes. A minimum
exists: valuations are nonnegative integers and the
set has infinitely many points. In each residue branch,
use a scaled p-ordering recursively (one can use the
ordinary digit ordering in the single-line branches).
Different branches contribute zero valuation to
differences. If k points have already been used in a
branch, the next cost there is k plus its internal
p-ordering cost. The sequence is nondecreasing,
because every further factor has nonnegative valuation.

For completeness these costs are exactly the
characteristic exponents: if a_i are the selected nodes,
the normalized Newton polynomials
prod_{i<k}(T-a_i)/prod_{i<k}(a_k-a_i)
are integer-valued by the minimizing property.
Successive evaluation at the selected nodes proves that
every integer-valued polynomial is a unique integral
linear combination of these polynomials, by eliminating
Newton coefficients in increasing order. This proves
independence of choices and the determinant formula.

It follows that w_m is the sorted merge, with multiplicity,
of m(p-1) copies of the stream k+w_1(k) and one copy of
the stream k+w_m(k), k>=0. This is also an effective
finite recursion: each nonzero output uses inner indices
less than its own index, since there are M zero-cost
first terms. Ties can be resolved by any fixed rule.
It gives every higher characteristic exponent exactly.

In particular for k<p^2,


```math
w_m(k)=\left\lfloor \frac{k}{m(p-1)+1}\right\rfloor .
\tag{4}
```


Indeed each residue class contains at least p different
classes modulo p^2. As long as fewer than p nodes have
been taken from each branch its next cost equals the
number previously taken there (choose an unused class
modulo p^2). Greedy choice balances the branch counts;
for k<p^2 their minimum is less than p. The same
lower bound follows just by counting first residues.
This proves (4).

For the entire local operator lattice the logarithmic
relative index between the single-line and m-line
conditions, counted with norm p, is thus


```math
(\log p)\sum_{k=0}^n(w_1(k)-w_m(k)).
\tag{5}
```


Unlike the mod-p kernel in the previous differential
note, this includes every elementary divisor of the
full integral operators, with no CRT height penalty
inserted in its definition.

## 3. Uniform centered estimate for the local factorial sequences

Define c_1=1/(p-1). For m=2,3 put u=m(p-1)^2/p
and let c_m be the positive solution of


```math
u c_m(c_m+1)=1 .
\tag{6}
```


Then, with an absolute constant for p>=7, m<=3,


```math
w_m(k)=c_m k+O((1+\log(k+1))^2),\qquad
 c_m=\frac1{mp}+O(p^{-2}).
\tag{7}
```


Here and below c_m is a real capacity constant, not the
unit derivative scalar of (1). We give the elementary
proof to control the error uniformly over rational primes.

By (3), w_1(k) differs from c_1 k by O(1+log(k+1)).
The sorted merge of arithmetic streams of positive
slopes A=p/(p-1) (with m(p-1) copies) and 1+c_m
(one copy) has kth term c_m k+O(1), with an absolute
constant: the number of terms <=t lies between
t/c_m and t/c_m+M, because (6) says
1/c_m=m(p-1)/A+1/(1+c_m).
Use M c_m=O(1). Equation (6) itself gives the
second estimate of (7).

For the actual streams every term of inner index i
is at least i. Also w_m(k)<=w_1(k)<=k/(p-1),
since taking the minimum over a union can only reduce
the characteristic exponent (or use inclusion of the
integer-valued polynomial lattices). The ideal linear
merge also has kth value at most k/(p-1)+1, by comparison
with the single-line streams. Therefore in determining
either kth value it suffices to keep inner indices
i<=floor(k/(p-1))+2 in every stream. Perturbing each
term of a finite list by at most E perturbs each sorted
order statistic by at most E. Write E(K) for the
largest error |w_m(i)-c_m i| with i<=K. Comparing
the truncated merges gives, for k sufficiently large,


```math
|w_m(k)-c_m k|\le
 E(\lfloor k/(p-1)\rfloor+2)+C(1+\log(k+1)).
```


All small k have a uniform bound by (3) and c_m<=c_1.
For k>=12 and p>=7 the inner argument is at most k/2.
Take the maximum for k<=K and iterate on halved
arguments; the sum of O(1+log(K/2^j)) is
O((1+log(K+1))^2). This proves (7).

## 4. A new centered global lattice interface

Let N denote the nonsplit rational primes p>3 with
p=1 mod 3. Use the actual local operator conditions
(2) at all ordinary degree-one primes, and integral
polynomial coefficients elsewhere. For degree <=n
they define full global lattices over O_F, since
outside p<=n the characteristic ideals are units
(and the actual integral matrix condition imposes no
new denominator there). The conditions are the
integral inverse images of the same actual global
operator matrices, with the explicit coefficient
integrality conditions at the excluded places.
Patch by their finite determinant denominators, or
use localization of the finite matrix equations.
There is no assumption of a simultaneous optimal
ordering of global nodes.

Define the kth leading-coefficient relative log
index between one and m twists, for m=2 or 3, by


```math
T_m(k)=2\sum_{p\in N}\log p\,(w_1(k)-w_m(k)).
```


The full relative log index for degree n is
sum_{k=0}^n T_m(k). The factor two counts the two
degree-one primes of F over p, where the two
Frobenius labels are opposite but both nonsplit.
At split cubic primes the index is zero exactly.

There is an explicit convergent centering constant


```math
B_m=2\sum_{p\in N}(\log p)
        (c_1-c_m-(1-1/m)/p).
```


The summands are O(log p/p^2) by (7).
We claim


```math
T_m(k)=2\sum_{p\in N}(\log p)
       \big(\lfloor k/p\rfloor-\lfloor k/(mp)\rfloor\big)
       + B_m k+O(\sqrt k(1+\log(k+1))^2).
\tag{8}
```


For p<=sqrt(k) use (7) and the two floor errors;
the total is O(sqrt(k)(1+log(k+1))^2) by Chebyshev.
For p>sqrt(k), formula (4) is exact (including k=0
by the trivial case). To replace floor(k/(mp-m+1))
by floor(k/(mp)), a difference is possible only
if some positive integer r satisfies
r(mp-m+1)<=k<rmp. For each such r<=O(sqrt(k)),
the possible integer p lies in an interval of length
(m-1)/m<1. Count the difference by the number of
such (r,p) pairs; each costs at most log k+O(1).
The total cost is O(sqrt(k) log(2k)).
Finally the tail of B_m k over p>sqrt(k) is O(sqrt(k))
by partial summation of Chebyshev's bound. This proves (8).

Thus the all-order genuine theta lattice has the
same critical-scale accuracy as a rational floor
convolution after explicit linear centering. This
is a new exact geometric interface for those
convolutions; it is not a proof of their estimates.
For the full determinant one sums (8), incurring
O(n^(3/2)(1+log(n+1))^2) error.

In the cubic benchmark compare three times the nonsplit
indicator with twice the indicator of all p=1 mod 3.
The rational floor transform in (8) is the corresponding
prime Dirichlet series multiplied by
(1-m^(-s))*zeta(s)/s. The multiplier 1-m^(-s) is nonzero
in Re s>0. Ordinary RH suffices to remove the possible
zeta cancellation in Re s>1/2. The eta-product real-zero
exclusion of the cubic factor makes either sign of a
one-sided bound permissible, as in the benchmark.
This version therefore can reuse our ordinary RH
program. It is not independent of ordinary RH in the
same way as the earlier truncated-ramp criterion.
The explicit linear constant B_m is part of the target;
its mere convergence is not a bound for the centered
lattice index.

## 5. Exact local reuse in the parent theta jets

The parent's
[ordinary type-prime jet theorem](../../paper/shared/theta-integral-frontier-type-prime-jets.tex)
uses normalized integral formal expansions in multiplicative
coordinates and unit periods. Its integral directions are
transported through its actual lattice frame. The coefficient
condition in Section 1 has a direct formal consequence:
whenever an integral theta expansion is in R[[t]] and the
chosen direction is c_j(1+t)partial_t, every operator P(D_j)
with P(c_j Z_p) contained in R preserves that expansion
integrally. This was proved on the monomials t^a in Section 1;
no algebraic specialization or new period is required.
It extends to several commuting integral multiplicative
directions by treating the variables successively.
For a torsion-dilated expansion the assertion applies in
the actual dilated coordinates; if one undoes the dilation
one must retain the corresponding scale on the direction,
as in the parent's original M-factor bound.

Consequently the all-order local polynomial operator
conditions are genuine sufficient conditions for the
local integrality part of the original jet argument,
with cubic unit scalings in an admitted eigen-direction.
They do not identify those polynomial operators with
the original global successive column/row maps, and they
supply no archimedean nonvanishing or collective source
degree. The original finite class weights, global
periods and matching of row/column maps still have to
be proved for such a replacement. No change to W06
or the original arithmetic assumptions follows from
this local lemma alone.

**Status:** exact all-order local operator lattice and
global characteristic-index identities; centered
approximation (8) with proof; actual local formal
theta-jet preservation. The quantitative global
lattice-degree inequality and hence the cubic
prime-discrepancy estimate remain open. No new
kernel verification or asymptotic numerical claim.
