# W08: integral class summation in the generic rational cells

**Status:** arithmetic local-to-global class product, original weighted genus unfolding, absolute height, and phase-sensitive pinned class sum. [Proof](../paper/shared/flag-generic-global-classes.tex).

At each occupied nonzero-Gram point, fix its two rational flags, its common unipotent S and its positive definite complement H. The original generic local estimates in [flag-generic-local-amplitude](flag-generic-local-amplitude.md) are combined with the following exact comparisons.

* GC1: global integral lattice orbits under S(F) are the restricted product of the local term orbits over a fixed datum. This uses finite lattice patching and additive strong approximation for the explicit block-unitriangular S, not strong approximation for the compact-at-infinity complement H.
* GC2–GC3: the relative stabilizer weights multiply, so the complex amplitude of the entire generic integral class is the product of the local amplitudes. At good places there is one orbit of weight and phase one.
* GC4–GC5: the source row key is the pair of original row lattices, their actual relative quotient graph and their rational unipotent double coset. Its orbit mass over one datum class is exactly the reciprocal of the complement datum stabilizer order. The genus sum is V0 times the product of the local reciprocal volumes.
* GC6: the exact height product is Htot = g^(-(2r+1)f) NG ND, with the original scaled endpoint determinants and level corrections.
* GC7: the generic mass is the fixed-frame definite gluing mass times the product of the original local frame weights. In particular ngenTot <= Htot^(s(s-1)) glueSum, improving the original intermediate exponent 3s^2. It is positive and finite.
* GC8–GC10: on a genuinely pinned real cell, the covolume is g^(-f #FreeE(w)) times the relative global mass. The finite phases multiply using c_v g = delta_v theta_v and the additive product formula. The squared norm of the original sum of generic integral returns in a fixed key is exactly the squared row weight times g^(-2f #FreeE(w)), the squared pinned orbital norm, and the product of the local generic squared amplitudes. No integer multiplicity is discarded.

The residue-field primitive density formula itself was already established in [the signed primitive-density refinement](global-norm-frontier-primitive-density.md); the new local argument in the preceding commit gives an independent elementary uniform bound and its saturation-mass / integral-frame-class consumer.

The arithmetic class comparison is not a new proof of the analytic uniform pinned point sum. The actual bounded scalar transition for every selected real quotient measure, and the exact normalized mean constant comparing glueSum to AA, remain to be supplied before closing StepLocGenPinnedG. StepThmBPinnedG still requires the weighted archimedean orbital estimate with its joint Jacquet norm.

## Pinned source interfaces

All paths refer to lean/src at jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.

Under Development/AbelianVarietyTheory/Definitions/SemilocalFrames:

- GFrames.lean (01781dbf051eb4692966d1cc007c35c55f95c929), definitions of c, IsTerm, LRel, mu, om, amp, sumD, ngen.
- LocClosed.lean (5493bb37c6e063eaea459cea038dd85357b209c9), definitions of Adapt, gdat, KeyEq, LocOver, InGen, massA, key, ClsRow and LocClosed.

Under Development/AbelianVarietyTheory/Proofs/FlagMeasures:

- ExistsTermOfGlobalTermStrongApprox.lean (fb618339640230b5ee2fda311692d116cc91c500), lines 174–225, local witness to actual term.
- TermRowEqIffMovedLatticeInnerDataEq.lean (6c3641ece9ac367aaafd74fdc10b82379187ec08), lines 16–40, graph/row equivalence.
- OrbitCountRowsDoubleCosetsInnerDatumClass.lean (42975f556b04da8de3a4eeef6b0b415f9ad0bdbb), lines 65–end, stabilizer index and squared row weights.
- RowWeightsLocalOrbitsSumEqGenusMass.lean (00717cc90c3daf77f45e781795f661292de58e69), rows_mass_genus.
- LocalHeightBasePairEqModuleProduct.lean (26d65f184d0377c52d1d616847dd8061d034e29d), 160–305, determinant scaling.
- GenericMassLeHeightPowMulGluedCount.lean (292ca52dabd9e5589ddf87a4b13b6f3829ef5d8a), genericMass_le_heightPow_mul_glueSum.
- CovolumeIntegralStabiliserNormalisedHaar.lean (856dbd1415ac8281df03a343e856b62bff4eae1f), const_entry and covolume_integralStabiliser_normalisedHaar_alt.
- MatEqOfIndep.lean (a9dd70ea6ab2c37d989ffb4952353c34de65ef77), dict_coords; StMatIntIff.lean (3c40c129954879e166ad2f3a1e989fdd9f383a99), stMat_int_iff.
- PsiOfEq.lean (5188ee754474b490e08258ed73e42c4c6214897b), psiOf_eq; LocalScalarMulEqDifferentGenMulTheta.lean (09d4c45ee2e8d847bfcce9cf3011c1bc076ff468), GCoord.c_mul_gS_eq_delta_theta.
- MovedTermLatticeIsGlobalTermPhase.lean (3206a9f842f5fd11e93515b10fc8929b70555b30), main; RowTermAmplitudeEqMassMulPhase.lean (29c62073075ebc7687dae206d9bdc4241efd5e06), 67–112; RowDoubleCosetSumNormSqBound.lean (32f443b691b03a3ddb0f511ccb5af86e293d1727), row_coset_sum_norm_sq.

The proof uses standard lattice patching, adelic quotient integration and finite genus finiteness. It is not a Lean replay. The exact pinned covolume and phase equations are derived in the original coordinates; no bound is claimed for a different arbitrary real Haar normalization.

**Continuation:** [Generic pinned local supplier](flag-generic-pinned-input.md) now assembles the actual StepLocGenPinnedG. The real weighted point sum remains.
