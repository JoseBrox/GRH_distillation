# A sufficient estimate averaged over the scale

## Result and scope

The preferred analytic endpoint can be weakened further. A pointwise upper
bound at every scale in a long interval is unnecessary. It is enough to
control the weighted integral of the **positive part** of the final upper
budget over arbitrarily late multiplicative intervals. The arithmetic and
geometric losses may be combined with their signs, and averaged over a
fixed nearby range of scales, before taking that positive part. This local
logarithmic average preserves every zero-detecting pole.

This is a consequence of the already proved general one-sided Laplace
criterion, not a new estimate for the actual arithmetic construction.
Neither a signed integral nor a small unweighted proportion of exceptional
scales suffices. All character families remain fixed during the intervals
used for their own accuracy stage.

## 1. The analytic statement

For a primitive character, let $G_\chi$ be the corrected smoothed prime sum
defined in the manuscript; in conductor one this is

\[
G_1(x)=\sum_{n\le x}\Lambda(n)(x/n-1)-x\log x+(1+\gamma)x.
\]

Fix a primitive target character $\chi$. At accuracy stage $j$ let

\[
H_j(x)=\sum_{\nu\in\mathcal C_j}a_{j,\nu}\Re G_\nu(x),
\qquad a_{j,\nu}>0,
\]

where $\mathcal C_j$ is finite and contains $\chi$ or $\bar\chi$.
The corrected conductor-one character is allowed. Fix $b_j>1$ and
$1/2<\theta_j<1$, with $\theta_j\to1/2$. Define

\[
I_j(Y)=\int_Y^{Y^{b_j}}(H_j(x))_+x^{-\theta_j}\,\frac{dx}{x}.
\]

**Theorem.** If, for every $j$,

\[
\liminf_{Y\to\infty}
\frac{\log(1+I_j(Y))}{\log Y}=0,\tag{1}
\]

then $L(s,\chi)$ and $L(s,\bar\chi)$ have no zeros with real part
greater than $1/2$. Applying this to all primitive characters gives
Dirichlet GRH by the functional equations and the usual Euler-factor
comparison. For ordinary RH take $H_j=G_1$ for every $j$.

**Proof.** Put $U=\log Y$ and $g_j(u)=H_j(e^u)$. The manuscript's
positive-family lemma gives the exponential growth bound and meromorphic
Laplace transform, with isolated simple poles and positive residues at
real poles. Every zero of the target or its conjugate contributes a
nonzero positive multiplicity to the residue factor, so it cannot cancel.
For every $\eta>0$, (1) supplies arbitrarily large $U$ for which

\[
\int_U^{b_jU}(g_j(u))_+e^{-\theta_ju}\,du\le e^{\eta U}.
\]

The nonnegative function $(g_j)_+$ majorizes $g_j$. The general one-sided
Laplace criterion therefore excludes poles to the right of $\theta_j$.
Letting $j$ tend to infinity proves the assertion. All constants and the
family are fixed during each application. No lower bound for the target
coefficient uniform in $j$ is needed. ∎

The equivalent quantifier form of (1) is: for every $\eta>0$, arbitrarily
large $Y$ satisfy $I_j(Y)\le Y^\eta$. The harmless addition of $1$ permits
$I_j(Y)=0$ and makes the logarithm nonnegative. Exceptional null sets have
no effect; a majorant only almost everywhere is sufficient because the
Laplace argument uses integrals throughout.

A pointwise estimate $H_j(x)\le M_jx^{\theta_j}$ on a whole window gives
$I_j(Y)\le M_j(b_j-1)\log Y$. Thus the previous vanishing-loss theorem
and its varying-family version are immediate special cases.

## 2. Apply the criterion to the combined signed arithmetic budget

For each fixed stage choose an unbounded set $\mathcal Y_j$ of allowed
starting points. Suppose the actual compatible data give, almost
everywhere on every selected interval with $Y\in\mathcal Y_j$,

\[
H_j(x)\le B_j(x),\qquad
B_j(x)=D_j(x)+C_j(x)+R_j(x),\tag{2}
\]

where $D_j$ is the normalized arithmetic discrepancy, $C_j$ is the
signed companion contribution, and $R_j\ge0$ contains the transfer and
centering costs. The functions in (2) must be measurable. Every term must
come from the same data in the pointwise comparison; this condition is
not removed by integration.

It suffices to prove (1), restricting its lower limit to the **same**
allowed starting points $Y\in\mathcal Y_j$, with

\[
\int_Y^{Y^{b_j}}(B_j(x))_+x^{-\theta_j}\,\frac{dx}{x}
\tag{3}
\]

in place of $I_j(Y)$. This retains cancellation between arithmetic,
geometric and companion terms. The separately estimated expression

\[
\int_Y^{Y^{b_j}}\{(D_j(x)+C_j(x))_++R_j(x)\}
                         x^{-\theta_j}\,\frac{dx}{x}
\tag{4}
\]

is a sufficient upper bound for (3), but is not intrinsic to the theorem.
Indeed $H_+\le B_+\le(D+C)_++R$.

For the present RH comparison, one may take

\[
D(x)=\bar E(x)/k(x),\qquad
C(x)=\operatorname{avg}_{t\in T}
       \{G_{\chi_d}+G_{\chi_q\chi_d}-G_{\chi_q}\}(a_t/b).
\]

Under its actual source size conditions the nonnegative remainder is

\[
R(x)=\frac{2-d_0}{d_0x}+\frac{2C_\Psi}{3fx}
                           +(1+\log(x+1))^2.
\]

The existing hypotheses $d_0\ge x^{-\varepsilon}$, $f\ge1$ make the
first two terms at most $2x^{-1+\varepsilon}+2C_\Psi/(3x)$.
For fixed $\varepsilon<1$, their weighted integral and that of the
logarithmic centering cost are bounded on the whole tail for every
$\theta>0$. Thus they automatically satisfy (1). The unresolved target
can be the positive-part integral of $D+C$ itself. A supplied companion
bound $C\le Mx^\theta$ permits the still stronger target for $D_+$.

Auxiliary primes and fields in this RH formula may vary with $x$: the
analytic function on the left remains the same $G_1$. For general
Dirichlet targets, it is the positive analytic family $H_j$, not every
auxiliary construction parameter, that must remain fixed at stage $j$.

If a further construction index has probability weights $p_u(x)$ and
$H_j(x)\le\sum_up_u(x)B_{j,u}(x)$, convexity gives

\[
(H_j(x))_+\le\left(\sum_up_u(x)B_{j,u}(x)\right)_+
                 \le\sum_up_u(x)(B_{j,u}(x))_+.
\]

Consequently a joint bound averaged over construction indices and scale
is sufficient. The first expression preserves more cancellation than
the second. No separate worst-case bound for every pair $(x,u)$ is
required by this analytic endpoint. Nonnegative integrands permit
Tonelli's theorem; measurability and the actual comparison (2) remain
requirements on a proposed supplier.

## 3. Controlled exceptional scales

Suppose for a fixed stage that $C,M\ge0$, $|H(x)|\le Cx^\alpha$ eventually and
$H(x)\le Mx^\theta$ outside a measurable set
$E_Y\subset[Y,Y^b]$. Then

\[
\int_Y^{Y^b}H(x)_+x^{-\theta}\,\frac{dx}{x}
\le M(b-1)\log Y+C\int_{E_Y}x^{\alpha-\theta}\,\frac{dx}{x}.
\tag{5}
\]

Thus the exceptional set may be discarded only when its **weighted**
contribution is subpower along arbitrarily late intervals. If
$\alpha>\theta$, a simple sufficient condition is

\[
\int_{E_Y}\frac{dx}{x}\le
              Y^{-b(\alpha-\theta)+o(1)}.\tag{6}
\]

The $o(1)$ is along the same chosen window sequence. Formula (5), which
retains the locations of the exceptional scales, is preferable to the
coarser (6). If $\alpha\le\theta$, the baseline bound itself suffices.
Under the manuscript's stated uniform quasi-RH estimate, a fixed finite
family has $\alpha=23/24$; its conductor and weight constants are fixed
at this accuracy stage. This use of quasi-RH retains that input's exact
hypotheses and is not an independent verification of it.

With the probability measure $dx/((b-1)x\log Y)$ on the window, (1)
also follows from a subpower $L^p$ bound for $x^{-\theta}B(x)_+$ for
any fixed $p\ge1$. Hölder's inequality and the factor $(b-1)\log Y$
prove this directly. Such a moment estimate remains an obligation for
the arithmetic supplier.

## 4. Average nearby scales before taking the positive part

There is a further relaxation that permits signed cancellation between
nearby scales. Fix $h>0$ and put

\[
\mathcal A_hH(x)=\frac1h\int_0^h H(xe^v)\,dv
                 =\frac1h\int_x^{e^hx}H(t)\,\frac{dt}{t}.
\]

Set $\mathcal A_0H=H$. At each accuracy stage $h=h_j\ge0$ may be
chosen freely but remains fixed during its window sequence.

**Smoothing lemma.** In the theorem of Section 1, one may replace
$I_j(Y)$ by

\[
I_{j,h_j}(Y)=\int_Y^{Y^{b_j}}
       (\mathcal A_{h_j}H_j(x))_+x^{-\theta_j}\,\frac{dx}{x}.
\tag{8}
\]

**Proof.** For $g(u)=H(e^u)$ the averaged function is
$g_h(u)=h^{-1}\int_0^h g(u+v)\,dv$. If $\Phi$ is the Laplace
transform of $g$, its transform initially in $\Re s>2$ is

\[
\Phi_h(s)=M_h(s)\Phi(s)-E_h(s),\qquad
M_h(s)=\frac{e^{hs}-1}{hs},
\]
\[
E_h(s)=\frac1h\int_0^h e^{sv}
                    \int_0^v g(w)e^{-sw}\,dw\,dv.
\]

The function $E_h$ is entire, because both integrations are on bounded
intervals and $g$ is locally integrable. The multiplier $M_h$ is entire
with removable value $1$ at zero. It has no zero in $\Re s>0$, since
$|e^{hs}|>1$ there, and is positive for real $s>0$. Thus every detecting
pole remains simple with nonzero residue; a real pole still has positive
residue. The averaged function retains an $O(e^{2u})$ bound. Apply the
general Laplace criterion to $g_h$ and the majorant $(g_h)_+$. When
$h=0$, use $M_0=1$, $E_0=0$ and the original proof. ∎

Crossley gives a discrete counterpart for Dirichlet families. With $c=\log 2$, the difference $-g(u)+3g(u-c)-2g(u-2c)$ uses zero-extended delays. Its multiplier $(1-2^{-s})(2^{1-s}-1)$ has no zeros in $0<\Re s<1$ and is positive on the real interval $(0,1)$. A one-sided window bound of exponent $\theta$ on the difference, with $0<\theta<1$, then excludes zeros of the family in $\Re s>\theta$. [Lean theorem](https://github.com/leecrossley/dirichlet-window-transfer/blob/fa94718cf9d65ee5b143ded4c91dc3873222cfdf/DelayedPole.lean#L176) and [archived result](https://doi.org/10.5281/zenodo.24410863).

Consequently (2) may be averaged first. The sufficient final arithmetic
target is the subpower growth of

\[
\boxed{\int_Y^{Y^{b_j}}
 \bigl(\mathcal A_{h_j}(D_j+C_j+R_j)(x)\bigr)_+
                  x^{-\theta_j}\,\frac{dx}{x}.}\tag{9}
\]

The original comparison must hold almost everywhere on the **expanded**
interval $[Y,e^{h_j}Y^{b_j}]$ for the same cofinal starting points along
which (9) has subpower growth. No data are required at smaller scales by
this local averaging. It is enough that the combined upper budget be
locally integrable there; the positive averaged part must have the stated
finite weighted integral. Contributions retain their signs until after
the inner average. This can be weaker than controlling the positive part
of the budget separately at every scale.

For clarity, the old positive-part criterion always supplies this one,
with slightly shorter windows. If $1<b'<b$, then eventually
$e^hY^{b'}\le Y^b$. Jensen's inequality and Tonelli's theorem give

\[
\begin{aligned}
\int_Y^{Y^{b'}}(\mathcal A_h B(x))_+x^{-\theta}\,\frac{dx}{x}
&\le\frac1h\int_0^h e^{\theta v}
 \int_{e^vY}^{e^vY^{b'}}B(t)_+t^{-\theta}\,\frac{dt}{t}\,dv\\
&\le M_h(\theta)\int_Y^{Y^b}B(t)_+t^{-\theta}\,\frac{dt}{t}.
\end{aligned}
\]

The limit $h=0$ has the same interpretation. The fixed factor
$M_h(\theta)$ has no effect on the subpower condition. Repeated finite
logarithmic averaging is also permitted: its multiplier is the product
of the corresponding nonvanishing multipliers, and its expanded range
has the sum of their widths. No uniform number of repetitions across
accuracy stages is needed.

## 5. Why the positive part and the exceptional-set weight matter

### A signed integral can hide a pole

Take $g(u)=e^{\beta u}\cos u$ with $\theta<\beta<1$. Its Laplace
transform is $(s-\beta)/((s-\beta)^2+1)$ and has poles at
$\beta\pm i$. For any fixed $b>1$, writing $a=\beta-\theta>0$,

\[
\int_U^{bU}g(u)e^{-\theta u}\,du
=\left[\frac{e^{au}(a\cos u+\sin u)}{a^2+1}\right]_U^{bU}.
\]

Choose $bU=(2n+1)\pi$. The upper endpoint is
$-ae^{abU}/(a^2+1)$ and dominates the lower endpoint as $n\to\infty$.
The signed integrals are negative on arbitrarily late windows despite
the two poles to the right of $\theta$. There are no real poles, so the
real-residue condition is satisfied. Controlling only the signed mean
cannot replace (1).

### An exponentially small exceptional set can still carry a pole

On the logarithmic scale put

\[
g(u)=\sum_{n=1}^{\infty}e^{3n/2}
             \mathbf1_{[n,n+e^{-3n/4}]}(u).
\]

The intervals are disjoint and $0\le g(u)\le e^{3u/2}$.
On $[U,bU]$ its support has length $O(e^{-3U/4})$.
Nevertheless, for $\Re s>2$, termwise integration and the exponential
series give

\[
\Phi(s)=\sum_{m=1}^{\infty}
 \frac{(-1)^{m+1}s^{m-1}}{m!\{e^{s-3/2+3m/4}-1\}}.\tag{7}
\]

On every compact subset of $\Re s>0$, the tail of this series converges
normally: the denominator grows geometrically in $m$, and the factorial
controls the numerator. Only the term $m=1$ has poles in this half-plane.
They lie at $3/4+2\pi i k$, and the unique real pole has positive residue
$1$. Thus all structural hypotheses of the general Laplace criterion
hold, while its conclusion fails for $\theta<3/4$.

This is an abstract counterexample to an insufficient analytic interface,
not a claim about zeta. It shows that even exponentially small logarithmic
measure is not a substitute for the precise weighted mass in (5).

## 6. Effect on the proof program

The weakest new target is one positive-part integral of a fixed local
logarithmic average of the **combined signed** normalized budget.
Uniform pointwise geometric bounds, frame bounds and componentwise error
estimates remain possible suppliers. They are no longer required by the
final analytic criterion itself. Fixing the local averaging width keeps
every detecting pole; an uncontrolled signed mean on a cofinal long
window, as in the counterexample, does not.

The argument does not produce the missing integral maps, justify changing
metrics, prove a height estimate, or permit an unrelated arithmetic datum
in different terms of one comparison. It also does not permit the analytic
target family to change from window to window at one fixed accuracy.

The prerequisite is the manuscript's general one-sided Laplace criterion
(`prop:landau-independent`), together with its positive-family residue
formula (`lem:positive-family`). The full pole argument was reread in
bounded passages for this continuation. No large upstream source read,
formal build or kernel replay is involved in this ordinary analytic proof.
