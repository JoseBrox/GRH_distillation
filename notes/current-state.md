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

1. The full initial radial matrix, successive restrictions, and integrated
   residue pairing for the actual generated functions.
2. Uniform global orbital-energy estimates, including the remaining
   coordinate-size and weighted lattice-pair inputs.
3. Seed nonvanishing and auxiliary-level-prime divisibility for the same
   integral theta maps whose norms are estimated.
4. Complementary-parity automorphic character-length bounds with integral
   congruence control.
5. Assembly for growing chains with compatible lattices, measures,
   denominators, and constants.

Recovered section 95 proves Fourier-decay results; it does not identify the
full initial radial matrix. Read its final paragraph before reopening an
earlier provisional gap. The dependency crosswalk is
[`recovery-crosswalk.md`](recovery-crosswalk.md), and recovered section 96
states the complete remaining obligations.

## Work in progress at this checkpoint

An algebraic reconstruction of a two-by-two operator matrix from its scalar
contraction is under investigation. It is not yet an established result and
does not close the radial-matrix problem. New conclusions must receive a
full proof and a separate source-comparison record before this status changes.

The audit overview and residual implementation terminology in the working
manuscript are being reconciled with the recovered evidence. The immutable
archive remains unchanged.

## Bounded resumption

```sh
python scripts/reconcile_recovery.py --section 95
python scripts/reconcile_recovery.py --label kt-fourteen
python scripts/source_excerpt.py --source lean/src/Main.lean --search theorem
python scripts/source_excerpt.py --source lean/src/Main.lean --lines 1:12
```

The source reader verifies the pinned Git blob before showing content. It
prints at most 25 search matches or 120 excerpt lines, with a 12,000-byte
excerpt limit. Downloaded source bytes stay in the ignored local cache.
Use exact paths and narrowly selected declarations. Never print the complete
manuscript, source tree, export, or integration certificate into conversation.

Keep proof checking as thorough as the claim requires; limit what is printed,
not what is verified. Commit coherent progress to `main` as it becomes ready.
