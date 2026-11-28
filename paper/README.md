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

**Current builds:** [RH](rh/main.pdf) and [Dirichlet GRH](grh/main.pdf) each have 17 pages; the [reading guide](guide/main.pdf) has one page. Both manuscripts were rebuilt with stabilized references and no overfull boxes, then rendered in full for overview inspection. The chain norm, finite Bessel transfer, rank-one false-lift proof, weighted pair count, rank-two period, crystalline loss and aggregate budget were inspected at readable scale, together with the title pages, conclusion and guide. The build records are [RH](../certificates/rh-build.json), [GRH](../certificates/grh-build.json) and [guide](../certificates/guide-build.json); they certify compilation, not the still-incomplete mathematics. The root compatibility PDF is byte-identical to the active Dirichlet PDF. The [structural review](../certificates/structural-simplification-review.json) records the new ordinary proofs, exact checks, internal reviews and remaining boundaries. Earlier review records and editions retain their original scope.
