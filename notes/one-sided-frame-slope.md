# One-sided period bounds in the arithmetic slope comparison

## Result and scope

A one-sided bound on the actual common-target operator can be used
**directly** in the slope argument. Its excess enters linearly, without
first bounding a squared Hilbert--Schmidt defect and taking a square root.
More generally, it is enough to dominate the operator by the calibrated
scalar operator plus a positive operator of small **trace**. The latter
operator may have large norm.

These are proved comparison theorems for the same arithmetic maps and
metrics. The required common-target majorant is not constructed here.
The inspected source's conditional trace-square estimate implies a trace
allowance when its quantitative hypotheses are supplied. Those remaining
global bounds, or a direct positive trace majorant, are still needed.
No RH or GRH
construction node is closed.

## 1. The direct comparison

Let \(f_i:E_i\to F\) be finitely many integral maps of nonzero Hermitian
lattices over one number field. Degrees and logarithmic map heights are
normalized by the field degree, and slopes use ordinary norms. Write
\(r_i=\operatorname{rank}E_i>0\), \(R=\sum_i r_i\), and
\(n=\operatorname{rank}F>0\). Suppose \(h(f_i)\le h_i\), and, for
\(s\in\mathbb R\) and \(U,H\ge0\), assume

\[
 \frac1R\sum_i r_i\{\mu(E_i)-h_i\}\ge s,\qquad
 \max_i\{\mu_{\max}(E_i)-h_i\}\le s+U,\qquad
 \mu_{\min}(F)\ge s-H.                                    \tag{1.1}
\]

At one complex embedding suppose the first \(n\) rows of matrices
\(T_i:\mathbb C^{r_i}\to\mathbb C^D\), \(D\ge n\), represent these
same maps, in individual source bases and **one common target basis**.
The auxiliary matrix norms are Euclidean. Take \(a\ge0\) and set

\[
 Q=\sum_iT_iT_i^*,\quad M=\operatorname{tr}Q>0,\quad
 \mathcal S=\bigoplus_iT_i^*T_i,\quad
 a^2=\frac R{M^2}\left\|\mathcal S-\frac MR I_R\right\|_{\rm HS}^2,
 \quad \nu=n/D,\quad\delta=1-\nu,
\]
\[
 \Phi(U,H)=
 \begin{cases}\sqrt{UH},&U\le H,\\(U+H)/2,&U>H.\end{cases}
\]

**Theorem.** Suppose
\[
 Q\le\alpha I_D+E,\qquad
 \alpha=(1+\lambda)M/D,\qquad
 \lambda\ge0,\quad E\ge0,\quad\operatorname{tr}E\le\epsilon M,
 \quad\epsilon\ge0.                                      \tag{1.2}
\]
Then
\[
 \boxed{\quad
 s-\mu(F)\le\frac{\delta U}{\nu}
  +\frac{a\Phi(U,H)+\lambda H+\epsilon(U+H)}
         {\nu(1+\lambda)}.
 \quad}                                                   \tag{1.3}
\]
When \(E=0\), set \(\epsilon=0\). When the matrices already act on
the final target, \(D=n\), so
\[
 \boxed{\quad
 s-\mu(F)\le
 \frac{a\Phi(U,H)+\lambda H+\epsilon(U+H)}{1+\lambda}.
 \quad}                                                   \tag{1.4}
\]
The independent bound \(s-\mu(F)\le H\) can always be retained.

**Proof.** Multiply the norm on \(E_i\) by \(e^{h_i}\). Its slopes
decrease by \(h_i\), and the map height becomes nonpositive.
Functoriality of the Harder--Narasimhan filtration for an integral map
of nonpositive height carries source slopes at least \(\xi\) into the
corresponding target filtration space. This is the usual determinant
inequality applied to a nonzero induced map into a lower-slope quotient.

For \(\xi\in[s-H,s+U]\), let \(p(\xi)\) be the total source filtration
rank divided by \(R\), and \(q(\xi)\) the target filtration rank divided
by \(n\). Lift the latter space to \(\mathbb C^D\) by adjoining all
discarded \(D-n\) coordinates. Its dimension fraction is
\(w(\xi)=\delta+\nu q(\xi)\), and it contains every image of the source
filtration spaces under \(T_i\).

If \(P\) is the direct-sum orthogonal projection onto those source
spaces and \(P_W\) projects onto that lifted target space, put
\(C=\sum_iT_iP_iT_i^*\). Positivity and the range inclusion give
\(0\le C\le Q\) and
\[
 M\{p-a\sqrt{p(1-p)}\}
 \le\operatorname{tr}C
 \le\operatorname{tr}(P_WQ)
 \le M\{(1+\lambda)w+\epsilon\}.                           \tag{1.5}
\]
The first inequality centers \(\mathcal S\), using
\(\|P-pI_R\|_{\rm HS}^2=Rp(1-p)\).
The last one uses \(\operatorname{tr}(P_WE)\le\operatorname{tr}E\);
it requires no commutation.

Write \(L=U+H\). The source upper slope bound and its mean imply
\(\int p\ge H\), and hence \(\int(1-p)\le U\), on this interval.
If \(z=\int(1-p)\), then
\[
 \int\sqrt{p(1-p)}\le\sqrt{z(L-z)}\le\Phi(U,H).
\]
Also \(\mu(F)\ge s-H+\int q\). Integrating (1.5) therefore gives
\[
 \nu(1+\lambda)\{s-\mu(F)\}
 \le \nu(1+\lambda)H-H+(1+\lambda)\delta L
        +a\Phi(U,H)+\epsilon L.
\]
The first three terms equal
\(\lambda H+(1+\lambda)\delta U\). This proves (1.3).
If \(L=0\), the conclusion follows directly from
\(\mu_{\min}(F)\ge s\). All other zero parameters are allowed.
\(\square\)

One can replace the term \(\epsilon L\) by the smaller exact quantity
\[
 \frac1M\int_{s-H}^{s+U}\operatorname{tr}(P_{W(\xi)}E)\,d\xi.
 \tag{1.6}
\]
Thus the trace estimate may itself retain the actual target filtration
before taking an outer average.

## 2. A positive trace allowance

For a self-adjoint matrix \(A\), let \(A_+\) denote its positive part.
The canonical choice at \(\lambda=0\) is
\[
 E_0=(Q-(M/D)I_D)_+,\qquad
 \beta=\frac{\operatorname{tr}E_0}{M}.
\]
Then
\[
 s-\mu(F)\le\frac{\delta U+a\Phi(U,H)+\beta(U+H)}{\nu}.
 \tag{2.1}
\]
Any supplied majorant
\[
                  Q\le(M/D)I_D+E,\qquad E\ge0              \tag{2.2}
\]
gives \(\beta\le\operatorname{tr}E/M\).
Indeed, if \(P_+\) is the spectral projection onto the positive
eigenspaces of \(Q-(M/D)I_D\), then
\[
 \operatorname{tr}E_0
 =\operatorname{tr}(P_+(Q-(M/D)I_D))
 \le\operatorname{tr}(P_+E)\le\operatorname{tr}E.
\]
Consequently \(E_0\) minimizes the trace among all positive majorants
in (2.2). For comparison with the squared-energy criterion,
\[
 \beta=\frac{\|Q-(M/D)I_D\|_1}{2M}
       \le\frac{\sqrt\eta}{2},\qquad
 \eta=\frac D{M^2}\|Q-(M/D)I_D\|_{\rm HS}^2.                 \tag{2.3}
\]
The equality uses trace zero; the inequality is Cauchy--Schwarz on the
eigenvalues. Formula (2.1) therefore never increases the target term
in the centered slope comparison. Its majorant uses only the trace of
the positive error, unlike the previous positive-majorant theorem that
also controls a centered squared norm of the majorant.

There is an analogous one-sided **source** allowance,
\[
 \gamma=\frac1M\operatorname{tr}((M/R)I_R-\mathcal S)_+.
\]
For every source projection of rank fraction \(p\),
\(\operatorname{tr}(P\mathcal S)\ge M(p-\gamma)\).
Thus the term \(a\Phi(U,H)\) in (1.3) may be replaced by
\[
              \min\{a\Phi(U,H),\gamma(U+H)\}.              \tag{2.4}
\]
The two valid integrated lower bounds prove this minimum. As before,
\(\gamma\le a/2\), and any positive lower majorant
\(\mathcal S\ge(M/R)I_R-E_{\rm s}\) gives
\(\gamma\le\operatorname{tr}E_{\rm s}/M\).
Consequently a sufficiently small pair of source and target trace
allowances can replace both squared-energy hypotheses in this
comparison. Positive total mass and the arithmetic hypotheses remain.
The corresponding rank bounds are
\[
 \operatorname{rank}Q\ge D(1-\beta),\qquad
 \sum_i\dim\ker T_i\le R\gamma.                           \tag{2.5}
\]
Each zero eigenvalue contributes \(M/D\) to the target negative
trace, or \(M/R\) to the source negative trace, proving both bounds.

There is no need for a uniform bound on (1.3) over the permitted scale
and component family. Whenever the quantities are measurable and their
nonnegative right sides are integrable, multiply by the actual
nonnegative frame weight and integrate. Keep the factors \(H,U,\nu\)
and normalization \(M\) from each datum inside that integral.
An estimate for the average matrix alone does not estimate these costs.

## 3. Both restrictions using only the trace allowance

Let \(J_i:\mathbb C^{r_i'}\to\mathbb C^{r_i}\) be isometries, let
\(\Pi\) be an orthogonal target projection of rank \(n>0\), and put
\[
 Q'=\sum_iT_iJ_iJ_i^*T_i^*,\quad Q_0=\Pi Q'\Pi|_{\operatorname{ran}\Pi},
 \quad M_0=\operatorname{tr}Q_0,\quad
 L=\operatorname{tr}(Q-Q'),\quad \rho=L/M,\quad\delta=1-n/D.
\]
Let \(R'=\sum_i r_i'>0\), and define
\[
 \Delta=\sum_i\|T_i^*T_i-I\|_{\rm HS}^2,\qquad
 \Delta_0=\sum_i\|J_i^*T_i^*\Pi T_iJ_i-I\|_{\rm HS}^2.
\]
If \(k=1-\rho-\delta-\beta>0\), then
\[
 \boxed{\quad
 M_0\ge Mk>0,\qquad
 \beta_0:=\frac{\operatorname{tr}(Q_0-(M_0/n)I)_+}{M_0}
       \le\frac{\beta+\rho}{k},\qquad
 \Delta_0\le\Delta+2M(\delta+\beta).
 \quad}                                                   \tag{3.1}
\]
The exact centered source defect \(a_0\ge0\) of these final maps is
\[
 a_0^2=\frac{R'\Delta_0-(M_0-R')^2}{M_0^2}
       \le\frac{R'\Delta_0}{M_0^2}.                        \tag{3.2}
\]
Thus (1.4) applies with \(\lambda=0\) directly on the final target.
If only the lost source rank \(l=R-R'\) is known, the previous elementary
diagonal estimate gives \(L\le l+\sqrt{l\Delta}\).

**Proof.** For a trace-zero self-adjoint matrix \(A\) and a compression
\(B=\Pi A\Pi|_{\operatorname{ran}\Pi}\), let \(b=\operatorname{tr}B\).
If \(b\ge0\), then
\(\operatorname{tr}(B-(b/n)I)_+\le\operatorname{tr}B_+
\le\operatorname{tr}A_+\).
If \(b\le0\), use instead the negative parts:
\(\operatorname{tr}(B-(b/n)I)_+
=\operatorname{tr}(B-(b/n)I)_-\le\operatorname{tr}B_-
\le\operatorname{tr}A_-=\operatorname{tr}A_+\).
The inequalities for compressed positive/negative traces follow from
their variational formula over orthogonal projections.

First remove the source directions. The centered matrix is
\[
 Q'-(M-L)I/D=(Q-MI/D)-(Q-Q')+(L/D)I.
\]
Since \(Q-Q'\ge0\), its positive trace is at most
\(\beta M+L\). Apply the compression result just proved to obtain
\(\beta_0M_0\le M(\beta+\rho)\).
The discarded target mass is at most
\[
 \operatorname{tr}((I-\Pi)Q')
 \le\operatorname{tr}((I-\Pi)Q)
 \le M(\delta+\beta),
\]
which proves the lower bound on \(M_0\).

For completeness, put
\(G=\bigoplus_iJ_i^*T_i^*T_iJ_i\) and
\(B=\bigoplus_iJ_i^*T_i^*(I-\Pi)T_iJ_i\).
Then \(0\le B\le G\), source compression does not increase
\(\|G-I\|_{\rm HS}^2\), and
\[
 \Delta_0=\|G-I\|_{\rm HS}^2-2\operatorname{tr}(GB)
                      +2\operatorname{tr}B+\operatorname{tr}(B^2)
 \le\Delta+2\operatorname{tr}B.
\]
Here \(\operatorname{tr}((G-B)B)\ge0\), without a commutation
assumption. Finally \(\operatorname{tr}B\) is exactly the discarded
target mass. Formula (3.2) follows by centering the block Gram matrix.
\(\square\)

The denominator and actual retained rank cannot be dropped. This
interface may be compared with the earlier squared-energy and uniform
Bessel interfaces; use whichever gives the smaller valid final cost.

For a comparison using only the two trace allowances, the same argument
also gives, with
\(\mathcal S_0=\bigoplus_iJ_i^*T_i^*\Pi T_iJ_i\) and
\(\gamma_0=M_0^{-1}\operatorname{tr}((M_0/R')I-\mathcal S_0)_+\),
\[
 \rho\le\frac{R-R'}R+\gamma,\qquad
 \gamma_0\le\frac{\gamma+\delta+\beta}{k}.                  \tag{3.3}
\]
The first bound applies the positive trace of
\(\mathcal S-(M/R)I_R\), also equal to \(\gamma M\), to the discarded
source projection. Source restriction followed by recentering cannot
increase the unnormalized source trace allowance, by the compression
argument above. Target restriction then subtracts a positive block
operator of trace at most \(M(\delta+\beta)\), increasing its
recentered negative trace by at most that amount. Divide by \(M_0\).
These are sufficient bounds, not a claim that using the fully
restricted target always gives the smallest target-rank cost.

## 4. Sharp examples and the limits of positivity

For the uniform bound with \(E=0\), let \(k\le D\), take \(k\)
rank-one maps onto distinct coordinate vectors, and put \(Q=P_k\).
Then \(M=k\), \(a=0\), and \(\lambda=D/k-1\).
Give the target image coordinates slope \(s\) and its other coordinates
slope \(s-H\); give every source slope \(s\). The maps are integral
and have height zero. Thus \(U=0\) and
\[
                 s-\mu(F)=\frac{\lambda H}{1+\lambda}.     \tag{4.1}
\]
This proves sharpness of the linear target penalty in (1.4).

The trace criterion can be substantially weaker than either a small
operator excess or small squared energy. For an integer \(N\ge2\), set
\(D=N^3\). Use \(D\) unit rank-one integral maps: \(N^2\) copies of
the first coordinate vector, and one copy of each of \(D-N^2\)
further coordinate vectors. Then
\[
 Q=\operatorname{diag}\left(N^2,
          \underbrace{1,\ldots,1}_{D-N^2},
          \underbrace{0,\ldots,0}_{N^2-1}\right),\quad
 M=R=D,\quad\Delta=a=0,
\]
\[
 \beta=\frac{N^2-1}{N^3}\longrightarrow0,\qquad
 \eta=N-\frac1N\longrightarrow\infty,\qquad
 \lambda_{\min}=N^2-1.                                   \tag{4.2}
\]
Give the image coordinates slope zero and the omitted coordinates
slope \(-H\), with unit source metrics. The maps again have height
zero and the actual slope loss is exactly \(\beta H\).
This is an arithmetic linear-algebra example, not the selected
automorphic family.

Positive-definite matrix coefficients, positive normalizers, a fixed
trace, and perfect diagonal norms cannot by themselves supply a small
Bessel excess. The simpler family of \(D\) copies of a single unit
coordinate vector has \(\Delta=0\), \(M=D\) but
\(\lambda_{\min}=\eta=D-1\) and \(\beta=1-1/D\).
Its block Gram matrix has entries one, and is the matrix coefficient
of the trivial unitary representation. Positivity is fully respected.
Likewise averaging \(D P_{e_j}\) over \(j=1,\ldots,D\) gives \(I_D\),
although every summand has the same large defects. This rules out an
unqualified replacement by the operator of the averaged family.

## 5. Same-map source applicability

All sources use the immutable revision
jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.
The earlier source audit identifies the actual positive normalizers
\(c_u\), period maps \(P_u\), and common target basis; the matrices are
\(T_u=c_u^{-1/2}P_u\). Domain and target restrictions must be the
actual ones. The new comparison does not change any lattice, map,
height, divisor or metric.

The source's fully compressed operator is exactly
\[
       Q_0=\sum_u c_u^{-1}\Pi P_u\Pi_uP_u^*\Pi.
\]
Regard it on the range of \(\Pi\), use its actual positive trace
\(M_0\), and use the diagonal defect of the same compressed maps.
Then (1.4) applies without any additional target-loss term.
An admissible replacement for the missing uniform Bessel input is
\[
 Q_0\le(M_0/n)I+E_0,\qquad E_0\ge0,\qquad
 \frac{\operatorname{tr}E_0}{M_0}(U+H)
 \ \text{small enough in the actual averaged frame budget}. \tag{5.1}
\]
The diagonal estimate and the source/target slope hypotheses still
have to hold on that same datum. Section 3 also permits supplying
this trace allowance before both restrictions.

### The existing linear orbital expansion is enough

There is no need to derive a new common-target unfolding. Let
\(S:\bigoplus_i\mathbb C^{r_i}\to\mathbb C^D\) be synthesis,
\(S(v_i)=\sum_iT_iv_i\), and let
\(\mathcal K=S^*S=[T_i^*T_j]\) be its normalized block Gram matrix.
For every \(\alpha>0\),
\[
 \boxed{\quad
 \operatorname{tr}(Q-\alpha I_D)_+
       =\operatorname{tr}(\mathcal K-\alpha I_R)_+.
 \quad}                                                   \tag{5.2}
\]
Indeed \(SS^*\) and \(S^*S\) have the same positive eigenvalues with
multiplicity; all additional zero eigenvalues contribute zero.
The existing source interface specifies an absolutely convergent
linear orbital expansion for each block of \(\mathcal K\) on its
full period maps. Its expansion and convergence hypotheses remain
explicit inputs here.
Section 3 transports an estimate for those maps through the actual
restrictions. A direct expansion for already restricted maps would
have to be identified on those maps separately.
When the full expansion's specified diagonal
identity cells sum to \(I_R\), write \(\mathcal K=I_R+N\).
Then a sufficient supplier for (1.2) is simply
\[
 \operatorname{tr}((1-\alpha)I_R+N)_+\le\epsilon M,
 \qquad \alpha=(1+\lambda)M/D.                            \tag{5.3}
\]
All off-diagonal cells remain unless their zero sum is separately
proved. The positive part is taken after their signed contributions
have been combined.

More generally, a positive block majorant
\(\mathcal K\le\alpha I_R+E_{\mathrm{block}}\) with
\(\operatorname{tr}E_{\mathrm{block}}\le\epsilon M\)
transfers to a common-target majorant. In the polar decomposition
\(S=V\mathcal K^{1/2}\), the partial isometry \(V\) gives
\[
 Q=V\mathcal K V^*
 \le\alpha I_D+VE_{\mathrm{block}}V^*,\qquad
 \operatorname{tr}(VE_{\mathrm{block}}V^*)
 \le\operatorname{tr}E_{\mathrm{block}}.
\]
This is an analytic comparison; it changes no arithmetic map.

Absolute convergence implies operator-norm convergence of the finite
block truncations. Symmetrize them if necessary. For self-adjoint
\(R\)-dimensional matrices \(A,B\),
\[
 |\operatorname{tr}A_+-\operatorname{tr}B_+|
       \le R\|A-B\|_{\mathrm{op}},
\]
by the variational formula
\(\operatorname{tr}A_+=\max_{0\le P\le I}\operatorname{tr}(PA)\).
Thus a bound (5.3) for all such finite truncations with the same
\(\epsilon M\) passes to the limit at each fixed datum. Any error
allowed in a quantitative truncation must retain this dimension
factor. The required uniform or suitably averaged tail bound itself
is still open.

If one instead supplies an ambient uniform Bessel bound, the earlier
joint-restriction theorem gives
\(\lambda_0\le\bar\lambda=(\lambda+\rho)/\kappa\), where
\(\kappa=1-\rho-(1+\lambda)\delta>0\).
For the final maps one may use
\[
 s-\mu(F)\le
 \min\left\{H,\frac{a_0\Phi(U,H)+\bar\lambda H}
                         {1+\bar\lambda}\right\}.          \tag{5.4}
\]
To justify substitution of the upper bound, write the fraction as
\(H+(a_0\Phi-H)/(1+\lambda_0)\). If \(a_0\Phi\le H\), it increases
with \(\lambda_0\); otherwise the independent bound \(H\) applies.
The retained rank and positive retained trace requirements remain.

The inspected source conclusions conditionally bound
\(\operatorname{tr}Q_0\) below and \(\operatorname{tr}(Q_0^2)\) above.
Once their quantitative hypotheses are supplied, they give the older
squared-energy bound and hence a positive trace allowance through
\(\beta_0\le\sqrt{\eta_0}/2\). They do not establish the desired
allowance without those remaining global bounds; a direct estimate
such as (5.1) or (5.3) is a weaker alternative supplier.
The positive kernel on arithmetic points for a fixed ordered word pair
lives on a different space; it is not identified with a positive
error on this common target. The projection/cuspidal-range contracts
inspected in this continuation also contain no equality identifying
their projector with this weighted period sum. No conclusion is drawn
from the name of the geometric scalar-pair predicate.

The certificate records exact hashes and ranges for the source
definitions of the weighted projection sum, the actual \(Q_0\) and
trace-square conclusion, the common arithmetic matrix identification,
the point-kernel majorant, and the separate projection-range contract.
Its exact checks supplement the proofs above. No upstream proof audit
or Lean kernel replay is claimed.

| Bounded source | Inspected lines | Role |
| --- | --- | --- |
| DataS | 33–48, 50–84 | Common spaces, period maps and prescribed volumes. |
| RelevantZeroGramTerms | 335–376 | Normalized block Gram, expansion/convergence and identity-cell predicates, and separate squared-pair kernel. |
| AdmissibleBoundsFromSource | 220–267 | Actual fully restricted operator and conditional trace-square comparison. |
| TopDensityNGeSixteen | 1004–1066, 1090–1122 | Common target basis and the same arithmetic maps. |
| LocalBesselAndTopKernel | 206–221, 655–672 | Point-indexed positive majorant and its squared-norm use. |
| WeightedProjectionSumSelfAdjoint | 64–77 | Definition of the weighted projection sum, with no supplied upper norm estimate in this passage. |
| ProjectionStatementOfFinal | 35–49 | Separate conditional cuspidal-range contract. |

Complete module paths, Git/SHA-256 values, excerpt hashes and exact
verification results are preserved in
[the certificate](../certificates/one-sided-frame-slope.json).
