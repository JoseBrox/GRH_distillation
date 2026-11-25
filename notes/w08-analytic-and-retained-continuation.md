# W08: pointwise closure, exact normalization, and retained-trace frontier

Updated 25 November 2026. This record continues
`JoseBrox/GRH_distillation@9a362ab91b1bf25dffc182feb86868c7e40ecff5`.
The pinned upstream revision is
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The original construction is due to Levent Alpöge. The proofs below are
ordinary mathematical reconstructions and replacements of specified
intermediate interfaces. No Lean replay or kernel verification is claimed.

## Current outcome

| Requested part | Result and exact scope |
|---|---|
| Archimedean pointwise estimate | Proved with a sufficient quadratic Gram power and an explicit original spectral reserve. The reserve is supplied for every shifted coefficient used by the actual weighted point sum. The stronger intermediate statement for every smaller Gram power or every near parameter is not asserted. |
| Uniform amplitude and row norm in `StepThmBPinnedG` | Proved by exact common-scalar cancellation, with no additional exponent loss. The internal analytic threshold is absorbed in the original existential size and level constants. |
| Retained theta columns and positive traces | The exact scalar-bearing dictionary, finite projector transport, improved restriction inequality, and fixed-normalizer trace identities are proved. The actual common theta row/anchored see-saw and the required moving-family concentration estimates remain open. |

Thus **W08 remains open**. No existing proof-map node is newly closed.
The unchanged counts are RH 6/9 and Dirichlet GRH 18/31.

## 1. The pointwise theorem actually supplied

Put `s=r+1`, `m=2s`, `n=k+2s−1`, and
`delta=||lambda′−lambda||_1`, where the coefficient has
Harish–Chandra parameter `lambda′`. Retain the original character,
section, compact parameters, shape, interlacing, separating-gap/cut,
and noncompact smooth-decay hypotheses. In addition to the original
fixed all-gap bound, impose

\[
 \operatorname{AllGaps}(\lambda,200\delta),\qquad
 q_0\ge\delta+s(48s^2+s+1).
\]

Here `q0` is the original minimum of the noncompact and nonempty
cloud-gap reserves, with both divisors retained. The [assembled
theorem](../paper/shared/archimedean-pointwise-assembly.tex) proves

\[
 n_L(\gamma)\operatorname{orbSq}_L(F,\gamma)
 \le b^{C_*m^4}\max\{1,G_L(\gamma)^{-1}\}^{C_*m^2}
                 \mathcal N_L(F).
\]

One sufficient fixed choice is
`C*=64+16 max(Ch,0)+24 CJ`, with `CJ` the existing moment constant.
All quantities on the two sides are the original ones, including the
character, point density and radial section. The inequality is
homogeneous and includes zero radial norm. For the original unshifted
parameter, `delta=0`, the original cubic gap hypothesis already supplies
the reserve after a fixed threshold increase, on the actual nonempty-cloud
range. At negative Gram the represented set is empty. No big-cell limiting argument is used to
identify a lower stratum.

### Proof components

1. **Quadratic interpolation grid.** With `N=3s` and
   `M=N(2r+1)`, the nodes `−min(u_l,u′_l)−3−5i`, `0≤i<M`, fit
   in the original closed two-unit cut. This repairs the earlier
   cubic grid-length demand. Fresh plus/minus insertions preserve
   the exact word admissibility, and each interpolation block has
   sum of absolute leading-coefficient weights at most one.
2. **All-head recursion.** Fourier inversion at singleton blocks
   and the exact block-growth lattice inequality at longer blocks
   give `E_s≤(6 Lambda²)^s max E_0,w`, `|w|≤3s`. The lattice sum is
   at most 17; there is no number-of-words factor. The explicit
   interlacing telescope proves the needed spectral normalizer
   comparison without a compact-rank exponent. Both arguments are
   in [archimedean-adaptive-grid.tex](../paper/shared/archimedean-adaptive-grid.tex).
3. **Same-form spectral energy.** The signed Pieri decomposition
   of the uncut polynomial coefficient is orthogonal for the
   original positive Jacquet form. Every normalized full central
   Capelli word has eigenvalue modulus at most one. Hence its
   actual empty-head energy is at most the same squared Jacquet
   norm, without a component count or a tensor-projection norm.
   See [the spectral proof](../paper/shared/archimedean-spectral-word-energy.tex).
4. **The cutoff limit.** Relative PBW puts the compact derivatives
   on the right. They annihilate the invariant Gram cutoff. A full
   Capelli factor contains at most `4s−2` noncompact derivatives,
   so the cutoff-sensitive order is at most
   `5+(4s−2)3s=12s²−6s+5`. Taking `p=6s²` makes this strictly less
   than `2p`, even at `s=1`. The actual quadratic level-zero forms
   converge. Constants used solely to prove convergence disappear
   in the limit. See [the direct PBW proof](../paper/shared/archimedean-cutoff-pbw.tex).
5. **Equal compact types.** Orthogonal Gelfand–Tsetlin branching
   gives two contraction chains of length `a=30s²+6≤36s²`.
   Every surviving one-step coefficient has squared modulus at
   least `(3b)^(−2)`. The actual positive cofactor vector obeys
   `||Omega||²=G/T′`; exact orbital factorization and the original
   radial density cancel the two powers of `T′`. The total moment
   power is `L=2p+a≤48s²` and polynomial degree `sL≤48s³`.
   See [the compact chains](../paper/shared/archimedean-wigner-two-chain.tex)
   and [their orbital transport](../paper/shared/archimedean-wigner-transport.tex).
6. **Original normalization and character.** The same positive
   unipotent scalar multiplies pointwise and radial norms; the
   remaining root factor is `pi^(2h_gamma)`, `h_gamma≤s²`.
   Transport from the actual character `a=kaRe>0` to one scales
   the Gram by `J=a^(2rs)` and the radial norm by `JW`.
   The point density contains the same `W`, including every
   exponent involving `k`. It cancels exactly. The remaining
   pointwise-to-radial factor is `a^(2rs−2d_gamma)`, where
   `0≤2d_gamma≤rs`. Compact finiteness is restored by one
   period-normalized coefficient matching every cell, not by
   asserting that split-torus translation preserves it. See
   [the character proof](../paper/shared/archimedean-character-transport.tex).

### The reserve and the consumer's quantifiers

The positive-minor point sum uses `P=M s³` for a fixed `M` and shifts
`delta≤sP`. The actual consumer retains a nonempty cloud-gap set.
Its strengthened base all-gap premise and original noncompact gap
give `q0≥Gamma_g m⁴/Cq²`. Choosing the internal analytic threshold
`Gamma_g≥Cq²(M+50)` gives

\[
 q_0\ge s(P+48s^2+s+1).
\]

The same fixed choice pays all moment and chamber-preservation
thresholds. This is proved in the [reserve
addendum](../paper/shared/archimedean-ap7-reserve.tex). It supplies
exactly the finite family used by AP7; it does not infer the `q0`
reserve from the all-gap bound proportional to `delta` alone.

The internal analytic threshold is distinct from the external `Cg`
fixed in `StepThmBPinnedG`. The source consumer chooses its size and
level thresholds afterward; `stdOfHyp_rec` supplies the required
internal analytic hypotheses. This preserves the original quantifier
order. In particular no external hypothesis is silently strengthened.
The [literal pinned-row theorem](../paper/shared/archimedean-pinned-row-closure.tex)
writes the original `StepThmBPinnedG` conclusion and all its auxiliary
measure quantifiers. The [normalization and consumer audit](pinned-pointwise-closure-independent-review.md)
records the exact source ranges for this final conversion.

## 2. Exact amplitude and row-norm cancellation

For each place choose a single finite compact-finite coefficient
`F_v` matching the actual local orbital operator on every relevant
nonzero-Gram cell and every radial section. The all-cell period
factorization and an absolute convolution majorant prove this
identity before any pointwise estimate is applied.

With the original finite masses and dimensions put

\[
 K_0=c_uc_{u'}\prod_v\kappa_v>0.
\]

The [exact comparison theorem](../paper/shared/flag-exact-norm-comparison.tex)
proves simultaneously

\[
 \prod_v\|J_v\|_{\rm HS}^2=K_0J_{\rm pin}^2,\qquad
 \prod_v jNorm2(F_v)=K_0 I_{\rm re}.
\]

Thus take `Cfac=K0^(−1)`, local `K_v=1`, and
`C1=Ca=Cn=0`. The scalar is fixed after the row and before all
points, sections, `nu_L` and `n_gen`, as the consumer requires.
Its arithmetic variation is irrelevant because it cancels exactly.
Finiteness is proved before passing from extended integrals to real
values; no division by a potentially zero norm occurs.

Combined with AP7, these identities supply the original analytic
weighted point sum with the original pinned measure and `I_re`.

## 3. Retained columns: proved identities and the exact remaining bridge

The [retained-column proof](../paper/shared/retained-column-positive-traces.tex)
transports source and target Gram operators from an actual common
pairing identity, retaining all scalar moduli, source cuts and target
cuts. It also proves the literal finite-projector identity for the
actual evaluation map: the finite fibre volume cancels its defining
Haar normalization. Neither result constructs the common theta row.

The outstanding identity must join the actual theta row, the same
automorphic evaluation map and the anchored see-saw for all retained
columns. Its nonzero word-dependent scalars must be carried into the
norms or separately evaluated. The new [reference-row and evaluation
lemmas](../paper/shared/retained-actual-row-evaluation.tex) determine two
of these factors exactly: the reference coefficient identity has scalar
one under its original coordinate pins, and the actual evaluated row
isometry is `(c_ev n_P)^(−1/2) E_t h e_E`. The global range/Petersson norm
pins, onto evaluation and anchored all-word pairing still need to be
realized for the same family. The [common-family source audit](theta-family-laws-source-audit.md)
locates a genuine constructor from the actual global `AllTrue` and
original-recursion `OntoAll` inputs; it does not treat those inputs as
proved by the finite dictionary. Matching representation types and
individual column norms cannot replace this: two orthogonal unit
columns and two coincident unit columns have identical individual
norms but different target Gram operators.

For the original prescribed positive normalizer `c`, source Gram
`S=direct_sum T_i* T_i` and target Gram `Q=sum T_i T_i*`, the new
exact identity is

\[
 g+b=\frac{\|S-(c/R)I\|_1+\|Q-(c/D)I\|_1}{2c}.
\]

The improved restriction theorem charges the original target excess
only once. If retained dimension fractions are `r_0,v_0` and the
normalizer is `c max(r_0,v_0)`, it gives

\[
 g_0+b_0\le
 \frac{g+b+1-\min(r_0,v_0)}{\max(r_0,v_0)}.
\]

The arbitrary-normalizer version is also proved. A useful sufficient
second-moment estimate is

\[
 g+b\le\tfrac12\left[\sqrt\epsilon+
 \sqrt{\epsilon+\eta(1+\sqrt\epsilon)^2}\right]
\]

when `R||S−(c/R)I||_HS²≤epsilon c²` and
`D tr(Q²)≤(1+eta)(tr Q)²`. These are estimates at the prescribed
normalizer, not a replacement by the observed mass. The required
moving arithmetic-family values of `epsilon,eta`, including the
near-one off-diagonal target comparison, remain to be proved.

The [concrete period-kernel budget](../paper/shared/retained-period-window-budget.tex)
also retains the original source variables. If
`||K_uu−I||_HS²≤q²d_u` and
`||K_uu′||_HS²≤(1+tau)d_ud_u′/D_*` for distinct words, put
`sigma=D_*/R` and `xi=|D/D_*−1|`. At the prescribed calibration `c=R`,

\[
 g+b\le\mathcal E=
 \frac{q+\sqrt{(1+\xi)(1+\tau+(1+q)^2\sigma)-1+2q}}2.
\]

For the retained calibration `c0=R0=r0 R`, the bound becomes
`(E+max(1−r0,1−v0))/r0`. The arbitrary prescribed calibration is
also retained in the theorem. The [dependency audit](retained-moving-trace-dependencies.md)
finds genuine outstanding inputs: the diagonal loop estimates
`RowBig`/`RowNotScalar` still occur as arguments of `DiagCL`; the
near-one distinct-word scalar comparison retains the global Poisson
and dual-lattice suppliers; and the actual dimension, moving window,
retained-rank and scalar-modulus bounds remain. A polynomial-cost point
sum alone does not establish these estimates.

## 4. Review and verification

The [consolidated verification record](../certificates/w08-analytic-retained-review.json)
records proof and review hashes, exact diagnostic scope, both builds,
the inspected pages, the unchanged counts and all unclosed obligations.

- The [second-type cancellation review](second-type-independent-review.md)
  checks the actual lattice moves, character convention and stabilizer
  weights. The complementary [Fourier/density review](second-type-fourier-independent-review.md)
  checks both dyadic models, arbitrary conductors, leakage and final
  exponents. Their conclusions retain the stated gluing and
  defect-stratification inputs.
- The [exact-normalization review](flag-exact-norm-independent-review.md),
  [spectral/cutoff review](archimedean-spectral-cutoff-independent-review.md),
  [Wigner/normalizer review](archimedean-wigner-normalizer-independent-review.md),
  [Wigner transport review](wigner-transport-independent-review.md),
  [final quantitative review](archimedean-final-assembly-review.md), and
  [assembly/reserve review](archimedean-assembly-reserve-independent-review.md)
  separate independent proof checking from authors' calculations.
- The [concrete retained-period trace review](retained-period-window-independent-review.md)
  checks the shared-target summation, all four constants, retained cuts
  and original calibration, and verifies that its remaining source
  hypotheses have not been silently dropped.
- Reproducible exact finite checks verified 1,592 quadratic Fourier sums
  and 10 density/leak cases; 15,182 retained-trace cases; and 17,678
  nonzero Wigner one-step bounds plus 18,936 chain cases. The scripts
  and JSON records are committed. These finite checks support the
  written proofs and do not establish their unbounded-rank assertions.
- Both manuscripts are compiled from their actual inputs; their build
  records and the route-synchronization record specify source hashes.
  Compilation, source-byte authentication, mathematical review and
  Lean kernel verification are distinct. Only the first three have
  been performed here.
