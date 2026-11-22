# Current continuation checkpoint

Updated 22 November 2026. The conventional reconstruction is not a complete
proof of RH or Dirichlet GRH. Start from the preferred mathematical route,
then inspect only the relevant bounded source contracts. The repository is
the persistent record; the archive is a baseline, not a file to reload.

## Two manuscripts and concurrent research

The [ordinary RH manuscript](../paper/rh/main.tex) and
[Dirichlet GRH manuscript](../paper/grh/main.tex) now have separate route
folders, with corresponding [RH](../blueprint/rh/README.md) and
[GRH](../blueprint/grh/README.md) programs. The common technical chapters
remain in `paper/sections/`; small proofs included by both papers belong
in `paper/shared/`. The [shared-results index](../blueprint/shared/README.md)
keeps the two applications and their extra hypotheses explicit.

The [node counts](../blueprint/progress.md) distinguish finished stated
implications or adopted inputs from open construction hypotheses. Moving
files or adding a node is not recorded as closing an existing open node.
The continuation was recovered from main through `0ffbc6f7e190d4b007eb1109df215857539c60f5`,
including its preceding geometric, sampling and cohomological checkpoints.
The source-import atlas and documentary section atlas have no proof
completion score. The published baseline is RH 6/9 and the GRH technical
map 17/31; the generated progress table carries the current values.

## Preferred RH route: no weight symmetry

The [direct RH comparison](rh-direct-transfer.md) is the active continuation.
The complete primitive-character kernel is nonnegative, including at ramified
primes. Compare the actual thick weights with their common lower endpoint,
then average translations before bounding the perturbation. This removes
both the field-degree and inverse-density factors from that error.
The existing uniform QRH bound handles the actual thin samples at their
larger arguments. It still concerns the whole thin character family,
including the separately corrected principal character.

The resulting zeta estimate consists of the normalized averaged arithmetic
discrepancy, one signed quadratic companion, and negligible size and
centering errors. The companion can use the manuscript's simultaneous
quadratic selection on an interval covering every shifted sample, under its
explicit uniform QRH hypothesis. There is no new pooled symmetry,
logarithmic-dispersion or thick logarithmic-derivative obligation.
The original weight lower endpoint gives centering radius one.

The [general quotient version](positive-kernel-transfer.md) applies to every
subgroup used in the Dirichlet construction. Its thick error depends on
four times the quotient index, which is the fixed target character order
in the existing program, instead of the growing ambient group. It does not
remove the signed projection or the all-character thin estimate.

The [source audit](rh-weight-symmetry.md) proves that the common sparse top
set actually forbids exact pooled symmetry, even for first moments, once
it is proper. Simultaneously translating top labels and weights leaves the
character phase unchanged. The [transport theorem](transport-symmetry-defect.md)
removes the field-degree factor from a quantitative alternative, but its
absolute majorant is too large for the current separated weights. These
are preserved results and limits, not tasks to repeat. The old three-mean
and complete-top projections remain conditional alternatives for a changed
construction; the preferred direct route needs neither.

## Smaller geometric and frame budget

The preferred [direct section-degree argument](geometric-degree-frontier.md)
uses the short integral sections already supplied for the same component
lattices. Their lower degree bound removes the separate negative-height
moment. Summing the exact degree-weighted volume comparison first supplies
one mean directly, without the earlier change of weights. The raw signed
version removes all heights from its remaining cost, while retaining the
actual section ranks and twist costs. A mean-volume estimate and an explicit
rank/surplus bound still have to be supplied.

The [mean-volume supplier](mean-volume-supplier.md) now isolates the
required normalized arithmetic intersection inequality for the selected
towers and weights, together with the prescribed norm and counting
comparison. Equal component volumes then give the mean by exact division.
An elementary finite-prime bound improves the additive allowance from
120 to 80. The auxiliary volume limit fixes each datum before taking the
section power to infinity, so it needs no uniform finite convergence
threshold. Uniform intersection control and the separate finite section
estimate remain unresolved; quasi-RH and no-Siegel bounds only control
the arithmetic error parameter in that geometric inequality.

The [tower-intersection reduction](tower-intersection-reduction.md) now
eliminates the two common scalar coefficients using a single normalized
Grassmannian test. The exact formula retains the block contrast, the factor
N/p and the smaller test remainder 8/(5fq). The actual anchored weights
need not have zero sum. Their central translation incurs an exact signed
determinant term, including the cutoff metric's finite-place correction;
no cancellation with a different period normalization is assumed.
The [classical height step](base-test-height-supplier.md) supplies this
test from all-point height floors and the signed cusp comparison using
only reciprocal perturbations and a one-sided limit. The
[actual point-height frontier](actual-point-height-frontier.md) reduces its
arithmetic supplier to a sum of degrees of the selected small image
eigensublattices. The [selected-degree identity](selected-eigenspace-degree.md) retains
both favorable integral indices and gives a two-case proof from only the
signed total conjugate imbalance. It also retains the exact selected
abelian rank f(m-r). The prescribed integral/metric comparison and cusp
mean remain required. A bare total
Faltings-height lower bound does not supply the selected degrees, and
the inspected published tangent-slope estimate does not imply the source's
stronger universal logarithmic interface. No claim that that interface is
false is made.

The [theta-jet reduction](theta-jet-slope-reduction.md) replaces the
longer tangent argument by leading-jet integrality, a flag determinant,
the product formula and very ampleness of the third tensor power. A much
smaller theta power suffices. The
[classical absolute Siegel supplier](absolute-siegel-supplier.md) supplies
the short integral vector in the same metric after finite extension;
principalizing its saturated line preserves the exact height. The
arithmetic and archimedean theta inputs are now supplied by the
[Moret--Bailly comparison](moret-bailly-theta-supplier.md), on the prescribed
tangent lattice with its exact metric. Together these arguments prove
the required tangent-slope bound with absolute constant 12. The
[remaining point-height comparison](remaining-point-height-comparisons.md)
also supplies the finite-prime allowance with constant 16 at the eventual
scales and the scalar period bound. The
[same-lattice determinant bridge](geometric-flat-determinant.md) now has
a direct proof using algebraic frame covariance, local Gram and lattice
norms, flat base change and the product formula. The different/conductor
correction cancels exactly. Conditional on the actual flat-family and CM
evaluation, the signed total is `(2R-n) P_E/2`, independent of toric rank
in constant signature. The flat-family and CM evaluation, signed cusp
mean and independent finite section estimate remain. Grouping
eigenspaces does not permit replacing the unramified host by the ramified
quadratic field; see the [host obstruction](quadratic-host-descent-obstruction.md).

The finite-place comparison now has a shorter
[character-degree proof](flat-family-finite-place-frontier.md): the Hodge
and conjugate filtrations force degree zero under Frobenius, and a
composition series retains the multiplicities of a ramified coefficient
algebra. The [integral coefficient-freeness proof](boundary-hodge-freeness.md)
identifies the proper formal module directly with a universal-extension
tangent module. Its functorial Witt lift and a three-step toric
filtration supply freeness, including ramified coefficient primes, once
the actual semiabelian quotient and pullback line bundle are identified.
The same local-stalk argument retains the prescribed lattice. The
[biextension construction](biextension-conjugate-filtration.md) now supplies
both Hodge and conjugate filtrations on it. Pointed first-order sections,
multiplication by the residue characteristic, and an alternating pairing
give a direct proof, including characteristic two. Compatible integral
formal charts on each test curve suffice; the geometric argument for
injectivity is needed only on its residue fibres. This removes the power-map
surjectivity hypothesis from this particular conclusion and requires no
extra global semiabelian scheme along the whole curve. The actual compatible
charts and original pullback line with scheme-theoretic self-duality remain
inputs. A tensor power with a different polarization cannot replace that line.
The [determinant torsion and vertical rigidity](determinant-torsion-rigidity.md)
now strengthen this calculation: the two filtrations give an explicit
torsion exponent for the character determinant, and a short effective-divisor
argument gives one normalized finite order on the connected fibre.
Its denominator divides the gcd of the fibre multiplicities. These
arguments retain ramified coefficient lengths and all actual-model
hypotheses. Identifying the boundary lattice and evaluating the common
order at the prescribed CM point remain; constancy does not make it zero.

The [CM integral-eigenframe calculation](cm-integral-eigenframes.md)
is now exact by relative trace duality: the integral character line is
the relative different times the generic eigenline. Conjugation
invariance gives equal finite norms for any semilocal different
generator, so this local calculation needs no real generator and no
finite unramifiedness of the CM extension over its real subfield.
The global construction's separate host conditions remain. Applying the
calculation still needs its actual integral product frame and CM point;
the archimedean period evaluation is separate.

The preferred [trace slope comparison](one-sided-frame-slope.md) now
uses one source deficit and one target excess, both measured by the
trace of a positive part. These may be small even when operator norms
or squared-energy errors are large. The source centered term is retained
where sharper, and one takes the minimum with older valid penalties.
The source slope spread, target lower slope and actual normalizers remain.
A perfect analytic frame still does not supply the intermediate geometric
component degree or the separate counting, divisor and quotient losses.

The [separation of code size and arithmetic height](code-rate-height-separation.md)
uses the source's existing quantified order to choose the code exponent
independently. Under the same full-map estimates and restrictions, its
frame cost is at most the source slope spread plus a decaying multiple
of the original height scale. This is a proved parameter improvement;
the global estimates and geometric height conditions are still inputs.

The positive spectral trace of the target operator equals that of the
normalized source block Gram matrix. Thus the full-period orbital
interface can supply the new target trace estimate without a new
common-target unfolding. Its exact expansion and convergence remain
hypotheses; signed terms are combined before taking the positive part.
The source trace deficit needs its own estimate. The actual arithmetic
spectral-tail bound is not supplied by positivity or total mass alone.

The [exact period-spectrum models](redundant-period-spectrum.md) show
why redundancy forces a large nonidentity contribution: the tail must
be measured above the mean eigenvalue. A single
[integral incidence construction](basis-invariant-trace-obstruction.md)
now proves the stronger limitation. It satisfies the diagonal and
pairwise estimates with zero error, yet retains the asymptotically sharp
square-root trace loss under every invertible comparison basis. The
same fixed arithmetic lattices have zero map height and attain the
slope loss. Small arbitrary source and target cuts retain an explicit
part of the obstruction. Thus basis changes alone cannot halve the
code redundancy exponent. These are countermodels to a matrix
implication, not to the actual theta construction. Keep the smaller
valid trace or energy penalty and seek the calibrated estimate for the
actual period maps; the ambient projector does not identify their sum.

The [common-unipotent reduction](common-unipotent-periodization.md)
identifies every word's unipotent group with one fixed group; the extra
condition on its distinguished vector is redundant. Its characters may
still repeat, and its stabilizers, quotient measures and normalizing
volumes remain distinct. A precise quotient isometry puts the original
scalar seeds in one Hilbert space, where the normalized synthesis is
arithmetic periodization with every rational double-coset term retained.
The actual infinite covering explains why ordinary Fourier orthogonality
does not supply its global norm. A weighted summation criterion now states
the needed calibrated bound on the finite seed spaces with their exact
source and target restrictions. No weights attaining that bound, or
global period estimate, have yet been supplied.

The actual source restrictions can be carried through positive retained
mass and then an ambient target comparison, preserving the discarded
rank times source-spread term. Alternatively, the full trace-compression
lemma estimates both final restrictions. Every application uses the
same restricted lattices, maps and common target basis. The source-only
formula has fewer formal mass hypotheses, but its coarse upper bound
can be trivial in the omitted regime; no automatic quantitative gain is
claimed there.

The [aggregate energies](averaged-theta-energy.md),
[centered frame estimates](frame-degree-compatibility.md), and
[joint uniform period bound](centered-global-energy-reduction.md) remain
valid alternative suppliers. The [actual source bridge](rh-centered-frame-bridge.md)
retains the correct slope units and nonframe losses. The
[finite-symmetry calculation](finite-symmetry-energy.md) still excludes
an unsupported appeal to ambient symmetry on the retained target.

The earlier [geometric combination](rh-geometric-combination.md) proves
useful general alternatives:

- Covering descent preserves the coefficient of the section-degree error.
  Under the same source scalar contracts the numerical constant improves
  from twice that coefficient plus nine to that coefficient plus seven;
  the exact formula retains the actual rank ratio.
- A weighted mean height and weighted negative-height moment suffice for
  the component estimate. The optimized bound retains the signed total
  Hilbert–Samuel surplus, excess-rank and twist costs. Uniform pointwise
  lower heights are one sufficient supplier, not an intrinsic condition.
- Average the refined frame penalty before bounding it. The resulting
  source-spread and target-height moments retain their correlations and
  the rank-loss and diagonal-error denominators.

These deductions do not prove the actual growing-family mean-volume,
section remainder or theta-energy bounds. The old
[determinant and component analysis](geometric-core-lower-bound.md),
[covolume defect](covolume-defect-budget.md) and
[averaged signed arithmetic identity](averaged-error-budget.md) locate the
remaining same-lattice and same-map identifications.

## Cohomology: finiteness is supplied, a uniform budget remains

[Classical global duality and even K-groups](qualitative-selmer-finiteness.md)
give an injection of the actual strict Selmer dual into the corresponding
finite even K-group. The CM host condition covers the prime two. For a
fixed host and finite twist range, the all-prime Selmer sum has finite
support and is bounded by the logarithm of a finite product of K-group
orders. No numerical prime cutoff or useful growing-family bound follows
from this qualitative statement.

The [finite-place reduction](finite-twisted-place-budget.md) keeps only
the actual twisted residue primes and their ramification-inertia fractions.
Generator primes use their already aggregated bound, with no extra fraction.
The local congruence comparison then needs one weighted finite Selmer budget.
The [two-primary character reduction](two-primary-selmer-reduction.md)
omits the nontrivial odd-order branch for RH, and a joint harmonic count
improves the resonant prime--twist exponent. The trivial character,
complementary parity, exceptional primes and integral local bounds remain.
The existing manuscript already provides an opposite-parity all-odd-prime
estimate (Theorem14.1 in the current GRH PDF); this supplier is to be
applied with the exact source group and local conditions, not reproved
merely because the odd-order branch has disappeared.
The source's LitThin is an analytic short-interval input, not cohomology.
The [coarse-bound assessment](coarse-selmer-budget.md) quantifies why the
existing exponent-14 bound, applied directly to the growing host, does
not fit the allowed budget. It remains useful after the existing
common-interval descent; no lower bound on actual Selmer sizes is inferred.

For RH, the [residual decomposition](rh-selmer-residual-budget.md) applies
the supplied cases and isolates three remaining sums. The
[integral Selmer product](rh-selmer-product-criterion.md) identifies those
sums exactly with one weighted logarithm of orders of finite integral
direct factors. Family averaging changes only the prime weights after
the actual common-host identifications. Its exponent-one part is relative
growth above a fixed lower layer of the two-power cyclotomic tower.
The retained parity gives trivial zeros at the ordinary special values,
so a nonzero Bernoulli-value formula does not supply the missing order
bound. A valid substitute must retain its regulator or integral
comparison and growing-family uniformity.

The [conormal pairing](rh-selmer-conormal-pairing.md) gives a shorter
lower deformation comparison. For the same marked model, the strict
Selmer group embeds linearly in the dual of its finite negative-weight
conormal quotient. Ambient torsion is removed before imposing the
global equations; the new torsion they create is retained. Compatible
normalized cocycles give one map at all coefficient levels, controlling
the exponent and each elementary divisor as well as total length.
Actual model existence and the upper graded-intersection estimate remain
separate inputs. The ordinary-RH specialization retains all five local
weights; its cyclotomic twist does not become self-inverse.

The [upper numerical length calculation](rh-selmer-euler-determinant.md)
also has a short determinant proof. On the actual finite multigraded
weight module, kernel and cokernel torsion cancel exactly. The remaining
Euler characteristic is a determinant valuation, equivalently a sum
over distinct degree-zero characters with their exact multiplicities.
This preserves a sharper intermediate inequality before the coarse
power-of-two bound. The graded specialization, eventual support and
local multiplicity estimates linking this module to the conormal
quotient remain genuine requirements.

The [leading quotient and mixed count](rh-selmer-mixed-count.md) now have
elementary proofs. The leading coefficient image is a finite free lattice;
rational tangent surjectivity supplies its entire generic monomial space.
This proves the exact Hilbert function without assuming flatness of the
original deformation quotient. A generating-function cancellation gives
the constant mixed difference and an explicit sufficient degree box,
including the smallest admissible weight counts. The scalar factor in the
lower bound is therefore accounted for. The
[graded Koszul comparison](rh-selmer-koszul-comparison.md) now supplies
eventual positivity, passage to the leading quotient, the upper quotient
inequality and exact extraction of the integral equation factors. Its
short proof uses a finite graded prime filtration and ordinary exact
sequences, retaining all higher homology and torsion kernels. It assumes
no global flatness, regular sequence, infinite residue field or dimension
bound. The remaining lower-side condition is a precise admissibility
power containment from the geometry of the equation scheme. Actual
marked-model existence, eventual support and generic multiplicity bounds
for the upper determinant remain separate.

The [resultant construction](rh-selmer-resultant.md) supplies the elementary
integer in the nonresonant orbit estimate with full integrality,
nonvanishing, simultaneous valuation domination and an explicit size
bound. Two auxiliary integers bounding the same orbit may be replaced
by their corrected greatest common divisor; the exceptional-prime factors
are retained. This is a sharper exact bound, not a proved uniform saving
for the actual integers. The trace-to-Selmer deformation comparison and
the remaining cases are still required.

The [arithmetic frontier](rh-selmer-valuation-frontier.md) now locates the
missing bridge in the integral negative-weight deformation comparison.
Two exact examples rule out shortcuts from the currently available
hypotheses: trace classes alone allow a corrected common divisor whose
logarithm is linear in the twist, and a finite weight-zero algebra with
rigid generic fibre can still hide arbitrary integral negative-weight
torsion. These are limitations of those hypotheses, not counterexamples
to the actual automorphic construction or to its desired Selmer estimate.

## Scalar acceptance conditions

The [scale-averaged criterion](scale-averaged-criterion.md) weakens the
final analytic target further. At each fixed accuracy it suffices to
control a weighted positive-part integral on arbitrarily late whole
windows. The combined signed arithmetic budget may first be averaged
over a fixed nearby range of scales: its transform multiplier preserves
every detecting pole. This permits cancellation before taking the
positive part. Pointwise bounds remain a sufficient supplier, but are
not intrinsically necessary. The arithmetic comparison must hold almost
everywhere on the slightly expanded windows used by local averaging.
An uncontrolled signed mean or a small unweighted exceptional proportion
does not suffice; explicit counterexamples are preserved in the note.

The [minimal budget](rh-minimal-budget.md) keeps the four normalized
arithmetic terms separate. With the actual source rank ranges, the old
conditional envelope improves to a factor 36 times a power with exponent
one half plus `(C+33/16) epsilon`. The explicit constant can remain.
The refined frame supplier is bounded by four thirds of its two
nonnegative correlated moments. Existing word-count entropy is already
negligible at the source scales.

A polynomial thin scale suffices for the final analytic transfer when
the conductor logarithm and dimension have polynomial growth. Replacing
the source's exponential scale, or adopting the formally optimal smaller
chain rank, has not been justified for the other arithmetic clauses.
These are exact acceptance conditions and limitations, not new constructors.

The [finite-table theorem](finite-window-sampling.md) is now the smaller
construction interface. At each fixed accuracy and each chosen large
integer interval, construct a finite table bounding the analytic target at
all sampled integers. The exact positive averaging matrix preserves signed
cancellation, and the interpolation error tends to zero. Tables may differ
on overlaps, so no measurable family of arithmetic choices is needed.
An almost-everywhere comparison is not silently promoted to integer data.
The [square-grid refinement](square-grid-sampling.md) needs only square
arguments. Its positive averaging coefficients preserve the signed
budget, and its interpolation error tends to zero for every exponent
strictly above one half. On a window from Y to its b-th power it reduces
the table size from order \(Y^b\) to order \(Y^{b/2}\), without changing
the analytic target. The preferred
[fourth-power refinement](fourth-power-sampling.md) uses the actual convex
ramps and concave correction rather than only a derivative bound. It
reduces the table size further to order \(Y^{b/4}\). Positive affine
averages retain signed cancellation even between adjacent rows. The
interpolation tail tends to zero, with no logarithmic factor for zeta or
any nonnegative arithmetic kernel. The RH manuscript gives the shorter
zeta proof; the GRH manuscript gives the general character-combination
theorem. Neither changes the existing node totals.

## Next mathematical work

1. **Geometric core (W10).** Use the now supplied tangent-slope estimate
   on the prescribed lattice and the explicit determinant bridge.
   Identify the actual compatible boundary charts, their original
   semiabelian fibre pullback line and coefficient character identity.
   The integral Hodge comparison, both filtrations, coefficient freeness,
   determinant torsion and vertical rigidity are now supplied under these
   hypotheses. Establish the CM product frame and period evaluation;
   retain the signed signature difference and exact selected abelian
   rank, and supply the signed cusp mean and independent finite
   section-rank/surplus estimate. The scalar prime and period bounds
   are already supplied; they are not the remaining geometric gap.
2. **Integral maps and global norms (W06/W08).** Supply nonzero integral
   theta maps, sharp auxiliary-level divisibility and positive normalizers.
   Bound their calibrated global trace costs or a sufficient refined-energy
   cost, carrying actual restrictions and arithmetic heights throughout.
   Pairwise matrix bounds do not automatically improve to a linear trace bound.
3. **Cohomology and assembly (W04/W02/W11).** Quantify the finite weighted
   Selmer product on the actual twisted places, retaining the integral local
   comparisons and surviving character cases. The elementary resultant
   supplier does not prove the trace-to-Selmer estimate: construct the
   marked models, use the proved compatible conormal pairing and exact
   numerical and Koszul comparisons, and supply their actual admissibility,
   support and multiplicity bounds. Assemble the signed
   finite fourth-power tables on arbitrarily late intervals, with all exponent losses
   and constants fixed at each accuracy.

The [RH program](../blueprint/rh/program.md) is the shorter first case.
The [GRH program](../blueprint/grh/program.md) retains all eleven
work packages and the [46-field ledger](../blueprint/endpoint-field-ledger.md).
These are shared-object responsibilities, not independent assumptions.
The main manuscript and [short guide](../paper/guide/main.tex) are organized
by mathematics. The guide has a twelve-page editorial limit.

The [project assessment](project-assessment.md) distinguishes the audited
milestone count from an unsupported percentage of a completed proof, and
records conditional paper-space budgets. The
[RH construction frontier](rh-construction-frontier.md) explains why four
characters do not bound integral indices or discharge the surviving source
clauses. Its exact paired-construction alternative is not adopted without
an actual paired supplier and signed relative estimate.

## Established structural and local reductions

- All five exported targets reduce to right-half-plane nonvanishing.
  Only total exponent loss tending to zero is necessary. Constants and
  window shapes may depend on accuracy, and a positive auxiliary family
  may change with accuracy while retaining the target character. Each such
  family stays fixed throughout its own arbitrarily late whole-window
  sequence. See [vanishing loss](vanishing-loss-program.md).
- The K-theory replacement reduces exponent 86 to 14 and moves ten older
  cohomological sections and four analytic alternatives out of the preferred
  route. The manuscript has 98 section files: 96 recovered plus two new,
  with 84 in the preferred exposition and 14 alternatives.
- The classical Galois substitution supplies W05, including all fifteen
  local laws, the global period dictionary and one common representation
  across the required correspondences. Its original stable theta-lift
  supplier is optional. Independent theta and geometric branches remain.
  See [the adoption proof](classical-galois-substitution.md).
- The local residue comparison is proved on the stated smooth classes:
  commutator matrix, Schwartz marginals, ordered mixed-word congruence,
  finite-decay approximation and one positive reciprocal Haar constant.
  Source lists recurse tail first; operators cannot be freely reordered.
  Original admissible parameters are retained without assuming shifted
  separation. See [the dictionary](residue-source-dictionary.md).
  Growing-rank global norm bounds are not supplied by these fixed-word
  local identities.

## Source, recovery and verification scope

The prior complete import audit read and matched all 175,187 local files at
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. Its preserved graph has
753,261 distinct local edges, no cycles, depth 203, and all files reachable
from Main. The 348 external import names remain boundaries; package internals
were not traversed. Reachability does not identify indispensable declarations.
The source atlas and its compressed graph are version controlled. This
continuation rechecks only the selected new source files and bounded passages,
not the entire old traversal. No new Lean build or kernel replay was run.

The recovery archive preserves all 622 bundle files and 621 manifest entries,
96 original sections, 1,522 labels, 646 result environments and 611 proofs.
Preservation is not an independent review of every proof. Unavailable chats
have not been invented as recovered work. The
[recovery crosswalk](recovery-crosswalk.md) supplies bounded resumption cards.

New mathematical results have independent reviews and exact supplemental
checks. Certificates distinguish source-byte identity, written proof review,
finite verification and unresolved construction hypotheses. Important early
results are already committed; the polished integrated checkpoint includes
updated TeX, compiled PDFs and regenerated proof maps.
The [current mathematical review](../certificates/continuation-review-2026-11-22.json)
ties the newly reviewed arguments to their exact artifacts. The
[integration record](../certificates/continuation-integration-2026-11-22.json)
records the recovered proofs, manuscript inputs, built PDFs and inspected
pages. Source-byte integrity, exact finite checks and mathematical review
remain separate. Earlier certificates retain their original snapshot scopes.

```sh
python scripts/source_excerpt.py --atlas --source Main --search theorem
python scripts/reconcile_recovery.py --section 10
python scripts/check_rh_direct_transfer.py
python scripts/check_rh_weight_symmetry.py
python scripts/check_rh_geometric_combination.py
python scripts/check_transport_symmetry_defect.py
python scripts/check_rh_minimal_budget.py
python scripts/check_geometric_degree_frontier.py
python scripts/check_averaged_theta_energy.py
python scripts/check_rh_construction_frontier.py
python scripts/check_finite_symmetry_energy.py
python scripts/check_frame_degree_compatibility.py
python scripts/check_rh_centered_frame_bridge.py
python scripts/check_mean_volume_supplier.py
python scripts/check_finite_window_sampling.py
python scripts/check_two_primary_selmer_reduction.py
python scripts/check_selected_eigenspace_degree.py
python scripts/check_finite_twisted_place_budget.py
python scripts/check_qualitative_selmer_finiteness.py
python scripts/check_theta_jet_slope_reduction.py
python scripts/check_absolute_siegel_supplier.py
python scripts/check_redundant_period_spectrum.py
python scripts/build_full_proof_program.py
python scripts/build_blueprint.py
python scripts/check_rh_continuation.py
```

The source reader verifies pinned bytes and limits output to 25 matches or
120 lines/12 KB. Large analyses stay local. Commit coherent results to main
promptly; bounded output never excuses weakening mathematical verification.
