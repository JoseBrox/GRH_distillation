# The classical height step and the remaining geometric supplier

## Result and status

Zhang's successive-minima inequality supplies the point-to-intersection
step in the remaining base test. It does not supply the heights of the
actual points. The inspected cusp comparison uses only perturbations
\(1/m\), \(m=1,2,\ldots\), so its hypotheses need not be formulated for
every positive rational perturbation.

The precise conditional conclusion is

\[
             \beta_B\ge-(C_h+C_u/2)\Lambda_B.                 \tag{0.1}
\]

The hypotheses below retain the prescribed metric, finite-place
conditions, an all-point height floor, and the signed cusp correction.
No geometric construction node is closed.

## 1. The classical theorem and normalization

Let \(X\) be a projective integral variety of dimension \(n\) over a
number field \(K\). For a metrized line bundle use

\[
 D(\bar L)=\deg_LX,\qquad
 I(\bar L)=\frac{\widehat{\deg}(\bar L^{n+1})}{[K:\mathbf Q]},\qquad
 h_{\bar L}(X)=\frac{I(\bar L)}{(n+1)D(\bar L)}.              \tag{1.1}
\]

Point heights are divided by the absolute degree of the point's field.
Suppose the underlying line bundle is ample and its metric is relatively
semipositive. For a smooth Hermitian model, this means semipositive
curvature at the infinite places and nonnegative degree on each curve
in each finite fibre. The metric is conjugation invariant. Relative
semipositivity does **not** impose nonnegative horizontal point heights.

The modern form of Zhang's theorem is

\[
 e_1(\bar L)\ge h_{\bar L}(X)
       \ge\frac{e_1(\bar L)+\cdots+e_{n+1}(\bar L)}{n+1},      \tag{1.2}
\]

where the \(e_i\) are the successive minima. It follows that

\[
 h_{\bar L}(P)\ge a\quad(P\in X(\overline K))
 \quad\Longrightarrow\quad I(\bar L)\ge(n+1)aD(\bar L).       \tag{1.3}
\]

Every infimum in each successive minimum is then at least \(a\).
No additional arithmetic nefness assumption is needed. For rational
tensor powers, heights, degrees and intersections scale respectively
by \(m^{-1}\), \(m^{-n}\), and \(m^{-(n+1)}\).

The primary modern reference is Yuan--Zhang,
*Adelic Line Bundles on Quasi-projective Varieties*,
[arXiv:2105.13587v9](https://arxiv.org/abs/2105.13587v9):
Theorem A.4.2, PDF page 234, and its adelic version A.5.2, page 243.
Pages 232 and 240 distinguish relative semipositivity from arithmetic
nefness; page 241 gives the height normalization. Dividing that book's
heights and intersections by \([K:\mathbf Q]\) gives (1.1).

The original reference is Zhang, *Positive Line Bundles on Arithmetic
Varieties*, JAMS 8 (1995), 187--221,
[Theorem 5.2, journal page 208](https://archive.ymsc.tsinghua.edu.cn/pacm_download/355/9113-plav.pdf).
Its printed statement assumes a smooth **relatively semiample** metric.
We use the modern formulation above, rather than silently weakening
the older hypothesis. Yuan--Zhang, page 233, explains this distinction
and the relevant result of Moriwaki.

A lower bound for the essential minimum alone is insufficient here:
\(e_1\ge h_{\bar L}(X)\) points in the other direction. The all-point
bound controls every successive minimum, including the absolute minimum.

## 2. Reciprocal perturbations and a one-sided limit

Fix a component, its actual cutoff \(B\), and its period and finite-place
normalizations. Let \(\bar L_{m,j}\), \(m,j\ge1\), be its prescribed
smooth Hermitian \(\mathbf Q\)-line bundles on projective models of
\(X\). The index \(m\) means perturbation \(1/m\), while \(j\) follows
actual smoothing parameters.

**Proposition.** Suppose \(a,\gamma,u\) are finite real numbers and:

1. For each \(m\), all sufficiently large \(j\) satisfy the positivity,
   conjugation invariance and ampleness conditions of Section 1, with
   \[
       h_{\bar L_{m,j}}(P)\ge a-\gamma/m
                    \quad(P\in X(\overline K)).             \tag{2.1}
   \]
   The threshold may depend on \(m\), but works for all points.
2. Finite real numbers \(d_m,A_m,V_m\) satisfy
   \[
      D(\bar L_{m,j})\longrightarrow d_m,\qquad
      \limsup_j I(\bar L_{m,j})\le A_m+(n+1)V_m.              \tag{2.2}
   \]
3. For the original prescribed intersection \(I_B\) and degree \(d_B>0\),
   \[
      A_m\longrightarrow I_B,\qquad d_m\longrightarrow d_B,\qquad
      V_m\longrightarrow u\,d_B/2.                         \tag{2.3}
   \]

Then

\[
                 \boxed{\frac{I_B}{(n+1)d_B}\ge a-u/2.}     \tag{2.4}
\]

**Proof.** By (1.3) and degree convergence,
\[
 (n+1)(a-\gamma/m)d_m
   \le\liminf_j I(\bar L_{m,j})
   \le A_m+(n+1)V_m.
\]
Let \(m\to\infty\). The convergent sequence \(d_m\) is bounded, so
\(\gamma d_m/m\to0\). Use (2.3) and divide by the positive denominator.
Negative \(a\), \(u\) or \(V_m\) cause no change. \(\square\)

No convergence rate uniform in \(m\) or in the growing family is
required: each datum is fixed before these limits. Convergence of the
corrected intersections in \(j\) is unnecessary; the one-sided upper
comparison suffices. Pointwise lower limits of heights with thresholds
depending on the algebraic point cannot replace (2.1).

## 3. The selected tower's exact normalization

Let the actual component set be finite and nonempty. For a component
\(Z\), put \(s_{B,Z}=I_{B,Z}/((n_Z+1)d_{B,Z})\).
Use the positive integers \(f,q\) and \(p\ge q\) of the tower reduction.
The source identification of its Grassmannian test is

\[
 I^{\mathrm{test}}_{B,Z}
     =s_{B,Z}(d_0+1)v_ZJ,\qquad
 d_0=fpq,\quad J,v_Z>0,\quad v=\sum_Zv_Z.                   \tag{3.1}
\]

Therefore the normalized total test of the preceding note is

\[
 \beta_B=\frac{\sum_ZI^{\mathrm{test}}_{B,Z}}{vfq(d_0+1)J}
        =\frac1{fq}\sum_Z\frac{v_Z}{v}s_{B,Z}.               \tag{3.2}
\]

For \(C_h,C_u,\Lambda_B\ge0\), if the proposition applies on the same
components with

\[
       a_Z=-C_hfq\Lambda_B,\qquad u_Z\le C_ufq\Lambda_B,      \tag{3.3}
\]

then (0.1) follows. More precisely, one can retain the signed mean
\(\sum_Z(v_Z/v)(a_Z-u_Z/2)/(fq)\). The classical theorem does not
provide the required uniformity of \(C_h,C_u\).

All pinned source references below are at
**jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de**.
They verify the source contracts, not their geometric suppliers.

| Mathematical input | Bounded source passage |
| --- | --- |
| Smooth semipositivity, finite-fibre nefness, generic ampleness | FlagIndices, 62--66 |
| Point floors in the interior and boundary complement | FlagIndices, 68--76 |
| Conjugation invariance | FlagIndices, 103--105 |
| Signed cusp mean | FlagIndices, 78--80 |
| Point-height/intersection normalization | StatementsZhangLowerX, 11--17; SlopeLowerBaseSettings, 39--63 |
| Degree and intersection tensor-power normalization | StatementsStokesGeo, 23--33 |
| Exact corrected metric and point-height denominator | CpRegPhRegOfNonneg, 67--90 |
| Corrected intersection upper comparison | StatementsStokesGeo, 38--49, 59--66 |
| Only reciprocal perturbations in the deduction | PStokesLimit, 16--24, 59--81 |
| Signed limit \(u\,d_B/2\) | PStokesLimit, 68--81 |
| Test identification (3.1) | HasBaseDegreeSettingStrict, 21--24; SlopeLowerBaseSettings, 101--108 |

The generic-ampleness predicate uses positive top intersection on
each positive-dimensional subvariety; interpreting this as ampleness
uses the usual Nakai--Moishezon criterion. The classical theorem is
applied to smooth corrected metrics, not directly to the singular
original cusp metric.

The only new factor \(1/2\) in this deduction is the explicit cusp
limit. The point-height theorem divides by the point degree, and
rational tensor powers scale linearly. Over \(\mathbf Q\), the
field-degree factor in (1.1) is one; viewing a number-field model
over \(\mathbf Z\) puts the same factor into its geometric degree.

## 4. The genuine surviving work

One must realize the prescribed reciprocal regularizations, prove their
all-point height floor including the boundary, and establish the
one-sided metric comparison and signed cusp limit with the required
uniform constants. The test identity (3.1) must concern those same
intersections.

The classical theorem supplies the generic implication from point
heights to top intersection. It supplies none of those geometric
premises. Multiplying all norms of an ample relatively semipositive
bundle by \(e^c\) preserves relative positivity and ampleness but
subtracts \(c\) from every normalized point and variety height.
Hence relative positivity alone cannot give a numerical height floor.

Bounds for an auxiliary \(L\)-function can control a scalar in
\(\Lambda_B\), after the metric and point-height comparisons are
established. They do not identify the prescribed metric.

## Verification

The companion certificate records pinned source files and both primary
PDFs with exact inspected passages/pages. Zhang's original theorem
was read from the rendered scan; the modern definitions, normalization
and theorem were read in the pinned v9 PDF. Exact scaling and signed
limit algebra supplement the proof. No Lean replay, upstream geometric
audit, or actual quantitative base-test supplier is claimed.

An independent root review checked Sections 1--4, the complete TeX
insertion, and the modern primary reference's definitions,
normalization and theorem. The finite nonempty component set and finite
limit constants were made explicit following that review. This review
does not establish the geometric hypotheses retained above.
