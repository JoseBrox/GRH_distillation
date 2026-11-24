# Hecke GRH — independent extension program

This is the third research level of GRH_distillation, after
[ordinary RH](../paper/rh/main.pdf) and [Dirichlet GRH](../paper/grh/main.pdf).
We seek the critical-line assertion for every unitary Hecke character
over every number field, including infinite-order characters and
Dedekind zeta functions. This is stronger in scope than Alpöge's
verified Dirichlet result. We have not proved the new assertion.

**[Arithmetic manuscript](paper/main.md)** · **[Proof map](blueprint/proof.svg)** ·
**[Program](blueprint/program.md)** · **[Progress](blueprint/progress.md)** ·
**[Checkpoint](notes/current-state.md)** · **[Frontier](notes/open-frontier.md)**

## What has been achieved

A Hecke L-function records prime ideals and character values.
A direct Mellin transform reduces the zero problem to a one-sided
estimate for an ordinary prime-counting deficit. A positive induction
identity shows that zeros survive norm pullback to a Galois extension.
Thus it suffices to work over totally imaginary Galois fields and
count only completely split rational primes at the square-root scale.
Exact local unit averaging gives nonnegative arithmetic kernels
even for infinite-order characters and ramified powers.

The main proof uses no Masullo trace identity and no special explicit
formula. All reductions have ordinary mathematical proofs here
relative to the stated classical theory. The original
[smoothed transfer](notes/masullo-transfer.md) and its
[alternative manuscript](paper/smoothed-and-trace.md) preserve the
results inspired by Masullo and the RiemannMasullo contributors,
with attribution and hypotheses. The alternative is not a
prerequisite of the arithmetic proof.

## What remains

There are two substantive open tasks:

- **Finite order:** bound the relative number of completely split
  primes compared with those splitting in the maximal abelian
  subfield. The relative route uses our completed Dirichlet proof
  for the abelian base case; an absolute-count alternative avoids
  that separate premise.
- **Infinite order:** bound the split-prime phase sums for the
  actual fixed unitary character.

The [first nonabelian benchmark](notes/s3-benchmark.md) is the
S3 splitting field of X^3-2. Its prime condition is equivalently
representation by the quadratic form u^2+27v^2. We have proved an
eta-product formula excluding all positive real zeros of its new
cubic Hecke factor. Either sign of a one-sided prime discrepancy
estimate would now suffice for this case, but that estimate is open.

The Dirichlet analytic block now transfers to
[general fixed-field finite-order companion families](notes/general-finite-order-companions.md)
under the stated Dirichlet QRH input. In the cubic case the
[relative balance](notes/cubic-relative-comparison.md) and
[good-prime reduction](notes/cubic-good-prime-comparison.md) leave
only unramified rational first powers in the arithmetic supplier,
with a simple bias of the top labels.

The [actual 2-primary Selmer window](notes/cubic-two-primary-window.md)
is proved for the full moving cubic host, using its fixed field's
class number one and elementary cyclotomic descent. The
[exceptional-prime comparison](notes/cubic-exceptional-prime-comparison.md)
handles the integral splitting error at 3; its genuine twisted
lengths remain open. The cubic field cannot be a CM host, but
[actual polarized twists and an equivariant three-line theta family](notes/cubic-torsor-realization.md)
realize the required local Frobenius labels on the old CM geometry.
Actual [cubic differential theta maps](notes/cubic-differential-theta-maps.md)
now supply the Hasse-invariant Frobenius divisibilities, an exact
split-sensitive simultaneous index and explicit canonical metric bounds.
The [coefficient-to-theta isomorphism](notes/cubic-theta-coefficient-interface.md)
and bounded-order global operators realize both cubic coefficients;
their CRT height still pays for the divisor.
The [fixed-conductor Selmer window](notes/cubic-fixed-conductor-selmer-window.md)
controls all fixed-odd-conductor cubic sectors at 3 and reduces the
one-sign 2-primary generator bound to 8.
The [polarized cubic deformation frame](notes/cubic-polarized-selmer-model.md)
and [cohomology count](notes/cubic-frame-cohomology.md)
supply the integral torsion injection, exact relative dimensions and
conditional polynomial spectrum at odd primes. The critical-scale
global degree/norm estimate, moving low-dyadic sectors at 3 and
the new automorphy/rigidity-based length comparison remain open.

A second, independent global arithmetic route now constructs
[integer-valued polynomial lattices](notes/global-interpolation-lattices.md)
whose relative index is exactly the integrated prime-ideal count.
The [derivative refinement](notes/global-derivative-lattices.md)
replaces pairwise divided differences by linear-size value and
derivative matrices, with critical-scale error and stable
archimedean metrics. The remaining relative saturated-covolume
lower bound would settle Dedekind RH without CM geometry or
Selmer theory, but is open. The
[one-sign polynomial companions](notes/polynomial-one-sign-companion.md)
remove the QRH input from a replacement cubic analytic block;
[high-dyadic 3-primary vanishing](notes/cubic-three-primary-vanishing.md)
deletes the cubic sectors with 2^b >= 192f and b >= 8, where
f is the actual odd conductor. The remaining moving low-dyadic 3-primary and odd-prime estimates,
and the sharp global degree/norm comparison, remain open.

The [all-order formal operator lattice](notes/cubic-formal-operator-lattices.md) identifies integral theta maps with polynomials integer-valued on actual cubic p-adic lines. The [symbol-derivative index](notes/cubic-symbol-derivative-lattices.md) recovers the truncated prime discrepancy with normalized error O(sqrt(X) log X), without a zeta multiplier. Collective degree/norm saving or normalized period coupling remains open.
The [marked point theorem](notes/cubic-point-shapes-and-rigidity.md) classifies the two-sided points in either characteristic and proves the obstruction to the standard rank-one tensor Euler-system hypothesis. The new [high-dyadic corner elimination](notes/cubic-corner-elimination.md) excludes all two-sided reducible points under its explicit conductor threshold, and the [actual relation count](notes/cubic-high-dyadic-presentation.md) reduces finiteness to the irreducible curve test. The [direct Euler-system route over the Eisenstein field](notes/cubic-eisenstein-euler-systems.md) recovers the rational image condition but leaves a rank-two local regulator and the genuine Euler-system classes to construct for lower dyadic cases. The full moving lengths and geometry remain open.
The [3-primary local defect theorem](notes/cubic-three-primary-local-defects.md) bounds normalized lifting losses by one, controls aggregate residual generator ranks and proves untwisted cubic vanishing at 3. Moving low-dyadic lengths and resonant odd-prime lengths are open.
The [unconditional two-prime theorem](../notes/unconditional-quadratic-selection.md) supplies the original two-sign numerical block with all congruences and exponential thin bound, without QRH; both parent manuscript sources and the partial common-window assembly now implement it.

The new [full connected monodromy theorem](notes/cubic-irreducible-monodromy.md) excludes imprimitive and orthogonal-type irreducible points in both characteristics: every remaining high-dyadic irreducible point has connected group SL3. The [trace and adjoint comparison](notes/cubic-trace-and-adjoint.md) identifies the entire integral invariant ring with the closed trace algebra, and proves finite local conditions for actual dual-number tangents. Genuine cuspidal attachment therefore implies normalized tangent rigidity by Thorne's theorem, without a separate Euler-system premise. The [automorphic seed audit](notes/cubic-automorphic-seed-frontier.md) constructs an ordinary 2+1 isobaric starting datum from the parent rank-two seed (for coefficient primes prime to the host conductor). It is not the required cuspidal GL3 seed. The symmetric-square route fails even after CM restriction preserving distinct residual constituents; the checked level-raising and reducible lifting theorems do not directly apply. The parent auxiliary class-rank argument also needs a new bound on the nontrivial cubic components over the nonabelian residual splitting field.

The [pure-cubic descent](notes/pure-cubic-selmer-descent.md) identifies each cubic strict Selmer sector with the extra direct summand over $C=\mathbb Q(\sqrt[3]2)$ of the rational-twist strict group, exactly away from 3 and up to an explicit polynomial isogeny error at 3. The field $C$ has class number one. For 3-cycle coefficient primes and inert cyclic host fields satisfying the stated class-number test, the entire sector vanishes at weights divisible by $\ell-1$. The [finite class-rank certificate](notes/cubic-finite-class-rank-certificates.md) gives exact cubic coinvariant control at inert primes, and $g_{\lambda,n}+s_\lambda<\ell^n$ certifies a bounded generator rank for the actual fixed auxiliary tower. A zero initial cubic component at inert primes suffices for integral vanishing at every twist weight. The [two-negative-weight elimination and specialization](notes/cubic-two-negative-weight-elimination.md) prove that when this residual adjacent vanishing accompanies the already proved corner vanishing, the full invariant ring is $\mathcal O$ and both irreducible-point premises hold vacuously. The exact inert specialization also supplies a common-window bound for a fixed finite list of successful finite-rank certificates. None of these tests has been proved to succeed uniformly for the moving data.

The [progress inventory](blueprint/progress.md) has 6/9 written
reductions or cited inputs; the former open node H07 was split
into the two tasks above. This is not a proof-completion percentage.

## Proofs and working rules

See the [direct criterion](notes/direct-prime-criterion.md),
[Galois reduction](notes/galois-base-change.md),
[unitary kernels](notes/unitary-positive-kernel.md),
[results](results/README.md), [limitations](negative-results/README.md)
and [sources](sources/README.md). Follow [project rules](../AGENTS.md):
commit reviewed proofs and precise partial results promptly.
Update manuscript, proof map and checkpoint together. Every essential
nonclassical input of a final proof must be proved in this repository.
