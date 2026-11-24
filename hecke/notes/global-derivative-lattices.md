# Linear-size derivative lattices and stable global metrics

24 November 2026. This improves the
[global interpolation construction](global-interpolation-lattices.md).
The new global evaluation matrices have only linearly many rows.
The arithmetic index agrees with the integrated Chebyshev function
up to an unconditional critical-scale error. A separate addition
of integral sampling points gives uniformly stable archimedean
metrics with negligible derivative-graph determinant penalty.
The lower bound on the resulting relative saturated covolume
is not yet proved.

## 1. Only values and ordinary derivatives are required

For a number field $E$ and $n\ge1$, put


```math
\Lambda_n=\{f\in E[X]_{\le n}: f(\mathcal O_E)\subset\mathcal O_E\},
\qquad
H_n=\{f\in\Lambda_n:f'\in\Lambda_n\}.
```


The first-divided-difference lattice $\mathcal P_{n,1}(E)$
of the interpolation note lies in $H_n$ by continuity at
coincident nodes. Write


```math
I_E(n+1)=\int_1^{n+1}\psi_E(t)\,dt,
\qquad
J_E^{\rm der}(n)=\log\#(\Lambda_n/H_n).
```


**Theorem.** For every fixed number field,


```math
0\le I_E(n+1)-J_E^{\rm der}(n)
 \ll_E (n+1)^{3/2}.
\tag{1}
```


In particular a sufficient critical-scale lower bound for
the finite-order Hecke problem over $E$ is


```math
J_E^{\rm der}(n)\ge
 \tfrac12(n+1)^2-O_\epsilon((n+1)^{3/2+\epsilon})
\tag{2}
```


on the same cofinal polynomial windows as in the interpolation
note. The derivative version has exactly the same strength
at this accuracy; this is not an approximation by a
different zeta function.

### Local equality at the decisive degree-one primes

Let $R$ be a completed DVR at a prime ideal of residue
cardinality $p$, a rational prime with $p^2>n$. Choose a
uniformizer $\varpi$. For $0\le i\le n$ write $i=mp+r$,
$0\le r<p$, and use the digit nodes $b_i=r+\varpi m$.
For $P_k(X)=\prod_{i<k}(X-b_i)$, the local basis theorem
in the interpolation note gives


```math
\Lambda_{n,R}=\bigoplus_{k=0}^n R
      P_k/\varpi^{\lfloor k/p\rfloor}.
```


In this range the first-divided-difference lattice is
obtained by multiplying the basis vectors with $k\ge p$
by $\varpi$, leaving all $k<p$ unchanged: the two local
leading exponents differ by one exactly when $k\ge p$.

We prove that the condition on ordinary derivatives
enforces precisely these multiplications. Write
$f=\sum_k c_k P_k/\varpi^{\lfloor k/p\rfloor}$,
with $c_k\in R$. For $k=mp+r$, $m\ge1$, at a point
$x=a+\varpi t$, $0\le a<p$, there are $m+1$ factors
of $P_k$ in residue class $a$ when $a<r$, and $m$
when $a\ge r$. Differentiating loses at most one
factor of $\varpi$, so $\varpi f'(x)$ is integral.
Its reduction contributed by the basis vector of
index $mp+r$ is zero if $a<r$, and otherwise is


```math
u_{m,r,a}\,\frac{d}{dT}\prod_{j=0}^{m-1}(T-j)
       \bigg|_{T=\bar t},
\qquad
u_{m,r,a}=\prod_{c\ne a}(a-c)^{m+\mathbf1_{c<r}}
             \in\mathbb F_p^\times .
\tag{3}
```


Indeed only terms differentiating a factor in residue
class $a$ survive after multiplying by $\varpi$ and
reducing. The other factors reduce to the displayed
unit. This proof works also when the local rational
prime ramifies, provided the residue cardinality is $p$.

Suppose $f'$ is integral-valued and let $m\ge1$ be
the largest quotient for which a coefficient
$c_{mp+r}$ has nonzero reduction. The polynomial (3)
as a function of $\bar t$ has degree $m-1$ and leading
coefficient $m u_{m,r,a}$. Here $m<p$ because
$n<p^2$, so that coefficient is nonzero. For every
$a$, the reduction of $\varpi f'(a+\varpi t)$ is a
polynomial of degree at most $m-1<p$ vanishing on the
whole residue field. Its leading coefficient gives


```math
\sum_{\substack{r\le a\\mp+r\le n}}
       u_{m,r,a}\,\bar c_{mp+r}=0 .
```


As $a$ runs from zero upwards these equations are
triangular with unit diagonal. They force every
coefficient in that quotient block to vanish, a
contradiction. Hence all $c_k$ for $k\ge p$ are
multiples of $\varpi$. Conversely these multiples
belong to the first-divided-difference lattice
and therefore have integral-valued derivative.

Thus $H_{n,R}=\mathcal P_{n,1,R}$ at every
degree-one prime with $p>\sqrt n$, and the
common relative length is $\max(0,n+1-p)$.

### Bounding all other places

The local difference between the two relative
indices is nonnegative and bounded by the local
length of $\Lambda_n/\mathcal P_{n,1}$, namely


```math
\sum_{k=0}^n\sum_{j\ge1}\mathbf1_{(NP)^j\le k}.
```


At the excluded places, every prime-power term
has rational norm $p^a$ with either $a\ge2$ or
$p\le\sqrt n$. The terms with $a=1$ contribute
at most $[E:\mathbb Q]\sum_{p\le\sqrt n}\log p$.
All higher rational powers together contribute
at most $[E:\mathbb Q]\sum_{a\ge2,\ p^a\le n}\log p$:
for a fixed rational power the sum of the
appropriate residue degrees is at most $[E:\mathbb Q]$.
Both quantities are $O_E(\sqrt n)$ by Chebyshev.
Multiplying by at most $n+1$ possible $k$ proves (1),
using the exact integrated index identity of the
interpolation note.

## 2. Actual global matrices with linearly many rows

Use the bounded global test set $S_{n+1}$ constructed
in Section 2 of the interpolation note. It has
$O_E(n+1)$ points and tests all integer-valued
polynomials of degree at most $n$. Since $f'$ has
degree at most $n-1$, this same set tests its
integer-valuedness. In the monomial coordinates let
$C$ be the matrix of values at the points of $S_{n+1}$,
and let $D$ be the ordinary derivative matrix,
$D X^k=kX^{k-1}$. Then $\Lambda_n$ is the integral
preimage of $C$, and $H_n$ is the integral preimage
of the stacked matrix


```math
C'=\begin{pmatrix}C\\CD\end{pmatrix}.
```


Both matrices have full column rank and only
$O_E(n+1)$ rows. All entries are integral.
Let $\mathfrak d(C)$ and $\mathfrak d(C')$ denote
their maximal-minor ideals. The local Smith form
and determinant-ideal formula give the exact relation


```math
J_E^{\rm der}(n)=
 \log N\mathfrak d(C)-\log N\mathfrak d(C').
\tag{4}
```


This eliminates the need to evaluate every pair
of nodes, and provides one global derivative
map with actual matching source and target.
Adding any number of further integral evaluation
nodes changes neither lattice nor (4).

## 3. Stable simultaneous archimedean sampling

We can remove a separate conditioning difficulty
of the raw bounded test set. Assume $E$ is totally
imaginary, which suffices by our finite-order Galois
reduction. Fix one embedding from each complex
conjugate pair. The Minkowski embedding of
$\mathcal O_E$ is a fixed full lattice and has a
fixed covering radius $c_E$ for the maximum norm.

Choose an integer $R_n\ge C_E(n+1)^2$ of order
$(n+1)^2$. Write $N=2n+1$ and $\zeta_j=e^{2\pi ij/N}$
for $0\le j<N$. By the covering radius choose
$z_j\in\mathcal O_E$ such that simultaneously at
every chosen embedding


```math
|\sigma(z_j)-R_n\zeta_j|\le c_E .
```


At the conjugate embeddings the corresponding
target circle is conjugated. The points are
distinct for sufficiently large fixed $C_E$,
since adjacent targets have distance
$2R_n\sin(\pi/N)$ greater than $2c_E$.
Add these nodes to the original test set, obtaining
$O_E(n+1)$ nodes of height $O_E((n+1)^2)$.
Use each point only once; in the estimates one
may retain repeated value rows, which does not
alter either integral preimage.

For a complex embedding use scaled monomials
$(X/R_n)^k$ as the common coordinates for both
value and derivative matrices. Let $C_0$ be
the exact circle value matrix
$(\zeta_j^k)_{j,k}$, with $0\le k\le n$.
It satisfies $C_0^*C_0=N I$. Write
$\delta_j=\sigma(z_j)/R_n-\zeta_j$.
If $D_0$ is the derivative in the scaled
variable, then $\|D_0\|\le n$ in the ordinary
coefficient Euclidean norm. The exact finite
Taylor formula for each row gives the perturbed
circle matrix


```math
C_{\rm circ}=\sum_{r=0}^n
       \operatorname{diag}(\delta_j^r)C_0D_0^r/r!.
```


Hence


```math
\|C_{\rm circ}-C_0\|
 \le\sqrt N\bigl(e^{c_E n/R_n}-1\bigr).
```


In particular its least singular value is at
least $\sqrt N/2$ and its largest at most
$2\sqrt N$, uniformly after increasing the fixed
$C_E$. The old bounded nodes satisfy
$|\sigma(a)|/R_n\le1/2$, again after increasing
the constant. Each of their scaled rows has
squared norm at most $\sum_{k\ge0}4^{-k}=4/3$.
As there are only $O_E(n+1)$ such rows, adding
them gives, for the augmented value matrix $V$,


```math
c(n+1)I\ \le V^*V\le C(n+1)I
\tag{5}
```


at every archimedean embedding, for fixed
positive constants depending only on $E$.

In the same coordinates the derivative on the
polynomial domain is $R_n^{-1}D_0$. Thus for
$A=V^*V$, the stacked matrix of values and
derivatives has Gram matrix


```math
A'=A+R_n^{-2}D_0^* A D_0.
```


Equation (5) yields the uniform bound


```math
0\le\log\frac{\det A'}{\det A}
 \le (n+1)\log(1+C_E n^2/R_n^2)
 =O_E((n+1)^{-1}).
\tag{6}
```


This is an actual archimedean estimate, rather
than an assumption on an interpolation condition
number. In particular the large number of
p-adic residue conditions does not force poor
conditioning of these global value matrices
once extra integral sampling rows are allowed.

## 4. The exact remaining covolume inequality

Let $L_V=V E^{n+1}\cap\mathcal O_E^M$ and
$L_{V'}=V'E^{n+1}\cap\mathcal O_E^{2M}$
be the saturated lattices in the actual
unscaled value spaces, endowed with the
induced Euclidean/Hermitian metrics at the
embeddings, and write $\mathscr V$ for
their covolumes divided by $c_E^{n+1}$
(where in this normalization $c_E$ denotes
the Minkowski covolume of $\mathcal O_E$,
not the covering radius).
The determinant formula from the interpolation
note, applied to the two matrices in a common
domain basis, gives


```math
J_E^{\rm der}(n)
 =\log\frac{\mathscr V(L_{V'})}{\mathscr V(L_V)}
       -\frac12\sum_{\sigma}
                \log\frac{\det A'_\sigma}{\det A_\sigma}.
```


Scaling the monomial columns by $R_n^{-k}$
does not alter either Gram determinant ratio:
the common change-of-basis factors cancel.
Thus (6) proves the global statement


```math
\log\frac{\mathscr V(L_{V'})}{\mathscr V(L_V)}
      = I_E(n+1)+O_E((n+1)^{3/2}).
\tag{7}
```


Equivalently one may keep the sharper exact
index $J_E^{\rm der}(n)$ on the right with
error $O_E((n+1)^{-1})$.

Projection of the derivative graph onto the
value coordinates maps its saturated lattice
into $L_V$. Its operator norm is at most
one, and its inverse on the real or complex
polynomial image has norm bounded by
$\sqrt{1+C_E n^2/R_n^2}$. Nonetheless its
integral index may be enormous. This is exactly
the missing arithmetic contribution; no
lower bound of size $\exp((n+1)^2/2)$ follows
merely from the near-isometry in (6).

The sole remaining bound in this explicit
alternative route is


```math
\log\frac{\mathscr V(L_{V'})}{\mathscr V(L_V)}
 \ge \tfrac12(n+1)^2
      -O_\epsilon((n+1)^{3/2+\epsilon})
```


on the stipulated windows. It implies (2),
and hence RH for the fixed Dedekind zeta
function by the already proved Mellin lemma.
This narrows the global estimate to a relative
saturated-covolume lower bound on two
linear-size, uniformly conditioned matrices.
It does not establish that lower bound.
No CM height, Selmer, Masullo, or QRH input
is used in (1), (4), (5), (6), or (7).

**Scope:** this is a new local derivative
equality, an unconditional error estimate
for the actual global index, and a proved
global archimedean conditioning estimate.
There is no claim of a new critical-line
zero exclusion, of the critical-scale
prime discrepancy itself, or of a Lean proof.

## 5. Independent finite verification in the cubic field

The [exact HNF script](../scripts/check_derivative_lattice.py) was
run with SymPy 1.14.0 on the degree-six field of discriminant
-34992. It independently checks the integral multiplication
basis and prime ideal norms, then computes the integer
row-lattice indices for 76 actual evaluation nodes and their
ordinary derivatives in degrees 3 through 10. The value index
agrees with the proved all-prime characteristic formula at every
tested degree, so the finite set tests the full value lattice
in those degrees. The derivative index is computed directly;
the divided-difference index for comparison comes from the
proved local formula, not an independent divided-difference HNF.
For degrees 3 through 7 the two relative indices coincide;
in degree 8 they differ by a factor of 4, in degree 9 by 48,
and in degree 10 by 576. These are concrete examples of the
small-prime discrepancy that (1) retains. The
[certificate](../certificates/derivative-lattice-check.json)
records all integer indices. This finite calculation is not an
asymptotic estimate or a zero test.
