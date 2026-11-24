---
title: "One-sided arithmetic reductions toward Hecke GRH"
date: "24 November 2026"
---

# One-sided arithmetic reductions toward Hecke GRH

## Abstract

We extend the analytic method of our reconstruction of Alpöge's
Dirichlet GRH proof to unitary Hecke characters of arbitrary number
fields. A positive induction identity reduces the problem, including
infinite-order characters, to totally imaginary Galois fields over
the rationals. For those fields the required zero-free statement is
equivalent to a one-sided estimate of a smoothed weighted count of
completely split rational primes. We give an exact growth law for
the zero-detecting discrepancy, allow arbitrary fixed polynomial
sampling grids, and reduce the estimate to three compact tests at
each rational frequency. The arithmetic estimate is open. A
Masullo-inspired global/local trace comparison is an alternative
supplier, not a premise of the arithmetic reduction.

## 1. The problem

For a number field $F$, let $C_F=\mathbb A_F^\times/F^\times$
and let $N$ be its idelic norm. A continuous unitary Hecke character
$\chi:C_F\to S^1$ has Euler product


```math
L_F(s,\chi)=\prod_{\mathfrak p}
 (1-\chi(\mathfrak p)(N\mathfrak p)^{-s})^{-1},
\qquad \Re s>1.
```


At a ramified character place the corresponding factor is absent.
The Hecke GRH target is the assertion that every zero in the open
critical strip has real part $1/2$. We use the classical continuation,
functional equation, zero count and individual Hecke explicit formula.
Finite and completed L-functions have the same zeros in that strip.

The restriction of a unitary character to a fixed positive-real
norm section is $t^{iu}$ for some real $u$. Removing it merely
translates the zeros vertically. Henceforth characters are normalized
on such a section. The problem includes Dedekind zeta functions,
finite-order and infinite-order Hecke characters, not arbitrary
higher-rank automorphic L-functions.

## 2. Detection by one-sided estimates

Choose a nonnegative smooth profile $h$ supported in
$[a,a+\ell]\subset(0,\infty)$ with transform


```math
M_h(w)=\int h(t)e^{wt}\,dt
```


nonzero on $|\Re w|\le1/2$. One construction is to multiply the
density of $a+\sum_{j\ge1}U_j$, with independent uniforms on
$[0,\ell 2^{-j}]$, by $e^t$. The transform is a locally uniformly
convergent product of the factors


```math
\frac{e^{\ell2^{-j}(w+1)}-1}{\ell2^{-j}(w+1)}
```


times $e^{a(w+1)}$. All factors are nonzero on the strip;
arbitrarily many initial factors give rapid Fourier decay.
This construction is due to the RiemannMasullo discussion
cited in the [source register](../sources/README.md).
For polar-free trace comparisons use $H=h/4-h''$ instead:
$M_H(w)=(1/4-w^2)M_h(w)$ cancels both polar values and stays
nonzero in the open strip, positive at real interior points.

For a fixed finite positive family of normalized characters
with weights $c_\chi>0$, put $w_\rho=\rho-1/2$. In any
symmetric band $r\le|\Re w|<R$, $0\le r<R\le1/2$, let


```math
f(y)=\Re\sum_\chi c_\chi\sum_{\rho\ \mathrm{in\ band}}
 m_\chi(\rho)M_P(w_\rho)e^{w_\rho y},
 \qquad P=h\ \text{or}\ H .
```


The series and all fixed-order derivatives on compact intervals
converge absolutely by rapid transform decay and the classical
fixed-character zero count. Write $\beta$ for the supremum of
the selected centered real parts (zero if empty). By symmetry
$\beta\ge0$.

**Theorem 2.1 (exact obstruction growth).** For $b>1$, $\theta\ge0$,


```math
\lim_{U\to\infty}\frac1U\log
\left(1+\int_U^{bU}f(y)_+e^{-\theta y}\,dy\right)
=b(\beta-\theta)_+ .
```


*Proof.* Absolute summability gives $|f(y)|\le Ce^{\beta y}$.
Its Laplace transform has the normally convergent meromorphic
partial fractions


```math
\frac12\sum_{\chi,\rho}c_\chi m_\chi(\rho)
\left(\frac{M_P(w_\rho)}{s-w_\rho}
+\frac{\overline{M_P(w_\rho)}}{s-\overline{w_\rho}}\right).
```


The transform is nonzero at every selected zero; at coincident
poles all multiplicities have the same positive sign, and at
real poles the residues are positive. Thus our Dirichlet
[one-sided Laplace criterion](../../paper/sections/recovered/03-sec-one-sided.tex)
applies. If $\beta>\theta$, take $\theta<\theta'<\beta$ and
$1<c<b$. The integral with weight $e^{-\theta' y}$ over
$[cU,bU]$ must eventually be at least one; otherwise a cofinal
subexponential sequence excludes a pole to the right of
$\theta'$. Changing the weight gains $e^{(\theta'-\theta)cU}$.
Let $\theta'\uparrow\beta$ and $c\uparrow b$. The upper bound
follows from $|f(y)|\le Ce^{\beta y}$. No maximal zero is
required. QED.

## 3. Finite arithmetic tests

**Theorem 3.1 (polynomial sampling).** Fix any $q>0$.
On the grid $x_k=k^q$, the function $F(x)=f(\log x)$ has
$|F''(x)|\le C x^{\beta-2}$. The affine chord error is
$O(x^{\beta-2/q})$. If $\beta>\theta$, its weighted integral
on a polynomial window has strictly smaller exponential growth
than the positive-part integral of Theorem 2.1. Consequently
upper tables at every sample on arbitrarily late whole windows,
with subpower weighted positive-part interpolated cost,
imply $\beta\le\theta$. The proof does not require knowing
$\beta$ when constructing the table.

**Theorem 3.2 (three compact tests).** For each rational $\gamma$,
integer $k\ge1$ and $\omega^3=1$, integrate translates of the
profile against the nonnegative weight


```math
(4-\theta)^k\mathbf1_{[k/8,k/2]}(y)
 \frac{y^ke^{-4y}}{k!}
 \bigl(1+\Re(\omega e^{-i\gamma y})\bigr),
\qquad 0\le\theta<1/2.
```


The resulting test is smooth and compactly supported above
log norm zero; if $P=H$ it remains polar-free. Let
$J_{k,\gamma,\omega}$ be its real normalized discrepancy.
A subexponential bound on the maximum positive part of the
three values on a cofinal $k$ sequence for each fixed
$\gamma$ implies $\beta\le\theta$. The sequence may depend
on $\gamma$, but must be common to the phases.

Indeed the three phases recover at least half the absolute
value of the complex Laplace derivative while retaining the
signed real derivative. Truncating the Gamma tails costs
$O(4^{-k})$ before normalization. Cauchy's coefficient
estimate at a uniquely nearest pole contradicts the budget
if its real part exceeds $\theta$; the case of a nearest
real pole uses its positive residue. The explicit Gamma
bounds and nearest-pole argument are proved in
[the full analytic note, §4](../notes/masullo-transfer.md).

At $\theta=0$ either criterion proves the critical line for
the full band, or emptiness of any positive exterior band.

## 4. Only degree-one prime ideals are needed

In the full band with $P=h$ let


```math
a_\chi(n)=\sum_{N\mathfrak p^m=n}
 \log N\mathfrak p\,\chi(\mathfrak p)^m,\qquad
A(n)=\sum_\chi c_\chi\Re a_\chi(n).
```


The individual explicit formula for the positive-log
translated profile gives


```math
f(y)=c_1e^{y/2}M_h(1/2)-
 \sum_n\frac{A(n)}{\sqrt n}h(\log n-y)
 +O(e^{-y/2}),
```


where $c_1$ is the weight of the trivial character, possibly
zero. The conductor term vanishes, and the lower polar and
archimedean terms decay. The coefficient bound


```math
|a_\chi(p^j)|\le[F:\mathbb Q]\log p
```


follows by summing the residue degrees above $p$ that divide
$j$. Chebyshev's estimate
$\sum_{p^j\le X,\,j\ge2}\log p=O(\sqrt X)$, together with
the fixed compact moving support, gives an $O(1)$ bound for
the higher rational prime powers. Thus the degree-one prime
deficit differs from $f(y)$ by only $O(1)$, preserving the
three preceding criteria.

For finite-order characters one has an exact positive
nonabelian Fourier kernel. If $N_0\trianglelefteq H_0\le G$
with abelian quotient $A_0=H_0/N_0$ and
$V_\lambda=\operatorname{Ind}_{H_0}^G\lambda$, then for
$a=gN_0$ and inertia $I_p$,


```math
\sum_{\lambda\in\widehat A_0}\overline{\lambda(a)}
 \operatorname{tr}(V_\lambda(F_p)^k|V_\lambda^{I_p})
=\frac{\#\{(u,i)\in G\times I_p:
 u^{-1}F_p^kiu\in gN_0\}}{|N_0||I_p|}\ge0 .
```


This follows from the induced-character formula, finite
orthogonality, and the averaging projector onto inertia
invariants. Each induced L-function is an actual Hecke
L-function of the appropriate fixed field, by abelian
reciprocity. We require no general Artin holomorphy.
See [the full note, §6](../notes/masullo-transfer.md) for the
ramified Euler factors and positive-family transfer.

## 5. Arbitrary characters reduce to Galois fields

**Theorem 5.1.** If $K/F$ is finite Galois and $\chi$ is any
unitary Hecke character, every zero of $L_F(s,\chi)$ in the
open strip occurs in $L_K(s,\chi\circ N_{K/F})$ with at least
the same multiplicity.

*Proof.* Let $J=\operatorname{Gal}(K/F)$, $n=|J|$. For
each nontrivial cyclic subgroup $C$, set


```math
d_{C,\lambda}=\sum_{u\in\operatorname{Gen}(C)}
 (1-\overline{\lambda(u)})\in\mathbb Z_{>0},
 \qquad \lambda\ne1.
```


Fourier expansion of the mean-zero function on $C$ equal
to $\varphi(|C|)$ at the identity, $-1$ on generators,
and zero elsewhere gives the positive induction identity


```math
n(\operatorname{Reg}_J-1_J)=
 \sum_{C,\lambda\ne1}d_{C,\lambda}\operatorname{Ind}_C^J\lambda .
```


The sum is over each cyclic subgroup once. Its right side
equals $-n$ at nonidentity elements and $n(n-1)$ at the
identity. The coefficients are rational algebraic integers
by cyclotomic symmetry and positive by their real parts.

Twist by $\chi$, omit the finitely many bad places $S$,
and use unramified determinant Euler factors:


```math
\left(\frac{L_K^S(s,\chi\circ N_{K/F})}{L_F^S(s,\chi)}\right)^n
 =\prod_{C,\lambda\ne1}
 L_{K^C}^S(s,(\chi\circ N_{K^C/F})\lambda)^{d_{C,\lambda}} .
```


Here $\lambda$ denotes the associated finite-order Hecke
character of $K^C$. The orbit calculation on $J/C$ gives
the local induction factor (see the detailed proof in
[the Galois note](../notes/galois-base-change.md)).
All factors on the right are holomorphic in the open
strip; the exponents are positive integers. Taking orders
gives the claimed inequality, and omitted unitary Euler
factors do not change orders there. QED.

Taking a normal closure over the rationals and adjoining
$i$ reduces the problem for all unitary characters to
totally imaginary Galois fields. This does not assert
the resulting fields are CM.

For a fixed such field $K$ and fixed normalized $\xi$,
take the positive family of the trivial character and
$\xi$. Outside the finite bad set, degree-one prime
ideals occur precisely over completely split primes.
Their nonnegative weights are


```math
A_\xi(p)=\sum_{\mathfrak p\mid p}(1+\Re\xi(\mathfrak p)).
```


**Main reduction.** Full Hecke GRH is equivalent to the
subexponential positive-part bound, on arbitrarily late
fixed-ratio windows, for each of the deficits


```math
D_{K,\xi}(y)=(1+\mathbf1_{\xi=1})e^{y/2}M_h(1/2)
-\sum_{p\ \mathrm{split}}
 \frac{\log p}{\sqrt p}h(\log p-y)A_\xi(p).
```


Indeed Section 4 makes this the full spectral sum up to
bounded error; Theorem 2.1 at $\theta=0$ detects all
off-line zeros, and Theorem 5.1 transfers the conclusion
to every base field. Conversely GRH makes the full
spectral sum bounded. For the finite-order subproblem
unweighted Dedekind-zeta deficits suffice by abelian
class-field factorization. Infinite-order character
phases remain essential.

## 6. The unresolved supplier

Our preferred arithmetic goal is the above split-prime
estimate for each fixed field and character. The first
nonabelian benchmark is the Dedekind zeta function of
the S3 normal closure of the cubic field generated by
the cube root of 2. The original Dirichlet proof's
integral Selmer, theta, norm and height constructions
are not automatically available for these coefficients.
The precise missing arithmetic estimate is in
[the frontier](../notes/open-frontier.md).

Alternatively, Masullo's strip-projection approach has
a band discrepancy given by left limits of the global
diagonal traces, with all edge orders included. Theorem
3.2 allows a one-sided quantitative estimate for actual
operators instead of an exact pointwise trace identity.
The normed-space, kernel and measure identifications
and the actual trace budget must still be supplied.
The primary arithmetic route does not depend on this
comparison or on the outcome of the crowdsourced proof.

All new claims here are reductions with the displayed
classical inputs, not a completed Hecke GRH proof or
new Lean verification. See the [sources](../sources/README.md),
[proof map](../blueprint/proof.svg) and
[limitations](../negative-results/README.md).
