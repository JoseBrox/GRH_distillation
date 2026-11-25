# W10: reference quotient metrics and the theta divisor certificate

Continuation of the [logarithmic tangent slopes](geometry-logarithmic-wall-heights.md)
and [reference convergence](geometry-reference-mixed-convergence.md) notes.
This is a conventional proof of the two local mathematical mechanisms,
with the remaining actual-family comparison hypotheses identified.

## 1. Uniform quotient metric at logarithmic period charts

The following elementary matrix argument explains the source
LogPeriodLimit and PrincipalNearBoundary chain without taking a
limit of unrelated Hermitian forms.

In a fixed toroidal chart use an adapted symplectic integral basis
and its holomorphic tangent frame A(z). The interior periods are

    A(z)^t (u + τ(z)v),    (u,v) ∈ Z^g × Z^g,
    τ(z) = T(z) + Σ_j B_j log(z_j)/(2πi),

with A holomorphic invertible at the chart centre, T holomorphic,
B_j real symmetric positive semidefinite integral matrices.
These are chart hypotheses, not conclusions of a generic
isomorphism of Lie algebras. At the centre the imaginary part of
T is positive on W=∩ker B_j. (The empty collection gives W=R^g.)
This is precisely the nondegenerate residual period condition.

Shrink the chart. Write the imaginary part in the orthogonal
splitting W⊕W^perp. Its W-block is bounded below by a>0, its
off-diagonal block has bounded norm M, and its W^perp block is
bounded below by λ min_j (−log|z_j|/(2π))−M with λ>0, since
Σ B_j is positive definite on W^perp. The elementary inequality
2M||w||||w'|| ≤ (a/2)||w||² + (2M²/a)||w'||² gives a fixed
lower bound cI for Im τ on the punctured chart, with c>0.
If W or its complement is zero, simply omit that block.

Now consider *any* face within the shrunk chart: let J be its
vanishing coordinates and W_J=∩_{j∈J} ker B_j. The finite
residual imaginary period form on W_J is the restriction of

    Im T(z) + Σ_{j∉J} B_j(−log|z_j|/(2π)).

It is ≥cI: evaluate the interior inequality on W_J and pass
to the face, where the divergent terms vanish identically on
this subspace. This includes intersections of boundary divisors,
not just the initially chosen stratum.

For clarity, in the normalized period coordinates the convergent
periods along a radial approach to this face form the lattice
Z^g ⊕ (W_J∩Z^g); the divergent periods cannot converge with
a nonzero fixed complementary v, since their imaginary parts
diverge. The quotient by the radical of the restricted integral
symplectic pairing is the symplectic lattice of the residual
abelian part. In the actual normalized period realization its
polarization Hermitian form is the inverse of the residual
imaginary period matrix on W_J, pulled back under the quotient
projection. Equivalently the limiting Hermitian form on all
g coordinates is zero on the orthogonal complement and has
norm ≤1/c. One can see this by a Schur complement of the
divergent block. A change back by A(z) costs at most the
square of a fixed bound for ||A(z)^(-1)||. The polarization
convention may contribute its fixed factor π, which must not
be dropped from an equality. Thus the canonical quotient norm
is uniformly bounded above by a constant times the smooth
reference tangent norm on the chart, provided the original
quotient period and frame identifications hold.

This bound is unaffected by finite changes of integral symplectic
basis when the same period lattice and Riemann form are used.
On a fixed compact model take a finite collection of shrunk
charts; continuous positive reference Gram matrices in the
extending frames have a positive minimum eigenvalue there.
This gives the uniform operator bound used in LW4. It does not
assume a uniform compactness statement as the tower varies.

There is a similarly simple torus observation. On a connected
complex base, let a homomorphism from a split torus T to a
semiabelian scheme extend over the closure of a stratum, and
be an embedding on a nonempty fibre. Every nonidentity
ℓ-torsion section of T remains nonidentity everywhere:
the ℓ-torsion of the semiabelian scheme is separated and étale,
so the equalizer with the identity is open and closed. A
positive-dimensional fibre kernel would contain nonidentity
ℓ-torsion for every prime ℓ; a finite nontrivial kernel would
contain such torsion for some ℓ. Hence all fibre maps remain
injective, and in characteristic zero their differential has
full rank. The Gram matrix of the cocharacter frame in a
continuous positive metric is therefore positive even at
the boundary of such an extension. Compactness bounds both
its extreme eigenvalues. Apply this separately on finitely
many compact splitting covers when the extension morphisms
are known. Neither a torus splitting solely on a noncompact
stratum nor generic injectivity of a matrix of rational functions
is a substitute for the extending morphism.

Source interfaces checked: GeometryProofs/LogPeriodLimit.lean
(at_point: adapted periods, the uniform positive bound and the
residual pairing); PrincipalNearBoundary.lean (principal quotient,
pullback of Hermitian form and equality of Riemann pairings from
all root-of-unity tests); BoundaryChartLieMetricBound.lean
(chart coordinate/reference metric comparison);
LieMetricHeightBound.lean (recentering, finite chart cover and
conjugation). The matrix proof gives the analytic inequality
once the source period/quotient realization is constructed.
The existence of the finite compact torus-extension covers and
the algebraic frame/orthogonal-flag pins remain to be verified.

## 2. A uniform theta lower order: no averaging of the products

Let R>1 be odd, and let X be the monodromy character lattice
with its O_E action. Let β be a positive semidefinite symmetric
real bilinear form with the conjugate-adjoint O_E action and
β(x,x)=2Q(x), Q nonnegative integral. Define φ_C as in the
source: the infimum at β of integral linear functionals on
the space of conjugate-adjoint forms which are strictly positive
on its nonzero positive cone. The integrality lattice here
consists of integral bilinear forms, not merely integral values
of Q. The fixed host supplies w₀∈O_E with w₀+bar w₀=1.

If x_1,…,x_N span X⊗Q over E, then

    φ_C(β) ≤ Σ_b Q(x_b).                         (DV1)

Indeed ℓ(γ)=Σ γ(w₀x_b,x_b) is integral on integral forms and
equals (1/2)Σ γ(x_b,x_b) by conjugate-adjoint symmetry.
It is nonnegative on positive semidefinite forms; equality
implies every x_b lies in their radical (Cauchy–Schwarz).
The radical is O_E-stable, so equality forces γ=0 by spanning
over E. Thus ℓ is one of the linear functionals in the defining
infimum. This proof also handles semidefinite β.

Let m=R². Suppose y_b span X/m²X over O_E. For every b choose
a minimum Q on the coset y_b+mX (exists by integral
nonnegativity), represented by x_b. These representatives
still span X/mX. The finitely generated abelian group
X/Σ O_E x_b equals its multiple by m, and hence has no free
part, since reduction of a positive-rank free quotient modulo
m is nonzero. The x_b therefore satisfy (DV1). Consequently

    Σ_b min_{χ∈X} Q(y_b+mχ)/m² ≥ φ_C(β)/m².       (DV2)

The normalized toric theta expansion at a torsion point lifted
to y_b has valuation at least min Q(y_b+mχ)/m²; integrality
of all coefficients and the ultrametric inequality are the
only estimates needed here. This is the precise odd-level
expansion convention of the pinned source
le_valuation_oddLevel_thetaConstant_integralExpansion.
Use the actual full R⁴-level symplectic torsor and its
surjective projection onto X/R⁴X. An admissible N-tuple
spanning modulo R remains spanning modulo R⁴ (local Nakayama,
or iterating the equation X=S+RX four times). Independent
shifts of its entries by R times a level-R representative
do not change this property, nor does a level automorphism.
Thus the product f of the N normalized theta constants has

    ord(f) ≥ φ_C(β)/R⁴.                         (DV3)

The estimate holds for every admissible shift and every
centered valuation realizing these data, not just at the
generic point where f is chosen. A zero factor gives infinite
order and does not invalidate the lower estimate.

## 3. A single nonzero section on the component

On the actual full-level torsor the normalized null values
are uniquely determined by the prescribed framed theta
section. On the fibre product of two faithfully flat
trivializations the level markings and normalized values
agree by uniqueness; the product therefore descends by the
faithfully flat equalizer. Scaling the framing multiplies
each null value by the scalar framing character and the
product by its N-th power. This gives the scalar weight-N
rule f on the open variety, with natural base change.

The source shifted nonvanishing statement is particularly
useful here. For a nonzero generator of the principal
theta line and a fixed point a, some translate by an
R-torsion point is outside its theta divisor. This is the
basepoint-freeness of the full torsion-translate system at
R>1 in its exact theta normalization (source goodPt).
For a normalized null value at level R², multiplication by
R² of a lift at level R⁴ sends x+R u to R²x+R³u. The
R³u, u modulo R, exhaust the R-torsion by freeness of
the level lattice. Hence one can choose the shift of each
of the N entries independently at the geometric generic
point of the component Z so all N factors are nonzero.
This one fixed choice gives a nonzero descended f on Z;
(DV3) continues to hold at all valuations, independently
of the generic choice. There is no need for a symmetrized
sum of theta products, which could introduce cancellation.

For the actual weight correction take R=5 and N=p+q.
The source thetaOn is exactly

    θ = idem_Z f^8 K^N ∏_τ s_τ^(4N),

where K is the key rule of character 4 keyEx and s_τ the
prescribed flat sections. The scalar weight computation
8 ex(0,N)+4N keyEx = exOf(8N hodgeWt+parWt(4N),0)
and the flat-section character subtract parWt(4N).
Thus θ has weight 8N hodgeWt. The key and flat factors
are nonzero on the component and have nonnegative order
in the actual integral frame. Over a horizontal valuation
of the characteristic-zero flag model the coefficient
field has order zero; the frame comparison is by units.
Equations (DV2) and (DV3) yield

    ord_D θ ≥ 8 φ_D/625                           (DV4)

at every centered valuation represented by the source
PhiAt, since both the valuation and φ are scaled by the
same positive number ρ. In particular (DV4) does not lose
a factor on a ramified cover. Normality extends θ from
the open if this bound holds at every boundary height-one
point: a rational section of an invertible sheaf on a
normal noetherian variety is regular exactly when its
orders at all height-one points are nonnegative.

The remaining inputs of this construction are explicit:
the actual full-level/normalized-null-value laws (including
goodPt), the integral expansion, existence and integral
frame laws of K and s_τ, and the actual centered PhiAt
realization. The formula is a proof of the divisor lower
bound from those inputs, not a construction of unrelated
global theta periods for W06.

## 4. Certificate, with the original constants retained

Let E_base denote the base divisor on the normalized blow-up
of the actual cusp ideal and b_D its coefficient at D.
For every divisor, a single cusp section with finite order
≤φ_D/2500 gives b_D≤φ_D/2500. This is the precise source
Hilbert–Samuel target; the weaker bound ≤3φ_D/625 is
already enough. With (DV4),

    ord_D θ³ ≥ 24 φ_D/625 ≥ 8 b_D.

At interior divisors b_D=0 by the actual interior
basepoint-free theorem. Hence div(θ³)−8E_base is effective
and θ³ has the required line weight 8(A−A'). This completes
the formal finite certificate implication, and proves its
lower-order calculation independently of Hilbert–Samuel.

The outstanding upper-order supplier is still the actual
Hilbert–Samuel jet estimate, or the alternative LW8 arc
comparison limsup Φ/log(1/|t|)≤6φ_D. Neither follows from
(DV2): φ_C is an *infimum* of positive integral functionals,
whereas an arbitrary analytic norm comparison may be in
the wrong direction. Do not declare the finite certificate
established until one of these upper-order routes and the
actual key/flat/centered input identifications is verified.

## Immutable source ledger

All below are under lean/src/ at
jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.

* Formalism/SharpRestriction/Divisibility/GeneratorPowers/
  PhiCSpan.lean, ETSpan.lean (DV1 and reduction modulo m).
* Development/AbelianVarietyTheory/Proofs/TorusSplitting/
  SumCosetMinGePhiCDivSq.lean (DV2).
* Development/AbelianVarietyTheory/Proofs/DivisorProofs/
  ExistsNonzeroSectionWeightBound.lean (tau_bound).
* Development/AbelianVarietyTheory/Definitions/Divisors/
  ExistsIsTauZeroNonzeroAll.lean (faithfully flat descent,
  scalar weight, admissible tuple, thetaOn).
* Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/
  ExistsShiftNullValNeZero.lean (independent R-torsion shifts).
* Development/AutomorphicArithmetic/ThetaCorrespondence/
  ThetaPairLifts/HodgeBundleWeights/ExistsNonzeroSectionWeightBound.lean
  (exists_theta_multiplication_rule, exists_section_of_theta_datum;
  the nonnegative key/flat valuation and normal extension).
* The same ThetaPairLifts/ThirdPlaceSeries/
  ValuationMultiplicityOfConsecutiveRun.lean (cube and eighth
  powers, same centered valuation, interior basepoint-free);
  ExistsCuspValueLePhiOfHilbertSamuel.lean (upper order φ/2500).

No Lean replay or complete source dependency verification is claimed.
