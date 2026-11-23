# Actual short integral theta generators

Classification: **closed quantitative supplier, independently reviewed**.
This is the original minimal-level short integral theta spanning conclusion,
not completion of W06 or W10. It removes the uniform archimedean norm and
short harmonic coefficient obligations for the actual raw theta family.

The focused proof is `paper/shared/theta-spanning-continuation-short.tex`.
The common arithmetic cover, canonical harmonic connection, actual raw
theta existence, finite Schwartz system, exact SW/heat comparison, raw
spanning and actual `intZ` integrality are prior proved inputs. No member
of the `PublishedHodgeBundleTheorems` placeholder package is used.

## Frontier discharged

For every original `CovGmin.Hyp` datum, put
`f=[E:Q]/2`, `r=p+q`, `X=f*r*Lb`, `d=DF`, and
`kappa=d+(n/2)*f*r`. The actual original cusp lattice contains a finite
coefficient-field spanning family whose global and every component
Petersson norm, at every field embedding, are at most
`exp(30000*X^2*kappa)`.

The construction retains `fieldSz(K)<=o<=391*X^2`, growing `n`, and
arbitrary Hermitian lattice indices. It does not assert that the family
generates the integral module. Its members are actual raw sections
multiplied by `Z*s_Lambda`, with the SAME common
`Z=M^(frn+d)*abs(disc(E))^d` and the SAME determinant-ideal scalar used
by the actual all-place integrality theorem.

## New proof ingredients

1. A direct elementary transference proof, applied to the actual trace
   dual including the different, gives `2fn` rationally independent
   vectors of every unimodular Hermitian lattice with simultaneous
   embedding norm at most `B0=2*f^(3/2)*n^2*rd(E)`. No free integral
   basis is assumed.
2. Integral grids of these vectors, an adjugate orthogonal projector,
   leading minors, and finite interpolation give the actual harmonic
   space an integral spanning family with
   `log(l1_sigma(P))<=140*r*Lstar*d`. The harmonic orbit-span assertion
   is justified by the Fock adjoint relation and the strict Casimir
   dominance argument, not just cited under a theorem name.
3. The actual half-maximum point has period minimum `>=exp(-40Lb)`.
   The proof uses original principal-level isotropic transvections,
   periodic Schwarz, and the exact trace-dual ideal, rather than a
   uniform fundamental domain. The original relation is
   `Mstar*k0=2*M*sqrt(dHost)`; field size controls this quantity.
4. Gaussian submean, packing, finite isogeny-sum orthogonality, and
   ordinary Cauchy derivatives give the actual normalized raw bound
   `m_Lambda^(r/2)*polyNorm(P)*exp(9000*X^2*kappa)`.
   The original Lie factor `(pi*2*xiR)^(-d/2)` cancels the same
   archimedean factor from the derivative directions. No derivative
   factorial or Fourier cardinality has been discarded.
5. Minkowski in the inverse original reflex index ideal gives
   `|sigma(s_Lambda)|*m_Lambda^(r/2)<=exp(fieldSz(K))`
   simultaneously at every embedding. Its ideal norm is exactly
   `m_Lambda^(r*[K:Q]/2)`. This cancels the analytic index and satisfies
   the actual determinant-ideal inclusion required by `intZ`.

The constants add as `20000+9000+391+67=29458<30000`.
The actual component and global measures have mass at most one, as
verified in `EvenDomainWeightBound`36–84; no Tamagawa volume bound is
inserted at this point. Finite dimensionality permits choosing a finite
subset without enlarging any norm.

## Decisive source interfaces

All source references are at `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
Complete authenticated paths and bounded ranges are in the certificate.

- `CuspFormEvaluations.EmbeddingHermSelf`56–124: actual trace-dual minimum.
- `HeightTheory.Transference`35–175 and
  `CuspFormEvaluations.TraceHermNondegenerate`57–139,299–358: the weak
  Euclidean transference and its exact Hermitian normalization.
- `ExistsEqMulProdMinors`126–245,250–369;
  `RowHighestLeSpanColWordComplex`172–242: Casimir dominance,
  simultaneous highest-vector uniqueness, Fock orthogonal-complement
  orbit spanning. Stable range is `p+q<=n`.
- `SpanGridPerpVecEqOrbitSpanOfLe`167–226,276–340:
  distinct embeddings and conjugates, exact adjugate grid interpolation.
- `ExistsShortHarmonicFamilyFewColumnsLinear`38–112 and
  `ExistsShortHarmonicFamilyUnimodular`96–193: integral grid belongs
  to the original symmetric lattice via the actual letter dictionary.
- `FirstMinAtHalfMax`19–103,111–211 and
  `ExistsSelfDualDataTransvectionPrincipalLevel`60–119:
  principal level, original AA, xi0, different, exact period constant.
- `MaxBoundPf`12–257: periodic Schwarz at the half-supremum frame.
- `NormalisedThetaValueBound`18–97,101–187 and
  `JetTranslateProjectedVacuumLe`150–288: same isogeny cosets,
  vacuum normalization and actual ordinary derivative directions.
- `NormRawThetaSeriesIndexBoundLeSqrt`54–116;
  `NormPhiHatIndPhi`208–315: literal raw prefactor and index,
  modulus-one Fourier weights, half-maximum and Lie normalization.
- `ExistsSmallScalarReflexIdealSelfDualLattice`29–152:
  exact inverse reflex ideal and simultaneous embedding bound.
- `ExistsGoodCoverAtMinimalLevel`20–57: the precise consumer; its
  first proof line discards the nominal published-theorem package.

## Exact next consumer and what remains

`HodgeBundleWeights.ShortSpanCompositionClosed`24–154 shifts these
minimal-level theta weights to arbitrary allowed dominant weights. It
uses a genuine key-unit twist and a genuine integral flat-line twist.
The latter requires actual `FlatExistsAt(c1)` with `|c1|<=9*r*Lb` and
unramified points of this same cover. Those inputs are not silently
supplied by the present theorem; their concrete construction is the
next active attack.

There is an exact useful shortcut once that shift is available.
`ShortSpanCompositionClosed` already gives an integral **K-spanning**
set and the original component Petersson bound. The `h0/hsh` inputs
in `ExistsDegreeParametersBound`33–76 need only a finite K-spanning
family. Choosing a finite subset bypasses the integral-module
generator conversion in `ShortGeneratorNormComparison`34–101, its
rank/Tamagawa input, and its `[K:Q]^4*rk*rd(K)` factor. This does not
bypass the field-size terms used in constructing the original short
sections.

## Verification scope

Run `python3 scripts/theta-spanning-continuation-short.py --offline`.
It authenticates the pinned source bytes and bounded excerpts, checks
the adjugate orthogonality identity in exact examples, the transference
recurrence, and the retained exponent bookkeeping. The general proofs
are in the TeX; diagnostics do not prove them. No Lean build is claimed.
