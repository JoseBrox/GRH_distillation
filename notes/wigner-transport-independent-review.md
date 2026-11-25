# Independent review of the actual Wigner transport

**Verdict:** the orbital factorization, Hilbert–Schmidt comparisons, radial moment inequality, and exact cancellation of the T′ factor in the inspected draft are valid under its stated compact-map and finite-decay hypotheses. This is an independent ordinary-mathematical audit, not Lean kernel replay.

Audited draft: `archimedean-wigner-transport.tex`, Git blob `3922a511cb69e572e4f23042a7d6f9d702bc4d85`, lines 1–188. The repository copy has the same blob. The compact two-chain maps were previously independently audited; this review concerns their transport to the original orbital maps.

## Decisive checks

1. **Actual cofactor and its full covariance.** The fixed ordinary source `paper/sections/recovered/84-rl-section.tex`, blob `b871894726975682950625508d473075d41418cb`, lines 13–117 and 120–195, defines the cofactor vector using the last row of the adjugate. The calculation gives norm square G/T′ and degree s=r+1 in conjugate matrix entries. Under both compact and both upper-unipotent actions, it gives Ω(k_L⁻¹n_L⁻¹gn_Rk_R)=k_R⁻¹Ω(g). This uses polynomial adjugate identities, so it remains valid when internal minors vanish. The leading minors are invariant under the same actions. The displayed polynomial degree of G^p A(Ω) is at most 2sp+as, as required.

2. **Exact integrand factorization.** Compact covariance gives A(k_R⁻¹Ω)=π′(k_R)⁻¹A(Ω)π_±(k_R). Consequently

   π(k_L)F(g′)A(Ω(g′))π_±(k_R)⁻¹
   =π(k_L)F(g′)π′(k_R)⁻¹A(Ω(g)).

   The final factor is independent of every integration variable. The same character, compact measures, unipotent measures, and discarded-stabilizer quotient occur on both sides. Thus Orb_±(F A)=Orb_0(F)A(Ω) with no scalar or representation-dimension correction. This argument does not require F itself to be covariant under the right compact group.

3. **Hilbert–Schmidt lower and upper bounds.** Applying the compact lower bound to B*e for an orthonormal basis of the left target and summing proves the stated lower bound for BA_±, with the same κ². The operator upper bound proves the upper Hilbert–Schmidt comparison. Both use the original point density, which depends on k,r,T,T′ and the point, not the shifted compact highest weight. No sum over a basis of W_± appears and there is no hidden compact-dimension factor.

4. **Original radial moment.** On the positive domain, 0<G=|D_s|²−TT′|D_{s−1}|²≤|D_s|². Orbital invariance of G and D_s gives

   E_±(G^p F A;γ) ≤ (T′)⁻ᵃ |D_s(γ)|^(4p+2a) E_0(F;γ)
   = (T′)⁻ᵃ E_0(D_s^(2p+a)F;γ).

   Integration against the unchanged big-cell measure is precisely the displayed radial norm inequality. Tonelli is sufficient before finiteness; the separate moment theorem supplies the finite bound in the intended application.

5. **Cancellation and orders.** The pointwise lower estimate introduces T′ᵃ and the radial upper estimate introduces T′⁻ᵃ. They cancel exactly before any uniform estimate. For p=6s² and a=30s²+6, the Gram pole is 2p+a=42s²+6≤48s² for every integer s≥1. The polynomial degree is s(2p+a)≤48s³. These inequalities include r=0. The cofactor formulas and Hilbert–Schmidt arguments also include k=1.

## Verification boundary

This review does not supply the different-type pointwise bound, the compact two-chain construction, the spectral moment theorem, or a cutoff/density theorem. They are explicit inputs in the draft and are being established and audited separately. In particular, this audit does not justify a stronger all-small-p or unrestricted `ThmBpDS` statement. It certifies the exact transport needed by the retained-family application once those inputs hold with the stated reserve.

Absolute convergence is required to pass the exact factorization through the actual quotient integrals for the finite-decay functions. The draft explicitly invokes the established finite-decay quotient-integrability bounds or proved compact exhaustion, rather than silently inferring it from compact covariance.
