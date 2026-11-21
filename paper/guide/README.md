# Short mathematical guide

[Read the guide](main.pdf) or [edit its complete TeX source](main.tex).

This is a didactic account of the problem, the proof strategy, the completed
reductions and the remaining arithmetic construction. It is organized by
mathematical dependence. It is not a chronological report or a substitute
for the detailed manuscript.

The current RH route compares the thick weights at their common lower
endpoint, uses positivity before averaging over translations, and controls
the thin samples with the existing uniform quasi-RH input. It imposes no
weight-symmetry hypothesis. The remaining target is one normalized averaged
arithmetic discrepancy, with the geometric comparison stated through its
actual height moments, section errors and map-frame costs. The short
one-sided analytic proof for zeta is included in full.

Keep the guide at most twelve pages, with readable type and margins. When
results change, rewrite the relevant explanation and remove superseded
material. Put detailed proofs, source dictionaries and verification records
in their existing project locations. Never shorten the guide by concealing
an assumption or presenting an unproved estimate as established.

Build and check the length with:

```sh
python scripts/build_paper.py --guide
```

The build checks references and overfull boxes and records actual input/PDF
hashes. Visual inspection is recorded separately. Changes to the guide do
not change the manuscript's recovered-section count.
