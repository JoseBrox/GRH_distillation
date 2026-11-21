# Distilling the Generalized Riemann Hypothesis

**[Read the main manuscript](paper/main.pdf)** · **[Mathematical sections](paper/sections/recovered/)** · **[Analytic companion](paper/companion/main.pdf)**

We are developing a simpler, human-readable proof from Levent Alpöge's announced argument for the Riemann Hypothesis and the Generalized Riemann Hypothesis for Dirichlet characters. The aim is to understand the mathematics, replace long arguments by shorter ones where possible, and give complete definitions and proofs in ordinary mathematical language.

For a Dirichlet character χ, the starting function is

```math
L(s,\chi)=\sum_{n=1}^{\infty}\frac{\chi(n)}{n^s}
\qquad (\mathrm{Re}\,s>1).
```

After analytic continuation, Dirichlet GRH says that every zero in the open strip between real parts zero and one lies on the line with real part one half. This is the version studied here; the project does not claim a theorem for every automorphic or number-field L-function.

## Where the proof stands

**The conventional reconstruction is not yet a complete proof of GRH.** It contains extensive proofs of intermediate results, together with explicitly stated classical inputs and conditional deductions. The decisive uniform arithmetic estimate remains open in this reconstruction.

The main manuscript includes all 96 recovered sections, organized in eight thematic parts, and a new section simplifying the radial matrix argument. The older files have been reconciled with the repository, and the short paper written at the restart is preserved as an analytic companion. The [recovery crosswalk](notes/recovery-crosswalk.md) identifies the later results that resolve earlier provisional gaps. The original files remain available in the [recovery archive](archive/recovered-2026-11-21/README.md).

The argument has three broad stages:

1. **Reduce the location of zeros to cancellation in prime sums.** A one-sided upper bound on arbitrarily large multiplicative intervals is sufficient; a bound for every large real number is unnecessary.
2. **Construct arithmetic objects that control those sums.** Quadratic characters, cyclotomic cohomology, integral polynomial spaces, and theta lifts supply the ingredients.
3. **Compare their sizes in compatible ways.** Divisibility and analytic norms must concern the same integral objects, with every denominator retained and constants controlled as the chain grows.

The first stage is written out. Much of the second and third stages is also present, including a shorter cohomological route through algebraic K-theory, normalized theta measures, local orbital identities, an automorphic multiplicity comparison, and Jacquet adjointness and Fourier decay.

The latest simplification obtains a whole matrix of differential operators from one scalar identity. It also proves how that matrix behaves at each step of a fixed finite chain. The [new argument](paper/sections/new/commutator-matrix.tex) uses commutators: the difference between applying two operations in opposite orders.

The remaining work concerns the integrated residue pairing, global orbital-energy bounds, nonvanishing and divisibility at auxiliary level primes, the remaining complementary-parity Selmer bounds, and the final assembly with uniform constants. The matrix argument does not supply estimates for chains whose length grows. These obligations are stated precisely in the manuscript's last part.

## How the newer zero-free results help

The quasi-Riemann hypothesis papers provide a fixed zero-free region and useful estimates for selecting auxiliary characters. The work on Landau–Siegel zeros supplies an independent real-zero argument. When a uniform quasi-Riemann bound is already assumed, the required exclusion of real zeros follows from it and needs no additional assumption. Both routes are used with their exact hypotheses and ranges.

These methods simplify particular steps. A fixed region to the right of the critical line does not itself give GRH, and a result about Dirichlet characters does not automatically apply to characters over varying number fields. The manuscript keeps these distinctions explicit.

## Reading the mathematics

| Part | Subject |
| --- | --- |
| I | Prime sums, the one-sided criterion, quadratic characters, and the slope comparison. |
| II | Cyclotomic cohomology and Selmer groups, including shorter alternative arguments. |
| III | Integral coefficient spaces, polynomial duality, and period pairings. |
| IV | Ordinary theta measures, their normalizations, and integral columns. |
| V | Local orbital identities, ideal sums, and unitary mass formulas. |
| VI | Automorphic dimensions, formal degrees, and the multiplicity comparison. |
| VII | Archimedean differential operators, radial forms, and Jacquet integrals. |
| VIII | The uniform estimates still needed for the conclusion. |

For the main logical route, begin with Part I and the final part, then read the particular arithmetic input being used. Within Part II, the algebraic K-theory argument gives a shorter route to the coarse bound; the longer homology construction is retained as an alternative. The [analytic companion](paper/companion/main.pdf) supplies additional foundational proofs and clarifies the limits of proposed analytic shortcuts.

## Original sources and verification

The original work is attributed to **Levent Alpöge**, whose [announcement](https://alpo.ge/remark.pdf) credits collaboration with Claude. The [source notes](sources/README.md) identify the original archive, fixed source revisions, and the precise scope of inspection. The [September 30](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026) and [October 5](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026) papers are additional sources of methods.

Preserving a proof text, checking a source hash, compiling a document, and verifying a mathematical argument are different checks. Their scopes are recorded separately in the [audit](audit/README.md) and [verification records](certificates/README.md). The full formal proof has not been independently rebuilt in this recovery session.

The [paper guide](paper/README.md) explains how to build both manuscripts. The [current checkpoint](notes/current-state.md) and [continuation index](notes/recovery-crosswalk.md) locate the latest result and the next unresolved inputs, so further work can proceed one mathematical module at a time.
