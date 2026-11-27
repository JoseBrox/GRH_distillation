# An explicit lower bound for the noncompact harmonic projection

## Result

The positive polar formula gives more than qualitative nonvanishing.
It gives a uniform lower bound for the projection of the explicit
highest polynomial onto the specified discrete-series line. The
formal degree and the choice of Haar measure cancel from the bound.

Use the matching Fock datum of
[the noncompact real-edge chapter](lsernau-noncompact-real-edges.md).
Let the row group be \(G=U(J)\) of rank \(r\), let the column rank be
\(m\), and put \(M=rm\), the number of complex polynomial variables.
Let \(\Phi\ne0\) be its homogeneous joint highest harmonic of degree
\(D\). Suppose that the doubled row parameter \(l=2\lambda\) satisfies
\(|l_i|\le L\). Write \(\tau=\tau_\Lambda\) for its bottom compact type,
\(e_l=d_l\overline{c_l}\) for the normalized discrete-series kernel,
and \(P_l=\pi(e_l)\).

The representation and kernel are the genuine ones supplied by
[the classical supplier chapter](lsernau-discrete-series-suppliers.md).
In particular, weighted integrability makes \(P_l\) a bounded operator
on the source Banach space. For the numerical estimate below it
suffices in addition that an integer \(h\ge4r^2\) be available in the
coefficient decay
\[
 |c_l(g)|\le\min\{1,(2/\|g\|)^h\}.
 \tag{0.1}
\]
The source matching gap is much larger than this threshold.

Set
\[
 \beta=L+r+1,\qquad
 T=D+M+2r\beta+1,\qquad \delta=\frac1{4T}.
 \tag{0.2}
\]
Normalize the invariant positive Hermitian form \(B\) so that its
restriction to polynomial Gaussians is the Fischer form and the
vacuum has norm one. Then
\[
 \boxed{\quad
 \frac{\|P_l\Phi\|_B^2}{\|\Phi\|_F^2}
 \ge\frac1{4\dim\tau}
       \left(\frac1{48T}\right)^{2r^2}.
 \quad}
 \tag{0.3}
\]
Consequently
\[
 \boxed{\quad
 \|P_l\Phi\|_B^{-1}
 \le\frac{2\sqrt{\dim\tau}\,(48T)^{r^2}}{\|\Phi\|_F}.
 \quad}
 \tag{0.4}
\]
The norm on the left is the norm of the invariant positive form.
It is not the integrable-coefficient Banach norm used to define
the Bochner projection.

## 1. A lower bound for the positive polar integrand

Use the operator norm in the sign frame \(J\), and put
\[
 B_\delta=\{g\in G:\|g-1\|\le\delta\},\qquad
 V_\delta=\operatorname{vol}(B_\delta)>0.
\]
Write \(g=kz\) for polar decomposition, with \(k\in K\) and \(z>0\).
If \(g\in B_\delta\), singular-value perturbation gives
\[
 \|z-1\|\le\delta,\qquad \|z\|\le1+\delta.
 \tag{1.1}
\]
For \(z\in U(J)\), \(z^{-1}=JzJ\). Thus the same norm bounds
hold for \(z^{-1}\), including
\(\|z^{-1}-1\|=\|z-1\|\). Compact conjugation preserves them.

The row embedding into the oscillator space is a direct sum of
copies of \(z\) and its conjugate, with inverses in the equivalent
swapped convention. Its operator norm is at most \(1+\delta\).
The positive complex-linear block \(C(z)\) in the harmonic
coefficient formula therefore has eigenvalues at most \(1+\delta\).
On homogeneous degree \(D\), substitution by \(C(z)^{-1}\) is a
positive operator with eigenvalues at least \((1+\delta)^{-D}\).
This can be seen in a unitary eigenbasis of \(C(z)\): every monomial
eigenvalue is a product of \(D\) inverse eigenvalues. Fischer
orthogonality is invariant under that unitary change of variables.

The vacuum determinant in that formula is a principal determinant
of dimension at most \(M\). All its eigenvalues are at most
\(1+\delta\). Hence the exact harmonic coefficient formula of
§5.1 of the noncompact chapter gives, for every \(u\in K\),
\[
 B(\Phi,\pi(u^{-1}zu)\Phi)
 \ge (1+\delta)^{-(D+M)}\|\Phi\|_F^2.
 \tag{1.2}
\]
The determinant character of the oscillator splitting contributes
one on positive elements, because their determinant is positive
and has modulus one.

Let \(\mu=\lambda+\rho\) and
\(W(z)=m_{-\mu}(z)\), with the principal-minor convention of the
supplier chapter. Each \(|\mu_i|\le\beta\). The near-identity
minor estimate in §2 of
[the Bessel-majorant chapter](lsernau-bessel-majorants.md) gives
\[
 |\log W(u^{-1}zu)|\le2r\beta\delta.
 \tag{1.3}
\]
For clarity, a negative level is expressed as a complementary
minor of the inverse, using \(\det z=1\). The total of the sizes
of the resulting minors is \(\sum_i|\mu_i|\), and the absolute
logarithm of each eigenvalue is at most \(2\delta\). This proves
(1.3) also when weights are negative.

The positive compact average, with probability measure on \(K\), is
\[
 \begin{split}
 I(g)&=\int_{K\times K}
 e_l(k_1^{-1}gk_2)
 B(\Phi,\pi(k_1^{-1}gk_2)\Phi)\,dk_1dk_2\\
 &=\frac{d_l}{\dim\tau}\int_K
 W(u^{-1}zu)^{-1}
 B(\Phi,\pi(u^{-1}zu)\Phi)\,du.
 \end{split}
 \tag{1.4}
\]
It is positive on all of \(G\), and (1.2)–(1.3) imply, on
\(B_\delta\),
\[
 I(g)\ge\frac{d_l}{\dim\tau}
 e^{-(D+M+2r\beta)\delta}\|\Phi\|_F^2
 \ge\frac{d_l}{2\dim\tau}\|\Phi\|_F^2.
 \tag{1.5}
\]
The last exponent has absolute value less than \(1/4\).

Weighted absolute integrability justifies compact averaging and
Haar invariance. Since \(P_l\) is self-adjoint and idempotent for
\(B\), we can integrate (1.4) and restrict its positive integrand
to the small ball:
\[
 \|P_l\Phi\|_B^2
 =B(\Phi,P_l\Phi)
 =\int_G I(g)\,dg
 \ge\frac{d_l V_\delta}{2\dim\tau}\|\Phi\|_F^2.
 \tag{1.6}
\]
This restriction uses the averaged integrand. No pointwise
positivity of the unaveraged integrand is being assumed.

## 2. Packing removes the formal degree and Haar scale

Put \(N=2r^2\), the real dimension of \(M_r(\mathbb C)\), and
\(G_R=\{g\in G:\|g\|\le R\}\), for \(R\ge1\).
The identity \(\|g^{-1}\|=\|g\|\) holds on \(U(J)\).

Choose a maximal \(\delta/R\)-separated set in the compact set
\(G_R\), using the ambient matrix norm. The disjoint ambient balls
of radius \(\delta/(2R)\), and the scaling law for ambient
Lebesgue measure, bound its cardinality by
\[
 \left(1+\frac{2R^2}{\delta}\right)^N
 \le\left(\frac3\delta\right)^N R^{2N}.
\]
If \(g\) is within \(\delta/R\) of a chosen point \(g_i\), then
\(\|g_i^{-1}g-1\|\le\delta\). Thus the corresponding left
translates \(g_iB_\delta\) cover \(G_R\). For the Haar measure
already used to define \(d_l\),
\[
 \operatorname{vol}(G_R)
 \le\left(\frac3\delta\right)^N R^{2N}V_\delta.
 \tag{2.1}
\]

Apply Tonelli's theorem to the decreasing majorant in (0.1):
\[
 \begin{split}
 d_l^{-1}
 &=\int_G|c_l(g)|^2\,dg\\
 &\le 2h\,2^{2h}\int_2^\infty
 R^{-2h-1}\operatorname{vol}(G_R)\,dR\\
 &\le\left(\frac3\delta\right)^N V_\delta\,
       \frac{h}{h-N}\,2^{2N}\\
 &\le2\left(\frac{12}\delta\right)^N V_\delta.
 \end{split}
 \tag{2.2}
\]
The integral converges because \(h>N\); the last inequality uses
\(h\ge2N=4r^2\). It follows that
\[
 d_l V_\delta\ge\frac12
            \left(\frac\delta{12}\right)^{2r^2}.
 \tag{2.3}
\]
Combining (1.6) and (2.3), and substituting (0.2), proves
(0.3)–(0.4). Both \(d_l^{-1}\) and \(V_\delta\) scale linearly
with Haar measure, so their ratio and the resulting bound are
unchanged by Haar normalization.

## 3. Parameter-only and product consequences

If the signature is \((p,q)\), \(p+q=r\), put
\[
 d_K=\frac{p(p-1)+q(q-1)}2.
\]
Weyl's dimension formula on the two compact blocks gives
\[
 \dim\tau\le(L+2r)^{d_K}.
 \tag{3.1}
\]
Indeed the difference of two entries of \(\lambda\) is at most
\(L\); the difference contributed by \(\rho_n-\rho_c\) is at
most \(r-1\); and the additional Weyl numerator shift is at most
\(r-1\). Each denominator is at least one. Thus the projection
ratio is bounded below by a reciprocal polynomial in \(D,M,L\)
for fixed \(r\), with completely explicit exponent.

For the constructed product of minors, the integer coefficients
and nonzero normalization give \(\|\Phi\|_F^2\ge1\). In that
normalization (0.4) therefore gives the absolute local bound
\[
 \|P_l\Phi\|_B^{-1}
 \le2(L+2r)^{d_K/2}(48T)^{r^2}.
 \tag{3.2}
\]
For independent infinite places, tensor the vectors and projections.
The squared norms and the ratios in (0.3) multiply, so the
corresponding product lower bound follows without an extra loss.

## 4. What this estimate supplies

This is a quantitative estimate for the explicit harmonic line in
the local oscillator representation. Together with the supplier
chapter it proves nonvanishing with an explicit reciprocal bound,
and the noncompact real-edge chapter supplies exact compact-support
smearing in the source Banach space.

The companion [quantitative smearing chapter](lsernau-quantitative-local-smearing.md)
controls all finite-degree polynomial inputs by integer spanning
matrices and a fixed bump, with explicit factorial losses. Its
input norm is the original Fischer norm. Neither estimate supplies
a right inverse bounded solely by the projected Hilbert norm or
a global arithmetic theta-test value. These require their own
arguments in the full chain-gauge construction. The quantitative
arithmetic return theorem is separately proved in
[the return chapter](lsernau-quantitative-returns.md).

This inequality is an ordinary consequence of the proved harmonic
coefficient, positive polar, minor-decay and packing formulas. It
uses no numerical integration or finite search. Its representation
theoretic suppliers and immutable source correspondences are
recorded in the two linked local chapters; no new Lean replay or
closure of a historical proof-map node is asserted.
