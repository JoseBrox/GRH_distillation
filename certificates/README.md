# What these checks establish

`source_files.json` records the exact bytes and hashes of the selected source files. Reproduce it with:

```sh
python3 scripts/check_sources.py --output certificates/source_files.json
```

The manifest fixes the repository, commit, path, and expected Git blob hash. The script also computes SHA-256 from the retrieved bytes. Downloads remain in the ignored `build/source-cache/` directory. After the first run, `--offline` verifies the same cached files without network access.

This is a **source-file integrity check**. It is not a Lean build, a kernel certificate, a complete dependency audit, or a certificate of GRH. The optional lexical inventory applies only to the listed files and includes comments.

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

Run `python scripts/check_classical_averaged_checkpoint.py` with the pinned
source and primary-paper caches present to reproduce
`classical-averaged-integrity.json`. The check verifies source blobs, recorded
line ranges, note and manuscript hashes, and the exact adoption dependencies;
it reports a missing cache instead of silently skipping that evidence.

These records distinguish written proofs, cited classical theorems and
independent human-readable comparisons from compilation or kernel acceptance.
The compatible arithmetic construction remains open.

## RH and geometric continuation

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

Run `python scripts/check_classical_averaged_checkpoint.py --rh-and-geometry`
to reproduce `rh-geometric-integrity.json` with the pinned caches present.
The integration records distinguish historical source-reading snapshots
from the final published manuscript hashes and label positions.
