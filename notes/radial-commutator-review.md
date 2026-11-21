# Independent review of the radial commutator construction

Reviewed: [the new matrix-restriction section](../paper/sections/new/commutator-matrix.tex),
with its bounded dependencies in recovered sections 85–88 and 95.
The independent algebraic check is
[check_commutator_matrix_review.py](../scripts/check_commutator_matrix_review.py);
its exact results and reviewed source hashes are in
[radial-commutator-independent-check.json](../certificates/radial-commutator-independent-check.json).

**Conclusion:** no blocking mathematical issue was found in the commutator
reconstruction or its application to the prescribed finite chains. The
construction supplies the previously missing full initial matrix restriction.
It does not establish the integrated residue-pairing identities or estimates
uniform in a growing chain length.

## 1. Algebra and operator order

The determinant–covector commutator has cofactor parameter `u − 1`; the
determinant–vector commutator has parameter `u` and a minus sign. The
cofactor–vector identity has the omitted indices in the order stated in the
draft. Antisymmetry in its two omitted column indices converts its contracted
mixed commutator into the stated double cofactor, with no additional factor
of two or four. This yields the signs

```math
\mathcal T(u)=
\begin{pmatrix}
D(u)&-[D(u),Z]\\
{[D(u),\bar Z]}&-[[D(u),Z],\bar Z]
\end{pmatrix}.
```

The universal argument uses the recovered ordered-minor expansion identities
and the explicitly stated commutation laws. It never commutes a coefficient
past a differential operator without accounting for its commutator.

The sandwich calculation requires that the middle entries commute with the
outer coordinates and their Euler derivatives. It does not require those
middle entries to commute with one another. Multiplication in the displayed
order gives all four claimed entries. The chain order is consequently
`L₀ ··· Lᵣ₋₁ t Tᵣ₋₁ ··· T₀`, including `t` for the empty chain.

## 2. Domains and the scalar-to-matrix implication

The full-group identity acts on the common smooth differential-operator
domain, and in particular on compactly supported smooth functions. It uses
no inverse Gram determinant and no inverse spectral polynomial. The
one-pair radial identity is restricted to `c ≠ 0`; a finite chain requires
every indicated coordinate to be nonzero. The one-pair theorem now states
`dim W ≥ 2`, covering the actual applications; the separate algebraic
remark correctly handles dimension one. Dimension zero is not claimed.

On the open cell, the full-group coefficient `Z₀` restricts to `c`, and
`conjugate(Z₀)` restricts to `conjugate(c)`. Both are invariant under the
unipotent translations imposing the character laws. Thus the scalar
restriction identity applies to all four functions `F`, `Z₀F`,
`conjugate(Z₀)F`, and `Z₀ conjugate(Z₀)F`. Subtraction gives the first and
mixed commutators exactly. This is a valid intertwining argument; it does
not assume that an arbitrary matrix is reconstructible from an arbitrary
single scalar entry, or that restriction to the open cell is globally
injective on unrestricted smooth functions. The specific contracted form
and its commutator identities are the essential additional information.

For the chain corollary the prescribed flag characters matter. At each
nonterminal stage the distinguished vector is the next isotropic basis
vector, and the terminal vectors are the given final character vectors.
The final theorem statement and proof both identify these standard flag
characters explicitly, incorporating the review clarification.
A succession of hyperbolic pairs with
unrelated arbitrary character data would not by itself imply the displayed
iteration.

## 3. Signature, conjugation and formal adjoints

I checked the explicit character rules in the generalized scalar reduction.
With `h` linear in its first argument, the coefficient conventions give
`B = conjugate(Z)` and the asserted left and right mixed-root rules. These
rules require nondegeneracy of the Hermitian form but no sign condition on
the character vectors. Their central characters vanish. The bordered
scalar calculation therefore extends to the isotropic intermediate vectors
used in the recursion; no division by their norms occurs.

For `γ(c) = |c|^(d+1)`, scalar conjugation sends `p` to
`p − (d+1)/2` and `−bar(p)` to `−bar(p) + (d+1)/2`.
Together with the two unnormalized diagonal parameters this gives exactly
`Y+p` and `Y−bar(p)`, with middle parameter `Y+(d−1)/2`.
The remaining dimension at stage `j` gives exponent `k+2(r−j)`;
the product equals the existing `γᵣ` from recovered section 95.

For real spectral parameter, the existing signed-minor adjoint rule gives
formal self-adjointness of the determinant. Multiplication by `Z` and
`conjugate(Z)` are formal adjoints. Reversing the commutators gives the
off-diagonal adjoint pair, and the Jacobi identity together with
`[Z, conjugate(Z)] = 0` gives the lower-right formal self-adjointness.
No assertion about self-adjoint closures or unbounded-operator spectral
domains is used.

The full-group coefficients and their derivatives are polynomially bounded,
including after formal adjoint formation. Finite differential compositions
preserve compact support and the fixed positive Gram cutoff. Their Jacquet
intertwining uses the dominated-differentiation and adjoint results already
proved in sections 94–95. Constants may depend on the fixed chain and word.

## 4. Independent exact computation

The independent script implements differential operators as maps from
multi-indices to exact rational-function coefficients. Composition is
computed by the full multivariate Leibniz formula, and equality is checked
coefficient by coefficient in normal order. It does not evaluate only a
finite list of test functions.

For dimensions one and two, it represents
`E_ab = η_a ∂/∂η_b − y_b ∂/∂y_a`, retaining the spectral parameter and every
component of `x` and `ξ` as independent symbols. All 17 Lie-relation checks,
9 cofactor–vector checks and 6 contracted commutator checks pass. In
particular, the dimension-one double commutator is zero and the
dimension-two signs agree exactly with the displayed unordered-pair formula.

A separate Weyl-sandwich calculation uses the genuinely noncommuting middle
entries `s∂s`, `s`, `∂s`, and `s²∂s+1`. All four matrix-entry identities
pass; three nonzero middle-entry commutators are confirmed. A negative
control replaces the first middle entry by `∂c`, violating independence
of the outer variable. The proposed reconstruction then fails in entries
`(1,2)` and `(2,2)`, as expected.

These checks independently verify the stated differential representations
and the concrete sign, order and independence risks. They do not replace
the universal algebraic proof, prove the analytic scalar restriction in
all ranks, or certify the rest of the GRH manuscript. The broader source
identification is recorded separately in the
[source comparison](source-check-2026-11-21.md).
