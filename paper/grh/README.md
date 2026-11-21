# Dirichlet GRH manuscript

The [manuscript](main.pdf) develops the argument for primitive Dirichlet
characters and its extension to imprimitive characters. Its
[TeX entry](main.tex) arranges the common technical chapters by mathematical
dependency. The compatible uniform arithmetic construction remains open.

The [GRH proof program](../../blueprint/grh/program.md) and
[technical map](../../blueprint/grh/proof.svg) track its requirements.
The [ordinary RH manuscript](../rh/main.pdf) specializes the target to zeta
and develops the shorter four-character comparison.

Both routes use the [shared technical chapters](../sections/) and
[shared-results index](../../blueprint/shared/README.md). Improvements are
reviewed in both applications, with their distinct conductor, field and
rank hypotheses retained. A simpler RH argument is not automatically a
Dirichlet-GRH argument.

Build from the repository root with `python scripts/build_paper.py --grh`.
The older `paper/main.pdf` link is maintained as an identical copy.
