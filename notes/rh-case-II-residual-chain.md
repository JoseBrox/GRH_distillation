# Case II deep-tower residual linkage

**Status: the original deep Case II three-link chain supplier is proved**, using the preceding mixed rank-four seed, classical finite Poitou–Tate duality and Chebotarev. See [shared proof](../paper/shared/rh-case-II-residual-chain.tex). This proves the residual linkage, not yet transport of automorphic support across the links.

The new proof uses the dimension formula to impose a prescribed one-dimensional tame ramification image at auxiliary split primes while imposing zero cohomology classes at all old bad primes. A finite triangular coefficient module gives the required cup primitives simultaneously with a nonzero root cocycle. All marked and local coordinates are retained. The explicit symplectic matrix law gives the intermediate pair. A compositum of cyclic degree-ell cyclotomic subfields kills its auxiliary inertia; the class-two subgroup has exponent ell even at ell=3. A nonzero root cocycle remains nonzero on the deeper normal subgroup because its residual character is nontrivial there. The original flags are transported by their unique lower/upper triangular factorizations. The three links are polynomial identities using square-zero lower-block ideals, so the proof also works in small finite residue characteristic.

The next missing supplier is PMExAlt and the dimension/characteristic-prime component argument (ClassicalFixedByIwahori), followed by passage from the original rational characteristic-zero or characteristic-prime point to the tower. Existence of a residual chain does not imply that its components are automorphic.

## Pinned sources

Revision `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`; paths relative to `lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties/`.

| Source | Blob SHA | Contract |
|---|---|---|
| ModularityArgument/ThresholdArguments/DenseThresholdCases/Chain2.lean | bf12a8e491cdcf752a2a66edfef666462fb24aa8 | exact deep-chain conclusion |
| WeakShimuraTheory/CompactIntegralFields/GysinAl.lean | 2901c65ca195f425147a9dbe79b1ef4fed30e8d5 | common nonzero root |
| WeakShimuraTheory/RamifiedLineCharacters/GysinPsOf.lean | 8fa4a48a5772cb3eaf649a51b3de7c0b79b3880c | cup primitive |
| WeakShimuraTheory/RamifiedLineCharacters/MemRamLine.lean | 0fc92783833790d14e7ce659cb8f2f754487b4dc | precise matrix and local identities |
| WeakShimuraTheory/RamifiedLineCharacters/CupRaw.lean | 718d4d1a63e689a32ac09a704c69b612870157e3 | finite coefficient representation |
| WeakShimuraTheory/RamifiedLineCharacters/CupNorm.lean | b967b012aa64df7e0e90a3485e33be7110c75a2c | marked normalization |
| WeakShimuraTheory/RamifiedLineCharacters/GysCore.lean | 2ab497ddbdbeb4f341deda22b197d6364fd620ff | prescribed ramification |
| WeakShimuraTheory/RamifiedLineCharacters/OpenKer.lean | 9430bb8075ec98c1811f7c795d778a49db582fcc | actual killing set |
| WeakShimuraTheory/RamifiedLineCharacters/PlacesQ.lean | e8d2bb6dbb29fe574801ff4e631c193e0adfd1ca | rational split primes |
| WeakShimuraTheory/ResidualChains/ExistsResidualDatumOverRestrictionToRationals.lean | 4ed6f3e8741cb1fd1c5d832ad666b03dd28786f2 | original restriction |
| WeakShimuraTheory/CompactIntegralFields/FlagFacts.lean | 6a8bec1598915621b57119f1ddfdded0e7140863 | initial good alternatives |
| WeakShimuraTheory/CompactIntegralFields/DiesEx.lean | 01065c7d16839ddc5ed4a2bec0c72a75f8a14835 | finite auxiliary abelian extension |
| WeakShimuraTheory/CompactIntegralFields/RestrT.lean | 7bdfe84d8734c8634cbce35fd7b1cbc1cd3e9229 | transported flags |
| WeakShimuraTheory/CompactIntegralFields/GlobalTheory.lean | 6b0279ec5b8fbe065f1fb5cd97d38e339fe7afd7 | lower block interpolation |
| WeakShimuraTheory/ResidualChains/MovePs.lean | 4fce9cb20348e7bca51df3c2112944d58f72b218 | adjusting local flag to the seed |
| WeakShimuraTheory/ResidualChains/LvSmulOne.lean | 67c7e603f56be2f8b6f42209b3c73f58629d636c | Levi projection |

No independent review, compiled manuscript or Lean execution is claimed. No whole proof-map node is closed.
