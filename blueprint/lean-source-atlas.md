# Complete pinned Lean source atlas

This view covers every local Lean source file at the pinned source revision. It is separate from the manuscript section atlas and the mathematical proof program.

## Freshly checked coverage

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
```

To reproduce the full inventory, make the pinned source checkout available locally and run:

```sh
python scripts/scan_lean_backbone.py --mirror build/lean-mirror
```

The scanner reads and verifies the large artifact locally and prints only aggregate counts. It refuses unclassified imports or unsupported import headers.

## Mathematical backbone and remaining interpretation

The [endpoint backbone](../notes/lean-endpoint-backbone.md) traces the final sufficient interfaces and the one coherent construction they require. The [global input review](../notes/lean-global-inputs.md) unfolds the Galois compatibility, stable theta lift, theta-integral matching and geometric covolume contracts. These are mathematical interpretation checkpoints, not a claim that every source lemma has been independently verified.

The conventional proof program must cover all of these branches, including any replaced by a correctly matched classical theorem. The complete import graph remains available when a dependency must be traced beyond the current mathematical boundary.
