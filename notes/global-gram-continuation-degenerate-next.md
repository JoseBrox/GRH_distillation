# The remaining arithmetic degenerate-orbit sum

The actual all-length tails, common-stabilizer fibre estimate, and
local degenerate orbital operator now have complete proofs:

- [All flag lengths](global-gram-continuation-length-tail.md).
- [Original fibre measure](global-gram-continuation-degenerate-fibres.md).
- [Original local operator and moment allowance](global-gram-continuation-degenerate-operator.md).

These results retain the original arithmetic objects and measures.
They do not yet complete the diagonal zero-Gram obligation.

## Exact next theorem

For each original arithmetic word `u`, the original relevant
nonidentity zero-Gram orbital series is absolutely summable, and its
operator `K''_uu` satisfies

```
||K''_uu||_HS^2 <= dim(pi_u) exp(-k f log k).
```

Prove this for the actual global double cosets, original local
stabilizer measures, global masses, phases and normalizing constants.
The ordinary-RH specialization retains its growing field and rank.
Generic returns and the final arithmetic Gram comparison are separate.

## Available input and first missing step

At every real place the actual normalized orbital operator obeys

```
||J_gamma||op <= (kappa/s) 16(4r+4)(4r)^(4r^2)
  (2H)^(16r^3+4r) Delta^(8r^2+2)
  (8 pi e/(k-1-j))^(j(k-1-j)) |D_j|^(-(k-1-j))
  sigma^(-(q-16r^3-4r-1)/r),
```

where `H=b^(CH m)` and the literal original moment range permits
`q=floor(C1 k r)`. Both branches of the original shift bound and
the large-weight interval have been checked; the family is unchanged.
There is no compact representation dimension in this operator bound.

The first remaining argument is the arithmetic weighted count with
the actual global stabilizer masses and row-lattice pair counts.
The direct zero-Gram chain is `KloostermanCosetSumLe`, followed by
`PairsDegCutCOfSteps` and `KloostermanDiagonalOfConditions`. Its
fixed-label bound combines the local amplitudes with a genus average
of embedded lattice pairs. The nonarchimedean nongeneric density in
`NonGenericLocalBound` belongs to the separate nonzero-Gram chain;
it has not been identified as an input of this zero-Gram argument.
It is also different from the established generic local density.

## Bounded source restart

All sources are pinned at
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
Use `scripts/source_excerpt.py --atlas --source MODULE --lines A:B`.
The following exact modules are cached; inspect their mathematical
arguments and dependencies before claiming the global sum.

| Module | First target | SHA-256 |
|---|---|---|
| `Formalism.SharpRestriction.CuspSpanNormBounds.KTwoCosetCount` | weighted coset sum, near line 164 | `0833db3563622d8a16b4f5e55a10a86ba4844c2f00f59c5b2b9310c9c4432044` |
| `Formalism.SharpRestriction.CuspSpanNormBounds.KTwoMinorIntegrality` | actual integrality and lattice-sum predicates | `5b7898f27c580aba1fefa827ae2f05d37d80086b0cbe6811e54293c48ff50995` |
| `Formalism.SharpRestriction.CuspSpanNormBounds.NonGenericAndKTwoTheorems` | local density, lines 22–28; exact target, 54–57 | `edc6d58c4a57d36bdf2733a9bfe6484d45189e3736ba36d4370d6e44ad80deb0` |
| `Development.AbelianVarietyTheory.Proofs.FlagMeasures.EqualWordsNonGenericEstimatesChain` | global assembly and its genuine suppliers | `090025d72c7beb50fdcdd8c2d15abeb9018787dc546a077f2caf3dbd0d1fafad` |
| `Formalism.LocalToGlobal.SiegelLatticeTheory.CokernelGLCounts.RankPointCounts.NGAnalytic` | arithmetic constants, lines 161–185; local sum, 298–330 | `39986b93e81209aa9f66db9986ec5ee3a08991fb22b11a70d32296d4ab61f6ae` |

The operator normalization is in `RelevantZeroGramTerms`, lines
412–417. The latest local proof certificate is
`certificates/global-gram-continuation-degenerate-operator.json`.
No Lean build is claimed.
