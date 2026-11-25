# W08 off-diagonal zero-Gram and retained trace comparison

[Proof](../paper/shared/flag-retained-zero-gram-traces.tex).
The zero-Gram normal form works for unequal negative norms T,T',
with common-tail ratio satisfying c conjugate(c)=T'/T.
Its common positive rank-k complement supplies a compact U(k)
acting on both quotient types. On the original real stabilizer
quotient the orbital integral intertwines these types.
Distinct types give zero, including every distinct-word pair
in the concrete DataNW regime.

Combining with the established diagonal result gives a bound
for the whole nonidentity zero-Gram error on the retained
period columns. If R0 is retained source dimension, d_i the
original full column dimensions, r_i the retained ranks,
s_i the chosen map weights, c the prescribed normalization,
the charge to the sum of normalized positive traces is
\[
c^{-1}\exp(-kf\log(k)/2)\sum_i s_i^2\sqrt{r_i d_i}.
\]
The inequality charges the signed error once in trace norm.
It keeps the exact target leakage and the trace of the
remaining Gram with the actual retained dimensions. There is
no hidden discarded-target contribution. The arithmetic
theta-chain identification, uniform nonzero-Gram estimates,
and the complete positive trace penalty remain open.

Pinned source jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de:
Development/AbelianVarietyTheory/Definitions/LatticeFrames/
VanishingGramTermsBoundParams.lean lines 49--67 (DataNW distinct
types and concrete regime); Formalism/LocalToGlobal/
SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/
KppOffCOfSteps.lean (7ddf12d27c05a060679b37e64cfc5c2136c82ff1),
lines 1--end, original relevance and zero-Gram off-diagonal
consumer. The argument uses the already proved actual
period identity and diagonal zero-Gram bound; it does not
claim the unrestricted source predicate with weaker displayed
hypotheses. The new trace lemma applies to prescribed scales
and arbitrary orthogonal cuts, and is independent of the
arithmetic realization of those cuts.
