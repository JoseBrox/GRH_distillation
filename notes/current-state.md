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
| Common finite theta data | [Finite theta](lsernau-common-theta-finite.md), [graded unfolding](lsernau-graded-period-unfolding.md), [terminal matching](lsernau-terminal-period-matching.md), [convergent Rallis and sharp data](lsernau-rallis-sharp-inversion.md) and [real grid parameters](lsernau-real-grid-parameters.md) supply their finite classes, exact period reductions, stable-range Gram identity under classical Siegel–Weil, definite real edges, finite vacuum inverse and actual grid block rules. Full-chain see-saw, compatible nonzero volumes and quantitative global norm assembly remain. |
| Noncompact local representations | [Explicit harmonics](lsernau-noncompact-real-edges.md) proves the product of minors, weights, uniqueness, Fischer saturation and centred Casimir comparison. [Classical discrete-series suppliers](lsernau-discrete-series-suppliers.md) supplies the normalized positive polar formula, root-cone support and positive-form rigidity, using Sun, Vogan–Zuckerman and the Dirac inequality with checked hypotheses. Nonzero projection and exact compact-support smearing therefore hold for the actual local representations. |
| Quantitative local control | [Projection lower bound](lsernau-projection-lower-bound.md) gives squared norm ratio at least (48T)^(-2r²)/(4 dim τ), with T=D+rm+2r(L+r+1)+1. [Quantitative local smearing](lsernau-quantitative-local-smearing.md) gives a linear map on every finite degree range with common compact support, explicit differential order, Cramer denominators and weighted smooth seminorms. It measures the original Fischer norm; the full projected-quotient inverse and compatibility of its large costs with the global budget remain. |
| A — short integral forms | The [scalar CM](lsernau-cm-theta-normal-form.md), [charged jet](lsernau-charged-jet-estimate.md), [Weil normalization](lsernau-weil-normalization.md), [marked chain](lsernau-marked-chain-charges.md), [split transfer](lsernau-split-transfer-and-level-lifts.md), [exceptional geometry](lsernau-exceptional-polynomial-geometry.md), [middle edge](lsernau-exceptional-middle-edge.md), [bounded branching](lsernau-branching-normalization.md), [marked Hecke index](lsernau-marked-hecke-index.md), [nonstandard transport](lsernau-nonstandard-weil-transport.md) and [common jet](lsernau-common-jet-conjugation.md) chapters supply their stated algebraic and local norm estimates. Remaining: arithmetic sharp lower tests, common-kernel gauge and chain squared-norm assembly. |
| B — returns and spanning | [Bessel majorants](lsernau-bessel-majorants.md), [stationary period](lsernau-stationary-bessel.md), [finite support/cuts](lsernau-support-to-cut.md) and [quantitative returns](lsernau-quantitative-returns.md) give the derivative/Schur bound, exact Gram coarea, local exponent 268n², integral frame separation, free-level weighted packing, absolute Poincare convergence and source truncation bound under the explicit coefficient and bounded-reduction hypotheses. [Global cuts](lsernau-global-cut-unfolding.md) have the required absolute convergence. [Positive-type closure](lsernau-positive-type-moment.md) and [dimension/compression](lsernau-common-moment-interface.md) remain conditional on the actual identity, terminal-fixer, open-cell and other second moments and good-form multiplicities. |
| C — spherical attachment | [Split attachment](lsernau-split-galois-attachment.md) supplies the classical spherical Galois representation at every positive rank and coefficient prime, including 2, on the source's actual Weil-data fields. Labesse, the explicit cuspidal-factor construction and Chenevier–Harris give the normalized unramified, crystalline and labelled Hodge clauses. The older protected quadratic, odd-rank and two-string route is an alternative, not a prerequisite. |
| C — labelled local compatibility | [Dominant matching](lsernau-iwahori-dominant-matching.md), [finite-type sorting](lsernau-iwahori-type-sorting.md), [full Shintani products](lsernau-shintani-product-types.md) and [prime CM assembly](lsernau-tame-local-global-assembly.md) complete the selected sorted-Iwahori and labelled polynomial assertions, including repeated determinant labels, finite inertia and potential crystallinity. The CM steps preserve Weil data and trace-one integers, and restriction to the common kernel transports actual period operators. A positive Weil element of degree k needs tower degree exactly k times the joint unit-character image, at most k(q−1). The finite all-powers lemma avoids an infinite tower. |
| C — selected twists | [Small twists](lsernau-general-small-twist.md), [main-summand data](lsernau-main-summand-data.md) and [critical-value systems](lsernau-critical-value-systems.md) prove their constructions under the displayed inputs. [Normalized transfer and critical norms](lsernau-normalized-transfer-critical-norm.md) supplies the full normalized rational representation identity on occurring comparison eigensystems, exact rectangular sharp mass, common finite Hecke Rallis operator, and the stable-range critical norm for z≥2. The actual good-form occurrence and multiplicities, scaled-kernel integrality and rank-two period at z=1 remain. The exact inverse-ratio height is below 5 per critical pair. |
| C — arithmetic lengths | [Integral separators](lsernau-integral-separators.md) proves finite local duality counts, the relation-cocycle lift, defect-to-colength comparison and global tied-length bound, including divisible coefficients. [Fontaine–Laffaille zero defect](lsernau-fontaine-laffaille-zero-defect.md) gives vanishing for the unramified aligned-window range, including every p∤M with λ_p=0 and the stronger threshold p≥b+δ+W+η+2. The source-uniform positive-loss and tame level-prime bounds remain open. |
| C — fixed-family costs and individual operators | [Fixed-relation Smith bounds](lsernau-fixed-relation-smith-bounds.md) gives cost κ=Σa_j/e_O at every prime for a fixed potentially crystalline family. The actual relation lattice may be unsaturated; the universal cocycle is nevertheless crystalline by rational extension and Galois descent. A certified rational kernel and one maximal-rank minor give an upper bound. Equality of residual and rational equivariant Hom dimensions gives zero cost. The [tied-row](lsernau-tied-row-construction.md), [local derivative](lsernau-local-tied-derivatives.md), [integral extraction](lsernau-tied-integral-extraction.md), [triangle](lsernau-triangle-detection.md), [Kummer](lsernau-kummer-relations.md) and [selector](lsernau-root-chain-selectors.md) arguments give individual detected integral operators under the remaining Selmer, detection and auxiliary-precision conditions. Enlarging the auxiliary modulus may change the family and κ, so a compatible uniform parameter choice is not proved. Hyperplane avoidance combines the operators without extra valuation loss. |
| Final comparison | [One-lift comparison](lsernau-one-lift-comparison.md) and the [signed determinant inequality](lsernau-mathematical-extraction-2026-11-26.md) are proved under their stated common-lattice inputs. Apply at one common family of scales and divide by the actual positive rank and prime-sum normalizer. |

## Immediate priorities

1. Fit the quantitative noncompact local constructions into the actual
   arithmetic sharp tests and common-chain gauge/squared-norm estimates;
   prove the full-chain see-saw with compatible nonzero volumes.
2. Establish scaled-kernel integrality and the rank-two critical period
   on the same lattices, and good-form eigensystem occurrence; use the
   normalized representation identity and z≥2 norm formula for small twists.
3. Prove the remaining source-uniform crystalline bounds below the
   Fontaine–Laffaille threshold and at level primes, or control the new
   Smith costs as auxiliary families vary. Retain all tied-row precision
   inequalities and sum the actual all-prime denominator budget.
4. Use the quantitative return theorem to prove the actual identity,
   terminal-fixer, open-cell and remaining second moments and multiplicities;
   finish the complement construction and signed determinant comparison.

## Verification and resumption

The exact-arithmetic [Fock script](../scripts/check_noncompact_fock_bridge.py)
was rerun successfully: 68 Casimir identities and 2,064 row/column
commutations, including one noncompact full-gap example. The
[discrete-series convention script](../scripts/check_discrete_series_suppliers.py)
checks 3,362 dominance/bottom-PRV cases, 16,416 lowered-PRV cases
(8,442 strict), and 84 Cholesky/minor cases. The
[finite smearing script](../scripts/check_quantitative_local_smearing.py)
checks 23 full-rank integral spanning matrices in four cases, of maximum
dimension 84. Its small noncompact examples test algebra below the full
source gap, as the certificate explicitly records. These are finite
algebra checks, not computational proofs of the analytic theorems.

The [source-ledger verifier](../scripts/check_local_source_ledgers.py) checks
61 cached Git blobs and all 69 exact path/SHA ledger rows in the listed notes;
its [certificate](../certificates/local-real-galois-integral-source-checks.json)
records the scope. The new local, Galois and arithmetic arguments received
independent internal audits of their decisive steps. No numerical
Galois invariance matrix, fresh Lean replay or external mathematical
review is claimed.

The [recovery index](recovery-crosswalk.md),
[source atlas](../blueprint/lean-source-atlas.md),
[formal audit](../audit/lsernau-formal-audit-2026-11-26.md) and
[attribution](../sources/README.md) distinguish external formal evidence,
our partial local build, source-byte checks and ordinary proofs.
Current PDF build and visual-review details are in
[the manuscript index](../paper/README.md). Compilation is not proof verification.

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
