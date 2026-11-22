# Simultaneous flag-ratio moments and the remaining first-length estimate

## Result and scope

The Casimir identity and derivative estimate used below were already proved
in `paper/sections/recovered/77-dc-section.tex`, Lemma `dc-derivative`,
lines 503--596 at repository revision
`1d6b784075cf61ce5d6b2f1b03cb0196c64130ab`. They are reused, not counted as
a new supplier. The additional result is a simultaneous weighted moment
estimate for the **original** adjacent flag-length ratios. It gives a
smaller first-length parameter reserve in the product-moment argument.

The measure, Bessel map, formal degree and Hilbert norm are retained.
In particular, this argument does not replace the original quotient
measure by a probability measure. Its analytic input is the original
unweighted Bessel norm bound. Its product corollary also needs the
original first-length moment estimate. Neither input is proved by
renaming it or assumed to be the leading-minor estimate itself.

This is a quantitative conditional advance inside the open archimedean
norm node. It does **not** prove the original leading-minor bound or the
weighted orbital bound in
[the target card](global-norm-frontier-archimedean-target.md). In particular,
it does not change the original function defining the noncompact and
cloud gap budget. Whole-node counts remain RH **6/9**, GRH **17/31**.

## 1. Derivative energy on longer words

Let $s_i\in\{1,-1\}$, and let $E_{ij}$ act on a common invariant smooth
domain in a unitary representation of $U(p,q)$, where $n=p+q$. Use the
matrix-unit convention
\[
 [E_{ij},E_{ab}]=\delta_{ja}E_{ib}-\delta_{bi}E_{aj},\qquad
 E_{ij}^{*}=s_i s_jE_{ji}.
\]
Put
\[
 \Omega=\sum_{i,j}E_{ij}E_{ji},\qquad
 \Omega_K=\sum_{s_i=s_j}E_{ij}E_{ji},\qquad \Omega=c_G I.
\]
The existing Casimir calculation gives
\[
 \sum_{i,j}\|E_{ij}v\|^2
   =2\langle v,\Omega_Kv\rangle-c_G\|v\|^2.                 \tag{1}
\]
The identity follows equally by inserting the adjoint relation in the
left side and relabelling the two indices; there is no factor $n^2$.

Let $S_0$ be a finite-dimensional compact-invariant subspace with
$\Omega_K\le A_0^2I$, $A_0\ge0$. Let $S_d$ span all matrix-unit words of
length at most $d$ applied to $S_0$. Then
\[
             \Omega_K|_{S_d}\le(A_0+2nd)^2 I.                 \tag{2}
\]
Here is a proof that does not require a new highest-weight calculation.
On $\operatorname{End}(\mathbb C^n)$ with its Hilbert--Schmidt norm, the
compact action is $T\mapsto[e_{ij},T]$, and
\[
 \sum_{s_i=s_j}\|[e_{ij},T]\|_{\rm HS}^2
 \le 2\sum_{i,j}\bigl(\|e_{ij}T\|_{\rm HS}^2+
                         \|Te_{ij}\|_{\rm HS}^2\bigr)
 =4n\|T\|_{\rm HS}^2\le(2n)^2\|T\|_{\rm HS}^2.
\]
The triangle inequality for the row of compact operators on a tensor
product adds the square roots of their energy bounds. The map
$e_{ij}\otimes v\mapsto E_{ij}v$ intertwines the compact actions by the
commutator relation. It need not be an isometry: its image only inherits
the **Casimir eigenvalues**, which is enough. Indeed, on finite-dimensional
unitary compact modules the Casimir is self-adjoint, the kernel is
invariant, and the image is spanned by images of its eigenspaces.
Adding $S_d$ to this image proves (2) by induction.

For the numerical range needed here assume
\[
 b\ge B_0\ge16n^3,\quad c_G\ge-n^3,\quad
             A_0\le4nB_0+16n^3.                              \tag{3}
\]
For $d\le n^3$, (2) implies $A_0+2nd\le6nB_0$. Thus
\[
 \sum_{i,j}\|E_{ij}v\|^2
 \le(72n^2B_0^2+n^3)\|v\|^2
 \le73n^2B_0^2\|v\|^2
 \le b^4\|v\|^2\qquad(v\in S_d).                           \tag{4}
\]
These inequalities are deliberately coarse; their purpose is to permit
words of total order $n^3$ with the same power $b^4$.

For comparison with the source, its parameter shape gives
$|\mu_i|\le3B_0$, $B_0\ge10^6n^7$, and
$c_G=\sum\mu_i^2-\sum\rho_i^2\ge-n^3$. The compact part of its level
condition has
$A_0=\sqrt{c_K}+4nj$ with $j\le4n^2$.
The lowest compact weight is $\mu+\rho-2\rho_K$, so
$c_K=\|\mu+\rho-\rho_K\|^2-\|\rho_K\|^2\le16nB_0^2$;
each coordinate of $\rho-\rho_K$ has absolute value at most $n$.
This implies (3). The lowest vector used in the flag-product argument
has $j=0$. None of these comparisons supplies the missing Bessel
normalization or first-length estimate.

## 2. The original adjacent-ratio inequality

Write $h(x,y)=x^*Jy$, where $J=J^*=J^{-1}$, and use the usual positive
Euclidean norm. Fix independent vectors $f_0,\ldots,f_r$ such that the
first $r$ span a totally isotropic space, $f_r$ is orthogonal to that
space, and $h(f_r,f_r)=-T<0$. For $g\in U(J)$ set
\[
 v_a=g^{-1}f_a,\quad
 L_a(g)=\operatorname{dist}\bigl(v_a,
                  \operatorname{span}(v_0,\ldots,v_{a-1})\bigr),
 \quad R_a(g)=\frac{L_{a+1}(g)}{L_a(g)}\quad(a<r).
\]
All lengths are positive. Use the original unipotent Bessel character,
whose adjacent imaginary coordinate $it$ contributes $\exp(-2it)$.
Let $\sigma$ be a unitary representation on a Hilbert space with a
common invariant smooth domain. Let $\mathcal B$ be a smooth Bessel
functional on that domain, valued in a Hilbert space $W$, and set
\[
                  F_v(g)=\sqrt d\,\mathcal B(\sigma(g)v),        \tag{5}
\]
where $d>0$ is the original formal degree. No rescaling depending on
$v$, $g$ or its weighted integral is allowed.

Then, at every admissible $g$,
\[
       R_a(g)^2\|F_v(g)\|^2
            \le\sum_{i,j}\|F_{E_{ij}v}(g)\|^2.                \tag{6}
\]
To verify the geometry, let $e$ be the Euclidean residual of $v_a$
against its predecessors, and $p$ the residual of $v_{a+1}$ against
$v_0,\ldots,v_a$. Put
\[
             w=-iJp,\qquad X=e w^*J-w e^*J.
\]
Then $X^*J+JX=0$, $h(e,e)=h(e,w)=0$, $X^3=0$, and
$\|X\|_{\rm HS}\le2L_aL_{a+1}$. For $j\le a$, $Xv_j=0$;
also $Xv_{a+1}=iL_{a+1}^2e$. On every later flag vector $X$ has
image in the span of the first $a+1$ vectors. On the orthogonal
complement of the isotropic flag it acts trivially modulo that flag.
Consequently $g\exp(tX)g^{-1}$ is in the original unipotent radical.
Its sole nonzero adjacent coordinate is $itL_{a+1}^2$, so its Bessel
character is $\exp(-2itL_{a+1}^2)$.

Differentiating Bessel equivariance gives
\[
 -2iL_{a+1}^2 F_v(g)
       =\sum_{i,j}(QXQ^{-1})_{ij}F_{E_{ij}v}(g),
\]
where the Cayley change of basis $Q$ is unitary. Cauchy--Schwarz,
unitary invariance of the Hilbert--Schmidt norm and the positive lengths
give (6). This is a direct reconstruction of the pinned source's
`BesselCayleySideBound.pointwise`, with an unnormalized rank-two matrix
to avoid square roots in the calculation.

## 3. Simultaneous moments with the unchanged measure

Let $\nu$ be the **original** quotient measure. Assume the functions
below are measurable, and retain the analytic input
\[
           \int\|F_v(g)\|^2\,d\nu(g)\le\|v\|^2             \tag{7}
\]
for all vectors in the word spaces used. This is the original mass
bound, not a definition of $\nu$. In its nonzero Bessel case the source
proves an isometry, but only the inequality is needed here. The zero
Bessel map is included and causes no division by zero.

For every multi-index $\alpha\in\mathbb N^r$ of total degree
$|\alpha|\le n^3$ and $v\in S_0$, (4), (6) and (7) imply
\[
 \int\prod_{a<r}R_a(g)^{2\alpha_a}\|F_v(g)\|^2\,d\nu(g)
                  \le b^{4|\alpha|}\|v\|^2.                 \tag{8}
\]
More generally the same bound holds for $v\in S_s$ when
$s+|\alpha|\le n^3$. Induct on $|\alpha|$. If $\alpha_a>0$,
multiply (6) by the remaining nonnegative ratio product and integrate.
Tonelli and the induction hypothesis bound this by
$b^{4(|\alpha|-1)}\sum_{i,j}\|E_{ij}v\|^2$; (4) proves (8).
Thus no separate Hölder step is needed for each ratio, and no factor
counting the ratios or the matrix units is introduced. The finite
right side proves finiteness of the actual weighted integrals.

## 4. A smaller first-length reserve

Let $A>0$. Suppose separately that the original first-length family supplies
\[
       \int L_0(g)^{2h}\|F_v(g)\|^2\,d\nu(g)
                           \le A^h\|v\|^2.                  \tag{9}
\]
For the source, $n=2r+k+1$, $k\ge1$, $m=2r+2$, and
$A=n^2T b^4(6B_0)^{2m}$. Assume $0\le\ell\le r+1$.
For $\ell=0$ use (7), with no first-length assumption; for $\ell=1$ use
(9) with $h=1$.
For $\ell\ge2$, it suffices to have (9) only at $h=\ell+1$:
\[
 \int\prod_{a<\ell}L_a(g)^2\|F_v(g)\|^2\,d\nu(g)
             \le A^\ell b^{2\ell(\ell-1)}\|v\|^2.           \tag{10}
\]
Indeed
$\prod_{a<\ell}L_a^2=L_0^{2\ell}
\prod_{a=0}^{\ell-2}R_a^{2(\ell-1-a)}$.
Apply Hölder for the measure $\|F_v\|^2d\nu$ with exponents
$(\ell+1)/\ell$ and $\ell+1$. The first factor uses (9) at
$h=\ell+1$. The second uses (8) with
\[
 \alpha_a=(\ell+1)(\ell-1-a),\qquad
 |\alpha|=\frac{\ell(\ell^2-1)}2\le n^3.
\]
The powers of $\|v\|^2$ recombine to $\|v\|^2$. No assumption that
this measure has mass one is used. If $v=0$, the assertion follows
directly from linearity, without invoking Hölder on a normalized measure.

The source instead uses individual moments up to $(r+1)^2$ and obtains
$A^\ell b^{4r\ell}$. Since $\ell-1\le r$, (10) is stronger.
For its integer shift $\eta$, the first-length recursion requires
$\|\eta\|_1+h\le q_0$. Thus the product-moment reserve can be reduced to

| Product order | Required reserve beyond $\|\eta\|_1$ |
|---:|---:|
| $0$ | $0$ |
| $1$ | $1$ |
| $\ell\ge2$ | $\ell+1$ |

For the subsequent exterior-power step, the family is first shifted to
$\eta+1_I$, $|I|=\ell$. The corresponding sufficient reserve is $0$
for $\ell=0$, $2$ for $\ell=1$, and $2\ell+1$ for $\ell\ge2$,
instead of the source's uniform $(r+1)(r+2)$. This is a conditional
improvement **inside that integer-shift construction**. It does not
identify this construction with the original leading-minor Jacquet
norm or license altering the two-branch real-valued gap function in
the target card. All family and noncompact gap hypotheses remain.

## 5. What must be proved next

The analytic mass input (7) must be transferred with the original
formal degree and quotient measures. Its source proof uses a
matrix-coefficient norm identity, absolute convergence, Weil
integration and the normalized Bessel period factorization.
The difficult first-length estimate (9) then needs the original
tensor projection bound and the degree-normalized lowering constants.
These are more substantial obligations than the Hölder simplification.

The present work must not be confused with (9). Ratio control cannot
control the common scale of all lengths: replacing every $L_a$ by
$cL_a$ leaves every ratio unchanged and multiplies the $\ell$-fold
product by $c^{2\ell}$. Similarly, (7) alone controls no unbounded
weight. These are explicit obstructions to closing the leading-minor
target from the result above alone.

## Source and verification record

All Lean entries below are pinned to
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The certificate stores each whole-file SHA-256, Git blob and bounded
excerpt hash. The prefixes are
`J = Development.AbelianVarietyTheory.Proofs.JetHarmonics.`,
`F = Development.AbelianVarietyTheory.Proofs.FlagMeasures.`, and
`B = CompanionTheory.AutomorphicTheory.PieriRules.ThetaBesselIsometries.`.

| Source | Bounded lines | Role |
|---|---:|---|
| `Development.AbelianVarietyTheory.Definitions.Jets.SumIoPr` | 16--30, 53--57 | Level, module and numerical shape definitions |
| `J.ExistsLieUnitaryElementSimpleRoot` | 55--112 | Original flag element and character scale |
| `B.BesselCayleySideBound` | 60--118 | Original pointwise adjacent-ratio estimate |
| `B.FamilySetupCayleyBound` | 78--94, 185--213 | Existing individual-ratio moment induction |
| `B.FamilySetupCayleyRecursion` | 19--49 | First-length recursion and exact shift reserve |
| `F.ProductMomentFirstLengthsLowestVector` | 66--115 | Existing separate Hölder assembly and $(r+1)^2$ reserve |
| `F.BesselExteriorPowerConstantBoundLargeGap` | 34--45 | Additional exterior shift and original $(r+1)(r+2)$ reserve |
| `B.FamilySetupBesselGrowth` | 31--68 | Original mass/isometry input, retained here |
| `B.FamilySetupCayleyMoment` | 110--150, 160--207 | First-length supplier still to reconstruct |
| `Formalism.SharpRestriction.CuspSpanNormBounds.OnePlaceEstimates` | 57--77 | Original leading-minor and derivative targets |

Run `python3 scripts/check_global_norm_frontier_mixed_ratio_moments.py --offline`.
The exact checks verify rank-two flag matrices over rational complex
numbers, the numerical energy inequalities, Hölder exponent identities
and the reserve comparison. They supplement the general proofs above;
they do not prove infinite-dimensional analytic hypotheses or constitute
a Lean build.
