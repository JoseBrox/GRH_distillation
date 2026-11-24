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
This permits a precise reuse of the parent algebraic estimates
where their hypotheses hold, but the new uniform cubic length
bound and actual geometric comparison remain open.

## 8. Remaining work and provenance

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
