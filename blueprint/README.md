# Proof blueprint

Start with the **[full proof program](full-proof-program.md)**. It tracks the
source-wide mathematical requirements, the smaller sufficient target, and
the exact conditions for adopting a simplification. Its eleven work packages
account for all 46 fields of the endpoint construction while retaining their
shared data and nonvacuity requirements.

This directory separates mathematical interfaces, manuscript organisation,
and the complete local source import graph. An import graph is not a proof-term
dependency certificate; none of these maps asserts that GRH is proved here.

## Complementary views

| View | Purpose | Meaning of an arrow |
| --- | --- | --- |
| [Reader's overview](overview.svg) | A compact map of the principal argument, displayed in the main README. | An input required by the following step. |
| [Technical proof map](technical.svg) | Arithmetic and analytic interfaces, with named evidence and open requirements. | A required mathematical dependency or assembly interface. |
| [Complete section atlas](module-atlas.svg) | Every section of the main manuscript, grouped by subject. | The source section cites the target section; this may be a forward pointer or an optional comparison. |
| [Complete source atlas](lean-source-atlas.md) | All 175,187 pinned local source files, with every import endpoint. | In the stored graph, the importing module depends on the imported module. |
| [Source subject diagram](source-subject-atlas.svg) | Every local source file assigned to a visible namespace group. | Namespace containment, not a mathematical implication. |
| [Endpoint field ledger](endpoint-field-ledger.md) | All 46 construction fields assigned to responsible work packages. | No arrows: the fields share one coherent collection of objects. |

The first two maps are curated mathematical descriptions. Their arrows do not
certify that all hypotheses have been discharged. The section atlas is generated
from actual cross-references; it is **not a logical proof graph**. A documentary
cycle in that atlas need not be a circular proof.

## Status legend

| Colour | Status | Exact scope |
| --- | --- | --- |
| Green | Written reduction | A proof is written with its stated inputs and scope. This is not a declaration that all upstream obligations are complete. |
| Blue | Cited input | An external mathematical theorem is invoked with its hypotheses. |
| Amber | Partly completed | Some of the required argument is written; a specified component remains. |
| Red | Open obligation | A theorem, estimate, compatibility statement, or final conclusion remains to be supplied. |
| Purple | Optional alternative | An argument preserved outside the preferred route. Some alternatives themselves have conditional premises. |
| Grey | Recovered text or context | The section is present and located. No fresh audit of every proof in it is claimed. |

Every coloured interface also carries a text status. The complete atlas uses grey
for recovered sections whose individual claims have not all been newly audited;
it does not colour all inherited mathematics green merely because a proof
environment exists.

## What is counted

There are **96 recovered section files**, not 96 components of the entire formal
proof. The commutator reconstruction and the new Jacquet integration theorem add
two files, giving **98 manuscript sections**. Fourteen sections are now in the
alternative appendix; **84 remain in the preferred exposition**. These include
context and mixed sections and are not asserted to be a minimal set of lemmas.

The [complete inventory](module-inventory.md) gives every file, its stable
identifier, subject, role, placement and references. The corresponding
[JSON inventory](module-inventory.json) records source hashes and labels.
Stable identifiers such as `r27` refer to recovered source sections, regardless
of numbering changes in the PDF. The analytic companion is separate: its eight
TeX files contain nine section commands.

The [structural review](../notes/global-architecture-review.md) establishes the
ten-section cohomological substitution and the four-section analytic branch
choice. It audits incoming references and implicit formula links, including
the mixed status of recovered sections 16 and 17. The arithmetic complex and
the necessary class-number and unit arguments remain in the preferred route.

The earlier archived source inventory is now supplemented by a fresh complete
local-source hash check and import traversal. The
[source certificate](../certificates/lean-source-inventory.json) records
175,187 modules, 753,261 local import edges, full reachability from Main and
import depth 203. The 348 external import names are explicit boundaries;
their package internals were not traversed. This remains distinct from a
Lean build or a declaration-level proof dependency audit.

## The central remaining theorem

The final comparison must use **compatible integral theta maps at every required scale**:
the lattices, measures, divisibility, nonvanishing and analytic norms must refer
to those same maps. It must then give a positive prime-sum estimate retaining
the target character on arbitrarily large multiplicative intervals, with the
combination fixed for each accuracy and constants controlled as the
construction grows. Separate estimates for unrelated objects do not supply
this theorem.

The source's full family construction supplies such data, but the analytic
conclusion only needs one suitable construction at each scale. Replacing the
family construction remains an open mathematical task. The final exponent
loss need only tend to zero; accuracy-dependent constants and interval shapes
are allowed with the exact quantifiers proved in the manuscript.

The earlier six-stage manuscript guide is superseded as a source-wide plan by
the full program. Galois compatibility, stable nonzero theta lifts, normalized
global theta identities and geometric Hodge-bundle covolume estimates are now
explicit branches. Local positivity does not discharge those global results.

## Maintaining the blueprint

Edit [proof-blueprint.json](proof-blueprint.json) when a mathematical interface
changes, supplying theorem labels or persistent evidence paths. Keep claims
about compact support, finite decay, fixed rank and uniform families distinct.
Then run, from the repository root:

```sh
python scripts/build_proof_architecture.py
python scripts/reconcile_recovery.py
python scripts/build_full_proof_program.py
python scripts/build_blueprint.py
```

The renderer verifies unique section identifiers and labels, valid graph
endpoints, existing evidence targets, exact coverage of the main manuscript inputs, and appendix placement
for all alternative sections. It records hashes in
[blueprint-check.json](../certificates/blueprint-check.json). These are structural
checks, not a mathematical proof certificate. Diagrams are local SVG files and
need no external rendering service when viewed on GitHub.

The architecture allocation records the reviewed 97-section baseline before
the new integration theorem. The live inventory adds explicitly recognized new
sections and checks against the actual manuscript. Thus a new result cannot
silently disappear from the full map or change the meaning of old section ids.
