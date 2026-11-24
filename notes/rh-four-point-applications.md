# Rational-point support, endpoint exclusion, and fixed-field descent

**Status: written reconstruction of the RH-specialized point-arithmetic completion.** This is not an independently checked proof or a Lean replay. The [shared proof](../paper/shared/rh-four-point-applications.tex) supplies (F), (E), and (A) from the earlier reconstructed suppliers, not the full general Dirichlet PMExAlt.aut.

- The exact nonsplit extension of a block endpoint is obtained from the rank-three square-zero symplectic module Hom(U,V) with its symmetric-map condition. Complex conjugation acts by -1; the ordinary condition cuts the local module to a rank-one flag-preserving summand. BU8 kills the needed local and global dual invariants. Finite Poitou–Tate yields at least q^j normalized pairs at precision j. Divisibility and finite inverse limits produce a nonzero integral cocycle with the original local coboundary parameter. Its block triangular twist preserves every characteristic polynomial, the original inertia conditions, and the Small condition. Normalization at c prevents a splitting.
- The rational lattice, three polynomial links, uniform cocycle bounds, sufficiently deep layer, and common coefficient space now put each actual Star pair on the same ordinary image ideal as the arithmetic seed.
- In characteristic ell the finite-weight clause forces constant residual characteristic polynomials, first on the deep tower and then on all rational group elements by taking powers. This excludes both forbidden curve types by the actual trace-algebra criterion (F).
- In characteristic zero the same-ideal arithmetic purity clause forces equality of good-prime eigenvalue magnitudes. The ratio p^2 of the two block determinants contradicts even one strict common half-power window, proving (E).
- The fixed trace field K' is selected before any point-specific tower is constructed. All auxiliary tower primes avoid its ramified prime. An abelian-quotient restriction argument excludes self twists of order dividing four, using distinct residual characters over L and ramification at the fresh prime for LK'. Thus irreducibility holds over L and LK'. Solvable base change and descent transfer the ordinary cuspidal attachment from L to the same K' for every original point, proving (A).

The existing conditional integral comparison then gives the individual polynomial length bound with an absolute exponent, without charging the auxiliary tower degree. This remains subject to audit of the entire new chain of conventional proofs. The moving weighted Selmer product is still to be assembled. The full local WitA/PotUnl and arbitrary Dirichlet conclusions are not claimed.

## Source interface and published input

Pinned revision: jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de, paths relative to lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties/.

| File | Blob SHA | Use |
|---|---|---|
| WeakShimuraTheory/NearSplit.lean | df515b5e784271bcb190297f00643300859160c9 | Small, KPair and rational point interfaces |
| WeakShimuraTheory/CompactIntegralFields/NotOver.lean | 9ca534a17dc1b269e7a658544c3767cf39b55260 | original nonsplit block extension bl |
| ModularityArgument/ThresholdArguments/DenseThresholdCases/Gsp4PromodularityCaseTwo.lean | 1b2a538376dacc6874911570832aeb5f829e9ec3 | exact last_step and rational support |
| WeakShimuraTheory/CompactIntegralFields/ChainDesc.lean | a76832ab2ea0aadbb261997fca8cded083798de5 | common residue chain |
| WeakShimuraTheory/CompactIntegralFields/SmallCo.lean | 3cdbd3c52024ba6500e253a8a34732633ec4e685 | finite coefficient realization |

Published descent: T. Barnet-Lamb, T. Gee, D. Geraghty and R. Taylor, [Potential automorphy and change of weight](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n2-p03-p.pdf), Annals of Mathematics 179 (2014), 501–609, Lemma 2.2.2. The irreducibility and polarization hypotheses have been checked in the written argument; no adequate residual image is assumed for this descent theorem.

No whole proof-map node is closed by this package. Independent review and compilation are pending.
