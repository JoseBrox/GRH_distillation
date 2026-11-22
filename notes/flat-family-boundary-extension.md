# A flat determinant on the actual semiabelian tangent bundle

## Result and retained geometric input

An elementary period argument supplies the missing analytic boundary
extension of the determinant section. It uses the actual semiabelian
family and its original polarization line. Together with the exact
level argument, resolution and GAGA, it constructs an algebraic
generator on the whole characteristic-zero model.

Here is the precise theorem. Let \(K\) be a number field, \(E\) a CM
field with an embedding \(\tau:E\to K\), and
\(\bar\tau=\tau\circ\mathrm{conj}\). Let \(Y/K\) be a normal,
geometrically integral proper variety, \(U\subset Y\) a dense smooth
open, and \(G/Y\) a smooth separated commutative group scheme of
constant relative dimension, all of whose geometric fibres are
semiabelian. Suppose the original line bundle \(\mathcal L\) on \(G\)
induces a principal polarization on \(G_U\), which is an abelian
scheme. Suppose an \(\mathcal O_E\)-action has the prescribed
polarization adjunction, and its integral period lattice and level
satisfy the hypotheses of the half-level determinant proposition.
Write
\[
 \mathcal V=\operatorname{Lie}(G/Y),\qquad
 \mathcal D_\tau=\det\mathcal V_\tau
                    \otimes(\det\mathcal V_{\bar\tau})^{-1}.
 \tag{1}
\]
In characteristic zero these eigenbundles are actual direct
summands of \(\mathcal V\).

**Theorem.** The line (1) has a nowhere-vanishing algebraic section
over \(K\), unique up to \(K^\times\). Its norm for the prescribed
Hodge tangent metric is constant on each complex abelian locus.
The extension uses the actual Lie bundle in (1); no boundary
divisor is added.

The theorem constructs the flat determinant from the stated model.
It does not construct that arithmetic model, its level charts or
its integral finite-place identifications. The already proved
finite-place rigidity and CM evaluation remain separate suppliers.
No full RH or GRH node is declared complete here.

## 1. A central isotropic period frame

Work on a sufficiently small complex polydisc \(S\), with coordinate
boundary \(z_1\cdots z_a=0\), obtained by pulling back the actual
algebraic family. Off that boundary the fibres are principally
polarized abelian varieties. Trivialize the actual Lie bundle.

At the central fibre write
\[
       0\longrightarrow T\longrightarrow G_0
         \xrightarrow{q} A\longrightarrow0,\qquad
       T\simeq\mathbf G_m^t,\quad \dim A=b,\quad g=t+b.
\]
The complex exponential has kernel \(\Gamma_0\) fitting into
\[
  0\longrightarrow 2\pi i\,\mathbf Z^t
    \longrightarrow\Gamma_0
    \longrightarrow H_1(A,\mathbf Z)\longrightarrow0.
 \tag{2}
\]
This follows from the homotopy sequence of the torus torsor; the
universal cover of a complex abelian variety is a vector space.
In particular \(\Gamma_0\) spans \(\operatorname{Lie}(G_0)\)
over \(\mathbf C\).

The line \(\mathcal L_0\) is a pullback of an algebraic line on
\(A\). Indeed the generic fibre of the split torus torsor \(q\)
has coordinate ring a Laurent polynomial ring over \(\mathbf C(A)\),
with trivial Picard group. Choose a rational section of
\(\mathcal L_0\) which has no divisor on that generic fibre.
Its divisor is vertical. Since \(q\) is smooth with integral
fibres, every vertical prime divisor is the multiplicity-one
pullback of a prime divisor of the smooth variety \(A\).
Thus this divisor, and hence the line, is pulled back from \(A\).

Consequently its alternating Chern form on \(\Gamma_0\) kills
the toric subgroup in (2) and descends to an integral form \(B_0\)
on \(H_1(A,\mathbf Z)\). This form is of type \((1,1)\), without
any assumption that the descended line is ample. One proof is
to average the Chern curvature of a Hermitian metric on the
line over translations of the compact torus \(A(\mathbf C)\).
The resulting constant real \((1,1)\)-form represents the same
Chern class.

We need the following elementary linear algebra fact. If an
integral alternating form on a complex torus is of type \((1,1)\),
there is a rational isotropic half-dimensional real subspace
\(L\) with \(L\cap iL=0\). To see this, its rational kernel is
stable under the complex structure. On the quotient by that
kernel, diagonalize the associated possibly indefinite Hermitian
form; the real span of a complex diagonal basis is Lagrangian
and transverse to its imaginary translate. Rational
Lagrangians are dense: in a rational Darboux chart they are
graphs of rational symmetric matrices, which are dense among
real symmetric matrices. Transversality is open, so choose a
rational such Lagrangian. In the kernel choose a rational
half-dimensional subspace transverse to its imaginary
translate, by density in the ordinary Grassmannian. Lift the
quotient Lagrangian and adjoin this kernel subspace. The resulting
subspace is isotropic and transverse to its imaginary translate.
Intersecting with the integral lattice makes it primitive.

Apply this to \(B_0\), lift the resulting half-lattice through (2),
and adjoin all toric periods. We obtain a primitive isotropic
rank-\(g\) subgroup \(\Gamma_A\subset\Gamma_0\) whose periods form
a complex basis of the actual central Lie algebra. This also
covers the purely toric fibre; rank zero uses empty bases.

## 2. Continuation preserves this integral primitivity

The exponential map of the family is holomorphic. Locally at
zero this follows by integrating the invariant vector fields,
with parameters; multiplication by an integer extends the local
exponential to any bounded part of the Lie bundle. Its derivative
at every period is invertible. The implicit function theorem
therefore continues each central period uniquely to a holomorphic
period section. Continue a finite basis of \(\Gamma_0\), shrink
once, and extend additively.

The alternating pairing of two continued periods is unchanged: its value
is the signed Chern number on the real two-torus parametrized by those
periods, hence an integer varying continuously with the base.
The continued \(\Gamma_A\) is therefore isotropic. Its period
matrix \(A(z)\) is holomorphic and invertible at zero, and remains
invertible after shrinking.

It is primitive in the full period lattice of every abelian fibre.
For \(\gamma\in\Gamma_0\) and \(n\ge1\), the section
\[
                \exp\bigl(S_\gamma(z)/n\bigr)
 \tag{3}
\]
is \(n\)-torsion on the entire polydisc. Multiplication by \(n\)
on a smooth group in characteristic zero is étale. Its kernel
is separated and étale, so the equalizer of (3) and the zero
section is both open and closed. On the connected polydisc,
(3) vanishes at one point exactly when it vanishes at zero.
Thus divisibility of a continued central period in any nearby
period lattice is exactly its divisibility in \(\Gamma_0\).
As \(\Gamma_A\) is primitive in \(\Gamma_0\), it is primitive
in each nearby lattice as well. This uses the same polydisc
for every \(n\); no intersection of infinitely many smaller
neighbourhoods is taken.

Complete these \(A\)-periods to an integral symplectic basis on
the universal cover of the punctured polydisc, with
\(B(A_i,B_j)=-\delta_{ij}\) in the linear-first convention
\(B=\operatorname{Im}H\). Write the complementary period rows
as \(\Omega A\). The normalized
period matrix is a holomorphic symmetric matrix \(\Omega(w)\)
with \(\operatorname{Im}\Omega>0\), where
\(z_j=\exp(2\pi i w_j)\) for \(j\le a\).
Since every monodromy fixes the \(A\)-periods pointwise, it sends
the complementary periods to themselves plus an integral
symmetric combination of the \(A\)-periods. Hence
\[
        \Omega(w+e_j)=\Omega(w)+N_j,\qquad
                N_j\in\operatorname{Sym}_g(\mathbf Z).
 \tag{4}
\]

## 3. Positive imaginary part gives all logarithmic growth

For completeness, the needed scalar fact has a short proof.
Let \(f(w+1)=f(w)+c\), where \(c\in\mathbf Z\) and
\(\operatorname{Im}f>0\). Then
\[
                     \exp(2\pi i f)
\]
is a bounded, nonzero holomorphic function of the punctured-disc
coordinate. It extends across the puncture. Its winding number
is \(c\), so its zero order is \(c\ge0\). Divide by the
\(c\)-th power of the coordinate and take a local holomorphic
logarithm of the resulting unit. It follows that \(f-cw\)
extends holomorphically. This includes \(c=0\).

Apply this to \(f=v^t\Omega v\) for integral \(v\). It proves
\(v^tN_jv\ge0\) on integral vectors, hence \(N_j\ge0\) by
homogeneity and density of rational vectors. Apply it to the standard basis vectors and their
pairwise sums to obtain
\[
            \Omega(w)=\sum_{j=1}^a w_jN_j+\Omega_0(z),
 \tag{5}
\]
with \(\Omega_0\) holomorphic on the whole polydisc. More
explicitly, the scalar argument works with the other nonzero
coordinates as parameters. It first extends the remainder across
the smooth parts of the coordinate divisors. Hartogs extension
then fills their intersections, which have complex codimension
at least two.

Put \(Y(z)=\operatorname{Im}\Omega(w)\),
\(N=\sum_jN_j\), and \(K_0=\ker N=\bigcap_j\ker N_j\).
On \(K_0\), every nonzero scalar quadratic form
\(v^t\operatorname{Im}\Omega_0(z)v\) is positive on the punctured
locus and harmonic on the full polydisc. It is nonnegative by
continuity and strictly positive at zero by the minimum principle.
Thus \(\operatorname{Im}\Omega_0(0)\) is positive definite on
\(K_0\). On \(K_0^\perp\), \(N\) is positive definite. A
Schur-complement estimate shows that, for some fixed \(T\),
\(\operatorname{Im}\Omega_0(0)+TN\) is positive definite.
Shrinking the polydisc ensures both that this remains true nearby
and that \(-\log|z_j|/(2\pi)\ge T\). Consequently
\[
       c\,1_g\ \le\ Y(z)\
          \le C\left(1+\sum_{j=1}^a|\log|z_j||\right)1_g
 \tag{6}
\]
for positive constants \(c,C\). Empty kernels and zero
monodromy matrices require no change in this argument.

## 4. These are the prescribed tangent norms

Use row vectors and the linear-first Hermitian convention.
The Riemann bilinear relations in the symplectic period basis give
\[
                     A H A^* = Y^{-1},
 \tag{7}
\]
where \(H\) is the original polarization's Hermitian form on
the actual Lie coordinates. If \(F(z)\) is a holomorphic
rank-\(k\) row frame which has rank \(k\) at zero, its prescribed
Hodge Gram matrix is
\[
           \Gamma_F=\pi FHF^*
                    =\pi(FA^{-1})Y^{-1}(FA^{-1})^*.
 \tag{8}
\]
The singular values of \(FA^{-1}\) are bounded above and bounded
away from zero near zero. Writing
\(D(z)=1+\sum_j|\log|z_j||\), (6) therefore gives
\[
               c_FD(z)^{-k}\le\det\Gamma_F(z)\le C_F.
 \tag{9}
\]
The factor \(\pi\) is retained. Formula (9) is on the original
Lie bundle and every full local subframe, including the two
coefficient eigenframes. It does not identify an arbitrary
extension of a flat local system with that bundle.

## 5. The determinant section has constant norm on the open set

The half-level proposition kills the determinant of every integral
period monodromy operator. Thus the determinant of each
coefficient summand of complexified homology has a single-valued
parallel generator.

Here the relation to (1), including the metric, can be checked
directly. Let \(H\) be the polarization's linear-first tangent
Hermitian form, so \(B=\operatorname{Im}H\) on real homology.
In its complexification put
\[
 e_+(v)=(v-iJv)/2,\qquad e_-(v)=(v+iJv)/2.
\]
The period map sends \(e_+(v)\) to \(v\) and kills \(e_-(v)\).
The Hodge exact sequence on the \(\tau\)-summand has quotient
\(\mathcal V_\tau\); polarization identifies its kernel with
\(\mathcal V_{\bar\tau}^*\). Analytically we may normalize this
identification by
\[
       e_-(v)\longmapsto
       \bigl(w\longmapsto2iB(e_+(w),e_-(v))\bigr)
                          =H(-,v).
 \tag{10}
\]
The expression with \(B\) is independent of the chosen lift
of \(w\), so this is a holomorphic identification.

The flat Hermitian form \(2iB(z,\bar w)\) on complexified
homology is \(H\) on the positive summand and minus the dual
of \(H\) on the kernel under (10). Taking absolute determinant
norms therefore identifies its flat determinant metric with
the determinant ratio of the unscaled tangent metric. Replacing
the tangent metric by the prescribed \(\pi H\) multiplies the
squared determinant norm by the constant \(\pi^{p-q}\), where
\(p=\operatorname{rank}\mathcal V_\tau\) and
\(q=\operatorname{rank}\mathcal V_{\bar\tau}\).
Thus the holomorphic determinant section has constant norm.
Normalize it analytically to norm one for the next step; no
claim about an algebraic scalar's absolute value is made.

## 6. Extension as a unit, algebraicity and descent

Write the normalized section in actual local eigenframes as
\[
                   s=\varphi\,\det(F_+)\det(F_-)^{-1}.
 \tag{11}
\]
It is single-valued by the level argument, and its unit norm says
\[
       |\varphi|^2\det\Gamma_{F_+}=\det\Gamma_{F_-}.
 \tag{12}
\]
Using (9) twice gives
\[
       |\varphi|\le C D^{p/2},\qquad
       |\varphi^{-1}|\le C'D^{q/2}.
 \tag{13}
\]
A holomorphic function with such logarithmic growth has no
negative Laurent coefficients: the coefficient of \(z^{-m}\)
is bounded by \(r^m(1+|\log r|)^N\), which tends to zero.
Apply this at the smooth coordinate divisors and then use
Hartogs extension at their intersections. Both \(\varphi\)
and its reciprocal extend holomorphically. Their product stays
one by density, so the extension is a unit.

For a general proper \(Y_{\mathbf C}\), first use Chow's lemma
and characteristic-zero resolution and principalization to
obtain a smooth projective variety \(Z\) proper birational over
\(Y_{\mathbf C}\), with coordinate boundary above the complement
of a smooth dense abelian open. Pull back the actual family,
line and Lie bundle. The preceding local proof extends \(s\)
as a nowhere-vanishing analytic section of the actual
pullback of \(\mathcal D_\tau\) on \(Z\).
Serre's GAGA theorem makes this section algebraic.

If \(f:Z\to Y_{\mathbf C}\) is this proper birational map,
normality gives \(f_*\mathcal O_Z=\mathcal O_{Y_{\mathbf C}}\).
For a direct justification, a regular function upstairs is
a rational function downstairs; properness extends the generic
lift over every codimension-one discrete valuation ring, so
the function is regular at each such ring, and normality makes
it regular downstairs. The projection formula now descends
the section. It stays nowhere zero because \(f\) is surjective.

Finally, flat base change for global sections gives
\[
 H^0(Y,\mathcal D_\tau)\otimes_K\mathbf C
       =H^0(Y_{\mathbf C},\mathcal D_\tau)=\mathbf C,
\]
since \(Y\) is proper and geometrically integral and
\(\mathcal D_\tau\) is trivial after this base change.
A nonzero \(K\)-section therefore exists and is nowhere zero;
all other generators differ by \(K^\times\). Its complex
restriction is a constant multiple of the normalized section,
so its prescribed metric remains constant. Applying the same
argument at every embedding of \(K\) proves the assertion
at every complex place.

## 7. Exact source match and remaining construction

All source modules below are pinned to
[jsmorph/rh, ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de](https://github.com/jsmorph/rh/tree/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de).
Only the stated bounded ranges were read into context.

| Source | Ranges | Supplied assertion |
| --- | --- | --- |
| ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/PushInvertible | 40–66 | Coefficient field, normal projective flat global model, dense generic abelian open, global semiabelian object and exact transport from the universal family |
| ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/TwoWeightEqOneAddRoot | 72–91, 144–160 | Global semiabelian group, original rigidified cubical line and adjunction; proper ample object with trivial kernel and prescribed level |
| ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/SemiabelianSchemes/AbelianSchemeQuotients/IsAbelianScheme | 19–48 | Smooth separated semiabelian family with actual geometric torus extensions |
| ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/IsCompletedStrictHens | 16–23 | Projectivity means a closed immersion into projective space, hence properness |
| AutomorphicSpectrum/Definitions/GlobalGeometry/BdryChart | 19–62 | Actual semiabelian family, Lie coordinates, original line and the exact \(\pi H\) Gram convention |
| AutomorphicSpectrum/Definitions/GlobalGeometry/IsFlatAnIffIsConstMul | 33–52, 121–185 | Unit analytic determinant; original tangent-frame transport; actual whole-generic-fibre eigenline |
| AutomorphicSpectrum/Proofs/GeometryProofs/LogPeriodsRiemannForm | 33–69, 83–126 | Original exponential and central-period data, with the original Hodge matrix |
| AutomorphicSpectrum/Proofs/MetricProofs/PeriodMatrixLocalTrivialization | 10–31 | Exact row-convention congruence (7) |
| AutomorphicSpectrum/Proofs/GeometryProofs/HodgeGramBoundNearBoundary | 52–119 | Exact actual-subframe determinant bounds (9) |
| AutomorphicSpectrum/Proofs/GeometryProofs/BoundaryChartFrameGrowth | 303–352 | Applying both bounds to the frame function and its inverse |
| AutomorphicSpectrum/Proofs/GeometryProofs/EigenFramesAnalytic | 121–198 | Extension, GAGA and normal birational descent on the same eigenline |
| AutomorphicSpectrum/Statements/GeometryStatements/FlatLineGenerator | 18–19 | Algebraic generator and uniqueness on the prescribed whole generic fibre |

The global family in the theorem is explicit in the source's
model definition, not inferred from analytic boundary charts.
The model's normality and projectivity are separate fields; its
global semiabelian object contains the original line and
coefficient action. The generic open is dense and its maps are
cartesian and preserve the original cubical line. On that open,
properness, ampleness and the scheme-theoretically trivial
translation kernel give a principal polarization. The coefficient
field contains every embedding of \(E\). On the component selected
by the source's generic point, IsGeom says exactly that this
coefficient field is relatively algebraically closed in the
function field. In characteristic zero this gives the
geometrically integral component required above. Normality
makes the irreducible components disjoint, so this component
is itself proper. The actual source model is projective; the
proper nonprojective formulation of the theorem is a harmless
generalization, handled explicitly by a projective modification.

Thus the proof supplies the analytic and characteristic-zero algebraic
generator once the source's actual proper semiabelian model,
coefficient action, original line, period lattice and level
identifications are given. It does not infer existence of those
objects from the theorem names in the table. Integral vertical
norm constancy, the supplied CM points and the arithmetic
moduli construction are still separate.

### Primary classical inputs

* J.-P. Serre, *Géométrie algébrique et géométrie analytique*,
  Annales de l'Institut Fourier **6** (1956), 1–42,
  §12, Theorems 1–2, pp.19–20:
  [primary article](https://numdam.org/articles/10.5802/aif.59/).
  Only projective GAGA is used after passing to \(Z\).
* J. Włodarczyk, *Simple Hironaka resolution in characteristic zero*,
  Journal of the American Mathematical Society **18** (2005),
  779–822, Theorems 1.0.1 and 1.0.3, pp.781–782:
  [author's primary PDF](https://www.math.purdue.edu/~wlodarcz/singularities/Resolution.pdf).
* Chow's lemma is the already pinned Stacks Project, Tag 0200,
  coherent.tex 4922–4940 at
  a04446e57ec1fbc252a871afcec7752fb2807b14.

The period, metric and boundary arguments above are proved here,
rather than taken from a general canonical-extension theorem.
The verification certificate authenticates source bytes and exact
finite identities; independent mathematical review has separate
scope. No Lean kernel replay is asserted.

## 8. Assembling the local norms without an extra constancy hypothesis

The new generator can be combined with the proved finite-place
rigidity. The following implication makes the remaining arithmetic
construction requirements explicit.

Suppose the same data extend to a normal integral proper flat
model \(\mathcal Y/\mathcal O_K\), with nonempty connected special
fibres. Suppose its prescribed integral conjugate determinant is
an invertible sheaf \(\mathcal M_\tau\), restricting to (1), and
its pullback at an integral point is the determinant of the
**same** integral eigenlattices used for the Hodge norms.
Suppose that, on every proper integral curve in a special fibre,
the actual two Hodge filtrations, coefficient freeness and
determinant identification supplied in the earlier propositions
apply to this line. In particular the determinant-torsion
proposition makes its degree zero on that curve. The exact
same-line identification at ramified coefficient primes is part
of this hypothesis; freeness of an unrelated bundle does not
suffice.

Let \(s\) be the algebraic generic generator just constructed.
At each finite place \(v\), vertical-line rigidity gives
integers \(M_v>0,a_v\) such that
\[
                s^{\otimes M_v}/\pi_v^{a_v}
\]
generates \(\mathcal M_\tau^{\otimes M_v}\) on the entire
localized model. Hence every integral point, including one
defined over a finite ramified extension, has
\[
           \log\|s\|_v
               =(a_v/M_v)\log|\pi_v|_v.                \tag{14}
\]
This is independent of the point. The right side is zero for
all but finitely many \(v\), since the divisor of a rational
section on this noetherian arithmetic model has finitely many
components. The complex norms are constant by the theorem.
Thus these are an adelic family of point-independent norms on
the prescribed line.

Retain the other arithmetic and metric hypotheses of the CM
calculation. Suppose its construction, for every required finite
place, gives an integral point on this **same component** of
\(\mathcal Y\), and its pulled-back original line and tangent
lattice are the product-isogeny model already proved in the
CM calculation. Formula (14) proves the equality between the
prescribed finite norm at the original point and its CM value.
The constant complex norms give the analogous equality there.
Therefore the retained local-norm comparison hypothesis of
the CM calculation is a conclusion of these geometric data,
and that calculation gives
\[
          \widehat{\deg}_{\mathrm n}\mathcal M_\tau|_x
                             =\frac{p-q}{2}P_E
\]
at any supplied point \(x\) with the same lattice conventions.

The remaining inputs are now the actual arithmetic model,
its curvewise determinant identifications, and the integral
CM maps to its selected component. A good abelian CM model and
a generic level point alone do not assert these identifications.
