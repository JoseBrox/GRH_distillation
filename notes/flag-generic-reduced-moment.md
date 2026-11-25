# Reduced generic archimedean moment

[Mathematical proof](../paper/shared/flag-generic-reduced-moment.tex). This is a direct concrete replacement of the arithmetic brackets in the generic assembly, not an assertion that StepThmBPinnedG is proved.

- RM1: sum only generic saturation masses. The original weighted local second moment is bounded by 2 Hp^(2s²+2s) ngen(C), s=r+1, with constant one at good places.
- RM2: uniform summability by disjoint complex polydisks around the CM Minkowski lattice. The bound is 14^(fs), instead of 64^(fs), for the original inverse block-minor weight summed over integral block-end points. No restriction on the field discriminant is needed.
- RM4: on the actual generic keys at a fixed occupied point, the squared grouped-vector sum is at most 2 AA_re H^(3s²+s+1) nPt J2_B, with AA_re=AA*rho^(2r(r+1)f(k-1)). It uses the uninflated mass (AN16), not the enlarged artificial witness (GP4).
- RM3: applying the original class-square expansion, weighted Cauchy–Schwarz and the normal count (NG4) with epsilon=1/2 yields a sufficient point-moment exponent p=3s²+s+2 ≤ 6s². The normal-count scalar is |mu(E)|² C_(1/2)^(2f) (TT')^(f/2). There is no added positive g^fp factor because H=g^(-(2r+1)f) NG ND exactly. The abstract source proof with C1=4 and C0=1 asks for A≥43. The smaller weight suffices only for the concrete actual generic route.

Dependencies: GL1–GL7, GC4–GC7, AN16, GP2, NG1–NG4 and actual class-square expansion on the absolutely convergent original returns. No claimed new proof of abstract ExactCores or of the normalizing FrameInputs/NormInputs.

Pinned source jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de:
- Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/MainEqCut.lean, lines 53–141, 195–305: weighted generic amplitude, class labels, grouped vectors, RowGenAbstract and the two brackets.
- Formalism/FlagUnipotentLattices/UnipotentStabiliserCharacterisation.lean: blockMinorWeight, original endpoint tuple multiplicity.
- Formalism/HermitianCurvature/StatementPN.lean: PointSumInput.
- Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/MainEqSteps.lean: A≥C1+C0+38 in abstract consumer.
- Formalism/SharpRestriction/CuspSpanNormBounds/BesselShellMomentBounds.lean (blob 6280709a4f1303e4f5afae10333c8174593795b3), lines 509–556 and 815–992: same point weight and one-place-to-global passage. No stronger analytic estimate is inferred from the arithmetic packing proof.

The remaining real pointwise estimates and their transfer to the actual pinned Jacquet norm are open; proving the smaller moment is sufficient for the generic row calculation without proving the full quantified StepThmBPinnedG. The small full-image nongeneric defect phase estimate remains separate. No Lean replay or manuscript build was performed.
