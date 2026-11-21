# Current continuation checkpoint

Updated 21 November 2026. The conventional reconstruction is not a complete
proof of RH or Dirichlet GRH. Start from the preferred mathematical route,
then inspect only the relevant bounded source contracts. The repository is
the persistent record; the archive is a baseline, not a file to reload.

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

The [geometric combination](rh-geometric-combination.md) proves:

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

These deductions do not prove the actual growing-family height, section
remainder or theta-frame bounds. The old
[determinant and component analysis](geometric-core-lower-bound.md),
[covolume defect](covolume-defect-budget.md) and
[averaged signed arithmetic identity](averaged-error-budget.md) locate the
remaining same-lattice and same-map identifications.

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

## Next mathematical work

1. **Geometric core (W10).** Prove the actual two weighted height bounds and
   total Hilbert–Samuel surplus for the cuspidal section lattice with its
   prescribed Petersson metric. Carry the signed errors through determinant
   descent, type indices and discarded degrees. Retain positive ranks and
   uniformity in the growing family.
2. **Integral maps and global norms (W06/W08).** Supply nonzero integral
   theta maps, sharp auxiliary-level divisibility, normalized global
   theta/orbital-energy estimates and their frame moments for those same maps.
3. **Cohomology and assembly (W04/W02/W11).** Complete the remaining
   complementary-parity integral congruence bounds and prove the total
   normalized discrepancy estimate throughout the required whole windows.
   Optimize numerical envelopes only within parameter ranges that the
   same construction actually supplies.

The [RH program](../blueprint/rh-proof-program.md) is the shorter first case.
The [full program](../blueprint/full-proof-program.md) retains all eleven
work packages and the [46-field ledger](../blueprint/endpoint-field-ledger.md).
These are shared-object responsibilities, not independent assumptions.
The main manuscript and [short guide](../paper/guide/main.tex) are organized
by mathematics. The guide has a twelve-page editorial limit.

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
The [current integration record](../certificates/rh-continuation-review.json)
ties the reviewed arguments and inspected pages to their exact artifacts;
the [offline integrity check](../certificates/rh-continuation-integrity.json)
verifies the new source excerpts, current notes and compiled-document inputs.
Earlier certificates retain their original snapshot scopes.

```sh
python scripts/source_excerpt.py --atlas --source Main --search theorem
python scripts/reconcile_recovery.py --section 10
python scripts/check_rh_direct_transfer.py
python scripts/check_rh_weight_symmetry.py
python scripts/check_rh_geometric_combination.py
python scripts/check_transport_symmetry_defect.py
python scripts/check_rh_minimal_budget.py
python scripts/build_full_proof_program.py
python scripts/build_blueprint.py
python scripts/check_rh_continuation.py
```

The source reader verifies pinned bytes and limits output to 25 matches or
120 lines/12 KB. Large analyses stay local. Commit coherent results to main
promptly; bounded output never excuses weakening mathematical verification.
