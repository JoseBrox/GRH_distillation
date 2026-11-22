# Trace comparisons with a prescribed normalization

## Mathematical result

The trace comparison can use a positive number fixed before the theta
maps are evaluated. It need not divide by their unknown total squared
norm. This has two consequences: a sufficiently small source defect
proves nonvanishing, and restrictions can be estimated without dividing
by an unknown surviving mass. The arithmetic heights and lattices are
unchanged. The required bounds for the actual maps remain to be proved.

This is an alternative sufficient route. Bounds normalized by the
actual mass do not, by themselves, give a bound at a prescribed scale.

## 1. A comparison valid even for zero maps

Let \(T_i:V_i\to W\) be finitely many maps of finite-dimensional
Hermitian spaces. Put \(R=\sum_i\dim V_i>0\), \(D=\dim W>0\), and

\[
 S=\bigoplus_iT_i^*T_i,\qquad Q=\sum_iT_iT_i^*,\qquad
 M=\operatorname{tr}S=\operatorname{tr}Q\ge0.
\]

Choose any \(c>0\), independently of whether the maps vanish, and set

\[
 g_c=\frac{\operatorname{tr}((c/R)I-S)_+}{c},\qquad
 b_c=\frac{\operatorname{tr}(Q-(c/D)I)_+}{c}.
 \tag{1}
\]

For a self-adjoint operator \(A\), its positive part \(A_+\) has the
positive eigenvalues of \(A\) and zero in the remaining eigenspaces.
The elementary variational identity is
\(\operatorname{tr}A_+=\max_{0\le P\le I}\operatorname{tr}(PA)\).

**Theorem 1.** Suppose \(V_i'\subseteq V_i\), \(W'\subseteq W\), and
\(T_iV_i'\subseteq W'\). Then

\[
 \frac{\sum_i\dim V_i'}R-\frac{\dim W'}D\le g_c+b_c.
 \tag{2}
\]

Moreover,

\[
 c(1-g_c)\le M\le c(1+b_c).
 \tag{3}
\]

In particular, \(g_c<1\) proves that at least one map is nonzero.
For zero maps, \(g_c=1\) and \(b_c=0\); all assertions remain valid.

*Proof.* Let \(P=\bigoplus P_i\) and \(P'\) be the orthogonal
projections onto these subspaces. If their normalized dimensions are
\(p,q\), the variational identity gives

\[
 c(p-g_c)\le\operatorname{tr}(PS)
 =\operatorname{tr}\sum_i T_iP_iT_i^*
 \le\operatorname{tr}(P'Q)\le c(q+b_c).
\]

Here the image inclusion supplies the middle inequality. Taking the
identity projections separately gives (3). No division by \(M\) occurs.

**Arithmetic consequence.** Let the \(T_i\) represent the same integral
maps \(f_i:E_i\to F\) of Hermitian lattices at one complex embedding,
in individual source bases and a common target basis. Assume

\[
 h(f_i)\le h_i,\quad
 R^{-1}\sum_i r_i(\mu(E_i)-h_i)\ge s,\quad
 \mu_{\max}(E_i)-h_i\le s+U,\quad
 \mu_{\min}(F)\ge s-H,
\]

where \(U,H\ge0\), heights use the actual arithmetic norms, and
\(h(0)=-\infty\). Then

\[
 s-\mu(F)\le\min\{H,(g_c+b_c)(U+H)\}.                 \tag{4}
\]

Indeed, rescale the source metrics by \(e^{h_i}\). The map heights
become nonpositive and the maps preserve the slope filtrations. On
\([s-H,s+U]\), write their normalized ranks as \(p(t),q(t)\).
The source mean and maximum give \(\int p\ge H\), while the target
minimum gives \(\mu(F)\ge s-H+\int q\). Integrating (2) proves (4);
the target minimum supplies the bound by \(H\). This includes \(U+H=0\).
The argument is the existing slope proof with \(c\) in place of \(M\).

If a more direct estimate gives
\(Q\le(1+\lambda)cD^{-1}I+E\), with \(E\ge0\),
\(\operatorname{tr}E\le\varepsilon c\), and \(\lambda\ge0\), the
same integration gives the stronger sufficient bound

\[
 s-\mu(F)\le
 \min\left\{H,\frac{g_c(U+H)+\lambda H+
                      \varepsilon(U+H)}{1+\lambda}\right\}.       \tag{5}
\]

## 2. Both restrictions with known dimension fractions

Let \(J_i:V_i^0\to V_i\) be isometries, and let \(\Pi\) be an
orthogonal projection on \(W\). Put

\[
 R_0=\sum_i\dim V_i^0>0,\quad n=\operatorname{rank}\Pi>0,
 \quad r=R_0/R,\quad v=n/D,
\]

and \(T_{i,0}=\Pi T_iJ_i\). These are the actual restricted maps.
Define their defects \(g_0,b_0\) by (1), with dimensions \(R_0,n\)
and the **prescribed** positive normalization
\(c_0=c\max(r,v)\).

**Theorem 2.** With \(g=g_c\), \(b=b_c\), one has

\[
 g_0+b_0\le
 \frac{g+2b+1-\min(r,v)}{\max(r,v)},\qquad
 M_0:=\sum_i\|T_{i,0}\|_{\rm HS}^2
       \ge c(r+v-1-g-b).                               \tag{6}
\]

Thus \(r+v>1+g+b\) proves nonvanishing of the restricted family.
There is no assumed lower bound on \(M\) or \(M_0\).

*Proof.* Put \(Q'=\sum_iT_iJ_iJ_i^*T_i^*\le Q\). The mass removed
by the target projection satisfies

\[
 L_t=\operatorname{tr}((I-\Pi)Q')\le c(1-v+b).
\]

Compression does not increase a positive trace. The source compression
has trace at least \(c(r-g)\), which proves the mass estimate. More
generally, for any final normalization \(c_0=c\theta\), \(\theta>0\),
the variational identity and \((A+B)_+\)'s trace subadditivity give

\[
 g_0\le\frac{g+1-v+b+(\theta-r)_+}{\theta},\qquad
 b_0\le\frac{b+(v-\theta)_+}{\theta}.                  \tag{7}
\]

For the first inequality, compress \((c/R)I-S\), add the positive
operator lost at the target, then account for the scalar threshold
change. For the second, use \(Q_0\le\Pi Q\Pi\) and account for the
target threshold change. Substitution of \(\theta=\max(r,v)\)
proves (6). Only the original arithmetic restrictions are used.

## 3. Why the prescribed normalization can be better

For \(T=\operatorname{diag}(1,1,0)\) on \(\mathbb C^3\), the choice
\(c=3\) gives \(g_c=1/3\), \(b_c=0\). Normalization by the actual
mass \(M=2\) instead gives \(g_M=b_M=1/3\). The prescribed comparison
therefore costs \(1/3\), rather than \(2/3\). Its constant is sharp:
take \(V'=\ker T\) and \(W'=0\) in (2).

The restriction bound is also attained. Start with the identity of
\(\mathbb C^4\), \(c=4\), and restrict the source and target to
different coordinate three-planes with two-dimensional intersection.
The resulting map is the preceding partial identity. Formula (6)
gives exactly \(1/3\), and its mass lower bound is exactly \(2\).

Actual-mass bounds cannot determine an absolute calibration: scalar
maps \(T=tI\), \(t\ne0\), have \(g_M=b_M=0\) for every \(t\), but
at the fixed choice \(c=R=D\) their defect sum is \(|1-|t|^2|\).
Their arithmetic heights must not be changed to conceal this issue.

## 4. Effect on the proof program

The ordinary arithmetic model still has to supply the integral maps,
their local divisibility, prescribed metrics and source/target cuts.
On the route proving small defects at a prescribed positive scale,
nonvanishing follows from (3) or (6); it is not an additional prerequisite
for the slope argument. In the theta construction the natural candidate
is the mass of the unfolded seed spaces. Identifying that mass is
separate from estimating the arithmetic periodization and its other
rational orbits. No such smallness is inferred here.

The main manuscripts retain the actual-mass comparison as another valid
choice, including its centered squared-energy refinement. At each finite
construction one may use whichever **proved** arithmetic bound is smaller.
No existing RH or GRH blueprint node is completed by this theorem alone.

## Verification

The proofs above are general. The companion script checks exact rational
examples, including zero maps, strict and non-strict nonvanishing cases,
both orders of retained fractions, and the sharp partial-identity example.
Those finite checks supplement the proofs. The existing slope-filtration
argument is in `paper/shared/trace-slope.tex`; this result changes its
matrix normalization, not its arithmetic hypotheses. No new assertion
about a Lean theorem or a full Lean replay is made.
