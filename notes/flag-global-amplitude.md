# Original amplitude and global zero-Gram pair sum

**Classification:** the normalization and amplitude consumer, and the
global weighted pair summation under the matched original local-data
hypothesis, are supplied. [Proof](../paper/shared/flag-global-amplitude.tex).

The original global normalization is not estimated by a new Haar
constant. With the local squared masses \(L_\tau\), compact dimensions
\(d_\tau\), \(c_\tau=L_\tau/d_\tau\), and the actual product-coordinate
unipotent covolume \(V_N\), the literal identity is
\[
(\mathrm{scl}\,\mathrm{vol}(K_2))V_N\prod_\tau c_\tau=1.
\]
This proves ConstC. Product Weil disintegration and the actual
arithmetic stabilizer covolume give FactC. The reference theorem
then cancels the large power of the root discriminant in the product
of the local orbital bounds. The infimum over the same adapted forms
gives the original weight, and the original k2a estimate follows.
This is the AmpAt consumer of LocDatC and the proved tail bound;
the existence of the matched local datum from the standing hypotheses
is kept explicit.

For j=0 the primitive last-vector quotient implies that the common
scalar is an algebraic unit, of norm one at all complex places.
It is a root of unity; the two actual distinct level primes force it
to be one. The admitted integral frame mover makes the term an
identity term. This proves JPosC.

With Cs=20, Cp=16, the product of the amplitude and fixed-label
pair factors has residual power S^(-4k). The remaining minor power
costs only S^(j+1); the distinct-label sum absorbs the residual.
The original size relation Cl*m^6*log(b)<=k*log(k) gives
\[
 \sum_{\mathrm{allPairs}(\mathrm{degSet})}a_ta_{t'}
 \le d_\pi\,\mathrm{massRows}\,e^{-3kf\log k/2}.
\]
All finite sums use the actual compatible row pairs; the result includes
summability. Irrelevance is treated by character cancellation on the
compact stabilizer quotient.

The source's final bound is with the **full column dimension** duC,
not merely the compact dimension dpiC. Its remaining finite interfaces
are the original Levi Gram comparison and
Gam1*massRows*dpiC<=duC. We do not claim KppDiag or the full W08
node until these and the local-data existence are verified.

## Pinned source audit

Revision jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.
Paths are under lean/src/.

| File | Blob | Interface |
|---|---|---|
| Development/AbelianVarietyTheory/Definitions/SemilocalFrames/ConstC.lean | 2285e3b54f064643dd1fb7f2dc9c8d162c733f48 | PullC, TensC, ConstC, FactC |
| Development/AbelianVarietyTheory/Proofs/FlagMeasures/NormalisingConstantsProductHypProof.lean | 1099ac34eeff53ebd2a2047986b5fccfe233e130 | exact product normalization |
| Development/AbelianVarietyTheory/Proofs/FlagMeasures/TermAmplitudeLeCovolumeLocalAmplitudes.lean | 40938a0f5b4f591f801694e644dd6ad21a9b4321 | original FactC |
| Development/AbelianVarietyTheory/Proofs/FlagMeasures/AmplitudeBoundAtTermsOfLocalData.lean | 3836a7bc80d1d9057a2fdde9f2bbe118186ff6df | actual AmpP implication, lines 113–228 |
| Development/AbelianVarietyTheory/Definitions/SemilocalFrames/GoodLoc.lean | 9fbf6f6175adb970c246e05c2a0615bb79b03953 | exact retained local-data hypothesis |
| Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/IsIdentityOfEqualFlags.lean | a3cae13d6e5637d05056bb4599b532f4933da8ad | JPosC |
| Formalism/SharpRestriction/CuspSpanNormBounds/KappaEndpoints.lean | f41d3d7dace19d5a35c6fff40b0cdf82ad50b237 | original k2a, k2e, normalized minors and labels |
| Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/PairsAmplitudeBoundOfTypeBound.lean | 2d8dad2667793eb35d567e5e3a8ffb993af6a149 | full finite-subset summation |
| Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RowsOther.lean | aaf5c0210f26d701b19d98ccd15c7b8b7cf6c212 | PairsDegAmp and KppDiag |
| Development/AbelianVarietyTheory/Definitions/LatticeFrames/VanishingGramTermsBoundParams.lean | fe800c98e18b014589a9ead9a8fec8701acf7c78 | full column dimension in final bound |

The estimates and quantifier order are checked algebraically. No
Lean replay or final manuscript compilation is claimed.
