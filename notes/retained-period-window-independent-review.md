# Independent audit: concrete retained period-window trace budget

## Verdict and exact scope

**Passed as an ordinary finite-dimensional theorem under its explicitly stated hypotheses on the actual normalized period kernels.** The proof preserves the original column normalizers and the prescribed trace calibration. It neither replaces calibration by observed trace nor constructs the missing moving arithmetic family estimates.

Reviewed snapshots:

- `retained-period-window-budget.tex`: SHA256 `955b09684bd212c8a5777e0b9d425788f31011cda86d2f4708082a09ac3bd1fb`.
- `retained-moving-trace-dependencies.md`: SHA256 `9b8ef053c490b174c87ee35fc710e1b6f75514fd8429003d155c89f04afc78e9`.

I independently checked the full algebra, the exact original-calibration trace identity used by the proof, the source/target restriction terms, and the decisive source statements distinguishing what the new pointwise theorem does and does not supply. No numerical experiment is needed for these identities; no Lean replay is claimed.

## Uncut trace estimate

For the literal normalized maps `A_u=c0X_u^(-1/2) P_u`, with the same common target `H`, put

\[
K_{uu'}=A_u^*A_{u'},\quad
S=\bigoplus_u K_{uu},\quad Q=\sum_u A_uA_u^*,\quad
M=\operatorname{tr}S=\operatorname{tr}Q.
\]

The source estimate in (PW2) gives

\[
\|S-I\|_{HS}^2\le q^2R,\qquad
|M-R|\le qR,\qquad
\|K_{uu}\|_{HS}\le(1+q)\sqrt{d_u}.
\]

The use of one common target is essential to the exact expansion

\[
\operatorname{tr}(Q^2)=\sum_{u,u'}\|A_u^*A_{u'}\|_{HS}^2.
\]

The off-diagonal sum is bounded by `(1+tau)(R²-sum d_u²)/D_*`. Dropping its nonnegative subtraction, then adding the diagonal estimate, gives precisely (PW8). With `sigma=D_*/R` and `xi=|D/D_*-1|`, this yields

\[
\frac{D\operatorname{tr}(Q^2)-2RM+R^2}{R^2}
\le (1+\xi)\bigl(1+\tau+(1+q)^2\sigma\bigr)-1+2q.
\]

At the **prescribed** `c=R`, the exact cancellation of the common trace `M` gives

\[
g_R+b_R=
\frac{\|S-I\|_1+\|Q-(R/D)I\|_1}{2R}.
\]

Applying the trace-norm/Hilbert--Schmidt inequality separately in dimensions `R,D` proves (PW4), including its factor `1/2`. The radicand is nonnegative for all stated parameters, including `q>=1`; no small-error assumption is used in the theorem. The simplified (PW10) follows from `1+xi<=2` and `(1+q)^2<=4` when `q,xi<=1`.

Zero-dimensional individual source summands cause no problem. The necessary global guards `R>0`, `D>0`, and `D_*>0` are explicit. No step divides by the observed mass `M`, so zero maps are also covered whenever (PW2) holds for the indicated errors.

## Actual restrictions and prescribed retained normalizer

Apply the independently proved joint source/target restriction inequality with the positive operators

\[
E_s=(I-S)_+,\qquad E_t=(Q-(R/D)I)_+.
\]

For actual source rank fraction `r0`, actual target rank fraction `v0`, and arbitrary prescribed `c0=theta R`, it gives exactly

\[
g_0+b_0\le
\frac{g_R+b_R+1-v_0+(\theta-r_0)_++(v_0-\theta)_+}{\theta}.
\]

Thus (PW6) follows with no observed-trace calibration. At `theta=r0`, its additional numerator is `max(1-r0,1-v0)`, proving (PW5). The target excess is charged once, including when both source and target restrictions are present. The positive guards on retained ranks and calibration are explicit.

The final norm-penalty substitution is conditional on the bound being attached to the **same actual retained theta maps, scalar moduli, heights and normalizer** at every required arithmetic sample. The manuscript states that boundary. In particular, an unweighted estimate for period columns cannot be transferred by merely knowing that each theta/period scalar is nonzero.

## Source and quantitative dependency checks

I reread the following pinned source excerpts in this independent audit, all in `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, under `lean/src/`.

| Source | Git blob | Checked range / conclusion |
|---|---|---|
| `Formalism/SharpRestriction/CuspSpanNormBounds/AdmissibleBoundsFromSource.lean` | `1caea89b8fb520994d0250597e3e6ec76147506e` | 1--110, 110--190, 190--285: original positive-trace parameters, `adm9`, `adm10`, `Conclusion1`, retained `Q0`, fixed `RR` and `Dstar/RR` |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DiagCL.lean` | `fa7dec6d60ea45bdd99e01ed2e39ad8af6e37592` | 1--60: `DiagCL` still explicitly takes `RowBig` and `RowNotScalar`; the proof passes these unchanged into the four-piece diagonal estimate |
| `Formalism/SharpRestriction/CuspSpanNormBounds/LocalBesselAndTopKernel.lean` | `4a96d6fc92d7471ba7980eb5177138076a778084` | 375--420: distinct-word generic scalar estimate with the near-one leading constant, original cut and dual-lattice hypotheses |

These statements support the dependency audit. In particular:

- `Conclusion1` has zero off-diagonal `Kpp`, zero-Gram diagonal error `d_u xK`, distinct-word nonzero-Gram bound `(1+b^-6)d_u d_u'/Dstar`, and diagonal remainder `Gamma d_u²/Dstar`.
- The sharper diagonal `q=sqrt(xK)+sqrt(C0/Gamma)` follows by the Hilbert--Schmidt triangle inequality once the original positive common `Gamma` and `d_u Gamma²/Dstar<=C0` are supplied. This is sharper than merely applying the square inequality with an extra factor 2. It does not bypass the missing full diagonal remainder estimate.
- The new equal-word generic and nongeneric scalar estimates do not remove `RowBig` and `RowNotScalar` from `DiagCL`. Claiming unconditional source nonvanishing from the theorem name alone would be invalid.
- The distinct-word estimate requires the near-one generic main term and small cut/dual-lattice errors. A polynomial-cost bound from `StepThmBPinnedG` cannot imply this leading constant by itself.
- The actual dimension estimate `adm10` is separate from the definition of `Dstar`; the actual rank cannot be replaced by the proposed main term.

**Overall:** the new trace-budget theorem is valid, useful and quantitatively explicit under (PW2). The source audit correctly keeps the actual loop bounds, near-one distinct-word estimate, dimension/window/cut bounds, common-row identification and final moving averaged budget open. It does not close request 3 or W08.
