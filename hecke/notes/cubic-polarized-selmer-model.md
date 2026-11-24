# The polarized rank-three arithmetic model for the new cubic Selmer sectors

24 November 2026. **Actual integral model and conditional quantitative
spectrum supplier.** This constructs a new polarized ordinary frame
for the two cubic characters at coefficient primes at least five.
The old rational-character frame cannot simply be twisted by a
common scalar: that cancels in the adjoint. The two new coefficients
occur in adjacent lower roots of the new model. Their strict torsion
has an integral first-order realization, and the large-conductor
local marks, strong irreducibility and fixed-field spectral count
have the requisite polynomial bounds.

The global automorphy/finite-ring/rigidity comparison producing the
actual one-character length estimate is still missing. In particular
this note does not assert that the original OneChar theorem applies
to nonabelian finite inertia.

## 1. Actual polarized diagonal and its two cubic roots

Keep $F=\mathbb Q(\omega)$ and $K=F(\sqrt[3]2)$, with the finite
cubic character $\lambda$ of $G_F$ of conductor dividing $6\mathcal O_F$.
Fix $e\ge1$, an actual host character $\rho=\rho_2\rho_o$ of
power-of-two order over $\mathbb Q$, with $\rho_o$ quadratic or
trivial of odd conductor, and modulus $N$ divisible by its conductor.
Write $\rho^N$ for its restriction to $G_F$ (norm pullback).
Fix a coefficient prime $\ell\ge5$, a coefficient DVR $\mathcal O$
containing the character values, its fraction field $E$, uniformizer
$\pi$, and residue field $k$. Let $\varepsilon$ be the $\ell$-adic
cyclotomic character and put


```math
a=\varepsilon^e\rho^N,\qquad
 \chi_1=a\lambda^{-1},\qquad
 \chi_2=1,\qquad
 \chi_3=a^{-1}\lambda^{-1}.
```


For the desired negative-twist module use


```math
D=(E/\mathcal O)(a^{-1}\lambda).
```


This is precisely one of the new coefficient modules of the
[exact Selmer decomposition](cubic-coefficient-interface.md);
complex conjugation exchanges it with the other one.

Let $J_3$ be the reversing matrix, and let the nontrivial element
of $C_2$ act on $\mathrm{GL}_3$ by
$A\mapsto J_3A^{-\mathsf t}J_3$.
Define the diagonal on $G_F$ by


```math
r_0=\operatorname{diag}(\chi_1,1,\chi_3),
```


and on a fixed complex conjugation $c$ put
$r_0(c)=(I,-1)$ in the semidirect group.
Because $a^c=a$ and $\lambda^c=\lambda^{-1}$,


```math
r_0(cgc^{-1})=J_3r_0(g)^{-\mathsf t}J_3 .
 \tag{1}
```


This constructs a representation of $G_\mathbb Q$, not merely
a choice of three formal diagonal weights. Its determinant on
$G_F$ is the finite character $\lambda^{-2}$.
Its adjoint on $M_3$ has conjugation action of $G_F$ and
$c:X\mapsto-J_3X^\mathsf t J_3$.

For the lower adjacent roots, put
$W_-=\mathcal O E_{21}\oplus\mathcal O E_{32}$.
Their characters on $G_F$ are respectively
$a^{-1}\lambda$ and $a^{-1}\lambda^{-1}$.
Complex conjugation interchanges the two root vectors with
a negative sign. Thus $W_-$ is exactly the induced rank-two
lattice


```math
W_-\simeq\operatorname{Ind}_{G_F}^{G_\mathbb Q}
                 \mathcal O(a^{-1}\lambda),
 \tag{2}
```


with the second coset basis chosen as $-E_{32}$.
The two opposite corner roots have characters $a^{\pm2}$,
so the fixed cubic factor cancels there, not in the adjacent
roots. This is the precise new adjoint dictionary.
All remaining root spaces and the diagonal form a
$G_\mathbb Q$-stable complementary summand.

## 2. The full local conditions and the arithmetic marks

The following two ranges give a separating mark at every
prime above $\ell$:

* the nonresonant range $\ell-1\nmid 2e$;
* the high-dyadic range where $\rho_2$ has exact conductor
  $2^b>8\ell^2$.

We give the checks separately. The second range works even
if a quadratic odd factor is ramified at $\ell$, although
this does not establish every original geometric condition
at such a prime.

At $\ell\ge5$, $F$ is unramified and $\lambda$ is unramified.
The residual cyclotomic character is surjective on inertia
onto $\mathbb F_\ell^\times$, while the odd-conductor
part of $\rho$ has inertia order at most two there.
In the nonresonant range one can choose an inertia element
$x$ with $\bar a(x)^2\ne1$.
Here $\lambda(x)=1$. The three residual diagonal
eigenvalues at $x$ are pairwise distinct.

In the high-dyadic range use an arithmetic Frobenius lift
at a prime $v\mid\ell$ of $F$, adjusted by inertia to have
$\bar\varepsilon(x)=1$ (local cyclotomic surjectivity allows
this). If $f_v\in\{1,2\}$ is the residue degree,
$\rho_2(x)=\rho_2(\ell^{f_v})$. As in the parent
[large-dyadic frame](../../paper/shared/rh-dyadic-host-frame.tex),
the inequality $2^b>8\ell^2$ gives
$\rho_2(\ell)^4\ne1$: indeed
$v_2(\ell^4-1)=v_2(\ell^2-1)+1$, and a primitive
dyadic character is faithful on $1+4\mathbb Z/2^b\mathbb Z$.
The odd quadratic factor cannot alter the square, and
reduction is injective on these prime-to-$\ell$ roots.
Thus $\bar a(x)^2\ne1$.
The cubic factor cannot cancel the nontrivial 2-power
factor. Consequently


```math
\bar\chi_1(x),\quad 1,\quad\bar\chi_3(x)
       \text{ are distinct},\qquad \bar\varepsilon(x)=1 .
 \tag{3}
```


In this second range every nonzero root has nontrivial
residual action on $x$, and so does its Tate dual.
Local duality therefore gives the $H^0$ and $H^2$
vanishings for those root modules at the coefficient
prime. In the first range the separating mark alone
does not imply the Tate-dual vanishing at exponent one.

**Integral strict torsion.** In both ranges, for every
$r\ge1$ the map $H^1(F,D[\pi^r])\to H^1(F,D)$
identifies the strict subgroup on the left with the
$\pi^r$-torsion of the strict subgroup on the right.

Here are all the local kernel checks. On inertia above
2 and 3 the cubic character is nontrivial of order three
(the totally ramified relative prime calculation in the
[2-primary theorem](cubic-two-primary-window.md)).
The other finite factor has 2-power order, and the Tate
character is unramified there. The resulting residual
character is nontrivial. This also proves $D^{G_F}=0$.
At any other inertia away from $\ell$ the integral
character has prime-to-$\ell$ finite order: if nontrivial
it has nontrivial reduction and zero invariants; if
trivial the invariants are all of $D$ and are divisible
by $\pi^r$. At the full decomposition groups above
$\ell$, the marks just constructed give a nontrivial
residual target character. Thus their invariants are
zero. For each relevant group $H$ the connecting map
from $D^H/\pi^rD^H$ in the cohomology sequence is zero,
so restriction into the full module is injective.
Globally the image is exactly the killed-by-$\pi^r$
cohomology. Taking the strict localization kernels
now proves the claimed identification, including the
full decomposition condition at $\ell$.

## 3. An actual integral normalized first-order model

Write $A_r=\mathcal O\oplus(\mathcal O/\pi^r)\epsilon_0$,
where $\epsilon_0^2=0$. By Shapiro with its local Mackey
decomposition, (2) gives an exact identification of
strict $H^1$ for the lower root pair over $\mathbb Q$
with the strict group over $F$ for $D[\pi^r]$.
For the full local condition the restriction of the
induced module is the direct sum of the induced local
modules at the places of $F$ above the rational place.
The same double-coset argument on inertia gives the
unramified condition. This is also checked in the
[coefficient interface](cubic-coefficient-interface.md).
Since the root pair is a direct summand, its cohomology
injects into that of the full polarized adjoint.

A cocycle $u$ in this root pair gives the actual
representation $(I+\epsilon_0 u(g))r_0(g)$
over the square-zero algebra, with the specified
semidirect action on the other coset. The cocycle law
is exactly the multiplication law, as the square of
the ideal is zero. On every distinguished local
group where the strict restriction is zero, this
representation is conjugate to the diagonal by a
square-zero conjugator. In particular it satisfies
the literal ordinary flag and its prescribed inertia
characters at $\ell$, and the prescribed kernel of
finite inertia at all other primes.

One can normalize these representations integrally,
with the same type of mark as the parent rank-three
construction. First take $u(c)=0$ by a coboundary,
using that 2 is invertible. Residual distinctness
at the mark $x$ makes


```math
d=\chi_1(x)-\chi_3(x)
    =\lambda(x)^{-1}(a(x)-a(x)^{-1})
 \quad\text{a unit in }\mathcal O .
```


For the normalized polarization,
$r(x^*)=J_3r(x)^\mathsf tJ_3$, where $x^*=cx^{-1}c$.
At the basepoint the difference is $dT_0$ with
$T_0=\operatorname{diag}(1,0,-1)$.
Conjugation by
$I+\epsilon_0 t(E_{21}-E_{32})$ keeps $r(c)=(I,-1)$
and changes the lower adjacent entry of this
difference by $\epsilon_0 t d$, since
$[E_{21}-E_{32},T_0]=E_{21}-E_{32}$.
There is a unique $t$ in $\mathcal O/\pi^r$
killing that entry. The other lower adjacent
entry is then its negative and is zero as well.
The upper adjacent entries were zero already.
This gives a normalized representative for each
strict cohomology class, with no division by a
nonunit and with the modulus $r$ retained.
The only residual freedom in a lower-root coboundary
preserving $c$ is the displayed one-dimensional
fixed line, so two representatives normalized
this way are equal if they are cohomologous in
the lower root module.

For precision, a new framed ordinary deformation
ring $R$ realizing these conditions can be constructed
over $\mathcal O$. Take $G_{\mathbb Q,S}$ with $S$
the primes dividing $6N\ell$ and infinity.
Its open residual kernel has topologically finitely
generated maximal pro-$\ell$ quotient, by finiteness
of its first cohomology with $\mathbb F_\ell$
coefficients. The kernel of this quotient is
characteristic, hence normal in the full group.
Every residual deformation factors through the
resulting finitely generated profinite quotient,
as seen on successive finite coefficient quotients.
Use matrices on its topological generators and
impose the closed group relation ideal, fixed
sign/polarization, determinant $\lambda^{-2}$ on
$G_F$, $r(c)=(I,-1)$, and the displayed adjacent
mark equations. Away from $\ell$ kill the inertia
subgroups in the kernel of the residual diagonal
on $G_F$; their index in inertia on $G_F$ is
prime to $\ell$ and equals the index for the
integral finite inertia characters.

At each prime of $F$ over $\ell$ use the Hensel
eigenvalues of a separating local element
as above. The differences are units. Their
spectral projectors and normalized ordered
eigenvectors exist over every complete local
coefficient algebra; an invariant flag of
the indicated residual order is necessarily
the flag of these eigenvectors. Impose the
vanishing of the forbidden lower matrix
entries and the exact inertia character
equations in these coordinates. These are
closed equations in the completed matrix
ring, with all denominator factors units.
They represent the stated condition even
on rings with coefficient torsion.
At conjugate primes use the transported
conditions. This construction supplies an
augmentation $R\to\mathcal O$ given by $r_0$.

Write $\mathfrak p$ for the augmentation ideal.
The square-zero representatives just constructed
give an $\mathcal O$-linear injection


```math
S_F(D)[\pi^r]\hookrightarrow
 \operatorname{Hom}_{\mathcal O}
    (\mathfrak p/\mathfrak p^2,\mathcal O/\pi^r).
 \tag{4}
```


More precisely its image lies in the lower
adjacent root derivations. The torus
$\operatorname{diag}(t,1,t^{-1})$ commutes
with the prescribed normalization and
preserves the equations, and these
derivations have the corresponding
single root weight. Equation (4) holds for
every finite modulus on this actual new
ring. It is not an assertion that its
conormal module is torsion, or that the
source's original ring with a single
rational compensated character equals $R$.

## 4. Strong irreducibility at irreducible characteristic-zero points

We can transfer the strong irreducibility part of the
parent [type-I theorem](../../paper/shared/selmer-support-continuation-type-one-rigidity.tex)
without the former special reciprocal residual trace.

**Lemma.** An absolutely irreducible characteristic-zero
rank-three point of $R$ restricted to $G_F$ remains
irreducible on every open subgroup and on the kernel of
the cyclotomic character after any finite extension of
$F$.

**Proof.** On an open normal subgroup, Clifford theory
in prime dimension three permits either scalar action
or three lines permuted transitively, if the restriction
is reducible. The inertia characters at $\ell$ have
cyclotomic exponents $e,0,-e$ times finite characters.
Inside every given open normal subgroup there is an
inertia element whose finite characters are trivial
and whose cyclotomic value has infinite order. It
has three distinct eigenvalues, excluding scalar
action. In the three-line case these lines are
precisely its eigenspaces. The ordinary local flag
is their ordered flag, so the local decomposition
group fixes the three lines individually.

Choose a global element $g$ permuting the three
lines as a 3-cycle. For the separating mark $x$
the trace of $r(gx^m)$ is zero for $m=0,1,2$,
since $x$ fixes each line. Reduction gives


```math
\sum_{i=1}^3\bar\chi_i(g)\bar\chi_i(x)^m=0,
                  \qquad m=0,1,2 .
```


The Vandermonde determinant of the three distinct
$\bar\chi_i(x)$ is nonzero in $k$, so all three
coefficients $\bar\chi_i(g)$ would be zero.
They are units, a contradiction. This works for
the new cubic residual diagonal without any
reciprocal trace identity.

The connected component of the Zariski closure
acts irreducibly because its inverse image has
finite index. Its unipotent radical has fixed
vectors and is normal, so acts trivially.
The component is reductive and its connected
center acts by scalars. Its derived group
therefore acts irreducibly as well.
The closure of the image of the commutator
subgroup contains this derived group.
The cyclotomic quotient is abelian and its
kernel contains the commutator subgroup.
Applying this argument after any finite
extension gives the final assertion. QED.

Thus for a point with the required automorphic
attachment, the irreducibility hypothesis in
Thorne's adjoint Bloch–Kato vanishing theorem
can be verified just as in the parent program.
The attachment of all points of the new ring
has not been proved. In particular one cannot
trivialize $\lambda$ in a finite CM auxiliary
extension of $F$: it would contain $K$, contrary
to the proved CM obstruction.

## 5. The reducible outer block and the genuinely new rigidity group

Suppose a characteristic-zero point has the outer
rank-two block $A$ and a middle line $d_0$ (the
parent's type-II shape). We do not claim here
that every reducible point has this shape.

At a coefficient-prime place the marked flag gives
the middle inertia character one and outer
determinant $\lambda^{-2}$ on inertia.
At all other places inertia factors through
the same finite prime-to-$\ell$ quotient as
the residual diagonal. Since the representation
is integral, reduction detects its finite
one-dimensional characters of that order.
It follows that $d_0$ and $\lambda^2\det A$
are everywhere unramified characters of $F$.
The class number of $F$ is one; hence


```math
d_0=1,\qquad \det A=\lambda^{-2}.
```


Put $W_F=\lambda A$. It has determinant one,
and the polarization gives
$W_F^c=J_2W_F^{-\mathsf t}J_2=CW_FC$,
where $C=\operatorname{diag}(-1,1)$.
The last equality is the elementary
determinant-one two-by-two matrix identity.
Thus $W_F$ extends to $G_\mathbb Q$ by
$W(c)=C$, with determinant $\chi_{-3}$.
This retains the rank-two extension mechanism
of the parent type-II proof, but now the
outer block is $\lambda^{-1}W_F$, not $W_F$.

If the outer block is absolutely irreducible,
its strong irreducibility follows by the same
Clifford and local-mark argument in dimension
two: use the two distinct residual outer
eigenvalues at $x$ and the trace equations
at $g$ and $gx$ for a transposition of
the two lines. Their two-by-two Vandermonde
matrix is invertible. The Tate-weight and
connected-monodromy arguments are identical.

The cross-block adjoint terms over $F$ now
carry $W_F\otimes\lambda^{\pm1}$ (using
$\det W_F=1$ to identify its dual).
The corresponding polarized cross-block
cohomology over $\mathbb Q$ is the induced
cohomology, i.e. the nonabelian twist by the
standard $S_3$ representation. This is
not the rational modular-form twist to
which the parent applies Kato's theorem.

Even assuming modularity of $W$ in the
parent's weight $2e+1$, one needs the
Bloch–Kato finite Selmer vanishing for
these cubic twists (with the actual local
conditions). The Rankin–Selberg formulation
uses the weight-one dihedral theta series
of $\lambda$ and the weight-$2e+1$ newform.
The known Beilinson–Flach theorems have
additional hypotheses (e.g. local regularity,
ordinary/eigenvalue and image conditions);
they cannot be invoked at every coefficient
prime solely from the separating mark.
In particular at a split-completely prime
the weight-one Frobenius has repeated
eigenvalue one. The parent Kato input is
not a proof of this new cross-block
vanishing. This is a precise new rigidity
obligation, in addition to constructing
the required global point families.

## 6. The quantitative spectrum does extend, once the actual point comparison is available

The parent's
[fixed-field Frobenius spectrum theorem](../../paper/shared/selmer-support-continuation-spectrum.tex)
counts representations over a fixed imaginary quadratic
field. We can retain its counting and integral resultant
argument for the following explicit new classes.

Class I consists of rank-three points whose restriction
to $F$ is absolutely irreducible and whose
$r\varepsilon^{-1}$ is attached, in the parent
normalization, to a regular algebraic conjugate
self-dual cuspidal representation of GL3/F.
Class II consists of the outer-block points of Section 5
whose $W\varepsilon^{-e}$ is attached to a normalized
classical newform of weight $2e+1$.
For both classes require the just-specified finite
inertia and ordinary conditions. At coefficient-prime
places require potential crystallinity or the parent
nonresonance alternative (no whole-character ratio
of successive diagonal characters equals
$\varepsilon$). This alternative is automatic
from the high-dyadic mark (3): the residual ratios
are nontrivial at $x$ while $\bar\varepsilon(x)=1$.
For $e\ge2$ it follows from the distinct differences
of the cyclotomic Hodge–Tate exponents.

The proof of the parent conductor bound SP7--SP9
then applies to these classes with a fixed
enlargement of the modulus. The only modification
is to its finite-character conductor argument:
the local finite inertia characters are products
of $\lambda^{\pm1}$ of conductor dividing
$6\mathcal O_F$ and norm-pullbacks of characters
of modulus $N$. Their products have conductor
dividing $6N\mathcal O_F$ by local reciprocity.
For coefficient-prime ordinary flags the
parent's de Rham dimension and local-duality
argument makes their extensions potentially
crystalline under the stated whole-character
alternative. The finite Weil–Deligne inertia
characters are exactly those in the flag.
Thus the Artin conductor of Class I divides
$(6N)^3\mathcal O_F$.
Full local–global compatibility and the local
newvector theorem give the same principal
counting level with $6N$ in place of $N$.

For Class II, $W_F$ similarly has conductor
dividing $(6N)^2\mathcal O_F$ (multiplication
by $\lambda$ cancels the prescribed cubic
inertia). The induction conductor formula
for $W\oplus W\otimes\chi_{-3}
=\operatorname{Ind}_{G_F}^{G_\mathbb Q}W_F$
gives the coarse rational conductor bound
$3^2(6N)^4$ for $W$; any larger fixed
polynomial modulus also suffices.
This formula applies to local Weil–Deligne
representations, including at the coefficient
prime, since the potential-crystalline or
whole-character condition has already been
checked over $F$ and passes to the finite
restriction. The outer-block newform has
level dividing that integer.

Fix a rational prime $p\ge7$ not dividing
$6N$, a prime $v\mid p$ of $F$, and put
$Q=Nv=p^f$, $f\le2$. The parent's
Borel–Serre cellular argument counts the
Class I automorphic representations by
$O_F((6N)^{54}(e+1)^6)$, retaining the
same highest weights $(e-1,0,1-e)$ at
both embeddings. Its classical modular
curve dimension bound counts Class II
by another fixed polynomial in $N(e+1)$.
The Galois-stable multiset of traces includes
multiplicities. For Class I use the parent's
trace normalization. For Class II take


```math
\alpha_g=
  1+\lambda(\operatorname{Frob}_v^{-1})^{-1}
           p^{-ef}(\beta_1^f+\beta_2^f),
```


where $\beta_i$ are the good-prime roots
of the weight-$2e+1$ newform polynomial.
For Galois stability include both cubic
conjugates in the indexing if necessary.
Exactly as in the parent proof, every
trace has all complex absolute values
at most three and $Q^e$ times it is an
algebraic integer. For the new class II
the extra root of unity changes neither
fact. Class I uses the same temperedness
and weak-admissibility argument.
This constructs a common multiset
of polynomial cardinality independently
of the coefficient prime $\ell\ne p$.

At the diagonal the corresponding trace is


```math
T_0=1+\lambda(\operatorname{Frob}_v^{-1})^{-1}
                    (Q^{-e}z+Q^ez^{-1}),
```


where $z=\rho^N(\operatorname{Frob}_v^{-1})$.
For every Galois conjugate,
$|T_0|\ge Q^e-Q^{-e}-1>3$.
Hence it is unequal to every trace in
the admissible multiset, including all
cubic conjugates. Multiplying differences
by $Q^e$ makes them algebraic integers.
Take the product over the multiset and
over all actual host character labels
and their scalar conjugates, allowing
both cubic signs. This product is a
nonzero rational integer $B_p$ with


```math
\log|B_p|\le C_F [N(e+1)]^A\log p
 \tag{5}
```


for some fixed $C_F,A$. Indeed the number
of host characters and scalar-conjugate
labels is polynomial in $N$ and every
factor has complex absolute value bounded
by $Q^e(3+1+Q^e+Q^{-e})$. The trace
multisets retain all repeated values and
each indexed representation is counted
once, as in the parent's SP6.

Consequently **if** the new integral
deformation argument supplies the actual
one-character length comparison


```math
\frac{\operatorname{length}_\mathcal O S_F(D)}{e_\mathcal O}
 \le C\sum_{r_i\in X}
     v_\ell\bigl(\operatorname{tr}r_i(\operatorname{Frob}_v^{-1})
                                                -T_0\bigr)
 \tag{6}
```


with $e_\mathcal O=v_\mathcal O(\ell)$,
a family $X$ of pairwise nonisomorphic
representations of the above classes and
a fixed $C$, then the full sum over
the coefficient primes and the indicated
character labels is bounded by the same
polynomial (5). Indeed every term is a
nonnegative normalized valuation of a
factor of $B_p$ (the multiplier $Q^e$
is an $\ell$-unit). Count the labels
with multiplicity in the product so
that the sum of all these valuations
is bounded by $v_\ell(B_p)$.
Use two distinct fixed auxiliary primes,
e.g. 13 and 17 in the moving quadratic
scheme, to include the coefficient prime
equal to one of them. They do not
divide $6N$ for the original congruences
$q,d\equiv3\bmod4$.
After summing with $\log\ell$, the
product formula for the nonzero integer
gives the required polynomial bound.

At the original subexponential auxiliary
sizes, $\log N=O(x^{\epsilon/4})$ and
$e\le t\le x^{C_t}$, this polynomial
logarithmic Selmer bound would be well
within the allowed exponential budget
after summing the twist indices.
For the one-sign polynomial auxiliaries
it is smaller still. Thus there is no
new large-field spectral-count obstacle
in (6). The obstacle is producing (6)
with the actual new ring, including
characteristic-prime finiteness,
automorphy, admissible point shape and
the cross-block rigidity just identified.

## 7. What is actually supplied

The new integral diagonal, polarized
adjoint dictionary, strict torsion and
marked conormal injection are constructed.
The high-dyadic and nonresonant marks,
strong irreducibility, type-II block
identification and conditional
polynomial Frobenius spectrum are proved
with the stated classical/parent inputs.
The original parent OneChar and Kato
arguments are not silently applied to
the new cubic representations.
No uniform actual odd-prime cubic
length estimate, global prime-discrepancy
inequality or completed Hecke node follows
without the remaining arithmetic
automorphy/rigidity/counting input.

## Later point-shape theorem

The [marked classification](cubic-point-shapes-and-rigidity.md) now proves the two-sided point-shape statement for the fully marked normalization in either characteristic and the even-dimensional fixed-space obstruction to the usual rank-one Euler-system method. The actual finite-ring and cross-block rigidity estimates remain open.
