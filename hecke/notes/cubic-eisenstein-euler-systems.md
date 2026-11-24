# The direct Eisenstein-field Euler-system alternative

24 November 2026. This note investigates the remaining low-dyadic
cross-block rigidity after [corner elimination](cubic-corner-elimination.md).
It proves the rational rank-one image condition for a single constituent,
computes the local regulator rank, and identifies exactly what would
still have to be constructed. It does not assert a nonzero Euler system
or new Bloch--Kato vanishing.

## 1. The target over F

Use the notation and hypotheses of the
[outer-block model](cubic-polarized-selmer-model.md), §5.
Let F=Q(omega), K=F(cuberoot(2)), eta=chi_{-3}, and lambda the
cubic character of K/F. At an actual irreducible outer-block
characteristic-zero point, the normalized representation W of G_Q
has determinant eta. Its restriction W_F has determinant one,
and is absolutely irreducible after every finite extension, as
proved in the model. Its ordered local inertia characters at ell
have cyclotomic exponents e,-e (e>=1) times finite characters.

Put B=Ind_F^Q lambda. The desired cross-block rigidity is
H_f^1(Q,W tensor B)=0. The restriction and induction identifications
give the equivalent single-constituent target


```math
V=W_F\otimes\lambda,\qquad H_f^1(F,V)=0. \tag{1}
```


Replacing lambda by its inverse gives the conjugate group of the
same dimension, because W extends over Q. Shapiro gives the displayed
identification of global cohomology. At each rational place, local
Shapiro and the decomposition of restriction of an induced module
into its local summands identify the unramified conditions away
from ell. At ell they identify the kernels after tensoring with
B_cris, using the projection formula for finite-index induction.
Thus the equivalence is for Bloch--Kato finite conditions, not just
for unrestricted cohomology or for the strict groups.

## 2. Rational rank-one image condition is restored

Let E be a finite ell-adic coefficient field for the point,
ell>=5. Set H=G_{K(mu_{ell^infinity})}. There exists tau in H
such that W_F(tau) is a nonidentity unipotent, and hence


```math
\dim_E V/(\tau-1)V=1. \tag{2}
```


The same assertion holds for U=V^vee(1).

**Proof.** The connected Zariski closure of W(G_F) is SL2
over the algebraic closure. Indeed strong irreducibility excludes
a reducible connected component (its inverse image is open);
in characteristic zero a proper connected algebraic subgroup of
SL2 is solvable and cannot act irreducibly in dimension two.
The closure is consequently SL2. Since G_F/H is abelian, the
Zariski closure of W(H) contains the derived group of this
closure, again SL2. The compact image W(H) is therefore infinite.
Its Q_ell-Lie algebra h is nonzero (a compact ell-adic analytic
group of dimension zero is finite). Its E-span is stable under
W(G_F), by normality of H. By Zariski density this span is stable
under SL2, hence equals sl2 by simplicity.

Choose an inertia element at a place over ell, killing the
finite inertia characters of the ordered flag, with cyclotomic
value t of infinite order. Such a choice is possible since
cyclotomic inertia has infinite image and the finite characters
have finite kernel index. Its eigenvalues on W are t^e,t^{-e},
distinct. The adjoint on sl2 has distinct eigenvalues
1,t^{2e},t^{-2e}, all in Q_ell. Each spectral projector is a
polynomial in this adjoint over Q_ell. Since h is stable under
the adjoint, the projectors preserve h. Its E-span is sl2,
so a nonzero element X of one of the two root lines lies in h.
It satisfies X^2=0. For sufficiently large n, the local
exponential theorem for closed ell-adic matrix groups gives
I+ell^n X=exp(ell^n X) in W(H). This is a nonidentity
unipotent. Lift it to tau in H. Both the cubic and cyclotomic
characters are one there, proving (2) for V and its Tate dual.
QED.

This also meets the additional field-fixing requirements in
Rubin's rational Hyp(F,U): F has class number one and its unit
group is mu6, so for ell>=5 its ell-power roots of units already
belong to F. Absolute irreducibility of U follows from that of W_F.

It does NOT meet the stronger integral hypotheses automatically.
On the cyclotomic kernel the actual distinguished residual
lattice of W_F has diagonal characters rho^N and (rho^N)^(-1)
of 2-power order. Multiplying either by a nontrivial cubic
value cannot give one, since ell>=5 preserves the prime-to-ell
roots of unity. If lambda=1, an eigenvalue one forces both.
On this particular residual diagonal lattice the fixed-space
dimension is zero or two; a free rank-one integral quotient
cannot occur. Changing to another stable lattice can alter
residual Jordan blocks, but cannot make its residual
semisimplification irreducible. Thus the integral residual
irreducibility hypotheses still fail. The rational statement
(2) is precisely what is needed for qualitative point rigidity,
rather than an integral numerical Euler-system bound.

## 3. The local rank is two, not one

Assume the actual outer point is geometric at ell (in particular
potentially crystalline, as in the verified nonresonant local
range of the model). Its two Hodge--Tate weights are e,-e,
up to the convention for signs; finite lambda does not change
them. At every v|ell the invariant space H^0(F_v,V) is zero:
a trivial subrepresentation would have weight zero, whereas
neither weight is zero. The Bloch--Kato local dimension formula
therefore gives


```math
\dim_E H_f^1(F_v,V)=[F_v:\mathbf Q_\ell],\qquad
 \sum_{v\mid\ell}\dim_E H_f^1(F_v,V)=2. \tag{3}
```


These formulas hold at a split or inert coefficient prime.
Let U=V^vee(1). Orthogonality under local Tate duality gives


```math
Q_\ell(U)=\bigoplus_{v\mid\ell}H^1(F_v,U)/H_f^1(F_v,U),
 \qquad \dim_E Q_\ell(U)=2.
```


Write H_rel^1(F,U) for finite conditions away from ell with
no condition at ell, and H_str^1(F,V) for finite conditions
away from ell and zero at all v|ell. Poitou--Tate gives the
exact sequence of E-vector spaces


```math
H_{\rm rel}^1(F,U)\longrightarrow Q_\ell(U)
 \longrightarrow H_f^1(F,V)^\vee
 \longrightarrow H_{\rm str}^1(F,V)^\vee\longrightarrow0.
 \tag{4}
```


In particular full rigidity is equivalent to strict rigidity
and surjectivity of the singular localization in (4).
With strict rigidity alone its dimension is at most two;
one nonzero singular localization reduces that bound to one.

Here is one precise sufficient Euler-system construction.
Use a lattice T in U and an Euler system in Rubin's sense
over F (including the necessary norm relations at primes
of F, the cyclotomic tower, and the allowed ramification
conditions). By (2), Rubin, *Euler systems*, Chapter II,
Hyp(F,V) and Theorem 2.3, pp. 24--25, show that a nontorsion
base class would kill the rational strict group. More
explicitly the strict group for the associated discrete Tate
dual is finite, so its rational counterpart is zero. If two
base classes in H_rel^1(F,U) can also be produced whose singular
localizations are independent, then (4) kills the full group.
They need not both come from Euler systems. The two-class
regulator, or an appropriate exterior-rank-two system and a
descent theorem proving the same conclusions, remains missing.

Rubin's Theorem 2.10 assumes that the singular local module
is spanned rationally by the localization of one class.
Equation (3) explains why that theorem cannot be applied
directly to the full finite condition in this case. It is not
enough to produce just one nonzero Beilinson--Flach element.
For a convention check see Chapter II, pp. 24--26,
https://swc-math.github.io/aws/1999/99RubinES.pdf .

## 4. Why direct projection of the rational tensor system is insufficient

The rational tensor has two equal quadratic determinants and no
element with one-dimensional fixed space, as proved in the
[point-shape note](cubic-point-shapes-and-rigidity.md).
Under Shapiro, an Euler relation at a good rational split prime
q=v v^c involves the product of the two local Euler factors
at v and v^c. In contrast an Euler system over F needs a
one-prime relation when the ray-class conductor is enlarged
at v alone. The conjugate factor does not in general become
a unit at the Kolyvagin specialization: on the cyclotomic
kernel where a single constituent has eigenvalue one, its
conjugate also has eigenvalue one (the two cubic twists are
reciprocal and det W_F=1). Thus neither taking a character
projection nor dividing out the conjugate factor formally
constructs the desired Euler system. This is an obstruction to
that deduction, not to the existence of a suitable system.

## 5. Analytic critical value and existing theorem audit

At geometric outer points the irreducible odd two-dimensional W
has distinct Hodge--Tate weights. Pan's Fontaine--Mazur theorem
for residually reducible representations, arXiv:1901.07166v2,
Theorems 1.0.2 and 1.0.4, gives modularity up to twist when its
stated hypotheses are met. In the parent's geometric Frobenius
convention the weight-2e+1 normalization is W epsilon^{-e}
with character eta; finite twists can be absorbed into the
newform. Strong irreducibility over F ensures cuspidal
quadratic base change. The cubic twist of this base change is
still cuspidal. Its unitary standard L-value at 1 is nonzero
by the classical GL2 line-one nonvanishing theorem of
Jacquet--Shalika/Shahidi. Equivalently the Rankin product of
the weight-2e+1 form and the weight-one dihedral theta form
has nonzero critical value at e+1 (and at e by the functional
equation), with the conventional classical normalization.
This addresses the analytic nonvanishing, not the cohomological
regulator or the automorphic attachment of rank-three points.

The following checked frameworks do not immediately supply (1).

* Kings--Loeffler--Zerbes, *Rankin--Eisenstein classes and explicit
  reciprocity laws*, arXiv:1503.02888v6, Hypothesis 11.1.2 and
  Theorem 11.7.3: the big-image hypothesis is not met for the
  actual rational tensor, and the two nebentypus characters
  have product one. One must not import the rank-one conclusion
  into this tensor.
* Burns--Sakamoto--Sano, *On the theory of higher rank Euler,
  Kolyvagin and Stark systems II*, arXiv:1805.08448v1,
  Hypothesis 3.2: the higher global exterior rank still uses
  residual irreducibility and a rank-one local quotient hypothesis.
  Increasing the exterior rank alone does not solve these
  hypotheses for the actual integral frame. This is a check of
  that framework, not an impossibility theorem for all higher-rank
  methods.
* Lei--Loeffler--Zerbes, *Euler systems for modular forms over
  imaginary quadratic fields*, Compos. Math. 151 (2015),
  DOI 10.1112/S0010437X14008033, Theorem 7.4.2: its indicated
  weight-two, Hecke infinity type and split ordinary setting
  do not cover all our odd weights and both coefficient-prime
  splitting types. It cannot supply the necessary universal
  point theorem merely by identifying F with an imaginary
  quadratic field.

In the high-dyadic range the separate corner-elimination theorem
makes this entire cross-block argument unnecessary. For the
remaining range the precise candidate is a genuine prime-of-F
system satisfying Rubin's rational hypotheses together with a
rank-two singular regulator, or another rigidity argument
yielding (1). No such classes or rank-two reciprocity law
have been constructed in this note. The full quantitative
moving Selmer length is still open.
