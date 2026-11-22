# The next arithmetic section input: a uniform theta denominator

## Exact next target

The determinant and geometric-filtration proofs now estimate the full
section lattice from the original geometric data and short integral
families. The next selected input is a **uniform clearing integer for
the actual theta generators**. This is a genuine finite-place statement;
an arbitrary full lattice has no comparable uniform short spanning family.

The pinned source is
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The precise declaration is `CovInt.integral_smul_thLa`, in
`Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsBoundedIntegerGoodCoverThetaSeriesIntegral`,
lines 31–118. Under its original good-cover, weight, level and connection
data, it produces one integer N_A, independent of the individual theta
generator, such that

\[
 N_A>0,\qquad \log N_A\le C(frL)^2\kappa_\theta,
 \qquad N_A s\theta\in M_{\mathrm{cusp}}.
\]

Here f and r are the original field/rank parameters, L is the size
parameter called `Lb`, and kappa_theta is the actual `sizeK(Dw,a,n)`.
The lattice is the original integral cusp lattice `AllWt.latW`, with its
valuation conditions at every arithmetic place. The supplied section
theta is the same normalized lattice theta series, with the actual
level indicator, harmonic polynomial, self-dual lattice, connection,
coefficient field and weight. It is not an arbitrary section.

The scalar s must satisfy the original fractional-ideal condition

\[
 (s)\prod_\tau I_\tau(\Lambda_{\rm norm})^{m_\tau}
 \subseteq
 \prod_\tau I_\tau(\Lambda)^{m_\tau}.
\]

The exact source names are `idealAt c La.Ln tau` and `idealAt c La.La tau`.
This condition and both determinant ideals must remain in the proof.
The original lattice must be unimodular and trivial at the stated bad
integer and at the level; its level compatibility and harmonic-polynomial
integrality are also retained.

The construction is explicit: N_A=Z^2, where Z is the original positive
integer `CovInt.intZ`. The logarithmic bound for Z is supplied separately
by `log_shortThetaSeriesDenominatorBound_le`; doubling it gives the bound
for N_A. The research target is the valuation proof, including the correct
local normalizations and all primes, rather than this final doubling.

## The three local branches

| Place | Original bounded source branch | Required conclusion |
|---|---:|---|
| A rational prime outside the level | 103–118 | The coprime-level clearing theorem supplies integrality after the determinant-ideal scalar; the second Z is integral and preserves it. |
| A rational prime dividing the level, with no prime square dividing the level below this place | 68–79, 95–102 | The determinant-ideal condition first gives an integral scalar locally; `smul_intZ_nonneg_away` gives the normalized theta valuation, then the extra Z preserves it. |
| A prime square dividing the level | 81–94 | `smul_intZ_sq_nonneg_of_sq_dvd` gives integrality with the full Z squared, retaining the local class-indicator and normalized theta factors. |

The intermediate factor `betaH` is not discarded: the source passes to
betaH inverse times theta, applies its local theorem, and restores betaH
with the clearing factor. Any shorter proof must reproduce that exact
normalization. It must also account for coefficient-field ramification
and the finite valuations in `valSet`, not just generic-fibre integrality.

## Why this is the useful next input

`HodgeBundleWeights.ExistsGoodCoverAtMinimalLevel`, lines 20–57, combines
three distinct suppliers: `CovGmin.span_thFam` (theta spanning),
`RawThetaSup.homN_smul_raw_le` (the raw theta norm), and the clearing
integer just isolated. Its proof explicitly ignores the surrounding
`PublishedHodgeBundleTheorems` argument at line 21. Thus there is an
actual source proof of this supplier; its imported package name is not
being treated as an independently verified theorem.

`ShortSpanCompositionClosed`, lines 24–31 and 68–112, next transports
the theta family by the original key-unit and integral flat-line twists.
`ShortGeneratorNormComparison`, lines 23–37, turns that spanning set into
short original cusp generators. The level-zero and level-D/T wrappers
then give the precise bounds used by the determinant proof. Clearing
the theta denominator would therefore advance a common input to the
short sections and the original frame, without reopening signed energy
or metric variation.

The raw theta spanning and norm estimates remain separate. So do the
actual arithmetic cover, toroidal model, canonical identification,
nef-and-big weight bundles and Bergman bound. The present target card
proves none of those inputs.

## Other retained data, now located

The actual component consumer is
`HodgeBundleWeights.ExistsDegreeParametersBound.hilbertSamuel_estimate_at_level`,
lines 33–76. It invokes:

- `ExistsWeightHodgeBundleGenerated`, lines 22–53, for the original
  toroidal flag, birational modification, canonical bundle identification
  and the exact global-section sandwich.
- `HermitianGeometricHypothesisHolds`, lines 19–47, for positivity and
  multiplication, preserving the supplied Bergman bound and short families.
- `GeneratedWeightsMulStableAndBounded`, lines 16–77, for multiplication
  of the original integral cusp forms and the Petersson estimate with
  factor square-root beta.
- `HeightBirationalImageEqTupleHeight`, lines 21–26, for transport of
  the same normalized image height. `IsImageHeightUnique`, lines 403–472,
  proves frame invariance using integral substitutions in both directions,
  the unchanged Hermitian norm, scalar invariance and Chow-form uniqueness.
  This is distinct from the already treated analytic metric comparison.

The source's convenient `PublishedHodgeBundleTheorems` structure bundles
many results (ToroidalCompactification, Grothendieck–Messing, Nadel
vanishing, principalization, and other arithmetic theorems). Auditing one
field does not establish the rest or construct the model. Likewise an
upstream source theorem that supplies the clearing integer is evidence
for its exact target, not a substitute for the new readable proof.

## Reuse to check before further work

Compare the proved [full type-prime jet estimate](theta-integral-frontier-type-prime-jets.md)
and [conjugate-prime divisibility](theta-integral-frontier-conjugate-gain.md)
with these exact theta series, level indicators, coefficient ideals,
normalizations and local places. Their shared words alone do not give
the required identification. In particular an all-order jet bound at
one type prime does not automatically supply the global cusp-lattice
valuation at all primes.

The accompanying certificate authenticates bounded source ranges. This
card is a next-target audit, not a newly proved supplier or a Lean build.
