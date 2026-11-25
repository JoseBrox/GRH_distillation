# Independent review: sufficient pointwise assembly and the AP7 reserve

## Verdict

The pointwise assembly and AP7 reserve argument pass the mathematical checks below. The conclusion is the explicitly reserved pointwise theorem and its application to the actual finite positive-minor family. It is not the stronger full `ThmBpDS` interface for arbitrary near parameters or every smaller Gram power.

The retained premises matter: the original local cut/separating-gap alternative, original all-gap and noncompact-gap hypotheses, the all-cell coefficient factorization, the proved fixed-cutoff exhaustion, the actual nonempty cloud-gap range, and the original leading-minor theorem are all used. The new cutoff/spectral argument does not replace any of those premises.

Reviewed snapshots:

| File | SHA-256 |
|---|---|
| `repo/paper/shared/archimedean-pointwise-assembly.tex` | `59206b6aaa1190b16e27c50e2f5169e21dfe0a36b0620f3dad02621d0279bdca` |
| `archimedean-ap7-reserve.tex` | `2383c5ed2bb17972ba1a3c12cd68e4c54415ff47cfdbdc0007166c4b097ddcd4` |
| `archimedean-character-transport.tex` | `53cbd16c89f4b57b39fb9c6512973544ec92e0383ade903a0bb4e4f11f97ace5` |

The coefficient F in the pointwise theorem is understood to belong to the original discrete series with Harish--Chandra parameter lambda-prime. Stating that explicitly in the theorem would remove a possible notational ambiguity.

## 1. Actual moment and gap premises

The existing iterated-minor theorem gives the original norm estimate

\[
\mathcal N(D_s^L F)\le b^{2C_Jm^2L}\mathcal N(F)
\]

under `delta+s(L+s+1)<=q0`, together with the original local hypotheses and the additional all-gap threshold `C_g_mom Lm`. The latter is supplied by a fixed increase of the base cubic threshold because `L<=48s^2` implies `Lm<=96s^3`. It must not be omitted merely because the displayed PA1 emphasizes the q0 reserve.

The proposed values `p=6s^2`, `a=0` or `30s^2+6`, and `L=2p+a` give `L<=48s^2` and polynomial degree `d=sL<=48s^3`. Thus PA2 supplies the exact moment reserve and also the original integer-family margin. The near-parameter all-gap condition alone would not supply that reserve; the draft correctly retains both conditions.

Taking `c=delta+d+1` gives the precise coordinatewise spectral majorant because `|lambda'_j-lambda_j|<=delta`. The arithmetic in PA6 is valid:

\[
\max\{8C_gs^3,200\delta\}\ge4C_gs^3+100\delta
\ge4\delta+192s^3+12\ge4c+8
\]

for `C_g>=51`, `s>=1`. Since the spectral parameters are bounded in absolute value by b and there are at least two of them, `gap_min<=2b`; hence `b>=2c+4`, stronger than the needed `b>=c+2`. The signed standard/dual shift ball remains in the same regular chamber.

The literal source `LeadMinorK.StdHyp` includes a different-type `HasCut` of width `C_g s^2`, or an equal-type `HasSeparatingGap` of width `2C_g s^2+1`. Consequently a fixed threshold `C_g>=36` supplies the two chains and the quadratic cut grid. This is a real source hypothesis, not an inference from `u!=u'` alone. The Wigner shifts remain between the original adjacent endpoints; the corresponding compact label bounds and cross separation survive. At the exceptional cut index only the two inequalities explicitly omitted from NC3 can change.

## 2. Standard-character height and decay are retained

The actual `LocOk` gate applies `StdHyp` to the scaled negative lengths `T*(kappa/ka)^(2r)` and `T'*(kappa/ka)^(2r)`. At standard character `kappa=1`, its upper bound and `ka<=b^C_h` give

\[
T,T'\le b^{C_h(m+2r)}\le b^{2C_hm}.
\]

The gate also supplies `T,T'>=1` in that realization, so the weaker two-sided bounds used in the normalizer lemma are valid. Under character transport, the standardized values `T_1*ka^(-2r)` and `T'_1*ka^(-2r)` equal the original values. The same original moment constant is therefore available; no rank-dependent replacement for C_h is needed.

The source noncompact gap is `C_g m^(9/2)(3sn^2+n^3)`. The established smooth-decay statement supplies all finite derivative seminorms at a common decay exponent at least `(C_g/2)s^4(3sn^2+n^3)-1`. A fixed increase of C_g pays the at-most `48s^3` polynomial loss and the existing fixed-cutoff exhaustion bound. The number of differentiations does not require an additional loss of decay exponent under that all-finite-orders hypothesis.

## 3. Cutoff passage is pointwise on every actual cell

For a fixed represented point of positive full-group Gram, every point in the original orbital integration locus has the same Gram polynomial. Once `epsilon<G(gamma)`, the cutoff factor is identically one on that entire locus. Thus its top point energy is exactly `G(gamma)^(2p) E(FA;gamma)`. This argument applies directly to every relevant nonzero-Gram cell; it does not approach the point through the open cell.

The previously proved spatial exhaustion is used while epsilon is fixed. The independently audited direct compact-suffix PBW argument then gives convergence of every original level-zero word form because

\[
5+(4s-2)3s=12s^2-6s+5<12s^2=2p.
\]

There are finitely many permitted words, so the maximum passes to the limit. The same-form spectral bound applies to the uncut polynomial coefficient and uses exactly the original beta and word normalizer. This gives PA7 with no surviving PBW or cutoff constant.

The different-type case uses `G^(2p)<=|D_s|^(4p)` in the original norm. The equal-type case uses the audited actual Wigner orbital identity and its norm comparison. Its factors `T'^a` and `T'^(-a)` cancel. Both cases give PA8 with the displayed exponent L.

## 4. Constants and exact orbital normalization

The PA9 absorption is safe. Since `3b<=b^2`, `a<=9m^2`, `L<=12m^2`, and `m>=2`, the pre-pole factor is bounded by

\[
b^{1+(44+2\max(C_h,0))m^2+24C_Jm^4}
\le b^{(13+\max(C_h,0)+24C_J)m^4}.
\]

The PA10 scalar is also correctly oriented. In the exact source comparison, the pair measure is `(kappa_N c_N)^2` times the analytic pair measure. At standard character `c=-2i`, each canonical complex root measure has density `||c||/(2*pi)=pi^{-1}` relative to Lebesgue measure. The quotient Weil identity therefore contributes `pi^h` to the orbital integral. Squaring gives

\[
n_L\operatorname{orbSq}_L=A_N\pi^{2h}E,
\qquad \mathcal N_L=A_NjN^2,
\qquad A_N=(\kappa_Nc_N)^4.
\]

The two copies of A_N cancel without bounding that positive scalar or dividing by a radial norm. The original quotient-pushforward uniqueness includes every admitted representative and quotient measure before the supremum is taken. The root count `h<=s^2` gives `pi^(2h)<=b^(m^4)` for `b>=3`. The pole satisfies `L<=12m^2`.

I independently checked the character-transport algebra as well. In CT12, write `x=q+v`; summing `4x(2x+k-1)` gives the stated block term plus `4h(h^2-1)/6`, exactly four times the sum of root distances in that block. The terminal singleton gives `tau^(4(k-1))`, the same as its factor of W. Thus every k-dependent weight exponent cancels before a bound is made.

The compact-finite replacement is legitimate: `F o chi^{-1}` is finite smooth, AP3 explicitly applies to finite smooth coefficients, and one compact-finite H with nonzero new period scalar can replace it after scalar multiplication. The replacement is chosen once for all points and sections. The period-map orientation `B_1=B_0 sigma(D)` is correct; both vectors in the translated coefficient acquire `sigma(D^{-1})`, so their new periods equal their old periods. No claim of compact-finiteness preservation under noncompact conjugation is used.

The return factor has exponent at most `2 max(C_h,0)rs(1+L)<=7 max(C_h,0)m^4`. Consequently PA4 dominates PA9, the root factor, the return factor, and the pole exponent. The zero-norm and zero-period cases follow from the already proved all-cell factorization. A represented point has nonnegative Gram; negative Gram therefore has empty representative set and zero original supremum.

## 5. AP7 reserve and exact scope

The q0 definition has two C_q divisors, and both are retained. In the nonempty cloud-pair range, the base all-gap bound `C_g m^4` and the original noncompact gap imply

\[
q_0\ge C_gm^4/C_q^2.
\]

For `P=M s^3`, `M=ceil(2a_w+4C_*+8)`, the choice `C_g>=C_q^2(M+50)` gives

\[
q_0\ge16(M+50)s^4
\ge s(P+48s^2+s+1).
\]

Each actual positive-minor expansion has total exponent at most P, hence its final coefficient parameter has `delta<=sP`. The last display supplies `delta+s(L+s+1)<=q0` for every one of those final coefficients, as well as the smaller intermediate positive-minor reserve. The AR3 thresholds also dominate both moment all-gap requirements and `200(delta+d)`; the factor 16 from `m^4` leaves ample room in each comparison.

The nonempty cloud-pair requirement cannot be inferred from a lower bound on all spectral gaps if the cloud has fewer than two entries: the source's totalized empty infimum is zero. It is already explicit in `rotated-sum-from-near-bp` (standing range `k>=3`) and in the addendum. The actual pinned-row application must retain its k-large/nonempty-cloud supplier.

Subject to that original range, the AP7 proof only asks for the pointwise theorem on the finitely generated family just checked. Enlarging its fixed base threshold is legitimate: M depends on the requested fixed weight and fixed analytic constants, not on r,k,f. No new rank-dependent hypothesis remains. This justifies the analytic input to the intended `StepThmBPinnedG` application without asserting the stronger unrestricted `ThmBpDS` theorem.

## Evidence

All upstream checks use `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. The key additional direct source checks were:

| Source under `lean/src/` | Git blob | Checked material |
|---|---|---|
| `Formalism/SharpRestriction/CuspSpanNormBounds/LeadMinorK.lean` | `793b55df37e7be237b3cb7b37060255ff3c89a3b` | 35--125: exact StdHyp/LocOk scaling, cut alternative, both q0 divisors, original norm and supremum |
| `Formalism/SharpRestriction/CuspSpanNormBounds/ContinuousRootCoords.lean` | `337f78736ab237cee41a4c81a911fd2a334ec7c5` | 149--224: actual canonical root density and exact root-coordinate Jacobian |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/OrbitalSquareEqHilbertSchmidtNormalisedVector.lean` | `37f16d49c6d78bc6ee1f7615bc3a0fbe763e6484` | 1--85 and 180--270: quotient Weil identity, standard root density, exact pair-measure ratio; exact orbital-scalar statement retrieved by source search |

The source statement and ordinary proof comparisons for beta, same-norm spectral energy, point density, norm transfer, Wigner maps and PBW convergence are recorded in the two preceding independent audit files. I also reread the original iterated-minor theorem, the Jacquet budget transport, and the AP7 positive-minor degree and shift calculation. No Lean kernel replay is claimed.
