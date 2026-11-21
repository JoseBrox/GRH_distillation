# The geometric core: determinant degree and component averaging

## Status and scope

This checkpoint identifies the exact integral lattice and metric in the remaining geometric lower bound and gives two elementary determinant reductions and a shorter component-averaging proof. It does **not** yet replace the arithmetic-geometric construction of the component height and Hilbert–Samuel estimates. In particular, a bound for the arithmetic degree of all sections does not by itself bound an arbitrary selected type subspace.

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

The source's numerical theorem gives \(-2(3C_H+C_S+4)U\) and assumes the stronger \(t\ge3D+5\). More significantly, (3.1) never uses the upper rank estimate \(r_Z\le w_Z/(1-z)\). Near proportionality of ranks and degrees is unnecessary for **this averaging step**. The source construction of the individual Hilbert–Samuel estimates must still be inspected before discarding its use elsewhere.

## 4. What can and cannot be bypassed

The determinant method and the exact orthogonal-projection defect allow the final inequality to depend on actual total degrees and actual complementary degrees, including their weighted averages. Maximal-slope bounds and exponentially small bad-rank fractions are sufficient ways to control those quantities, not necessary features of the final estimate.

There is a real obstruction to using the total degree of all sections alone. For an orthogonal direct sum of two rank-one lattices, the slopes can be \(-M\) and \(+M\), while the total slope is zero. Selecting the first summand gives arbitrarily negative slope. Thus a replacement must retain either the complement degree, a determinant of the selected quotient, or a genuine geometric descent such as (2.1).

The terminal source stage is a definite signature with \(q=0\): `CoveringLowDefectBound`, 36–46. It is handled by a separate period/representation-weight comparison. This removes the positive-dimensional component-height route at that stage. No verified specialization yet shows that every stage in the Riemann-zeta case is terminal or has rank-one section lattice.

## 5. Remaining mathematical work

1. Audit the geometric height estimate and the arithmetic Hilbert–Samuel lower bound at the exact weights, levels, period metrics and error scale \(B_0\log\log x\).
2. Determine which use of the upper rank comparison in constructing `HSAt` is genuinely necessary. The averaging proof above does not need it.
3. Seek a direct determinant-of-cohomology estimate for the selected type or its quotient. Such an estimate must retain the integral lattice and the metric scalar from Section 1.
4. For an RH-only specialization, verify the available signatures, fields, type ranks and covering ranks before claiming that any positive-dimensional geometric branch disappears.

The named 28-field Hodge bundle remains a bundle of exact source contracts, not a blanket assertion that a familiar theorem with a similar name supplies each one. Its field list and assembly are pinned in the certificate. The new proofs above are elementary determinant and real-variable arguments and do not require an additional classical reference.
