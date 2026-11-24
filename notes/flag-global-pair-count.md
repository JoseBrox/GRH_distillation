# Global fixed-label term-pair count

**Closed supplier obligation (W08): the original PairsP estimate.**

[Proof](../paper/shared/flag-global-pair-count.tex).
The actual full row system parametrizes unimodular quotients with
primitive last vector of norm `-T`. The fixed isotropic ideals and
split row decompositions give the correspondence in both directions.
For a fixed definite complement with cyclic discriminant module
O_E/T, primitive unimodular gluings are graphs of anti-isometries of
the two discriminant modules. Since T splits completely, there are
exactly (T-1)^f gluings. Orbit-stabilizer with reciprocal automorphism
orders gives the exact weighted row/genus comparison; the gluing
factor cancels against the original total row mass. This supplies
RowsOrbC and RowsMeanC with no genus-count loss.

The previously proved PerRowC and embedded-isometry genus estimate
now give the weighted fixed-label global sum. The original integral
leading ideals imply that all nonzero normalized minor norms are
positive integers; the original archimedean height factor gives
Delta <= A S^2, Db <= (A S^2)^r. With A=b^(Ca m^2 f), the full
finite double sum of pairBd times the two datBd factors is bounded
by the product of the original k2e factors. The powers (x x')^(k/2)
cancel the two inverse powers in datBd. The exact size assumptions
give Cp=16, Ch=300000 Ca, C'_0=1, Cl_0=42 Ca, where
Ca=max(1,2(CH+1),CT). These choices have the original order of
quantifiers.

This proves PairsP, not AmpP, TypeP, the final zero-Gram sum or the
full W08 node. Next verify the original amplitude at every term,
combine the fixed-label count with the distinct-label sum, and
complete generic returns, finite columns and the final traces.

## Pinned source interfaces
Pinned source: jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.
Paths below are under lean/src/Development/AbelianVarietyTheory/.

| Path | Git blob | Relevant interface |
| --- | --- | --- |
| Definitions/SemilocalFrames/RowsMeanC.lean | 33e9a6334a36fbac72ce59c379358fbdb14c0002 | original row orbit and genus means |
| Definitions/SemilocalFrames/PerRowC.lean | c406932d46d85320d0a2cfd75fd776219312cf96 | PairsAt, PairsP, PerRowC |
| Definitions/SemilocalFrames/PairBdNonneg.lean | d6176424a868b3c8c0a787e252e93ad2831763fe | exact pairBd |
| Definitions/SemilocalFrames/AdaptSelf.lean | 97311ee488582c1c5ecf2f6cba4e4a79ffdf2eee | exact datBd |
| Proofs/FlagMeasures/ExistsRowOfUnimodularLatticePrimitiveVector.lean | 5f96a3c75c001af15e5a4d7c901800330e29b226 | original row existence |
| Proofs/FlagMeasures/RowsEqOfStabilizerConjugateLattices.lean | a915cae9d82889bb5682bc221ba3fbead4b1c0cf | lines 332–401, row uniqueness |
| Proofs/FlagMeasures/OrbSumFibreEquiv.lean | 12d621f52711b115ec4afe746ce216ee0a5c5cfd | exact gluing orbit sum |
| Proofs/FlagMeasures/RowsGenusWeightedSumComparison.lean | 611a88706d8cd228711c9a7c36752f24630d5fd3 | lines 36–86, RowsOrbC |
| Proofs/FlagMeasures/RowsMeanBoundOfGenusMean.lean | cff0557eda4d2ab51b548699172bd9b5488b6297 | lines 144–168, RowsMeanC |
| Proofs/FlagMeasures/RelevantTermNormsGeOneAndBounded.lean | 431e7225a8ba5fea7151e6b2b7afc54a0a0e8d7f | norm bounds |
| Proofs/FlagMeasures/ParameterSizeConstraints.lean | 543568643502512966db0d19ecb9846a71ea2e8f | original size constraints |
| Proofs/FlagMeasures/SumPairBdMulDatBdLe.lean | a20699682444e8f75fc33b93453580275d7d53af | lines 307–394, exact finite sum |
| Proofs/FlagMeasures/TermPairCountBoundOfSiegelMassRatios.lean | e0515a28287cd69e35a0399f2334d9e12e840935 | lines 70–164, PairsP consumer |

The normalized product formula uses BlockEnds.lean
(8509b64296431d5ab15f64ecdf09c5188a82b832) in
Formalism/SharpRestriction/CuspSpanNormBounds/.
Independent written reconstruction from the original row and arithmetic
hypotheses, with bounded source readings. No full Lean replay or
manuscript build was performed.
