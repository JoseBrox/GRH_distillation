# Distilling the Generalized Riemann Hypothesis

**[Short guide](paper/guide/main.pdf)** · **[RH manuscript](paper/rh/main.pdf)** · **[Dirichlet GRH manuscript](paper/grh/main.pdf)** · **[RH proof map](blueprint/rh/proof.svg)** · **[GRH proof map](blueprint/grh/proof.svg)** · **[Shared overview](blueprint/overview.svg)** · **[RH program](blueprint/rh/program.md)** · **[GRH program](blueprint/grh/program.md)** · **[Source atlas](blueprint/lean-source-atlas.md)**

We are developing a simpler, human-readable proof from Levent Alpöge's announced argument for the Riemann Hypothesis and the Generalized Riemann Hypothesis for Dirichlet characters. The aim is to understand the mathematics, replace long arguments by shorter ones where possible, and give complete definitions and proofs in ordinary mathematical language.

For a Dirichlet character χ, the starting function is

```math
L(s,\chi)=\sum_{n=1}^{\infty}\frac{\chi(n)}{n^s}
\qquad (\mathrm{Re}\,s>1).
```

After analytic continuation, Dirichlet GRH says that every zero in the open strip between real parts zero and one lies on the line with real part one half. This is the version studied here; the project does not claim a theorem for every automorphic or number-field L-function.

## Objective and current status

The goal is a **complete and substantially shorter proof in ordinary mathematics**—not a line-by-line transcription of formal code. We seek a proof whose main ideas, definitions, hypotheses and estimates can be followed and checked by mathematicians without navigating a very large Lean development.

**The human-readable proof is not yet complete.** Several substantial reductions and local arguments are written, but the decisive uniform arithmetic–geometric estimate needed to conclude RH and Dirichlet GRH remains to be established. The manuscripts distinguish proved implications, explicitly cited classical theorems, conditional arguments and outstanding obligations.

## Two concurrent routes

The [ordinary RH manuscript](paper/rh/main.pdf) concentrates on the zeta function and its four-character arithmetic comparison. The [Dirichlet GRH manuscript](paper/grh/main.pdf) treats the general character and conductor. They have separate manuscripts and proof programs, while sharing the geometric, integral and analytic results that apply to both. An improvement in either route is checked in the other with its precise hypotheses.

The current proof-map counts are **RH: 6/9** and **Dirichlet GRH: 17/31**, as recorded in the [progress table](blueprint/progress.md). A finished conditional implication can still require an open arithmetic input. These counts therefore describe the proof program, not a percentage of RH or GRH proved.

## Current research priorities

The main task is now to **prove the missing arithmetic inputs**. We keep the preferred proof architecture fixed while attacking its open construction, estimate and compatibility requirements. Simplification is useful when it removes a substantial dependency or materially improves a decisive estimate.

For each major gap, the [frontier theorems](notes/open-frontier-theorems.md) state a precise target. We attempt that target directly, identify the first missing argument, and test new constructions or other methods against the exact downstream requirement. A useful lemma is not recorded as completion of the larger node that needs it. Ordinary RH is the preferred testing ground, while both routes remain active.

## The argument in outline

The strategy connects three kinds of mathematics:

1. **Detect zeros through prime sums.** An analytic criterion turns the desired zero statement into bounds for corrected prime sums. Finite tables at fourth powers suffice, with the required growth control on arbitrarily late intervals. Signed contributions are combined before their positive part is bounded.
2. **Construct arithmetic maps.** Galois representations, Selmer groups, theta series and geometric section spaces produce integral maps. Divisibility at finite primes and norms at complex embeddings give two ways to measure those same maps.
3. **Make the bounds meet.** The arithmetic and analytic estimates must use the same objects, measures, lattices and normalizations. Their combined error must be small enough as the auxiliary construction grows.

For ordinary RH, an eventual one-sided bound for the corrected zeta prime sum, with exponent arbitrarily close to one half, already suffices. The more flexible finite-table criterion allows averaging and cancellation. Neither criterion creates the arithmetic estimates it requires.

## What has been established

The [short guide](paper/guide/main.pdf) explains the mechanisms; the manuscripts and linked construction files give the technical statements and proofs.

- **Analytic reductions.** The criteria detecting zeros through prime sums, the finite sampling argument and the four-character RH comparison are proved.
- **The prescribed geometric spaces.** The original models, line bundles, boundary comparisons and level changes are constructed. Both lower section-norm bounds, the global upper bound and short generators of the entire integral cusp lattice are proved. The arithmetic degree of that same lattice now satisfies the required component inequality, with its stated error term.
- **Integral theta maps.** The actual sections have finite integral spanning families with uniform norm bounds. The local chain preserves its exact divisibility, phases and initial integral source. Its comparison with the final global maps remains to be made.
- **Arithmetic rigidity.** The original auxiliary fields, ordinary families and support constructions are supplied. The weight-zero deformation algebra is finite, including its torsion and nilpotents. The original good-data argument now has rigidity at both irreducible and reducible characteristic-zero points, using Thorne's and Kato's theorems with the exact twists. The global deformation equations now have their exact weighted counts, with the full integral ideal retained. The local comparison and the uniform torsion bound remain.
- **Global norm estimates.** The prescribed global return identity and measure normalizations are proved. Far returns have an exponentially small bound. All required flag-length tails, degenerate-fibre volumes and the original degenerate local operator bound are supplied. The global arithmetic sums and the final trace errors remain open.

These results remove concrete inputs from the open frontier. Their scope matters: an identity at fixed arithmetic data does not establish a useful bound across a growing family.

## What remains to prove

The [technical frontier](notes/open-frontier-theorems.md) separates five connected obligations:

| Obligation | The missing output |
| --- | --- |
| Final arithmetic comparison | Compatible finite tables whose total signed cost satisfies the analytic criterion. |
| Integral Selmer bound | The original local deformation chart and integral comparison, followed by a uniform bound for the specified weighted product of finite group orders. |
| Integral theta maps | Compatibility of the constructed local theta chain with the final normalized global maps and their restrictions. |
| Global analytic norms | Compatibility of the proved Gram identity with the final arithmetic maps, and sufficiently small rank-weighted trace errors. |
| Geometric sections and heights | The signed mean-height bound and rank losses for the same section family, with the point-height comparison and remaining numerical constructions. |

A construction at one level, a finite constant depending on that construction, or an estimate for a different map does not complete these obligations. Qualitative Selmer finiteness does not control growing torsion. The section-degree inequality still requires a useful bound for its prescribed mean height and rank losses. Four surviving characters do not bound auxiliary field degrees or geometric dimensions.

![The principal mathematical dependencies](blueprint/overview.svg)

**Map key:** green denotes a written implication with stated assumptions; blue a cited input; amber a partially established step; red an open obligation. A green implication can still depend on an unresolved red input.

## A shorter route for the original Riemann Hypothesis

For ordinary **RH**, only the zeta prime sum is needed. The conductor-one specialization simplifies the character projection to four terms, and the preferred positive-kernel comparison avoids imposing an artificial symmetry on the auxiliary weights. The quasi-RH estimates can be applied at the larger scales of the complementary terms, subject to their exact hypotheses.

The cohomological side is smaller as well. Classical algebraic K-theory and global duality give finiteness and finite prime support for the strict Selmer groups. RH also removes the nontrivial odd-order character case, leaving one weighted product of orders of specified finite groups. At an odd prime, under the stated deformation hypotheses, a strict Selmer group embeds in the dual of one finite module obtained from first-order equations. The abstract lower and upper comparisons now have short proofs that retain the integral torsion. The actual ordinary families, local propagation and required rank-two and rank-three support constructions are proved; the original good-data rigidity is proved, while the uniform integral bound remains to be proved for the growing family. Polynomial resultants and greatest common divisors also shorten one of the integer bounds, with the exceptional primes retained.

A one-sided upper **or** lower estimate for the corrected zeta prime sum, with exponent arbitrarily close to one half, would suffice for RH. The [RH proof program](blueprint/rh/program.md) and [direct comparison](notes/rh-direct-transfer.md) isolate the remaining averaged arithmetic and geometric estimates. They do **not** yet constitute a complete proof of RH.

![Ordinary RH: the analytic reduction and remaining arithmetic construction](blueprint/rh/proof.svg)

Read the [ordinary-RH map](blueprint/rh/README.md) from top to bottom. Its central open step is one compatible arithmetic construction. The separate quadratic companion estimate is an optional way to control part of the combined signed bound, so its arrow is dashed. The colors have the same meaning as in the shared overview; written implications retain their stated assumptions.

## Where to read the mathematics

| Resource | What it contains |
| --- | --- |
| [Short guide (PDF)](paper/guide/main.pdf) and [TeX](paper/guide/main.tex) | A didactic overview of the problem, the analytic criterion, the proof strategy and the RH specialization. |
| [RH manuscript (PDF)](paper/rh/main.pdf) and [TeX](paper/rh/main.tex) | The zeta criterion, positive-kernel comparison and precise remaining arithmetic requirements for ordinary RH. |
| [Dirichlet GRH manuscript (PDF)](paper/grh/main.pdf) and [TeX](paper/grh/main.tex) | Detailed definitions, reductions, arithmetic and geometric arguments, conditional dependencies and alternatives. |
| [Full proof program](blueprint/full-proof-program.md) | The source-wide logical requirements and the smaller sufficient targets. |
| [Module atlas](blueprint/module-inventory.md) and [proof diagrams](blueprint/README.md) | The 98-module mathematical organization, preferred route, alternatives and dependency interfaces. |
| [Analytic companion (PDF)](paper/companion/main.pdf) | Independent analytic reductions and rigorous checks of proposed shortcuts. |
| [Results](results/README.md) and [limitations](negative-results/README.md) | Precise proved reductions and explanations of why some tempting arguments are insufficient. |
| [Audit](audit/README.md) and [certificates](certificates/README.md) | Source inspections, reproducible calculations and the scope of verification. |

The preferred exposition uses 84 of the 98 reconstructed mathematical modules, retaining 14 as alternatives. These organizational counts are not claims of minimality or proof completion. The source atlas separately indexes 175,187 local Lean files at a fixed revision.

The main manuscript is divided into eight mathematical parts: the prime-sum criterion; cyclotomic cohomology; integral coefficient spaces; theta measures; local orbital identities; automorphic dimensions; archimedean and Jacquet arguments; and the estimates required to close the proof. Alternative methods appear in an appendix.

## External results and verification

Alpöge's [announcement](https://alpo.ge/remark.pdf) credits collaboration with Claude. The [source notes](sources/README.md) give the fixed Lean revision and attribution details. We also study the [September 30](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026) and [October 5](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026) quasi-RH approaches and results excluding Landau–Siegel zeros where their exact hypotheses permit.

These results can shorten particular parts of the argument, but a **fixed zero-free region weaker than GRH is not GRH**, and bounds for Dirichlet characters do not automatically apply to characters over varying number fields.

Finally, mathematical validity, TeX compilation, source-integrity checks, Lean import traversal and kernel verification are distinct tasks. The repository records what has actually been checked; **the entire formal proof has not been independently rebuilt or kernel-audited as part of this distillation**. No unverified input is treated as proved merely because it appears in source code or in a completed-looking diagram.
