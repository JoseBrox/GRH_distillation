# All-cell Pieri transfer and the weighted rotated summation reduction

**New exact supplier.** The two-sided relative-functional factorization AP3 on every relevant nonzero-Gram cell follows by disintegrating the actual diagonal stabilizer quotient into one full Bessel subgroup and the remaining quotient. The original period identity gives the first integration; right-equivariance and Bessel multiplicity one then give the second scalar. Both orders are absolutely convergent by the established terminal quotient properness estimate and the actual large-gap smooth-decay bound. If either normalized period map is zero, integrate that full side first. Thus the proof does not infer absence of all Bessel functionals from a zero period form.

AP3 shows that a zero radial Jacquet norm forces every nonzero-Gram orbital evaluation to vanish. Apply this to the differences of the finite exterior-Pieri summands and their normalized representatives. This gives AP5, with the original coefficients, even for cells with vanishing internal minors. The conjugate-minor expansion follows by the dual exterior decomposition and the radial adjoint identity; its coefficient-sum constant may increase by one. No continuity across strata or uniform quotient majorant is needed.

**New conditional analytic reduction.** The exact weighted rotated point sum now follows from the ordinary unweighted near-parameter pointwise estimate AP6 (the original BpIneq, at its prescribed scale) and the already proved moment and expansion suppliers. AP8 chooses one positive-minor monomial, of degree at most M s^3 for s=r+1 and M depending only on the desired weight and pole constant. The required spectral shift is at most M s^4. The actual all-gap threshold and noncompact gap supply the full real reserve. AP9 is the one-place inequality with a rank-dependent inverse-Gram exponent A_s=ceil(C_* m^2). That exponent cancels exactly by the global product formula. An elementary count of embedded integral block-end minors proves the remaining reciprocal-weight sum <= b^(10fs), with no lower bound on individual archimedean embeddings. The total cost is b^(C_rot m^5 f).

This bypasses the stronger intermediate WeightedExpansionRotated with fixed A and fixed dist'. In particular one need not obtain a fixed inverse-Gram power or fixed shift radius as r varies. The constant C_rot and strengthened all-gap threshold are uniform. The proof retains the actual rotated points, stabilizer-root and quotient measures, characters, block weights, relative norm and prescribed section.

**Remaining obligations.** AP6 is still an assumption of the weighted-sum theorem. The all-rank pointwise analytic bound (ThmBpAt / ThmBpDS and its character-scale comparison), and the original uniform global-to-local amplitude and row-norm comparisons (AmpUnif / RowRestUnifR or a direct substitute), must still be supplied. The argument is on the established smooth-decay and terminal-quotient hypotheses; it is not a standalone construction of those earlier inputs. It does not close StepThmBPinnedG, W08, or the RH/GRH proofs.

Proof: [global-norm-frontier-all-cell-pieri.tex](../paper/shared/global-norm-frontier-all-cell-pieri.tex).

## Pinned source interfaces

All paths relative to lean/src of jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.

- Formalism/SharpRestriction/CuspSpanNormBounds/RootMeasBig.lean, blob f8dc96616ccec4598ee82de3c398243682160beb, lines 17–68: besselIntg, pairMeas, RStab, stabAct, IsRootMeas, IsOrbQuot, IsRelStab, OrbInt and IsPtRep.
- Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean, blob d008b93b66125f83b7adb112628b058dde3b1096: LocBessel and its actual compact and unipotent measures.
- Formalism/SharpRestriction/CuspSpanNormBounds/TheoremBConstants.lean, blob db06cb5a048c6da5b2edf1d326facacc309ff99e: OneStepCellExpansion, both minor signs and its all-cell equality.
- Formalism/SharpRestriction/CuspSpanNormBounds/LeadMinorK.lean, blob 793b55df37e7be237b3cb7b37060255ff3c89a3b, lines 35–116, 135–188, 211–218: StdHyp, LocOk, jNorm2, orbSq, q0, local and global weights, BData and BpIneq.
- Formalism/SharpRestriction/CuspSpanNormBounds/OnePlaceEstimates.lean, blob d641a2a34206975a819216642052bc0ca832b69a: BesselRangeNearParameter and its moment reserve.
- Formalism/SharpRestriction/CuspSpanNormBounds/LocalDataRealPlace.lean, blob 9083c189780e9bb4bdb7b54471cd4e37fd1b16c3: rhoReal and ptLocS.
- Formalism/SharpRestriction/CuspSpanNormBounds/BesselShellMomentBounds.lean, blob 6280709a4f1303e4f5afae10333c8174593795b3, lines 509–581, 613–725, 815–1005: local weight and minor scales, positivity, product formula cancellation and weighted sum.
- Formalism/SharpRestriction/CuspSpanNormBounds/WeightedUniformRotatedOfExpansion.lean, blob 8f01f46680f6a7220ce57d41f48567ef0dc8418b, lines 31–86, 147–173: original fixed-A, fixed-dist' intermediate and uniform weighted-sum consumer.
- Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmBUseR.lean, blob 16af0476859d9fafdbaef8193f89b1e96a792ee9: JointNormBoundRotatedUniform and pointSum_of_B3R.
- Development/AbelianVarietyTheory/Statements/DiscreteSeriesShifts/ThmBpDS.lean, blob ee9d3566504b7c3fc887401194b7512aefcbfe92; Development/AbelianVarietyTheory/Proofs/FlagMeasures/BesselPointwiseBoundAtLargeGaps.lean, blob c9a44c230884a39bd723de20f97fca1df55943bf: remaining pointwise theorem.
- Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/ThmBChainG.lean, blob 2da396f549ca4ab56d1b093e05af08f444450bf8: generic consumer of JointNormBoundRotatedUniform, AmpUnif and RowRestUnifR.

No Lean replay, independent full review or manuscript compilation is claimed.
