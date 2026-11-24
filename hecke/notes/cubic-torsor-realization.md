# Actual cubic torsors and normalized equivariant theta lines

24 November 2026. This constructs local Frobenius objects for the
cubic comparison without introducing the non-CM splitting field as
an endomorphism field. It also identifies a precise obstruction to
descending one of the parent's principal theta lines individually.
The global arithmetic inequality remains open: the local realization
below is not the required global theta/divisor map.

The [good-prime reduction](cubic-good-prime-comparison.md) permits
the new arithmetic supplier to use only first-power good primes.
We nevertheless verify the local Frobenius counts at ramified places
as well, since the original arithmetic balance includes them.

## 1. The actual degree-three coefficient torsor

Write $F=\mathbb Q(\omega)$, $K=F(\alpha)$,
$\alpha^3=2$, and choose the cyclic action with
$\sigma(\alpha)=\omega\alpha$.
Over $S=\operatorname{Spec}\mathcal O_F[1/6]$ the scheme


```math
\mathcal T=\operatorname{Spec}
 \bigl(\mathcal O_F[1/6][z]/(z^3-2)\bigr)
```


is a finite étale cyclic torsor of rank three: $z$ and
$3z^2$ are units, and its three geometric points are
$z_0,\omega z_0,\omega^2 z_0$. Its generic field is the
actual $K$. No assumption about the class group is needed.

At a good prime ideal $v$ of $F$, with $Q=Nv$, we have
$Q\equiv1\bmod3$. Arithmetic Frobenius permutes the three
points by


```math
z_0\longmapsto z_0^Q
 =2^{(Q-1)/3}z_0=\omega^{r_v}z_0 .
```


The last equation uses the image of $\omega$ in the
residue field. It supplies the actual cubic Frobenius
label $r_v$, with the Artin convention of the
[relative comparison](cubic-relative-comparison.md).
The integral permutation module on the three points,
with its ordinary orthonormal permutation basis, has


```math
\operatorname{Tr}(U^{-s}\operatorname{Fr}_v^j)
 =3\mathbf1_{j r_v=s}.
\tag{1}
```


This counts fixed basis points, not the dimension of
the fixed subspace of a cyclic permutation (the latter
would be one for a nontrivial cycle). Its Fourier
eigencharacters are the actual $1,\lambda,\lambda^{-1}$.
Projector denominators are exactly those already
discussed in the coefficient interface.

For the full relative field $L=K L_0$, use the finite flat
scheme $\operatorname{Spec}\mathcal O_L$ over
$\operatorname{Spec}\mathcal O_F$. Its geometric reduced
fiber at a finite prime $v$ consists of $|G/I_v|$ points.
They are the embeddings of the residue fields of the
primes over $v$ into a fixed algebraic closure of the
base residue field. The action of $G=\operatorname{Gal}(L/F)$
is transitive with stabilizer $I_v$. With the convention
that a group element acts by precomposition on an
embedding (a left action because $G$ is abelian),
arithmetic Frobenius acts by its lift $F_v$.
The fixed-point equalizer of $g^{-1}\operatorname{Fr}_v^j$
on the reduced fiber is the entire fiber if
$jF_v=g$ modulo $I_v$, and is empty otherwise. Therefore


```math
\#\operatorname{Fix}(g^{-1}\operatorname{Fr}_v^j)
 =|G/I_v|\mathbf1_{jF_v-g\in I_v}.
\tag{2}
```


This is exactly the relative arithmetic kernel,
including at ramified places. At such a place it is
the permutation representation on the inertia
quotient (equivalently the generic regular
representation's inertia invariants), not the
nonreduced special fiber with multiplicities.

Since the orders three and $|B'|$ are coprime,
every subgroup of $C_3\times B'$ is a product of
its two projections. Thus the cubic fixed-point
factor and the original abelian fixed-point factor
multiply exactly. At 2 and 3 the cubic inertia
is all of $C_3$ by the
[class-number and local field calculation](cubic-two-primary-window.md),
so the cubic factor there is one for every label.
The good-prime supplier does not need these bad
fibers, but (2) shows they have not been confused
with unramified degree-three fibers.

**Compatibility under base change.** Over a prime of
$L_0$ above $v$ of residue degree $f_0$, the cubic
Frobenius label is $f_0r_v$ modulo 3. Since
$[L_0:F]$ is a power of two, $f_0$ is invertible
modulo 3; the original label is recovered by
multiplying by its inverse. Thus keeping the
original CM host does not erase the cubic label.
At further coefficient fields of residue degree
divisible by three this recovery fails; one must
keep the lower-field label explicitly. Nor may
one replace the relative norm $Nv$ in the
arithmetic hinge by the norm of an upper prime.
These are actual compatibility requirements.

## 2. The cubic twist exists for the original CM action

Let $\mathcal A$ be a polarized abelian scheme over
an $S$-scheme, with an action of an order containing
$\mathbb Z[\omega]$ on which Rosati acts by complex
conjugation. In particular this applies to the
good-prime part of the proposed parent CM host,
which contains $F$. The action $U=[\omega]$ has
order three and preserves the polarization, since
$U^\dagger U=[\bar\omega\omega]=1$.

Pull back $\mathcal A$ along the cubic torsor.
Combine its natural descent data with $U^j$
for $j=0,1,2$. This is a descent cocycle:
the action commutes with the coefficient order,
and $U^3=1$. Effective finite étale descent
gives the twisted polarized abelian schemes
$\mathcal A_j$ of the same dimension and with
the same coefficient-order action. One may
use a polarization-compatible ample line
bundle to descend projectivity; equivalently
the étale-local product of the three translates
of an ample bundle has its canonical cyclic
linearization and is ample. The polarization
morphism itself descends by invariance. Thus
the non-CM field is only a field of definition
for an isomorphism, never an endomorphism field.

For a concrete elliptic model let


```math
E_j:y^2=x^3+2^{2j},\qquad j=0,1,2.
```


These are smooth elliptic schemes away from 6,
all with the order-three automorphism
$U(x,y)=(\omega x,y)$ and its positive canonical
principal polarization. The actual isomorphism


```math
\phi_j:E_0\longrightarrow E_j,\qquad
 (x,y)\longmapsto(\alpha^{2j}x,2^j y)
```


is defined over the torsor, integral at every
place away from 6, and preserves origins and
polarizations. It satisfies


```math
\sigma^k(\phi_j)=U^{2jk}\phi_j,\qquad
 \phi_j^*\left(\frac{dx}{2y}\right)
     =\alpha^{-j}\frac{dx}{2y}.
\tag{3}
```


Thus on the two CM eigenspaces of its Tate
module the two twists are inverse cubic
characters; for instance, when $U$ acts by
$\omega$ the multiplier is $\lambda^{2j}$
under the chosen Frobenius convention.
This is an actual algebraic realization of
the cubic character and its inverse, not
an assumption that an abstract character
is a CM endomorphism. The differential scale
in (3) is a unit at the good places, with
a fixed archimedean scale $2^{-j/3}$.
It must be retained when using differential
coordinates; it is not a new growing
parameter. At 2 and 3 no good-reduction
coordinate assertion is made.

## 3. An obstruction to one invariant principal theta line

There is a specific problem with directly twisting
the parent's individual nonvanishing theta section.
On $E_0$ the three nonzero points of order two are


```math
h_j=(-\omega^j,0),\qquad j=0,1,2.
```


They are permuted cyclically by $U$. For a degree-one
line bundle on an elliptic curve, the associated point
in $\operatorname{Pic}^1$ is unique. The line bundle
is symmetric precisely when that point is 2-torsion.
Consequently the only $U$-invariant symmetric
degree-one line bundle on $E_0$ is $\mathcal O([0])$.
Its one-dimensional section space consists of
multiples of a section vanishing at the identity.

In contrast, the parent's ordinary theta normalization
in
[theta-integral-frontier-type-prime-jets](../../notes/theta-integral-frontier-type-prime-jets.md)
uses a symmetric line $\mathcal O([h])$ for nonzero
2-torsion $h$, with section a formal unit at the
identity. No individual such line is $U$-invariant
in this j-zero model. This is an explicit obstruction
to simultaneous cubic equivariance and this *one-line*
normalization; it is not a refutation of a more
general theta construction.

There is an exact replacement.

**Theorem (equivariant theta family).** Over
$\mathcal O_F[1/6]$ put


```math
\mathscr L_j=\mathcal O([h_j]),\qquad
 \mathscr V=\mathscr L_0\oplus\mathscr L_1\oplus\mathscr L_2 .
```


Each $\mathscr L_j$ is relatively ample of degree one.
Give it the rigidification at the origin in which
its canonical divisor section $s_j$ has value one.
These sections are integral, and for every geometric
fiber they are units near the origin and span their
respective one-dimensional global section spaces.
Pullback by $U$ carries $\mathscr L_j$ with its
canonical section and rigidification to
$\mathscr L_{j-1}$ with the corresponding data.
The direct sum therefore has an actual cyclic
linearization, with normalized sections permuted
exactly. After the descent of §2 it gives a rank-three
vector bundle and equivariant normalized local
theta families on each of the twists, with
permutation Frobenius (1) on their labels.

**Proof.** Each $h_j$ is a disjoint section from
the origin at every prime away from 6, and its
divisor is Cartier on the smooth elliptic scheme.
The canonical divisor section is consequently
nowhere zero along the origin and is a unit in
the completion there. On every geometric fiber
Riemann--Roch in genus one gives $h^0=1$, $h^1=0$
for a degree-one line, and the section is nonzero.
Cohomology and base change therefore identify
the global section line with the base, generated
by $s_j$ (it also follows by evaluating at the
origin). The three pullback identities are
identities of Cartier divisors and their
canonical sections. They give cyclic coherence
without choosing a scalar root. Descent of the
direct sum and its maps is effective. The
geometric fibers are those of the original
three theta lines; descent changes the label
permutation by the cubic cocycle. QED.

Equip these lines at every complex embedding
with the transported invariant canonical theta
metrics, rigidified at the origin. The automorphism
$U$ is an isometry of the positive polarization.
The three metrics and their canonical sections
are transported into each other, so their
corresponding normalized section norms agree.
The orthogonal direct sum has unitary permutation
action. This proves an actual good-place
equivariance of the integral theta normalization.
It is not a new bound on any of the parent's
mixed derivatives in growing ranks.

More generally if a rigidified symmetric
principal line $\mathscr L$ on a polarized
abelian scheme has no invariant theta
characteristic, its three orbit lines form
the same equivariant direct-sum construction.
A symmetric invariant alternative is the line
$\bigotimes_{j=0}^2 U^{j*}\mathscr L\otimes
\mathscr L^{-2}$: each difference $U^{j*}\mathscr L/
\mathscr L$ lies in $\operatorname{Pic}^0[2]$,
so the displayed line is symmetric, represents
the same polarization, and is $U$-invariant.
The rigidification removes the scalar cocycle
ambiguity. But it need not have a section that
is a unit at the origin, as the explicit
elliptic obstruction shows. The orbit family
is the appropriate replacement when that
unit property is needed.

## 4. Exact preservation of the parent's scalar norm data

On the orbit family the old maps can always
be repeated on all three slots. For an integral
map $T$ of Hermitian lattices, repeat it as
$T\otimes I_3$ on an orthogonal sum with the
unitary permutation lattice. Its operator norm
is exactly that of $T$, each nonzero singular
value is repeated three times, and its finite
elementary divisors are repeated three times.
Thus per-rank determinant slopes of these
repeated maps are unchanged.

For a family $T_i$ with its fixed normalizers,
write $Q=\sum_iT_iT_i^*$, $M=\operatorname{Tr}Q$,
$D=\dim W$, and
$\Delta=\sum_i\|T_i^*T_i-I\|_{\rm HS}^2$.
The repeated family has


```math
Q'=Q\otimes I_3,\quad M'=3M,\quad D'=3D,\quad
 \Delta'=3\Delta .
```


In particular the centered relative target
energy $D\operatorname{Tr}(Q^2)/M^2-1$
is unchanged. This is an exact transfer of
the finite-dimensional part of the parent's
[centered energy argument](../../notes/centered-global-energy-reduction.md),
provided the original maps and metrics are
the actual ones. It cannot supply a
norm estimate for maps that mix different
cubic weight slots.

Indeed, repeating a map and postcomposing
by a permutation or a unitary cubic phase
does not change its local elementary
divisors. If the arithmetic weights are
constant in the cubic coordinate, summing
over that coordinate kills the cubic
characters by Fourier orthogonality:
$\sum_{r=0}^2\omega^r=\sum_{r=0}^2\omega^{2r}=0$.
The remaining arithmetic balance is purely
abelian. Thus an equivariant repeat of
the old construction, with no label-sensitive
coupling, cannot produce the new prime
discrepancy.

## 5. A literal local divisor realization for the good primes

The remaining good arithmetic expression
can already be realized by actual finite
lattice modifications, which isolates the
missing global bound. This is deliberately
only a local realization, not a disguised
claim about the parent's maps.

Fix one top order $a$, top label $t$ and
profile $w$ as in the good-prime comparison.
At a good prime ideal $v$ of $F$, with
Frobenius $g_v\in G$, put


```math
n_v=
 \begin{cases}
 \left\lfloor M(a/Nv-w_{g_v})_+\right\rfloor,&
                     g_v\notin\Phi,\\
 0,&g_v\in\Phi ,
 \end{cases}
```


where $M\ge1$ is an integer scale. At all
other primes put $n_v=0$. There are only
finitely many nonzero exponents. The
Frobenius selector in this definition is
the actual equalizer of §1 on the finite
étale fiber. On the rank-$|G|$ lattice
$V=\mathcal O_L$ over $\mathcal O_F$,
modify the local lattice at $v$ by
multiplication with $\mathfrak p_v^{n_v}$.
Equivalently take the global sublattice


```math
V'=\left(\prod_v\mathfrak p_v^{n_v}\right)V .
```


The relative colength is $|G|n_v$
at each modified place, because $V$
is locally free of rank $|G|$. The
formula of §1 gives the precise comparison


```math
0\le\mathcal A_{\rm good}
   -\frac1{Mf}\log\#(V/V')
 \le \frac{C}{M}\frac{a}{w_{\min}},
 \qquad w_{\min}=\min_g w_g .
\tag{4}
```


To prove the error bound, each floor loses
less than one, the active primes satisfy
$Nv\le a/w_{\min}$, and $|G|/f=2$.
The logarithmic sum of degree-one prime
ideals is $O(a/w_{\min})$ by the elementary
Chebyshev bound. This proves (4) with an
absolute constant, including the
normalization. All local integral
modifications are actual lattices on
the existing finite coefficient algebra.

For the candidate common thin weight
$w_*=b/\exp(x^{\epsilon/3})$ and thick
weights at least $b$, take
$b=\exp(x^\epsilon)$ and $a/b=x+O(1)$.
Then $w_{\min}=w_*$, and with $M=1$
the total normalized rounding error
after the usual step/translation
averages is


```math
O\left(\frac{x\exp(x^{\epsilon/3})}{b d_0}\right),
```


which is smaller than every fixed
negative power of $x$ when
$d_0\ge x^{-\epsilon}$ and $\epsilon>0$
is fixed. Thus elementary integer
rounding is not an intrinsic difficulty
for a replacement supplier with these
actual weights.

However the patch itself provides no
height saving: with any fixed common
archimedean metric the determinant
index of $V'$ records exactly the
local divisor just imposed. In ordinary
normalized Arakelov degree,
$\widehat{\deg}(V')=\widehat{\deg}(V)-
\log\#(V/V')/[F:\mathbb Q]$.
The inclusion map has norm one, but
does not bound the degree of its
source from below. This is why arbitrary
local modifications cannot prove the
desired estimate. They must arise
as divisibilities of a globally
controlled nonzero family of maps,
with the source and target lattices
and their metrics tied to the same
arithmetic data.

## 6. Next geometric obligation

The good-prime Frobenius selector,
the cubic twist of the polarized CM
family, and a compatible normalized
three-theta-line system are now actual
objects. Pure tensor duplication
preserves the old norm estimates but
cannot detect the cubic contribution.

The new required construction is a
global family of label-sensitive maps
between the descended orbit
coefficient bundles, with arithmetic
divisibilities producing (4) (or the
good-prime hinges directly), and the
parent's simultaneous nonvanishing,
degree, and period-norm bounds.
The good-prime reduction avoids
requiring a new ramified hinge formula,
but integral denominators and
geometry at 2 and 3 may still need
separate treatment. The source
theta chain and global Poincare
period maps are not identified with
this new family merely by their
common polarization or local
Frobenius labels.

No such global family or quantitative
bound is proved here. This is a
construction of the local coefficient
geometry and a precise next
compatibility target, not closure
of the S3 benchmark or H07F.
