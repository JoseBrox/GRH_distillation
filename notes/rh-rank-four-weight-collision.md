# Rank-four finite-weight collision estimate

**Status: proved the original `off_diagonal_nilpotent_rank_four` dimension bound from its finite-weight hypothesis alone.** This is a conditional supplier for the characteristic-prime component argument, not a construction of the ordinary automorphic ideal and not a new whole-node closure.

The [shared proof](../paper/shared/rh-rank-four-weight-collision.tex) uses local class field theory, the original diagonal-character equations and Krull's height theorem. For the original prime q containing J and the coefficient uniformizer, coincidence of two distinct local characters on T.U1(v) implies

    dim(B/q) + d_v <= 2d + 1,

where d_v is the actual common local degree and r*d_v=d. Two opposite pairs of graded characters give at most 2d independent inertial parameters. The collision removes d_v-1 parameters; the remaining cyclotomic direction costs one parameter. All subsequent prime quotients are domains in characteristic ell, so the pro-ell principal-unit targets have no torsion. This treats ell=3 without any division by ell, and retains the exact inertia restriction rather than just a chosen open subgroup. The finite-weight condition implies that killing the exhibited parameters leaves a zero-dimensional quotient.

At the original threshold d>=30(C+1)^2, r<=C and N=2d+1-2r, both required strict inequalities of ch_core hold.

## Pinned source audit

All files below refer to `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

- `ModularityArgument/ThresholdArguments/DenseThresholdCases/OffDiagonalNilpotentRankFour.lean`, blob `65b45b2eb21068455400806d1bd8e1653ed034ce`: precise weight-collision contract and parameter count.
- `BuildingsResidueChars/DeformationSpaceLocalCharactersContinuous.lean`, blob `0ead952ef698085830d3b31e984c7e6acfdd5a82`: actual local characters, residue-one condition and opposite pairs.
- `WeakShimuraTheory/NearSplit.lean`, definition of Tower.U1 (lines 203–204): inertia, cyclotomic kernel and trivial residual representation.
- `ModularityArgument/ThresholdArguments/DenseThresholdCases/ClassicalFixedByIwahori.lean`, blob `0316320a19911532bdbd44f882225fa0d8dfc619`: exact characteristic-prime component consumer.
- `ModularityArgument/ThresholdArguments/DenseThresholdCases/PotentialModularityTower.lean`: fin, p1, seed, pur and aut clauses, with the actual single ideal retained.
- `ModularityArgument/ThresholdArguments/DenseThresholdCases/PmTwo.lean`, blob `5adaa1584a8c10c80aeb9465bf178a7780bccd0c`, and `PmExTh.lean`, blob `86074391c1e4ef4c5fa800b9802b31eed2eb895a`: the source forms its ideal as the sum of the images of two ordinary Hecke ideals. Merely choosing the union of automorphic components at the new seed is insufficient.

## Remaining barrier

The constructed residual chain must be accompanied by the original automorphic support propagation. In particular the two-link ordinary Hecke-ideal construction needs its finite-weight property, the seed-local-zero assertion (from the original adjoint-lifting argument), regular characteristic-prime curve propagation, purity and descent. The dimension estimate proved here is one part of the component step; the local normalized chart, the reducible-locus and irreducible-fibre bounds and the full same-ideal construction are not being claimed by it. No new whole-node closure, Lean execution, independent review or compiled PDF is claimed.
