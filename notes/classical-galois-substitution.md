# Adopted classical Galois input

## Conclusion

The conventional reconstruction now supplies the source's universal
Galois-representation contract from the classical theorem package.
The full local-law dictionary and the global automorphic/period dictionary
have both passed independent review. This closes W05 as a cited input
with proved normalization and transport steps.

The source's separate production of this Galois input through a geometric
seed, congruences and stable theta lifting is retained as an alternative.
This substitution does not remove theta-integral identities, geometric
covolume bounds or integral congruence estimates used independently.
It is a mathematical comparison, not a new Lean compilation.

## 1. Inputs now available

| Input | Exact role | Proof and evidence |
| --- | --- | --- |
| Classical full local correspondence | All fifteen local laws, together with local Artin and epsilon witnesses, at every required number-field completion | [Local correspondence](classical-local-correspondence.md) |
| Depth-zero type formula | Supplies the additional weak type law with the exact inertial character and zero monodromy | [Global input audit](lean-global-inputs.md), depth-zero subsection |
| Global classical representation | One continuous semisimple representation, weight and labeled Hodge–Tate family, before all local models and embeddings | [Global and period dictionary](galois-period-dictionary.md) |
| Toral and tame preimages | Under the full correspondence, every guarded parameter has a preimage satisfying the source's comparison conditions | [Local preimage proofs](local-correspondence-bridge.md) |
| Transfer to arbitrary weak correspondences | Restricted uniqueness and injectivity recover the universal source row with the same global representation | [Transfer proof](fixed-correspondence-reduction.md) |

The full local family quantifies over number fields and their finite
completions. These are finite extensions of Q_p; an equal-characteristic
local correspondence is not being assumed or silently omitted.

The source's epsilon witness uses the underlying Weil constant at 1/2,
independent of monodromy. Its adjacent-rank equation agrees with the
classical equation because the relevant tensor has no inertia invariants.
The passage from induced representations to a generic irreducible quotient
is explicit; it uses uniqueness of Whittaker functionals and the separate
JPSS divisibility statement. This point was strengthened during independent
review.

## 2. Substitution theorem

**Proposition.** At the pinned source interfaces, the classical full local
correspondence and the classical global Galois theorem supply
Row0b IsRecT, including all its local, weight, crystalline and period-model
quantifiers. They also provide the local weak-correspondence existence
input used with that row.

**Proof.** Choose the classical correspondence at each required finite
completion. The full-law and depth-zero type comparisons make this a
family of weak source correspondences.

For any allowed CM field, positive rank, coefficient prime, complex
identification and regular algebraic polarized cuspidal representation,
the global dictionary supplies one global representation r, one weight
w and all labeled Hodge–Tate multisets. Its coefficient model can be
enlarged, and its period rings transported, after this global choice.
No local model causes r to be chosen afresh.

Fix any other allowed weak local correspondence rc and a local component σ.
Write x=algNorm(σ) for its algebraically normalized twist, and put y=rc(x).
When y falls under either guarded comparison, the preimage
lemmas give a good component z whose classical parameter is y. Restricted
uniqueness on good components says that the weak parameter of z is also y.
The weak injectivity statement therefore gives x=z. The two
correspondences agree on this required parameter.

Consequently the classical local comparison for r is exactly the
comparison demanded by the arbitrary weak correspondence. The unguarded
dimension statement follows separately from the dimension laws.
Continuity, semisimplicity, weights and spherical crystallinity do not
depend on which local correspondence was named. This proves the universal
row without changing the already chosen r, w or Hodge–Tate multisets. ∎

Above the coefficient prime, the classical theorem is stronger than the
source guard: zero monodromy of the target parameter suffices for full
Frobenius-semisimplified compatibility. Monodromy dominance gives this
conclusion; purity alone would not.

## 3. Consequence for the full proof program

The same completed row can be reused at the repeated literature fields
and at the verified construction of the Selmer windows. The replacement
preserves the existing downstream interfaces, so it does not require a
second program based on changing every consumer to a fixed correspondence.

The adopted route now uses the conventional theorem stated in the
manuscript's Galois and adjoint-vanishing section, with the classical
local correspondence. The technical dictionary is retained here to make
the connection with the pinned source auditable.

This eliminates the original Galois-construction supplier from the
preferred logical route. It makes no claim about an exact number of
unused source files: imports are not theorem-term dependencies, and the
same geometric or analytic tools can occur in other branches.

The unresolved work remains the compatible global arithmetic construction:
the required integral maps and divisibility, theta identities and norms,
geometric core lower slopes and discarded-degree budgets, and the
remaining cohomological and counting estimates. Availability of r alone
does not supply these bounds.

## 4. Verification

The local dictionary records fourteen pinned source files and seven
primary references. The global dictionary records twenty-one pinned
source files and five primary references. Both have independent PASS
reviews from the other specialists; the endpoint reviewer also checked
the final quantifier order and their composition with the universal-row
transfer. The previous preimage and type-formula certificates remain
part of the dependency chain.

The composition certificate records the exact hashes of these five
inputs and of this note. Every source read was bounded and checked
against the same immutable source revision. No newly run Lean kernel
verification is claimed.
