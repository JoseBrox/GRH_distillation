# Full second-type local cancellation

[Written proof STC1–STC9](../paper/shared/flag-second-type-cancellation.tex).
This completes the missing small full-image branch left by DS4, and in fact gives
the complete second-type estimate without counting families. The proof retains
the actual datum, graph congruence, phases, and both reciprocal-stabilizer weights.

- STC1: a unimodular orthogonal summand of rank rho=k-2r-3 inside the complement lattice gives uniform quadratic Fourier cancellation, including nontrivial characters of arbitrarily high conductor and residue characteristic two. The density error is at most epsilon=q^(1-rho), sharpening the source factor 8/7.
- STC2: nonprimitive pairing leakage costs at most 2(1+epsilon)epsilon; in the nonsplit case it costs at most (1+epsilon)epsilon².
- STC3–STC6: explicit Eichler moves, integral graph congruence, a short self-dual trace-extension proof, exact phase change, nontriviality of the move character by duality, and preservation of all three defect-family parameters away from leakage.
- STC7: the original per-family amplitude is bounded by 7 epsilon times its mass. Reversibility gives a symmetric kernel on actual lattices; pair-orbit stabilizer weights are then exact. Summing families at fixed datum costs no family-count factor.
- STC8: combine STC7 with DS3 for the positive second-type mass and the strict-image branch. The entire nongeneric squared amplitude is at most Hp^(2s²+10s+19) q^(-(k-2r-5)) nn, hence satisfies the source exponent 39s². At Hp=1 the nongeneric terms are empty.

Dependencies: GL1–GL6 and DS1–DS3, with the original relevance and linked witness dictionary.
The source being reconstructed is jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de:
all filenames below are relative to lean/src/Development/AbelianVarietyTheory/.
- Definitions/SemilocalFrames/ComplementReferenceCompactSubgroup.lean and NoLeak.lean: actual family, scalar reference, kernel and phases.
- Proofs/FlagMeasures/TermExponentsNonnegAndDefectGroupBound.lean and TermLevelZeroAndBoundedRepresentatives.lean: saturation and level inputs (also direct coefficient argument STC5).
- Proofs/FlagMeasures/ExistsNormOneOrthTriple.lean, NormGaussSumLe.lean, QuadricCharacterLeakSharesFinite.lean and TermIntegralNearOneBound.lean: orthogonal summand, density and leakage.
- Proofs/FlagMeasures/FrameMoveCharacterNeOne.lean, EichlerMapMemUnipotentCharacter.lean, MoveLatticeIsTermSameDatumWithWitnesses.lean, HermitianDoubleCosetFramesDatumMoveProperties.lean, HermitianMovePreservesFrameLatticeLevels.lean, HermitianDefectClassMemTraceFirstFrameSpan.lean, HermitianDoubleCosetInFamilyMovedOfNotLeak.lean, HermitianDoubleCosetMoveTermWeightCharacter.lean and ExistsIsometryOfSameTrace.lean: move and no-leak preservation.
- Proofs/FlagMeasures/HermitianFamilyTraceVolumeConst.lean, HermitianFramesReferenceSubgroupsRelIndexEq.lean, HermitianMovesTotalMeasureEstimates.lean, HermitianDoubleCosetKernelRowSumNearOne.lean, HermitianDoubleCosetKernelBoundByWeight.lean, ExistsSymmInvariantKernelHermitianFrames.lean, NormOrbitSumLeOfSymmKernel.lean and AmplitudeLeMassSecondTypeFamily.lean: normalization, symmetry and weighted averaging.
- Proofs/FlagMeasures/HermitianFramesStabilizerActsOnTerms.lean, FramesCharactersAgreeCommonStabiliser.lean: orbit invariance.
- Proofs/FlagMeasures/HermitianDoubleCosetSecondTypeFamilyAmpSqLe.lean, NonzeroDefectHeightPowerAbsorbsConstants.lean: final squared amplitude.

Status: written local supplier, with independent [move/kernel review](second-type-independent-review.md) and [Fourier, density, leakage and final-exponent review](second-type-fourier-independent-review.md). Both found no blocking error under the stated GL/DS hypotheses. Dyadic scalar-domain, inverse-integrality and orbit-weight clarifications have been integrated. The exact finite checks cover 1,592 Gauss sums and 10 density/leak cases; their scope is recorded in [the certificate](../certificates/second-type-fourier.json). The proof is included in both rebuilt manuscripts. No Lean replay is claimed. The [archimedean and exact-norm continuation](w08-analytic-and-retained-continuation.md) now supplies the actual analytic `StepThmBPinnedG` route. The common retained theta-row identity and moving positive-trace estimates remain open, so W08 and both RH/GRH programs remain incomplete.
