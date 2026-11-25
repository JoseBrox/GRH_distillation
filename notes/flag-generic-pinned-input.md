# Complete generic pinned local input (W08)

[Mathematical proof](../paper/shared/flag-generic-pinned-input.tex).

The earlier GL7 / GC1–10 / GM1–12 calculations and exact AA identity (AN15) now assemble into the equal-word generic pinned local supplier `StepLocGenPinnedG`, on the actual concrete hypotheses. In particular, the scale is precisely (g^{-fb(w)}) on a represented point, equal to 1 on the regular locus. The quotient-measure factor cancels the class covolume factor, and the denominator is positive on every occupied point because an individual nonzero term has nonzero pinned orbital operator. The finite record uses exactly the tested keys and their finite sets of occupied local datum representatives, not an assertion of finiteness of the entire global genus. The total generic mass uses the untruncated local pairing-class mass and the genuine global reference frame. Unfold is an inequality for finite subsets, so the finite restriction is legitimate. After the mass inequality only the abstract upper-bound V0 is enlarged, not the actual measures.

Explicit choices from GL7: C1=4, C0n=1, CSt=0, e1=2. The larger source allowances 39 and 9 also work. The scalar bound is uniform with no height loss. The generic mass target can be taken to be 2 AA rho^(2r(r+1)f(k-1)) H^(10s²+12s+1) nPt, exactly the source eN, while the uninflated arithmetic estimate has exponent s(s-1).

**Pinned source interfaces:** all under jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de, lean/src.
- Development/AbelianVarietyTheory/Proofs/FlagMeasures/ExistsScaleNormalisedLocalReading.lean, blob 0e79860d095093ee9a49357f169bf69af73c1342, scale_pin; statement blob a7315209d1943ad057966b681e0367f060419bf0.
- Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/RealObj.lean, blob ee435fa738ff88d9e4b71fa5e49a735f89df0d08, IsPtRep, gamW, FreeE, stCoord, NuQPin.
- Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/NGData.lean, blob cdce063c1cde7f59a7c3cb9fbc3393e8267fa01c, nmlOf, Jw, J2of.
- Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/MainEqCut.lean, blob 072770f63ba10f961c64e3073c53c34efd52c1e4, LocalInputG, ZAt, clsG, grpGC, a2GC, NOfG.
- Same directory MainEqLoc.lean, blob 57ded91f7eea576dfee84a96b8ebb75e8147d011, LocalInputLeG, localInputG_of_le, StepLocPinnedG and stepLocGenPinnedG_of_loc; MainEqAna.lean, blob e33ecea05bb5fcc3174714721121ce66bee52460, StepLocGenPinnedG and StepThmBPinnedG.
- Formalism/HermitianCurvature/StatementPN.lean, blob fc7e8086bbe8872adbdb3a86422fe4a2ee6a6e62, LocalNG, Basic, MassRatioAt, Unfold, IsPt, eN, GenMassInput, PointSumInput.
- Development/AbelianVarietyTheory/Proofs/FlagMeasures/FamilyGroupSumFactorsRowWeightAmplitudeProof.lean, blob 909c5d36a649e9c9705771dc7eb7ad5a94d814aa, squaredGroupSum_classDoubleCoset_eq_rowWeight.
- Formalism/SharpRestriction/CuspSpanNormBounds/IsTermOver.lean, blob 6a536a02807d5dc242b3245e9da264bdd1e666cf, actual Hp, PrimeTo, Reps, amp, nn; NGLocModel.lean (in RankPointCounts), blob c4faae817b4c192b2e6dec7177a78e1bb21679db, toL.

**Boundary.** This is a mathematical assembly, not a Lean replay. The analytic point sum still uses the original unscaled pinned measure. The [pointwise and exact-normalization continuation](w08-analytic-and-retained-continuation.md) now supplies the analytic weighted point sum on this route, and the independently reviewed [second-type cancellation](second-type-independent-review.md) supplies the remaining nongeneric local gain. The common retained theta-row comparison and moving positive-trace estimates remain; no W08 closure is claimed.
