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
The [general finite-order companion theorem](../notes/general-finite-order-companions.md)
extends the analytic supplier beyond the cubic case.
The [2-primary theorem](../notes/cubic-two-primary-window.md)
supplies the full moving cubic host's common-window Selmer bound;
the [exceptional-prime comparison](../notes/cubic-exceptional-prime-comparison.md)
supplies the additional integral splitting error at 3, but not
its twisted lengths. The
[good-prime comparison](../notes/cubic-good-prime-comparison.md)
removes higher powers and ramified primes from the required
arithmetic supplier and permits a simpler top-set bias.
The [cubic torsor](../notes/cubic-torsor-realization.md) realizes
the local Frobenius and normalized orbit theta data on the retained
CM host. The global label-sensitive maps, their quantitative
bounds and new odd-prime Selmer estimates are still missing.
The [one-sign polynomial companion](../notes/polynomial-one-sign-companion.md)
removes QRH from a replacement analytic block, and the
[high-dyadic 3-primary theorem](../notes/cubic-three-primary-vanishing.md)
closes the indicated integral character sectors, not the whole
odd-prime budget.

An independent finite-order construction uses
[global interpolation](../notes/global-interpolation-lattices.md)
and [linear-size derivative lattices](../notes/global-derivative-lattices.md).
The actual global index equals the integrated Chebyshev count
up to O_E(n^(3/2)); the added integral sampling gives stable
archimedean metrics with negligible determinant penalty.
The quantitative relative saturated-covolume lower bound in
the [frontier](../notes/open-frontier.md) is still open.
It would avoid all CM, Selmer and separate abelian inputs
for the finite-order assertion. The geometry route is retained.

Neither H07F nor H07I has been completed.

See the [open frontier](../notes/open-frontier.md) and
[progress](progress.md). The map has nine nodes now, formerly eight;
this is a subdivision of an open node, not a regression or a new
completion. The counts are structural and incomparable with the more
finely resolved Dirichlet map.
