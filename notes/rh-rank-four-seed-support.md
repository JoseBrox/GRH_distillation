# Rank-four seed support and the anticyclotomic ordinary ideal

**Status:** the seed-support implication, including the original all-primes-below-the-seed conclusion, is proved for the actual ordinary Hecke quotient and the original link maps when supplied. The infinite-order twisting invariance of the same ideal is proved. This is a direct replacement for the characteristic-zero use of the source's adjoint-lifting theorem; it is not yet PMExAlt.

The detailed argument is in [the shared manuscript](../paper/shared/rh-rank-four-seed-support.tex).

- The already constructed ordinary `ModU` quotient has finite torsion-free weight algebra and the full arithmetic occurrence and finite twisting clauses. Introduce a formal anticyclotomic variable; evaluate its finite-order specializations, use Weierstrass preparation and density, and specialize at the required principal unit. This proves equality of the image ideals for the original twists, not merely equality of their characteristic-zero points.
- At an actual irreducible seed of the ordinary determinant ring, Chenevier's theorem lifts every fixed-weight dual-number determinant to a representation. The ordinary product equations give the entire labeled flag. Crystallinity of all extensions after a finite local extension follows from the local Bloch--Kato and Euler characteristic formulas because the gaps are at least two. At the distinguished place the residual Frobenius ratios are one, whereas the residue cardinality is not one modulo ell. This forces the infinitesimal inertia restriction to vanish. The symmetric conjugate pairing produces the polarized adjoint over the real subfield. Thorne's 2022 theorem now applies with precisely the cyclotomic irreducibility hypothesis of the seed. All relative tangents vanish.
- Finite torsion-free weight support and the vanishing relative tangent imply that the original local determinant ring is regular at the seed and its Hecke ideal vanishes there. This controls **all** primes below the seed kernel, even if they are not themselves arithmetic points.
- For a supplied original `Link` and maps `IsPhi`, parity selects a twist by beta^0 or beta^1 giving integral weights. The paired cuspidal seed becomes an ordinary arithmetic point of the same quotient. The image-ideal equality transports the local vanishing to the untwisted image ideal. Taking two links preserves the seed condition for their sum.

## Pinned source audit

Revision: `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. Paths below are relative to `lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties/`.

| Source | Blob SHA | Exact use |
|---|---|---|
| WeilGroupCharacters/UniversalOrdinaryDeterminantRing.lean | 65ce51224af6634182dda7b48716e73279990d15 | lines 131–188: determinant, polarization, ordered products, inertia, weight map |
| WeakShimuraTheory/IsAlgClosureField.lean | 59667119383f64652253bc8abdb342394326a8fa | Link and IsPhi |
| ModularityArgument/ThresholdArguments/DenseThresholdCases/HidaModularIdealMap.lean | 578481684dd7c473c1f4953d04b8f1a6a774960f | exact twist-ideal equality |
| ModularityArgument/ThresholdArguments/DenseThresholdCases/EigenbasisRankFour.lean | ca0036e7a1ea8d6dc207372af19cba99ea286c84 | fixed-weight tangent argument and support implication |
| ModularityArgument/ThresholdArguments/DenseThresholdCases/BirthPm.lean | 9e0b1de2618efff0ad14a05180b827e2be5a8dfd | seed parity and literal LocZero consumer |
| ModularityArgument/ThresholdArguments/DenseThresholdCases/PotentialModularityTower.lean | b4a35b6314a7b356694b56f4b5500e5d023b1e33 | exact seed condition and five PMExAlt clauses |

Classical references: [Chenevier, Theorem 2.22(i)](https://gaetan.chenevier.perso.math.cnrs.fr/articles/determinants.pdf); [Thorne, Theorem 6.1](https://arxiv.org/abs/2207.04925), also used in the existing rank-four rigidity proof; local Tate duality and Bloch--Kato's local dimension formula.

## Remaining frontier

Construction and verification of the original links and determinant maps remain to be assembled; the characteristic-prime curve clause still requires the rank-four regularity and component dimension arguments. In particular this is not a proof of the stronger `ModUAlt` local automorphic windows, and does not identify that condition with the established ordinary `ModU`. No proof of PMExAlt or whole-node closure is claimed. This new proof has not yet had a separate independent review or manuscript compilation.
