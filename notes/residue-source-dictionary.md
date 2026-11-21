# One local compatibility theorem for the residue branch

Checkpoint: 21 November 2026. Source pin:
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
This note refines [the earlier source-interface checkpoint](source-residue-interface.md).
Exact hashes and inspected ranges are in
[`residue-source-dictionary.json`](../certificates/residue-source-dictionary.json).
It is a conventional mathematical reduction and bounded source comparison,
not a Lean build or an independent verification of the whole formal proof.

## The contract in the complete proof plan

The local residue branch should be represented by **one compatibility theorem**,
followed by positivity under its terminal spectral hypotheses. Its conclusion
is an exact sesquilinear identity, stronger than positivity alone:

\[
 \beta(\mathcal R_w F,H)
   =C_r^{-1}\langle\mathcal R_w^{\mathrm{rad}}\Phi_F,\Phi_H\rangle,
 \qquad C_r>0.
\]

The place, rank, compact representations and Haar measures are fixed before
choosing the constant. The **same constant works for every finite word**.
The initial domain, spectral signs and separation conditions are needed for
the later positivity assertion, not for this purely polynomial compatibility
identity when all its scalar denominators are nonzero.

This contract is one input to the larger theta/norm construction. It does not
provide global orbital energy, arithmetic nonvanishing or divisibility, or
bounds uniform in growing ranks.

## Why the five source interfaces compress to one argument

Let \(\mathcal C\) be a common coefficient class preserved by the entries of
the contracted group matrix and their finite ordered compositions. The rapidly
decreasing class with a fixed positive Gram cutoff in recovered section 95 is
such a class, by `cm-group-preservation`. Let \(J\) be the gauged Jacquet
restriction, acting componentwise on any finite auxiliary coefficient space.
Suppose

\[
 JQ_{ab}(Y)=Q^{\mathrm{rad}}_{ab}(Y)J,
 \qquad
 \langle JF,JH\rangle=C_r\beta(F,H).
\]

Here \(C_r>0\) depends only on the fixed measures and place data. The first
identity holds on \(\mathcal C\), with all iterated expressions in their
common smooth domain; the second pairing is absolutely defined there.

Every finite matrix polynomial \(P\) in the contracted entries then satisfies
\(JP=P^{\mathrm{rad}}J\). Indeed the assertion holds for one entry and
constant auxiliary matrices, passes to sums, and passes to an ordered product
by composition. No two noncommuting factors are exchanged. Entrywise insertion
at a fresh auxiliary factor and transposition of that factor commute with the
componentwise map \(J\), so the statement includes both signed residue steps.

Apply the pairing identity to \(PF,H\), which belong to the same coefficient
class. It gives

\[
 C_r\beta(PF,H)
 =\langle J(PF),JH\rangle
 =\langle P^{\mathrm{rad}}JF,JH\rangle.
\]

Taking \(P=\mathcal R_w\) proves the claimed identity for every defined word,
with the original constant \(C_r^{-1}\). The proof does not choose a new scalar
for each word. This is now manuscript corollary `ji-word-pairing`.

The needed mathematical inputs already appear as `cm-chain-restriction`,
`cm-group-preservation`, `ji-polynomial-intertwining`, and `jf-radial-pairing`.
The current argument merely uses them simultaneously on one invariant class.
The explicit finite-decay extension remains available for each fixed polynomial
degree through `ji-finite-decay-positivity`.

## Source endpoint and exact scope

`StatementJC.RadialModuleForm` (lines 90–106) requires the exact identity above,
with its positive constant quantified before the word. `RadialModuleFormOfParts`
(108–109) splits its proof into five named interfaces:

1. positive radial pairing normalization;
2. action of every group word after radial restriction;
3. Jacquet transforms lying in the required smooth radial class;
4. commutation of Jacquet transformation with the word;
5. preservation of the coefficient class by the word.

The preceding naturality proof combines these obligations through the common
coefficient class. The source's assembled theorem is at lines 3203–3205 of
`HermitianCurvatureProofs/LevelFormSesquilinearFiniteClass.lean`; reading that
assembly is not an independent verification of all its dependencies.

## Exact definition dictionary

The following comparison is complete for the local words, their radial action
and their pairing on the smooth rapidly decreasing coefficient class. It does
not identify every global form or every finite differentiability class in the
source. Source names belong in this technical note; the manuscript uses ordinary
mathematical language throughout.

| Source definition and inspected lines | Mathematical identification |
| --- | --- |
| `StatementC` 15; `StatementD` 193–194 | A letter has a sign and a real parameter. `positionted` assigns its original list index as a fresh auxiliary factor. |
| `StatementD` 164, 176–189; `StatementWd` 89–102 | Operators act rightmost first; both recursions process the list tail before its head. The chronological manuscript word is the reversed source list. |
| `StatementWd` 34–55 | Insertion is by matrix units. The two rational matrices are the permutation and contraction matrices, with denominator exactly \(z-1\). |
| `StatementQ` 889–918, 967–1013 | The first component of the paired operator algebra is the actual operator. Its projection preserves sums, products and complex scalar multiplication. The recorded second component supplies the formal adjoint. |
| `StatementWR` 19–41; `StatementT` 9–11 | The coordinate operators are \(p=c\partial_c\), \(\bar p=\bar c\partial_{\bar c}\), and multiplication by \(c,c^{-1},\bar c,\bar c^{-1}\). Thus the plus transfer is \(T(Y)\), and the real-parameter minus transfer is \(W(Y)\). |
| `CompositeFormulaLevelZero` 47–64, 103–109 | The initial radial matrix is the signed terminal matrix conjugated by the ordered coordinate-transfer product. `RRi` applies the same residue recursion, and `act` uses its first operator component. |
| `StatementMA` 308; `StatementQ` 269–287, 391–393; `StatementBF` 67–73 | The gauge is \(\gamma_r(c)=\prod_a|c_a|^{2(r-a)+k}\); the open-cell representative is exactly the manuscript's \(b(c,m)\). |
| `CompositeFormulaLevelZero` 68–82; `StatementB` 91–96, 165–180 | At level zero the form is the finite auxiliary sum paired with terminal Haar measure and outer density \(\prod_a|c_a|^{-2}\,dc_a\), linear in its first argument. |
| `StatementFr` 219–222; `CompositeFormulaLevelZero` 116–118; `StatementI` 13–19 | Original real parameters separated by more than two, with the common cut and margin two, satisfy the source's spectral admissibility hypotheses. |

### Order, insertion and partial transpose

Let the source list be \([\ell_0,\ldots,\ell_{h-1}]\). The source definition
of a nonempty word applies its tail first, so chronological step \(j\),
for \(1\le j\le h\), is source letter \(\ell_{h-j}\). Identify the
manuscript factor \(j\) with source factor \(h-j\). This merely permutes
the finite tensor factors and preserves the sum of their pairings. It does
not commute any operator factors.

Write \(A(Y)\) for the current main matrix and \(R\) for the residue.
At a fresh factor \(a\), the exact updates are

\[
\begin{array}{lll}
 +\text{ at }\lambda:
 &A_+(Y)=A(Y)\dfrac{(Y-\lambda)I-\Pi_a}{Y-\lambda-1},
 &R_+=R\,\operatorname{ins}_a A(\lambda),\\[6pt]
 -\text{ at }\lambda:
 &A_-(Y)=\dfrac{(\lambda-Y)I-\Omega_a}{\lambda-Y-1}A(Y),
 &R_-=R\,\operatorname{ins}_a A(\lambda)^t.
\end{array}
\]

These are `re-plus-module` and `re-minus-module`, and hence the recurrence
`mx-residue-recursion`. The transpose acts on the two-by-two main index that
is inserted at the fresh factor; it does not reverse arbitrary products of
old, noncommuting coefficient entries. The scalar determinant updates are

\[
 q_+(Y)=q(Y)\frac{Y-\lambda+1}{Y-\lambda},\qquad
 q_-(Y)=q(Y)\frac{\lambda-Y}{\lambda-Y-1}.
\]

The source transfer recursion (`StatementWd` 119–137) is also tail first:
its head transfer multiplies the tail transfer on the left. After the above
reindexing it is exactly \(V_h=U_h\cdots U_1\). This is the order used in
the mixed congruence and the integrated rank descent.

For the paired operator algebra, projection to the first component sends
the coordinate transfer to

\[
 T(Y)=\begin{pmatrix}Y+p&-c\\c^{-1}&0\end{pmatrix}.
\]

The first component of its entrywise star, at real \(Y\), is

\[
 W(Y)=\begin{pmatrix}Y-\bar p&-\bar c\\\bar c^{-1}&0\end{pmatrix}.
\]

The sign in the upper left entry follows from
`IsActualLevel` pairing \(p\) with \(-\bar p\). The terminal matrix is
paired with its conjugate-parameter transpose. Consequently the first
component of the source conjugation in `QQi` is the manuscript's ordered
formal-adjoint conjugation of the signed terminal contracted matrix.
Entrywise intertwining and induction now identify `D.RRop` with the actual
action of `P5.RRi` on gauged Jacquet transforms.

### Gauge, open cell and normalization

Source `Mdim(k,r,a)` is \(M_a=2(r-a)+k+1\). Its `resG` multiplies by
\(\prod_a|c_a|^{M_a-1}=\gamma_r(c)\), exactly the manuscript gauge.
For each hyperbolic pair, source `bigCell(c,m)` sends
\(e_a\) to \(c_af_a\) and \(f_a\) to \(\bar c_a^{-1}e_a\), and
acts by \(m\) on the middle space. This is precisely the definition in
section 93. Equivalently it is `wCell(c)` times the embedded middle matrix;
there is no additional Weyl factor in the actual representative.

At level zero, `P5.form` integrates all outer coordinates and the terminal
group. Source `IsHaarOn` requires the terminal measure to be nonzero, finite
on compact sets and invariant under both translations. The source allows
an arbitrary compatible Haar normalization. Its Hilbert--Schmidt pairing is
linear first, as in the manuscript. The identity

\[
 \gamma_r(c)^2\prod_a|c_a|^{-2}
       =\prod_a|c_a|^{2(M_a-2)}
\]

matches the outer density in `StatementBF.bcWeight` (146–151). The terminal
factor \((|\zeta|^2-TT')^{k-1}\), the section representative and the
actual Jacquet transforms in `betaBig` (157–159) are the quotient data in
sections 93–95. Their arbitrary Haar scaling is precisely the retained
positive constant in `jf-radial-pairing`.

Thus the source constant `Cst` in `RadialModuleForm` is \(C_r^{-1}\),
with the measures fixed before the word. It is not silently set to one.
The source's radial functions vanish outside the open radial domain and
are smooth locally on it (`StatementQ` 922–932); the dictionary makes no
assertion of smoothness across the excluded coordinate or Gram boundaries.

The formal source uses total division, so it even assigns values to words
whose displayed rational denominators vanish. The human residue formulas
are stated where their denominators are nonzero. The polynomial naturality
identity itself holds for arbitrary scalar coefficients, so it also survives
the source's zero-inverse convention if that convention is explicitly adopted.
None of the positivity arguments uses such singular words.

## The source cut gives a shorter positivity hypothesis

The source requires separation of the **original** insertion parameters,
\(|\lambda_i-\lambda_j|>2\), in `WordOK`. This does not imply the shifted
separation used in `ji-fused-positivity`: a plus parameter zero and a minus
parameter \(5/2\) have original distance \(5/2\), but shifted distance
\(3/2\). The earlier theorem remains correct; a separate corollary covers
the source hypothesis without strengthening it.

No new long sign calculation is necessary. Recovered lemma
`rp-parameter-signs` already proves, under interlacing and the common cut
with margin two,

\[
 (-1)^{k-l}p_\rho(\lambda+\delta)>0\quad(-1\le\delta\le1),
 \qquad q(\lambda)>0,\quad q(\lambda-1)>0.
\]

The dictionary `StatementM` 108–135, 225 identifies the source polynomials,
interlacing data and sign with these expressions. The range \(1\le l\le k\)
is also explicit in the source actual-positivity endpoint
(`CompositeFormulaLevelZero` 377–390). Original-parameter
separation excludes every difference \(-2,-1,0,1,2\), so `re-word-domain`
gives recursive admissibility for either sign. The existing
`rp-recursive-positive` and `re-density` then prove terminal positivity.
The mixed congruence and the rank descent require nonzero denominators and
fresh factors, and impose no additional shifted separation.

This gives the new corollary `ji-unshifted-positivity`: both the compact-input
and the stated smooth finite-decay positivity conclusions hold under the
source's original parameter separation and common cut. The extension has
the same finite derivative and decay indices as before. The source list
`positionted(w)` supplies freshness automatically. At every reduced rank the
spectral sign remains \((-1)^{k-l}\), since `parLev` changes only the rank.

Both short manuscript corollaries received an independent review on
21 November 2026. That review checked the fixed normalization quantifier,
preservation of the coefficient class, original versus shifted separation,
and the fact that the congruence and rank descent need no stronger separation.

## Verification boundary and next use

**Proved and checked:** one word-independent compatibility identity; the
local source's finite word, coordinate operator, gauge and measure dictionary;
and compact/smooth finite-decay local positivity with its original cut and
separation hypotheses. The source comparison is by bounded reads of pinned,
hash-verified definitions; it is not a fresh Lean kernel check.

**Not established here:** equality with every other global source form,
an extension from smooth functions to all source classes having only finitely
many derivatives, global orbital-energy estimates, arithmetic nonvanishing
or divisibility, or quantitative bounds uniform in growing ranks and words.
The source's `NiceCoef` class is smooth with every finite weighted derivative
bound (`StatementJC` 20–23), so this finite differentiability boundary does
not obstruct the compatibility contract inspected here.

The full proof program can therefore use one local residue-compatibility
contract, with its cut-positivity corollary, as an input to the larger
theta/norm construction. The global tasks remain explicit separate obligations.
