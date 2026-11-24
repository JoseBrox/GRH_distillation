# Integral cubic-sector comparison at the exceptional primes

24 November 2026. The [prime-to-six decomposition](cubic-coefficient-interface.md)
used semisimplicity. This note removes that restriction at the level
of strict Selmer **comparison**, with explicit uniformly controlled
integral errors. It does not bound the actual new odd-prime sector
lengths. The independent
[2-primary common-window theorem](cubic-two-primary-window.md)
already bounds the whole moving cubic host at 2, so the 2-primary
comparison below is optional. At 3 it removes a genuinely new
integral splitting issue.

Keep $F=\mathbb Q(\omega)$, $K=F(\sqrt[3]2)$,
$L_0=F R_h(\sqrt{-q},\sqrt{-d})$, $L=K L_0$,
$B'=\operatorname{Gal}(L_0/F)$ of order $m=2^{h+2}$, and the cubic
character $\lambda$ of $K/F$. The strict condition on a discrete
Galois module $D$ is


```math
S_E(D)=\ker\left(H^1(G_E,D)\longrightarrow
 \prod_{v\nmid\ell}H^1(I_v,D)\times
 \prod_{v\mid\ell}H^1(G_{E_v},D)\right).
```


This includes the full local decomposition condition at
$\ell$, not just the inertia condition. For the Tate module
$\mathbb Q_\ell/\mathbb Z_\ell(-e)$ use the abbreviation
$\lambda_\ell(E,e)$ for its $\mathbb Z_\ell$-length. Qualitative
finiteness of those groups is supplied by the parent's
[K-theory/duality theorem](../../notes/qualitative-selmer-finiteness.md).
All extensions are totally imaginary.

## 1. Strict kernels under an integral isogeny

Let $\mathcal O$ be the ring of integers of a finite extension of
$\mathbb Q_\ell$, with fraction field $E_\mathcal O$.
Suppose $f:T\hookrightarrow T'$ is a Galois-equivariant
injection of free finite-rank $\mathcal O$-lattices of the
same rank with finite cokernel $C$. The induced map of
discrete modules fits into an exact sequence


```math
0\longrightarrow C\longrightarrow
 T\otimes_\mathcal O(E_\mathcal O/\mathcal O)
 \longrightarrow T'\otimes_\mathcal O(E_\mathcal O/\mathcal O)
 \longrightarrow0 .
```


For example, identify $C=T'/fT$ with the preimage of $T'$ in
the common fraction-field space modulo $T$. Put $D,D'$ for
the two discrete modules. Let $S$ be a fixed finite set
of places of the base number field containing those over
$\ell$ and all ramification of both lattices. Then


```math
\operatorname{length}_\mathcal O S_E(D)
 \le \operatorname{length}_\mathcal O S_E(D')
       +\operatorname{length}_\mathcal O H^1(G_{E,S},C).
 \tag{1}
```


Here $G_{E,S}$ is the maximal Galois group unramified outside
$S$ (include the archimedean places if needed). Indeed
functoriality carries strict classes to strict classes.
The kernel of the resulting map is represented by classes
of $H^1(G_E,C)$ by the long exact cohomology sequence.
For a representative class and $v\notin S$, the restriction
to $I_v$ maps to zero in $H^1(I_v,D)$. Both $C$ and $D$ have
trivial inertia action there. The injection of modules gives
an injection of their homomorphism groups on inertia, hence
the restriction of the representative is itself zero.
Since $C$ is unramified there, inflation--restriction shows
that the class belongs to $H^1(G_{E,S},C)$. This proves (1).
No surjectivity on strict kernels is assumed.

For a filtration of a finite module by residue-field
representations $C_i$, repeated use of the long exact
sequence gives


```math
\operatorname{length}_\mathcal O H^1(G_{E,S},C)
 \le\sum_i \dim_{k_\mathcal O}H^1(G_{E,S},C_i)
```


when each $C_i$ is killed by the uniformizer. In particular
a bound for one-dimensional composition factors gives a
bound proportional to the integral length of the cokernel.
The inequalities hold with infinite lengths as well;
all finite comparisons below follow from qualitative
finiteness of the field groups and the finite errors,
using isogenies in both directions.

## 2. At 3: a single lost residue-field dimension

Work first over $L_0$, not over its growing character
decomposition. Let $\Gamma=C_3=\langle u\rangle$ and let
$\mathcal O_3=\mathbb Z_3[\omega]$, a DVR with uniformizer
$1-\omega$ and residue field $\mathbb F_3$.
The evaluation map


```math
\begin{aligned}
 f:\mathbb Z_3[\Gamma]&\longrightarrow
      \mathbb Z_3\oplus\mathcal O_3,\\
 P(u)&\longmapsto(P(1),P(\omega))
\end{aligned}
```


is equivariant, with $u$ acting trivially on the first
factor and by $\omega$ on the second. Its matrix in the
displayed integral bases is


```math
\begin{pmatrix}1&1&1\\1&0&-1\\0&1&-1\end{pmatrix}.
```


The determinant is 3. Its image is exactly the sublattice
of pairs with $P(1)\equiv P(\omega)\bmod(1-\omega)$:
the inclusion is clear and both sublattices have index
3. The cokernel is a single trivial $\mathbb F_3$-module.
The reverse integral isogeny $3f^{-1}$ has cokernel of
$\mathbb Z_3$-length two, killed by 3; its composition
factors are trivial $\mathbb F_3$-modules, since $\Gamma$
is a 3-group. These facts include the integral defect
at 3 exactly.

Tensor the maps by the Tate lattice $\mathbb Z_3(-e)$.
On the residue factors this twist is trivial, since
$L_0$ contains $\mu_3$. Shapiro and the local Mackey
decomposition identify the strict group for the regular
representation with $S_L(\mathbb Q_3/\mathbb Z_3(-e))$,
with the full local condition at 3 and the inertia
condition elsewhere. This is true even though the
relative degree is divisible by 3: Shapiro is induction,
not division by the group order. For the local inertia
condition, the restriction of the induced module is a
direct sum induced from the inertia subgroups of the
primes above it; each component of the local restriction
is the corresponding restriction after the Shapiro map.
For the full local condition the identical statement
uses decomposition groups. Thus the strict kernels
are exactly identified, as in the earlier coefficient note.

Write $D_\lambda=(\mathbb Q_3(\omega)/\mathcal O_3)(-e)
\otimes\lambda$ over $L_0$. The ramification set for both
lattices over $L_0$ consists only of places over 2 and 3,
since $K/F$ is unramified away from 6. Let
$S_{23}$ be this set, and put


```math
B_3=\dim_{\mathbb F_3}H^1(G_{L_0,S_{23}},\mathbb F_3).
```


Using (1) in both directions with the explicit isogenies
gives the precise inequalities


```math
\begin{aligned}
 \lambda_3(L,e)&\le
 \lambda_3(L_0,e)+\operatorname{length}_{\mathbb Z_3}S_{L_0}(D_\lambda)+B_3,\\
 \lambda_3(L_0,e)+\operatorname{length}_{\mathbb Z_3}S_{L_0}(D_\lambda)
   &\le \lambda_3(L,e)+2B_3.
\end{aligned}\tag{2}
```


There is no dependence of the error on $e$.

Choose a coefficient DVR $\mathcal O$ containing
$\omega$ and all $m$-th roots of unity, and denote by
$e_\mathcal O$ its absolute ramification index at 3.
The dyadic quotient $B'$ has order prime to 3, so the
exact character decomposition of the earlier coefficient
note applies over $F$. Base-changing the rank-two term
of (2) to $\mathcal O$ splits it over the fraction field,
but need not split its original integral lattice at 3.
To avoid assuming such a splitting, use the single
$\mathcal O_3$-rank-one module $D_\lambda$ directly:
extending scalars along $\mathcal O_3\to\mathcal O$
preserves normalized length by finite freeness.
Since $\mathcal O_3$ has residue degree one and
ramification index two,


```math
\operatorname{length}_{\mathbb Z_3}S_{L_0}(D_\lambda)
 =\frac{2}{e_\mathcal O}\sum_{\rho\in\widehat B'}
  \operatorname{length}_{\mathcal O}
   S_F((E_\mathcal O/\mathcal O)(-e)\otimes
                  \lambda(\rho^N)^{-1}). \tag{3}
```


Here the $\rho^N$ labels denote the actual norm-pullback
characters of $B'$, and inverse conventions follow from
restriction; changing all cubic labels by inversion
does not change the summed lengths by conjugation.
The factor 2 in (3) is the rank-two coefficient
normalization, not an assumption of an integral
cubic Fourier splitting. Extension of scalars commutes
with the cohomology and strict kernels, since the
integer extensions are finite free; it multiplies
the corresponding integral lengths by the relative
ramification index. This also verifies the factor
when the coefficient extension has nontrivial residue
degree.

### Explicit bound for the error

Kummer theory (the constant module $\mathbb F_3$
is identified with $\mu_3$ over $L_0$) gives an exact
sequence with the $S_{23}$-units modulo cubes and the
3-torsion of the $S_{23}$-class group. Thus, writing
$D_0=[L_0:\mathbb Q]$ and $h(L_0)$ for its class number,


```math
B_3\le D_0/2+|S_{23}|+\frac{\log h(L_0)}{\log3}.
```


Here the unit rank is $D_0/2-1+|S_{23}|$, with one
additional dimension for the root-of-unity torsion.
We have $|S_{23}|\le2D_0$.
For an elementary uniform class-number upper bound,
Minkowski gives a representative integral ideal of norm
at most $2^{D_0}\sqrt{|D_{L_0}|}$ in every class.
The count of integral ideals of norm at most $V$ is at
most $V^2\zeta_{L_0}(2)\le V^2\zeta(2)^{D_0}$,
by the Euler factors. In particular
$h(L_0)\le 8^{D_0}|D_{L_0}|$.
Since $L_0$ is a subfield of
$\mathbb Q(\mu_{3\cdot2^{h+2}qd})$, the discriminant
tower formula and cyclotomic root-discriminant
bound give
$\log\operatorname{rd}(L_0)\le\log(3\cdot2^{h+2}qd)$.
Combining,


```math
B_3=O(D_0(1+h+\log(qd))) \tag{4}
```


with an absolute implied constant. Thus the loss
in (2) is only polynomial in the actual source scales.
On windows $h=O(\log x)$, $\log(qd)\le x^{\epsilon/4}$,
$t\le x^{C_t}$, its weighted sum over $e<t$ is
polynomial in $x$ and fits any fixed exponential
allowance $\exp(x^\delta)$, $\delta>0$. This settles the
extra integral comparison error at 3, not the
sum of the new twisted lengths (3).

## 3. At 2: optional full diagonal comparison

Over the coefficient ring $\mathcal O$ containing $\mu_3$
and $\mu_m$ at 2, the order-three projector is integral.
Use its exact decomposition for $L/L_0$ first. For either
nontrivial cubic sector, Shapiro over $F$ gives the
regular $B'$-module tensored by the rank-one Tate/cubic
lattice. Compare it with the sum of its $m$ character
lattices via the integral Fourier matrix
$(\rho(g))_{\rho,g}$, and in reverse by
$(\rho(g)^{-1})_{g,\rho}$.
Their product is $mI$. The determinants have equal
valuation, because inversion merely permutes the
characters before transposition. Hence each cokernel
has $\mathcal O$-length
$\tfrac m2 v_\mathcal O(m)$, and is killed by $m$.
These are equivariant maps, not formal rational
decompositions.

Every residue-field composition factor of these
cokernels is the reduction of the fixed cubic
character (with inverse if that label is chosen).
The 2-power characters act trivially on such simple
factors in characteristic two, and the Tate twist is
also trivial modulo 2. Restriction to the fixed
field $K$ of degree three over $F$ is injective
on $H^1$ of each factor by inflation--restriction;
the coefficients become trivial there.
Let $S$ consist of the primes over $2,3,q,d$.
The dimension of $H^1(G_{K,S},\mathbb F_2)$ is at
most 17 by Kummer theory: $K$ has class number one
by the [class-number proof](cubic-two-primary-window.md),
unit rank two, one dimension for torsion, and at most
$1+1+6+6=14$ primes in $S$. Extending coefficients
to the residue field preserves that dimension.

Applying (1) in both directions and normalizing by
the ramification index of $\mathcal O$ at 2 gives


```math
\left|\lambda_2(L,e)-\lambda_2(L_0,e)
 -\frac2{e_\mathcal O}\sum_{\rho}
 \operatorname{length}_{\mathcal O}
 S_F((E_\mathcal O/\mathcal O)(-e)
                   \otimes\lambda(\rho^N)^{-1})
\right|
 \le17m\log_2 m. \tag{5}
```


In the formula, $e_\mathcal O$ is now at 2.
The two cubic sectors have equal lengths by
conjugation, as before. The formula is also
valid when $h=0$; no growing-order semisimplicity
is used at 2. The class-number result is for
the fixed $K$, not for the moving $L$.
The new error is again polynomial in the
actual source scales. For the main proof the
whole-group bound of the 2-primary common-window
theorem is simpler and should be preferred.

## 4. A limitation of residual comparison

Small residual dimensions cannot by themselves bound
the remaining 3-adic length in (3). For example take
$\mathcal O_3=\mathbb Z_3[\omega]$ and the finite
module $M_a=\mathcal O_3/(1-\omega)^a$, with
$C_3$ acting by multiplication by $\omega$.
Its fixed subgroup has $\mathcal O_3$-length one,
whereas $M_a$ has length $a$, arbitrarily large.
It also has a one-dimensional residue-field quotient.
Therefore neither bounded invariant length nor
bounded residual dimension implies a uniform
length bound for the full cubic character sector.
This is an explicit module obstruction, not an
example of an actual Selmer group violating its
desired bound.

The remaining new arithmetic input at 3 is a
bound for the genuine twisted groups in (3).
At odd primes outside 3 the earlier exact
decomposition applies. No new automorphic
deformation count or geometric divisor estimate
is inferred from these isogenies.

**Scope:** proved integral cohomological comparisons,
with the classical class-field/Kummer inputs and
the exact parent local Selmer condition. Not a new
kernel-checked Lean theorem or a bound on the
actual cubic odd-prime lengths.

The [exact field and lattice checker](../scripts/check_s3_field.py)
verifies the determinant-three evaluation matrix and integrality of
three times its inverse. See its
[recorded output](../certificates/s3-field-check.json).
