# Short mathematical guide

[Read the guide](main.pdf) or [edit its complete TeX source](main.tex).

This is a didactic account of the problem, the proof strategy, the completed
reductions and the remaining arithmetic construction. It is organized by
mathematical dependence. It is not a chronological report or a substitute
for the separate [RH](../rh/main.pdf) and [Dirichlet GRH](../grh/main.pdf)
manuscripts.

The short one-sided analytic proof for zeta is included in full. The more
flexible final target combines the arithmetic terms with their signs,
averages nearby scales, and bounds the weighted integral of the positive
part. The guide explains why that averaging preserves the poles detecting
zeros.

For RH, positivity and translation averaging handle the thick weights,
and the uniform quasi-RH input controls the thin samples. Short integral
sections reduce the geometric comparison to one weighted mean height.
Summing the volume comparison first improves that mean, and the tower
calculation reduces to a single normalized test intersection. One upper
bound for all periods together can control their centered energy. These
reductions retain the same actual maps and normalizations; the compatible
construction, genuine global energy and geometric bounds remain open.

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
