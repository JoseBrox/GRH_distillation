# The actual theta family: bounded `FamAllQ` / `LawsX` source audit

## Verdict and scope

There is a genuine source construction of `FamAllQ`; it is not correct to say that no supplier exists. Its premise is an actual `RealPack W` satisfying `AllTrue W`, together with `OntoAll` for the original recursion and the stated classical representation-theoretic inputs. The checked proof body constructs one central bottom datum, compatible rows and columns, the family laws, all five links, and the arithmetic ratio condition. It does not take `FamAllQ` or `LawsX` themselves as hypotheses.

This does **not** yet close the retained theta comparison in the present ordinary reconstruction. The construction still has to be instantiated with the same global models, Petersson metrics, actual row embeddings, and anchored all-word see-saw family as the retained `TC` / `ColIn` data. In particular, the finite class-space and period identities do not supply `AllTrue W`, the full cuspidal `OntoAll` property, or the final anchored scalar modulus. No new assumption should be hidden by replacing these inputs with the names of their source structures.

This report is a bounded source audit and an identification of exact conditional consequences. It is **not a Lean replay**, a proof of all imported classical theorems, or a reconstruction of the entire global theta theory. All source citations below refer to `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, under `lean/src/`.

## 1. The precise actual-family package

`FamAllQ W` asks for a **single** central finite-adelic element `z`, chosen before the word `u`. For every word it then asks for one family `f` and one bottom datum `d` satisfying

\[
d.\mathrm{Pin}(z),\qquad \mathrm{LawsX}(f),\qquad
\mathrm{LinkZero},\ \mathrm{LinkTail},\ \mathrm{LinkDown},\
\mathrm{LinkOnto},\ \mathrm{LinkComm},\ \mathrm{RatioQ}.
\]

The last condition includes nonvanishing of `cTop` and the original arithmetic `UnitRatio` relation between `(cTop/cBot)` at each tuple and at the reference tuple. It is a relative condition; it is not an assertion that the absolute analytic scale is one. [`FamAllQ.lean`, lines 19–30.]

The direct source theorem `famAllQ_of_allTrue` assumes `CuspRapidDecay`, `DiscreteSeriesCover`, `HarishChandraModules`, `StrongApproxSU`, `AllTrue W`, `1 ≤ B.R.rS`, and `OntoAll (I.rec7 l Z)`. Its body is explicit: it first chooses the common central bottom datum, then for every word chooses the true geometric family datum and consistent rows, constructs columns using the family invariance theorem, and assembles the laws and links. `LinkOnto` is obtained by applying the separately supplied `OntoAll` hypothesis. [`TrueGeometryFamilyRowData.lean`, lines 29–45.]

The exact `AllTrue` fields are

\[
\mathrm{PkHyp}(W),\quad \mathrm{TrueW}(W),\quad
\mathrm{TrueQ}(W),\quad \mathrm{TwStd}(W),\quad
\mathrm{LevTrue}(W),\quad \mathrm{Nonempty}(\mathrm{RealRec}(W.Q)).
\]

Here `LevTrue` identifies the actual type places with the original base-prime set and identifies `xiH` with the `TC` character at the actual tuple. These are substantive matching conditions on the realization, not an invitation to select unrelated isomorphic spaces. This audit has not constructed all six fields from the current finite `TC` / `ColIn` reconstruction. [`LevTrue.lean`, lines 81–90.]

## 2. What the common-row construction really provides

`exists_consistent_row_choices` invokes `rowOf_is` and `rowOf_same` on the original level, model and chain data. The factory `rowOf` uses the original step vectors and Weil data, the fixed Hermitian geometry and volumes in the geometric datum, and restrictions of the original `ioY` and terminal `ioXT` maps. Its correctness proof identifies those restrictions with the actual maps. It does not replace them with arbitrary isometries. [`ExistsConsistentRowChoices.lean`, lines 13–20; `NotLevGEmpty.lean`, lines 159–200.]

One qualification matters: `RowCh.Same` states equality, across tuples, of the three volume components `vS`, `vT`, `vU` for each BF and FB step. It does **not** itself state equality of all theta operators, a common retained-row embedding, or a Petersson norm identity. The latter properties have their own actual-model pins. [`NotBadPrimeBase.lean`, lines 196–211.]

The associated top-row reading convention also retains the original stabilizer cardinality explicitly:

\[
f(v)(hx)=|\operatorname{Stab}_2(c)|\,
\operatorname{period}\bigl(e_W^{-1}(\delta_c(jv))\bigr)(G).
\]

Removing this cardinality, or changing the norm on the class coordinates without the matching dictionary, would change the analytic scalar. [`NotBadPrimeBase.lean`, lines 225–228.]

## 3. The common finite coefficients and the content of `LawsX`

`LawsX` contains the common and tuple validity conditions, local finiteness, the real-place equality, the two valuation conditions, a kernel relation, a terminal-period relation, and continuity/automorphy with a common central character. In `PerX`, the finite coefficient `a` is chosen before the row tuple; this placement is essential for transporting linear relations. [`ValLastX.lean`, lines 205–221.]

The checked column construction obtains these fields from the same family. It gets local finiteness and valuation identities from its integral laws; obtains a common definite class-kernel datum `ClsPinD` from the actual top-row reading; and invokes that datum for the kernel, terminal-period and automorphy fields. Its `LawsX` assembly is explicit. [`TrueGeometryFamilyColumnData.lean`, lines 127–137.]

The finite-support kernel supplier explains why the coefficients are common. Starting from the common definite class data, it chooses the shared real test representation, writes the actual theta lifts as class sums, and applies the finite averaging-span statement to the single real test. The resulting finite set of real points and coefficients is then used for **every** tuple, ramified vector and reading variable. The proof keeps the original frame determinant factors in the coefficient array. This is a finite linear-algebra construction after the actual class-kernel identity has been supplied; it does not interchange a pointwise limiting approximation with a theta distribution. [`SeeSawKernelLiftCombinationOfDefiniteClassData.lean`, lines 14–51.]

The source still invokes genuine analytic suppliers for the local integral laws, top-row realization and class-kernel identity. Reading the assembly above verifies the dependency and the common-coefficient quantifiers. It does not independently discharge those analytic suppliers for the current moving retained family.

## 4. `LinkComm` has one common bottom similarity

The actual column constructor supplies the level-prime operators, kernel-back and tail-reading identities, exact local lift relation, chart-zero reading and chart-zero surjectivity to `type_data_unit_shift_relation`. [`TrueGeometryFamilyColumnData.lean`, lines 138–163.]

The checked parallel `ThirdPlaceSeries` proof gives the decisive mechanism explicitly. For each type-prime shift it chooses one bottom operator `S_eta` and its positive norm ratio. Chart-zero injectivity forces the local operator at **every** tuple to intertwine with this same `S_eta`. Iteration yields one bottom linear equivalence `A`, one positive similarity ratio, and the original nonzero factor `cS(n)` from finite cardinalities. The last equality combines kernel-chain commutation with this common iterate. It does not choose a different bottom equivalence independently for each tuple. [`LinkCommOfLaws.lean`, lines 31–69.]

The ratio part of the actual column construction separately uses the original phase and ideal-index identities. It does not adjoin arbitrary complex ratios to force the result. Even so, relative arithmetic control of `cTop/cBot` and existence of a positive bottom similarity do not determine the final absolute Petersson normalization. [`TrueGeometryFamilyColumnData.lean`, lines 164–199.]

## 5. `OntoAll` has an explicit but substantial supplier

`FamilyLinkOnto` constructs the reachability chain from the actual successive row maps and then applies `OntoAll` to produce the requested cuspidal preimage. Surjectivity of a finite retained projector is not used as a substitute. [`FamilyLinkOnto.lean`, lines 35–63.]

There is a direct source theorem for `OntoAll`. Its premises are Harish–Chandra finiteness, cusp rapid decay, discrete-series coverage, Harish–Chandra modules, Casselman–Wallach, unramified Howe correspondence, the unitary-pair Weil representation, the unitary Weil–Siegel formula and convergent Siegel–Weil formula, doubling, and unramified GL doubling. The body obtains the Hecke inner-product form from doubling and the upward theta Hecke parameter from the unramified correspondence, then applies the actual chain-surjectivity theorem. The parallel local-type-dictionary formulation uses the explicit `DoublingMethodLocalZetaIntegrals` premise. [`ThetaLiftOntoAll.lean`, lines 30–34; `OntoAllOfPrintsAndHecke.lean`, lines 24–29.]

Thus the precise remaining issue is not the absence of a named supplier. It is the ordinary verification and application of those analytic theorems, with their hypotheses and normalizations, to the same realized family. That work is not contained in the finite `TC` / `ColIn` calculation or in this bounded audit.

## 6. Joined scalar: what is now fixed, and what is still needed

The separately reviewed actual-row calculation in `retained-actual-row-evaluation.tex` gives reference scalar exactly `lambda = 1`, conditional on the original `Read`, `Seam`, `CxFacts` and `IotaRd` pins. With the original range and norm ties it also gives the actual evaluation isometry

\[
j=(c_{\rm ev}n_P)^{-1/2}E_t\,H_E.e\,e_E,
\]

using the original positive Haar ratio and row mass. This simplifies the earlier joined scalar to

\[
a_u=\epsilon(d.a_u)\,\kappa_u,
\qquad
B_u(x,y)=a_u\langle J_Vy,P_u I_u U_u x\rangle.
\]

It does **not** remove the anchored see-saw scalar `d.a_u` or the actual pairing-conversion factor `kappa_u`. Passing to the normalized literal period column `P_u/sqrt(c0X_u)` multiplies the scalar by `sqrt(c0X_u)`. Consequently the corresponding target Gram still carries

\[
|\epsilon(d.a_u)\kappa_u|^2\,c0X_u.
\]

The equality of this number to one, or an adequate uniform comparison with the prescribed trace scale, must be proved for the **same** family. Neither `RowCh.Same`, relative `RatioQ`, nor the reference scalar-one identity proves it. This is consistent with the retained-row agent's final report `retained-actual-row-final-audit.md`.

The checked `JointOfFamAllQ` continuation takes the supplied family laws, derives `MainX` by the see-saw transport theorem, and combines the links and served-prime condition to obtain the common equivalence, positive ratio and arithmetic scalars. It does not by itself provide the final anchored `MIid` or compute the above absolute modulus. The existing `notes/theta-relation-transport.md` records the downstream anchored algebra; that algebra remains conditional on the matching actual realization and anchor. [`JointOfFamAllQ.lean`, lines 21–29.]

## 7. Exact remaining interface for the retained application

The following is the bounded, concrete boundary to retain in the manuscript and status record:

1. Construct the original `RealPack W` on the current `TC` / `ColIn` family and establish its six `AllTrue` fields, including the actual character and level ties.
2. Supply the original global theta model, the reference reading/seam pins, the Petersson row range and norm ties, and the actual evaluation placement for that same `W`. The separate row reconstruction identifies the exact conditional maps and scalars; it does not invent these pins.
3. Apply the actual cuspidal `OntoAll` supplier with its classical hypotheses checked, so that `LinkOnto` is obtained on the required global row space.
4. Carry the same realization through the common finite-test `LawsX` identities and anchored all-word see-saw identity. Compute `epsilon(d.a_u) kappa_u` against the original `c0X_u` and prescribed trace scale. Do not reset a scalar separately on each row or replace the prescribed trace scale by the observed trace.

There is no new unconditional retained-column comparison or positive-trace closure in this audit. The exact finite comparisons and conditional row identities remain useful, but **W08 remains open** at this actual-family and scalar-budget interface.

## Source ledger

Each path below is relative to `lean/src/` at the immutable pin stated above. Line ranges identify bounded excerpts actually read; imported results beyond those excerpts are not claimed independently checked.

| Source | Git blob | Checked ranges |
|---|---|---|
| `Development/AbelianVarietyTheory/Definitions/LatticeFrames/FamAllQ.lean` | `9c1df5cc36db3e77454eae9856e6cee328ad0e8b` | 1–35 |
| `Development/AbelianVarietyTheory/Definitions/LatticeFrames/LevTrue.lean` | `f55aefabae4df901d4b8a507281580960f9ec4ea` | 78–96 |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/TrueGeometryFamilyRowData.lean` | `814416d33b9a115ef39751d87834b6b1d880ea99` | 29–47 |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ExistsConsistentRowChoices.lean` | `246656e2936b86d9d5e62236c0c8d11ce176bafe` | 1–21 |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/NotLevGEmpty.lean` | `26604a0b7e88d0368119e1345e8c8afac39c8358` | 150–245 |
| `Development/AbelianVarietyTheory/Definitions/LatticeFrames/NotBadPrimeBase.lean` | `3f728bfff04aa5295aa392194d03b8d4f8d11937` | 196–236 |
| `Development/AbelianVarietyTheory/Definitions/LatticeFrames/ValLastX.lean` | `242b8c628d536957e2bfb902e11ec23bf1d1cf6a` | 204–255 |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/TrueGeometryFamilyColumnData.lean` | `3a9fe55e91a0d6a73a839a77d10fe979f627b522` | 47–130; 129–199 |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawKernelLiftCombinationOfDefiniteClassData.lean` | `a8debf56e34bff947638e036b8292004afcd672a` | 14–51 |
| `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkCommOfLaws.lean` | `6931ac357b3f2376dfcd582dfc5e7826399b8dc1` | 29–70 |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/FamilyLinkOnto.lean` | `b82b5702a0a3ba7527f56c7f4bc24c3948ce4a46` | 35–63 |
| `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaLiftOntoAll.lean` | `cbd6b7075dda3b1bff9c37db29725d7b8f1c81b8` | 1–37 |
| `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/OntoAllOfPrintsAndHecke.lean` | `3f9c7008bedae079ebe6f24b7aae0d9f1c9cec70` | 1–31 |
| `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/JointOfFamAllQ.lean` | `44f4291ace78e4c83245a488b4086d89aa6b3e89` | 1–31 |

The `ThirdPlaceSeries` sources above are explicitly identified as the parallel formulation. The actual `FamAllQ` constructor and actual `LawsX` assembly were read in the AbelianVarietyTheory branch; this report does not silently identify unrelated structures from the two branches.
