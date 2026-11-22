# A one-sided critical-scale criterion for simple zeros

**Status (22 November 2026): the implication below is proved; the arithmetic upper bound is OPEN.** This note pursues an alternative to the exact second-moment criterion in [the companion note](simple-zero-prime-energy-criterion.md). Its critical-scale estimate is not a consequence of the present RH/GRH analytic and arithmetic bounds, and it is **not** a proof of simplicity.

## 1. A general one-sided boundary-pole lemma

**Lemma.** Let $H:[1,\infty)\to\mathbb R$ be locally integrable, with Mellin transform

```math
F(s)=\int_1^\infty H(x)x^{-s-1}\,dx
```

initially convergent for sufficiently large $\mathrm{Re}\,s$.
Suppose $F$ continues meromorphically to an open neighborhood
of the closed half-plane $\mathrm{Re}\,s\ge\theta$;
it is holomorphic at every *real* $s\ge\theta$.
If $H(x)\le Cx^\theta$ for all sufficiently large $x$, then

1. $F$ has no poles in $\mathrm{Re}\,s>\theta$;
2. $F$ has no pole of order at least two on $\mathrm{Re}\,s=\theta$.

The same conclusion holds with continuation to a region containing
$\mathrm{Re}\,s>\theta$ and the boundary points under consideration,
with holomorphy at $s=\theta$.

**Proof.** Increase $C$ if necessary to make it positive. Choose
$X_0\ge1$ so $f(x)=Cx^\theta-H(x)\ge0$ for $x\ge X_0$.
Its Mellin transform is initially

```math
\widehat f(s)=\frac{CX_0^{\theta-s}}{s-\theta}
 -F(s)+E(s),\quad
E(s)=\int_1^{X_0}H(x)x^{-s-1}\,dx,
\tag{1}
```

with $E$ entire. Since (1) is holomorphic at all real $s>\theta$,
the classical Landau theorem for nonnegative Mellin integrands
([proved in our RH manuscript](../paper/rh/sections/02-analytic-endpoint.tex))
forces its abscissa of convergence to be at most $\theta$.
Hence $\widehat f$ is holomorphic for $\mathrm{Re}\,s>\theta$,
and (1) gives part 1.

At $s=\theta+\delta$, $F$ and $E$ are holomorphic at
$\theta$, so nonnegativity and (1) imply

```math
0\le\widehat f(\theta+\delta)=\frac C\delta+O(1)
\qquad(\delta\downarrow0).
```

For each real $t$, the triangle inequality and $f\ge0$ yield

```math
|\widehat f(\theta+\delta+it)|
\le\widehat f(\theta+\delta)=O(\delta^{-1}).
```

For $t\ne0$, the rational term in (1) remains bounded as
$\delta\downarrow0$. Thus
$F(\theta+\delta+it)=O(\delta^{-1})$, excluding a pole of
order at least two. At $t=0$, $F$ is holomorphic by hypothesis.
This proves part 2. QED.

**Important:** A simple off-real pole in the right half-plane is
also excluded; a function may have no pole there despite having an
underlying *simple* zero of some other meromorphic function.

## 2. The nonnegative second von Mangoldt coefficient

Let $\Lambda$ be von Mangoldt's function and let $*$ denote
Dirichlet convolution. Define

```math
b(n)=(\Lambda*\Lambda)(n)+\Lambda(n)\log n\ge0.
\tag{2}
```

Differentiating the Euler product proves, initially for
$\mathrm{Re}\,s>1$,

```math
\frac{\zeta''(s)}{\zeta(s)}
=\sum_{n\ge1}\frac{b(n)}{n^s}.
\tag{3}
```

Write $\gamma_E$ for Euler's constant and $\gamma_1$ for
the first Stieltjes constant, with convention

```math
\zeta(1+z)=z^{-1}+\gamma_E-\gamma_1z+O(z^2).
```

Let

```math
P_2(t)=t^2-2(1+\gamma_E)t+
 2(1+\gamma_E+\gamma_E^2+\gamma_1)
\tag{4}
```

and define the *centered second-prime ramp*

```math
H_2(x)=\sum_{n\le x}b(n)(x/n-1)_+
       -xP_2(\log x),\qquad x\ge1.
\tag{5}
```

**Theorem (a one-sided sufficient condition for simplicity).**
If there exist finite $C$ and $X_0$ such that

```math
\boxed{H_2(x)\le C\sqrt{x}\qquad(x\ge X_0),}
\tag{6}
```

then *every nontrivial zero of the Riemann zeta function is simple*.
No RH assumption is needed.

**Proof.** Termwise Mellin integration of (3) and of the explicit
centering polynomial gives

```math
F_2(s)=\int_1^\infty H_2(x)x^{-s-1}\,dx
=\frac{\zeta''(s)/\zeta(s)}{s(s-1)}
-\frac2{(s-1)^3}
+\frac{2(1+\gamma_E)}{(s-1)^2}
-\frac{2(1+\gamma_E+\gamma_E^2+\gamma_1)}{s-1}.
\tag{7}
```

The Laurent expansion at $s=1$ is

```math
\frac{\zeta''(s)/\zeta(s)}{s(s-1)}
=\frac2{(s-1)^3}
-\frac{2(1+\gamma_E)}{(s-1)^2}
+\frac{2(1+\gamma_E+\gamma_E^2+\gamma_1)}{s-1}
+O(1).
\tag{8}
```

Thus $F_2$ is holomorphic at $1$. It is holomorphic
at every real $s>0$ apart from possible $s=0$, because
zeta has no real zeros for $0<s<1$, and is holomorphic
at $s=1/2$ in particular. (The positivity of the alternating
eta series establishes $\zeta(s)<0$ on $0<s<1$.)

Apply the preceding lemma to $H_2$ with $\theta=1/2$.
Assumption (6) rules out every pole of $F_2$ for
$\mathrm{Re}\,s>1/2$, and every pole of order at least two on
$\mathrm{Re}\,s=1/2$.

But if $\rho$ were a zero of $\zeta$ of multiplicity
$m\ge2$, a local expansion gives

```math
\frac{\zeta''(s)}{\zeta(s)}
=\frac{m(m-1)}{(s-\rho)^2}+O((s-\rho)^{-1}),
```

and hence, since $\rho\notin\{0,1\}$,

```math
F_2(s)=\frac{m(m-1)}{\rho(\rho-1)}
 (s-\rho)^{-2}+O((s-\rho)^{-1}).
\tag{9}
```

This genuine double pole is impossible if
$\mathrm{Re}\,\rho\ge1/2$.
A zero with $\mathrm{Re}\,\rho<1/2$ has a zero
of the same multiplicity at $1-\overline\rho$,
to the right of one half, by the functional equation
and conjugation. All multiple zeros are therefore excluded. QED.

This argument does **not** show RH: at a simple off-line zero,
$\zeta''/\zeta$ has at most a simple pole and might even be
holomorphic if $\zeta''(\rho)=0$. The theorem targets
*simplicity alone*, and (6) is not established.

## 3. Dirichlet version: a two-sided sufficient condition

For nonprincipal primitive $\chi$, write
$v_\chi(n)=\Lambda(n)\chi(n)$ and

```math
b_\chi(n)=(v_\chi*v_\chi)(n)+v_\chi(n)\log n,
\quad
H_{2,\chi}(x)=\sum_{n\le x}b_\chi(n)(x/n-1)_+
-x\frac{L''(1,\chi)}{L(1,\chi)}.
\tag{10}
```

The Mellin transform is

```math
F_{2,\chi}(s)=\frac{L''(s,\chi)/L(s,\chi)}{s(s-1)}
-\frac{L''(1,\chi)/L(1,\chi)}{s-1},
\tag{11}
```

holomorphic at $1$. If the *two-sided* estimate
$|H_{2,\chi}(x)|\le C_\chi\sqrt x$ holds eventually,
the Mellin integral converges absolutely for
$\mathrm{Re}\,s>1/2$ and grows at most $O(\delta^{-1})$
at $s=1/2+\delta+it$. A double pole (9), with $L$
in place of zeta, is excluded in that region and on its boundary;
the Dirichlet functional equation and conjugation reflect any
left-half zero to the right within the same primitive character.
Thus all nontrivial zeros of that $L(s,\chi)$ are simple.

The bound for a general character is *two-sided*, not (6):
the coefficients $b_\chi$ need not be real or positive, and
a possible real central zero requires separate attention.
Neither estimate has been established.

## 4. What remains, and checks

This is a sharper **one-sided alternative** to the exact scalar
energy criterion, not its proof. It asks for a square-root
bound on a centered sum over the explicitly nonnegative
prime-pair coefficients (2), rather than the exact global
mean-square constant.

The centering (4) and cancellation (8) were checked
independently by symbolic Laurent expansion. A finite
arithmetic evaluation of (5) at $x=10,100,1000,10000,100000$
was also performed using the exact Dirichlet convolution;
it tests the signs and the normalization, but cannot
establish the eventual upper bound.

The current repo supplies upper comparisons for the **first**
corrected prime ramp $G$, not for the quadratic coefficients
$\Lambda*\Lambda+\Lambda\log$. Its fourth-power sampling and
positive-family transport therefore do not supply (6).
The nonnegative coefficients in (2) alone cannot prove (6):
for $\zeta(s)^m$, with $m\ge2$, the analogous coefficients
are also nonnegative, but the function has multiple zeros
on any zeta zero. A new arithmetic estimate distinguishing
the actual degree-one zeta function would be necessary.

**Conclusion:** Conditional implication proved, arithmetic
hypothesis (6) open. No RH/GRH/simplicity completion claimed
and no existing progress-node status changed.

**Sources:** [RH Mellin and Landau lemmas](../paper/rh/sections/02-analytic-endpoint.tex);
[prime-energy companion](simple-zero-prime-energy-criterion.md);
[classical von Mangoldt coefficients](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/05.0_pp_1_34_Dirichlet_series_I.pdf).
