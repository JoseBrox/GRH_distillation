# The fixed-row weighted count is supplied (W08)

**Closed obligation: PerRowC**, including the original row-label congruence (CompatC). The [finite-adelic proof](../paper/shared/flag-row-congruence.tex) establishes (FC7) without the genericity or nonzero-Gram restrictions of some intermediate source statements. It uses the actual self-dual lattice, row representatives and finite Levi label.

Modulo the original g, the reference hyperbolic pairs, the last line of norm -1, and the two idempotent-supported dual weight modules give a direct decomposition of the reference lattice. Admissibility gives an upper unitriangular action on the isotropic flag and fixes the last line modulo that flag. The actual residue maps identify the supported coefficient ring with the product of residue fields, so the recorded Levi matrices are the true actions on the first weight module (no identity fallback). Equality implies that the relative action is trivial there and, by the perfect hermitian pairing, on the dual weight module. Thus it is trivial on the entire orthogonal quotient. Localization, with the original fixed-convention generators at the primes over g, gives (FC7) on the rational target lattice. No factor of g or field degree is lost.

The [rational normal forms and labels](flag-adapted-normal-form.md) and [term-class theorem](flag-term-correspondence.md) then give PerRowC for arbitrary finite subsets of the original ordered pairs on a fixed row. The bound has the exact integer index range, original reciprocal source automorphism weight, embedded triple cardinality and product of the two datBd factors. The nonnegative extended-real formulation follows by counting only attained triples before enlarging their cardinalities.

This does **not** prove the global zero-Gram norm estimate. The [global fixed-label theorem](flag-global-pair-count.md) now supplies PairsP by the exact genus comparison and finite parameter sum. Complete the amplitude product and the full zero-Gram sum with the original weights. Generic returns and finite-column estimates remain independent.

## Pinned source interfaces

Source jsmorph/rh at ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de, paths under lean/src/.

| Path | Blob | Relevant data |
| --- | --- | --- |
| Formalism/SharpRestriction/CuspSpanNormBounds/GlobAut.lean | 2103e49fe83fce42d4962f85acd9d4f6a589d645 | lamAf, AutInst, Kset |
| Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean | 7f21195438209fd7fc4d0b081fe53297f07fb9c4 | 180–282: frame, Gram, idempotents, approximation, lattice span |
| Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/TermOp.lean | 35f737cb9e89fc17f159a562740961263fbb0ec3 | 194, 207–221, 276–330: kOf, ColSys, TypedRed, leviM, rowOf |
| Formalism/SharpRestriction/CuspSpanNormBounds/IsPrimitiveSub.lean | 5806b474f3381b159d9d80ba86547df0eb0cb4ab | 65–105, 139–145, 175: ModG, IsFixedConv, admissibility, NgX |
| Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/AdmNPf.lean | cfc00db6729a8869f0b410b87b2bb061daabe9b6 | 140–end: normalized congruence |
| Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/IotaDictPf.lean | c60d7d712527a4fc9d65de720fd5728e483cff5d | 17–126: identity and relative Levi label |
| Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/BridgeAR.lean | 1a1c47efcc247f904df3df2eef19b40831f1584c | 52–end: rational congruence |
| Development/AbelianVarietyTheory/Proofs/FlagMeasures/TermsOverRowCompatible.lean | 9cd963e30b73c861883a7f3ac8b7299d3d4750e4 | CompatC and its exact direction |
| Development/AbelianVarietyTheory/Definitions/SemilocalFrames/PerRowC.lean | c406932d46d85320d0a2cfd75fd776219312cf96 | PerRowC, exact statement |
| Development/AbelianVarietyTheory/Proofs/FlagMeasures/TermPairsRowLatticeCountedViaEmbeddings.lean | e7dfe42dc83b4e5a39cfcff0015a17b108abfae1 | termData, pairTrip, perRowC |

Independent mathematical proof and bounded source-interface audit; no Lean replay or full manuscript compilation.
