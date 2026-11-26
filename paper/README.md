# Mathematical manuscripts

The **[revised proof plan](../blueprint/merged-proof-plan.md)** is the
current research guide after the Sernau–Anthropic audit. Its ordinary
[determinant](../notes/lsernau-mathematical-extraction-2026-11-26.md) and
[spanning/prime-sum](../notes/lsernau-moment-and-prime-reductions.md)
arguments are written separately. The existing manuscripts below preserve
the earlier four-character/geometric route and its reusable proofs; they
have not been relabelled as a completed reconstruction of the new source.

| Route | Manuscript | Source | Research program |
| --- | --- | --- | --- |
| Ordinary Riemann hypothesis | [RH paper](rh/main.pdf) | [TeX entry](rh/main.tex) | [RH program](../blueprint/rh/program.md) |
| Dirichlet generalized Riemann hypothesis | [GRH paper](grh/main.pdf) | [TeX entry](grh/main.tex) | [GRH program](../blueprint/grh/program.md) |
| Introduction to both routes | [Short guide](guide/main.pdf) | [TeX source](guide/main.tex) | [Proof maps](../blueprint/README.md) |
| Additional analytic arguments | [Companion](companion/main.pdf) | [TeX entry](companion/main.tex) | [Shared results](../blueprint/shared/README.md) |

Both research manuscripts are incomplete. They distinguish proved reductions,
cited theorems, conditional constructions and the remaining estimates. The RH
paper is organized around zeta and the smaller character projection. The GRH
paper develops the full character-dependent construction and technical arguments.

## Shared mathematics

The [technical chapters](sections/), [common preamble](preamble.tex) and
[references](references.tex) form the common library. The GRH entry assembles
those chapters; the RH paper proves its shorter analytic and arithmetic
comparisons and cites precisely stated shared results where appropriate.
The [proof-library manifest](shared/manifest.json) records which fragments
each paper includes directly. Longer alternatives can stay in the GRH
technical text without enlarging the shorter RH exposition.
The [shared-results index](../blueprint/shared/README.md) records the applications
and extra hypotheses of each route. Improvements are reviewed in both routes;
an RH-specific simplification is not silently generalized to all characters.

The eight-page guide remains an organizational introduction to both routes,
with a twelve-page editorial limit. Audit records, source identifiers and
chronological checkpoints stay outside the mathematical exposition.

## Building and verifying

From the repository root:

```sh
python scripts/build_paper.py --rh
python scripts/build_paper.py --grh
python scripts/build_paper.py --guide
python scripts/build_paper.py --companion
python scripts/build_route_blueprints.py
```

The default build is GRH. Existing `paper/main.tex` and `paper/main.pdf` links
remain compatibility entries for that manuscript. They are not a third route.
Both route builds use XeLaTeX, stabilize references, reject undefined citations
and overfull boxes, and record hashes of every actual TeX input, including
shared chapters. The PDFs are inspected separately for readable layout.

The [source atlas](../blueprint/lean-source-atlas.md) and
[verification records](../certificates/README.md) distinguish pinned source
bytes, ordinary mathematical review, exact finite calculations and remaining
construction hypotheses. None of these checks alone establishes RH or GRH.
