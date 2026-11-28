# Current continuation checkpoint

RH and Dirichlet GRH are **not yet proved by this ordinary reconstruction**.
Read the [shared manuscript](../paper/determinant/body.tex) and
[dependency plan](../blueprint/merged-proof-plan.md). Use modulus 18480
for RH and a fixed multiple of 18480 and the target conductor for
Dirichlet GRH. The immutable readable source is `grh/src/` at
`72fead102f663d5c7a407964a13dc0cf9d977207`.

## The current proof structure

| Construction | Proved suppliers | Exact remaining boundary |
| --- | --- | --- |
| Common theta data | [Finite data](lsernau-common-theta-finite.md), [Weil transport](lsernau-nonstandard-weil-transport.md), [common conjugation](lsernau-common-jet-conjugation.md), [graded unfolding](lsernau-graded-period-unfolding.md), [terminal matching](lsernau-terminal-period-matching.md), [convergent Rallis](lsernau-rallis-sharp-inversion.md). | Full analytic see-saw datum, compatible nonzero volumes, and admissible-scale realization. A raw terminal scalar can vanish. |
| A: actual short chain | [Charged scalar jets](lsernau-charged-jet-estimate.md), [common-chain transport](lsernau-common-chain-transport.md), [norm budget](lsernau-common-chain-norm-budget.md). The jet scale cancels the level denominator; joint invariance gives exact class sums. Actual pointwise norm error is at most `108 f a log b`, within the original `f a(log b)^3`; the indicated terminal class norm costs 109. | Analytic construction of the supplied datum and exceptional-prime arithmetic corrections. Baseline gauge and asymptotic definite-chain norm are closed. |
| A: sharp comparisons | [Six-copy scalar bound](lsernau-sharp-scalar-couplings.md), [actual six-copy transport](lsernau-six-copy-test-transport.md), [false-lift periods](lsernau-rank-one-false-lift-periods.md), [branching](lsernau-branching-normalization.md), [marked Hecke index](lsernau-marked-hecke-index.md), [exceptional middle edge](lsernau-exceptional-middle-edge.md). Blocks `(6,4,4,2z-14)` preserve the original target and vacuum exponent; the sharp Fourier exponent is `6f`. Actual rank-one false-lift orthogonality is proved for `33<2z`. | The common-chain analytic realization and arithmetic budgets remain separate. The rank-one test-form orthogonality supplier is closed. |
| Noncompact edges | [Explicit harmonics](lsernau-noncompact-real-edges.md), [classical representation inputs](lsernau-discrete-series-suppliers.md), [projection lower bound](lsernau-projection-lower-bound.md), [quantitative smoothing](lsernau-quantitative-local-smearing.md). | Whole projected-quotient inverse and the remaining noncompact global cost. Harmonic-line control and finite Fischer-input control are proved. |
| B: returns and finite types | [Quantitative returns](lsernau-quantitative-returns.md), [exact Bessel subgroup](lsernau-bessel-subgroup-moment.md), [equal good multiplicities](lsernau-good-form-multiplicities.md), [direct Bessel transfer](lsernau-bessel-good-type-transfer.md), [weighted lattice count](lsernau-link-lattice-counting.md), [three-quotient frame count](lsernau-corank-frame-fibres.md). Bad mass is at most `2b^(-9)` at each prime and equals the normalized actual source trace. The full weighted near-pair count is proved for the specified cell family. | Gauge-dependent orbit bound, integral link-lattice cut, reduction to the cell family, and terminal-fixer/open-cell moments. The [single-link reduction](lsernau-single-link-energy-frontier.md) then supplies both strips; their identity and good-source deficits are consequences, not extra analytic obligations. |
| C: attachment | [Spherical attachment](lsernau-split-galois-attachment.md), [dominant matching](lsernau-iwahori-dominant-matching.md), [type sorting](lsernau-iwahori-type-sorting.md), [Shintani products](lsernau-shintani-product-types.md), [CM tower assembly](lsernau-tame-local-global-assembly.md). Valid at every rank and coefficient prime, including 2. | Apply on the same actual spaces and preserve integral normalizations; rational occurrence does not imply integral splitting. Older quadratic/odd-rank constructions are alternatives. |
| C: selected values | [Small twists](lsernau-general-small-twist.md), [main-summand data](lsernau-main-summand-data.md), [critical systems](lsernau-critical-value-systems.md), [stable-range critical norms](lsernau-normalized-transfer-critical-norm.md), [integral kernels](lsernau-integral-critical-kernels.md). At rank two, [arithmetic](lsernau-rank-two-period-arithmetic.md) and [analytic period](lsernau-rank-two-period-norm.md) now supply the measure, Euler law, fully ramified norm and nonzero base case. | Their common-chain application and the remaining arithmetic denominator budget. The rank-two analytic endpoint is closed; imprimitive Euler factors can still vanish. |
| C: integral operators | [Separators](lsernau-integral-separators.md), [tied rows](lsernau-tied-row-construction.md), [local derivatives](lsernau-local-tied-derivatives.md), [integral extraction](lsernau-tied-integral-extraction.md), [triangle detection](lsernau-triangle-detection.md), [Kummer](lsernau-kummer-relations.md), [root selectors](lsernau-root-chain-selectors.md). Hyperplane avoidance combines detected operators without added valuation loss. | Simultaneous numerical Selmer, detection, crystalline and extraction bounds. A generic spectral projector requires its own congruence-module cost. |
| C: crystalline loss | [Fontaine–Laffaille zero range](lsernau-fontaine-laffaille-zero-defect.md), [fixed-family Smith](lsernau-fixed-relation-smith-bounds.md), [inertia algebra](lsernau-uniform-inertia-relations.md), [full bounded class](lsernau-bounded-class-crystalline-loss.md). [Exact cyclotomic loss and aggregate budget](lsernau-exact-cyclotomic-loss-and-budget.md) computes a linear lower bound and an explicit sparse cyclotomic-inertia upper bound. | The actual growing-field nonabelian family needs an effective aggregate bound. Fixed-data uniformity in family size and precision is proved; Hodge weights alone do not imply cyclotomic inertia. |
| Final determinant and zero criterion | [One-lift comparison](lsernau-one-lift-comparison.md), [signed determinant](lsernau-mathematical-extraction-2026-11-26.md), [prime reduction](lsernau-moment-and-prime-reductions.md), [zero detection](lsernau-zero-detection.md). | Construct the common integral objects, complement basis and signed budget at the same scales. Preserve actual rank and the signed missing-rank term. |

## Structural cuts to preserve

1. Use one finite chain transport, followed by its proved norm budget.
   The Gram-matrix/intermediate-module class count replaces quantitative
   adelic approximation. Do not reopen that norm supplier.
2. Use six sharp copies directly in the four-block comparison. Its
   false-lift proof uses two finite orbits, first occurrence and one
   small Hecke inverse, followed by Fourier detection of the block
   period. The twelve-copy [alternative](lsernau-sharp-global-extraction.md)
   and quantitative hyperbolic-plane recursion are not prerequisites.
3. Use the induced Bessel measure and mirabolic generic representation
   for good-type trace. Conjugacy-averaged local character integrals are
   no longer prerequisites of this step; other local-density consumers
   retain their own hypotheses.
4. Use the weighted lattice mean and three finite frame quotients for
   pair counting. Congruence and torsion-index cancellation reduce the
   geometric gain and its range to one integral cut; both restricted
   moments then share the same three remaining geometric inputs.
5. Use equal-rank constancy, anisotropic Siegel–Weil and explicit local
   integrals for the rank-two period. Three complementary theta exchanges
   are not required for this endpoint.
6. Prove the single weighted aggregate projection inequality in
   [the budget chapter, §4](lsernau-exact-cyclotomic-loss-and-budget.md#4-the-aggregate-projection-budget-is-the-needed-input).
   A separate original-sized bound at every prime/eigenform/critical pair
   is stronger than necessary. Include every actual cost in the sum.

## Immediate priorities

1. Complete the analytic common-chain see-saw, compatible nonzero
   volumes, higher-rank gluing periods and exceptional corrections.
2. Prove the remaining gauge orbit, integral link-lattice cut and zero-term inputs of
   [single-link reduction](lsernau-single-link-energy-frontier.md).
   The weighted lattice average, frame-fibre count, moment summation
   and numerical comparisons are now proved. The
   [congruence and torsion-index gain](lsernau-link-gain-index.md)
   leaves the precise cut (15); its range bounds then follow.
   Terminal-fixer and open-cell bounds remain on the same analytic data.
3. Bound the actual growing-field aggregate projection cost, preserving
   sparse labelled weights and Frobenius structure. Qualitative finiteness
   and parameter reordering alone do not pay it.
4. Complete the complement basis and apply the signed determinant
   inequality and proved analytic criterion on one common admissible datum.

## Verification and resumption

The [verification index](../certificates/README.md) records pinned source
bytes, exact finite computation and internal proof review separately.
New checkers cover common-chain expansion/Gram and norm exponents,
Bessel induction and rational weights, rank-two Cartan/Fock identities,
weighted lattice and integral frame formulas, rank-one finite orbits,
and exact cyclotomic coinvariants and sparse certificates. These checks
supplement the proofs and primary classical references; they do not
prove the analytic theorems by numerical testing or replay Lean.

The decisive norm-counting, Bessel, rank-two and cyclotomic arguments
received independent internal mathematical checks. No external review,
explicit computation for the actual growing Galois family, or fresh
full Lean replay is claimed. Current PDF build and visual-review details
are in the [manuscript index](../paper/README.md).

Use the [recovery index](recovery-crosswalk.md),
[source atlas](../blueprint/lean-source-atlas.md),
[formal audit](../audit/lsernau-formal-audit-2026-11-26.md) and
[attribution](../sources/README.md) for earlier work and evidence.
Read the independent [Hecke checkpoint](../hecke/notes/current-state.md)
before changing that track; its cubic datum, critical formulas,
exceptional primes and infinite-order phases remain separate.

Legacy whole-node counts: RH **6/9**, Dirichlet **18/31**, Hecke **6/9**.
No whole historical node is closed by these supplier advances.
