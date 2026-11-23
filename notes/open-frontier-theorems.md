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
deformation models' remaining two-sided rigidity
argument for the now-constructed support, ordinary modules and integral Hecke
determinant, retaining their stated ordinary local conditions. For those same
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
For the actual prime-to-ell character inputs, the ordinary arithmetic
seed is now constructed at the original level and field, with every
residual, inertial, ordinary, polarization and automorphic clause.
The rank-two CM twist is now constructed under the full original
`Twist` contract, with its exact conjugate and outside-coset square
identities and one inertia exponent prime to ell. This includes
ramification at two and both fields with extra units, without any
class-number restriction or arithmetic field extension.

The full original `PT` arithmetic-point implication is now proved for
ranks two through four. Lowest-weight evaluation embeds the constructed
classical ordinary eigenvector into the original completed scalar module,
with the exact residual block and every local uniformizer factor.

The actual marked universal ring and its exact six relation families now
supply all S5 hypotheses. Finite-flat splitting, local completion and
coefficient descent prove the full original `Core`, `CoreBC` and `Raw`
prime-chain propagation contracts, retaining every original linking prime
and an explicitly supplied stable starting prime in support.

The exact normalized coefficient curves and arithmetic auxiliary tower
are now constructed. Their actual local/global cohomology systems retain
the original inertia quotient, cyclotomic action and all local degrees.
These supply the full original `PfromAut`, hence `P1core`, `P2core` and
`P3core`, with exponent `n*[F:Q]+n*q` and unchanged curve kernels.

The same actual Hecke ideal now satisfies the complete original
`HidaProps` and `Modular` contracts. Full integral control at every
algebraic weight, fixed-weight density, all arithmetic-point Speh
decompositions, the distinguished-prime kernel conditions and exact
finite twisting are proved. This is original `ModU`, not the stronger
`ModUAlt`. An actual absolutely irreducible seed lies on a stable Hecke
component of dimension `1+n*[F:Q]`. The actual normalized `SeedIn`
transfer is now proved in ranks two and three, together with a stable
starting chart of dimension `n*[F:Q]+2`. It uses a finite homogeneous
entry algebra and recovers exactly the original Hecke quotient, with
no integral realization of generic matrix entries assumed.

The [actual rank-two curve and propagation theorem](selmer-support-continuation-rank-two-propagation.md)
now supplies the original `PropagationTheoremGL2`. It preserves `FinLam`,
all `Ok`/`Big` local-degree inequalities, the ordinary obstruction cone
and the exact arithmetic `P1` condition. It uses algebraized entry fields
before completion; no bound on a completed fraction-field transcendence
degree is assumed.

The [rank-three propagation theorem](selmer-support-continuation-rank-three-propagation.md) now supplies the actual type-E finite-weight ideal and the Sharp determinant section with its nonsplit thick links. The [arithmetic transfer](selmer-support-continuation-rank-three-transfer.md) verifies the original coefficient surjection, Nice/Thick conditions and full P1/P23 chain, including characteristic three. Thus the original rank-three AllGood/OffFin conclusion holds for the actual Hecke ideal.

The [finite-point theorem](selmer-support-continuation-finite-points.md) now supplies the complete original AbsMain: both GoodPt assertions and FinPt with every original DVR/field-test quantifier. A residue-pullback coefficient ring gives the exact universal map, and one balanced upper/lower monomial forces triangularity at fixed characteristic-prime weight.

**First missing construction.** Supply the actual GalLink/auxiliary frame and finite-endomorphism transfer giving two-sided global rigidity, then discharge the moving-family integral Selmer budget. The entire characteristic-prime fibre, nilpotents and integral torsion remain part of these requirements; support coverage gives no uniform nilpotence exponent.

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
Exact mixed pullback and all-place assembly now prove the whole original
`CovInt.integral_smul_thLa` implication on the actual cover: one `intZ`,
fixed before the generator, clears every original valuation test and
satisfies the required uniform logarithmic size bound. The literal
raw-theta value identity transports by harmonic base change; its two
finite indices and determinant-ideal scalar are retained.
The actual local `Good3` chart is now constructed over a finite unramified
extension, retaining every eigenlattice defect, the canonical gauge and
all original harmonic values with no additional valuation loss.
The full original sized good cover and its normalized complex dictionary
are now constructed. The actual raw theta section is now constructed over
every coefficient algebra, with its literal value and original classical
scalar. In the required positive-weight range it belongs to the original
bounded cusp space, so the same clearing integer gives its integral image.
The actual polynomial Gaussian now satisfies the full original
thin-slab integrability and reproducing contracts, including even `n=2r`,
rank zero and definite signatures. The proof retains the actual frame
Jacobian, every derivative factor and the positive reproducing scalar;
no arithmetic uniform lower bound is inferred.
The exact original Siegel--Weil class-sum comparison now holds for every
actual Host and every admitted family, with its principal-level marking,
automorphism mass, determinant phase and original rational Weil operator.
The Host's everywhere-finite-unramified condition is retained in the
local-genus identification. The exact harmonic heat comparison is now
proved for the actual class-sum difference, including its doubled
Gaussian and invariant derivatives. The explicit finite Schwartz
system now satisfies all the original `IsSystem` clauses and gives
the level-theta span. The identity-cover transfer proves the actual
`HolSub0LeSpanRaw`, retaining the full arithmetic character, common
component coordinates and prescribed principal level. The [short theta theorem](theta-spanning-continuation-short.md)
now proves the literal `ExistsGoodCoverAtMinimalLevel`: a finite integral
K-span with norm at most `exp(30000 X^2 kappa)` in every original
component and coefficient embedding. The determinant scalar keeps and
cancels the exact lattice index. The [actual key shift](theta-spanning-continuation-key.md) now
removes the tag integrally, retains the original primitive boundary line
and all dyadic/ramified factors, and supplies the exact shifted family.
The [actual local-chain theorem](theta-spanning-continuation-chain.md) now constructs the point/phase models, exact integral coefficient coordinates, all local kernel laws and the literal twisted initial source. It supplies the selected exponent and positive conjugate gain for the original finite TC/ColIn chain, keeping its frame form and class masses.

**First missing identity.** Identify that specified chain, after its original source twist and all retained cuts, with the global Poincare operators normalized by the original c0X. Retain the exact coefficient norm, periods, finite Haar masses, compact types and radial factors. Neither representation-type agreement nor local divisibility supplies this identity or the global trace bound. The original growing coefficient field remains part of its quantifiers.

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
is sufficient for the exact density conclusion. The actual unitary-to-complex
transfer now supplies `PhiZero` and `DensC` at every original head,
with the exact compact factors, cofactor normalization and Haar constants.
The actual compact top lift and terminal `HeadTop` are now proved
under their unchanged original place and operator hypotheses. Their
cutoffs and inverse spectral factors enter exact identities only.
The original compact `KernelFourierIntegralBound`, continuity at zero
and full diagonal positivity are now proved with the exact point
normalization. Every original admissible old word is covered by the
unused-block construction, and all rational word corrections remain.
The original compact off-diagonal kernel bound is now proved, including
actual `LiftDegAll` and `DegLift`. Its degree is exactly `2j-s` after
Jacquet transform, with every sign, shift and two-head normalizer retained.
The original compact block-growth estimate is now proved by the actual
Banach-valued matrix germ, an invariant mean retaining the residual Gram
term, and a pointwise Fejer argument on the exact sampling lattice. The
full original `FormLimit` now extends these kernels through the prescribed
compact exhaustion at every head, with one fixed finite decay exponent
and a threshold depending only on the original top-lift constant.
The terminal normal form now proves the original `PolyTop` degree drop
and its exact leading factor. The ordered radial recurrence and the
actual first-component word update give `RadAATop`, `TopFirst` and the
full arbitrary-grid `DegTop`, retaining the prescribed operator and its
differential realization. The actual controlled top lift is now constructed
on every valid source cut: `TopLiftExists3` holds with `Cb=11`, original
`InDDplus2`, the exact recursive radial action and full empty-word identity.
It permits `k=1`; the actual arithmetic place package also has `k>=2`.
The unrestricted differently named source predicate is not substituted.
The original `WuDecay` and coefficient integrability now hold for every
existing arithmetic setting under its exact gap hypothesis. Weighted
Tonelli in the actual induced space gives the original exponent, and a
compact reproducer fixes its prescribed seed exactly. Neither the setting
nor a uniform bound is inferred. Actual arithmetic folding now supplies
`MultPoly` and `IUnfold`; the original finite phases and level splitting
supply `PhWellDef`. Every framed rational return is absolutely summable
in the established gap range, with the original unipotent intersections,
finite indices and Haar factors. The [period identity](global-gram-continuation-period-identity.md)
now supplies actual `EntryUnfold` and `KExpansion`, including the exact
antiunitary coefficient dictionary and original normalizers. The [actual
projector theorem](global-gram-continuation-projectors.md) supplies full
`InHH` and `PuLinear`: the original `HHX` projector fixes all periods, so
that particular target cut has exactly zero loss. The
[arithmetic minimum](global-gram-continuation-minimum.md) controls the
source's higher-rank `leastSize` by the original quotient norm uniformly
over the finite columns. The [quantitative seed theorem](global-gram-continuation-quantitative.md) now proves an explicit normalized moment of order `10n^2` and its weighted L1 consequence, without an unspecified compact-mass reciprocal. Exact transport of the original additive character removes uncontrolled frame heights. Under the cited `FarBound`, this gives an explicit far-return integral in terms of the field, T, weights and original Haar ratio. It does not by itself make that contribution small in the final trace budget.

**First missing construction.** Identify this Poincare Gram operator with
the final restricted arithmetic chain and its scalar class-kernel
dictionary, retaining every further target projection. Prove the uniform
positive trace deficit/excess bounds for these same maps. In particular
the remaining intrinsic Haar/covolume factors and near-return contributions must be controlled as the field grows, and the explicit far bound must be absorbed with the actual final normalizers.

## W10: the exact integral geometric supplier

**Frontier theorem G.** For the now-constructed original integral models
and sized good cover, identify their actual integral section lattices,
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
The actual level cover now supplies every `DeltaDat.IsLev` field, the
formal connection over every coefficient algebra and exact framed lifting.
The ray-class compositum now supplies the literal `FnAlgClosed`, relative
normality and the prescribed field-size bound for every original component,
including all ranks and both definite signatures.
The normalized complex `Member` theorem now constructs the original
primitive theta section, probability norm, squared multiplier, all six
adelic dictionary laws and exact `AA*L0` marking. Together these supply
the whole original sized `Deep.Good` contract. The actual raw-theta sections
now descend over arbitrary coefficient algebras and lie in the original
bounded cusp space under `CovGmin.Hyp`, with all normalization factors and
both finite indices retained. Their integral image follows from the
established uniform clearing integer. The actual finite theta system
and identity-cover comparison now give algebraic spanning. Hodge
semipositivity, the exact logarithmic canonical weight and effective
adjoint separation now prove the required nef/big lines, generation
on the interior and both birational cusp systems under the original
weight gaps.

The actual minimal-level short integral span now has its uniform
Petersson bound. The [flat-degree theorem](theta-spanning-continuation-flat.md)
supplies `FlatExistsAt` with the exact finite correction; the
[parallel-twist theorem](theta-spanning-continuation-twist.md) supplies
`UnramPts` and controlled integral parallel sections over the original
field, including the normalized bad-prime rounding cost.

The [key-weight theorem](theta-spanning-continuation-key.md) now proves
the original integral shift, including at two and on the prescribed
boundary arcs, and supplies both literal `h0` and `hsh`. Its same-field
short-span bound is `exp(400000*(X^3*S+X^5))`; the original size
inequalities absorb this after a permitted fixed starting threshold.

**First missing construction.** Supply the actual pointwise Bergman,
height and multiplication comparisons, then prove the numerical
arithmetic section remainder for these same lattices.
The existing cusp, jet and signed-boundary lemmas are to be applied unchanged.

## Completion discipline

The shared mathematical fragments, their notes and certificates specify
the exact proven subobligations. The work-package acceptance lists remain
in `blueprint/grh/program.json`; the RH product and final budget remain
in its separate manuscript. No whole node is newly closed by the local
constructions above. The next research effort belongs to the actual
arithmetic section construction, the marked characteristic-prime support and
global marked deformation models, and the
global period-return estimate, not further optimization of the already
proved frame inequalities.

The [actual thick-region theorem](geometry-bergman-continuation-thick.md) now supplies the precise lower Bergman estimate `exp(-C(l1(u1)+(fr)^8))`, with an absolute constant and the original chart, metric, component probability and Haar normalization. A tensor/Minkowski argument uses the exact trace-self-dual lattice to prove thick injectivity; a complete-quotient dbar construction and regular-weight cuspidality give the actual cusp peak. The original numerical host inequalities connecting this exponent to `lenT`/`unitE` remain explicit. The next analytic inputs are the thin theta-pivot lower bound and the global integral cusp-frame upper bound.
