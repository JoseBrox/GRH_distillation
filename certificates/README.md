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

The script checks finite rational identities. The proof for all integers m ≥ 2 is in the paper. In particular, an evaluation at ϑ = 0 records the limiting algebraic exponent and does not assert an arithmetic estimate at that endpoint.

## Compiled paper

`paper-build.json` records the hashes of the TeX sources and the compiled PDF, the engine, and the scope of the build checks. Rebuild with `python3 scripts/build_paper.py`. Visual review of the rendered pages is a separate step; compiling a document does not verify its mathematics.
