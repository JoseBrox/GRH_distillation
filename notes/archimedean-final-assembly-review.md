# Independent quantitative review of the sufficient pointwise assembly

Reviewer: the analytic-pointwise agent, separately from the parent assembly author and the character-transport author. This review covers the quantitative assembly and the displayed frame/root/radial algebra. It is not a Lean replay or a proof of the stronger full near-parameter interface.

## Outcome

The constants and spectral budgets in `paper/shared/archimedean-pointwise-assembly.tex` pass the checks below. The actual AP7 family satisfies its additional explicit reserve after enlarging only the fixed gap threshold. The character-transport draft's root Jacobian, block exponents, radial Jacobian, Gram scaling, period-map orientation, and cancellation of the compact-rank factor also pass.

The direct cutoff proof and Wigner cofactor transport were written by this agent, so this document does not purport to be their independent review. They were independently reviewed by the parent and the retained-theta agent; the Wigner transport also received a separate review from the uniform-comparisons agent.

## Pointwise constants

Let `s=r+1`, `m=2s`, `p=6s²`, `a=0` for different types and `a=30s²+6` for equal types. Since `s>=1`,

\[
a\le36s^2=9m^2,\qquad L=2p+a\le48s^2=12m^2,
\qquad d=sL\le48s^3.
\]

For `c=delta+d+1`, the maximum of the two original gap lower bounds `8 C_g s³` and `200 delta` is at least `4 C_g s³+100 delta`. If `C_g>=51`, this is at least `4 delta+192s³+12`, which dominates `4c+8`. A nonempty spectral gap and the coordinate bounds `|lambda_j|<=b` then imply `c+2<=b`.

The cutoff-sensitive derivative count is

\[
5+(4s-2)3s=12s^2-6s+5<12s^2=2p.
\]

Thus the exact quadratic level-zero cutoff limit uses a strictly positive epsilon power even at `s=1`.

With `h=max(C_h,0)`, `b>=3`, and `C_J>=1`, the factor in (PA8) obeys

\[
2(3b)^{2a}b^{(8+2h)m^2+2C_Jm^2L}
\le b^{(13+h+24C_J)m^4}.
\]

Indeed `3b<=b²`, `4a<=36m²`, `L<=12m²`, and `m²>=4`; the stated constant has ample room for the factor two. The source root count `h_gamma<=s²` gives `pi^(2h_gamma)<=b^(m⁴)` for `b>=3`. The character-return factor satisfies

\[
2h r s(1+L)\le2h s^2(1+48s^2)\le7h m^4.
\]

Consequently `C_*=64+16h+24C_J` dominates all displayed exponent losses and the pole coefficient `12`.

## Exact AP7 reserve

The pinned definition was checked directly in `LeadMinorK.lean` lines 108–115:

\[
q_0=C_q^{-1}\min\{h_{NC}/(C_q\sqrt m),\operatorname{cloudGap}\}.
\]

Both divisors are essential. With the actual nonempty cloud-gap set, base all gaps at least `C_g m⁴`, and the retained noncompact gap at least `C_g m^(9/2)(3sn²+n³)`, one gets

\[
q_0\ge C_gm^4/C_q^2.
\]

For `P=Ms³` and the actual AP7 shifts `delta<=sP`,

\[
\delta+s(L+s+1)\le s(P+48s^2+s+1)
\le(M+50)s^4.
\]

Thus the fixed choice `C_g>=C_q²(M+50)` supplies the sufficient pointwise reserve. The further fixed thresholds in `archimedean-ap7-reserve.tex` give all moment and chamber-preservation gaps simultaneously. The original `ConclusionB3` already explicitly asks for `AllGaps(C_g m⁴)` in `OnePlaceEstimates.lean` lines 40–45, so the exponent of the existing consumer hypothesis is unchanged.

## Character-transport algebra

For one complex root let conjugation send the old coordinate `x` to `x_1=q x`, where `q=t_j/t_i>0`. The old canonical density is `(a/pi) dx`; its pushforward is `(a/pi)q^-2 dx_1`. The new standard-character density is `(1/pi)dx_1`. Their ratio is therefore

\[
q^2/a=\eta q^2,\qquad\eta=a^{-1}.
\]

Multiplying over the root pattern yields `alpha_gamma=eta^(d_gamma-2S_gamma)` exactly. The quotient measure scales by its reciprocal, as the Weil identity requires. This independently confirms both the direction and the exponent in (CT10)–(CT11).

The block identities (CT12) follow by direct summation of `1,v,v²`; they give the point-density factor `W eta^(-4S_gamma)` including a terminal singleton. The radial change of variables has real Jacobian `J=a^(2rs)`, while its density has factor `W`. Both terms of the original Gram polynomial scale by the same `J`: the first through the full leading determinant, the second through the scaled product `TT'` and the preceding leading determinant. Therefore `W` cancels from the pointwise-to-radial comparison, leaving exactly

\[
J\eta^{2d_\gamma}=a^{2rs-2d_\gamma}.
\]

The original root pattern has `0<=2d_gamma<=rs`, which proves the bound used in (CT16). These statements include `r=0` (empty first-frame product and empty root pattern) and `k=1` (terminal radial exponent zero).

Finally, for `chi(g)=D^-1 g D`, the asserted period maps `B_1=B_0 sigma(D)` satisfy the correct transformed character covariance. In (CT7), the two factors `sigma(D)` and `sigma(D^-1)` cancel against these transformed period maps in the original coefficient scalar. Thus the compact-finite replacement in (CT9) has the required orientation and preserves both all-cell values and the original radial norm through the already established factorization.

## Source trace

All upstream source checks use `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

| Source | Git blob | Bounded ranges |
|---|---|---|
| `Formalism/SharpRestriction/CuspSpanNormBounds/LeadMinorK.lean` | `793b55df37e7be237b3cb7b37060255ff3c89a3b` | 35–125 |
| `Formalism/SharpRestriction/CuspSpanNormBounds/OnePlaceEstimates.lean` | `d641a2a34206975a819216642052bc0ca832b69a` | 1–52 |
| `Formalism/HermitianCurvature/StatementTBB.lean` | `1943087061b73cb08fe6059f7e9ac9ac2edd6fd8` | 1–63 |

The last source shows that the literal empty-word diagonal factor is `nPt(k,r,TT,head)`, independent of either compact representation; this was also checked independently by the retained-theta reviewer.

## Independent final pinned-row quantifier review

The final `archimedean-pinned-row-closure.tex` passes an additional independent review against the literal source quantifiers. The source first fixes six external real constants and the requested integer weight `A`, then permits choices of `C_B>=0`, `C'_0`, and `C_{ell,0}`, before all original settings, mass data, points, and measures. Accordingly the internal analytic gap threshold `Gamma_g(A)` is chosen after `A`, and `C_{ell,0}>=128 Gamma_g` is allowed. The external `C_g` remains unchanged.

The exact `stdOfHyp_rec` hypotheses are `Cl>=8`, `Ch>=0`, `beta>=2`, `Cw<=beta`, `CT<=beta Ch`, `1/8+2Cg<=beta Ch`, `128|Cs|<=m`, and `|Cs'|<=m`. Its actual output contains both `StdHyp(Cs)` and the extra all-gap bound `Cs' k m³`. The standing hypothesis includes `Cl<=m`; the rank conditions give `k>=m`. Therefore `Cs=Cs'=Gamma_g` and the fixed choice `Cl_0>=max(8,128 Gamma_g)` supply the exact AP7 bound `AllGaps(lambda,Gamma_g m⁴)`. There is no circular dependence on the rank and no new row hypothesis.

The choices `Ch=|CT|+1/8+2|Cg|` and `beta=max(2,Cw)` satisfy the signed-constant inequalities even for arbitrary external real constants. Taking the analytic size `B=b^beta`, the conversion `C_B=beta max(C_rot,0)` gives the original exponential factor. The amplitude/norm constant `K_0` cancels and does not enter `C_B`. All coefficients and this positive factor are fixed before the auxiliary `nuL,ng`; the literal point-sum fields are independent of those auxiliaries. The zero-integral case uses multiplication only and is included.

This verdict concerns the constants and source quantifiers; the exact all-cell normalization and actual point dictionary have their own independent reviews. It does not close the separate retained theta or moving trace interfaces.

Additional pinned source ledger:

| Source | Git blob | Bounded ranges |
|---|---|---|
| `Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/MainEqAna.lean` | `e33ecea05bb5fcc3174714721121ce66bee52460` | 95–138 |
| `Formalism/SharpRestriction/CuspSpanNormBounds/BruhatCellsKronecker/StandardHypothesesOfScaleHyp.lean` | `12810c29fb549816783759e82938887ead969b68` | 1–30, 600–640, 635–660 |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/BDataOfR.lean` | `bfd3071ae72df574b4cf474a1b205c4769d20b3c` | 310–352 |
| `Formalism/SharpRestriction/CuspSpanNormBounds/StandingNumericalData.lean` | `f6b85bc4a9e85ffb73ba7842269f9b010bcf12d1` | 106–160 |

The SHA256 of `StandardHypothesesOfScaleHyp.lean` is `4f54e245e391070de10e0fb9a12a29d9ebf5a05e5896875cf6b0562e0cd06da7`; `MainEqAna.lean` is `62df5432d11a77fc0d42b70fa199a6eb0a24b4ddd8b8808bf8a9c6dd3c8fc8ed`; `BDataOfR.lean` is `e0ecfe6207d5d7b7d76d0bbeef22960d48bb70a479678808cf1ca18525d18057`; `StandingNumericalData.lean` is `4944cc95513fd659cc0a14ba1cf0397a042bc6a32ce509925f09820b4212c8e1`.
