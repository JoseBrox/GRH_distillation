# Actual terminal density from a compact complex germ

## Status and frontier

**Closed local supplier, independently reviewed:** the original
`KloostDens` for compact smooth invertible-supported coefficients, at
every relevant block head, with the exact source character and measures.
This is not a claim of `GermRate`, `HeadTop`, the full local kernel
estimate, or W06/W08 completion.

The crucial downstream remaining interface is `PhiZero`: a compact
smooth general-linear coefficient representing the actual unitary
orbital vector for every head with the original stabilizer measures.
`DensityConstantOfParts` lines 50–64 combines precisely that interface,
the density proved here, and regular-cell vanishing. The latter is
available from the already established big-cell pointwise theorem.

## New argument

The source invokes a strong rank-uniform germ theorem on a partially
averaged coefficient. The actual density consumer only involves a fixed
compact coefficient. Block Gaussian elimination shows that every fixed
partial average remains compact smooth and supported away from singular
matrices. Consequently no uniform Schwartz tail analysis is needed.

For the two-block orbit `diag(t J_n,D/t^n)`, use the actual matrix-entry
change followed by the original determinant corner relation. After row
reversal, the matrix is

`t S + diag(q_t,x_1,...,x_n) + Y`,

where `Y` is strictly upper triangular and its determinant is
`D'=(-1)^n D`. Write its determinant as `A q+B`. On the support, every
matrix entry is bounded independently of small `t`; `B=O(t)` and
`A=prod x+O(t)`. Since `D' != 0`, `A` and every `x_i` stay away from zero.
This gives a single compact smooth amplitude for stationary phase.

The phase is `g0=sum x+D'/prod x`; its critical points have all `x_i=z`
with `z^(n+1)=D'`. Its complex Hessian is `z^-1(I+11^t)`. The real
Hessian has signature zero, so the original self-dual complex measure
gives precisely `|t|^n |z|^n/(n+1)`, without an extra phase. The linear
term in the solved corner is `sum Y_(i,i+1)/z`, producing the original
long-orbit character. The reduced Jacobian and the final scaling give
exactly the leading coefficient `|z|^(n^2)/(n+1)` and an `O(|t|)` error
after multiplying the two-block integral by `|t|^(n^2)`.

Distinct roots are isolated by averaging against their additive
characters on expanding annuli. Induction first handles every last
singleton via a compact Schur-complement coefficient, and then every
longer last block via this germ. All block patterns are covered.

## Normalizations and quantifiers

- Every fixed rank, nonzero additive character parameter, nonzero
  determinant and compact smooth Banach-valued coefficient is allowed.
- Remainder constants may depend on all those fixed data. This dependence
  is harmless for the exact zero conclusion; no such constant enters a
  global exponent or a numerical norm budget.
- The `G` source uses `(|beta|/(2*pi))` times planar Lebesgue measure.
  The `PhiTop` source uses planar Lebesgue measure. Their exact factors
  are `b^(n(n+1)/2)` and `b^(n(n+3)/2)`, both nonzero.
- Lower stabilizer roots inside a reversed block remain quotiented out.
- No assertion about the measure of rational sampling points follows
  from an almost-everywhere identity. The density conclusion is at every
  actual relevant head.
- The finite diagnostic checks verify polynomial/normalizer formulas,
  not the stationary-phase theorem or an unbounded-rank proof. The
  latter is the human argument in the shared TeX and the primary
  stationary-phase reference.

## Source evidence

Pinned repository `jsmorph/rh`, revision
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`; source hashes and bounded
excerpts are recorded by the package checker. The primary stationary
phase statement is Evans–Zworski, *Lectures on Semiclassical Analysis*,
version 0.2, Theorem 3.15. Its hypotheses, leading determinant/signature
factor, and derivative-seminorm remainder were read directly.

Jacquet's 1998 density theorem is nonarchimedean. Aizenbud–Gourevitch's
archimedean transfer paper treats real general-linear matrices and
Hermitian matrices; its density corollary was not silently applied to
complex general-linear matrices. The complex result here is proved
directly from the displayed source coordinates.
