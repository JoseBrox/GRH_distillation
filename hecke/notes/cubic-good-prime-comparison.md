# A simpler cubic arithmetic supplier: first powers and a biased top set

24 November 2026. This strengthens the
[relative arithmetic comparison](cubic-relative-comparison.md).
The entire arithmetic quantity to be bounded can be reduced to
unramified rational primes split in the fixed Eisenstein field,
without requiring a new ramified divisor construction or the
source's precise target-share distribution. The reduced supplier
is still an open quantitative estimate. Its exact local
Frobenius realization is treated in the
[cubic torsor note](cubic-torsor-realization.md).

Use the same finite relative group
$G=C_2^2\times C_3\times B$ with $B=C_{2^h}$,
over $F=\mathbb Q(\omega)$, and retain $\Phi$ (first sign zero),
$f=|\Phi|=|G|/2$, $c=((1,1),0)$ and the first-sign
character $\chi_c$. For every finite prime ideal $v$ of $F$
and $j\ge1$ the actual kernel is


```math
\kappa_g(v^j)=|G/I_v|\mathbf1_{jF_v-g\in I_v}.
```


Here the local value of a ramified character is zero.
At a top order $a>0$, top label $t$, and weight profile
$w(\rho)>0$ on $\Phi$, put $w_g=w(c+g+t_0)$ for $g\notin\Phi$.
Assume $w_g\le a$. The original exact arithmetic term is


```math
\mathcal A_F(a,t,w)=\frac1f
 \sum_{g\notin\Phi}\sum_{v,j}
 (\log Nv)\kappa_g(v^j)
       \left(\frac{a}{(Nv)^j}-w_g\right)_+ .
```


Its correcting main term $\mathcal M_F(a,w)$ is (4) of the
relative comparison; it contains only the principal Laurent
constant and the first-sign logarithmic derivative.
All sums over $v,j$ in the arithmetic term are finite.
The normalized averaged discrepancy $E/k$, with
$k=|T|mb d_0/2$, is the one in the relative comparison.

## 1. A nonnegative exact centering error

Call a pair $(v,j)$ good if $j=1$, $Nv=p$ is a rational
prime, and $p\notin\{2,3,q,d\}$. Then $p$ splits in $F$
and is unramified in the entire relative host. Let
$\mathcal A_{\rm good}$ be the restriction of
$\mathcal A_F$ to the good pairs. Put


```math
C_{\rm bad}=
 \frac1f\sum_{g\notin\Phi}
   \sum_{(v,j)\ {\rm not\ good}}
  \frac{\log Nv}{(Nv)^j}\kappa_g(v^j).
```


This is finite: higher rational prime powers are absolutely
summable after division by their norm, and the remaining
excluded first powers are finite. Its sign is nonnegative.

**Proposition.** With the corrected main term
$\mathcal M_{\rm good}=\mathcal M_F-a C_{\rm bad}$,


```math
\begin{aligned}
 \mathcal A_F-\Re\mathcal M_F
 &=\mathcal A_{\rm good}-\Re\mathcal M_{\rm good}
       -R_{\rm bad},\\
 R_{\rm bad}&=\frac1f\sum_{g\notin\Phi}
  \sum_{(v,j)\ {\rm not\ good}}
       (\log Nv)\kappa_g(v^j)
          \min\{a/(Nv)^j,w_g\}\ge0.
\end{aligned} \tag{1}
```


In particular an **upper** bound for the good discrepancy
supplies an upper bound for the full discrepancy with
no added error. The correction constant involves only
the two abelian terms:


```math
C_{\rm bad}=\sum_{(v,j)\ {\rm not\ good}}
 \frac{\log Nv}{(Nv)^j}(1-\chi_c(v)^j).
 \tag{2}
```


**Proof.** Use $(A-w)_+=A-\min(A,w)$ in every excluded
summand. The sign follows from the nonnegative local
kernel. For (2), average its character expansion on the
complementary coset $G\setminus\Phi$. Only the trivial
character (phase 1) and $\chi_c$ (phase -1) survive.
Inertia coefficients are already included. QED.

This is an exact formula, not an estimate at good
primes inferred by ignoring bad primes. In particular
it does not create a cubic logarithmic derivative
in the main term. By abelian factorization the two
terms in (2) come from rational Dirichlet factors.

## 2. The centering loss is within the square-root budget

Let $W=\max_g w_g\le a$ and $X=a/W\ge1$. The error
in (1) satisfies, with absolute constants,


```math
R_{\rm bad}\ll
 \sqrt{aW}+ W\bigl(1+\log(qd)\bigr).
 \tag{3}
```


Indeed $\sum_g\kappa_g(v^j)=|G|$ by character
orthogonality. Summing in $g$ first bounds the
contribution of all higher rational powers by


```math
2\sum_{\substack{v,j\\(Nv)^j=p^r,\ r\ge2}}
    (\log Nv)\min\{a/(Nv)^j,W\}.
```


The sum of the residue degrees over any rational
prime is at most $[F:\mathbb Q]=2$. Thus its cumulative
logarithmic mass up to $Z$ is $O(\sqrt Z)$, by the
elementary higher-power Chebyshev bound in the
[direct criterion](direct-prime-criterion.md).
Split at $X$: the initial contribution is
$O(W\sqrt X)$ and partial summation of the tail
gives $O(a/\sqrt X)$. These agree and prove the first
term of (3). The excluded first rational powers
are in $\{2,3,q,d\}$, and their total contribution
is at most $4W\sum_{p\in\{2,3,q,d\}}\log p$.
This proves (3) including all ramification.

In the proposed source regime $a_t/b=x+O(1)$,
$W\ll b$ and $d_0\ge x^{-\epsilon}$, the total of
(3) over all top labels and steps, after averaging
the translations and dividing by $k$, is


```math
O\left(x^{1/2+\epsilon}
          +x^\epsilon(1+\log(qd))\right).
```


The companion selection has $\log(qd)\le x^{\epsilon/4}$
at large $x$. Thus the good discrepancy and the
full discrepancy differ by at most
$O(x^{1/2+\epsilon})$ in that normalization.
The desired vanishing-loss window estimate for
either one is equivalent to the estimate for the
other after adjusting the error budget.
For the sufficient *upper* direction the exact
sign in (1) already avoids needing (3).

The constants have no dependence on the order of
the auxiliary group. In particular all local
residue-degree-two terms, all higher powers and
the finite ramification set can be removed from
the new geometric arithmetic supplier.

## 3. The good-prime labels need only two Frobenius cases

For $p\notin\{2,3,q,d\}$ with $p\equiv1\bmod3$,
there are two prime ideals $v,\bar v$ above $p$.
Their norm-pullback characters agree, while
$\lambda(\bar v)=\lambda(v)^{-1}$. Write
$G=C_3\times G_0$ with $G_0=C_2^2\times B$.
Their Frobenius labels are therefore $(r,b_0)$
and $(-r,b_0)$ for a common $b_0\in G_0$,
where $r=0$ exactly when
$2^{(p-1)/3}\equiv1\bmod p$. Otherwise
$r$ is either nonzero cubic label.

Since the good primes are unramified, their
combined kernel on the two ideals is


```math
\kappa_{(s,b)}(v)+\kappa_{(s,b)}(\bar v)
=|G|\mathbf1_{b=b_0}
      (\mathbf1_{s=r}+\mathbf1_{s=-r}).
\tag{4}
```


Thus if the first sign of $b_0$ is zero,
the pair contributes nothing to the complementary
coset sum. If that sign is one, the contribution
to $\mathcal A_{\rm good}$ is exactly


```math
2\log p\left[
  (a/p-w_{(r,b_0)})_+
 +(a/p-w_{(-r,b_0)})_+\right]. \tag{5}
```


For $r=0$ the same hinge occurs twice.
There is no ambiguity about the two nontrivial
cubic labels; the sum is invariant under their
interchange. The weights retain their actual
translation by $c+t_0$.

This makes the open arithmetic quantity a
rational-prime sum with a binary extra test
(the cubic residue test) in addition to the
existing abelian Frobenius data. It is not a
Dirichlet congruence test: the earlier
nonabelian coefficient obstruction still applies.
No new global map is obtained from the identity.

## 4. The target distribution can be much simpler

Let $T$ be the actual nonempty top set of the
relative comparison and put


```math
p_0(T)=\frac{|\{t\in T:\ t\bmod B=0\in C_3\}|}{|T|}.
```


The translation over $u\in B$ leaves the twelve
characters of $G/B$. Their nine quadratically
twisted corrected sums and first derivatives
are supplied by the
[companion theorem](cubic-companion-selection.md),
with its stated Dirichlet QRH and classical inputs.
The two untwisted cubic corrected functions are
equal and real:
$G_\lambda=G_{\lambda^{-1}}$, since conjugation
permutes the ideals of $F$ and preserves their
norms and primitive Euler factors. Their
logarithmic derivatives at one agree as well.

Assume the same short shift $|a_t/b-x|\le1$.
With the notation $Q$ of the relative comparison,
ordinary Fourier orthogonality now gives the
exact leading term


```math
Q=G_1(x)+(3p_0(T)-1)G_\lambda(x)
       +O(x^{1/2+\epsilon/2}+\log(2x)). \tag{6}
```


Indeed for a cubic root $\zeta$ the sum
$\zeta+\zeta^{-1}$ is 2 on the trivial coset and
-1 on either nontrivial coset, regardless of
their relative proportions. The first-sign
phase is one for the untwisted characters.
There is no small-share approximation:
the coefficient $3p_0-1$ is exact.
The error uses the actual companion bounds,
and the elementary short-shift derivative
estimate $O(\log(2x))$ from the relative
comparison. Constants are fixed at each
accuracy stage.

Consequently the full thick/thin transfer, with
its thin bounds and widths as already proved
sufficient, gives


```math
G_1(x)+(3p_0(T)-1)G_\lambda(x)
       \le E/k+O(x^{1/2+\epsilon}). \tag{7}
```


One may replace $E$ on the right by the good
centered discrepancy from (1).

There are two useful sufficient options.

- Take every top label in the trivial cubic
  coset ($T\subset B$, hence $p_0=1$).
  Then the positive family is simply
  $G_1+2G_\lambda$, independent of the
  auxiliary construction. The one-sided
  positive-residue lemma applies without any
  separate abelian GRH input. More generally
  any fixed $p_0>1/3$ works. This dispenses
  with the original shares $4/10,3/10,3/10$.
- If the abelian base is known by the Dirichlet
  theorem, $G_1$ has the fixed-field bound
  $O_\delta(x^{1/2+\delta})$ for every
  $\delta>0$. This follows, for example,
  by shifting the absolutely convergent
  smoothed Perron integral for the two
  abelian factors to $\Re s=1/2+\delta$,
  using the standard local log-derivative
  estimate and cancelling their poles
  at one with the true corrections.
  The new cubic factor has no real zeros
  by the [eta proof](s3-benchmark.md),
  so either sign of its one-sided bound
  suffices. It is enough that $3p_0(T)-1$
  stay uniformly away from zero with
  a fixed sign throughout the relevant
  cofinal windows. The value of $p_0$
  may vary with the scale; divide (7)
  by its signed coefficient and bound
  the appropriate positive part using
  its fixed lower absolute bound.
  At $p_0=1/3$ the target cancels
  entirely, so a uniform unbiassed
  projection alone cannot detect it.

Both are strictly simpler *acceptance criteria*
for the arithmetic supplier. No claim is made
that the original top set of a geometric
construction can be changed at will. The same
actual maps, labels, metric and counts must
produce the selected $T$; different constraints
may be needed in a new geometric realization.

## 5. A useful thin-profile replacement, if the geometry permits it

In the scalar arithmetic comparison the thin
part of the *centered* discrepancy is exactly
a sum of $w_gG_\psi(a/w_g)$ over the thin labels.
If two profiles agree on the thick positions and
all their thin arguments lie in the established
thin range, then the difference of their
normalized discrepancies is bounded by the sum
of the two thin budgets (8) of the relative
comparison. This follows directly by subtracting
their exact Fourier identities; it does not
compare their uncentered prime sums.

In particular, at the source scales
$b=\exp(x^\epsilon)$ and
$X'=\exp(x^{\epsilon/3})$ one can choose a
candidate common thin weight $w_*=b/X'$,
giving thin arguments of order $xX'$.
The whole thin normalized contribution is
negligible, by the proved companion thin
bound. This gives a simple possible new
profile with all weights large enough for
elementary integer rounding of the good
divisor lengths, as explained in the
torsor note. It is not a license to
replace the weights in the original
arithmetic geometry: that must be
constructed with the new actual profile
if this option is adopted.

**Conclusion.** The open relative geometric
supplier may now be sought for the good
discrepancy of (5) and a simple biased
cubic top set, rather than an exact
ramified prime-power formula with finely
prescribed top shares. The reduction
retains the signs, primitive local
Euler factors, true correcting constants
and fixed-window quantifiers. It does not
supply the quantitative bound for the
good discrepancy or an actual geometric
map. No H07F or H07I closure is claimed.
