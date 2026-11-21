# One averaged construction at each scale

## Checkpoint and result

This note refines work packages W02/W11. It identifies a strictly weaker sufficient arithmetic target than the source's pointwise construction package. The source facts are byte-verified against `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`; the certificate records only bounded inspected excerpts. The new inequalities below are ordinary mathematical deductions, not newly kernel-checked Lean declarations. The missing arithmetic/geometric construction is not being declared proved.

Three simplifications are already established at the displayed interface:

1. It suffices to bound the **average arithmetic discrepancy over the translation subgroup**. The source final comparison assumes a bound for every translation separately and then averages it.
2. The source already has a mean-slope theorem that needs only the **averages of two loss terms**, rather than the two pointwise bounds imposed by `CoreAtH`.
3. Finite multiplicative factors can remain explicit. The final extra exponent loss in `core_gm` merely absorbs a factor depending on the fixed character level; the varying-family analytic criterion allows that factor to depend on accuracy.

A complete clause ledger and a more flexible finite-error version follow below as this checkpoint is extended. The first averaged comparison is already proved here.

## 1. The averaged comparison

Retain one of the source's arithmetic hosts, its finite abelian group A, translation subgroup B, selected set T, and nonempty thick set S contained in B. Write

\[
 n_T=|T|>0,\qquad m\geq1,\qquad b>0,\qquad d=|S|/|A|>0.
\]

For each u in B, define the arithmetic discrepancy

\[
 E_u=\sum_{t\in T}\sum_{i=1}^{m}
       \bigl(\mathcal A(a_t,t,w_{u,i})-
                    \operatorname{Re}\mathcal M(a_t,w_{u,i})\bigr),
 \qquad \overline E=\frac1{|B|}\sum_{u\in B}E_u.
\]

The functions are the explicit prime-power sum and its main term in `FirstPrimeNeSecondPrime.lean:75–91`; their full conventional formulas are recorded below. All terms use the same host, Frobenius and inertia data, weights, logarithmic derivatives and top labels. The sets used in the arithmetic and geometric sides cannot be chosen independently.

Assume the source's size/thick-thin conditions, character-projection conditions and costs in `SplitInertia.SizesA`, `ThinScales`, `CostWindows` and `CharsA`, at sufficiently large x for their elementary character-translation estimates. Let H(x) be the resulting positive selected-character sum, and let

\[
 R(x)=\sum_{\psi\in B^\perp\setminus K}|G_\psi(x)|
\]

be the auxiliary-character remainder. Then

\[
 \boxed{\quad
 H(x)\le R(x)+4x^{1/2+\varepsilon}
       +\frac{2\overline E}{n_T m b d}
       +\frac4{dx}.
 \quad}                                                    \tag{1}
\]

In particular the numerator needs only an averaged upper bound; negative discrepancies may cancel positive discrepancies. One does not need an upper bound for every E_u separately.

### Proof

The local thick-part comparison in `ChCore.lean:75–152`, combined with the exact arithmetic balance in `ChBalance.lean:200–202`, gives for every u

\[
 \sum_{t\in T}\sum_{i=1}^{m}\operatorname{Re}\Theta_{u,t}(a_t/b)
       \le E_u+2n_Tmb/x.
\]

The source applies a pointwise upper bound on E_u before summing (`ChCore.lean:302–325`). Instead, sum this displayed inequality first and divide by the positive cardinality of B. Character orthogonality gives exactly

\[
 \frac1{|B|}\sum_{u\in B}\sum_{t,i}
       \operatorname{Re}\Theta_{u,t}(a_t/b)
 =\frac{mbd}{2}
       \sum_{t\in T}\operatorname{Re}
          \sum_{\psi\in B^\perp}\psi((1,0),t)G_\psi(a_t/b).
\]

This is `sum_Th` together with `ChCore.lean:326–333`. The character-translation estimate in lines 419–439 bounds the last t-sum below by

\[
 n_T\bigl(H(x)-R(x)-4x^{1/2+\varepsilon}\bigr).
\]

Divide the resulting inequality by n_T m b d/2. Every denominator is positive, giving (1). No estimate on an individual E_u has been used. ∎

## 2. Consequences for the source numerical envelope

If the source's auxiliary-character hypotheses hold for a fixed level of order o, then `SigALe.lean:38–60` gives R(x)≤4o x^(1/2+ε). The original construction is one supplier of an upper bound on the normalized averaged discrepancy in (1).

The last four lines of `CoreGm.lean` absorb the finite factor 1+4o into x^ε. Before that absorption, the same proof already gives

\[
 H(x)\le(1+4o)x^{1/2+(e_D+e_L+6)\varepsilon}.
\]

Thus the final +ε loss and its extra threshold are dispensable when multiplicative constants may depend on the accuracy stage. This does not improve a nonvanishing geometric exponent loss; it simply avoids demanding an unnecessary exponent absorption.

More substantially, (1) imposes no intrinsic square-root restriction on m. The familiar m≈√x choice comes from the particular construction's error terms x/m and m, not from Fourier averaging itself. A different construction may be accepted if its normalized averaged discrepancy and its other explicit errors fit a vanishing total-loss budget. If m or any rank grows with x, that budget must hold for all x in the required whole windows at a fixed accuracy; a theorem for each fixed m separately is insufficient.

## 3. The existing mean-slope route

`ChainSlopeWindows/LevelOfCongruence.lean:199–235` proves the source mean bound from averaged loss assumptions

\[
 \operatorname{avg}_u(\mathcal A_u-\Gamma_u)\le L,
 \qquad \operatorname{avg}_u I_u\le L.
\]

The pointwise package instead asks both inequalities for every u (`QuotientSlopeBoundsWith.lean:34–35`). Therefore an averaged construction can use the weaker mean theorem directly. Reindex its data by B, or prove that the chosen indexing has the required uniform pushforward to B. A surjection alone does not preserve uniform averages.

Each word set W(u) must be finite and nonempty, and its rank weights d_w must be strictly positive. These requirements justify the weighted means, maxima and rank-normalised slope expressions. An empty space cannot be used to make the construction clauses vacuous.

Within a word set, the divisibility inequality enters `s_lower5` only through its positive rank-weighted average (`LevelOfCongruence.lean:50–66`). The same proof permits that averaged divisibility inequality, provided it concerns the same h, log T and quotient maps. The upper/maximal-slope and variation estimates used separately to control the maximum-minus-mean term still need their own proofs; they are not erased by averaging.

## Remaining work in this checkpoint

The full clause ledger and the finite projection/thin-transfer error criterion are being recorded next. The global construction must still supply the averaged arithmetic discrepancy through compatible integral maps, slopes, norms and covolumes. None of the existing local positivity statements alone supplies that growing-family estimate.
