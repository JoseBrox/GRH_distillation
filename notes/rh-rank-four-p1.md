# Rank-four characteristic-prime curves: the original p1 clause

**Status:** the original `PotentialModularityTower.p1` clause for the same sum of two ordinary Hecke image ideals is proved using the previously established ordinary P1core theorem. See [shared proof](../paper/shared/rh-rank-four-p1.tex).

The local distinctness assumption gives a single cyclotomic-kernel inertia element whose four eigenvalue ratios all have infinite order. Clifford's elementary sum-of-translates argument and the source's quadratic self-twist exclusions first give irreducibility on the CM subgroup and then on its cyclotomic kernel. The identity component of the latter's Zariski closure acts semisimply without repeated constituents, since it contains a torus with four distinct weights. Four one-dimensional summands are ruled out by the residual ratio of order greater than four: the residual ratios would factor through a subgroup of S4, whose cyclic quotients have order at most four. The remaining connected cases are dimension four or two blocks of dimension two. A degree-four Newton polygon, with a separable binomial on a possible length-two edge, produces a simple spectrum in each preserving coset. For an interchanging coset the characteristic polynomial is a quadratic in the square of the eigenvalue; the leading trace and determinant degrees imply separation. Consequently the simple spectra are dense in the precise cyclotomic kernel required by the source's N3. The remaining NiceI conditions follow from local distinctness and the original distinguished-place Frobenius condition. P1core transports support to all primes below each link curve and hence to all primes below the original curve.

## Pinned interfaces

Revision `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, paths relative to `lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties/`.

| File | Blob SHA | Use |
|---|---|---|
| WeakShimuraTheory/NearSplit.lean | df515b5e784271bcb190297f00643300859160c9 | U1, Ok.g2/g3/g3'/ord |
| WeilGroupCharacters/UniversalOrdinaryDeterminantRing.lean | 65ce51224af6634182dda7b48716e73279990d15 | NiceI and P1core |
| WeakShimuraTheory/CompactIntegralFields/H4.lean | 064d21fe4cbf75a1df92adab8fde40ecf6b3cbdb | original rank-four NiceI criterion |
| WeakShimuraTheory/StabilizerIndexBounds/NonComm.lean | 18658b799c7edeeb331cafb472095451b3fbaccf | exclusion of virtually abelian monomial case |
| AlgebraTools/MonomialRepresentations/RegCosetFour.lean | 7210bec0c83ccbb69b220fbb4475ca5109f0c4ca | simple spectrum in every open coset |
| ModularityArgument/ThresholdArguments/DenseThresholdCases/ModularDeformationQuotientRegularAtPoint.lean | see pinned file | original P1core-to-LocZero consumer |
| ModularityArgument/ThresholdArguments/DenseThresholdCases/PotentialModularityTower.lean | b4a35b6314a7b356694b56f4b5500e5d023b1e33 | p1 conclusion |

## Remaining frontier

The single ideal now has fin, seed and p1, and weak purity at the remaining RH weights, using the already established ordinary quotient. The remaining local component presentation, reducible-locus and irreducible-fibre dimension bounds, and the residual-chain transport are separate. The full PMExAlt aut clause requires the stronger local windows and descent; the RH-specific route only needs fixed-field attachment. No independent review or compiled manuscript is claimed. No whole proof-map node is closed.
