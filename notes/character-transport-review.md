# Exact character transport for the actual pinned row

**Status:** ordinary proof written in archimedean-character-transport.tex. The independent archimedean agent reviewed CT1–CT16 and confirmed the root-measure orientation, block exponent identities, radial and Gram Jacobian, exact cancellation, and period covariance. The independent retained-theta agent separately verified CT12, including the terminal singleton, and CT8–CT9, including the actual finite-smooth scope of AP3, continuity/density, and the point/section-independent compact-finite replacement. Root review is pending. Current draft Git blob: **33a9364dbf875ba27de4f0514d7c3edf3cad1b67**. No Lean replay has been performed.

## Actual character versus root-Haar scale

The canonical choice theta=1 fixes the root-Haar normalization. It does not make the character parameter equal to one. The literal raw toBessel datum has
\[
c=2a,\qquad a=\mathrm{kaRe}(D)=D.\mathrm{host.ka}/(g_0g_1).
\]
After the already prescribed phase rotation its character is \(c=-2ia=\mathrm{cOfDpsi}(a)\). The pointwise standard-character gate requires \(c=-2i\).

Use the frame transformation
\[
\eta=a^{-1},\qquad\tau=a^r,\qquad
t_j=\tau\eta^{r-j}=a^j,\quad0\le j\le r.
\]
The diagonal unitary-group element D scales the first r isotropic basis vectors by \(t_j\), the opposite ones reciprocally, and fixes the middle space. The group map is \(\chi(g)=D^{-1}gD\); the negative vectors are multiplied by tau. Thus the new character is \(\eta c=-2i\), while the representation, compact parameters, and spectral reserve are unchanged.

The original standardized size data are preserved:
\[
T_1=a^{2r}T,\quad T'_1=a^{2r}T',\qquad
T_1(1/a)^{2r}=T,\quad T'_1(1/a)^{2r}=T'.
\]
The actual LocOk lower bounds \(Ta^{2r},T'a^{2r}\ge1\) become the standard-character lower bounds \(T_1,T'_1\ge1\).

## Exact factors and cancellation

Let \(P_\gamma\) be the root pattern, \(d=|P_\gamma|\), and
\(S=\sum_{(i,j)\in P_\gamma}(j-i)\). Put
\[
\alpha=\eta^{d-2S},\qquad
J=\tau^{4(r+1)}\eta^{2r(r+1)}=a^{2r(r+1)},\qquad
W=\prod_{j=0}^r t_j^{4(2(r-j)+k-1)}.
\]

The exact identities are
\[
\begin{split}
\mathrm{orbSq}_1&=\alpha^{-2}\mathrm{orbSq}_0,\\
\mathrm{ptWeight}_1&=W\alpha^2\eta^{-2d}\mathrm{ptWeight}_0,\\
\mathcal N_1&=JW\mathcal N_0,\\
\mathcal G_1&=J\mathcal G_0.
\end{split}
\]

The new canonical root Haar measure is alpha times the pushforward of the old one. This follows because the root coordinate at (i,j) scales by \(t_j/t_i\), with real Jacobian \((t_j/t_i)^2\), and its prescribed character density scales by eta. Its orbital quotient measure must therefore scale by alpha inverse. This is forced by the same Weil identity, not a free change of root-Haar scale.

For each normal-form block of length h with q indices after it, the block entry scales by \(\tau^2\eta^{2q+h-1}\). Its density exponent is \(2h(2q+k+h-2)\), with the terminal-singleton determinant factor having the same homogeneity. The exact algebra is
\[
\begin{split}
4\sum_{v=0}^{h-1}(2(q+v)+k-1)
 &=4h(2q+k+h-2),\\
4\sum_{v=0}^{h-1}(q+v)(2(q+v)+k-1)
 &=(2q+h-1)\,2h(2q+k+h-2)
           +4h(h^2-1)/6.
\end{split}
\]
The final term is four times the sum of root distances in that block. This proves the point-density identity on every cell, including zero internal minors.

On the big cell the root pattern is empty and the amplitude scalar is one. The radial coordinate change is \(q_j\mapsto t_j^2q_j,\ \zeta\mapsto\tau^2\zeta\), with real Jacobian J and weight multiplier W. This proves the norm identity. Both terms in the Gram polynomial scale by J.

Hence the entire k-dependent factor W cancels before estimation. A standard-character bound with majorant B gives
\[
\mathrm{ptWeight}_0\,\mathrm{orbSq}_0
\le a^{2r(r+1)-2d}
      B(a^{2r(r+1)}\mathcal G_0)\mathcal N_0.
\]
No division by an orbital value or a radial norm occurs.

## Literal compact-finite coefficient legality

The direct transported function \(\widetilde F=F\circ\chi^{-1}\) is finite smooth, but torus translation need not preserve finiteness under the chosen maximal compact subgroup. We do not assert that it does.

With the exact pushed subgroup measures, the new period-normalized maps are
\[
B_1=B_0\sigma(D),\qquad B'_1=B'_0\sigma(D).
\]
Therefore \(s_{\sigma,1}(\widetilde F)=s_{\sigma,0}(F)\). Choose one compact-finite rank-one coefficient H with nonzero new period scalar, and multiply it by
\[
s_{\sigma,1}(\widetilde F)/s_{\sigma,1}(H).
\]
The already proved all-cell factorization AP3 identifies the resulting compact-finite coefficient with \(\widetilde F\) at every original orbital evaluation and in radial norm. This choice is made once, before the point and section. If the numerator is zero, choose the zero coefficient; AP3 gives all-cell vanishing. No extra coefficient scalar remains in the identities.

## Uniform estimate

Since \(0\le2d\le r(r+1)\), if \(a,a^{-1}\le b^{C_h}\) and the standard bound is
\[
b^B\max\{1,\mathcal G_1^{-1}\}^{p}\mathcal N_1,\quad p\ge0,
\]
the actual bound has constant
\[
b^{B+2C_h r(r+1)(1+p)}
 \max\{1,\mathcal G_0^{-1}\}^{p}\mathcal N_0.
\]
For \(p\le48(r+1)^2\), the additional exponent is at most
\(7C_h(2r+2)^4\). This transport consumes no spectral reserve and introduces no new shifted representation; it transmits only the standard-character estimate actually proved on the retained family.

## Immutable source ledger

All paths are relative to lean/src in **jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de**. Bounded excerpts were read; no declaration was treated as proved merely from its name.

| Module under Formalism/ | Blob | Audited ranges |
| --- | --- | --- |
| SharpRestriction/CuspSpanNormBounds/NormalizedLocalScale.lean | 7a23e65a713ef4b29ab0bda15f7ca084baf06bfb | 215–241: actual toBessel character. |
| SharpRestriction/CuspSpanNormBounds/SBridge.lean | 5a82ca4e33caad9c065ad11b6c659c8e6b4f5f34 | 20: kaS; 79–82: phase-rotated toBesselK character. |
| SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean | d008b93b66125f83b7adb112628b058dde3b1096 | 153: cOfDpsi(s)=-2is. |
| SharpRestriction/CuspSpanNormBounds/LeadMinorK.lean | 793b55df37e7be237b3cb7b37060255ff3c89a3b | 68–80: exact LocOk gates; 168: kaRe. |
| SharpRestriction/CuspSpanNormBounds/ContinuousCjIT.lean | d911c84665b7386353e863db7e29752e36a14f8a | 12–28: tF, dM, cj and inverse; 132–172: unitary-group membership and bijection. |
| SharpRestriction/CuspSpanNormBounds/TrD.lean | 1c8e889b6ac92ad9d3322001a68bc92b9d4aea70 | 13–44: same representation and parameters, scaled character/vectors, pushed measures. |
| SharpRestriction/CuspSpanNormBounds/StarVecMulDM.lean | 77305371eeb31407d807adf58bc7f090c908a312 | 13–14: alpha; 34–47: Gram-matrix and big-cell scaling. |
| SharpRestriction/CuspSpanNormBounds/DMiMulVecApply.lean | 7ca4d27f27bbc2d8735f8a9778b4e3c7fadb1a5f | 77–109: ell_cj and psi_cj, exact character transport; 127–172: subgroup and stabilizer transport. |
| SharpRestriction/CuspSpanNormBounds/ContinuousRootCoords.lean | 337f78736ab237cee41a4c81a911fd2a334ec7c5 | 149–224: root-density and real-Jacobian calculation, including canonical density norm(c)/(2pi). |
| SharpRestriction/CuspSpanNormBounds/BlockExponentKappaIdentity.lean | ff056c9acef4cefa0727dc876a5f95850d4034b4 | 17–32: W and density exponents; 73–116: root distance sums and alpha; 130–178: block algebra; 208–228: exact density identity. |
| SharpRestriction/CuspSpanNormBounds/BcWeightEqZeroOf.lean | ae09fd6111b855576ef1bb1579d56efc1974f609 | 14–81: radial map, Jacobian and weight; 117–147: exact radial norm identity. The written null-boundary argument also covers k=1. |
| SharpRestriction/CuspSpanNormBounds/RatioInvLeFrameFactor.lean | 5a09c2fb443bc936501912801c5a54e540af0988 | 36–40: transformed point; 101–134: leading minor, Gram, root-pattern invariance; 188: root count bound. |
| SharpRestriction/CuspSpanNormBounds/IsPtRepTrDat.lean | f7bd0a8950342c4c380db2a0a302fbb5040a55ad | 63–74: admissible transformed datum and points; 95–147: exact orbital-square identity and converse transport; 149–189: Jacobian and W identification. |
| PeriodIntegrals/CapelliEig.lean | 9a58e4b577568c67a155315abd33b73b53330ff9 | 19–25: literal compact-finite coefficient predicate, motivating the AP3 replacement. |
| SharpRestriction/CuspSpanNormBounds/TheoremBConstants.lean | db06cb5a048c6da5b2edf1d326facacc309ff99e | 139–190: the original consumer uses eta=ka inverse and tau=ka^r, preserving its standardized T gates. |

## Boundary

The proof retains the prescribed phase rotation and original pinned measures when returning to the row. It does not infer the stronger full ThmBpDS or all-small-p result from the sufficient retained-family reserve. The spectral/differential and cutoff arguments establishing the standard-character estimate remain separate inputs to this transport.
