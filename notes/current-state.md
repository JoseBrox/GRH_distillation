# Current continuation checkpoint

Updated 21 November 2026. Start here, then open one relevant mathematical module.

## Recovery is complete for the supplied material

The three attachments supplied again in this session are byte-identical to
`archive/recovered-2026-11-21/grh_audit_v2.tex`,
`grh_reconstruction_v2.tex`, and `grh_audit_reproducibility.zip`.
The recovered baseline was already integrated at commit
`2f5f79f2b6f7c4da99c3add332eb664047a0ba86`.
Fresh reconciliation preserves 96 sections, 1,522 unique labels, 646 result
environments and 611 proof environments. All 622 bundle files are present;
all 621 internal-manifest entries verify. The eight analytic companion files
are also preserved. This is a preservation check, not a new proof audit of
every statement. Prior-chat retrieval is disabled; no unavailable continuation
is being represented as recovered.

## Mathematical status

The conventional reconstruction is incomplete. Its analytic implication from
the fixed positive prime-sum combination to Dirichlet GRH is written out.
The sufficient uniform arithmetic estimate remains unproved.

The current frontier is:

1. The normalization and order comparison for any differently presented
   source fusion forms. Actual integration, the mixed-sign congruence and
   positivity for every fixed finite word of the explicit residue recursion
   are proved under the terminal domain, sign and separation hypotheses.
2. Uniform global orbital-energy estimates, including the remaining
   coordinate-size and weighted lattice-pair inputs.
3. Seed nonvanishing and auxiliary-level-prime divisibility for the same
   integral theta maps whose norms are estimated.
4. Complementary-parity automorphic character-length bounds with integral
   congruence control.
5. Assembly for growing chains with compatible lattices, measures,
   denominators, and constants.

Recovered section 95 proves Fourier-decay results. The new sections
`paper/sections/new/commutator-matrix.tex` and
`paper/sections/new/jacquet-integrated-descent.tex` identify the full matrix,
prove its restriction chain, and integrate the actual residue pairings.
Read these updated conclusions
before reopening an earlier provisional gap. The dependency crosswalk is
[`recovery-crosswalk.md`](recovery-crosswalk.md), and recovered section 96
states the complete remaining obligations.

## New results completed after recovery

The full contracted matrix is recovered from its scalar Capelli determinant
by three commutators with the Hermitian matrix coefficient and its conjugate.
The scalar restriction theorem therefore gives all four matrix entries, and
iteration gives the exact ordered restriction formula for every fixed finite
standard flag. The proof checks the isotropic intermediate vectors, spectral
shifts, coefficient order, support, covariance and Haar adjoints. This closes
the algebraic matrix/restriction obligation; it supplies no chain-uniform
estimate. Its hypotheses have now been sharpened to specify orthogonal
normalized hyperbolic splittings and the precise Jacquet signature and
character data. See [the fresh review](review-of-recent-advances.md).

See [the proof note](commutator-matrix-2026-11-21.md) and
[independent review](radial-commutator-review.md). Exact polynomial checks
give 810 identities in dimensions 1, 2 and 3. A separate implementation checks
complete normal-ordered coefficients in dimensions 1 and 2, tests the transfer
formula with noncommuting entries, and rejects a negative control that violates
coordinate independence. These checks support the written general proof;
they are not its substitute.

An additional independent PBW calculation checks the scalar bordered Capelli
expansion in full dimensions 3, 4 and 5: respectively 26, 113 and 586 nonzero
terms agree exactly. A deliberately wrong terminal shift gives 18 residual
terms. See `certificates/bordered-capelli-review-check.json`.

The new [integration argument](jacquet-integrated-descent.md) puts all
first-coordinate polynomial residue marginals in one matrix of Schwartz
functions. The distinct-index integration identity follows immediately.
The general mixed-sign congruence and terminal positivity then give actual Jacquet
positivity at every fixed rank. One cutoff-density argument extends this to
decay index `A+2h+delta` and derivative order `(k+2r+1)h+5`. Only the paired
scalar density is asserted Schwartz; transformed factors need not separately
be globally square integrable. [Independent review](matrix-schwartz-review.md)
checks that distinction, order, signs, domains and constant dependence.

The supplementary exact Laurent-action check covers all sign words of lengths
1, 2 and 3 in 672 cases with noncommuting terminal coefficients. Wrong-order
and wrong-minus-argument controls fail. The written ordered-transfer proof establishes arbitrary length; finite
checks support it without replacing it.

## Structural simplification and complete maps

The 96 recovered sections are an editorial division of the mathematical
manuscript, not the entire Lean dependency graph. There are now 98 section
files, including the two new ones. Fourteen alternatives are retained after
`\appendix`; 84 files remain in the preferred exposition. These include
context and mixed sections, not 84 indispensable or independently proved lemmas.

The bounded-order case `sv-exact-case` now uses `kt-fourteen`; its exponent
86 becomes 14. This removes the dependency on recovered sections 15 and
18–26. Under the selected uniform QRH route, sections 6–9 are alternatives
as well. The [architecture review](global-architecture-review.md) checks all
25 incoming explicit references and 16 implicit formula links before that
cut. Sections 13–14 and the early class-number/unit parts of 16–17 remain.

The [proof blueprint](../blueprint/README.md) provides the compact README
diagram, technical interface graph, and complete section atlas/inventory.
The latter shows documentary references, not certified proof premises.
The six-stage reading spine identifies the desired compatible construction;
it does not establish that construction or GRH.

Corollary `sz-qrh-real-gap` also removes a redundant assumption: under a common
Dirichlet zero-free boundary `vartheta < 1`, the required real-zero gap follows
with constant `(1-vartheta) log 3`. The independent determinant route is retained.

The audit overview is reconciled with the recovered formal evidence, and
implementation identifiers in fifteen mathematical sections are now recorded
outside the exposition. The immutable archive remains unchanged. The new
[source comparison](source-check-2026-11-21.md) checks seven selected Lean files
against the recovered hashes and two source papers against pinned Git blobs.
It is not a new full kernel replay or an audit of all proofs in those papers.

## Next mathematical task

Match the explicit finite-word theorem to any different source fusion-form
conventions, then pursue the uniform global orbital-energy estimates and the
same-object norm/divisibility comparison. Fixed-chain local positivity is now
proved; bounds uniform in growing chains and the four arithmetic/global
obligations listed above remain open.

The [bounded source comparison](source-residue-interface.md) locates the exact
remaining form identity. It confirms that the positive normalization is
reciprocal and chosen before the word, that the rightmost operator acts first,
and that new transfer factors multiply on the left. No mismatch was found.
The remaining dictionary must match the residue recursion, transpose, shifts,
scalar denominators, radial gauge and common Haar measure; the note pins the
three inspected files and the exact next definitions to locate.

## Bounded resumption

```sh
python scripts/reconcile_recovery.py --section 95
python scripts/reconcile_recovery.py --label kt-fourteen
python scripts/source_excerpt.py --source lean/src/Main.lean --search theorem
python scripts/source_excerpt.py --source lean/src/Main.lean --lines 1:12
python scripts/source_excerpt.py --manifest certificates/source-frontier-2026-11-21.json --source StatementQ.lean --lines 198:206 --offline
```

The source reader verifies the pinned Git blob before showing content. It
prints at most 25 search matches or 120 excerpt lines, with a 12,000-byte
excerpt limit. Downloaded source bytes stay in the ignored local cache.
Use exact paths and narrowly selected declarations. Never print the complete
manuscript, source tree, export, or integration certificate into conversation.

Keep proof checking as thorough as the claim requires; limit what is printed,
not what is verified. Commit coherent progress to `main` as it becomes ready.
