# Current continuation checkpoint

Updated 23 November 2026. RH and Dirichlet GRH are **not yet proved** by
this reconstruction. This is a short resumption index; complete statements,
proofs and source evidence belong in the linked files. Earlier versions
remain in Git history. The latest recovered baseline is
`103f0de0e8d9002081218e40d4df700dd90bb13b`.

## Start here

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
| W04: integral Selmer estimate | [Finite-end descent](selmer-support-continuation-finite-end.md) through the exact Galois quotient, on one common finite-index subgroup; the rank-two/rank-three support and ordinary families are supplied. | Construct the original auxiliary frame, including every size and seed clause; prove two-sided global rigidity and the uniform weighted integral Selmer bound. |
| W06: integral theta chain | [Actual selected-prime chain](theta-spanning-continuation-chain.md), including point models, value lattices, phases, both local divisibilities and the original twisted initial source. | Identify that same chain with the final normalized global operators, including all restrictions, periods and finite masses. |
| W08: global norms | [Period Gram identity](global-gram-continuation-period-identity.md), [actual target projector](global-gram-continuation-projectors.md), [arithmetic minimum](global-gram-continuation-minimum.md), [quantitative seed](global-gram-continuation-quantitative.md), and [exact covolume and Haar cancellation](global-gram-continuation-haar-budget.md). | Absorb the explicit far-return bound at the literal source cutoff; control near returns and the positive traces of the same final restricted maps. |
| W10: geometric sections and heights | Original integral models and sized cover; [short integral span](theta-spanning-continuation-short.md), [key shifts](theta-spanning-continuation-key.md), and [thick-region section bound](geometry-bergman-continuation-thick.md) with its original numerical records. | Prove the thin-region and upper cusp-frame estimates, actual point-height and multiplication comparisons, then the numerical section remainder. Construction of the numerical records is still required. |
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

For RH the remaining Selmer product is exactly

```math
\log\mathcal P(w)\le\tfrac12 C_V y(B_0+N_c),\qquad
\mathcal P(w)=\prod_{p\ne2}\prod_{e=1}^{t-1}
(\#\Pi_{p,e}\mathcal S(E,p,e))^{w_p}.
```

Its projectors, exceptional primes, lower layers and supplied cases are
those in the RH manuscript. Qualitative finiteness and rational rigidity
do not bound growing integral torsion. GRH keeps its own character weights
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

Whole-node counts remain **RH 6/9; Dirichlet GRH 17/31**. They count proved
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
