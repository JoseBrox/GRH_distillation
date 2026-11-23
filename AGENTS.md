# Project working instructions

Develop a rigorous, readable distillation of the announced GRH proof. Attribute the original work to Levent Alpöge and distinguish verified source attribution from the model version supplied in the project brief.

- Write standard mathematics. Define objects and state all hypotheses and ranges.
- Distinguish proofs, conditional results, cited results, conjectures, and computational evidence.
- Check decisive estimates, constant dependence, limiting arguments, and boundary cases. Preserve meaningful negative results.
- Organize the paper by mathematical dependencies. Keep recovery and chronological records outside it.
- Cite immutable source revisions. Do not infer that an imported theorem is proved merely from its name.
- Include reproducible scripts and checkable outputs for decisive computations. Do not call an unrun computation or unbuilt Lean project verified.
- Commit coherent checkpoints to `main` as ready, as authorized by the owner. Never force-push or discard unrelated work.
- Report the current finished/total node counts for both the RH and GRH maps at the end of the full answer. Report them earlier only when a count changes. Announce any newly completed existing node, and distinguish such completion from adding or reorganizing nodes.
- Exclude generated TeX byproducts. Include final TeX sources and compiled PDF.
- Do not invent missing earlier work. Reconcile recovered material if it becomes available.

## Bounded continuation

- Start from `notes/current-state.md` when present and the relevant resumption card in `notes/recovery-crosswalk.md`. The archive is a baseline, not a file to reload into conversation.
- Never return a complete large source, export, manuscript, registry, or connector response to conversation. Download and analyze large artifacts locally; report the specific conclusion and its verification scope.
- Locate a declaration or label first, then read a bounded range. `scripts/source_excerpt.py` verifies one pinned source before printing a bounded search or excerpt. For other sources, record the immutable revision, file hash, and exact line ranges beside the result.
- Keep mathematical claims, dependencies, counterexamples, and verification evidence in version-controlled files. Update the current checkpoint and commit coherent progress to `main` promptly, without force-pushing.
- Bounded output is a context-management measure, never a reason to skip a decisive proof check. Distinguish preserved historical evidence, checks rerun now, cited external verification, and open obligations.

- Keep `notes/current-state.md` below 200 lines as a current resumption index. Link full statements, proofs and verification evidence; do not accumulate historical results or obsolete next steps there. Preserve mathematical detail in the referenced files.
