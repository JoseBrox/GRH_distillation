# The cubic frame: local dimensions, rigidity at the diagonal and corner vanishing

24 November 2026. This extends the [polarized integral cubic
model](cubic-polarized-selmer-model.md) by three actual arithmetic
suppliers from the parent deformation argument. It does not
establish finite characteristic-prime rings, automorphy of all
their points or the uniform lengths of the adjacent cubic groups.

## 1. Exact cohomological count in the high-dyadic range

Use the notation of the polarized model, with coefficient prime
$\ell\ge5$, residue field $k$, $a=\varepsilon^e\rho^N$ and diagonal
$(a\lambda^{-1},1,a^{-1}\lambda^{-1})$ over $F$.
Here $e\ge1$ and $2^b>8\ell^2$ is the exact high-dyadic conductor
condition. Use the fixed-determinant adjoint, namely trace-zero
matrices. Its weights for the torus $\operatorname{diag}(t,1,t^{-1})$
are denoted $W_j$ after reduction to $k$.
At infinity complex conjugation acts by negative reversing transpose.
Consequently the dimensions $n_j=\dim W_j$ and
$c_j=\dim W_j^{c=1}$ are

| $j$ | -2 | -1 | 0 | 1 | 2 |
| --- | --- | --- | --- | --- | --- |
| $n_j$ | 1 | 2 | 2 | 2 | 1 |
| $c_j$ | 0 | 1 | 1 | 1 | 0 |

Indeed the diagonal trace-zero space has $c$-fixed line
$\operatorname{diag}(u,0,-u)$, each adjacent pair is exchanged
with negative sign and the two corner lines have sign minus.
Without the fixed determinant one simply adds a diagonal
sign-minus line; the final defect below is unchanged.

Let $\Gamma=G_{\mathbb Q,S}$ for $S$ containing the primes
dividing $6N\ell$ and infinity. At each finite $v\ne\ell$ take
the inertia kernel $N_v$ of the residual base representation
(including its component sign). It is normal in inertia and
of index prime to $\ell$, because the finite inertia image has
order supported only at 2 and 3. On $N_v$ the adjoint is trivial.
Thus the local cohomology classes satisfying the infinitesimal
kernel condition are exactly the unramified classes:
vanishing on $N_v$ reduces the inertia cocycle to one on a finite
group of order prime to $\ell$, where its cohomology vanishes.
The converse follows by adjusting a representative by a
coboundary, which also vanishes on $N_v$.

Write $L_v=H^1_{\rm ur}(\mathbb Q_v,W_j)$ for $v\ne\ell$.
At $\ell$ take zero local classes for negative weights,
unramified classes for weight zero and all local classes for
positive weights. These are the weightwise first-order conditions
for the marked ordinary model: after a local conjugation the
flag is fixed, its inertia diagonal characters are fixed, and
its upper triangular deformation entries are free. The conjugate
local conditions agree by polarization. This identifies the
local classes, not a claim that the complete ring has no further
obstructions.

The high-dyadic mark in the polarized model has
$\bar\varepsilon(x)=1$ and three distinct residual eigenvalues,
so every nonzero-weight module and its Tate dual have no
invariants at $\ell$. By local duality its $H^2$ is zero there.
The global dual invariants in weight zero vanish too:
over $F$ the diagonal action is trivial and
$\bar\varepsilon|_{G_F}$ is nontrivial, since $F$ has discriminant
$-3$ and $\ell\ge5$. The global invariants in weight zero have
dimension $c_0=1$.

Use precisely the relative obstruction complex from the
[parent high-dyadic frame](../../paper/shared/rh-dyadic-host-frame.tex)
(DH4--DH5). Its relative obstruction space $\mathrm{Ob}_j$ fits
into the short exact sequence with outer terms

* the cokernel of $H^1(\Gamma,W_j)\to
  \bigoplus_{v\in S,\ v<\infty}H^1(\mathbb Q_v,W_j)/L_v$;
* the kernel of $H^2(\Gamma,W_j)\to
  \bigoplus_{v\in S,\ v<\infty}H^2(\mathbb Q_v,W_j)$.

This follows by taking a global two-cocycle with local primitives,
modulo global coboundaries and allowed local one-cocycles, exactly
as in DH5. Poitou--Tate gives surjectivity of the last $H^2$
map by the vanishing of global dual invariants above. The
Euler-characteristic identity gives the exact defect


```math
\dim H^1_L-\dim\mathrm{Ob}_j
=h^1-h^2-\sum_{v\in S,\ v<\infty}
  (h^1_v-h^2_v-\dim L_v).
```


Here $h^1-h^2=h^0+n_j-c_j$. At $v\ne\ell$ the local summand
vanishes by $\dim H^1_{\rm ur}=h^0_v$ and the local Euler
characteristic. At $\ell$ the local term is $n_j$ for $j<0$
and zero for $j>0$, by the local invariant and $H^2$ vanishings;
for $j=0$ it is $n_0$ because $L_\ell$ is unramified.
Thus the five defects in order $j=-2,-1,0,1,2$ are exactly


```math
(0,-1,0,1,1).
```


These are the parent's numerical relative dimensions, now
verified for the genuine nonabelian cubic adjacent modules.
This is not an assertion that the parent universal ring
represents this new problem.

## 2. Rational rigidity of the nonpositive-weight distinguished data

Restrict a characteristic-zero class in a negative weight to a
finite normal extension killing the finite characters, including
the quadratic sign and the cubic character. Over that field
the module is a sum of negative cyclotomic twists. The class
is unramified outside the coefficient prime and is zero in full
local cohomology at that prime. The parent's
[negative-weight rigidity proposition](../../paper/shared/selmer-negative-weight-rigidity.tex)
therefore makes it a coboundary. Restriction is injective in
characteristic zero by corestriction, even if the extension
degree is divisible by the coefficient prime. This proves the
negative-weight vanishing on the new model itself. For weight
zero the restriction is a trivial module, with unramified
classes everywhere. The finite ideal class group makes its
characteristic-zero additive cohomology zero.
These proofs use a finite extension for cohomological
restriction only, not a claim that this extension is CM.
They do not erase integral torsion or bound its length.

The parent Cl1 class-number input also holds for the
multiplier-one subgroup: it is the absolute group over the
Eisenstein field $F$, whose class number is one.
A locally constant additive character trivial on all finite
inertia factors through its trivial ideal class group.

## 3. An actual residual corner vanishing

The negative corner line $W_{-2}$, unlike the adjacent pair,
is a rational Dirichlet character. With
$\eta=\chi_{-3}$, it is


```math
\gamma=\eta\,\bar\varepsilon^{-2e}\bar\rho^{-2}.
```


The auxiliary odd quadratic factors disappear when squared.
The odd part has primitive conductor $f\mid 3\ell$ and its order
divides $\ell-1$. The dyadic part is the square of the primitive
dyadic character of conductor $2^b$; for $b\ge4$ its exact
conductor is $2^{b-1}$, by the cyclic group generated by 5.
The product is odd, since the other factors are squares.

Take $d=\operatorname{ord}_4(\ell)$ and $h=v_2(\ell^d-1)$.
The order of the odd part divides $\ell^d-1$. The
[parent Bernoulli-unit and cocycle theorem](../../paper/shared/selmer-dyadic-twist-vanishing.tex)
applies provided $f4^h\le2^{b-1}$.
In particular the sufficient uniform threshold


```math
2^b\ge24\ell(\ell+1)^2
```


works: for $\ell\equiv1\bmod4$ one has
$2^h\le\ell-1$, and otherwise
$2^h=2\cdot 2^{v_2(\ell+1)}\le2(\ell+1)$.
This is independent of the moving odd quadratic auxiliary
conductors. To apply the actual cocycle corollary, a strict
negative-corner class vanishes on $N_v$ at every $v\ne\ell$,
where $N_v$ has prime-to-$\ell$ index in inertia, and its
localization at $\ell$ is a coboundary. That coboundary
vanishes on the kernel of $\gamma$ in inertia. All the
corollary's relative-index hypotheses therefore hold.
It follows that $H^1_L(\Gamma,W_{-2})=0$ in this range.

This removes the residual negative corner obstruction
under an explicit higher conductor threshold. It is not
vanishing of either adjacent cubic component. Those are
precisely the nonabelian terms that the desired length
estimate must control.

## 4. Remaining arithmetic supply

In the high-dyadic range the ordinary flags also give the
parent's potentially crystalline local alternative at
characteristic-zero points with the prescribed integral
inertia type. Indeed the three exponents are $e,0,-e$.
Work over the original coefficient-prime local field of $F$,
before killing the finite inertia characters. The diagonal
characters are potentially crystalline (each is a cyclotomic
power times a finite inertia type and an unramified character).
The ordered upper-root extension modules have negative
Hodge--Tate weights with the convention of the parent.
For exponent difference one, equality of the whole ratio
with $\varepsilon$ is excluded by the three distinct
residual values at the mark, where $\bar\varepsilon(x)=1$;
for larger difference the infinite cyclotomic inertia
already excludes equality. The local Euler-characteristic
and Bloch--Kato dimension argument of the parent DH7 gives
finite extension classes, by induction on the flag: the
dual Tate twist has no invariants since none of its
successive characters is trivial. These assertions are
checked over the original local field, not by assuming
the mark survives a further restriction. Restrict the
resulting finite classes to a finite extension where
the diagonal characters are crystalline. Induction
using the crystalline extension criterion gives
potential crystallinity with the prescribed finite
inertia semisimplification. This is a
local assertion, and supplies no global automorphic
attachment.

Together with the integral conormal injection in the
polarized model, the exact dimensions and diagonal
rigidity above permit an attack on the parent's graded
presentation/counting argument using the new ring.
One must still establish the actual characteristic-prime
finite-ring estimate and the required point shape,
automorphy, and cubic cross-block finite Selmer vanishing.
The conditional fixed-field Frobenius polynomial count is
already available in that model. No uniform bound on the
adjacent cubic integral length follows yet from these
rational and residual vanishing statements alone.

## Subsequent use of the residual corner vanishing

The [corner-elimination theorem](cubic-corner-elimination.md)
uses this residual vanishing to exclude every two-sided reducible
point under the stated threshold in both characteristics. The
[actual homogeneous relation count](cubic-high-dyadic-presentation.md)
removes the negative-corner generator and equation and gives the
single irreducible curve criterion. The high-dyadic conditional
length comparison no longer needs cross-block finite Selmer vanishing.
