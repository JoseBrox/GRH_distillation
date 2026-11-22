# One unipotent group and the exact arithmetic periodization operator

## Result and scope

The unipotent groups displayed separately for different words in the
period construction are **the same group**. Their characters, stabilizers,
arithmetic quotients, and normalizing volumes still depend on the word.
This gives a common Fourier analysis and an exact common Hilbert space
for the original Poincare seeds. The remaining estimate is the norm of
arithmetic periodization on the actual finite seed spaces, with the
prescribed source and target restrictions.

The statements below retain all rational double-coset contributions.
They do not prove a calibrated global norm bound, integral period-map
existence, or a new RH or GRH node. Both routes can use the reduction
whenever they use this same period construction.

All source references are to `jsmorph/rh` at
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

## 1. The common group and its varying characters

Let \(E/F\) be a CM extension and \((V,h)\) a nondegenerate Hermitian
space, with \(h\) conjugate-linear in its first argument. Fix hyperbolic
pairs \(e_1,\ldots,e_r,f_1,\ldots,f_r\), with
\(h(e_i,f_j)=\delta_{ij}\), and write
\(X=\langle e_i\rangle\) and
\(W=\langle e_i,f_i\rangle^\perp\).
The source vectors \(z_u\) lie in \(W\). Over the real or finite adelic
coefficient algebra, its displayed definition of \(N_u\) is

\[
\begin{split}
(n-1)e_i&\in\langle e_j:j<i\rangle,\\
(n-1)z_u&\in X,\\
(n-1)y&\in X\quad(y\in X^\perp).
\end{split}                                                   \tag{1}
\]

**Proposition 1.** The middle condition is redundant. Consequently every
\(N_u\) equals the group \(N\) defined by the first and last conditions.

**Proof.** Since \(z_u\in W\subset X^\perp\), the last condition applies
to \(z_u\). The converse inclusion follows by retaining the first and
last conditions from (1). This argument works over the original finite
adelic algebra, not just over its field factors. \(\square\)

For \(r\ge1\), put \(v_{u,i}=e_{i+1}\) for \(i<r\) and
\(v_{u,r}=z_u\). With the source level denominator \(m>0\) and its
fixed global additive character \(\Psi_E\), the character of \(N\) is

\[
\chi_u(n)=\Psi_E\left(m^{-1}\ell_u(n)\right),\qquad
\ell_u(n)=\sum_{i=1}^r h(f_i,nv_{u,i}).                         \tag{2}
\]

The source real and finite formulas are exactly the corresponding
components of (2); their compatibility with the rational diagonal is
retained. Upper triangularity on the \(e_i\) shows
\(\ell_u(nn')=\ell_u(n)+\ell_u(n')\): in the coefficient of \(e_i\)
only the preceding simple-root coefficient and the diagonal coefficient
one contribute. The same calculation applies to \(z_u\) in the last
slot. Thus \(\chi_u\) is a unitary character, trivial on \(N(F)\).
For two words,

\[
\frac{\chi_u(n)}{\chi_v(n)}=
\Psi_E\left(m^{-1}h(f_r,n(z_u-z_v))\right).                    \tag{3}
\]

Distinct vectors in \(W\) give distinct characters. Indeed, for
\(w\in W(\mathbb A_F)\), the unitary transvection

\[
 e_r\mapsto e_r,\qquad
 y\mapsto y-h(w,y)e_r\ (y\in W),\qquad
 f_r\mapsto f_r+w-\tfrac12h(w,w)e_r                            \tag{4}
\]

fixes the other hyperbolic pairs and belongs to \(N\). In (3) its
argument is \(-m^{-1}h(w,z_u-z_v)\). Nondegeneracy of \(h|_W\) and
nontriviality of \(\Psi_E\) prove the assertion. The division by two
is in characteristic-zero local fields; no integral transvection at
the dyadic places is claimed. For \(r=0\), (1) instead gives the trivial
group and the empty sum gives the trivial character.

The source does not require the displayed vectors \(z_u\) to be
pairwise distinct. Words with the same vector therefore belong to the
same character space; their compact representation types require a
separate comparison. Even for distinct characters, the group fixing
\(e_i,f_i,z_u\), and its arithmetic column space, can vary with \(u\).

On the compact quotient \(N(F)\backslash N(\mathbb A_F)\), normalized
to volume one, distinct characters are orthonormal. Translation proves
orthogonality, so Bessel's inequality gives, whenever the integral is
defined,

\[
\sum_{\chi\in\mathcal X}
\left|\int_{N(F)\backslash N(\mathbb A_F)}
       f(ng)\overline{\chi(n)}\,dn\right|^2
\le \int_{N(F)\backslash N(\mathbb A_F)}|f(ng)|^2\,dn.         \tag{5}
\]

Here \(\mathcal X\) is a set of distinct characters, so repeated
words of one character are not counted repeatedly. Compactness follows
by a central filtration of the characteristic-zero unipotent group with
additive successive quotients and compactness of
\(\mathbb A_F/F\); for the latter see B. Conrad,
[A lattice in the adele ring, section 2](https://virtualmath1.stanford.edu/~conrad/248APage/handouts/adelelattice.pdf).
Equation (5) is an identity on the unipotent quotient at a fixed \(g\).
It does not assert that this Fourier operation is an orthogonal
projection on the automorphic quotient.

## 2. The exact normalizing constants

In this section \(\mu_{N,u}\), \(F_{N,u}\), \(\mu_{H,u}\), and
the Weil quotient measure are the source's **archimedean** factors.
The finite adelic ambient and level measures remain fixed. These
fundamental regions are not the full adelic quotient appearing in (5).
Keep the original measures and put

\[
c_u=\frac{v_Kv_{N,u}v_{H,u}}{d_u}>0,\qquad
v_K=\operatorname{vol}(K_2),\quad
v_{N,u}=\mu_{N,u}(F_{N,u}),\quad
v_{H,u}=\mu_{H,u}(H_u),\quad d_u=\dim\pi_u.                  \tag{6}
\]

Thus the source's \(\operatorname{vol}(N_u)\) already includes
\(v_K\). Equality of the groups does not imply equality of their
chosen Haar measures, lattice fundamental regions, or constants (6).
Comparison with the arithmetic normalization retains the stated
identification of \(d_u\) with the dimension prescribed by the highest
weight; it is not inferred from notation alone.

One common Haar measure on \(N_\infty\) may nevertheless be used without
changing any normalized period matrix. Write
\(\mu_{N,u}=t_u\mu_N\), \(t_u>0\). The Weil quotient measure changes
to \(\nu'_u=t_u\nu_u\). If \(W_u\) is the original unit-norm
Whittaker vector, set \(W'_u=t_u^{-1/2}W_u\). Then it still has squared
integral one for \(\nu'_u\), while

\[
\Phi'_u=t_u^{-1/2}\Phi_u,\qquad
P'_u=t_u^{-1/2}P_u,\qquad c'_u=c_u/t_u,
\qquad \frac{P'_u}{\sqrt{c'_u}}=\frac{P_u}{\sqrt{c_u}}.        \tag{7}
\]

This is an auxiliary analytic description of the same normalized
operator. The original integral map \(P_u\), its arithmetic lattices,
metrics and height bounds remain fixed. In particular (7) is not a
license to replace that integral map by \(P'_u\) in a height estimate.

## 3. A genuine common Hilbert space

Fix a finite word family. Write \(G=G(\mathbb A_F)\), \(\Gamma=G(F)\), and let
\(\Delta_u\le\Gamma\) be the source's rational stabilizer. The
scalar seed \(\Phi_u(a)\) is left \(\Delta_u\)-invariant. Set
\(Y=\Gamma\backslash G\) and \(X_u=\Delta_u\backslash G\), with
quotient measures induced from the same ambient Haar measure. Assume
the source's fundamental-domain and absolute-folding hypotheses.
In particular, for each vector in a basis of the finite column space,

\[
 y\longmapsto\sum_{\delta\in\Delta_u\backslash\Gamma}
           |\Phi_u(a)(\delta s(y))|\quad\hbox{belongs to }L^2(Y), \tag{8}
\]

where \(s\) is a measurable section. The source folding estimate,
applied to the nonnegative seed \(|\Phi_u(a)|\), is one way to supply
(8). This is stronger than merely asserting conditional cancellation
of the Poincare series. It implies that each seed lies in \(L^2(X_u)\).

**Proposition 2.** There is a unitary identification

\[
\mathcal U:\bigoplus_uL^2(X_u)\ \longrightarrow
 L^2\!\left(Y,\bigoplus_u\ell^2(\Delta_u\backslash\Gamma)\right),
\qquad
(\mathcal U f)_{u,\delta}(y)=f_u(\delta s(y)).                \tag{9}
\]

**Proof.** The sets \(\delta s(Y)\), for cosets
\(\Delta_u\delta\), partition a fundamental region for \(\Delta_u\).
Left invariance of the ambient Haar measure gives
\(\int_{X_u}|f_u|^2=\int_Y\sum_\delta|f_u(\delta s(y))|^2\).
The same partition constructs the inverse, proving surjectivity.
Changing representatives or the section permutes the fibre coordinates.
For vector-valued seeds covariant under a unitary representation of
\(\Delta_u\), one uses the associated bundle and the induced unitary
cocycle as well; dropping that cocycle would be incorrect. The actual
scalar seeds here are invariant, as required in their source contract,
because the compact coefficient has already been contracted. \(\square\)

For the finite direct sum \(\mathcal C=\bigoplus_u C_u\), define

\[
(Aa)_{u,\delta}(y)=c_u^{-1/2}\Phi_u(a_u)(\delta s(y)),\qquad
\mathcal Fv(y)=\sum_{u,\delta}v_{u,\delta}(y).                \tag{10}
\]

The domain of \(\mathcal F\) used here consists of vectors for which
the sum of absolute values belongs to \(L^2(Y)\). Assumption (8) places
\(A\mathcal C\) in this domain. The normalized synthesis is exactly

\[
                    Sa=\sum_uc_u^{-1/2}P_u a_u=\mathcal F Aa. \tag{11}
\]

The unitary map in (9) is unconditional under the quotient hypotheses.
The seed map \(A\) is isometric only if the **actual** one-cell identity
\(\int_{X_u}\Phi_u(a)\overline{\Phi_u(b)}=c_u\langle a,b\rangle\)
holds with the chosen inner-product convention. When \(\pi_u\) is
irreducible and the corresponding measure decomposition is supplied,
compact Schur orthogonality gives
its factor \(v_{H,u}/d_u\), the unit norm of \(W_u\) gives one, and
the remaining factors are \(v_Kv_{N,u}\). Finite stabilizer weights or
a different column metric cannot simply be omitted. Equations (9)--(11)
do not assume this extra isometry or change the original column metric.

## 4. Every orbital contribution remains

Under the absolute unfolding hypotheses, expansion of (11) gives

\[
\begin{split}
\|Sa\|^2={}&\sum_{u,v}\frac1{\sqrt{c_uc_v}}
\sum_{\gamma\in\Delta_u\backslash\Gamma/\Delta_v}
\int_{(\Delta_u\cap\gamma\Delta_v\gamma^{-1})\backslash G}
\Phi_u(a_u)(g)\,
\overline{\Phi_v(a_v)(\gamma^{-1}g)}\,dg.                   \tag{12}
\end{split}
\]

This is the source's double-coset formula with its exact normalization.
In particular, (9) has not made different automorphic images
orthogonal. Common-unipotent Fourier orthogonality can kill the identity
cell for distinct \(\chi_u\), when the compatible quotient
disintegration is used: its integral along
\(N(F)\backslash N(\mathbb A_F)\) contains
\(\chi_u\overline{\chi_v}\). Nonidentity cells involve intersections
with conjugate unipotent groups, so (5) does not remove them.

The obstruction to treating (11) as a free Bessel inequality is exact.
If \(h\ne0\) lies in \(L^2(Y)\), its pullback satisfies

\[
\|h\circ(X_u\to Y)\|_{L^2(X_u)}^2
=[\Gamma:\Delta_u]\,\|h\|_{L^2(Y)}^2.                       \tag{13}
\]

The value is infinite when the index is infinite. In the present
isotropic construction, for \(r\ge1\) this infinitude has an explicit
proof. For every \(t\in E\) with \(\bar t=-t\), the unitary map
\(e_1\mapsto e_1+t f_1\), fixing \(f_1\) and the orthogonal
complement of this hyperbolic plane, is rational. Two such maps have
the same \(\Delta_u\)-coset only if their parameters agree, since
every element of \(\Delta_u\) fixes \(e_1\). There are infinitely
many such parameters. This applies also to the common cover
\(N(F)\backslash G\).

Consequently the formal adjoint of unrestricted fibre summation is
the repeated constant fibre, which is not in \(\ell^2\). The operator
\(\mathcal F\) is unbounded on the full space in (9). Its restriction
to the actual finite seed space is well-defined by (8); estimating
that restriction is the arithmetic problem. This identifies an actual
covering issue, rather than an obstruction manufactured from unrelated
matrices.

## 5. Actual restrictions and a calibrated sufficient bound

Let \(J_u:C'_u\hookrightarrow C_u\) be the prescribed isometric
source restrictions and \(\Pi:H\to H_0\) the actual orthogonal target
projection. Put \(J=\bigoplus_uJ_u\), \(n=\dim H_0\), and

\[
S_0=\Pi\mathcal F AJ,\qquad
Q_0=S_0S_0^*=\sum_uc_u^{-1}\Pi P_uJ_uJ_u^*P_u^*\Pi,
\qquad M_0=\operatorname{tr}Q_0>0.                           \tag{14}
\]

For example, a one-unfolding description of its adjoint is

\[
\langle c_u^{-1/2}P_uJ_u a,h\rangle_Y
=c_u^{-1/2}\int_{X_u}\Phi_u(J_u a)(g)\overline{h(g)}\,dg
\quad(h\in H_0),                                           \tag{15}
\]

where the pairing is linear in its first argument. Absolute convergence
follows from (8) and Cauchy--Schwarz on \(Y\); the pullback of \(h\)
need not belong to \(L^2(X_u)\). For target restriction, the exact
quadratic form is \(\|\Pi Sa\|^2=\|Sa\|^2-\|(1-\Pi)Sa\|^2\).
Thus one must not insert \(\Pi\) into a seed or discard orbital
terms without a justified identity.

Here is a concrete sufficient summation theorem to seek. Suppose positive
measurable weights \(w_{u,\delta}(y)\) satisfy

\[
\sum_{u,\delta}w_{u,\delta}(y)\le L\quad\text{almost everywhere},
\qquad
\int_Y\sum_{u,\delta}
\frac{|\Phi_u(J_u a_u)(\delta s(y))|^2}
     {c_u w_{u,\delta}(y)}\,dy
\le B\sum_u\|a_u\|^2.                                      \tag{16}
\]

Weighted Cauchy--Schwarz, followed by \(\|\Pi\|\le1\), proves
\(Q_0\le LB I_{H_0}\). If
\(LB\le(1+\varepsilon)M_0/n\), then

\[
\frac{\operatorname{tr}(Q_0-(M_0/n)I)_+}{M_0}
\le\frac{\varepsilon}{1+\varepsilon}.                        \tag{17}
\]

Indeed, for \(0\le\lambda\le LB\),
\((\lambda-M_0/n)_+\le(1-M_0/(nLB))\lambda\), and one sums
over eigenvalues. The source trace allowance and the arithmetic height
hypotheses are still required. No weights achieving this calibration
on the actual seed spaces have been proved here. The usefulness of
(16) is that it asks for a sum over one common arithmetic covering,
while retaining the actual metrics, volumes, cuts and total trace.

## 6. Bounded source evidence

| Pinned source | Ranges | Content used |
|---|---|---|
| `HaarTransversals/HidaSetting.lean` | 24--46, 59--66, 106--115, 136--156, 207--231, 267--317, 338--347 | Common flag, redundant condition on \(z_u\), exact characters and rational compatibility, Haar and quotient measures, unit Whittaker norm |
| `HaarTransversals/PoincareInHH.lean` | 60--75, 144--199, 248--263 | Word stabilizers, scalar seed invariance, arithmetic summation, normalizing constant |
| `HaarTransversals/PoincareSeriesSquareIntegrable.lean` | 15--25, 50--81 | Absolute-folding hypotheses and full double-coset formula |
| `FlagStabilizerTensors/PoincareConstantEq.lean` | 50--59 | The factor \(\operatorname{vol}(K_2)\) occurs once in \(c_u\) |
| `FlagStabilizerTensors/ParametersTermRelations.lean` | 38--75, 213--255, 286--294, 319--342 | Original column norm, common target, period maps, isometric arithmetic identification, measure preservation and dimension tie |
| `CuspSpanNormBounds/AdmissibleBoundsFromSource.lean` | 212--244 | Same restricted operator \(Q_0\) |

The checker authenticates the listed immutable files and bounded ranges,
checks the transvection and opposite-root formulas exactly, and checks
finite quotient instances of (9), (12), (13), and the weighted estimate.
These checks supplement the proofs; they do not prove the unsupplied
global period estimate or replay the Lean kernel.
