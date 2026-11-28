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
| A — short integral forms | The [scalar CM](lsernau-cm-theta-normal-form.md), [charged jet](lsernau-charged-jet-estimate.md), [Weil normalization](lsernau-weil-normalization.md), [marked chain](lsernau-marked-chain-charges.md), [split transfer](lsernau-split-transfer-and-level-lifts.md), [exceptional geometry](lsernau-exceptional-polynomial-geometry.md), [middle edge](lsernau-exceptional-middle-edge.md), [bounded branching](lsernau-branching-normalization.md), [marked Hecke index](lsernau-marked-hecke-index.md), [nonstandard transport](lsernau-nonstandard-weil-transport.md) and [common jet](lsernau-common-jet-conjugation.md) chapters supply their stated algebraic and local norm estimates. [Sharp scalar couplings](lsernau-sharp-scalar-couplings.md) proves the all-prime lower bound, sparse coupling gain, exact carries and actual admissible frame/weight inequalities; six copies suffice. Padding gives the existing twelve-copy [global sharp extraction](lsernau-sharp-global-extraction.md) with one common height-controlled factor. Remaining: transport into the actual comparison maps, common-kernel gauge and chain squared-norm assembly. |
| B — returns and spanning | [Bessel majorants](lsernau-bessel-majorants.md), [stationary period](lsernau-stationary-bessel.md), [finite support/cuts](lsernau-support-to-cut.md) and [quantitative returns](lsernau-quantitative-returns.md) give the derivative/Schur bound, exact Gram coarea, local exponent 214n², integral frame separation, free-level weighted packing, absolute Poincare convergence and source truncation bound under the explicit coefficient and bounded-reduction hypotheses. [Global cuts](lsernau-global-cut-unfolding.md) have the required absolute convergence. [Exact Bessel subgroup](lsernau-bessel-subgroup-moment.md) computes the normalized subgroup term, its multiplicity and the block truncation error. [Good-form multiplicities](lsernau-good-form-multiplicities.md) now proves equality of the full finite Hecke modules using the two split cuspidal places and the refined Harris–Labesse argument. [Finite good-type density](lsernau-finite-good-type-density.md) supplies exact allowed/primitive counts, sharp Green masses and the finite bad-projector bound, with its admissible size inequalities checked. [Positive-type closure](lsernau-positive-type-moment.md) and [dimension/compression](lsernau-common-moment-interface.md) remain conditional on the actual identity, terminal-fixer, open-cell and other second moments. |
| C — spherical attachment | [Split attachment](lsernau-split-galois-attachment.md) supplies the classical spherical Galois representation at every positive rank and coefficient prime, including 2, on the source's actual Weil-data fields. Labesse, the explicit cuspidal-factor construction and Chenevier–Harris give the normalized unramified, crystalline and labelled Hodge clauses. The older protected quadratic, odd-rank and two-string route is an alternative, not a prerequisite. |
| C — labelled local compatibility | [Dominant matching](lsernau-iwahori-dominant-matching.md), [finite-type sorting](lsernau-iwahori-type-sorting.md), [full Shintani products](lsernau-shintani-product-types.md) and [prime CM assembly](lsernau-tame-local-global-assembly.md) complete the selected sorted-Iwahori and labelled polynomial assertions, including repeated determinant labels, finite inertia and potential crystallinity. The CM steps preserve Weil data and trace-one integers, and restriction to the common kernel transports actual period operators. A positive Weil element of degree k needs tower degree exactly k times the joint unit-character image, at most k(q−1). The finite all-powers lemma avoids an infinite tower. |
| C — selected twists | [Small twists](lsernau-general-small-twist.md), [main-summand data](lsernau-main-summand-data.md) and [critical-value systems](lsernau-critical-value-systems.md) prove their constructions under the displayed inputs. [Normalized transfer and critical norms](lsernau-normalized-transfer-critical-norm.md) supplies the full normalized rational representation identity on occurring comparison eigensystems, exact rectangular sharp mass, common finite Hecke Rallis operator, and the stable-range critical norm for z≥2. [Integral critical kernels](lsernau-integral-critical-kernels.md) proves the z≥2 scaled-kernel gauge and integral group-ring norm systems, with exact Fourier denominator M^(fn) instead of M^(2fn). [Two-place comparison](lsernau-good-form-multiplicities.md) supplies actual occurrence and multiplicities. [Rank-two arithmetic](lsernau-rank-two-period-arithmetic.md) proves the z=1 integral gauge/measure and exact Euler relation, saving M^(12f+h)d^(h/2) in its scale. The fully ramified analytic period and nonzero base case remain. The exact inverse-ratio height is below 5 per critical pair. |
| C — arithmetic lengths | [Integral separators](lsernau-integral-separators.md) proves finite local duality counts, the relation-cocycle lift, defect-to-colength comparison and global tied-length bound, including divisible coefficients. [Fontaine–Laffaille zero defect](lsernau-fontaine-laffaille-zero-defect.md) gives vanishing for the unramified aligned-window range, including every p∤M with λ_p=0 and the stronger threshold p≥b+δ+W+η+2. [Bounded-class crystalline loss](lsernau-bounded-class-crystalline-loss.md) gives a finite bound for the full enlarged family at every prime, including 2 and level primes, independent of its ranks and precision. Its numerical size as the field, target and weights grow remains open. |
| C — fixed-family costs and individual operators | [Fixed-relation Smith bounds](lsernau-fixed-relation-smith-bounds.md) gives cost κ=Σa_j/e_O at every prime for a fixed potentially crystalline family. The actual relation lattice may be unsaturated; the universal cocycle is nevertheless crystalline by rational extension and Galois descent. A certified rational kernel and one maximal-rank minor give an upper bound. Equality of residual and rational equivariant Hom dimensions gives zero cost. The [tied-row](lsernau-tied-row-construction.md), [local derivative](lsernau-local-tied-derivatives.md), [integral extraction](lsernau-tied-integral-extraction.md), [triangle](lsernau-triangle-detection.md), [Kummer](lsernau-kummer-relations.md) and [selector](lsernau-root-chain-selectors.md) arguments give individual detected integral operators under the remaining Selmer, detection and auxiliary-precision conditions. [Uniform inertia relations](lsernau-uniform-inertia-relations.md) caps the actual obstruction by local cohomology and gives a fixed Smith bound independent of auxiliary precision and unramified twists whenever all rational inertia actions factor through one fixed potentially crystalline inertia algebra. This is an explicit supplier for selected main-summand lifts. The bounded-class theorem now covers the full enlarged family Y without a fixed inertia algebra, using Liu’s torsion-limit theorem and an Artinian obstruction argument. Coefficient extension preserves the normalized bound for a fixed target lattice. The growing-field numerical budget remains open. Hyperplane avoidance combines the operators without extra valuation loss. |
| Final comparison | [One-lift comparison](lsernau-one-lift-comparison.md) and the [signed determinant inequality](lsernau-mathematical-extraction-2026-11-26.md) are proved under their stated common-lattice inputs. Apply at one common family of scales and divide by the actual positive rank and prime-sum normalizer. |

## Immediate priorities

1. Transport the proved sharp arithmetic tests through the actual comparison
   maps. Complete the common-chain integral gauge, squared norms and full
   see-saw with compatible nonzero volume factors.
2. Prove the fully ramified analytic rank-two period and nonzero base case.
   Its integral gauge, group-ring measure and exact Euler relations are
   supplied; apply the stable-range systems and normalized rational
   representation identity on the now-proved common good eigensystems.
3. Quantify the bounded-class crystalline constants as the original global
   field, targets and weights grow, or prove an effective replacement that
   fits the signed all-prime budget. Auxiliary-family/precision uniformity
   is proved; the remaining Selmer, detection and extraction inequalities
   must still be met simultaneously.
4. Prove the non-Bessel identity, terminal-fixer, open-cell and remaining
   second moments, using the exact Bessel term and finite good-type density.
   Complete the complement basis and signed determinant comparison.

## Verification and resumption

New exact checks and source records are in the
[verification index](../certificates/README.md): sharp scalar coefficients
and weight cases, rank-two finite residue/Euler identities, finite
cuspidal projector conventions and good-type density. The bounded-class
verifier checks the pinned source interfaces and Liu’s published PDF;
it does not compute the uniform constant. These checks supplement the
written proofs and their identified classical inputs. They do not prove
an analytic period or replay Lean.

The decisive scalar, rank-two, multiplicity and bounded-class arguments
received independent internal mathematical reviews, with their scope
recorded in the verification index. No external mathematical review,
numerical Galois invariance-matrix calculation or fresh Lean replay is
claimed. The previous [source-ledger certificate](../certificates/local-real-galois-integral-source-checks.json)
and earlier exact checks retain their recorded historical scope.

The [recovery index](recovery-crosswalk.md),
[source atlas](../blueprint/lean-source-atlas.md),
[formal audit](../audit/lsernau-formal-audit-2026-11-26.md) and
[attribution](../sources/README.md) distinguish external formal evidence,
our partial local build, source-byte checks and ordinary proofs.
Current PDF build and visual-review details are in the
[manuscript index](../paper/README.md). Compilation is not proof verification.

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
