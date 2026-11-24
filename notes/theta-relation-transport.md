# Relation transport for the actual theta-period comparison

The [shared proof](../paper/shared/theta-relation-transport.tex) reconstructs the finite-test coefficient convolution, the downward see-saw relation induction, the bottom scalar choice, the nonzero-anchor argument, and arithmetic descent of the row corrections. It is conditional on the actual common family and its analytic unfolding/realization inputs, not closure of W06.

The key distinction from literal normalized-map equality is that the original source has two different products of complex scalars. Write A_j=cV_j cK_j cK_(j+1), B_j=cI_j cI_(j+1); C_t is the even-step product of A_j times cP, and D_t the full product of cI. The upward relation weighted by C_t descends to the bottom relation weighted by D_t. In the common real double test, the finite coefficients are a single convolution a(y')=sum_{nu,z} a_nu(z)b_{nu,z}(y'), independent of row tuple. This is where the common real action matters; using a different test family for each row would not transfer a relation. The last step includes cP. The proof retains the actual local support, absolute convergence, rapid decay and density assumptions of the unfolding.

The bottom relation uses the inverse column similarity U and c_t=C_t s/D_t. A nonzero Poincare witness b0 forces the corresponding scalar p(phi0) to be nonzero. Anchoring gives c_t perCol b0=p(phi0)b. The source then normalizes by the base tuple and the original norm dictionary, retaining a nonzero analytic scalar for each word.

There is no need to adjoin an arbitrary complex row ratio to K. The algebraic base pairing identity shows that if a normalized ratio z_t is not in the image of K, the entire algebraic period at that tuple is zero; one can use correction 1 there. Otherwise its unique preimage is used. The source's UnitRatio says z_t^b is a nonzero rational number supported on the auxiliary primes of that tuple, and ServedQ excludes the served coefficient prime. Thus its preimage has exactly zero valuation at that prime. No global unit or general absolute-height claim is made. The corrected base pairing factors through the original rational row quotient and the original isometries, with the nonzero analytic scalar retained as in L1e.

Remaining: construct the actual common family LawsX/FamAllQ and its local support, real test and unfolding suppliers from TC/ColIn, in particular the actual row lift, onto and commutation clauses, RatioQ. ServedQ is now proved from the original twisting data: the reference tuple has no ramified auxiliary prime; at a twisting place of residue characteristic p, both the selected auxiliary character and the twisting character are unramified above p. Apply the nonzero-anchor argument only when the original Poincare witness is obtained. This does not close the global normalized-operator comparison.

The served-prime proof is included in the [shared manuscript](../paper/shared/theta-relation-transport.tex), paragraph `par:theta-served-prime`. The pinned proof interfaces are `Definitions/LatticeFrames/RatioOKOfRootOfUnity.lean` (95791e4f36883bb1c609c355c1da1ac55aed4285), lines 66–109, and `Proofs/DecoratedLatticeProofs/ServedQOfBot.lean` (02ebc682b0036d46a5d633488db18b2c95f2fb2b), lines 17–19. No global analytic family is inferred.

## Source audit

All paths below under lean/src at jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.

- Development/AbelianVarietyTheory/Definitions/LatticeFrames/ValLastX.lean (242b8c628d536957e2bfb902e11ec23bf1d1cf6a): original LawsX, StepX, LastX, MainX, scalar products.
- Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawDoubleLiftCombinationOfLaws.lean (1517ba1a156f2f2cbeb2511e2b9fc20d4c8a7d7c): two finite coefficient families and common Fock test.
- Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawDoubleStepLinearRelationsPeriods.lean (5b611d478b863543d639689d34879923013cab44): double-step test relation.
- Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawLastTwoStepsTransportLinearRelations.lean (0517d26c1442c584b34ee5231da55ac7eac36803): terminal coefficient and test.
- Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/MainXOfStepXLastX.lean (7ec466804ad1a4771805022424cefd2fd58de0b1): exact products.
- Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/RelOfLinks.lean (546a6dc0cafad41db9c88130db105241a824fd02): bottom relation and cTop/cBot, inverse similarity.
- Development/AbelianVarietyTheory/Definitions/LatticeFrames/FamAllQ.lean (9c1df5cc36db3e77454eae9856e6cee328ad0e8b): RatioQ, ServedQ and actual family inputs.
- Development/AbelianVarietyTheory/Definitions/LatticeFrames/UnitRatio.lean: root of rational S-unit definition.
- Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/JointStarProductNonvanishing.lean (dcbc285e466da1cb216920e22124514f2a8f05d3): anchored bottom relation.
- Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/MiStar2OfAnchored.lean (e7842b47c630ce3c2d8f119df09b065a65abaa20): normalization at the base tuple.
- Formalism/LocalToGlobal/IndefiniteReal/IsometricPeriodsOfUnitHypotheses.lean (e36d152ff6cfd309344c6e915b91ca1ce87dd8c8): zetaOf, MatrixIdentityOffBase, ZetaOK and L1e.

These are conventional proof/interface checks, not execution of the Lean development. The analytic family inputs remain explicit.
