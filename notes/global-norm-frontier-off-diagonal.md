# Actual inverse-parameter kernel supplier

Classification: **closed local obligation**, independently reviewed.
The whole W08/W06 obligations remain open.

## Frontier and result

The missing compact off-diagonal supplier is the source's
`KernelArgumentHypothesisScalar`, not a new abstract Cauchy inequality.
The shared theorem proves it for every original admissible word on
the established grids, with the exact point and word normalization.
It also proves the actual `LiftDegAll` and `DegLift` identities.

The decisive new information is a prescribed-operator calculation.
After the original right Jacquet average, the bit-one operator at
head `h || (s,t)` reduces to its bit-zero operator at level `j-s`,
multiplied by `(-1)^(s-1)/t` (plus) or its conjugate (minus).
The plus calculation peels ordered last columns.  The minus
calculation peels ordered last rows, lowering the spectral parameter
at every step.  The character values on both paired chains are
exactly one with the original `cStd=-2i` normalization.

This gives the mixed degree `2j-s` and leading scalar
`(-1)^(s-1)(1/t-1/t')`.  Its degree reduction is **after Jacquet
transform**; it is not a pointwise polynomial-degree claim for
the original slice function.  The exact Jacquet Gram identity
and old-operator intertwining justify replacing only its form
class.  The proof makes this distinction explicit.

The final scale is
`exp(10/49) A1 (28N/I)^(2j-s)`, with `N=20(r+1)` and the same
original spectral `A1`.  Separate finite maxima at the two
heads give precisely the source's two existential extensions.
No terminal `j=r+1` case is silently supplied: the source consumer
only requires `j<=r`.  The rank-zero case is vacuous.  Cases
`s=1`, `j=s`, `K=0`, `t=t'`, and old words occupying an arbitrary
pattern of long blocks are covered.

## Verification scope

The checker authenticates the bounded original source interfaces.
Its exact universal-enveloping-algebra diagnostics check both
ordered Laplace formulas and their spectral shifts in small ranks;
it separately checks the anti-diagonal determinant ratio, normalized
two-head Cauchy factors, and mixed leading coefficient with nonreal
parameters.  The written inductions, not finite experiments,
establish all-rank and all-word assertions.  No Lean build or
numerical proof of the analytic integral identities is claimed.

## Remaining decisive steps

1. Pass the compact suppliers to the actual finite-decay eigenfunctions
   with the original growing differential-order budget.
2. Prove the source block-growth comparison, with its exact `covol/pi`,
   reciprocal shift and limsup over punctured complex neighborhoods.
3. Supply the original uniformly controlled arithmetic top lift and
   identify the global theta-map Gram operators with all rational returns.

The first two now have precise compact input identities.  They are
not consequences of the unchanged abstract frame inequality.
