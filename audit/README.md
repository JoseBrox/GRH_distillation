# Audit status

At source commit `ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, `lean/src/Statements.lean` defines the following propositions:

1. Zeros of the Riemann zeta function, excluding negative even integers and the special value at 1, have real part one half.
2. Every Dirichlet L-function is nonzero for real part greater than one half, excluding the principal-character value at 1.
3. Every zero of every Dirichlet L-function in the open critical strip has real part one half.
4. The restriction of the preceding assertion to primitive characters.

`lean/src/Main.lean` exports five theorems using these statements and Mathlib's `RiemannHypothesis` proposition. Their declarations have been read. Their existence as text is not evidence that their complete proofs have been independently checked.

## Current verification boundary

| Item | Status |
| --- | --- |
| New repository and initial state | Inspected. |
| Original announcement | Read. |
| Mirror provenance claims | Read; original archive hashes not independently recomputed. |
| `Statements.lean` and `Main.lean` | Read at the pinned revision. |
| Classical primitive-character reduction | Independently written and checked in the paper, including the functional equation and boundary cases. |
| Selected source bytes | 29 files matched to their pinned Git blob hashes; SHA-256 hashes also computed. |
| Complete import and theorem dependency chain | Not yet verified. |
| Absence of admitted proofs or added axioms in all dependencies | Not established. |
| Lean compilation and kernel check | Not run in this environment. |
| Agreement of every internal definition with the advertised statement | Not established. |
| Complete ordinary-mathematics proof of GRH | Not yet present. |

Further results must distinguish source inspection, compilation, dependency/axiom inspection, and independent mathematical proof. Searching for a few suspicious words cannot replace these checks.

[The detailed source audit](theorem-and-dependencies.md) identifies the first substantive dependencies and the exact scope of the selected-file inspection. [The source-file record](../certificates/source_files.json) is reproducible from the manifest and does not claim completeness of the dependency graph.
