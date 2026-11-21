# Averaged geometry and the combined Riemann-hypothesis estimate

## Result and scope

Three ordinary mathematical simplifications are proved here.

1. Determinant descent preserves the coefficient of the section-degree error. For the actual covering contracts, the constant `2(C_F+C_U)+9` can be replaced by `C_F+C_U+7`, with a sharper expression retaining the actual rank ratio.
2. The component-degree estimate needs a weighted mean height and a weighted first moment of the negative heights. A uniform lower bound for every component height is a sufficient way to obtain these moments, not an intrinsic requirement. An explicit optimized bound replaces the earlier coarse logarithmic estimate.
3. The refined frame comparison can be averaged before estimating its nonlinear terms. Its diagonal-error cost then retains its correlation with the source slope spread, which can be substantially smaller than the target height gap.

All statements keep the actual lattices, metrics and rank weights. They do not establish the remaining mean geometric height theorem, the actual Hilbert--Samuel remainder, or the normalized theta-frame estimates for the growing RH family. In particular, this is a simplification of the sufficient combined estimate, not a completed proof of RH. No Lean build or kernel replay is claimed.

The source revision is `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. The source comparison uses only two small files, downloaded and hash-verified before bounded inspection. Exact paths, hashes and inspected ranges are recorded in [the certificate](../certificates/rh-geometric-combination.json). The existing geometric and frame proofs are in manuscript Section 10, especially `prop:geometric-det-descent`, `prop:geometric-component-average` and `qrh-sharper-slope`.

## 1. Covering descent without doubling the section error

Let \(A,B\) be nonzero Hermitian lattices, of ranks \(a,b\), over a number field. Write \(\nu=2\widehat{\deg}/\operatorname{rk}\), with arithmetic degree normalized by the field degree. Suppose an integral injection
\[
\Phi:A\longrightarrow B^{\oplus n},\qquad n\ge1,
\]
has operator norm at most \(e^\beta\) at every embedding, and \(B\) is spanned over the number field by integral vectors of norm at most \(e^\Lambda\) at every embedding. Assume
\[
0<\beta\le\Lambda,\quad \beta\le U,\quad |T|\le\Lambda,
\quad nb\le(1+\beta/\Lambda)a,
\]
\[
\nu(A)\ge-T-CU,\quad C\ge0,\qquad \mu_0\ge\nu(B)-2\beta.
\]
The symbol \(\mu_0\) here denotes a real core slope in the same squared-norm normalization as \(\nu\); it is not the ordinary half-sized slope. Put \(\lambda=a/(nb)\). Then
\[
\boxed{\mu_0\ge-T-\lambda CU-
  2\beta(1+\lambda)-(1-\lambda)(2\Lambda-T)
  \ge-T-(C+7)U.}\tag{1.1}
\]

**Proof.** Injectivity gives \(\lambda\le1\), while the rank assumption gives \(\lambda\ge(1+\beta/\Lambda)^{-1}\). Determinant descent gives
\[
\nu(B)\ge\lambda(\nu(A)-2\beta)-2(1-\lambda)\Lambda.
\]
Substitute the lower bound for \(\nu(A)\), subtract \(2\beta\), and collect the main term \(-T\). This is the first inequality in (1.1). Further,
\[
(1-\lambda)\Lambda\le\lambda\beta,\qquad
2\Lambda-T\le3\Lambda,
\]
so its error is at most
\[
\lambda CU+(2+5\lambda)\beta\le CU+7U.
\]
This uses the sign \(C\ge0\); a signed actual section error should instead be retained in the first formula. No absolute value of \(-T-CU-2\beta\) has been introduced. That unnecessary absolute value is what doubled \(C\) in the old numerical envelope. ∎

The source dictionary is exact. In `CovolXOfCovol.lean`, `MapsAt` (119--123) supplies \(\Phi\), its norm bound and the upper comparison with the positively shifted rank. `RkAt` (125--126) gives the displayed rank ratio, `GminAt` (128--131) the short spanning set, and `RingAt` (116--117) the final loss \(2\beta\). The size bounds (75--79) give \(\beta\le U\), \(\beta\le\Lambda\) and \(|T|\le\Lambda\). `FlatAt` and `UAt` (135--138) give \(\nu(A)\ge-T-(C_F+C_U)U\). The positive source rank in `DeepGoodAt` (111--114) and injectivity ensure \(n,b>0\). Thus the conclusion of `LowerBoundOfAllEstimates.lowAt_of_cover` (65--105) can be proved with `C_F+C_U+7` under the same contracts and the already proved determinant lemma. Its original numerical step (18--51) gives `2(C_F+C_U)+9`.

The constant 7 is optimal if one retains only these scalar inequalities. For \(\beta=1\), \(\Lambda=N\), \(T=-N\), \(C=0\), \(\lambda=N/(N+1)\), the exact error in (1.1) is \(2+5N/(N+1)\), which tends to 7. These inequalities can also be realized by diagonal Hermitian lattices over \(\mathbf Q\): take \(A\) of rank \(N\) with all basis norms \(e^{-N/2}\), take \(B\) of rank \(N+1\) with its first \(N\) basis norms \(e^{1-N/2}\) and its last norm \(e^N\), and embed on the first coordinates. Set \(\mu_0=\nu(B)-2\). This is an extremal example for the abstract contracts, not an example of the arithmetic-geometric construction.

## 2. A component bound from two height moments

Let the finite nonempty component set have weights \(w_Z>0\), ranks \(r_Z\ge w_Z\), and heights \(h_Z\in\mathbf R\). Put
\[
W=\sum_Zw_Z,\quad R=\sum_Zr_Z,\quad
\mathsf M=\frac1W\sum_Zw_Zh_Z,\quad
\mathsf N=\frac1W\sum_Zw_Z\max(-h_Z,0).
\]
Assume only
\[
\mathsf M\ge-H,\qquad \mathsf N\le c,\qquad H,c\ge0.
\tag{2.1}
\]
Suppose \(A>0\), \(a\ge0\), \(t>a\), and the actual component arithmetic degrees satisfy
\[
d_Z\ge w_Z\{t h_Z-a|h_Z|-A\log(2+|h_Z|)-R_Z\}-C_Z,
\tag{2.2}
\]
where \(R_Z,C_Z\) are allowed to be signed. Define
\[
\beta=t-a>0,\quad H_0=\min(H,c),\quad
y_* =\max\{2+2c-H_0,A/\beta\},
\]
\[
K_*=2ac+A\log y_* -\beta(y_*-2-2c),\qquad
\Gamma=\frac1R\sum_Z(w_ZR_Z+C_Z).
\]
Then \(K_*\ge0\) and
\[
\boxed{\frac{\sum_Zd_Z}{R}\ge-\frac WR K_*-\Gamma
\ge-K_*-\Gamma.}\tag{2.3}
\]

**Proof.** The identity \(|h|=h+2\max(-h,0)\) gives
\(\langle |h|\rangle_w=\mathsf M+2\mathsf N\). Jensen's inequality for the concave logarithm gives
\[
\left\langle t h-a|h|-A\log(2+|h|)\right\rangle_w
\ge \beta\mathsf M-2a\mathsf N
       -A\log(2+\mathsf M+2\mathsf N).
\]
The right side decreases with \(\mathsf N\), so it is at least
\[
\phi(\mathsf M):=\beta\mathsf M-2ac-A\log(2+\mathsf M+2c).
\]
Since \(\mathsf M\ge-\mathsf N\ge-c\), the mean obeys \(\mathsf M\ge-H_0\). The logarithmic argument is therefore at least \(2+c>0\). The function \(\phi\) is strictly convex, with derivative \(\beta-A/(2+\mathsf M+2c)\); hence its minimum over this half-line is \(-K_*\), attained at \(\mathsf M=y_*-2-2c\). At the endpoint \(\mathsf M=-H_0\), \(\phi\) is negative, so \(K_*\ge0\). Summing (2.2), and using \(W\le R\), proves (2.3). ∎

This bound is optimal given only (2.1). For any \(\mathsf M\ge-c\) with \(z=\mathsf M+2c>0\), put mass \(c/z\) at \(-z\) and mass \(1-c/z\) at \(+z\). The mean is \(\mathsf M\), the negative moment is \(c\), and \(|h|\) is constant, so every inequality used in the proof is equality. Omit zero-mass points. The degenerate case \(z=0\) has \(c=\mathsf M=0\) and one point at zero. Apply this construction at the minimizing mean.

The existing geometric hypotheses still imply (2.1): their pointwise bound \(h_Z\ge-c\) gives \(\mathsf N\le c\), and the verified degree-spread/mean-volume argument gives the displayed weighted lower mean with
\[
H=(2\rho-\rho^2)c+(1-\rho)^2X+(1-\rho)c_c.
\]
Thus this is a valid improvement of the already established bound, without a new geometric assumption. A replacement construction could instead prove (2.1) directly and omit both the pointwise lower height and the degree-spread conversion. The two moment estimates must then concern exactly the Hilbert--Samuel weights \(w_Z\), not an unrelated uniform component average.

For comparison, when \(t\ge a+1\) the earlier constant was
\[
K_0=(t-a-1)H+2(a+1)c+A\log\max(A,1)+2.
\]
One always has \(K_*\le K_0\). Indeed,
\(A\log(2+\mathsf M+2c)\le A\log\max(A,1)+2+\mathsf M+2c\), and minimizing the resulting affine lower bound over \(\mathsf M\ge-H_0\) proves the comparison. This does not rely on a numerical experiment.

For the actual raw Hilbert--Samuel statement, retain
\[
C_Z=(r_Z-w_Z)P_Z+r_Zc_Z
\]
as in [the geometric core note](geometric-core-lower-bound.md). The same actual total surplus and twist cost enters \(\Gamma\), with its signs unchanged. The source `SumAt` (158--159) then gives the squared-norm cover slope at least \(-2((W/R)K_*+\Gamma)\). Substituting that bound in the first formula of (1.1) preserves its actual rank ratio and signed remainder before any uniform error bound is taken.

Two boundaries are necessary. A signed mean alone does not suffice: equally weighted heights \(M,-M\) have mean zero while the nonlinear mean in (2.2) tends to minus infinity. With \(A>0\), the condition \(t>a\) is necessary for a lower bound from these two moments alone: take every height equal to \(M\to\infty\). Neither example contradicts the stronger source hypotheses.

## 3. Averaging the refined frame comparison

Let a finite nonempty index set carry probabilities \(p_u>0\). For each \(u\), suppose the **same integral maps and common target basis** satisfy the hypotheses of the manuscript's refined slope theorem. Write their nonnegative source spread and target gap as \(U_u,H_u\), their diagonal defect as \(0\le e_u<1\), their isotropy defect as \(\eta_u\ge0\), and their retained rank loss as \(0\le\delta_u<1\). Put
\[
q_u=\sqrt{e_u},\quad
\mathcal A_u=\frac{U_u\log(1+H_u/U_u)
 +2q_u\{\sqrt{U_u(U_u+H_u)}-U_u\}}{1-q_u},
\quad \mathcal B_u=\eta_uH_u.
\]
Both terms with \(U_u=0\) mean their continuous values zero. The refined pointwise theorem gives
\[
s_u-c_u\le\frac{\mathcal A_u+\mathcal B_u/2+
 \sqrt{\mathcal A_u\mathcal B_u+\mathcal B_u^2/4}}{1-\delta_u}.
\tag{3.1}
\]
Define
\[
v_u=\frac{p_u}{1-\delta_u},\quad
\mathcal A_*=\sum_uv_u\mathcal A_u,\quad
\mathcal B_*=\sum_uv_u\mathcal B_u.
\]
Then
\[
\boxed{\sum_up_u(s_u-c_u)\le
\mathcal A_*+\frac{\mathcal B_*}{2}
 +\sqrt{\mathcal A_*\mathcal B_*+\mathcal B_*^2/4}.}\tag{3.2}
\]

**Proof.** Sum (3.1). Its square-root terms have sum
\[
\sum_uv_u\sqrt{\mathcal B_u(\mathcal A_u+\mathcal B_u/4)}
\le\sqrt{\left(\sum_uv_u\mathcal B_u\right)
             \left(\sum_uv_u(\mathcal A_u+\mathcal B_u/4)\right)}
\]
by Cauchy--Schwarz. This is exactly (3.2). The argument includes zero moments. ∎

One can bound \(\mathcal A_*\) using only four explicit correlated moments. Set
\[
w_u=\frac{p_u}{(1-\delta_u)(1-q_u)},\quad
U_* =\sum_uw_uU_u,\quad H_* =\sum_uw_uH_u,
\]
\[
U_q=\sum_uw_uq_uU_u,\qquad H_q=\sum_uw_uq_uH_u.
\]
Then
\[
\boxed{\mathcal A_*\le
U_*\log(1+H_*/U_*)
 +2\{\sqrt{U_q(U_q+H_q)}-U_q\}=:\mathcal R.}\tag{3.3}
\]
For the first summand use the concavity and degree-one homogeneity of \(U\log(1+H/U)\). For the second use Cauchy--Schwarz in the form
\[
\sum_uw_uq_u\sqrt{U_u(U_u+H_u)}
\le\sqrt{U_q(U_q+H_q)}.
\]
Subtract \(U_q\). No division by \(U_q\) is needed. If \(U_*=0\), every relevant \(U_u\) is zero and (3.3) reads zero. If \(H_*=0\), every height-dependent cost vanishes. The right side of (3.2) is increasing in \(\mathcal A_*\), so \(\mathcal R\) can replace it there.

An alternative useful bound for the mixed term is
\[
\mathcal A_*\le U_*\log(1+H_*/U_*)+
2\min\{\sqrt{E_UH_*},\sqrt{E_HU_*}\},
\]
where \(E_U=\sum_uw_ue_uU_u\) and \(E_H=\sum_uw_ue_uH_u\). This follows from
\(\sqrt{U(U+H)}-U\le\sqrt{UH}\) and two applications of Cauchy--Schwarz. One may use the smaller of this estimate, (3.3), or the actual \(\mathcal A_*\).

The denominators \(1-\delta_u\) and \(1-q_u\) are retained. Small unweighted means of \(\delta_u\) or \(e_u\) cannot replace them. When the source spread is small relative to the target gap, the diagonal term now costs a mixed source-spread/target-gap moment instead of a height gap multiplied by the square root of the diagonal error. If every \(U_u=0\), the sharper endpoint theorem gives directly
\[
\sum_up_u(s_u-c_u)\le
\sum_u\frac{p_u\eta_uH_u}{(1+\eta_u)(1-\delta_u)}.
\]
One may also use this endpoint estimate only on the indices where \(U_u=0\), and (3.2) on their complement. All displayed bounds are homogeneous in the outer weights, so restricting to a subset does not require inserting an artificial normalization factor.

These estimates are conditional on the refined theorem's actual map/frame hypotheses. The source's separately quoted frame inequality alone, with its extra \(\log|W_u|\), does not justify deleting that term or using this refined coefficient. The map and metric identification remains an explicit construction obligation.

## 4. The combined arithmetic and geometric target

Use exactly the inner positive rank weights and outer translation probabilities of `cs-weighted-lower`. Write
\[
\mathcal K=\sum_up_u\left[A_u-\Gamma_u+
  \langle D+e+\ell-\mu\rangle_u-M_u\right].
\]
When its weighted lower comparisons hold, (3.2) proves
\[
\boxed{\overline E\le\mathcal K+
\mathcal A_*+\mathcal B_*/2+
\sqrt{\mathcal A_*\mathcal B_*+\mathcal B_*^2/4}.}\tag{4.1}
\]
If the lower comparisons hold with the signed defects of equation (16) in [the averaged-budget note](averaged-error-budget.md), add their joint mean \(\sum_up_u(a_u+b_u)\) to \(\mathcal K\). Their signs need not be discarded. Any source-slope term \(\mu\) replaced by Sections 1--2 must first be identified with that same section lattice and normalization. The present note does not silently identify unrelated slopes.

For the RH specialization, use the source-compatible [direct transfer](rh-direct-transfer.md). Its positive prime kernel freezes only the thick weights, and then translation averaging gives the four required characters. This requires no symmetry of the actual weights: such full pooled symmetry is in fact [incompatible with the unchanged sparse-top family](rh-weight-symmetry.md). Under the direct transfer's thin-sum and source size conditions, insert (4.1) in its criterion
\[
G_1(x)\le\frac{\overline E}k
 +\frac1{|T|}\sum_t C_{q,d}(a_t/b)
 +\frac{2-d_0}{d_0x}+\frac{2C_\Psi}{3fx}
 +(1+\log(x+1))^2.
\]
Here \(d_0=|S|/|A|\), \(k=|T|mbd_0/2\), and \(C_\Psi\) is a Chebyshev constant as defined in that note. The \(b\) is the original thick lower endpoint, not a pooled mean. Its signed companion is \(C_{q,d}=G_{\chi_d}+G_{\chi_q\chi_d}-G_{\chi_q}\). The existing larger-scale QRH input supplies the stated thin estimate; that input and its uniformity have not been independently reproved here.

Thus a bound for this **one signed total** suffices. Source slopes can be bounded using the actual two height moments, signed section surplus, and rank-preserving covering formula; frame errors can be bounded by the correlated moments in Section 3. No separate worst-case upper estimate for every component, cover or translated frame is intrinsic to this criterion.

The remaining work is substantive: prove these geometric and arithmetic bounds for one compatible growing family and control the entire normalized right side on the required whole windows with total exponent loss tending to zero. The direct transfer closes the need for a new symmetry construction at this analytic interface. A fixed-geometry asymptotic, a small average rank defect, or bounded quadratic logarithmic derivatives alone supplies none of the missing uniform geometric estimates.

## Verification

The note contains full ordinary proofs, including the signs, normalized ranks, logarithmic domains, empty/zero cases and sharpness boundaries. The verification script checks the extracted source bytes, exact rational descent cases, the symbolic optimization identities, and equality models. Its algebra checks supplement the proofs; they do not assert a new Lean theorem or verify the missing arithmetic-geometric suppliers. The independent `rh_source_symmetry` review of Sections 1--3 passed, including the extremal models, normalized rank algebra, two-moment optimization, weighted frame inequalities and zero cases. It checked the refined frame statement against the existing manuscript but did not independently re-download the geometric source files or audit the upstream geometric suppliers. Section 4 is a direct substitution into the independently reviewed direct-transfer theorem.
