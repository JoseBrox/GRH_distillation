# The original Case II starting tower and rational marked lattice

**Status:** proved the RH specialization of the original initial tower, labels, lat, and restrQ suppliers, retaining the actual KPair, Star alternative, Small coefficient condition and inertial labels. See [the proof](../paper/shared/rh-four-rational-lattice.tex).

The real abelian tower is defined by two independent finite conditions, y=phi and eta=eta', using three new quadratic characters of distinct prime conductor. The original RH psi has power-of-two order, so no separate l-primary cancellation is needed. The local witnesses at 2 and l use the actual nII conductor inequality. Three independent fresh-inertia sign changes give the global witnesses for every root-product condition, the quadratic permutation exclusion and the distinct mark.

The lattice proof replaces the six-case root-system linear program by a direct lexicographic maximum. After Hensel diagonalization at the mark and symplectic Gaussian elimination of the actual flag, only the lower flag weight -wPs can have valuation zero. Maximize b then a in the rational polyhedron of the eight root valuations. The earlier odd strict-cocycle theorem shows that absence of -wAl implies absence of -wTh, and absence of wBe and wPs implies absence of -wAl. A feasible-direction argument therefore forces wBe tight, hence a>b>=0, excludes all roots outside nP, and then forces -wPs tight. This proves LatShape, including the non-coboundary alternative, after a finite extension of the actual coefficient DVR.

The original rational flags transport to every deeper tower because the leading minors of the product of an nP residual matrix and qQ flag are units. The ordinary inertial characters are preserved, and the original Mu torsion condition follows from their exact finite-order and cyclotomic factors.

## Pinned source audit

Revision `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, paths relative to `lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties/WeakShimuraTheory/`.

| File | Blob SHA | Contract |
|---|---|---|
| NearSplit.lean | df515b5e784271bcb190297f00643300859160c9 | Amb.Small, KPair, QPair, LatShape, Tower, Ok, Two |
| FrobeniusFields/QuadEx.lean | 5c93c3a5a0c10614bb4f180bb504f10a8941f637 | three independent quadratic choices |
| FrobeniusFields/Adj2.lean | 891b2a5b5efaad5f59dac2eba40d2a72f843e2a2 | sign changes at fresh inertia |
| FrobeniusFields/OddPowNe.lean | 05f3783b15736a9d86acdc9568cc332bbdf71303 | witnesses for Ok.g2/g3/g3'/ord/dist |
| FrobeniusFields/Two2.lean | f7ae09d7474692265b683ed8b382c985182cd57b | original Two properties |
| FlagsAndDiagonals/ResFlag.lean | 9659d03bf4d2d90e8be7a6cd4050a96b991936d2 | residual leading minors |
| CompactIntegralFields/Labels.lean | 88a3fc01e0610a55f5777fee4928095ff3f2b449 | labeling and marked flag reduction |
| FlagsAndDiagonals/StarConj.lean | 10d8b5f0da9218779421b0e4b1df1fc2b4e51036 | Star implies StarE after conjugation |
| CompactIntegralFields/RootSystemLinearProgramCases.lean | f3e73f032d4d57a4a6d671cfb238ffa6a0c256a3 | original finite root LP |
| CompactIntegralFields/LatSix.lean | b6b78f3b99b05d8f503fc3949b01d2de9de4d5f0 | actual residual lattice target |
| CompactIntegralFields/RestrQ.lean | 4baff32652ab8cdb00e764fee2a134e19e438c89 | flag transport and inertia |
| RedIdeal.lean | 47b5b4c76358745d25f5108f11b76d1d2d77f8e8 | exact support sets and cocycle conditions |

This is the ordinary RH Case II specialization, not a proof for arbitrary Dirichlet twists. The initial fields and further auxiliary primes can avoid the fixed trace field's discriminant. The universal finite-type space and its simultaneous seed/target coefficient realization still need to be supplied in the conventional proof; the last application of propagation is not claimed here. No independent review or manuscript compilation yet.
