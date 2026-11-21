# Sources and attribution

## Alpöge's original work

The original mathematical work is by **Levent Alpöge, in collaboration with Claude**, as described in his [announcement](https://alpo.ge/remark.pdf). The project brief identifies the model as **Fable 5.2**; that version is not specified in the announcement we inspected. The Fable 5.2 credit in the mirror's README is explicitly for an added timeline image and does not establish which model produced the original proof.

The announcement links fourteen parts of `lean.tar.gz`, at `https://alpo.ge/lean.tar.gz.part01` through `https://alpo.ge/lean.tar.gz.part14`. It is an announcement of a formal proof, not a detailed mathematical paper proving every statement discussed here.

## Stable Lean references

We use the [jsmorph/rh mirror at commit ecd09ff9](https://github.com/jsmorph/rh/tree/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de). Its README reports that `lean/` is an unmodified copy of the original archive. We have not yet independently downloaded and hashed the original archive.

| File | Role |
| --- | --- |
| [Statements.lean](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Statements.lean) | Definitions of the exported RH and Dirichlet-GRH propositions. |
| [Main.lean](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Main.lean) | The five exported theorem declarations. |
| [lean-toolchain](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/lean-toolchain) | Declared compiler version. |
| [lakefile.toml](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/lakefile.toml) | Build roots and declared Mathlib revision. |

The mirror states that the original archive contains no license file. We link to the source rather than copying the complete archive into this repository.

## Quasi-RH sources

Both papers are attributed to **OpenAI, with human assistance**, as stated in their source repository.

1. *The Quasi-Riemann Hypothesis*, September 30, 2026. [Pinned source directory](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026), with `paper.pdf` and `build/paper.tex`.
2. *The Quasi-Riemann Hypothesis*, October 5, 2026. [Pinned source directory](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026), with `paper2.pdf` and `build/paper2.tex`.

The dates distinguish the approaches; they do not imply progressively stronger conclusions. Precise statements and the scope of checking belong in the audit and paper.

## Our contributions

The exposition, mathematical reconstructions, checks, and limitations developed here are distinct from the original announced proof. A proof of a reduction is not a verification of its difficult input. Cite each imported result and state every unresolved input explicitly.

## Reading one source at a time

Start from the [current continuation checkpoint](../notes/current-state.md).
The bounded reader checks a selected file against its pinned Git blob before
showing a declaration search or an explicitly requested line range:

```sh
python scripts/source_excerpt.py --source lean/src/Main.lean --search theorem
python scripts/source_excerpt.py --source lean/src/Main.lean --lines 1:12
```

The file is cached locally, not copied into the conversation in full. Search
output is limited to 25 matches; excerpts are limited to 120 lines and 12,000
bytes. A source-byte check is not a proof check or a Lean build.

The complete pinned local source is now indexed in the
[source atlas](../blueprint/lean-source-atlas.md). To select any indexed
module by its full name while keeping the same bounds:

```sh
python scripts/source_excerpt.py --atlas --source Main --search theorem --offline
```

The reader checks the local mirror bytes against the stored Git blob and then
uses the verified cache. If the local mirror is unavailable, omit `--offline`
to retrieve only the selected file. The full import index and its precise
verification scope are preserved in the repository; large source bodies stay
outside conversational context.
