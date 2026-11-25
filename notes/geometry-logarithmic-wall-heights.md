# W10: logarithmic tangent slopes and the reference wall argument

## New proved supplier

[The proof](../paper/shared/geometry-logarithmic-wall-heights.tex) establishes
the absolute bound

    mu_max(Lie A) <= C log(2 + dim A + max(0, -deg_n Lie A))

for principally polarized abelian varieties with the stable integral
tangent lattice and polarization metric. The proof takes a high
theta level m^2 with m = 6 ceil(H), uses integral isometric theta
translations, and filters a standard coefficient lattice by integral
ordinary directional jets. The determinant-degree inequality is applied
to the entire quotient of that coefficient lattice. Each successive
one-dimensional jet is nonzero up to order m^2/3 by very ampleness of
L^3. The matrix lemma bounds the mean log sup norm of the original
rank-one theta section; translation leaves that norm unchanged.
The choice of m absorbs the entire theta pushforward height and
coefficient-rank term. The absolute Siegel lemma then gives the
maximum slope, not just a bound on integral vectors over one field.

This supplies the abelian slope theorem in the source SlopeBoundSt
normalization, up to its fixed metric constant. The uniform toric
and abelian quotient metric comparison is recorded separately, as
is the original orthogonal flag/determinant identification needed
for FibreInput and the reference lower point-height bound.

Primary references checked:
- F. Pazuki, Theta height and Faltings height, Bull. SMF 140 (2012),
  19–49, Theorem 3.4, Propositions 2.5 and 5.1.
  https://www.numdam.org/item/10.24033/bsmf.2623.pdf
- E. Gaudron and G. Rémond, Théorème des périodes et degrés minimaux
  d'isogénies, Comment. Math. Helv. 89 (2014), 343–403, Prop. 3.6.
  https://lmbp.uca.fr/~gaudron/art11.pdf
- Gaudron–Rémond, Minima, pentes et algèbre tensorielle,
  Israel J. Math. 195 (2013), 565–591, Thm. 1.1.
  https://lmbp.uca.fr/~gaudron/art10.pdf
- Zhang, Positive line bundles on arithmetic varieties,
  JAMS 8 (1995), 187–221, (5.2).

## Wall limit: a shorter proof with explicit remaining inputs

The fixed-tower argument proves I1 by telescoping on the common
models at new primes, using nef mixed intersections and the
original sandwiches; it needs no source coefficient theorem.
It replaces I2's uniform rate by exact equality of the smoothing
variation on the isometrically linked models, followed by
qualitative convergence of mixed intersections on one fixed
reference model. The logarithmic tangent estimate and the original
prefix bounds produce the all-point lower bound after adding the
small auxiliary ample perturbation. The dense upper bound uses
bounded ample-height points on the fixed reference variety.
The successive-minima theorem, the O(theta) flag degree at the
perturbed wall, and fixed-dimensional interpolation then give the
required qualitative wall limit, under the listed actual model
hypotheses. No varying-dimension uniform constant is required for
this step.

This is not an unconditional closure of the actual wall limit.
The separate verification of the uniform reference fibre metric
identifications, original prefix estimates, semipositive smoothing,
proportionality and fixed-reference mixed-intersection convergence
must be retained; the determinant-only height proof does not
supply all of these automatically.

Source chain (all at jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de):
Development/AutomorphicSpectrum/Proofs/GeometryProofs/
SlopeBoundOfLargeDegreeLine.lean, HodgeCptLieMetricBound.lean,
RootTowerUniformHeightBound.lean, TowerI5OfReference.lean,
RefLowerOfFibreInput.lean; Definitions/GlobalGeometry/
SlopeBoundSt.lean, ArchBetween.lean; Proofs/MetricProofs/
WeightedFlagDegreeLowerBound.lean; Proofs/DivisibilityProofs/
TowerWeilTheorem.lean, RealTowerI1.lean and RealTowerConvI2.lean.

## Divisor certificate

The normalized-blow-up certificate now has a direct analytic
upper-order test: on a transverse arc at a general point of a
base divisor, the full Bergman function has leading logarithm
-2 times the divisor multiplicity times log(1/|t|).
This yields (LW8) under sublogarithmic metric growth.
Combined with the original proposed theta lower valuation and
the explicit sufficient factor-six monodromy comparison, it would
give precisely the divisor certificate. Neither that comparison
nor the actual global lower-valuation theta section is asserted
proved here. In particular a nonvanishing product over one
generic fibre alone would not certify the divisor.

Relevant source: HodgeBundleWeights/ExistsNonzeroSectionWeightBound.lean
and ThirdPlaceSeries/ExistsSectionOrderBoundHilbertSamuel.lean,
ExistsCuspValueLePhiOfHilbertSamuel.lean, and
ValuationMultiplicityOfConsecutiveRun.lean, under
Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/.
The original construction uses the weight 8N hodgeWt and its cube,
together with the normalized odd-level toric theta constants and
the key/parallel factors. The source upper order is phi/2500;
the certificate has slack, as (LW8) makes explicit.

## Other requested obligations

W06: FamAllQ still needs the actual AllTrue and OntoAll
realizations with the same analytic normalization; this turn
does not construct them. W08: the distinct-word near-one bound
still needs the global block-level Gram estimates and the actual
lattice/model ties of GLOB.partG and ArithmeticGlobalModelCondition.
The source stThmA_of_frames in Formalism/SharpRestriction/
CuspSpanNormBounds/BlockEstimateWords.lean identifies their
use in the global row recursion. A pointwise polynomial-cost
amplitude bound or an abstract positive trace identity does not
establish the necessary near-one coefficient.

## Verification status

New written slope proof, reference wall proof under explicit
hypotheses, and finite arc order lemma. Classical theorem
statements checked against the primary papers. No independent
review, full source replay, or manuscript PDF rebuild in this
checkpoint. No whole W-node is closed.
