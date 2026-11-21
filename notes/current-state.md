# Current continuation checkpoint

Updated 21 November 2026. Begin with the full proof program, then read one
bounded source contract or mathematical section. The conventional proof of
Dirichlet GRH remains incomplete.

## New reviewed continuation: RH transfer without symmetry

The [direct RH comparison](rh-direct-transfer.md) supersedes the proposed
search for exact pooled weight symmetry. The source's common sparse top set
forces separated top and non-top weights, so exact pooled symmetry is
impossible, even for first moments. The [source proof](rh-weight-symmetry.md)
records the precise eventual range and the verified contracts.

The successful replacement keeps the existing source design. Positivity of
the complete primitive-character kernel, including ramified primes, permits
a one-sided comparison with the lower endpoint of the thick weights.
Averaging translations before bounding this perturbation removes both the
field-degree and inverse-density factors from that error. The existing
large-scale QRH bound controls the actual thin samples. Thus the RH transfer
needs no symmetry assumption, no logarithmic-dispersion hypothesis and no
new bound for the auxiliary logarithmic derivatives. The remaining central
target is the normalized averaged arithmetic discrepancy, together with
the already identified signed quadratic companion and negligible numerical
errors. The same actual integral maps and geometric estimates are still
required.

The [geometric refinements](rh-geometric-combination.md) preserve the
coefficient of the section-degree error under descent, replace individual
lower height bounds by two weighted height moments, and average the sharper
frame cost before taking estimates. The [transport theorem](transport-symmetry-defect.md)
is retained as an alternative for other constructions; its absolute
majorant is too large for the current sparse-top weights.

These results have independent mathematical reviews and exact supplemental
checks. Source-byte checks are distinct from proof checks; no new Lean build
was run. The notes and certificates form a complete early checkpoint while
the main manuscript, short guide and blueprints are being reorganized.

## Full-proof structure is now the starting point

- [Full proof program](../blueprint/full-proof-program.md): eleven work packages,
  their exact goals, quantifier order, acceptance conditions and next tasks.
- [Endpoint field ledger](../blueprint/endpoint-field-ledger.md): all 46 fields
  of the source's coherent construction, assigned once. These share objects
  and are not 46 independent assumptions.
- [Complete source atlas](../blueprint/lean-source-atlas.md): every local source
  module and import edge, separate from the manuscript section atlas.
- [Endpoint analysis](lean-endpoint-backbone.md) and
  [global inputs](lean-global-inputs.md): source contracts and pinned evidence.

The source-wide plan supersedes the earlier list of four global bottlenecks.
It explicitly includes Galois/local compatibility, normalized global theta
matching, and geometric Hodge-bundle log-covolume bounds. The classical Galois
input is now adopted, and its original stable theta-lift supplier is optional.
The 96 recovered sections never exhaustively represented
these source interfaces. The main manuscript still has 98 section files:
96 recovered plus two new, with 14 alternatives and 84 in the preferred flow.

## Complete source coverage: what was actually checked

All 175,187 local Lean files at `jsmorph/rh` commit
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de` were read locally and matched to their
pinned Git blob hashes. The rebuilt import graph has 753,261 distinct local
edges, is acyclic, has depth 203, and reaches all local files from Main.
The 348 external import names are explicit boundaries; package internals were
not traversed. All-source import reachability does not mean every declaration
is essential to the target proof. No new Lean build or kernel replay was run.

The compressed complete graph is version controlled. The large source checkout
stays in ignored `build/lean-mirror`; no complete large file was printed into
conversation. The first source-wide checkpoint is commit `993681b`.

## Structural simplifications

The five exported targets reduce to one common right-half-plane nonvanishing
assertion. One classical Galois compatibility result is now reused in the
repeated source bundle fields and the Selmer windows. The complete source
family construction supplies a smaller sufficient interface: one compatible
host at each required scale, controlling an averaged arithmetic discrepancy
and explicit finite projection and transfer errors. A direct replacement
construction is still open; isolating this interface does not prove existence.

The final analytic loss need only tend to zero. The new independently reviewed
`thm:vanishing-loss-windows` and `cor:variable-loss-construction` permit
accuracy-dependent constants and interval shapes. The stronger
`cor:varying-positive-families` also permits new auxiliary characters and
positive weights at each accuracy, provided the target character or its
conjugate remains present. Each combination stays fixed throughout its own
arbitrarily late whole-window sequence. Uniformity in x within each fixed
accuracy remains essential; a common auxiliary family across accuracies is
unnecessary. See
[the proof and limiting cases](vanishing-loss-program.md).

The earlier exponent86-to14 K-theory substitution remains in force. Ten old
cohomological sections and four analytic alternatives are bypassed in the
preferred route, with their proofs retained in the appendix.

## Local residue comparison completed

The commutator matrix, the matrix of Schwartz marginals, the ordered mixed-word
congruence, and the finite-decay approximation are written and independently
reviewed. The new `ji-word-pairing` uses one positive reciprocal Haar constant
for every polynomial/word and auxiliary dimension. The source dictionary now
matches the operators, open cell, gauge and measure on the smooth coefficient
classes. Source lists recurse tail first, so chronological insertions reverse
the source list positions; operators themselves are not freely reordered.

`ji-unshifted-positivity` reuses the existing original-parameter terminal
criterion. Separation of original parameters does not imply the stronger
shifted separation, and that implication is not used. The theorem retains
the common cut, interlacing, sign and 1<=l<=k conditions. See
[the complete local dictionary](residue-source-dictionary.md).

This closes the local smooth-class interface, not every global form, arbitrary
merely finitely differentiable coefficient class, or growing-rank norm bound.
The supplementary exact 672-case mixed-word check is regenerated against the
new manuscript. The earlier scalar PBW and commutator reviews remain valid.

## Next research priorities

The latest completed reductions sharpen these priorities. The
[geometric core analysis](geometric-core-lower-bound.md) identifies the
actual cuspidal section lattice and proves determinant descent and a
component-degree averaging lemma with the actual Hilbert–Samuel surplus.
Its mean-volume/height input and total surplus bound remain open. The
[averaged error analysis](averaged-error-budget.md)
proves a zero-total-coefficient obstruction to a positive zeta-only
projection, and gives exact fixed-quotient descent with balanced fibres.
The three-mean/Jensen transfer and weighted-frame reductions have passed
independent review and are integrated into the main manuscript. Exact
pooled translation symmetry is not supplied by the inspected family
interfaces; it remains an explicit sufficient hypothesis. None of these
reductions claims the missing global construction.

The [RH-only analysis](rh-specialization.md) proves a short zeta positivity
criterion and traces the conductor-one specialization. The newly created
[didactic guide](../paper/guide/main.pdf) is organized by mathematical ideas,
with a twelve-page editorial limit. Its analytic, geometric and finite-group
explanations have separate independent reviews. It is not a completed RH proof.

For RH, order one makes the translation subgroup the whole finite group and
the subset shares automatic. The projection has exactly four characters.
Only one signed quadratic-companion mean must be bounded, together with the
geometric discrepancy, thin-weight term and logarithmic dispersion. Centering
the actual thick mean uses only the zeta derivative estimate; the source
conditions allow radius two. The auxiliary primes and field degrees still
grow. The [RH program](../blueprint/rh-proof-program.md) records the precise
savings and the surviving W01–W11 obligations.

1. W10: bound the actual mean-volume/height input and the total Hilbert–Samuel
   surplus for the cuspidal section lattice with the prescribed Petersson
   metric. Use exact determinant descent, type indices and discarded degrees.
   Positive component ranks and uniformity in the growing family are retained.
2. W02/W11: attempt the simpler RH construction first. Supply pooled
   translation symmetry for the actual maps and metrics, or prove a quantitative
   symmetry-error bound. Control the single signed companion, three mean-weight
   terms, logarithmic dispersion and weighted frame moments on whole windows.
   The complete normalized loss must tend to zero in exponent. The general
   Dirichlet target keeps its additional character quantifiers.
3. W06/W08: seed nonvanishing, sharp auxiliary-level divisibility, and normalized
   global theta/orbital-energy bounds for those same maps. Complete the remaining
   W04 complementary-parity integral congruence bounds in parallel.

W05 is closed as a cited classical input with proved normalization and
transport comparisons. The [adoption proof](classical-galois-substitution.md)
preserves one global representation before all local correspondences and
period models. Independent theta, integral and geometric branches remain.
No exact count of source files removed is inferred from the import graph.

The next possible refinement is a transport-distance bound for defects of
pooled symmetry: differentiation of the scaled corrected sums cancels their
linear logarithmic-derivative terms. This direction is recorded for further
proof; no reviewed quantitative transport theorem or canonical theta
transport construction is claimed in the present checkpoint.

## Recovery and bounded resumption

The supplied originals are byte-identical to the preserved archive. All 622
bundle files and 621 manifest entries remain verified; all 96 recovered sections,
1,522 labels, 646 result environments and 611 proofs are preserved. This is not
an independent review of all those proofs. Prior unavailable chats are not
represented as recovered.

```sh
python scripts/scan_lean_backbone.py --module Main
python scripts/source_excerpt.py --atlas --source Main --search theorem --offline
python scripts/reconcile_recovery.py --section 3
python scripts/build_full_proof_program.py
python scripts/build_blueprint.py
```

The atlas reader can select any pinned local module by its exact name or unique
path suffix. It verifies the bytes and prints at most25 search matches or120
lines/12KB. Run large analyses locally and retain concise results, dependencies
and evidence in version-controlled files. Commit coherent results to main
promptly; never weaken mathematical verification to save context.

## Completed continuation: averaged arithmetic target and covolumes

The new [one-construction target](one-construction-target.md) proves that the
final character comparison needs an averaged arithmetic discrepancy and
explicit finite projection and transfer errors. The six arithmetic clauses,
the complete geometric-core clauses, eleven size/slope requirements and
twenty-seven scalar windows of the source supplier are now inventoried.
The manuscript also proves a weighted lower-estimate lemma, keeping the actual
nonlinear frame cost and avoiding unnecessary preliminary uniform envelopes.

The [covolume defect](covolume-defect-budget.md) is an exact orthogonal splitting
identity with a discarded mean-degree and integral-index budget. Suitable
polynomial decay of the exceptional rank can suffice when the other terms
have the stated growth; small rank alone is insufficient. Both meaningful
counterexamples and the normalization to the source slope are retained.

## Completed continuation: classical Galois substitution

The [classical local correspondence inventory](classical-local-correspondence.md)
proves all fifteen full laws and the additional Artin and epsilon witnesses.
The [global period dictionary](galois-period-dictionary.md) matches the
automorphic, weight and period-model quantifiers. Both have independent
reviews. Together with the depth-zero type formula, local preimages and
universal weak-correspondence transfer, they supply the entire required
Galois row. Above the coefficient prime, zero target monodromy suffices by
monodromy dominance. The separate original Galois-construction supplier is
now an alternative; the manuscript states the classical theorem and its
period-realization lemma in ordinary mathematics.

The early partial checkpoint was committed as `e48d334`. All subsequent
results carry persistent proofs, exact source ranges, hashes and the scope
of independent review. No new Lean compilation or kernel replay is claimed.
