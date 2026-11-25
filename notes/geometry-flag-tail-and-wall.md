# W10: alternating Frobenius tails and finite wall/rank interfaces

The new [alternant proof](../paper/shared/geometry-flag-tail-alternants.tex) supplies both **uniform numerical Frobenius-tail estimates** for the original tower remainder. A single exterior-power shift commutator extracts the correct power-sum coefficient independently of its decomposition. Bumped Vandermonde determinants reduce to hook Schur polynomials, with exact factorial factors. A confluent divided difference (residue) handles the singular Grassmannian test directly.

* Regular weights: the normalized remainder is at most q W(u), improving the former 2 q W(u). This retains the actual floor-cutoff convention and the small-block separation hypothesis.
* Grassmannian test: the normalized remainder is at most 728. This is weaker than the source's sharper 8/(5 f q) but is absolute and sufficient; it requires no additional geometric hypothesis. It avoids the original singular-test polynomial recursion.
* Substituting the previously proved signed base-test lower bound, the resulting **conditional** weighted intersection lower bound is -236 Lambda_B L(u)-q W(u); with the original norm-count/volume bridge and its allowance it gives -316 Lambda_B L(u)-q W(u). The earlier constant 135 remains available if the sharper source test remainder is supplied.

The [finite wall and rank proof](../paper/shared/geometry-flag-finite-wall.tex) has two further consequences.

1. The exact cutoff identity follows from the actual Prop6 change, within-block antisymmetry, transitive label invariance, fixed flag-height wall vanishing and convergence at finitely many fixed rational weights on each cross wall. Subtract the exact absolutely convergent tail and take the quotient by the two shift functionals: the quotient is constant across cutoffs. Its limit is zero by the Vandermonde divisibility argument. Thus the quantitative uniform wall approximation and its interpolation constants are unnecessary for this exact comparison. Actual wall limits and symmetry still require geometric verification.
2. A finite sufficient lower image-degree certificate consists of the vanishing of the weight-difference section on the prime divisors of the normalized base-ideal blow-up, with multiplicities at least a times the base divisor. Once supplied, nef intersection positivity proves the required lower bound (FW1), with no Hilbert--Samuel threshold. The precise product (FW2) retains all cross gaps in the weight-shift loss. Inserting it into the established jet estimate gives a finite rank inequality. This does not yet construct the section satisfying the divisor certificate. It is a reduction of the source ValMult route, not an assertion that ordinary boundary support suffices.

## Actual source correspondence

Pinned revision jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.

- Development/WeilBound/CoreStatements/FlagImmersions/AltCMul.lean, AltEqZero.lean, SumChooseLe.lean and RestDegreePowerBound.lean: alternate extraction and regular tail supplier.
- Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/LieTermFlagBound.lean, LinRootRemainderBound.lean and TestPolynomialRemainderBound.lean: original consumers for regular and singular tests.
- Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/HeckeSectionsIsotropicCommutatorPairingPower.lean: restTerm, restSum, IsDecomp, muSmall, fibClass, testPoly, IdentAt, ThmW, ThmBA.
- Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/Proportional.lean: I8, Prop6, PropA, PropF, I9.
- Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/PowerSumDeltaDecomposition.lean and TowerIdentityAtCutoff.lean: exact shift coefficients and original passage from large cutoffs.
- Development/AbelianVarietyTheory/Definitions/Divisors/GenRatios.lean: actual ValMult and ValBound.
- Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ValuationMultiplicityOfConsecutiveRun.lean: original weight-difference section and valuation supplier. Its missing actual exceptional-divisor vanishing cannot be inferred from the numerical jet estimate.

## Verification and limits

The accompanying script checks 4,900 finite exterior shift identities, 2,600 hook-content identities and ratio bounds, 20 exact confluent-residue examples, and rational constants. It was executed with Python/SymPy 1.14.0. These diagnostics are not a proof of the general statements; the ordinary proofs are in the two shared sections.

The new estimates and exact-cutoff reduction do not establish the missing global flag-height symmetry and wall limits, the complete norm-count-volume comparison, the actual image-degree certificate, or the moving arithmetic family. W06 common realization and W08 off-diagonal global scalar counting remain open. No whole node is claimed closed. No independent proof review or full manuscript build has been completed in this pass.
