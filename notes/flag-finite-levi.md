# Finite Levi Gram, original column count, and diagonal zero-Gram saving

The finite interfaces in GA9 are now supplied by
[the finite Levi proof](../paper/shared/flag-finite-levi.tex).
The exact original diagonal zero-Gram saving follows **under the
matched local-data hypothesis** of the global amplitude theorem:
`||K''_uu||_HS^2 <= duC exp(-k f log k)`.
Here duC is the full column dimension, not the compact dimension dpiC.

The finite Gram bound is proved directly: the finite character
convolution is a sum of conjugates of an orthogonal character
projection. The elementary Gelfand--Graev anti-involution argument
proves multiplicity one, and mirabolic restriction gives the necessary
degree lower bound without using a general character-degree formula.
The actual TypedRed ring gives exactly f factors over each of the
two distinct split rational level primes. Full.psi_ne supplies
nontriviality of every residue character. The resulting Pg is <= 2.

The exact column count retains the row stabilizer. In the actual
split fixed-frame coordinates, each finite integral stabilizer
surjects onto the selected GL_k residue group, with the level subgroup
the inverse image of the upper unitriangular group. The two distinct
residue characteristics imply the finite rational row stabilizer
acts freely on the resulting cosets. Consequently the actual
column fibre size is Gam1 times the reciprocal row automorphism
order, and the full column dimension is Gam1*massRows*dpiC.

The actual finite phase follows from the fixed-frame congruences
and TypedRed.psi_eq; saturation of the full degenerate nonidentity
term set follows by its rational row stabilizer actions. Expanding
the actual column blocks by the finite double-coset bijection gives
the original GG matrix, with its conjugation and row weights intact.
Combining with GA7 gives FL8, with no further arithmetic loss.

**Remaining:** construct the matched local lowest-vector Bessel
data (LocDatC in the exact standing regime), and then establish the
generic nonidentity return estimates and the final retained
arithmetic theta Gram / positive-trace comparisons. W08 remains
open. No claim of a Lean replay or complete manuscript compilation.

## Pinned source audit

All paths are under lean/src/ of jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.
The proof uses the actual Full, HidaSetting, TypedRed and row/column
representatives, not arbitrary instances of a finite comparison.

| Path (under Formalism/LocalToGlobal/SiegelLatticeTheory/) | Blob | Interface |
|---|---|---|
| FlagStabilizerTensors/PoincareConstantEq.lean | 01c55e7b210ccca4b2885c0cb6761f5e01e7d046 | Full.psi_ne, rowsOK, colReps |
| HaarTransversals/HidaSetting.lean | 7f21195438209fd7fc4d0b081fe53297f07fb9c4 | fixed frames, integral Gram, ew, level approximation |
| ClosedLocalOrbits/TermOp.lean | 35f737cb9e89fc17f159a562740961263fbb0ec3 | chiN/chiL, ColReps, TypedRed, iotaOf, rowOf, vec, GG |
| ClosedLocalOrbits/GGMirabolic.lean | 2bbfca810a6d1405b214ba7ab03691ffc855beb6 | original finite convolution |
| ClosedLocalOrbits/GaugeLatticeShifts/ColPhaseCut.lean | c35597df09a68bc7c0abff25100ef9cad5e6b677 | scOf, Aset, LeviCols, PhaseAt |
| ClosedLocalOrbits/GaugeLatticeShifts/ColFreePf.lean | 354842a0418121be0f3bcb77e886a86d900a4ecf | exact column bijection |
| ClosedLocalOrbits/GaugeLatticeShifts/NormCut.lean | 415b4280a32ba07c22dbca5a7b7044e7e99d5a44 | original ColFree, ColPhase, SatGram, norm expansion |
| ClosedLocalOrbits/GaugeLatticeShifts/NormExpSatHolds.lean | 8bc35f69b73c99e57420abb4cf6cd5ac681d4951 | actual degenerate saturation |
| ClosedLocalOrbits/GaugeLatticeShifts/SatGramActLStmt.lean | 3d7a7e745e590f1981f9aade1877cef9539657e6 | actual left-action requirements |
| ClosedLocalOrbits/GaugeLatticeShifts/SatGram.lean | 619aa729fdf3d4e038cf95e20f415d2b9a58b58c | actual typed reduction |
| CokernelGLCounts/RankPointCounts/MainEqCut.lean | 072770f63ba10f961c64e3073c53c34efd52c1e4 | NormExpDegC, Pg, dimension consumer |
| CokernelGLCounts/RowsOther.lean | aaf5c0210f26d701b19d98ccd15c7b8b7cf6c212 | final KppDiag |
| CokernelGLCounts/RowsConc.lean | 33aa2cac882fa5e1f0e6472274e570655235aa64 | actual standing context |

The dimension interfaces additionally use
Formalism/PeriodIntegrals/UnitaryGroupMassFormula/RankTwoDimensionFormula/
DimFormCOfSteps.lean (7c12896eaae0579e2d554e923335d3f1d9120ae0),
GammaOneEqProd.lean (903c2a205002618f5d99f5bb876ea57f4906b37f),
IndexGe.lean (6952539d448b6c473cdfd33c637c849f55bc5fc7),
and StabBoundHolds.lean (20203c825d65b58e53b916a04910d5f60a9a5feb).
