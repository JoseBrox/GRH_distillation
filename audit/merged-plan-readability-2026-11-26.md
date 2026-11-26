# Architecture and readability audit of the merged proof plan

26 November 2026. Baselines: our old preferred program at
[74d18f3](https://github.com/JoseBrox/GRH_distillation/tree/74d18f39aa5db2b02e1ca83078b57768c5d92885),
the merged plan at
[4423ed5](https://github.com/JoseBrox/GRH_distillation/blob/4423ed559381fe7202711056b634fc0d3db6677c/blueprint/merged-proof-plan.md),
and the [Sernau–Anthropic source at 72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207).
The latter credits Levent Alpöge and Claude for the originating proof and
Sernau's collaboration with Anthropic and Claude for its shortening.

## Comparison, not a priority claim

The new development is a distillation **and a mathematical reconstruction**
of Alpöge's method. Both engineer prime-sensitive integral divisibility
of theta lifts, compare archimedean sizes and finite-place integrality,
and deduce a prime-sum estimate excluding zeros. The new route changes
how the lower estimate is obtained: regular families of coefficient-prime
specific anticyclotomic twists, one-lift and exchange determinant identities,
and a common corrected Gram determinant, rather than our former geometric
covolume supplier. The shared spirit does not imply that every construction
or constant is identical. We have not established a declaration-by-declaration
equivalence of the two original formal developments.

Source evidence: [root README](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/README.md),
[reading guide, §§1–3](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/GUIDE.md),
[main inequality, lines 1–85](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean#L1-L85),
and our [old work-package registry](https://github.com/JoseBrox/GRH_distillation/blob/74d18f39aa5db2b02e1ca83078b57768c5d92885/blueprint/grh/program.json).
The source's independent formal verification is documented separately in
[lsernau-formal-audit-2026-11-26.md](lsernau-formal-audit-2026-11-26.md).

## Reproducible qualitative change estimate

Unit of comparison: each of the eleven old work packages, with equal
weight. "Replaced" means its preferred acceptance criterion or supplier
strategy changes materially; "adapted" means the mathematical task survives
but a new target/parameter/dictionary must be proved; "retained" means its
principal mathematical role survives (not that all existing lemmas transfer
without checking hypotheses).

| Old package | Classification | Reason |
| --- | --- | --- |
| W01 analytic conclusion | Adapted | Exact one-sided remainder and quadratic twist replace the former preferred averaging interface. |
| W02 compatible construction | Replaced | Common A/B/C determinant data, rather than sampled finite tables as default. |
| W03 auxiliary data | Adapted | Actual new admissible fields, places, sparse weights and scales. |
| W04 integral Selmer | Replaced | Selected-twist presentations, local lengths and projection denominators, rather than moving untwisted lengths as default. |
| W05 Galois attachment | Retained | Attachment and local conditions remain needed; audit their weaker sufficient forms in the new source. |
| W06 theta/integrality | Adapted | Same kind of integral maps, but a new common diagram and normalization. |
| W07 archimedean/local analysis | Retained | Local positivity and estimates remain relevant with verified parameter dictionary. |
| W08 global theta/norm | Adapted | Two scalar moments and exact common chain, not every retained-space trace estimate. |
| W09 automorphic spectrum/counting | Retained | Multiplicity, local types and dimension/counting remain indispensable. |
| W10 geometric covolume | Replaced | Selected-twist determinant lower bound is preferred; old geometric statements remain open where recorded. |
| W11 final arithmetic budget | Replaced | Signed determinant comparison and exact remainder, rather than the full weighted geometric-slope budget. |

Thus 4/11 (36%) are replaced, 4/11 (36%) adapted and 3/11 (27%) retain
their principal role. About 73% are affected. This is a transparent
architecture estimate, **not** a percentage of work done, source lines,
time remaining, or eventual manuscript savings. Unequal weights would
give a different estimate.

## Readability audit

The change is substantial and the new high-level plan is preferable:
the contradiction can be explained through three mutually compatible
inequalities, two scalar moments, and the product formula. It removes
the need to finish W10 on the preferred route and reduces the demand
for full untwisted deformation calculations. This is a genuine
dependency simplification, not just renaming.

Four safeguards prevent false simplification:

1. **Not literally one determinant for every twist.** The determinant
   of the untwisted full basis is the common scalar. Each local twist
   has its own Gram determinant and clearing matrix. The exact ratio,
   complementary vectors, both conjugate factors and one common
   multiplier are needed to compare them.
2. **Nonvacuity and common data come first.** Rank, source spanning,
   positive dimension, nonzero theta determinants, scalar and Haar
   normalizations, fixed modulus/auxiliary prime before the limit, and
   the signs of the shared main terms must be established. A/B/C may
   not use independently convenient parameter families. Use the
   source's proven scale existence with a checked conventional
   reconstruction, not a list of individually plausible inequalities.
3. **A short summary is not yet a short proof.** The source's Lib
   contains substantial reconstructions, not just standard references;
   its citation inventory explicitly has unchecked locations. A
   classical substitution is acceptable only when hypotheses and
   conclusion match, or a shorter written bridge is proved. In
   particular the Galois attachment, local Hodge conditions, trace,
   theta and reciprocity inputs must be tracked.
4. **Separate proof from research archive.** The main paper should
   contain the exact analytic criterion, the three comparison theorems,
   the elementary core proofs and the short arithmetic constructions.
   Put specialist proofs needed for completeness in dependency-ordered
   chapters/appendices with explicit pointers. Do not reproduce old
   abandoned paths, Lean elaboration infrastructure, audits, or multiple
   proofs of the same lemma in the main narrative. An elementary
   exposition with standard undergraduate prerequisites is not yet
   justified; the attainable immediate target is a conventional proof
   for a number theorist, with a separate accessible introduction.

### Preferred acceptance gates

The following gates are *not new claims of completion* and not a
replacement count for the legacy RH/Dirichlet/Hecke maps.

| Gate | Exact output |
| --- | --- |
| G0 | Fixed q0,d; admissible simultaneous scale/field/level/weight construction, all relevant spaces nonzero where required. |
| G1 | Common theta diagram, exact normalizations and common algebraic field/lattices; all operators identified. |
| G2 (A) | Short integral spanning generators and actual clearing index on the common maps. |
| G3 (B) | Two scalar moments giving a controlled translate count and retained rank. |
| G4 (C1) | Bounded tied Selmer modules, selected twists and L-value systems; actual projection denominator with normalized lengths. |
| G5 (C2) | Nonzero one-lift and exchange/chain determinants, exact value-ratio and complement budgets. |
| G6 | Signed combined budget implies the exact arithmetic remainder estimate on the same data. |
| G7 | Analytic implication and boundary handling; already written conditional on G6. |

G4 should be decomposed into (i) arithmetic auxiliary-prime and tied-group
bound, (ii) polynomial presentation and witness, (iii) torsion
specialization and (iv) first-order projection and Hecke-value comparison.
The already proved specialization should not be repeatedly optimized
before the missing arithmetic inputs. G1/G2/G3 should progress alongside
G4. G5 must use the same diagram, not an analogous one. Verify G0 early,
especially the nonvacuity and fixed parameter order.

The largest immediate possible savings are on G4 and G5, not on the
already elementary final product-formula argument. Hecke reuse starts
with the field-independent presentation, scalar moments and determinant
algebra; it does not identify the arithmetic or theta objects over general
number fields. Keep the cubic fixed-CM benchmark and infinite-order
characters separate until a genuine bridge is proved.

No comprehensive page-count estimate or optimality theorem is claimed.
No old node is closed by this audit. The previous eight-page PDF remains
a compact exposition of the architecture, not the updated detailed
research ledger or a conventional proof.
