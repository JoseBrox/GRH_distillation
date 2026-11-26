# Audit of the Sernau–Anthropic GRH rewrite

Date: 26 November 2026. Source revision:
[`lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207`](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207).
Our comparison starts at `GRH_distillation@74d18f39aa5db2b02e1ca83078b57768c5d92885`.

## Scope and initial conclusion

**The exported theorem is Dirichlet GRH**, with ordinary RH as a special
case. The declarations quantify over every positive integer modulus and
every complex Dirichlet character, including imprimitive characters.
They use Mathlib's `DirichletCharacter.LFunction`, rather than a newly
defined substitute. The half-plane statement excludes the principal
character's pole at 1. The zero-on-the-line statement concerns the open
critical strip. General Hecke characters over number fields are absent
from these exported statements.

Evidence: [`grh/src/Statements.lean`, lines 1–16](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L1-L16),
and [`grh/src/Main.lean`, lines 4–22](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L4-L22).
The compact edition exposes the same propositions.

**This is a substantial rewriting of the same underlying method, not an
independent elementary proof.** The repository credits Levent Alpöge and
Claude for the original proof and describes a collaboration with Anthropic
for the shortening. The readable edition organizes the argument around
three statements about the same forms and lattices:

1. Short integral source forms have short, almost integral images.
2. A small collection of translates supplies sufficiently many independent
   images.
3. A product-formula argument with coefficient-prime-dependent twists
   forces the corresponding corrected covolume to be large.

The common main term cancels. See [`grh/GUIDE.md`, section 1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/GUIDE.md#L5-L29)
and [`grh/src/New/Reduction/MainInequality.lean`, lines 5–67](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean#L5-L67).

The determinant lower-bound route is a serious candidate to replace our
W10 geometric supplier in the preferred plan. This changes a dependency;
it does not prove the previously open W10 assertions. The theta identities,
global second moments, denominator control and exact normalizations remain
substantial mathematics.

## Verification boundary

The upstream README reports builds, an axiom list containing only
`propext`, `Classical.choice`, and `Quot.sound`, and independent checking
of the readable edition. These are **upstream reports**, not checks
reproduced by merely reading the README. It also explicitly says that no
mathematician has read the whole proof and that no conventional paper is
provided. An axiom inventory, an import inventory and a successful build
answer different questions from a human reconstruction.

The [independent static audit and local execution record](lsernau-formal-audit-2026-11-26.md)
now record the actual checks. A lexical scan found no watched placeholder,
axiom or environment-mutation token in production source; the five
intentional `sorry`s in each Comparator challenge file are outside the
production imports. The statement files of both editions are identical.
The pinned Mathlib definitions were inspected. No result is promoted in
our human proof maps solely from theorem names or upstream reports.

Internal lemmas with structure hypotheses are not, by that fact alone,
gaps in the formal proof. The final exports have no such extra premises;
a complete formal audit follows their actual suppliers. For our human
reconstruction, those suppliers still need written proofs or correctly
matched conventional references.

## Comparison with our previous plan

The rewrite provides explicit source implementations of the entire
advertised chain. Our previous conventional reconstruction had written
many useful local and conditional results, but still lacked compatible
global theta, norm and geometric suppliers. It would be misleading to
describe the old human reconstruction as more complete than this formal
development merely because our prose is easier to read.

| Question | Audited conclusion |
| --- | --- |
| Same theorem? | Yes: ordinary RH and Dirichlet GRH. Neither repository's present human reconstruction establishes general Hecke GRH. |
| Same method? | Same Alpöge origin and arithmetic/theta/prime-sum idea, with major reorganization and different intermediate arguments. |
| Smaller source? | The reproducible lexical inventory counts 299,902 nonblank code lines in 803 readable source files and 76,149 in 794 compact source files. These are code measures, not human proof lengths. |
| Better plan? | Yes, as the present research and exposition choice: A/B/C exposes the cancellation and supplies a concrete determinant alternative to the unfinished W10 route. This is not a proof of optimal simplicity. |
| Can we merge it with ours? | Yes at exact interfaces: retain our one-sided analytic reasoning and integral/trace refinements, and prefer the new determinant and selected-twist structure. Old and new fields and lattices are not silently identified. |
| Any decisive flaw found? | None in the audited statement boundary or the abstract endgame and selected ordinary reductions. This is not an exhaustive human verification of all 803 readable source files. The local formal execution scope is stated separately. |

The new source uses some deep mathematical results in forms tailored to
its proof. Its own `REFERENCES.md` says that only some references were
checked: 228 citations were in its comparison, 66 with directly confirmed
locations, and citations in 122 other files were outside that check.
That is not by itself a defect in a closed formal proof. It does mean
that `Lib` cannot be treated as a list of already verified conventional
black boxes when extracting our paper.

## Strengthenings proved before integration

The [determinant extraction](../notes/lsernau-mathematical-extraction-2026-11-26.md)
proves the product-formula comparison for one common determinant with
independent local choices, a combined correction, averaged archimedean
control, exact Schur-complement cost and signed missing-rank term. It
also gives short compression and clearing lemmas and exact examples
showing why the index's coefficient two and complement cannot be dropped.

The [spanning/prime note](../notes/lsernau-moment-and-prime-reductions.md)
proves an arbitrary weighted-family covering theorem from a *mean*
positive source deficit and one covariance moment, with an improved
affine recurrence and logarithmic selection cost. Its fixed-modulus
prime-sum argument checks the additive constant and removes the larger
cutoff error without a moving-conductor estimate. Finite-height twist
selection remains a separate analytic supplier.

The [Hecke transfer](../hecke/notes/lsernau-transfer-plan-2026-11-26.md)
proves the exact abelian-induced boundary of the immediate Dirichlet
reduction and a zero structural-defect theorem for suitable odd-order
anticyclotomic coefficient lines. The latter includes both cubic sectors
at every coefficient prime at least 5. Small lengths after additional
twists still depend on the general twisting theorem; the old untwisted
lengths and the determinant-ratio geometry are not supplied.

These ordinary mathematical proofs received independent parallel reviews
within this session. Those reviews are not an external human audit or a
formalization of our new lemmas.

## Adopted plan and remaining work

The **[revised proof plan](../blueprint/merged-proof-plan.md)** is now the
preferred continuation. Reconstruct the selected-twist theorem and its
integral denominator application; build the exact common theta diagram;
establish its scalar moments, one-lift and chain determinant ratios; then
assemble the signed budget and exact prime-sum endpoint. Use the
conductor-one instance first, then the arbitrary fixed conductor.

The old wall/divisor and general untwisted propagation branches are
preserved as alternatives and sources of lemmas. The numerical map
counts remain RH 6/9, Dirichlet 18/31 and Hecke 6/9. No old open node
is counted as completed merely because the preferred route bypasses it.

## Source integrity

These SHA-256 values were computed from the clean checkout at the pinned
revision; they certify source bytes, not mathematical correctness.

| Source path | SHA-256 |
| --- | --- |
| `grh/src/Statements.lean` | `79ef7ca776e42abe1f46caee13ea09bd19f1e2d0b1620d8d5d200258f33b47bf` |
| `grh/src/Main.lean` | `40da180aea415129d3f2c2f374c6ba4606be91a199871efc84a1d19a67a17c6d` |
| `grh/src/New/Reduction/MainInequality.lean` | `521a8a669cc7f6d35b74ffe1e1bbec432c9012285a927b01e7047c4c161ea452` |
| `grh-compact/src/New/Main.lean` | `b6b285737cc0c306f380442eae279fd3127693c1074e7978d80f8ffd14f4078e` |

## Attribution and integration policy

The source is Apache 2.0, copyright 2026 Anthropic, PBC. This project
cites the immutable revision and writes its own ordinary mathematical
arguments. A useful replacement must specify its hypotheses and retain
the actual field, lattice, metric, Haar measure and scalar factors.
Readable and compact editions are compared as separate proofs: their
different error budgets and analytic endings must not be spliced together
without a compatibility argument.
