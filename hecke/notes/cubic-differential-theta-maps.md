# Equivariant differential theta maps with genuine cubic Frobenius divisibility

24 November 2026. **Actual global maps and good-prime divisibilities.**
This constructs finite-dimensional equivariant maps on the even-level
theta spaces of the explicit cubic CM twists. The maps have proved
arithmetic divisibilities depending on the actual cubic Frobenius,
and explicit Hermitian norm bounds. They are not the parent's TC/ColIn
theta chain or its normalized Poincare maps. The critical-scale global
degree estimate for either realization remains open.

## 1. The same geometric objects and their integral lattices

Let $F=\mathbb Q(\omega)$, $\omega^2+\omega+1=0$,
$\alpha=\sqrt[3]2$, $K=F(\alpha)$, and for $j=0,1,2$ put


```math
E_j:\ y_j^2=x_j^3+2^{2j},\qquad
 \eta_j=dx_j/(2y_j),\qquad
 D_j=2y_j\partial_{x_j}+3x_j^2\partial_{y_j}.
```


Here $D_j$ is a derivation of the affine coordinate ring: it kills
the defining equation. On the smooth elliptic scheme away from
6 it is the invariant vector field dual to $\eta_j$.
These are the curves of the [torsor realization](cubic-torsor-realization.md).
The action $U_j(x_j,y_j)=(\omega x_j,y_j)$ preserves the
canonical principal polarization.

For $m\ge2$ write $V_{j,m}$ for the $\mathcal O_F$-lattice with
basis the monomials $x_j^a y_j^b$, $a\ge0$, $b\in\{0,1\}$,
$2a+3b\le m$. Their pole orders at the origin are distinct:
apart from zero, they are all integers from 2 through $m$.
Over $F$ this is $H^0(E_j,\mathcal O(m[0]))$; away from 6 it
is exactly the global integral section lattice of that line.
Indeed the affine complement of the origin has the displayed
coordinate ring with its unique normal form in $y_j$;
the monomials have distinct orders and leading coefficients
units at the origin. Thus the bound on pole order selects
precisely the indicated monomials. At 2 and 3 we mean the
explicit monomial lattices, not a smooth elliptic model.

These are actual theta section spaces for the power $m$ of
the canonical symmetric principal line. The previously
constructed orbit lines at nonzero 2-torsion $h_s$ satisfy
$\mathcal O(2[h_s])\cong\mathcal O(2[0])$: the divisor of
$x_j-x_j(h_s)$ is $2[h_s]-2[0]$. Thus the even-level spaces
also have the integral orbit-line interpretation over the
torsor away from 6. This does not replace the parent's
individual principal unit theta normalization.

The formulas on monomials are


```math
\begin{aligned}
 D_j(x_j^a)&=2a x_j^{a-1}y_j,\\
 D_j(x_j^a y_j)&=(2a+3)x_j^{a+2}
                  +2a\,2^{2j}x_j^{a-1}.
\end{aligned}
```


Terms with coefficient zero are omitted. They prove, on
these same integral lattices, $D_j:V_{j,m}\to V_{j,m+1}$.
Hence for every $n\ge1$ the following is a global integral
map, with no prime-wise choice of matrix:


```math
\Theta_{j,m,n}:\mathcal O_F[T]_{\le n}\longrightarrow
 \operatorname{Hom}_{\mathcal O_F}(V_{j,m},V_{j,m+n}),
 \qquad P\longmapsto P(D_j).
 \tag{1}
```


It is injective over $F$. If $P$ has degree $k$ and nonzero
leading coefficient, $P(D_j)x_j$ has pole order $k+2$
with nonzero leading coefficient: in the local parameter
of the invariant differential the highest derivative has
leading coefficient $(-1)^k(k+1)!$ times that of $x_j$.
Lower derivatives have smaller pole order.

The maps are equivariant for the actual cubic CM action.
Since $U_j^*D_j(U_j^*)^{-1}=\omega^{-1}D_j$, act on the
domain by $P(T)\mapsto P(\omega^{-1}T)$ and on the codomain
by conjugation by $U_j^*$. More importantly the actual
isomorphisms $\phi_j:E_0\to E_j$ over $K$ give


```math
\phi_j^*D_j(\phi_j^*)^{-1}=\alpha^jD_0,\qquad
 \phi_j^*\Theta_{j,m,n}(P)(\phi_j^*)^{-1}
     =\sum_{k=0}^n c_k\alpha^{jk}D_0^k
 \quad(P=\sum_kc_kT^k).
 \tag{2}
```


The identities follow from $\phi_j^*\eta_j=\alpha^{-j}\eta_0$.
The pullback on the monomial lattices over $\mathcal O_K[1/6]$
is an isomorphism, with basis multiplier
$\alpha^{2ja+3jb}$, a unit there. Equation (2) incorporates
the two actual nontrivial cubic coefficients and their
Galois covariance: $\sigma(\alpha^{jk})=\omega^{jk}\alpha^{jk}$.
Unlike a common tensor repetition, distinct derivative
degrees carry different powers of the cubic character.

## 2. Frobenius enters the invariant derivative itself

Let $v\mid p$, $p>3$, $p\equiv1\bmod3$, so $Nv=p$.
On the residue field of $v$ the actual cubic label is
$r_v\in\mathbb Z/3$ with


```math
2^{(p-1)/3}=\bar\omega^{r_v}.
```


The invariant derivative in characteristic $p$ satisfies
$D^p=A(E,\eta)D$ with $A$ the Hasse invariant.
This standard formula is Katz–Mazur, *Arithmetic Moduli of
Elliptic Curves*, (12.4.1.3), printed p.354
([author text](https://math.bu.edu/people/jsweinst/AWS/Files/KatzMazurArithmeticModuli.pdf)).
Its Cartier characterization is (12.4.1.4).
In our Weierstrass equation this gives


```math
A_{j,v}=[x^{p-1}](x^3+2^{2j})^{(p-1)/2}
       =A_{0,v}\bar\omega^{jr_v},
 \qquad A_{0,v}=\binom{(p-1)/2}{(p-1)/3}\bmod p .
 \tag{3}
```


For the coefficient formula write
$\eta=y^{-p}(x^3+2^{2j})^{(p-1)/2}dx/2$ and apply Cartier.
Its selection of powers $x^{kp-1}$ leaves only $k=1$,
since the polynomial degree is $3(p-1)/2<2p-1$.
All binomial factorials in $A_{0,v}$ are smaller than $p$,
so $A_{0,v}\ne0$. In particular the curves are ordinary.
The exponent of 2 in the selected coefficient is
$2j((p-1)/2-(p-1)/3)=j(p-1)/3$, proving (3).
For $p\equiv2\bmod3$ the corresponding Hasse invariant is zero;
we do not use those primes for the cubic selector.

Choose the integer $a_p$ of smallest absolute value congruent
to the displayed binomial modulo $p$. For $s\in\mathbb Z/3$
form the actual global map


```math
\Delta_{j,p,s}=D_j^p-a_p\omega^s D_j.
 \tag{4}
```


When used on $V_{j,m}$ its target is $V_{j,m+p}$.
Its reduction is zero at $v$ precisely when $jr_v=s$:
by (3) the reduction is
$A_{0,v}(\bar\omega^{jr_v}-\bar\omega^s)D_j$.
The nonzero derivative of $x_j$ proves the converse for
every $m\ge2$. In particular for any positive integer $r$,


```math
\Delta_{j,p,s}^r V_{j,m}
 \subset v^r V_{j,m+pr}
 \qquad(jr_v=s).
 \tag{5}
```


This is an inclusion of actual integral section lattices,
by composing the same operator on the successive pole
orders. If the label is different, its $r$th power is
not identically zero modulo $v$: $D_j^p=A_{j,v}D_j$ with
$A_{j,v}\ne0$ implies $D_j^r x_j\ne0$ for every $r\ge1$
(otherwise repeated application would give $D_jx_j=0$).
The matched exponent in (5) is a lower bound, not an
assertion of exact valuations above the first power.

For a finite collection of such primes, one may compose
the actual operators (4), raised to prescribed powers.
All are polynomials in the same $D_j$ and commute.
Their divisibilities hold simultaneously, with all other
factors integral. For each factor take, for example,
$r_p=(\lfloor a/p\rfloor-w_p)_+$ for integer top order
and nonnegative integer weights. This realizes the
desired hinge as a genuine divisor of a global
differential map at the matching cubic primes. However
its total differential order is $\sum_p p r_p$, not $a$.
The product construction is therefore not yet a
critical-scale replacement for the parent theta chain.

Equivariance of (4) is also explicit:
conjugation by $U_j^*$ multiplies it by $\omega^{-1}$,
because $p\equiv1\bmod3$. Equivalently it is equivariant
after twisting its source by the corresponding character.
Powers and products add these character weights.

## 3. Hermitian norm bounds on the actual section spaces

We record norms on the maps (1), (4), not on unrelated
Euclidean coefficient arrays. They are explicit, but
not claimed to be the parent's normalized period norms.

At a complex embedding uniformize $E_j$ by its invariant
coordinate $z$, so $D_j=d/dz$. Give $\mathcal O([0])$ its
canonical smooth Hermitian theta metric, normalized once
and for all; write $u(z)$ for the norm of the canonical
divisor section. The norm of a meromorphic function
$f$ viewed as a section of $\mathcal O(m[0])$ is
$|f(z)|u(z)^m$. The function $u$ is smooth and positive
away from the origin and comparable to $|z|$ in a fixed
small local disk about it. The logarithmic gradient is
$O(1+\operatorname{dist}(z,0)^{-1})$.
The metric is invariant under the action $U_j$, since
the divisor and curvature are invariant and its
normalization can be chosen invariant. Use normalized
flat Haar measure for the $L^2$ Hermitian metric.

There are fixed constants $C,B\ge1$, uniform over the
three curves and both embeddings, such that for $m\ge2$,


```math
\|D_j f\|_{\infty,m+1}
       \le C(m+1)\|f\|_{\infty,m},
 \qquad
 \|f\|_{\infty,m}\le C(m+1)\|f\|_{2,m}.
 \tag{6}
```


For the first inequality, at $z\ne0$ use the analytic
disk of radius $c\min(1,\operatorname{dist}(z,0))/(m+1)$
in the invariant coordinate, with fixed sufficiently
small $c>0$. On that disk the ratio of $u$ to its value
at the center lies between $\exp(-C/(m+1))$ and
$\exp(C/(m+1))$, by the logarithmic gradient bound.
Cauchy's estimate for the first derivative and
$u(z)\ll\min(1,\operatorname{dist}(z,0))$ give the first
inequality. At the origin it follows by continuity
of the section norm. For the second inequality, use a
finite collection of nonsingular holomorphic local
frames of the line with smooth positive norm. At
every point take a disk of radius $c/(m+1)$ contained
in one frame chart. The metric varies by a factor
$\exp(O(1))$ after its $m$th power. The submean value
estimate for the holomorphic section coefficient
then bounds its squared value by $O((m+1)^2)$ times
the global squared $L^2$ norm. This works also at
the origin. All constants are fixed before $m,n$ vary.

Let $B\ge\sup u$ on all the curves. For $P=\sum c_kT^k$,
iterating (6) and then embedding the lower pole order
into $m+n$ by the additional canonical sections gives


```math
\|\Theta_{j,m,n}(P)\|_{2,m\to2,m+n}
 \le C(m+1)\sum_{k=0}^n
       |c_k| B^{n-k} C^k\frac{(m+k)!}{m!}.
 \tag{7}
```


Indeed the iteration for $D^k$ supplies the product
of the $k$ successive factors $C(m+i)$; the unused
$n-k$ powers contribute at most $B^{n-k}$.
The target $L^2$ norm is at most its supremum norm.
This proves an actual operator bound with natural
theta metrics. With the associated weighted Euclidean
norm on the polynomial coefficients, Cauchy–Schwarz
costs only $\sqrt{n+1}$.

For (4) and its products, the polynomial coefficients
are explicitly those of the factors $T^p-a_p\omega^sT$,
with $|a_p|\le p/2$ and $|\omega^s|=1$ at every
embedding. For an order bound $A=\sum_p p r_p$, put
$Z=C(m+A+1)$, increase $C$ so $Z\ge1$, and use (7)
to bound the product by


```math
C(m+1)B^A
    \prod_p (Z^p+(p/2)Z)^{r_p}.
 \tag{8}
```


Dividing by the matched ideal factors gives the
corresponding local integral maps with the exact
archimedean scalar normalization if the divisor is
principal. This estimate retains the full order $A$.
In particular it does not have the small centered
norm error required by the parent construction.
The weights of the actual differential operators
cannot be discarded merely because the twists are
isomorphic over $K$.

## 4. A simultaneous linear algebra realization of the cubic count

There is a more efficient way to impose the first-order
divisibilities (3) simultaneously, without composing
a large product of prime-dependent differential orders.
This yields a new exact relative index on the maps (1).

For $n\ge2$ take $m=2n$ and put
$W_n=\mathcal O_F[T]_{\le n}$. Let $\mathcal P_n$ be all
prime ideals $v$ above rational primes $3<p\le n$ with
$p\equiv1\bmod3$. Define actual sublattices of $W_n$ by


```math
B_{j,n}=\{P\in W_n:\ P(D_j)V_{j,2n}
                      \subset vV_{j,3n}\ \forall v\in\mathcal P_n\}.
 \tag{9}
```


These are defined by the entries of the same global maps
(1), reduced modulo the single rational squarefree modulus
$\prod_{3<p\le n,p\equiv1(3)}p$. They are not arbitrary
local modifications with unspecified divisibilities.

**Local kernel.** Over $k_v=\mathbb F_p$, the kernel in
(9) is exactly the polynomial multiples, of degree at
most $n$, of


```math
q_{j,v}(T)=T^p-A_{j,v}T .
```


The inclusion follows from the Hasse relation.
For the reverse, divide the polynomial by this monic
polynomial and consider the remainder of degree $k<p$.
If nonzero, evaluate the remainder in the derivation
on $(x_j-x_j(P_0))^k$ at a geometric point $P_0$ where
$y_j(P_0)\ne0$. The local coordinate $x_j-x_j(P_0)$ has
nonzero derivative there. Every lower derivative
vanishes at $P_0$, while the $k$th derivative equals
$k!(2y_j(P_0))^k\ne0$. For $k=0$ use the constant
function. These test functions are in the scalar
extension of $V_{j,2n}$ since $k<p\le n$.
Thus a nonzero remainder cannot annihilate that
space. This also proves the independence of
$1,D_j,\ldots,D_j^{p-1}$ on the stated actual lattice.

For $j=0,1$, the two monic polynomials coincide if
$r_v=0$ and otherwise have greatest common divisor $T$:
the two distinct nonzero values of $A$ give disjoint
sets of nonzero roots. Their least common multiple
therefore has degree $p$ in the first case, $2p-1$
in the second. By CRT the relative index is exactly


```math
\log\#\bigl(B_{0,n}/(B_{0,n}\cap B_{1,n})\bigr)
 =2\sum_{\substack{3<p\le n,\ p\equiv1(3)\\
                   2^{(p-1)/3}\ne1\bmod p}}
    \min(n+1-p,p-1)\log p .
 \tag{10}
```


At each $v$ the extra codimension is
$\min(n+1,2p-1)-p$ in the nonsplit case, and zero
in the split case. The factor two counts both primes
of $F$ over $p$. Every local condition and every
finite-dimensional space in this formula was
constructed above. There is no assumption of a
prime-distribution estimate or of simultaneous
optimal interpolation nodes.

There is also an exact triple variant:
$B_{0,n}\cap B_{1,n}\cap B_{2,n}$ uses the monic lcm
of degree $3p-2$ at nonsplit primes and degree $p$
at split primes. This follows by the same argument,
since all three nonzero Hasse scalars are distinct
at a nonsplit prime. All these lattices are stable
under the action $P(T)\mapsto P(\omega^{-1}T)$,
as is seen from (9) or from the local monic ideals.

## 5. Analytic consequence and the missing bound

For a set $\mathcal A$ of rational primes define


```math
C_{\mathcal A}(X)=
   \sum_{p\in\mathcal A}(\log p)
               ((X-p)_+-(X-2p)_+).
```


Let $\mathcal E$ be the primes $p>3$, $p\equiv1\bmod3$
and $\mathcal N$ those in $\mathcal E$ not splitting in
$K$. At $X=n+1$ equation (10) differs from
$2C_{\mathcal N}(X)$ by $O(X)$: the difference of the
two hinge expressions per prime is at most one,
and Chebyshev bounds their total logarithmic mass.
Thus the actual relative index counts the *nontrivial*
cubic Frobenius classes with a compactly truncated
ramp kernel.

The fixed cubic discrepancy $R(x)$ of the
[S3 benchmark](s3-benchmark.md) has coefficients
$3\mathbf1_{\mathcal N}-2\mathbf1_{\mathcal E}$.
For Re $s>1$, the Mellin transform of


```math
\frac{3C_{\mathcal N}(X)-2C_{\mathcal E}(X)}{X}
```


is the corresponding rational prime series times
$(1-2^{-s})/[s(s+1)]$. Indeed the integral for
$(X-p)_+/X$ is $p^{-s}/[s(s+1)]$.
The prime series is $L'_F(s,\lambda)/L_F(s,\lambda)$
up to the contribution of higher rational prime
powers and the fixed bad set, which is holomorphic
in Re $s>1/2$ by absolute convergence.
The multiplier has no zero there. At real poles
there is no sign obstruction: the eta-product proof
excludes all real zeros of this cubic factor.

Consequently the one-sided window criterion, with
exponent $\theta>1/2$ tending to $1/2$, applies to
either sign. In terms of the index $J_n$ in (10),
it suffices to bound either signed positive part of


```math
\frac{(3/2)J_n-2C_{\mathcal E}(n+1)}{n+1}
```


by $(n+1)^{1/2+o(1)}$ on the prescribed cofinal
windows. This is an exact criterion for the cubic
factor, not a new critical-scale bound. For
completeness the continuous ramp function divided
by $X$ has derivative $O(1)$ away from its finitely
many corners on bounded intervals, uniformly by
Chebyshev; explicitly each active term has
derivative bounded by $2p/X^2$, and their sum is
$O(1)$. Thus square-grid interpolation costs
$O(\sqrt X)$ even for this signed discrepancy.
In the Mellin proof the one-sided lemma can be
used with meromorphic continuation in Re $s>1/2$
rather than Re $s>0$: every nearest-pole disk used
to exclude a pole right of $\theta>1/2$ can be
chosen entirely in that domain. Alternatively
retain the full prime-power series and its
$O(\sqrt X)$ normalized discrepancy, which
satisfies the original continuation hypotheses.

The crucial missing estimate is a bound on the
relative integral degree of (9), with the same
norms and without assuming the desired
prime-counting conclusion. The norm estimate
(7) is an upper bound on operators for given
coefficients; it does not bound the size of
short spanning families of (9). CRT and (10)
identify their index but do not supply a useful
lower degree estimate. The parent's global
divisor argument still requires its same-map
source/target degree and norm comparisons.
In particular multiplying by fixed cubic
units cannot by itself create the new good-prime
divisibilities; here the relation (3) is what
does so.

**Status:** (1)--(10), the good-prime higher
divisibilities and the explicit norm bounds are
proved. This is a new family of actual equivariant
differential operators on the cubic theta spaces,
not a proof that the original large-rank theta
chain and automorphic period maps have been
identified with it. No critical-scale
prime-discrepancy estimate, global Selmer length
bound, or complex-zero exclusion is claimed.

## Reproducible checks

Run `python hecke/scripts/check_cubic_theta.py` (NumPy and SymPy).
The [certificate](../certificates/cubic-theta-check.json) records
228 curve/prime cases, checking the p-Lie identity on both x and y,
and 12 exact stacked-matrix rank tests. These are finite consistency
checks, not proofs of a critical-scale estimate. The
[coefficient-to-theta interface](cubic-theta-coefficient-interface.md)
subsequently supplies monic simultaneous operators of the
prescribed order, with an explicit CRT height cost.
