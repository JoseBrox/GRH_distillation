# Nongeneric saturation-index stratification

The [proof](../paper/shared/flag-defect-stratification.tex) extends the established GL1–GL7 local mass calculation to **actual nongeneric terms**. In the original rank range, put s=r+1, l=k-1, P=Hp, beta=q^i=[sat Λ:M], and q^j=cardI.

- DS1 identifies the source image Ihat/M canonically with the quotient of the fixed complement datum lattice by the actual complement lattice. In particular j≤i; a nongeneric term outside TypeBe has j<i. This verifies the strict-index step directly, including the linked level congruence.
- DS2 counts index-q^j sublattices with bound 16(j+1)q^((l-1)j), uniform in l and the local field. At inert places j is even.
- DS3 proves the squared amplitude bound P^(2s²+10s+11) q^(-l) nn on the entire strict-image branch, and P^(2s²+10s+11) q^(-I) nn for all defect indices i≥I≥1. It includes any further invariant term restriction. The two bounds retain the original reciprocal stabilizer weights and all phases; no cancellation is assumed.
- DS4 proves the original P^(39s²) q^(-(k-2r-5)) nn estimate on the union of these branches with I=k-2r-5. The first-type supplier is therefore proved. The large-defect portion of the second type is also proved without cancellation. Only 1≤i=j<k-2r-5 remains in the local nongeneric gain. A q^(-1) saving holds for *all* nongeneric terms by DS3 (q^(-2) at an inert place), but is not the required full saving.

Pinned interfaces: jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.

- Development/AbelianVarietyTheory/Definitions/SemilocalFrames/ComplementReferenceCompactSubgroup.lean, lines 134–207 (Mof, M, sat, be, BBzero, RR, levC, TypeBe, complementLatticeOfDatum, TauRel, Ihat, cardI).
- Development/AbelianVarietyTheory/Proofs/FlagMeasures/GluingImageCardPowLeDefectGroupCard.lean (small_image).
- Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermitianFramesFirstTypeAmpSqBound.lean (first_type_bound).
- Development/AbelianVarietyTheory/Proofs/FlagMeasures/NonzeroDefectHeightPowerAbsorbsConstants.lean (ampSq_nonzero_defect).
- Development/AbelianVarietyTheory/Proofs/FlagMeasures/HermitianDoubleCosetSecondTypeFamilyAmpSqLe.lean (family_bound).
- Formalism/SharpRestriction/CuspSpanNormBounds/IsTermOver.lean, NGAt.

Dependencies: the actual linked frame classes, primitive-saturation mass, discriminant gluing and stabilizer sums GL1–GL7. The large-defect threshold is an original-parameter threshold, not a new hypothesis for the whole local theorem. The subsequent [second-type cancellation](flag-second-type-cancellation.md) supplies the remaining small full-image phase estimate and full nongeneric bound. StepThmBPinnedG remains open. No Lean replay or full manuscript compilation was performed for this change.
