# Cubic theta coefficient realization and simultaneous operators of bounded order

24 November 2026. This strengthens the actual global
[differential theta maps](cubic-differential-theta-maps.md).
It constructs a rank-three coefficient-to-theta map that couples
the entire cubic torsor to a single even-level theta space, gives
the corresponding Frobenius action on that space, and constructs
simultaneous monic differential operators of the prescribed order.
The archimedean cost of the latter still contains the divisor it
realizes. No sharp global arithmetic inequality or identification
with the parent's TC/ColIn period chain is claimed.

## 1. A single actual cubic coefficient-to-theta map

Keep $F=\mathbb Q(\omega)$, $\alpha^3=2$,
$K=F(\alpha)$, $E_1:y^2=x^3+4$, and
$R=\mathcal O_F[1/6]$. The degree-three torsor algebra
$A=R[z]/(z^3-2)$ is finite etale over $R$.
Its geometric roots $z_s=\alpha\omega^s$ index the
nonzero two-torsion points $(-z_s^2,0)$ on $E_1$.
For each such point the divisor of $x+z_s^2$ is twice
the point minus twice the origin. Therefore its square
represents the fourth power of the corresponding
unit-normalized orbit theta section in the common line
$\mathcal O(4[0])$ (with the origin rigidification
using the invariant local coordinate).

Define the global $R$-linear map


```math
\Phi:A\longrightarrow H^0(E_1,\mathcal O(4[0])),\qquad
 f\longmapsto \operatorname{Tr}_{A/R}
                  \bigl(f(z)(x+z^2)^2\bigr).
 \tag{1}
```


This is a trace in the finite etale coefficient algebra,
not a trace of the still-unconstructed global period map.
After base change splitting the torsor it maps its three
idempotents to the actual three theta sections
$(x+z_s^2)^2$. Each has the same leading coefficient
at the origin. Its image is in the even subspace for
elliptic inversion, with basis $x^2,x,1$.

The calculation on the integral basis $1,z,z^2$ is exact:


```math
\Phi(1)=3x^2,\qquad \Phi(z)=12x,\qquad
 \Phi(z^2)=12.
 \tag{2}
```


Indeed the trace of $z^k$ is zero unless $3\mid k$,
when it is $3\cdot2^{k/3}$.
Thus the determinant in the displayed bases is
$432=2^4 3^3$. It is a unit over $R$.
This proves that (1) is an actual integral
isomorphism onto that even theta space at every
good prime. Both nontrivial cubic components
survive. In contrast, the same construction with
the unsquared sections $x+z_s^2$ lands in dimension
two and necessarily kills one Fourier component.

Let $u:z\mapsto\omega z$ on $A$ and $U(x,y)=(\omega x,y)$.
With the canonical rigidification on the common theta
line, the following equivariance is literal:


```math
\Phi\circ u^{-1}=(\omega U^*)\circ\Phi .
 \tag{3}
```


It follows either from (2) or directly by relabelling
the trace. In particular the scalar factor in the
theta linearization is not omitted: $\omega U^*$
fixes the leading $x^2$ section at the origin.

At a prime $v$ of residue cardinality $p\equiv1\bmod3$,
the arithmetic Frobenius endomorphism of $A/vA$ is
$z\mapsto z^p=\bar\omega^{r_v}z$, where $r_v$
is the actual cubic label. Thus transporting Frobenius
by (1) gives the actual linear operator on the even
theta space with eigenvalues $1,\bar\omega^{r_v},
\bar\omega^{2r_v}$ in the basis $x^2,x,1$.
By (3) the label action and Frobenius trace satisfy


```math
\operatorname{Tr}\bigl((\omega U^*)^{s}
           \Phi\operatorname{Fr}_v^k\Phi^{-1}\bigr)
   =3\,\mathbf1_{k r_v=s}.
 \tag{4}
```


Here the reduction and the inverse of (1) are integral
at the good prime. This is the actual cubic kernel on
theta sections, not just a permutation space external
to them. The sign convention in (4) follows from the
inverse action in (3).

### Exact fixed-rank norm cost

At each complex embedding give $A$ the orthogonal
permutation metric $\|f\|^2=\sum_s|f(z_s)|^2$.
Give the theta target its canonical $L^2$ metric,
as in the differential map note. The automorphism
$U$ is an isometry; the three eigenvectors $x^2,x,1$
of $\omega U^*$ are pairwise orthogonal, since their
unitary eigenvalues are distinct.
The source basis $1,z,z^2$ is orthogonal as well.
The three singular values of (1) are consequently


```math
\frac{3\|x^2\|}{\sqrt3},\qquad
 \frac{12\|x\|}{\sqrt3\,|\alpha|},\qquad
 \frac{12\|1\|}{\sqrt3\,|\alpha|^2}.
```


They are fixed positive constants, independent of
the moving auxiliary data. This gives an exact norm
comparison on the actual coefficient and theta
lattices, with only fixed finite-place determinant
cost at 2 and 3 on the monomial models.
It does not identify the theta metric with the
parent's normalized global period metric.

If an admitted parent integral section map is $T$,
one may genuinely tensor it with (1) on the external
product with this elliptic curve. The section spaces
of the external line product are the tensor products
by Kunneth in degree zero (use the existing parent
locally free section lattice and its base-change
property); or one may simply take the indicated
actual tensor sublattices. Product Haar measures
give product Hermitian metrics. The tensor map
$T\otimes\Phi$ has singular values all pairwise
products of those of $T$ and $\Phi$. At good primes
its elementary divisors are those of $T$ repeated
three times, because $\Phi$ is an integral
isomorphism. The Frobenius label operator on the
new coefficient factor is now realized within the
section space by (4).
This supplies a coefficient realization for the
parent's integral maps. Tensoring alone still does
not give a new label-sensitive divisor inequality:
one needs the local Frobenius-dependent operator
coupling, as below.

## 2. The p-Lie formula on the original higher-rank geometry

The local mechanism of the differential theta maps
does not require dimension one.
Let $\mathcal A$ be a smooth commutative abelian scheme
with a compatible action of $R$, and $U=[\omega]$.
Over $R$ the Lie bundle splits into its two cubic
eigenbundles (and any invariant summand if $U$ is an
abstract order-three action). The projectors are
integral since 3 is invertible.
For a good prime of residue characteristic
$p\equiv1\bmod3$, the p-fold composition of an
invariant derivation is an invariant derivation:
the middle terms of the Leibniz expansion vanish
modulo $p$. On the Lie bundle this defines an
additive p-semilinear map, because invariant
derivations commute for a commutative group.
It commutes with $U$ as a semilinear map and hence
preserves these eigenspaces when $p\equiv1\bmod3$.

Twist the polarized scheme by the actual cubic
torsor with automorphism $U^j$. Over the splitting
cover, in an eigenbundle choose the convention
in which a descended invariant vector field
is identified with $\alpha^k D$ for some
$k\in\{0,1,2\}$ determined by that eigencharacter
and the descent cocycle. Such frames exist locally:
the eigensummands of the torsor algebra are
generated by $1,z,z^2$ and their generators are
units on the cover. If the original p-map matrix
in a frame of that eigenbundle is $H$, in the
corresponding descended frame its matrix is


```math
H_{\rm twisted}=\alpha^{k(p-1)}H
                     =\bar\omega^{k r_v}H\quad\bmod v .
 \tag{5}
```


This follows by p-semilinearity followed by the
inverse frame scaling; no global algebraic
Frobenius lift is assumed.
For a mixed frame the analogous formula has the
source factor $\alpha^{kp}$ and the inverse target
factor; on the eigenspace above they give (5).
It is valid after base change at a residue-degree
one prime of $F$ with the lower-field Frobenius
label retained. For a larger residue field one
must track the actual semilinearity and iterate
to recover its residue Frobenius; the rational
prime is not silently replaced by the upper norm.

This is an exact local Hodge/differential
compatibility for the actual twisted abelian
scheme, including the higher-rank CM geometry
if its good-prime hypotheses hold. It does not
identify all its Hasse matrices with the scalar
ones of $E_j$. In particular the parent
Frobenius-linked correction sequences and
divisor formulas must be checked with the
new matrices and the selected tangent flags.

## 3. Simultaneous monic operators of the correct order

In Section 2 of the differential map note, a
product of prime-specific operators has order
$\sum_p p r_p$. This can be avoided by a global
coefficient construction, retaining the actual
local divisibilities.

Fix $j\in\{1,2\}$ and an integer $a\ge1$.
At finitely many degree-one good prime ideals
$v$ of $F$, above rational primes $p_v$, prescribe
nonnegative integers $h_v$ with $p_v h_v\le a$.
At each such place use its actual matching label
$s_v=j r_v\bmod3$. For example one can take
$h_v=(\lfloor a/p_v\rfloor-w_v)_+$ with integer
nonnegative weights $w_v$. Write


```math
I=\prod_v v^{h_v}.
```


The local monic polynomial of degree $a$


```math
P_v(T)=T^{a-p_vh_v}
          (T^{p_v}-a_{p_v}\omega^{s_v}T)^{h_v}
```


maps $V_{j,m}$ into $v^{h_v}V_{j,m+a}$ under
$T\mapsto D_j$, by the already proved divisibility.
All its nonzero monomials have degree congruent
to $a$ modulo three, because $p_v\equiv1\bmod3$.

**Theorem.** There is a single monic
$P\in\mathcal O_F[T]$ of degree $a$ with
$P(\omega^{-1}T)=\omega^{-a}P(T)$ such that


```math
P(D_j)V_{j,m}\subset I V_{j,m+a}
                  \quad\text{for every }m\ge2 .
 \tag{6}
```


The same operator works at all the prescribed
primes; its order is $a$, not the sum of the
local orders. Its coefficients, apart from the
monic coefficient, have absolute values at
both complex embeddings at most
$C_F\sqrt{NI}$.

**Proof.** Use CRT modulo the pairwise coprime
ideals $v^{h_v}$ on each coefficient below
degree $a$, requiring congruence to $P_v$.
Only coefficients of degree $a\bmod3$ need
be chosen; the rest are zero. The leading
coefficient is one. Since $F$ is norm-Euclidean,
$I=(\gamma)$ for a nonzero integral $\gamma$,
and $|\sigma(\gamma)|=\sqrt{NI}$ at both
complex embeddings. Every coefficient class
has a representative in the translate of
a fixed centered fundamental parallelogram
scaled by $\gamma$, with the stated bound.
The difference $P-P_v$ has all coefficients
in $v^{h_v}$. All powers of $D_j$ are
integral on the actual monomial lattices,
so (6) follows at each local place and hence
globally. The leading term makes the map
nonzero in characteristic zero by the
pole-order argument in the differential
map note. QED.

In particular the normalized map
$\gamma^{-1}P(D_j)$ is integral on the
actual lattices at *every* finite prime,
including the monomial models at 2 and 3.
It is equivariant with the indicated
homogeneous character (twist the source
linearization accordingly). Its norm
is explicitly bounded using (7) of the
differential map note:


```math
\begin{aligned}
 \|\gamma^{-1}P(D_j)\|_{2,m\to2,m+a}
 \le C(m+1)\biggl[
 &C_F\sum_{\substack{0\le k<a\\k\equiv a(3)}}
        B^{a-k}C^k\frac{(m+k)!}{m!}\\
 &+(NI)^{-1/2}C^a\frac{(m+a)!}{m!}\biggr].
\end{aligned}
\tag{7}
```


The constants are independent of $a,m$ and the
finite prime set. This is an actual global
divisibility and norm estimate on the same
map, with a correct differential order.
It is substantially smaller in order than
the product construction.

One can also construct joint operators for
several cubic twists. At each prime choose
the product of the distinct matching
$T^{p_v}-a_{p_v}\omega^sT$ factors to the
required largest exponents for their
respective groups of labels. If their
total local degree is at most $a$, multiply
by the appropriate power of $T$ to make
a monic polynomial of degree $a$ and
apply the same CRT proof. The equal
Hasse scalars at a split prime allow
reuse of one factor for all twists.
At a nonsplit prime different factors
must be retained. This construction is
compatible with the exact local lcm
formula in the differential map note.

## 4. The exact remaining norm/degree issue

The coefficient estimate for the unnormalized
operator in (6) costs $\frac12\log NI+O_F(1)$
in logarithmic coefficient height. This is
precisely the size of the prime divisor
it realizes. Normalizing by $\gamma$ in
(7) cancels this cost, but supplies no
independent lower bound on the source
degree. One cannot conclude a sharp
bound on $\log NI$ from (7).

There is an elementary upper bound on
$NI$ from the leading pole coefficient:
applying (6) to $x_j$ gives
$I\mid((a+1)!)$ in $\mathcal O_F$,
since its highest pole coefficient is
$(-1)^a(a+1)!$ and lower derivatives have
smaller pole order. This does not improve
the all-prime factorial budget to the
centered cubic prime-discrepancy bound.
The local hinge exponents were chosen
within that elementary factorial bound
in the first place.

The useful conclusion is thus precise:
we now have actual label-sensitive cubic
theta maps, simultaneously prescribed
good-prime divisibilities at the correct
operator order, and proved archimedean
norms. To obtain the required prime
inequality one still needs a *collective*
degree/norm estimate for a family of
such maps, not just CRT representatives
whose height pays for the entire
arithmetic index. The parent's
determinant/period argument would have
to identify the actual theta derivative
operators with its normalized source
and target lattices, or a new global
degree argument must give that saving.
Neither is supplied here.

No assertion about the original
TC/ColIn see-saw, global Poincare
period equality, or the final
square-root-scale prime estimate
is made from these finite-dimensional
constructions.
