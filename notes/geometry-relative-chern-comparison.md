# Relative Chern correction: exact descent from the original test lattices

**Result.** [The relative Chern theorem](../paper/shared/geometry-relative-chern-comparison.tex) proves the full two-equation numerical correction **from the original pointwise lattice facts**, via two quotient comparisons in relative K-theory. It also gives a common projective birational modification on which the original TestFacts descend, without adding any numerical height or intersection loss. This substantially shortens the W10 algebraic model/intersection part, but does not yet prove the actual test facts on the induced torsion orders, or the entire linked tower.

## Exact identities and source matching

- RC1: retain the actual affine coefficient lattice A, H=A^vee, the graphs Gam and Del, and the two image/kernel conditions.
- RC2: retain the character-line ideals I=xId, coordinate grades D=dId, nested cotangent lattices K, and the step graph B. The three identities are D=I, the second projection onto K, and the span-of-p-th-powers kernel at the successor label.
- RC6: two graph quotients give [H:T]=[Lie:W]+[Om:OmHT]+[w^-1 Lie:Lie] in relative K with support on the special fibre.
- RC7: the two projection sequences of the step graph, dualized with the same coordinate identifications, give [I_tau,i^vee:(I_phi^-1 tau,i^vee)^p]=[K_tau,i^vee:K_tau,i+1^vee]. This telescopes because K_0=Lie^vee and K_n=p Lie^vee.
- RC4: after applying k! times the localized Chern character with the original complementary Q, the source Relations follow exactly: C_tau=h_tau-La_tau/(p-1), p^k h_tau=h_phi tau+La_phi tau. The multiplier k in La is retained; div(p) is not set to zero by forgetting the support.
- RC5: finite orbit formula with m=orbit length: h_tau=(sum_{a=1}^m p^{k(m-a)}La_phi^a tau)/(p^{km}-1). No limiting argument needed. Absolute coefficient row sum is 1/(p-1)+1/(p^k-1)-2/(p^{km}-1). The aggregate first correction on any complete orbit is zero, but an individual label need not vanish.
- The common-model lemma constructs the required locally free images by relative Grassmannians, identifies kernels after flattening images, and descends via faithfully flat extensions of height-one DVRs and reflexivity on a normal scheme. It keeps the original bundles by pullback. No claim of a small-height flattening model is needed for the numerical identities.

Classical intersection input: Fulton, *Intersection Theory*, 2nd ed., §18.1 (Theorem 18.1, Proposition 18.1, Corollary 18.1.2, and the graph construction over an arbitrary scheme). [Stacks, §42.50](https://stacks.math.columbia.edu/tag/0FB0), Lemmas 42.50.2 and 42.50.4, gives the localized power-sum construction for perfect objects and pullback; the localized class is evaluated on the supporting fibre before pushforward to the model. This is not an application of the ordinary Chow class of a principal divisor.

Pinned source revision: jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de, prefix lean/src/Development/AutomorphicSpectrum/:
- Definitions/CommutativeAlgebra/LieLatticeData.lean (blob 76c510e0d9b024a9059e4b95b7d02c40a81ce507), definitions af, hh, dId, xId, kk, stepGraph, imH, kerH, Base, Good1, Good2, Facts, TestFacts.
- Definitions/CommutativeAlgebra/IsLatticeFamily.lean (blob 0d06e1239cc6255862c2f9ac33178e9d8601ed31), lines 18–52, including CkRelations and homogeneous Q.
- Definitions/DivisibilityTowers/BundleChernComparison.lean (blob 16936b384d6fe65a412205db633bfbe6d588b2ff), lines 36–83 and 101–126, defining ck, laNum, Relations, LabelChernComparison, rootPs, liePs, bracket and FlagChernComparison.
- Proofs/AlgebraProofs/ArithmeticRelationsStatementHolds.lean (blob 2680644e3065dd4cb33bc66051b6329e315e27b0), lines 12–46, original route through lattice_family_ckRelations and UniformizerModelPermModuleLattice.
- Proofs/AlgebraProofs/LatticeFamilyModelFacts.lean and LatticeFamilyModelComparison.lean, common models; ModelOverPrimePermModuleLattice.lean, descent of CkRelations; LocalComparisonOfOrbitsHolds.lean, the original geometric-series solution.
- Proofs/DivisibilityProofs/LinkedTowerPowerSum.lean, downstream Prop6. The two-level global linkage also uses the original metric/model hypotheses in Definitions/DivisibilityTowers/LocalAtPlaces.lean.

## What remains

The [torsion-character flag reduction](geometry-torsion-character-flags.md) now proves the finite-flat annihilator and discriminant identities, gives two exact step-graph comparisons from the original chart pins and obtains the coordinate equality from quotient GenAF without separate full-order tightness. The actual remaining TestFacts (chart pins, generation and Hodge image/kernel) must still be established for the original induced torsion orders and pairings, with the same labels and roots of unity. In particular, equality of two degrees or approximate Hodge–Tate exactness is not enough for the three coordinate identities RC2. The source's relevant chain includes the HodgeTatePoints modules RaCpaf, RaSmith, RaCoord, RbAflat, RcFlag, RdChain, RdFlag, RiRank, StightBad, and the corresponding fundamental ideal and Hodge lattice statements. The previous corrected-flag theorem gives the separate trivial flag and nef conditions, not these pointwise identities. Check the actual dual/label identifications and linked metric model construction, then use the exact signed delta polynomial in the original tower mean. No closure of W10 or W08 is asserted.

Verification: checked the algebraic signs, scalar divisor normalizations, full orbit sum, and the precise base/test hypotheses against the cited pinned source. Written proof only; no Lean replay or independent full manuscript build in this checkpoint.
