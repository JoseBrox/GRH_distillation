# The actual lower Bergman bound in the thin region

> **Later status (23 November 2026).** The [component section-degree estimate](geometry-section-continuation.md), [actual tangent-degree comparison](geometry-point-continuation.md), and [corrected integral fibres](geometry-hodge-specialization.md) have since been supplied. The regularized point-height identity and final weighted budget are still separate; see the [live frontier](current-state.md).

## Result and scope

The ordinary proof in paper/shared/geometry-bergman-continuation-thin.tex
constructs the missing determinant jet on the **original** principally
polarized CM period torus. It gives the literal lower bound

~~~
B_Z(x) >= exp(-phi(x)/625),
phi(x) = 2f/(rd(E)^2 lambda(x)^2).
~~~

The first minimum, section, component and probability norm are the
original ones. The proof retains the construction's numerical family
hypotheses. Their existence is not inferred from a source theorem's
name. Point heights and the final arithmetic section remainder remain
open; W10 is not completed.

Independent reviews checked the determinant construction, anisotropy,
periodization, absolute unfolding, frequency separation, Gaussian
estimates and exact downstream numerical and metric interfaces.
The certificate's PASS
refers to source authentication and exact diagnostics, not an
automatically verified general proof.

## New mathematical construction

For the prescribed determinant operator of degree D on n columns,

~~~
|P(partial)F(0)|^2 / ||F||_2^2
  >= 2^(-3n) 16^(-D) exp(-2 pi n C phi/q),
C = 8100 m^4 (2fm)^4 rd(E)^7.
~~~

This implies the source's Jbound because r>=2 and K6>=2.

1. Short integral coefficient vectors give a saturated, CM-stable
   isotropic sublattice I. Integrality forces a short projected
   extension to remain isotropic. Its exact dual lattice is the
   imaginary-frequency lattice of the original periods, with minimum
   at least 1/(Omega theta).
2. A lattice's Voronoi cell is contained in the convex hull of its
   lattice points in three times the cell. Repeatedly round 2v and
   divide by two. Maximize each determinant over these frequencies
   and normalized abelian directions. Multilinearity controls
   relative errors without a condition-number hypothesis.
3. The actual Appell–Humbert periodization has scalar modulus
   exp(-pi q |b|^2-pi q |a|^2/2+2pi <b,u>).
   The Voronoi condition bounds the last term by 3pi |b|^2.
   The CM real form makes its holomorphic quadratic term vanish
   on one embedding, so the prescribed column jets are exact.
4. An abelian column of derivative order c uses
   (sqrt(qc) <z,xi>)^c/c!. Its jet and normalized Gaussian overlap
   have coefficients binom(c,l)/l!. The Bessel bound
   exp(2 sqrt(pi c) sqrt(q)|a|) is absorbed by the original linear
   bound for R0^2. Dropping the factorial would introduce an
   unjustified degree-times-log-degree loss.
5. An explicit absolute overlap estimate justifies unfolding.
   Integration over U/I then kills every nonzero dual frequency.
   Remaining overlaps are Laguerre polynomials times a Gaussian
   on a thick lattice. Principal unimodularity retains the original
   probability normalization.

## Exact original interfaces

All sources are pinned to
jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.
The certificate records full paths, file and range hashes.

* GCauchyStatement 160–174 implies every displayed analytic
  hypothesis: hR0 at169 is exactly R0²≥90(g+D); C5 at174 is
  the retained t0 threshold; C1 at170 gives d*² Omega theta²<1,
  hence Omega theta²<1 since d*=2fm≥2; C2 at171 gives b0≥1;
  C3 at172 gives q≥180m²d*²R≥11520. The conditions on m,f,R
  are163–168. The abstract parameter record only has fr≥2.
  Actual r≥2 comes from Formalism.LocalRingCardinality.Params
  13–14,32: m≥2, k≥m+3 and r=k+m−1, so r≥6.
* ThinCore254 retains b^16≤M≤b^70. The actual supplier
  CuspFormExistsBelowFrameBound134–152 proves these using
  b^8≤g_i≤b^35 and M=g0g1. EtaBoundLengthUnit139–161 proves
  Mdeep=M·15^a≥bM, where b=exp(L), L≥1, and
  a=floor(3L/log3); indeed a log3≥3L−log3≥L.
  Its165–177 records the actual square-root parameter choice and
  the original family bounds. Thus deep thinness Mdeep lambda²<b
  gives M lambda²<1 without changing either minimum or metric.
* IsBlockProd 29–31 requires disjoint columns across ALL blocks.
  ExistsBlockProductMemIntegralHarmonic 226–242,292–338 constructs
  them with the exact row degrees, harmonicity and coefficient bound.
* NonemptyUnitAt 84–85 gives the actual theta probability norm one.
  ThetaFunctionTorusL2Norm 61–100 transports that same norm.
  TiledBoundaries.NstatementOf 22–68 proves finite-isogeny pullback
  and translation preserve it exactly.
* CardLatticeQuotientHalfLevel 43–79 retains the original projective
  module, giving M^(fr), hence M^(gn) on n columns.
* SumLeFinsumOfSurjectsOntoFinset 232–337 gives actual scalar
  M^(-D) kappa sqrt(2xi_R)^D with |kappa|^2=M^D, hence squared factor
  (2xi_R/M)^D. IsTorusAtOfIsTorusOf 205–233 retains the first minimum.
* ThinCore 251–344 gives the original minimal-level consumer.
  CuspFormExistsBelowFrameBound 165–190 transports the actual
  metric and minimum to the deep cover.
* ExistsConstantTwistOfThinDivisor 12–49 gives g supported on the
  SAME component Z with ||g(z)||=K||f(z)|| for every z in Z and
  K>0 independent of z. It uses the existing key and parallel twists.
  BergmanKernelThinPartEstimate 16–49 squares the unsquared ratio.

## Verification and next frontier

~~~
python3 scripts/geometry-bergman-continuation-thin.py --offline
~~~

The checker authenticates sources; verifies ordinary-derivative
factorials, normalized Laguerre moments and the absolute-overlap
square completion symbolically; and verifies positive all-parameter
margins in the Gaussian-tail and endpoint budgets. Finite anisotropic
lattice examples supplement the general Voronoi argument.

With the thick bound, global upper bound and full integral frame,
this supplies the pointwise norm estimates. The next decisive target
is the actual finite arithmetic jet/height construction and its
section-degree remainder, retaining the same integral lattices.
