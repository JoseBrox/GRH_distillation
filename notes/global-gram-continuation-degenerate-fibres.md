# The original degenerate flag fibre estimate

> **Later status (23 November 2026).** The previously missing [degenerate local orbital operator](global-gram-continuation-degenerate-operator.md) is now supplied. The “exact next consumer” paragraph below records the original checkpoint, not the current frontier. The [arithmetic zero-Gram sum](global-gram-continuation-degenerate-next.md), remaining global returns, and final traces are still open.

**Classification: closed obligation — the geometric fibre supplier.**
The proof is in
[global-gram-continuation-degenerate-fibres.tex](../paper/shared/global-gram-continuation-degenerate-fibres.tex).
It proves the literal original normal-form fibre estimate, including
arbitrary right translates and the original stabilizer measure. It does
not close the full diagonal zero-Gram bound or change a proof-map count.

## Exact result

Let `G=U(k+r,r+1)`, `1<=j<=r`, and `j+2<=k`. Retain the original
common normal form for `gamma=n1*g0*n2`, its block-antidiagonal
cross-pairing matrix, the common negative vectors, and the measure
`mu_R=(conj(n2^-1))_*(s d rho)`, where `d rho` is the original
polynomial-coordinate Lebesgue measure and `s>0`.

Let `Delta>=1` bound the reciprocals of every nonzero leading minor
of size at most `r`. Let `S,S'` be the original maxima of all flag
lengths and their inverses. Let `Y` be the original projected Gram
volume divided by the absolute value of the nonzero `j`th minor.
For a nonnegative measurable cutoff whose `mu_R` integral on every
left stabilizer fibre is at most one, every `g in G`, `R>=1`, `y>0`,
the `dn` integral over

```
S(ng), S'(gamma*ng) <= R,        y < Y(ng) <= 2y
```

is at most

```
(4r)^(4r^2) (R^(2r) Delta)^(8r^2)
    (pi e/(k-1-j))^(j(k-1-j)) (2y)^(2(k-1-j)) / s.
```

The locus `Y(ng)=0` has `dn` measure zero. The proof preserves the
actual form, flag vectors, Euclidean norm, central dimension, and
coordinate Haar measures; it does not replace them by abstract data.

## The argument that was missing

The common stabilizer and its section are explicit products of
upper unitriangular and two-step unipotent matrices. Their multiplication
gives a unique coordinate factorization with real Jacobian exactly one.
Conjugation by an upper unitriangular matrix also has real Jacobian one
on the skew Hermitian coordinate space; no unrecorded factor from its
diagonal imaginary coordinates appears.

For `M=R^(2r) Delta`, the first `l` moved flag vectors and `l-1`
matching original flag vectors give one triangular pairing determinant.
The exterior Cauchy–Schwarz inequality bounds it by `R^(2l)`.
Within each antidiagonal block the logarithm of a prefix product
interpolates between the two nonzero endpoint minors. This proves
the bound `M` for every pairing with a moved dual vector. Consequently
the section coordinates satisfy

```
|upper off-block entry| <= M,
||m^-1 B_a|| <= M,
|skew entry|, |imaginary diagonal entry| <= 2r M^2.
```

The actual positive projected Gram volume is exactly
`Gram(P*m^-1*B_1,...,P*m^-1*B_j)`, where `rank(P)>=k-1`.
The determinant of the first moved-flag change of coordinates cancels
the original denominator. Moreover `|det(m)|=1`, so the real central
Jacobian is one even for an unbounded middle isometry. The proved
Euclidean estimate (GV8) now applies with its exact dimension and
measure. Integrating the remaining coordinate discs and intervals
gives the displayed constant. Unipotent and compact invariance, with
an explicit flag Iwasawa argument, extend the calculation to every
right translate; the transported cutoff produces exactly `1/s`.

## Pinned source interfaces

Every module is at `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The JSON certificate records all full source hashes and authenticated
Git blob hashes. These are bounded source inspections and an independent
standard-mathematics proof, not a Lean build.

| Module suffix | Inspected interface or argument |
|---|---|
| `Definitions.SemilocalFrames.UpperOff` | 11–108: original matrices, polynomial measures, projector, Gram volume, minor bound and cutoff |
| `Definitions.SemilocalFrames.BlockAnti` | 11–15: exact block-antidiagonal condition |
| `Definitions.SemilocalFrames.IsNormalFormStabilizerMeasure` | 11–80: original common normal form, stabilizer scalar, fibre target and operator consumer constants |
| `Proofs.FlagMeasures.MovedDualVectorPairingBoundedMajorant` | 136–184, 271–373: exterior determinant and moved-dual pairing |
| `Proofs.FlagMeasures.SiegelHeightBoundSection` | 345–463: actual section coordinate bounds |
| `Proofs.FlagMeasures.FlagGramEqGramDetProjectionNormalForm` | 238–335, 380–410: actual central projection and Gram normalization |
| `Proofs.FlagMeasures.LintegralFlagUnipotentEqStabilizerTimesSection` | 327–381: exact original measure disintegration |
| `Proofs.FlagMeasures.CommonStabilizerSetEqRangeNormalForm` | 150–245: necessity of the original stabilizer coordinates; the new proof also gives the converse explicitly |
| `Proofs.FlagMeasures.FlagUnipotentGramNullAndFibreVolumeNormalForm` | 88–180: original normal-form supplier |
| `Proofs.FlagMeasures.FibreVolumeNormalFormStabiliser` | 79–174: arbitrary right translate and transported scalar |

The first ten suffixes have prefix `Development.AbelianVarietyTheory.`.
The flag lengths are also checked in
`Formalism.SharpRestriction.CuspSpanNormBounds.RelevantZeroGramTerms`,
lines 299–303. The sole pre-existing analytic input is the fully proved
Euclidean Gram-volume estimate (GV8), including its zero-set assertion.

## Verification and next decisive step

Run `python3 scripts/global-gram-continuation-degenerate-fibres-check.py`.
It checks all pinned source bytes against the atlas, exact symbolic
matrix multiplication and Haar-coordinate identities, the original
central Gram normalization in a nontrivial rational example, and the
uniform polynomial exponent accounting. The uniform geometric proof
is the TeX proof; the finite matrix diagnostics are not substitutes for it.

The exact next consumer is
`Proofs.FlagMeasures.AmplitudeDegenerateOperatorNormLeRealPlace`,
lines 165–259, with the already proved all-length tail and the recovered
dyadic summation. Its operator uses the original positive constant
`c_Phi`, the original seed unipotent factor `kappa`, and `s`; its bound
must retain `kappa/s`. A complete diagonal zero-Gram estimate still
requires that operator assembly, its allowed moment order, the actual
arithmetic leading-minor count, and the original global normalizations.
See [the exact next checkpoint](global-gram-continuation-degenerate-next.md).
