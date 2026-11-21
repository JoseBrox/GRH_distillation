# The remaining source-to-residue interface

Checkpoint: 21 November 2026. This is a bounded comparison with pinned
source bytes, not a Lean build, kernel replay, or audit of the complete
dependency closure. No mismatch has been established. The exact source
word/form identification remains to be proved.

The new manuscript result `ji-fused-positivity` concerns the explicit
mixed-sign recursion of recovered section 89. Its source-facing boundary
is now a concrete identity of operators and forms, rather than another
general positivity argument.

## Pinned evidence

All three files are in `jsmorph/rh` at commit
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. They were searched first and then
read in bounded ranges with `scripts/source_excerpt.py`, using
`certificates/source-frontier-2026-11-21.json` and `--offline`. The tool
recomputes and checks each Git blob hash before printing an excerpt.

Paths below are relative to `lean/src/Formalism/HermitianCurvature/`.

| File | Git blob SHA-1 | SHA-256 |
| --- | --- | --- |
| `StatementJC.lean` | `30a61e319e5296392019a442628d194946f0212d` | `922ff4187ce58d5e6404c63bab097e1ae32e75c901a38917a258b18348d614af` |
| `StatementQ.lean` | `1e7035a15be9a61cbbe34f56091f376dcd464a07` | `11b2b51b9071900af15b1bfe99ce33e894ef5d8466011fe0908eecc689d180d7` |
| `HermitianCurvatureProofs/LevelFormSesquilinearFiniteClass.lean` | `381267d8cd896b2c373cba1e7029993941c559d1` | `110d0f80e58fa94ae16a0c1d22f11101ef890f23af7a47646159517165cddb38` |

The last file is abbreviated **LevelForm** below.

| Exact source range | What was checked |
| --- | --- |
| StatementJC 20–23 | `NiceCoef`: smoothness, every finite weighted derivative bound, and a positive Gram cutoff |
| StatementJC 25–47 | The full word-action identity `RadialModuleAct` |
| StatementJC 49–64 | The positive measure-normalization identity `RadialBetaPos` |
| StatementJC 66–109 | Jacquet compatibility, preservation of the coefficient class, `RadialModuleForm`, and its five-input interface |
| StatementQ 379–397 | Operator composition, the gauged restriction `resG`, and the nested transfer sandwich |
| LevelForm 121–131 | The actual proof of `radial_module_form_of_parts` |
| LevelForm 1581–1596 | The ordered transfer prefix and its equality with `P5.tprod` |
| LevelForm 1639–1705 | The dressed matrix, full word action, and `radial_module_action` |
| LevelForm 2595–2604 | The reciprocal positive normalization used in `radial_beta_pos` |
| LevelForm 3203–3205 | The assembled theorem `radial_module_form` |
| LevelForm 3280–3296 | The downstream use of the form identity to transfer radial positivity |

## The precise endpoint

`StatementJC.RadialModuleForm` does not merely assert positivity. With
the actual place/level data and `P5.IsData`, it supplies one real constant
\(C_{\mathrm{st}}>0\), chosen **before** the word \(w\), such that

\[
\texttt{D.formLev}(w;F,F')
=C_{\mathrm{st}}\,
\texttt{P5.form}\bigl(
 \texttt{P5.act}(\texttt{P5.RRi}(L,st,0,\texttt{D.positionted}\(w\)))\Phi,
 \Phi'\bigr).
\]

The omitted fixed arguments are exactly those of StatementJC 90–106.
The vectors \(\Phi,\Phi'\) are the restricted Jacquet transforms of
\(F,F'\). This is an identity of sesquilinear forms, with the first
argument acted on, for every coefficient family satisfying `NiceCoef`.
The identity itself quantifies over all words; the later positivity use
separately supplies the admissibility condition `hOK` (LevelForm 3292).

The source's short assembly proof uses precisely `RadialBetaPos`,
`RadialModuleAct`, `JFInFF`, `BesselModule`, and `ModuleNice`
(StatementJC 108–109; LevelForm 121–131). The endpoint is assembled from
named proofs at LevelForm 3203–3205. Reading these statements and assembly
lines does not independently verify all five proofs.

## Normalization and ordering actually checked

**The scalar normalization has the expected reciprocal direction.**
LevelForm 2597–2600 first obtains

\[
\texttt{P5.form}(\Phi,\Phi')
   = C_1\sum_a\beta(F_a,F'_a),\qquad C_1>0,
\]

then chooses \(C_{\mathrm{st}}=C_1^{-1}\). This is consistent with
`jf-radial-pairing` in section 95, whose convention is
\(\langle\Phi_F,\Phi_H\rangle=C_r\beta(F,H)\).
After identifying the measures and restricted transforms, the source
level form must therefore be \(C_r^{-1}\) times the radial form. The
read proves the direction and word-independence of the source constant;
it does not yet identify its numerical value with our \(C_r^{-1}\).
Setting both constants to one without an explicit common Haar
normalization would be unjustified.

**The ordinary operator product acts rightmost first.** StatementQ 379
defines the product as \(M_{ac}(N_{cb}f)\). Moreover, LevelForm 1581–1584
defines its transfer prefix by \(T_{n+1}=T^{(n)}T_n\), so the newest
transfer is multiplied on the left. This agrees with the ordering
convention in the manuscript's fixed-chain congruence. LevelForm
1642–1644 explicitly has the sandwich
\(s\,T(\bar Y)^*X.QQ(Y)T(Y)\).

These checks do **not** identify the independent residue-word ordering:
the translation `D.positionted`, and the definitions `D.RRop` and
`P5.RRi`, have not been unfolded in the verified frontier. The source
word-action proof reduces to `module_of_words` at LevelForm 1682–1691.
Thus a rightmost-first operator convention alone is insufficient to
settle chronological insertion, auxiliary-factor placement or transpose.

**The radial gauge is visible, but its whole dictionary is not yet
checked.** StatementQ 391–393 multiplies by
\(\prod_{a<i}|c_a|^{\texttt{Mdim}(k,r,a)-1}\) before evaluating on the
open cell. The manuscript uses
\(\prod_a|c_a|^{2(r-a)+k}\). The remaining dictionary must verify the
dimension identity, the open-cell coordinates and the Haar density
together. The defining declaration of `Mdim` is not in the three source
files inspected here.

## The smallest remaining matching lemma

For fixed actual place and level data, choose the explicit dictionary
between a source word and the manuscript's signed, chronologically
indexed insertions. Prove that its source residue acts as the manuscript
residue on the common positive-cutoff Jacquet domain, including the empty
word. An induction should verify exactly:

\[
\begin{array}{lll}
\text{plus:}&t_+(Y)=t(Y)R_\Pi(Y-a),
 &\mathcal R_+=\mathcal R\,\operatorname{ins}t(a),\\
\text{minus:}&t_-(Y)=R_\Omega(b-Y)t(Y),
 &\mathcal R_-=\mathcal R\,\operatorname{ins}t(b)^t.
\end{array}
\]

Here the transpose acts only on the fresh two-dimensional index. The
spectral shifts, initial sign, scalar denominators \(z-1\), old-factor
ordering and permitted parameter domain must all agree. These are the
explicit recursions in `re-plus-module`, `re-minus-module` and
`mx-residue-recursion`; no factor may be freely commuted to manufacture
a match.

Next identify the source form and the manuscript pairing using the same
gauged restriction and Haar measure. The positive, word-independent
normalization above then transfers `ji-fused-positivity` to that source
presentation. This would close the local source-form interface. It would
not supply growing-chain energy estimates, automorphic congruence bounds,
or arithmetic nonvanishing/divisibility.

The next bounded source work is therefore to locate and pin the
definitions of `D.positionted`, `D.RRop`, `P5.RRi`, `P5.form`, and
`Mdim`, and only the word-recursion lemmas needed for the displayed
induction. No broad rereading of the full formal proof is required.
