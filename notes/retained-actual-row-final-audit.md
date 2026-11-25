# Actual retained rows: exact reference identity, evaluation factor, and boundary

## Mathematical result

The new ordinary addition is `retained-actual-row-evaluation.tex`. It sharpens the previously recorded retained-row boundary in two ways, with all hypotheses stated on the original models and maps.

First, the source's original reference-row coordinate pins imply the theta identity with **scalar exactly 1**. At the reference tuple, the original row matrix is the identity. Expanding the original row coordinates in their basis gives

\[
i_C(\sigma_\epsilon w)=\Theta_{\mu_0}(j_R\operatorname{cr}(w)),
\]

and the literal `IotaRd`, `Seam.eR_eq`, and `CxFacts.theta` pins therefore yield

\[
\Theta_{\mu_0}(j_Re_Vy)
 =e_R(\iota_{\mu_0}c_F(\sigma y)).
\]

There is no additional analytic scalar in this coefficient calculation. If the actual good-range pin and original lattice norm tie are also supplied, the same map is onto the specified good complex row space with norm ratio `sqrt(n_P)`. The ordinary proof uses the actual algebraic basis, density of the fixed totally complex field embedding, and continuity. It does not infer the Petersson norm tie from equality of finite representation labels or finite class-pairing norms.

Second, the actual translated evaluation map has a completely fixed positive normalization. With the original Petersson embedding `h=HE.e`, original row lift `e_E`, and actual evaluation

\[
E_tT(x)=T(v_0)(\iota^{-1}(x)t),
\]

the precise source range and norm statements imply

\[
j=(c_{\rm ev}n_P)^{-1/2}E_t h e_E.
\]

Here `n_P` is the original row mass, and `c_ev` is the positive Haar ratio

\[
(\iota^{-1})_*\mu_{A,\mathrm{actual}}=c_{\rm ev}\nu_0.
\]

The same `E_t` obeys the previously proved exact finite-projector transport. No finite group order, compact representation dimension, formal degree, or observed row norm is inserted. The positive scalar is uniquely determined by this composite when the original row space is nonzero. In the zero-dimensional case the formula remains valid, but the zero map cannot determine a unique scalar.

## What this establishes for the joined scalar

Conditional on the actual reference-row pins, the scalar previously written `a_u=epsilon(d.a_u lambda) kappa_u` simplifies to

\[
a_u=\epsilon(d.a_u)\kappa_u.
\]

The anchored analytic scalar `d.a_u` and pairing conversion `kappa_u` still have to be computed for the same realized family. Replacing the literal period column `P_u` by `P_u/sqrt(c0X_u)` replaces this scalar by `a_u sqrt(c0X_u)`. Thus the target Gram still contains the corresponding squared moduli. The exact row normalization does **not** prove that these final moduli equal one.

## Concrete remaining application interface

The present finite TC/ColIn reconstruction gives the original finite class spaces, stabilizer masses, coordinate/projector identities, and scalar-one terminal period dictionary. To invoke the above lemmas for the actual `FamAllQ`/`PtRows` family, the ordinary reconstruction must still produce the following matching global objects and prove their original properties:

1. The complex theta model's `CxFacts.h2`, reference theta factorization and the actual `Read`/`Seam`/`IotaRd` pins for these finite spaces. In particular, the good range must be the specified global row space.
2. The original `RRTie`/`HLatTie` to the Petersson row metric, and the literal `e_E` range and squared-norm identities for the same original row quotient. These are the mathematical content of (RE4)--(RE5), not consequences of the finite projector.
3. The original group, finite-level and coefficient pins, plus onto evaluation, for the same finite placement `t`, lowest vector and row lift. The source has a genuine supplier route, described below; these inputs have not yet all been reconstructed here for the moving family.
4. The anchored all-word see-saw identity and pairing conversion for that same realization, including the scalar moduli relative to the original `c0X_u`. The actual `FamAllQ`/`LawsX` supplier has a [separate bounded audit](theta-family-laws-source-audit.md); the relation-transfer formalism alone is not its construction.

There is an actual source constructor; it is not correct to say that no source supplier exists. `ExistsSpectralLevelObjectsReplacedStages.exists_sRest_top` constructs the finite placement, evaluation tie, row isometry, and spectral rest. But its hypotheses explicitly include the actual `e_E` range and norm identities, group/coefficient pins, original models, and multiplicity-dimension tie. Its redivision construction must also be matched to the same original family, rather than replacing retained spaces merely to obtain an isometry.

By contrast, `SpectralStagePointRowPlacementTransfer` only transports the `see`, `ev`, and `rowJ` fields of an already supplied `SAt`. Citing that transfer as their constructor would be circular. Similarly, the finite TC/ColIn period equality alone is not a supplier for the global Petersson model and anchored all-word identity.

## Source ledger and verification scope

All sources are in `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, under `lean/src/`. These are bounded source checks and ordinary proof reconstructions, **not a Lean replay**. The relevant excerpts were read and retained in the current task's source cache.

| Source | Git blob | Checked range and role |
|---|---|---|
| `Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/GoodPartHasComplexCoordinates.lean` | `6d858d982efc6e1296b672e517d5bda782552d14` | 1--95: `Read`, `Seam`, `IotaRd`, `RRTie`, `CxFacts` |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ICCptEq.lean` | `6324d59e4937823c78a2af3d245656b151e59494` | 1--34: basis expansion and exact scalar-one `theta_eq` |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsImNeZeroOfTotallyComplex.lean` | `9fe9d6d558d61f980cf054739276abec67480b5e` | 1--85: onto row map and original `sqrt(n_P)` norm ratio |
| `Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ConcreteLevelAdelicSubset.lean` | `d09c663aa7a93b7c7ebbc7827a3ceddc39d2e639` | 1--75, 76--167: actual evaluation definition and `exists_rowJ_of_evalOn` construction |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/TranslatedRowEvaluationSquareIntegrableNorm.lean` | `0ad80d89639f47b552cb9867093f822e22921a58` | 1--90: original positive Haar ratio and exact quotient evaluation norm |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/GoodRowsCompareByLevelMatchingEvaluation.lean` | `86d556f401e42817d999fe960cdc48b2439329ee` | 38--90: actual onto evaluation supplier and its hypotheses |
| `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsSpectralLevelObjectsReplacedStages.lean` | `57cf9d36f0b6a49b410c031a407cb1751a31c897` | 1--40: actual spectral/row constructor, explicit range/norm and dimension-tie hypotheses |
| `Development/AbelianVarietyTheory/Proofs/FlagMeasures/SpectralStagePointRowPlacementTransfer.lean` | `3d4559938d4594af7d9bdc2c7ce586a2826c915b` | 1--48: transport of an existing `SAt`, not its supplier |

**Status:** the new reference-row and evaluation-normalization lemmas are proved with their actual pins stated. They reduce the scalar ambiguity and identify the precise original map. The original moving-family application, anchored scalar moduli and positive-trace budget are not thereby closed; W08 remains open.
