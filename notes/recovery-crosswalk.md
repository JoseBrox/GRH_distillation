# Recovery crosswalk and continuation index

The three supplied attachments are already preserved byte for byte in
[the recovery archive](../archive/recovered-2026-11-21/README.md).
Their ZIP contains 622 regular files; all 621 entries in its internal
manifest match their recorded sizes and SHA-256 hashes. The remaining file
is the manifest itself. Both separate TeX files equal the bundled copies.
The bundle was created on 21 November 2026 at 04:13 UTC.

The integration restores the **entire recovered reconstruction** as the
[main manuscript](../paper/main.tex), with one file per recovered section.
The shorter repository paper is retained as an
[analytic companion](../paper/companion/main.tex). No continuation absent
from both these sources has been invented or treated as recovered.

Run `python3 scripts/reconcile_recovery.py` to regenerate
[the integration certificate](../certificates/recovery-integration.json).
It maps every original section, result, label and dependency to the working
files. It verifies preservation and inclusion, not the truth of every proof.
Editorial and mathematical revisions are distinguished from exact copying
by section and result hashes. The archived originals remain unchanged.

## What has been reconciled

The original reconstruction contains 96 sections, 1,522 unique labels,
646 result environments, 611 proof environments and 45 bibliography entries.
Its supplied PDF has 535 pages; the supplied audit has 66 pages.
These page counts describe the recovered PDFs, not the newly typeset paper.
The separate restart paper contributes eight source files, 74 labels and
21 result environments. Its baseline hashes are preserved in
[the companion baseline](../certificates/restart-paper-baseline.json).

The following numbers refer to the **recovered** section order, which the
certificate preserves even when new sections are inserted in the paper.

| Recovered sections | Mathematical role | Status at the recovered endpoint |
| --- | --- | --- |
| 1–4 | Exact prime-sum target; Mellin transforms; one-sided interval criterion; numerical balance | Analytic implication supplied; required arithmetic estimate still open. |
| 5–11 | QRH consequences, exact prime removal, quadratic determinants, slope comparison, simultaneous character selection | QRH-dependent conclusions keep their uniform input; shorter mean-square alternative is unproved. |
| 12–18 | Cyclotomic intervals, arithmetic homology, units, ideal classes and strict Selmer comparison | Early coarse obligations are discharged by later sections, with classical inputs stated. |
| 19–26 | Detection of powers, cycles, ideal lattices, finite-field functionals and finite-set count | Original coarse homological route reconstructed. |
| 27–28 | Coarse bound through algebraic K-theory; opposite-parity Selmer bound | Shorter routes recorded, retaining their classical K-theory, special-value and duality inputs. |
| 29–34 | Complementary-parity special cases, character comparison, adjoint vanishing, compatible choices | Special cases supplied; general automorphy and quantitative integral bounds remain separate. |
| 35–47 | Polynomial lattices, branching, divisor comparison, coefficient maps, decorated classes and lowering | Exact normalizations and stabilizers retained. |
| 48–60 | Ordinary theta moments, periods, equivariance, supports, coefficient fields, Hecke incidence and valuations | Selected-prime column bound supplied; seed nonvanishing and auxiliary-level-prime bounds remain separate. |
| 61–64 | Hermitian flags, degenerate orthogonality, Gram determinants and dyadic summation | Sharper local estimates supplied; coordinate-size and weighted lattice-pair inputs remain. |
| 65–69 | Local theta kernels, scalar germ, Parseval induction and global ideal sums | Local majorants and ideal summation supplied; required uniform global orbital-energy bounds remain. |
| 70–78 | Mass, dimensions, formal degree, automorphic projection and cusp estimates | Ambient multiplicity comparison closes in recovered section 77. |
| 79–89 | Archimedean coefficients, radial positivity, differential lifts and recursive frame | Stated operator identities supplied; full initial matrix and complete restriction chain remain. |
| 90–95 | Jacquet integrals, weighted decay, group majorants, adjointness and actual Fourier decay | Actual Fourier decay closes an earlier explicit hypothesis; full residue assembly remains. |
| 96 | Final dependency review and remaining constructions | Governs the recovered endpoint; earlier provisional lists must be read with these later closures. |

“Supplied” records the proofs and hypotheses present in the recovered
manuscript. This recovery pass has not independently rechecked all 611 proofs.

## How the analytic companion fits

| Companion material | Relation to the recovered reconstruction |
| --- | --- |
| Gaussian Poisson summation, gamma function, primitive Gauss sums and normalized functional equation | Expands classical analytic inputs used near the start of the main paper. |
| Primitive and imprimitive characters and reflection | Complements the original audit; includes conductor one and boundary cases. |
| Global one-sided prime-sum criterion | Weaker interval hypothesis is not claimed here; recovered section 3 supplies the additional multiplicative-window argument. |
| Smoothed Möbius criterion, including ideals and omitted Euler factors | Additional general analytic reduction; its cancellation hypothesis is still arithmetic work. |
| Replicated sums, sextic extraction and exponent limitation | Precise limitation of the stated second-moment deduction, compatible with recovered section 6. |
| Exact cube-factor inversion and finite descent | Useful independent algebraic and quantitative reductions. |
| Uniform continuation and counterexamples to nonuniform inference | Clarifies which positive saving must be common across a family. |

The companion's example showing that window estimates do not imply global
growth for an arbitrary function remains valid. It is not an objection to
the recovered theorem about the specific logarithmic-derivative prime sums.
Likewise, a fixed zero-free region or the exclusion of real zeros does not
supply the missing bounds for growing theta chains or varying-field Hecke
characters. The main paper states the exact range of those simplifications.

## Progress after the recovered endpoint

The [commutator-matrix argument](../paper/sections/new/commutator-matrix.tex)
now establishes the full group matrix, all four entries of its one-pair
restriction, and the complete successive restriction formula for each fixed
finite standard flag. It also proves polynomial coefficient growth, covariance,
support preservation and the Haar adjoint identities needed by the existing
Jacquet arguments. The proof uses the recovered scalar Capelli identity;
three commutators supply the remaining entries. See the
[proof and source-comparison note](commutator-matrix-2026-11-21.md) and
[independent review](radial-commutator-review.md).

The new corollary `sz-qrh-real-gap` also makes the real-zero exclusion a
consequence, rather than a second assumption, whenever uniform Dirichlet QRH
is already used. The independent determinant route remains available.

These are new results and dependency clarifications, not recovered work.
Earlier provisional assertions in sections 95 and 96 have been updated.

The [integration theorem](jacquet-integrated-descent.md) now justifies the
actual finite-word integrations through a matrix of Schwartz marginals.
One ordered congruence proves positivity for every fixed finite mixture of
both operations under the terminal domain and sign hypotheses, and one density
argument extends it to an explicit class with finite decay. Differently
presented source fusion forms still require a normalization/order comparison.

The [global architecture review](global-architecture-review.md) replaces the
bounded-order exponent 86 by 14 and removes ten older cohomological sections
from the preferred dependency route. Four analytic alternatives are also in
the appendix. The [complete proof map](../blueprint/README.md) retains all 96
recovered sections and both new sections, with their exact roles.

## The remaining mathematical frontier

1. Match any differently presented source fusion forms to the explicit
   recurrence now proved positive. Actual integration, mixed-sign congruence
   and finite-decay extension hold with the specified terminal hypotheses.
2. Establish the outstanding uniform global orbital-energy estimates, including
   the coordinate-size reduction and weighted lattice-pair count where required.
3. Prove seed nonvanishing and the sharp auxiliary-level-prime divisibility
   for the same integral theta maps whose archimedean norms are estimated.
4. Complete the complementary-parity automorphic character-length bounds,
   with quantitative integral congruence control and the required uniformity.
5. Assemble these bounds for growing chains, with compatible lattices,
   measures, denominator factors, exceptional spaces and parameter order.

The exact final target is the fixed positive combination of smoothed prime
sums defined in the main paper, bounded by an arbitrarily small power above
the square root on arbitrarily large fixed-shape multiplicative intervals.
The estimate remains unproved in the recovered reconstruction.

## Keeping further work small enough to resume

Work on one named mathematical input at a time. The integration certificate
locates its section, theorem labels, references and original source fragments.
Use `python3 scripts/reconcile_recovery.py --section 95` or
`python3 scripts/reconcile_recovery.py --label kt-fourteen` for a bounded
resumption card; neither command prints the complete registry.
Use the relevant source manifest from the bundle to identify a Lean module,
fetch it from a pinned external revision, verify its hash, and read only the
needed definitions and proof ranges. Do not load the full source tree into chat.

Record the precise claim, hypotheses, proof, source comparison and remaining
interfaces beside the appropriate mathematical section. Preserve meaningful
counterexamples and reproducible exact checks. Compile the paper, rerun the
structural integration check, and commit coherent verified progress to `main`.

Formal verification has a separate evidentiary boundary. The recovered audit
records complete export inventory and statement comparison, plus Sutherland's
external report of kernel acceptance; it explicitly records no complete local
kernel replay. The restart audit records a smaller direct source inspection.
Neither scope should be silently substituted for the other or called a new
independent verification performed during this recovery.
