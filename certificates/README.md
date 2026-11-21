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
