# Case II: marked rank-four symplectic induction

**Status: the full original Case II seed supplier `SeedIIAlt` is proved, using the previously constructed mixed Hilbert seed and the cited classical base-change, induction and temperedness theorems.** This is not the third-case seed or arbitrary-point automorphy. The proof is in [the shared manuscript](../paper/shared/rh-symplectic-induction.tex).

The construction is ordinary index-two induction from the real quadratic field in `T.Two.quad`. It preserves the original tower and coefficient embedding. It gives:

- One marked integral lattice with the precise residual support, a nonzero entry in the required alternative, the exact multiplier and killing condition.
- Explicit lower symplectic flag matrices with unit denominators, entry (2,0) equal to ±1 and (2,1) in the maximal ideal. This preserves the literal `Fr.IsPair`, `Fr.Res` and `Fr.InV` conditions.
- Irreducibility on the original cyclotomic kernel inside the CM field, not merely on an open subgroup. A quadratic-character exclusion uses `Ok.g3'` and `Ok.g3`; the two different local weight multisets rule out an isomorphism of the two inducing factors there.
- A cuspidal attachment by cyclic base change and quadratic automorphic induction, with the source's geometric Frobenius normalization and all finite-place windows. Blasius's theorem for holomorphic Hilbert forms is used only in rank two.
- The precise character twist, squared weights, evenness and finite-order identity required by `IsSeedAlt`.

## Source check

Pinned revision: `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. Paths below are under `lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties/` unless noted.

| Source | Blob SHA | Checked interface |
|---|---|---|
| WeakShimuraTheory/NearSplit.lean | df515b5e784271bcb190297f00643300859160c9 | Tower, Ok, Two, Deep, Wts |
| WeakShimuraTheory/RedIdeal.lean | 47b5b4c76358745d25f5108f11b76d1d2d77f8e8 | IsPair, Res, InV |
| ModularityArgument/ThresholdArguments/DenseThresholdCases/PotentialModularityTower.lean | b4a35b6314a7b356694b56f4b5500e5d023b1e33 | IsSeedAlt, SeedPairAlt, SeedIIAlt, PMExAlt |
| IdeleGenerators/QuadraticSplitting/QuadSplit.lean | 75ea610c302191d6be44fb6a28f291bbe0d22e50 | induction and marked matrix contract |
| ModularityArgument/AutomorphyLifting/PrimeIndexConstruction/ContRes.lean | af78dabc6988a33708fada6a51f70be3a8afb02e | mixed seed admission |
| BuildingsResidueChars/GaloisCharacterResidualDecomposition.lean | a8c551b6196889592a79409a8230d4ecf64fb4e4 | residual identities |
| BuildingsResidueChars/ExistsRibetLattice.lean | cdc30770a6b2b2d31cc2e7c8403271db47be1544 | marked integral lattice |
| BuildingsResidueChars/SymmetricSquareMixedExists.lean | 7f031be98299bd9eb789dcdd5f3a2f5789627c74 | index-two induction, not a symmetric square |
| BuildingsResidueChars/MixFlagExists.lean | 0258cc184d0501e0a68e8eeb9e82f5d28c664ac1 | both lower flag charts |
| BuildingsResidueChars/InducedFlagCondition.lean | 160c12844ca7711a7d65751a48ad6215cba6a9e7 | original local groups |
| BuildingsResidueChars/InducedDeletionCondition.lean | 75461c26d99657247bc28bfa21c63c721a8aa865 | character twist |
| BuildingsResidueChars/InducedIrreducible.lean | 49eba375c15f91f818f502d12dadd38023db96c7 | irreducibility on the cyclotomic kernel |
| BuildingsResidueChars/ResidualCharactersPsiNe.lean | 74cdf2994697a4ead33283c6b8fc8bfc9c7cdc3d | exclusion of quadratic character |
| ModularityArgument/ThresholdArguments/DenseThresholdCases/BirthSeedII.lean | b2ade834411b5e6e8bbbe2c4672fbfdc973ed427 | literal final assembly |
| ModularityArgument/ThresholdArguments/DenseThresholdCases/BirthIndS.lean | 9e2cce4e9cf11be5df0ef1033e8e74d00763e284 | attachment to original CM field |
| ModularityArgument/LeviSmoothLocalization/WinUpDown.lean | 8c9a100542cbcd6feecc899d9abd540b7943020f | local window |

Classical references: [Henniart 2012](https://numdam.org/item/10.24033/bsmf.2622.pdf), Theorems 1–5 and concluding remark in §3.7, and [Blasius](https://arxiv.org/abs/math/0511007), Theorem 1. Their hypotheses are explained in the proof. The exact SymPy diagnostic [check-rh-symplectic-induction.py](../scripts/check-rh-symplectic-induction.py) was run successfully on the symplectic form, marked matrix and both flag charts. This diagnostic is not a substitute for the proof. No Lean execution or independent manuscript review is claimed.

## Remaining frontier

The next separate input is `PMExAlt`: a single potential-modularity ideal with its finite-weight, characteristic-prime propagation, seed membership, purity and arbitrary-point automorphy clauses. The [deep Case II residual chain](rh-case-II-residual-chain.md) now proves residual linkage. Component transport across those links still has to be established. The rank-four seed does not supply those clauses by itself. The whole W04 node and the three point premises (F), (E), (A) are not closed.
