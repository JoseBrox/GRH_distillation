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
Finite tables at fourth powers suffice when their interpolated positive
weighted cost meets the stated growth condition.

For RH, positivity and translation averaging handle the thick weights,
and the uniform quasi-RH input controls the thin samples. Short integral
sections reduce the geometric comparison to one weighted mean height.
Summing the volume comparison first improves that mean, and the tower
calculation reduces to a single normalized test intersection. Classical
height theory identifies the required all-point lower bound and cusp
correction. Classical theta sections now supply the tangent-slope estimate
in the required metric. First-order sections construct the two finite-field
filtrations; determinant torsion and a connected-fibre argument then give
one finite order. Relative trace duality supplies the exact CM eigenframe
factor. A direct period argument extends the determinant section across
the complex boundary on the prescribed model. One CM elliptic curve gives
the product and period value. A short cokernel identity constructs the
exact integral determinant at ramified primes. The prescribed pure-period
point descends to a number field with its original line and finite level
maps. Properness and classical uniqueness then extend its exact line and
tangent lattice integrally. The actual arithmetic model, its original
global family and fibre data, and the pointwise period presentation remain
required.
The Selmer comparison combines a compatible conormal pairing, exact
graded calculations and a finite slice with at most two points. Its
abstract numerical estimate is proved under the stated arithmetic-model
hypotheses. Finite inertia averaging and the Hilbert class field supply
diagonal point uniqueness. Qualitative Selmer finiteness, local cohomology
and the explicit marking give all nonpositive base-point rigidity. The
actual local/model comparisons, two-sided rigidity and uniform integral
bounds remain.
Two trace errors control the slope comparison at any prescribed positive
mass. A strict source deficit also proves aggregate nonvanishing. Exact
seed norms and weighted Cauchy--Schwarz give a scalar sufficient bound for
the complete period sum, including all rational translates. These
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
