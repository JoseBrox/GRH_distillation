# Actual selected-prime chain and its original integral lattices

## Result and classification

**Closed local construction and compatibility obligation, independently
reviewed.** The focused theorem in
`paper/shared/theta-spanning-continuation-chain.tex` constructs the actual
point models, integral coordinate dictionary, phase-equivariant kernels,
and twisted stage-zero source for the original finite TC/ColIn chain.
It therefore supplies the previously explicit point-model and map-glue
hypotheses of the selected and conjugate divisibility arguments.

This is not a closure of all W06. In particular it does not identify the
TC/ColIn chain with the separately normalized global Poincare period maps
constructed in the W08 continuation. It establishes the original frame
form and finite class masses exactly on the TC side, so this remaining
comparison is now an equality between two specified constructions.

## Exact frontier supplied

For each admitted finite column datum, using the same coefficient field,
phases, normalized theta family, and direction constants as the established
ordinary CM construction, construct:

1. the original `PtModel`, with exact original class representatives and
   stabilizer orders;
2. `Coord.Ok` and `ValIs`, identifying point-value lattices with the
   prescribed localized coefficient lattices and their rational images;
3. `KerPt`, `KerIs`, and all five original `KerLaws`;
4. the original `Step0Tie`, including the literal rational-image definition
   of the twisted source, its prime-power scalar, residue norm operators,
   and ordered upper-neighbor product.

The construction is carried out, rather than retained as those four
hypotheses. The finite datum retains the original split-prime, level,
character, even-rank, hook and stabilizer bounds. The old normalized
ordinary-CM covariance, common finite coefficient-field construction,
simultaneous moment laws and local incidence theorem are used as proved
inputs, not assumed anew.

At a selected place, with `N_i=k+i(t+1)`, `h=(t+1)/2`, the theorem now
realizes the exact exponent

\[
 \ell=\sum_{i=1}^m\left(fN_{i-1}+\sum_\tau s_{i-1,\tau}
                  +\sum_{\tau\notin J}r_{i,\tau}\right)
       +h|J|m(m+1)/2-m\sum_{\tau\in J}b_\tau.
\]

The last summand is the original source twist, used once. At a conjugate
place the same actual maps retain the positive divisibility `T^(mfh)`.
Both are inclusions in the original embedded local lattices with unique
rational target lifts. No inverse or nonvanishing of any kernel is used.

## Construction details that matter

The point space includes the entire original root-of-unity phase group.
If `g` has underlying unitary map `gamma`, its phase is `chi(g)`. A point
represented by `(zeta,d)` transforms under `(gamma,eta)` to
`(eta*zeta/chi(g),g*d)`. The quotient relation is
`gamma(g)=1`, `zeta=zeta'*chi(g)`, and equality of the remaining off-prime
data. Adding the selected local lattice/functionals converts the latter
condition into actual equality of decorated lattices. This retains
stabilizer orders exactly. It is not an absolute-value argument.

The coefficient map is inverse polynomial frame evaluation. In conjugate
type the local embedding is conjugated and the actual dual frame is used.
The global target lattice is not an assumed saturation: uniqueness of the
polynomial, its stabilizer equations, and a product of finitely many
denominators outside the chosen place construct the rational lift.

The literal `Kmap` identity uses the exact ratio of `muInvDet` factors
divided by `chiF`, which equals the original product of `rhoAt` and
`rhoAt'`. The equality on character uniformizers and local units is retained.
The target polynomial condition is also literal: its residual partition
is the source partition plus the determinant exponent in the old
columns, followed by zeroes. Upper triangular target frame changes
give exactly this character before taking coefficients in the jet
variables. Each coefficient therefore already satisfies the target
homogeneity and column-addition equations, so the original target
projection is the identity. The authenticated weight recursion is
`Definitions.GaloisGeometry.TrueWtAddSSNonneg` 331–366, and its exact
`JetInVV` application is `JetStepEqZeroExample` 30–43.
The finite theta Fourier average, square-root index, common period and
ordinary mixed derivatives remain inside the same jets. No factorial or
new lattice index enters the comparison.

The hook-product theorem already proved in the recovered manuscript
supplies target Weyl/dual-Weyl equality. The source's imported
`Published.InducedSimpleLowestAlcove` is therefore not silently taken as a
new unproved mathematical input. The original endpoint
`mu_1-mu_n+n-1 <= T` is safe: the residual partition has last part zero,
so its largest actual hook is strictly smaller than T.

The phase extension preserves the **original frame Hermitian form**;
this is not a claimed isometry with an arbitrary Euclidean coefficient
norm. Stabilizer masses are unchanged. The original stage-zero class
equivalence preserves the decorated lattice, and both the residue-dilation
norm operator `Nm` and the upper-neighbor operator commute with it by
termwise equality. `Nm` is not confused with a normalization of evaluation.

## Bounded source evidence

All paths are under `lean/src/` in
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The script records Git blob identities, SHA-256 hashes and the exact
excerpts below. Source bytes are authenticated; no Lean build is claimed.

| Module suffix under `Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/` | Ranges | Decisive interface |
| --- | --- | --- |
| `OffOfNotMem` | 83–129, 130–156 | Actual off-prime split, unchanged markings and local modifications |
| `ExistsLevelPrimePointModelRealisation` | 39–94, 103–187, 189–251, 274–298, 421–475, 477–528 | Phases, local points, exact frame norm, class masses and actual realization |
| `ExistsCoordinatesValueLatticesEqWeylLattices` | 16–109, 112–180, 181–227, 229–275, 281–324, 394–423 | Exact polynomial coordinates, conjugate dual frames, value lattices and rational lifts |
| `KmapOfOkOfVecP` | 40–94, 96–142, 238–288, 290–309 | Ordinary-jet formula and exact original character/phase identity |
| `TrueChainKernelEqPointKernelAtRepresentatives` | 14–46 | Actual class-map equality at representatives |
| `ChThOkOfColIn` | 27–70, 80–100, 111–152 | Finite-indicator covariance of the same theta family |
| `MoveStep` | 26–43, 47–88 | Literal chain, actual point splitting, dilation and equivariance |
| `ExistsPointKernelRealisedModels` | 41–90, 114–188 | Unique complex extension and representative-independent phase kernel |
| `TrueChainKernelsBoundLevelPrimePlaces` | 17–59 | Selected scalar, same theta term and actual determinant shift |
| `TrueChainKernelsBoundConjugatePrimePlaces` | 19–63 | Conjugate scalar and same theta term |
| `ConjugatePrimeBoundPointKernelOfCoefficientKerne` | 33–68 | Transfer retaining the positive conjugate factor |
| `HeckeLawPointKernelOfCoefficientKernel` | 246–274 | Transfer of exact local incidence identity |
| `TwistedChainInitialLatticeCompatibleTrueColumns` | 20–48, 58–95, 109–136, 160–173 | Same initial decorated lattice, `Nm`, upper neighbors and original source tie |
| `ExtInOfValIn` | 58–85, 98–135, 139–198 | Allowance removal, exact step exponent, mass denominators and integral orbit sum |
| `LevelChainSharpColumnValuationOfPointKernelLiftL` | 21–25, 57–63, 78–91 | Actual downstream chain consumer |

Additional definitions authenticated by the script are `FormsStable`
128–240 and 307–328, `LevelChainSharpColumnValuationOwnChainIff` 45–75,
`ExistsRecordDat` 20–70, and the original `ColIn`/`AmbIn` clauses in
`TrueColumnChoicesHeckeCharReferenceEqOne` 127–147, 165–194, 219–261.

The certificate separately hashes the established recovered CM,
coefficient, incidence and exact product proofs. It checks a nontrivial
finite phase quotient, including phase lift independence and exact
stabilizer orders, and small exact integer kernel-lattice bases. These
are diagnostics of the displayed formulas, not substitutes for the
general construction and proof in the TeX file.

## Remaining boundary and next attack

No additional point-model hypothesis was found after checking the actual
finite datum and the normalized ordinary CM suppliers. The theorem does
not prove that every desired global host datum exists with a uniform
field degree; it uses precisely the common finite coefficient datum
already constructed. Its degree and root discriminant remain actual
parameters, not bounded constants. It does not close nonvanishing or
global norm estimates.

The decisive next identity is between the now-fixed TC/ColIn chain,
including its exact value norm and class masses, and the W08 literal
Poincare maps `Pu/sqrt(c0X)` with their source inclusions and retained
target restrictions. Agreement of representation type does not identify
these maps. Every compact type, `c0X`, period, finite Haar mass and radial
factor must appear in that comparison. The [sharp column valuation](theta-sharp-level-closure.md) completes
the separate auxiliary-level node for the reference and every twisted
column. The W06 work package remains partial.
