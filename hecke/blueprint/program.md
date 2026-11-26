# Hecke GRH proof program

**Preferred new attack (26 November 2026):** follow the
[Sernau selected-twist transfer plan](../notes/lsernau-transfer-plan-2026-11-26.md)
for the cubic benchmark. The zero structural-defect lemma is proved over
CM fields with the stated local and coprime-order hypotheses, including
all cubic coefficient primes at least 5 and all permitted dyadic levels.
The degree-independent specialization is also proved; small twisted lengths and their global
determinant-ratio realization remain separate tasks. The older suppliers
below retain their stated scope, and the Hecke count remains 6/9.

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
CM host. The [actual equivariant differential maps](../notes/cubic-differential-theta-maps.md)
give Frobenius-sensitive integral divisibilities, an exact
simultaneous index and canonical metric bounds. The
[theta coefficient isomorphism](../notes/cubic-theta-coefficient-interface.md)
realizes the full torsor and correct-order simultaneous operators.
A collective centered degree/norm estimate remains missing.
The [fixed-conductor window](../notes/cubic-fixed-conductor-selmer-window.md)
controls all fixed-odd-conductor cubic sectors at 3 and the
one-sign moving 2-primary groups jointly. The
[polarized rank-three model](../notes/cubic-polarized-selmer-model.md)
and [frame count](../notes/cubic-frame-cohomology.md)
supply actual integral conormal injection, local dimensions,
diagonal rigidity and conditional polynomial spectrum.
The automorphy/rigidity-based length comparison and remaining
moving sectors are open.
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

The [all-order formal operator lattice](../notes/cubic-formal-operator-lattices.md) identifies integral theta maps with polynomials integer-valued on actual cubic p-adic lines. The [symbol-derivative index](../notes/cubic-symbol-derivative-lattices.md) recovers the truncated prime discrepancy with normalized error O(sqrt(X) log X), without a zeta multiplier. Collective degree/norm saving or normalized period coupling remains open.
The [marked point theorem](../notes/cubic-point-shapes-and-rigidity.md) classifies the two-sided points in either characteristic and proves the obstruction to the standard rank-one tensor Euler-system hypothesis. The latest [corner elimination](../notes/cubic-corner-elimination.md) removes the outer-block points in the high-dyadic range; [actual relation count and curve criterion](../notes/cubic-high-dyadic-presentation.md) reduce its conditional length estimate to irreducible point arithmetic. The [Eisenstein-field alternative](../notes/cubic-eisenstein-euler-systems.md) restores rational rank-one image but requires a genuine Euler system and rank-two singular regulator in the remaining cross-block cases. The curve exclusion, attachment, remaining low-dyadic and moving lengths are open.
The [3-primary local defect theorem](../notes/cubic-three-primary-local-defects.md) bounds normalized lifting losses by one, controls aggregate residual generator ranks and proves untwisted cubic vanishing at 3. Moving low-dyadic lengths and resonant odd-prime lengths are open.
The [unconditional two-prime theorem](../../notes/unconditional-quadratic-selection.md) supplies the original two-sign numerical block with all congruences and exponential thin bound, without QRH; both parent manuscript sources and the partial common-window assembly now implement it.

The new [full connected monodromy theorem](../notes/cubic-irreducible-monodromy.md) excludes imprimitive and orthogonal-type irreducible points in both characteristics: every remaining high-dyadic irreducible point has connected group SL3. The [trace and adjoint comparison](../notes/cubic-trace-and-adjoint.md) identifies the entire integral invariant ring with the closed trace algebra, and proves finite local conditions for actual dual-number tangents. Genuine cuspidal attachment therefore implies normalized tangent rigidity by Thorne's theorem, without a separate Euler-system premise. The [automorphic seed audit](../notes/cubic-automorphic-seed-frontier.md) constructs an ordinary 2+1 isobaric starting datum from the parent rank-two seed (for coefficient primes prime to the host conductor). It is not the required cuspidal GL3 seed. The symmetric-square route fails even after CM restriction preserving distinct residual constituents; the checked level-raising and reducible lifting theorems do not directly apply. The parent auxiliary class-rank argument also needs a new bound on the nontrivial cubic components over the nonabelian residual splitting field.

The [pure-cubic descent](../notes/pure-cubic-selmer-descent.md) identifies each cubic strict Selmer sector with the extra direct summand over $C=\mathbb Q(\sqrt[3]2)$ of the rational-twist strict group, exactly away from 3 and up to an explicit polynomial isogeny error at 3. The field $C$ has class number one. For 3-cycle coefficient primes and inert cyclic host fields satisfying the stated class-number test, the entire sector vanishes at weights divisible by $\ell-1$. The [finite class-rank certificate](../notes/cubic-finite-class-rank-certificates.md) gives exact cubic coinvariant control at inert primes, and $g_{\lambda,n}+s_\lambda<\ell^n$ certifies a bounded generator rank for the actual fixed auxiliary tower. A zero initial cubic component at inert primes suffices for integral vanishing at every twist weight. The [two-negative-weight elimination and specialization](../notes/cubic-two-negative-weight-elimination.md) prove that when this residual adjacent vanishing accompanies the already proved corner vanishing, the full invariant ring is $\mathcal O$ and both irreducible-point premises hold vacuously. The exact inert specialization also supplies a common-window bound for a fixed finite list of successful finite-rank certificates. None of these tests has been proved to succeed uniformly for the moving data.

The [characterwise strict-control theorem](../notes/cubic-characterwise-strict-control.md) gives exact specialization for all coefficient-prime splitting types and a finite rank certificate with correction s_theta<=2, counting only the coefficient-prime places of F on which the actual finite adjacent character is trivial. The existing high-dyadic separator makes s_theta=0 even at cubic-split primes; the zero initial class-rank test is then equivalent to vanishing of the actual integral adjacent group, simultaneously for weights in its tame residue class. Eventual success of the rank test for each fixed datum is equivalent to mu=0 for its actual cubic character component. Neither the nonabelian mu assertions nor the moving uniform rank/length estimate are proved.

The [five actual class-number certificates](../notes/pure-cubic-class-certificates.md) prove h(Q(cuberoot(2),sqrt(-q))) divides 18,54,108,288,1620 for q=7,11,19,23,43 respectively, by 368 exact principal relations. At 3-cycle coefficient primes they imply integral cubic vanishing for weights divisible by ell-1, with no inertness restriction on the quadratic factor. These are fixed quadratic sectors, not high-dyadic moving-window certificates. The [explicit exceptional nonvanishing example](../notes/cubic-three-primary-nonvanishing-example.md) proves that at q=139 the quadratic cubic-twist sector at coefficient prime 3 is nonzero at every positive twist weight. Uniform zero across the full admissible host family is false; a finite-rank or upper-length bound is not contradicted.

Neither H07F nor H07I has been completed.

See the [open frontier](../notes/open-frontier.md) and
[progress](progress.md). The map has nine nodes now, formerly eight;
this is a subdivision of an open node, not a regression or a new
completion. The counts are structural and incomparable with the more
finely resolved Dirichlet map.
