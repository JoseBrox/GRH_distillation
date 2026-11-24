# Reference Haar volume and the original common stabilizer

**Status:** proved, in the prescribed normalized local coordinates. See
[shared proof](../paper/shared/flag-reference-haar.tex).

For (s=r-j), (v=\operatorname{rd}(E)/2ge1), (f=[F:\mathbb Q]), the exact
reference group's covolume is the product of (v^f) for each allowed
block-upper and skew off-diagonal entry, (v^{f(k+1)}) per middle column,
and the imaginary lattice volumes in the skew diagonal. This proves
the source's two-sided estimate (v^{ksf}/L_v\le\mathrm{covol}\le v^{ksf}L_v),
(L_v=(8v)^{2(r+1)^2f}). Multiplication by the relative stabilizer
index gives CovTC, with no replacement of the arithmetic weight.
The full unipotent reference case gives CovNC, since
(\kappa^f v^{krf}=2^{r^2f}).

The integral middle lifts use a trace-one algebraic integer, not
division by 2 in the lattice. The Haar product uses a triangular
fundamental set, not a false rectangular integrality assertion.
The normal form is obtained from the original return by changing
both graded bases; its inverse orientation has the same measure
scalar. No identification of the orbital coordinate measure with the
earlier Hilbert--Schmidt Lie-algebra measure is made.

## Pinned source audit

Source revision: jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.
Paths below are relative to lean/src/Development/AbelianVarietyTheory/.

| File | Git blob | Checked interface |
|---|---|---|
| Definitions/SemilocalFrames/UpperOff.lean | 0fb307538c33149e131daf7baf32b57ffd76e742 | Upper, middle and skew coordinates, lebN |
| Definitions/SemilocalFrames/IsNormalFormStabilizerMeasure.lean | 38e73df348426a4aa38bb12147b76a7d89154c8e | IsNormal0, lebR0, measure transport |
| Definitions/SemilocalFrames/IsFundOne.lean | 50136efd4e2ef9b564326866e3ced273c3bc2d9b | IsFrameOf, original real coordinates |
| Proofs/FlagMeasures/AdaptedNormalFormGivesRealNormalForm.lean | c926be460646c14d062204fd355e11a6ca2ab4d4 | FrameC, lines 165–519 |
| Proofs/FlagMeasures/CovolumeReferenceLatticeStabiliserBounds.lean | c60e2a0e5cb796c041abfb02371d4a729c5b7787 | covol_ref, lines 99–293 |
| Proofs/FlagMeasures/HermitianStabiliserCovolumeLe.lean | 093fd522467f821a66dd1750b8d0408b0be005a6 | CovTC relative index calculation |
| Proofs/FlagMeasures/IntegralUnipotentCovolumeFiniteBounded.lean | 06a109a573ccf81ad3c903b1b3a5af3f8ca6861e | CovNC, lines 42–120 |

This is a mathematical proof against the bounded source interfaces,
not a Lean replay. The complete global amplitude and zero-Gram
summation still require their normalization and finite-level interfaces.
