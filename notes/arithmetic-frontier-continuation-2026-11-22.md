# Arithmetic continuation: results and next obligations

> **Historical checkpoint — 22 November 2026 (not the current task list).** Its “Working sequence” and “what remains” columns describe the original stage. Later proofs changed those priorities, but the original mathematical statements and source provenance remain valuable. Use the [current checkpoint](current-state.md) and [frontier theorems](open-frontier-theorems.md) for active obligations.

This checkpoint continues the reconstruction from main at
`1b856f01372ec4287347dbfdef26f0e1f83573e7`. The priority is to supply
the original arithmetic hypotheses inside open nodes. Existing node counts
remain **ordinary RH 6/9; Dirichlet GRH 17/31**. These count finished stated
implications or adopted inputs, not a percentage of either proof completed.

## Mathematical changes

| Result | Classification and significance | What remains |
|---|---|---|
| [Full arithmetic isotropic count](geometry-arithmetic-frontier-isotropic-integrability.md) | A missing arithmetic subobligation is proved. Finite rational-line orbits, exact vector-stabilizer unfolding and a convergent ideal sum prove the first moment of all nonzero isotropic vectors. The earlier cusp argument no longer needs an independent integrability assumption. | Identify the original geometric sheets, Hodge metric and lattice, and prove the signed boundary comparison and arithmetic section remainder. |
| [Original geometric mean](geometry-arithmetic-frontier-curvature-haar-mean.md) | The determinant Hodge metric gives the exact invariant density. Its normalized average is a weighted sum of the original arithmetic Haar means, retaining finite sheet multiplicities and stabilizers. The denominator is definitionally the same analytic integral against one, so no extra degree comparison is needed. | Construct the original geometric sheets and metric identification; the signed boundary intersection limit remains separate. |
| [Local reducible prime inclusion](selmer-integral-frontier-incidence.md) | A needed local algebra supplier has a short proof. A proper incidence space is regular with connected closed fibre, hence irreducible; its dimension gives the precise prime inclusion used in propagation. | Supply the original deformation presentation and the patched automorphic dimension, then propagate through the full characteristic-prime fibre. |
| [Selmer relations and local resultant](selmer-integral-frontier-padded-relations.md) | Independent coefficients are obtained by redundant coordinates. The explicit constant \(2\sum_jv_t(\delta_j)\) bounds the actual auxiliary odd terms uniformly in the truncation; corrected descent keeps complex conjugation. | The remaining global/ordinary local cohomological bounds and patched automorphic modules. |
| [Full type-prime theta jets](theta-integral-frontier-type-prime-jets.md) | The original indicator has its required all-order mixed-derivative bound with the full \(p^{fab}\) denominator and local constant one. The proof uses the same ordinary CM family, exact period directions and root phases. | Other required local cases, the global norm estimates, and nonvanishing. |
| [Actual chain rank](level-chain-integrality.md) | A source-index correction: the rank is \(k+i(t+1)\), not \(k+it\). The general chain argument survives and gives a stronger correct saving. | Original local maps, integral laws, other denominators and normalized analytic estimates remain required. |
| [Conjugate-prime divisibility](theta-integral-frontier-conjugate-gain.md) | A real but lower-order gain: the actual inactive lattice acquires \(T^{mfh}\). The rational-lift step and finite-place support are retained. This does not improve the endpoint exponent. | Use the gain in the signed comparison before absolute values; prove the main uniform norm estimates. |
| [Special-fibre obstruction](selmer-integral-frontier-special-fibre.md) | An unsuccessful shortcut is ruled out precisely. Rational rigidity, or passing to a torsion-free quotient, can lose the integral conormal torsion that the argument must bound. | Prove the characteristic-prime curve exclusion for the actual deformation ring. The example is not a Galois counterexample. |
| [Signed analytic boundary energy](geometry-arithmetic-frontier-signed-boundary-energy.md) | The prescribed logarithmic boundary growth gives finite energy and full mass. The actual regularizations converge in corrected energy, and polynomial interpolation recovers the original signed energy without assuming that the Hodge class is Kähler. | The complete signed arithmetic limit still requires the actual compact-model integration dictionary and common vertical curvature. |
| [Original bounded cusp approximants](geometry-arithmetic-frontier-bounded-cusp-energy.md) | The exact inner-chart sandwich proves pointwise, \(L^1\) and corrected-energy convergence for the prescribed sequence. The kernel's circle invariance suffices; continuity of the limiting weight is unnecessary. | Original geometric data and their compact-model arithmetic comparison remain required. |
| [Exact metric variation and locality](geometry-arithmetic-frontier-exact-metric-variation.md) | The intersection recursion gives the positive sign and factor \(n+1\). Tensor cancellation proves full locality and the exact original rational-twist polynomial, removing a separate locality supplier. | Identify the original mixed integrals and common vertical curvature on the compact model. Metric-ratio cancellation alone does not settle curvature. |
| [All modular Selmer solutions](selmer-integral-frontier-dual-detection.md) | Stabilization and completeness control every finite-level solution from the exact integral detection hypothesis. No integral cocycle lift or separate Bockstein hypothesis is needed. | Apply the proved fraction-field detection through the integral paired module and prescribed detecting elements. |
| [Odd paired detection](selmer-integral-frontier-odd-detection.md) | The actual odd supplier is proved using central block idempotents, matrix units, distinct twists and a four-factor relation pairing. It works in the original positive characteristic and retains the specified polarization. | The actual normalized-point span and independent odd Selmer classes remain construction inputs. |
| [Complete fraction-field detection](selmer-integral-frontier-even-detection.md) | The even correction finishes the algebraic paired determinant theorem. A matrix-unit primitive avoids division by block size; the final polarization uses only division by two. The commutator-subgroup condition is retained and a counterexample shows why normality alone is insufficient. | Integral coefficient assembly, denominator transfer, simultaneous finite auxiliary choice and the remaining global/ordinary local estimates. |

The geometric and local propagation entries advance inside open nodes. The rank correction is
necessary for correctness. The conjugate gain is useful to retain but is a
secondary optimization. No statement here establishes a small normalized
Gram error or the final signed discrepancy.

## Analytic norm investigation: an explicit limit

The actual global comparison was followed through the bounded source
contracts recorded in
`certificates/arithmetic-frontier-global-norm-audit.json`:

* The Bessel comparison uses a common target unitary identification, a
  source identification for each word, and the prescribed nonzero scalar.
  Its uniform errors are assertions about these same normalized maps.
* The normalized period Gram matrix is identified with the Poincare sum
  only after the original folding, orbital-integrability, well-definedness
  and absolute-convergence hypotheses. A matrix expansion with those
  hypotheses does not estimate its off-diagonal or nonidentity terms.
* The available qualitative weighted integrability of the archimedean
  reproducing kernel gives no stated uniform numerical constant as rank
  and auxiliary fields grow.
* The actual global theta comparison uses a possibly nonsplit Hermitian
  space, a full-rank finite-place cutoff on the smaller theta series,
  compatible coinvariants, and a nonzero common comparison constant.
  Applying a vaguely specified convergent-range theta identity would
  discard these hypotheses. No such substitution has been made.

The full arithmetic count theorem improves the geometric cusp argument.
It does not remove the previously proved inverse-moment obstruction to
integrating the much higher lattice-minimum power in the present kernel
majorant. No new source-to-projector transfer or uniform normalized
source-deficit estimate was obtained in this inspection.

## Working sequence

1. Complete the original local theta suppliers and test their exact
   normalizations on the actual period maps. Keep the corrected ranks and
   signed local gains. For the global norms, attack the actual near-return
   and tail estimates or a valid signed alternative; another abstract
   frame inequality is not the next target.
2. Apply the proved fraction-field paired determinant theorem to the
   original integral coefficient module, with its exact denominator
   transfer and simultaneous auxiliary choice, then prove the remaining
   global and ordinary local estimates. The complete-equation argument
   already controls nonliftable modular cocycles. Keep the characteristic-prime fibre,
   component chains, and original automorphic modules. Independent
   presentation coefficients are supplied by redundant coordinates.
3. Apply the arithmetic count theorem through the original geometric
   sheets and Hodge metric, retaining their multiplicities and component
   volumes. The intersection recursion, bounded cusp energy limit and
   rational-twist normalization are proved. Complete their compact-model
   integral comparison, retaining common vertical curvature and component
   weights; the interior mean requires no extra algebraic-degree comparison.
4. Carry every result to both routes. The ordinary RH character projection
   is smaller, but its auxiliary geometric ranks and integral indices still
   grow. Preserve the full short analytic RH argument in the guide.

Continue until the selected concrete obligation is proved or the decisive
missing step is precisely located and checkpointed. Do not turn an unchanged
whole-node count into a claim of no mathematical progress, and do not turn a
new local lemma into a claim that an entire arithmetic construction is done.

## Verification and persistence

The proof notes contain the mathematical arguments and retained hypotheses.
Their certificates authenticate pinned source bytes and bounded excerpts;
their exact computations check specified identities and edge cases. They do
not constitute a Lean build. Independent reviews accompany the new count
and incidence proofs. The manuscripts, guide, maps and build records are
updated together, with the guide's complete short analytic proof preserved.
Historical review certificates remain evidence for their original commits.
The current [integration record](../certificates/arithmetic-frontier-integration-2026-11-22.json)
binds the fourteen published checkpoints, both manuscripts, the eight-page
guide and the inspected page ranges. Recheck its artifact identities,
source inclusion, unchanged node status and preserved analytic proof with
`python scripts/check_arithmetic_frontier_continuation.py`.
