# The actual upper cusp norm and integral frame

## Result and classification

**Closed supplier obligations:** the original global upper Bergman,
supremum and rank bounds; the corresponding multiplication norm; and
the prescribed finite frame generating the entire integral cusp lattice.
These do not close W10. The thin lower bound, point heights and final
arithmetic section remainder remain open.

The proofs are
`paper/shared/geometry-bergman-continuation-upper.tex` and
`paper/shared/geometry-cusp-frame-continuation.tex`.
They apply to the actual constructed cover, coefficient embeddings,
Hermitian lattices and component probability measures. Their arithmetic
volume calculation uses the classical theorem that the Tamagawa number
of a special unitary group is one. The source's larger published-theorem
package is not imported wholesale.

## Exact upper bound

Put f=[E+:Q], r=the original rank, Delta=abs(disc E),
D=fr(r-1)/2. For total model-weight spread at most w>=1, the constants are

```
epsilon = min(1, pi/(2 M sqrt(d_H) (f w+2) log 2)),
rho     = 1/(200 r^3 (w+f)),
A       = (1+2(2fr)^2 Delta/epsilon)^(2 f r^2),
V       = 2 h_E M^(2f(r^2+1)) rd(E)^(f(r^2-1)/2),
C_sup   = 8 D!/(pi rho^2)^D * A * V.
```

The point norm squared is at most C_sup times the original component
Petersson norm squared. Thus the actual Bergman function and section
rank are at most C_sup. The multiplication norm is at most sqrt(C_sup).
Under the original logarithmic size inequalities,
log C_sup <=250 f^2 r^2 L; in the original family this gives exactly
log C_sup <=4000(fr L_b)^3.

The calculation retains all growing field and rank factors.
Conductor one does not make these quantities bounded.

## Decisive arguments

1. The existing principal-level isotropic-flow construction forces a
   half-supremum frame to have q_x(v)>=epsilon for every nonzero original
   lattice vector. The form is periodic with the exact identity
   M_* k_0=2 M sqrt(d_H). The norm-factor loss is 2^(w/2), for the
   unsquared point norm. Periodic Schwarz gives exp(-pi/(M_*k_0 epsilon));
   squaring only occurs afterward in the supremum estimate.
2. The trace dual is not silently identified with the original lattice.
   The exact inclusion (Delta/2) J_x L^* subset L retains the different
   and the factor two from summing over a CM type. Elementary
   transference produces r E-independent integral vectors of q-length
   squared at most (2fr)^4 Delta^2/(4 epsilon).
3. A returning arithmetic matrix is determined by its values on those
   vectors. The actual chart changes majorants by at most a factor two.
   Euclidean packing gives the explicit multiplicity A. The exact
   Gram-minor metric and invariant density give the submean factor
   2 D!/(pi rho^2)^D. The half-maximum costs four, not two.
4. E/E+ is unramified at all finite primes, including those above two.
   Self-dual local lattices give the usual smooth SU densities. The
   trace-zero Lie lattice has trace-form determinant ideal (r), so its
   finite index cancels the same index in the invariant differential
   measure. The diagonal torus and root coordinates give the exact
   compact factor (2^(r(r-1)/2)(2pi)^(r-1)sqrt(r))^f.
5. Level-one volumes retain stabilizer weights. The proof passes to
   the actual principal level M>=3 before using an ordinary flag
   fundamental-set volume. Torsionfreeness is proved on the underlying
   integral lattice by the p-adic binomial argument; killing the
   determinant character alone would not suffice. This was corrected
   during independent volume review.
6. Hilbert 90 and integral unit reduction retain h_E M^(2f) determinant
   classes; the finite-level index is at most M^(2fr^2). Only after the
   full mass V has been included is the original component probability
   normalization used.

## Generating the entire integral module

For a coefficient field K of degree a and a lattice of K-rank q,
a K-spanning family of norm <=R yields at most 2aq **Z-generators**
of norm at most a^3 q rd(K) R. Short rationally independent integral
coefficient vectors come from the trace-dual transference bound.
Their products with a selected K-basis form a full Z-sublattice.
Reduce generators of the finite quotient in its half-open
parallelepiped. This preserves membership in the original lattice
and makes the norm bound independent of its unknown index.

For X=fr L_b, Y=kappa/T+1, the proved short sections and rank bound give

```
log(number of generators) <=5000 X^3,
log(generator norm bound) <=806000 X^5 Y,
log(Bergman bound)         <=4000 X^3.
```

The original P>=X^12 and X>=8 give the literal required frame
inequalities log n<=P, log beta<=P, log Lambda<=P(kappa/T+1).
The same original field is retained, including
log[K:Q], log rd(K)<=391 X^2. There is no free-module assumption.

## Source and independent verification

Every Lean source is pinned to
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The checker records full paths, Git blob hashes, SHA-256 hashes and
bounded interface ranges. Important source interfaces include

* `Divisors.UnifOfSpaceEq`103–116: literal constants.
* `FundamentalDomains.MaxBoundPf`12–257: original unsquared norm,
  periodic flow, 2^(w/2), and exact half-maximum inequality.
* `ExistsThickPointHyperbolic`269–423: original trace dual and short
  independent vectors, without a free integral basis.
* `CardGroupElementsChartReturnLe`128–213 and
  `NormFactorAndDensityNearOneInFlagChart`97–185: actual chart and measure.
* `CuspFormSupNormLePeterssonIntegralComponent`67–194: exact local consumer.
* `RiemannianLieVolumeFormula`13–28;
  `RealUnitaryCovolumeSum`89–145;
  `CovolumeRealSpecialUnitaryEqFlagDomainMass`129–160:
  retained Lie index, local densities and compact factor.
* `MassBoundOfTamagawaUnitary`15–87,
  `NormOneTorusClassNumberBoundProof`14–44 and
  `FramedDictionaryBound`20–57: actual determinant and finite-level mass.
* `WeightedFrameSumPositive`86–164 and
  `LevelGeometryWeightBound`38–107: original probability and component cuts.
* `ShortGeneratorNormComparison`25–101 and
  `ExistsLatFrameOfIsShortGen`19–60: entire Z-generation, original frame
  norm and original coefficient field.
* `ExistsCuspFrameWeights`76–112,187–231: the exact final consumer.

The primary volume reference is G. Prasad, *Volumes of S-arithmetic
quotients of semi-simple groups*, Publ. Math. IHES 69 (1989), §§3.3,
3.7, 3.11, https://www.numdam.org/item/PMIHES_1989__69__91_0.pdf .
Section 3.3 explicitly records the special unitary, outer type-A
case. The argument uses the full adelic sum of component covolumes,
so it does not apply the noncompactness hypothesis of strong
approximation to a definite group.

The root independently reviewed the whole upper argument and its
numerical constants. A second agent reviewed the arithmetic volume
normalization and identified the stabilizer correction above.
The executable checks authenticate sources and test exact finite
normalization and lattice models. They are supplementary evidence;
they do not prove the general mathematical statements or build Lean.

## Next frontier

The remaining lower bound in the thin region requires an actual
theta section with the prescribed point-to-supremum ratio. Its source
reduction uses a finite sum of squared theta values and the original
harmonic jets. It is not a consequence of the upper bound, integral
spanning or qualitative nonvanishing. Point heights and the final
arithmetic section remainder remain separate as well.
