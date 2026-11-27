# Classical suppliers for the noncompact discrete-series kernel

## Result and its dependencies

The discrete-series package isolated in §6 of [the noncompact real-edge chapter](lsernau-noncompact-real-edges.md) can be supplied by classical representation theory, with its normalizations checked explicitly. The main ingredients are Vogan–Zuckerman's construction and recognition of cohomologically induced representations, Sun's bottom-layer coefficient formula, and the Dirac inequality. The arguments below specialize those theorems to the exact unitary groups and parameters used in the source.

There is a useful simplification: **the coefficient-rigidity assertion needs regular integral parameters, but no additional opposite-sign gap**. The gap is needed for the weighted absolute integrability used in Banach-space projection and smoothing. The proof of rigidity first forces equality of Casimir scalars by the Dirac inequality, then applies Vogan–Zuckerman's Proposition 6.1. It does not infer a representation from its quadratic Casimir alone.

This chapter proves an ordinary mathematical implication from explicitly cited classical theorems. It does not reprove the general discrete-series construction, cohomological induction, the Dirac-square formula, or the direct-integral theorem. It also does not assert a new Lean replay. The source revision remains

`lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207`.

## 1. Parameters, compact weights and principal minors

Let

\[
 G=U(J),\qquad J=\operatorname{diag}(\epsilon_1,\ldots,\epsilon_r),
 \qquad \epsilon_i\in\{1,-1\},\qquad K=U(r)\cap G.
\]

For the noncompact case both signs occur. Order the indices so that

\[
 \lambda_1>\cdots>\lambda_r,\qquad
 \lambda_i\in (r-1)/2+\mathbf Z.
 \tag{1.1}
\]

The source parameter is \(l=2\lambda\). All positive roots are \(e_i-e_j\), \(i<j\); such a root is compact when \(\epsilon_i=\epsilon_j\). Let \(\rho_c,\rho_n\) be the half-sums of compact and noncompact positive roots, and \(\rho=\rho_c+\rho_n\). In these coordinates

\[
 \rho_i=(r+1-2i)/2,
 \qquad
 \nu=\lambda-\rho,
 \qquad
 \Lambda=\lambda+\rho_n-\rho_c=\nu+2\rho_n.
 \tag{1.2}
\]

Here \(\nu\) is integral and dominant for all positive roots: consecutive entries of \(\lambda\) differ by a positive integer, so

\[
 \nu_i-\nu_{i+1}=\lambda_i-\lambda_{i+1}-1\ge0.
 \tag{1.3}
\]

Both \(\Lambda\) and \(\lambda-\rho_c\) are compact dominant. Indeed, if \(i<j\) are consecutive indices of one sign, then

\[
 (\lambda-\rho_c)_i-(\lambda-\rho_c)_j
 =\lambda_i-\lambda_j-1\ge0.
 \tag{1.4}
\]

For arbitrary same-sign \(i<j\), the difference \((\rho_n)_i-(\rho_n)_j\) is the number of opposite-sign indices strictly between them. Thus \(\rho_n\) is compact dominant as well. These elementary checks are the dominance hypotheses needed below.

For an integral weight \(w\), define \(m_w(A)\) by its distinct levels \(t_1<\cdots<t_s\):

\[
 m_w(A)=(\det A)^{t_1}
 \prod_{a=2}^s
 \det(A_{I_a,I_a})^{t_a-t_{a-1}},
 \qquad I_a=\{i:w_i\ge t_a\}.
 \tag{1.5}
\]

This definition agrees with the source's product over integer levels, including its determinant factors at negative levels. We use it on positive-definite matrices, where it is positive, and on the relevant compact block matrices. For compact-dominant \(w=\Lambda\), its restriction to \(K\) is the coefficient of a unit highest vector \(v\) in the irreducible compact representation \(\tau=\tau_\Lambda\):

\[
 m_\Lambda(k)=\langle v,\tau(k)v\rangle,
 \qquad
 a_\Lambda:=\int_K|m_\Lambda(k)|^2\,dk
 =\frac1{\dim\tau}.
 \tag{1.6}
\]

The compact Haar measure has mass one, and inner products are conjugate-linear in the first variable. Formula (1.6) follows by realizing the highest vector as a tensor of exterior-power highest vectors and determinant characters, then applying compact Schur orthogonality. This also fixes the convention when some entries of \(\Lambda\) are negative.

## 2. The classical realization and the group hypotheses

Let \(\mathfrak b=\mathfrak t\oplus\mathfrak n\) be the upper triangular Borel for the order (1.1). It is stable under the Cartan involution of \(G\), and its real Levi group is the compact diagonal torus \(T\). The integral vector \(\nu\) defines a unitary character of \(T\). Equation (1.3) verifies the admissibility condition (5.1) of Vogan–Zuckerman: the character has nonnegative pairing with every root of \(\mathfrak n\).

We use the following published classical facts in this specialization. Vogan–Zuckerman's Theorem 5.3 constructs \(A_{\mathfrak b}(\nu)\), gives its infinitesimal character \(\nu+\rho\), its bottom compact type \(\nu+2\rho_n\), and its compact-weight support. Their Theorem 6.16, together with (6.13)–(6.15), identifies it as the discrete series with parameter \(\nu+\rho\): the split component of the Borel Levi is trivial, so the inducing parabolic in that theorem is the whole group. Sun's §6.3 gives multiplicity one of the bottom type. These are cited theorems, not conclusions drawn from source-file names. [VZ84, pp. 73–74 and 82–83; Sun07, p. 220]

The semisimple statements in [VZ84] apply first to \(SU(p,q)\), where \(p,q\) count the two signs. The passage to \(U(p,q)\) preserves the specified compact central character. More explicitly,

\[
 U(p,q)=Z(U(p,q))\,SU(p,q),
\]

and the two factors intersect in a finite central subgroup. The character on the center is fixed by \(\sum_i\Lambda_i=\sum_i\lambda_i=\sum_i\nu_i\). Its restriction to the finite intersection agrees with the character of the bottom type, so the representation descends from the product to \(U(p,q)\). This gives a genuine irreducible unitary discrete series \(\pi_\lambda\), not just a Lie-algebra module. Since the center is compact, square integrability modulo the center gives square integrability for a Haar measure on \(G\).

Let \(v\) be a unit highest vector in its bottom compact type and set

\[
 c_\lambda(g)=\langle v,\pi_\lambda(g)v\rangle,
 \qquad
 \kappa_\lambda=\sum_i\lambda_i^2-\frac{r(r^2-1)}{12}.
 \tag{2.1}
\]

With the trace-form normalization, \(\Omega=\sum_{i,j}E_{ij}E_{ji}\) acts by \(\kappa_\lambda\). In particular \(c_\lambda(1)=1\).

Sun's group assumptions also hold: \(G\) is connected and reductive, and its connected derived group \(SU(p,q)\) has finite center. The chosen Borel is one of the allowed theta-stable parabolics, its Levi character is \(\nu\), and its bottom extremal weight is exactly \(\Lambda\). No stable-range theta-correspondence hypothesis is involved here.

## 3. Sun's formula in the source's principal-minor conventions

The relevant result in the **published** Sun paper is Theorem 6.3 and its specialization (26) in §6.3, p. 220. The source header's reference to “Theorem 1.1” does not identify this statement in the published article.

Write \(P_v\) for the orthogonal projection onto \(\mathbf Cv\). Sun's formula, specialized to \(A_{\mathfrak b}(\nu)\), is

\[
 P_\tau\pi_\lambda(kx^2)|_\tau
 =\dim\tau\int_K
  (\delta_{\mathfrak n}\nu)(\widetilde H_{\mathfrak b}(ux))
  \tau(ku^{-1})P_v\tau(u)\,du,
 \quad k\in K,\quad x\in\exp\mathfrak p.
 \tag{3.1}
\]

Here \(\delta_{\mathfrak n}\) is the determinant of the adjoint action on \(\mathfrak n\), so its weight is \(2\rho\). Consequently \(\delta_{\mathfrak n}\nu\) has weight

\[
 2\rho+\nu=\lambda+\rho.
 \tag{3.2}
\]

We now determine \(\widetilde H_{\mathfrak b}\) and the minor orientation directly. Put \(z=x^2>0\). The complex group is \(GL_r(\mathbf C)\), its compact real form is \(U(r)\), and the decomposition in Sun's (7) is upper triangular times compact. Factor

\[
 ux=n a v_0,\qquad
 n\text{ upper unipotent},\quad
 a=\operatorname{diag}(a_1,\ldots,a_r)>0,\quad v_0\in U(r).
\]

Then

\[
 uzu^*=n a^2n^*,\qquad
 \widetilde H_{\mathfrak b}(ux)=a^2.
 \tag{3.3}
\]

The latter uses the compact conjugation \(y\mapsto(y^*)^{-1}\) in Sun's Flensted–Jensen duality. It is not the holomorphic Cartan involution on the complex diagonal torus. Keeping this distinction prevents a spurious constant value of \(\widetilde H\).

For an upper unipotent \(n\), the determinant on the **trailing** index set \(\{j,\ldots,r\}\) in \(n a^2n^*\) is \(\prod_{i=j}^r a_i^2\). This follows because rows with indices at least \(j\) involve only columns with indices at least \(j\). The weight

\[
 w=-\lambda-\rho
\]

is strictly increasing in the index, and its superlevel sets in (1.5) are precisely such trailing intervals. Therefore

\[
 m_{-\lambda-\rho}(uzu^*)
 =\prod_i(a_i^2)^{-\lambda_i-\rho_i},
\]

and (3.2)–(3.3) give

\[
 (\delta_{\mathfrak n}\nu)(\widetilde H_{\mathfrak b}(ux))
 =m_{-\lambda-\rho}(uzu^*)^{-1}>0.
 \tag{3.4}
\]

Taking the coefficient of \(v\) in (3.1), changing \(u\) to \(u^{-1}\), and using compact covariance now yield

\[
 \boxed{
 c_\lambda(pzq^{-1})
 =\frac1{a_\Lambda}\int_K
 \frac{m_\Lambda(pu)\overline{m_\Lambda(qu)}}
 {m_{-\lambda-\rho}(u^*zu)}\,du
 },\qquad p,q\in K,\quad z>0\text{ in }G.
 \tag{3.5}
\]

For completeness, first take \(q=1\) in (3.1). To obtain general \(p,q\), write \(pzq^{-1}=(pq^{-1})(qzq^{-1})\) and then change the integration variable from \(u\) to \(qu\). This gives exactly the numerator and denominator in (3.5).

Equation (3.5) is the expression in the source's `dsCoeff_polar`, with `paramAddRho l` equal to \(\lambda+\rho\) and `kTypeNormSq` equal to \(a_\Lambda\). It fixes both the phase and the normalization: at \(p=q=z=1\), the integral is \(a_\Lambda\). Thus it supplies a genuine discrete-series realization for the ordinary mathematical kernel used in the preceding chapters.

## 4. The positive compact average, including its constant

Fix a Haar measure \(dg\) on \(G\) and put

\[
 d_\lambda=\left(\int_G|c_\lambda(g)|^2\,dg\right)^{-1}>0,
 \qquad e_\lambda=d_\lambda\overline{c_\lambda}.
 \tag{4.1}
\]

Let \(\sigma\) be a representation preserving a positive Hermitian form \(B\), and let \(x\) be compact highest of weight \(\Lambda\). The following calculation is valid in its Hilbert completion, or directly for continuous compact integrals. Put

\[
 W(z)=m_{-\lambda-\rho}(z)>0\quad(z>0).
\]

For \(g=k_0z\), the average in question is

\[
 I(g)=\int_{K\times K}e_\lambda(k_1^{-1}gk_2)
     B(x,\sigma(k_1^{-1}gk_2)x)\,dk_1dk_2.
\]

Insert the conjugate of (3.5), and, for fixed \(u\), set

\[
 a=k_1^{-1}k_0u,\qquad b=u^{-1}k_2,\qquad t=u^{-1}zu.
\]

The compact integrand becomes

\[
 \frac{d_\lambda}{a_\Lambda W(t)}
 \overline{m_\Lambda(a)}\,\overline{m_\Lambda(b)}
 B(x,\sigma(atb)x).
\]

The operator \(\int_K\overline{m_\Lambda(k)}\sigma(k)\,dk\) is \(a_\Lambda\) times the orthogonal projection onto the highest-vector lines of all copies of \(\tau_\Lambda\). In particular it fixes \(x\) up to the scalar \(a_\Lambda\). Applying it first to the \(b\)-integral and then to the \(a\)-integral gives

\[
 \boxed{
 I(k_0z)=d_\lambda a_\Lambda
       \int_KW(u^{-1}zu)^{-1}
       B(x,\sigma(u^{-1}zu)x)\,du.
 }
 \tag{4.2}
\]

All factors outside the last coefficient are positive. This proves exactly the normalization required in §6.2 of the noncompact chapter. When that last coefficient is positive on positive-definite elements, as proved there for the relevant polynomial Gaussian, the average is strictly positive. Absolute integrability, established next, then makes the nonzero-projection argument legitimate.

## 5. Weighted integrability, Schur identities and compact smoothing

Fix a growth exponent \(A\ge0\), and let

\[
 h=\min_{\epsilon_i\ne\epsilon_j}|\lambda_i-\lambda_j|.
\]

The principal-minor argument in [the Bessel-majorant chapter, §1](lsernau-bessel-majorants.md) starts from (3.5) and proves, for every integer \(0\le m\le h\),

\[
 |c_\lambda(g)|\le\min\{1,(2/\|g\|)^m\}.
 \tag{5.1}
\]

Its use here is not circular: (3.5) has now been supplied from Sun's theorem, and the minor inequalities and the packing argument in that chapter are elementary. The latter gives, for this fixed Haar measure,

\[
 \operatorname{vol}\{g:\|g\|\le R\}\le C_G R^{4r^2},\qquad R\ge1,
 \tag{5.2}
\]

where \(C_G<\infty\) depends on a compact identity neighborhood and its volume. Summing over dyadic shells proves

\[
 \int_G|c_\lambda(g)|\|g\|^A\,dg<\infty
 \quad\text{if some integer }m\le h\text{ satisfies }m>A+4r^2.
 \tag{5.3}
\]

The source hypothesis \(h\ge500r^3+A\) is more than sufficient. Square integrability alone would not give (5.3); the gap and (5.1) are the extra inputs.

For the same Haar measure, discrete-series Schur orthogonality gives

\[
 \pi_\lambda(e_\lambda)=P_v,\qquad
 e_\lambda*e_\lambda=e_\lambda,\qquad
 e_\lambda^*=e_\lambda.
 \tag{5.4}
\]

Here \(\sigma(f)=\int f(g)\sigma(g)\,dg\),
\((f_1*f_2)(g)=\int f_1(y)f_2(y^{-1}g)\,dy\), and
\(f^*(g)=\overline{f(g^{-1})}\). The compact center causes no modular factor. The right-convolution convention in the quantitative-return chapter uses the conjugate kernel; that chapter explicitly records the conversion.

The exact compact reproducing bump is now an unconditional consequence of this classical realization. To recall the construction, let

\[
 q(k)=\dim\tau\,\overline{m_\Lambda(k)}\,dk
\]

be the compactly supported measure on \(K\). Multiplicity one gives \(\pi_\lambda(q)=P_v\). Choose a compact smooth approximate-identity term \(b\) with

\[
 a=\langle v,\pi_\lambda(b)v\rangle\ne0,
\]

which is possible because this number tends to one along the approximate identity. Then

\[
 \beta=a^{-1}q*b*q\in C_c^\infty(G),\qquad
 \pi_\lambda(\beta)=P_v,
 \qquad
 \beta*e_\lambda=e_\lambda=e_\lambda*\beta.
 \tag{5.5}
\]

The last identities follow from the rank-one Schur identities; adjoints cause no additional assumption because \(\pi_\lambda(\beta^*)=P_v\) as well. Differentiating the compact factor on the appropriate side of (5.5) proves weighted \(L^1\)-integrability of every left or right derivative of \(e_\lambda\). For mixed derivatives use \(e_\lambda=\beta*e_\lambda*\beta\) and move each family to its compact outer factor. The norm bound \(\|xy\|\le\|x\|\|y\|\), compact support of those derivatives, and (5.3) justify weighted Young's inequality twice.

This constructs an exact bump for each parameter. It does not claim uniform bounds for all of its seminorms. The quantitative-return chapter obtains its derivative-family bounds from the unitary representation and Schur orthogonality, so such a uniform bump estimate is not required there.

## 6. Compact root-cone support

Vogan–Zuckerman's Theorem 5.3(c), specialized to the Borel, says that every compact highest weight \(\mu\) of \(A_{\mathfrak b}(\nu)\) has the form

\[
 \mu=\Lambda+\sum_{\substack{i<j\\\epsilon_i\ne\epsilon_j}}
             n_{ij}(e_i-e_j),\qquad n_{ij}\in\mathbf Z_{\ge0}.
 \tag{6.1}
\]

This is stronger than the full positive-root-cone support required in the noncompact chapter. To check its agreement with the source's polar-cone definition, define

\[
 \mathcal C=\Bigl\{\beta\in\mathbf Z^r:
      \sum_i\beta_i=0,\quad
      \sum_{i=1}^j\beta_i\ge0\ (1\le j<r)\Bigr\}.
 \tag{6.2}
\]

The equality

\[
 \beta=\sum_{j=1}^{r-1}
       (\beta_1+\cdots+\beta_j)(e_j-e_{j+1})
\]

shows that (6.2) is the cone generated by all positive roots. If \(o_1<\cdots<o_r\), summation by parts gives

\[
 o\cdot\beta=-\sum_{j=1}^{r-1}(o_{j+1}-o_j)
                   (\beta_1+\cdots+\beta_j)\le0.
\]

Conversely, this inequality for every strictly increasing \(o\) forces \(\sum_i\beta_i=0\), by translating \(o\) by arbitrary constants. It forces each partial sum to be nonnegative by making its corresponding positive gap in \(o\) arbitrarily large. Thus \(\mathcal C\) is exactly `HCParam.rootCone` in the order of \(l\). Equation (6.1) proves the required assertion \(\mu-\Lambda\in\mathcal C_l\).

## 7. Casimir rigidity for an irreducible unitary representation

### 7.1 The Dirac bound at the specified compact type

Let \(\Pi\) be an irreducible unitary representation of \(G\) containing \(\tau_\Lambda\), and suppose \(\Omega\) acts by the real scalar \(c\). We claim

\[
 c\le\kappa_\lambda.
 \tag{7.1}
\]

We use two standard finite-dimensional facts about the spin representation \(S\) for \(\mathfrak p\). It contains the compact representation of highest weight \(\rho_n\), and the total spin representation is self-dual. Hence it contains the dual representation with lowest weight \(-\rho_n\). The PRV component theorem says that the compact-dominant conjugate of a highest weight plus a lowest weight occurs in the tensor product. These precise facts are also stated and used in Parthasarathy's proof of Proposition 3.2. [Par15, pp. 172–173]

By (1.4), the relevant sum is already compact dominant:

\[
 \zeta=\Lambda-\rho_n=\lambda-\rho_c.
 \tag{7.2}
\]

Thus the spin-cover compact type of highest weight \(\zeta\) occurs in \(\Pi\otimes S\). The Dirac-square identity and unitarity give, on this type,

\[
 0\le D^2
 =-\bigl(c+\|\rho\|^2\bigr)+\|\zeta+\rho_c\|^2
 =-c-\|\rho\|^2+\|\lambda\|^2.
 \tag{7.3}
\]

This is (7.1). The sign in (7.3) is essential. The identity used is the general formula (3.2) in [HPP11], followed by its Proposition 3.3; no assertion specific to Wallach representations is being imported.

For clarity about the central normalization, apply the semisimple identity on \(SU(p,q)\). Put \(s=\sum_i\lambda_i\). The central element \(\sum_iE_{ii}\) acts by \(s\), and

\[
 \Omega_{\mathfrak{gl}_r}=\Omega_{\mathfrak{sl}_r}
                     +\frac1r\Bigl(\sum_iE_{ii}\Bigr)^2.
\]

Subtracting the common center \((s/r)(1,\ldots,1)\) from \(\lambda\) and \(\zeta\), and then adding \(s^2/r\) back on both sides, gives exactly (7.3) with the Euclidean coordinate norm. Thus no Killing-form scale or compact-central term has been silently dropped.

### 7.2 Equality and recognition

Assume now \(c\ge\kappa_\lambda\). Equation (7.1) forces

\[
 c=\kappa_\lambda.
 \tag{7.4}
\]

Apply **Vogan–Zuckerman, Proposition 6.1**, p. 78, to the Borel and its character \(\nu=\lambda-\rho\). Its hypotheses are:

- the character is admissible in the sense of (5.1);
- it vanishes on the complement of the compact Cartan in the chosen Cartan;
- the representation is irreducible unitary;
- the bottom compact type occurs and the Casimir scalar is the prescribed one.

Admissibility was checked in (1.3). The second condition is empty because the Borel Levi and Cartan are compact. Occurrence is the assumption on \(\Pi\), and (7.4) is the required Casimir scalar. Rescaling from the trace form to the Killing form rescales both prescribed Casimir scalars by the same factor, preserving their equality. The proposition identifies the Harish-Chandra module of \(\Pi\) with \(A_{\mathfrak b}(\nu)\), hence with that of \(\pi_\lambda\).

As above, the semisimple theorem applies to the restriction to \(SU(p,q)\). This restriction is irreducible: the center of \(U(p,q)\) acts by scalars, and any closed \(SU(p,q)\)-invariant subspace is therefore \(G\)-invariant. The central character is fixed by the occurring compact type, so the identification extends to \(G\). Unitary globalizations of the same irreducible Harish-Chandra module are unitarily equivalent. Multiplicity one of \(\tau_\Lambda\) gives, for a highest vector \(x\),

\[
 \langle x,\Pi(g)x\rangle
 =\|x\|^2c_\lambda(g).
 \tag{7.5}
\]

This proves the irreducible rigidity assertion for every parameter satisfying (1.1). Its proof uses no gap estimate. If the group is compact, the same conclusion follows directly from compact highest-weight theory; for \(r=1\) it is the corresponding character identity.

## 8. Passage to the source's positive-form Banach representation

Suppose \(X\) is a Banach space, \(\sigma\) is a strongly continuous representation of \(G\) on \(X\), and \(B\) is a continuous positive-definite invariant Hermitian form. Let \(x\in X\) be smooth, compact highest of weight \(\Lambda\), and satisfy

\[
 d\sigma(\Omega)x=cx,\qquad c\in\mathbf R,\qquad c\ge\kappa_\lambda.
 \tag{8.1}
\]

Completion for \(B\) gives a Hilbert space \(\mathcal H\). Continuity of \(B\) makes the inclusion \(X\to\mathcal H\) continuous. The operators \(\sigma(g)\) extend as isometries, and strong continuity on the completion follows first on the dense subspace \(X\), then on all of \(\mathcal H\). Banach smoothness implies Hilbert smoothness of \(x\), so (8.1) remains valid there.

Consider the closed cyclic space generated by \(x\). It is separable, since \(G\) is second countable and \(g\mapsto\sigma(g)x\) is continuous. We use Harish-Chandra's type-I theorem and admissibility of irreducible unitary representations: this cyclic unitary representation decomposes into irreducible unitary representations \(\Pi_t\). The type-I statement is recalled in [ALTV, §1, p. 5]; admissibility is recalled in [VZ84, p. 54].

Here is a bounded-operator justification that the specified Casimir passes to the fibers. Choose a countable compact smooth approximate identity \(f_j\). Let \(\Omega_G\) denote the differential operator on test functions normalized by

\[
 \Pi(\Omega_Gf)=d\Pi(\Omega)\Pi(f)
\]

for smooth representations. Integration by parts is valid because \(f\) is compactly supported. Centrality of \(\Omega\) and (8.1) give

\[
 \sigma(\Omega_Gf_j)x=c\,\sigma(f_j)x.
 \tag{8.2}
\]

Both integrated operators in (8.2) are bounded and decompose fiberwise. Outside one null set, (8.2) holds in every fiber for all \(j\). Admissibility implies that the Casimir acts in \(\Pi_t\) by a scalar \(c_t\), so

\[
 (c_t-c)\Pi_t(f_j)x_t=0\quad\text{for every }j.
\]

Since \(\Pi_t(f_j)x_t\to x_t\), every fiber with \(x_t\ne0\) has \(c_t=c\). This avoids assuming, without proof, that an unbounded Casimir operator decomposes on a prescribed domain.

The compact rank-one averaging operator

\[
 Q_\Lambda=\dim\tau\int_K\overline{m_\Lambda(k)}\sigma(k)\,dk
\]

is bounded and fixes \(x\). It too decomposes fiberwise, so each nonzero \(x_t\) is compact highest of weight \(\Lambda\). If the highest-vector hypothesis was initially expressed by compact Lie-algebra equations, the same assertion follows from the unitary compact decomposition: only highest vectors of the compact type \(\Lambda\) survive those equations. This also proves that the compact orbit of \(x\) spans a finite-dimensional copy of \(\tau_\Lambda\).

Section 7 applies in every nonzero fiber. Its normalized highest-vector coefficient is \(c_\lambda\), and integrating the fiber coefficients yields

\[
 \boxed{
 B(x,\sigma(g)x)=B(x,x)c_\lambda(g)\quad(g\in G).
 }
 \tag{8.3}
\]

The polynomial Banach growth bound is not needed for this Hilbert-space recognition. It is needed for the Bochner integrals in the projection and smearing statements. If \(\|\sigma(g)\|\ll\|g\|^A\), (5.3) gives those integrals in the original Banach space. Equality established in the Hilbert completion is equality in the Banach space, because positive definiteness makes the inclusion injective. Thus the exact compact-support smoothing argument of the preceding chapter applies with its analytic package now supplied.

## 9. A separate check using adjacent compact types

The preceding proof is the main rigidity argument. The following elementary calculation checks its compatibility with the alternative recognition theorem of Parthasarathy, which characterizes the discrete series by occurrence of \(\Lambda\) and absence of compact-dominant \(\Lambda-\alpha\) for positive noncompact roots \(\alpha\). It also gives an explicit strict Dirac obstruction when \(h>1\). [Par15, Theorem 1.1]

Put \(a=\lambda-\rho_c\). Within each sign block it is decreasing, with integral successive differences. Fix \(i<j\) of opposite signs. Compact sorting of \(a-e_i+e_j\) gives

\[
 \operatorname{dom}_{W_K}(a-e_i+e_j)
 =a-e_{i_0}+e_{j_0},
 \tag{9.1}
\]

where \(i_0\) is the last index in the same-sign tie of \(a_i\), and \(j_0\) is the first index in the same-sign tie of \(a_j\). To see this, decrementing a single entry by one can only move it past entries of its original value; all lower distinct values differ by at least one. Incrementing an entry has the dual description. The two changes lie in different sign blocks.

If \(a_i=a_{i_0}\), then

\[
 \lambda_i-\lambda_{i_0}
 =\#\{t:i<t\le i_0,\ \epsilon_t=\epsilon_i\}.
\]

The left side is at least \(i_0-i\), by (1.1), while the right side is at most \(i_0-i\). Equality forces every intervening index to have the same sign and every intervening gap in \(\lambda\) to be one. The analogous statement holds between \(j_0\) and \(j\). Since the original \(i,j\) have opposite signs, it follows that \(i_0<j_0\), and hence

\[
 \lambda_{i_0}-\lambda_{j_0}\ge h.
\]

If the compact type \(\mu=\Lambda-e_i+e_j\) occurred, the PRV component of \(\tau_\mu\otimes\tau_{\rho_n}^*\) would have the weight in (9.1). Its Dirac norm would satisfy

\[
 \|\operatorname{dom}_{W_K}(\mu-\rho_n)+\rho_c\|^2
 =\|\lambda\|^2-2(\lambda_{i_0}-\lambda_{j_0})+2
 \le\|\lambda\|^2-2h+2.
 \tag{9.2}
\]

For \(h>1\), this is strictly below \(\|\lambda\|^2\), contradicting the Dirac inequality when \(c\ge\kappa_\lambda\). This verifies the forbidden-type condition in Parthasarathy's theorem throughout the source gap range. It is not needed to remove the gap from the main argument in §7.

## 10. Verification record and precise boundary

The exact-arithmetic script [check_discrete_series_suppliers.py](../scripts/check_discrete_series_suppliers.py) was run successfully. It checks:

- 3,362 integral-parameter, compact-dominance and bottom-PRV identities;
- 16,416 lowered-PRV sorting identities, including 8,442 strict inequalities when \(h>1\);
- 84 upper-Cholesky principal-minor identities, including negative and mixed weights.

The certificate is [discrete-series-suppliers.json](../certificates/discrete-series-suppliers.json). The tests use rational arithmetic and no floating point. They check finite conventions and edge cases; they do not computationally certify the cited representation-theoretic theorems, integrals or a Lean build.

Relative to the stated classical theorems, §§2–8 supply all three parts of \(\mathrm{DS}(l,A)\) in §6 of the noncompact chapter: genuine normalized coefficient and weighted integrability, positive polar averaging, and root-cone support with positive-form Casimir rigidity. The explicit harmonic construction and compact-support smearing implications in that chapter can therefore use these suppliers. The quantitative-return chapter can likewise use the genuine coefficient in its Schur argument.

The companion [projection-bound chapter](lsernau-projection-lower-bound.md) uses this package to give an explicit lower norm and reciprocal bound on the harmonic line. [Quantitative local smearing](lsernau-quantitative-local-smearing.md) supplies explicit finite-degree maps in the original polynomial norm. Fitting their losses into the chain budget, global arithmetic theta tests and full-chain gauge/norm assembly remain separate. Closing this local analytic package does not by itself close a historical proof-map node.

### Primary references

- **[VZ84]** D. A. Vogan, Jr. and G. J. Zuckerman, *Unitary representations with non-zero cohomology*, Compositio Mathematica **53** (1984), 51–90. [Publisher archive PDF](https://numdam.org/item/CM_1984__53_1_51_0.pdf). The specific results used are (5.1), Theorem 5.3, Proposition 6.1, and Theorem 6.16 with (6.13)–(6.15). The relevant printed pages 73, 74, 78, 82 and 83 were inspected, including the displayed formulas.
- **[Sun07]** B. Sun, *Matrix coefficients of cohomologically induced representations*, Compositio Mathematica **143** (2007), 201–221, DOI 10.1112/S0010437X06002508. [Publisher full PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2691743B10189C85555AD30421582301/S0010437X06002508a.pdf/matrix_coefficients_of_cohomologically_induced_representations.pdf). Use §2.2, (7), Theorem 6.3 and formula (26), rather than the source header's “Theorem 1.1”.
- **[HPP11]** J.-S. Huang, P. Pandžić and V. Protsak, *Dirac cohomology of Wallach representations*, Pacific Journal of Mathematics **250** (2011), 163–190. [Publisher PDF](https://msp.org/pjm/2011/250-1/pjm-v250-n1-p06-p.pdf). Only the general Dirac-square identity (3.2) and its unitary inequality, Proposition 3.3, are used.
- **[Par15]** R. Parthasarathy, *Classification of discrete series by minimal K-type*, Representation Theory **19** (2015), 167–185, DOI 10.1090/ert/467. [Author-uploaded published paper](https://www.researchgate.net/publication/282775275_Classification_of_discrete_series_by_minimal_-type). Theorem 1.1 and the spin/PRV discussion in the proof of Proposition 3.2 are the relevant passages.
- **[ALTV]** J. Adams, M. van Leeuwen, P. Trapa and D. Vogan, *Unitary representations of real reductive groups*. [Author manuscript](https://math.mit.edu/~dav/hermitianFormsSMFfinalC.pdf), §1, p. 5, for the stated type-I direct-integral theorem of Harish-Chandra.

### Immutable source correspondences

All paths are under `grh/src/` at the pinned revision above. The ordinary proofs in this chapter use the primary references and displayed calculations, not these declarations as axioms.

| Source path | Corresponding content | Git blob SHA |
|---|---|---|
| `Lib/DiscreteSeries/FlenstedJensen/PsiKTypes.lean` | `dsCoeff_polar`, lines 87–108; coefficient and compact-cone conventions | `410c54e38d20e4c29f56b4a2aab4f9d750f95975` |
| `Lib/DiscreteSeries/FlenstedJensen/SquareIntegrability.lean` | coefficient realization and Schur normalization | `d6cc5f4a9f2831f12a22e272581732bb436688b9` |
| `Lib/DiscreteSeries/Rigidity/HighestVectorsAndFiltration.lean` | the source's filtration route to rigidity | `e9814b21cc102732e5840c7d160de1cce92df4cc` |
| `Lib/DiscreteSeries/Rigidity/KernelFixes.lean` | positive compact average, lines 348–433; coefficient rigidity, lines 510–595 | `2a41b692a2e3af63716d039f57acd193e848e6cc` |
