# The terminal theta period and its analytic comparison

## Result and classification

**Closed supplier obligations, not closure of W06.** The full proofs are
in `paper/shared/theta-period-continuation.tex`.

1. The terminal period of the actual TC/ColIn chain equals the embedding
   of its algebraic class sum, with scalar one. The comparison preserves
   every intermediate automorphism mass, root phase, the actual conjugate
   word-prime element, and the original integral branching scalar. It
   also holds on the original twisted source. It introduces no new
   denominator and does not remove the original branching or pairing
   denominators.
2. The actual normalized Poincare pairing unfolds to the original Bessel
   integral with factor `vol(K2)/(beta_u*sqrt(c0X_u))`. Here `beta_u>0`
   is the uniquely specified conversion between the original Bessel
   Haar measure and the product of the original real stabilizer measure
   with the finite stabilizer measure normalized to give the intersection
   `S_f intersect x_u*K2*x_u^-1` mass one. No Haar factor is absorbed into
   an unspecified complex scalar. Its positivity does not require a
   nonzero theta map or period.

The second comparison retains the radial integral. It is not an equality
of the integral theta chain with `P_u/sqrt(c0X_u)`.

## Exact finite arithmetic step

The point/kernel realization already proves the one-step polynomial
dictionary. It commutes with the original class-weighted sums, so an
induction identifies the entire chain. The final two coupled steps are
the same class sums written with different representatives; the
orbit--stabilizer identity retains their weights. Evaluation commutes
with the actual lowering coefficient extraction and inverse Gram
projection. The terminal column and row carry inverse characters,
which cancel in their bilinear polynomial pairing.

This is the source's `ptilCol_eq` and its actual application
`KernelsOverOfFamily.period_true`. It supplies the finite-period part
of `PeriodRelationsTrueColumnsAtTuple`, without making an analytic
isometry or a claim about a uniform coefficient-field degree.

## What the source actually proves at the next boundary

The source's `SBes.PerLaw` is a Poincare-to-Bessel pairing law.
`BottomRelationOfPin.botRel_two` transports two-term linear relations
between period expressions. `JointStarProductNonvanishing.anchor_word`
then uses an actual nonzero Poincare pairing to prove that the
proportionality factors are nonzero. It does not infer nonvanishing
from representation type or from an existential scalar that could be
zero. The later identity retains coefficients depending on the row
tuple, and these are not identified with `sqrt(c0X)`.

Consequently the previously phrased literal normalized-map equality is
a stronger target than these individual source interfaces. This note
does not weaken W06's downstream requirement: any use of the source's
relation comparison instead must prove that it transfers the required
norm and integral estimates, with its actual row factors and retained
restrictions. Kernel agreement alone has no quantitative content.

**Next direct target:** reconstruct the actual see-saw relation for the
same chain and actual row realization, then apply the nonzero-pairing
argument only after the final normalized source-deficit bound supplies
the required nonzero Poincare family. Track the row factors in the
arithmetic map-height correction. Do not set those factors to one or
assume that they are algebraic units.

## Verification

`scripts/theta-period-continuation.py --offline` authenticates bounded
source ranges and the exact proof files. Its finite exact models check
the class weights, inverse phases, nontrivial branching scalar, and
the finite stabilizer/level measure factor by independent sums.
They are diagnostics of the formulas, not proofs of the arithmetic
construction. No Lean build is claimed.

The geometric point-height proof was separately reviewed in
`certificates/geometry-point-continuation-theta-review.json`.
