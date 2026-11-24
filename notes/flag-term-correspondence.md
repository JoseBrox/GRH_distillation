# Weighted flag terms: integral orbit and embedded-triple comparison

**Status:** the integral frame mover, same-source-row conclusion, reciprocal automorphism multiplicity, term uniqueness at fixed induced isometry, embedded graph and fixed-triple fibre bound have direct written proofs in [flag-term-correspondence.tex](../paper/shared/flag-term-correspondence.tex). These apply to both parent targets with no new field-degree cost.

The critical step is that equivalent flags are transported by a lattice stabilizer; the comparison of the two source rows first uses a projective hyperbolic splitting over the Dedekind ring, including its integral trace-one correction above 2. The remaining ambiguity is measured by the induced automorphism on X-perp/X, not by the group of all lifts to V. Its reciprocal exactly cancels the finite multiplicity. The same frame class and definite isometry determine the original double coset.

The graph in the definite quotient is obtained by matching the primitive flag submodules modulo g and representing the divided pairing by unimodularity. Both projections are onto, both kernels are the g-multiples, and the pairing is preserved modulo g. The index is the original fixed index, and the quotient has at most j <= r generators, by its injection into a quotient of the j-dimensional isotropic space modulo a full lattice. Local Smith form and CRT are needed for the global generator bound.

For paired terms the actual congruence on Lambda intersect X-perp yields the original embedded triple (not an arbitrary mod-g isometry). Its fibre is bounded by the product of the two original datBd expressions, using the preceding fixed-normal-form weighted lattice sum. No extra automorphism-group factor occurs.

The final theorem is deliberately stated **conditional on the exact rational adapted-normal-form incidence (NFExC, LabC) and the original row-label congruence**. The relevant-term proof in the source runs through NFFull and a signed-block cell argument; it is not enough to assume just zero Gram determinant. These two remaining source interfaces must be reconstructed before claiming full PerRowC. The row admission proof itself is included (fixed-congruence local coefficients, integral upper-unitriangular change, then localization). The zero-Gram parameter sum, generic-return and finite-column estimates are not claimed.

## Source audit

Pinned jsmorph/rh revision ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de; paths under lean/src/Development/AbelianVarietyTheory/ unless noted. The proof matches the following read declarations:

| File | Blob | Content |
|---|---|---|
| Definitions/SemilocalFrames/AdaptSelf.lean | 97311ee488582c1c5ecf2f6cba4e4a79ffdf2eee | SameGr, Adapt, omI, datOf, IsH, FrEqv, datBd (12–44) |
| Definitions/SemilocalFrames/FlagPairDefinitePartLattice.lean | ca3429e212b3df6c27de7ca085c2063c2aad17cd | IsModIso, IsFrame, IsAdm, iotaGraph |
| Definitions/SemilocalFrames/NormalFormDualOrthogonalLast.lean | 65d77595fcdcf1ec568ead93a509298b4be7e292 | NF, GenBy, IsDat, Trip |
| Proofs/FlagMeasures/SmulMemOfOne.lean | f5578025795aae19dc35968e1891ade39d7811a7 | integral frame movement (244–423) |
| Proofs/FlagMeasures/RowLatticeTermAdaptedNormalForm.lean | ecab0101410bae5be0036171c941da68557a3f13 | admission (149–362), term application (372–427) |
| Proofs/FlagMeasures/EquivFramesSameSecondLatticeFiberProof.lean | 3c5f4e4d39a3e516ccb37a174a910e9e8462df92 | same row and decomposition (149–246) |
| Proofs/FlagMeasures/FrameClassTermCountLeCardAut.lean | ec6542e179fc496b3de4a0689f9ca8ee8a0b3832 | actual reciprocal multiplicity (18–179) |
| Proofs/FlagMeasures/TermDeterminedByFrameClassAndIsometry.lean | 38d78bffacf4b17ffbe6657ee4f3f9cd1d0199fd | term uniqueness (51–152,207–287) |
| Proofs/FlagMeasures/TripOfTerms.lean | 92f22d33c6d9b8b803d20903f9a975fd105c1abc | congruence to Trip (147 onward) |
| Proofs/FlagMeasures/IsHermIsometryGraphModScalarFlagPairIota.lean | a825316b765edd70e3b6f8570da4df049f727338 | graph totality via projective extension (236–303) |
| Proofs/FlagMeasures/FlagFrameVectorMemCommonSubspace.lean | a1106b743c65343bd0da860a51ccad536554ddf0 | transport and weighted sum |
| Proofs/FlagMeasures/EqCHolds.lean | edb0f4813ff7fd1acc05353d56a9d7e0ba1badfe | equality of double cosets |

Source read is not Lean execution. No manuscript compilation, full W08 closure, or whole-map-node change is asserted.
