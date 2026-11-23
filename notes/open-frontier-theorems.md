# Current frontier theorems

These are construction and estimate targets, not completed results. The
preferred architecture is fixed. Ordinary RH is the first test case;
Dirichlet GRH keeps its separate target character and conductor. All
parameters, lattices, maps and normalizations below are those in the
current manuscripts. A result closes a node only after the whole stated
target and its compatibility requirements are verified.

## Common quantifiers and the final acceptance test: W02/W11

For ordinary RH let `G` be the corrected zeta prime sum in the RH
manuscript. For Dirichlet GRH, fix a primitive target character first and
use the nonnegative character combination in the GRH analytic criterion.
That combination must retain the target with positive coefficient, and
must stay fixed throughout the windows of each accuracy stage.

**Frontier theorem A.** For each accuracy stage `j`, choose
`1/2 < theta_j < 1`, with `theta_j -> 1/2`, a fixed `b_j>1`, a fixed
`h_j>=0`, and an unbounded sequence of integers `N`. Put

\[
 L=\lceil N^{b_j}\rceil,\qquad
 K=\lceil e^{h_j/4}L\rceil .
\]

Construct actual compatible arithmetic data at **every** `k^4`,
`N<=k<=K`, giving a valid upper bound `B_k` for that stage's fixed
analytic function. Let `P_B` be their affine interpolant and let

\[
 \beta_n=h_j^{-1}\int_0^{h_j}P_B(n^4e^v)\,dv
 \quad(h_j>0),\qquad \beta_n=B_n\quad(h_j=0).
\]

With `J_beta` the affine interpolant of the row values, prove

\[
 \liminf_{N\to\infty}
 \frac{\log\left(1+\sum_{n=N}^{L-1}
     \int_{n^4}^{(n+1)^4}(J_\beta(x))_+x^{-1-\theta_j}\,dx\right)}
      {\log N}=0 .
\]

The liminf is along the chosen unbounded sequence. Each table may use
different arithmetic data, but each entry must identify the *same* maps
in its geometric, integral and analytic comparisons. The source/target
restrictions, probability weights, ranks, companion term and all exponent
losses are retained. The proven fourth-power interpolation theorem then
supplies the final analytic implication. No table satisfying this theorem
has yet been constructed.

For RH the exact entry to be bounded is `B_j(x)` in
`paper/rh/sections/06-compatible-budget.tex`, equation `rh-final-budget`,
with the signed thin companion allowed there. Its frame contribution is
the actual rank-weighted penalty below. The four-term sufficient
arithmetic envelope has loss `(C+33/16) epsilon`; if `C` depends on the
accuracy, this product must tend to zero. Constants are fixed before the
window grows. No alteration of this exponent accounting is made here.

## W04: the actual integral Selmer product

**Frontier theorem S.** Construct the original marked local/global
deformation models for the now-constructed ordinary modules and integral
Hecke determinant, with their stated ordinary local conditions and
two-sided rigidity. For those same
models prove the integral congruence comparison used by the weighted
Selmer consumer, together with its required bound on the actual prime
support. In the conductor-one specialization its remaining numerical
part is exactly

\[
 \log\mathcal P(w)\le\tfrac12 C_V y(B_0+N_c),\qquad
 \mathcal P(w)=\prod_{p\ne2}\prod_{e=1}^{t-1}
       (\#\Pi_{p,e}\mathcal S(E,p,e))^{w_p},
 \quad y=x^\varepsilon,\quad B_0=fm e^y y.
\]

Here `Pi_(p,e)`, all exceptional primes and the lower cyclotomic layers
are exactly those of `shared-rh-selmer-projectors`; the supplied-case
estimates of `shared-rh-supplied-cases` must hold on the same windows.
The constant is fixed at each accuracy before the fields and windows
grow. The general-character version uses its original twisted-prime
weights and ramification-normalized integral lengths; the RH projector
formula is not substituted into that version.

**Discharged subobligations.** Both finite-level cohomological bounds,
their exact limiting comparison, and the actual ordinary automorphic
module/diamond-trace construction now have proofs. The latter constructs
the original modules, including their full integral group-ring freeness
and augmentation quotient, rather than a replacement rational module.
Coefficient change, faithful good weight-zero classical specialization,
the actual integral Hecke determinant and exact classical Galois
compatibility are proved. The original compact types exist at arbitrary
conductor over the original coefficient ring; their full restriction-of-scalars
rank cost is retained. The actual Taylor--Wiles auxiliary modules and
both integral comparison maps now supply the full original `TWAut`
contract for each given arithmetic realization, with the exact source
multiplier and uniform exponent n!. The actual polarized coefficient
model now supplies every original `URep/S6` field at each supplied
normalized curve. Its exact original closed ideal and entire residual
radical are retained; its annihilator-prime implication gives no uniform
annihilator exponent. The actual tangent injections, second-order
ordinary compatibility and integral presentation now prove the full
original `GalOut` at every supplied curve, under exactly the original
three Selmer conditions. The full original `S5` patched-support supplier
now has an explicit construction: exact fibre support, dimension
`1+D_wt+n*q_TW`, and movement with unchanged prime contraction. Its
approximate-annihilation step preserves the original multiplier and
relation exponent; varying finite free ranks are allowed.

**First missing construction.** Construct the original nonzero arithmetic
seed with every prescribed residual and local condition, and finish the
global marked deformation model and prime-chain application. The patched
support may be empty and cannot replace this seed. Propagation must retain
the entire characteristic-prime fibre
and the actual two-sided rigidity. Neither qualitative finiteness,
fixed-point constants nor a torsion-free quotient proves the displayed
moving-family bound.

## W06: the integral theta construction

**Frontier theorem I.** For each entry of theorem A construct the
prescribed theta maps on the source and target lattices used in its
analytic norms. Prove their original selected-prime and auxiliary-level
image divisibilities for every integral test vector, with the original
periods, coefficient different, root phases, source twists and chain
ranks `N(i)=k+i(t+1)`. Obtain any required aggregate nonvanishing from
the source deficit of theorem N below; individual maps may be zero.

The type-prime mixed jets, discriminant clearing, adapted arithmetic
lattice, full-primary trace and arbitrary level-prime theta estimate
are proved. The actual models now have their integral theta section,
full `Model.N3` uniformization and torsion action, `PushInvertible`,
and degree-one `SplitFibres`. Reached-section regularity has scalar one.
Exact mixed pullback and all-place assembly give one original clearing
integer once the remaining good-cover and map comparisons are supplied.
The actual local `Good3` chart is now constructed over a finite unramified
extension, retaining every eigenlattice defect, the canonical gauge and
all original harmonic values with no additional valuation loss.
The first missing inputs are the exact good-cover compatibility,
theta spanning and the remaining divisibility laws for the same maps.
A constructed integral theta section does not supply the global norm.

## W08: the actual global period Gram operators

For the final restricted maps `T_(u,i):V_(u,i)->W_u`, put

\[
 S_u=\bigoplus_iT_{u,i}^*T_{u,i},\qquad
 Q_u=\sum_iT_{u,i}T_{u,i}^*,\qquad
 g_u=\frac{\operatorname{tr}((c_u/R_u)I-S_u)_+}{c_u},\quad
 b_u=\frac{\operatorname{tr}(Q_u-(c_u/D_u)I)_+}{c_u}.
\]

The positive `c_u` is prescribed by the original seed normalization;
`R_u,D_u` are the actual retained dimensions. Let `U_u,H_u` be the
original source slope spread and target height gap after the stipulated
map-height correction. The precise contribution to theorem A is

\[
 P_{\mathrm{norm}}(x)=\kappa(x)^{-1}
       \operatorname{avg}_u\min\{H_u,(g_u+b_u)(U_u+H_u)\}.
\]

**Frontier theorem N.** Identify the original global period operators
with their correctly normalized kernel expressions, retaining every
rational return, volume, compact type and restriction. Prove estimates
on their two positive traces which put this *actual* penalty into the
signed table budget of theorem A. If the chosen consumer needs a nonzero
family, prove `g_u<1` at that consumer's final normalization. An estimate
for an ambient projector or an unperiodized seed does not suffice.

A concrete stronger sufficient target, useful for testing a construction,
is `P_norm(k^4)<=C_eta (k^4)^(1/2+eta)` for each fixed `eta>0`, with
`C_eta` independent of the table size and all its arithmetic entries.
The final test allows the weaker jointly averaged signed budget, so this
pointwise target is not imposed on every possible solution.

**Discharged local steps.** The actual signed discrete-series and
period-normalized Bessel families supply the iterated weighted norms,
with original parameter reserves, character scales and Haar measures.
Their finite coefficient expansion holds pointwise throughout the
original big cell. The complete rank-zero orbital bound is proved,
with the stronger estimate b^4/G. No assertion identifies ordinary RH
with rank zero. The exact wave isometry for all signed residue words is also proved.
The mixed determinant inequality now supplies the original `SizeStd`
and `SizeStdCpt`, with every rational word correction and no inverse of
a degenerate residue form. Actual compact slices and the nonterminal
partial-head Fourier transfer are proved for every original block head
and admissible word. The actual compact complex Kloosterman density is
now proved at every block head, including singular internal minors. Its
stationary-phase constants depend on the fixed compact coefficient, which
is sufficient for the exact density conclusion. The next local suppliers
are the unitary-to-complex density transfer and terminal top lift.
The global arithmetic return sum and period-Gram identity remain
separate from every local norm identity.

## W10: the exact integral geometric supplier

**Frontier theorem G.** Complete the remaining good-cover comparisons
for the now-constructed original
integral models. Identify their actual integral section lattices,
heights and prescribed metrics, and construct the short spanning
families and multiplication bounds required by the established
geometric-filtration and determinant-degree theorems. Prove the
prescribed sheet/volume and cusp identifications so that the signed
boundary comparison applies to these very lattices. Bound the resulting
numerical section remainder in theorem A with its original rank factors
and exponent losses.

**Discharged construction.** The original generic moduli scheme,
full Tate-genus condition and exact half/full-level equivalence are
proved. Each original integral model satisfies complete individual
`LevelStructureConditions`, including all specified valuation rings.
Its integral theta generator, all coefficient expansions and exact
torsion action prove `PushInvertible` and full `Model.N3`;
`SplitFibres` holds with degree one. The actual global `N6` model
dominates every prescribed localization over the same number field,
with the original cartesian family and primitive-line comparisons.
The coordinated finite level transitions and exact Siegel comparison
now prove the original `N0` and full `N2`. The auxiliary prime is uniform
over all admissible half-levels, using their original imaginary-quadratic
descent condition.
The full formal-arc clause `N4` is now proved, including arbitrary
permitted evaluation maps and the original selected half-label. Thus
the complete source `PartI` construction is supplied on the coordinated
models, with its original coefficient fields and primitive lines.
The full local `Good3` chart and all-model uniformization are now supplied
at each original integral framed point after an unramified extension.
The harmonic-value comparison preserves the existing discriminant bound.

**First missing construction.** Construct the original good cover and
its precise field/component and integral-lattice comparisons. The
[component-field checkpoint](geometry-component-field-frontier.md)
constructs a ray-class field of the required numerical size; its action
on every original component is still unproved. Identify
the actual geometric section and height
inputs and prove their numerical arithmetic remainder. The existing
cusp, jet and signed-boundary lemmas are to be applied unchanged.

## Completion discipline

The shared mathematical fragments, their notes and certificates specify
the exact proven subobligations. The work-package acceptance lists remain
in `blueprint/grh/program.json`; the RH product and final budget remain
in its separate manuscript. No whole node is newly closed by the local
constructions above. The next research effort belongs to the actual
good-cover and section construction, the exact arithmetic seed and
global marked deformation models, and the
global period-return estimate, not further optimization of the already
proved frame inequalities.
