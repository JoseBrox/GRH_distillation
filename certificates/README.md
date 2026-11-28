# What these checks establish

> **Verification scope.** Verification certificates are **versioned evidence**, not an updatable proof-completion score. Older review reports and source/PDF hashes apply to the revisions they record; they must not be rewritten to match later manuscripts. Current research targets are in the [checkpoint](../notes/current-state.md) and [dependency plan](../blueprint/merged-proof-plan.md). No Lean kernel rebuild is claimed.

## Current navigation: recent certificate families

The new [Sernau source inventory](../audit/lsernau-source-inventory-2026-11-26.json)
and [formal audit](../audit/lsernau-formal-audit-2026-11-26.md) record the
pinned rewrite and the actual scope of static and execution checks.
Source inventory, partial compilation, full build and dependency replay
are separate verification levels. The audit also records the independently
published verification and the matching source-hash manifest.
The [further-reductions review](lsernau-further-reductions-review.json)
records the new analytic, specialization and CM results; the earlier
integration review retains its original checkpoint hashes.
The [revised-plan build](revised-plan-build.json) records the historical eight-page PDF. The active manuscripts have since been reorganized; see the [archive](../paper/archive/README.md) and [current manuscript publication status](../paper/README.md). No old PDF hash certifies a new source.
The [revised plan](../blueprint/merged-proof-plan.md)
keeps its ordinary mathematical suppliers explicit.

| Workstream | Selected recent proof and review records |
| --- | --- |
| Selmer and deformation | [Uniform spectrum](selmer-support-continuation-spectrum.json), [RH nonresonant primes](rh-selmer-nonresonant.json), [dyadic Bernoulli theorem](rh-dyadic-bernoulli-unit.json) and [independent review](rh-dyadic-bernoulli-unit-review.json) |
| Integral theta | [Terminal period and Bessel unfolding](theta-period-continuation.json) |
| Global norms | [Embedded-isometry mean](embedded-isometry-genus-count.json), [unipotent covolume](unipotent-stabilizer-covolume.json), [integral transport](flag-lattice-transport.json), [weighted normal-form sum](weighted-flag-lattice-sum.json) and [review](weighted-flag-lattice-sum-review.json) |
| Geometry | [All-point height](geometry-point-height.json), [signed determinant assembly](geometry-height-assembly.json) and [independent review](geometry-height-assembly-review.json) |
| Active compiled manuscripts | [RH build](rh-build.json), [GRH build](grh-build.json), [short guide build](guide-build.json) |

## Active structural simplifications and proof closures

The [structural review](structural-simplification-review.json) records the
new ordinary proofs, independent internal checks, precise hypotheses and
remaining boundaries. The primary references are identified in each note.

| Supplier | Reproducible verification and scope |
| --- | --- |
| [Actual common-chain transport](../notes/lsernau-common-chain-transport.md), [norm budget](../notes/lsernau-common-chain-norm-budget.md), [six-copy comparison](../notes/lsernau-six-copy-test-transport.md) | [Checker](../scripts/check_common_chain_transport.py), [certificate](common-chain-transport.json): exact finite gluing/Gram identities, integral monomial contractions, rank and vacuum exponents, pinned source blobs and the numerical cost ledger. Minkowski counting and the uniform norm argument are written proofs. The analytic see-saw and general product-form gluing remain separate. |
| [Rank-one false-lift periods](../notes/lsernau-rank-one-false-lift-periods.md) | [Checker](../scripts/check_rank_one_false_lift_periods.py), [certificate](rank-one-false-lift-periods.json): 11 source blobs, 2,870 projection entries, 17,640 congruence stabilizers, 9,792 Gaussian-binomial coefficients, 384 norm products and 8,448 transfer exponents. The ordinary proof closes the actual rank-one test; the higher-rank gluing periods are not claimed. |
| [Direct Bessel good-type transfer](../notes/lsernau-bessel-good-type-transfer.md) | [Checker](../scripts/check_bessel_good_type_transfer.py), [certificate](bessel-good-type-transfer.json): 10 balanced/one-sided induction comparisons over 45,294 subgroup matrices, 8,268 exact rational weight inequalities and 246 cuspidal equalities. Andrews–Thiem's primary theorem, mirabolic induction and the actual trace identity justify the general result. Analytic strip estimates are retained hypotheses. |
| [Rank-two analytic period](../notes/lsernau-rank-two-period-norm.md) | [Checker](../scripts/check_rank_two_period_norm.py), [certificate](rank-two-period-norm.json): 3 symbolic rational identities, 390 Cartan/Euler coefficient comparisons, 17,764 finite matrices and 17 Fock norms, with pinned sources and primary-reference hashes. The constant-lift and anisotropic Siegel–Weil proof closes the fully ramified norm and nonzero initial period; computation does not substitute for those theorems. |
| [Exact cyclotomic loss and aggregate budget](../notes/lsernau-exact-cyclotomic-loss-and-budget.md) | [Checker](../scripts/check_exact_cyclotomic_loss.py), [certificate](exact-cyclotomic-loss.json): 32 exact cyclic/coinvariant cases and 8 sparse all-prime integer certificates, with source hashes. The actual growing-field nonabelian projection budget is still open. |
| [Weighted lattice average](../notes/lsernau-link-lattice-counting.md) | [Checker](../scripts/check_link_lattice_counting.py), [certificate](link-lattice-counting.json): 534 Smith types, 93,762 explicit nonzero rows, 80 Hermitian complement and 20 Gaussian-integer index identities, 180 local zeta coefficients and 1,260 weight trades. The ordinary proof retains the essential conductor gain. |
| [Three-quotient frame count](../notes/lsernau-corank-frame-fibres.md) | [Checker](../scripts/check_corank_frame_fibres.py), [certificate](corank-frame-fibres.json): 36 exact integral-move cases, 18 skew solutions, six universal exponent certificates and six source blobs. Together with the lattice theorem this proves the full weighted pair count in the specified cell, corank and discriminant range. |
| [Link congruence and torsion-index gain](../notes/lsernau-link-gain-index.md) | [Checker](../scripts/check_link_gain_index.py), [certificate](link-gain-index.json): 125 graph pairs, 100 determinant examples, 174 nondegenerate congruence examples, 120 finite-group/Hermite comparisons and 60 bordered minors. The written proof isolates one still-open integral link-lattice cut. |
| [Conditional single-link reduction](../notes/lsernau-single-link-energy-frontier.md) | [Checker](../scripts/check_single_link_energy.py), [certificate](single-link-energy-frontier.json): seven source blobs and universal exact scale comparisons. The integral cut, gauge-specific orbit bound and zero-term reduction remain explicit hypotheses; neither restricted moment is claimed proved. |

The previous five-supplier review below is a frozen earlier checkpoint.
Its hashes and then-open boundaries are retained as historical evidence;
the new review records later closures and current artifact hashes.

## Earlier five-supplier verification

The [supplier review](supplier-closure-review.json) records the exact
scope of the ordinary proofs, independent internal mathematical reviews,
remaining obligations and current artifacts. The five suppliers are
organized by their use in the determinant argument:

| Supplier | Reproducible check and precise scope |
| --- | --- |
| [All-prime sharp scalar tests](../notes/lsernau-sharp-scalar-couplings.md) | [Script](../scripts/check_sharp_scalar_couplings.py), [certificate](sharp-scalar-couplings.json): 108 exact derivative-coefficient cases, 51,456 large-prime weight cases and 3,396 sparse-weight cases, 1,068 with nonempty couplings. Nine source blobs are checked. The formal-group and analytic theta assertions are proved in the note, not by this enumeration. |
| [Good-form multiplicities](../notes/lsernau-good-form-multiplicities.md) | [Script](../scripts/check_good_form_multiplicities.py), [certificate](good-form-multiplicity-conventions.json): 98,458 signature tuples and all regular degree-two cuspidal characters of GL2(F2) and GL2(F3), with exact cyclotomic orthogonality, unipotent averages and projector convolution. The automorphic comparison uses the specified Harris–Labesse theorems. |
| [Finite good-type density](../notes/lsernau-finite-good-type-density.md) | [Script](../scripts/check_finite_good_type_density.py), [certificate](finite-good-type-density.json): 5,504 polynomials, 4,041 exact regular-label masses, 136 allowed-label counts and 816 tuple-deficit comparisons. The universal argument and admissible numerical estimates are written proofs relative to Green's character theorem. |
| [Rank-two period arithmetic](../notes/lsernau-rank-two-period-arithmetic.md) | [Script](../scripts/check_rank_two_period_arithmetic.py), [certificate](rank-two-period-arithmetic.json): 397,442 prime-square residue matrices, 72 q-binomial/corank identities, 8 Laurent Euler squares and 528 denominator-exponent comparisons. The finite checker does not prove analytic interpolation; that assertion is now supplied by the separate rank-two analytic proof above. |
| [Uniform bounded-class crystalline loss](../notes/lsernau-bounded-class-crystalline-loss.md) | [Source verifier](../scripts/check_bounded_class_crystalline_sources.py), [record](bounded-class-crystalline-loss-sources.json): three pinned interfaces and Liu's published reference. The Artinian-cohomology proof is qualitative; no numerical loss constant is computed. |

The combined [source-ledger verifier](../scripts/check_supplier_closure_sources.py)
checks 29 ledger rows against 26 distinct immutable Git blobs and the
Harris–Labesse and Liu primary PDFs. Its [record](supplier-closure-source-checks.json)
also hashes the five proof notes. Run it with `--offline` after its cache
has been populated. Source-byte verification, finite computation, ordinary
mathematical proof and Lean kernel replay are separate kinds of evidence;
no new Lean replay or external mathematical review is claimed.

The remainder of this file is a **historical index of checks**, with commands and claims preserved at their original scope. The “current” label in dated sections refers to that historical checkpoint.

## Historical reduction continuation (22 November 2026)

The [reduction review](reduction-continuation-review-2026-11-22.json)
records six new mathematical suppliers and two precisely delimited norm
checkpoints. It separates independent proof review, exact examples,
authenticated source interfaces and adopted classical theorems. The
[integration record](reduction-continuation-integration-2026-11-22.json)
records the two manuscripts, the eight-page guide, visual checks and
unchanged proof-map counts. Reproduce the current snapshot check with:

```sh
python scripts/check_reduction_continuation.py
```

The new mathematical checks are:

```sh
python scripts/check_dominant_return_deficit.py
python scripts/check_level_chain_integrality.py
python scripts/check_finite_section_jet_bound.py
python scripts/check_selmer_tangent_comparison.py
python scripts/check_cusp_counting_mean.py
python scripts/check_selmer_crystalline_component_comparison.py --offline
python scripts/check_projector_kernel_tail.py
```

The crystalline check also authenticates the downloaded primary-reference
bytes and bounded extracts; omit `--offline` to populate an empty cache.
The kernel checkpoint authenticates its stated upstream estimate and
proves the cutoff simplification and moment limitation. It does not
replace the full upstream proof of that estimate. No new Lean build or
whole-node completion is claimed. All earlier review and integration
records describe their own version-controlled snapshots.

## Previous difficult-node continuation

The [frontier proof review](frontier-progress-review-2026-11-22.json)
records independent mathematical reviews and frozen proof/checker identities.
The [earlier integration record](frontier-progress-integration-2026-11-22.json)
separately records the manuscripts, short guide, blueprint updates and
visual inspection. Reproduce its artifact checks with:

```sh
python scripts/check_frontier_progress_integration.py
```

The supplemental exact calculations and authenticated source excerpts are
reproduced by:

```sh
python scripts/check_prescribed_trace_calibration.py
python scripts/check_rh_selmer_diagonal_rigidity.py
python scripts/check_ramified_hodge_determinant.py
python scripts/check_whittaker_scalar_envelope.py
python scripts/check_seed_return_deficit.py
python scripts/check_cm_integral_map_extension.py
python scripts/check_rh_selmer_negative_weight_rigidity.py
python scripts/check_cm_period_point_descent.py
```

These checks distinguish written proofs, classical inputs, source identity
and finite examples. They do not build the upstream Lean project or prove
the remaining arithmetic estimates. The previous hard-node integration and
its validator retain the earlier manuscript snapshot at
`c9def8d66b96082ad46a06c161de6b8da800b440`; they are historical records,
not assertions that today's manuscripts have their former hashes.

## Pinned source files

`source_files.json` records the exact bytes and hashes of the selected source files. Reproduce it with:

```sh
python3 scripts/check_sources.py --output certificates/source_files.json
```

The manifest fixes the repository, commit, path, and expected Git blob hash. The script also computes SHA-256 from the retrieved bytes. Downloads remain in the ignored `build/source-cache/` directory. After the first run, `--offline` verifies the same cached files without network access.

This is a **source-file integrity check**. It is not a Lean build, a kernel certificate, a complete dependency audit, or a certificate of GRH. The optional lexical inventory applies only to the listed files and includes comments.

## Fourth-power, determinant and integer comparisons

The [continuation review](continuation-review-2026-11-22.json) records
independent mathematical reviews, exact artifact hashes and their scope.
The accompanying supplemental checks are reproduced with:

```sh
python scripts/check_fourth_power_sampling.py
python scripts/check_geometric_flat_determinant.py
python scripts/check_rh_selmer_resultant.py
python scripts/check_rh_selmer_valuation_frontier.py
python scripts/check_flat_family_finite_place_frontier.py
```

They check the interpolation and endpoint algebra, bounded pinned source
passages, determinant normalization, exact resultants and the exceptional
prime factors in the common-divisor bound. Finite checks supplement the
written universal proofs. The reviewed reductions do not supply the
remaining arithmetic construction or complete an existing proof-map node.

The two frontier checks also record the exact source hypotheses at the
remaining arithmetic and geometric comparisons. The
[integration record](continuation-integration-2026-11-22.json) separately
records the recovered classical proofs, final manuscript builds, page
review and current diagram checks.

## Exponent calculations

`exponents.json` contains exact rational evaluations of the two affine exponents in the power argument, their intersection, and the sextic specializations. Reproduce the check with:

```sh
python3 scripts/verify_exponents.py --check certificates/exponents.json
```

The script checks finite rational identities. The proof for all integers $m\geq2$ is in the paper. In particular, an evaluation at $\vartheta=0$ records the limiting algebraic exponent and does not assert an arithmetic estimate at that endpoint.

## Compiled paper

`paper-build.json` records the hashes of the TeX sources and the compiled PDF, the engine, and the scope of the build checks. Rebuild with `python3 scripts/build_paper.py`. Visual review of the rendered pages is a separate step; compiling a document does not verify its mathematics.

## Matrix identities and integrated pairings

- `bordered-capelli-review-check.json` records an exact PBW normal-order check
  of the bordered determinant identity in full dimensions 3, 4 and 5, with a
  wrong-shift negative control. Reproduce it with
  `python scripts/check_bordered_capelli.py`.
- `commutator-matrix-check.json` and
  `radial-commutator-independent-check.json` record complementary exact tests
  of the matrix reconstruction and transfer operators. Their written proofs
  retain all-rank arguments and the required analytic domains.
- `fused-transfer-exact.json` records rational Laurent-action checks of the
  residue congruence, with noncommuting terminal coefficients, all sign words
  through length three, and wrong-order and wrong-argument controls. Run
  `python scripts/check_fused_transfer.py` to reproduce them. Finite action
  checks support the written argument and do not prove arbitrary length.

## Structural proof maps

`proof-architecture-allocation.json` records the reviewed 97-section baseline,
the optional branches and the exact dependency substitution. The live
`blueprint/module-inventory.json` additionally includes recognized new sections
and their current hashes. `blueprint-check.json` checks graph endpoints, exact
section coverage, unique labels and appendix placement. None is a full formal
dependency audit or a proof of the missing arithmetic estimate.

## Current arithmetic and geometric comparisons

- `classical-galois-substitution.json` ties together the full local
  correspondence, depth-zero type formula, global period dictionary, local
  preimages and universal weak-correspondence transfer. It records the
  adopted classical supplier and the exact hashes of its dependencies.
  The two new dictionaries include pinned source ranges, primary references
  and independent mathematical reviews.
- `one-construction-target.json` records the complete original clause ledger
  and the finite averaged criterion with weighted lower estimates.
- `covolume-defect-budget.json` records the orthogonal covolume identity,
  discarded-degree/index criterion, counterexamples and geometric obligations
  still to be proved.

At the earlier checkpoint it certifies, run
`python scripts/check_classical_averaged_checkpoint.py` with the pinned
source and primary-paper caches present to reproduce
`classical-averaged-integrity.json`. The check verifies source blobs, recorded
line ranges, note and manuscript hashes, and the exact adoption dependencies;
it reports a missing cache instead of silently skipping that evidence.

These records distinguish written proofs, cited classical theorems and
independent human-readable comparisons from compilation or kernel acceptance.
The compatible arithmetic construction remains open.

## RH and geometric continuation

The current preferred continuation is recorded in:

- `rh-direct-transfer.json`: positive primitive-character kernels, including
  ramified primes, the one-sided thick comparison, the exact thin-sample
  count, the general fixed-quotient extension and source cost substitutions. Run
  `python scripts/check_rh_direct_transfer.py`.
- `rh-direct-source-applicability.json`: the actual source quotient,
  primitive-character identification, corrected principal sum and
  all-character thin hypotheses, with independently checked source hashes
  and bounded excerpts.
- `rh-weight-symmetry.json`: the sparse-top obstruction to both pooled
  measures and first moments, quantitative lower bounds, and the optional
  complete-top identity. Run `python scripts/check_rh_weight_symmetry.py`.
- `rh-geometric-combination.json`: the improved covering coefficient,
  optimized two-height-moment estimate and averaged refined frame penalty.
  Run `python scripts/check_rh_geometric_combination.py`.
- `transport-symmetry-defect.json`: conductor-uniform transport, primitive
  inertia kernels and the signed residual identity. Its absolute majorant
  is too large for the current source family; the direct transfer avoids
  that limitation. Run `python scripts/check_transport_symmetry_defect.py`.
- `rh-minimal-budget.json`: exact four-term normalization at the actual
  source ranks, the improved exponent loss, sharp frame comparison and
  relaxed analytic transfer allowances. Run
  `python scripts/check_rh_minimal_budget.py`.
- `scale-averaged-criterion.json`: the positive-part whole-window criterion,
  pole-preserving local averaging and exact hypotheses of the combined
  arithmetic budget. Its written proof and independent review are recorded;
  finite computation is not used to certify the analytic theorem.
- `geometric-degree-frontier.json`: exact volume weights, short-section
  degree floors, the one-mean estimate and the raw signed rank cost. Run
  `python scripts/check_geometric_degree_frontier.py`.
- `averaged-theta-energy.json`: exact aggregate energies, retained-energy
  compression and the same-map kernel interface. Run
  `python scripts/check_averaged_theta_energy.py`.
- `rh-construction-frontier.json`: surviving RH clauses, the unbounded
  integral index and the optional paired-construction comparison. Run
  `python scripts/check_rh_construction_frontier.py`.
- `finite-symmetry-energy.json`: the exact finite-group averaging identity,
  surviving multiplicity variance and the actual target-stability
  obstruction. Run `python scripts/check_finite_symmetry_energy.py`.
- `frame-degree-compatibility.json`: centered dimension and slope
  comparisons, optimum common normalization, sharp target-cut examples
  and limits of a proposed frame replacement for geometric degree. Run
  `python scripts/check_frame_degree_compatibility.py`.
- `rh-centered-frame-bridge.json`: the actual quotient-source, target,
  units and rank dictionary; explicit nonframe residual; surviving four
  error shapes. Run `python scripts/check_rh_centered_frame_bridge.py`.
- `mean-volume-supplier.json`: the precise normalized tower-intersection
  requirement, prescribed metric and counting bridge, fixed-data limiting
  step and improved finite-prime allowance. Run
  `python scripts/check_mean_volume_supplier.py`.
- `concurrent-routes-review.json`: current integration and visual review,
  with exact hashes of the reviewed artifacts and remaining obligations.
  `rh-continuation-integrity.json` verifies the current continuation records,
  pinned selected sources and bounded ranges, current build sources and
  reviewed artifacts. Run `python scripts/check_rh_continuation.py` with
  the pinned source cache present; missing evidence causes failure.

The following reductions are shared by the separate manuscripts. Their
notes contain the mathematical proofs; their certificates distinguish
source authentication, independent review and supplemental computation.

| Certificate | Result or precise limitation |
| --- | --- |
| `finite-window-sampling.json` | Finite integer tables suffice on growing intervals, with an explicit interpolation error. |
| `two-primary-selmer-reduction.json` | The nontrivial odd-order branch disappears for RH; harmonic prime–twist counting reduces the loss. |
| `qualitative-selmer-finiteness.json` | Classical duality and finite even K-groups supply finiteness and finite prime support, including at two. |
| `finite-twisted-place-budget.json` | Only the weighted finite sum at the actual twisted places is required. |
| `coarse-selmer-budget.json` | The existing coarse bound is too large to supply the required growing-family budget directly. |
| `selected-eigenspace-degree.json` | A two-case argument bounds the selected degree while retaining favorable integral indices and exact ranks. |
| `theta-jet-slope-reduction.json` | Integral leading derivatives give an economical conditional theta proof of the tangent slope bound. |
| `absolute-siegel-supplier.json` | The absolute Siegel lemma applies in the prescribed metric, after finite extension and principalization. |
| `redundant-period-spectrum.json` | The correct global spectral threshold and exact countermodels delimit what pairwise estimates imply. |

Run the corresponding `scripts/check_<name>.py`, replacing hyphens in the
certificate name by underscores. The continuation integrity check includes
these records, their bounded source passages and their primary references.

These records contain independent mathematical review scopes and exact
supplemental checks. They do not verify the missing arithmetic construction.
The following earlier records retain their original source inspections and
proof scopes; the current integrated continuation records superseding
manuscript and rendering evidence separately.

- `rh-geometric-checkpoint.json` joins the final proof, source, computation,
  blueprint and rendering evidence, with the remaining arithmetic hypotheses
  stated explicitly.
- `rh-specialization.json` records the conductor-one source specialization,
  the eventual one-sided zeta criterion, the single signed companion budget,
  the actual-mean centering calculation and the surviving growing-field inputs.
- `averaged-error-budget.json` records signed Fourier accounting, fixed
  quotients, the cancellation obstruction, the three-mean transfer and frame
  moments. Run `python scripts/check_averaged_errors.py` to reproduce the exact
  finite checks in `averaged-error-exact.json`; these support the proofs and
  do not replace them.
- `geometric-core-lower-bound.json` records the actual core lattice,
  determinant descent, orthogonal type averages, component averaging and the
  exact Hilbert–Samuel surplus, with its remaining geometric bounds.
- `guide-build.json` and `guide-review.json` record the short guide's length,
  current source/PDF hashes, independent mathematical reviews and page review.

At its original checkpoint, run
`python scripts/check_classical_averaged_checkpoint.py --rh-and-geometry`
to reproduce `rh-geometric-integrity.json` with the pinned caches present.
Those historical checks intentionally retain the then-current note and
manuscript hashes; use the new continuation check for the present integration.
The integration records distinguish historical source-reading snapshots
from the final published manuscript hashes and label positions.
