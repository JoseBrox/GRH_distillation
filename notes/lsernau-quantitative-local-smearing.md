# Quantitative compact smearing from integral polynomial relations

## What is proved

For every fixed polynomial degree, the exact compact-support smearing in [the noncompact real-edge chapter](lsernau-noncompact-real-edges.md) admits an explicit linear choice with a common compact support and controlled invariant smooth seminorms. The construction uses a fixed local bump, differential operators, and integer linear algebra before projection.

This avoids assuming a lower singular-value bound for a matrix of analytically projected vectors. The bounds are large: they involve factorials and powers of the dimension of the polynomial space. They do not establish that the resulting losses fit the global chain gauges. Moreover, the input norm in the result is the Fischer norm of the original polynomial, not the Hilbert norm of its projection.

All representation-theoretic inputs are supplied in [the discrete-series supplier chapter](lsernau-discrete-series-suppliers.md). The argument below is an ordinary quantitative refinement of the finite-degree Howe proof, followed by an explicit smooth bump construction.

## 1. Setup and the quantitative statement

Use the matching Fock datum of the noncompact chapter. Write \(r,m\) for row and column ranks, \(M=rm\), and \(\gamma,\gamma'\) for the two integral constants in the displayed row and column Lie actions. Let

\[
 \Phi\in\mathbf Z[X_1,\ldots,X_M],\qquad
 d_0=\deg\Phi,\qquad a=\min(r,m),
\]

be the explicit homogeneous product of layer minors, normalized to equal one at the matching matrix. Then

\[
 \|\Phi\|_{\mathrm{coeff},1}\le a^{d_0}.
 \tag{1.1}
\]

Let \(P_l\) be the row discrete-series projection, \(x=P_l\Phi\ne0\), and let \(\rho'\) denote the derived column action. The column parameter is \(l'\), its bottom compact type is \(\tau'\), and \(|l'_c|\le L'\). All norms on matrices below are the operator norm except for the explicitly specified Lie-algebra directions, which have Frobenius norm one.

Fix \(D\ge d_0\). Define the following explicit positive integers:

\[
 \begin{split}
 N&=\binom{M+D}{M},\qquad s_0=(m-1)d_0,\qquad
 s_*=s_0+\left\lfloor\frac{D-d_0}{2}\right\rfloor,\\
 B_0&=1+|\gamma|+|\gamma'|+\max_a|\Lambda_a|
           +(r+m+1)(D+2)^2,\\
 K_0&=(N+1)!B_0^N,\\
 H_0&=\max\{1,B_0K_0,a^{d_0}B_0^{s_0}\},\\
 C_0&=N!H_0^{N-1},\qquad
 U_D=C_0^{D-d_0+1},\\
 Q_D&=(N!H_0^N)^{D-d_0+1}.
 \end{split}
 \tag{1.2}
\]

The symbols \(B_0,K_0\) in (1.2) are numerical bounds, not the Hermitian form or maximal compact group. Put

\[
 \delta=\frac1{128m(L'+m+1)},\qquad
 K_m=8192m(m^2+1)^3,
 \qquad
 \Xi_{M,D}=\left(\sum_{j=0}^{D}\frac{M^j}{j!}\right)^{1/2}
 \le e^{M/2}.
 \tag{1.3}
\]

For a smooth compactly supported function on \(G'=U(l'\text{'s signs})\), let

\[
 p_{t,A}(f)=\max_{0\le j\le t}\ 
 \sup_{\|Y_1\|_F,\ldots,\|Y_j\|_F\le1}
 \int_{G'}|D_{Y_1}\cdots D_{Y_j}f(g)|\|g\|^A\,dg,
 \tag{1.4}
\]

where the \(Y_i\) belong to the real unitary Lie algebra and
\(D_Yf(g)=\left.\frac d{dt}\right|_0f(\exp(tY)g)\). Mixed left and right invariant derivatives satisfy the same bounds.

**Theorem.** There is a complex-linear map

\[
 \mathcal S_D:\mathcal P_{\le D}\longrightarrow C_c^\infty(G')
\]

such that

\[
 P_lP=\pi'(\mathcal S_DP)x,
 \qquad
 \operatorname{supp}(\mathcal S_DP)\subset K'B_\delta K',
 \quad B_\delta=\{g:\|g-1\|\le\delta\}.
 \tag{1.5}
\]

For all integers \(t\ge0\), all \(A\ge0\), and all \(P\in\mathcal P_{\le D}\),

\[
 \boxed{
 \begin{aligned}
 p_{t,A}(\mathcal S_DP)
 &\le 2\dim\tau'\,(1+\delta)^A\,
       2^{s_*}U_D\Xi_{M,D}\,
       \left(\frac{K_m}{\delta}\right)^{t+s_*}\\
 &\hspace{25mm}\cdot(t+s_*+1)!\,((t+s_*)!)^2\,
       \|P\|_F.
 \end{aligned}}
 \tag{1.6}
\]

The algebraic differential operator used to construct \(\mathcal S_DP\) has rational coefficients when \(P\) has rational coefficients. For integral \(P\), a single positive integer \(q_D\le Q_D\), independent of \(P\), clears those coefficients. This statement concerns the algebraic differential operators. The normalizing scalar of the smooth bump need not be algebraic; its inverse is bounded in absolute value by two.

If \(D<d_0\), every polynomial of degree at most \(D\) has zero row projection, and one can take \(\mathcal S_D=0\).

## 2. A finite version of the Howe spanning argument

Write \(V_j=\mathcal P_{\le j}\), with \(V_j=0\) for \(j<0\), and let \(\mathfrak p'_{\mathbf C}\) be the span of the noncompact column matrix units. Define \(Z_j\subset V_j\) as the span of:

1. \((\rho(E_{aa})-\Lambda_a)P\), for \(P\in V_j\);
2. \(\rho(E_{ba})P\), for compact row raising operators \(E_{ab}\) and \(P\in V_j\);
3. \(\rho(E_{ab})Q\), for arbitrary row matrix units, where \(Q\in V_{j-2}\) is row compact-highest of a weight \(\nu\) with \(\nu-\Lambda\notin\mathcal C_l\).

The degree restrictions ensure that every listed vector lies in \(V_j\). The first two operators preserve degree. A noncompact matrix unit changes degree by at most two.

Let \(T_\Phi=U(\mathfrak k'_{\mathbf C})\Phi\), the compact column module generated by \(\Phi\), and put

\[
 S_j=V_{j-1}+\rho'(\mathfrak p'_{\mathbf C})V_{j-2}
       +Z_j+
       \begin{cases}T_\Phi,&j\ge d_0,\\0,&j<d_0.\end{cases}
 \tag{2.1}
\]

**Finite spanning lemma.** For every \(j\ge0\),

\[
 S_j=V_j.
 \tag{2.2}
\]

Here is why the global saturation proof really gives this finite statement. Every summand in (2.1) is stable under the compact column action. For the noncompact-image summand this follows from
\([\mathfrak k',\mathfrak p']\subset\mathfrak p'\); for \(Z_j\) it follows from commutation of the two Lie actions and degree preservation by compact columns. In particular, compact columns preserve each row-highest weight space used in the third kind of relation.

If \(S_j\ne V_j\), its nonzero Fischer orthogonal complement contains a column highest vector \(Q\). Orthogonality to \(V_{j-1}\) makes \(Q\) homogeneous of degree \(j\). Taking adjoints of the first two kinds of relations makes \(Q\) row highest of weight \(\Lambda\).

Every column Laplacian \(L\) lowers degree by two. Applying the opposite noncompact column matrix unit to \(LQ\in V_{j-2}\) gives a vector in \(S_j\). Its pairing with \(Q\) is, up to its nonzero sign, \(\|LQ\|_F^2\); the additional term has degree at most \(j-4\) and is orthogonal to \(Q\). Hence all column Laplacians kill \(Q\).

For the rows, the extremal-Laplacian argument in §4.3 of the noncompact chapter produces a row Laplacian whose value on \(Q\), if nonzero, is highest of weight \(\Lambda+e_a-e_b\). If that weight is outside the positive root cone, the third kind of relation and the same Fischer pairing force its norm to vanish. If it is in the cone, the matching inequalities and the row-purity calculation from column harmonicity force the same Laplacian to vanish. Thus \(Q\) is a pre-joint harmonic.

The uniqueness proof gives \(Q=c\Phi\). If \(j<d_0\), the degrees are incompatible. If \(j\ge d_0\), \(\Phi\in S_j\), contradicting orthogonality. This proves (2.2). Notice that only compact column stability was used, and every input vector has the explicitly stated degree bound.

Every element of \(Z_j\) has zero row projection, by the integration-by-parts and root-cone arguments already proved. Projection therefore turns (2.2) into a finite recursion using only lower-degree projected polynomials and column derivatives of them.

## 3. Integral generators and their size

Use the unnormalized monomial basis in each \(V_j\). The creation and annihilation formulas have integer coefficients, as do \(\gamma,\gamma'\) and \(\Lambda\). Inspection of one matrix unit gives

\[
 \|\rho(E_{ab})P\|_{\mathrm{coeff},1},\quad
 \|\rho'(E_{cd})P\|_{\mathrm{coeff},1},\quad
 \|(\rho(E_{aa})-\Lambda_a)P\|_{\mathrm{coeff},1}
 \le B_0\|P\|_{\mathrm{coeff},1}
 \tag{3.1}
\]

whenever the input degree is at most \(D\). A quadratic derivative contributes at most \((D+2)^2\) per summand; there are at most \(r\) or \(m\) summands, and (1.2) also covers the scalar terms. We use (3.1) only when the output belongs to the appropriate truncated space.

### Integer bases of row-highest spaces

The row diagonal operators are diagonal on monomials with integer eigenvalues. Split \(V_{j-2}\) into its finitely many row weight spaces. On a weight space with \(u\le N\) monomials, stack the compact raising matrices. This gives an integer matrix with entries bounded by \(B_0\). Its kernel is precisely the row-highest space of that weight.

If the matrix has rank \(t\), choose an invertible \(t\)-by-\(t\) minor \(A\), and take the corresponding pivot columns. For each free column \(b\), the vector with that free coordinate equal to \(\det A\) and pivot coordinates \(-\operatorname{adj}(A)b\) lies in the kernel. The selected independent rows span all rows, so it solves the entire system. These vectors form an integer basis of the kernel over \(\mathbf C\). For rank zero use the standard basis.

Leibniz's determinant bound gives coefficient \(\ell^1\)-norm at most

\[
 (t+1)t!B_0^t\le(N+1)!B_0^N=K_0.
 \tag{3.2}
\]

The off-cone condition is an integer partial-sum test in the order of \(l\). Keep just the weights outside the cone and apply the row matrix units to this integer basis. The resulting third-kind generators of \(Z_j\) have norm at most \(B_0K_0\).

### A bounded word length for the compact orbit of \(\Phi\)

The compact highest-weight module generated by \(\Phi\) is spanned by products of compact lowering matrix units. Such a nonzero product needs at most

\[
 s_0=(m-1)d_0
 \tag{3.3}
\]

factors. To see this, use the column compact half-root-sum as a height functional. Each compact lowering root decreases height by a positive integer. After subtracting the fixed vacuum weight, the weights of a degree-\(d_0\) monomial are sums of \(d_0\) signed coordinate weights. Their heights lie in an interval of length at most \((m-1)d_0\). A longer lowering word therefore vanishes. The PBW theorem for the compact highest-weight module then gives the spanning assertion.

Keep all lowering words of length at most \(s_0\) applied to \(\Phi\). They are integer polynomials, and (1.1), (3.1) give the height bound \(a^{d_0}B_0^{s_0}\). Together with monomials, their noncompact column images, and the generators of \(Z_j\), they form an explicit integer spanning matrix for (2.2), whose entries are bounded by \(H_0\).

## 4. Cramer's rule gives the actual right inverse

Write \(N_j=\dim V_j\le N\). Select any \(N_j\) independent columns of the preceding spanning matrix, forming a square integer matrix \(A_j\). This is an effective selection: enumerate columns and retain a column exactly when it increases rank over \(\mathbf Q\). Its determinant is a nonzero integer. In particular,

\[
 |\det A_j|\ge1,
 \qquad
 |\det A_j|\le N_j!H_0^{N_j}\le N!H_0^N.
 \tag{4.1}
\]

The adjugate formula gives the induced coefficient \(\ell^1\)-norm bound

\[
 \|A_j^{-1}\|_{1\to1}
 \le N_j!H_0^{N_j-1}\le C_0.
 \tag{4.2}
\]

The arithmetic lower bound in (4.1), together with the proved full rank, is the essential point. It replaces an unproved lower bound for a projected analytic spanning map.

Apply this decomposition recursively. A column from \(V_{j-1}\) uses the preceding recursion. A column of the form \(\rho'(Y)Q\), \(Q\in V_{j-2}\), prepends the one column matrix unit \(Y\). A relation in \(Z_j\) contributes zero after projection. A compact-orbit column contributes its known lowering word on \(\Phi\).

For \(j<d_0\) no compact-orbit column is present, so induction gives \(P_lV_j=0\). For \(D\ge d_0\), this procedure constructs a complex-linear map

\[
 P\longmapsto u_P
\]

into formal sums of column matrix-unit words, with

\[
 P_lP=d\pi'(u_P)x,
 \qquad
 \operatorname{length}(u_P)\le s_*,
 \qquad
 \|u_P\|_{\mathrm{word},1}
 \le U_D\|P\|_{\mathrm{coeff},1}.
 \tag{4.3}
\]

The length bound follows from the recurrence
\(s_j\le\max(s_{j-1},1+s_{j-2},s_0)\), starting at \(j=d_0\), with zero recursions below \(d_0\) omitted. In particular, at \(j=d_0+1\) the noncompact contribution differentiates a zero operator and adds no word; its bound is still \(s_0\). The norm bound follows from (4.2), with at most one factor \(C_0\) per degree. All choices of matrices are made once for the datum and degree bound, independently of \(P\).

For integral \(P\), the product of the absolute determinants \(|\det A_j|\), \(d_0\le j\le D\), clears every coefficient of \(u_P\). Each recursive branch strictly lowers degree, so no determinant is needed twice. Equations (4.1) give the simultaneous denominator bound \(q_D\le Q_D\) in the theorem. These rational coefficients refer to words in the complex matrix units, before their conversion into Frobenius-unit real directions in §7.

Finally,

\[
 \|P\|_{\mathrm{coeff},1}
 \le\left(\sum_{|\alpha|\le D}\frac1{\alpha!}\right)^{1/2}\|P\|_F
 =\Xi_{M,D}\|P\|_F.
 \tag{4.4}
\]

The use of integral monomials in (4.1) and Fischer normalization in (4.4) is deliberate; replacing the matrix columns by orthonormal monomials before taking determinants would lose the integer determinant bound.

## 5. A fixed quantitative smooth bump

This construction works on \(U(J')\) of rank \(m\). Put \(d=m^2\), and identify its real Lie algebra with \(\mathbf R^d\) using a Frobenius-orthonormal basis. Define

\[
 \eta(t)=\begin{cases}e^{-1/(1-t^2)},&|t|<1,\\0,&|t|\ge1,\end{cases}
 \qquad I=\int_{-1}^1\eta(t)\,dt>\frac14,
\]

and \(\psi(y)=I^{-d}\prod_{i=1}^d\eta(y_i)\). It is a nonnegative smooth probability density. For every multi-index of order \(s\),

\[
 \|\partial^\alpha\psi\|_1\le512^s(s!)^2.
 \tag{5.1}
\]

One direct derivative bound is \(\sup|\eta^{(s)}|\le64^s(s!)^2\). For \(|t|<1\), apply Cauchy's estimate on the circle of radius \((1-|t|)/8\); there the real part of \(1/(1-z^2)\) is at least \(1/[8(1-|t|)]\). Optimizing the resulting exponential times \((1-|t|)^{-s}\) gives the bound. The same estimate makes every derivative tend to zero at the endpoints. Since \(I>1/4\), each coordinate differentiated at least once costs at most an additional factor eight in its normalized \(L^1\)-norm, proving (5.1).

Set \(b=\delta/(4m)\), and scale the density to \(\psi_b(y)=b^{-d}\psi(y/b)\). On its support the corresponding Lie matrix \(X\) satisfies \(\|X\|\le\|X\|_F\le\delta/4\). The Cayley map

\[
 g(X)=(1+X)(1-X)^{-1}
\]

sends its support into \(B_\delta\). If Haar measure pulls back as \(j(X)\,dX\), define

\[
 b_\delta(g(X))=\psi_b(X)/j(X),
\]

extended by zero. Then \(b_\delta\ge0\), it is smooth and compactly supported, and \(\int b_\delta\,dg=1\), for the actual chosen Haar measure.

There is no hidden estimate for \(j\) in the following \(L^1\) derivative bound. In Cayley coordinates the field \(D_Y\) is

\[
 V_Y(X)=\tfrac12(1-X)Y(1+X).
\]

Haar invariance gives \(\operatorname{div}(jV_Y)=0\), so

\[
 D_Y(f/j)=j^{-1}T_Yf,
 \qquad T_Yf=V_Y\cdot\nabla f+(\operatorname{div}V_Y)f.
 \tag{5.2}
\]

Thus \(\|D_{Y_1}\cdots D_{Y_s}b_\delta\|_{L^1(dg)}
=\|T_{Y_1}\cdots T_{Y_s}\psi_b\|_{L^1(dX)}\).

For \(\|Y\|_F\le1\), the sum of the absolute coefficients of all components of the quadratic polynomial vector field \(V_Y\) is at most
\(C=2(d+1)^3\). For example its constant, linear and quadratic parts are bounded respectively by
\(\sqrt d/2,d\sqrt d,d^2\sqrt d/2\). The coefficient sum of \(\operatorname{div}V_Y\) is at most \(2C\).

After \(s\) applications, write \(T_{Y_1}\cdots T_{Y_s}\psi_b\) as \(\sum_\alpha p_\alpha\partial^\alpha\psi_b\). Its coefficient sum obeys

\[
 H_{s+1}\le C(2s+3)H_s,\qquad H_0=1,
 \quad\text{hence}\quad
 H_s\le(2C)^s(s+1)!.
\]

On the support \(|y_i|\le b\le1\), coefficient sums bound polynomial values. Combining this with (5.1) and scaling gives

\[
 \boxed{
 p_{s,0}(b_\delta)
 \le\left(\frac{8192m(m^2+1)^3}{\delta}\right)^s
          (s+1)!(s!)^2.
 }
 \tag{5.3}
\]

The right-translation Cayley field is \(\tfrac12(1+X)Y(1-X)\) and has the same coefficient bounds. Since the group is unimodular, (5.2) and (5.3) also handle arbitrary mixed left/right words. These estimates are independent of Haar rescaling.

Pointwise smooth seminorms can be controlled too. In these Frobenius coordinates,

\[
 j(X)=j_0|\det(1-X)|^{-2m}.
\]

Indeed \(J'g^{-1}dg=2(1-X)^{-*}(J'\,dX)(1-X)^{-1}\); congruence by a matrix \(A\) on skew-Hermitian matrices has real determinant \(|\det A|^{2m}\). With the compact-dual Haar normalization used in the return chapter,

\[
 j_0=\frac{2^{m(m+1)/2}}{\operatorname{vol}U(m)},\qquad
 \operatorname{vol}U(m)=\prod_{a=0}^{m-1}\frac{2\pi^{a+1}}{a!}.
\]

The power of two accounts for the \(1/\sqrt2\) in each Frobenius off-diagonal basis vector and the derivative two of the Cayley map. Since
\(\sup|\partial^\alpha\psi_b|\le(4/b)^d(64/b)^s(s!)^2\), the same proof gives

\[
 \sup_g|D_{Y_1}\cdots D_{Y_s}b_\delta(g)|
 \le J_\delta(K_m/\delta)^s(s+1)!(s!)^2,
 \quad
 J_\delta=j_0^{-1}(1+\delta/4)^{2m^2}
                        (16m/\delta)^{m^2}.
 \tag{5.4}
\]

Thus an invariant weighted \(L^\infty\) version of (1.6) holds after multiplying its right side by \(J_\delta\). The dependence on Haar normalization in this pointwise statement is explicit.

## 6. A reproducer with a bounded scalar denominator

The near-identity coefficient estimate proved in §2 of [the Bessel-majorant chapter](lsernau-bessel-majorants.md) gives

\[
 |c_{l'}(g)-1|\le\frac12\quad(g\in B_\delta)
\]

for the choice (1.3). Hence

\[
 a_0=\int b_\delta(g)c_{l'}(g)\,dg,
 \qquad |a_0|\ge\tfrac12.
 \tag{6.1}
\]

For the probability Haar measure on \(K'\), let

\[
 q(k)=\dim\tau'\,\overline{m_{\Lambda'}(k)}\,dk.
\]

Compact Schur orthogonality and Cauchy–Schwarz give
\(\|q\|_{\rm TV}\le\sqrt{\dim\tau'}\). Set

\[
 \beta_0=a_0^{-1}q*b_\delta*q.
 \tag{6.2}
\]

The exact rank-one argument gives \(\pi'(\beta_0)x=x\). Its support lies in \(K'B_\delta K'\), where \(\|g\|\le1+\delta\). Moving invariant derivatives through the two compact convolutions conjugates their directions by elements of \(K'\); these preserve Frobenius norm. Thus

\[
 p_{s,A}(\beta_0)
 \le2\dim\tau'\,(1+\delta)^A
      (K_m/\delta)^s(s+1)!(s!)^2.
 \tag{6.3}
\]

This controls both the support and all invariant \(L^1\) smooth seminorms of a single exact reproducer. The scalar denominator in (6.1) is bounded uniformly; no unspecified near-identity limiting choice remains.

## 7. From differential words to the smearing map

Put \(\mathscr D_Y=-D_Y\). Integration by parts gives

\[
 \pi'(\mathscr D_Yf)=d\pi'(Y)\pi'(f).
\]

These operators extend to the complexified enveloping algebra with the same order as its products. A complex matrix unit is a linear combination of at most two Frobenius-unit vectors in the real unitary Lie algebra, with sum of absolute coefficients at most two. For example, if \(s=\epsilon_c'\epsilon_d'\) and \(c\ne d\), use

\[
 Y_1=(E_{cd}-sE_{dc})/\sqrt2,\qquad
 Y_2=i(E_{cd}+sE_{dc})/\sqrt2,\qquad
 E_{cd}=(Y_1-iY_2)/\sqrt2.
\]

For a diagonal matrix unit use \(E_{cc}=-i(iE_{cc})\). Define

\[
 \mathcal S_DP=\mathscr D_{u_P}\beta_0.
 \tag{7.1}
\]

Equations (4.3), (6.2) give (1.5), and differentiation does not enlarge support. A word of length at most \(s_*\) costs at most \(2^{s_*}\) when expanded into real unit directions. Combining (4.3), (4.4) and (6.3) gives precisely (1.6).

## 8. The remaining quantitative distinction

The construction is explicit in the usual mathematical sense: enumerate bounded-degree monomials and lowering words, compute integer highest kernels, select independent columns, solve finite integer systems, and apply the resulting differential words to one specified bump. It produces a common support, explicit seminorm bounds, an explicit word-length bound, and a simultaneous rational denominator bound for the algebraic operators.

It does **not** claim a comparable bound relative to \(\|P_lP\|_B\) alone. Two polynomials with the same projection can receive different smearing functions, and \(P_l\) can have small singular values on other finite-degree directions even though its value on \(\Phi\) has a lower bound. Passing to a bounded right inverse on the projected Hilbert space would require controlling that additional quotient norm. The integer-matrix argument solves the stated problem with the original polynomial as input.

Nor is (1.6) asserted to fit the numerical global chain gauges. With \(N=\binom{rm+D}{rm}\), the Cramer loss is much larger than a small fixed power of the height parameters. Improving that loss, or showing that a particular chain needs only a much smaller family of polynomial directions, remains a separate quantitative task. The local estimate is nevertheless uniform and eliminates the previous nonuniform choice of smearing functions on every fixed-degree polynomial space.

### Exact finite checks

The script [check_quantitative_local_smearing.py](../scripts/check_quantitative_local_smearing.py) was run successfully. It builds the truncated spaces, computes integer bases for the highest-vector kernels, selects full-rank columns, and verifies their nonzero integer determinants. It checks 23 spanning matrices in four examples, with maximum dimension 84. The examples include noncompact column recursion, two noncompact factors, and a nontrivial compact row raising equation. The noncompact parameters are deliberately small and do not satisfy the source large gap; these are exact algebraic checks, not analytic certificates. The output is [quantitative-local-smearing.json](../certificates/quantitative-local-smearing.json). No bump integral, derivative seminorm, theta integral, or Lean build was computationally tested.

### Source correspondence

The finite truncation refines `New.IsJointHarmonic.howe_argument`, lines 535–599 of `Lib/DiscreteSeries/Theta/LocalCorrespondence.lean`, at the immutable revision
`72fead102f663d5c7a407964a13dc0cf9d977207` (blob `768df29f7cc12b6c814dacea70ca8d4afcef6d36`). The proof above exposes the finite spaces and coefficients rather than citing that declaration as a proof. The polynomial actions, their Banach differentiability, the layer-minor height, and the projected kernel relations are proved in the linked noncompact chapter. The bump estimates in §§5–7 are derived here directly.
