# Distilling the Riemann hypotheses

The goal is the shortest rigorous conventional proof we can obtain of ordinary RH and Dirichlet GRH, and then an extension to general Hecke GRH. We use the original proof by **Levent Alpöge with Claude** and the [Sernau–Anthropic reconstruction](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207). See [sources and attribution](sources/README.md) for exactly what we extract, prove anew and retain. The external formal theorem is Dirichlet GRH; our ordinary reconstruction is incomplete.

## Read the mathematics

| Active manuscript | Mathematical scope |
| --- | --- |
| [Ordinary RH](paper/rh/main.tex) | Conductor-one target, fixed admissible modulus 18480. |
| [Dirichlet GRH](paper/grh/main.tex) | Every fixed target modulus, including imprimitive characters. |
| [Common mathematical body](paper/determinant/body.tex) | The shared determinant argument and its proved and open inputs. |
| [Hecke GRH](hecke/paper/main.md) | Independent analytic extension and nonabelian cubic benchmark. |

The [reading guide](paper/guide/main.tex) explains the proof idea. See [manuscript organization and builds](paper/README.md). Older PDFs and the original geometric route are in the [historical archive](paper/archive/README.md); they are not the current manuscripts.

## The proof in outline

The preferred route constructs short integral theta images; a scalar moment estimate supplies enough independent images; selected twists give the opposite determinant bound. One common main term cancels in the product formula. With the appropriate arithmetic parameters, the resulting prime-sum estimate implies the desired zero theorem.

The analytic endpoint, abstract spanning and determinant comparisons, and simultaneous small-twist theorem are written in ordinary mathematics under their stated hypotheses. The [Selmer datum construction](notes/lsernau-main-summand-data.md) derives its conditions from the attached, type-compatible representations. The [critical-value construction](notes/lsernau-critical-value-systems.md) derives the integral systems and a smaller ratio budget from the exact kernel and period inputs. The [common finite theta construction](notes/lsernau-common-theta-finite.md) identifies the levels, class-sum normalization and ramified source, and proves direct restriction of the two moments. The [two-string attachment argument](notes/lsernau-galois-two-string.md) and [one-lift comparison](notes/lsernau-one-lift-comparison.md) establish the cancellation, integral-frame and finite determinant steps. The [scalar CM supplier](notes/lsernau-cm-theta-normal-form.md) proves the marked good equation and integral theta sections and their non-split normal form. The [charged jet theorem](notes/lsernau-charged-jet-estimate.md) gives the local product and Schur-jet bound on the specified Weil normalization inputs. The [finite positive-type closure](notes/lsernau-positive-type-moment.md) and [common Ribet element](notes/lsernau-ribet-polynomial.md) establish the finite arguments with their precise arithmetic hypotheses. The outstanding work is the actual Weil-lattice, vacuum and period normalization inputs, exceptional-prime/chain charge comparison and sharp main-pair tests; actual Poincare amplitude unfolding, identity, open-cell and terminal-fixer estimates; nonzero see-saw and period identities; odd-rank attachment and labelled local-global inputs; actual tied-row and trace-ideal valuation and coefficient extraction giving the individual integral separators; and chain exchange identities. The [detailed proof plan](blueprint/merged-proof-plan.md) is the authoritative dependency program. The [current checkpoint](notes/current-state.md) is only a resumption index.

## Research navigation

- [Proof blueprint](blueprint/README.md) and [architecture/readability audit](audit/merged-plan-readability-2026-11-26.md).
- [Source atlas](blueprint/lean-source-atlas.md), [formal-source audit](audit/lsernau-formal-audit-2026-11-26.md) and [verification records](certificates/README.md).
- [Hecke extension](hecke/README.md), including the transferable CM-field results and remaining field-specific conditions.

The original stable node counts are RH **6/9**, Dirichlet **18/31**, Hecke **6/9**. They refer to the historical interfaces, not percentages of the present proof. We do not mark an old open result proved just because it is no longer on the preferred path. The original source ledgers and alternative results are preserved as research resources.
