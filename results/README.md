# Results proved in the manuscript

These are mathematical reductions and comparisons. Their proofs are in [the paper](../paper/main.pdf); none establishes the missing arithmetic input for a complete proof of GRH.

## Primitive characters and reflection

If a character modulo $N$ is induced by a primitive character $\psi$ of conductor $q$, then

```math
L(s,\chi)=L(s,\psi)\prod_{p\mid N,\ p\nmid q}(1-\psi(p)p^{-s}).
```

Every added factor is nonzero for $\mathrm{Re}\,s>0$. The primitive and imprimitive functions therefore have the same zeros, with multiplicities, in that half-plane away from poles. The normalized functional equation reflects a primitive zero at $s$ to a zero for the conjugate character at $1-s$. Thus primitive nonvanishing in the right half of the critical strip implies Dirichlet GRH.

The proof includes conductors, Gauss sums, the theta transformation, the conductor-one case, and the boundary at real part zero.

## A one-sided prime-sum criterion

Put

```math
G(x)=\sum_{n\leq x}\Lambda(n)(x/n-1)-x\log x+(1+\gamma)x.
```

For nonprincipal $\chi$ with $L(1,\chi)\ne0$, put

```math
g_\chi(x)=\sum_{n\leq x}\Lambda(n)\chi(n)(x/n-1)+x\frac{L'(1,\chi)}{L(1,\chi)}.
```

Let $R$ and the $m_\chi$ be positive integers, with a finite character family closed under conjugation and $m_{\bar\chi}=m_\chi$. An eventual upper bound

```math
R G(x)+\sum_\chi m_\chi\mathrm{Re}\,g_\chi(x)\leq Cx^\theta,\qquad 0\leq\theta<1,
```

implies zero-freeness in $\mathrm{Re}\,s>\theta$ for zeta and all characters in the family. No lower bound is needed. The paper proves the exact Mellin identities, the positivity argument, and the sign of the possible residue. It does not prove this arithmetic upper bound.

## A smoothed Möbius-sum criterion

If, for every fixed smooth compactly supported test $W$ and every $\varepsilon>0$,

```math
\sum_n\mu(n)\chi(n)W(n/X)\ll_{\chi,W,\varepsilon}X^{\theta+\varepsilon},
```

then $L(s,\chi)$ has no zero in $\mathrm{Re}\,s>\theta$, for $\theta\geq0$. The paper also proves the version for ideals and deleted Euler factors. A test chosen to have nonzero Mellin transform at a hypothetical zero gives a direct contradiction.

## Consequences of a second-moment bound

The paper proves the exact inequality that extracts one sum from many approximately equal sums. Applying it to sixth powers gives the October source's $11/12$ exponent **conditional on its displayed arithmetic inputs**. The precise optimization limitation is recorded in [negative-results](../negative-results/README.md).

## Inversion and uniformity

The remaining proved results include exact Möbius inversion for added cube factors, an induction with an explicit bound on its number of steps, and a continuation theorem with a common positive saving over a family. All multiplicativity, support, and uniformity hypotheses are stated in the paper.
