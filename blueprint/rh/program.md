# A shorter program for ordinary RH

**The RH transfer is now proved without any weight-symmetry hypothesis.
The compatible arithmetic and geometric estimate needed to finish the proof
remains open.**

The [RH manuscript](../../paper/rh/main.pdf) presents this route separately;
the [short guide](../../paper/guide/main.pdf) explains the larger picture.
The [direct comparison](../../notes/rh-direct-transfer.md) proves the preferred
RH reduction, and the [geometric refinements](../../notes/rh-geometric-combination.md)
state the smaller remaining budget.

![The RH specialization and its remaining arithmetic requirements](proof.svg)

Green means a written deduction under its stated inputs. Blue means a cited
input. Red means a remaining construction or estimate. In particular, a green
transfer theorem can depend on an unresolved arithmetic construction.

## Present construction frontier

The original model system, good cover, raw integral theta sections and
ordinary automorphic families are constructed. Exact Gaussian reproduction,
the weighted Siegel--Weil identity and the actual harmonic heat comparison
retain the prescribed scalars. The actual raw theta system now has a
short integral K-span with uniform component and embedding norms. The
flat determinant degree and integral parallel twists are supplied.
The rank-two characteristic-prime curves and full stable-component
propagation are proved. The complete rational-return sum is the actual
Poincare Gram operator; its original target projector fixes the periods
exactly. The arithmetic flag controls the original higher-rank minimum.
The [frontier theorems](../../notes/open-frontier-theorems.md) concentrate
on rank-three thick support and the uniform integral Selmer bound,
selected-prime divisibility compatibility, final arithmetic-map
identification and uniform trace estimates, and pointwise norm/height
bounds. The original key shift now supplies both exact short-family
hypotheses of the degree argument. Four
characters do not bound fields, ranks or integral defects. No whole node
is closed by these suppliers.

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
and the arithmetic comparison holds on the same expanded intervals. The
[fourth-power criterion](../../notes/fourth-power-sampling.md) now permits
independent finite tables of comparisons only at fourth-power arguments.
It uses convexity of the prime ramps and the known concave correction,
so its interpolation error is of square-root order for zeta. This avoids
a measurable choice of arithmetic objects over a continuum. The explicit
sampled comparisons are required; they do not follow from an almost-everywhere
bound. Only the total exponent loss must tend to zero. The analytic
function remains the zeta sum even when auxiliary primes change.

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
[precise criterion](../../notes/scale-averaged-criterion.md) retains the common
windows and measurability hypotheses. Its arithmetic bound is still to prove. The finite-table alternative
requires only finitely many constructions for each interval and allows
independent choices on overlapping intervals.

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
weights. The [direct component argument](../../notes/geometric-degree-frontier.md)
sums the degree-weighted volume comparison first. Short integral sections
supply a lower degree bound for the same lattices, eliminating a separate
negative-height moment. The raw version retains signed section-rank and
twist costs. The finite section estimate remains an actual requirement.

The [tower reduction](../../notes/tower-intersection-reduction.md) replaces
two scalar coefficients by one normalized Grassmannian test and a signed
determinant term. Its exact formula keeps the block contrast, rank factor
and test remainder. A [classical height theorem](../../notes/base-test-height-supplier.md)
then supplies the test from an all-point height floor, including the
boundary, and the prescribed cusp comparison. Reciprocal perturbations
and a one-sided limit suffice. The [actual point-height comparison](../../notes/actual-point-height-frontier.md)
reduces the arithmetic supplier further to one sum of degrees of the
selected small image eigensublattices. The [selected-degree identity](../../notes/selected-eigenspace-degree.md)
now gives a two-case proof retaining the favorable integral indices and
only the signed total conjugate imbalance. The exact abelian rank is kept
separate from the toric rank. A [short theta-jet proof](../../notes/theta-jet-slope-reduction.md)
reduces the tangent bound to integral theta sections and their uniform
norms, with a smaller tensor power. The
[classical theta supplier](../../notes/moret-bailly-theta-supplier.md) now
provides those inputs in the prescribed metric, giving constant 12.
The [determinant bridge](../../notes/geometric-flat-determinant.md) keeps
the exact signed signature difference and cancels the finite correction.
The integral comparison has four shorter parts:
[coefficient freeness](../../notes/boundary-hodge-freeness.md) from a
universal extension and the torus filtration,
[both filtrations](../../notes/biextension-conjugate-filtration.md) from
first-order sections and relative Frobenius,
[determinant torsion and constant finite order](../../notes/determinant-torsion-rigidity.md),
and [exact CM eigenframes](../../notes/cm-integral-eigenframes.md) from
the relative different. The local conjugate-norm calculation needs no
real generator or finite unramifiedness over the real subfield; the
global host requirements remain. Compatible formal charts along test
curves suffice for the filtration argument, including in characteristic
two; no extra global semiabelian family along the curve is required.
The [elliptic product and period calculation](../../notes/cm-product-period-calculation.md)
now supplies the integral CM product and exact signed value, including
the dyadic lattice comparison. The
[ramified determinant construction](../../notes/ramified-hodge-determinant.md)
now supplies the integral line from the actual global biextension and
geometric fibre data. Pointed first-order sections construct its Hodge
extension; generic properness and flatness force coherent adjunctions.
The corrected character determinant has exactly the prescribed tangent
eigenlattice at every integral point, also after finite ramified extension.
Individual tangent eigensheaves need not be free over the coefficient
algebra. The [pure-period descent](../../notes/cm-period-point-descent.md)
now identifies the exact algebraic CM point on its chosen component,
with its original line and both finite level maps. It uses the actual
moduli point separation and prescribed pointwise period presentation.
The [CM extension theorem](../../notes/cm-integral-map-extension.md)
then uses properness and classical semiabelian uniqueness to identify its
exact integral line and tangent eigenlattices. The actual global family,
original cubical line, fibre comparisons and pointwise period data,
original geometric sheets, Hodge metric and lattice identification,
required height inputs and arithmetic section remainder remain requirements.
The supplied-model theorem proves the signed boundary comparison. The
[arithmetic first-moment theorem](../../notes/geometry-arithmetic-frontier-isotropic-integrability.md)
proves integrability of the full original count; the
[cusp counting theorem](../../notes/cusp-counting-mean.md) then supplies
allowance 3 from the original measure and lattice identities. The
[curvature and sheet theorem](../../notes/geometry-arithmetic-frontier-curvature-haar-mean.md)
supplies that exact mean comparison from the original geometric data,
with no additional algebraic-degree normalization. The
[boundary period proof](../../notes/flat-family-boundary-extension.md)
constructs the generic algebraic determinant and assembles its local norms
on that model. Anchoring a weight entry
does not make its sum zero or cancel its determinant contribution.

The [prescribed-scale slope comparison](../../notes/prescribed-trace-calibration.md)
uses a positive number \(c\) fixed before evaluating the maps, with a
source trace deficit \(g_c\) and a target trace excess \(b_c\). It permits
individual zero maps and never divides by their unknown total norm.
The inequality \(g_c<1\) proves that at least one map is nonzero; it
does not prove every map nonzero. For an entirely zero family,
\(g_c=1\) and \(b_c=0\). Both errors still need arithmetic estimates
for the same integral maps and metrics.

The [actual-mass trace comparison](../../notes/one-sided-frame-slope.md)
remains an alternative when its positive-mass hypothesis is supplied.
Both versions permit a small amount of mass in large-norm directions.
The source slope spread and target lower slope remain explicit.
Keep the smaller valid trace or energy penalty.

For the target error, synthesis and its adjoint have the same positive
spectrum. Thus a spectral-tail bound on the full normalized block Gram
matrix suffices; its signed orbital terms are combined before taking the
positive part. The [exact periodization formula](../../notes/common-unipotent-periodization.md)
now identifies the common unipotent group and the full arithmetic sum.
The [scalar envelope](../../notes/whittaker-scalar-envelope.md) proves
the exact seed constant \(c_u=v_Kv_{N,u}v_{H,u}/d_u\) from the original
compact representation and finite column cells. This is before
arithmetic folding and gives no nonvanishing assertion about the folded
map. Its weighted version gives an explicit positive function \(F\),
retaining every rational coset. On the retained target of dimension
\(n\), the target defect is bounded by
\[
 \frac1c\int (F-c/n)_+B_0,
\]
where \(B_0\) is the sum of squared absolute values of an orthonormal
target basis. The integral still needs a uniform arithmetic bound.
The actual level splitting, column stabilizers, compact irreducibility
and Haar measures are retained. The weighted pairing justifies unfolding
from absolute summability and square-integrable period sums.

The prescribed-scale compression formulas use known dimension fractions,
without division by unknown surviving mass. The older actual-mass formulas
retain their own lost-mass conditions. The [sharp return comparison](../../notes/dominant-return-deficit.md)
bounds source loss by the integrable scalar `B-(2m-A)_+^2`, retaining
the actual source cuts and target loss. It caps crowded regions by their
seed mass and preserves the part a dominant return cannot cancel.
Together with the target envelope it bounds both defects at the retained
seed rank. Smallness remains an arithmetic task; signed information may
give a smaller bound. Finite mass of \(F\) alone
does not control the weighted positive part.

The [earlier energy reductions](../../notes/averaged-theta-energy.md) and
[uniform period bound](../../notes/centered-global-energy-reduction.md)
remain sufficient alternatives. Their extra error denominators are required
when those particular formulas are used; the prescribed-scale trace
theorem requires its stated slope hypotheses and both trace estimates.
Counting,
divisor, initial section and quotient losses remain in the combined budget.

Four retained characters do not bound the integral splitting index: the
[frontier audit](../../notes/rh-construction-frontier.md) gives a quotient
consisting of four copies of the integers modulo the growing group order.
The [finite-symmetry analysis](../../notes/finite-symmetry-energy.md) also
retains the actual target-stability condition; positivity and total mass
alone do not control the required trace errors.

## A smaller cohomological requirement

[Classical duality and even K-groups](../../notes/qualitative-selmer-finiteness.md)
supply finiteness of the actual strict Selmer groups, including the prime
2, and finite prime support for each fixed host and twist range. This
removes separate qualitative finiteness and summability obligations. The
useful bound as the host and twists grow remains quantitative.

For RH, every auxiliary character has order a power of two, so the
[nontrivial odd-order branch](../../notes/two-primary-selmer-reduction.md)
is empty. The trivial character, complementary parity, exceptional
primes and local integral comparisons remain. Counting prime--twist
pairs jointly also improves the polynomial exponent.
The reconstructed opposite-parity estimate remains an available supplier;
its application must retain the actual group and local conditions.

The congruence consumer needs only the
[finite weighted sum on actual twisted places](../../notes/finite-twisted-place-budget.md).
Keep the ramification-inertia fractions away from generator primes;
the latter already have aggregate estimates. The support must be the
one chosen by the same arithmetic construction.

For the actual RH host, the
[residual decomposition](../../notes/rh-selmer-residual-budget.md) and
[integral projectors](../../notes/rh-selmer-product-criterion.md) leave
one weighted product of orders of finite Selmer direct factors. Its
quantitative bound remains open. The
[resultant calculation](../../notes/rh-selmer-resultant.md) supplies the
elementary integer certificate in one orbit estimate. When two such
integers bound the same orbit, a corrected greatest common divisor
replaces their product; both exceptional primes are retained. This
neither supplies the trace-to-Selmer inequality nor proves a uniform
saving for the actual integers.

The [conormal pairing](../../notes/rh-selmer-conormal-pairing.md) supplies
the lower comparison at odd primes for the same marked model: the
strict Selmer group embeds in the dual of one finite negative-weight
conormal quotient. It controls every elementary divisor and the exponent.
Ambient torsion is removed before imposing the global equations, whose
new torsion is retained. The actual models remain, with their automorphy
and two-sided rigidity inputs. The RH
specialization does not remove the five local weights or make the
cyclotomic twist self-inverse. The
[exact Euler determinant](../../notes/rh-selmer-euler-determinant.md)
keeps every generic multiplicity before the coarse upper bound.
The [finite free leading quotient and generating-function count](../../notes/rh-selmer-mixed-count.md)
give the lower numerical constant with an explicit degree threshold,
without assuming global flatness. The
[graded Koszul comparison](../../notes/rh-selmer-koszul-comparison.md)
proves positivity and exact scalar extraction; the
[four-weight argument](../../notes/rh-selmer-admissibility.md) proves
admissibility. Finally, the
[finite-slice argument](../../notes/rh-selmer-upper-multiplicity.md)
gives uniform eventual support and the generic multiplicity bound.
These complete the abstract numerical comparison under the stated
chart, spanning, finiteness, separation, tangent and trace conditions.
The one- or two-point slice also identifies the exact source of its
factor two. The [full abstract theorem](../../notes/rh-selmer-core-wrapper.md)
now supplies integral Smith normalization and the weight-zero chart cut.
An equation-valued adjustment gives a nonzero chart representative with
unchanged point values, and one orbit per degree-zero character supplies
the finite cover.

The [diagonal-point proof](../../notes/rh-selmer-diagonal-rigidity.md)
now supplies fixed-point uniqueness from the actual inertia trace,
residual separation and class-number exclusions. Its transfer to the
graded model retains local point lifting and the density comparison.
The same class-field argument gives the weight-zero global rigidity
statement. The [negative-weight proof](../../notes/rh-selmer-negative-weight-rigidity.md)
uses qualitative strict Selmer finiteness to prove rational vanishing
for every finite-order twist, without a numerical \(K\)-group bound.
It treats all three actual negative adjoint summands and proves that
the marked normalization makes a base-point coboundary zero.
The scalar result includes the prime 2; the actual graded-model
comparison still uses odd primes. The [graded comparison](../../notes/selmer-tangent-comparison.md)
supplies the permitted point rescaling, tangent lifting and faithful
cocycle comparison from the actual weighted presentation and finite
degree-zero quotient. The [crystalline component comparison](../../notes/selmer-crystalline-component-comparison.md) supplies the local finite-cocycle condition from the original ordinary equations and local-ring factorization. The arithmetic model, two-sided
rigidity, construction of the marked model and integral lifting remain.
Neither characteristic-zero uniqueness nor tangent
rigidity removes integral conormal torsion. The
[arithmetic frontier](../../notes/rh-selmer-valuation-frontier.md) shows
why generic rigidity alone cannot bound the missing integral torsion,
and why the trace classes alone give no uniform common-divisor saving.

## What the pairwise norm bounds do not give

The [exact spectral examples](../../notes/redundant-period-spectrum.md)
show why the full nonidentity orbital contribution is necessarily large
in this redundant normalization. The estimate must concern its positive
tail above the mean eigenvalue. The
[integral incidence construction](../../notes/basis-invariant-trace-obstruction.md)
attains the sharp square-root loss under every invertible comparison
basis, with fixed height-zero arithmetic maps. Small arbitrary source
and target cuts preserve an explicit part of that loss. Preserve the
smaller valid energy penalty unless an actual global input improves it.
An ambient projector is not automatically the sum of the chosen periods.
The common unipotent group does give Fourier orthogonality for distinct
characters on its compact adelic quotient. The full arithmetic
periodization still contains the other rational orbits. The exact seed
normalization and weighted seed identity now give the scalar envelope
for the complete target operator. The source deficit and the required
weighted target estimate remain open.

## Why the earlier symmetry route is optional

The source uses a common sparse set of distinguished places. Weights there
are separated from weights on its complement by a factor at least x times
the group order. Once that set is proper, exact pooled translation symmetry
is impossible, even for first moments. The proposed absolute transport
criterion is also too large for these weights. The
[source obstruction](../../notes/rh-weight-symmetry.md) and
[transport analysis](../../notes/transport-symmetry-defect.md) preserve the
proofs and their limits.

Conditional three-mean and complete-top projections remain valid alternatives
for a different construction. They are unnecessary for the preferred route.
Translating the top set together with the weights does not fix the issue:
the relevant character phase depends on their difference and is unchanged.

## Next mathematical work

1. Construct the actual integral theta kernels and verify their local laws,
   original value lattices, stabilizer units and twisted-source ties.
   The [full type-prime mixed-jet bound](../../notes/theta-integral-frontier-type-prime-jets.md)
   is now proved with the original denominator and local constant one.
   The [exact chain identity](../../notes/level-chain-integrality.md)
   supplies the auxiliary-prime iteration, retaining the source factor
   and every intermediate rank. Keep all other period denominators and
   normalized global identities. Bound the sharp scalar return cost
   (or a smaller signed source deficit) and the scalar
   target excess at a prescribed
   \(c>0\), with the same restrictions and arithmetic metrics.
   A strict source deficit supplies aggregate nonvanishing; any consumer
   requiring individual nonvanishing still needs that stronger statement.
   Seed mass before folding supplies neither trace estimate. The
   [scalar-pair lattice theorem](../../notes/global-norm-frontier-scalar-density.md)
   now supplies equality of the original local densities, and the
   [signed finite-place bound](../../notes/global-norm-frontier-primitive-density.md)
   refines their existing count. Remaining local orbital laws and the
   quantitative archimedean Bessel estimate are separate suppliers.
2. Bound the finite weighted Selmer product on the actual twisted primes for
   the growing auxiliary fields. Construct the marked models and verify
   the weighted chart and finite degree-zero quotient. Apply the proved
   point and tangent comparisons; identify the original local ordinary equations, local-ring factorization and finite inertia conditions for the crystalline comparison
   to use nonpositive base-point rigidity at odd primes. Establish
   the two-sided rigidity and trace conditions. Use diagonal separation
   with its actual local and point-lifting hypotheses, the compatible
   conormal pairing and the full abstract length theorem. Retain every
   surviving character case and exceptional prime.
   The [paired determinant theorem](../../notes/selmer-integral-frontier-even-detection.md)
   is proved over the original fraction field, and the
   [complete-equation argument](../../notes/selmer-integral-frontier-dual-detection.md)
   controls all modular solutions. The [integral assembly](../../notes/selmer-integral-frontier-integral-detection.md),
   [finite selection](../../notes/selmer-integral-frontier-finite-selection.md)
   and [coefficient-extension theorem](../../notes/selmer-integral-frontier-coefficient-extension.md)
   now prove the full simultaneous auxiliary choice under the original point,
   group and spectral hypotheses. The [ordinary local count](../../notes/selmer-integral-frontier-ordinary-local-count.md)
   now has one explicit constant for every truncation and auxiliary level
   at fixed data. Finish the remaining global and distinguished-place bounds
   and the actual patched automorphic modules and dimensions.
3. Construct the actual global arithmetic family, its original cubical
   biextension and geometric fibre comparisons, with the moduli separation
   and prescribed pointwise pure-period presentations. The exact CM point,
   original line and component then descend; properness and semiabelian
   extension give its integral map and exact tangent lattice.
   The ramified determinant line is constructed
   from those data. Apply the supplied boundary, tangent-slope,
   determinant-torsion and CM-period arguments. Identify the geometric
   sheets, Hodge metric and lattice; the
   [curvature theorem](../../notes/geometry-arithmetic-frontier-curvature-haar-mean.md)
   then gives the original arithmetic Haar mean. Both boundary energy
   limits and the [exact arithmetic metric variation](../../notes/geometry-arithmetic-frontier-exact-metric-variation.md)
   are proved, including metric locality and the rational-twist polynomial.
   The [compact-model theorem](../../notes/geometry-arithmetic-frontier-compact-model-stokes.md)
   identifies their original mixed integrals and proves zero vertical
   curvature everywhere. Energy concavity and the same rational-twist
   polynomial give the signed arithmetic boundary inequality. Construct
   its actual model and height inputs and bound the arithmetic section
   remainder.
   The full count is integrable by the
   [arithmetic first-moment theorem](../../notes/geometry-arithmetic-frontier-isotropic-integrability.md).
   Apply the [cusp theorem](../../notes/cusp-counting-mean.md) with these
   original measure and lattice identities. Identify the actual nef
   and birational section data and apply the
   [finite jet rank bound](../../notes/finite-section-jet-bound.md),
   retaining its excess-rank denominator. Use the
   [selected degree comparison](../../notes/selected-eigenspace-degree.md),
   [base-test supplier](../../notes/base-test-height-supplier.md),
   [tower reduction](../../notes/tower-intersection-reduction.md) and
   [mean-volume supplier](../../notes/mean-volume-supplier.md) in the same
   prescribed metrics.

Assemble signed fourth-power tables from these same constructions and
bound their weighted positive parts on arbitrarily late intervals.

The [GRH program](../grh/program.md) retains the general Dirichlet
target and every surviving compatibility condition. The RH case is a
substantially smaller first target, but its central arithmetic estimate is
still unproved in this reconstruction.
