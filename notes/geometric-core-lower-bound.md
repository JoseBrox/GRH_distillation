# The geometric core: determinant degree and component averaging

## Status and scope

This checkpoint identifies the exact integral lattice and metric in the remaining geometric lower bound. It proves elementary determinant descent, averaging of orthogonal types, a shorter component-averaging inequality, and an alternative which retains the actual Hilbert–Samuel excess-rank cost instead of a worst-case rank comparison. It does **not** yet replace the arithmetic-geometric construction of the component height and Hilbert–Samuel estimates. In particular, a bound for the arithmetic degree of all sections does not by itself bound an arbitrary selected type subspace.

All source references below are to `jsmorph/rh` at `ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. The companion certificate records Git blob hashes, SHA-256 hashes and bounded inspected ranges. The exact projection defect used below is proved in [the covolume defect budget](covolume-defect-budget.md).

## 1. The actual lattice and its normalization

Fix one stage. The smaller coefficient field is the number field of definition of the automorphic geometric datum. Let \(V\) be the space of algebraic cuspidal sections which are holomorphic in every good complex realization. Its integral lattice is defined by nonnegative valuations at every prescribed finite valuation. Intersect this lattice with the span of the specified finite type. This is the **core lattice** \(E\).

The source definitions are precise:

| Object | Pinned declaration and lines | Mathematical content |
|---|---|---|
| Cuspidal section space | `IsProbabilityMeasureMuPart.cuspW`, 425–427 | Algebraic sections intersected with the holomorphic subspace in each good complex realization. |
| Integral section lattice | `supLat`, 574–578; `latW`, 586 | All prescribed finite valuations are nonnegative. |
| Selected core | `NormNegCmConstantEqAtAllEmbeddings.typeK`, 276–278; `latTypeK`, 286–288 | Integral sections intersected with the linear span of the required type. |
| Core norm | `nrmK`, 283–284; `normW`, 802 | The Petersson norm described below. |
| Geometric cover | `latOver`, 255–256 | Integral sections on a deep cover intersected with the span of pullbacks of the selected type. |
| Component degree | `degC`, 263–264; `degOn`, 822 | Normalized arithmetic degree of the component section lattice. |

The Petersson measure is the probability measure `muQ1`, not an unspecified invariant measure. At a component it is the probability measure `muOn`. The pointwise metric has the additional scalar

\[
 c(G)=\exp\!\left(-\frac12 S(G)\log(2\pi\xi)\right),
 \qquad S(G)=\sum_{\tau}\sum_{i<\operatorname{mult}(\tau)}G_1(\tau,i).
\]

This is `lieFacZ` at lines 664–665 and the actual value of \(\xi\) is `xiR D`. The scalar multiplies the norm, not its square. The definitions `petW` 787–788 and `normW` 802 therefore specify a period normalization that must be preserved in any replacement proof.

Write \(\widehat{\deg}\) for the degree normalized by the number-field degree and normalized so that the usual metric on \(\mathcal O_K\) has degree zero. Set

\[
 \mu(E)=\widehat{\deg}(E)/\operatorname{rk}E,
 \qquad \nu(E)=2\mu(E).
\]

For the totally complex coefficient fields these are exactly the source's `slope` and `slope_sq`: the discriminant and factor-of-two corrections are displayed in `HarderNarasimhan/StatementPl.muDef`, 64–65. The identity `degW_eq`, 826, is \(\widehat{\deg}(E)=\operatorname{rk}(E)\nu(E)/2\).

**Exact metric-scaling identity.** If \(\nu_0(E)\) uses the same lattice, probability measure and pointwise metric before multiplication by \(c(G)\), then

\[
 \boxed{\nu(E)=\nu_0(E)+S(G)\log(2\pi\xi).}
\]

Indeed, the determinant norm of a rank-\(r\) lattice is multiplied by \(c(G)^r\), so its degree changes by \(-r\log c(G)\). This is an identity, not an estimate or a choice of a convenient metric. It does not by itself identify the different main period \(\log\Omega\).

The desired core bound is

\[
 \nu(E)\ge -T_i-CU,
 \qquad U=B_0\log\log x.
\]

With stage number \(s=i+1\), the source's exact main term is

\[
 T_i=\sum_\rho(k+2s-m-1)w(s,\rho)\log\Omega.
\]

These are `CovolXOfCovol.LowAt`, 96, and `ZscOfNum`, 64–66. A Faltings-height estimate for a single Hodge line is not automatically this section-lattice estimate.

**Order of quantifiers.** Within each admissible family, one nonnegative constant \(C\) is chosen before the sufficiently large parameter \(x\), and the estimate then holds for every allowed row and every stage. Cover estimates quantify over every good deep cover at each nonterminal stage. This is `Lifts`/`EvTied`/`Covers`, 201 and 216–223. Choosing a new uncontrolled \(C\) for each \(x\), row or cover would not prove the required bound.

## 2. An elementary determinant descent lemma

Let \(A,B\) be Hermitian \(\mathcal O_K\)-lattices of ranks \(a,b\), with \(a>0\), and let

\[
 \Phi:A\longrightarrow B^{\oplus n}
\]

be integral and injective. Put \(m=nb\), \(C=(\Phi(A)\otimes K)\cap B^{\oplus n}\), \(Q=B^{\oplus n}/C\), endowed with the subspace and quotient metrics, and \(J=[C:\Phi(A)]\). Let \(h_{\det}(\Phi)\) be the normalized sum of the logarithms of the norms of the top exterior power of \(\Phi\) on \(A\otimes K\). Then

\[
 \boxed{n\widehat{\deg}(B)
 =\widehat{\deg}(A)-h_{\det}(\Phi)
   +\widehat{\deg}(Q)+[K:\mathbf Q]^{-1}\log J.}\tag{2.1}
\]

**Proof.** The induced metric on the image changes its degree by \(-h_{\det}(\Phi)\). Saturation increases degree by \([K:\mathbf Q]^{-1}\log J\). Additivity of determinant degree in the saturated exact sequence \(0\to C\to B^{\oplus n}\to Q\to0\) gives (2.1). These statements also follow directly by taking exterior powers and multiplying the finite indices and Archimedean determinants.

Suppose \(\|\Phi_\sigma\|\le e^P\) at every embedding. Suppose also that \(B\otimes K\) is spanned by elements of \(B\) of norm at most \(e^\Lambda\) at every embedding. Then

\[
 \boxed{\nu(B)\ge \lambda\bigl(\nu(A)-2P\bigr)
                -2(1-\lambda)\Lambda,
 \qquad \lambda=\frac{a}{nb}.}\tag{2.2}
\]

Here \(0<\lambda\le1\). The projected short vectors span \(Q\otimes K\); choose a linearly independent subset. Their integral span has determinant norm at most \(e^{(m-a)\Lambda}\) by Hadamard, and is contained with finite index in \(Q\). Thus \(\widehat{\deg}(Q)\ge-(m-a)\Lambda\). Also \(h_{\det}(\Phi)\le aP\) and \(\log J\ge0\). Substitute these inequalities in (2.1).

This proof uses ordinary determinants and saturation; no Harder–Narasimhan filtration or extremal slope is required. It also exposes a weaker alternative: retain the actual quotient degree in (2.1), avoiding a short-vector estimate entirely when the quotient determinant can be computed.

In the source, \(A\) is the shifted-weight section lattice on a deep cover, \(B\) is the covered selected type, \(P\) is the cover error and \(\Lambda=\mathrm{PP}\,\kappa\). `MapsAt` supplies \(\Phi\), `GminAt` supplies the short spanning set, and `RkAt` controls \(\lambda\). `RingAt` then gives \(\nu(E)\ge\nu(B)-2b_0\). These are `CovolXOfCovol`, 116–131, and the exact source application is `LowerBoundOfAllEstimates.lowAt_of_cover`, 65–105.

Consequently the determinant identity sharpens and shortens the numerical descent. It does **not** prove the geometric maps, short sections, or their estimates.

### Averaging all orthogonal types first

There is a further exact option when the outer average in the final argument permits it. Suppose \(V=\bigoplus_{\tau}V_\tau\) is an orthogonal decomposition, \(L_\tau=L\cap V_\tau\), \(r_\tau=\operatorname{rk}L_\tau>0\), \(r=\operatorname{rk}L\), and \(J=[L:\bigoplus_\tau L_\tau]\). Then

\[
 \boxed{\sum_\tau\frac{r_\tau}{r}\nu(L_\tau)
       =\nu(L)-\frac{2\log J}{[K:\mathbf Q]r}.}\tag{2.3}
\]

If every projection \(P_\tau\) satisfies \(NP_\tau(L)\subset L\) for a common integer \(N\ge1\), then

\[
 J\le N^{[K:\mathbf Q](r-\max_\tau r_\tau)}.
\]

For the index bound, omit an index with maximal rank and map the quotient into the product of \(N^{-1}L_\tau/L_\tau\) over all remaining indices. If every remaining projection is integral, the omitted projection is integral as well because their sum is the original lattice vector. Hence this map is injective. Orthogonal determinant multiplicativity proves (2.3).

Thus a **rank-weighted** average of all type slopes needs only the full-space degree and the integral index. It need not use any individual type lower bound. Applying this to the final proof requires an actual match between its type weights and \(r_\tau/r\), and an orthogonal decomposition of the same lattice. Neither match has yet been verified for the selected source family. Invariance of normalized metrics under embeddings does not alone imply equivariance of the chosen covers or equality of these type weights.

## 3. A shorter component-averaging bound

The next result is proved from explicit numerical hypotheses. In the source these hypotheses are the component height and arithmetic Hilbert–Samuel estimates; their geometric proofs remain separate.

Let \(Z\) run through a nonempty finite set. Suppose

\[
 0<\delta_0\le\delta_Z\le\frac{\delta_0}{1-\rho},\quad
 0\le\rho<1,\quad w_Z=B\delta_Z>0,\quad r_Z\ge w_Z.
\]

Let \(c,X,c_c\ge0\) and \(h_Z,s_Z\in\mathbf R\) satisfy

\[
 h_Z\ge-c,\qquad
 (1-\rho)\max(0,s_Z+c)\le h_Z+c+c_c,
 \qquad \frac1{\#Z}\sum_Zs_Z\ge-X.
\]

Finally, suppose \(A>0\), \(R\ge0\), \(a\ge0\), \(t\ge a+1\), and the arithmetic degrees \(d_Z\) satisfy

\[
 d_Z\ge w_Z\{t h_Z-a|h_Z|-A\log(2+|h_Z|)-R\}.
\]

Define

\[
 H=(2\rho-\rho^2)c+(1-\rho)^2X+(1-\rho)c_c,
 \quad
 K=(t-a-1)H+2(a+1)c+A\log\max(A,1)+R+2.
\]

Then \(K\ge0\), and

\[
 \boxed{\frac{\sum_Z d_Z}{\sum_Z r_Z}\ge-K.}\tag{3.1}
\]

**Proof.** Put \(u_Z=h_Z+c\ge0\). The degree-spread bound implies

\[
 \frac{\sum w_Zu_Z}{\sum w_Z}
 \ge(1-\rho)\frac{\sum u_Z}{\#Z}
 \ge(1-\rho)\{(1-\rho)(c-X)-c_c\}.
\]

Thus the \(w\)-weighted mean of \(h_Z\) is at least \(-H\). For every \(y\ge0\), the inequality \(\log v\le v-1\), applied with \(v=(2+y)/A\), gives

\[
 A\log(2+y)\le A\log\max(A,1)+2+y.
\]

Since \(|h_Z|\le h_Z+2c\), the braces in the degree estimate are at least

\[
 (t-a-1)h_Z-2(a+1)c-A\log\max(A,1)-R-2.
\]

Their weighted mean is at least \(-K\). Summing yields \(\sum d_Z\ge-K\sum w_Z\ge-K\sum r_Z\), proving (3.1).

### Consequence for the verified source contracts

Set \(a=3(D+1)\), \(t=\mathrm{lenT}\), \(B=\mathrm{binT}\), and use `HeightAt`, `HSAt`, `DegAt` and only the first inequality of `ShareAt` in `CovolXOfCovol`, 140–156. Suppose the source error budget is \(U\ge1\) and

\[
 tX\le C_HU,\quad tc_c\le C_HU,\quad
 c(6D+10+t(z+2\rho))\le C_HU,
 \quad A\log\max(A,1)+R\le C_SU,
\]

with \(z\ge0\) and \(t\ge3D+4\). As \(H\le X+c_c+2\rho c\), the preceding explicit constant obeys

\[
 K\le(3C_H+C_S+2)U.
\]

The source `SumAt`, 158–159, therefore gives the actual conclusion

\[
 \boxed{\nu(\text{base-weight cover sections})
       \ge-2(3C_H+C_S+2)U.}\tag{3.2}
\]

The source's numerical theorem gives \(-2(3C_H+C_S+4)U\) and assumes the stronger \(t\ge3D+5\). More significantly, (3.1) never uses the upper rank estimate \(r_Z\le w_Z/(1-z)\). Near proportionality of ranks and degrees is unnecessary for **this averaging step**. The verified source does use the upper-rank estimate in constructing `HSAt`: `HilbertSamuelLowerBoundOfComponents`, 110–113. The next section shows precisely how to retain its actual cost instead.

## 4. Exact Hilbert–Samuel surplus: no componentwise upper-rank bound

The raw source statement is `Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/RealCubicMeans/LogMeanShares/LogMeanStatements/HSClaim.lean`, lines 7–22. Require a positive component rank \(r\), positive integers \(t,D\), \(n,\Lambda,\beta,\Lambda_D,\Lambda_T\ge1\), \(\delta>0\), and the positive constant \(C=26\). In particular every logarithmic argument below is positive and \(\sqrt\beta>0\). Set

\[
w=\binom{t-1}{D}\delta,\quad z=1-w/r,
\quad \ell=\log\Lambda+C\log\{nD\delta(2+|h|+\log\Lambda)\},
\quad g=(D+1)(\log n+1)/2+1.
\]

Here the source application has `C=26` and `j0=1`. The claim says `0<=z<=1` and

\[
\frac{d}{r}\ge(1-z)\{t h-3(D+1)|h|-J-CD^2(\ell+\log t)
 -(t+D+1)\log\beta-(t+D^2)(g+2)\}
-z\{t(\log2+\ell+\tfrac12\log\beta)+\log\Lambda_D+\log\Lambda_T\}.
\]

Thus **multiplying out**, without bounding `z`, gives

\[
d\ge w\{t h-3(D+1)|h|-J-CD^2(\ell+\log t)
 -(t+D+1)\log\beta-(t+D^2)(g+2)\}-(r-w)P,
\]

where

\[
P=t(\log2+\ell+\tfrac12\log\beta)+\log\Lambda_D+\log\Lambda_T.
\]

For `Lambda>=1`, put

\[
\ell_0=\log\Lambda+C\log\{nD\delta(1+\log\Lambda)\},
\quad A=C^2D^2,
\]

\[
R_Z=J+CD^2(\ell_0+\log t)+(t+D+1)\log\beta+(t+D^2)(g+2).
\]

Because `2+|h|+logLambda <= (1+logLambda)(2+|h|)`, one has

\[
\ell\le\ell_0+C\log(2+|h|).
\]

The source flat twist preserves the component ranks (`HilbertSamuelLowerBoundOfComponents`, 52 and 103). If it satisfies `d'_Z >= d_Z-r_Z c_Z`, the exact usable lower bound is

\[
d'_Z\ge w_Z\{t h_Z-a|h_Z|-A\log(2+|h_Z|)-R_Z\}
 -(r_Z-w_Z)P_Z-r_Zc_Z,\qquad a=3(D+1).
\tag{A.1}
\]

Apply the weighted-height argument of Section 3 of the main note. Let

\[
R_{\rm tot}=\sum_Zr_Z>0,\quad W=\sum_Zw_Z,\quad
K_0=(t-a-1)H+2(a+1)c+A\log\max(A,1)+2,
\]

\[
\Gamma_{\rm HS}=
\frac{\sum_Z\{w_ZR_Z+(r_Z-w_Z)P_Z+r_Zc_Z\}}{R_{\rm tot}}.
\]

For `t>=a+1`, summing (A.1) yields the proved inequality

\[
\boxed{\nu(\text{base-weight cover})\ge
-2\left(\frac{W}{R_{\rm tot}}K_0+\Gamma_{\rm HS}\right)
\ge-2(K_0+\Gamma_{\rm HS}).}\tag{A.2}
\]

The last step uses `K0>=0` and `W<=Rtot`. **No upper rank-share estimate is used.** There is a single actual total surplus cost `sum(r-w)P`, which can be averaged further over the final outer indices before bounding it. Negative `R_Z` or twist costs are allowed and are retained with their signs.

The existing source supplier `ExistsDegreeParametersBound.hsClaim_short_alt_alt`, lines 34–43, constructs the raw claim without `ShareCondition`. Its proof uses topology and domain regularity, Bergman frames, geometric weight-pair comparison, short vectors, and size bounds. The later `HilbertSamuelLowerBoundOfComponents`, 110–113, uses the **upper** share inequality only to replace the actual surplus cost by a uniform explicit bound. This numerical replacement can be omitted in a proof using (A.2).

**Rank guard.** Positive component rank is required separately. Lean's real division is total; its raw predicate may hold at rank zero, so positivity must not be inferred just from the written quotient formula. Existing lower Share implies positivity; a shorter geometric nonzero-section proof would suffice. Once `r>0`, the raw inequality `0<=z` already gives `w<=r`.

**Limit of the simplification.** Formula (A.2) proves the reduction. It does not yet show `Gamma_HS=O(U)` for the actual family without the original share estimate. A proof of that average bound, or a direct total-degree estimate, is still needed before removing that geometric supplier. This is a precise smaller obligation, not an unconditional core estimate.

## 5. Primary fixed-geometry Hilbert–Samuel references and uniformity

1. Atsushi Moriwaki, *Continuity of volumes on arithmetic varieties*, arXiv:math/0612269v2, Theorem A (p.2), equivalently Corollary 5.5. The theorem gives the small-section asymptotic for a fixed nef smooth Hermitian line bundle and a fixed twist. PDF: <https://arxiv.org/pdf/math/0612269v2>. SHA-256 `cbc3cf83dacad86d65a7d69a95affb866e0ada9cf585b695e7753b7480551d98`; local text inspected lines 67–75.
2. Robert J. Berman and Gerard Freixas i Montplet, *An arithmetic Hilbert–Samuel theorem for singular hermitian line bundles and cusp forms*, Compositio Math. 150 (2014), 1703–1728, DOI `10.1112/S0010437X14007325`. Theorem 4.4, author PDF p.16, gives the total L2 degree asymptotic for a fixed semi-positive log-singular Hermitian line bundle, generically semi-ample and big, nef on vertical fibres, with fixed log-singular twist. PDF: <https://perso.pages.math.cnrs.fr/users/gerard.freixas/articles/Berman-Freixas.pdf>. SHA-256 `cda28b25ac9d7142b9424f36e9e4eac026db22da3d2db0d80d6a4f4ce233fc83`; local text inspected lines 853–866. Theorem 5.4 is an explicit Petersson example for Hilbert modular surfaces; it is not a theorem uniform in arbitrary unitary dimension, field, level and weight.

The source Hodge field `ArithHilbertSamuel` in `PublishedTheorems/Divisors₂/SmallSecTensTriv.lean` 14–19 is likewise a fixed-data little-o asymptotic. It cannot, on its own, bound the required growing-family diagonal at `t=lenT(x)`. Each fixed-data error may tend to zero only beyond a threshold depending arbitrarily on that data. Nor does a count of small sections alone identify the arithmetic degree of an arbitrary selected type. The source quantitative construction, or a verified uniform replacement, remains necessary.

There are genuinely quantitative classical alternatives. Huayi Chen, *Explicit uniform estimation of rational points I. Estimation of heights*, DOI `10.1515/CRELLE.2011.138`, Theorem 4.8, reformulates a David–Philippon lower bound for the degree of the projective coordinate quotient \(\operatorname{Sym}^t\mathcal E/I_t\). Its threshold is

\[
 t\ge(n-D)(\delta-1)+1,
\]

where \(n\) is the ambient projective dimension, \(D\) the variety dimension and \(\delta\) its degree. Its right side also involves the minimal slope and other invariants of \(\mathcal E\). The author PDF p.22 was checked both as text and visually: <https://webusers.imj-prg.fr/~huayi.chen/Recherche/effunifI.pdf>, SHA-256 `32dcd5296f6fcc579943fc91e2ff0591dbfe9badd8d9dc6d5957939dfddde0c1`. This is a concrete candidate, but the threshold, quotient lattice and quotient metric have not been matched to our sections and Petersson metric. The source's available bound is on \(\log\delta\), which does not by itself imply this threshold. No replacement is adopted from this reference.

## 6. The genuine height input underneath the Hodge bundle

The Hodge bundle's 28 fields do not alone supply the height lower bound. `TopCovolG` additionally consumes the volume input, `HypothesesX`, `HypothesesH`, Grothendieck deformation, `HSCore.Quoted`, and the companion mean-height theorem.

The exact companion contract is `ModelSmall.DeepStR`, 63–66: one universal nonnegative constant, then all allowed global data and stages `1<=j<m`, subject to `m^2<=k`, all good deep covers whose specified level integer has at most 15 prime factors. The conclusion is the following mean-volume-slope statement for **every** strictly decreasing integral weight with its required gap:

\[
\frac1{\#Z}\sum_Z s_Z\ge
-C\left[(\log B+\ell)\|u\|_1
 +q\sum_\tau(\max_i u_{\tau i}-\min_i u_{\tau i})\right],
\]

where each `s_Z` is a lower bound for the component's volume slope for the mixed finite valuation model, `B` is the explicit weight/gap bound, and

\[
\ell=\log\operatorname{rd}(E)+|d\log L(1)|.
\]

This is `SemiposAtOfPositive.MeanGe/MeanAll/errX`, 88–105. A bound for the root discriminant or the logarithmic derivative controls only its error parameter. It does not prove the mean-volume-slope statement. The theorem is supplied through arithmetic intersection, Moriwaki positivity/Hilbert–Samuel, Hodge–Tate comparison, formal section descent and finite-flat quotient constructions (`DeepStROfHyp`, 47–58).

The reduced human proof can organize this into three substantive tasks: a period-normalized mean geometric height bound; an arithmetic section-degree estimate with the averaged surplus (A.2); and integral determinant descent (2.1). These are concrete mathematical contracts, with the numerical HN/maximal-slope machinery removed where the determinant arguments suffice.

## 7. What can and cannot be bypassed

The determinant method and the exact orthogonal-projection defect allow the final inequality to depend on actual total degrees and actual complementary degrees, including their weighted averages. Maximal-slope bounds and exponentially small bad-rank fractions are sufficient ways to control those quantities, not necessary features of the final estimate.

There is a real obstruction to using the total degree of all sections alone. For an orthogonal direct sum of two rank-one lattices, the slopes can be \(-M\) and \(+M\), while the total slope is zero. Selecting the first summand gives arbitrarily negative slope. Thus a replacement must retain either the complement degree, a determinant of the selected quotient, or a genuine geometric descent such as (2.1).

The terminal source stage is a definite signature with \(q=0\): `CoveringLowDefectBound`, 36–46. It is handled by a separate period/representation-weight comparison. This removes the positive-dimensional component-height route at that stage. No verified specialization yet shows that every stage in the Riemann-zeta case is terminal or has rank-one section lattice.

## 8. Remaining mathematical work

1. Audit the geometric height estimate and the arithmetic Hilbert–Samuel lower bound at the exact weights, levels, period metrics and error scale \(B_0\log\log x\).
2. Bound the actual total Hilbert–Samuel surplus in (A.2), or verify a direct total-degree bound, so that the existing uniform upper-rank supplier can be omitted rather than merely replaced by an unproved average estimate.
3. Seek a direct determinant-of-cohomology estimate for the selected type or its quotient. Such an estimate must retain the integral lattice and the metric scalar from Section 1.
4. For an RH-only specialization, verify the available signatures, fields, type ranks, covering ranks and equivariance before claiming that any geometric branch disappears. The current numerical supplier explicitly uses field parameter f≥8 and rank parameter r≥100 (`HilbertSamuelLowerBoundOfComponents`, 59–68); trivial target character does not force small section rank.
5. Test the rank-weight matching required by (2.3). If it holds, average type degrees before proving individual lower bounds.

The named 28-field Hodge bundle remains a bundle of exact source contracts, not a blanket assertion that a familiar theorem with a similar name supplies each one. Its field list and assembly are pinned in the certificate. The new proofs above are elementary determinant and real-variable arguments and do not require an additional classical reference.

## Independent verification

The root agent and `endpoint_backbone` independently checked Sections 2–3 (determinant descent and component averaging): **PASS**, including the determinant signs, rank-zero quotient, weighted-mean formula, denominator direction, improved constant and weaker threshold. `endpoint_backbone` also checked the type-averaging identity and the raw-surplus extension against the pinned source: **PASS**, with explicit positivity of the logarithmic arguments requested and incorporated above. No Lean kernel rerun is claimed.
