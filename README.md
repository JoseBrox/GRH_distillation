# Distilling the Riemann hypotheses

We seek the shortest rigorous conventional proof we can obtain of ordinary RH and Dirichlet GRH, followed by an extension to general Hecke GRH. The source is the argument of **Levent Alpöge with Claude** and the [Sernau–Anthropic reconstruction](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207). Our ordinary reconstruction is **incomplete**. [Sources and attribution](sources/README.md) distinguish the original argument, our new proofs and the retained inputs.

## Read the mathematics

| Manuscript | Scope |
| --- | --- |
| [Ordinary RH](paper/rh/main.pdf) ([TeX](paper/rh/main.tex)) | Conductor-one target; admissible fixed modulus 18480. |
| [Dirichlet GRH](paper/grh/main.pdf) ([TeX](paper/grh/main.tex)) | Every fixed target modulus, including imprimitive characters. |
| [Shared mathematical body](paper/determinant/body.tex) | One dependency-ordered argument, with each open supplier identified. |
| [Reading guide](paper/guide/main.pdf) | The determinant idea in one page. |
| [Hecke GRH](hecke/paper/main.md) | Separate number-field extension and nonabelian cubic benchmark. |

The [proof plan](blueprint/merged-proof-plan.md) specifies the mathematical acceptance tests. The [checkpoint](notes/current-state.md) is a short resumption index; [build instructions](paper/README.md), the [source atlas](blueprint/lean-source-atlas.md) and [verification index](certificates/README.md) provide supporting navigation. Earlier presentations remain in the [archive](paper/archive/README.md).

## One argument, three constructions

A nonzero algebraic determinant satisfies the product formula. Arithmetic divisibility gives short integral theta images. A moment estimate must supply enough independent images. Selected twists then give the opposite bound for the same corrected determinant. Its signed main terms cancel, leaving a prime-sum estimate from which the zero theorem follows. The [finite determinant comparison](notes/lsernau-mathematical-extraction-2026-11-26.md) and [analytic implication](notes/lsernau-zero-detection.md) are proved under their stated construction hypotheses.

### A. Construct the short forms once

The [common finite theta data](notes/lsernau-common-theta-finite.md), [CM normal form](notes/lsernau-cm-theta-normal-form.md), [charged jets](notes/lsernau-charged-jet-estimate.md) and [common conjugation law](notes/lsernau-common-jet-conjugation.md) supply the scalar kernels and their actual arithmetic normalization. The [common-chain transport theorem](notes/lsernau-common-chain-transport.md) carries them through the genuine adjacent-rank chain in one calculation: the charged jet scale cancels its level denominator, vacuum projection preserves joint level invariance, and the finite class sums introduce no stabilizer denominators. It proves the baseline integral gauge and transports the marked-prime gain. The [norm-budget theorem](notes/lsernau-common-chain-norm-budget.md) closes the actual all-conjugate norm estimate with error `108 f a log b`, stronger than the required `f a(log b)^3`. Its short Gram-matrix class count removes the quantitative adelic-approximation supplier.

The [scalar sharpness theorem](notes/lsernau-sharp-scalar-couplings.md) needs six copies. The [six-copy comparison theorem](notes/lsernau-six-copy-test-transport.md) inserts those six directly into the four-block test on the same target, with integral monomial contraction, exact vacuum cancellation and finite class sums. The sharp Fourier factor is halved, from exponent `12f` to `6f`. The [rank-one false-lift theorem](notes/lsernau-rank-one-false-lift-periods.md) now proves its orthogonality: two finite orbits give bottom vanishing, first occurrence and a small Hecke inverse kill the tower, and Fourier separation detects the required block period. This replaces the quantitative hyperbolic-plane recursion.

The [exceptional edge estimates](notes/lsernau-exceptional-middle-edge.md), [terminal branching](notes/lsernau-branching-normalization.md) and [marked Hecke index](notes/lsernau-marked-hecke-index.md) supply their local integral and index bounds. The [graded unfolding](notes/lsernau-graded-period-unfolding.md), [terminal matching](notes/lsernau-terminal-period-matching.md) and [convergent Rallis identity](notes/lsernau-rallis-sharp-inversion.md) supply individual analytic comparisons. For noncompact edges, [classical representation suppliers](notes/lsernau-discrete-series-suppliers.md), [projection lower bounds](notes/lsernau-projection-lower-bound.md) and [quantitative smoothing](notes/lsernau-quantitative-local-smearing.md) prove the local constructions. Full-chain see-saw, compatible nonzero volumes, exceptional corrections and the remaining noncompact global cost are not supplied merely by the finite chain calculation.

### B. Prove that enough short forms are independent

The [return theorem](notes/lsernau-quantitative-returns.md) supplies absolute convergence and quantitative truncation. The [Bessel-subgroup identity](notes/lsernau-bessel-subgroup-moment.md) gives its exact main contribution. The [two-place multiplicity theorem](notes/lsernau-good-form-multiplicities.md) identifies the actual good Hecke modules on the two equal-rank spaces, using the specified split cuspidal types and Harris–Labesse.

A shorter finite argument now handles the unwanted types. [Direct Bessel good-type transfer](notes/lsernau-bessel-good-type-transfer.md) combines a hook-unipotent induction identity with the mirabolic generic representation. Together with the [exact finite counts](notes/lsernau-finite-good-type-density.md), it gives bad-type mass at most `2b^(-9)` at each chosen prime and the exact corresponding source trace. This removes the conjugacy-averaged local integral estimate from that step.

The [weighted lattice theorem](notes/lsernau-link-lattice-counting.md) and [three-quotient frame proof](notes/lsernau-corank-frame-fibres.md) close the full weighted near-pair count, retaining its essential `N^(-kf)` gain. The [link-gain proof](notes/lsernau-link-gain-index.md) supplies the congruence and torsion-index cancellations. The [single-link reduction](notes/lsernau-single-link-energy-frontier.md) then supplies both restricted moments under three explicit remaining inputs: the integral link-lattice cut, its gauge-specific orbit bound, and zero-term reduction. Their summation and scale comparisons are proved.

The same chapter proves that the two restricted-group second moments imply both the identity estimate and a mean positive source deficit at most `4b^(-6)`. Thus those two conclusions are no longer independent analytic obligations. The restricted moments themselves, the terminal-fixer and open-cell estimates, and their remaining analytic terms are still open. [Positive-type closure](notes/lsernau-positive-type-moment.md) and the [common moment interface](notes/lsernau-common-moment-interface.md) specify how those estimates produce rank.

### C. Bound the selected-twist determinant

[Spherical attachment](notes/lsernau-split-galois-attachment.md) gives the actual Galois representations at every rank and coefficient prime, including 2. [Dominant matching](notes/lsernau-iwahori-dominant-matching.md), [finite-type sorting](notes/lsernau-iwahori-type-sorting.md), [Shintani products](notes/lsernau-shintani-product-types.md) and [CM tower assembly](notes/lsernau-tame-local-global-assembly.md) supply their labelled local compatibility. The older quadratic and odd-rank attachment constructions remain alternatives.

The [small-twist theorem](notes/lsernau-general-small-twist.md) uses the [main-summand Selmer data](notes/lsernau-main-summand-data.md) and [critical-value systems](notes/lsernau-critical-value-systems.md). [Normalized transfer and critical norms](notes/lsernau-normalized-transfer-critical-norm.md) and [integral critical kernels](notes/lsernau-integral-critical-kernels.md) supply the stable-range formulas. At rank two the [arithmetic period theorem](notes/lsernau-rank-two-period-arithmetic.md) gives the integral measure and exact Euler relation. The [analytic period theorem](notes/lsernau-rank-two-period-norm.md) now closes the fully ramified identity and nonzero base case: a constant equal-rank theta lift, anisotropic Siegel–Weil and explicit local integrals replace three complementary theta exchanges.

The [integral separator](notes/lsernau-integral-separators.md), [tied-row](notes/lsernau-tied-row-construction.md), [triangle detection](notes/lsernau-triangle-detection.md), [Kummer](notes/lsernau-kummer-relations.md) and [root selector](notes/lsernau-root-chain-selectors.md) arguments construct detected operators under the stated arithmetic bounds. [Fontaine–Laffaille](notes/lsernau-fontaine-laffaille-zero-defect.md) proves the large-prime zero-loss branch. [Smith bounds](notes/lsernau-fixed-relation-smith-bounds.md), [inertia relations](notes/lsernau-uniform-inertia-relations.md) and the [bounded-class theorem](notes/lsernau-bounded-class-crystalline-loss.md) supply progressively stronger fixed-data finiteness, including uniformity over auxiliary ranks and precision.

The [exact cyclotomic calculation and aggregate budget](notes/lsernau-exact-cyclotomic-loss-and-budget.md) sharpen the remaining task. They compute a genuine crystalline loss exactly, prove that a bound retaining only weight-interval width must grow at least linearly, and give an effective all-prime bound for the restricted case of sparse cyclotomic inertia. They also show that the determinant needs only **one weighted aggregate projection cost**, rather than a source-sized estimate for every individual projection. The actual growing-field, nonabelian family still needs that effective bound, with all Selmer and detection costs included.

## What remains decisive

1. Finish the analytic common-chain comparison, compatible nonzero volumes and higher-rank gluing periods.
2. Prove the restricted, terminal-fixer and open-cell moment estimates on those same data.
3. Establish the growing-field aggregate arithmetic budget, including Selmer, detection and extraction costs.
4. Assemble the complement basis and signed determinant inequality at one common admissible scale, then apply the proved zero criterion.

The [formal audit](audit/lsernau-formal-audit-2026-11-26.md) records the external formal evidence. Our source-byte checks, exact finite computations, classical-reference checks and ordinary proofs are distinct forms of verification; no fresh full Lean replay is claimed. Historical whole-node counts remain RH **6/9**, Dirichlet **18/31**, Hecke **6/9**. They are interface counts, not percentages of completion.
