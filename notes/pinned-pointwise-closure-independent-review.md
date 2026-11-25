# Independent audit of PA10 and the literal pinned point-sum closure

**Verdict:** PA10 agrees with the exact pinned source normalizations. The sufficient pointwise theorem and AR9 close the actual `StepThmBPinnedG` consumer when combined with the exact amplitude/row-norm comparison. The necessary quantifier clarification is that the strengthened analytic gap threshold Γg is distinct from the externally fixed Cg. It is supplied through the existing existential Cl0 threshold, not by changing Cg or adding a new premise.

Publication-style addendum: `archimedean-pinned-row-closure.tex`, initial blob `e3921197568c898d79b969b0873caad4ad90240d`, theorem label `thm:archimedean-pinned-row-closure`. This gives the original quantified point-sum conclusion and a direct proof. No Lean replay or full manuscript build is asserted by this audit.

## PA10

For standard character c=−2i, one complex stabilizer root has canonical density norm(c)/(2π)=π⁻¹. Thus the literal root Haar measure is π^(−h) times the analytic root Haar measure. The exact quotient Weil formula multiplies the orbital map by π^h. The literal pair measure is (κN·cN)² times the analytic pair measure, because there are two unipotent integrations. Hence the orbital **square** is

    orbSq = (κN.toReal·cN)^4 π^(2h) ||vecV||².

The literal point weight equals the analytic nPt after swapping the original block-list convention. Multiplying the displayed identity by that weight proves the first line of PA10. On the big cell h=0. The exact radial frame-change formula at c=cStd has conjugation parameter 1 and GamLev=1, and therefore gives

    jNorm2 = (κN.toReal·cN)^4 jN2.

The factor is the same A_N in both equations. Finite positive κN and cN make A_N positive; no bound on it and no division by any norm is needed. For the supremum, Weil uniqueness handles different admissible quotient measures at a fixed representative. The same-point compact/unipotent orbit description and unitary invariance of Hilbert–Schmidt norm handle different representatives. This is the precise meaning of the representative-independence sentence following PA10.

## Quantifier and reserve audit

The literal `MainEqAna.StepThmBPinnedG` fixes external Cg,cb,Cw,cT,CT,C0 and the natural number A before choosing CB,C′0,Cl0. Its conclusion quantifies over every later setting, mass tie, admissible mass datum, pinned ν, and auxiliary νL/ng.

Choose β=max(2,Cw), Ch=|CT|+1/8+2|Cg|, and analytic size B=b^β. AR9 and the sufficient pointwise theorem fix Crot and Γg from A,Ch and the already fixed supplier constants. Set CB=β·max(0,Crot), and choose Cl0 at least 8 and 128Γg as well as the pre-existing comparison thresholds. The context implies m≥Cl and k≥m. The literal hypotheses of `stdOfHyp_rec` are then all satisfied with Cs=Cs′=Γg:

- Cl≥8, Ch≥0, β≥2 and Cw≤β;
- CT≤βCh and 1/8+2Cg≤βCh;
- 128|Cs|≤m and |Cs′|≤m.

Its conclusion gives the original standard hypotheses at size B and all gaps at least Γg·k·m³. Since k≥m, it gives all gaps at least Γg·m⁴. The same source conversion supplies the noncompact-gap estimate used in AR1–AR7. Also k≥m≥8 implies the nonempty cloud-gap-set condition in the actual weighted proof. The reserve is therefore simultaneous across the finite positive-minor and Wigner shift family.

The derivation uses AR9 only for this actual setting. It does not need to prove the stronger `JointNormBoundRotatedUniform` interface on every abstract rank, including abstract small k outside the actual context.

There is no circularity: Ch,β,C*,M,Crot,Γg are fixed from the external constants and A first; then C′0,Cl0 are fixed; only afterward is the setting or rank quantified. The rank lower bound is a consequence of the original context.

## Literal row and auxiliary fields

The exact comparison supplies θ=θ′=1, K_v=1, C1=Ca=Cn=0 and Cfac=K0⁻¹, with K0>0 chosen before every point, section and νL/ng. It gives the original pinned square and the original Ire exactly. The prescribed unitary phase rotation preserves the radial norm and identifies the rotated orbitals in BSumR.

The actual occupied-point construction gives an integral normal-form point above each occupied point. Any chosen lift is injective on a finite set of distinct labels. The exact point-density identity and NG·ND≤normWt give weight comparison constant 1. Thus the original finite sum is at most K0⁻¹ BSumR. AR9 then gives B^(Crot m⁵f) Ire, which is at most exp(CB m⁵f log b) Ire.

In the literal NOfG definition, jacobianSquareBound uses νB alone, and n,NG,ND are the fixed functions nPt,NGPt,NDPt. νL appears in a2 and J2loc; ng appears only in ngen. The point/weight ties are universally quantified over νL/ng, so the actual conclusion has exactly the requested auxiliary quantifiers. Zero Ire causes no exception because every inequality is homogeneous and K0 remains positive.

## Immutable source ledger

All paths are relative to `lean/src` at **jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de**. Every listed decisive range was read. Source algebra was audited as ordinary mathematics; no declaration was accepted solely from its name.

| Module | Blob | Audited decisive ranges |
| --- | --- | --- |
| Development/AbelianVarietyTheory/Proofs/FlagMeasures/StandardBesselScaleBound.lean | 39aaa22c0405f6edbfbcc4b6b2e73b689f5c71e0 | 45–97: point-weight dictionary; 115–142: π-factor bound; 165–216: literal orbital/radial conversion and multiplication by common factor. |
| Development/AbelianVarietyTheory/Proofs/FlagMeasures/OrbitalSquareEqHilbertSchmidtNormalisedVector.lean | 37f16d49c6d78bc6ee1f7615bc3a0fbe763e6484 | 173–220: canonical root measure; 235–246: pair measure; 344–384: exact orbital scalar; 386–400: representative comparison; 406–455: orbital supremum. |
| Development/AbelianVarietyTheory/Proofs/FlagMeasures/BesselEnergyNormalisedFrameChange.lean | c70038ccdf02b0808aaca98b5172d33d318ebed7 | 70–109: exact radial change of frame, specialized to character ratio 1. |
| Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/MainEqAna.lean | e33ecea05bb5fcc3174714721121ce66bee52460 | 116–129: complete literal StepThmBPinnedG quantifiers and conclusion. |
| Formalism/SharpRestriction/CuspSpanNormBounds/BruhatCellsKronecker/StandardHypothesesOfScaleHyp.lean | 12810c29fb549816783759e82938887ead969b68 | 144–169: m≥Cl and k≥m; 365–371: original spectral gap; 610–662: exact hypotheses and proof of stdOfHyp_rec. |
| Formalism/SharpRestriction/CuspSpanNormBounds/SBridge.lean | 5a82ca4e33caad9c065ad11b6c659c8e6b4f5f34 | 67–71: complete StdOfHyp conclusion, including extra Γg·k·m³ all-gap bound. |
| Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/BDataOfR.lean | bfd3071ae72df574b4cf474a1b205c4769d20b3c | 24–34: rotated factorization; 186–223: original ties; 263–286: Cfac quantifiers; 345–399: full generic wrapper and constant placement. |
| Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/BDataOf.lean | 64b8cb0eb74d81bec590fc857868620d5ee131c3 | 115–140: rotated base datum and fourth-power gap; 372–416: norm tie; 582–598: point/weight ties; 641–654: original generic conclusion identical to StepThmBPinnedG. |
| Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ThmBUseR.lean | 16af0476859d9fafdbaef8193f89b1e96a792ee9 | 20–39: rotated sum and uniform interface; 47–105: point-sum comparison, including injective occupied-point choice. |
| Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/PointUniformity.lean | 997c90cde089a64ae1ed8cc8ef6f986ed82c2efc | 74–143: actual occupied-point construction from relevance, integral Gram entries/minors and positivity; no empty-input shortcut is used in this proof. |
| Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/ThmBTies.lean | d5a4d36b48a729cae151d23e65e9ff7de290aa54 | 351–383: NG·ND≤normWt retaining root discriminant; 392–416: exact weight tie with constant 1. |
| Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/MainEqCut.lean | 072770f63ba10f961c64e3073c53c34efd52c1e4 | 126–138: NOfG fields and auxiliary-data independence. |

The supplied pointwise proof and its spectral/cutoff/moment ingredients have separate independent review records. This audit checks the normalization and final concrete consumer assembly; it does not identify the retained theta columns or establish the still separate common-row/see-saw bridge.
