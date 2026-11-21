# The mathematical manuscripts

- [Main reconstruction (PDF)](main.pdf): the entire recovered mathematical baseline and the new scalar-to-matrix argument, organized in eight parts.
- [Main TeX file](main.tex), [preamble](preamble.tex), [recovered sections](sections/recovered/), and [new mathematical sections](sections/new/).
- [Analytic companion (PDF)](companion/main.pdf) and [its TeX source](companion/main.tex): the shorter paper written at the restart, preserved with its additional analytic arguments.

The main reconstruction is **incomplete**. It proves intermediate results and states classical inputs, conditional hypotheses, and the remaining uniform arithmetic estimates separately. The final part states the current frontier; earlier provisional statements must be read with the later results that discharge them. The [recovery crosswalk](../notes/recovery-crosswalk.md) gives a compact guide.

Build from the repository root:

```sh
python3 scripts/build_paper.py
python3 scripts/build_paper.py --companion
python3 scripts/reconcile_recovery.py
```

The main manuscript uses XeLaTeX and Latin Modern fonts; the companion uses pdfLaTeX. Both builds stabilize references, reject undefined citations and overfull boxes, and record hashes of the actual TeX inputs and resulting PDF. The build scripts make no network requests and can use the installed TeX tree when its generated format database is absent.

The reconciliation check preserves the unchanged archive and maps all recovered sections, labels, results and dependencies to working files. It distinguishes exact copying from editorial or mathematical revision. It does not independently verify every proof.

Write new mathematics in the appropriate section, with complete hypotheses and proofs. Keep source identifiers, audit details, chronological records, and computation logs outside the mathematical exposition. Retain useful alternative proofs without confusing them with necessary steps in the shortest route.

The new [commutator argument](sections/new/commutator-matrix.tex) proves the
full matrix restriction and its successive restrictions for a fixed finite
chain. The final part now separates that completed algebraic step from the
remaining integrated residue pairing and estimates uniform in growing chains.
The original recovered section numbers in the crosswalk remain fixed even
when a new section changes the numbering in the compiled paper.
