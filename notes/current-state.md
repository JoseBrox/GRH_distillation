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

1. The integrated residue pairing for the actual generated functions,
   using the completed full initial matrix and successive restrictions.
2. Uniform global orbital-energy estimates, including the remaining
   coordinate-size and weighted lattice-pair inputs.
3. Seed nonvanishing and auxiliary-level-prime divisibility for the same
   integral theta maps whose norms are estimated.
4. Complementary-parity automorphic character-length bounds with integral
   congruence control.
5. Assembly for growing chains with compatible lattices, measures,
   denominators, and constants.

Recovered section 95 proves Fourier-decay results. The new section
`paper/sections/new/commutator-matrix.tex` now identifies the full initial
radial matrix and proves its restriction chain. Read these updated conclusions
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
estimate or integrated residue-pairing theorem.

See [the proof note](commutator-matrix-2026-11-21.md) and
[independent review](radial-commutator-review.md). Exact polynomial checks
give 810 identities in dimensions 1, 2 and 3. A separate implementation checks
complete normal-ordered coefficients in dimensions 1 and 2, tests the transfer
formula with noncommuting entries, and rejects a negative control that violates
coordinate independence. These checks support the written general proof;
they are not its substitute.

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

Use the established matrix identity to assemble the integrated residue pairing
for the actual generated vectors, retaining the domain, convergence and scalar
weights. Keep fixed-chain arguments distinct from bounds uniform in growing
chains. The four arithmetic/global obligations listed above remain open.

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
