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

**Publication status:** active TeX sources have been reorganized; new PDF builds and their certificates have not yet been run/published in this repository checkpoint. The old PDF blobs are preserved only in the archive. Older build records remain historical evidence, not certification of the changed sources. A fresh build and visual inspection are required before publishing replacement PDFs.
