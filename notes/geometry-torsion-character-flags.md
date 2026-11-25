# Short finite-flat proof of the torsion-character flag supplier

[Proof in both manuscripts](../paper/shared/geometry-torsion-character-flags.tex).

This is a further reduction of the actual W10 TestFacts, using the original split-point coordinates, not an adapted generic flag.

- The annihilator inclusion w R^n <= A_tau follows for every finite flat F_q-module order, by extension of the generic additive characters via Cartier duality and the truncated logarithm modulo p.
- The discriminant/colength identity 2 lambda(P)=|P(C)| deg omega_P holds without tightness for each actual split-coordinate subgroup and quotient. Proof: Raynaud's F-line presentation, exact cotangent sequences and trace-discriminant transitivity for a finite flat torsor. It does not rely on a dimension comparison of almost modules.
- Under the literal source chart pins (Base.th and the square-ideal/equivariance/kernel pins), the two step-graph identities in RC2 follow from exact cotangent sequences. In the original coefficients omega_(Q_i,tau)=I_(tau,i)/I_(phi^-1 tau,i)^p. Hence the original second projection of B is K_i, and its first-coordinate-only kernel at phi tau is I_(tau,i)^p. No numerical length-equality hypothesis or whole FlagConcl is needed for these two identities.
- The remaining RC2 equality D_tau,i=I_tau,i follows from quotient generation by functions additive modulo p (GenAF). The proof first propagates the generator ideals along the Frobenius orbit, then uses a single monomial evaluation determinant to force all coordinate inclusions to be equalities. No separate full-order IsTight premise is needed. The same determinant shows that the original additive-coefficient degree equality on each quotient order is sufficient for GenAF.
- This completes the local algebra *given the stated geometric pins and generation*. RC1 (the Hodge image/kernel identities), realization of the chart order/pins and quotient generation on the original induced orders are not declared proved. The linked global tower, weighted mean and rank losses remain.

## Sources and scope

Classical inputs: the finite locally free subgroup quotient theorem, SGA 3 Exp. III 4.15 (finite locally free group schemes are lci; see also Messing, *The Crystals Associated to Barsotti-Tate Groups*, II.3.2.6), cotangent-complex transitivity and flat base change, and Raynaud, [*Schémas en groupes de type (p,...,p)*, Bull. SMF 102 (1974), 241–280](https://www.numdam.org/articles/10.24033/bsmf.1779/), Cor. 1.5.1. The last applies over the local valuation ring with the required Teichmüller roots; the augmentation eigenspaces are free lines. We explicitly prove the generic-character and determinant calculations, and derive the exact cotangent sequence using generic étaleness and torsion freeness, rather than claiming arbitrary cotangent sequences are left exact.

Source: jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de, prefix lean/src/Development/AutomorphicSpectrum/:
- Definitions/CommutativeAlgebra/LieLatticeData.lean: Base.th, af, dId, xId, kk, stepGraph, Facts.
- Definitions/CommutativeAlgebra/StepOrderRes.lean: stepOrder, stepOrderRes, idealX, idealD, afLatT.
- Statements/AlgebraStatements/PolarisedFlagStatement.lean: FlagConcl, FlagStatement (the explicit GenAF and IsTight premises).
- Proofs/GeometryProofs/OrdinaryCurveHodgePrime.lean: testFacts, hFlag, hTh', hleaf, hseq', and the final three coordinate comparisons.
- Proofs/GeometryProofs/ChartDThSqIdealMemAndSmulMemAndEigMemSqIdeal.lean: exactly the three chart pins.
- Proofs/AlgebraProofs/HodgeKernelImageLattice.lean: pt_seq_lin, reduction of RC1 to actual Hodge image/preimage.
- Proofs/AlgebraProofs/PtAfTypeMain.lean: actual affine-coordinate comparison at a retract.
- Proofs/AlgebraProofs/FlagComparisonTheorem.lean and StableHopfOrderSubgroupGeneration.lean: original product-inequality and generation route.

The alternative does not infer GenAF from the mere existence of a finite flat Hopf order. Nor does it identify a source chart graph with an arbitrary isomorphic finite torsion module. The exact chart pins are indispensable in the stated graph argument. The source test-point theorem uses additional ordinary-curve and Hodge–Tate hypotheses to prove the remaining geometric inputs. This is a written proof with classical citations, no Lean replay or full manuscript build.
