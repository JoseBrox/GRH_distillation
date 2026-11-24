# Hecke GRH proof program

The preferred route is the [elementary arithmetic manuscript](../paper/main.md).
It does not depend on the Masullo formalization. The smoothed spectral
route is an optional alternative. H07 has been subdivided into its
two genuinely distinct arithmetic tasks.

| ID | Responsibility | State | Exact output or remaining task |
| --- | --- | --- | --- |
| H01 | Classical Hecke setup | Cited | Euler product, continuation, functional equation and class field reciprocity. No explicit formula is needed on the preferred route. |
| H02 | One-sided zero detection | Proved | Direct Mellin transform and our independently written window lemma; optional smoothed tests retained. |
| H03 | Degree-one prime reduction | Proved | Higher rational prime powers removed at elementary square-root cost. |
| H04 | Galois-field reduction | Proved | Positive induction and norm-pullback zero inclusion for all unitary characters. |
| H05 | Positive arithmetic kernels | Proved | Exact local unit averaging for every unitary character, including ramified powers; finite-order induction kernels retained. |
| H06 | Rational and abelian base case | Cited | Alpöge's verified result for calibration; for the final independent relative proof use our completed Dirichlet reconstruction, still open. |
| H07F | Finite-order arithmetic estimate | Open | Relative split-prime counts in Galois fields (or absolute split-prime counts). First benchmark: S3. |
| H07I | Infinite-order arithmetic estimate | Open | One-sided split-prime phase sums for each normalized infinite-order character, or a positive combined-family estimate. |
| H08 | Alternative spectral supplier | Open (optional) | Actual compatible geometric trace inequalities; independently prove all necessary external lemmas before making them part of the preferred proof. |

H01 supplies the analytic setup, H02–H05 the written reductions.
The finite-order assertion uses H07F and, for the relative version,
the abelian base case H06. The infinite-order assertion uses H07I.
Together with H04 they imply full Hecke GRH. The absolute version
of H07F does not require H06 as a separate premise. H08 may provide
an alternative sufficient supplier, but is not a prerequisite.

H07F has a concrete first milestone in the [S3 benchmark](../notes/s3-benchmark.md):
the exact cubic-residue/form description and eta-product real-zero
exclusion are proved. The remaining complex-zero problem is still
equivalent to a square-root-scale one-sided prime discrepancy estimate
(in either direction). The [companion selection](../notes/cubic-companion-selection.md)
and [relative scalar comparison](../notes/cubic-relative-comparison.md)
now supply the genuine Dirichlet-style analytic blocks for this
benchmark, with fixed coefficients and actual logarithmic derivatives.
The [coefficient interface](../notes/cubic-coefficient-interface.md)
reduces its proposed prime-to-six Selmer denominator to the parent
abelian term and two equal cubic sectors over a fixed quadratic field.
The original CM host cannot contain the cubic field, so an actual
equivariant local-system realization and quantitative arithmetic
bounds are still missing. Neither H07F nor H07I has been completed.

See the [open frontier](../notes/open-frontier.md) and
[progress](progress.md). The map has nine nodes now, formerly eight;
this is a subdivision of an open node, not a regression or a new
completion. The counts are structural and incomparable with the more
finely resolved Dirichlet map.
