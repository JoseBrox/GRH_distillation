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
