# Audit of the Sernau–Anthropic GRH rewrite

Date: 26 November 2026. Source revision:
[`lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207`](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207).
Our comparison starts at `GRH_distillation@74d18f39aa5db2b02e1ca83078b57768c5d92885`.

## Scope and initial conclusion

**The exported theorem is Dirichlet GRH**, with ordinary RH as a special
case. The declarations quantify over every positive integer modulus and
every complex Dirichlet character, including imprimitive characters.
They use Mathlib's `DirichletCharacter.LFunction`, rather than a newly
defined substitute. The half-plane statement excludes the principal
character's pole at 1. The zero-on-the-line statement concerns the open
critical strip. General Hecke characters over number fields are absent
from these exported statements.

Evidence: [`grh/src/Statements.lean`, lines 1–16](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L1-L16),
and [`grh/src/Main.lean`, lines 4–22](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L4-L22).
The compact edition exposes the same propositions.

**This is a substantial rewriting of the same underlying method, not an
independent elementary proof.** The repository credits Levent Alpöge and
Claude for the original proof and describes a collaboration with Anthropic
for the shortening. The readable edition organizes the argument around
three statements about the same forms and lattices:

1. Short integral source forms have short, almost integral images.
2. A small collection of translates supplies sufficiently many independent
   images.
3. A product-formula argument with coefficient-prime-dependent twists
   forces the corresponding corrected covolume to be large.

The common main term cancels. See [`grh/GUIDE.md`, section 1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/GUIDE.md#L5-L29)
and [`grh/src/New/Reduction/MainInequality.lean`, lines 5–67](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean#L5-L67).

The determinant lower-bound route is a serious candidate to replace our
W10 geometric supplier in the preferred plan. This changes a dependency;
it does not prove the previously open W10 assertions. The theta identities,
global second moments, denominator control and exact normalizations remain
substantial mathematics.

## Verification boundary

The upstream README reports builds, an axiom list containing only
`propext`, `Classical.choice`, and `Quot.sound`, and independent checking
of the readable edition. These are **upstream reports**, not checks
reproduced by merely reading the README. It also explicitly says that no
mathematician has read the whole proof and that no conventional paper is
provided. An axiom inventory, an import inventory and a successful build
answer different questions from a human reconstruction.

The independent static audit, local build attempt and precise completion
status will be recorded in a separate formal audit. No result is promoted
in our human proof maps solely from this source's theorem names or README.

## Source integrity

These SHA-256 values were computed from the clean checkout at the pinned
revision; they certify source bytes, not mathematical correctness.

| Source path | SHA-256 |
| --- | --- |
| `grh/src/Statements.lean` | `79ef7ca776e42abe1f46caee13ea09bd19f1e2d0b1620d8d5d200258f33b47bf` |
| `grh/src/Main.lean` | `40da180aea415129d3f2c2f374c6ba4606be91a199871efc84a1d19a67a17c6d` |
| `grh/src/New/Reduction/MainInequality.lean` | `521a8a669cc7f6d35b74ffe1e1bbec432c9012285a927b01e7047c4c161ea452` |
| `grh-compact/src/New/Main.lean` | `b6b285737cc0c306f380442eae279fd3127693c1074e7978d80f8ffd14f4078e` |

## Attribution and integration policy

The source is Apache 2.0, copyright 2026 Anthropic, PBC. This project
cites the immutable revision and writes its own ordinary mathematical
arguments. A useful replacement must specify its hypotheses and retain
the actual field, lattice, metric, Haar measure and scalar factors.
Readable and compact editions are compared as separate proofs: their
different error budgets and analytic endings must not be spliced together
without a compatibility argument.
