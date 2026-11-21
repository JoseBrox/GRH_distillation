# Results proved in the manuscript

These are mathematical reductions and comparisons. Their proofs are in [the paper](../paper/main.pdf); none establishes the missing arithmetic input for a complete proof of GRH.

## Primitive characters and reflection

If a character modulo N is induced by a primitive character ψ of conductor q, then

```text
L(s, χ) = L(s, ψ) ∏_{p | N, p ∤ q} (1 − ψ(p)p^(−s)).
```

Every added factor is nonzero for Re(s) > 0. The primitive and imprimitive functions therefore have the same zeros, with multiplicities, in that half-plane away from poles. The normalized functional equation reflects a primitive zero at s to a zero for the conjugate character at 1 − s. Thus primitive nonvanishing in the right half of the critical strip implies Dirichlet GRH.

The proof includes conductors, Gauss sums, the theta transformation, the conductor-one case, and the boundary at real part zero.

## A one-sided prime-sum criterion

Put

```text
G(x) = ∑_{n≤x} Λ(n)(x/n − 1) − x log x + (1 + γ)x.
```

For nonprincipal χ with L(1, χ) ≠ 0, put

```text
g_χ(x) = ∑_{n≤x} Λ(n)χ(n)(x/n − 1) + x L'(1, χ)/L(1, χ).
```

Let R and the m_χ be positive integers, with a finite character family closed under conjugation and m_{χ̄} = m_χ. An eventual upper bound

```text
R G(x) + ∑_χ m_χ Re(g_χ(x)) ≤ C x^θ,    0 ≤ θ < 1,
```

implies zero-freeness in Re(s) > θ for zeta and all characters in the family. No lower bound is needed. The paper proves the exact Mellin identities, the positivity argument, and the sign of the possible residue. It does not prove this arithmetic upper bound.

## A smoothed Möbius-sum criterion

If, for every fixed smooth compactly supported test W and every ε > 0,

```text
∑_n μ(n)χ(n)W(n/X) ≪_{χ,W,ε} X^(θ+ε),
```

then L(s, χ) has no zero in Re(s) > θ, for θ ≥ 0. The paper also proves the version for ideals and deleted Euler factors. A test chosen to have nonzero Mellin transform at a hypothetical zero gives a direct contradiction.

## Consequences of a second-moment bound

The paper proves the exact inequality that extracts one sum from many approximately equal sums. Applying it to sixth powers gives the October source's 11/12 exponent **conditional on its displayed arithmetic inputs**. The precise optimization limitation is recorded in [negative-results](../negative-results/README.md).

## Inversion and uniformity

The remaining proved results include exact Möbius inversion for added cube factors, an induction with an explicit bound on its number of steps, and a continuation theorem with a common positive saving over a family. All multiplicativity, support, and uniformity hypotheses are stated in the paper.
