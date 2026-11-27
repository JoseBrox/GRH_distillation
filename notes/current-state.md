# Current continuation checkpoint

RH and Dirichlet GRH are **not yet proved by this ordinary reconstruction**.
Read the [active common manuscript](../paper/determinant/body.tex) and
[authoritative dependency plan](../blueprint/merged-proof-plan.md).
For RH first fix modulus 18480; for Dirichlet allow any fixed multiple
of the target conductor and 18480. Source revision throughout:
`72fead102f663d5c7a407964a13dc0cf9d977207`, readable `grh/src/` tree.

## Mathematical dependencies

| Part | Established suppliers and exact remaining boundary |
| --- | --- |
| Analytic endpoint | [Zero detection](lsernau-zero-detection.md) and [prime reduction](lsernau-moment-and-prime-reductions.md) prove the final implication from the stated arithmetic remainder, including quadratic-twist selection and the one-sided Landau argument. |
| Common finite theta data | [Finite theta](lsernau-common-theta-finite.md), [graded unfolding](lsernau-graded-period-unfolding.md), [terminal matching](lsernau-terminal-period-matching.md), [convergent Rallis and sharp data](lsernau-rallis-sharp-inversion.md) and [real grid parameters](lsernau-real-grid-parameters.md) supply the finite classes, exact period reductions, stable-range Gram identity under classical Siegel–Weil, definite real edges, finite vacuum inverse, and actual grid block rules. Full-chain see-saw, compatible nonzero volumes and quantitative kernel/projection control remain. |
| Noncompact real edges | [Explicit harmonics and smoothing](lsernau-noncompact-real-edges.md) proves the product of minors, matching weights, uniqueness, Fischer saturation, centred Casimir comparison and compact reproducing bump. Positive nonzero projection and exact compact-support smearing are proved **conditional on the stated positive polar, root-cone and large-gap rigidity package**. The full noncompact `IsEdge` supplier is not marked complete. |
| A — short integral forms | The [scalar CM](lsernau-cm-theta-normal-form.md), [charged jet](lsernau-charged-jet-estimate.md), [Weil normalization](lsernau-weil-normalization.md), [marked chain](lsernau-marked-chain-charges.md), [split transfer](lsernau-split-transfer-and-level-lifts.md), [exceptional geometry](lsernau-exceptional-polynomial-geometry.md), [middle edge](lsernau-exceptional-middle-edge.md), [bounded branching](lsernau-branching-normalization.md), [marked Hecke index](lsernau-marked-hecke-index.md), [nonstandard transport](lsernau-nonstandard-weil-transport.md) and [common jet](lsernau-common-jet-conjugation.md) chapters supply their stated algebraic and local norm estimates. Remaining: arithmetic sharp lower tests, common-kernel gauge and chain squared-norm assembly. |
| B — returns and spanning | [Bessel majorants](lsernau-bessel-majorants.md), [stationary period](lsernau-stationary-bessel.md), [finite support/cuts](lsernau-support-to-cut.md) and [quantitative returns](lsernau-quantitative-returns.md) give the derivative/Schur bound, exact Gram coarea, local exponent 268n², integral frame separation, free-level weighted packing, absolute Poincare convergence and source truncation bound under the explicit coefficient and bounded-reduction hypotheses. [Global cuts](lsernau-global-cut-unfolding.md) now have the required absolute convergence. [Positive-type closure](lsernau-positive-type-moment.md) and [dimension/compression](lsernau-common-moment-interface.md) remain conditional on the actual identity, terminal-fixer, open-cell and other second-moment estimates and good-form multiplicities. |
| C — spherical attachment | [Split attachment](lsernau-split-galois-attachment.md) supplies the classical spherical Galois representation at every coefficient prime, including 2, with conjugate-Weyl weights, geometric Frobenius and crystalline period actions checked. It uses Labesse and the explicit cuspidal-factor construction with Chenevier–Harris. [Protected steps](lsernau-protected-quadratic-steps.md), [odd-rank patching](lsernau-odd-rank-patching.md) and [two-string cancellation](lsernau-galois-two-string.md) provide the field and representation reductions. |
| C — labelled local compatibility | [Trace transfer](lsernau-base-change-trace-transfer.md), [norm roots](lsernau-global-norm-roots.md), [specific Hecke transfer](lsernau-specific-hecke-transfer.md) and [finite Shintani labels](lsernau-shintani-label-transfer.md) supply their stated automorphic transfers. The split attachment chapter now proves unramified sorted Iwahori extraction, pro-Iwahori Hilbert 90, descent index k times the joint unit-character image, and the finite noncommutative all-powers-to-inertia lemma. Remaining: actual dominant Iwahori double-coset matching, finite-product-type sorted extraction and compatible tower instantiation. |
| C — selected twists | [Small twists](lsernau-general-small-twist.md), [main-summand data](lsernau-main-summand-data.md) and [critical-value systems](lsernau-critical-value-systems.md) prove their constructions under the displayed attached local types, scaled-kernel and period inputs. The exact inverse-ratio height is below 5 per critical pair. Those concrete inputs remain required. |
| C — lengths and individual operators | [Integral separators](lsernau-integral-separators.md) proves finite local Tate-duality counts, the Smith-lattice lift of relation-respecting cocycles, the local defect-to-colength inequality and the global tied-length bound, also for divisible coefficients. Combined with [Ribet algebra](lsernau-ribet-polynomial.md), [tied rows](lsernau-tied-row-construction.md), [local derivatives](lsernau-local-tied-derivatives.md), [integral extraction](lsernau-tied-integral-extraction.md), [triangle detection](lsernau-triangle-detection.md), [Kummer relations](lsernau-kummer-relations.md) and [root-chain selectors](lsernau-root-chain-selectors.md), this constructs individual detected integral operators under the **numerical crystalline-defect and remaining labelled/local hypotheses**. Hyperplane avoidance assembles them without extra valuation loss. A strict spectral projector instead pays the largest Smith exponent of its congruence module. [Fontaine–Laffaille zero defect](lsernau-fontaine-laffaille-zero-defect.md) now proves vanishing for the unramified crystalline aligned-window range, including all p∤M with λ_p=0 and the stronger threshold p≥b+δ+W+η+2. |
| Final comparison | [One-lift comparison](lsernau-one-lift-comparison.md) and the [signed determinant inequality](lsernau-mathematical-extraction-2026-11-26.md) are proved under their stated common-lattice inputs. Apply at one common family of scales and divide by the actual positive rank and prime-sum normalizer. |

## Immediate priorities

1. Supply the normalized noncompact discrete-series positive polar and
   rigidity/root-cone package; apply the proved Fock and exact smoothing
   argument, and quantify the inverse projection on the actual real edges.
2. Finish the actual dominant Iwahori matching and finite-product-type
   sorted extraction. Combine these with the proved spherical attachment,
   tame index descent and finite all-powers lemma in the permitted global towers.
3. Prove the remaining positive numerical crystalline defect estimate
   below the Fontaine–Laffaille threshold and at the tame level primes.
   The zero-loss branch, the defect-to-length comparison and the
   conditional individual denominator operators are now written.
4. Use the quantitative return theorem to establish the actual identity,
   terminal-fixer, open-cell and remaining second moments and multiplicities;
   finish full-chain see-saw, sharp lower tests, gauge/norm assembly and
   the determinant complement construction on the same data.

## Verification and resumption

The exact-arithmetic [Fock script](../scripts/check_noncompact_fock_bridge.py)
was rerun successfully: 68 Casimir identities and 2,064 row/column
commutations; a rank-(2,3) noncompact example satisfies the full large
source gap; the rank-(4,4) determinant example tests only the formulas.
See its [certificate](../certificates/noncompact-fock-bridge.json).
No analytic projection, completion or infinite theorem is certified by
those finite checks. The quantitative restriction and coarea constants
were independently audited and the convolution conventions fixed.

The [recovery index](recovery-crosswalk.md),
[source atlas](../blueprint/lean-source-atlas.md),
[formal audit](../audit/lsernau-formal-audit-2026-11-26.md) and
[attribution](../sources/README.md) separate external formal verification,
our partial local build, source-byte checks and ordinary mathematical proofs.
No fresh Lean replay or external mathematical review is asserted.
The current RH and GRH PDFs were rebuilt (12 pages each), as was the
one-page guide, with stabilized references and no overfull boxes. Revised
sections and both target title pages were visually inspected; see the
[build records](../paper/README.md). Compilation is not proof verification.

## Independent Hecke track and retained alternatives

Read the [Hecke checkpoint](../hecke/notes/current-state.md) and
[Hecke manuscript](../hecke/paper/main.md) before changing that track.
Its cubic datum realization, critical-value formulas, common theta
comparison, exceptional primes and infinite-order phases remain separate.
The [historical archive](../paper/archive/README.md) and
[pre-reorganization checkpoint](https://github.com/JoseBrox/GRH_distillation/blob/6b74526223ae1724fa7872c27664b6a565f15244/notes/current-state.md)
preserve prior work without adding superseded prerequisites.

Legacy proof-map counts: RH **6/9**, Dirichlet **18/31**, Hecke **6/9**.
No whole legacy node is closed by these supplier advances.
