# Complete pinned Lean source atlas

This view covers every local Lean source file at the pinned source revision. It is separate from the manuscript section atlas and the mathematical proof program.

## Coverage of the recorded full-source scan

- **175,187 local Lean files**, all matched byte-for-byte to their pinned Git blob hashes.
- **753,261 distinct local import edges**; the graph is acyclic.
- **175,187 modules reachable from Main**; maximum import depth, including Main, is **203**.
- **348 distinct external imports** are explicit boundary nodes. Their package internals are not included in this local inventory.

All-source import reachability does not establish that every declaration is needed by the five target proofs. Imported modules can contain unused results. This scan is not a Lean build or a kernel replay.

## Every top-level source family

| Source family | Files |
| --- | ---: |
| BuildAid | 5 |
| CompanionTheory | 2,027 |
| Development | 141,928 |
| Formalism | 18,254 |
| GroundTheory | 8,507 |
| Lemmata | 167 |
| Main | 1 |
| PositivityTheory | 449 |
| ReciprocityTheory | 3,845 |
| Statements | 1 |
| Supplements | 3 |

The large source families include abelian-variety theory, automorphic spectrum, Galois and local-global theory, theta integrals, and geometric covolume estimates. They cannot be represented faithfully by treating the recovered 96 sections as the entire source proof.

## Durable complete graph

The [compressed source graph](lean-source-imports.json.gz) contains every source module, pinned Git blob hash, byte/line counts, and local or external import endpoint. Its compact row schema is documented inside the file. The [inventory certificate](../certificates/lean-source-inventory.json) records the root tree, aggregate source digest, all subject groups and grouped import counts.

Query one module without loading a source file into the conversation:

```sh
python scripts/scan_lean_backbone.py --module Main
python scripts/source_excerpt.py --atlas --source Main --search theorem --offline
```

To reproduce the full inventory, make the pinned source checkout available locally and run:

```sh
python scripts/scan_lean_backbone.py --mirror build/lean-mirror
```

The scanner reads and verifies the large artifact locally and prints only aggregate counts. It refuses unclassified imports or unsupported import headers.

## Mathematical backbone and remaining interpretation

The [endpoint backbone](../notes/lean-endpoint-backbone.md) traces the final sufficient interfaces and the one coherent construction they require. The [global input review](../notes/lean-global-inputs.md) unfolds the Galois compatibility, stable theta lift, theta-integral matching and geometric covolume contracts. These are mathematical interpretation checkpoints, not a claim that every source lemma has been independently verified.

The [classical Galois substitution](../notes/classical-galois-substitution.md)
now replaces the source's Galois-construction supplier in the preferred proof
program. The atlas still describes the complete original source. No number
of eliminated files is inferred from this substitution: an imported file
can contain arguments used in several surviving branches.

The [full proof program](full-proof-program.md) covers these branches and records
the acceptance conditions for each proposed replacement. The
[source subject diagram](source-subject-atlas.svg) accounts for the entire
local tree; the [complete subject table](source-subjects.md) lists all 343
two-component groups. The complete import graph remains available when a
dependency must be traced beyond the current mathematical boundary.

## Bounded source comparisons in the current continuation

The complete import inventory above is preserved evidence from its recorded
scan. This continuation authenticated only the selected source files used
below; it did not download or rebuild the entire development.

| Mathematical supplier | Bounded source comparison and evidence |
| --- | --- |
| Exact auxiliary-prime iteration | [Chain note](../notes/level-chain-integrality.md) and [source certificate](../certificates/level-chain-integrality.json): original rational-image lattice, local kernel laws and triangular commutation factors. |
| Finite upper section rank | [Jet theorem](../notes/finite-section-jet-bound.md) and [source certificate](../certificates/finite-section-jet-bound.json): component geometry, nef weight differences and exact binomial rank shares. |
| Selmer point and tangent comparison | [Completed comparison](../notes/selmer-tangent-comparison.md) and [independent review](../certificates/selmer-tangent-comparison-review.json): the permitted grading rescaling, actual framed universal property and marked coboundaries. |
| Crystalline local tangent condition | [Component comparison](../notes/selmer-crystalline-component-comparison.md) and [certificate](../certificates/selmer-crystalline-component-comparison.json): the original ordinary equations, fixed local subgroup, saturated radical and exact adjoint coefficient module; Kisin's finite-algebra theorem supplies the infinitesimal comparison. |
| Sharp source trace loss | [Return theorem](../notes/dominant-return-deficit.md) and [certificate](../certificates/dominant-return-deficit.json): the original seed evaluations, rational returns and normalizers. |
| Average cusp correction | [Counting theorem](../notes/cusp-counting-mean.md) and [certificate](../certificates/cusp-counting-mean.json): the original Hodge norm, integral rational spanning, probability measure, count homogeneity and signed metric comparison. |
| Limits of finite support | [Return-support checkpoint](../notes/dominant-return-nonvanishing-frontier.md) and [certificate](../certificates/dominant-return-nonvanishing-frontier.json): infinitely many congruent rational returns in the isotropic case, with qualitative decay distinguished from a relative tail estimate. |
| Quantitative projector tail | [Kernel checkpoint](../notes/projector-kernel-tail.md) and [certificate](../certificates/projector-kernel-tail.json): the normalized exponential far-return estimate, admissible cutoff, and missing period-Gram transfer; the cusp logarithmic mean does not supply the higher inverse moment in its current majorant. |

These are conventional mathematical substitutions with explicit hypotheses.
They do not identify an exact number of unnecessary Lean files or constitute
a new kernel verification.
