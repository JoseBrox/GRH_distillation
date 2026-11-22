# What these checks establish

## Current difficult-node continuation

The [frontier proof review](frontier-progress-review-2026-11-22.json)
records independent mathematical reviews and frozen proof/checker identities.
The [current integration record](frontier-progress-integration-2026-11-22.json)
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
