# One torsion point for many integral polynomials

26 November 2026. **Status: the specialization theorems below are proved
here in ordinary mathematics.** They reconstruct the degree-independent
roots-of-unity ingredient of
[`lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207`][source],
and strengthen its error bookkeeping. The finite arithmetic presentations
and auxiliary-prime constructions to which the ingredient is applied
remain separate obligations.

The source attributes the underlying proof to Levent Alpöge with Claude
and the shorter rewriting to Sernau, Anthropic colleagues and Claude.
The source antecedents are `RootsOfUnity.lean` and
`GeneralTheorem.lean`, cited precisely below. No Lean code is copied and
no kernel replay is claimed.

## 1. The statement needed by the twist construction

Fix a prime $p$ and an algebraic closure $\overline{\mathbf Q}_p$ with
valuation $v(p)=1$, $v(0)=+\infty$, and valuation ring $\mathcal O$.
All lengths and valuations in the intended application use this
normalization, including after ramified coefficient extension.

**Theorem 1: simultaneous specialization with one total error.**
Fix a positive integer $s_0$, real numbers $\rho>0$, $B\ge0$ and
$\epsilon>0$. There is an integer $H$, depending only on these parameters
and $p$, with the following property.

Let $P_i\in\mathcal O[X_1,\ldots,X_s]$ be any finite family, where
$s\le s_0$, of arbitrary degrees. For each $i$ suppose there is a
possibly different point $x_i\in\mathcal O^s$ such that

```math
v(x_{ij})\ge\rho,\qquad
\sum_i v(P_i(x_i))\le B.                              \tag{1.1}
```

Then there are $p$-power roots of unity $\zeta_1,\ldots,\zeta_s$ with
$\zeta_j^{p^H}=1$, $0<v(\zeta_j-1)\le\rho$, and

```math
\sum_i\bigl(v(P_i(\zeta_1-1,\ldots,\zeta_s-1))
                     -v(P_i(x_i))\bigr)_+\le\epsilon. \tag{1.2}
```

Here $(t)_+=\max(t,0)$. In particular every selected value is nonzero
and every individual valuation increases by at most $\epsilon$.
The same $H$ works before the coefficients, degrees, number of
polynomials or witness points are supplied. The bound $B$ on their
**total** witness valuation is essential.

The source records the individual $\epsilon$ bounds. Keeping the sum of
the positive increases gives the stronger conclusion (1.2), which is
useful when several determinant or L-value factors share one budget.
The proof below also removes the artificial restriction that each
coordinate's error be less than one.

## 2. Two elementary valuation facts

For a nonzero polynomial $f(X)=\sum_k a_kX^k$ and $t\ge0$, write

```math
w_t(f)=\min_k\{v(a_k)+kt\}.
```

The minimum is over nonzero coefficients. The following facts hold for
real $t$, not merely rational $t$:

1. $w_t(fg)=w_t(f)+w_t(g)$.
2. If $v(y)\ge t$, then $v(f(y))\ge w_t(f)$.
3. If $f\in\mathcal O[X]$, then

   ```math
   w_t(f)=w_0(f)+\sum_{\alpha:\,f(\alpha)=0,\ v(\alpha)>0}
                            \min\{v(\alpha),t\},       \tag{2.1}
   ```

   with roots counted with multiplicity; a zero root contributes $t$.

**Proof.** The second assertion is the ultrametric inequality. For the
first, select the smallest index achieving the minimum in each factor.
In the product coefficient at the sum of these indices, there is exactly
one term achieving the sum of the minima; the other terms have larger
valuation. Hence there is no cancellation of that least term. For (2.1),
factor $f$ over $\overline{\mathbf Q}_p$ and use the first assertion and
$w_t(X-\alpha)=\min\{t,v(\alpha)\}$. The roots of nonpositive valuation
are absorbed into $w_0(f)\ge0$. These arguments also cover nonmonic
polynomials and roots outside $\mathcal O$. QED.

Put

```math
r_h=\frac1{\varphi(p^h)}
    =\frac1{p^{h-1}(p-1)},\qquad h\ge1.
```

Every primitive $p^h$-th root $\zeta$ satisfies $v(\zeta-1)=r_h$.
For completeness, the shifted cyclotomic polynomial
$\Phi_{p^h}(1+X)$ is Eisenstein at $p$: modulo $p$ it is
$X^{\varphi(p^h)}$, its constant coefficient is $p$, and its leading
coefficient is one. Its Newton polygon is the single segment from
$(0,1)$ to $(\varphi(p^h),0)$, so all roots have valuation $r_h$.
Equivalently, the Eisenstein valuation argument gives that value directly.
The radii $r_h$ are distinct and decrease to zero.

## 3. One coefficient controls the average distance to torsion

**Lemma 2: truncated distance bound.** If $a\in\mathcal O^\times$,
$h\ge1$ and $L>0$, then

```math
\sum_{\zeta\ {\rm primitive}\ p^h}
               \min\{v(\zeta-a),L\}\le h+L.           \tag{3.1}
```

**Proof.** The roots of
$F(Y)=(Y+a)^{p^h}-1$ are all the differences $\xi-a$ with
$\xi^{p^h}=1$, and all are integral. By (2.1), the sum of their
truncated valuations is $w_L(F)$. The coefficient of $Y$ is
$p^h a^{p^h-1}$, of valuation $h$, so $w_L(F)\le h+L$.
Restricting the nonnegative sum to primitive roots gives (3.1). QED.

This is the entire torsion-averaging estimate. Taking $L$ adjustable,
instead of fixing $L=1$, will allow any prescribed error.

## 4. One variable, without a degree bound

**Lemma 3: selection of a torsion shell.** Let $f\in\mathcal O[X]$
be nonzero, $\rho>0$, $B\ge w_\rho(f)$, and $\delta>0$.
Choose $h_*\ge1$ with $r_{h_*}\le\rho$, and choose $H\ge h_*$
so that

```math
B<\delta\sum_{h=h_*}^{H}\frac1{h+2\delta}.            \tag{4.1}
```

Then some primitive $p^h$-th root $\zeta$, with $h_*\le h\le H$,
satisfies

```math
v(f(\zeta-1))\le w_{r_h}(f)+\delta.                  \tag{4.2}
```

**Proof.** Let $R_h$ be the multiset of roots of $f$ whose valuation
is exactly $r_h$, and let $N_h$ be its cardinality. Each root belongs
to at most one such multiset. Equation (2.1) therefore gives

```math
\sum_{h=h_*}^{H}N_hr_h\le w_\rho(f)\le B.
```

By (4.1), for some $h$,
$N_hr_h(h+2\delta)\le\delta$. Apply Lemma 2 with
$a=1+\alpha$, for each $\alpha\in R_h$, and $L=2\delta$.
This $a$ is a unit since $v(\alpha)=r_h>0$.
There are $1/r_h$ primitive roots of order $p^h$.
Averaging the resulting inequalities supplies one such $\zeta$ with

```math
\sum_{\alpha\in R_h}
       \min\{v(\zeta-1-\alpha),2\delta\}\le\delta.
```

No summand can reach the truncation level $2\delta$, so the
truncations can all be removed. For roots whose valuation differs
from $r_h$, the ultrametric inequality is an equality:
$v(\zeta-1-\alpha)=\min\{r_h,v(\alpha)\}$.
Factoring $f$ now gives the exact identity

```math
v(f(\zeta-1))-w_{r_h}(f)
 =\sum_{\alpha\in R_h}
              \bigl(v(\zeta-1-\alpha)-r_h\bigr)
 \le\delta.
```

In particular the selected value cannot be zero. QED.

The harmonic sum diverges, so $H$ exists independently of the
degree. An explicit sufficient choice satisfies

```math
H+1+2\delta>
     (h_*+2\delta)\exp(B/\delta),                   \tag{4.3}
```

because the sum in (4.1) is at least the integral of
$1/(t+2\delta)$ from $h_*$ to $H+1$. This is an effective
existence bound, not a practical claim about the size of the resulting
torsion orders.

## 5. Moving all witness points to one point

We prove Theorem 1 with the stronger total positive-part conclusion.
Take

```math
\delta=\epsilon/s_0,
\qquad
B+\epsilon<\delta\sum_{h=h_*}^{H}\frac1{h+2\delta},
\qquad r_{h_*}\le\rho.                             \tag{5.1}
```

Process the coordinates in order. At an intermediate stage all
processed coordinates have already been replaced by common numbers
$\zeta_j-1$; the unprocessed coordinates of each point retain their
original values. Write $b_i$ for the current valuation of $P_i$.
Their sum is at most $B+k\delta$ after $k$ stages.

For the next coordinate, replace it by a variable $Y$ to obtain
univariate integral polynomials $g_i(Y)$. Their current, possibly
different coordinate values have valuation at least $\rho$. Thus

```math
w_\rho(g_i)\le b_i,\qquad
w_\rho\!\left(\prod_i g_i\right)
              \le\sum_i b_i\le B+\epsilon.
```

Apply Lemma 3 to the product. For the selected root, put
$b'_i=v(g_i(\zeta-1))$ and $\mu_i=w_{r_h}(g_i)$.
Then

```math
b'_i\ge\mu_i,\qquad b_i\ge\mu_i,\qquad
\sum_i(b'_i-\mu_i)\le\delta.
```

Consequently

```math
\sum_i(b'_i-b_i)_+\le\delta.                         \tag{5.2}
```

This both preserves the total budget and bounds its positive increase.
After at most $s_0$ stages, the inequality
$(a-c)_+\le(a-b)_++(b-c)_+$ gives (1.2).
All chosen orders divide $p^H$, and all chosen radii are at most
$\rho$. This proves Theorem 1. QED.

The empty family causes no problem: the product is one. With no
variables there is nothing to change. Thus the only excluded case
$s_0=0$ has the evident trivial formulation.

## 6. All required powers, including negative ones

The source needs the first $m$ powers of a twist simultaneously.
A slightly more general and sharper formulation costs no extra
argument.

**Lemma 4: witnesses for a power substitution.** Let $j\ne0$ be an
integer and $v(x)>0$. Put $L_j=p^{v_p(|j|)}$. There is $y$ with

```math
(1+y)^j=1+x,\qquad v(y)\ge v(x)/L_j.                \tag{6.1}
```

**Proof.** If $x=0$, take $y=0$. Otherwise first assume $j>0$ and write $j=L_ju$, with $p\nmid u$.
The monic polynomial $(1+Z)^{L_j}-(1+x)$ has integral roots, and
the valuation of their product is $v(x)$; hence one root $z$
has valuation at least $v(x)/L_j$. The map $1+y\mapsto(1+y)^u$
is invertible on $1+\mathfrak m$ by the elementary simple-root
Hensel lemma, and its inverse preserves $v(y)=v(z)$.
Choose this $y$ with $(1+y)^u=1+z$.
For $j<0$, replace $1+x$ by its inverse; the new parameter
$-x/(1+x)$ has the same valuation. QED.

**Theorem 5: one tuple for a finite set of powers.** Fix a nonempty
finite set $J\subset\mathbf Z\setminus\{0\}$, put

```math
L=\max_{j\in J}p^{v_p(|j|)},
```

and assume (1.1) with radius $r>0$. There is an $H$ fixed before
the polynomials, depending only on
$p,s_0,r,B,\epsilon,J$, and a tuple of $p^H$-torsion roots such that
every $\zeta_k^j$ is nontrivial and

```math
0<v(\zeta_k^j-1)\le r\quad(j\in J),
\qquad
\sum_{i,j\in J}
\bigl(v(P_i((\zeta_k^j-1)_k))-v(P_i(x_i))\bigr)_+
       \le\epsilon.                               \tag{6.2}
```

**Proof.** For each $(i,j)$, Lemma 4 gives a witness $y_{ij}$ for
the substituted function

```math
Q_{ij}(X)=P_i(((1+X_k)^j-1)_k)
```

whose coordinates have valuation at least $\rho=r/L$ and whose
value equals $P_i(x_i)$. For $j>0$ this is an integral polynomial.
For $j<0$, multiply by a sufficiently large product of powers of
$1+X_k$ to clear the denominators. The resulting polynomial is
integral and this multiplication changes neither valuation at the
witnesses nor valuation at torsion points, since all these factors
are units there. Its degree may depend on the original polynomial;
Theorem 1 places no restriction on that degree.

Apply Theorem 1 to this family, with witness budget $|J|B$.
In its proof choose

```math
h_*>\max_{j\in J}v_p(|j|),\qquad r_{h_*}\le r/L.
```

Every chosen $\zeta_k$ has order $p^{h_k}$ with $h_k\ge h_*$.
For $j\in J$ its power has order $p^{h_k-v_p(|j|)}$, hence is
nontrivial, and

```math
v(\zeta_k^j-1)
 =p^{v_p(|j|)}r_{h_k}\le L\rho=r.
```

The positive-part bound is exactly Theorem 1 for the transformed
family. QED.

For $J=\{1,\ldots,m\}$, one may use
$L=p^{\lfloor\log_p m\rfloor}\le m$. Thus $r/L$ replaces the
source's more restrictive witness radius $r/m$. The finite signed
set $J$ also treats both twisting signs directly.

## 7. Why the order of choices is now correct

The source's `Line.exists_twistPolynomials` supplies, for every
sufficiently large integer $N$, a family $P_{i,N}$ with a bounded
number of variables but potentially increasing degree. It also
supplies witnesses satisfying

```math
v(x_{i,N,k})\ge r,\qquad
v(P_{i,N}(x_{i,N}))\le\beta_i+s_0r.                 \tag{7.1}
```

The constants $s_0,r,\beta_i$ are fixed before $N$.
Theorem 5 therefore gives an $H$ **before choosing $N$**.
Choose $N\ge H$ within the cofinal range in which the polynomials
exist. Every selected root then has order dividing $p^N$, so it
can evaluate the source's characters with values in
$\mathbf Z/p^N\mathbf Z$. There is no circular request to enlarge
$N$ after seeing the degree of $P_{i,N}$.

Choose $r$ and the specialization tolerance $\epsilon'$ so that
$s_0r+\epsilon'<1$. Equations (7.1) and (6.2) then give

```math
v(P_{i,N}((\zeta_k^j-1)_k))
        \le\beta_i+s_0r+\epsilon'<\beta_i+1.        \tag{7.2}
```

This is the strict threshold required by the source's conversion
from a presentation minor to the length of a divisible Selmer
module. If the auxiliary inertia character at coordinate $k$ is
surjective onto $\mathbf Z/p^N\mathbf Z$, its $j$-th twisted
character is nontrivial there by Theorem 5. The ramification
valuation sum over the primes and their conjugates is at most
$2sr$, where $s$ is the actual number of auxiliary primes.
With the source's $2s\le s_0$, it is at most $s_0r$.

The new total error bound lets all presentation minors and
Stickelberger evaluations share one specialization allowance.
Whether this improves the final arithmetic exponent requires
tracking their structural defects and their occurrences in the
actual determinant identity.

What is still missing from an ordinary proof of the general twist
theorem is the arithmetic supplier of (7.1): the auxiliary-prime
construction, finite Selmer presentations, sharp minors and their
witnesses, descent and the exact evaluation-to-length implication.
This note completes the roots-of-unity specialization ingredient
conditional on those precise interfaces; it does not prove their
arithmetic hypotheses.

## 8. Necessary hypotheses and verification

**Positive witness radius is indispensable.** If $\rho=0$, take
$f_H(X)=(1+X)^{p^H}-1$ and any unit $x\in\mathcal O$.
Its reduction at $x$ is $\bar x^{p^H}\ne0$, so $v(f_H(x))=0$.
Yet it vanishes at every $\zeta-1$ with $\zeta^{p^H}=1$.
Thus there is no order bound chosen from a zero witness budget
without the strictly positive radius.

**A finite witness budget is indispensable.** The same polynomial
vanishes on all bounded-order torsion points; allowing its witness
valuation to grow with $H$ defeats any proposed uniform bound.
Likewise nonintegral coefficients allow one to divide by powers
of $p$ and artificially lower that witness valuation without
changing the zeros. Integrality, the radius and the budget play
different roles and are all retained above.

The proofs are exact valuation arguments. They use no numerical
sampling, conjectural zero-free assertion or bound on the moving
polynomial degrees.

Pinned source ranges checked:

| Source | Lines | Role |
| --- | --- | --- |
| [`RootsOfUnity.lean`][roots] | 46--116, 119--334, 352--510 | Radii, shell selection, coefficient estimate, coordinate replacement and uniform quantifiers. |
| [`GeneralTheorem.lean`][general] | 318--365, 392--456 | Simultaneous powers and order of choices in the twisting theorem. |
| [`Line.lean`][line] | 629--686 | Cofinal presentation polynomials, fixed witness budget and strict length threshold. |
| [`GaussValuation.lean`][gauss] | 167--195, 361--411 | Gauss valuations and power-substitution witnesses. |

SHA-256 of the complete source files, in table order:

```text
b4ba540cd44c45dfed412fb85918ed07e3e79034f2ca5bebebcc89296113c73b
6da04d47b2f1c4231fa7721328a255c28e605a2697adfe2b6bfcfb60e125ddbe
5f21e8bb68bd160c4070adeafbf0e44c132596ce53385b05dacfba4885a9b4e4
b015922360e7dff15d343cd561caa58f6af11ded2a36027e550631199ac3f2fb
```

[source]: https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207
[roots]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/RootsOfUnity.lean
[general]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/GeneralTheorem.lean
[line]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/Line.lean
[gauss]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/GaussValuation.lean
