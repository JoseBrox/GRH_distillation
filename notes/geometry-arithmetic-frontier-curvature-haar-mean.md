# The original geometric mean and arithmetic Haar measure

## Result and scope

The local Hodge determinant metric gives the invariant volume form on
the original matrix domain. Summing its density over the original
geometric sheets gives a probability measure whose component measures
are normalized arithmetic Haar measures, with explicitly retained
sheet multiplicities and component volumes.

The denominator in the original definition is already the integral
of this **same analytic density** against the constant function one.
Thus no separate comparison with an algebraic degree, and no boundary
intersection theorem, is needed to normalize this mean. This closes
the measure-comparison supplier once the original complex
uniformization and its Hodge metric have been identified.

The geometric input is explicit: the source's finite collection of
arithmetic components, fundamental sets, local sheets and local Hodge
potential comparison, recorded by its `Pieces` structure. We do not
construct that structure or infer it from an abstract probability
contract. The actual arithmetic model, global family, original
lattice/metric identification and signed boundary limit remain
separate. No whole node is completed: RH \(6/9\), GRH \(17/31\).

The existing manuscripts contain the preceding abstract Haar scaling
argument and arithmetic integrability theorem, but a bounded search
of their mathematical sections found no existing proof of this
original determinant-density and finite-sheet normalization step.

## 1. The determinant metric and its exact density

For integers \(p,q\ge0\), let
\[
 \mathcal D_{p,q}
 =\{Z\in M_{p,q}(\mathbf C):I_q-Z^*Z>0\},
 \qquad
 \Phi(Z)=-\log\det(I_q-Z^*Z).
 \tag{1}
\]
If one of \(p,q\) is zero, this is a point and \(\Phi=0\).
For a product of these domains put
\[
 n=\sum_\sigma p_\sigma q_\sigma,\qquad
 \Phi=\sum_\sigma\Phi_\sigma,\qquad
 b(Z)=\prod_\sigma
       \det(I-Z_\sigma^*Z_\sigma)^{-(p_\sigma+q_\sigma)}.
 \tag{2}
\]
The source has \(p_\sigma=j\), \(q_\sigma=j'\) for every factor,
so \(n=fjj'\) and \(b=\exp(N\Phi)\), where \(N=j+j'\).

Here is the direct metric calculation. Write a positive \(p\)-plane
in the Hermitian space with form \(\operatorname{diag}(I_p,-I_q)\)
as the graph of \(W\in M_{q,p}(\mathbf C)\). Give the ambient
space its positive Hodge metric: \(h\) on this plane and \(-h\)
on its orthogonal complement. In the quotient frame represented by
the last \(q\) coordinate vectors, the quotient metric has Gram matrix
\[
                         (I_q-WW^*)^{-1}.                 \tag{3}
\]
Indeed, the orthogonal representative of a quotient vector \(y\)
has the form \((W^*u,u)\), where \(u=(I_q-WW^*)^{-1}y\).
Its positive squared norm is \(y^*(I_q-WW^*)^{-1}y\).
Therefore the determinant quotient norm is
\(\det(I_q-WW^*)^{-1/2}\). Replacing \(W\) by the transpose
coordinate \(Z=W^t\) gives the same real determinant in (1).
A nonvanishing holomorphic change of determinant frame adds
the real part of a holomorphic function to its logarithm.
This proves the local potential form
\[
                          \varphi=\Phi/2+\Re H.             \tag{4}
\]
Any fixed positive factor in the Hodge metric only changes the
constant in the potential. The actual identification with the
original quotient Hodge metric is required; an arbitrary smooth
Hermitian metric would not suffice.

For a tangent matrix \(T\), differentiation gives
\[
 (\partial\bar\partial\Phi)_Z(T,\bar T)
 =\operatorname{tr}\bigl((I_p-ZZ^*)^{-1}
                T(I_q-Z^*Z)^{-1}T^*\bigr).                 \tag{5}
\]
Thus its complex Hessian is, up to ordering and transpose of
coordinates, the tensor product of the two displayed positive
matrices. The determinant is
\[
 \det(\Phi_{a\bar b})
 =\det(I_p-ZZ^*)^{-q}\det(I_q-Z^*Z)^{-p}
 =\det(I_q-Z^*Z)^{-(p+q)}.                                 \tag{6}
\]
The last equality is the determinant identity
\(\det(I_p-ZZ^*)=\det(I_q-Z^*Z)\). For the product domain,
the Hessian is block diagonal. Equation (4) has zero extra Levi
form, and division by two contributes \(2^{-n}\). Consequently
\[
 \det(\varphi_{a\bar b})=2^{-n}b,\qquad
 (dd^c\varphi)^n=\frac{n!}{\pi^n}b\,dV,
 \quad dd^c=\frac{i}{\pi}\partial\bar\partial.               \tag{7}
\]
This convention agrees exactly with the source: its repeated-potential
density is \(n!(2/\pi)^n\det(\varphi_{a\bar b})\).
In dimension zero, the empty determinant and \(0!\) are one,
so (7) remains valid. Definite factors contribute a point and a
factor one; signatures need not be equal for (2)--(7).

## 2. This density is the homogeneous Haar density

The unitary group acts transitively on the domain, with compact
stabilizer. In the negative-plane coordinates, a block unitary matrix
acts by
\[
 Z\longmapsto(AZ+B)(CZ+D)^{-1}.
\]
Preservation of the indefinite Hermitian form gives
\[
 I-Z'^*Z'=(CZ+D)^{-*}(I-Z^*Z)(CZ+D)^{-1}.                  \tag{8}
\]
The potential changes by \(2\log|\det(CZ+D)|\), which is locally
pluriharmonic. Therefore the positive form in (7), and hence
\(b\,dV\), is invariant. The positive-plane coordinates used in
(3) give the equivalent formula after transposition and the
corresponding interchange of block coordinates.

Let \(\pi:G\to\mathcal D=G/K\) be the original orbit map, with
\(K\) compact, and choose Haar measure \(dg\). Since \(\pi\)
is proper, its pushforward is a locally finite invariant measure.
Uniqueness of such a measure on a transitive homogeneous space gives
\[
                         \pi_*dg=c\,b\,dV,\qquad 0<c<\infty.
 \tag{9}
\]
This is also precisely the original `GroupDict` conclusion: its
orbit map has compact majorant stabilizer and its holomorphic action
changes the potential by a pluriharmonic function. No absolute
Haar normalization is assigned a value.

### Generic stabilizers cannot be dropped between components

Let \(\Gamma\) be the original arithmetic subgroup, and let
\(s\) be the order of its kernel on \(\mathcal D\). This kernel
is finite, being a discrete subgroup of the compact action kernel.
Away from a null set it is the entire point stabilizer: for each
element acting nontrivially on the connected complex domain, its
fixed locus is a proper analytic subset; there are only countably
many elements. This argument includes compact, zero-dimensional
factors. If the whole domain is a point, \(s=|\Gamma|\).

For a measurable fundamental set \(\mathcal F\subset\mathcal D\),
put
\[
                V_{\mathcal F}=\int_{\mathcal F}b\,dV.
 \tag{10}
\]
Give \(\Gamma\backslash G\) the quotient measure associated to
counting measure on \(\Gamma\). Small quotient charts outside the
exceptional fixed loci have fibre measure \(1/s\) times the
fibre measure in (9). Thus
\[
 \operatorname{vol}(\Gamma\backslash G)
      =\frac{c}{s}V_{\mathcal F},\qquad
 \pi_*\nu_\Gamma=\frac{\mathbf1_{\mathcal F}b\,dV}{V_{\mathcal F}}
 \quad\hbox{on the quotient}.                              \tag{11}
\]
Here \(\nu_\Gamma\) is normalized Haar probability. The preceding
arithmetic theorem gives finite positive quotient volume, hence
\(0<V_{\mathcal F}<\infty\). The normalized identity is unaffected
by \(c\) or \(s\), but **relative component weights** involve
\(V_{\mathcal F}=(s/c)\operatorname{vol}(\Gamma\backslash G)\).
Replacing it by a raw covolume without these factors is unjustified.

## 3. Sum the original sheets and normalize once

Retain the exact geometric sheet data. There are finitely many
arithmetic components \(k\), each with a fundamental set
\(\mathcal F_k\) in a domain of the same complex dimension \(n\),
and measurable sets \(B_m\subset\mathcal F_{k(m)}\) with holomorphic
local sheets \(\gamma_m\). Their images are disjoint in the original
projective variety and cover its interior up to a null set in its
smooth local charts. Their multiplicities satisfy
\[
 \sum_{m:k(m)=k}\mathbf1_{B_m}(t)=d_k
 \quad\hbox{for almost every }t\in\mathcal F_k,
 \qquad d_k\in\mathbf Z_{\ge0},\quad \sum_k d_k>0.           \tag{12}
\]
On each sheet the **original** potential satisfies (4), with the
corresponding domain potential. These are the source `Pieces`
fields, not newly inferred geometric existence statements.

Let \(g\) be a function on the projective variety: its homogeneous
coordinate representative is invariant under the coordinate torus.
Let \(I(g)\) denote the source's analytic integral against the
repeated original Hodge potential. Change of holomorphic coordinates
and (7) give
\[
 I(g)=c_n\sum_m\int_{B_m}g(\gamma_m(t))\,b_{k(m)}(t)\,dV(t),
 \qquad c_n=n!/\pi^n.                                    \tag{13}
\]
To justify this for the actual projection definition of the source
integral, discard the branch and exceptional analytic loci. The
chosen finite linear projection gives finitely many holomorphic
inverse sheets there; the Hessian determinant transforms by the
squared absolute complex Jacobian, exactly the real change-of-variable
factor. Both these projection sheets and the \(\gamma_m\) cover the
same smooth points with the specified multiplicities. Refining their
overlap partitions proves (13). Their null complements do not change
the integral. The source's `IsSheetCover.cover` records the needed
null-set condition in every original chart.

Use nonnegative measures and Tonelli first. For the original
real-valued integral, assert (13) only when the right hand side is
absolutely integrable. The formula for \(g=1\), (12) and (11) give
\[
 I(1)=c_n\sum_k d_kV_k\in(0,\infty),\qquad
                  V_k=\int_{\mathcal F_k}b_k\,dV.          \tag{14}
\]
For \(d_k>0\), define the average of the sheet values by
\[
 \bar g_k(t)=\frac1{d_k}
     \sum_{m:k(m)=k}\mathbf1_{B_m}(t)\,g(\gamma_m(t)).
 \tag{15}
\]
This is a finite sum almost everywhere by (12). Discard components
with \(d_k=0\), whose sheet sets are null. Absolute integrability
means integrability of the analogous average of \(|g|\); it is
not inferred from possible cancellation in \(\bar g_k\).
For example, two sheet values \(1/t,-1/t\) on \(0<t<1\) have
zero average, but their average absolute value has divergent integral.
Equations (13)--(15) yield the exact normalized mean
\[
 \boxed{\quad
 \frac{I(g)}{I(1)}
 =\sum_{k:d_k>0}w_k\int_{\Gamma_k\backslash G_k/K_k}
                       \bar g_k\,d\nu_k,\qquad
 w_k=\frac{d_kV_k}{\sum_\ell d_\ell V_\ell}.
 \quad}                                                  \tag{16}
\]
The probability measure on the original variety is equivalently
obtained by pushing forward the sheet measures in (13) and dividing
by (14). Thus (16) applies to every integrable function on the
original variety, not only functions constant on the finite fibres.
When \(g\) is a lattice invariant, such as the original shortest
length or full isotropic vector count, the prescribed fibre
identifications give a common value on these sheet fibres.
Then \(\bar g_k\) is that original lattice function.

The source defines
\[
 \begin{split}
  \varphi_\mu&=\log(h_\mu),\\
  \deg_\mu&=\operatorname{geomDeg}(P,\mu,n)
            =\operatorname{ptsIntegral}(P,(\log h_\mu)^n,1),\\
  \operatorname{mean}_X(g)
       &=\operatorname{ptsIntegral}(P,\varphi_\mu^n,g)/\deg_\mu.
 \end{split}                                             \tag{17}
\]
Thus its denominator is **exactly \(I(1)\)**. The same scalar
\(c_n\) occurs in both integrals, and cancels. No replacement of
an algebraic intersection number by an analytic volume occurs.

## 4. Consequences and the remaining geometric frontier

Apply the full isotropic-count integrability theorem separately to
the finite arithmetic components. The lattice isomorphism and
norm comparison in the original group dictionary identify the
original count on every sheet. The fixed positive norm factor
\(\kappa\) merely rescales the radius. Hence its component means
are finite and scale by \(t^{2f(N-1)}\). The weights in (16)
are finite, positive and independent of the radius, so the same
integrability and homogeneity hold for the original geometric mean.
The earlier packing-to-mean proof then supplies the original
logarithmic cusp bound with \(C_u=3\).

The consumers used here are the nonnegative full isotropic counts,
the nonnegative function \(\log^+(r/\lambda)\), and the original
nonnegative cusp weight \(U\). Their integrability follows in that
order from arithmetic unfolding, the counting-to-logarithmic-mean
argument and the pointwise cusp bound. There is no cancellation
between sheets for these functions. The source probability contract
also explicitly requires integrability of a general test function.
We make no equality assertion for its totalized real integral on
a function not absolutely integrable for the geometric sheet measure.

No new analytic hypothesis was introduced: the preceding arithmetic
theorem supplies convergence, and the original Hodge determinant
metric supplies the positive invariant density. What is still
required is the actual geometric construction and its sheet/metric
identifications, including the original finite-level data. A
`FullerData` record by itself does not provide these: its metric
and period fields are not forced to be the same geometric model.

The integral considered here is the source's ordinary interior
Hessian density, with its chart-null complement. This result does
not identify a boundary Monge--Ampère current, prove an arithmetic
intersection limit, or remove the signed boundary requirement.
Those are separate assertions even though the interior mean is
now normalized exactly.

## 5. Pinned source and verification record

All paths refer to
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The associated checker records byte hashes and bounded excerpt hashes.

| Source module suffix | Lines | Exact role |
|---|---:|---|
| `GroundTheory...HodgeLowerBound.FrameDefinitions.IsFrameOverLine` | 60–99 | Original determinant quotient metric; `phMu=log(muLine.h)` by definition. |
| `GroundTheory...HodgeLowerBound.FrameDefinitions.Weights` | 136–143 | `degMu` and original mean. |
| `ReciprocityTheory...BirationalGeometry.ArithmeticHilbertSamuelLowerBound` | 73–74 | `geomDeg` is the same analytic integral against one. |
| `ReciprocityTheory...BirationalGeometry.IsSemipositiveOn` | 206–219 | Complex Hessian and exact \(n!(2/\pi)^n\) density convention. |
| `ReciprocityTheory...BirationalGeometry.IsIntersectionFamily` | 116–145 | Finite projection, local inverse sheets, and original analytic integral. |
| `Development...Definitions.MetricPeriods.IsFundSet` | 15–24, 49–78 | Matrix domain, potential, density, actual period family, finite-index arithmetic subgroup and fundamental set. |
| `Development...Definitions.MetricPeriods.GroupDict` | 14–43 | Actual lattice, norm factor, group isomorphism, compact orbit fibres and potential cocycle. |
| `Development...Definitions.GlobalGeometry.IsSheetCover` | 20–28, 38–73 | Original sheets, null complements, finite multiplicities, fibre and potential identifications. |
| `Development...Proofs.MetricProofs.MongeAmpereDensityOfBallPotential` | 337–385 | Source determinant formula and exact common scalar; independently derived in (5)–(7). |
| `Development...Proofs.MetricProofs.HaarPushforwardEqBallDensity` | 394–464 | Original Haar pushforward target; independently derived in (8)–(9). |
| `Development...Proofs.MetricProofs.SheetCoverOfArithmeticVarietyStatement` | 11–12 | Exact source change-of-sheets contract and its absolute-integrability conditions. |

The manuscript fragment states the mathematics without these source
identifiers. The checker authenticates the source and checks exact
matrix determinant, mixed-density normalization, finite-sheet and
stabilizer-weight identities. This is not a Lean build, and the
finite algebra checks do not certify the existence of the original
uniformization or arithmetic family.
