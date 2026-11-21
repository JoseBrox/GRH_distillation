# The mathematical manuscripts

- [Short didactic guide (PDF)](guide/main.pdf) and [complete TeX source](guide/main.tex): the problem, proof strategy, RH-only specialization and remaining construction, kept to at most twelve pages.

- [Main reconstruction (PDF)](main.pdf): the entire recovered mathematical baseline and two new arguments, organized in eight parts and an appendix of alternatives.
- [Main TeX file](main.tex), [preamble](preamble.tex), [recovered sections](sections/recovered/), and [new mathematical sections](sections/new/).
- [Analytic companion (PDF)](companion/main.pdf) and [its TeX source](companion/main.tex): the shorter paper written at the restart, preserved with its additional analytic arguments.

The main reconstruction is **incomplete**. It proves intermediate results and states classical inputs, conditional hypotheses, and the remaining uniform arithmetic estimates separately. The final part states the current frontier; earlier provisional statements must be read with the later results that discharge them. The [recovery crosswalk](../notes/recovery-crosswalk.md) gives a compact guide.

Build from the repository root:

```sh
python3 scripts/build_paper.py
python3 scripts/build_paper.py --companion
python3 scripts/build_paper.py --guide
python3 scripts/reconcile_recovery.py
```

The main manuscript uses XeLaTeX and Latin Modern fonts; the companion uses pdfLaTeX. Both builds stabilize references, reject undefined citations and overfull boxes, and record hashes of the actual TeX inputs and resulting PDF. The build scripts make no network requests and can use the installed TeX tree when its generated format database is absent.

The reconciliation check preserves the unchanged archive and maps all recovered sections, labels, results and dependencies to working files. It distinguishes exact copying from editorial or mathematical revision. It does not independently verify every proof.

Write new mathematics in the appropriate section, with complete hypotheses and proofs. Keep source identifiers, audit details, chronological records, and computation logs outside the mathematical exposition. Retain useful alternative proofs without confusing them with necessary steps in the shortest route.

The new [commutator argument](sections/new/commutator-matrix.tex) proves the
full matrix restriction and its successive restrictions for a fixed finite
chain. The new [integration theorem](sections/new/jacquet-integrated-descent.tex)
proves actual Jacquet positivity for every fixed finite mixture of the two
residue operations under the stated terminal sign and domain hypotheses. The final part
separates these completed local steps from global estimates and bounds
uniform in growing chains.
The original recovered section numbers in the crosswalk remain fixed even
when a new section changes the numbering in the compiled paper.

There are 98 section files: 96 recovered sections and two new ones. Fourteen
alternative sections follow `\appendix`; 84 remain in the preferred exposition.
The latter includes context and mixed sections, so it is not a count of minimal
independent lemmas. The [proof blueprint](../blueprint/README.md) records every
section and keeps documentary references distinct from logical obligations.

The [full source-wide program](../blueprint/full-proof-program.md) now supplies
the research backbone. It includes Galois/local compatibility, global theta
matching and geometric Hodge-bundle covolume estimates that were not separately
visible in the earlier manuscript map. The classical Galois theorem and its
period comparison are now supplied in the Galois and adjoint-vanishing section;
the stable theta-lift construction of that input is retained as an alternative.
The introduction and final construction section identify the surviving requirements.

Two further simplifications are integrated without adding section files:
the vanishing-total-loss theorem in Section3 with its scalar corollary in
Section4, and the word-independent pairing and original-parameter positivity
corollaries in the Jacquet section. Exact source evidence remains outside the
ordinary mathematical exposition.

The slope section now also proves a finite character-averaging criterion, a
weighted lower-estimate lemma and an exact orthogonal covolume identity. These
isolate the average arithmetic loss and the discarded-degree/index budget
that the remaining construction must control. Their hypotheses and proofs
are in the manuscript; the source dictionaries and verification records are
kept in the accompanying notes.
