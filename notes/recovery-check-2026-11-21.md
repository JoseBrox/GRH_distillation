# Attachment, integration and evidence recheck — 21 November 2026

Baseline: `2f5f79f2b6f7c4da99c3add332eb664047a0ba86`.
This check distinguishes preservation of prior work, the status recorded by
that work, and verification performed again in this continuation.
The complete machine-readable record is
[attachment-recheck-2026-11-21.json](../certificates/attachment-recheck-2026-11-21.json).

## Preservation is complete for the supplied material

All three current attachments are byte-identical to the files already in
[`archive/recovered-2026-11-21`](../archive/recovered-2026-11-21/README.md).
The recheck independently recomputed their SHA-256 values. No newly attached
mathematical text was missing from the repository.

The ZIP contains 622 regular files. Every one of its 621 internal-manifest
entries matches both its recorded byte count and SHA-256; the sole unlisted
file is the manifest itself. All ZIP CRC checks pass, and the two TeX files
inside the bundle equal their separately attached counterparts. The bundle
preserves 543 files under `mathematics/`, 60 under `formal_export/`, 12 under
`source_archive/`, and seven files at its root. The large original Lean
archive and the complete exported proof are intentionally absent; the bundle
contains provenance, programs, observations and certificates for them.

Fresh structural reconciliation confirms:

| Item | Count and result |
| --- | --- |
| Original reconstruction | 48,261 lines; 96 sections |
| Recovered section inclusion | All 96 included; all were byte-identical before the editorial cleanup below |
| Labels | All 1,522 preserved; no duplicate labels or unresolved mathematical cross-references |
| Result environments | All 646 preserved |
| Proof environments | All 611 preserved |
| Bibliography | All 45 entries preserved |
| Analytic companion | All eight baseline files byte-identical; all 74 baseline labels retained |
| Original audit | Entire attached audit preserved unchanged, including its 26 labels and 76 bibliography entries |
| Baseline build record | All 99 recorded TeX source hashes and the recorded main PDF hash match baseline Git objects |

These checks certify preservation and structural consistency. They do not
certify the truth of every mathematical argument. The recovered PDF checks
record 535 pages for the old reconstruction and 66 pages for the old audit;
those are archival page counts, not a new build result. The main PDF must be
rebuilt after the editorial or mathematical changes of this continuation.

The first fresh reconciliation was directed to a scratch report. Its checks
finished and the report was written, but its summary-print step rejected a
report path outside the repository. Reading that report established the
pre-edit counts above. A subsequent ordinary run of
`python scripts/reconcile_recovery.py` completed with exit status zero and
updated the version-controlled integration certificate after the cleanup.
No incomplete or failed mathematical computation is counted as a pass.

## Formal evidence recovered, without pretending to rerun it

The former audit overview described the initial, smaller source-inspection
phase. It has now been reconciled with the later evidence actually present
in the archive. The evidence is accessible through the
[original ZIP](../archive/recovered-2026-11-21/grh_audit_reproducibility.zip):

- `formal_export/solution_inventory.json` records a complete scan of the
  hash-identified solution export, with only the three standard axioms and
  no unsafe/partial declarations, unknown record forms or duplicate names.
- `formal_export/statement_definition_comparison.log` records equality of
  the five target types and their transitive constant declarations; it
  compares definitions and nontarget theorem bodies, not merely names.
- `formal_export/mit_verified/audit.log` is the archived external
  target-specific axiom report. The all-environment census and the axioms
  occurring in the five target proofs are different questions.
- `formal_export/mit_verified/nanoda.log` records an external successful
  exit. Its connection to the published export depends on the accompanying
  primary report because the log omits its configuration contents and
  input hash.
- `formal_export/mit_verified/local_olean_comparison.json` records 31 local
  compiled modules, of which 25 match the published binary hashes. It does
  not establish complete byte reproduction or a complete local `Main` build.

The scanner and comparator are reproducible audit programs, not formally
verified implementations of a proof kernel. The attachment recheck inspected
the preserved records; it did not rerun these large computations. No complete
local kernel replay and no complete human proof of GRH are claimed by this
continuation. See the corrected [audit overview](../audit/README.md).

## Editorial separation of mathematics and implementation names

Twenty-four narrow replacement blocks in fifteen sections move implementation
identifiers and file paths out of the mathematical exposition. The immutable
archive remains unchanged. The table retains their exact correspondence; the
certificate records every complete former paragraph, its replacement and its
original line location at the baseline commit.

| Recovered section | Retained source correspondence |
| --- | --- |
| [19](../paper/sections/recovered/19-sd-section.tex) | `SDetect`: power detection, with `q = ℓ^ν`; `SFew`: its role in finite-set separation |
| [20](../paper/sections/recovered/20-sh-section.tex) | `SZc`, `SRel`: cyclic homology and the integral relation |
| [21](../paper/sections/recovered/21-si-section.tex) | `SStein`: ideal-lattice isomorphism with the nonempty-index or `β = 1` qualification |
| [22](../paper/sections/recovered/22-se-section.tex) | `SEta`: pushforward identities, with `M = 2E + 1 < ℓ^c` |
| [23](../paper/sections/recovered/23-sf-section.tex) | `SCoc`, `STrans`, `STheta`, `SPhi`: finite-field evaluations and stable additivity |
| [24–25](../paper/sections/recovered/25-sb-section.tex) | `SClass`, `BOdd`, `SUpper`: arithmetic cycles, stable rational homology and finite-image bounds |
| [28](../paper/sections/recovered/28-ms-section.tex) | `ShaMinus`: eigenvalue `(-1)^(e+1)`; `ThmBcFree`: whole-eigenspace bound with additional constant zero |
| [39](../paper/sections/recovered/39-ib-section.tex) | `ioStd`, `brStd`: the two normalized integral maps of Theorem `ib-standard-integral` |
| [45](../paper/sections/recovered/45-ip-section.tex) | `Formalism/LocalToGlobal/Divisibility/TiedLemmas.lean`; `Formalism/LocalToGlobal/GroupLattices/JointServices/ValIntNonneg.lean` |
| [75](../paper/sections/recovered/75-rv-section.tex) | `kapBd`, `vInv = r_E/2`, `stepLt(1/2)`, `NonzeroFlagBound`: flag normalization and rare-volume bound |
| [76](../paper/sections/recovered/76-nu-section.tex) | `layerProd`, `kapBd`, `vInv`, `NearModerate`: layer product, normalization and explicit near-unipotent threshold |
| [90](../paper/sections/recovered/90-jk-section.tex) | `TailIntegrals/TailInt.lean`; `CHInt`, `CH`, `TailFin`, `C1`, `SUB`, `KER`, `SLOW`, `OS`: exact coordinate integral, tails and oscillatory estimate |
| [91](../paper/sections/recovered/91-ju-section.tex) | `BAt`, `FormulaF`, `IW`, `DelFormula.lean`, `AAt`: unipotent integrability, orthogonalization and the separate group-integral obligation |
| [92](../paper/sections/recovered/92-jm-section.tex) | `AAt`, `XiExists`, `CoefBound`, `XiInt`, `gN`, `AB`, `StatementB.lean`, `TailIntegrals`: group integrability and the majorant; the inverse-open-cell convention is retained mathematically |

The cleanup leaves every hypothesis, mathematical argument and conclusion
intact. Two result-environment hashes change solely because source-name
sentences were removed or rephrased: Corollary `sd-source` and Theorem
`ib-standard-integral`. One of the 611 proof-environment byte strings changes
solely by removing the concluding reference to source assertion `IW`.
The other 610 proof environments are byte-identical. These are manually
reviewed editorial changes; the structural script is not an equivalence
prover. Its result and section hashes transparently record the changes.

## Mathematical frontier preserved by the integration

The endpoint is governed by recovered section 96, not by earlier provisional
lists of missing work. The central fixed positive combination of smoothed
prime sums still lacks the required upper bound by every positive power
above the square root on arbitrarily large fixed-shape multiplicative
intervals. The quasi-RH and no-Siegel-zero inputs do not by themselves fill
that gap.

The most concrete outstanding work is the full initial radial matrix and its
successive restrictions, the integrated residue pairing for the generated
functions, uniform global orbital-energy bounds, seed nonvanishing and
auxiliary-level divisibility for the same integral theta maps, and the
remaining complementary-parity bounds. Growing-chain assembly must preserve
all constants, lattices, measures, denominators and parameter order.

A useful next bounded mathematical task is to isolate a single missing
restriction or residue identity for one fixed chain and state precisely what
its extension to varying chains requires. The established analytic
reductions may then be simplified independently, with every additional
arithmetic hypothesis kept explicit. The recovery check supplies no new
proof of any of these remaining estimates.
