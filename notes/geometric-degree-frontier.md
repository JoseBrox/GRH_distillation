# From mean volume directly to section degree

## Result and scope

The actual short-section construction supplies a lower degree bound for each
component lattice. Combining that lower bound with Hilbert–Samuel removes the
independent negative-height moment from the final degree argument. A single
weighted mean height suffices. In the source parameter range, the extra cost
has the required size: at most twice the source scalar error.

There is also an exact cancellation before estimating the mean height. The
component degrees occurring in the volume comparison cancel the degrees in
the Hilbert–Samuel weights. Equal component volumes then let the unweighted
mean-volume theorem supply the required weighted mean without an intermediate
change of weights.

Finally, a version using the raw Hilbert–Samuel inequality eliminates every
height from its surplus remainder. It retains signed constants and actual
rank ratios, and requires no upper rank-share estimate. Its remaining cost is
an explicit expression in those ranks and the section parameters. Bounding
that expression for the actual family is still necessary. An explicit
counterexample below shows why it cannot follow from the raw scalar contracts
alone.

All results below are ordinary mathematical deductions. The source comparisons
refer to jsmorph/rh at revision
ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de. The
[certificate](../certificates/geometric-degree-frontier.json) records verified
source bytes and bounded inspected passages. No Lean compilation or
independent verification of the deep geometric inputs is claimed.

## 1. The exact geometric weights cancel

Let a finite nonempty set of components have image degrees
\(\delta_Z>0\). Suppose the smaller weight has the same positive top degree
\(\delta_*\) on every component. Write
\[
 w_Z=B\delta_Z,\quad B>0,\quad W=\sum_Zw_Z,\quad
 N=\#\{Z\},\quad q=\frac{NB\delta_*}{W}.
\]
Suppose
\[
 \delta_*\le\delta_Z\le\frac{\delta_*}{1-\rho},
 \qquad 0\le\rho<1,
 \tag{1.1}
\]
and the exact component comparison is
\[
 \delta_*(s_Z+c)\le\delta_Z(h_Z+c+\gamma),
 \qquad c,\gamma\ge0.
 \tag{1.2}
\]
Then \(1-\rho\le q\le1\), and, with
\(\mathsf M=W^{-1}\sum_Zw_Zh_Z\) and
\(\bar s=N^{-1}\sum_Zs_Z\),
\[
 \boxed{\mathsf M\ge q\bar s-(1-q)c-\gamma.}
 \tag{1.3}
\]
Indeed, multiply (1.2) by \(B\), sum, and divide by \(W\).
In particular, if \(\bar s\ge-X\), \(X\ge0\), then
\[
 \mathsf M\ge-H_q,\qquad
 H_q=qX+(1-q)c+\gamma\le X+\rho c+\gamma.
 \tag{1.4}
\]
The proof does not assume a pointwise lower bound on \(h_Z\). The source's
proof of (1.2) does use its short generators; this distinction does not remove
those geometric hypotheses.

### Source applicability

The stronger comparison (1.2), before replacing its degree ratio by
\(1-\rho\), occurs in the proof of
*HodgeBundleWeights/HeightAddLogNonneg*, lines 47–55. For every
\(\varepsilon>0\), that proof gives
\[
 \delta'_Z(s_Z+c)
 \le\delta_Z(h_Z+c+\gamma+\varepsilon);
\]
letting \(\varepsilon\downarrow0\) gives (1.2). The cost is the source's
nonnegative multiplication cost plus its finite height-comparison cost.
All metrics, finite valuations and period factors are the prescribed ones.

The equality \(\delta'_Z=\delta_*\) is an actual source identity, not an
assumption that all image degrees are equal.
*ComponentImageDegreeBetweenOfProportionality*, lines 18–20, identifies all
top degrees from equal component volumes. The same proof, lines 15–26,
establishes (1.1). *CompactificationTopChernEqVolume*, lines 19–35, supplies
equal component volumes under its compactification and uniformization
hypotheses. The actual family uses these same two inputs in
*ThirdPlaceSeries/CoveringDegreeMultiplicative*, lines 43–55.

Thus (1.3) uses a geometric identity already available in the original
construction. The previous conversion through the weaker, degree-free
comparison paid two factors \(1-\rho\). Summing the degree comparison first
retains \(q\), and its coarse loss is \(\rho c\), rather than \(2\rho c\).
The genuine mean-volume theorem supplying \(\bar s\ge-X\) remains a deep input.

## 2. One mean height suffices when short sections span

Let \(E_Z\) be nonzero Hermitian lattices over the same number field, with
positive ranks \(r_Z\), normalized arithmetic degrees \(d_Z\), and weights
\(0<w_Z\le r_Z\). Put
\[
 \mathcal R=\sum_Zr_Z,\qquad \theta=W/\mathcal R\in(0,1].
\]
Suppose integral vectors of norm at most \(e^L\), at every embedding, span
each \(E_Z\) over the number field, where \(L\ge0\). Choosing a field basis
from these vectors and applying the determinant norm inequality gives
\[
 d_Z\ge-r_ZL.                                      \tag{2.1}
\]
The integral span of the selected basis has finite index in \(E_Z\);
that index increases the degree, so the sign in (2.1) is unchanged.
Arithmetic degree here is divided by the number-field degree and assigns
degree zero to the standard metric on its ring of integers.
The source defines this degree as rank times half its squared-norm slope:
*IsProbabilityMeasureMuPart*, lines 32–50 and 149–164. Thus (2.1)
corresponds to a squared-norm slope at least \(-2L\), with no additional
factor of two in the degree bound. The correction for the field
discriminant is already included in *StatementPl*, lines 64–65.

Assume also
\[
 d_Z\ge w_Z\{t h_Z-a|h_Z|-A\log(2+|h_Z|)-R_0\},
 \tag{2.2}
\]
where \(a,R_0\ge0\), \(A>0\), and \(t\ge a+1\). Set
\(\lambda=t-a-1\ge0\), \(b=t+a>0\), and \(K=\max(2,A)\).
Then, without any bound on the negative-height moment,
\[
 \frac{\sum_Zd_Z}{\mathcal R}
 \ge\lambda\theta\mathsf M
   -\frac{2a+1}{b}L
   -\theta R_0
   -\theta A\log\!\left(K+\frac{L}{b\theta}\right).
 \tag{2.3}
\]
Consequently, if \(\mathsf M\ge-H\), \(H\ge0\),
\[
 \boxed{\frac{\sum_Zd_Z}{\mathcal R}
 \ge-\lambda\theta H-\theta\{R_0+A\log\max(A,1)\}
      -2\log2-\frac{2a+2}{t+a}L.}
 \tag{2.4}
\]
The term \(2\log2\) can be omitted when \(A\ge2\).

**Proof.** For one component put \(P=r_ZL/w_Z\). If \(h=-y\le0\) and
\(0\le y\le P/b\), (2.2) gives
\[
 \frac d w\ge-\lambda y-\frac{b-\lambda}{b}P
                  -R_0-A\log(K+P/b).
\]
Here \((b-\lambda)y\le(b-\lambda)P/b\) and
\(\log(2+y)\le\log(K+P/b)\). If \(y\ge P/b\), the same bound follows
from \(d/w\ge-P\), since \(\lambda y\ge\lambda P/b\) and the two
subtracted terms are nonnegative.

If \(h\ge0\), maximizing \(A\log(2+h)-h\) over \(h\ge0\) gives
\[
 A\log(2+h)\le h+A\log\max(2,A).
\]
This again proves the same bound. Thus for every real \(h_Z\),
\[
 \frac{d_Z}{w_Z}\ge
 \lambda h_Z-\frac{2a+1}{b}\frac{r_ZL}{w_Z}
 -R_0-A\log\!\left(K+\frac{r_ZL}{bw_Z}\right).
\]
Summation and concavity of the logarithm prove (2.3).
Finally,
\[
 \theta A\log\!\left(K+\frac{L}{b\theta}\right)
 \le\theta A\log K+\frac Lb,
\]
because \(\log(1+u)\le u\) and \(A/K\le1\).
Also \(A\log K\le A\log\max(A,1)+2\log2\).
This proves (2.4), including \(L=0\) and \(\lambda=0\). No division by
either of those quantities occurs. \(\square\)

### The additional cost is controlled at the actual source scale

The source *ThirdPlaceSeries/ShortVectorWeightBound*, line 26, supplies
the spanning vectors for the **component section lattice itself**, at every
weight on its path, including the final untwisted weight. Their Petersson
norm is at most \(e^{P\kappa}\). Thus (2.1) holds with \(L=P\kappa\).
It is a lower degree bound, not an upper slope bound. The norm and degree
definitions are *IsProbabilityMeasureMuPart*, lines 790–822.

For the source dimension \(D\ge1\), put \(a=3(D+1)\). Its scalar conditions
give
\[
 z=7(D^2/t+D\rho),\qquad \rho\ge0,\qquad zL\le b_0.
\]
Therefore
\[
 \frac{2a+2}{t+a}L
 =\frac{6D+8}{t+3D+3}L
 \le14D^2\frac Lt\le2b_0.                  \tag{2.5}
\]
These are the same numerical conditions in
*ThirdPlaceSeries/SizesOfCoverStatement*, line 19; no upper rank-share
estimate is needed for (2.5).

If the existing upper rank-share supplier is retained, the source numerical
Hilbert–Samuel theorem can be applied **before the flat twist**: set its
twist cost to zero and its two degrees equal.
*DegBoundOfClaimNumbers*, line 9, then gives (2.2) with
\[
 A=26(26D^2+2zt)\ge676,\qquad R_0=4000b_0.
\]
*HilbertSamuelALogALe*, lines 5–9, gives \(A\log A\le6000b_0\).
Combining (1.3), (2.3)–(2.5), and a subsequent flat-twist inequality
\(d'_Z\ge d_Z-r_Zc_Z\), yields
\[
 \boxed{\frac{\sum_Zd'_Z}{\mathcal R}
 \ge\lambda\theta\{q\bar s-(1-q)c-\gamma\}
       -10002b_0-\frac{\sum_Zr_Zc_Z}{\mathcal R}.}
 \tag{2.6}
\]
The twist costs in (2.6) may be signed. The actual twist preserves the
component ranks; see *HilbertSamuelLowerBoundOfComponents*, lines 52–54
and 103–113. There is no need to charge it twice.

Formula (2.6) supplies the degree conclusion from a mean-volume input,
short generators and the existing Hilbert–Samuel estimate. It removes a
separate negative-height-moment obligation. It does not prove the
mean-volume theorem or remove the upper rank-share input used in that
particular uniform Hilbert–Samuel supplier.

## 3. Raw surplus: a height-free bound with signed constants

The following variant also removes the dependence on height inside the
actual excess-rank cost. Suppose (2.1) holds and, for each component,
\[
 d_Z\ge w_Z\{t h_Z-a|h_Z|-A_Z\log(b_Z+|h_Z|)-R_Z\},
 \tag{3.1}
\]
where \(A_Z>0\), \(b_Z\ge1\), and \(R_Z\) is any real number.
Choose \(0\le\lambda<t-a\), so \(s=t-a-\lambda>0\), and put
\[
 \beta=t+a,\quad
 P_Z=\left(\frac{r_ZL}{w_Z}-R_Z\right)_+,\quad
 K_Z=\max(b_Z,A_Z/s),
\]
\[
 \mathcal B_Z=
 R_Z+\left(1-\frac{\lambda}{\beta}\right)P_Z
      +A_Z\log(K_Z+P_Z/\beta).
 \tag{3.2}
\]
Then
\[
 \boxed{\sum_Zd_Z\ge
             \lambda\sum_Zw_Zh_Z-\sum_Zw_Z\mathcal B_Z.}
 \tag{3.3}
\]
Indeed, \(d_Z/w_Z+R_Z\ge-P_Z\). Apply the preceding negative-height
split at \(P_Z/\beta\) to this shifted degree. For \(h\ge0\), use
\[
 A_Z\log(b_Z+h)\le s h+A_Z\log\max(b_Z,A_Z/s).
\]
Since \(K_Z\ge1\), the logarithmic cost is nonnegative in the branch
using the degree floor. This proves (3.3). The signed constant \(R_Z\)
is retained, both explicitly and inside \(P_Z\).

### Exact raw Hilbert–Samuel dictionary

For the source raw inequality let \(C=26\), \(D,t\) be positive integers,
\(t>a=3(D+1)\), and all of
\(n_Z,\Lambda_Z,\beta_Z,\Lambda_{D,Z},\Lambda_{T,Z}\) be at least one.
Require \(\delta_Z>0\), \(B=\binom{t-1}{D}>0\), and positive component
rank. Set
\[
 w_Z=B\delta_Z,\quad e_Z=r_Z-w_Z\ge0,\quad
 \alpha_Z=e_Z/w_Z,\quad V_Z=CD^2+t\alpha_Z,
\]
\[
 b_Z=2+\log\Lambda_Z,\quad A_Z=CV_Z,\quad
 \ell_{0,Z}=\log\Lambda_Z+C\log(n_ZD\delta_Z),
\]
\[
 g_Z=(D+1)(\log n_Z+1)/2+1,
\]
\[
 \begin{aligned}
 R_Z={}&J_Z+CD^2\log t+(t+D+1)\log\beta_Z
       +(t+D^2)(g_Z+2)+V_Z\ell_{0,Z}\\
 &+\alpha_Z\{t(\log2+\tfrac12\log\beta_Z)
                       +\log\Lambda_{D,Z}+\log\Lambda_{T,Z}\}.
 \end{aligned}                                                   \tag{3.4}
\]
Then (3.1) is **exactly** the raw Hilbert–Samuel lower bound after
collecting terms. In particular,
\[
 \ell_Z=\ell_{0,Z}+C\log(b_Z+|h_Z|)
\]
is an equality; there is no replacement of this logarithm by a larger
height-dependent remainder.
All logarithmic arguments are positive. Positive rank is required before
multiplying the source slope statement by \(r_Z\); the raw predicate
alone must not be used to infer it.

The source constructs this raw inequality in
*ThirdPlaceSeries/ExistsDegreeParametersBound*, lines 34–43, without the
upper rank-share hypothesis. The raw statement is *HSClaim*, lines 7–22.
Combining (1.2), (3.3), and the flat twist gives the direct degree estimate
\[
 \boxed{\sum_Zd'_Z\ge
 \lambda B\delta_*\sum_Zs_Z
 -\lambda\{(W-NB\delta_*)c+W\gamma\}
 -\sum_Zw_Z\mathcal B_Z-\sum_Zr_Zc_Z.}
 \tag{3.5}
\]
No separate mean-height or negative-height assertion occurs in (3.5).
All heights have disappeared from its right side.
No componentwise upper rank bound was used. The explicit cost
\(\sum w_Z\mathcal B_Z\), rather than a mixed surplus–height moment,
is what remains to be estimated.

## 4. What the reduction does not supply

The raw contracts and short-vector degree floor cannot by themselves give a
small total surplus. Here is a concrete scalar obstruction.
Take one component, \(D=1\), an integer \(t\ge15\), \(\delta=1\),
\(w=t-1\), \(r=2w\), and \(h=s=c=\gamma=0\). Put
\[
 n=\Lambda=\beta=1,\quad J=0,\quad
 \Lambda_D=\Lambda_T=e^L,\quad d=-rL,\qquad L>0.
\]
The raw excess-rank fraction is \(1-w/r=1/2\).
Its surplus cost contains
\((r-w)(\log\Lambda_D+\log\Lambda_T)=2wL=rL\);
all the other subtracted terms are positive.
Hence the raw Hilbert–Samuel inequality and the degree floor both hold.
The mean height and mean-volume lower bound are zero, but \(d/r=-L\).
A rank-\(r\) diagonal Hermitian lattice with basis norms \(e^L\)
realizes that degree and floor.

Even the source-sized scalar relation need not prevent this example:
take \(z=7/t\) and \(b_0=zL\). Then \(zL=b_0\), while
\(L/b_0=t/7\) is unbounded. The example violates the upper rank-share
condition once \(t>14\), exactly where that missing condition matters.
It is an obstruction to the reduced scalar implication, not an example
of the actual automorphic geometry.

Thus a uniform or averaged rank/surplus estimate still carries mathematical
content. The new argument removes independent control of negative heights
and surplus–height correlations; it does not make arbitrary complementary
section degrees harmless.

## 5. Exact averaging, frontier and verification

Equations (2.3), (2.6), and (3.5) retain the actual rank fractions and signed
volume and twist contributions. They can be multiplied by nonnegative
outer weights and summed, or integrated over the scale parameter when
the quantities are measurable and the relevant integrals exist.
When the coefficients depend on scale, those coefficients remain inside
the integral. They must not be replaced by an unweighted mean.

In particular, a future analytic criterion allowing fixed logarithmic
averaging of the complete signed discrepancy can use these degree
inequalities before taking its positive part. This is a legitimate way
to preserve cancellations; no bound for that integrated geometric cost
has been proved here.

The remaining geometric frontier is now precise:

1. Supply the period-normalized mean-volume lower bound for the actual
   moving family, with its uniform order of quantifiers.
2. Apply the [finite jet bound](finite-section-jet-bound.md) to supply
   the upper rank comparison from the actual section realization,
   birational linear system, nef line-bundle inequalities and image-degree
   bound. It gives the smaller relative loss
   `D rho + (2D^2+4D)/t`, retaining the denominator in the excess rank.
   The arithmetic section-degree remainder in (2.6), or the explicit
   height-free signed cost in (3.5), still requires control.
3. Transport this same component degree through the existing determinant
   descent and type-cut identities, retaining their indices and
   complementary degrees.

These are still substantial arithmetic-geometric tasks. The new elementary
argument shortens the required interface; it is not evidence that a fixed
number of further prompts, or a specified final page count, will complete
the proof.

The [reproducible check](../scripts/check_geometric_degree_frontier.py)
verifies the pinned source bytes, exact symbolic identities, source-scale
absorption and the scalar obstruction. Its finite examples supplement the
written proof. It does not verify the deep geometric construction.

The independent source review of Sections 1–3 passed: it checked the same
component lattice and metric, the normalized-degree factor, untwisted
Hilbert–Samuel substitution, flat twist, and the exact raw-surplus
collection. A separate root review checked Sections 1–2 and the mechanism
of Section 3. Neither review claims a replay of upstream proofs.
