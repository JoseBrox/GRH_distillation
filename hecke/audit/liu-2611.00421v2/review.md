# Audit and extensions of Liu's joint marked-moment method

27 November 2026. Baiying Liu, [Joint marked moments and optimized zero-free half-planes for unitary Hecke L-functions, v2](https://hexagonmath.org/pdf/2611.00421v2), 101 pages. This is a separate analytic research supplier, not a premise of the active arithmetic proof of RH, Dirichlet GRH or Hecke GRH.

## 1. Assessment, scope and dependency structure

The claimed theorem is nonvanishing in the open half-plane Re(s)>B*, with B*=0.873345856106718576801..., for unitary Hecke L-functions over arbitrary number fields, and a corresponding statement for finite-dimensional continuous unitary Weil representations (norm-character poles excepted). It improves the previous claimed bound B2=(777−sqrt(1081))/852=0.87338196661320752... by about 0.00003611. It is not RH, and the optimality claim concerns a specified set of positive moment/detector inequalities, not all methods. The proof uses sextic Kummer characters, two ordinary Dirichlet polynomials and a product of marked prime polynomials; joint moment propagation, signed Poisson comparisons and a zero detector produce the new strip. Sections 6–7 optimize their length/amplitude geometry, Section 8 and Appendix A implement it in the analytic sums, and Section 9 assembles and transfers the conclusion.

**Verdict:** no irreparable mathematical error was established. This is a targeted audit, not a complete certification of the 101-page proof or of the imported papers. In particular the full global marked Poisson/packing argument and the strict inequalities for all finite stages have not been independently reproduced. The PDF was inspected through its indexed text and selected page images; no local byte hash could be obtained in this environment. Version v2 is the pinned publication identifier, not a mutable latest-version link.

The following boundary matters:
* Sections 6.1–6.2: differential equation, tangent propagation, algebraic contact and positive dual identity independently checked (see Section 2 and the exact script). The full comparison over all unequal moment lengths, Proposition 6.4 and all finite-stage Bernstein certificates are not certified by these checks.
* Appendix A.1: the elementary centered cube-free estimate is valid, including common truncation and the finite prime masks; Section 3 gives a stronger and more general proof. Appendix A.5: the random partition argument is valid with the fixed-family, polynomial-cardinality hypotheses, and can be improved as below.
* Subsection 8.2 and Appendix A.4: some local sextic Gauss-sum and reciprocity identities checked; do not infer the full multi-orientation correlation estimate from them. In particular the printed formula on p. 96 is \(\overline{\chi_I(\Delta)}^4=\chi_I(\Delta)^2\); PDF text extraction loses overbars. An apparent unbarred counterexample is not a flaw in the paper. At a shared prime, the requisite character is nontrivial and the transferred frequency vanishes modulo its local period; the zero-frequency sum vanishes. This checks only the local vanishing, not the global reciprocity factors, origins or chart measures.
* The essential remaining checks are Proposition 8.6, the hypotheses and uniform positive reserves of Propositions 8.9, 8.18 and 8.20, Appendix A.4 (both Poisson orientations, fixed-inducing rows, masks and origins), Theorem 8.21, the complete numerical stage comparisons, and the full zero-detector application in Section 9. The initial moment and detector inputs imported from the paper's references [2], [3], [5], [6] must also be checked with their actual quantifiers. In particular arbitrary fixed anchors, independent heights, moving masks, and the order of small parameters cannot be inferred merely from a finite-order theorem.
* The author's [older Lean replay description, pinned revision b1d396b513a16fa150ba1fdf119d25b590102168](https://github.com/liubaiying101/Improved-zero-free-half-planes-for-the-quasi-Riemann-hypothesis/blob/b1d396b513a16fa150ba1fdf119d25b590102168/README_on_lean.md) reports a different bound 0.874957019420098946... with formal replay. It is not verification of the new v2. No fresh Lean replay was performed. The earlier uniform bound 7/8 and B2 are inputs only if independently accepted; see also [Gao's unitary extension](https://hexagonmath.org/2611.00334v1) and [Hu's 7/8 paper](https://hexagonmath.org/2610.00216v2).

All results below are ordinary mathematical deductions with explicit hypotheses, independent of accepting the claimed v2 theorem.

## 2. Exact endpoint checks and a quantitative finite-stage theorem

Write
\[
 G(R)=\frac{11R}{16}-\frac7{24}
       -\frac5{16}(7R^4(R-2/3))^{1/5},
 \qquad 2/3<R\le 7/9,
\]
and \(a(R)=(45R-24)/(R(45R-30)),\ b(R)=(9R-7)/(R(45R-30))\).
The positive real fifth root is meant. Direct differentiation gives
\[
 G'=aG+b,\quad G(7/9)=0,\quad
 G''=\frac{7^{1/5}}{45R^{6/5}(R-2/3)^{9/5}}>0.
\]
For \(R\mapsto r<R\) put \(q=R-r,\ H=r/R,\ u=(1-H)/6\).
The necessary cutoff from Proposition 6.2 is
\[
 k\ge k_*(R,z)=\frac{5R/4-5/6}{R-1/2-z}>0.
\]
The propagated value is at most \(Y=Hz+u(1/k-2)\). Algebra gives
\(Y_*=z-q(az+b)\) at \(k=k_*\). Since \(0<qa(R)<1\) for \(r>2/3\), this affine map is increasing, and convexity gives the claimed upper envelope.

**Quantitative extension (finite-stage defect).** Fix a compact interval I inside (2/3,7/9], with \(A=\max_I a,\ 0<m=\min_I G'',\ M=\max_I G''\). Take a descending chain \(R_j\) in I, \(q_j=R_j-R_{j+1}>0\), \(Aq_j\le1/2\), and \(z_0\le G(R_0)\). Assume the necessary cutoff condition above at each stage. Write \(z_{j+1}=Y_j-d_j\) with \(d_j\ge0\), \(p_j=u_j(1/k_{*,j}-1/k_j)\ge0\), and \(e_j=G(R_j)-z_j\). With \(L=R_0-R_n\),
\[
\begin{split}
 e_{j+1}&=(1-q_ja(R_j))e_j+p_j+d_j+
       \int_{R_{j+1}}^{R_j}(t-R_{j+1})G''(t)\,dt,\\
 e^{-2AL}\left(e_0+\frac m2\sum q_j^2+\sum(p_j+d_j)\right)
 &\le e_n\le e_0+\frac M2\sum q_j^2+\sum(p_j+d_j).
\end{split}
\]
Proof: substitute the affine tangent identity and Taylor's formula with integral remainder. Iterate the exact recursion; each propagation multiplier is between 0 and 1, and its products are at least exp(−2AL) by log(1−x)≥−2x on [0,1/2]. This proves both inequalities. Thus no finite admissible strict descent attains the limiting envelope. On a fixed interval, any such n-step chain has curvature defect at least exp(−2AL)mL²/(2n). Equal mesh with ideal cutoffs and no extra losses gives the matching O(1/n) upper bound for the **relaxed** recursion. This is a quantitative obstruction and an adaptive-mesh error budget, not a proof of admissibility of ideal physical stages. The paper's other margin and support requirements remain.

For the contact, set \(\delta(r)=(45r-14)/(6+54r)\), \(B(r)=(99r-14)/(12(9r-1))\).
The root in (0.7523220538,0.7523220539) satisfies
\[
 [19(3r-2)(9r+2)/(3(45r-14))]^5=7r^4(r-2/3).
\]
Cancel the factor \(3r-2\) after clearing denominators; substitute \(r=(12B-14)/(108B-99)\) and take the primitive integer numerator. The accompanying script derives the degree-nine polynomial in the paper, verifies the rational isolating intervals by Sturm root counts, and proves irreducibility by the Rabin criterion over F_11 (gcd with X^(11^3)−X is 1, and X^(11^9)=X mod the polynomial). Exact bisection gives bracket width <10^−70 and displayed midpoint
0.8733458561067185768011847960650723567704419398439811895833474137524671.
The checks were actually run with SymPy; they are not numerical sampling of the analytic inequalities.

For the three affine necessary bounds \(L_0=5/6+M/12-\ell/6,\ L_K=1/3+7M/12+\ell/3,\ H=1+3\delta/4-(1/2+\delta/4)M+3\delta\ell/4\), the weights
\[
 \frac{25\delta+8}{6(4\delta+3)},\quad
 \frac{4-\delta}{6(4\delta+3)},\quad \frac1{4\delta+3}
\]
are positive for 0<δ<4, sum to one, and give the constant \((14+25\delta)/(18+24\delta)\). Equality of their maximum with that constant occurs precisely at
\(M=2(9\delta+2)/(3(4\delta+3)),\ \ell=(5-6\delta)/(3(4\delta+3))\).
This independently proves the exact unconstrained three-plane minimax, including rigidity. Physical feasibility requires all other comparisons; it does not follow from the dual identity.

**Sensitivity of the relaxed obstruction.** Put \(F=(1+r)/2+G(r)\).
The contact equation \(1-\delta F=(10+3\delta)/18\) is equivalent to
\(G=G_{\rm req}:=4/(9\delta(r))-2/3-r/2\).
Here δ'>0 and G_req'<−1/2; on [3/4,7/9] one has G'>−1/6 by bounding \((7r^4(r-2/3))^{1/5}\le7/9\) and its logarithmic derivative by 52/15. Thus the contact is simple. If a new moment method supplies \(G+\epsilon J\) near the contact (J continuously differentiable), the implicit function theorem gives
\[
 r'(0)=-J(r_*)/(G'(r_*)-G_{\rm req}'(r_*)),\qquad
 B'(r_*)=9/[4(9r_*-1)^2]>0.
\]
A positive envelope gain strictly lowers this particular obstruction to first order. This guides where improvements matter, without asserting that all the other constraints remain feasible.

## 3. Multivariate centered power-free estimate and a larger saving

This generalizes Lemma A.1, pp. 91–92. Fix a number field F, integers d≥1 and k≥2, and fixed unitary Hecke characters ψ_j, whose pure norm twists are absorbed into the independent heights v_j. Fix compact supports in (0,infinity) for smooth W_j and put \(V_j(x)=W_j(x)x^{iv_j}\). Zero-extend Euler coefficients at the ramified primes of each character. Define \(\mathcal R(\mathbf X)\) as the sum of \(\prod_j\psi_j(\mathfrak a_j)V_j(N\mathfrak a_j/X_j)\) over integral ideals for which \(\prod_j\mathfrak a_j\) is k-free (total valuation <k). At primes dividing an arbitrary ideal R, allow arbitrary subsets of the valuation vectors of total degree <k, identical in both arms. One may also allow fixed complex coefficients of modulus ≤1 on those vectors. At the other primes the coefficients are the original ones. Include the fixed ramified primes in the exceptional set when convenient.

Let \(\prod X_j=\prod Y_j=T,\ L=\min_j(X_j,Y_j)\ge1,\ D_0=\max_j(X_j,Y_j)\). All constants below are uniform in R and its masks; depend on F,d,k, the fixed characters, supports and the indicated parameters. Write \(\mathcal P_J=\prod_j p_J(W_j)(1+\sum|v_j|)^J\), increasing J if necessary.

**Unconditional theorem.**
\[
 |\mathcal R(\mathbf X)-\mathcal R(\mathbf Y)|
 \ll_\epsilon T L^{-(1-1/k)}(NR)^\epsilon
 (1+\log(2D_0))^C\mathcal P_J.
\]
Indeed, at a good prime put \(x_j=\psi_j(\mathfrak p)(N\mathfrak p)^{-s_j}\) and \(P_k(\mathbf x)=\sum_{|\mathbf e|<k}\mathbf x^{\mathbf e}\).
After dividing out \(\prod L(s_j,\psi_j)\) the convolution polynomial is \(P_k\prod(1-x_j)\). Every nonconstant monomial has total degree at least k, since the low-degree terms agree with the truncated inverse of \(\prod(1-x_j)\). Exceptional-prime coefficients have bounded degree and size and constant term of modulus ≤1. For the individual unrestricted sum \(F_j(Q)\), Mellin inversion and a contour at 1/k give \(F_j(Q)=m_jQ+O(\mathcal P_{j,J}Q^{1/k})\), with \(m_j=\operatorname{Res}_{s=1}L(s,\psi_j)\widehat V_j(1)\). Also \(F_j(Q)=O(p_0(W_j)Q)\) for all Q>0 by ideal counting and support. Telescope the product against \(\prod m_j Q_j\); each error is bounded by the product of Q_j times a sum of \(\min(1,Q_j^{-(1-1/k)})\). In the common convolution truncation \(D_j=N\mathfrak d_j\le C_WD_0\), the main products cancel termwise because T agrees. Bound the remaining error by \(O(TL^{-(1-1/k)}\mathcal P_J\prod D_j^{-1/k})\). The good-prime absolute local norm at this exponent is \(1+O(q^{-1})\); its product over \(q\le C_WD_0\) is logarithmic by the elementary prime harmonic estimate over F. The exceptional-prime norms are at most \(1+O(q^{-1/k})\), with finitely many small primes absorbed in the constant. Their product is \(O_\epsilon((NR)^\epsilon)\). This proves the theorem, including the case of absent principal residues.

**Stronger theorem using a prior zero-free region.** Suppose each fixed \(L(s,\psi_j^k)\) has no zeros in Re(s)>b for some \(0<b<1\), allowing its possible pole. For any \(0<\sigma<1\) with \(k\sigma>b\),
\[
 |\mathcal R(\mathbf X)-\mathcal R(\mathbf Y)|
 \ll_{\epsilon,\sigma} T L^{-(1-\sigma)}(NR)^\epsilon
 (1+\log(2D_0))^C\mathcal P_J. \tag{1}
\]
Only zero-freeness of the individual powers is required, not the new claimed v2 bound.

Proof. Factor the multiple Dirichlet series as
\[
 \prod_{j=1}^d\frac{L(s_j,\psi_j)}{L(ks_j,\psi_j^k)}
       \mathcal H_R(\mathbf s),\qquad
 H_{\mathfrak p}=P_k(\mathbf x)\prod_j\frac{1-x_j}{1-x_j^k}
\]
at good primes, with the actual allowed polynomial at exceptional primes. When only x_j is nonzero, \(H_{\mathfrak p}=1\); hence every nonconstant monomial has at least two distinct variables. In the region with one real part ≥σ and all other real parts ≥1, the good-prime factor is \(1+O(q^{-1-\sigma})\) uniformly (use the absolutely convergent local power series for large q). Thus the Euler product there is analytic in the interior, normally convergent up to these contours and bounded uniformly; exceptional-prime factors are \(O(1+q^{-\sigma})\) and yield \(O_\epsilon((NR)^\epsilon)\). This argument does not divide by a possibly vanishing local mask polynomial.

For the fixed power L-functions, their reciprocals have polynomial vertical growth on any fixed line strictly right of b. For completeness, on bounded real intervals to the right of b use a disk centered at 2+it with radius strictly below 2−b but covering the desired buffered strip. For |t| large it contains no pole or zero. Choose the log at the center by its absolutely convergent Euler series. Polynomial growth of L in vertical strips bounds the real part of this logarithm by O(log(2+|t|)). Borel–Carathéodory on a strictly smaller disk bounds the logarithm in modulus by the same order. Exponentiating gives the reciprocal polynomial bound. The remaining bounded region is compact and any norm-character pole becomes a removable zero of the reciprocal. Farther right use the Euler product directly.

Start multiple Mellin inversion on real parts \(c=1+1/\log(2D_0)\). Shift the first coordinate alone to σ, then shift the next coordinate only in the preceding residue term, and so on. The only possible crossed pole in each coordinate is the simple pole at 1 of a principal numerator. Do not shift all variables to σ together: mixed factors need not converge in that larger region. The remaining unshifted coordinates are at c and previously evaluated residues at 1. The preceding Euler and vertical bounds and rapid Mellin decay justify the shifts and bound each error with the shifted variable j by
\(O(T X_j^{-(1-\sigma)}(NR)^\epsilon(1+\log(2D_0))^C\mathcal P_J)\).
Here \(X_i^{c-1}\le e\); absolute Euler bounds on the unshifted L-factors are \(O(1+\log(2D_0))\) by the simple pole of ζ_F, and all other factors have polynomial growth with fixed exponents. Integration by parts in each compact test controls arbitrary independent heights by the displayed seminorm. The only possible full residue is a constant times T, with identical constant in both arms. Subtract. This proves (1).

Anisotropic refinement: if some ψ_j is nonprincipal, shift that coordinate first; there is no residue, and the bound on each uncentered arm is \(T X_j^{-(1-\sigma)}\) times the same factors. When several such coordinates exist, choose the longest among them. This can improve the estimate even without equal products. If there are no such coordinates the centered cancellation remains essential.

For k=3 and a separately established earlier bound 7/8, the saving can approach 17/24=0.708333... instead of 2/3. With the earlier B2 it can approach \(1-B_2/3=0.70887267779559749...\). These are strict limiting savings: choose σ strictly above b/3, and keep an explicit reserve for every later exponent comparison. No use of B* to prove B* is permitted. Constants are for fixed inducing characters; a varying family requires an additional uniformity argument.

**Preserve the saving in the fixed-inducing comparison.** Appendix A.4, p. 97, has raw value bounded by \(U^\epsilon (X/D)\max(1,L_f/D)^{-\eta}\), where D is extracted norm and \(D\ge D_{\min}=NG\,ND_2\). For \(1/2\le\eta<1\), the squared expression decreases with D both below and above L_f and is continuous at the junction. Therefore the exact envelope is
\[
 U^{O(\epsilon)}\frac{X^2}{D_{\min}^2}
       \max(1,L_f/D_{\min})^{-2\eta}.
\]
For \(D_{\min}\le L_f\) this equals the paper's relaxed bound \(U^{O(\epsilon)}X^2/(D_{\min}L_f)\) times the extra factor \((D_{\min}/L_f)^{2\eta-1}\). For \(D_{\min}>L_f\) retain \(D_{\min}^{-2}\). The original proof discards this factor even with η=2/3. Exploit it in a revised exponent budget before attempting another optimization. It is not a uniform strict gain when \(D_{\min}\) is close to \(L_f\); no new zero-free constant follows from this refinement alone.

## 4. Prime-list refinement with smaller discrepancy

Lemma A.5 uses independent random labels at each prime to realize a fixed finite tree of partitions, preserving bounded prime polynomial coefficients after restriction. The following extension allows any preassigned polynomial-size list of bounded coefficient arrays and prefixes, and improves the logarithmic loss.

For integer dyadic U, suppose the list at each scale has at most U^C tests, each supported on a norm annulus of scale P≤U^C (bounded lower scales included), each coefficient of modulus ≤1, with all arrays independent of the labels. Include all prefix tests if desired. Fix a finite tree with fixed node probabilities b; labels for different primes are independent, with child probabilities conditional on the parent. There is one labeling of all primes such that, for every sufficiently large dyadic U, every test and every node, the error in the unnormalized restriction is
\[
 O_{F,C,\mathrm{tree}}\!\left(\sqrt{\frac{P}{\log(2P)}\log U}\right).
\]
For a child with relative density b', subtract b' times the corresponding parent discrepancy; the same bound follows.

Proof: a rational prime p has at most [F:Q] primes above it; prime ideals of residue degree one and norm ≤2P are O_F(P/log(2P)) by Chebyshev, and those of higher degree are O_F(sqrt P). The latter is also O_F(P/log(2P)). Hoeffding on the real and imaginary parts of the independent centered node indicators times the coefficients gives failure probability at most \(4\exp(-cT^2/N)\) for N eligible primes. For a sufficiently large constant in T, the union over polynomially many tests and the fixed tree is O(U^−2); use summability over dyadic U and Borel–Cantelli. Zero or very small N are trivial. This proves existence of a single labeling, not just separate labels at each scale. Norm weights p^(-1/2) cost P^(-1/2) by partial summation; the compact smooth test costs its sup norm and first variation. Norm twists of polynomial height can be treated by a polynomial mesh in height: derivative of the unnormalized test in height is O(N log(2P)) if the phase is log Np, so sufficiently fine polynomial mesh controls the residual; using log(Np/P) instead only helps. A finite set of anchors and a polynomial conductor/mask range admit polynomially many discrete tests by ideal and ray class counting. Thus the normalized error is \(O(\sqrt{\log U/\log(2P)})\), in particular O(1) when P is a fixed positive power of U. This is a logarithmic improvement, not a new moment exponent. Arbitrary label-dependent arrays or unrestricted moving infinity types are not covered. The original paper's fixed tree and fixed coefficient families satisfy the required independence; their exact physical uses still need the full audit.

## 5. Twisted Heilbronn transfer with multiplicity control

The active project already has rank-one Galois descent by positive Aramata–Brauer induction in [galois-base-change.md](../../notes/galois-base-change.md). The following stronger standard Heilbronn mechanism, written for a fixed arbitrary unitary Hecke twist, is a useful independent supplement to Section 9 of Liu. It does not assume Artin holomorphy.

Let E/K be finite Galois with group G, χ a unitary Hecke character of K, and s0 in the open strip 0<Re(s0)<1. For each irreducible complex character ρ of G define \(n_\rho=\operatorname{ord}_{s_0} L_K(s,\chi\otimes\rho)\) (negative for poles). Meromorphic continuation follows by Brauer induction, class field theory, and the classical Hecke functions of norm-pulled-back χ times the finite cyclic characters; the usual local induction identity includes the ramified Euler factors, or remove all finitely many bad factors, which have no singularities or zeros in Re(s)>0 by unitarity. Define the virtual character \(\Theta=\sum n_\rho\rho\). For every cyclic C≤G and λ in its dual, Frobenius reciprocity and induction of Euler factors give
\[
 \langle\Theta|_C,\lambda\rangle
 =\operatorname{ord}_{s_0}L_{E^C}(s,\chi_{E^C}\lambda)\ge0.
\]
Indeed the possible norm-character pole has real part 1, outside the strip. Consequently each restriction is an actual character; \(|\Theta(g)|\le\Theta(1)\) follows by taking C=<g>. The regular representation yields \(\Theta(1)=\operatorname{ord}_{s_0}L_E(s,\chi_E)=m\ge0\). Orthogonality now gives the stronger simultaneous inequality
\[
 \sum_\rho |n_\rho|^2=|G|^{-1}\sum_{g\in G}|\Theta(g)|^2\le m^2.
\]
In particular a nonzero norm-pulled-back rank-one L-function forces every finite-image twist to be holomorphic and nonzero there, and an individual order is bounded in absolute value by m. No hypothesis about the signs of individual Artin orders is needed. This is an extension of the existing project's rank-one descent interface, not a proof for all infinite-image Weil representations or a stronger zero-free strip. On Re(s)=1 one must handle possible poles separately; no such boundary assertion is made.

## 6. Local sextic identity and normalization

For a good residue field of cardinality q, an order-six character χ and a nontrivial additive character ψ, put \(g_j=q^{-1/2}\sum_{x\ne0}\chi^j(x)\psi(x)\). Write \(A=-g_2^3,\ C=\overline A g_2=-\overline{g_2}^{\,2},\ G=\overline{\chi(4)}g_3\) (the field has odd characteristic, and the good-prime assumptions exclude characteristic 3). The standard quadratic Hasse–Davenport duplication gives \(g_1 g_4=\overline{\chi(4)}g_2g_3\). Since \(g_4=\overline{g_2}\) and \(|g_j|=1\) for j=1,...,5, it follows that \(g_1=Gg_2^2\). Together with \(g_5=\chi(-1)\overline{g_1}\) this proves \(g_1g_2=Gg_2^3,\ -g_1\overline G=\overline C,\ -g_5G=\chi(-1)C\). In the frequency-scaling formula \(\overline{\chi(\Delta)}^4=\chi(\Delta)^2\) is exact, because the order divides six. In general \(\overline{\chi(\Delta)}^{m-2}=\chi(\Delta)^2\) for order dividing m and Δ a unit. At nonunit Δ the scaling formula with inverse is not used; test the character sums directly. These are local identities, not a replacement for the global Poisson proof.

## 7. Integration and remaining research

The active Hecke manuscript's prime-deficit criterion, selected-twist arithmetic, theta and determinant budget remain unchanged. The new results are independent useful analytic tools: Section 3 for centered sums with common finite masks, Section 2 for designing finite stages and finding the sensitivity of the comparison, Section 4 for disjoint marked refinements, Section 5 for transferring nonvanishing and controlling Artin orders. No claim is made that the project's arithmetic theta sums already meet the hypotheses of Section 3 or that Liu's moment method closes the prime-deficit criterion at 1/2.

Priority within this alternative: (i) audit the exact initial sources and two global signed Poisson orientations, their fixed-inducing exclusions, uniform height dependence and origins; (ii) reproduce all finite comparison certificates and the detector with strict reserves; (iii) incorporate the full extraction-dependent saving of Section 3 and recompute the optimization, checking whether an actual positive gap survives the worst fibers; (iv) establish a new moment or genuinely better signed numerator/inverse estimate if the current positive obstruction survives. The present work has not lowered B* and has not certified v2. No legacy proof-map node is closed.
