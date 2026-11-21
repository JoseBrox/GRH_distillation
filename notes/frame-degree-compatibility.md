# Can the theta frame replace the geometric degree estimate?

## Conclusion

The frame contracts alone do not supply the absolute, period-normalized
degree bound required in W10. The final arithmetic theta maps have target
the dual lattice of the final space; W10 concerns selected cuspidal lattices
at intermediate stages. No identity between those different lattices has
been established.

There are nevertheless three useful improvements.

* Exact proportional expansion of all source subspaces gives a relative
  slope inequality with **no frame penalty, source-spread hypothesis or
  target minimum-slope hypothesis**.
* A centered projection estimate gives a new quantitative slope bound.
  Its error vanishes for a perfect frame with no target cut; the effect
  of a target cut depends on the source spread.
* A common positive rescaling of the comparison matrices has an explicit
  optimum. It replaces the raw diagonal error by a scale-invariant defect,
  without changing an arithmetic map, its metric, or its height.

All three improvements are compatible with the actual common-basis interface.
Neither proves the stronger expansion condition for the source family.
Exact determinant and short-image criteria below identify what additional
arithmetic information could supply an absolute degree bound. Explicit
counterexamples show why an approximate frame cannot supply that
information by itself.

All degrees are normalized by the number-field degree, and \(\mu\) denotes
ordinary arithmetic slope. Source squared-norm slopes and map heights are
twice the ordinary quantities used here. Source references use
jsmorph/rh at ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.

## 1. Exact rank expansion removes the slope-comparison loss

Let \(E_i,F\) be nonzero Hermitian \(\mathcal O_K\)-lattices of ranks
\(r_i,n\), put \(R=\sum_i r_i\), and let
\(f_i:E_i\longrightarrow F\) be integral maps with ordinary heights
\(h(f_i)\le h_i\in\mathbf R\). Fix one complex embedding.
Suppose that, for **every** collection of complex subspaces
\(V_i\subset E_{i,\mathbf C}\),
\[
 \frac{\dim_{\mathbf C}\sum_i f_i(V_i)}{n}
 \ge\frac{\sum_i\dim_{\mathbf C}V_i}{R}.
 \tag{1.1}
\]
Then
\[
 \boxed{\mu(F)\ge
       \frac1R\sum_i r_i\{\mu(E_i)-h_i\}.}
 \tag{1.2}
\]

**Proof.** Multiply all norms of \(E_i\) by \(e^{h_i}\). Its slopes
decrease by \(h_i\), and the integral map now has height at most zero.
The height-zero functoriality proved in the manuscript implies
\[
 f_i((E_i)_{\ge t})\subset F_{\ge t}
 \qquad(t\in\mathbf R)
\]
for the adjusted source filtrations. Apply (1.1) to their complexifications:
\[
 \frac{\operatorname{rk}F_{\ge t}}n
 \ge\frac1R\sum_i\operatorname{rk}(E_i)_{\ge t}.
\]
Choose a finite interval containing every source and target slope.
Integrating these normalized survival functions gives their mean slopes,
up to the same lower endpoint. This proves (1.2). All norms used for the
arithmetic heights remain the prescribed ones, apart from the explicit
source rescaling already accounted for by \(h_i\). \(\square\)

There is no use of a pre-existing bound for \(\mu(F)\) in this argument.
If the adjusted source mean is independently known, (1.2) is therefore
noncircular. If that mean is itself the unknown arithmetic expression,
(1.2) remains a comparison and is not an absolute bound for it.

The condition is strong. It forces each \(f_i\) to be injective, by taking
\(V_i\subset\ker f_i\), and forces joint surjectivity, by taking every
\(V_i=E_{i,\mathbf C}\). Individual invertible changes of source bases,
a common invertible target change of basis, and nonzero individual
scalar factors preserve (1.1).

## 2. A centered frame test, including the target cut

Let \(T_i:\mathbf C^{r_i}\to\mathbf C^D\), and define
\[
 S=\bigoplus_iT_i^*T_i,\quad Q=\sum_iT_iT_i^*,\quad
 M=\operatorname{tr}S=\operatorname{tr}Q>0,
\]
\[
 \Delta=\|S-I_R\|_{\rm HS}^2,\qquad
 V_s=\left\|S-\frac MR I_R\right\|_{\rm HS}^2
     =\Delta-\frac{(M-R)^2}{R}\ge0,
\]
\[
 V_t=\left\|Q-\frac MD I_D\right\|_{\rm HS}^2,\qquad
 a=\frac{\sqrt{RV_s}}M,\qquad
 b=\frac{\sqrt{DV_t}}M=\sqrt\eta.
\]
For source subspaces of total dimension \(k\), let \(W\) contain all
their images, and put \(p=k/R\), \(q=\dim W/D\). Then
\[
 \boxed{p-a\sqrt{p(1-p)}
        \le q+b\sqrt{q(1-q)}.}
 \tag{2.1}
\]
In particular \(q\ge p-(a+b)/2\).

**Proof.** Let \(P_i\) be the source orthogonal projections,
\(P=\bigoplus_iP_i\), and \(C=\sum_iT_iP_iT_i^*\).
Then \(0\le C\le Q\), its range is contained in \(W\), and
\[
 \operatorname{tr}C=\operatorname{tr}(PS)
 \ge Mp-\sqrt{V_s}\sqrt{Rp(1-p)}.
\]
This is Hilbert–Schmidt Cauchy–Schwarz after centering both matrices;
\(\|P-pI_R\|_{\rm HS}^2=Rp(1-p)\).
With \(P_W\) the target projection, positivity gives
\[
 \operatorname{tr}C\le\operatorname{tr}(P_WQ)
 \le Mq+\sqrt{V_t}\sqrt{Dq(1-q)}.
\]
Divide by \(M\). The coarser consequence uses
\(\sqrt{u(1-u)}\le1/2\). \(\square\)

If \(a=b=0\), this gives exact proportional expansion in the full
target. In particular, individual isometries whose ranges form a tight
frame satisfy (1.1) when the arithmetic target is that full target.

### A sufficient discrete test for the actual arithmetic target

Suppose the first \(n\le D\) rows of the matrices represent the arithmetic
maps in the allowed bases. Put \(\delta_0=(D-n)/D\). If the actual
arithmetic images of a family of subspaces span a space of dimension \(r\),
the full images lie in a space of dimension at most \(r+D-n\).
Apply (2.1) to that containing space. It gives
\[
 \frac{k}{R}-\frac rn
 \le\delta_0\left(1-\frac rn\right)+\frac{a+b}{2}
 \le\delta_0+\frac{a+b}{2}.
 \tag{2.2}
\]
Consequently
\[
 \boxed{\delta_0+\frac{a+\sqrt\eta}{2}<\frac1{nR}}
 \tag{2.3}
\]
is sufficient for (1.1): a positive difference \(k/R-r/n\) is an
integer divided by \(nR\), and is therefore at least \(1/(nR)\).

The strict inequality and the actual ranks are essential. This is not
a claim that the existing errors are small enough. In particular,
when \(D>n\) and \(R\ge D\), the target-cut term alone is at least
\(1/D\ge1/(nR)\), so this convenient sufficient test cannot apply.
The actual projected maps might still satisfy (1.1); that would require
additional information. Applying (2.1) directly to their projected
matrices is another option, with their recomputed energies.

## 3. The best common normalization of the comparison matrices

Write \(U_s=\operatorname{tr}(S^2)>0\). Replacing every \(T_i\) by
\(\sqrt t\,T_i\), \(t>0\), gives diagonal error
\[
 e(t)=\frac{t^2U_s-2tM+R}{R}
     =\frac{U_s}{R}\left(t-\frac M{U_s}\right)^2
       +1-\frac{M^2}{RU_s}.
\]
Hence the exact optimum is
\[
 \boxed{t_*=\frac M{U_s},\qquad
 e_* =1-\frac{M^2}{RU_s}
     =\frac{a^2}{1+a^2}\in[0,1).}
 \tag{3.1}
\]
It is no larger than the original diagonal error. The normalized target
isotropy \(\eta\), all images, and every rank condition are unchanged.
The new mass satisfies \(M_*/R=1-e_*\).

Thus the refined frame comparison may use \(\sqrt{e_*}\) in place of
the raw square root of the diagonal error. This operation changes
only the comparison matrices: the same scalar is absorbed into their
invertible source-basis matrices. It does not multiply any arithmetic
map by a possibly nonintegral scalar and does not change its global
height. A retained family can be normalized separately after restriction.

Positive mass still has to be established. The individual positive
normalizers needed to define the original theta matrices remain separate
requirements. Also, \(e_*\) may approach one, so the denominator
\(1-\sqrt{e_*}\) can be large. The normalization does not turn an
ineffective frame estimate into a uniform small error by itself.

For comparison, forcing mass exactly \(R\) gives diagonal error \(a^2\).
That normalization need not improve the original error; (3.1) is the
actual minimum. The ratio \(M^2/U_s\le R\) is the effective source rank.

### A centered slope bound

Retain the integral maps and ordinary height bounds of Section 1.
Suppose the first \(n\le D\) rows of the matrices in Section 2 represent
these maps in the allowed bases. Let \(u,H\ge0\), and assume
\[
 \frac1R\sum_i r_i\{\mu(E_i)-h_i\}\ge s,\qquad
 \mu_{\max}(E_i)-h_i\le s+u,\qquad
 \mu_{\min}(F)\ge s-H.
\]
Put \(\nu=n/D>0\), \(\delta_0=1-\nu\), and
\[
 \Phi(u,H)=
 \begin{cases}
  \sqrt{uH},&u\le H,\\
  (u+H)/2,&u>H.
 \end{cases}
\]
Then the centered source and target defects from Section 2 give
\[
 \boxed{s-\mu(F)\le
       \frac{\delta_0u+a\Phi(u,H)+\sqrt\eta\,(H+u)/2}{\nu}.}
 \tag{3.2}
\]
No bound for the absolute trace mass is needed beyond \(M>0\).

**Proof.** Adjust the source norms as in Section 1, so every map has
height at most zero. For \(\xi\in[s-H,s+u]\), let \(p(\xi)\) and
\(q(\xi)\) be the normalized source and target filtration ranks.
Height-zero functoriality puts the full matrix images in the sum of
the target filtration space and the \(D-n\) discarded coordinates.
Its ambient dimension fraction is
\(w(\xi)=\delta_0+\nu q(\xi)\). Equation (2.1) therefore gives
\[
 \nu q(\xi)\ge p(\xi)-\delta_0
             -a\sqrt{p(\xi)(1-p(\xi))}
             -\sqrt\eta\sqrt{w(\xi)(1-w(\xi))}.
\]
All adjusted source slopes are at most \(s+u\).
Their mean lower bound implies
\[
 \int_{s-H}^{s+u}p(\xi)\,d\xi\ge H,\qquad
 \int_{s-H}^{s+u}(1-p(\xi))\,d\xi\le u.
\]
Indeed, the first integral is the mean of
\((\alpha-(s-H))_+\) over the adjusted source slopes \(\alpha\);
source slopes below \(s-H\) cause no difficulty.
Writing \(x=\int(1-p)\) and \(W=u+H\), Cauchy–Schwarz gives
\[
 \int\sqrt{p(1-p)}\le\sqrt{x(W-x)}\le\Phi(u,H).
\]
The maximum is at \(x=u\) when \(u\le H\), and at \(x=W/2\)
otherwise. The target contribution is at most \(W/2\).
Finally, the lower target slope bound gives
\(\mu(F)\ge s-H+\int q\); target slopes above \(s+u\) only
improve this inequality. Integrate the displayed rank bound and use
\(\nu=1-\delta_0\). The terms containing \(\delta_0H\) cancel,
leaving (3.2). The case \(u+H=0\) is immediate. \(\square\)

When \(a=\eta=\delta_0=0\), the cost in (3.2) is zero. It therefore
improves the earlier bound in that limit, which retained a logarithmic
source-spread term. It is a complementary estimate in general: its
\(\sqrt\eta\) dependence can be worse than the earlier refined bound.
One may take the minimum of the available bounds and the immediate
bound \(s-\mu(F)\le H\).

The perfect-frame target-cut coefficient is sharp. Take one full
identity matrix of size \(D\), and let the arithmetic map project to
\(n=\nu D\) coordinates. Give each discarded source coordinate slope
\(s+u\), and every retained coordinate slope
\(s-\delta_0u/\nu\), with the same metrics on the target.
The projection has height zero, the source mean is \(s\), and
\[
 s-\mu(F)=\delta_0u/\nu.
\]
Thus equality holds in (3.2), provided \(H\ge\delta_0u/\nu\).
This example retains the actual target cut; it does not claim that the
source family has zero defects.

## 4. What a determinant or short-image argument really requires

Let \(f:\bigoplus_iE_i\to F\) be the stacked integral map, assumed
surjective over \(K\). Put \(E=\bigoplus_iE_i\), \(K_0=\ker f\), give
the quotient \(E/K_0\) its quotient metrics, and let \(J=[F:f(E)]\).
The exact determinant identity is
\[
 \boxed{\widehat{\deg}F
 =\sum_i\widehat{\deg}E_i-\widehat{\deg}K_0
       -h_{\det}(f)+\frac{\log J}{[K:\mathbf Q]}.}
 \tag{4.1}
\]
Here \(h_{\det}(f)\) is the normalized logarithm of the determinant norm
of the induced isomorphism \(E/K_0\to F\).
The proof is determinant multiplicativity, followed by the finite-index
comparison. In orthonormal bases for the **arithmetic metrics**,
\[
 h_{\det}(f)=\frac1{2[K:\mathbf Q]}
          \sum_{v\mid\infty}n_v\log\det(f_vf_v^*).
 \tag{4.2}
\]
Analytic frame matrices in unrelated invertible bases cannot be inserted
into (4.2). Even when (4.2) is available, a bound for the kernel degree
is still needed. A small kernel rank does not bound its degree.

There is a different, useful sufficient criterion. Suppose integral
source vectors \(v_j\in E_{i(j)}\), \(1\le j\le n\), have images
forming a \(K\)-basis of \(F\). Define
\[
 \ell(v)=\frac1{[K:\mathbf Q]}
              \sum_{v_\infty\mid\infty}n_{v_\infty}
                    \log\|v\|_{v_\infty}.
\]
Hadamard's inequality and the nonnegative image-index contribution give
\[
 \boxed{\mu(F)\ge-\frac1n\sum_{j=1}^n
                    \{\ell(v_j)+h(f_{i(j)})\}.}
 \tag{4.3}
\]
Indeed, each image vector has logarithmic norm at most the displayed
source norm plus map height, and their determinant is bounded by the
product of their norms at every embedding.
This would bypass a separate target degree theorem if those actual
integral vectors and their global heights were independently controlled.
An orthonormal complex basis is not such an integral generating family.

## 5. Three precise obstructions

### Absolute degree is invisible to a common metric shift

Take identical rank-one integral lattices and the identity map, and
multiply both metrics by \(e^c\). The orthonormal matrix of the map
is still \(1\), its height is still zero, and both frame errors are zero.
Both arithmetic slopes decrease by \(c\).
Thus exact frames and map heights alone do not bound an absolute slope.

If only the target metric is multiplied by \(e^c\), then
\[
 \mu(F)\mapsto\mu(F)-c,\qquad
 h(f_i)\mapsto h(f_i)+c.
\]
The difference between the two sides of (1.2) is unchanged. Normalizing
the target degree by an unknown metric shift merely transfers that
unknown constant into the map heights. No metric in the actual
construction is being changed here; these models disprove the proposed
inference from frame data alone.

### Tiny average defects can hide an arbitrarily large kernel degree

Over \(\mathbf Q\), let \(F=\mathbf Z^N\), \(N\ge2\), with norm
\(e^H\|\cdot\|_2\), where \(H>0\).
Let \(E_0=\mathbf Z^2\) have orthogonal basis norms
\(e^{-NH},e^H\), and map its second coordinate to the first coordinate
of \(F\), killing the first. For \(2\le j\le N\), take a source line
of basis norm \(e^H\) mapping to the \(j\)-th coordinate of \(F\).
Every map is integral and nonzero, with height zero. Moreover
\[
 \sum_i\widehat{\deg}E_i=0,\quad R=N+1,\quad
 \mu(F)=-H,\quad\widehat{\deg}K_0=NH.
\]
In the actual orthonormal arithmetic bases,
\[
 Q=I_N,\quad M=N,\quad\Delta=1,\quad
 \eta=0,\quad e_*=e=\frac1{N+1}.
\]
The determinant height in (4.1) is zero and the image index is one.
The kernel degree is the entire obstruction.
The centered rank inequality is sharp on that kernel:
\[
 p=\frac1{N+1},\quad q=0,\quad a^2=\frac1N,\qquad
 p=a\sqrt{p(1-p)}.
\]
There is therefore no bound for the target slope from the adjusted
source mean, map heights and a fixed positive frame error alone.
Replacing \(\mathbf Z\) by the ring of integers of any fixed CM field,
with these same basis norms at every embedding, preserves every
normalized degree and height calculation.

### A perfect full frame need not survive the target cut

In \(\mathbf C^3\), take the orthonormal columns
\[
 T_1=(3/5,0,-4/5),\quad T_2=(4/5,0,3/5),\quad
 T_3=(0,1,0),
\]
and retain only the first two target coordinates. All projected maps
are nonzero, but the first two images span one line:
\[
 \frac{2}{3}>\frac{1}{2}.
\]
Thus (1.1) fails although the full frame has \(\Delta=\eta=0\).
It is compatible with integral arithmetic maps
\(f_1=f_2:1\mapsto(1,0)\), \(f_3:1\mapsto(0,1)\);
the allowed invertible source-basis factors are \(3/5,4/5,1\).
Give the target basis norms \(e^{-H},e^{2H}\), and give each source
the norm of its corresponding target vector. The maps have height
zero, the source mean slope is zero, but \(\mu(F)=-H/2\).
Adding further coordinate columns makes the lost target fraction
arbitrarily small while preserving a proportional-rank obstruction.
Consequently a positive target cut cannot simply be erased from a
frame argument, even when all individual arithmetic maps are injective.

## 6. Actual source compatibility and the remaining alternative

The pinned interface separates the analytic matrices from arithmetic
metrics. *FrameTraceRatioFinEquiv*, lines 59–90, gives actual integral
maps and their height bounds, but asks only that the matrices \(Y_i,Y'\)
changing the comparison bases be invertible. Its first-row identity is
\[
 A_i^{\rm first}=Y'^{-1}\,\sigma(f_i)\,Y_i.
\]
The arithmetic metric matrices are separate objects.
*TopDensityNGeSixteen*, lines 679–689, instantiates this interface with
the actual source lattices and the final dual target lattice.

The source period matrices are taken in orthonormal analytic bases:
*TopDensityNGeSixteen*, lines 1004–1015.
The Bessel identity permits nonzero word-dependent constants,
*GlobalTheoremInputs*, lines 65–67.
The actual bridge at *TopDensityNGeSixteen*, lines 1245–1258, absorbs
their inverses into the source change of basis. These statements are
enough for rank arguments and for the optimal normalization (3.1).
They do not supply integral orthonormal source vectors, determinant
bounds for all the basis changes, or an absolute arithmetic degree.
The period normalization
\[
 T_u=c_u^{-1/2}P_u,\qquad
 c_u=\operatorname{vol}(N_u)\operatorname{vol}(H_u)/\dim\pi_u
\]
is the one recorded in the energy note; it must not be mistaken for a
permitted rescaling of the integral arithmetic map.

The ordinary height in (1.2) is half the source squared-norm height:
*StatementPl*, lines 55–65. This factor agrees with the corresponding
factor of two for arithmetic slopes.

Finally, the W10 lattice is the selected cuspidal core at each
nonterminal stage, as identified in
[the geometric core note](geometric-core-lower-bound.md).
It has its prescribed Petersson and period metric and the target
bound \(\nu(E)\ge-T_i-CU\). It is not automatically the final dual
target of the theta frame. Applying (4.3) to that core would require
new integral maps into the core and controlled source generators;
applying (1.2) would require the corresponding rank expansion and
independently controlled adjusted source mean.

The bounded investigation therefore ends at two concrete alternatives:
prove exact proportional expansion for the actual projected maps to
remove the final relative frame penalty, or construct controlled
integral spanning images for the actual W10 core to replace its degree
supplier. Neither follows from the inspected energy and basis contracts.
The geometric mean-volume and section-degree route remains necessary
until such additional arithmetic information is supplied.

## Verification

The source byte hashes, bounded passages, exact matrix examples and
symbolic identities are recorded by
[the checker](../scripts/check_frame_degree_compatibility.py) and
[certificate](../certificates/frame-degree-compatibility.json).
An independent mathematical review passed the rank-expansion slope
theorem, centered projection argument, integer-gap condition and
trace normalization, with the positive-rank, same-embedding and
all-subspace hypotheses retained. The optimum (3.1) was independently
checked by completing the square. The centered slope bound (3.2)
was independently checked, including source truncation, target
overshoot, all zero cases, cancellation of the target-cut height term,
and its sharp perfect-frame example. None of these checks is a Lean
build or an upstream geometric proof audit.
