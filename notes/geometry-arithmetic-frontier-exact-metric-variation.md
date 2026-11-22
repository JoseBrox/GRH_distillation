# Exact arithmetic metric variation

## Result and scope

The original intersection axioms give the exact metric-change identity,
with positive sign and coefficient one in a single slot. Telescoping gives
the factor \(n+1\) multiplying unnormalized energy. There is no additional
factor \(1/2\). The half in the final cusp comparison comes from the
original corrected potential \(\psi-\varphi=U/2\).

A short argument also proves the source's metric-locality statement from
the same axioms. Consequently a smooth representative agreeing on the
original complex variety gives the same intersection number. This removes
the separate locality supplier from the source's metric-change proof.

The statements here concern the original arithmetic functional and its
original mixed archimedean integrals. Their identification with integrals
on the specified compact complex model is retained explicitly. This
checkpoint does not construct that model or complete the signed boundary
comparison. RH remains \(6/9\); GRH remains \(17/31\).

## 1. Setting and the sign of a trivial metric

Let \(P\) define the original arithmetic variety of dimension \(n+1\).
Its homogeneous coordinates have finitely many blocks. Write
\(\mathcal C\) for the open set on which every block is nonzero and
\(X(\mathbb C)\subset\mathcal C\) for the original complex points.
A Hermitian line is specified by an integral multidegree and a positive
smooth function \(h\) on \(\mathcal C\) with the prescribed homogeneity.
The source's section norm is
\[
                         \|s(z)\|=\frac{|s(z)|}{h(z)}.
 \tag{1}
\]
Its auxiliary values outside \(\mathcal C\) need not be positive.

Write \(I_P(L_0,\ldots,L_n)\) for an intersection family satisfying the
original symmetry, tensor additivity and divisor recursion. The recursion
has finite-divisor contributions **minus**
\[
 \mathcal J_P(\log h_1,\ldots,\log h_n;\log\|s\|).
 \tag{2}
\]
Here \(\mathcal J_P\) is exactly the original mixed archimedean integral,
including its full sheet sum and original normalization.

Let \(\delta\) be a smooth degree-zero function on \(\mathcal C\),
extended by zero off \(\mathcal C\), and let \(R_\delta\) be the
degree-zero line with metric denominator \(e^\delta\).
The section \(1\) has no divisor, and
\(\log\|1\|_{R_\delta}=-\delta\). Thus the original recursion gives
\[
 I_P(L_1,\ldots,L_n,R_\delta)
           =\mathcal J_P(\log h_1,\ldots,\log h_n;\delta).
 \tag{3}
\]
The empty divisor and the minus sign are both essential. The statement
also holds when \(n=0\), with the original zero-dimensional integral.

## 2. A short locality argument

First suppose two same-degree smooth metrics \(A,B\) agree on all of
\(\mathcal C\). Consider the auxiliary smooth Hermitian line
\[
 h_C(z)=\prod_k\left(\sum_i|z_{ki}|^2\right)^{1/2},
                \qquad \deg C=(1,\ldots,1).
 \tag{4}
\]
It is positive and smooth on \(\mathcal C\), and zero outside
\(\mathcal C\). Therefore \(A\otimes C=B\otimes C\) as the complete
homogeneous data, including their otherwise irrelevant values off
\(\mathcal C\). Tensor additivity and cancellation give
\[
                    I_P(L_1,\ldots,L_n,A)
                   =I_P(L_1,\ldots,L_n,B).
 \tag{5}
\]
No assertion that the ratio metric agrees with \(B/A\) off the cone is
needed. Such an assertion would in general be false.

For arbitrary same-degree smooth \(A,B\), put
\(\delta=\log h_B-\log h_A\) on \(\mathcal C\), and zero outside.
The equal multidegrees make this function invariant under every nonzero
block scaling. The line \(A\otimes R_\delta\) agrees with \(B\) on
\(\mathcal C\). Combining (3)--(5) yields
\[
 \begin{split}
 I_P(L_1,\ldots,L_n,B)-I_P(L_1,\ldots,L_n,A)
   =\mathcal J_P(\log h_1,\ldots,\log h_n;\delta).
 \end{split}
 \tag{6}
\]

Now suppose \(A,B\) agree only on \(X(\mathbb C)\). Then \(\delta\)
vanishes at every sheet point in the defining integral, so the right
side of (6) is zero. Replacing one factor at a time proves full locality
on \(X(\mathbb C)\). For zero factors the assertion is tautological.
In particular, the original smooth representatives and conjugation
invariant smooth representatives do not change intersections whenever
they have the required smoothness and the same degree.

## 3. Top intersections and the energy factor

Apply (6) to successive words with \(j\) factors \(B\) and the remaining
factors \(A\). Symmetry and telescoping give
\[
 I_P(B^{n+1})-I_P(A^{n+1})
  =\sum_{j=0}^n
      \mathcal J_P((\log h_B)^{[j]},
                   (\log h_A)^{[n-j]};\,\log h_B-\log h_A).
 \tag{7}
\]
Bracketed exponents indicate repeated arguments, not powers.
This is an exact identity for the original source functional. It needs
only the three original intersection axioms; the additional projection
and field-contraction axioms of the full family are not used.

On a smooth compact complex realization with the original integral
dictionary, let \(h_A=h_0e^\varphi\), \(h_B=h_0e^\psi\),
\(\theta=dd^c\log h_0\), and
\[
                         dd^c=\frac{i}{\pi}\partial\bar\partial .
 \tag{8}
\]
If the mixed integrals in (7) are the Chern-form integrals with all
original component weights, then
\[
 I_P(B^{n+1})-I_P(A^{n+1})
              =(n+1)\bigl(E_\theta(\psi)-E_\theta(\varphi)\bigr).
 \tag{9}
\]
For several complex components the right side is the original weighted
sum of these unnormalized energies. Equation (9) uses the standard mixed
energy difference, with its factor \(1/(n+1)\). For smooth potentials
that formula follows by integration by parts; the finite-energy extension
is covered by the separately reviewed signed-boundary checkpoint.

The local density fixes (8) without an implicit factor:
\[
 \mathcal J_P \text{ uses }
 n!\left(\frac2\pi\right)^n
       D(H_1,\ldots,H_n)\,dV,\qquad
 H_j=(\partial_{z_r}\partial_{\bar z_s}\varphi_j)_{rs},
 \tag{10}
\]
where \(D\) is the mixed discriminant normalized by \(D(H,\ldots,H)=\det H\).
This is precisely the density of
\(dd^c\varphi_1\wedge\cdots\wedge dd^c\varphi_n\).
It preserves the source's counting of complex sheets; no division by two
or change of complex-place weights has been inserted.

## 4. Original vertical factors and rational twists

Fix the original finite cutoff and write \(V\) for the product of its
positive vertical metric factors. On the original complex variety the
unbounded regularization has denominator
\[
             h_t=h_{\mathrm{ref}}e^{\varphi_t}V .
 \tag{11}
\]
Its actual smooth representative is the source's \(\mu_t\).
The pinned source proves the pointwise formula for the rationally
twisted line \(N_{p,q,t}\), for integers \(p\geq0\) and \(q\geq1\):
\[
              h_{N_{p,q,t}}=h_t^q h_{A'}^p,\qquad
              \deg N_{p,q,t}=q\deg\mu_t+p\deg A'.
 \tag{12}
\]
The positivity and homogeneity of the original factors are retained;
they are not replaced by a new choice of metric. At smooth scales,
locality just proved identifies the original representative with
\(\mu_t^{\otimes q}\otimes(A')^{\otimes p}\) for intersections.
Hence the source's normalized intersection is exactly
\[
 \begin{split}
 \frac{I_P(N_{p,q,t}^{n+1})}{q^{n+1}}
    &=P_t(p/q),\\
 P_t(z)&=\sum_{j=0}^{n+1}\binom{n+1}{j}z^j
                I_P(\mu_t^{[n+1-j]},(A')^{[j]}).
 \end{split}
 \tag{13}
\]
In particular \(P_t(0)\) is exactly the original function defining the
arithmetic limit. Thus the algebraic rational-twist normalization and
the constant-coefficient identification are established. Convergence
still needs the analytic comparison; polynomial interpolation alone
does not supply the values to which it is applied.

For the source's bounded corrected line, the tied reference metric is
the same and its denominator on the variety is
\[
       h_{M_{p,q,t'}}=
           (h_{\mathrm{ref}}e^{\psi_{t'}}V)^q h_{A'}^p.
 \tag{14}
\]
Therefore
\[
       q^{-1}\log\frac{h_{M_{p,q,t'}}}{h_{N_{p,q,t}}}
                           =\psi_{t'}-\varphi_t .
 \tag{15}
\]
The common vertical factors and the ample twist cancel in this ratio.
Each of the \(n\) mixed curvature factors contributes \(q\), and the
logarithmic ratio contributes another \(q\); these cancel exactly the
source's denominator \(q^{n+1}\).

At the limit, the original corrected potential is
\(\psi-\varphi=U/2\). With the still required compact-model dictionary,
concavity consequently gives the coefficient
\((n+1)\int U\,T^n/2\), not a quarter of this quantity.
Cancellation in (15) does **not** prove that the common vertical metric
has zero curvature. Its curvature identification remains part of the
geometric dictionary needed to recover the original measure \(T^n\).

## 5. Source dictionary and remaining interface

All source references below are pinned to
jsmorph/rh revision ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.
The certificate records full hashes and the bounded excerpts.

| Source declaration | Verified role |
|---|---|
| IsIntersectionFamily, 88--109, 147--151, 180--198 | Homogeneous metric, tensor product, norm convention, recursion and its sign |
| ArithmeticHilbertSamuelLowerBound, 86--91; InterNamed, 37--38 | The actual full intersection system includes the family used here |
| InterDerived, 11--47 | Empty divisor of \(1\), degree-zero section, exact negative-potential convention |
| ThmISt, 80--96 | Original metric-change and full metric-locality contracts |
| IntersectionNumberMetricChange, 30--98, 184--206 | Source ratio and telescope; its separate locality assumption is eliminated above |
| IsSemipositiveOn, 206--219; IsIntersectionFamily, 116--145 | Complex Hessian, mixed density, full sheet integral |
| InterRes, 60--78 | Explicit compact-resolution integral comparison contract, still needed for (9) |
| Weights, 95--112, 149--162 | Smooth representatives and the original arithmetic-limit function |
| PMuRegSmooth, 106--157; StokesLimitStatementHolds, 194--259 | Original restricted metric and exact rational-twist logarithm |
| StatementsStokesGeo, 23--39 | Original \(q^{-(n+1)}\) top normalization |
| CpRegPhRegOfNonneg, 35--61, 71--87 | Conjugation invariant representatives, corrected potential \(U/2\), original bounded metric |

The local density calculation settles the differential normalization.
The global identification of the original sheet integral with the
specified compact model's mixed Chern integral, including the common
vertical curvature and component weights, is still required. The
original geometric and regularization data also remain supplied
hypotheses rather than constructions in this checkpoint.

For the compact-model energy identity, the primary reference is
R. J. Berman, S. Boucksom, V. Guedj and A. Zeriahi,
*A variational approach to complex Monge--Ampère equations*,
Publications Mathématiques de l'IHÉS **117** (2013), 179--245,
Proposition 2.1, p. 193. The published PDF and its hash are recorded
in the certificate. Its normalized energy is multiplied by the
original volume to obtain the unnormalized functional used here.

The reproducible checker authenticates the source and checks independent
exact exterior-algebra densities, symbolic telescoping and rational
normalizations. These supplement the general proof; they are not a
Lean build or a numerical proof of the infinite-dimensional comparison.
