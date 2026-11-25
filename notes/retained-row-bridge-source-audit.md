# Concrete retained-row bridge: exact finite projector and unresolved evaluation

## Result

The finite-projector subsection in [retained-column-positive-traces.tex](../paper/shared/retained-column-positive-traces.tex) proves the exact finite-projector transport for the actual translated evaluation map, with the original reduction quotient, idempotent coefficients and Haar density displayed. The congruence-fibre volume cancels exactly. The formula is

\[
\mathfrak c G_{\rm an} \mathfrak c E_t=E_t e_{\rm TC},
\qquad \mathfrak c=\text{complex conjugation}.
\]

This identifies the good projections on the evaluation image. It does not manufacture an onto evaluation map or identify the actual theta row lift with it. The last paragraph gives a two-column example with equal individual norms and equal block-diagonal source Gram, but target excesses 0 and 1/2 at the same prescribed normalizer. This is a diagnostic of the missing common-row identity, not a counterexample to the actual arithmetic data.

The addendum also records the precise joined scalar. If the actual base-tuple anchored identity, common row tie and pairing conversion are supplied, the Bessel dictionary has

\[
a_u=\epsilon(d.a_u\lambda)\kappa_u,
\qquad B_u(x,y)=a_u\langle JV y,P_u I_u U_u x\rangle.
\]

The source and row coordinate similarities become unitary conjugations because their positive norm factors cancel. Normalizing the literal period map to \(P_u/\sqrt{c_{0X,u}}\) replaces \(a_u\) by \(a_u\sqrt{c_{0X,u}}\), not by 1. This concrete normalizer must accompany any later positive-trace transfer.

## Exact unmatched map

The finite normalized TC/ColIn dictionary and terminal period theorem identify the algebraic chain pairing with its complex chain pairing, the coefficient-level statement used in `ChainTieT` after the original coordinate identifications. They do not on their own establish

\[
\Theta_{\mu_0}(j_R e_V y)
 =\lambda e_R(\iota_{\mu_0}c_Fy)
\]

for a **single** map \(e_R\) whose translated automorphic evaluation is onto the actual retained row space and has the original common norm ratio. This is the concrete `RowTieT`/`EvalTieT` interface. The normalized finite dictionary identifies the left-hand side on the chain's point-polynomial spaces; the actual Poincare construction fixes the right-hand row functions and norms. Agreement of their representation labels does not prove equality of these two maps.

In addition, `MIid` explicitly asks for the anchored theta/Poincare bilinear identity for the same \(e_R\), all words and all row tuples. The finite-projector argument does not provide that see-saw identity. The currently written relation-transport theorem proves the algebra once common LawsX, the actual bottom relation, and a nonzero Poincare anchor are supplied; it does not construct all of those inputs.

## Source route found, with its actual prerequisites

There is an exact upstream supplier route for the evaluation part, so the obstruction should not be described as an unsupported claim that no supplier exists. `GoodRowsCompareByLevelMatchingEvaluation.evalTieT_of_levelMatch` constructs the evaluation isomorphism and norm ratio using:

1. the actual discrete-series model comparison and its original lowest vector;
2. the real/finite group and host identifications;
3. a finite placement that conjugates the **actual** level subgroup and character;
4. the original finite reduction action and coefficient pins (`RowLevelMatchAt`);
5. the ordinary discrete-series classification and square-integrable evaluation argument.

Its proof uses exactly the finite-projector identity reconstructed in the addendum. A further source theorem, `RowLevelMatchAtOfLevelConjugation.rowLevelMatchAt_of_conjLevel`, constructs the pins from the designated residue-place identifications, equality of embedded idempotent coefficients, level conjugation, and the original integral frame. `ThetaLevelConjugateCharacter` transports that result through the actual bundle data. Those are precise possible next suppliers. This audit does **not** claim to have proved all their hypotheses for the current original TC/ColIn and W08 constructions in ordinary mathematics; that would require a separate joined-row realization proof.

`JoinSubspaceRealDataExists` then constructs the joined map using actual primitive-row characterisation, the original lattice norm tie, the evaluation tie and an almost-everywhere formula for the same row map. In particular the latter is not replaced by an arbitrarily chosen isometry of two spaces with equal dimension. This source route confirms the specific remaining map and normalizer recorded above.

## Immutable source ledger

All paths below are under `lean/src/` in `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. They are source checks and ordinary proof attribution, not a Lean replay.

| Path | Git blob | Checked range / use |
|---|---|---|
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RowLevelMatch.lean` | `b43045df7be0e370cccf36fb860b37ddc3296672` | 18–46 actual placement, reduction action and coefficient matching |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/GoodOpStarTranslatedEvalEqGoodProjector.lean` | `d85da30bd97fb221bcafd07bdf3bccd50d001e8a` | 33–102 reduction fibres and representative independence; 103–160 fibre-volume cancellation and coefficient conjugation |
| `Formalism/LocalToGlobal/IndefiniteReal/EvalTieTOne.lean` | `173c694961fdded47f0c2c97df39ddc895e097e7` | 18–34 exact evaluation isomorphism, norm ratio and anti-linear row map |
| `Development/AbelianVarietyTheory/Proofs/TwistedOperators/GoodRowsCompareByLevelMatchingEvaluation.lean` | `86d556f401e42817d999fe960cdc48b2439329ee` | 38–90 precise evaluation supplier, finite projector use, onto and injective steps |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/JoinSI.lean` | `39f4f465e1c2b7b4a4c85b8369ef25e260023aa3` | 53–70 ChainTieT/RowTieT/ColNormT/PairTieT; 112–194 unitary transport and exact scalar; 229–260 literal Poincare pairing in spOf |
| `Formalism/LocalToGlobal/IndefiniteReal/IsometricPeriodsOfHypotheses.lean` | `24aed492b6b14485f38e0c72d6eb476be843f126` | 84–115 MIDat, MIid and SEEIso |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/JoinSubspaceRealDataExists.lean` | `8a457467e44223f68244252e8f8474cd0523a7db` | 24–85 joined-map construction and literal row-evaluation hypotheses |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaLevelConjugateCharacter.lean` | `4460fd2df6ebd15b72be15be9199c80d9b9805bb` | 49–86 invariance under the source's scale update and transport through original twisting data |

The current positive result is the finite-projector lemma and the explicit scalar-bearing reduction. No common FamAllQ/PtRows realization, anchored MIid, or actual family positive-trace bound is asserted as completed by this addendum.
