# Rational adapted normal forms for the actual relevant terms

**Closed supplier obligations (W08):** NFExC and LabC. See the [written proof](../paper/shared/flag-adapted-normal-form.tex).

Relevance imposes a successor relation on leading common isotropic vectors. The trace pairing gives the equality over the original CM field, not only after embedding into the complex numbers. The common indices must form a tail, with one scalar of norm one; when the intersection is zero, the zero-Gram equality and positivity give the last-vector comparison instead. A skew-hermitian operator on the nondegenerate leading pair then imposes an equality on sums of simple-root coefficients. Elementary monomial elimination shows that the signed cross matrix consists of contiguous reversed blocks. Rational isotropic duals are obtained by subtracting half their hermitian Gram matrix along the common tail. All changes preserve the original graded bases.

Every adapted form has the prescribed labels: leading minors are preserved, the original convention conjugates the cross matrix, and the norm of the original different ideal supplies exactly the same exponent. Empty leading blocks are included. No field extension, lattice-index loss or new rank-dependent constant occurs. This discharges the two rational hypotheses of the [weighted fixed-row comparison](flag-term-correspondence.md); the [original row-label congruence](flag-row-congruence.md) now supplies (FC7), completing PerRowC.

## Source interfaces checked

Pinned source: jsmorph/rh at ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de. Paths relative to lean/src/.

| File | Git blob | Relevant declarations |
| --- | --- | --- |
| Development/AbelianVarietyTheory/Definitions/SemilocalFrames/PerRowC.lean | c406932d46d85320d0a2cfd75fd776219312cf96 | NFExC, LabC, PerRowC (47–67) |
| Development/AbelianVarietyTheory/Definitions/SemilocalFrames/NormalFormDualOrthogonalLast.lean | 65d77595fcdcf1ec568ead93a509298b4be7e292 | NF (33–59), nD, Del, Db (79–87) |
| Development/AbelianVarietyTheory/Definitions/SemilocalFrames/AdaptSelf.lean | 97311ee488582c1c5ecf2f6cba4e4a79ffdf2eee | Adapt and label (12–22) |
| Development/AbelianVarietyTheory/Proofs/FlagMeasures/ExistsAdaptedNormalFormRelevantTermProof.lean | 7436964d08e1007657fa0aacd0a90aa592c98bb1 | actual term incidence (114–155), signs (57–90) |
| Development/AbelianVarietyTheory/Proofs/FlagMeasures/AdaptedNormalFormNormsMinorsEqLabelProof.lean | 927f4192c8bb5d42fbc67743b97dd202ae23ed2c | exact normalized minor and labels (12–44, 74–137) |
| Formalism/FlagUnipotentLattices/MemOfOrthogonalAnisotropic.lean | bfe4673a2fc741b79d560890f57b36145a2e73bb | flag, relevance, Gram, NFFull (25–125) |
| Formalism/FlagUnipotentLattices/MinkowskiFactorialBounds/ExistsHasLeadingCoeffOfMemSpanBelow.lean | e84b8180de977e0157635e27d4ec9ab457463b14 | successor and common tail (335–639), disjoint case (868–924, 1362–1460) |
| Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/RelevantSetZeroGNotIdentity.lean | da06167b1c4cb26abdfe772750727063be2c0b51 | original membership and rational normal form (15–48) |
| Formalism/SharpRestriction/CuspSpanNormBounds/BruhatCellsKronecker/CellDef.lean | e1e7a45b84156ffecbea96a524b05655e59174d4 | matrix relevance (12–66) |
| Formalism/SharpRestriction/CuspSpanNormBounds/BruhatCellsKronecker/CellGeo.lean | f015ef41e12a07a14855d9e2878a6529c85ed5fa | leading-pair realization (681–765) |
| Formalism/SharpRestriction/CuspSpanNormBounds/BruhatCellsKronecker/CellMono.lean | 548e125fbb8bf436f2030e81e706f30db655535c | monomial descent (81–116) |
| Formalism/SharpRestriction/CuspSpanNormBounds/Point.lean | dbf5f722fe192facd6c88f11de9673665eba3399 | exact constant anti-diagonal block convention |
| Development/AbelianVarietyTheory/Proofs/FlagMeasures/FlagFramesSameGradedDefinitePartLatticeEq.lean | 1a1e98891f47bbe4943fb65ea0388e151d353632 | adaptation invariants (366–396) |

Source reading and independent rational proof; not a Lean replay or full manuscript build. W08 remains open.
