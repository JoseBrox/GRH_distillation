# Distilling the Generalized Riemann Hypothesis

This project studies Levent Alpöge's announced proof of the Riemann Hypothesis and the Generalized Riemann Hypothesis. Its purpose is to understand the argument, check its dependencies, and write a shorter proof in ordinary mathematical language, with complete definitions and proofs.

For a Dirichlet character $\chi$, the Dirichlet series

$$L(s,\chi)=\sum_{n=1}^{\infty}\frac{\chi(n)}{n^s}\qquad (\operatorname{Re}s>1)$$

extends beyond its initial domain of convergence. The version of GRH studied here says that every zero in the open strip $0<\operatorname{Re}s<1$ lies on the line $\operatorname{Re}s=1/2$. The original source also states nonvanishing to the right of that line, with the usual exception at the pole of a principal character.

## Original result and attribution

**Levent Alpöge, announced proof of RH and GRH, November 2026, in collaboration with Claude.** The project was initiated with the attribution **Fable 5.2**. The [author's announcement](https://alpo.ge/remark.pdf) names Claude but does not specify its model version. We retain the requested version attribution as information supplied with this project, pending confirmation in an original source.

The original Lean archive is linked from the announcement. For stable file references we use the [public source mirror](https://github.com/jsmorph/rh/tree/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de), pinned to commit `ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. The mirror is a source reference, not an independent verification of the proof. See [the source notes](sources/README.md).

## Current status

**[Read the developing paper (PDF)](paper/main.pdf)** · **[TeX source](paper/main.tex)** · **[Proved results](results/README.md)** · **[Limitations of the methods](negative-results/README.md)**

The paper contains complete proofs of analytic reductions and explicitly conditional comparisons with the quasi-RH approaches. It does **not yet contain an independently verified proof of GRH**. The unresolved arithmetic inputs are stated separately.

The written results include the primitive-character reduction, a one-sided criterion for weighted prime sums, a criterion based on smoothed Möbius sums, and an exact limitation of the sixth-power averaging argument. These help identify what a shorter proof must actually establish.

The source statements have been inspected. They concern all Dirichlet characters of positive modulus; they do not assert GRH for every automorphic or number-field L-function. The full Lean dependency chain has not been built or checked here.

The repository records independently recomputed hashes for 29 selected source files. An exact-rational script checks the exponent calculations. The paper has been compiled with stable references. The [verification records](certificates/README.md) explain the scope of each check.

The earlier conversation's mathematical files are not present in the current workspace. [The recovery record](notes/recovery.md) states exactly which context survived. No missing proof, certificate, computation, or previous result is treated as recovered.

## How to read the project

| Location | Purpose |
| --- | --- |
| [paper/](paper/README.md) | The developing mathematical paper, its TeX source, and its compiled PDF. |
| [audit/](audit/README.md) | The source statements, dependency checks, and remaining verification work. |
| [sources/](sources/README.md) | Original references, exact source versions, and attribution. |
| [results/](results/README.md) | Short accounts of results proved in the paper. |
| [negative-results/](negative-results/README.md) | Precise limitations of proposed arguments and proved examples of invalid inferences. |
| `scripts/` | Reproducible computations and document-building tools. |
| `data/` and `certificates/` | Inputs and independently checkable outputs of computations. |
| [notes/](notes/recovery.md) | Project continuity records, kept separate from the mathematical exposition. |

## Reproducing the checks

```sh
python3 scripts/build_paper.py
python3 scripts/verify_exponents.py --check certificates/exponents.json
python3 scripts/check_sources.py --output certificates/source_files.json
```

The first command needs a TeX installation; the other scripts use only the Python standard library. The source check downloads exactly the files pinned in the manifest and can subsequently run with `--offline`. No command is a full formal verification of GRH.

## Mathematical standards

Every result must say whether it is proved here, conditional on a stated hypothesis, quoted from an identified source, or still conjectural. Decisive estimates must state their ranges and the dependence of their constants. Numerical evidence must be labelled as such. The paper is organized by mathematical dependencies, not by the order in which the project developed.

The [September 30](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026) and [October 5](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026) quasi-RH papers are additional sources of methods. Their estimates must be checked before being used, and a fixed zero-free region strictly weaker than GRH is never substituted for GRH.
