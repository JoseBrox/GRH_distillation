# A shorter program for ordinary RH

**The RH transfer is now proved without any weight-symmetry hypothesis.
The compatible arithmetic and geometric estimate needed to finish the proof
remains open.**

The [RH manuscript](../paper/rh/main.pdf) presents this route separately;
the [short guide](../paper/guide/main.pdf) explains the larger picture.
The [direct comparison](../notes/rh-direct-transfer.md) proves the preferred
RH reduction, and the [geometric refinements](../notes/rh-geometric-combination.md)
state the smaller remaining budget.

![The RH specialization and its remaining arithmetic requirements](rh/proof.svg)

Green means a written deduction under its stated inputs. Blue means a cited
input. Red means a remaining construction or estimate. In particular, a green
transfer theorem can depend on an unresolved arithmetic construction.

## The analytic target

Only the corrected zeta prime sum must be bounded. An eventual upper bound
with exponent arbitrarily close to one half suffices; an eventual lower bound
of the opposite sign also suffices. The constants and thresholds can depend
on the exponent. The guide gives the short positivity proof.

The more flexible route controls a weighted positive-part integral over
arbitrarily late whole intervals from Y to Y raised to a fixed power greater
than one. The combined signed budget may first be averaged over a fixed
nearby range of scales: this logarithmic average preserves every detecting
pole. A pointwise upper bound is a stronger sufficient supplier. At each
accuracy the interval shape and averaging width are fixed before Y varies,
and the arithmetic comparison holds almost everywhere on the same slightly
expanded intervals. Only the total exponent loss must tend to zero. The
analytic function remains the zeta sum even when auxiliary primes change.

## The preferred arithmetic comparison

The construction separates larger, or thick, weights from smaller, or thin,
weights. The full character kernel has nonnegative prime coefficients,
including at ramified primes. This permits a one-sided comparison of each
thick weight with its common lower endpoint. Averaging translations before
bounding the perturbation removes both the growing field-degree factor and
the inverse-density factor from that error.

The remaining thin samples occur at much larger prime-sum arguments.
The existing uniform quasi-Riemann hypothesis estimate controls them,
including the separately corrected principal character. The source's size
conditions make both transfer errors negligible. Thus the preferred
comparison requires no equal weight distributions, equal first moments,
logarithmic-dispersion estimate, or new bound for thick-weight logarithmic
derivatives. The large-scale thin estimate still concerns the whole character
family; it must not be omitted.

After this comparison, only four character terms remain: zeta and three
quadratic twists. Rearranging leaves one signed quadratic companion.
The manuscript's simultaneous quadratic selection bounds that companion on
the required sample interval, conditional on its stated uniform quasi-RH
input. Sample intervals must include the short endpoint shifts.

What remains is the **weighted positive-part integral of the locally
averaged signed discrepancy and companion**, for the same integral maps and
geometric objects. Separate discrepancy and companion bounds are sufficient
but not necessary. The transfer and centering errors already have finite
weighted tail integrals under the stated source size conditions. The
[precise criterion](../notes/scale-averaged-criterion.md) retains the common
windows and measurability hypotheses. Its arithmetic bound is still to prove.

## What the specialization removes

| Requirement in the general target | Ordinary RH |
| --- | --- |
| Reach each primitive target character | Retain only the conductor-one character. |
| Treat arbitrary target conductor and order | Both are one. |
| Compare primitive and imprimitive target functions | No target comparison is needed. |
| Impose the selected subset-share condition | This condition is automatic. |
| Project onto a general character quotient | Exactly four sign characters remain. |
| Control a growing collection of thick-weight derivative constants | Positive-kernel comparison removes them. |
| Construct a symmetric family of weights | The preferred proof has no such requirement. |

The auxiliary primes, field degrees and geometric dimensions still grow.
The source construction has not become a fixed-dimensional argument.

## Degree and norm bounds

The geometric comparison keeps the actual Hermitian metrics and rank
weights. The [direct component argument](../notes/geometric-degree-frontier.md)
sums the degree-weighted volume comparison first. Short integral sections
supply a lower degree bound for the same lattices, eliminating a separate
negative-height moment. The raw version retains signed section-rank and
twist costs. The finite section estimate remains an actual requirement.

The [tower reduction](../notes/tower-intersection-reduction.md) replaces
two scalar coefficients by one normalized Grassmannian test and a signed
determinant term. Its exact formula keeps the block contrast, rank factor
and test remainder. A [classical height theorem](../notes/base-test-height-supplier.md)
then supplies the test from an all-point height floor, including the
boundary, and the prescribed cusp comparison. Reciprocal perturbations
and a one-sided limit suffice. The [actual point-height comparison](../notes/actual-point-height-frontier.md)
reduces the arithmetic supplier further to one sum of degrees of the
selected small image eigensublattices. The required bound and exact
metric/integral comparisons remain open. Anchoring a weight entry does not make its sum
zero or cancel its determinant contribution.

The preferred [slope comparison](../notes/one-sided-frame-slope.md) now
uses two positive trace errors of the same maps: a source deficit and a
target excess. This permits a small amount of mass in directions with
large norms. Neither squared-energy control nor a small uniform operator
excess is intrinsic. The source slope spread, target lower slope and
positive total mass remain explicit arithmetic hypotheses. One may keep
the sharper centered source term and take the minimum with older valid
penalties; no useful regime is discarded.

For the target error, synthesis and its adjoint have the same positive
spectrum. Thus a spectral-tail bound on the full normalized block Gram
matrix suffices; its signed orbital terms are combined before taking the
positive part. The orbital expansion and convergence themselves remain
inputs. The proved trace-compression formulas carry this bound through
the actual source and target restrictions, retaining their lost mass and
dimensions. The source trace error still needs its own bound. Estimates
for an average operator alone do not bound the required correlated costs.

The [earlier energy reductions](../notes/averaged-theta-energy.md) and
[uniform period bound](../notes/centered-global-energy-reduction.md)
remain sufficient alternatives. Their extra error denominators are required
when those particular formulas are used; the final-space trace theorem
requires positive mass and the stated slope hypotheses instead. Counting,
divisor, initial section and quotient losses remain in the combined budget.

Four retained characters do not bound the integral splitting index: the
[frontier audit](../notes/rh-construction-frontier.md) gives a quotient
consisting of four copies of the integers modulo the growing group order.
The [finite-symmetry analysis](../notes/finite-symmetry-energy.md) also
retains the actual target-stability condition; positivity and total mass
alone do not control the required trace errors.

## Why the earlier symmetry route is optional

The source uses a common sparse set of distinguished places. Weights there
are separated from weights on its complement by a factor at least x times
the group order. Once that set is proper, exact pooled translation symmetry
is impossible, even for first moments. The proposed absolute transport
criterion is also too large for these weights. The
[source obstruction](../notes/rh-weight-symmetry.md) and
[transport analysis](../notes/transport-symmetry-defect.md) preserve the
proofs and their limits.

Conditional three-mean and complete-top projections remain valid alternatives
for a different construction. They are unnecessary for the preferred route.
Translating the top set together with the weights does not fix the issue:
the relevant character phase depends on their difference and is unchanged.

## Next mathematical work

1. Bound the [selected small-eigenspace degree sum](../notes/actual-point-height-frontier.md)
   and prove its exact point-height comparison and the cusp/metric hypotheses
   in the [base-test supplier](../notes/base-test-height-supplier.md), then use
   the [tower reduction](../notes/tower-intersection-reduction.md) and
   [mean-volume supplier](../notes/mean-volume-supplier.md).
   Equal component volumes then give the mean exactly. Supply the separate
   finite section-rank costs, using short sections to avoid a separate
   negative-height input, and carry signed errors through determinant descent.
2. Supply nonzero integral theta maps, sharp finite-prime divisibility,
   normalized global identities and the two trace estimates for those same
   maps. A signed block spectral-tail bound supplies the target estimate;
   retain the independent source estimate and the actual compression costs.
3. Complete the remaining cohomological estimates for the growing auxiliary
   fields and bound the combined normalized positive-part scale integral on
   the same expanded cofinal windows.

The [GRH program](grh/program.md) retains the general Dirichlet
target and every surviving compatibility condition. The RH case is a
substantially smaller first target, but its central arithmetic estimate is
still unproved in this reconstruction.
