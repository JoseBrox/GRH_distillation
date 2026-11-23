# The actual unitary-to-complex-matrix density transfer

## Classification and downstream interface

**Closed local supplier, independently reviewed:** `PhiZero` for
the original compact coefficients and every relevant head, and hence
`DensC` after the already proved big-cell pointwise vanishing and compact
complex `KloostDens`. This does not yet claim `HeadTop`, the full local
kernel bound, W06/W08, or a new proof-map completion.

The statement retains the actual unitary groups, both negative middle
vectors, their lengths T,T', all block heads, the prescribed compact
representation factors and Haar measures, and the two positive Haar
constants. No compact Haar measure is silently made a probability.
The original additive character is cStd=-2i and betaU=2i; the `PhiTop`
coordinates use planar Lebesgue, not the self-dual normalization used
in the intermediate compact-germ calculation.

## Actual construction

The section of the reduced-matrix map is defined globally on

`G(Z)=|det Z|²−TT'|det top_r(Z)|²>0`.

With kappa=adj(Z)e_last, the rank-one projection Q=kappa kappa*/||kappa||²
annihilates the Gram defect in the sense QRQ=0. The matrix
K=(I-Q)R(I-Q)/2+(I-Q)RQ solves K+K*=R and QK=0. This yields exactly the
source frame columns without dividing by an internal leading minor.
Explicit indefinite Gram--Schmidt completes them to an isometry. The
two cofactor normalizations are sqrt(G/T)/|det Z| and
sqrt(G/T')/|det Z|, both positive. The remaining positive complement is
fixed pointwise, giving the original third D-frame condition.

The paired flag Gram determinant is (-1)^(r+1)G. Its signature is
(r+1,r+1), leaving a positive complement of dimension k-1. This proves
properness of simultaneous N0(z)×N0(z') integration on compact positive
Gram subsets. Differentiation under a common compact support gives a
smooth fibre average. The original epsilon bound forces its support
away from G=0 and hence from det=0, making extension by zero smooth.

Compact ambiguities are removed using all three D-frame conditions.
The first two force the compact factors to fix the positive cofactor
directions; the third identifies their actions on the remaining
positive complement. Their factors therefore cancel exactly. This is
stronger than a bare orbit-isometry or multiplicity-one argument and
is required for the actual vector-valued period normalization.

The N-to-upper-unipotent Haar disintegration has positive constants
cL,cR, retained as Phi_F=cL*cR times the fibre average. The quotient
root decomposition has unit real Jacobian, and the original normalized
cut cancels the original stabilizer measure exactly. Thus every head
has the prescribed `PhiTop` integral of the same compact coefficient.

## Quantifiers and scope

- The proof covers r=0, k=1 and heads with vanishing internal minors.
- The finite diagnostic computations do not replace the unbounded-rank
  algebraic proof or the properness argument in the shared TeX.
- Local properness constants can depend on all place data and the
  compact support. Their only downstream use is an exact zero
  conclusion, so they consume no uniform norm or exponent budget.
- This eliminates the unitary/matrix density transfer. The remaining
  terminal step is an actual compact top lift for the original word
  operator, followed by the already established differential identity
  and density. No almost-everywhere substitute is made at the rational
  sampling points.
