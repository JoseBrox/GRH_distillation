# Fixed-reference convergence: an elementary cutoff proof

This note supplies the analytic convergence and smoothing-variation part of
the reference-model argument in [geometry-logarithmic-wall-heights.md](geometry-logarithmic-wall-heights.md).
It uses the actual regularization bounds, not an additional conjecture about
singular intersection products. All constants in the proof may depend on the
fixed analytic system, but not on a model realizing that system, its degree,
or its varying cutoffs.

## 1. Hypotheses and conventions

Let X be a compact smooth complex d-fold, D a simple normal crossings divisor,
and ω a fixed Kähler form. The finite set of line bundles has smooth reference
curvatures α_i and regularization potentials φ_i(t), with t tending to zero.
Write γ_i(t)=α_i+dd^c φ_i(t), using the same curvature and log-metric
conventions throughout. Changing the convention by a fixed common constant
does not change the estimates below. The actual regularization fields
(IsSingWeight, IsRegFamily and IsRegFamilyC2) give, with
r=e−2 log||s_D||≥e on X\D and L=log(1/t), for small t:

* −C log r ≤ φ_i ≤ C, and φ_i ≤ φ_i(t) ≤ C;
* γ_i(t) ≥ −ε(t)Θ, where Θ is a fixed positive form,
  ε(t)=O(log L/L);
* φ_i(t)−φ_i ≤ t^(1/3)+ε(t) wherever r≤L;
* φ_i(t) tends to φ_i in C² on compact subsets of X\D.

The function r is locally a sum of positive multiples of −log|z_j| plus
a smooth function. Consequently it is integrable against smooth volume,
and dd^c r is a bounded smooth form off D. Multiplying ω by a fixed constant
if necessary, all α_i+ω and β_i(t)=γ_i(t)+ω are positive closed smooth
forms for small t. In particular no positivity assumption on individual
root *differences* is needed. All assertions below permit mixtures of
regularization parameters and smooth reference forms.

## 2. Uniform tail lemma

For any product μ of d factors chosen among the β_i(t), α_i+ω and ω,
with arbitrary sufficiently small parameters, one has

    μ{r≥R} ≤ C(1+log R)/R,
    ∫_{r≥R} log r dμ ≤ C(1+log R)^2/R          (R≥e).

Proof. Choose a smooth nonnegative increasing concave function h_R on
[r_min,∞), equal to r/R up to R and constant beyond 2R, with derivative
between 0 and 1/R. Its value is at least 1 for r≥R. The composite
χ_R=h_R(r) extends smoothly across D, being constant near it. Off D,
the chain rule and concavity give dd^c χ_R ≤ Cω/R; the same inequality
holds on X. Moreover dd^c χ_R is supported where r≤2R. Here and below
the tail sets can include D, on which all smooth volume forms have zero
mass.

For a mixed positive closed (d−1,d−1)-form T made from the indicated
factors, the signed measure ν=dd^c χ_R ∧ T has integral zero by Stokes.
Its positive mass is at most C/R times ∫ω∧T; its negative mass is
the same. The latter integral is a fixed cohomological number,
independent of the regularization parameters. On the support of ν,
|φ_i(t)|≤C'(1+log(2R)), since φ_i≤φ_i(t)≤C. Integration by parts
therefore gives

    |∫ χ_R dd^c φ_i(t) ∧ T|
      = |∫ φ_i(t) dd^c χ_R ∧ T|
      ≤ C''(1+log R)/R.

Replace each β_i(t) by α_i+ω, one factor at a time. The mixed T stays
positive. The integral of χ_R against the resulting all-smooth product
is O(1/R), because χ_R≤r/R off D and r is locally log-integrable.
The finite telescoping sum proves the first bound. The second follows
from the layer-cake formula

    ∫_{r≥R} log r dμ =
      log R μ{r≥R} + ∫_R^∞ μ{r>a} da/a.

All constants can be chosen simultaneously for the finite species.
Expanding γ_i(t)=β_i(t)−ω proves the same bounds for total variation
of signed mixed curvature products. The d=0 case is just convergence
on finitely many points of the open domain; a genuine divisor has
empty support there.

## 3. Mixed arithmetic intersections and the original rate

Fix any algebraic realization of this analytic system with smooth
reference metrics, and let I(t) be a mixed arithmetic intersection of
d+1 of its regularized metrized lines, divided by the degree of the
realization. The metric-change identity expresses I(t')−I(t) as a
sum of d+1 archimedean integrals of φ_i(t')−φ_i(t) times mixed
curvatures at t and t'; no finite-place terms change. This identity
is obtained by changing one metric at a time (multilinearity and the
definition of the arithmetic class of a smooth function). For a
generically finite holomorphic realization π of degree n, the actual
line_eq and ref_pot fields identify these integrands with pullbacks
of the ones on X: smooth curvature depends only on the potential
modulo pluriharmonic functions. Integration of a top form multiplies
by n, as follows by change of variables off the branch locus; the
degree normalization cancels it. If a further normalization is used,
retain its fixed factor, not an independently chosen volume.

Take 0<t'≤t small and R=L=log(1/t). On r≤R, the regularization error
for both parameters is bounded by t^(1/3)+O(log L/L) (log x/x is
decreasing for x≥e). On the complement the difference is bounded by
C(1+log r). The uniform tail lemma and the fixed total variation bound
(cohomological mass of positive mixed products after expansion)
therefore imply

    |I(t')−I(t)| ≤ C (1+log L)^2/L.              (RC1)

In particular the normalized mixed arithmetic intersections are
Cauchy, and their limits are the ordinary limits of the actual
smooth arithmetic intersections. With t=exp(−1/s²), the right side
is O(s²(1+log(1/s))²)=O(s), for 0<s≤s₀. Finite linear combinations
with coefficients in a fixed bounded set have the same conclusion.
This proves the convergence/rate assertion required by the reference
argument; a separate general theory of products of singular currents
is unnecessary for this purpose. It even recovers the original
AgreementPos estimate whenever its AnSys/Realis fields are in force.
The argument does not establish the existence of those fields for
an unrelated metric.

## 4. The flat prefix and the weighted metric estimate

For a last prefix whose regularized curvature is both semipositive and
seminegative (the actual Flat field), that curvature vanishes. The
difference of two regularized potentials is therefore a smooth
pluriharmonic function on a compact component, hence constant.
Evaluate the difference at any fixed interior point of that component.
The regularization convergence there bounds the constants uniformly
as t tends to zero. In particular the last-prefix potential is
uniformly bounded (including at the boundary); it is not necessary
to claim that the potential itself is constant.

For a decreasing weight u=(u₁,…,u_N), write
a_i=u_i−u_{i+1}≥0 for i<N, a_N=u_N. Abel summation gives
Σu_j x_j=Σ a_i Σ_{j≤i} x_j exactly. The actual RealTie fields
fund_deg and fund_reg identify the prefix degrees and regularized
prefix log metrics; ref_none and phT_none leave the auxiliary line
unchanged. Relative to the smooth reference, the nonnegative gaps
multiply potentials bounded above by C and below by
−C log log(1/t), while the last prefix is bounded on both sides.
The smooth reference comparisons on a fixed compact model cost
only bounded terms. Thus for bounded weights the weighted prefix
variation is between −C(1+log log(1/t)) and C in the prefix
potential convention (reverse signs if comparing log *norms* in
the opposite direction). The exact sign in the height application
is the one prescribed by fund_reg; one must not silently substitute
a root norm for a prefix norm.

The common-model isometric linkage of the preceding note now allows
(RC1) to be used directly in its LW6/LW7 argument. For fixed reference
data no independent uniform convergence-in-cutoff estimate remains.

## Source check and limits

Compared with the pinned source jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de:

* lean/src/ReciprocityTheory/AnalyticForms/LeviForms/IsRegFamilyInhabitStatement.lean
  (IsSingWeight, IsRegFamily, IsRegFamilyC2): the explicit potential bounds.
* lean/src/Development/AutomorphicSpectrum/Definitions/MetricPeriods/MetricsProjectionFormulaNef.lean
  (Realis): line_eq, ref_pot, positive degree and normalized intersections.
* lean/src/Development/AutomorphicSpectrum/Definitions/DivisibilityTowers/RefLinked.lean
  (RealTie, Flat): actual prefix and auxiliary line conventions.
* lean/src/Development/AutomorphicSpectrum/Statements/GeometryStatements/AgreementPos.lean:
  convergence and smoothing rate to be supplied.

The proof above uses only smooth Stokes, positivity, the SNC local
expression and the elementary metric-change formula. It avoids
assuming uniform log-log integrability merely from pointwise
convergence. It does not by itself supply the remaining toroidal
Lie-metric identifications, flag degree/proportionality, divisor
comparison or common theta realization.
