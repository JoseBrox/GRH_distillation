# Available project context

This record was made on 21 November 2026 to preserve the context available when work moved to this repository after a message-delivery timeout.

## Established project instructions

The project continues an audit of Alpöge's announced GRH proof. The intended main deliverable is a human-readable mathematical paper with full definitions, theorem statements, and proofs. An earlier request suggested about twenty pages if the mathematics permits this, while explicitly giving correctness and completeness priority over page count.

The audit and writing are to advance together. Useful ideas from the quasi-RH approaches are to be integrated only after their hypotheses and proofs have been checked. The paper should be simplified where possible and organized as a paper, not a historical ledger. Important negative results, reproducible code, data, and certificates should be preserved. Clean results are to be committed to `main` as they become ready.

The project brief attributes Alpöge's work to collaboration with Fable 5.2. The inspected original announcement credits Claude without naming a model version.

## What was available at restart

- A short summary of the earlier conversation titled “Audit GRH proof”, dated 20 November 2026.
- The request to continue the review and develop a complete ordinary-mathematics proof.
- The full September 30 quasi-RH URL and a truncated reference to the October 5 approach, now identified from the source repository.
- The new repository and its initial two-line README.

## What was missing at the first checkpoint

No earlier TeX manuscript, proof text, audit report, program, data file, certificate, or computational output was available in the current workspace. The prior-conversation retrieval service returned that it was disabled. The project source-file list supplied for this conversation was empty.

That first checkpoint preserved the actual available brief and newly verified source references. The short analytic paper written immediately afterwards was a new reconstruction, not a recovery of unseen earlier work.

## Recovery from the supplied files

Later on 21 November 2026, the project owner attached `grh_audit v2.tex`, `grh_reconstruction v2.tex`, and `grh_audit_reproducibility.zip`. All three originals are now preserved in [the recovery archive](../archive/recovered-2026-11-21/README.md), with SHA-256 hashes and a full member inventory.

The recovered reconstruction has 48,261 lines. The ZIP contains 622 regular files, including both manuscripts and their PDFs, source provenance, formal-export checks, mathematical continuations, exact computations, and negative results. The separately supplied TeX files are byte-identical to the versions in the ZIP. All members passed CRC checks during safe extraction.

The recovered reconstruction supersedes the short restart paper as the main mathematical baseline. The restart paper is retained as an analytic companion while its results are compared with the recovered work. Earlier statements that no mathematical files had been recovered describe the first checkpoint only and are no longer the current status.

The original large Lean archive and the complete exported proof are not included in these three attachments. They contain records of earlier inspections, not those full inputs. At this restart we have directly read selected source files from a pinned public mirror. We must distinguish those direct checks, the earlier checks documented in the recovered reports, and independent verification reported by other researchers.

No continuation after the supplied bundle is treated as recovered unless its text, data, or supporting record is actually available. New results must be identified as new work. Reconciliation must follow the mathematical dependencies: many obligations described as open in an early section are discharged later in the recovered manuscript.

This record belongs outside the main paper. New mathematics belongs in the appropriate sections of the paper, with separate audit records where necessary.

## Modular integration in the resumed session

The three newly attached copies match the archived originals exactly. All 622 ZIP members and all 621 internal-manifest entries were checked again. The full reconstruction is now the working manuscript in `paper/main.tex`, split into 96 mathematical sections and grouped in eight parts. The earlier short paper is preserved in `paper/companion/`. See [the recovery crosswalk](recovery-crosswalk.md) for the dependency reconciliation and precise remaining frontier. Prior-chat retrieval remains disabled; no missing continuation is represented as recovered.
