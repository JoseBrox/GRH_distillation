# Mathematical manuscripts

The preferred ordinary RH and Dirichlet route is now presented as a single shared mathematical argument, with separate target-specific entry files. See [the common body](determinant/body.tex), [RH](rh/main.tex), [Dirichlet GRH](grh/main.tex), [guide](guide/main.tex), [revised proof plan](../blueprint/merged-proof-plan.md) and [Hecke manuscript](../hecke/paper/main.md).

The active manuscript is organized by mathematical necessity: analytic endpoint, common data, A (short forms), B (spanning), C (selected-twist determinant), and final signed budget. Specialist proofs are linked at their exact use; unproved suppliers remain explicit. No chronological continuation notes or abandoned branches are included as prerequisites. Earlier results remain accessible in the [historical manuscript archive](archive/README.md), shared technical files and Git history.

## Building

From a checkout with a working TeX installation:

```sh
python scripts/build_paper.py --rh
python scripts/build_paper.py --grh
python scripts/build_paper.py --guide
python scripts/build_paper.py --revised-plan
```

The existing build script stabilizes references and checks overfull boxes. It generates the active PDF files at their usual locations. The historical [companion](companion/main.pdf) remains available as optional analytic material. The root compatibility entry `paper/main.tex` inputs the active Dirichlet manuscript.

**Current builds:** [RH](rh/main.pdf) and [Dirichlet GRH](grh/main.pdf) each have 14 pages; the [reading guide](guide/main.pdf) has one page. They were rebuilt from the current active sources with stabilized references and no overfull boxes. All GRH pages were rendered and inspected in overview; the revised noncompact, Galois and arithmetic sections, both target title pages, the concluding page and the complete guide were also inspected at readable scale. The build records are [RH](../certificates/rh-build.json), [GRH](../certificates/grh-build.json) and [guide](../certificates/guide-build.json); they certify compilation, not the still-incomplete mathematics. The root compatibility PDF is byte-identical to the active Dirichlet PDF. Historical editions remain in the archive.
