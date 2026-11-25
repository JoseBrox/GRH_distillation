# W08 nonzero-Gram cells and normal multiplicity

[Proof](../paper/shared/flag-nondegenerate-normal-count.tex).
On the original admitted terms the corank-one relation is equality
of the two-sided positive quotient graphs. The generic scalar
refinement is equality of last-vector coefficient functions.
The original point, normal vectors and rational double cosets are
retained. Both adjugate normal classes have content
\((g)^{r+1}\mathfrak d^{r(r+1)}\). With the original normalized Gram
invariant \(N_G\), the number of occupied rational normal classes
at a fixed point and corank-one class is at most
\[
|\mu(E)|^2(TT')^f (N_G/g^{2f(r+1)})^2.
\]
The expression \(N_G/g^{2f(r+1)}\) is a positive integer.
This supplies occupied-point StepPointsG, StepNormOneG and the
normal-count inputs in both generic and nongeneric cases. It
improves the original \(\rho^{12r(r+1)f}(TT')^{6f}N_G^6\).
There is no field-dependent implicit constant and no identification
of distinct integral double cosets.

## Pinned interfaces

All refer to jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.
Under Formalism/SharpRestriction/CuspSpanNormBounds:
BlockEnds.lean (8509b64296431d5ab15f64ecdf09c5188a82b832),
BruhatCellsKronecker/CellDef.lean (e1e7a45b84156ffecbea96a524b05655e59174d4),
Point.lean (dbf5f722fe192facd6c88f11de9673665eba3399), and
IsPrimitiveSub.lean (5806b474f3381b159d9d80ba86547df0eb0cb4ab),
lines 65--105, 139--152, 180--250: point, admission, ThPairs, s0, IsScalar.

Under Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts:
PairingOmegaPrimeZ.lean (bf9c3bd96e5e6451746cd17917ddaa3b9d75fc62),
lines 40--130, gives the exact adjugate normal.
CorankRelation.lean (203fd942a24de1bc4c862de4aae37e72b24f2ab0),
RelCOfOcc.lean (bd72d5fc6cbf9dd5d1672fef7083412961097d89),
NmlLineHolds.lean (33c7a2e5a2e7acb78ef1de5dcc80e53f4e8729eb),
FramesMem.lean (f9620a2ae9c6a817f7616c8fa17bc14aeb399409),
UnitaryNormalVectorCount.lean (9fbca3ab432c79c6f83f700b859a1717e64f59ca),
LemmaG3OfCoefficients.lean (39ed6eee2d334f16195bfe9a7d119e2b7463e7ce)
give the two-sided normal ratio and separation interfaces.
NormalInvariants.lean (4c68f3d8828e519d6181fea233d26547bb6ceeeb),
MainEqNormals.lean (9634e4f339dc8b1c718df804d007789019779fe5),
MainEqNormOne.lean (b4574e5c572e98745c9eecb22d584698c371fb5a),
MainEqPoints.lean (47a6e9ce1f7e73e169652487728b65f6d4817942),
MainEqSteps.lean (e1d36eaa8c13c9744dd7b6f5b3acbca8d10de1fc),
MainEqClass.lean (9200891b301e65e8464d5087cfcf817c8b711bca)
give the corresponding consumers. RowsConc.lean in the parent
directory (33aa2cac882fa5e1f0e6472274e570655235aa64) and
Formalism/HermitianCurvature/StatementPN.lean
(fc7e8086bbe8872adbdb3a86422fe4a2ee6a6e62) specify normalization.

Remaining: StepLocGenPinnedG, StepThmBPinnedG, integral
class amplitude sums and final analytic comparisons. No
universal statement about fallback points or all integral
term representatives is inferred from an occupied-point count.
