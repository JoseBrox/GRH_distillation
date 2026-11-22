# The signed boundary comparison through finite energy

## Result and present scope

The source's logarithmic growth condition gives a direct finite-energy
proof. Its specified approximations also converge in energy after any
positive Kähler correction. Polynomial interpolation then recovers the
original signed analytic energy. None of these conclusions requires the
original Hodge class to be Kähler. These are analytic substeps under the
actual regularization data, without constructing those data.

The complete signed arithmetic comparison is **not yet claimed** here.
Section 4 states the exact remaining comparison with the original
arithmetic intersection and its bounded cusp correction. The finite-energy
argument below is proved; the final application still needs that interface
check. No whole RH or GRH node is completed.

## 1. A logarithmic barrier has finite energy

Let \(X\) be a compact Kähler manifold of complex dimension \(n\), with
Kähler form \(\omega\), and let \(D\) be a normal-crossing divisor.
Let \(r\geq1\) be smooth on \(X\setminus D\), with local expressions
\[
 r=O(1)+\sum_{i=1}^{a}\log |z_i|^{-2}
 \qquad(D=\{z_1\cdots z_a=0\}).
\]
Suppose \(u\) is \(\omega\)-plurisubharmonic, bounded above, and
\[
                    u\geq-C\log r-C .
 \tag{1}
\]
Then \(u\) has finite Monge--Ampère energy and full Monge--Ampère mass.

Here finite energy uses the unnormalized functional
\[
 E_\omega(v)=\frac1{n+1}\sum_{k=0}^n
       \int_Xv\,(\omega+dd^cv)^k\wedge\omega^{n-k}.
 \tag{2}
\]
For unbounded potentials it is extended by decreasing bounded
approximations. Finite energy means \(E_\omega(u)>-\infty\).
We use the non-pluripolar products in the unbounded case.

**Proof.** Choose a smooth Hermitian metric on \(\mathcal O(D)\), and
write \(\rho=\log\|s_D\|^2\). Multiplying its norm by a constant makes
\(\rho\leq-A<0\). On the complement of \(D\),
\[
 dd^c\rho=-\eta,\qquad
 \psi=-b\log(-\rho)-c,\qquad
 dd^c\psi=-\frac b{-\rho}\eta+
                  \frac b{\rho^2}d\rho\wedge d^c\rho ,
 \tag{3}
\]
where \(\eta\) is a smooth closed real form. On a finite collection of
relatively compact normal-crossing charts,
\(-\rho=r+O(1)\). Since \(r\geq1\), increasing \(A\) gives
\[
                  \log(-\rho)=\log r+O(1).
 \tag{4}
\]
Choose \(b\geq C\), then \(c\) so that \(\psi\leq u\). Choose the norm
shift \(A\) large enough that
\(\omega-(b/(-\rho))\eta\geq\omega/2\). Thus \(\psi\) is
\(\omega\)-plurisubharmonic after extension across \(D\).

For the energy check, smoothly truncate \(h(s)=-b\log(-s)-c\)
from below. Explicitly, take a smooth convex function \(\chi\) equal
to \(0\) on \((-\infty,-1]\) and to the identity on \([1,\infty)\),
with \(0\leq\chi'\leq1\), and set
\[
 h_j(s)=-j+\chi(h(s)+j),\qquad \psi_j=h_j(\rho).
\]
After an innocuous common constant shift, \(\psi_j\leq0\).
The \(\psi_j\) are smooth on \(X\), decrease to \(\psi\), and
\[
 0\leq h_j'\leq\frac b{-\rho},\qquad h_j''\geq0,\qquad
 T_j:=\omega+dd^c\psi_j
       =\omega-h_j'\eta+h_j''d\rho\wedge d^c\rho\geq0 .
 \tag{5}
\]
The smooth forms \(B_j=\omega-h_j'\eta\) are uniformly bounded
between positive multiples of \(\omega\). The singular term in (5)
has rank one. Consequently
\[
 d\psi_j\wedge d^c\psi_j\wedge T_j^{k-1}
    =(h_j')^2d\rho\wedge d^c\rho\wedge B_j^{k-1}.
 \tag{6}
\]
The required uniform bound is therefore reduced to
\[
 \int_{X\setminus D}
        \frac{d\rho\wedge d^c\rho\wedge\omega^{n-1}}{\rho^2}<\infty .
 \tag{7}
\]
To check it at a crossing, put \(s_i=-\log|z_i|^2\).
The numerator is bounded by a constant times
\(1+\sum_i|z_i|^{-2}\) against smooth volume. For its \(i\)-th
singular term, radial integration is bounded by
\[
 \int\frac{ds_i}{(A+\sum_\nu s_\nu)^2}
       \prod_{\nu\ne i}e^{-s_\nu}\,ds_\nu .
 \tag{8}
\]
Integrating first in \(s_i\) proves finiteness. Also
\(\int_X|\psi|\omega^n<\infty\).

On the compact manifold, integration by parts gives
\[
 \begin{split}
 \int_X(-\psi_j)T_j^k\wedge\omega^{n-k}
 &=\int_X(-\psi_j)T_j^{k-1}\wedge\omega^{n-k+1}\\
 &\quad+\int_Xd\psi_j\wedge d^c\psi_j
                     \wedge T_j^{k-1}\wedge\omega^{n-k}.
 \end{split}
 \tag{9}
\]
Equations (6)--(8), followed by induction on \(k\), uniformly bound
all terms in (2). Hence \(E_\omega(\psi)>-\infty\). Monotonicity
gives \(E_\omega(u)\geq E_\omega(\psi)>-\infty\); finite energy gives
full mass. The precise external facts are BEGZ, Propositions 2.10,
2.11 and 2.14(i), and BBGZ, Proposition 2.4 and Proposition 2.8.
These are cited results, not consequences of the source's terminology.
If \(D\) is empty or \(n=0\), the assertion follows from boundedness.
\(\square\)

## 2. Recovering the original nef class

Let \(\theta\) be a smooth closed real \((1,1)\)-form and let
\(T=\theta+dd^c\varphi\geq0\), with \(\varphi\) smooth off \(D\)
and satisfying (1). Suppose smooth \(\varphi_t\) satisfy:

1. \(\varphi\leq\varphi_t\leq C_0\) for sufficiently small \(t>0\);
2. \(\varphi_t\to\varphi\) locally in \(C^2\) on \(X\setminus D\);
3. for every \(\varepsilon>0\),
   \(\theta+dd^c\varphi_t+\varepsilon\omega\geq0\) eventually.

The last condition implies that \(\alpha=[\theta]\) is nef. It does
not make \(\theta\) itself positive.

Choose \(B>0\) with \(\theta+B\omega\) Kähler. Section 1 applied to
this form proves finite energy and full mass for \(T+B\omega\).
Set
\[
 a_k=\int_{X\setminus D}T^k\wedge\omega^{n-k},\qquad
 c_k=\int_X\theta^k\wedge\omega^{n-k}.
\]
The approximations in (2)--(3) and Fatou's lemma, applied first with
fixed \(\varepsilon>0\), give
\[
 \int_{X\setminus D}(T+\varepsilon\omega)^k\wedge\omega^{n-k}
       \leq\int_X(\theta+\varepsilon\omega)^k\wedge\omega^{n-k}.
\]
Letting \(\varepsilon\downarrow0\) yields \(a_k\leq c_k\). The
full mass just proved gives
\[
 \sum_{k=0}^n\binom nkB^{n-k}a_k
   =\int_X(\theta+B\omega)^n
   =\sum_{k=0}^n\binom nkB^{n-k}c_k.
 \tag{10}
\]
All deficits \(c_k-a_k\) are nonnegative, so each is zero. In
particular the original measure has its full cohomological mass,
\[
                         \int_{X\setminus D}T^n=\int_X\theta^n.
 \tag{11}
\]
Moreover finite energy in the corrected class gives
\(\int_X|\varphi|(T+B\omega)^n<\infty\). Expanding this positive
measure shows that \(|\varphi|\) is integrable against every
\(T^k\wedge\omega^{n-k}\). If \(U/2=\psi-\varphi\) with \(\psi\)
bounded, the same holds for \(|U|\). These assertions preserve signs
in the eventual arithmetic comparison.

Here \(C^2\) convergence is essential to the stated Fatou proof.
It has not been replaced by mere \(L^1\) convergence.

## 3. The actual approximations converge in corrected energy

Fix \(\varepsilon>0\). Choose \(t_0\) for which
\(\theta+dd^c\varphi_{t_0}+(\varepsilon/2)\omega\geq0\).
Then
\[
          \omega_\varepsilon
           =\theta+dd^c\varphi_{t_0}+\varepsilon\omega
\]
is Kähler. Put \(u=\varphi-\varphi_{t_0}\) and
\(u_t=\varphi_t-\varphi_{t_0}\). For sufficiently small \(t\), these
are \(\omega_\varepsilon\)-plurisubharmonic; \(u\) has finite energy
by Section 1. Bounds (1) and hypothesis 1 imply \(L^1\) convergence
by dominated convergence, while \(u_t\geq u\). Monotonicity and
upper semicontinuity of energy therefore give
\[
 E_{\omega_\varepsilon}(u)
 \leq\liminf_{t\to0}E_{\omega_\varepsilon}(u_t)
 \leq\limsup_{t\to0}E_{\omega_\varepsilon}(u_t)
 \leq E_{\omega_\varepsilon}(u).
 \tag{12}
\]
No monotonicity of the original parameter \(t\) is required.

There is also a direct way to recover the original *signed analytic
energy*. For all sufficiently large fixed \(B\), the form
\(\theta+B\omega\) is Kähler, and the same proof gives convergence of
\[
 Q_t(B)=\frac1{n+1}\sum_{k=0}^n
   \int_X\varphi_t\,
       (\theta+dd^c\varphi_t+B\omega)^k
                           \wedge(\theta+B\omega)^{n-k}.
 \tag{13}
\]
Both \(Q_t\) and its limit \(Q\) are polynomials in \(B\) of degree
at most \(n\). The limit polynomial is defined by replacing
\(\varphi_t\) by \(\varphi\) and integrating off \(D\). All its
coefficients are absolutely integrable: Section 2 controls
\(|\varphi|T^k\wedge\omega^{n-k}\), and the remaining smooth
\(\theta\)-factors are bounded by fixed multiples of \(\omega\).
Evaluate at \(n+1\) distinct sufficiently large values of \(B\).
Vandermonde inversion proves coefficientwise convergence, in
particular \(Q_t(0)\to Q(0)\). Thus the correction is removed from
the original signed analytic energy; no assertion of
semipositivity for the uncorrected approximants is used.

This applies to the source's Hodge regularization under its stated
geometric data. Use the upper-semicontinuous extension from
\(X\setminus D\); arbitrary prescribed values on \(D\) do not enter
the source's off-divisor truncation, these integrals, or this
extension:

| Exact source | Content used |
|---|---|
| Regularisation.Statements, 92--119 | Normal-crossing charts, \(r\), upper bound and logarithmic lower bound |
| FrameDefinitions.Weights, 39--55 | Original weight is \(\varphi\) relative to the specified smooth reference |
| RegularizedWeightPshAndBounds, 137--179 | Smooth approximations from above, a uniform upper bound, and every positive curvature correction |
| RegularizedWeightTendstoC2, 426--430 | Local \(C^2\) convergence off the divisor |

The first two are supplied geometric structures; the latter two are
authenticated source proofs. Constructing the original model and
identifying its actual metric with these structures remains necessary.

## 4. Exact next interface for the signed arithmetic limit

For two finite-energy potentials in the corrected Kähler class
\([\theta+z\omega]\), with \(z>0\), let \(E_z\) denote its
unnormalized energy. Concavity gives the proved comparison
\[
              E_z(\psi)-E_z(\varphi)
                 \leq\int_X(\psi-\varphi)
                               (\theta+z\omega+dd^c\varphi)^n .
 \tag{14}
\]
It follows first for bounded potentials from the variation formula
and integration by parts, then for finite-energy potentials by their
canonical truncations. BBGZ, Proposition 2.1, Proposition 2.4 and
Lemma 2.7 provide the corresponding energy and mixed-integrability
statements. The source defines the relevant correction exactly as
\(\psi-\varphi=U/2\), not \(U\).

To turn (14) into the source's signed limit, verify the following
identifications with its original intersection family:

1. Changing the archimedean potential changes the top arithmetic
   intersection by \((n+1)\) times the unnormalized energy difference,
   with the original complex-place weights, vertical factors, and
   \(dd^c\) convention.
2. The original bounded cusp approximations have the same corrected
   energy limit as \(\psi\). Their data explicitly give bounded
   plurisubharmonic local weights; their gluing and the specific
   normalization still need the complete source comparison here.
3. The smooth rationally twisted intersections are the polynomials
   obtained from the original multilinear intersection system.

There is a short way to remove the Kähler correction once these are
checked. If
\[
 P_t(z)=\widehat{\deg}((\overline L_t+z\overline A)^{n+1})
\]
has degree at most \(n+1\), convergence at \(n+2\) fixed positive
rational values of \(z\) forces convergence of every coefficient by
invertibility of a Vandermonde matrix. Thus its constant coefficient
has exactly the original limit at \(z=0\). This avoids assuming that
the original class is Kähler or silently changing the limiting
arithmetic height.

Equations (10)--(11) identify the geometric degree with the original
analytic mass. Section 2 also makes
\(\int U(T+z\omega)^n\) a polynomial with finite coefficients.
Consequently the original regularized lower bounds and (14), if
identified by items 1--3, yield
\[
 \operatorname{arLim}\geq
       (n+1)\left(a\,\operatorname{degMu}
                 -\frac12\int U\,T^n\right)
   =(n+1)\left(a-\frac{\operatorname{meanU}}2\right)
                    \operatorname{degMu}.
 \tag{15}
\]
This is precisely StokesLimitBound, lines 57--58 and 76--85.
The original definitions are Weights, 140--162, and
CpRegPhRegOfNonneg, 71--87. The present checkpoint proves the
logarithmic barrier, full-mass transfer, corrected-energy convergence,
recovery of the signed analytic energy, and the conditional assembly,
but does **not** mark items 1--3 as
verified for the source's arithmetic intersection.

## Primary references and verification

- S. Boucksom, P. Eyssidieux, V. Guedj and A. Zeriahi,
  *Monge--Ampère equations in big cohomology classes*,
  Acta Mathematica **205** (2010), 199--262,
  [author's published PDF](https://www.math.univ-toulouse.fr/~guedj/fichierspdf/BEGZ10.pdf),
  Propositions 2.10--2.11, pp. 228--229, and 2.14(i), p. 231.
- R. J. Berman, S. Boucksom, V. Guedj and A. Zeriahi,
  *A variational approach to complex Monge--Ampère equations*,
  Publications Mathématiques de l'IHÉS **117** (2013), 179--245,
  [published PDF](https://www.numdam.org/item/10.1007/s10240-012-0046-6.pdf),
  Proposition 2.1, p. 193; Proposition 2.4, p. 195;
  Lemma 2.7 and Proposition 2.8, p. 196.

The source certificate records the pinned Lean revision, exact excerpt
hashes, downloaded primary-source hashes, and the unresolved interfaces.
These are classical mathematical arguments and source checks, not a
Lean build or a completed arithmetic model construction.
