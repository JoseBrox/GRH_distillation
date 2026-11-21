# Audit of the stated theorem and its first reductions

## Scope and status

The source inspected is the public mirror [jsmorph/rh](https://github.com/jsmorph/rh), pinned to commit
[ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de](https://github.com/jsmorph/rh/commit/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de).
This note records selected source inspection on 2026-11-21. It is not a successful build, a kernel check, or an audit of the complete transitive dependency graph.

The inspected set contains 24 Lean files and the toolchain, manifest, and Lake configuration. The accompanying JSON lists exact paths, blob hashes supplied by GitHub, imports, and declaration locations. A simple lexical scan of these 24 source files found no tokens `sorry`, `admit`, `sorryAx`, `native_decide`, `implemented_by`, or `axiom`. This limited observation does not establish their absence from the remaining source or from compiled dependencies. GitHub text search is also not a completeness certificate.

The source pin specifies Lean `leanprover/lean4:v4.33.1` and Mathlib commit `0df444a360eaa60ab8c11dca51a86af692955474`. Lean and Lake are unavailable in the current runtime. The mirror README itself reports that its maintainer had not built or read the proofs.

No specific mathematical contradiction has been established by this inspection. No independent verification of the announced GRH proof has been completed.

## What the top-level theorem actually asserts

[Statements.lean](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Statements.lean) defines four predicates.

- `RiemannZetaZerosOnLine`, beginning at line 3: every zero of the Riemann zeta function other than the negative even integers, with the point 1 explicitly excluded, has real part 1/2.
- `DirichletLNonvanishingRightOfHalf`, beginning at line 6: for every positive modulus and every Dirichlet character, the Dirichlet L-function is nonzero for real part greater than 1/2, except for the principal-character point at 1.
- `DirichletLZerosOnLine`, beginning at line 10: every zero of every Dirichlet L-function in the open strip 0 < Re(s) < 1 has real part 1/2.
- `PrimitiveDirichletLZerosOnLine`, beginning at line 14: the same assertion restricted to primitive characters.

[Main.lean](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Main.lean) exposes five theorems:

| Declaration | Line | Supplied proof |
|---|---:|---|
| `riemannHypothesis` | 4 | `rhOfAll` |
| `riemannZeta_eq_zero_re` | 6 | `rhOfAll` |
| `LFunction_ne_zero_of_half_lt_re` | 8 | `allChi` |
| `LFunction_eq_zero_re` | 10 | `claimAll.2.1` |
| `LFunction_eq_zero_re_of_isPrimitive` | 12 | `critAll` |

Thus the GRH assertion at the exposed interface concerns Dirichlet L-functions, for arbitrary characters and arbitrary positive moduli. These declarations do not assert GRH for all automorphic L-functions or for all number-field zeta functions. Those broader conclusions must not be attributed to these declarations without a separate theorem.

## A complete classical reduction

Two source files contain a comparatively short mathematical argument that can be checked without following the entire automorphic construction:

- [ClaimStrip.lean](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean).
- [CritLine.lean](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Formalism/GammaFactorNonvanishing/CritLine.lean).

In ordinary mathematics, if a character chi modulo N is induced by a primitive character psi modulo q, then

\[
L(s,\chi)=L(s,\psi)\prod_{\substack{p\mid N\\p\nmid q}}
             (1-\psi(p)p^{-s}).
\]

For Re(s)>0, each added factor is nonzero because its second term has modulus at most p^{-Re(s)}<1. The primitive and imprimitive functions therefore have the same zeros, with multiplicities, in this open half-plane away from poles.

The primitive completed function satisfies

\[
\Lambda(s,\psi)=\varepsilon_\psi\Lambda(1-s,\overline\psi),
\qquad |\varepsilon_\psi|=1.
\]

Its gamma and power factors are finite and nonzero throughout 0<Re(s)<1. A zero with real part below 1/2 consequently gives a zero for the conjugate primitive character at 1-s, whose real part is above 1/2. A universal nonvanishing assertion to the right of 1/2 excludes both possibilities.

The associated manuscript section gives a complete derivation of the primitive functional equation using Gaussian Poisson summation, including the primitive Gauss-sum identity and the conductor-1 zeta case, rather than merely citing a functional equation without normalization.

### Edge cases verified in the reduction

1. A positive modulus is required. In Lean this is `[NeZero N]` with N a natural number.
2. The conductor is positive. The Lean code explicitly obtains the corresponding nonzero instance where needed.
3. The primitive principal character has conductor 1. Its completion has poles at 0 and 1, both outside the open strip.
4. For a nonreal character, the reflected zero belongs to the conjugate (inverse) character. It need not belong to the same character.
5. The imprimitive Euler factors can have zeros on Re(s)=0. They cannot be discarded on that boundary.
6. The original interface excludes the principal-character value at 1. An ordinary complex-analysis presentation should describe this as a pole, rather than use the totalized function value chosen by a proof assistant.
7. No uniformity in the conductor is needed for the reflection argument. Universal quantification over the characters is essential.

In the Lean file, the relevant declarations are `factor_ne_zero` (line 7), `prim_zero` (23), `gamma_ne_zero` (35), `prim_reflect` (42), and `strip` (59). The further zeta reduction `zeta` begins at line 75 and also uses Mathlib's nonvanishing for Re(s) >= 1 and the characterization of gamma-factor zeros. Its assumptions should be tracked separately if that part is reproduced.

This reduction is proved. Its nonvanishing input remains the central unverified part of the present human-readable distillation.

## Where the difficult input enters

[MainTheorems.lean](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Supplements/Kernels/MainTheorems.lean) defines `allChi` by applying
`UpperTheory.FinalTheorems.everyCharacter`.

[MainConclusion.lean](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean) contains:

- `everyCharacter_of_row` at line 7, conditional on a Galois-representation existence-and-compatibility statement named `Row0b`.
- `everyCharacter` at line 10, supplying `galoisLocalGlobalStrong_recParameter` for that input.
- An RH corollary at line 13.

The proof of `everyCharacter_of_row` calls
`every_character_of_literature_of_vWin`, with an explicitly constructed collection of input theorems and with `vwin_of_row`. The long file
[EveryCharacterOfLiteratureOfVWin.lean](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean)
collects many analytic, representation-theoretic, geometric, and arithmetic results. Its presence does not make these results assumptions in the final theorem: they are supplied by proof terms. Nor does their naming establish that their mathematical formulations match every conventional literature theorem. That correspondence and the proofs are substantive remaining audit tasks.

### Meaning of the Galois-representation statement

[WeightsConjBis.lean](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/TypeConditions/WeightsConjBis.lean) defines `Row0b` at lines 69–73.

It quantifies over a CM number field, an algebraic closure, a prime ell, an embedding of the ell-adic algebraic closure into the complex numbers, a positive rank, and a regular algebraic polarized cuspidal representation. It asks for an ell-adic Galois representation, an integer weight, and Hodge–Tate weight multisets satisfying `PropsB`.

The explicitly visible fields of `PropsB` include continuity, semisimplicity, local compatibility away from ell, the relation between infinity types and Hodge–Tate weights, conjugate weight symmetry, and local conditions above ell. Some local assertions are restricted by predicates describing toral or tame, squarefree, zero-monodromy cases. In particular, the helper predicate `IsQpBig` includes rank 1 or a residue prime greater than 16 times the square of the rank. It would be inaccurate to summarize this as unrestricted local-global compatibility at all places.

### The next two proof inputs

[RowSrc.lean](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/RowSrc.lean) supplies the Galois statement by applying `galoisRepresentations_of_thetaLift` to a theorem of stable theta-lift existence.

[GaloisRepresentationsOfThetaLift.lean](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GaloisRepresentationsOfThetaLift.lean) splits its input into:

- A geometric realization statement, supplied by `Geo.geoOne_holds`.
- A stable theta-lift statement, supplied by `TP.K.tLiftK`.

The [integral-structure development](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/Development.lean) also assembles congruence, trace-limit, descent, and compatibility results.

The [geometric realization](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/WeightOneGeometricRealization.lean) is supplied through a holomorphic Lefschetz formula for finite étale correspondences. The inspected general [Lefschetz source](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/LefschetzFixedPointFiniteEtaleCorrespondence.lean) assumes a smooth projective complex scheme, two finite étale correspondence maps, an explicitly finite fixed-point set, tangent matrices, and nonvanishing fixed-point denominators. It proves a finite-dimensionality assertion and the expected alternating trace formula by reduction to integral open-and-closed components. The integral case and the supporting geometric statements have not all been checked.

The [theta-lift definition](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/HalfIndexLattices/TLiftK.lean) has an eventual-rank quantifier and explicit signature, Hecke-character restriction, infinity-type, and weight inequalities. The [supplied proof](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/TPGHolds.lean) collects Siegel–Weil, level, norm, local representation, convergence, and differential inputs. None of these may be silently removed in a short proof.

## What remains to validate

A defensible next audit should distinguish three tasks.

1. **Formal checking.** Rebuild the pinned source with the pinned Lean and Mathlib versions, verify import resolution, and inspect the axiom dependencies of all five top-level declarations. Merely searching source text for the word `sorry` is insufficient.
2. **Mathematical interpretation.** Unfold each proposition at the reduction boundary and compare it with its standard mathematical meaning, including local restrictions, exceptional characters, nonempty structures, rank thresholds, positivity, denominators, and quantifier order.
3. **Distillation.** Prove a small number of ordinary mathematical estimates sufficient for the desired nonvanishing theorem. The actual estimates must carry all parameter dependencies. The half-plane conclusion cannot serve as a disguised assumption.

There is an additional analytic route worth auditing in
[ZeroFreeAllOfTopG.lean](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Development/AutomorphicArithmetic/CharacterBoxes/ZeroFreeAllOfTopG.lean):
it passes from connected families and character-host conditions to primitive nonvanishing. The earlier
[explicit-formula interface](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ExplicitFormulaErrorOfHostConditions.lean)
defines a weighted Chebyshev expression and the assertion that an eventual upper bound implies zero-freeness. That assertion is a definition in this file; its proof lies elsewhere. A paper must not present the definition itself as the required analytic theorem.

