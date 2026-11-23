# Complete pinned Lean source atlas

This view covers every local Lean source file at the pinned source revision. It is separate from the manuscript section atlas and the mathematical proof program.

## Coverage of the recorded full-source scan

- **175,187 local Lean files**, all matched byte-for-byte to their pinned Git blob hashes.
- **753,261 distinct local import edges**; the graph is acyclic.
- **175,187 modules reachable from Main**; maximum import depth, including Main, is **203**.
- **348 distinct external imports** are explicit boundary nodes. Their package internals are not included in this local inventory.

All-source import reachability does not establish that every declaration is needed by the five target proofs. Imported modules can contain unused results. This scan is not a Lean build or a kernel replay.

## Every top-level source family

| Source family | Files |
| --- | ---: |
| BuildAid | 5 |
| CompanionTheory | 2,027 |
| Development | 141,928 |
| Formalism | 18,254 |
| GroundTheory | 8,507 |
| Lemmata | 167 |
| Main | 1 |
| PositivityTheory | 449 |
| ReciprocityTheory | 3,845 |
| Statements | 1 |
| Supplements | 3 |

The large source families include abelian-variety theory, automorphic spectrum, Galois and local-global theory, theta integrals, and geometric covolume estimates. They cannot be represented faithfully by treating the recovered 96 sections as the entire source proof.

## Durable complete graph

The [compressed source graph](lean-source-imports.json.gz) contains every source module, pinned Git blob hash, byte/line counts, and local or external import endpoint. Its compact row schema is documented inside the file. The [inventory certificate](../certificates/lean-source-inventory.json) records the root tree, aggregate source digest, all subject groups and grouped import counts.

Query one module without loading a source file into the conversation:

```sh
python scripts/scan_lean_backbone.py --module Main
python scripts/source_excerpt.py --atlas --source Main --search theorem --offline
```

To reproduce the full inventory, make the pinned source checkout available locally and run:

```sh
python scripts/scan_lean_backbone.py --mirror build/lean-mirror
```

The scanner reads and verifies the large artifact locally and prints only aggregate counts. It refuses unclassified imports or unsupported import headers.

## Current exact heat interface

The [harmonic heat proof](../notes/theta-spanning-continuation-heat.md) and
[bounded-source certificate](../certificates/theta-spanning-continuation-heat.json)
authenticate the original heat equations, doubled coordinates and
`KernelIdentity` consumer at the pinned revision. The mathematical proof
retains the invariant contracted jets, not all Jacobi derivatives.
No Lean build or uniform arithmetic norm estimate is asserted.

## Mathematical backbone and remaining interpretation

The [endpoint backbone](../notes/lean-endpoint-backbone.md) traces the final sufficient interfaces and the one coherent construction they require. The [global input review](../notes/lean-global-inputs.md) unfolds the Galois compatibility, stable theta lift, theta-integral matching and geometric covolume contracts. These are mathematical interpretation checkpoints, not a claim that every source lemma has been independently verified.

The [classical Galois substitution](../notes/classical-galois-substitution.md)
now replaces the source's Galois-construction supplier in the preferred proof
program. The atlas still describes the complete original source. No number
of eliminated files is inferred from this substitution: an imported file
can contain arguments used in several surviving branches.

The [full proof program](full-proof-program.md) covers these branches and records
the acceptance conditions for each proposed replacement. The
[source subject diagram](source-subject-atlas.svg) accounts for the entire
local tree; the [complete subject table](source-subjects.md) lists all 343
two-component groups. The complete import graph remains available when a
dependency must be traced beyond the current mathematical boundary.

## Bounded source comparisons in the current continuation

The complete import inventory above is preserved evidence from its recorded
scan. This continuation authenticated only the selected source files used
below; it did not download or rebuild the entire development.

| Mathematical supplier | Bounded source comparison and evidence |
| --- | --- |
| Exact auxiliary-prime iteration | [Chain note](../notes/level-chain-integrality.md) and [source certificate](../certificates/level-chain-integrality.json): original rational-image lattice, local kernel laws and triangular commutation factors. |
| Finite upper section rank | [Jet theorem](../notes/finite-section-jet-bound.md) and [source certificate](../certificates/finite-section-jet-bound.json): component geometry, nef weight differences and exact binomial rank shares. |
| Selmer point and tangent comparison | [Completed comparison](../notes/selmer-tangent-comparison.md) and [independent review](../certificates/selmer-tangent-comparison-review.json): the permitted grading rescaling, actual framed universal property and marked coboundaries. |
| Crystalline local tangent condition | [Component comparison](../notes/selmer-crystalline-component-comparison.md) and [certificate](../certificates/selmer-crystalline-component-comparison.json): the original ordinary equations, fixed local subgroup, saturated radical and exact adjoint coefficient module; Kisin's finite-algebra theorem supplies the infinitesimal comparison. |
| Sharp source trace loss | [Return theorem](../notes/dominant-return-deficit.md) and [certificate](../certificates/dominant-return-deficit.json): the original seed evaluations, rational returns and normalizers. |
| Average cusp correction | [Counting theorem](../notes/cusp-counting-mean.md) and [certificate](../certificates/cusp-counting-mean.json): the original Hodge norm, integral rational spanning, probability measure, count homogeneity and signed metric comparison. |
| Full arithmetic isotropic count | [First-moment theorem](../notes/geometry-arithmetic-frontier-isotropic-integrability.md) and [certificate](../certificates/geometry-arithmetic-frontier-isotropic-integrability.json): five pinned modules identify the actual lattice stabilizer, full count and averaging consumer; classical finite covolume and rational-line finiteness reduce the unrestricted count to a convergent ideal sum. |
| Original geometric mean and Haar measure | [Curvature proof](../notes/geometry-arithmetic-frontier-curvature-haar-mean.md) and [certificate](../certificates/geometry-arithmetic-frontier-curvature-haar-mean.json): thirteen pinned modules identify the original quotient Hodge metric, interior Hessian density, finite sheets and denominator, retaining exact sheet and component weights. |
| Integral Selmer special fibre | [Frontier checkpoint](../notes/selmer-integral-frontier-special-fibre.md) and [certificate](../certificates/selmer-integral-frontier-special-fibre.json): the full normalized deformation ring, equal-characteristic curve criterion and actual rank-three propagation consumer; no replacement by a torsion-free quotient. |
| Reducible local prime inclusion | [Incidence proof](../notes/selmer-integral-frontier-incidence.md) and [certificate](../certificates/selmer-integral-frontier-incidence.json): the exact determinant locus and its complete-local deformation-presentation consumer, retaining independent cotangent coordinates and the actual module dimension. |
| Selmer presentation and auxiliary count | [Coordinate and resultant proofs](../notes/selmer-integral-frontier-padded-relations.md) and [certificate](../certificates/selmer-integral-frontier-padded-relations.json): nineteen pinned files retain the actual index-two descent, original cohomological quantifiers and uniform local constant. |
| Full type-prime mixed jets | [Local theta proof](../notes/theta-integral-frontier-type-prime-jets.md) and [certificate](../certificates/theta-integral-frontier-type-prime-jets.json): the complete indicator denominator, exact differential frame, both split branches and original unit-ideal consumer. |
| Limits of finite support | [Return-support checkpoint](../notes/dominant-return-nonvanishing-frontier.md) and [certificate](../certificates/dominant-return-nonvanishing-frontier.json): infinitely many congruent rational returns in the isotropic case, with qualitative decay distinguished from a relative tail estimate. |
| Quantitative projector tail | [Kernel checkpoint](../notes/projector-kernel-tail.md) and [certificate](../certificates/projector-kernel-tail.json): the normalized exponential far-return estimate, admissible cutoff, and missing period-Gram transfer; the cusp logarithmic mean does not supply the higher inverse moment in its current majorant. |
| All modular Selmer solutions | [Complete equations and detection](../notes/selmer-integral-frontier-dual-detection.md) and [certificate](../certificates/selmer-integral-frontier-dual-detection.json): fourteen pinned modules identify complete function lifts, residual finiteness, integral paired detection and the exact uniform counting quantifiers. |
| Signed analytic boundary energy | [Finite-energy proof](../notes/geometry-arithmetic-frontier-signed-boundary-energy.md) and [independent review](../certificates/geometry-arithmetic-frontier-signed-boundary-energy-review.json): ten pinned modules retain the actual regularization hypotheses and the remaining arithmetic interfaces. |
| Original bounded cusp regularization | [Exact convergence](../notes/geometry-arithmetic-frontier-bounded-cusp-energy.md) and [review](../certificates/geometry-arithmetic-frontier-bounded-cusp-energy-review.json): eleven pinned modules identify the actual circle-invariant kernel, inner charts, overlap, gluing and near-positivity. |
| Exact arithmetic metric variation | [Variation and locality](../notes/geometry-arithmetic-frontier-exact-metric-variation.md) and [review](../certificates/geometry-arithmetic-frontier-exact-metric-variation-review.json): fourteen pinned modules preserve recursion sign, mixed density, original vertical factors and rational normalization. |
| Odd paired determinant detection | [Block proof](../notes/selmer-integral-frontier-odd-detection.md) and [review](../certificates/selmer-integral-frontier-odd-detection-review.json): ten pinned modules match the actual paired trace, relation pairing, polarization and positive-characteristic frame. |
| Even completion of paired detection | [Complete fraction-field proof](../notes/selmer-integral-frontier-even-detection.md) and [review](../certificates/selmer-integral-frontier-even-detection-review.json): five pinned modules retain the commutator subgroup, trace correction, characteristic restriction and separate integral assembly. |
| Original integral paired detection | [Integral theorem](../notes/selmer-integral-frontier-integral-detection.md) and [review](../certificates/selmer-integral-frontier-integral-detection-review.json): exact integral direct-sum coordinates, common denominators and the unchanged cyclotomic kernel. |
| Complete simultaneous auxiliary choice | [Finite selection](../notes/selmer-integral-frontier-finite-selection.md) and [ramified extension](../notes/selmer-integral-frontier-coefficient-extension.md): the exact open-subgroup finiteness definition, odd-family construction, integral common kernel, local witnesses, spectral splitting and equal residue-field cardinalities. |
| Original compact-model signed comparison | [Model and Stokes theorem](../notes/geometry-arithmetic-frontier-compact-model-stokes.md) and [certificate](../certificates/geometry-arithmetic-frontier-compact-model-stokes.json): original sheet integrals, vertical unit equations, fixed positive twists and signed boundary target. |
| Signed local-density refinement | [Local estimate](../notes/global-norm-frontier-primitive-density.md) and [certificate](../certificates/global-norm-frontier-primitive-density.json): exact primitive cutoff, modified split tuple and rank parity. The full primitive count was already proved in the local-density chapter. |
| Ordinary local Selmer count | [Local arithmetic theorem](../notes/selmer-integral-frontier-ordinary-local-count.md) and [certificate](../certificates/selmer-integral-frontier-ordinary-local-count.json): exact finite Tate/Euler pairing, original primal coefficient module, local torsion condition and one constant for every truncation and auxiliary level. |
| Original scalar-pair density equality | [Complementary-lattice theorem](../notes/global-norm-frontier-scalar-density.md) and [certificate](../certificates/global-norm-frontier-scalar-density.json): original first-r quotient flags, full modified frame lattices, designated split-level graph and discriminant modules over the maximal algebra. |

These are conventional mathematical substitutions with explicit hypotheses.
They do not identify an exact number of unnecessary Lean files or constitute
a new kernel verification.

The [limiting Selmer contract](../notes/selmer-integral-frontier-limit-comparison.md) authenticates the original `Lim`, finite Selmer quotient comparison, `CohLim` and Laurent conversions. Its [certificate](../certificates/selmer-integral-frontier-limit-comparison.json) records 23 pinned modules and bounded ranges; the common arithmetic tower and patched support remain separate constructions.

The full-primary theta trace checkpoint authenticates fourteen bounded
source modules in `certificates/geometry-arithmetic-frontier-primary-trace.json`.
It records the unramified host, actual adapted matrices, finite-height and
rational-torsion splitting, full product-section invariance, exact Tate
rank and local index, and original normalized chain rule. The reached
section and mixed level-torsion suppliers remain separately identified.

The generic PEL comparison authenticates the original host, primitive
line, complete finite-level labels and distinct `Moduli`/`Model` interfaces
in `geometry-arithmetic-frontier-generic-pel.json`, together with the exact
Lan reference revision. The reached-section regularity certificate records
twenty bounded modules for the actual quadratic coefficient filtration,
canonical theta translations, scalar-one pullback and integral Fourier
saturation. Both packages have independent review certificates.

The ordinary automorphic module certificate authenticates twenty-five
bounded modules for the fixed tame level, original unnormalized ordinary
operator, integral sections, exact residue diamond quotient and commuting
Hecke family. The Jacquet transfer certificate authenticates eighteen
modules for the mixed period norm, signed exterior decomposition, full
Harish-Chandra reserve and both original character-scale branches. Neither
certificate asserts a full automorphic determinant/support construction,
a global period-Gram identification or a Lean build.

The classical specialization certificate authenticates thirteen original
weight, ordinary-module and specialization interfaces, preserving the
principal cyclotomic shift and the actual weight-zero consumer. The mixed
level certificate authenticates twelve interfaces for ordered theta
translations, normalized pullback, arbitrary level-prime powers, the exact
cover value and the one-clearing-integer denominator. Both have independent
mathematical reviews; their finite controls are not Lean builds.

The integral PEL supplier compares five original level, Model and stronger
uniformization interfaces with three exact Lan reference revisions. It
constructs the individual Model; it does not mark the stronger contracts
complete. The local representation/period supplier authenticates fifteen
original interfaces and four primary references, including the exact
numerical-family domain and zero-base period comparison. The classical
representation and amenable-positivity arguments now supply the actual
local leading-minor estimate. Full global return estimates remain open.

The exact `OnePlaceEstimates` iteration and coefficient-expansion contracts
are now supplied by the common iterated-minor and big-cell continuity
proofs. The latter uses the original `Hpk`, `Nset`, `bigCell` and smooth
section, without internal middle-block pivots or replacement of specified
points by almost-everywhere representatives. `TBB.KernelFourierIntegralBound`
and the global return assembly remain open. Source hashes and bounded
excerpts are in `global-norm-frontier-iterated-minors` and
`global-norm-frontier-big-cell-continuity` certificates.

## Newly verified actual suppliers

- [DVR uniformization](../notes/geometry-arithmetic-frontier-dvr-uniformization.md),
  [integral theta](../notes/geometry-arithmetic-frontier-integral-theta.md), and
  [level symmetries](../notes/geometry-arithmetic-frontier-level-symmetry.md): the exact
  original `PELUnif`, `TorsionIso`, `PushInvertible`, `SplitFibres`, `Model.N3` and
  `LevelStructureConditions`, including nondiscrete valuation rings. Their
  certificates authenticate bounded source interfaces and primary references.
- [Hecke determinant](../notes/selmer-integral-frontier-hecke-determinant.md) and
  [integral types](../notes/selmer-integral-frontier-type-construction.md): the original
  ordered ordinary relations, actual finite Hecke algebra, all classical isobaric
  blocks, exact compact-type covariance and arbitrary-conductor inertia.
- [Rank-zero pointwise bound](../notes/global-norm-frontier-rank-zero-pointwise.md):
  original `RootMeasBig`, quotient measure, full `orbSq` supremum and
  `TheoremBPrimePointwise` at r=0, with exact density and parameter losses.

No Lean build or completion of the larger proof-map nodes is claimed.

The [global model certificate](../certificates/geometry-arithmetic-frontier-global-model.json)
authenticates `Model`, `Descends`, `Dominates` and the entire original `N6`
valuation quantifier. The [independent review](../certificates/geometry-arithmetic-frontier-global-model-review.json)
checks the arithmetic outside-finitely-many-primes agreement, effective
scheme descent, and exact source comparison maps.

The [wave-isometry certificate](../certificates/global-norm-frontier-wave-isometry.json)
records the exact `waveG`, `uInv`, `VIso`, `VIsoCpt` and tail-first
residue recursion. The [review](../certificates/global-norm-frontier-wave-isometry-review.json)
checks all signed tensor factors, actual integrating stabilizers, gauge
and common Haar constant. The all-word equality is proved by induction;
finite exact tests serve as independent checks of signs and order.

The [level-system certificate](../certificates/geometry-arithmetic-frontier-level-system.json)
authenticates the original `N0`, `IsTransition`, `N2` and
`SiegelCompare` clauses, including the essential `Level.fromK`
restriction. Its [independent review](../certificates/geometry-arithmetic-frontier-level-system-review.json)
checks the fixed cones, original coefficient rings, simultaneous inert
prime and exact intermediate model. No arbitrary half-ideal is
substituted for the prescribed one.

The [Taylor--Wiles certificate](../certificates/selmer-integral-frontier-taylor-wiles.json)
authenticates the full `TWBase`, `TWRing`, `TWMaps` and `TWAut`
contracts and their actual arithmetic realization. Its
[independent review](../certificates/selmer-integral-frontier-taylor-wiles-review.json)
checks the integral trace/dual-tensor maps, exact original multiplier,
residual block, weight coordinates and uniform n! relation exponent.
Source authentication and finite symbolic checks are distinguished from
the general mathematical argument.

The [formal-arc certificate](../certificates/geometry-arithmetic-frontier-formal-arcs.json)
authenticates `ArcIn`, `HasArcData`, `N4`, the exact all-power
expansion and torsion contracts, and the original `PartI` conjunction.
Its [independent review](../certificates/geometry-arithmetic-frontier-formal-arcs-review.json)
checks all of the uniqueness and specialization quantifiers, including
the unconstrained values outside the selected half-label submodule and
the actual two-dimensional toroidal extension. `PartI` is now supplied;
the larger quantitative W10 obligation remains open.

The [mixed determinant certificate](../certificates/global-norm-frontier-mixed-cauchy.json)
authenticates the exact `SizeStd`, `SizeStdCpt`, `pairJ` and
signed determinant corrections. Its
[independent review](../certificates/global-norm-frontier-mixed-cauchy-review.json)
checks all-word order, invariant Jacquet domains and degenerate forms;
it also preserves a separate exact group-algebra order check. Finite
tests supplement the all-word proof and do not assert a global norm bound.

The [polarized-model certificate](../certificates/selmer-integral-frontier-polarized-model.json)
authenticates the exact `URep`, `Hat.ker`, `OoPt.ker` and `chBar`
interfaces. Its [independent review](../certificates/selmer-integral-frontier-polarized-model-review.json)
checks the distinction between the relation generators, their original
closure, and the algebraic span after coefficient-curve completion.
The full determinant is verified by the primary cycle formula in arbitrary
odd residue characteristic. No radical or torsion is discarded.

The [partial-head certificate](../certificates/global-norm-frontier-partial-head-transfer.json)
and [independent review](../certificates/global-norm-frontier-partial-head-transfer-review.json)
verify the actual restricted-root quotient, Gram cutoff, undressed
operator recursion and arbitrary representative quantifier. They supply
`SliceCpt`, `HeadJ` and nonterminal `RadHead`, while retaining the separate
terminal orbital-density and top-lift obligations.

The [local propagation certificate](../certificates/selmer-integral-frontier-local-propagation.json)
and [independent review](../certificates/selmer-integral-frontier-local-propagation-review.json)
match the full `GalOut` quantifiers. They check the original finite-lattice
continuity, ordinary ordered product, paired second-order algebra and
actual integral presentation. The separate source finite-generation
field concerns the full group; profinite Schreier transfers it to the
open index-two equation group. Neither construction supplies a nonzero seed.

The [terminal-density certificate](../certificates/global-norm-frontier-terminal-density.json)
and [independent review](../certificates/global-norm-frontier-terminal-density-review.json)
match the original complex `KloostDens`, all block heads and the exact
source additive character. They verify the compact-support germ, its
Jacobian and stationary-phase coefficient against the primary theorem.
The result supplies exact density, not the stronger rank-uniform `GermRate`.

The [local-chart certificate](../certificates/geometry-arithmetic-frontier-good3.json)
and [independent review](../certificates/geometry-arithmetic-frontier-good3-review.json)
verify `IntegralChartA3`, `FrTrunc`, all four canonical-gauge identities
and the exact `Good3` supplier. The primary henselian, flat-section and
normal-base theorems are checked on the original models. Exact cocycle
and harmonic tests supplement the all-degree proof; no global field-size
or nonharmonic gauge-independence claim is made.

The [patched-support certificate](../certificates/selmer-integral-frontier-patched-support.json)
and [independent review](../certificates/selmer-integral-frontier-patched-support-review.json)
verify all `S5` fields and its original annihilation quantifiers. The
prequotient module is retained for the dimension proof; only its radical
support descends through the equation ideal. The arithmetic substitution
keeps all `n*q_TW` diamond directions. No nonzero seed is supplied by patching.

The [unitary-density certificate](../certificates/global-norm-frontier-unitary-density.json)
and [independent review](../certificates/global-norm-frontier-unitary-density-review.json)
verify the original `PhiZero` and `DensC` contracts, including every relevant
head and the zero convention for invalid heads. They authenticate the
cofactor frame, compact-factor cancellation and exact quotient measures.
Twenty exact frame diagnostics supplement the arbitrary-rank human proof;
no uniform analytic or global period estimate follows from density alone.

The [level-cover certificate](../certificates/geometry-arithmetic-frontier-level-cover.json)
and [independent review](../certificates/geometry-arithmetic-frontier-level-cover-review.json)
verify the universal coefficient-algebra quantifier of `IsNab`, reduced
test-ring descent and every original `DeltaDat.IsLev` field. Exact nilpotent
and nonflat diagnostics supplement the formal-geometric proof.

The [component-field certificate](../certificates/geometry-arithmetic-frontier-component-field.json)
and [independent review](../certificates/geometry-arithmetic-frontier-component-field-review.json)
authenticate the original everywhere-unramified host, component function
fields with flag variables and the exact sized-field consumer. Primary
Shimura, CM and class-field theorems are checked with their rational-class,
definite-signature and polarization hypotheses. Local congruence diagnostics
include the dyadic case and a ramified negative control.

The [terminal-transfer certificate](../certificates/global-norm-frontier-terminal-transfer.json)
and [independent review](../certificates/global-norm-frontier-terminal-transfer-review.json)
match the original `MkTopCut`, `MkTop` and `HeadTop` interfaces. They
retain `IsTopLift2`, `InDDplus2`, the exact radial gauge, actual signed
Capelli inverse and all terminal type weights. The support construction
uses no unproved uniform bound for its auxiliary cutoffs.

The [arithmetic-seed certificate](../certificates/selmer-integral-frontier-arithmetic-seed.json)
and [independent review](../certificates/selmer-integral-frontier-arithmetic-seed-review.json)
verify the literal `IsSeed` fields and the actual prime-to-ell `SeedPtOf`
input. Eight primary theorem interfaces retain every cusp, primitive
conductor, small-prime ordinary condition and base-change hypothesis.
The review corrects the rank-two half-norm normalization; exact ell=3
controls test both indispensable Eisenstein congruence hypotheses.

The [kernel-Fourier certificate](../certificates/global-norm-frontier-kernel-fourier.json)
and [independent review](../certificates/global-norm-frontier-kernel-fourier-review.json)
match `NP`, `Ew`, every-word `IsExt`, `KernelFourierIntegralBound`,
`HeadContinuityAtZero` and the full-index `PosAt`. Terminal nonpositive
Gram parameters are treated by the original zero convention. Exact
normalization and word-occupancy diagnostics supplement the analytic proof.

The [off-diagonal certificate](../certificates/global-norm-frontier-off-diagonal.json)
and [independent review](../certificates/global-norm-frontier-off-diagonal-review.json)
match the full original `LiftDegAll`, `DegLift` and
`KernelArgumentHypothesisScalar` contracts. The original right-character
differentials, ordered dual peeling, actual compact averaging and
Jacquet-form quotient are retained. Exact noncommutative PBW diagnostics
supplement the written induction, without asserting a Lean build.

The [normalized Member certificate](../certificates/geometry-arithmetic-frontier-member.json)
and [independent analytic review](../certificates/geometry-arithmetic-frontier-member-review.json)
authenticate 26 bounded source interfaces and the actual primitive line,
period coordinates, probability normalization, all six dictionary clauses
and exact lattice marking. Four cached primary references are rehashed;
Grauert's original base-change theorem and corrigendum are separately
recorded direct readings. The arithmetic and downstream audit is recorded
in the [root review](../certificates/geometry-arithmetic-frontier-member-arithmetic-review.json).
These establish the original sized good-cover supplier, not all W10.

The [CM twist certificate](../certificates/selmer-integral-frontier-cm-twist.json)
and [independent review](../certificates/selmer-integral-frontier-cm-twist-review.json)
authenticate the literal `IsTwist`, universal `Twist` and geometric-Artin
avatar interfaces. CHT Lemma 4.1.3 and Chebotarev are checked against
primary sources. Exact finite-group checks include all ramified quadratic
2-adic unit models, both exceptional root-of-unity fields, and a case
with ell dividing the class number; split/inert determinant signs are
checked independently. The human theorem supplies all original inputs.

The [arithmetic-point certificate](../certificates/selmer-integral-frontier-arithmetic-point.json)
and [independent review](../certificates/selmer-integral-frontier-arithmetic-point-review.json)
authenticate 21 exact source interfaces and four primary theorems.
The audit checks original-field Labesse descent, semisimplified local
compatibility without an extra regularity hypothesis, saturated integral
weights, completed-module evaluation and universal-point identification.
The exact `epsArt` and `UnifVal` contracts fix geometric reciprocity and
the retained factor `Norm(varpi)/q`. No characteristic-prime support or
uniform integral torsion conclusion is inferred from this theorem.

The [actual-denominator certificate](../certificates/geometry-arithmetic-frontier-actual-theta-denominator.json)
and [independent review](../certificates/geometry-arithmetic-frontier-actual-theta-denominator-review.json)
authenticate eleven bounded source interfaces. `ThClass` and `ThShort`
identify the literal raw sum, and the original final integral consumer
fixes every quantifier and scalar ideal. The review checks finite-field
torsion descent, unique translated sections and harmonic base change;
135 finite-index and 340 Fourier-indicator diagnostics accompany the
general proof. This applies existing estimates to the actual construction.

The [compact block-growth certificate](../certificates/global-norm-frontier-block-growth.json)
and [independent review](../certificates/global-norm-frontier-block-growth-review.json)
authenticate eighteen bounded source interfaces. The audit follows the
literal original block-growth contract, both normalizations, terminal
old-word density and every lattice sample. Exact diagnostics cover 303
lower weights, 177 terminal weights, 708 terminal word factors and twelve
free-block inverses. The source cutoff, punctured complex limsup and
positive residual Gram term remain; finite-decay extension is separate.

The [marked-propagation certificate](../certificates/selmer-integral-frontier-marked-propagation.json)
and [independent review](../certificates/selmer-integral-frontier-marked-propagation-review.json)
authenticate 41 bounded source interfaces and two primary determinant
theorems. The audit retains every Core/CoreBC/Raw quantifier, all six scalar
relation families, the original closed equation ideal, varying splitting
ranks and the same ultrafilter throughout. Free generator lifts avoid an
unavailable homomorphic lift; full polynomial laws avoid division by n!.
Exact coefficient, exponent and dimension checks supplement the human
proof. The starting stable prime remains a hypothesis.

The [finite-decay certificate](../certificates/global-norm-frontier-finite-decay.json)
and [independent review](../certificates/global-norm-frontier-finite-decay-review.json)
authenticate fifteen bounded source interfaces, including the literal
all-head `FormLimit` and finite-derivative allowance in `InDDPlus`.
The original normalized quotient cut proves noncompact orbital existence
before any limit identity is used. Exact coordinate diagnostics and eight
nonnegative-coefficient polynomial certificates check the all-parameter
exponent budgets. The original top-lift supplier remains a hypothesis.

The [arithmetic-propagation certificate](../certificates/selmer-integral-frontier-arithmetic-propagation.json)
and [independent review](../certificates/selmer-integral-frontier-arithmetic-propagation-review.json)
authenticate 31 bounded source interfaces and two primary references.
The audit checks the literal Point/Nice/IsPt/P1--P3 contracts, integral
normalization, full cyclotomic Chebotarev congruence and every ArSys/CohAx
field. Milne's real-place qualification makes degree-three cohomology
vanish at odd ell; the original cokernel contract uses modules killed
by ell. Exact valuation, unit-root and local-cocycle diagnostics accompany
the arbitrary-rank proof. No auxiliary-prime size or lattice-index bound
is inferred.

### Actual ordinary-family supplier

The [ordinary-family certificate](../certificates/selmer-integral-frontier-ordinary-families.json)
and [independent review](../certificates/selmer-integral-frontier-ordinary-families-review.json)
authenticate 20 bounded source interfaces and four primary references.
The audit checks full integral control, all fixed-weight and arithmetic-point
quantifiers, exact Speh normalization, the original `RingProps.unr0`,
finite twisting and the distinction between `ModU` and `ModUAlt`.
Exact integral-projector, adjoint and exponent diagnostics supplement
the human proof; no Lean build or final Selmer length bound is asserted.

### Actual terminal-degree supplier

The [terminal-degree certificate](../certificates/global-norm-frontier-terminal-degree.json)
authenticates 20 pinned modules for the exact PolyTop, RadAATop, TopFirst
and DegTop contracts. Its human proof preserves the actual unitary
character, ordered Capelli factors, radial gauge, terminal normalizer
and all grid/word quantifiers. Independent review and exact unitary,
PBW, Toda and grid diagnostics are recorded in the companion review.
These records do not assert a Lean build or global norm estimate.

### Actual controlled top lift

The [top-lift certificate](../certificates/global-norm-frontier-top-lift.json)
and [independent review](../certificates/global-norm-frontier-top-lift-review.json)
authenticate 24 pinned modules for literal `TopLiftExists3` and `InDDplus2`.
The audit checks the common-type inverse, finite determinant conjugations,
noncommuting recursive slopes, weighted adjoint and all-rank differential
budget. Exact matrix, Weyl-algebra and exponent diagnostics supplement
the human construction. The valid-cut bounds and `k=1` endpoint are
explicit; no global norm estimate or Lean build is asserted.

### Actual weighted arithmetic seeds

The [seed-decay certificate](../certificates/global-norm-frontier-seed-decay.json)
and [independent review](../certificates/global-norm-frontier-seed-decay-review.json)
authenticate eight pinned modules and four primary references. The audit
checks the exact signed parameter and gap, original `IsWu`, `WuWeighted`
and `WuReprod`, formal-degree idempotent, induced-space multiplicity and
all measure conventions. Nonnegative polynomial certificates and finite
nonabelian convolution diagnostics supplement the analytic proof. The
arithmetic setting and uniform global bounds remain separate.

### Actual raw-theta construction and cusp target

The [raw-theta certificate](../certificates/geometry-arithmetic-frontier-raw-theta.json)
authenticates 37 pinned modules, the original row-weight and period
dictionaries, and the primary Miller--Schmid rapid-decay theorem including
central finiteness. Independent review checks arbitrary-base descent,
full product commutators, distinct finite indices, exact classical scalar,
adapted period/gauge identities and the original bounded cusp target.
Exact finite diagnostics and negative controls supplement the human proof;
no Lean build, spanning theorem or uniform archimedean estimate is asserted.

### Actual Gaussian integrability and reproduction

The [Gaussian certificate](../certificates/geometry-arithmetic-frontier-gaussian-reproduction.json)
and [independent review](../certificates/geometry-arithmetic-frontier-gaussian-reproduction-review.json)
authenticate nine pinned modules, including the literal kernel and its
full spanning consumer. The all-rank proof keeps the original mixed-row
Gaussian, harmonic contractions, full frame Jacobian and reproducing
scalar. Exact matrix, minor, Jacobian and Fischer diagnostics check signs
and normalizations; the endpoint integral follows analytically. These
records assert neither a Lean build nor a uniform arithmetic period norm.

### Exact actual-Host Siegel--Weil comparison

The [class-sum certificate](../certificates/geometry-arithmetic-frontier-siegel-weil.json)
and [independent review](../certificates/geometry-arithmetic-frontier-siegel-weil-review.json)
authenticate six pinned modules and three primary references. The audit
checks the exact Host unramifiedness, admitted-family and rational `TransH`
contracts against the convergent Gan--Qiu--Takeda formula, its probability
measure and unitary constant. Local unit norms, character extension,
CRT replacement, central phase and automorphism mass are explicit. No
arbitrary ramified-genus comparison or Lean build is asserted.


### Normalized support and actual spanning suppliers

The [seed-transfer certificate](../certificates/selmer-support-continuation-seed-transfer.json)
authenticates fifteen pinned modules, the original normalized `SeedIn`
contract and starting-chart consumer. The proof keeps the integral Hecke
quotient through a homogeneous finite entry algebra. The
[finite-system](../certificates/theta-spanning-continuation-system.json)
and [raw-span](../certificates/theta-spanning-continuation-raw.json)
certificates record the literal `IsSystem`, level span and identity-cover
`HolSub0LeSpanRaw` interfaces, including Schrödinger inner-product
conventions, full `ChiOne`, original index factors and harmonic descent.
Their finite diagnostics check normalization; the proofs are conventional
mathematics, not Lean builds.

### Positivity and complete arithmetic return summation

The [positivity certificate](../certificates/geometry-positivity-continuation.json)
and [independent review](../certificates/geometry-positivity-continuation-review.json)
record fifteen pinned source modules, seven primary references and the
exact canonical-weight and dimension checks. The applied semipositivity
and effective separation theorems match the original compactification,
boundary extension and nef/big intersection hypotheses.

The [folding](../certificates/global-gram-continuation.json),
[finite-phase](../certificates/global-gram-continuation-phases.json) and
[framed-return](../certificates/global-gram-continuation-framed.json)
certificates retain the original gap, finite lattice integrality,
extended different, level character, stabilizer and Haar definitions.
They prove fixed-setting convergence of the entire original framed-return
sum, without a uniform trace estimate or a replacement of the raw kernel
by a normalized abstract Gram matrix. The
[combined independent review](../certificates/arithmetic-construction-continuation-review.json)
records the reviewed conventional arguments and their precise limits.

### Quantitative theta spans, rank-two support and exact period target

The [short-span certificate](../certificates/theta-spanning-continuation-short.json)
and [independent review](../certificates/selmer-support-continuation-theta-review.json)
retain the literal minimal-level consumer and every norm normalization.
The [flat-degree](../certificates/theta-spanning-continuation-flat.json) and
[parallel-twist](../certificates/theta-spanning-continuation-twist.json)
ledgers authenticate `FlatExistsAt`, integral frames, `UnramPts` and the
exact scalar-rounding cost, including primary good-reduction hypotheses.
The [curve](../certificates/selmer-support-continuation-rank-two-curve.json)
and [propagation](../certificates/selmer-support-continuation-rank-two-propagation.json)
ledgers retain the full rank-two source quantifiers and ordinary cone.

The [period](../certificates/global-gram-continuation-period.json),
[projector](../certificates/global-gram-continuation-projectors.json) and
[minimum](../certificates/global-gram-continuation-minimum.json) ledgers
check `EntryUnfold`, `KExpansion`, `InHH`, `PuLinear`, the exact original
target, and `leastSize` over all submodules. Exact diagnostics test complex
phases, noncommutative convolution, fractional differents and covolume
normalization; general proofs are in the corresponding TeX. The
[independent review](../certificates/arithmetic-quantitative-continuation-review.json)
records decisive checks and limitations. No Lean build or whole-node
completion is asserted.

The [key-shift certificate](../certificates/theta-spanning-continuation-key.json)
authenticates fifteen source interfaces and Moret–Bailly's all-prime key
formula. Exact diagnostics verify both metric exponents, 1,215 weight
cases and 2,673 downstream budget cases. The conventional proof retains
the actual positive quadratic period expansion and ramified eigenframe
determinant; the odd elliptic boundary counterexample excludes a broader
principal-line claim. The output is the literal `h0`/`hsh` family, not a
replacement integral basis. Its independent review is in the combined
quantitative review above.

### Current support, local-chain and quantitative analytic frontiers

The [rank-three transfer](../certificates/selmer-support-continuation-rank-three-transfer.json) and [finite-point](../certificates/selmer-support-continuation-finite-points.json) ledgers retain the original determinant law, closed ordinary/inertia algebra, all-open-subgroup conditions and every complete-DVR test. The type-E, Sharp and normalized-propagation ledgers distinguish nilpotent equations from dimension arguments.

The [local theta-chain ledger](../certificates/theta-spanning-continuation-chain.json) checks the actual phase quotient, stabilizer masses, target polynomial identities, original integral coordinate images and twisted initial source. It does not substitute that chain for the separate Poincare maps. The [quantitative seed ledger](../certificates/global-gram-continuation-quantitative.json) authenticates actual characters, original projectors and measures, with exact diagnostics for the larger tensor reserve and transformed Witt frames.

The [thick-peak ledger](../certificates/geometry-bergman-continuation-thick.json) authenticates the exact squared minimum, nonprincipal-to-principal orbit comparison, tag-zero character law and component norm dictionary. It separately hashes Demailly and Harris primary references and records exact curvature/weight diagnostics. The complete quotient solve and regular-weight cuspidality are ordinary mathematical proofs, not inferred from those computations. The [combined independent review](../certificates/arithmetic-frontier-second-review.json) records the decisive checks and remaining limits. No whole-node completion or Lean build is asserted.

The [finite-end ledger](../certificates/selmer-support-continuation-finite-end.json) checks the literal GalLink kernel, marked maps and complete-DVR scalar towers. The [Haar/covolume ledger](../certificates/global-gram-continuation-haar.json) retains the exact NOinf lattice, source box, fractional different and formal-degree scale; exact tangent and Gaussian determinant diagnostics supplement the conventional proof. The thick ledger now also authenticates the original HostNum/WtNum records and quotient-weight budget. These suppliers do not construct missing family records or complete their entire proof-map nodes.
