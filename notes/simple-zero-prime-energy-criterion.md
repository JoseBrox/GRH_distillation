# A prime-side energy criterion for RH and simple zeros

**Status (22 November 2026): proved equivalences; the decisive prime-side upper bound remains OPEN.** This is an exact mathematical reduction using the corrected prime sum in [the RH analytic manuscript](../paper/rh/sections/02-analytic-endpoint.tex), not a proof of the Riemann hypothesis or the simple-zero conjecture. No source-wide Lean rebuild or new source theorem is claimed.

## 1. One scalar inequality detects all multiple zeros

Let $\gamma_E$ be Euler's constant and define for $x\ge1$

```math
G(x)=\sum_{n\le x}\Lambda(n)(x/n-1)
       -x\log x+(1+\gamma_E)x,\qquad
\mathcal M(X)=\frac{1}{\log X}
                 \int_1^X\frac{G(x)^2}{x^2}\,dx\quad(X>1).
```

Let $\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$, and set

```math
C_0=2+\gamma_E-\log(4\pi)
 =0.04619141793224206762\ldots,
```

```math
C_2=2C_0-2\left.\frac{d^2}{ds^2}\log\xi(s)\right|_{s=0}
 =0.0000742012728749297430\ldots .
\tag{1}
```

**Theorem 1 (exact arithmetic criterion).**
(a) RH holds if and only if $\limsup_{X\to\infty}\mathcal M(X)<\infty$.
(b) Under RH, the ordinary limit exists and equals

```math
\lim_{X\to\infty}\mathcal M(X)
 =\sum_{\gamma\ \text{distinct}}
   \frac{m_\gamma^2}{(\gamma^2+1/4)^2},
\qquad
C_2=\sum_{\gamma\ \text{distinct}}
   \frac{m_\gamma}{(\gamma^2+1/4)^2}.
\tag{2}
```

Here $\rho=1/2+i\gamma$ runs over nontrivial zeta zeros and $m_\gamma$ is its positive integer multiplicity (the sum includes both signs of $\gamma$).
(c) Consequently

```math
\boxed{\text{RH and every nontrivial zero simple}
 \ \Longleftrightarrow\
 \limsup_{X\to\infty}\mathcal M(X)\le C_2.}
\tag{3}
```

**Proof.** For $\Re s>1$, the source's Mellin calculation gives

```math
F(s):=\int_1^\infty G(x)x^{-s-1}\,dx
=-\frac{\zeta'(s)/\zeta(s)}{s(s-1)}
-\frac1{(s-1)^2}+\frac{1+\gamma_E}{s-1}.
\tag{4}
```

It continues meromorphically and has residue
$-m_\rho/[\rho(\rho-1)]\ne0$ at every nontrivial zeta zero.
Put $h(u)=e^{-u/2}G(e^u)$ and $B(U)=\int_0^U|h(u)|^2du$.
If the limsup in (a) is finite, then $B(U)=O(U)$, so for every
$\alpha>0$,

```math
\int_0^\infty e^{-\alpha u}|h(u)|^2du
=\alpha\int_0^\infty e^{-\alpha U}B(U)\,dU<\infty.
```

Cauchy--Schwarz makes the Laplace transform of $h$ absolutely
convergent and holomorphic for $\Re(s-1/2)>0$. It agrees with
$F(s)$ when $\Re s>1$, thus elsewhere by analytic continuation.
Therefore no nontrivial zero can have $\Re\rho>1/2$, and the
functional equation gives RH. This proves one implication in (a).

For the reverse implication and (b), the classical smoothed von
Mangoldt explicit formula, valid for $x>1$, is

```math
G(x)=\log(2\pi)
 -\sum_\rho\frac{m_\rho x^\rho}{\rho(\rho-1)}
 -\sum_{k\ge1}\frac{x^{-2k}}{2k(2k+1)}.
\tag{5}
```

The sum over zeros is absolutely convergent because its denominator
is quadratic in the ordinate. Under RH, writing
$\rho=1/2+i\gamma$, (5) implies

```math
h(u)=\sum_{\gamma\ \mathrm{distinct}}
 \frac{m_\gamma}{\gamma^2+1/4}e^{i\gamma u}
 +O(e^{-u/2})\qquad(u\ge0).
\tag{6}
```

The Fourier series is absolutely and uniformly convergent, since
$\sum_\gamma m_\gamma/(\gamma^2+1/4)=C_0<\infty$.
Hence $h$ is bounded, proving the other implication in (a).
Expanding the square of (6), then averaging on $[0,U]$, kills all
distinct-frequency cross terms. Absolute convergence justifies
dominated passage through the double sum; the decaying correction
does not change the limit. This proves the first equality in (2).

For the second equality use the Hadamard product of $\xi$ and
the absolutely convergent partial fraction identity

```math
\frac1{\rho^2(1-\rho)^2}
=\frac1{\rho^2}+\frac1{(1-\rho)^2}
       +\frac2{\rho(1-\rho)}.
```

The symmetry $\rho\leftrightarrow1-\rho$ yields
$\sum_\rho m_\rho/\rho^2=-(\log\xi)''(0)$,
while $\sum_\rho m_\rho/[\rho(1-\rho)]=C_0$.
On RH, $\rho(1-\rho)=\gamma^2+1/4$, proving (1)--(2).
Subtracting the two sides of (2) now gives

```math
\lim_{X\to\infty}\mathcal M(X)-C_2
=\sum_{\gamma\ \mathrm{distinct}}
 \frac{m_\gamma(m_\gamma-1)}{(\gamma^2+1/4)^2}\ \ge0.
\tag{7}
```

Every term is nonnegative, and it is zero exactly when
$m_\gamma=1$. Combining this with (a) proves (c). QED.

**Quantitative consequence.** For a multiple conjugate pair
$\pm\gamma$ with $m_\gamma\ge2$, the defect in (7) is at least
$4/(\gamma^2+1/4)^2$. Thus an exact bound on that defect rules out
multiple zeros up to a prescribed height. There is no *uniform
positive gap* over all heights, so approximate numerical equality
alone can never settle all zeros.

## 2. Primitive Dirichlet L-functions

For a fixed nonprincipal primitive character $\chi$, use the complex
corrected sum already in the manuscript,

```math
G_\chi(x)=\sum_{n\le x}\Lambda(n)\chi(n)(x/n-1)
 +x\frac{L'(1,\chi)}{L(1,\chi)}.
```

Write $\Lambda_\chi(s)=(q/\pi)^{(s+a)/2}
\Gamma((s+a)/2)L(s,\chi)$, with $a=0$ or $1$
the character parity, and define the explicit constant

```math
C_{\chi,2}=
-\left.(\log\Lambda_\chi)''\right|_{s=0}
-\left.(\log\Lambda_\chi)''\right|_{s=1}
+2\left(
 \frac{\Lambda_\chi'(1)}{\Lambda_\chi(1)}
-\frac{\Lambda_\chi'(0)}{\Lambda_\chi(0)}
\right).
\tag{8}
```

The two endpoint values of the completed nonprincipal primitive
function are nonzero. Its Hadamard product shows that
$C_{\chi,2}=\sum_{\rho}m_\chi(\rho)/[\rho^2(1-\rho)^2]$;
on GRH all summands are real and positive.
The Mellin transform of $G_\chi$ is the source's
$-[L'/L]/[s(s-1)]+[L'(1,\chi)/L(1,\chi)]/(s-1)$,
so the same finite-limsup argument excludes zeros to the right
of one half. The functional equation together with conjugation
reflects zeros **of the same primitive $\chi$** across that line.
Conversely, shifting the Mellin contour past its nontrivial zeros,
the remaining poles at zero and the trivial zeros contribute
$O_\chi(1+\log x)$. Thus on GRH

```math
e^{-u/2}G_\chi(e^u)
 =\sum_{\gamma\ \mathrm{distinct}}
  \frac{m_\chi(1/2+i\gamma)}{\gamma^2+1/4}e^{i\gamma u}
  +O_\chi((1+u)e^{-u/2}).
```

The same almost-periodic Parseval proof now yields the analogous
equivalence, for that fixed character, between
**GRH for $\chi$ plus all its zeros simple** and the single inequality

```math
\limsup_{X\to\infty}\frac1{\log X}
 \int_1^X\frac{|G_\chi(x)|^2}{x^2}\,dx
 \le C_{\chi,2}.
\tag{9}
```

For the conductor-one character, use (1)--(3). No uniformity in
$\chi$ is claimed or needed for these equivalences.

## 3. A positive finite-window certificate for one zero

Assume RH, and define the following *entirely prime-side* even
function for real $u$:

```math
V(u)=e^{-|u|/2}\left[
G(e^{|u|})-\log(2\pi)
+\sum_{k\ge1}\frac{e^{-2k|u|}}{2k(2k+1)}
\right].
```

By (5)--(6), $V(u)=\sum_\gamma a_\gamma e^{i\gamma u}$,
with $a_\gamma=m_\gamma/(\gamma^2+1/4)>0$.
For $T>0$, $t\in\mathbb R$, put

```math
\mathcal F_T(t)=\frac1T\int_{-T}^T
 \left(1-\frac{|u|}{T}\right)V(u)e^{-itu}\,du .
```

The triangular kernel has nonnegative Fourier transform, so

```math
\mathcal F_T(t)=\sum_\gamma a_\gamma
 \left(\frac{\sin((\gamma-t)T/2)}
 {(\gamma-t)T/2}\right)^2\ge0.
\tag{10}
```

At a zero of ordinate $t=\gamma_0$, all terms are nonnegative,
so $m_{\gamma_0}\le(\gamma_0^2+1/4)\mathcal F_T(\gamma_0)$.
Consequently the **strict inequality**

```math
(\gamma_0^2+1/4)\mathcal F_T(\gamma_0)<2
\tag{11}
```

is a finite-window *sufficient certificate* of simplicity at that
zero. Conversely, if the zero is simple, then (10) tends to
$1/(\gamma_0^2+1/4)$ as $T\to\infty$; some finite $T$ passes
(11). Thus (11) for some $T$ is exactly equivalent to simplicity
of the specified zero, conditional on RH. The integrand in (10)
depends only on primes up to $e^T$ and elementary correction terms.

## 4. The genuinely open step

These exact identities do **not** prove (3) or (9). Under RH the
trivial estimate $|V(u)|\le C_0$ only yields

```math
\lim_{X\to\infty}\mathcal M(X)\le C_0^2
 =0.00213364709059105\ldots
 \quad\text{versus}\quad
 C_2=0.00007420127287493\ldots .
```

The easy upper bound is about **28.75 times too large** to imply
simplicity. The repository's theta/frame Hilbert--Schmidt bounds
concern **different arithmetic operators**, not this logarithmic
prime-square average. There is no proved identity identifying their
trace errors with (7).

What would finish the argument is the new scalar inequality (3),
or the family of inequalities (11) at every zero. In particular, an
asymptotic positive proportion of simple zeros is insufficient:
a single double zero arbitrarily high contributes a tiny but
**strictly positive** term to (7).

**Numerical cross-check only (not proof).** Computing $\xi$ and its
second logarithmic derivative with 50-digit precision gives the
constant (1). Direct sums over the first 100 positive zeta ordinates,
including conjugates, give $0.00007416962834581\ldots$, strictly
below $C_2$ as expected from the positive omitted tail.
The identity in (7) is proved symbolically; these numerical tests
do not establish the required bound.

**Sources.** [Project's Mellin proof](../paper/rh/sections/02-analytic-endpoint.tex);
[standard explicit formula for von Mangoldt's sum](https://mathworld.wolfram.com/MangoldtSummatoryFunction.html);
[Alpöge--Furman 2026](https://arxiv.org/abs/2608.13637);
[Lamzouri 2026](https://arxiv.org/abs/2609.02882).
