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
| Common theta data | [Finite theta chapter](lsernau-common-theta-finite.md) identifies the actual spaces and levels, proves free class integration and the joint-tensor chain formula, and fixes the normalization. [Graded period unfolding](lsernau-graded-period-unfolding.md) proves height growth, rapid-input quotient convergence, surviving Bessel orbits, exact additive and rational-orbit unfolding, and the normalized double-period reduction with a nonzero fixed scalar. Full chain see-saw, integrated lift injectivity, and quantitative kernel bounds remain open. |
| A — short integral forms | [Scalar CM supplier](lsernau-cm-theta-normal-form.md) proves the actual marked good equation, torsion integrality, derivative ring and scalar non-split normal form. [Charged jet chapter](lsernau-charged-jet-estimate.md) proves the finite Fourier/product transfer from the specified Weil inputs, the multivariable normal form, and the strengthened uniform charged Schur bound. [Standard Weil normalization](lsernau-weil-normalization.md) proves the prescribed lattice, splitting character, coprime frames, finite and archimedean period factors, integral vacuum, scalar torsion conjugate bound and translated scalar-jet covariance in the classical standard model. [Marked-prime charges](lsernau-marked-chain-charges.md) proves the actual collision formula, full marks, diagram and charged-filling comparison, whole-prefix Hecke propagation with at least half the transfer allowance, and the exact weight-degree auxiliary-prime index. [Split transfer and level lifts](lsernau-split-transfer-and-level-lifts.md) proves the exact local split Hecke polynomial, gluing tensor, double-lift/Up identities, source-level preservation and sharper Fourier loss at N, and the definite gauge comparison relative to rational theta equivariance. [Exceptional polynomial geometry](lsernau-exceptional-polynomial-geometry.md) proves the simultaneous weighted depth bound, sharper edge-inclusion determinant bound, exact Pieri-cone volume and terminal gauge from the integral branching intertwiner. [Middle edge](lsernau-exceptional-middle-edge.md) proves the integral root gain and halfway pairing divisibility, defect dimensions, single-copy invariant averaging, actual Frobenius-factor contraction and stepwise pairing congruence, and sharpened pairing colength throughout the source degree range. [Bounded branching](lsernau-branching-normalization.md) constructs the integral intertwiner, its tail-hook normalization and exact Gram contraction. [Marked Hecke index](lsernau-marked-hecke-index.md) identifies the actual global edges and propagates the sharper index through all marked operators, repetitions and ramified intersection. [Nonstandard Weil transport](lsernau-nonstandard-weil-transport.md) fixes the exact hyperbolic Levi phase, proves rational invariance by doubling, canonical pointed transport, tensor products and absolute mixed theta summation for a fixed splitting. [Common jet comparison](lsernau-common-jet-conjugation.md) proves compatible scalar torsion lifts with exact phases, the common finite semilinear jet and Weil law, the uniform Gaussian vacuum bound with a smaller lattice term, and the conjugated Schur-jet operator estimate. Remaining: sharp tests, full common-kernel gauge and chain squared-norm assembly. |
| B — spanning | Exact ramified dimension and direct restriction of the two moments proved in the [finite theta chapter](lsernau-common-theta-finite.md). Conditional rank and index bounds sharpened. [Positive-type moment](lsernau-positive-type-moment.md) proves the finite maximal-fixer closure with factor 1+3b^{-4}. [Global quotient and cut identities](lsernau-global-cut-unfolding.md) establishes the class-return Gram and weighted cut integration and level cancellation under the actual local/convergence inputs. The graded period theorem supplies the local unfolding and double-period steps and their rapid-input convergence. Establish the specific real Bessel formula, Poincare-series majorants, support-to-cut and terminal matching, good-form multiplicities, identity, terminal-fixer and open-cell estimates. |
| C — attachment | [Two-string cancellation](lsernau-galois-two-string.md) constructs disjoint torus characters and proves all-rank cancellation, spherical clauses and normalized lift trace compatibility from the actual theta polynomial, odd-rank and local-global inputs. [Odd-rank patching](lsernau-odd-rank-patching.md) proves the open-normal-subgroup extension and sharp splitting-degree reduction. [Protected quadratic steps](lsernau-protected-quadratic-steps.md) proves the required field and character construction, exact splitting and inertia generation. Establish actual weak base change, split-case attachment and Iwahori/Shintani local compatibility. |
| C — selected twists | [Small-twist theorem](lsernau-general-small-twist.md) proved under its stated data hypotheses. [Main-summand datum construction](lsernau-main-summand-data.md) gives the matrix span, scalar normalization, rank and smaller defect bound once attached local-type-compatible representations are supplied. [Critical-value systems](lsernau-critical-value-systems.md) gives integral group-ring construction and a uniform constant inverse-ratio height conditional on the actual scaled kernels and period formulas. |
| C — determinant | [One-lift comparison](lsernau-one-lift-comparison.md): integral Weyl frame, finite gluing gauge and norm calculation, adjoint, projection and simultaneous separator calculation, exact determinant ratio and sharper conditional signed budget. [Ribet polynomial](lsernau-ribet-polynomial.md) proves the integral tied-row common-element algebra. [Tied rows and coefficient](lsernau-tied-row-construction.md) constructs the main and character matrices and proves the exact squarefree-coefficient budget under the local-defect and triangle/detection hypotheses. Remaining: prove those arithmetic estimates and the auxiliary-level trace-ideal integral action, period and spanning identities, kernel estimates, sharp tests and complement construction. |
| Final comparison | [Signed determinant inequality](lsernau-mathematical-extraction-2026-11-26.md) is proved abstractly. Apply it at one common family of scales and divide by the actual positive rank and prime-sum normalizer. |

### Immediate priorities

1. Apply the exact transport and common definite Schur-jet bound;
   complete uniform chain gauge/norm assembly and sharp tests. Use
   the proved split transfer, auxiliary double-lift, depth and Pieri
   calculations and terminal gauge identity.
2. Supply the specific real Bessel integral, quantitative Poincare
   majorants, support-to-cut and terminal matching. Apply the proved
   graded period recursion and prove the nonzero full-chain scalar, identity/open-cell/terminal-fixer estimates,
   multiplicities, and the Rallis norm and rank-two period identities.
3. Prove actual weak base change, split-case
   attachment and Iwahori/Shintani comparison, and the two nonzero
   theta lifts. Apply the proved Galois gluing and cancellation,
   Selmer datum and critical-value constructions.
4. Supply the arithmetic tied-row length, local-defect and triangle/detection
   bounds and trace-ideal integral action. Obtain the individual separators,
   then assemble the one-lift and chain determinant comparisons.

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
