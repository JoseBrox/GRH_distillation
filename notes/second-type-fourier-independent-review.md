# Independent review of second-type Fourier, density and leakage estimates

**Verdict: passed under the stated original GL/DS hypotheses.** I independently read the Fourier lemma, the character nontriviality argument, the scalar-fibre measure, and the final weighted sums in `paper/shared/flag-second-type-cancellation.tex`, Git blob `9e92c808009591079285e75cbf82a2555ad01676`. This review closes the Fourier coverage gap in the earlier move/kernel audit. It is an ordinary proof check; I did not replay Lean or rerun the finite diagnostic script.

## Decisive calculations

1. The earlier local section explicitly works over an unramified quadratic algebra, including the split algebra. The saturated lattice W=Λ∩D⊥ has primitive reduction of dimension n−2s in the self-dual ambient reduction. The radical of its restricted pairing has dimension at most 2s. Therefore it contains a unimodular Hermitian summand of rank ρ=n−4s. In the field case, a nondegenerate Hermitian space over the residue field has a vector of nonzero norm even at q=2; splitting it off and using surjectivity of the unramified unit norm yields orthonormal coordinates. The split case uses paired dual bases. Integral orthogonal projection gives U=O^ρ⊥U1. The hypothesis k≥4r+7 implies ρ≥2r+4≥4.

2. For t of conductor exponent i>0 and an arbitrary linear unitary additive character η on O, write I=∫O ψF(tN(z))η(z)dz. In |I|², substituting z=z′+b gives the inner z′-character ψF(t Tr(z′·bar(b))). There is **no division by 2 or coefficient 2** in this trace-pairing argument. Because O/R is unramified (or split) and ψF has conductor R, that character is trivial precisely for b∈π^iO. Hence |I|²≤vol(π^iO)=q^(−2i), so |I|≤q^(−i), uniformly in η and its conductor. The estimate is valid for split O=R×R as well: Tr(z′·bar(b))=z′1 b2+z′2 b1 is a perfect pairing.

3. Tensoring ρ coordinates gives q^(−iρ). There are q^i−q^(i−1) t-frequencies of exact conductor exponent i. The complete error sum is

       Σ(i≥1)(q^i−q^(i−1))q^(−iρ)
       = (1−q⁻¹)ε/(1−ε) ≤ ε,

   with ε=q^(1−ρ). The final inequality follows from ε≤q⁻¹. The zero frequency equals 1 in the density calculation and 0 for every nontrivial additive character of U. Thus both parts of STC1 hold, including characters whose conductor exceeds a and including a=0.

4. Failure of h(v,W)=O forces all ρ orthonormal coordinates into at least one maximal ideal αO. In the field case α=π, [O:αO]=q² and N(α)=π². In the split case α=(π,1) or (1,π), so the index is q and the norm is π. Writing b=2 or b=1, respectively, restriction costs q^(−bρ) and rescaling shifts the quadratic conductor by b. The low frequencies contribute at most q^b; the high frequencies contribute at most q^b ε. Consequently the restricted mass is at most (1+ε)q^{b(1−ρ)}. One maximal ideal gives (1+ε)ε² in the field case; union over the two split ideals gives 2(1+ε)ε. No disjointness assumption is made in this union bound.

5. In STC4–STC5, triviality of χb on U and testing all O-multiples imply h(θ⁻¹Z,U)⊂O by the original annihilator/conductor property. Since U is saturated in the self-dual Λ, its dual in V is Λ+Y: extend the integral functional from the direct summand U to Λ, and subtract its self-dual representative. The remainder annihilates span(U)=Y⊥, hence lies in Y. Thus θ⁻¹Z=z+y with z∈Λ∩D. Exact level j of b means the index j−1 coefficient pair (c,c′) violates RR; in θz it occurs at index j because Z=cu_j+c′u′_j and y∈X_j+X′_j. It forces level(z)≥j+1, contradicting maximality of j. This proves genuine nontriviality for every exact-level pair, including dyadic and split cases.

6. The scalar variable ranges over the whole trace-zero field space, normalized by T=π^aO∩ker Tr. For fixed v, the condition σ∈π^aO, σ+bar(σ)=Q(v) has a solution exactly when Q(v)∈π^aR, since the unramified/split trace is onto. Each nonempty t-fibre is a translate of T with volume one. At residue characteristic two Q(v)/2 need not be integral, but the integral is over that full affine translate, so the proof does not discard it.

7. The normalization q^aβ/βj cancels the exact-level b-fraction βj/β. STC1 bounds the undiscarded row-mass error and phase sum each by ε. The discarded moves lie in the uniform leakage set, so each resulting error is at most (3+2ε)ε. Reversible weighted summation gives 2(3+2ε)ε≤7ε because ε≤1/8. This requires no count of families or restriction of the cancellation statement to an arbitrary subset of a family.

8. The final exponent arithmetic checks: q⁻¹ε²=q^(1−2ρ)≤q^{−(k−2r−5)}, since k−2r−5=ρ−2. The strict-image exponent k−1 is at least k−2r−5. For P≥2, 49≤P^6 and two squared-triangle contributions are absorbed by the additional P^8 used in the draft. Finally 2s²+10s+19≤39s² for every integer s≥1. The separate P=1 and r=0 branches are handled as stated.

## Read ranges and scope

- `flag-second-type-cancellation.tex`: lines 1–110, 115–225, 246–286, 344–420 and 439–511.
- `flag-generic-local-amplitude.tex`, blob `56757feb10a0851168f5efba1a84df3bb0d21539`: lines 1–12, confirming the unramified/split local hypotheses.
- `flag-defect-stratification.tex`, blob `9a73caac13dfcfc84d1124aec9e0e8ab38ad66a1`: lines 1–95, confirming the actual ranks, additive index convention and RR interpretation.

The unchanged move preservation, common Haar normalization and pair-orbit reversibility have a separate independent report. I checked how their conclusions enter the Fourier-to-global summation, rather than claiming to have independently rebuilt every one of those geometric steps here. No blocking issue was found.
