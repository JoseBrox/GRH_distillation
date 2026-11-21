# Proof blueprint

This directory separates the **mathematical route**, its **remaining interfaces**,
and the **complete manuscript inventory**. It covers the conventional reconstruction.
It is not an enumeration or independent verification of the entire Lean dependency tree.

## Three views

| View | Purpose | Meaning of an arrow |
| --- | --- | --- |
| [Reader's overview](overview.svg) | A compact map of the principal argument, displayed in the main README. | An input required by the following step. |
| [Technical proof map](technical.svg) | Arithmetic and analytic interfaces, with named evidence and open requirements. | A required mathematical dependency or assembly interface. |
| [Complete section atlas](module-atlas.svg) | Every section of the main manuscript, grouped by subject. | The source section cites the target section; this may be a forward pointer or an optional comparison. |

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

The archived large-source inventory is historical evidence, not a fresh Lean
build. Its counts, provenance and limitations are recorded in the
[allocation certificate](../certificates/proof-architecture-allocation.json).

## The central remaining theorem

The final comparison must use **one compatible family of integral theta maps**:
the lattices, measures, divisibility, nonvanishing and analytic norms must refer
to those same maps. It must then give the fixed positive prime-sum estimate on
arbitrarily large multiplicative intervals, with constants controlled as the
construction grows. Separate estimates for unrelated objects do not supply
this theorem.

The six-stage reading spine in the structural review organizes this objective.
Its six stages are a plan for a shorter proof, not six completed theorems that
already imply GRH. Local residue identities, global orbital energy, integral
congruence bounds and growing-chain uniformity have separate statuses.

## Maintaining the blueprint

Edit [proof-blueprint.json](proof-blueprint.json) when a mathematical interface
changes, supplying theorem labels or persistent evidence paths. Keep claims
about compact support, finite decay, fixed rank and uniform families distinct.
Then run, from the repository root:

```sh
python scripts/build_proof_architecture.py
python scripts/reconcile_recovery.py
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
