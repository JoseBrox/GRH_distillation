# Current continuation checkpoint

Updated 25 November 2026. RH and Dirichlet GRH are **not yet proved** by
this reconstruction. This is a short resumption index; complete statements,
proofs and source evidence belong in the linked files. Earlier versions
remain in Git history. The repository main branch and the linked proof records give the current state.

Third research level: [Hecke GRH](../hecke/README.md) has its own [checkpoint](../hecke/notes/current-state.md), [program](../hecke/blueprint/program.md), [manuscript](../hecke/paper/main.md) and [frontier](../hecke/notes/open-frontier.md). The [full formal operator lattice](../hecke/notes/cubic-formal-operator-lattices.md) and [symbol derivative](../hecke/notes/cubic-symbol-derivative-lattices.md) give exact higher local divisibilities and a critical-error relative index, without the zeta multiplier. The [marked point classification](../hecke/notes/cubic-point-shapes-and-rigidity.md) covers both point characteristics and proves the rank-one tensor Euler-system obstruction. The [local 3-primary defect theorem](../hecke/notes/cubic-three-primary-local-defects.md) controls integral lift losses and proves untwisted cubic vanishing, not uniform moving lengths. The [high-dyadic corner elimination](../hecke/notes/cubic-corner-elimination.md) excludes reducible points and the [actual presentation](../hecke/notes/cubic-high-dyadic-presentation.md) reduces finiteness to irreducible curves; [direct Eisenstein-field Euler systems](../hecke/notes/cubic-eisenstein-euler-systems.md) restore rational image but leave a rank-two regulator. Hecke 6/9; the global degree saving and remaining odd-prime length bounds are open.

**Transfer back to RH/Dirichlet:** the [unconditional quadratic selection](unconditional-quadratic-selection.md) replaces the QRH-dependent numerical companions and exact exponential thin bound, on the original two-sign fields with all splitting and size conditions. Its [shared manuscript proof](../paper/shared/unconditional-quadratic-selection.tex) is included in both manuscripts and the partial common-window assembly now uses it. The stronger all-height zero-free source clause, and any separate consumer of it, are not supplied by this theorem. No whole W03 closure is claimed.

**Hecke-to-parent handoff (24 November):** [Shared rank-three corner elimination](hecke-parent-corner-handoff.md) proves the absence of the reducible two-sided branch when the residual negative corner vanishes. For ordinary RH it applies at odd coefficient primes in the admitted frame with $2^b\ge8\ell(\ell+1)^2$, and at 3 already under DH1. The general Dirichlet criterion retains the actual odd conductor in the Bernoulli bound. It is an integral simplification of the fixed-inertia ring, not of the auxiliary variable-weight propagation ring. It also supplies a reusable prime-dimensional strong-irreducibility test. The [parent corner reduction](../paper/shared/rank-three-corner-elimination.tex) now implements the handoff in both manuscripts. Retain the intermediate-conductor argument. The RH weighted Selmer supplier remains as recorded below; the general Dirichlet W04 remains open. The [two-negative-weight refinement](../hecke/notes/cubic-two-negative-weight-elimination.md) proves the entire invariant ring equals the coefficient DVR when both negative residual spaces vanish. The [finite class-rank certificate](../hecke/notes/cubic-finite-class-rank-certificates.md) also isolates a reusable finite-layer Iwasawa generator test, not a uniform bound for moving fields. The [characterwise strict-control refinement](../hecke/notes/cubic-characterwise-strict-control.md) gives the exact finite-class-rank comparison with at most one correction per coefficient-prime place of the base; the actual high-dyadic separator removes the correction even at split places. This can simplify finite tests for the parent fixed-inertia adjacent character; no uniform moving Selmer bound is inferred.

## Start here

**External reconstruction audit (25 November):** the
[pinned Adriazola audit](../audit/adriazola-reconstruction-2026-11-25.md)
finds substantial explicit hypotheses and repairable local errors, not a
complete 287-page conventional proof. Three strengthened tools are now
included in both manuscripts: [arbitrary p-adic Smith windows](padic-smith-window.md),
[integral isotypic projectors](integral-isotypic-projector.md), and
[Fitting bounds with repeated residual blocks](residual-block-fitting.md). The [further refinements](adriazola-strengthened-tools.md) give multiplicity-sensitive Fitting loss, weighted rank-deficient Smith windows and integral central projector clusters; their actual arithmetic application hypotheses remain explicit.
The last permits individual residual images, with an explicit factorial
error or a stable determinant law, and preserves normalized defects under
ramified coefficient extension. Actual family and arithmetic hypotheses
remain; no whole node is closed. The existing K1 bound is already stronger
than the reconstruction's proposed shortcut.

1. Read this file and the relevant row below. Keep the preferred proof
   architecture fixed unless a substantial mathematical improvement appears.
2. Open the corresponding target in [frontier theorems](open-frontier-theorems.md),
   then its latest proof note. Locate a declaration before reading source.
3. Attack the missing arithmetic construction or uniform bound. Check that
   it supplies the same objects and quantifiers as its downstream consumer.
4. Commit a reviewed result or a precise obstruction promptly. Update the
   current target, rather than appending another history to this file.

Prioritize ordinary RH. Aim for roughly 70% direct attacks, 20% verification
and 10% consequential simplification. Four surviving RH characters do not
bound the auxiliary field degrees, geometric dimensions or lattice defects.

## Active obligations

| Obligation | Latest established input | First remaining task |
| --- | --- | --- |
| W04: integral Selmer estimate | The original nonresonant count and [RH inertial integral count](rh-dyadic-host-count.md) bound all RH nonresonant primes, all dyadic conductors >8 ell^2 at admissible odd primes, and the entire exponent-one residual product. The [general dyadic Bernoulli and cocycle theorem](selmer-dyadic-twist-vanishing.md) proves the exact source threshold with the odd conductor retained and constructs the actual remaining RH rank-four datum. The [integral symplectic model](rh-symplectic-integral-model.md) supplies the local component, normalized chart, relative equations and finite-modulus derivation. The [rank-four finite local conditions and rigidity implication](rh-symplectic-point-rigidity.md) include actual dual-number points and require only the original automorphy premise for rigidity. | The [fixed-field rank-four spectrum](rh-symplectic-spectrum.md) supplies the uniform trace bound under cuspidal attachment over one selected quadratic field. The [conditional integral comparison](rh-symplectic-length.md) supplies the complete individual length inequality from the three actual point premises (F), (E), (A). The [curve and endpoint criteria](rh-symplectic-curve-frontier.md) reduce (F) to excluding irreducible rank-four and irreducible-block characteristic-prime curves and give a one-good-prime strict half-power window sufficient for (E). The [mixed Hilbert weight-change theorem](rh-mixed-hilbert-seed.md) supplies the original mixed rank-two seed at unchanged level, including the Eisenstein starting packet and normalization checks. The [marked rank-four symplectic induction](rh-symplectic-induction.md) supplies the full Case II seed (SeedIIAlt), including the integral lattice, original local flags, irreducibility on the cyclotomic kernel and cuspidal attachment. The [deep Case II residual chain](rh-case-II-residual-chain.md) now links the original residual restriction to that seed by three polynomial links through good points. The [rank-four weight-collision estimate](rh-rank-four-weight-collision.md) supplies the original dimension loss using only the finite-weight property. The [rank-four seed-support theorem](rh-rank-four-seed-support.md), [two-link ideal theorem](rh-rank-four-link-ideal.md), and [characteristic-prime clause](rh-rank-four-p1.md) supply the original sum ideal with its finite-weight, seed, and p1 properties. The [component propagation theorem](rh-rank-four-component-propagation.md) carries support across the original residual chain under the original arithmetic bounds and degree threshold. The [uniform deep-tower bounds](rh-four-uniform-tower-bounds.md), [rational lattice and flag reduction](rh-four-rational-lattice.md), [common coefficient space](rh-four-common-space.md), and [point-arithmetic applications](rh-four-point-applications.md) now give a written reconstruction of all three point premises (F), (E), (A) for the actual remaining RH Case II datum. The block-extension construction preserves the original characteristic polynomials; the characteristic-prime exclusion uses the finite-weight clause; the characteristic-zero endpoint exclusion uses a strict good-prime half-power window. Cuspidal attachment descends to one fixed quadratic field by solvable base change/descent. The conditional individual integral comparison thus has written suppliers for all its hypotheses, giving the polynomial individual length bound. The [four-interface closure review](rh-weighted-selmer-closure.md) replaces the mixed seed's Hasse descent by a [quadratic Eisenstein multiplier](rh-quadratic-eisenstein-multiplier.md), supplies [direct irreducible propagation](selmer-irreducible-propagation.md), and verifies the ordinary-family and abstract-length interfaces. The [weighted assembly](rh-weighted-selmer-assembly.md) now has all individual RH suppliers in the written reconstruction: log P(w) <= C*(Nt)^A* = o(exp(x^epsilon)), with both quadratic factors retained, giving the required half-allowance on the original windows. The RH weighted Selmer contribution is closed as a stated supplier; the general Dirichlet W04 and the compatible norm/geometric construction remain open. Full all-place WitA/PotUnl and general Dirichlet PMExAlt.aut are not claimed. Both manuscripts were rebuilt during the 25 November external audit; no Lean replay was performed. |
| W06: integral theta chain | [Actual selected-prime chain](theta-spanning-continuation-chain.md), including point models, value lattices, phases, both local divisibilities and the original twisted initial source. The [sharp auxiliary-level column theorem](theta-sharp-level-closure.md) completes the separate level node for the reference and every twisted column. | The [terminal finite period and Poincare–Bessel unfolding](theta-period-continuation.md) are identified with their exact scalars and masses. The [see-saw relation transfer](theta-relation-transport.md) reconstructs the exact two scalar products, common finite-test convolution, bottom relation, anchoring and arithmetic descent without adjoining row factors. Construct the actual common family LawsX/FamAllQ, its analytic unfolding, row lift and commutation, and RatioQ; the served-prime exclusion ServedQ is proved; obtain the prescribed nonzero pairing and norm dictionaries on the retained spaces. |
| W08: global norms | The integral lattice/mass, actual generic local input, all-cell Pieri expansion and complete nongeneric cancellation are proved; see the [current W08 continuation](w08-analytic-and-retained-continuation.md). | The [archimedean pointwise theorem](../paper/shared/archimedean-pointwise-assembly.tex) now holds on its explicit original spectral reserve. The [reserve check](../paper/shared/archimedean-ap7-reserve.tex) supplies the entire finite shifted family used by the actual weighted point sum. The [exact amplitude and row-norm comparison](flag-exact-norm-comparison.md) cancels the common row scalar with zero exponent loss, supplying the analytic `StepThmBPinnedG` route with its original quantifier order. The new second-type and archimedean arguments have passed independent mathematical review; no Lean replay is claimed. The [retained-column proof](retained-column-positive-traces.md) gives exact scalar-bearing Gram transport, the actual finite-projector identity and an improved restriction cost `g+b` in place of `g+2b`. The common theta row/anchored see-saw and moving positive-trace concentration estimates remain open. W08 remains open. |
| W10: geometric sections and heights | The actual corrected fibres and tangent degrees give the all-point height floor. [Finite-fibre nefness, the original regularizations and the signed determinant test](geometry-height-assembly.md) are now proved, with beta_B ≥ −107 Lambda_B/2 and every vertical factor retained. | The [compatible polarized test tower and exact corrected flag sequence](geometry-exact-corrected-flags.md) give the geometric trivial flag and dominant-weight positivity at the correction primes. The [uncorrected finite-place flag bound](geometry-uncorrected-flag-nefness.md) now proves M2 on the actual models, including boundary curves. Prove the exact two-level Frobenius-linked correction identities for the weighted mean; then bound section-rank losses and finish the same numerical family. |
| W02/W11: final arithmetic comparison | [Fourth-power sampling](fourth-power-sampling.md), [direct RH transfer](rh-direct-transfer.md), and [signed averaged criterion](scale-averaged-criterion.md). | Construct compatible finite tables meeting frontier theorem A, with all losses and auxiliary data controlled on the same windows. |

These are larger obligations than their individual suppliers. No table
satisfying the final criterion has been constructed. No whole proof-map
node is closed merely because one supplier is proved.

## Exact acceptance conditions

At each accuracy stage fix `1/2 < theta < 1`, the interval exponent `b>1`,
the averaging width, and (for GRH) a nonnegative character combination
retaining the target. These remain fixed on an unbounded sequence of
windows. The accuracy stages must permit `theta -> 1/2`.

Construct arithmetic comparisons at **every required fourth-power sample**,
including the expanded range needed for averaging. Different finite tables
may use different choices. Within one entry, however, the geometric,
integral and analytic arguments must concern exactly the same maps and
lattices. Average the signed total bound before taking its positive part.
The required weighted positive-part integral has logarithm `o(log N)`
along the chosen sequence; see theorem A for its literal formula.

For the final restricted maps, the norm penalty is

```math
P_{\mathrm{norm}}(x)=\kappa(x)^{-1}\operatorname{avg}_u
\min\{H_u,(g_u+b_u)(U_u+H_u)\},
```

where `g_u` and `b_u` are the prescribed normalized positive source-deficit
and target-excess traces. Their original positive normalizer is retained.
A bounded seed, an ambient projector or a Gram expansion at fixed data
does not supply this moving-family estimate. The RH final signed budget is
`rh-final-budget` in `paper/rh/sections/06-compatible-budget.tex`.

For RH the supplied weighted Selmer bound is exactly

```math
\log\mathcal P(w)\le\tfrac12 C_V y(B_0+N_c),\qquad
\mathcal P(w)=\prod_{p\ne2}\prod_{e=1}^{t-1}
(\#\Pi_{p,e}\mathcal S(E,p,e))^{w_p}.
```

Its projectors, exceptional primes, lower layers and supplied cases are
those in the RH manuscript. The weighted proof uses the integral length theorem, not merely qualitative finiteness or rational rigidity. GRH keeps its own character weights
and ramification-normalized lengths.

## Established inputs to reuse without re-optimizing

- **Analytic route:** the [positive-kernel comparison](positive-kernel-transfer.md)
  and direct RH transfer remove the proposed weight-symmetry requirement.
  [The symmetry obstruction](rh-weight-symmetry.md) explains why that older
  route fails for the actual sparse weights. Uniform quasi-RH applies only
  with its stated character and conductor hypotheses. The source exponent
  loss `(C+33/16) epsilon` must still tend to zero.
- **Geometric route:** the original PartI models, sized good cover and
  normalized complex theta dictionary are supplied. Use the [direct
  section-degree argument](geometric-degree-frontier.md), [finite jet
  bound](finite-section-jet-bound.md), actual short sections, determinant
  degree and parallel twists. The signed boundary and quotient-mean
  identities retain their original metrics and finite-place corrections.
- **Selmer route:** finite cohomological comparisons, integral compact
  types, ordinary modules and determinant, arithmetic seed, normalized
  curves and full rank-two/rank-three support are supplied in the cited
  construction notes. Preserve the entire characteristic-prime fibre,
  nilpotents, equation ideal and ordinary local conditions.
- **Norm route:** the local operator, Bessel, Fourier and terminal-degree
  arguments are indexed in [shared results](../blueprint/shared/README.md).
  The global expansion includes every rational return and the exact
  antilinear coefficient dictionary. The target projector already shown
  to fix period images causes zero loss; further projections need proof.

## Manuscripts and navigation

The [RH manuscript](../paper/rh/main.tex) and
[GRH manuscript](../paper/grh/main.tex) have separate route folders and
[RH](../blueprint/rh/program.md)/[GRH](../blueprint/grh/program.md) programs.
Common technical proofs are in `paper/shared/` and `paper/sections/`.
The [shared-results index](../blueprint/shared/README.md) records exact
applications and extra hypotheses. The [short guide](../paper/guide/main.tex)
is a didactic account organized by mathematics, not by research chronology.

Whole-node counts are **RH 6/9; Dirichlet GRH 18/31**. The existing technical node `level` is closed. They count proved
stated implications or adopted cited inputs, not fractions of completed
proofs. The authoritative status data are
[progress.json](../blueprint/progress.json).

## Source and verification discipline

The pinned Lean mirror is
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The [source atlas](../blueprint/lean-source-atlas.md) and compressed import
index preserve the earlier traversal of 175,187 local modules. Reachability,
source-byte hashes, finite computations, conventional proof review and
Lean kernel verification are distinct. The full Lean development has not
been independently rebuilt or kernel-audited in this project.

Use the bounded reader for selected source files:

```sh
python scripts/source_excerpt.py --atlas --source MODULE --search DECLARATION
python scripts/source_excerpt.py --atlas --source MODULE --lines FIRST:LAST --offline
```

It authenticates pinned bytes and limits excerpts to 120 lines/12 KB.
Keep large analyses local and return only decisive ranges to conversation.
The [recovery crosswalk](recovery-crosswalk.md) locates archived sections;
recover only a relevant resumption card. Do not reload the archive or
entire manuscripts. Historical certificates remain tied to their original
snapshots; do not rerun them as if they asserted current artifact hashes.

Run the new result's meaningful checks, independent proof review, relevant
manuscript builds and affected-page inspection. Do not repeat every old
check. Keep unresolved dependencies explicit in both proof and checkpoint.
