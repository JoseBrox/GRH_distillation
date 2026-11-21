# Fixing one local correspondence throughout the proof

## Finding and present status

The new mathematical proof can be organised around **one fixed, coherently normalised classical local Langlands correspondence**, instead of constructing global Galois compatibility separately for every map satisfying the weaker source interface. The precise smaller Galois contract is given below. Its conversion into fixed-family pair and self-dual Galois packages is proved directly from the original proof terms. A stronger local comparison then recovers the unchanged universal source row.

The two local preimage statements needed for that comparison are now proved and independently reviewed under the full local correspondence laws. The separate classical depth-zero type formula has also passed independent review. Thus the weak-correspondence quantifier is no longer an open local gate under those laws. The complete classical replacement still requires the exact full local-law dictionary and the global automorphic, weight and period-model dictionary. Until they are supplied, the source construction remains in the proof plan.

This note complements [the global-input analysis](lean-global-inputs.md), which checks the candidate classical Galois theorems and their remaining normalisation dictionary. It does not remove the separate global theta identity, geometric covolume, or growing-family estimates.

## 1. Where the universal interface actually enters

All paths below are relative to `lean/src/Development/AutomorphicArithmetic/` in the pinned mirror `jsmorph/rh` at `ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. Exact Git blob identifiers, SHA256 hashes and inspected ranges are in [the certificate](../certificates/fixed-correspondence-reduction.json).

`CharacterBoxes/MainConclusion.lean`, 7–11, passes the same Galois row three times: twice into `OpenLiteratureStatements` and once to `vwin_of_row`. The literature structure contains two copies of that row and an existence statement for weak local correspondences (`ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean`, 215–218). Here and below `ThirdPlaceSeries/` abbreviates `ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/`.

The two apparent Galois inputs are not two independently required existence theorems:

| Source route | Actual use of the row | Fixed-family replacement needed |
|---|---|---|
| `field_of_starFull_alt` | Constructs `PairUAlt` using the same row witness | The pair package with all local parameters evaluated at the fixed correspondence |
| `ofDual_star_alt` | Constructs `CarUAlt` for conjugate-self-dual representations | The self-dual package with the same fixed correspondence |
| `literature_automorphy.car` | Passes the row to `PublishedInputsCombined`, which constructs `CarUAlt` again | Reuse the preceding fixed-family self-dual package |
| `vwin_of_row` | Passes the row as `RowT` into the automorphy/window branch | Specialise `RowT`, the local Galois conclusions and their consumers consistently |

The first three facts follow from `ThirdPlaceSeries/SOfStar.lean`, 33–54; `EveryCharacterOfLiteratureOfVWin.lean`, 609–625; and `PublishedInputsCombined.lean`, 18–36. The finite-GL and local-correspondence arguments of `carU_of_finite_gl_recT` are unused: the proof is literally `fun _ _ h => h` (`SPairs.lean`, 15). Likewise the first three arguments of `field_of_starFull_alt` are unused (`SOfStar.lean`, 52–53). These wrappers introduce no additional mathematical content at this point.

The window route is explicit in `DenseThresholdCases/VwinOfRow.lean`, 4–5, and `TopMainZj.lean`, 38–58 and 71–74. The relevant `RowT` and `One.M.Row` are definitionally the same universal row (`AutomorphyLifting/WeakOfAtt.lean`, 47; `Foundations/UnitarySphericalFixing/SatakeParameters/RecT.lean`, 4–6).

## 2. The smaller Galois contract

Fix once and for all a family

\[
  \mathcal R_{E,\Omega,A,w,h}:
  \operatorname{Irr}\bigl(\mathrm{GL}_n(E_w)\bigr)\longrightarrow
  \operatorname{WD}(E_w),\qquad n\geq1.
\]

The notation on the right denotes isomorphism classes of Weil–Deligne parameters in the chosen realisation. The indices range over **every number field**, its algebraic closure, every finite place and every extension of that place to the closure. They are not restricted to the one field or rank of an eventual application. For each index, take the classical correspondence, transported into that realisation, with a single stated reciprocity convention. In source terminology the family must satisfy `IsRecT` at each index; the stronger classical laws together with the explicit depth-zero type law imply this (`Foundations/LocalLanglands/IsRecTOfIsRec.lean`, 91–112).

For every CM number field \(E\), algebraic closure \(\Omega\), prime \(\ell\), isomorphism \(\iota:\overline{\mathbf Q}_\ell\simeq\mathbf C\), rank \(n\geq1\), and regular algebraic polarized cuspidal representation \(\pi\) with its polarization character, require one representation \(r\), one integer weight and one family of Hodge–Tate multisets with the following properties:

1. The continuity, semisimplicity, infinity-weight formula and conjugate-weight symmetry are exactly those of `PropsB`.
2. At **every** finite place away from \(\ell\), and every chosen extension to \(\Omega\), require the `AwayB` comparison with
   \[
      \mathcal R_{E,\Omega,A,w,h}\bigl(\pi_w\otimes|\det|^{(1-n)/2}\bigr).
   \]
   Retain its dimension equality, exact toral comparison when the target monodromy vanishes, and tame squarefree inertia-character comparison with the stated residue-characteristic restriction.
3. Above \(\ell\), retain the spherical crystalline clause and all de Rham, potentially semistable and Hodge–Tate clauses of `AboveB`; in its local comparison clause evaluate the target parameter using this same \(\mathcal R\). Keep the original toral-or-tame-squarefree and zero-monodromy hypotheses.
4. Keep the source quantification over period models, their comparison data, all local algebraic embeddings and all induced embeddings. The fixed family does not select one convenient period realisation or one convenient \(\ell\)-adic embedding.

Call this contract \(\mathrm{Row}(\mathcal R)\). It is exactly `Row0b` with

\[
  \operatorname{Rc}_{\mathcal R}(h,rc)\quad\Longleftrightarrow\quad
  rc=\mathcal R_{E,\Omega,A,w,h}.
\]

The source already parameterises `PropsB`, `AboveB` and `Row0b` by an arbitrary relation `RecNotion`; only their endpoint instantiation chooses `IsRecT`. See `Foundations/GaloisRepresentations/TypeConditions/WeightsConjAlt.lean`, 16–18, and `WeightsConjBis.lean`, 39–73. Consequently the smaller contract is an exact specialisation of an existing interface, not an informal omission of inconvenient local conclusions.

**Quantifier order matters.** The family is fixed before any Galois representation is selected. For each global input, the same \(r\), weight and Hodge–Tate data must work at all places and in all the allowed period models. Choosing a different \(r\) separately at each place would not satisfy this contract.

## 3. What is proved by specialisation

### Proposition: the first pair and self-dual packages need only the fixed family

Let \(\mathcal R\) satisfy the local weak laws above, and suppose \(\mathrm{Row}(\mathcal R)\) holds. Define the fixed-family versions of `NiceAlt`, `IsGalUAlt`, `PairUAlt` and `CarUAlt` as follows:

- replace each universally quantified local correspondence in the compatibility clauses by \(\mathcal R\);
- replace `NiceAlt` by the assertion that there is a local component whose **\(\mathcal R\)-parameter** satisfies `NcW`;
- keep the global quantifiers, periods, normalisations and remaining conditions unchanged.

Then the fixed-family `PairUAlt` follows. With the source's contragredient identification, the fixed-family `CarUAlt` follows as well.

**Proof.** Apply \(\mathrm{Row}(\mathcal R)\) to the polarized automorphic representation. The source conversion `aw_of_away` turns its `AwayB` comparison into the pair package's `Aw` comparison. For a local component satisfying `NcW` for \(\mathcal R\), the dimension law gives the same toral-or-tame-squarefree guard used in `star_guard'_alt`. The fixed-family `AboveB.nice` clause then supplies exactly the required de Rham and Hodge–Tate conclusions. Its crystalline clause is unchanged. For a conjugate-self-dual representation, the same contragredient identification supplies the polarized pair, and the same above-prime clause gives the additional `Ab` comparison. These are exactly the proof steps of `SOfStar.lean`, 25–51, with the correspondence argument set equal to \(\mathcal R\). No comparison with a second weak correspondence occurs. ∎

This proof is a mathematical rechecking of the displayed proof terms; no Lean refactoring or new kernel build has been performed. It proves the stated replacement for these first consumers, not the whole downstream window theorem.

### A genuine obstruction to an automatic replacement

The original `NiceAlt` means

\[
 \exists\sigma,\;\exists rc\text{ satisfying the weak laws},\qquad
       \operatorname{NcW}(rc(\operatorname{algNorm}\sigma)).
\]

It appears in `ThirdPlaceSeries/WeightsConj.lean`, 21–29. This does **not** formally imply the corresponding assertion for \(\mathcal R\). Likewise the original away and self-dual clauses quantify every weak correspondence (lines 35–36 and 64–66). Merely changing the input row leaves those stronger conclusions unjustified.

There are two immediate valid routes:

1. Recast the downstream proof with the fixed-family predicates, and produce its local type hypotheses directly for the classical parameters.
2. Prove that every relevant weak-correspondence parameter agrees with the classical one. The source uniqueness theorem gives such agreement only when the automorphic representation lies in `Good`; that membership must be established at each required use.

No unproved converse from a toral/tame target parameter to `Good` is being assumed here.

### A shorter conditional route: recover the original universal row

There is a stronger local comparison principle that can avoid refactoring every downstream consumer.

**Good-preimage hypothesis.** At each local realisation, suppose every parameter \(y\) in either of the following two classes has a preimage \(z\) under the fixed classical correspondence such that \(z\) belongs to `Good`:

- \(y\) is toral and has zero monodromy;
- \(y\) is tame and squarefree, has zero monodromy, and satisfies the source's rank/residue-characteristic bound \(\operatorname{IsQpBig}(w,\dim y)\).

Here “tame” and “squarefree” refer to the exact source predicates `TmW` and `Sqf`; identifying them with an informal classical condition is part of the local bridge. Assume also that the fixed classical correspondence satisfies `IsRecT` with the same normalisation.

**Proposition.** Under the Good-preimage hypothesis, \(\mathrm{Row}(\mathcal R)\) implies the original universal `Row0b IsRecT`.

**Proof.** Let \(rc\) be any weak correspondence, let \(x\) be a local irreducible representation, and suppose \(y=rc(x)\) is in one of the two classes. Choose \(z\in\mathrm{Good}\) with \(\mathcal R(z)=y\). Weak-correspondence uniqueness on `Good` gives

\[
  rc(z)=\mathcal R(z)=y=rc(x).
\]

The weak injectivity law has exactly the needed direction: equality \(rc(x)=rc(z)\), together with \(z\in\mathrm{Good}\), implies \(x=z\). Therefore

\[
  rc(x)=\mathcal R(x).
\]

Now use the **same** global representation, weight and Hodge–Tate multisets supplied by \(\mathrm{Row}(\mathcal R)\). The dimension clause of `AwayB` holds for arbitrary \(rc\), because both local correspondences satisfy the dimension law. Whenever a toral or tame comparison is requested, the displayed equality identifies its target with the classical target, so the fixed-family comparison applies. The same argument handles `AboveB.nice`; its rank bound agrees with the parameter-dimension bound by the dimension law. Continuity, semisimplicity, weights, conjugate weights and the spherical crystalline clauses do not mention a choice of correspondence. All period and place quantifiers therefore remain unchanged. This proves the original row. ∎

The argument is purely local before the final substitution, so it proves compatibility with *every* weak map without choosing a new global Galois representation for each map. It also transfers the old existential `NiceAlt` witnesses to the classical family, since the source guard converts `NcW` into one of the two classes above.

This proposition has passed independent review. Its Good-preimage hypothesis is now discharged under the full local correspondence laws in [the local-correspondence bridge](local-correspondence-bridge.md): the support-polynomial identity and irreducibility force every cuspidal-support factor to have rank one in the toral case; the full depth-law converse and the first-congruence fixed-vector lemma give `Good` in the tame rational-local-field case. These arguments need neither zero monodromy nor squarefreeness nor the lower residue-characteristic bound, although those conditions remain in the global compatibility clauses.

The separate [classical depth-zero type formula](lean-global-inputs.md#the-classical-depth-zero-type-formula) has also been checked: the finite-field cuspidal type and compact-induction correspondence give the exact inertia polynomial; the unramified quadratic correction disappears on inertia. This supplies the required type comparison with geometric Artin normalisation. The exact full local-law dictionary and the global automorphic/period-model dictionary remain open; the local preimage and type-formula gates do not.

## 4. The actual choices and the coherence requirement

`RecTExists` quantifies all number fields, closures and finite-place realisations and asserts the existence of a weak correspondence (`IsRecTOfIsRec.lean`, 78–80). Its proof chooses local reciprocity, a cuspidal correspondence, and a Langlands extension, then proves the required laws (`LocalCentralUnits/RecTExists.lean`, 20–66). The theorem by itself contains no selected family or independently stated naturality condition.

The window code makes fresh existential eliminations at concrete points. Representative inspected sites are:

| Site | Source action | Fixed-family action |
|---|---|---|
| `AutomorphyLifting/ExistsRec.lean`, 21 and 25 | `exRec′` and `exLL′` call `recTExists` | Return the selected \(\mathcal R\) with its laws |
| `DenseThresholdCases/GuPolG.lean`, 26–31 | Chooses a map for the de Rham conclusion; other clauses accept arbitrary maps | Select \(\mathcal R\) and specialise the other local conclusions too |
| `DenseThresholdCases/RROrdAway.lean`, 57–72 | Chooses a map, applies Galois compatibility and local principal-series identities | Apply the same identities to \(\mathcal R\) |
| `DenseThresholdCases/RROrdAbove.lean`, 29–30 | Chooses a map and extracts its reciprocity normalisation | Use the chosen family and the same normalisation |
| `DenseThresholdCases/TTypePST.lean`, 14–16 | Chooses a map to turn local type information into a potentially semistable conclusion | State and use the type condition for \(\mathcal R\) |

A local text search found 47 files containing 55 non-import lines mentioning the three witness functions `recTExists`, `exRec′` and `exLL′` inside `Development/AutomorphicArithmetic`. This is a locator inventory, **not** a proof-dependency count, and includes unused or alternative declarations. The certificate records its bounded path/line inventory. The representative sites above have been read and byte-verified; the other sites are a remaining audit queue, not verified replacements.

Fixing arbitrary choices by the axiom of choice alone would not establish coherence. The family must respect the field, closure and place identifications actually used in descent. The source's `RecTTransport` states the precise comparison under `PlaceIso` and `RepRel`, with conclusion `WDRel`, for `Good` representations (`Foundations/LocalLanglands/RecTTransport.lean`, 317–324). Its uniqueness theorem also compares weak correspondences only on `Good` (`LocalCentralUnits/RecTUnique.lean`, 28–53). These are adequate at a use already proved to be `Good`. Any use outside that class needs the full classical transport theorem or a separate proof. The classical depth-zero type law must also be retained; it is not supplied merely by a notation saying “the local Langlands correspondence”.

## 5. Proposed replacement program and the exact stopping point

The preferred route is now to finish the exact full local-law and global automorphic/period-model dictionaries, then use the proved preimage lemmas and the preceding proposition to retain the existing downstream interfaces. No separate downstream fixed-family refactoring is needed for this route.

The following fixed-family refactoring was the earlier alternative. It remains available if a future exposition deliberately chooses a narrower local interface, but it is not the current open-preimage task:

1. State the classical local correspondence once, with the reciprocity, algebraic twist, depth-zero type and transport conventions needed by the proof.
2. Prove \(\mathrm{Row}(\mathcal R)\) from the classical global Galois theorems, including the period-model and weight dictionary described in `lean-global-inputs.md`.
3. Use the proposition above to obtain the pair and self-dual packages, sharing the same global witnesses whenever their hypotheses coincide.
4. Specialise the window and local-type predicates to this same family. Audit the identified witness sites and any transport or comparison that previously accepted arbitrary weak correspondences. In particular, never reuse the old existential `NiceAlt` without a comparison proof.
5. Reconnect the specialised packages to the remaining theta, covolume and window constructions; prove the same final scalar estimates and apply the already established analytic criterion.

The source contains a parallel stronger-correspondence route: `recFull` is `IsRec`, and `TypeConditions/OfStar.lean`, 60–83, converts `Row0b recFull` into the analogous pair and self-dual packages. This provides a useful model for the new exposition, but those stronger-correspondence packages have not been substituted for all current weak-correspondence consumers.

**Current conclusion.** Under the full local correspondence laws, a fixed-family Galois row supplies the original universal weak-correspondence row with the same global representation, weight and Hodge–Tate data. The two local preimage proofs and the classical type formula are complete at their stated mathematical interfaces and have passed independent review. The remaining obligations are the exact full local-law and global automorphic/period-model dictionaries. Consequently the source's geometric-seed, congruence and theta-lift construction is still retained as a complete source route; no independent theta-integral or geometric-covolume branch is removed by this reduction.
