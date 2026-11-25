# Exact generic gluing mass and block-end telescoping

The new supplier is [flag-generic-gluing-mass.tex](../paper/shared/flag-generic-gluing-mass.tex). It continues the fixed-cell and integral-class results in [flag-generic-global-classes.md](flag-generic-global-classes.md).

**Proved.** For the actual corrected primitive lattice, with complement rank l=k-1, the definite gluing mass is exactly the unimodular rank-l mass times the determinant factor, the finite Euler factors from l+1 to n, and the primitive densities. The proof computes the local fibre Jacobian and cancels the complement gauge against the classical Hermitian mass formula (MM6). In particular the mass is not merely an unspecified finite-place proportionality constant. The primitive density formula itself is older; its coarea use and this normalization are the new steps. The determinant calculation works also at the split and dyadic places. The argument uses the previously cited classical mass formula; it is not a new proof of that theorem.

**Proved.** On occupied cells the exact primitive density product is bounded by twice the original alpD product for k >= m+f+5. The block-end determinant factors telescope with exponents t_i+t_(i+1), and last exponent t_b-1. Hence nPt >= NG^(k-1), removing the original Htot^(6m) loss. Together with GC7 the generic mass loss is only Htot^(s(s-1)) at the arithmetic stage.

**Still conditional.** GM12 is the original-normalizer comparison conditional on GM11 (the equality identifying cExpl*massRows*product(alpD) with AA*g^(mfl)). That equality is not derived merely from the gluing mass. The original arbitrary-selected-to-pinned real quotient measure comparison and the analytic uniform rotated Bessel point sum also remain open; no closure of StepLocGenPinnedG or StepThmBPinnedG is claimed.

## Source dictionary

Pinned source: jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.

- Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/StepsR.lean, blob ec4f4d5d8e82a6e53c03d18bedf8eec77b91492d: cMass, cExpl, IsGlueReps.
- Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/DataInst.lean, blob 0faa5aa11af43f784043da332f8075db9b8cf734: alpD.
- Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RowsConc.lean, blob 33aa2cac882fa5e1f0e6472274e570655235aa64: NGPt, NDPt, nPt, HPt.
- Development/AbelianVarietyTheory/Proofs/FlagMeasures/GramInvariantPowLeHaarWeightStatement.lean, blob 502d09e452450857094861430e24c021cedad3e2: old H^(6m) loss improved by GM10.
- Development/AbelianVarietyTheory/Proofs/FlagMeasures/MeanCountConstantEqUnscaledMainConstant.lean, blob f9e854f2408faf59e13d1e23e54a83d7301d4d8b: countConst_eq_unscaledConst, the remaining GM11 normalization. Its proof relies on the actual NcAllC, mass-data and measure comparisons, not just the explicit mass count.
- Development/AbelianVarietyTheory/Proofs/FlagMeasures/FamilyGenericMassPositiveBoundedProof.lean: consumer of these inequalities.
- Existing mass formula and primitive-density references: [maximal Hermitian mass](maximal-hermitian-mass.md), [signed primitive density](global-norm-frontier-primitive-density.md).

The proof is mathematical; it has not been checked by Lean or a manuscript build.

**Continuation:** [Exact AA normalization](flag-aa-normalization.md) now supplies GM11 under the original measure and row hypotheses, hence the mass comparison GM12. The pinned real comparison and weighted point sum remain.
