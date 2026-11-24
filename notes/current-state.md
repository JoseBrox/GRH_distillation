# Current continuation checkpoint

Updated 24 November 2026. RH and Dirichlet GRH are **not yet proved** by
this reconstruction. This is a short resumption index; complete statements,
proofs and source evidence belong in the linked files. Earlier versions
remain in Git history. The repository main branch and the linked proof records give the current state.

Third research level: [Hecke GRH](../hecke/README.md) has its own [checkpoint](../hecke/notes/current-state.md), [program](../hecke/blueprint/program.md), [manuscript](../hecke/paper/main.md) and [frontier](../hecke/notes/open-frontier.md). Its preferred proof now uses an independent direct prime-count Mellin criterion, Galois norm-pullback reduction and separate finite-order/phase suppliers. The [S3 benchmark](../hecke/notes/s3-benchmark.md) has a proved eta-product real-zero exclusion; the complex-zero estimate remains open. The Hecke map is 6/9 after subdivision of H07. RH and Dirichlet counts are unchanged.

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
| W04: integral Selmer estimate | The original nonresonant count and [RH inertial integral count](rh-dyadic-host-count.md) bound all RH nonresonant primes, all dyadic conductors >8 ell^2 at admissible odd primes, and the entire exponent-one residual product. The [general dyadic Bernoulli and cocycle theorem](selmer-dyadic-twist-vanishing.md) proves the exact source threshold with the odd conductor retained and constructs the actual remaining RH rank-four datum. The [integral symplectic model](rh-symplectic-integral-model.md) supplies the local component, normalized chart, relative equations and finite-modulus derivation. The [rank-four finite local conditions and rigidity implication](rh-symplectic-point-rigidity.md) include actual dual-number points and require only the original automorphy premise for rigidity. | The [fixed-field rank-four spectrum](rh-symplectic-spectrum.md) supplies the uniform trace bound under cuspidal attachment over one selected quadratic field. The [conditional integral comparison](rh-symplectic-length.md) supplies the complete individual length inequality from the three actual point premises (F), (E), (A). The [curve and endpoint criteria](rh-symplectic-curve-frontier.md) reduce (F) to excluding irreducible rank-four and irreducible-block characteristic-prime curves and give a one-good-prime strict half-power window sufficient for (E). Prove these arithmetic exclusions and the fixed-field attachment (A), then assemble the weighted product on the same windows. The reduced host fields still retain both varying quadratic factors. No complete W04 closure is claimed. |
| W06: integral theta chain | [Actual selected-prime chain](theta-spanning-continuation-chain.md), including point models, value lattices, phases, both local divisibilities and the original twisted initial source. The [sharp auxiliary-level column theorem](theta-sharp-level-closure.md) completes the separate level node for the reference and every twisted column. | The [terminal finite period and Poincare–Bessel unfolding](theta-period-continuation.md) are identified with their exact scalars and masses. Prove the intervening see-saw and actual row realization, then compare the final restricted global operators. |
| W08: global norms | The integral minor sum, exact masses and embedded-isometry genus mean are proved. [Integral transport](flag-lattice-transport.md), [all stabilizer layers](unipotent-stabilizer-covolume.md), and the [fixed-normal-form weighted sum](weighted-flag-lattice-sum.md) now give the original bound, with the constraint xi²b² ≤ Delta retained. | Prove the original term-class correspondence and reciprocal automorphism weights. Complete the zero-Gram sum, generic returns, finite columns and final positive traces. |
| W10: geometric sections and heights | The actual corrected fibres and tangent degrees give the all-point height floor. [Finite-fibre nefness, the original regularizations and the signed determinant test](geometry-height-assembly.md) are now proved, with beta_B ≥ −107 Lambda_B/2 and every vertical factor retained. | Supply the general flag positivity and exact Frobenius-linked correction sequences needed for the weighted mean; then bound section-rank losses and finish the same numerical family. |
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
