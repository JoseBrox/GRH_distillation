# The common coefficient space for RH rank-four propagation

**Status:** conventional proof of the original SpaceEx and simultaneous finite coefficient realization for the actual fitted deep RH towers. See [the proof](../paper/shared/rh-four-common-space.tex).

The universal diagonal framed ring with independent local characters admits a completed weight decomposition. Its weight-zero part is a complete Noetherian ring (finite monoid generators), whereas its finite sums of homogeneous pieces form the required finite-type entry algebra. Dickson's lemma yields the adic continuity comparison. Every invariant entry monomial is a product of cycle traces up to known similitude units: flip a path by reverse-complementation using the symplectic inverse identity, reducing the only possible imbalance vector (c,-c,-c,c). This gives integral coefficient uniqueness including at ell=3. Adjoining flags and imposing the exact equations gives the original Space.

For nonsplit residues the complete diagonal universal ring does not directly represent the lift. The proof rescales with a cocharacter positive on nP or nM. Modulo each Artinian precision the ring R_m[[z]][I_m z^{-D}] contains the rescaled diagonal lift; the nilpotent ideal makes it complete local. The image of each homogeneous piece is a single Laurent monomial, so z=1 evaluation is valid on finite sums. Taking compatible limits supplies the original lift maps. Polynomial residual links give constant coefficient maps by characteristic-polynomial and character uniqueness, then descend from k[[t]] to k[t].

The same coefficient ring can contain the finite seed and link data and all finite polynomial residual coefficients. Both mixed-characteristic and equal-characteristic Small DVRs admit the required finite enlargement.

## Pinned source audit

Revision `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, paths relative to `lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties/WeakShimuraTheory/`.

| File | Blob SHA | Contract |
|---|---|---|
| CompactIntegralFields/SpaceEx.lean | 2fd4ce1566c6b1d1565235bf0e0004b0fa04e5e2 | all original space fields |
| RedIdeal.lean | 47b5b4c76358745d25f5108f11b76d1d2d77f8e8 | Space, IsRes and Linked |
| AdicExtensionMatrices/UnivRep.lean | e58146aae0daebf8c5f67b12be6fe1abf675c642 | original diagonal framed universal ring |
| AdicExtensionMatrices/SxUnivD.lean | a91f4e6f45fd585c9b8f206db3a0c2bd32671ab1 | independent local characters |
| AdicExtensionMatrices/SubMemMax.lean | 77127a3b91f4851ad1359948532ac13c1cbb9cb8 | homogeneous coordinates |
| AdicExtensionMatrices/EqMono.lean | aec1dfb35a7f47c68a872b945d33174a01012640 | invariant coefficient recovery |
| AdicExtensionMatrices/GenZero.lean | a5ed15a06c2289e76dd6bd34dc072fd2e7fca578 | coefficient-generation contract |
| AdicExtensionMatrices/PairNear.lean | f29c896541ce93cf0999f8eaee99fad51b0010b5 | cocharacters on the two residual supports |
| AdicExtensionMatrices/PreOfCore.lean | e3e25e6948c8c7d4a2675aa537b244608b4a5403 | adjoining flags |
| AdicExtensionMatrices/PreLine.lean | 461a9184fc6608635f81d6d2d039dc36c8485182 | polynomial residual link maps |

This proof has not been independently reviewed or compiled. It addresses the space interface, not yet the final point-exclusion and fixed-field automorphy conclusion.
