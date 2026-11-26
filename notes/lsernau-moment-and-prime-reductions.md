# A shorter spanning argument and a fixed-modulus analytic ending

26 November 2026. **Status: the abstract propositions below are proved
here. Their arithmetic hypotheses are not asserted for a new theta
construction.** They refine two parts of the Sernau–Anthropic rewrite of
Alpöge's proof at
[`72fead102f663d5c7a407964a13dc0cf9d977207`](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207).

The first proposition generalizes the finite-group spanning argument to
arbitrary finitely supported probability distributions, replaces a
uniform source hypothesis by its mean positive deficit, and keeps the
exact affine recurrence instead of introducing a stopping threshold.
The second explains why the readable edition has a particularly simple
analytic ending: its auxiliary character and modulus are fixed while
the large cutoff tends to infinity.

## 1. Two scalar moments suffice for spanning

Let (S,T) be finite-dimensional complex Hilbert spaces, of dimensions


```math
d=\dim S>0,\qquad D=\dim T>0.
```


Let $A_t:S\to T$ be a finite family, with probabilities
$p_t\ge0$, $\sum_t p_t=1$. Zero-probability members may be removed.
For a self-adjoint operator $H$, write $H_+$ for the operator obtained
by replacing its negative eigenvalues by zero. Put


```math
K=\sum_t p_t A_tA_t^*,\qquad
 \delta={1\over d}\sum_t p_t\operatorname{tr}(I-A_t^*A_t)_+.
```


Suppose that, for some $\epsilon\ge0$,


```math
\operatorname{tr}K^2\le{(1+\epsilon)d^2\over D},
 \qquad e:=2\delta+\epsilon<1.                       \tag{M1}
```


No group action, pointwise singular-value estimate, or uniform bound on
the individual source deficits is assumed.

### Proposition 1 (mean-deficit covering)

Set $\lambda=d/(2D)$. Then $0<\lambda<1$. For every integer
$k\ge0$, at most $k$ of the maps have images whose span has
codimension at most


```math
D\{e+(1-e)(1-\lambda)^k\}.                         \tag{M2}
```


In particular, for $e<\eta<1$, one can obtain a span of dimension at
least $(1-\eta)D$ using at most


```math
k=\left\lceil {2D\over d}
             \log{1-e\over\eta-e}\right\rceil
```


maps. The total source-dimension cost satisfies


```math
kd\le d+2D\log{1-e\over\eta-e}.                   \tag{M3}
```


The sharper integer choice replaces $2D/d$ by
$1/[-\log(1-\lambda)]$.

**Proof.** Let $F\subset T$ have dimension $\alpha D$, and let
$U_t=A_t^{-1}F$. For any subspace $U\subset S$,


```math
\dim U-\|A_tP_U\|_{\rm HS}^2
 =\operatorname{tr}\bigl(P_U(I-A_t^*A_t)\bigr)
 \le\operatorname{tr}(I-A_t^*A_t)_+.
```


Here $P_U$ is orthogonal projection. On $U_t$, the image of $A_t$
lies in $F$, so
$\|A_tP_{U_t}\|_{\rm HS}^2\le\|P_FA_t\|_{\rm HS}^2$.
Average the resulting inequality. Hilbert–Schmidt Cauchy–Schwarz gives


```math
\sum_t p_t\dim U_t
 \le\delta d+\operatorname{tr}(P_FK)
 \le d\{\delta+\sqrt{\alpha(1+\epsilon)}\}
 \le {d\over2}(1+\alpha+e).                         \tag{M4}
```


The last inequality is $2\sqrt{uv}\le u+v$, with
$u=\alpha$, $v=1+\epsilon$. Some $t$ satisfies the same upper
bound for $\dim U_t$. Rank–nullity for the map to $T/F$ now gives


```math
\dim(F+A_tS)-\dim F=d-\dim U_t
 \ge {d\over2}(1-\alpha-e).                         \tag{M5}
```


The positive deficit is at least $d-\operatorname{rank}A_t$, hence
$\delta d\ge d-D$. Since $\delta<1/2$, this proves $d<2D$.
Writing $r$ for the current missing share $1-\alpha$, (M5) gives


```math
r_{j+1}\le(1-\lambda)r_j+\lambda e.
```


If $r_j\le e$, stop; keeping the same subspace still satisfies this
inequality. Starting at $r_0=1$ and iterating proves (M2). Finally
$(1-\lambda)^k\le e^{-\lambda k}$, and the ceiling costs less than
one additional map. This proves (M3). Repeated choices cause no problem:
while $r_j>e$, a chosen map must add positive rank and therefore cannot
already have its whole image in the span. $\square$

The unrelaxed square-root inequality in (M4) also gives the stronger
one-step bound


```math
r_{j+1}\le r_j-{d\over D}
  \bigl(1-\delta-\sqrt{(1+\epsilon)(1-r_j)}\bigr)_+.
                                                               \tag{M6}
```


The affine version is usually easier to use. Its limiting missing share
is $2\delta+\epsilon$, rather than a separately imposed multiple of
one common error parameter.

### The finite-group identity

If a finite group acts unitarily on $T$, and $A_g=\rho(g)B$ with
uniform probability, then


```math
\operatorname{tr}K^2
 ={1\over|G|}\sum_{g\in G}\|B^*\rho(g)B\|_{\rm HS}^2.          \tag{M7}
```


Indeed, expand $K^2$, move factors cyclically inside the trace and
replace the pair $(g,h)$ by $(g,g^{-1}h)$. Each relative group
element occurs $|G|$ times.

If the target is the image of an invariant orthogonal projector $P$,
apply Proposition 1 to $A_g=P\rho(g)B$, regarded as a map into
$PT$. Its covariance is $PK_BP$; its squared Hilbert–Schmidt norm
is at most that of $K_B$. Thus an upper bound for the unprojected
moment supplies the projected moment, while the source deficit must be
that of $PB$. Projecting can destroy the near-isometry, and that loss
cannot be omitted.

For the source's common error $u$, its near-isometry assumption is
equivalent to
$\operatorname{tr}(I-B^*PB)_+\le ud$. To see the equivalence,
maximize $\operatorname{tr}(P_U(I-B^*PB))$ over subspaces $U$:
the positive eigenspace realizes the maximum. The source's second moment
then permits $\delta\le u$, $\epsilon=u$, and $e\le3u$.
For any $3u<\eta<1$, (M3) replaces the source's sufficient threshold
$16u$ and its coarser logarithmic covering constant.

### Integral restrictions remain visible

Let $S_0\subset S$ have codimension $c$. Restricting $k$ maps
to $S_0$ reduces the dimension of their combined image by at most
$kc$: choose a complement of $S_0$, and bound the sum of the
images of that complement by $kc$. Consequently the final missing
share is at most the bound in (M2) plus $kc/D$.

This is a rank statement. It does not bound an integral index, construct
short integral vectors, or identify the actual Poincaré map. When used
with Theorem A, select independent vectors from the original short
images; do not replace them by orthogonal projections or arbitrary
complex combinations and assume integrality survives. Scaling a map by
a nonzero common scalar preserves its image, but the norm and index
calculations must retain that scalar.

Two elementary obstructions explain the hypotheses. With all $A_t=0$,
the second-moment upper bound alone holds but no image is nonzero. With
one isometric embedding into a fixed proper subspace, the source deficit
is zero but repeated choices never leave that subspace; the moment
condition detects the concentration.

**Source comparison.** This proves and strengthens the mechanism in
[`New/Spanning/SecondMoment/FewTranslates.lean`, lines 313–388 and 472–534](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/FewTranslates.lean#L313-L534).
The actual theta moments are supplied there by
[`SpanningTheorem.lean`](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean).
Our [retained positive-trace framework](retained-column-positive-traces.md)
and [weighted scalar transport](weighted-height-and-scalar-traces.md)
are useful potential suppliers. Equality of their maps, normalizations
and probability measures with this construction remains a separate check.

## 2. The larger cutoff needs only fixed-modulus prime estimates

Fix a positive modulus $q$ and a nonprincipal quadratic character
$\chi$ of conductor coprime to $q$. Define


```math
a(n)=\Lambda(n)(1-\chi(n))1_{n\equiv1\pmod q},\qquad
 A(t)=\sum_{n\le t}a(n).
```


The classical prime number theorem in the finitely many fixed residue
classes modulo $q\operatorname{cond}\chi$ gives, for every $B>0$,


```math
A(t)={t\over\varphi(q)}
       +O_{q,\chi,B}\!\left({t\over\log^B t}\right).             \tag{P1}
```


Prime powers at the finitely many ramified primes contribute only
$O_{q,\chi}(\log t)$. The coefficient of the main term is
$1/\varphi(q)$, since the fixed nonprincipal quadratic twist has
zero mean on the coprime residue classes. No zero-free estimate uniform
in a growing modulus is being invoked.

### Proposition 2 (integrated remainder)

There is a real constant $c=c(q,\chi)$ such that


```math
R(x)=\sum_{n\le x}a(n)(1/n-1/x)
      -{\log x\over\varphi(q)}-c
      =O_{q,\chi,B}(\log^{-B}x)                              \tag{P2}
```


for every $B>0$.

**Proof.** Partial summation gives the exact identity


```math
\sum_{n\le x}a(n)(1/n-1/x)=\int_1^x {A(t)\over t^2}\,dt.
```


Put $E(t)=A(t)-t/\varphi(q)$. The integral
$c=\int_1^\infty E(t)t^{-2}\,dt$ converges by (P1), and


```math
R(x)=-\int_x^\infty {E(t)\over t^2}\,dt.
```


Use (P1) with exponent $B+1$ and integrate
$1/(t\log^{B+1}t)$. $\square$

**The constant must be identified.** If
$F(s)=\sum_n a(n)n^{-s}=c_0/(s-1)+b_0+O(s-1)$, with
$c_0=1/\varphi(q)$, partial summation gives

```math
F(s)=s\int_1^\infty A(t)t^{-s-1}\,dt
 ={c_0s\over s-1}+s\int_1^\infty E(t)t^{-s-1}\,dt.
```

Taking the limit from real $s>1$ shows $b_0=c_0+c$.
Thus the constant in (P2) is $b_0-c_0$, not $b_0$.
The source writes
$F(s)=\operatorname{logDerivMean}(d,q,s)+c_0s/(s-1)$;
therefore its prescribed constant
$\operatorname{Re}\operatorname{logDerivMean}(d,q,1)$
is exactly our $c$. This checks the normalization needed to use (P2)
for the source's remainder. See
[`PrimeError.lean`, lines 263–291](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L263-L291).

### Corollary 3 (polynomially weighted companion removal)

Fix finitely many functions satisfying (P2). Suppose
$\log x_1(x)\ge x^\kappa$, with fixed $\kappa>0$, and their
coefficients have total absolute value $O(x^a)$, for a fixed $a$.
Then for every fixed $M>0$, their combined contribution at $x_1$
is $O(x^{-M})$. Choose $B>(M+a)/\kappa$ in (P2).

The quantifier order is essential: first fix the characters, $q$,
the accuracy and the requested power; only then let $x$ grow.
This conclusion cannot be used for a character whose conductor changes
with $x$, unless a corresponding uniform theorem is separately proved.

### Application to the readable source

The source holds $q_0$ and its auxiliary quadratic prime $d$ fixed.
Its exact prime-sum identity and main comparison imply


```math
R_{q_0,d}(x)\le {\varphi(q_0)(\log b)^6\over m}
   +|R_{q_0,d}(x_1)|+\log b\,|R_{1,d}(x_1)|.                 \tag{P3}
```


For each $0<\varepsilon<1/100$, admissible data have
$m\ge\sqrt x$, $\log b\le2x^\varepsilon$, and
$\log x_1\ge x^{\varepsilon/12}$. Corollary 3 makes the last
two terms $O(x^{-2})$, after choosing its exponent sufficiently
large. Hence (P3) yields


```math
R_{q_0,d}(x)\ll_{q_0,d,\varepsilon}x^{-1/2+6\varepsilon}.
                                                               \tag{P4}
```


This implication is proved under (P3) and the stated data-existence
hypotheses. It does not itself produce (P3).

This is the argument in
[`New/Reduction/OneSidedBound.lean`, lines 35–162](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L35-L162).
The compact edition uses a different, movable-cutoff window argument
and an $8\varepsilon$ allowance. The preferred ordinary exposition
uses (P1)–(P4), keeping the readable edition's fixed-parameter construction.

## 3. The final zero-detection step and its separate proof

The source's analytic criterion does **not** infer all Dirichlet GRH
from (P4) for one arbitrary quadratic twist. Its hypothesis ranges over
all primes $d$ in a specified progression. For a proposed zero it
chooses one twist whose finite collection of twisted L-functions has no
zero in the relevant bounded rectangle. It then uses Landau's one-sided
lemma and nonnegative real residues to exclude the proposed zero.

That choice precedes the limit $x\to\infty$, so the constants in
(P2) may depend on it. It still requires a genuine finite-height
quadratic-twist selection theorem. In the source this is
`exists_entireL_quadTwist_ne_zero`, used explicitly in
[`New/Reduction/Zeros/Criterion.lean`, lines 37–108](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/Criterion.lean#L37-L108).
The [ordinary zero-detection note](lsernau-zero-detection.md) now supplies
this theorem by a theta mollifier, three-lines and an elementary Jacobi
second moment. It also proves the exact transform, the real-residue
argument and a weaker net-multiplicity selection interface. Thus the
analytic endpoint is complete relative to the named classical results
and the arithmetic remainder bound. Mere nonnegativity of $a(n)$ is not
a replacement for the residue argument.

For ordinary RH one may instead retain our direct zeta criterion if an
actual comparison to the zeta remainder is supplied. The old four-term
comparison is not automatically an identity for the new CM data.

## Consequences for the proof plan

The preferred interface for the new spanning module is the mean source
deficit and one scalar second moment, with explicit rank and denominator
costs. The analytic ending uses fixed-modulus prime number theory and
the one-sided zero criterion. Uniform moving-conductor estimates,
fine spectral conditioning, and the old four-character data are only
needed where a specific remaining supplier actually uses them.
These changes shorten the required interfaces; the global theta
construction, its moment bounds and the twisted determinant estimates
still need ordinary mathematical reconstruction.
