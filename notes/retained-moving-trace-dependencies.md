# Moving retained positive traces: quantitative supplier and remaining dependencies

## Result

The new ordinary theorem in `retained-period-window-budget.tex` turns the **actual** period Gram estimates into an explicit budget at the original prescribed seed calibration. For the normalized original columns `A_u=c0X_u^(-1/2)P_u`, write `R=sum dim C_u`, `D=dim H`, and `D_*` for the original proposed dimension main term. If

\[
\|A_u^*A_u-I\|_{HS}^2\le q^2d_u,\qquad
\|A_u^*A_{u'}\|_{HS}^2\le(1+\tau)d_ud_{u'}/D_*
\quad(u\ne u'),
\]

then at prescribed `c=R`, with `sigma=D_*/R` and `xi=|D/D_*-1|`,

\[
g+b\le E:=\frac{q+\sqrt{(1+\xi)(1+\tau+(1+q)^2\sigma)-1+2q}}2.
\]

For actual retained source and target fractions `r0,v0`, and the prescribed retained scale `c0=R0=r0 R`, the bound is

\[
g_0+b_0\le\frac{E+\max(1-r_0,1-v_0)}{r_0}.
\]

For another prescribed scale `c0=theta R`, the theorem retains the exact two calibration terms rather than replacing it by `R0` or by the observed mass. The target cut is charged linearly in its lost dimension fraction in this joint estimate. This improves the cruder route through a target-cut mass lower bound, but it does not supply missing arithmetic estimates.

## What the newly completed analytic estimates do and do not supply

The new `StepThmBPinnedG` route supplies the original weighted point sum with cost `b^(C m^5 f)`. Combined with the already reconstructed generic local input and the concrete reduced moment, it supplies the equal-word generic scalar row bound `RowMainEqC`. The second-type cancellation supplies the missing nongeneric local gain. These are substantial new analytic suppliers for the diagonal and nongeneric portions.

The target trace requires a different precision level. The exact source `AdmissibleBoundsFromSource.Conclusion1` asks for

\[
\|K_{uu'}\|_{HS}^2\le(1+b^{-6})d_ud_{u'}/D_*
\quad(u\ne u').
\]

Its source proof uses the **distinct-word** scalar estimate `adm9`, equivalently `LocalBesselAndTopKernel.Conclusion1`:

\[
\operatorname{genScal}(u,u')\le
\left(1+C_A(r+1)(C_A/\operatorname{ThA})^f\right)
(1+eSum) f_3\,d_ud_{u'}/D_*.
\]

The original cut and dual-lattice hypotheses must give the small excess in this displayed leading constant. The polynomial-cost point-sum bound does not imply it. In the written reconstruction, the local orbital recursion and finite character calculations are supplied, but the global scalar recursion after Poisson summation, with the exact lattice indices and moving-family constants, is still explicitly a separate input (`65-sec-theta-local-audit.tex`, final global subsection). The source route exists; it should not be described as absent. Its `LocalBesselAndTopKernel.Adm1` includes `admA`, `GlobalLatticeMajorantHypothesis`, `ColumnSpaceRanks`, `SpectralWeightsCM`, and `ArithmeticGlobalModelCondition`, as well as local identities already reconstructed. Their actual-family realization has not been proved by the new AP6/AP7 result.

## The diagonal source-deficit issue is narrower but still has an input

If the actual diagonal nonzero-Gram remainder satisfies

\[
\|R_u\|_{HS}^2\le\Gamma d_u^2/D_*,\qquad
d_u\Gamma^2/D_*\le C_0,
\]

then the independently proved zero-Gram estimate gives

\[
\|K_{uu}-I\|_{HS}^2\le d_u
\left(\sqrt{x_K}+\sqrt{C_0/\Gamma}\right)^2,
\qquad x_K=e^{-kf\log k}.
\]

Hence the source trace would obey `g<=sqrt(x_K)+sqrt(C_0/Gamma)` before any target cut, and be strictly less than one once this explicit number is below one. This would give a nonzero actual period map without using the theta comparison.

However, one cannot infer that full diagonal remainder estimate just from the theorem name `diagonal_contribution_of_equal_words`. Its codomain `DiagCL` **still explicitly takes** `RowBig` and `RowNotScalar` as arguments. These are the large-corank and nonscalar loop bounds. The new generic and nongeneric scalar estimates fill `RowMainEqC` and the relevant `RowNGC` supplier; they do not delete those other two hypotheses.

The loop supplier route is explicit. `RowsConc.LoopsCutC` supplies the actual amplitude/lattice-size data; `rowLoopsC_of_cut` then uses `PN.LoopCores`. The moving-family version `LoopEvaluationThresholdZero` additionally takes actual `RowsND`, `RowsDeg`, and `RowsOne` bounds, tied to the same term data by `JtPin`, `WRowPin`, and `FibreCount`, and the original `FormAt`. The currently completed scalar normal count alone is not a statement of all those weighted class sums. Therefore this audit does not claim an unconditional new `PuNZ` theorem.

## Other exact moving-family dependencies

1. The actual dimension count must bound `xi=|Dall/Dstar-1|`, with the original finite idempotent and Haar measure. This is `adm10`; `Dstar` is a proposed main term, not the actual rank by definition.
2. The selected word window must bound `sigma=Dstar/R`. More selected columns do not by themselves prove the target estimate: the leading constant in the off-diagonal Gram bound remains essential.
3. Source and target cuts must supply their actual retained fractions. The source primitive-cut route bounds the discarded source fraction by `2f/min T_u`; the target fraction must be supplied for the particular retained row projection.
4. The common theta/period dictionary must identify all columns in one common target, with the original nonzero comparison scalars and prescribed calibration. Individual period isometries do not suffice.
5. The resulting numerical `E_0` must satisfy the original height-weighted averaged budget over every requested fourth-power sample and expanded averaging window. Pointwise smallness at one fixed datum is insufficient.

For example, aligned unit columns can have zero source deficit and target excess approaching one, independently of how many columns are repeated. This confirms why neither source nonvanishing nor a coarse uniform norm bound can replace the distinct-word correlation estimate.

## Immutable source ledger

All paths are under `lean/src/` at `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. Source identities were checked in bounded excerpts; no Lean replay is claimed.

| Source | Git blob | Bounded ranges and role |
|---|---|---|
| `Formalism/SharpRestriction/CuspSpanNormBounds/AdmissibleBoundsFromSource.lean` | `1caea89b8fb520994d0250597e3e6ec76147506e` | 1–110, 110–190, 190–285; actual admitted estimates, `Conclusion1`, `eF`, `AF`, `BF`, `Conclusion2Family` |
| `Formalism/SharpRestriction/CuspSpanNormBounds/StandingNumericalData.lean` | `f6b85bc4a9e85ffb73ba7842269f9b010bcf12d1` | 1–110; original `genScal`, dimension comparison, word data |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RowsConc.lean` | `33aa2cac882fa5e1f0e6472274e570655235aa64` | 1–120, 150–205; `RowMainEqC`, `RowNGC`, `LoopsCutC`, loop input route |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DiagCL.lean` | `fa7dec6d60ea45bdd99e01ed2e39ad8af6e37592` | 1–56; remaining `RowBig` and `RowNotScalar` arguments in the codomain |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DiagCLC.lean` | `d6d0b5f00353b667f340233cbacc08111120bd8c` | 1–34; theorem preserves the `DiagCL` hypotheses |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RowsOther.lean` | `aaf5c0210f26d701b19d98ccd15c7b8b7cf6c212` | 25–100; exact diagonal decomposition and four bounds |
| `Formalism/SharpRestriction/CuspSpanNormBounds/BruhatCellsKronecker/ShiftedParametersOfDifferingLetters.lean` | `36cab771c1fdf7be1bee1d9f66710bad3fb86e94` | 327–410; actual use of `adm9` for distinct words |
| `Formalism/SharpRestriction/CuspSpanNormBounds/LocalBesselAndTopKernel.lean` | `4a96d6fc92d7471ba7980eb5177138076a778084` | 375–420, 675–725; precise generic scalar target and remaining global suppliers |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/LoopEvaluationThresholdZero.lean` | `e8fa6973fa50015c620b7e1d42b954dfb9ec4678` | 1–120; moving loop bounds still take the three actual weighted row sums |

The concrete positive-trace theorem is proved under (PW2), with every final cut and calibration retained. This audit has not established all moving-family hypotheses of (PW2), and does not close request 3 or W08.
