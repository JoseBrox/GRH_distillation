# A compact dyadic prime-window filter: audit and RH alternative

**Status:** Analytical alternative; the required arithmetic estimate is **not proved**. This examines [Crossley's PR #1](https://github.com/JoseBrox/GRH_distillation/pull/1), his [pinned Lean proof](https://github.com/leecrossley/dirichlet-window-transfer/blob/fa94718cf9d65ee5b143ded4c91dc3873222cfdf/DelayedPole.lean), and his [prime-window RH formalization](https://github.com/leecrossley/prime-window-rh-criterion/blob/main/PrimeWindow.lean). The identities and conditional equivalence below are independently justified in ordinary mathematics; no external kernel build or large finite certificate has been rerun here.

## 1. An exact finite-prime-window identity

Fix $b>1$. For $1<t\le b$, put $W_b(t)=b(1-t^{-1})$; for $b<t<b^2$, put $W_b(t)=b^2/t-1$; otherwise set $W_b(t)=0$. This nonnegative tent has support $[1,b^2]$, height $b-1$, and main-term integral

```math
M_b:=\int_1^{b^2}W_b(t)\,dt=b(b-1)\log b.
```

For $R_\chi(x)=\sum_n\Lambda(n)\chi(n)(x/n-1)_+$, a termwise calculation proves

```math
R_\chi(b^2y)-(b+1)R_\chi(by)+bR_\chi(y)
=\sum_{y<n<b^2y}\Lambda(n)\chi(n)W_b(n/y).
\tag{1}
```

Indeed contributions below $y$ cancel both in their constant and $y/n$ terms, while contributions above $b^2y$ vanish. The two intermediate ranges give the two branches of the tent. Endpoint values are zero.

For $G(x)=R_1(x)-x\log x+(1+\gamma)x$, (1) becomes

```math
-G(b^2y)+(b+1)G(by)-bG(y)
=M_by-\sum_{y<n<b^2y}\Lambda(n)W_b(n/y).
\tag{2}
```

The same transformation of a nonprincipal corrected character sum cancels its entire linear term $xL'(1,\chi)/L(1,\chi)$. In particular no infinite Euler tail or derivative at one occurs in the *transformed* arithmetic expression.

A three-point combination of ramps at $y,by,b^2y$ supported only on $(y,b^2y)$ must satisfy two linear equations (zero total coefficient and zero coefficient weighted by $1,b,b^2$). Up to a scalar its coefficients are therefore $b,-(b+1),1$. The mixed signs are *forced*, not a stylistic choice.

## 2. Pole preservation, but not monotone smoothing

Write $g(u)=G(e^u)$, $c=\log b$, and $D_c g(u)=g(u-c)$ for $u>c$, zero otherwise. Set

```math
T_bg=-g+(b+1)D_cg-bD_{2c}g .
```

For the unilateral Laplace transform in its initial region of convergence,

```math
\mathcal L(T_bg)(s)=m_b(s)\mathcal Lg(s),\qquad
m_b(s)=(1-b^{-s})(b^{1-s}-1).
\tag{3}
```

The factors vanish only on the boundary lines $\mathrm{Re}\,s=0,1$. Thus any zero-detecting pole in $0<\mathrm{Re}\,s<1$ survives. For real $0<\beta<1$, $m_b(\beta)>0$, preserving the positive residue requirement of the original one-sided Landau criterion. The submitted Lean source proves this for $b=2$ and admissible Dirichlet families, *conditioned on* a window bound for the transformed function.

This is not interchangeable with the positive forward logarithmic average in [our existing criterion](scale-averaged-criterion.md). In particular $g\le B$ does not imply $T_bg\le T_bB$: a narrow negative bump at the largest sampled argument can make $T_bg$ arbitrarily positive while $g\le0$. Our existing one-sided arithmetic estimates therefore cannot simply be filtered. They require new two-sided control or an independent estimate for the finite prime window.

There is also a general order-theoretic obstruction: the convolution kernel of $T_b$ is the signed measure $-\delta_0+(b+1)\delta_c-b\delta_{2c}$, with total mass zero. Convolving it with any nonzero positive finite averaging measure still has total mass zero but has a nonzero Laplace multiplier. It therefore cannot be a nonnegative measure. Thus post-averaging with a positive kernel cannot turn this filter into an order-preserving operator. This explains why compactifying the prime sum and preserving our original one-sided majorant are intrinsically different operations.

## 3. An independent, concise eventual-sign equivalence for ordinary RH

Let $P_b(y)=\sum_p(\log p)W_b(p/y)$, and define the **ordinary-prime deficit**

```math
D_b(y)=M_by-P_b(y).
\tag{4}
```

This is not the prime-power deficit (2). The difference is a nonnegative sum of terms contributed by $p^k$, $k\ge2$.

**Theorem.** For every fixed $b>1$, if $D_b(y)\ge0$ for all sufficiently large $y$, then RH holds. Conversely, set

```math
C_0=2+\gamma-\log(4\pi)
=\sum_{\rho}\frac1{\rho(1-\rho)}
=0.0461914179\ldots,
```

where nontrivial zeros are counted with multiplicity. Assuming RH, eventual strict positivity $D_b(y)>0$ holds for every fixed

```math
b>b_0=\left(\frac{1+\sqrt{C_0/2}}{1-\sqrt{C_0/2}}\right)^2
=1.8452905\ldots.
```

In particular

```math
\boxed{\mathrm{RH}\quad\Longleftrightarrow\quad
2y\log2-\sum_{y<p<4y}(\log p)W_2(p/y)\ge0
\ \text{for all sufficiently large }y.}
\tag{5}
```

**Proof, eventual nonnegativity implies RH.** The entire Mellin transform of $W_b$ is

```math
H_b(s)=\int_1^{b^2}W_b(t)t^{s-1}\,dt
=\frac{(b^s-1)(b^s-b)}{s(s-1)},\qquad H_b(1)=M_b.
\tag{6}
```

Let $U(s)=\sum_p\sum_{k\ge2}(\log p)p^{-ks}$; it converges holomorphically for $\mathrm{Re}\,s>1/2$. Termwise Mellin integration in $\mathrm{Re}\,s>1$ yields

```math
\int_1^\infty D_b(y)y^{-s-1}\,dy=
\frac{M_b}{s-1}
+H_b(s)\frac{\zeta'(s)}{\zeta(s)}
+H_b(s)U(s)+E_b(s).
\tag{7}
```

Here $E_b$ is entire: only finitely many prime-window terms occur for $y<1$, with support away from zero. The pole at $s=1$ cancels because $H_b(1)=M_b$. The right side has no real singularity for $s>1/2$, since zeta has no real zero in $(0,1)$. If $D_b$ is eventually nonnegative, the classical Landau theorem for Mellin transforms of nonnegative functions excludes an abscissa of convergence $\sigma_c>1/2$, as that abscissa would be a real singularity. Thus the transform is holomorphic on $\mathrm{Re}\,s>1/2$. But a hypothetical zeta zero $\rho$ with $1/2<\mathrm{Re}\,\rho<1$ would be a genuine pole of (7): $H_b(\rho)\ne0$ by its two factors. The functional equation then gives RH.

**Proof, RH implies eventual strict positivity when $b>b_0$.** For $y>1$, the classical explicit formula for the compactly supported weight gives

```math
D_b(y)=\sum_\rho y^\rho H_b(\rho)
+\sum_{k\ge1}y^{-2k}H_b(-2k)
+\sum_{p,\,k\ge2}(\log p)W_b(p^k/y).
\tag{8}
```

The trivial-zero terms $H_b(-2k)$ are positive. On RH, $\rho=\tfrac12+i\tau$, and

```math
|H_b(\rho)|\le
\frac{\sqrt b(1+\sqrt b)^2}{|\rho|^2}.
```

The classical identity $\sum_\rho|\rho|^{-2}=C_0$, valid under RH, therefore bounds the zero contribution by $\sqrt y\,\sqrt b(1+\sqrt b)^2C_0$. By the ordinary PNT and partial summation, the prime-square terms alone satisfy

```math
\sum_p(\log p)W_b(p^2/y)
= B_b\sqrt y+o_b(\sqrt y),\qquad
B_b=\int_1^bW_b(t^2)\,dt
=2\sqrt b(\sqrt b-1)^2 .
```

Other prime powers are nonnegative. Hence

```math
\liminf_{y\to\infty}\frac{D_b(y)}{\sqrt y}
\ge\sqrt b\,[2(\sqrt b-1)^2-C_0(1+\sqrt b)^2].
\tag{9}
```

The bracket is strictly positive for $b>b_0$. For $b=2$ the easy bound $C_0<1/20$ already suffices, since

```math
2(\sqrt2-1)^2-\frac{(\sqrt2+1)^2}{20}
=\frac{117-82\sqrt2}{20}>0
```

($C_0<1/20$ follows from the standard elementary inequalities $\gamma<0.58$, $\log(4\pi)>2.53$; the final inequality follows by squaring positive quantities). This proves the theorem. $\square$

This proof uses classical Mellin theory, the zeta explicit formula, the PNT and Landau's positivity theorem. It is **not** an unconditional verification of inequality (5). Its RH-implies-positivity direction concerns sufficiently large $y$, not all scales.

Crossley's [separate all-width manuscript](https://github.com/leecrossley/prime-window-all-widths/blob/f12e654b888be6d87780be8f81c065cf73f844db/PROOF.md) claims sharper width thresholds and conditional positivity for **all** scales, with large finite certificates. Its proof outline has been inspected, but those finite checks have not been independently reproduced here.

## 4. Consequences for the RH and Dirichlet GRH programs

**RH-only:** The local deficit (5) is an appealing alternative target. A sufficiently strong one-sided bound on the *negative* prime-power deficit is allowed because the Riemann zeta function has no real zeros in the open critical strip. The prime-only nonnegative sign gives such a bound with the elementary $O(\sqrt y)$ cost of the higher prime powers. The stronger sparsely spaced full-power-window implication uses the original Landau window lemma, rather than the eventual-sign proof above.

**Dirichlet GRH:** For a positive real-weight character family whose principal character has coefficient $a_0$, (2) becomes a finite prime-power sum with coefficient $a_0+\sum_{\chi\ne1}a_\chi\mathrm{Re}\,\chi(n)$ and principal main term $a_0M_by$. A direct analytic supplier would need a **lower bound** on that weighted sum, on the correct cofinal windows and for the *same* auxiliary integral maps as the geometry. The sign cannot be reversed freely when real Dirichlet zeros have not all been excluded. Excluding only exceptional zeros close to one is not equivalent to eliminating every real zero in the critical strip.

**Research decision:** Retain this as an optional analytic branch. Test whether the preferred RH arithmetic construction can supply the finite-window lower estimate directly, respecting ramified primes, auxiliary characters, same-map normalizations and its growing parameters. Do not infer that the signed filter improves the currently available one-sided bounds. No arithmetic or geometric obligation has been discharged by the PR.

## 5. A discrete square-sampling criterion

The same classical argument shows something stronger about sampling, without invoking the large formal source. For each fixed $b>1$, the prime-only deficit $D_b(y)$ is Lipschitz at large scales. Indeed, on its support each summand $W_b(p/y)$, viewed as a function of $y$, is piecewise linear with slope of absolute value at most $b^2/p$. At points of differentiability,

```math
|D_b'(y)|\le M_b+b^2\!\sum_{y\le p\le b^2y}\frac{\log p}{p}
\le M_b+\frac{b^2}{y}\,\vartheta(b^2y)\ll_b1,
```

where $\vartheta(x)=\sum_{p\le x}\log p\ll x$ is Chebyshev's elementary bound. Continuity at breakpoints makes this a global Lipschitz bound for all sufficiently large $y$.

**Corollary (RH from tests at squares).** Let $b>b_0$, where $b_0$ is the explicit threshold in Section 3. Then

```math
\mathrm{RH}\quad\Longleftrightarrow\quad
D_b(n^2)\ge0\quad\text{for every sufficiently large integer }n.
\tag{10}
```

In particular $b=2$ works. To prove the nontrivial direction, interpolate from $n^2\le y<(n+1)^2$. The Lipschitz bound gives $D_b(y)\ge-C_b\sqrt y$. Hence $F(y)=D_b(y)+C_b\sqrt y\ge0$ eventually. Its Mellin transform is (7) plus $C_b/(s-1/2)$, holomorphic at every real $s>1/2$. Landau's positivity theorem again rules out any nonreal zero pole with $\mathrm{Re}\,s>1/2$. Conversely, RH gives eventual positivity *at every real scale* by (9), hence also at squares.

More generally, a grid $y_n\to\infty$ with gaps $y_{n+1}-y_n\ll\sqrt{y_n}$ suffices for this implication. If gaps are $O_\varepsilon(y_n^{1/2+\varepsilon})$ for every fixed $\varepsilon>0$, the same proof gives zero-freeness in each $\mathrm{Re}\,s>1/2+\varepsilon$, hence RH. Testing finitely many squares is, of course, not enough.

A square-sampling formulation is also credited to earlier work in [Crossley's README](https://github.com/leecrossley/prime-window-rh-criterion/blob/main/README.md). The significance here is its elementary compatibility with the [finite-table RH acceptance conditions](finite-window-sampling.md): it can reduce a continuous statement to a discrete family, *if* an arithmetic argument supplies the sign. The sign remains unproved.

## 6. An exact match with the preferred quadratic projector

The current [RH direct transfer](rh-direct-transfer.md) uses the *positive arithmetic projector*

```math
D_+(x)=G_1(x)+G_{\chi_q}(x)-G_{\chi_d}(x)-G_{\chi_q\chi_d}(x),
\qquad
K_{q,d}(n)=(1+\chi_q(n))(1-\chi_d(n)).
```

Here $\chi_q,\chi_d$ are the quadratic characters of two distinct odd auxiliary primes. Applying (1) and (2) gives the **exact local identity**

```math
-D_+(4y)+3D_+(2y)-2D_+(y)
=2y\log 2-\sum_{y<n<4y}\Lambda(n)K_{q,d}(n)W_2(n/y).
\tag{11}
```

All linear corrections of the three nonprincipal terms disappear. The kernel $K_{q,d}(n)$ is real and nonnegative even at primes dividing the auxiliary conductors. At an unramified prime $p$, it equals $4$ if $\chi_q(p)=1$, $\chi_d(p)=-1$, and $0$ otherwise.

**Prime-power advantage.** For even $k\ge2$, $K_{q,d}(p^k)=0$ except possibly at $p=d$. Indeed at primes outside $qd$ both quadratic characters square to $1$; at $p=q$, $\chi_d(q)^{2k}=1$; at $p=d$, $K_{q,d}(d^{2k})=2$. Consecutive even powers of an odd $d$ have ratio $d^2\ge9>4$, so at most one can lie in $(y,4y)$, contributing $O(\log(2y))$. All remaining higher powers are odd powers $k\ge3$, and Chebyshev's bound gives

```math
\sum_{\substack{p^k\le4y\\ k\ge3}} \log p
\ll\sum_{k=3}^{\lfloor\log_2(4y)\rfloor}(4y)^{1/k}
\ll (4y)^{1/3}+(4y)^{1/4}\log(4y)\ll y^{1/3}.
```

Since $0\le K_{q,d}\le4$ and $0\le W_2\le1$, the difference between the prime-power sum in (11) and its prime-only version is $O(y^{1/3})$, **uniformly in the distinct odd primes $q,d$**. At most two ramified-prime terms distinguish the prime-only kernel from four times the selected split/inert prime count; these are $O(\log(2y))$, and vanish under the relevant local sign conditions.

This is a useful feature of the actual RH construction, not merely of the abstract Dirichlet-family transfer. The improved $O(y^{1/3})$ deletion bound is nevertheless **not** the unresolved geometric estimate: we still need a lower bound for this local selected-prime sum to force the required upper bound for (11). The preferred RH comparison gives a one-sided *upper* bound for a cumulative $D_+$ observable, and (11) has mixed signs. Furthermore, $D_+$ is a *signed* combination of characters even though $K_{q,d}\ge0$; it cannot be treated as an admissible positive-residue character family without separate justification. The original quadratic-twist selection and common-map arithmetic hypotheses remain necessary to transfer any local estimate to the zeta target.

**Verification scope:** Formulae (1)–(9) and the bound $C_0<1/20$ were checked algebraically. The pinned external Lean source and its recorded kernel/axiom output were inspected, not rebuilt. No new finite certificate and no independent full Lean verification is claimed.
