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
