# The selected eigenspace sum: signed degrees, exact ranks and the theta input

## Status

The scalar part of the actual point-height argument admits a direct
two-case proof. It needs no implicit logarithmic absorption or repeated
maximum-slope argument. Moreover, the arithmetic cost is proportional
to the **abelian rank remaining after the toric part is removed**.
Integral splitting and image indices improve the estimate, with the
sign displayed below.

These are proved reductions for the same Hermitian lattices. They do
not yet prove the arithmetic estimate on the actual nonzero abelian
eigenspaces. The source's claimed logarithmic slope supplier is traced
to integral torsion translates of theta sections and a jet determinant;
the decisive geometric inputs are being separated from the elementary
determinant argument. W10 remains open.

## 1. The scalar step requires only two cases

All degrees in this note are ordinary Arakelov degrees divided by the
degree of the number field. Let \(\bar V\) have rank \(n\), degree
\(d\), and pairwise orthogonal, generically complementary integral
eigensublattices \(W_\tau,W'_\tau\), indexed by a finite set.
Let \(V_\tau\subset W_\tau\) have the same generic fibre, with all
metrics inherited from \(\bar V\). Write
\[
 X=\sum_\tau\widehat{\deg}_{\rm n}W_\tau,\qquad
 Y=\sum_\tau\widehat{\deg}_{\rm n}W'_\tau,\qquad
 T=\sum_\tau\widehat{\deg}_{\rm n}V_\tau,\qquad
 R=\sum_\tau\operatorname{rk}V_\tau .
\]
Put
\[
 \delta=d-X-Y,\qquad \nu=X-T,\qquad b=X-Y.
 \tag{1.1}
\]
The direct sum of the eigensublattices has finite index in \(\bar V\),
and each \(V_\tau\) has finite index in \(W_\tau\). Thus
\[
 \delta,\nu\ge0,\qquad d=2T-b+\delta+2\nu.
 \tag{1.2}
\]
For example,
\(\delta=[K:\mathbf Q]^{-1}\log
\#(V/\bigoplus_\tau(W_\tau\oplus W'_\tau))\).
There is no archimedean correction in this expression: the summands
are orthogonal and carry the inherited metrics.

**Proposition.** Suppose \(C_s\ge0\) and the actual selected sum satisfies
\[
 T\le R C_s\log(2+n+\max\{-d,0\}).
 \tag{1.3}
\]
Then, with \(z_+=\max\{z,0\}\),
\[
 \boxed{\quad
 T\le R C_s\log\!\left(2+n+(b-\delta-2\nu)_+\right).
 \quad}
 \tag{1.4}
\]
In particular one may replace \(b-\delta-2\nu\) by any upper bound
for it. The stronger hypothesis bounding the maximum slope of every
sublattice of \(\bar V\) is only one way to supply (1.3).

**Proof.** The right side is nonnegative. If \(T\le0\), the conclusion
is immediate. If \(T>0\), (1.2) gives
\[
 \max\{-d,0\}
   = (b-\delta-2\nu-2T)_+
   \le (b-\delta-2\nu)_+.
\]
Substitute into (1.3). This also covers \(C_s=0\) and \(R=0\);
in the geometric situation \(R=0\) means that all selected lattices
vanish. \(\square\)

There is no need to control the absolute value of each conjugate
degree difference in this step. Only the **signed total** \(b\)
occurs. Also, the two integral defects in (1.1) are favourable;
charging their absolute values would discard useful information.

**Uniform consequence.** Suppose \(\Lambda\ge1\), \(C_f\ge0\),
\[
 n\le G\le e^\Lambda,\qquad b\le C_fG\Lambda.
 \tag{1.5}
\]
Then
\[
 T\le C_s\{1+\log(3+C_f)\}R\Lambda.
 \tag{1.6}
\]
Indeed \(2+n+(b-\delta-2\nu)_+
\le e^\Lambda(3+C_f\Lambda)\). Concavity of the logarithm gives
\[
 \log(3+C_f\Lambda)
 \le \log(3+C_f)+\frac{C_f}{3+C_f}(\Lambda-1)
 \le \Lambda\log(3+C_f),
\]
because \(C_f/(3+C_f)\le1<\log(3+C_f)\).
This proves (1.6) with an explicit constant.

## 2. Application to the actual toric and abelian ranks

In the pinned construction, let \(f\) be the number of conjugate
pairs of embeddings, \(N=p+q\), and \(m\) the dimension of the
selected eigenspace before removing the toric part. Its adapted
family has \(r\) toric vectors and \(k\) abelian vectors, with
\[
 r+k=m.
 \tag{2.1}
\]
The source rank identity gives
\[
 \operatorname{rk}V_\tau=\operatorname{rk}W_\tau=k,\qquad
 R=fk=f(m-r).
 \tag{2.2}
\]
Here \(V_\tau\) is the actual image lattice used in the labelled
degree, while \(W_\tau\) is its saturation in the corresponding
abelian quotient eigenspace. One must not equate their degrees.
Their difference is exactly the nonnegative term \(\nu\) above.

The source supplies \(n\le fN\le e^\Lambda\). Its separate
conjugate-degree comparison implies \(b\le C_f fN\Lambda\);
bounding individual absolute values is sufficient but stronger
than needed. Conditional on the same selected slope estimate (1.3),
\[
 T\le C_A f(m-r)\Lambda,\qquad
 C_A=C_s\{1+\log(3+C_f)\}.
 \tag{2.3}
\]
Thus the purely toric selected case \(k=0\) needs no tangent-slope
or theta estimate at all: its selected degree sum is zero.

The already verified labelled-degree identity is
\[
 \Phi_B(P)\le fmX_B+T-fr\log\operatorname{rd}(E)
                    +\frac{fr}{2}\log(4\pi).
 \tag{2.4}
\]
Retaining (2.3) gives the more precise cost
\[
 \Phi_B(P)\le
 fmX_B+C_Af(m-r)\Lambda
 -fr\log\operatorname{rd}(E)+\frac{fr}{2}\log(4\pi).
 \tag{2.5}
\]
If \(X_B\le C_X\Lambda\), \(\log\operatorname{rd}(E)\ge0\) and
\(\log(4\pi)\le\Lambda\), then
\[
 \Phi_B(P)\le
 \{C_X+\max(C_A,\tfrac12)\}\,fm\Lambda.
 \tag{2.6}
\]
This follows from
\(C_A(m-r)+r/2\le m\max(C_A,1/2)\).
It improves the independent payment of a full abelian cost and a
full toric cost. All geometric identifications, regularizations and
signed cusp-limit hypotheses in the point-height argument remain.

## 3. The actual logarithmic-slope implementation

The inspected implementation does not substitute a classical
linear Faltings-height slope bound into the logarithmic interface.
Its chain is:

1. A primitive integral theta section is produced, after a number
   field extension, with mean logarithmic square-mean norm at most
   \(h_+/2+Cg\), where \(h_+=\max(-d,0)\).
2. For each positive integer \(m\), integral sections of
   \(L^{\otimes m^2}\) are obtained from torsion translates of that
   theta section. They span at each complex embedding and are
   asserted to have the same supremum bound as the original theta
   section; no power \(m^2\) is paid in that bound.
3. Integral directional jets through order \(m^2/3\), together with
   the product formula and a Gaussian Cauchy estimate, give a lower
   bound on the mean logarithmic norm of a nonzero integral tangent
   vector.
4. An absolute Siegel lemma converts this line estimate, after
   isometric field extension, into the maximum-slope bound.

The cancellation of the theta-section height against the number of
jets is the substantive mechanism. The integral torsion-translation
step, including bad reduction, cannot be replaced merely by the
complex translation identity or the matrix lemma for periods.

### Decisive pinned declarations inspected so far

All paths below are relative to the fixed source tree
jsmorph/rh at ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.
The source ledger and exact verification certificate accompany the
completed note.

| Declaration or module | Bounded ranges | Role |
|---|---:|---|
| MetricPeriods.IsAdapted | 30–65 | Actual image lattice, inherited quotient metric and adapted dimensions |
| AdaptedFamilyExistsOnEigenspaceStatement | 7–8 | Exact rank \(k\) after removing the toric part |
| PlurisubharmonicCones.ExistsSmulMemOfEig | 9–89 | Current abstract small-block proof |
| PlurisubharmonicCones.HeightComparisonGlobalModel | 150–238 | Same-data saturated eigenspaces, slope and conjugate-degree inputs |
| MetricProofs.AbelianPartHeightLinear | 201–212 | Orthogonal degree sum is at most total degree |
| SlopeBoundOfLineLargeDegree | 17–19 | Source supplier chain |
| SlopeBoundOfLargeDegreeLine | 94–143 | Absolute Siegel step and ordinary norm normalization |
| LineOfKeyDegree | 196–267, 269–375 | Jet determinant and parameter choice |
| ExistsThetaSectionsBounded | 210–245, 403–468 | Claimed integral torsion translates with uniform supremum bounds |
| IsThetaMeanSquareNorm | 98–131 | Exact meanings of height, norm, supremum bound and logarithmic line estimate |

## 4. Remaining work

The arithmetic supplier for \(k>0\) has not been closed here.
The next decisive check is the same-data integrality of the
torsion-translated theta sections, and the exact finite-place loss
if the claimed uniform statement needs an additional hypothesis.
The two-case scalar reduction and the exact-rank improvement do
not depend on resolving that question.
