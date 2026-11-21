# Distilling the Generalized Riemann Hypothesis

**[Read the short guide](paper/guide/main.pdf)** · **[Main manuscript](paper/main.pdf)** · **[Full proof program](blueprint/full-proof-program.md)** · **[Complete source atlas](blueprint/lean-source-atlas.md)**

We are developing a simpler, human-readable proof from Levent Alpöge's announced argument for the Riemann Hypothesis and the Generalized Riemann Hypothesis for Dirichlet characters. The aim is to understand the mathematics, replace long arguments by shorter ones where possible, and give complete definitions and proofs in ordinary mathematical language.

For a Dirichlet character χ, the starting function is

```math
L(s,\chi)=\sum_{n=1}^{\infty}\frac{\chi(n)}{n^s}
\qquad (\mathrm{Re}\,s>1).
```

After analytic continuation, Dirichlet GRH says that every zero in the open strip between real parts zero and one lies on the line with real part one half. This is the version studied here; the project does not claim a theorem for every automorphic or number-field L-function.

## Where the proof stands

**The conventional reconstruction is not yet a complete proof of GRH.** It contains extensive proofs of intermediate results, together with explicitly stated classical inputs and conditional deductions. The decisive uniform arithmetic estimate remains open in this reconstruction.

The number **96** refers to the sections of the recovered mathematical manuscript. It is not a division of the entire formal proof into 96 independent modules. The main manuscript now contains those 96 sections and two new sections: **98 in all**. Of these, **84 remain in the preferred exposition and 14 are retained in an appendix of alternative methods**. Some retained sections contain background or more than one argument, so 84 is not a count of indispensable lemmas. The analytic companion is a separate work.

The older files have been reconciled with the repository. The [recovery crosswalk](notes/recovery-crosswalk.md) identifies later results that resolve earlier provisional gaps, and the originals remain in the [recovery archive](archive/recovered-2026-11-21/README.md).

The proof-wide source analysis now covers all **175,187 local Lean files** at the fixed source revision. That source map is broader than the manuscript: it records the Galois, theta-integral and geometric covolume arguments, including alternative ways to supply them. These are explicit in the [full proof program](blueprint/full-proof-program.md). Its eleven work packages organise the research; they are not eleven completed theorems or a claim that the proof has only eleven indispensable steps.

The argument has three broad stages:

1. **Reduce the location of zeros to cancellation in prime sums.** A one-sided upper bound on arbitrarily large multiplicative intervals is sufficient; a bound for every large real number is unnecessary.
2. **Construct arithmetic objects that control those sums.** Quadratic characters, cyclotomic cohomology, Galois representations, integral coefficient spaces, theta lifts, and geometric covolume estimates supply the ingredients.
3. **Compare their sizes in compatible ways.** Divisibility and analytic norms must concern the same integral objects, with every denominator retained and constants controlled as the chain grows.

The first stage is written out. Much of the second and third stages is also present, including a shorter cohomological route through algebraic K-theory, normalized theta measures, local orbital identities, an automorphic multiplicity comparison, and Jacquet adjointness and Fourier decay.

There are now two further simplifications. Three commutators recover a whole matrix of differential operators from one scalar identity and determine its restrictions along a fixed finite chain. A single theorem about Schwartz functions then justifies the integrations for every finite residue expression. Together with an ordered matrix identity, it proves Jacquet positivity for every fixed finite mixture of plus and minus insertions, under the stated sign and domain hypotheses. One approximation argument extends this positivity from compact support to an explicit class with finite decay and differentiability bounds.

The Galois representations are now supplied by classical theorems, with their local correspondences, weights and period normalizations checked. This removes the separate construction of those representations by stable theta lifting from the preferred route. The independent theta identities and geometric estimates remain necessary; the [comparison proof](notes/classical-galois-substitution.md) records the exact scope of the substitution.

The remaining work includes geometric covolume bounds, normalized global theta identities and energy estimates, nonvanishing and auxiliary-level divisibility, the remaining complementary-parity Selmer bounds, and their compatible assembly. Fixed finite-chain identities do not supply estimates for chains whose length grows. The proof program states these requirements separately.

## A map of the proof

![A shorter route toward Dirichlet GRH, with the status of each main step](blueprint/overview.svg)

**Green:** a written reduction with its stated hypotheses. **Blue:** a cited mathematical input. **Amber:** part of the required argument is written. **Red:** a remaining obligation. A green step may depend on an earlier red step; its colour does not assert that the final conclusion has been established.

The [detailed proof map](blueprint/README.md) separates all the arithmetic, geometric and analytic requirements. The complete source atlas, the manuscript section atlas, and the mathematical proof program are distinct views. Importing a source file does not show that every theorem in it is indispensable to the final proof.

## A shorter overall argument

The principal structural simplification replaces the older coarse cohomology construction by the algebraic K-theory estimate with exponent **14**. Applying it also in the bounded-order character argument replaces the exponent **86** there. This removes ten sections of finite-field homology and arithmetic-cycle constructions from the preferred route. The arithmetic complex, the needed class-number and unit estimates, and the stated classical theorems remain necessary inputs.

Four more sections become alternatives when the uniform quasi-Riemann hypothesis is used throughout: the separate real-zero route and a proposed analytic shortcut that still needs a stronger mean-square estimate. All fourteen sections remain available in the appendix, with their hypotheses and proofs intact. The [structural review](notes/global-architecture-review.md) records why the preferred route no longer depends on them.

The final estimate admits a further simplification: it is enough to construct compatible arithmetic data at every required scale. The source's larger families are one way to obtain those data; a new proof may construct them directly, provided it proves every required estimate and compatibility.

The arithmetic comparison can now use an **average of the discrepancies**, with explicit finite errors, instead of separate bounds for every translation. Weighted lower estimates and the actual geometric losses suffice. For covolumes, a new exact splitting formula tracks the discarded subspace’s mean degree and the integral index; exponential decay of its dimension is one sufficient method, not a necessary hypothesis of that comparison. The corresponding geometric estimates remain to be proved.

Positivity gives a further simplification for the general Dirichlet argument:
compare the larger weights before averaging over a subgroup. The resulting
error depends on the fixed target character order, rather than the growing
auxiliary field degree. The [quotient comparison](notes/positive-kernel-transfer.md)
proves this directly, including the contributions at ramified primes.

The analytic endpoint also needs only a **total exponent loss tending to zero**. Each accuracy may have its own auxiliary characters, positive weights, multiplicative interval shape, starting threshold and multiplicative constant. Each positive combination must retain the target character and stay fixed during its own sequence of intervals. Uniform control within each such construction remains necessary. The new theorem and its scalar-construction corollary make this distinction precise; they do not themselves establish the arithmetic bound.

## What if we only want ordinary RH?

The [RH program](blueprint/rh-proof-program.md) has one analytic target:
the corrected prime sum for zeta. A short positivity argument shows that
either an eventual upper bound or an eventual lower bound with exponent
arbitrarily close to one half is sufficient. The guide gives the upper-bound
proof in full.

The existing arithmetic construction also simplifies: conductor one makes
one distribution condition automatic and leaves only four character terms.
A new positive-kernel comparison bounds the effect of changing the larger
weights before averaging. The smaller weights are handled at the much larger
prime-sum scales already covered by the uniform quasi-Riemann hypothesis.
This argument requires no symmetry of the weights. In fact, the prescribed
sparse set of distinguished places prevents the exact symmetry considered
earlier; the new comparison avoids that requirement entirely.

The resulting [RH estimate](notes/rh-direct-transfer.md) leaves one central
task: bound the normalized average arithmetic discrepancy for the same
integral maps and geometric objects. The quadratic companion terms have
the conditional selection estimate already proved in the manuscript.
Sharper covering estimates and weighted height and frame averages reduce
the remaining geometric budget. The auxiliary primes and geometric
dimensions still grow, and their uniform bounds remain essential.
A complete short proof of RH has not yet been obtained.

## How the newer zero-free results help

The quasi-Riemann hypothesis papers provide a fixed zero-free region and useful estimates for selecting auxiliary characters. The work on Landau–Siegel zeros supplies an independent real-zero argument. When a uniform quasi-Riemann bound is already assumed, the required exclusion of real zeros follows from it and needs no additional assumption. Each route is stated with its exact hypotheses and ranges.

These methods simplify particular steps. A fixed region to the right of the critical line does not itself give GRH, and a result about Dirichlet characters does not automatically apply to characters over varying number fields. The manuscript keeps these distinctions explicit.

## Reading the mathematics

Begin with the [short mathematical guide](paper/guide/main.pdf)
([TeX source](paper/guide/main.tex)). It explains the problem, the prime-sum
criterion, the arithmetic construction and what can be simplified for
ordinary RH. It is organized by mathematical ideas and kept to at most
twelve pages. Complete reductions and remaining assumptions are distinguished
throughout; the detailed proofs remain in the main manuscript.

| Part | Subject |
| --- | --- |
| I | Prime sums, the one-sided criterion, quadratic characters, and the slope comparison. |
| II | Cyclotomic cohomology and Selmer groups, using the shorter K-theory argument. |
| III | Integral coefficient spaces, polynomial duality, and period pairings. |
| IV | Ordinary theta measures, their normalizations, and integral columns. |
| V | Local orbital identities, ideal sums, and unitary mass formulas. |
| VI | Automorphic dimensions, formal degrees, and the multiplicity comparison. |
| VII | Archimedean differential operators, radial forms, and Jacquet integrals. |
| VIII | The uniform estimates still needed for the conclusion. |
| Appendix | Alternative analytic and cohomological methods, with their limitations. |

For the main logical route, begin with Part I and the final part, then read the particular arithmetic input being used. Within Part II, the algebraic K-theory argument gives a shorter route to the coarse bound; the longer homology construction is retained as an alternative. The [analytic companion](paper/companion/main.pdf) supplies additional foundational proofs and clarifies the limits of proposed analytic shortcuts.

## Original sources and verification

The original work is attributed to **Levent Alpöge**, whose [announcement](https://alpo.ge/remark.pdf) credits collaboration with Claude. The [source notes](sources/README.md) identify the original archive, fixed source revisions, and the precise scope of inspection. The [September 30](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026) and [October 5](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026) papers are additional sources of methods.

Preserving a proof text, checking a source hash, compiling a document, and verifying a mathematical argument are different checks. Their scopes are recorded separately in the [audit](audit/README.md) and [verification records](certificates/README.md). The full formal proof has not been independently rebuilt in this recovery session.

The [paper guide](paper/README.md) explains how to build both manuscripts. The [current checkpoint](notes/current-state.md) and [continuation index](notes/recovery-crosswalk.md) locate the latest result and the next unresolved inputs, so further work can proceed one mathematical module at a time.
