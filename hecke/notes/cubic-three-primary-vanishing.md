# Vanishing of the high-dyadic cubic 3-primary sectors

24 November 2026. **Actual new odd-prime Selmer vanishing.** This
uses the parent's proved Bernoulli-unit theorem and elementary Kummer
reflection. It is not a bound for the surviving low-conductor sectors.

Keep $F=\mathbb Q(\omega)$ and the cubic character $\lambda$ of
$F(\sqrt[3]2)/F$. Let $\rho=\rho_2\rho_o$ be a Dirichlet character
from the real dyadic layer and the one or two auxiliary quadratic
fields of our cubic host. Thus $\rho_2$ is even of exact conductor
$2^b$, and $\rho_o$ is quadratic or trivial of odd conductor $f$,
prime to 3. Write $\rho^N$ for its restriction to $G_F$, equivalently
norm pullback. The auxiliary primes are distinct from 2 and 3.
Let $\mathcal O$ be a coefficient DVR over $\mathbb Z_3$ containing
the character values and $\omega$, with uniformizer $\pi$, residue
field $k$ and fraction field $E_\mathcal O$.

**Theorem.** If $b\ge 8$ and $2^b\ge192f$, then for either cubic sign
and every integer $e$,


```math
S_F((E_\mathcal O/\mathcal O)(-e)\otimes
                 \lambda^{\pm1}(\rho^N)^{-1})=0.
\tag{1}
```


Here $S_F$ is the exact strict kernel of
[cubic-exceptional-prime-comparison](cubic-exceptional-prime-comparison.md):
the restriction to inertia is zero away from 3, and the restriction
to the full decomposition group is zero at 3. In particular the
theorem is uniform over all twist indices in the source window,
not just a residual-length estimate.

## 1. A class-group consequence of the parent's Bernoulli units

Put $M=\mathbb Q(\omega)R_{b-2}(\sqrt{-q},\sqrt{-d})$, using only
the chosen quadratic factors; alternatively omit those not needed
by $\rho$. This is an abelian CM field of power-of-two degree,
containing $\mu_3$ but no $\mu_9$. Its Galois group over $\mathbb Q$
has order prime to 3. The character $\rho$ factors through it.

Write $\omega_3$ for the mod-3 cyclotomic character of this
Galois group, lifted in characteristic zero as $\chi_{-3}$.
For a residual character $\theta$ of the group with exact
dyadic conductor $2^b$ and odd part of conductor dividing $3f$
and order at most two, suppose first that $\theta$ is odd.
The parent's
[Bernoulli-unit theorem and cocycle corollary](../../paper/shared/selmer-dyadic-twist-vanishing.tex)
apply to its prime-to-3 lift: take $Q=9$, $h=v_2(Q-1)=3$,
so the required threshold is $(3f)4^3\le2^b$.
All the finite odd-order conductor factors here have character
order dividing 8 (indeed at most two). Reduction of the dyadic
roots of unity preserves their orders.

Consequently the $\theta$-eigenspace of
$\operatorname{Cl}(M)/3\operatorname{Cl}(M)\otimes_{\mathbb F_3}k$
is zero. Indeed a nonzero such eigenspace gives an additive
map $u:\operatorname{Cl}(M)\to k$ with
$u(g a)=\theta(g)u(a)$ by projection onto the eigenspace.
Class field theory gives an unramified homomorphism on $G_M$.
Inflation-restriction with the coefficient module $k(\theta)$
extends it to a class in $H^1(G_\mathbb Q,k(\theta))$, since the
quotient has order prime to 3. Its restriction vanishes on
$I\cap G_M$ for every finite inertia group $I$, a subgroup
of $I\cap\ker\theta$ of index prime to 3.
The parent's cocycle corollary makes it a coboundary, contrary
to its nonzero restriction. This argument does not require that
the full cyclotomic field of the conductor have degree prime
to 3.

Now let $\theta$ be even with the same conductor hypotheses,
and let $\theta^*=\omega_3\theta^{-1}$. This is odd,
with the same exact dyadic conductor, and odd conductor
dividing $3f$. Its class-group eigenspace just proved zero is
also zero in $\operatorname{Cl}(M)[3]\otimes k$: decompose
the finite 3-primary group using the prime-to-3 character
idempotents over the integers of a sufficiently large
unramified coefficient extension, and apply Nakayama to
the zero mod-3 component.

If the $\theta$-component of the class group mod 3 were
nonzero, Kummer theory over $M$ would supply a nonzero
$\theta^*$-component of the radical of the unramified
elementary abelian cubic class-field extension. More explicitly,
the radical is the Galois module
$\operatorname{Hom}(\operatorname{Cl}(M)/3\operatorname{Cl}(M),
\mu_3)$, embedded in $M^\times/M^{\times3}$. Taking the
duality and the action on $\mu_3$ gives precisely the
character $\omega_3\theta^{-1}$. For any Kummer class of
an everywhere unramified extension, all finite valuations
are divisible by 3; otherwise the cube root has a nonintegral
valuation in the unramified valuation group. Hence its class
belongs to the domain of the exact sequence


```math
0\longrightarrow
  \mathcal O_M^\times/\mathcal O_M^{\times3}
 \longrightarrow
 \{a\in M^\times:\operatorname{ord}_{\mathfrak p}(a)
                        \in3\mathbb Z\ \forall\mathfrak p\}/M^{\times3}
 \longrightarrow \operatorname{Cl}(M)[3]\longrightarrow0.
```


The final map takes the class of the ideal with cube $(a)$.
The odd part of the unit term has only the character
$\omega_3$: for each unit $u$, the unit $u/\bar u$ has
absolute value one at every embedding of this CM field and
is therefore a root of unity by Kronecker's theorem.
Since 2 is invertible modulo 3, this proves that the
minus part comes from roots of unity. Their mod-cubes
3-component is exactly $\mu_3$, since $M$ has 2-power
degree and so cannot contain $\mu_9$.
The high dyadic conductor ensures $\theta^*\ne\omega_3$.
Thus both outer $\theta^*$-components vanish, a contradiction.
This proves the desired even-component vanishing as well.
No reflection inequality with an unspecified exceptional
unit character is being used.

## 2. Residual strict classes over the Eisenstein field

Let $\vartheta=\bar\rho^{-1}$ and $V=k(\vartheta|_{G_F})$.
Its restriction to $G_M$ is trivial. Inflation-restriction
for $M/F$ gives an injection
$H^1(G_F,V)\to H^1(G_M,k)$ with the character equivariance.
A strict class restricts to an unramified homomorphism at all
finite places (the stronger zero condition at 3 certainly
implies this). It factors through $\operatorname{Cl}(M)$.

Since $F/\mathbb Q$ is quadratic, the two possible full
Galois characters in this equivariant Hom space are
$\vartheta$ and $\vartheta\omega_3$: their restrictions to
$\operatorname{Gal}(M/F)$ are the prescribed same character.
Both have the high dyadic conductor, odd conductor dividing
$3f$ and odd part of order at most two. Both class-group
components vanish by Section 1, so the strict group over
$F$ for $V$ is zero.

## 3. Integral lifting: checking every local kernel

Write
$D=(E_\mathcal O/\mathcal O)(-e)\otimes
\lambda^{\pm1}(\rho^N)^{-1}$. As $F$ contains $\mu_3$,
the residual cyclotomic character on $G_F$ is trivial.
The cubic character also reduces to one in characteristic
3. Thus $D[\pi]=V$, irrespective of the sign or $e$.

We check that the global and all strict local restrictions
of the map $H^1(V)\to H^1(D)$ from
$0\to V\to D\xrightarrow{\pi}D\to0$ have zero kernel.
For any of the relevant groups $H$ this follows if
$D^H$ is zero or divisible by $\pi$, by the long exact
sequence. If the residual rank-one character is nontrivial
on $H$, some scalar differs from one by a unit and
$D^H=0$. If the entire integral character is trivial on
$H$, then $D^H=D$ is divisible.

At inertia over 2 the high dyadic character is residually
nontrivial. The extension $F/\mathbb Q$ is unramified at
2, so restriction does not remove this inertia. This
also proves the global invariant assertion. At a prime
over an auxiliary odd conductor factor of $\rho_o$,
the same argument applies because $F$ is unramified
there. At every other inertia away from 3 and 2 the
whole integral character is unramified: the fixed cubic
extension is unramified outside 6, the Tate twist is
unramified away from 3, and the remaining finite
character factors are unramified by their conductors.

At the prime above 3 use the full decomposition group.
The character $\rho$ is unramified over $\mathbb Q_3$.
The extension $F/\mathbb Q$ has residue degree one there,
so an arithmetic Frobenius has $\rho$-value $\rho(3)$.
The element $-3$ generates the cyclic group
$1+4\mathbb Z/2^b\mathbb Z$ (its successive squared
powers have valuations $v_2((-3)^{2^j}-1)=j+2$).
The character $\rho_2$ is even and primitive,
so $\rho_2(3)=\rho_2(-3)$ has order $2^{b-2}$.
Multiplication by the quadratic value $\rho_o(3)$
cannot make it trivial. Its reduction still has
that nontrivial order because it is prime to 3.
Consequently the full local residual character
at 3 is nontrivial as well.

These cases verify all injections, including the full
condition at 3 rather than only an inertia condition.
It follows from the long exact sequence globally and
the local injections that $S_F(D)[\pi]$ is exactly the
image of the strict residual group $S_F(V)$. Section 2
makes it zero. The group $S_F(D)$ is $\pi$-primary
torsion, so every nonzero element would give a nonzero
element killed by $\pi$. This proves (1).

## 4. Consequences and limits

In the exact cubic-sector length sum (3) of
[cubic-exceptional-prime-comparison](cubic-exceptional-prime-comparison.md)
every sector satisfying the threshold in this note can be
deleted, before summing over the twist indices. There
is no additional projection or extension-of-scalars cost.
The integral comparison error of that note still applies.

In particular all auxiliary-untwisted high dyadic
sectors ($f=1$, $b\ge8$) vanish. With a polynomial
auxiliary prime the threshold may also hold for
some genuinely twisted high layers. This is a
condition on the *actual* conductor: it is not
claimed for the exponentially large auxiliary
primes in our original two-sign scheme, or
uniformly over an arbitrary common subwindow
of the polynomial companion theorem.

There is no new bound here for the lower
dyadic layers, cubic sectors at primes at least
5, the abelian 3-primary sum, or the global
prime-discrepancy inequality. The reflection
argument is special to the reduction of the
cubic character at 3 and cannot simply be
repeated at primes where that character
remains nonabelian in the induction over Q.
