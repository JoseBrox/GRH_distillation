# Exact cancellation in the uniform amplitude / row comparison

Status: written direct supplier for the actual concrete `StepThmBPinnedG` route, independently reviewed mathematically. The root agent checked the scalar cancellation, consumer quantifiers and radial Jacobian. The retained-theta agent checked the all-cell coefficient matching, absolute majorant, actual nonzero-period argument and the literal equality of radial definitions. This supplies the normalization comparisons. AP6 for the actual finite shifted family is now supplied by the separate [pointwise assembly and reserve check](w08-analytic-and-retained-continuation.md). No Lean replay has been performed.

Pinned source: `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

## 1. The consumer does not require a uniformly bounded comparison scalar

`Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/BDataOfR.lean`, blob `bfd3071ae72df574b4cf474a1b205c4769d20b3c`, lines 24–34 and 263–287, allows an arbitrary nonnegative `Cfac`, chosen after the row and before all represented points, sections, `nuL` and `ng`. The only required norm bound is

\[
C_{\rm fac}\prod_v M_v\le b^{C_n m^2f}I_{\rm re}.
\]

Thus the source's detour through `RowRestUnifR` (which fixes `Cfac=1` by rescaling root Haar measures into a window) is unnecessary. Keep the original canonical root measures, all local scales equal to 1, and retain `Cfac` until the radial identity. This preserves the actual pinned global measure and original `Ire`.

## 2. Three scalar conventions

Fix the original words `u,u'`, their real places, actual local period functions, and the original mass datum. Write

\[
c_u=\frac{\mu_{N,u}(F_{N,u})\mu_{H,u}(H_u)}{\dim V_u},
\quad c_{0X,u}=V_K c_u,
\quad c_{u,v}=\frac{L_{u,v}}{\dim V_{u,v}},
\]

where `L_uv` is the positive finite squared local quotient mass established in `flag-local-data.tex`. The mass datum's `c0` is `c_u`, not `c0X_u`; the latter includes `V_K`. This distinction is essential.

Under the fixed unitary frame and type transports, the actual local normalized orbital operator is

\[
\mathcal J_v(g)=a_v U_vJ_v(g)U_v'^{-1},\qquad
|a_v|^2=\kappa_v=(c_{u,v}c_{u',v})^{-1}>0.
\]

The literal global tensor operator has squared scalar

\[
s_{\rm gl}=
\left(\frac{V_K}{\sqrt{c_{0X,u}c_{0X,u'}}}\right)^2
=(c_uc_{u'})^{-1}.
\]

Set

\[
K_0=\frac{\prod_v\kappa_v}{s_{\rm gl}}
=c_uc_{u'}\prod_v\kappa_v>0.
\tag{U1}
\]

`K0` depends only on the fixed pair of words and matched local choices, not on the represented point, radial section, or pinned quotient representative measure. The actual product Weil formula and Hilbert–Schmidt norm of a tensor product give

\[
\prod_v\|\mathcal J_v(g_v)\|_{\rm HS}^2
=K_0 J_{\rm pin}^2(w).
\tag{U2}
\]

At arbitrary pinned quotient measures, invariance of the rank-one integrand along the stabilizer makes the integral depend only on the quotient pushforward; the Weil formula identifies that pushforward. This is why changing measurable representatives introduces no scalar. All conjugating type maps are unitary. No division by `J_pin(w)` occurs; (U2) includes zeros.

Source interfaces: `.../RootLatticeThresholds/LocNorm.lean`, blob `6cbd8f5dd509d8870039d7bd7933a4de5aa799c0`, lines 18–34 and 43–65; `.../RootLatticeThresholds/AmpWin.lean`, blob `2b5c474b87e0118ff7d31de929b9d6d8b3484863`, lines 21–69, 82–110; `CompanionTheory/AutomorphicTheory/UniformLocalFormulas/RankOneTermInvariant.lean`, blob `6b24ade1fe56dc5b96becb3ef13f0b086a340d61`, lines 72–90 and 189–254.

## 3. The radial Jacobian is explicit

Put `rho=rd(E)=2v`, `s=r+1`, and for `0<=a<r`

\[
\lambda_a=\rho^{-2(r-a)},\qquad M_a=2(r-a)+k+1.
\]

On an original diagonal Gram parameter `z=(z_0,...,z_r)`, the local frame change sends

\[
q_a=\lambda_a z_a\ (a<r),\qquad q_r=z_r.
\]

The original Gram–Jacobian weight is

\[
W(z)=\prod_{a<r}|z_a|^{2(M_a-2)}
(|z_r|^2-TT')^{k-1}
\]

on `z_a != 0` and `|z_r|^2>TT'`. This follows from

\[
G(\operatorname{diag}z)=\prod_{a<r}|z_a|^2(|z_r|^2-TT'),
\quad \operatorname{Jac}(\operatorname{diag}z)
=\prod_{a<r}|z_a|^{4(r-a)}.
\]

The arithmetic parameter measure uses `2 dx dy` in every complex coordinate; `MM_v` uses ordinary `dx dy`. Complex scaling has real Jacobian `lambda_a^2`. Consequently

\[
K_{\rm pl}=2^{r+1}\prod_{a<r}\lambda_a^{-2(M_a-1)},
\quad
\left(\prod_v\kappa_v\right) I_C=K_{\rm pl}^f\prod_vM_v.
\tag{U3}
\]

This is first an identity of nonnegative extended integrals by Tonelli, including arbitrary sections: any two representatives of the same diagonal Gram matrix differ by the original two Bessel subgroups, and hence their orbital operators differ by unitary factors. Hyperplanes `z_a=0` and the circle `|z_r|^2=TT'` have Lebesgue measure zero, so the strict/open-domain conventions do not alter the integral. This handles `k=1`, where the boundary power can be 0, as well as `r=0` (empty product, `Kpl=2`).

The elementary sum gives

\[
\sum_{a<r}4(r-a)(M_a-1)
=\sum_{j=1}^r4j(2j+k)
=2r(r+1)(k-1)+\frac{r(r+1)(8r+10)}3.
\]

Therefore

\[
K_{\rm pl}^f
=2^{f(r+1)}\rho^{2r(r+1)(k-1)f}
\rho^{fr(r+1)(8r+10)/3}.
\tag{U4}
\]

The *literal* two `FrameInputs` equations say

\[
I_C=c_uc_{u'}K_{\rm pl}^f I_{\rm re}.
\tag{U5}
\]

The finite-energy justification in the next section permits cancellation of the positive finite `Kpl^f` in U3–U5, giving

\[
\prod_vM_v=K_0I_{\rm re}.
\tag{U6}
\]

No covariance formula or separate upper/lower bound for `K0` is needed. In particular the large rank/field factors in U4 are never separately estimated.

Source interfaces: `Formalism/HermitianCurvature/StatementPN.lean`, blob `fc7e8086bbe8872adbdb3a86422fe4a2ee6a6e62`, lines 15–47; `.../RootLatticeThresholds/CarrierEnergyCV.lean`, blob `5e6d956706daea68e7a0ed34ac81842726ba0626`, lines 50–96 and 296–327; `CompanionTheory/AutomorphicTheory/UniformLocalFormulas/HilbertSchmidtDiagonalInvariant.lean`, blob `00cf0c0e55fc1afc4d44b3d0cbba2a10b02ede11`, lines 151–217; `.../UniformRestrictionOfEnergy.lean`, blob `2235fb6e737db05bd6ff553f1547adcda6a08301`, lines 29–59.

## 4. Matching a single coefficient on every cell

Use period-normalized nonzero maps `B,B'` and the original common lowest vector `v0`, writing actual local functions as `Phi(g)=alpha B sigma(g)v0`, `Phi'(g)=alpha' B' sigma(g)v0` with `||v0||=1`. The constants are finite and nonzero; no uniform estimate for their reciprocals is required.

For smooth compact-finite `x,y` with `Bx != 0`, `B'y != 0`, set `S=||Bx||^2||B'y||^2`. The all-cell relative factorization AP3 applied to

\[
F_0(g)=\langle\sigma(g)y,x\rangle(Bx\otimes B'y^*)
\]

gives `Orb(F0,g)=S T_g` at every represented relevant nonzero-Gram cell. Keep the original compact and unipotent Haar measures throughout and define

\[
q_{B'}=\int_{S'\backslash G}\|B'\sigma(x)v_0\|^2\,d\dot x\in(0,\infty).
\]

This is positive and finite directly from the given positive finite quotient mass of `Phi'` and `Phi'=alpha' B' sigma(.)v0`. Its numerical value is unnecessary: in particular no compact-type dimension or formal-degree normalization is silently introduced. The exact relative identity is

\[
q_{B'}T_g=\int_{R'\backslash G}
B\sigma(gx)v_0\otimes(B'\sigma(x)v_0)^*\,d\dot x.
\tag{U7}
\]

In AP4 divide by one fixed nonzero factor `<a,Bx>`, replace `y` by `sigma(x)v0`, replace the second test vector by `B'sigma(x)v0`, and integrate over `S'\G`. Equivariance gives `tau'(s')B'sigma(x)v0=B'sigma(s'x)v0`. The two Weil identities disintegrate `R'\G` over `S'\G` with fibre `R'\S'`, so the left integral is the right side of U7 and the right integral is `q_B' T_g`. This is a pointwise argument for each fixed relevant nonzero-Gram `g`.

Here is the required absolute-convergence verification. Choose a symmetric submultiplicative Frobenius norm `N>=1`. The original smooth coefficient estimate gives `|<sigma(h)v0,x>| <= C_x N(h)^(-a)` for the fixed smooth test vectors used to expand each Bessel map through AP1. For `0<=b<=a` and `a-b>4n^2`,

\[
\int_G N(h_1x)^{-a}N(h_2x)^{-a}\,dx
\le N(h_1h_2^{-1})^{-b}\int_GN(y)^{b-a}\,dy<\infty.
\]

Indeed `N(h1 h2^-1)<=N(h1 x)N(h2 x)`. Allocate `b` powers to this factor, discard one of the two remaining factors, which is at most 1, and use left Haar invariance. The group-volume argument in `global-norm-frontier-quotient-mass.tex` actually proves the stronger threshold `2n^2`, so `4n^2` suffices. The actual terminal quotient properness estimate gives

\[
\int_{\Delta_gR\backslash(S\times S')}N(s^{-1}gs')^{-b}\,d\dot{(s,s')}<\infty
\quad\text{for }b>64(r+1)^2(2n^2+1).
\]

For example take `b=256(r+1)^2(n^2+1)` and then `a>b+4n^2`; the original large-gap reserve supplies this exponent. On expanding both period identities, use the simultaneous action `a'·(s,s',x)=((g a' g^-1)s,a's',a'x)` on `S×S'×G`. The coefficients at `s^-1 g x` and `s'^-1 x` are invariant, and relevance cancels the compact-character factors. The composed Weil disintegrations of this quotient bound the full absolute integral by a fixed finite constant times the product of these two displayed integrals (with `h1=s^-1 g`, `h2=s'^-1`). Consequently all changes of order in U7 are legitimate, and the actual amplitude itself is absolutely convergent. The fixed-point properness constant may depend on `g`; it is used only for convergence and never enters a uniform inequality.

Thus the fixed coefficient

\[
F=\frac{\alpha\overline{\alpha'}q_{B'}}{c_NS}\,F_0
\]

matches the actual local orbital operator at every cell. Since it is a finite compact-finite coefficient, the established mixed Jacquet identity gives finite radial norm; on the big cell it is exactly `MM_v`, with its original section, weights and measures. This proves finiteness of every `MM_v` and, by the extended-integral identity U3 with positive finite scalar factors, of the original carrier energy `I_C`. Only then is `toReal` used. This establishes U6 without the pointwise bound AP6.

Nonvanishing of the period-normalized maps can be checked from the actual L2 embeddings, rather than assumed for every abstract representation: the formal-degree-normalized rank-one convolution idempotent fixes the nonzero given seed; multiplicity one makes its range the line of that seed. Its subgroup-integrated continuous kernel is the seed rank-one kernel. Therefore the normalized period form is nonzero and proportional to the actual functional. This is the same actual projector argument in `flag-local-data.tex` and `global-norm-frontier-seed-decay.tex`.

Source audit for the convergence manipulation: `Formalism/SharpRestriction/CuspSpanNormBounds/FrobeniusCoefficientMemLp/SigmaFiniteAmplitudes/FlipOneTwo.lean`, blob `1725d4c8c69f3137b9d8b3302543eec909d4bbfe`, lines 20–121, contains exactly the absolute product-majorant and two-Weil-identity argument, before the Schur evaluation. `FlipOneThree.lean` in the same directory, blob `00396eafaca22657aa366d2151be00a7e6a82a3c`, lines 13–48, inserts the original smooth-decay bounds. `Formalism/LocalToGlobal/SiegelLatticeTheory/TraceIntegralEstimates/AmpOrbCoef.lean`, blob `86f3a8897fca9163ff763cbc6a3282abcdc3c8aa`, lines 93–221, records the corresponding fixed coefficient construction. The proof above retains `q_B'` rather than importing that file's explicit formal-degree scalar.

## 5. Direct uniform conclusion

Choose `theta=theta'=1`, `K_v=1`, `Ca=0`, `C1=Cn=0`, and

\[
C_{\rm fac}=K_0^{-1}.
\]

Then U2 gives the required pointwise product factorization and U6 gives the exact row-norm identity

\[
C_{\rm fac}\prod_vjNorm2(F_v)=I_{\rm re}.
\tag{U8}
\]

At canonical root scale the local orbital matching has no measure-comparison loss. For the full abstract `AmpUnif` window one would use `Ca=max(0,2C1)` because changing a root measure by `theta'` scales its quotient orbital operator by `theta'^{-1}`, hence its square by `theta'^{-2}`. The actual route needs only the case `C1=0`.

The coefficient scalar, all local masses and `K0` may vary with the arithmetic setting, but cancel pointwise versus norm before any uniform estimate. Hence none enters `CB`. Combined with AP6 plus the already proved all-cell weighted rotated summation, this supplies the original `StepThmBPinnedG` point sum with its original pinned measure and `Ire`. AP6 for this family is now proved separately; the retained theta-column dictionary remains a separate obligation.

## 6. Scope and review boundary

The proof is for the actual standing data, including the given integrable projector, positive finite original quotient masses, exact arithmetic/frame ties, original period identity, smooth-decay reserve, mixed Jacquet identity and all-cell factorization. Those actual-data inputs were already written in the manuscript; no stronger universal nonvanishing claim is made. The two radial equations used here are the literal equations in the given `MassDataAdmissible` / `FrameInputs`, rather than a new construction of all `NormInputs` or of the mass datum.

The useful simplification is `Cfac=K0^-1`, which bypasses estimates on arithmetic covolumes and every potentially large coefficient-normalization scalar. It supplies the local amplitude comparison and exact row norm with `C1=Ca=Cn=0`, on the original parameter and measures. The former analytic assumption AP6 is now discharged on the exact family used by the point sum. The actual retained theta-column dictionary and positive-trace estimates are separate. This note and the accompanying TeX have not been Lean replayed; independent mathematical review of the newly written comparison has passed.

## 7. Independent review evidence

The root agent checked `RowBDataGR` quantifiers, the exact `LocNorm.K0` scalar and the exponent algebra U3–U6. The retained-theta agent checked the two disintegrations and convolution majorant in U7, nonvanishing from the actual seed projector, and the following literal radial definitions at the same immutable pin:

- `lean/src/Formalism/SharpRestriction/CuspSpanNormBounds/NormalizedLocalScale.lean`, blob `7a23e65a713ef4b29ab0bda15f7ca084baf06bfb`, lines 188–192: `MMv` integrates the original `bcWeight` times `HS²(A.J W.muG(bigCell))`.
- `lean/src/Formalism/SharpRestriction/CuspSpanNormBounds/LeadMinorK.lean`, blob `793b55df37e7be237b3cb7b37060255ff3c89a3b`, lines 86–88: `jNorm2` is the same radial weight and squared Hilbert–Schmidt norm through `jNormSq`.
- `lean/src/Formalism/SharpRestriction/CuspSpanNormBounds/FrobeniusCoefficientMemLp/AmpBig.lean`, blob `d28135395c082e2c60ffc36b1c8ff263f2286907`, lines 82–195: the big-cell stabilizer is trivial, its canonical root Haar is unit Dirac, the quotient measure is the original `W.muG`, and the orbital measure is the original `pairMeas`.

Thus no compact, root, or coefficient scalar is missing between `jNorm2(F_v)` and `MMv`; they coincide pointwise in the radial integrand. The written null-boundary argument also handles `k=1`, and empty products handle `r=0`.
