# Current continuation checkpoint

RH and Dirichlet GRH are **not yet proved by this ordinary reconstruction**.
Read the [active common manuscript](../paper/determinant/body.tex) and
[authoritative dependency plan](../blueprint/merged-proof-plan.md).
For RH first fix modulus 18480; for Dirichlet allow any fixed multiple
of the target conductor and 18480.

## Mathematical dependencies

| Part of the preferred proof | Established and remaining |
| --- | --- |
| Analytic endpoint | [One-sided zero detection and quadratic-twist selection](lsernau-zero-detection.md), [prime reduction](lsernau-moment-and-prime-reductions.md): proved relative to the stated classical inputs and the missing arithmetic remainder. |
| Common theta data | [Finite theta chapter](lsernau-common-theta-finite.md) identifies the actual spaces and levels, proves free class integration and the joint-tensor chain formula, and fixes the normalization. Global see-saw, injectivity, and uniform kernel bounds remain open. |
| A — short integral forms | The common divisibilities, archimedean squared norm and finite clearing index are open on the preferred source data. |
| B — spanning | Exact ramified dimension and direct restriction of the two moments proved in the [finite theta chapter](lsernau-common-theta-finite.md). Conditional rank and index bounds sharpened. Establish good-form multiplicities and actual unfolding estimates. |
| C — attachment | [Two-string cancellation](lsernau-galois-two-string.md) constructs disjoint torus characters and proves all-rank cancellation, spherical clauses and normalized lift trace compatibility from the actual theta polynomial, odd-rank and local-global inputs. Prove those suppliers. |
| C — selected twists | [Small-twist theorem](lsernau-general-small-twist.md) proved under its stated data hypotheses. [Main-summand datum construction](lsernau-main-summand-data.md) gives the matrix span, scalar normalization, rank and smaller defect bound once attached local-type-compatible representations are supplied. [Critical-value systems](lsernau-critical-value-systems.md) gives integral group-ring construction and a uniform constant inverse-ratio height conditional on the actual scaled kernels and period formulas. |
| C — determinant | [One-lift comparison](lsernau-one-lift-comparison.md): integral Weyl frame, finite gluing adjoint, projection and simultaneous separator calculation, exact determinant ratio and sharper conditional signed budget. Prove the actual period and spanning identities, kernel estimates, individual congruence separators, sharp tests and complement construction. |
| Final comparison | [Signed determinant inequality](lsernau-mathematical-extraction-2026-11-26.md) is proved abstractly. Apply it at one common family of scales and divide by the actual positive rank and prime-sum normalizer. |

### Immediate priorities

1. Prove the uniform local integral bounds, global see-saw identity,
   injectivity, Rallis norm and rank-two period identities on the
   specified common spaces and levels. Establish the global Poincare unfolding estimates
   and good-form multiplicity comparison on this diagram.
2. Establish the two nonzero theta lifts with their exact Hecke
   polynomials, odd-rank attachment and the nonspherical labelled
   local-global clauses on the common eigensystems. Apply the
   proved cancellation, Selmer datum and critical-value
   constructions and small-twist theorem.
3. Prove the integral projection denominator and one-lift
   comparison, then assemble the chain ratio and final signed budget.

## The small-twist proof library

The theorem above uses [auxiliary primes](lsernau-auxiliary-prime-supply.md),
[classical duality descent](lsernau-classical-tied-descent.md),
[finite presentations](lsernau-finite-selmer-presentations.md) and
[degree-independent specialization](lsernau-twist-specialization.md).
The cofinal parameter choice and the shared excess budget are part
of the established abstract result.

## Hecke extension

Read the [Hecke checkpoint](../hecke/notes/current-state.md) and
[active manuscript](../hecke/paper/main.md).
The CM structural theorem and small-twist theorem are available
under their explicit conditions. The cubic datum realization,
critical-value formulas and common theta comparison remain open;
exceptional primes and infinite-order phase bounds require separate work.

## Historical alternatives and evidence

The [old checkpoint at the pre-reorganization revision](https://github.com/JoseBrox/GRH_distillation/blob/6b74526223ae1724fa7872c27664b6a565f15244/notes/current-state.md)
indexes the extensive earlier Selmer, theta, global-norm and geometric
results. They remain possible suppliers after an exact matching
dictionary, not extra prerequisites. The [archive](../paper/archive/README.md)
preserves the original manuscript and PDFs.

The [source audit](../audit/lsernau-audit-2026-11-26.md),
[formal verification record](../audit/lsernau-formal-audit-2026-11-26.md)
and [source atlas](../blueprint/lean-source-atlas.md) distinguish external
formal verification, our partial local build and ordinary mathematical
reconstruction. See [attribution](../sources/README.md).

Legacy proof-map counts: RH **6/9**, Dirichlet **18/31**, Hecke **6/9**.
No whole node is closed merely by changing the preferred route.
The reorganized TeX is current; older compiled PDFs are archived,
not new builds. No fresh Lean replay, external mathematical review,
or new PDF build is claimed for these changes.
