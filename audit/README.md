# Audit status

## Sernau–Anthropic rewrite, 26 November 2026

The [pinned comparison audit](lsernau-audit-2026-11-26.md) and
[formal statement/trust audit](lsernau-formal-audit-2026-11-26.md) distinguish
the actual Dirichlet statements, static source checks, upstream checker
reports and locally repeated execution. The
[source inventory](lsernau-source-inventory-2026-11-26.json) is reproducible.
The [revised proof plan](../blueprint/merged-proof-plan.md) adopts the
short-forms/spanning/determinant architecture, with newly proved abstract
improvements and an explicit Hecke transfer boundary. It does not promote
the old geometric or untwisted Selmer nodes to completed status.

## External conventional reconstruction audit, 25 November 2026

The [audit of Adriazola's 287-page reconstruction](adriazola-reconstruction-2026-11-25.md)
pins its source revision, answers the six comparison questions, identifies
explicit hypotheses and local counterexamples, and records three strengthened
tools integrated into both manuscripts. Supporting reviews cover
[geometry and coefficients](adriazola-geometry-2026-11-25.md) and
[Galois, congruences and K1](adriazola-galois-2026-11-25.md).
This is a critical-dependency audit with selected detailed proof checks,
not a certification of every lemma or a replay of the original formal proof.
The [source manifest](../certificates/adriazola-source-audit.json) and
[integration review](../certificates/adriazola-integration-review.json)
record exactly what was checked. Counts remain RH 6/9 and Dirichlet GRH 18/31.

## Earlier formal and project audit evidence

The recovered records contain substantially more formal-audit evidence than the
small source inspection performed when this repository was first started.
The table below distinguishes those records from checks actually repeated in
the present workspace. Preserving and checking a log does not repeat the
computation that produced it.

## The mathematical statements

At source commit `ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`,
`lean/src/Statements.lean` defines the assertions that the nontrivial zeros
of the Riemann zeta function and of Dirichlet L-functions lie on the critical
line, together with a nonvanishing formulation to its right and the
primitive-character restriction. The exceptional principal-character value
at 1 is excluded. `lean/src/Main.lean` exports five theorems, including the
Mathlib formulation of the Riemann hypothesis.

The [detailed source audit](theorem-and-dependencies.md) records the initial
inspection of these declarations and selected dependencies. Its smaller
verification scope must be read alongside the recovered evidence below.

## Evidence and its scope

| Check | Evidence now available | What was repeated in this continuation |
| --- | --- | --- |
| Attachment identity | All three originals are preserved in the recovery archive. | Byte comparison and SHA-256 checks against the attachments. |
| Reproducibility bundle | 622 regular files; its internal manifest lists 621 entries and excludes only itself. | All recorded byte counts and SHA-256 values, ZIP CRCs, and equality of the separately supplied and bundled TeX files. |
| Manuscript preservation | 96 recovered sections, 1,522 labels, 646 result environments, 611 proof environments and 45 bibliography entries. | Inclusion and reference checks; every recovered section was byte-identical before the documented editorial cleanup. |
| Selected sources | The initial certificate records 29 files checked against pinned Git blob hashes. | Seven targeted Lean files checked against recovered SHA-256 hashes; two mathematical source files checked against pinned Git blobs. The bounded declaration ranges are in the new source certificate; no full dependency traversal or full paper-proof audit is claimed. |
| Prior local compilation | Recovered records report 31 local source modules compiled; the complete local `Main` build was not finished. | The stored records were inspected; this build was not rerun. |
| Prior complete export inventory | The recovered scanner report covers the entire hash-identified solution export and records only `propext`, `Quot.sound` and `Classical.choice`, with no unsafe/partial declarations, duplicate names or unknown record forms. | The report's preservation was checked; the large export was not downloaded or rescanned here. |
| Prior transitive statement comparison | Recovered comparison records report equality of the five target types and their transitive constant declarations, including definitions, opaque bodies, inductive data and nontarget theorem bodies. | The records and their stated scope were inspected; the comparison was not rerun here. |
| Public target-specific axiom audit | Sutherland's archived report lists the same three standard axioms for each of the five target proofs. | External evidence, not a new local axiom traversal. |
| Independent kernel acceptance | The recovered audit preserves Sutherland's primary report and the published nanoda exit/timing log. | External evidence, not a kernel execution in this workspace. |
| Complete local kernel replay | The recovered audit explicitly records that this was not completed locally. | Not performed. |
| Ordinary-mathematics proof | The complete recovered manuscript and analytic companion are preserved. | Structural checks and narrow editorial review; no independent recheck of all 611 proofs is claimed. The central uniform arithmetic estimate remains open in the reconstruction. |
| New radial matrix argument | A written commutator proof recovers the full matrix and its successive restrictions for fixed finite standard flags. | Separate mathematical review, 810 finite exact identities, complete coefficient checks in dimensions one and two, and a negative control. The general proof is in the manuscript; finite computation does not replace it. |
| Complete current source import inventory | All 175,187 pinned local Lean files and 753,261 distinct local import edges. | Every source blob hash recomputed; all local modules reachable from Main; acyclic import graph of depth203. The 348 external import names are boundaries. This is not an elaborated proof dependency or kernel audit. |
| Full-proof mathematical program | All 46 fields of the endpoint construction assigned to eleven work packages, with shared choices and nonvacuity retained. | The main source interfaces and their exact quantifiers were inspected; global Galois, theta-matching and geometric covolume requirements are explicit. Not every supporting source theorem was independently audited. |
| Local residue/source comparison | General mixed-word positivity, word-independent pairing normalization, and original-parameter admissibility. | Independent mathematical review, 672 exact finite cases, and a pinned15-file operator/word/gauge/measure dictionary on smooth coefficient classes. No global or growing-chain estimates are inferred. |
| Classical Galois substitution | The universal Galois input is supplied by classical theorems, with the local and period-model comparisons proved. | Fifteen full local laws, Artin and epsilon witnesses; fourteen pinned local source files and seven primary references; twenty-one global source files and five primary references; independent mathematical reviews. The original Galois supplier becomes optional. This is not a new Lean compilation. |
| Averaged construction target | Finite character averaging, explicit projection/transfer errors, and weighted lower estimates. | Complete source clause ledger and independently reviewed conventional proofs. The compatible arithmetic construction remains open. |
| Geometric covolume defect | Exact orthogonal splitting, discarded mean-degree and integral-index budget, and a sufficient polynomial-decay criterion. | Fifteen pinned source files and an independent proof review; counterexamples show why rank alone and index-free estimates fail. The actual geometric core lower slope remains open. |

The current [RH specialization](../notes/rh-specialization.md),
[averaged error reductions](../notes/averaged-error-budget.md), and
[geometric core analysis](../notes/geometric-core-lower-bound.md) have
independent mathematical reviews and pinned source dictionaries. They add
short RH-only analytic proofs, a four-character signed budget, conditional
three-mean transfer, and exact determinant and Hilbert–Samuel remainder
formulas. The remaining construction includes the required symmetry or its
defect bound, the signed companion, actual mean-height/surplus bounds and
compatible integral maps. The finite computation is reproduced by
`scripts/check_averaged_errors.py`; it does not establish these open inputs.

The source of the recovered formal evidence is the
[original reproducibility bundle](../archive/recovered-2026-11-21/grh_audit_reproducibility.zip),
particularly `formal_export/EXPORTED_PROOF_AUDIT.md`,
`formal_export/solution_inventory.json`,
`formal_export/statement_definition_comparison.log`, and
`formal_export/mit_verified/`. The
[original audit manuscript](../archive/recovered-2026-11-21/grh_audit_v2.tex)
contains the full account. The
[recovery recheck](../notes/recovery-check-2026-11-21.md)
and [integration certificate](../certificates/recovery-integration.json)
record the current preservation checks and editorial changes.

The [fresh source note](../notes/source-check-2026-11-21.md) and
[matrix proof review](../notes/radial-commutator-review.md) record the new work
after recovery. The [new local dictionary](../notes/residue-source-dictionary.md)
and [vanishing-loss theorem](../notes/vanishing-loss-program.md) record further
completed reductions. Global forms and estimates uniform in growing chains
remain separate. The [full proof program](../blueprint/full-proof-program.md)
supersedes the manuscript-only overview as a map of the source-wide task.

## Limits that remain material

The scanner and structural comparator are independently written audit programs,
not formally verified software and not kernel proof checkers. Their recorded
results are reproducible computational evidence under their stated parsing and
normalization rules. The canonical challenge contains admitted target proofs
by design; comparison of the target statements does not compare those admitted
bodies with the solution proofs.

The public nanoda timing log records exit status zero but does not include the
configuration contents or input hash. Associating that run with the published,
hash-identified export therefore relies on the verifier's accompanying primary
report. The archived all-environment axiom census also contains compiler-support
axioms and `sorryAx`; this is different from the target-proof dependency audit,
which reports only the three standard axioms above.

The recovered compiled-module comparison found 25 exact binary matches among
31 local modules, with six different hashes. It does not establish complete
byte reproduction; a differing binary hash alone does not establish a changed
proposition or invalid proof.

None of these formal records supplies the outstanding mathematical estimates
in the human-readable reconstruction. New progress must state separately
what is proved in ordinary mathematics, what is conditional on a cited theorem,
what was inspected in source, and what was actually executed.

The [subsequent strengthened tools](../notes/adriazola-strengthened-tools.md) refine the three integrations, preserving their application conditions.
