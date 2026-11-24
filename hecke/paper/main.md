---
title: "Arithmetic reductions toward Hecke GRH"
date: "24 November 2026"
---

# Arithmetic reductions toward Hecke GRH

## Abstract

We reduce the critical-line assertion for arbitrary unitary Hecke
characters to two elementary types of prime-counting estimates:
relative counts of completely split rational primes, and counts
weighted by the real part of an infinite-order character. The
analytic argument is a direct Mellin transform of the counting
deficit. A positive character identity proves that zeros survive
norm pullback to a Galois extension. The preferred proof requires
neither the explicit formula nor a spectral trace formula.
For a first nonabelian field, the remaining prime-counting problem
has an elementary cubic-residue description; an eta-product
identity excludes real zeros and permits either sign of a
one-sided estimate. The required estimates for complex-zero
exclusion are open.

## 1. The problem and proof architecture

Let $F$ be a number field and $C_F=\mathbb A_F^\times/F^\times$
its idèle class group. A unitary Hecke character $\chi$ is a
continuous homomorphism $C_F\to S^1$. Its Euler product is


```math
L_F(s,\chi)=\prod_{\mathfrak p}
 (1-\chi(\mathfrak p)(N\mathfrak p)^{-s})^{-1},
\qquad \Re s>1,
```


where the factor is absent at a ramified character place.
Hecke GRH says that every zero in $0<\Re s<1$ lies on
$\Re s=1/2$. This includes finite-order and infinite-order
characters, Dedekind zeta functions and Dirichlet L-functions.

We use classical Hecke continuation, Euler factors, the functional
equation and class field reciprocity, in their standard forms.
The finite and completed functions have the same zeros in the
open strip. Fix a continuous section of the idelic norm:
the restriction of a unitary character to the section is
$t^{iu}$ for real $u$. Removing this norm power translates
zeros vertically. Normalized characters suffice.

The main analytic and algebraic proofs are given below and in
the linked proofs within this repository. Nothing in this
preferred route assumes a result of Masullo's crowdsourced
formalization. The optional spectral route is described
separately with attribution.

## 2. A single Mellin integral detects zeros

Let $c_\chi>0$ be the weights of a fixed finite family of
normalized characters over $F$ and $c_1$ the total weight of
the trivial character (zero if absent). Put


```math
a_\chi(n)=\sum_{N\mathfrak p^m=n}
     \log N\mathfrak p\,\chi(\mathfrak p)^m,\qquad
A(n)=\sum_\chi c_\chi\Re a_\chi(n).
```


Set the local value to zero when the Euler factor is absent.
Only rational prime powers occur. Define the real deficit


```math
D(x)=c_1x-\sum_{n\le x}A(n).
```


**Theorem 2.1.** If for some fixed $b>1$ and $0<\theta<1$


```math
\liminf_{Y\to\infty}\frac{
 \log\left(1+\int_Y^{Y^b}D(x)_+x^{-1-\theta}dx\right)}
 {\log Y}=0,
```


then no member of the family has a zero in $\Re s>\theta$
(the principal pole at one is not a zero).

*Proof.* Logarithmic differentiation of the absolutely
convergent Euler product and integration of a step function
give, in $\Re s>1$,


```math
\int_1^\infty D(x)x^{-s-1}dx
 =\frac{c_1}{s-1}+\frac1{2s}\sum_\chi c_\chi
 \left(\frac{L'_F}{L_F}(s,\chi)
       +\frac{L'_F}{L_F}(s,\bar\chi)\right).
```


The pole from the trivial character at one cancels.
Every zero in $\Re s>0$ gives a simple pole of the transform,
with residue its positive weighted multiplicity divided
by the zero. Real residues are positive, and complex
residues cannot cancel. The elementary bound
$|a_\chi(p^k)|\le [F:\mathbb Q]\log p$ gives
$D(x)=O(x\log x)$.

Apply the one-sided Laplace window lemma of our Dirichlet
proof to $g(u)=D(e^u)$. For completeness its
[full proof is reproduced here in the repository](../notes/direct-prime-criterion.md#2-the-one-sided-window-lemma-with-proof):
gamma localization to $[U,bU]$, the inequality
$|g|+g=2g_+$ and Cauchy's estimates at a uniquely nearest
pole prove zero exclusion; a real nearest pole uses its
positive residue. All hypotheses are checked above.
The functional equation and conjugation then give GRH
for the family at $\theta=1/2$. QED.

An eventual bound $D(x)\le C_\epsilon x^{1/2+\epsilon}$
for each $\epsilon>0$ is the simpler sufficient special
case. The window theorem does not require such an estimate
on the entire tail.

## 3. Only degree-one prime ideals matter

For a rational prime $p$, summing residue degrees above $p$
that divide $k$ gives $|a_\chi(p^k)|\le[F:\mathbb Q]\log p$.
The elementary Chebyshev bound implies


```math
\sum_{\substack{p^k\le X\\k\ge2}}\log p
 =O(\sqrt X).
```


The terms with $k=2$ have this bound directly; the terms
with $k\ge3$ contribute $O(X^{1/3}\log X)$.
Thus higher rational prime powers may be removed at
$O_F(\sqrt x)$ cost for every fixed family. This error
adds only $O(\log Y)$ to the window budget at
$\theta=1/2$. Finitely many bad rational primes at the
first power may also be omitted.

For a nonnegative weighted prime count, the deficit is
bounded between square-grid samples by monotonicity:
if $D(j^2)\le B_j$ then for $j^2\le x\le(j+1)^2$,


```math
D(x)\le B_j+c_1(2j+1).
```


Thus upper tables over whole square-grid windows suffice.
No smooth test or explicit formula is needed. The
[direct-prime note](../notes/direct-prime-criterion.md)
also proves a capped-ramp version connected to the
corrected smoothed sums in our Dirichlet program.

There is an exact positive kernel for arbitrary unitary
Hecke characters, not just finite-order characters.
For a finite family $\chi_i$ and $b_i\ge0$, form


```math
P(g)=\left|\sum_i b_i\chi_i(g)\right|^2.
```


Its expansion into characters has nonnegative coefficients.
At a finite place, average $P(\varpi^k u)$ over the local
unit group with probability Haar measure. The resulting
number is precisely the corresponding combination of
actual Euler coefficients: the average kills the ramified
characters and preserves the unramified ones. It is
nonnegative. Taking the family $1,\chi$ gives, after
division by two, $1+\Re\chi$. This proves the arithmetic
positivity including ramification. The
[full kernel note](../notes/unitary-positive-kernel.md)
also gives explicit Fejer kernels using powers of an
infinite-order character.

## 4. Reduction to totally imaginary Galois fields

**Theorem 4.1.** Let $K/F$ be finite Galois and $\chi$
a unitary Hecke character of $F$. Every zero of
$L_F(s,\chi)$ in the open strip occurs with at least
the same order in $L_K(s,\chi\circ N_{K/F})$.

*Proof.* Write $J=\operatorname{Gal}(K/F)$ and $n=|J|$.
For each nontrivial cyclic subgroup $C$ and nontrivial
$\lambda\in\widehat C$, set


```math
d_{C,\lambda}=\sum_{g\in\operatorname{Gen}(C)}
 (1-\overline{\lambda(g)}) .
```


These are strictly positive integers: the cyclotomic
Galois group permutes the generators, and each real
summand is positive. Fourier expansion of the mean-zero
function which is $\varphi(|C|)$ at the identity, $-1$
on generators and zero elsewhere gives


```math
n(\operatorname{Reg}_J-1_J)
 =\sum_{C,\lambda\ne1}
 d_{C,\lambda}\operatorname{Ind}_C^J\lambda .
```


Every cyclic subgroup is counted once: at $g\ne1$
the induced-character sum equals $-n$ since each
conjugate of $g$ generates exactly one such subgroup.
At the identity it equals $n(n-1)$ by partitioning
the nonidentity elements into generator sets.

Twist by $\chi$, omit the finitely many bad places
$S$ of $F$, and use unramified determinant Euler factors:


```math
\left(\frac{L_K^S(s,\chi\circ N_{K/F})}
 {L_F^S(s,\chi)}\right)^n
 =\prod_{C,\lambda\ne1}
 L_{K^C}^S(s,(\chi\circ N_{K^C/F})\lambda)^{d_{C,\lambda}}.
```


Here $\lambda$ is identified by class field theory with
the associated finite-order Hecke character of $K^C$.
For local compatibility, an orbit of Frobenius on $J/C$
of length $f$ gives one prime of residue degree $f$.
On that orbit the determinant factor is
$1-\chi(\mathfrak p)^f\lambda(u^{-1}g^fu)(N\mathfrak p)^{-fs}$
for a representative $uC$. This is the actual Hecke
factor. All functions on the right are holomorphic
in the open strip and all exponents are positive.
Taking orders gives the result; restoring bad Euler
factors preserves orders in $\Re s>0$.
This is the twisted Aramata–Brauer argument, with no
Artin holomorphy assumption.
See [the full algebraic proof](../notes/galois-base-change.md). QED.

Adjoining $i$ to the normal closure over the rationals
reduces the problem to totally imaginary finite Galois
fields $K/\mathbb Q$ (not necessarily CM fields). Normalize
the pulled-back character by a norm twist if needed.

## 5. Two arithmetic obligations

Fix such a field $K$ of degree $d$. At an unramified
rational prime, a degree-one prime ideal exists exactly
when the rational prime splits completely. Define


```math
P_K(x)=\sum_{\substack{p\le x\\p\ \mathrm{split\ completely\ in}\ K}}\log p,
```


where ramified primes are omitted.

### Finite order: relative split-prime counts

For a finite-order character of $F$, let $E/F$ be its
finite cyclic class field. The factorization of $\zeta_E$
over the characters of $\operatorname{Gal}(E/F)$ has
holomorphic factors in the critical strip; hence RH
for $\zeta_E$ implies the character's critical-line
assertion. Theorem 4.1 permits passage to a Galois
normal closure. Consequently the finite-order problem
reduces to Dedekind zeta functions of Galois fields.

Let $A$ be the maximal abelian subfield of $K$,
of degree $a$. By Theorem 4.1 the quotient
$Q=\zeta_K/\zeta_A$ is holomorphic in the open strip.
It has no pole in $\Re s>0$ (the simple poles at one
cancel, and the classical boundary nonvanishing applies).
Its logarithmic derivative divided by $s$ is the
Mellin transform of $\psi_A(x)-\psi_K(x)$, with
positive residue at every real zero. Removing higher
rational powers gives


```math
\psi_A(x)-\psi_K(x)=aP_A(x)-dP_K(x)+O(\sqrt x).
```


It therefore suffices to supply the window criterion
of Theorem 2.1 at $\theta=1/2$ for the relative deficit


```math
D_F(x)=aP_A(x)-dP_K(x).
```


This removes the entire abelian contribution exactly.
The abelian zeta function $\zeta_A$ factors into
Dirichlet L-functions. Alpöge's verified result supplies
it as a calibration; a final proof independent of
external formalizations will invoke our completed
Dirichlet reconstruction instead. That reconstruction
is still incomplete. Alternatively the absolute
deficit $x-dP_K(x)$ suffices without invoking the
Dirichlet theorem. Both suppliers are open in general.

### Infinite order: character phase counts

For each fixed normalized unitary infinite-order
character $\xi$ on $K$, apply Theorem 2.1 to the single
character. Its main term is zero. Thus it suffices
to bound


```math
D_I(x)=-\sum_{\substack{p\le x\\p\ \mathrm{split\ in}\ K}}
 \log p\sum_{\mathfrak p\mid p}\Re\xi(\mathfrak p)
```


in the same one-sided window sense, outside the fixed
bad prime set. This separates the genuinely infinite-order
problem from the unweighted finite-order count.

One may instead use the positive family $1,\xi$ and
the single combined deficit


```math
(1+\mathbf1_{\xi=1})x-\sum_{p\le x,\ p\ \mathrm{split}}
 \log p\sum_{\mathfrak p\mid p}(1+\Re\xi(\mathfrak p)).
```


It has nonnegative arithmetic weights and the same
zero-detection implication. No assumption of a
uniform bound across all fields or characters is made.
The two missing suppliers and their alternatives are
stated precisely in [the frontier](../notes/open-frontier.md).

## 6. First nonabelian case

Take $K=\mathbb Q(\omega,\sqrt[3]{2})$ and
$A=\mathbb Q(\omega)$, where $\omega$ is a primitive
cube root of unity. The Galois group is $S_3$.
For $p>3$, splitting in $K$ is equivalent to $p\equiv1
\bmod3$ and $2^{(p-1)/3}\equiv1\bmod p$. Equivalently
the prime has the form $u^2+27v^2$ (the classical
cubic reciprocity theorem).

Write $E(x)$ for the log-weighted count of primes
$p>3$ with $p\equiv1\bmod3$, and $C(x)$ for the
count restricted to the cubic-residue condition.
The relative deficit is $2(E(x)-3C(x))$ up to
the bounded bad-prime adjustment.

There is an additional simplification. Let $\lambda$
be the nontrivial cubic character of the Eisenstein
field arising from $K/A$. Its two nontrivial
characters give the same L-function, by conjugation.
With the primes over 2 and 3 omitted,


```math
\frac{\zeta_K^S(s)}{\zeta_A^S(s)}=L_A^S(s,\lambda)^2 .
```


The primary-generator description of $\lambda$ gives
the following exact eta-product identity:


```math
(2\pi)^{-s}\Gamma(s)L_A^S(s,\lambda)
=\int_0^\infty \eta(6it)\eta(18it)t^{s-1}dt .
```


The [benchmark note](../notes/s3-benchmark.md#4-elementary-eta-product-and-real-zero-exclusion)
proves it directly using a lattice bijection and Euler's
pentagonal-number identity. The integrand is positive on
$t>0$ for real $s$, and decays exponentially at both
ends. Hence the new factor has no positive real zeros.
No assertion about its complex zeros follows just from
this positivity.

The nearest-real-pole obstruction is now absent, so
either sign of the relative deficit can be bounded
in Theorem 2.1. It suffices to show a subpower cost of


```math
\int_Y^{Y^b}(\pm(E(x)-3C(x)))_+x^{-3/2}dx
```


on arbitrarily late fixed-ratio polynomial windows.
The sign may be fixed on a cofinal subsequence.
This is the first explicit nonabelian arithmetic
benchmark. We have not supplied this estimate.

## 7. Reusing the Dirichlet arithmetic machinery in the cubic case

The independent counting reduction is the simplest analytic endpoint.
For the actual cubic arithmetic estimate we may also use our
Dirichlet construction's corrected ramps. Let $F=\mathbb Q(\omega)$
and retain the selected auxiliary quadratic primes $q,d$ and dyadic
real field $R_h$. The field
$L_0=F R_h(\sqrt{-q},\sqrt{-d})$ is the parent abelian CM host with
base character $\chi_{-3}$; its relative CM extension is unramified
at finite places. Adjoining the cubic field gives a relative abelian
extension of $F$ with group $C_3\times C_{2^h}\times C_2^2$.

Our [companion theorem](../notes/cubic-companion-selection.md) proves
simultaneous bounds for the genuine corrected sums of the quadratic
twists of the cubic character and its powers, including their
logarithmic derivatives at one. This uses the parent's Dirichlet
quadratic-correlation lemma, a classical automorphic zero-density
theorem, and an elementary moment argument. The classical nonreal
Hecke zero-free region suffices for the entire relative family's
large-scale thin bounds. There is no assumption of Hecke GRH.

The [relative arithmetic comparison](../notes/cubic-relative-comparison.md)
gives the exact scalar balance over prime ideals, with all ramified
Euler factors and the same normalized Fourier averaging as in the
Dirichlet program. It reduces the benchmark to one concrete
arithmetic discrepancy bound using the actual integral maps.

The relative extension is not CM, and no CM field contains the
$S_3$ splitting field. Hence the original PEL host cannot be
changed by adjoining this field. The remaining construction is
to retain $L_0$ with a finite cubic coefficient system and realize
the actual relative Frobenius kernel. The
[coefficient interface](../notes/cubic-coefficient-interface.md)
proves that the candidate strict Selmer groups at primes outside
two and three split exactly into the original abelian sector and
two equal cubic sectors over the fixed Eisenstein field.

### Actual integral and local geometric suppliers

The [2-primary theorem](../notes/cubic-two-primary-window.md)
proves that the fixed splitting field $K$ has class number one
and unique principal primes above 2 and 3. The elementary
one-ramified-prime argument makes the respective primary class
groups vanish in its fixed cyclotomic towers. For the full
moving relative host $L_h=K R_h(\sqrt{-q},\sqrt{-d})$, the strict
2-adic Iwasawa module needs at most 144 generators. The parent's
descent, determinant-growth and common-interval arguments give,
with their exact ranges and simultaneous auxiliary choices,


```math
(\log 2)\sum_{1\le e<t}\lambda_2(L_h,e)
\le \exp(x^{4\epsilon/5}).
```


Thus the actual 2-primary sum, not just a formal component
comparison, is controlled. The
[exceptional-prime comparison](../notes/cubic-exceptional-prime-comparison.md)
uses the integral evaluation
$\mathbb Z_3[C_3]\to\mathbb Z_3\oplus\mathbb Z_3[\omega]$,
whose cokernel has order three. The new projection error in
the strict Selmer comparison is polynomial in the actual
source scales. The comparison alone does not bound the genuine twisted lengths
at 3 or the remaining odd primes; the high-dyadic result below
settles specific sectors.

There is also a simpler sufficient arithmetic supplier.
The [good-prime comparison](../notes/cubic-good-prime-comparison.md)
removes the higher rational powers and ramified first powers
by an exact linear correction to the main term. The omitted
centered remainder is nonnegative and costs only
$O(x^{1/2+\epsilon})$ in the displayed normalization.
A top set in the trivial cubic coset gives the fixed positive
family $G_1+2G_\lambda$ without the original fine share
distribution. The new count requires only unramified rational
first powers split in $F$, with the binary cubic-residue test.

The [torsor construction](../notes/cubic-torsor-realization.md)
realizes this test by the actual finite étale cover $z^3=2$
away from 6. On the CM elliptic curves
$E_j:y^2=x^3+2^{2j}$ the cubic descent cocycle is given by
$(x,y)\mapsto(\omega x,y)$. The three nonzero two-torsion
points give an equivariant orbit of symmetric principal
theta lines, each with a unit-normalized section at the origin.
The orbit is necessary for this normalization: no single
invariant symmetric principal line has such a section in
this model. A direct sum of the orbit lines preserves the
local equivariance and unitary norm data. The same note
constructs a local divisor patch realizing the good-prime
hinges with controlled rounding.

These local objects alone do not give a global arithmetic
bound; the differential construction below goes beyond them. The patch merely imposes the desired divisibilities;
its source-degree loss is exactly its local index. The global
label-sensitive theta maps must produce those divisibilities
while retaining the parent's nonvanishing, degree and norm
estimates. Pure tensor repetition or cubic phases do not
change the divisors, so the new bound cannot be inferred from
the old norm estimates alone. The global supplier and the
uniform odd-prime Selmer estimates remain open.

### General finite-order companion selection

The [fixed-field density version](../notes/general-finite-order-companions.md)
extends the true companion and thin-scale estimates to any
fixed number field, finite-order target family and polynomially
growing real dyadic layers. It uses Thorner's Hecke zero-density
theorem and the same explicitly stated Dirichlet QRH input,
not special GL2 induction or Hecke GRH. The arithmetic
construction for these families and all infinite-order
target estimates remain separate open tasks.

### A smaller companion supplier and genuine vanishing at three

The [polynomial auxiliary theorem](../notes/polynomial-one-sign-companion.md)
replaces the two-sign analytic block by one prime $q\asymp U^J$
in a fixed reduced progression, for the window $U\le x\le U^J$.
The classical quadratic large sieve gives, on dyadic blocks,
a bound of size $U^\kappa(\sqrt N+N/\sqrt q)$ for the prime
coefficients of the selected companions. Retaining the second
term even beyond the companion conductor makes it possible to
recover their true logarithmic derivatives at one by a
zero-density-selected contour and partial summation.
The entire growing thin family has a uniform zero-free-region
estimate at arguments at least $\exp(C(\log U)^2)$.
No uniform Dirichlet QRH assumption is needed for this
replacement. Its one-sign scalar comparison gives
$G_1+2G_\lambda\le E/k+O(x^{1/2+\epsilon})$ with only three
quadratic companions; the compatible global geometry and
arithmetic bound for $E/k$ remain open.

The [high-dyadic 3-primary theorem](../notes/cubic-three-primary-vanishing.md)
also gives an actual integral improvement. For a character with
even primitive dyadic component of conductor $2^b$ and auxiliary
quadratic odd conductor $f$, the strict cubic sectors at 3
vanish for both cubic signs and every twist index provided
$b\ge8$ and $2^b\ge192f$. Modulo the coefficient uniformizer
the cubic action is trivial; the parent's Bernoulli-unit
cocycle theorem kills the odd class-group components, Kummer
reflection kills the corresponding even components, and the
full local restriction maps verify that no torsion is lost
in passage from residual to integral strict groups.
The actual conductor threshold is essential. This does not
bound the lower dyadic layers, or the remaining odd primes.

### Actual cubic coefficient theta operators

The [differential construction](../notes/cubic-differential-theta-maps.md)
uses the invariant derivation $D_j=2y\partial_x+3x^2\partial_y$
on $E_j:y^2=x^3+2^{2j}$. On the actual lattice of sections of
$O(m[0])$, it maps to the next pole order. A polynomial
$P(D_j)$ is a global equivariant integral operator, with
the natural character on its coefficient space. At a good
degree-one prime $v$ over $p$, the Hasse invariant gives


```math
D_j^p=A_{0,p}\bar\omega^{jr_v}D_j\pmod v,
\qquad A_{0,p}=\binom{(p-1)/2}{(p-1)/3}\not\equiv0\pmod p .
```


Here $r_v$ is the actual cubic Frobenius label. Thus
$D_j^p-a_p\omega^sD_j$ is divisible by $v$ exactly for
the matching label $s=jr_v$, with powers supplying higher
divisibilities. Its coefficient space gives the exact
simultaneous index, where $B_{j,n}$ imposes reduction-zero
on the maps from pole order $2n$ to $3n$ at all good $v$
above $p\le n$:


```math
\log\#(B_{0,n}/(B_{0,n}\cap B_{1,n}))
=2\sum_{\substack{p\le n,\ p\equiv1(3)\\
2^{(p-1)/3}\ne1\bmod p}}
\min(n+1-p,p-1)\log p .
```


Both facts follow on the actual section lattices from the
p-Lie relation and monic local polynomial kernels.
With canonical theta metrics there is the uniform estimate


```math
\|P(D_j)\|_{2,m\to m+n}
\le C(m+1)\sum_{k=0}^n |c_k| B^{n-k}C^k\frac{(m+k)!}{m!},
\qquad P(T)=\sum_{k=0}^n c_kT^k .
```


The [coefficient-to-theta map](../notes/cubic-theta-coefficient-interface.md)
is the rank-three trace map
$f\mapsto\operatorname{Tr}(f(z)(x+z^2)^2)$ from the
cubic torsor to the even fourth-power theta space.
Its images of $1,z,z^2$ are $3x^2,12x,12$, hence it
is an integral isomorphism away from 6 with fixed
archimedean singular values. It supplies the actual
cubic coefficient representation; the higher-rank
p-Lie formula describes its label-sensitive twist.
For any prescribed monic degree $a$ and local exponents
$h_v$ with $p_vh_v\le a$, CRT supplies one equivariant
monic global operator with all the simultaneous matched
divisibilities, instead of a product whose order grows
as the sum of the local orders. Its coefficient height
is bounded by half the log norm of the prescribed
divisor plus a fixed constant. This pays for the entire
divisor and does not supply the desired critical-scale
saving. The original normalized global period chain
has not yet been identified with these maps.

### Additional cubic Selmer suppliers

The [fixed-conductor joint window](../notes/cubic-fixed-conductor-selmer-window.md)
combines high-dyadic 3-primary vanishing with a fixed-field
cyclotomic generator bound for the remaining low dyadic layers.
It controls both cubic 3-primary sectors at every fixed odd
conductor on the same windows as the moving 2-primary estimate.
The one-sign auxiliary prime may be chosen in a fixed
Chebotarev class, a 3-cycle with $q\equiv3\bmod8$, reducing
the 2-primary generator bound from 48 to 8. The remaining
moving low-dyadic 3-primary groups are not covered.

The [new polarized integral model](../notes/cubic-polarized-selmer-model.md)
uses the diagonal $(a\lambda^{-1},1,a^{-1}\lambda^{-1})$,
$a=\varepsilon^e\rho^N$. Its adjacent lower root pair is
the genuine induced cubic module, not a scalar twist of
the old adjoint. The strict torsion injects into the
marked conormal dual at each modulus. The
[cohomological calculation](../notes/cubic-frame-cohomology.md)
gives the exact high-dyadic relative dimension defects
$(0,-1,0,1,1)$, rational nonpositive-weight rigidity
and residual negative-corner vanishing when
$2^b\ge24\ell(\ell+1)^2$.
The fixed-Eisenstein-field spectral argument gives a
polynomial trace-resultant bound conditional on the
actual finite-ring/point comparison. At reducible
points the new cross-block condition involves the cubic
twist of the rank-two representation, a Rankin--Selberg
Selmer problem not covered by the parent's Dirichlet Kato
argument. The uniform new odd-prime lengths, automorphy,
point comparison and critical global geometric estimate
are still open.

### All-order theta operators and further Selmer reductions

The [formal-group theorem](../notes/cubic-formal-operator-lattices.md)
identifies the full good-prime integral operator lattices on sufficiently
large theta spaces with integer-valued polynomials on the union of
the lines $c_0\alpha^j\mathbb Z_p$. The lines coincide at split primes
and have distinct nonzero residue directions otherwise. The
characteristic exponents are computed by greedy Newton bases.
The [symbol derivative](../notes/cubic-symbol-derivative-lattices.md)
requires both $P(D_j)$ and $P'(D_j)$ to be integral. For $m$ lines
and $n<p^2$, its local relative length is exactly
$(n+1-m(p-1)-1)_+$; at small primes it is at most
$(n+1)(1+\lceil\log_2(n+1)\rceil)$. Thus the global relative
difference has the truncated-prime hinge with error
$O(X^{3/2}\log X)$ before division by $X=n+1$. Its Mellin
multiplier has no zeta factor. The collective global degree/norm
saving remains open, and the symbol derivative is not automatically
a global commutator with a meromorphic theta coordinate.

The [marked point theorem](../notes/cubic-point-shapes-and-rigidity.md)
classifies the new two-sided points as irreducible rank three or an
irreducible outer block with middle line, in either characteristic.
In the normalized cross-block tensor both determinants equal
$\chi_{-3}$. Its fixed spaces all have even dimension, so the usual
rank-one Euler-system hypothesis cannot hold on the cyclotomic kernel.
The cross-block finite Selmer vanishing and actual point arithmetic
remain unproved. The [3-primary local comparison](../notes/cubic-three-primary-local-defects.md)
uses the exact conductor exponent two of the cubic character,
distinct from the first cyclotomic character's exponent three.
It bounds normalized lifting losses by one, and aggregate residual
generator ranks by the moving abelian class-group 3-rank plus
sixteen per cubic sign. The completely untwisted sectors vanish
by the fixed cubic cyclotomic calculation and full local condition
at 3. Integral lengths in the moving exceptional sectors are open.

The [unconditional two-prime theorem](../../notes/unconditional-quadratic-selection.md)
supplies all the original numerical corrected companion and thin
estimates without uniform QRH. Both original primes and all congruences
are retained. It uses classical relative progression estimates and
zero-density theorems; the rational specialization has been integrated
in both parent manuscript sources. The stronger all-height source
clause is not asserted.

### Eliminating the high-dyadic reducible points

The [corner-elimination theorem](../notes/cubic-corner-elimination.md)
uses residual negative-corner vanishing to eliminate that generator
from the actual minimal integral ring. In particular this holds
when $2^b\ge24\ell(\ell+1)^2$. All negative-weight entries then belong
to the ideal generated by actual weight-minus-one adjacent entries.
At a two-sided reducible outer-block point all these adjacent entries
are zero, forcing every negative entry to be zero, a contradiction.
The proof holds in both characteristics, not merely for the
rationalized deformation ring.

The [actual homogeneous relation count](../notes/cubic-high-dyadic-presentation.md)
uses the marked cocycle normalization, local obstruction lifting and
the relative dimensions to give defining equations in the precise
numbers $0,n_{-1}+1,n_0,n_1-1,n_2-1$ at weights
$-2,-1,0,1,2$. No negative-corner generator or equation remains.
Finiteness of the full degree-zero ring is now equivalent to
exclusion of absolutely irreducible characteristic-$\ell$ curves.
If this curve exclusion and the characteristic-zero irreducible
automorphic attachment with finite-adjoint rigidity are supplied,
the parent abstract length theorem uses only the irreducible
rank-three trace spectrum. The high-dyadic comparison does not
require the cubic cross-block Rankin--Selberg vanishing.

### Direct Euler systems over the Eisenstein field

In the remaining cross-block case put $V=W_F\otimes\lambda$ and
$U=V^\vee(1)$. Shapiro with finite local conditions identifies
the rational tensor Selmer group with $H_f^1(F,V)$.
The [direct image and regulator calculation](../notes/cubic-eisenstein-euler-systems.md)
proves that a nonidentity unipotent occurs in the image of
$G_{K(\mu_{\ell^\infty})}$, using strong irreducibility, the
ell-adic Lie algebra and the two distinct infinite inertia
weights. Thus Rubin's rational rank-one image condition is
available over $F$, although the actual residual lattice
does not meet the corresponding integral conditions.
The two nonzero Hodge--Tate weights are opposite. Local
duality and the Bloch--Kato dimension formula give
\[
 \dim_E\bigoplus_{v\mid\ell}H^1(F_v,U)/H_f^1(F_v,U)=2 .
\]
A genuine Euler system over $F$ with a nontorsion base class
would kill the rational strict dual group under Rubin's theorem;
two independent singular localizations would then kill the
full finite group by Poitou--Tate. Simply projecting the
rational Rankin--Selberg system does not yield its required
one-prime ray-class norm relations, and the checked higher-rank
descent framework retains residual image hypotheses.
No such two-class regulator or full vanishing has been proved.
The high-dyadic elimination above should therefore be used
before attempting this remaining Euler-system construction.

## 8. An independent global interpolation construction

There is a global arithmetic alternative for the finite-order
assertion that does not use the CM maps or their Selmer bounds.
Fix a totally imaginary number field $E$ and put

```math
\mathcal P_{n,r}(E)=
\{f\in E[X]_{\le n}:[x_0,\ldots,x_s]f\in\mathcal O_E
\text{ for all integral nodes and }s\le\min(r,n)\}.
```

The [interpolation proof](../notes/global-interpolation-lattices.md)
gives the precise local characteristic exponent at residue
cardinality $q$:

```math
w_q(k,r)=\sum_{j\ge1}(\lfloor k/q^j\rfloor-r)_+ .
```

A digit ordering realizes this exponent for the Newton basis.
Using the successive minima of each prime-power ideal lattice
and bounded representatives of its residue classes, the same
explicit set of $O_E(n+1)$ algebraic integers of height
$O_E((n+1)^{1/[E:\mathbb Q]})$ tests every local polynomial
lattice of degree at most $n$ (the chosen digit subsequences
can differ with the place). The actual global maximal-minor
ideals of the evaluation matrices therefore give

```math
\log\#(\mathcal P_{n,0}/\mathcal P_{n,1})
=\sum_{k=0}^n\psi_E(k)=\int_1^{n+1}\psi_E(t)\,dt.
```

Here $\psi_E$ sums $\log N\mathfrak p$ over prime-ideal powers.
No Dirichlet base case or Frobenius-divisor patch is a premise
of the equality.

The [derivative refinement](../notes/global-derivative-lattices.md)
uses $\Lambda_n=\mathcal P_{n,0}$ and
$H_n=\{f\in\Lambda_n:f'\in\Lambda_n\}$. At every degree-one
prime $p>\sqrt n$ the derivative condition recovers the
first-divided-difference lattice exactly: in the Newton basis
the derivative reductions on each first residue class give
triangular systems in the second digit, with leading coefficient
$m\ne0\bmod p$ for $m=\lfloor k/p\rfloor<p$.
All omitted places cost only $O_E((n+1)^{3/2})$ by the
elementary higher-rational-prime-power bound. Thus

```math
0\le \int_1^{n+1}\psi_E(t)\,dt-\log\#(\Lambda_n/H_n)
\ll_E (n+1)^{3/2}.
```

Only values and ordinary derivatives at the bounded test set
are now needed; the two global matrices are $V$ and
$V'=(V;VD)$, where $D$ is polynomial differentiation.
They have linearly many rows. Adding linearly many integral
points approximating circles of radius of order $n^2$ at
every embedding makes the scaled value Gram matrices uniformly
conditioned and the stacked derivative Gram penalty $O_E(1/n)$
in log determinant, without changing either integral preimage.
If $\mathscr V$ is the normalized covolume of the actual
saturated image lattice, this gives

```math
\log\frac{\mathscr V(L_{V'})}{\mathscr V(L_V)}
 =\log\#(\Lambda_n/H_n)+O_E(1/n).
```

The decisive remaining sufficient inequality is

```math
\log\frac{\mathscr V(L_{V'})}{\mathscr V(L_V)}
 \ge \frac{(n+1)^2}{2}
  - O_{E,\epsilon}((n+1)^{3/2+\epsilon})
```

on arbitrarily late whole fixed-ratio polynomial windows
at every accuracy. To see the implication, set
$I_E(x)=\int_1^x\psi_E(t)\,dt$. The Mellin transform of
$x/2-I_E(x)/x$ equals
$1/(2(s-1))+\zeta'_E(s)/(s(s+1)\zeta_E(s))$ for $\Re s>1$.
Its principal pole cancels and at a real zero $\rho>0$
the residue is positive. Theorem 2.1 therefore applies,
using monotone interpolation even if the lower bound is
only supplied at $n+1=j^2$. This would prove RH for $\zeta_E$,
and for every totally imaginary Galois $E$ would settle
the finite-order Hecke problem by our Galois reduction.

The covolume inequality is **open**. Local divisibilities
and stable Gram matrices do not by themselves give the
integral index lower bound. The actual finite-dimensional
construction is proved, not the necessary asymptotic
estimate. The exact
[HNF check](../certificates/derivative-lattice-check.json)
in the S3 field verifies the small-degree value/derivative
indices for degrees 3–10, not the asymptotic bound.
This route is independent of the retained CM and spectral
alternatives; the infinite-order phase estimate remains open.

### The remaining high-dyadic point problem

For the cubic frame, the [strong-irreducibility and monodromy argument](../notes/cubic-irreducible-monodromy.md) applies to the actual characteristic-prime curves as well as characteristic-zero points. A prime-dimensional imprimitive representation would give a trace identity on the kernel of its finite permutation action, contradicting independence of the distinct restricted residual characters. The dyadic ratios have order greater than six. Finite determinant then forces the connected algebraic monodromy to be semisimple; in dimension three the proper irreducible alternative is orthogonal. Its essentially self-dual residual character relation is impossible for the diagonal $(a\lambda^{-1},1,a^{-1}\lambda^{-1})$, since $a^c=a$ and $\lambda^c=\lambda^{-1}$ with $\lambda$ of order three. The connected group is therefore $\mathrm{SL}_3$.

The [integral trace-generation theorem](../notes/cubic-trace-and-adjoint.md) recovers the three coordinate projectors from the separating mark and writes all balanced entry monomials as closed matrix-cycle traces. The complete invariant algebra is the closed trace algebra, including its torsion and nilpotents. A finite fixed-weight Hecke comparison on the actual characteristic-prime curves would force their characteristic polynomials to be constant, excluding irreducibility. For characteristic-zero points the same note establishes the finite local conditions for the actual dual-number tangents, using the ordered weight filtration and local duality. Cuspidal attachment then implies adjoint vanishing by Thorne's theorem and hence normalized tangent rigidity. These two point premises remain open.

The [automorphic starting-packet construction and audit](../notes/cubic-automorphic-seed-frontier.md) produces an ordinary conjugate-self-dual $2+1$ isobaric packet at auxiliary weights using the parent rank-two construction, for coefficient primes prime to the host conductor. The needed cuspidal GL3 packet is not yet supplied. The symmetric-square seed is excluded by the residual self-duality relation, and the checked level-raising and residually reducible automorphy-lifting theorems have unmet hypotheses. The original deep auxiliary tower additionally requires a new cubic-component class-rank bound. The parent abelian Ferrero–Washington estimate only controls the invariant component. Thus neither irreducible point premise is discharged, and the high-dyadic length comparison remains conditional. The lower-dyadic Euler-system strategy is unchanged.

## 9. Remaining work and provenance

The preferred proof is self-contained within the
repository relative to the stated classical results;
its analytic and algebraic arguments require no
external crowdsourced proof. The new arithmetic
estimates remain missing, and the relative route
also needs our completed Dirichlet proof if used
for the final independent manuscript.

Masullo's proposed strip-trace formula and the
RiemannMasullo contributors' work inspired the earlier
compact-test transfer. We retain the
[full smoothed and trace route](smoothed-and-trace.md)
and [technical transfer note](../notes/masullo-transfer.md)
as alternatives. They credit the originating results
and record their exact hypotheses. If the spectral
route is ever adopted as a required input, its
necessary geometric lemmas must be proved in
ordinary mathematics in this repository. A missing
trace comparison is not an admissible premise of a
claimed final proof.

See the [source register](../sources/README.md) for
classical references and precise attribution,
the [proof program](../blueprint/program.md) for
dependencies, and the [checkpoint](../notes/current-state.md)
for the current research frontier.
