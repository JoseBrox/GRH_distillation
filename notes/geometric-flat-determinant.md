# The exact determinant comparison on the prescribed lattices

## Result and scope

The local-to-global step in the conjugate-eigenspace comparison has a
short proof with determinant lines and the product formula. It needs no
integral Fourier projector, no estimate for a splitting index, and no
extra loss at ramified coefficient primes. The **actual flat line and its
CM period evaluation remain hypotheses** of this reconstruction. They
have a proof route in the pinned development; this note does not claim
an independent reconstruction of their existence or of that entire route.

The exact conclusion, before the source takes absolute values, is

\[
 \widehat{\deg}_{\rm n}W-\widehat{\deg}_{\rm n}W'
       =\frac{\operatorname{rk}W-\operatorname{rk}W'}2\,P_E,
 \qquad
 P_E=\gamma+\log(2\pi)-\log\operatorname{rd}(E)
                         -\frac{L'(1,\chi_{-d})}{L(1,\chi_{-d})}.
 \tag{1}
\]

Here the eigensublattices, their Hodge metrics, the semistable model,
the CM host and the quadratic character are the prescribed ones. The
signature is constant on the two halves of the chosen CM type.
The source host conditions, including the finite unramifiedness of
\(E/E^+\), are retained. This is **not** an application with the ramified
quadratic host \(\mathbf Q(\sqrt{-d})\).

Consequently the signed sum needed by the tangent argument is exactly
\((2R-n)P_E/2\), where \(R\) is the selected rank and \(n\) the total
abelian rank. It is not necessary to bound each difference separately
by the sum of its ranks. The correction and all signs are proved below.
Neither W10 nor either endpoint node is completed: RH remains 6/9 and
Dirichlet GRH 17/31.

## 1. Integral eigenlattices commute with flat extension

Let \(K\) be a number field, \(V\) a finite projective
\(\mathcal O_K\)-module with an action of \(\mathcal O_E\), and
\(\tau:\mathcal O_E\to\mathcal O_K\) an embedding. Define

\[
 W_\tau=\{v\in V:av=\tau(a)v\text{ for every }a\in\mathcal O_E\}.
\]

Choose an integral basis \(a_1,\ldots,a_s\) of \(\mathcal O_E\).
Then \(W_\tau\) is the kernel of the single map
\(V\to V^s\), \(v\mapsto((a_i-\tau(a_i))v)_i\).
Every torsion-free extension algebra over the Dedekind domain
\(\mathcal O_K\) is flat. Tensoring the kernel sequence therefore
identifies the extended eigenlattice with the kernel of these same
equations over the extension algebra. This applies to a number-field
extension and to localization at any finite prime, including a ramified
prime. The eigenlattice is saturated, since its quotient embeds into
the torsion-free module \(V^s\).

This proves the required integral base-change fact directly. Dividing
by a discriminant, group order or eigenvalue difference is unnecessary.
For a smooth group scheme, the Lie module itself commutes with base
change. Thus the argument applies to the actual Cartesian model maps,
with the action and Hodge metric transported by those maps. It does not
permit replacement by an unrelated isogenous variety or integral model.

## 2. A determinant-line comparison

Give \(V\) Hermitian metrics at its complex embeddings. Let
\(W,W'\) be two eigenlattices of ranks \(a,b\), with inherited
metrics, and put
\(\mathcal D=\det W\otimes(\det W')^{-1}\).
At a finite place use the norm whose unit ball is the local determinant
lattice. The degree convention is

\[
 \widehat{\deg}_{\rm n}\mathcal D
       =-\frac1{[K:\mathbf Q]}
          \left(\sum_\sigma\log\|s\|_\sigma
               +\sum_p\sum_{j:K\hookrightarrow\mathbf C_p}
                                      \log\|s\|_j\right),
 \tag{2}
\]

for any nonzero rational section \(s\); complex conjugate embeddings
are counted separately and \(|p|_p=p^{-1}\). The product formula
makes (2) independent of \(s\).

After one common finite extension if necessary, suppose a family supplies
a scalar \(\varphi(x,y)\in K^\times\) for any pair of rational
eigenframes \(x,y\). Require that its values commute with field
embeddings and field extension: all local values below come from this
one algebraic scalar. Assume the transformation rule

\[
 \varphi(Ax,By)=\varphi(x,y)\frac{\det B}{\det A}.
 \tag{3}
\]

Assume its archimedean logarithmic norm is computed with the prescribed
Hodge Gram matrices, and that at each finite place its logarithmic norm
is the logarithm of \(|\varphi|\) on integral local eigenframes of the
same model. These are exactly the two local norm requirements of the
flat-family supplier. Then its adelic degree equals
\(\widehat{\deg}_{\rm n}W-\widehat{\deg}_{\rm n}W'\).

**Proof.** The expression
\(s=\varphi(x,y)(\bigwedge x)\otimes(\bigwedge y)^{-1}\)
is independent of the frames by (3). At an infinite place,

\[
 \log\|s\|_\sigma=\log|\sigma\varphi(x,y)|
          +\frac12\log\det\operatorname{Gram}_\sigma(x)
          -\frac12\log\det\operatorname{Gram}_\sigma(y).
 \tag{4}
\]

At a finite place take integral bases \(x_0,y_0\) of the actual
eigenlattices and write \(x=Ax_0,y=By_0\). Their determinant unit
norms and (3) give

\[
 \log\|s\|_j=\log|j\varphi(x,y)|+
                          \log|j\det A|-\log|j\det B|
               =\log|j\varphi(x_0,y_0)|.                 \tag{5}
\]

The equality of the local norms identifies the supplied adelic line
with \(\mathcal D\). Add (4) and (5), use (2), and cancel the
algebraic scalar by the product formula. A common finite extension
does not change normalized degree: every embedding occurs with the
extension multiplicity. Section 1 identifies the integral eigenlattices
after that extension. Ranks zero use \(\det(0)=\mathcal O_K\) and
determinant one, so the proof covers them too. \(\square\)

The potential integral splitting index of \(W\oplus W'\) in \(V\)
does not enter this **difference** of determinant degrees. It does enter
their sum and is retained, with its favourable sign, in Section 4.

## 3. The different/conductor correction cancels exactly

Write \(\mathfrak D_E\) for the different of \(E/\mathbf Q\).
If \(K\) contains the chosen image of \(E\), the normalized finite
sum is

\[
 \frac1{[K:\mathbf Q]}
  \sum_p\sum_{j:K\hookrightarrow\mathbf C_p}
       \bigl(\log|j\mathfrak D_E|-\log|d|_p\bigr)
           =\log d-\log\operatorname{rd}(E).             \tag{6}
\]

For an ideal the notation means the logarithm of the norm of a local
generator. Indeed its finite sum is minus the logarithm of the ideal
norm, and \(N_{E/\mathbf Q}\mathfrak D_E=|\operatorname{disc}E|\).
The second sum is \(-[K:\mathbf Q]\log d\) by the product formula.
Both have finite support, and the count of embeddings proves (6).

The CM evaluation of the corrected flat norms supplies the value

\[
 \frac{a-b}{2}P_E+b\bigl(\log d-\log\operatorname{rd}(E)\bigr).
 \tag{7}
\]

The actual integral-frame logarithmic norms add
\(b(\log|j\mathfrak D_E|-\log|d|_p)\) at finite places, keeping
the infinite norms unchanged. By the minus sign in (2), their degree is
(7) **minus** \(b(\log d-\log\operatorname{rd}(E))\).
Thus their degree is exactly \((a-b)P_E/2\), and Section 2 proves
(1). The finite correction is accounted for by equality; it is neither
dropped nor charged again as an absolute error.

This part reconstructs the correction and determinant calculation.
The existence of the flat generator with the required local norms and
the initial CM evaluation (7) are still the geometric inputs. The
source proves them through its flat-family and CM-period arguments;
this note checks the displayed contracts and their bounded consumers,
not their entire ancestry and not a Lean kernel replay.

## 4. Only the signature imbalance enters the selected sum

Retain the notation of [the selected-degree argument](selected-eigenspace-degree.md):
\(X=\sum\widehat{\deg}_{\rm n}W_\tau\),
\(Y=\sum\widehat{\deg}_{\rm n}W'_\tau\),
\(T=\sum\widehat{\deg}_{\rm n}V_\tau\),
\(\delta=d_V-X-Y\ge0\), and \(\nu=X-T\ge0\).
Here \(d_V\) denotes the total degree, not the conductor. Retain also
the tangent-slope hypothesis
\[
 T\le12R\log\bigl(2+n+(-d_V)_+\bigr).                    \tag{8a}
\]
The earlier theta argument supplies (8a) for the prescribed principally
polarized semistable tangent lattices under its stated hypotheses; it
is not a conclusion for arbitrary Hermitian lattices.
Sum (1), with the actual selected orientation in each pair. If the
same period parameter applies to all pairs, then

\[
 X-Y=\frac{2R-n}{2}P_E,
 \qquad
 T\le12R\log\left(2+n+
                 \left(\frac{2R-n}{2}P_E-\delta-2\nu\right)_+\right).
 \tag{8}
\]

The second inequality is the already proved tangent-slope bound and
the two-case signed-degree argument, now with the **exact** input.
In particular it can be weakened to

\[
 T\le12R\log\left(2+n+
                       \frac{|2R-n|}{2}|P_E|\right).       \tag{9}
\]

For constant signature \((p,q)\), removing \(r\) toric directions
from both halves and selecting the half of size \(m\in\{p,q\}\)
gives \(R=f(m-r)\), \(n=f(p+q-2r)\). Consequently
\(2R-n=f(2m-p-q)\): the signed period cost is independent of the
toric rank. When the selected half is smaller and \(P_E\ge0\),
the positive-part period cost in (8) vanishes. Equal signatures also
make it vanish. Neither favorable case is asserted for the whole
existing growing family without checking its actual parameters.

## 5. Bounded source evidence and remaining work

All source files are pinned to
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

| Module | Inspected lines | Role |
|---|---:|---|
| `Definitions.GlobalGeometry.IsConstMul` | 30–43, 59–82 | Frame covariance, actual archimedean and integral-frame norms, correction |
| `PlurisubharmonicCones.ExistsSmulMemSpan` | 93–152, 154–178, 188–261 | Same Hodge Gram matrices and same local eigenframes, including finite primes |
| `PlurisubharmonicCones.ExistsCoordLattice` | 346–409, 418–448 | Determinant norms give actual degrees; product-formula comparison |
| `GeometryStatements.FlatDegree` | 12–19 | Corrected CM-degree supplier, including the additional finite term |
| `GeometryProofs.KroneckerCharacterPeriodFormula` | 16–45, 47–102, 104–146 | Exact different/conductor subtraction |
| `GeometryProofs.PhiDegFibLatLeOfIsOFamilyOfIsAdapted` | 20–71, 73–124, 126–153 | Actual flat line, exact equality before its final absolute-value bound |
| `GeometryProofs.AbelianPartLieSignature` | 18–28 | The common shift from \((p,q)\) to \((p-r,q-r)\) |
| `GeometryProofs.FlatDegreeHolds` | 60–118 | Upstream proof route for the corrected CM evaluation |

The [CM product and period calculation](cm-product-period-calculation.md)
and [boundary extension and local-norm assembly](flat-family-boundary-extension.md)
now supply the flat-family/CM evaluation under explicit model hypotheses.
The next geometric work is to identify the actual arithmetic model,
its integral determinant line at ramified primes, and integral CM maps
to the same component carrying the prescribed lattices. The regularized
height identity, signed cusp mean, and finite section-degree estimate
remain. The determinant bridge above need not be reopened as an
unspecified extra comparison.
The certificate records exact source and excerpt hashes and finite
algebra checks; it makes no broader proof-completion claim.
