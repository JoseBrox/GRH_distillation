# Averaged arithmetic errors and exact finite Fourier reduction

## Current use

The signed identities and conditional comparisons below remain valid.
The preferred RH route is now [direct thick/thin transfer](rh-direct-transfer.md),
which needs no pooled symmetry. The
[fixed-quotient extension](positive-kernel-transfer.md) also applies to the
general Dirichlet program. The [source obstruction](rh-weight-symmetry.md)
shows that the unchanged sparse-top family cannot meet the exact symmetry
used in Sections 6--7; those sections are alternatives for different data.
The quantitative transport criterion is preserved separately, with the
same obstruction and its limits stated explicitly.

## Status and scope

This checkpoint strengthens the finite averaging target of [one-construction-target.md](one-construction-target.md), and the manuscript propositions `cs-finite-average` and `cs-weighted-lower`. The finite Fourier statements below are proved in ordinary mathematics. They do not construct the integral maps, theta identities or covolume comparisons still required by the arithmetic program, and they are not a new Lean build.

The first structural conclusion is an obstruction: **the existing character projection always has total coefficient zero**. Consequently neither a clever top set nor algebraic cancellation between finitely many such hosts can turn it into a nonzero combination having only nonnegative character coefficients. A positive zeta coefficient is sufficient for the analytic RH endpoint once the whole positive combination has the required bound, but the current arithmetic projection must still pay for a signed companion, or be replaced by a genuinely different arithmetic identity.

The second conclusion is constructive at the finite-group level: a fixed quotient, with exactly balanced fibres, keeps the Fourier coefficients and the number of surviving characters independent of the ambient group size. Actual primitive Dirichlet characters must also be identified across hosts; fixed abstract labels alone do not fix an analytic combination.

## 1. Normalization and the exact signed budget

Retain the data of `cs-finite-average`: a finite abelian group A; a subgroup B; nonempty T contained in A and S contained in B; an integer m at least one; positive b, a_t and weights w_{u,i}(rho). Write

\[
 G=(\mathbb Z/2\mathbb Z)^2\times A,\quad
 \Phi=\{((0,e),a)\},\quad f=2|A|,\quad
 X=B^\perp,\quad d=|S|/|A|,
 \quad k=|T|mbd/2>0.
\]

The embedding of B is u mapped to ((0,0),u). Put c=((1,1),0), t_0=((0,0),t), e_1(t)=((1,0),t), and y_t=a_t/b. Let

\[
 Q=\frac1{|T|}\sum_{t\in T}\Re\sum_{\psi\in X}
            \psi(e_1(t))Z_\psi(y_t).
\]

For rho=c+g+t_0, define

\[
 D_{u,t,i,\psi}(\rho)=
 w_{u,i}(\rho)Z_\psi(a_t/w_{u,i}(\rho))
 -\mathbf1_{\Phi_{S,u}}(\rho)bZ_\psi(y_t),
\]

and retain its **signed real transfer sum**

\[
 \mathcal T=\Re\frac1{|B|f}
  \sum_{u,t,i}\sum_{g\notin\Phi}\sum_{\psi\in\widehat G}
       \psi(-g)D_{u,t,i,\psi}(c+g+t_0).
\]

The exact arithmetic balance and orthogonality give

\[
 \boxed{\ \overline E=kQ+\mathcal T.\ }                 \tag{1}
\]

For any desired positive character combination H, put \(\mathcal F=H-Q\). Then the exact identity is

\[
 \boxed{\ H=\mathcal F+(\overline E-\mathcal T)/k.\ }    \tag{2}
\]

Thus an upper bound for the **combined** signed expression suffices. The earlier nonnegative bounds R_F and R_T are convenient majorants for \(\mathcal F\) and \(-\mathcal T\); separate absolute values are not logically required. Equation (2) alone is not an arithmetic estimate: its usefulness depends on proving bounds for these same data, before replacing summands by absolute values.

The signs and factor k follow directly from the manuscript proof: on the thick set g=e_1(s+u-t), averaging over B leaves only X, and summing over S contributes |S|/f=d/2. The source identities are `ChBalance.lean:200–202`, `FirstPrimeNeSecondPrime.lean:75–96`, and `ChCore.lean:56–73,90–104,140–152`; the companion certificate pins their bytes and bounded ranges.

## 2. The unavoidable signed coefficient

Let Q_0=A/B, and write a character of X as

\[
 \psi_{\sigma,\tau,\theta}((e_1,e_2),a)
    =(-1)^{\sigma e_1+\tau e_2}\theta(a+B),
 \qquad \sigma,\tau\in\{0,1\},\quad\theta\in\widehat{Q_0}.
\]

Define the probability distribution of top cosets by

\[
 \mu(q)=\frac{|T\cap(q+B)|}{|T|},\qquad
 \widehat\mu(\theta)=\sum_{q\in Q_0}\mu(q)\theta(q).
\]

Then, with exactly the manuscript normalization,

\[
 \boxed{\ \alpha_{\sigma,\tau,\theta}
       =(-1)^\sigma\widehat\mu(\theta).\ }              \tag{3}
\]

In particular the trivial character has coefficient 1 and the first sign character epsilon_1 has coefficient -1, for **every** nonempty top set and every subgroup B. This is unchanged by replacing the uniform measure on T with any probability measure on A.

### Zero-total-coefficient obstruction

For every such projection,

\[
                 \sum_{\psi\in X}\alpha_\psi=0.        \tag{4}
\]

Indeed, (3) pairs each coefficient for sigma=0 with its negative for sigma=1. Equivalently, character orthogonality on G/B gives zero at e_1(t), because its first sign coordinate is nonzero. This argument does not require positive Fourier coefficients, conjugation symmetry or nontrivial Q_0.

If different abstract characters induce the same primitive Dirichlet character, merging their coefficients preserves the total sum. Any finite real or complex linear combination of these coefficient vectors still has sum zero, even when the hosts differ. Therefore it cannot equal a nonzero vector of real nonnegative coefficients. In particular it cannot equal a positive multiple of zeta alone. This is a statement about coefficient identities; it makes no unsupported assertion about linear independence of analytic functions.

With \(\mathcal K=\{1\}\) and zeta weight 1, the manuscript's absolute projection majorant includes at least \(|Z_{\epsilon_1}(x)|\), before the short-shift errors are added. Since the zero coefficient mass is preserved by cross-host cancellation, using several hosts does not by itself remove this issue.

### No fixed analytic cancellation modulo smooth corrections

There is also an analytic strengthening which requires only the classical nonvanishing of nonprincipal Dirichlet L-functions at one, already used in the manuscript. For finitely many distinct primitive characters chi and fixed complex coefficients c_chi, suppose

\[
                         \sum_\chi c_\chi G_\chi(x)
\]

is continuously differentiable on a terminal half-line. Then all the coefficients are zero.

To prove this, let N be a common multiple of the conductors. At every sufficiently large prime p not dividing N, the derivative jump of G_chi is \(\log p\,\chi(p)/p\). The principal correction and the logarithmic-derivative corrections are smooth. Hence \(R(p)=\sum_\chi c_\chi\chi(p)=0\) at all these primes. Fix a retained character xi and lift every character to modulus N. For real sigma>1 form

\[
 \sum_\chi c_\chi
   \left(-\frac{L_N'}{L_N}(\sigma,\chi\bar\xi)\right).
\]

Its prime terms are \(R(p)\bar\xi(p)\log p/p^\sigma\), so only finitely many are nonzero. All higher prime-power terms converge uniformly as sigma tends to one: their absolute values are bounded by a constant times \(\sum_p\sum_{k\ge2}\log p/p^{3k/4}<\infty\). Thus the displayed expression is bounded. Every nonprincipal term is bounded by nonvanishing at one, including the finite Euler factors of an imprimitive character. The unique principal term has expansion \(c_\xi/(\sigma-1)+O(1)\). Therefore c_xi=0, as claimed.

For real parts, first write \(\Re G_\chi=(G_\chi+G_{\bar\chi})/2\) and merge conjugate characters. More generally \(\Re(cG_\chi)=(cG_\chi+\bar cG_{\bar\chi})/2\). Symmetrization preserves the real total coefficient. Thus a fixed zero-total-coefficient projection cannot become a nonzero positive character combination by adding an arbitrary continuously differentiable correction on a terminal half-line. This uses neither Dirichlet's theorem on primes in progressions as an extra input nor any assertion that zeros of different L-functions are distinct. The coefficients and character family in this argument must be fixed; it does not prohibit estimates or cancellations for varying hosts at individual scales.

### Which quadratic character is epsilon_1?

The additive epsilon_1 is `chC` in `FirstPrimeNeSecondPrime.lean:21–24`. The map `toE` swaps the two multiplicative sign coordinates (`RecH.lean:10–11`), and `chr_bij` identifies this additive character with `Frame.chC` (`ChrBij.lean:21–24`). The latter is the second multiplicative sign, `chD`, not the designated `psC` character (`ZsmulGeneratorEqZeroOfProjection.lean:100–110`). `HostAx.art_ch` identifies its Dirichlet values on units with the Legendre character a mapped to (a/d) (`ConjEMemHostFIff.lean:99`). Here the host has an odd prime d congruent to 3 modulo 4 (`HostFacts.lean:34–42`). The Legendre character is nontrivial and its conductor divides the prime d, so its conductor is d. It is the quadratic character of the field Q(sqrt(-d)). The designated `psC` character belongs to the other sign coordinate; conflating them would hide the obstruction.

## 3. A fixed quotient with balanced fibres

Let pi:A onto Q_0 be a surjective homomorphism onto one fixed finite group and put B=ker pi. The canonical pullback identifies X with the characters of \((\mathbb Z/2\mathbb Z)^2\times Q_0\), so

\[
                         |X|=4|Q_0|.                 \tag{5}
\]

Equation (3) depends on A and T only through the normalized fibre counts mu. In particular, for a fixed nonempty T_0 contained in Q_0, taking T=pi^{-1}(T_0) gives mu equal to the uniform probability on T_0: every nonempty fibre has |B| elements, and |T|=|B||T_0|. More generally, equal positive fibre counts over T_0 give the same conclusion; full fibres are not necessary. For a prescribed probability distribution, the exact requirement is that the normalized counts equal that distribution, not merely that pi(T)=T_0.

This proves a fixed-quotient descent statement even if |A|, |B|, m and the geometric ranks grow with x. To obtain one fixed analytic positive combination at a given accuracy, also require that each selected quotient character induces the **same primitive Dirichlet character**, with the same merged coefficient, throughout that accuracy's whole windows. Auxiliary characters may vary if their aggregate error is bounded; the selected positive combination may not silently vary.

As a counterexample to using surjectivity alone, take A=(Z/2Z)^2, project onto the first factor and take T={(0,0),(0,1),(1,0)}. Its image is all of Q_0=Z/2Z, but its nontrivial Fourier coefficient is 1/3, whereas uniform top cosets give zero.

## 4. Positive weights and a single companion bound

Let nu be any probability distribution on Q_0 and take mu=nu*nu_check, where nu_check(q)=nu(-q). Then

\[
           \widehat\mu(\theta)=|\widehat\nu(\theta)|^2\ge0.
\]

Thus all coefficients with sigma=0 are nonnegative, and those with sigma=1 are their negatives. At a common argument x, define

\[
 H_+(x)=\sum_{\tau,\theta}|\widehat\nu(\theta)|^2
                    \Re Z_{0,\tau,\theta}(x),\qquad
 H_-(x)=\sum_{\tau,\theta}|\widehat\nu(\theta)|^2
                    \Re Z_{1,\tau,\theta}(x),
\]

omitting zero coefficients. The exact projected sum is \(H_+-H_-\), and the trivial character occurs in H_+ with coefficient 1. With common top scale a_t/b=x, (1) therefore gives

\[
                   H_+=H_-+(\overline E-\mathcal T)/k. \tag{6}
\]

Only an **upper** bound for the single weighted companion H_- is needed in this inequality. Separate absolute bounds for all its characters are stronger than necessary. Nonconstant top scales introduce the actual signed short-shift error, not a new change of coefficients.

Another exact design is

\[
 \mu=(1-\kappa)\,\operatorname{unif}(Q_0)+\kappa\,\delta_0,
 \qquad 0\le\kappa\le1.
\]

Its Fourier coefficients are 1 at the trivial character and kappa elsewhere. For q=|Q_0| and kappa=1/(3q+1), the probabilities are 4/(3q+1) at zero and 3/(3q+1) elsewhere: these are precisely the source's prescribed shares. This separates an elementary positive-coefficient design from the arithmetic task of realizing it by an admissible top set. A finite set realizes a probability distribution only when the required integer fibre counts fit inside its fibres; an arbitrary real distribution may instead be used only after proving the corresponding weighted version of the arithmetic and geometric identities.

For an RH-only endpoint, it is enough that the fixed H_+ contains zeta with positive coefficient and obeys the established vanishing-loss whole-window upper bounds. It is not necessary to arrange H_+=G_1. The companion is allowed to change with the host. However, proving such bounds for one **fixed** positive H_- at every accuracy would, by the same analytic criterion, prove the corresponding zero-free conclusions for its retained primitive characters as well. Equation (6) is consequently a weaker one-sided construction target, not an automatic resolution of those unknown estimates.

## 5. Fibre weights and a Parseval bound

### Correct weights on a surjective construction index

The original construction supplies a finite index set U and a map tr:U to A whose image contains B, rather than a bijection with B. Restrict to the nonempty fibres over B. For v in such a fibre put

\[
 p_v=\frac1{|B|\,|\operatorname{tr}^{-1}(\operatorname{tr}v)|}.
\]

Then the p_v are positive, sum to one, and push forward to the uniform probability on B. Thus every pointwise inequality for the actual geometric datum indexed by v can be averaged with these weights. An arithmetic quantity depending only on tr(v) has exactly its desired uniform mean. This repairs the possible bias of uniform averaging over U without discarding any nonempty word set or any positive rank weight. A bound already proved only for the unweighted U-average does not automatically remain valid after reweighting: prove the required weighted budget, or show the fibres have equal cardinality. If each fibre supplies several valid pointwise upper bounds for the same arithmetic discrepancy, one may instead choose the least of these finitely many bounds in that fibre and then average over B. Neither operation creates new maps.

### Fourier mismatch in mean square

Let mu and mu_0 be two top-coset probability distributions on Q_0. For q=|Q_0| put

\[
 V_\theta(x)=Z_{0,0,\theta}(x)+Z_{0,1,\theta}(x)
            -Z_{1,0,\theta}(x)-Z_{1,1,\theta}(x).
\]

The common-argument projection equals \(\Re\sum_\theta\widehat\mu(\theta)V_\theta\). Hence its change on replacing mu by mu_0 has absolute value at most

\[
 \boxed{\quad
 \sqrt{q\sum_{z\in Q_0}|\mu(z)-\mu_0(z)|^2}\,
 \sqrt{\sum_{\theta\in\widehat{Q_0}}|V_\theta(x)|^2}.
 \quad}                                                     \tag{7}
\]

This is Cauchy–Schwarz followed by the finite Parseval identity
\(\sum_\theta|\widehat\mu-\widehat\mu_0|^2=q\sum_z|\mu-\mu_0|^2\).
It retains cancellation between the four signs before taking norms. The same argument bounds the actual short-shift error by

\[
 \sqrt{q}\left(\frac1{|T|}\sum_t\sum_\theta
        |V_\theta(y_t)-V_\theta(x)|^2\right)^{1/2}.           \tag{8}
\]

These bounds have no factor |A| when the quotient is fixed. They still require the displayed spectral mean square to be controlled; Parseval does not itself bound an unknown Dirichlet sum. If all primitive characters in the four-sign quotient family are fixed, their logarithmic derivatives at one are fixed finite constants. The definitions of G then give a local shift bound of size
\(O((1+\log^2(2x))|y-x|)\) for \(|y-x|\le1\), \(x\ge2\), with a constant depending on that finite family. Indeed, between prime powers the derivative of the prime sum is \(\sum_{n\le y}\Lambda(n)\chi(n)/n\), whose absolute value is at most \(\sum_{n\le2x}\log n/n=O(1+\log^2(2x))\); the principal correction contributes only O(log x), and the fixed nonprincipal corrections contribute fixed constants. The function is continuous at each cutoff, so integration gives the assertion. With varying auxiliary characters, these constants must be retained rather than called uniform.

## 6. Translation symmetry removes characters before transfer estimates

Define the averaged nonlinear weight profile

\[
 F_{t,\psi}(\rho)=\frac1{|B|}\sum_{u\in B}\sum_{i=1}^m
       w_{u,i}(\rho)Z_\psi(a_t/w_{u,i}(\rho)).
\]

Suppose it is B-invariant as a function of rho for every sampled t and psi. Replacing g by rho-c-t_0 in the arithmetic balance then gives the **exact** reduced expression

\[
 \boxed{\quad
 \overline E=\Re\frac1f\sum_t\sum_{\psi\in X}\psi(c+t_0)
                     \sum_{\rho\in\Phi}\psi(-\rho)F_{t,\psi}(\rho).
 \quad}                                                     \tag{9}
\]

To prove this, first keep all characters of G. For psi outside X choose v in B with psi(v) different from one. Translating the inner rho-sum by v preserves the profile but multiplies the sum by psi(-v), so that sum vanishes. This is cancellation of the actual nonlinear transfer terms, before absolute values; it is not an estimate involving every character of the growing ambient group.

A sufficient condition, independent of the functions Z, is equality of the pooled empirical measures

\[
 \frac1{|B|m}\sum_{u,i}\delta_{w_{u,i}(\rho+v)}
   =\frac1{|B|m}\sum_{u,i}\delta_{w_{u,i}(\rho)}
       \qquad(v\in B).                                    \tag{10}
\]

In particular (10) follows from exact covariance
\(w_{u,i}(\rho)=v_i(\rho-u)\), or from equality of the corresponding lists as multisets. Condition (10) is weaker: individual frames need not be translates. Applying a function to two equal finite measures proves the needed profile invariance.

Under (10), the old transfer majorant can be replaced by a majorant of the reduced signed transfer on X. When exact covariance holds, one such majorant is

\[
 \frac1f\sum_{t,i}\sum_{\psi\in X}
 \left|\sum_{\rho\in\Phi}\psi(-\rho)
  \bigl(v_i(\rho)Z_\psi(a_t/v_i(\rho))
        -\mathbf1_{\Phi_{S,0}}(\rho)bZ_\psi(a_t/b)\bigr)\right|.
                                                               \tag{11}
\]

The outer phase has absolute value one. Formula (11) uses 4|Q_0| characters and keeps spatial cancellation inside each absolute value, whereas the original R_T sums absolute values over all 4|A| characters and over all places separately.

**Source boundary.** `CoreAtH.lean:29–41` and `SplitInertia.lean:67–73` identify the actual weights on the arithmetic and geometric sides. They do not assert (10). Even `SizesA` does not imply it. For example, let A=B=Z/2Z, m=1, S={0}, b=1. At second-sign-one places set

\[
 w_0(0)=2,\quad w_0(1)=1/2,\qquad
 w_1(0)=1/2,\quad w_1(1)=1.
\]

Take all second-sign-zero weights equal to 1/2, eta=0, b'=1/4, X'=1, x=a_t=10 and N=20. Every displayed `SizesA` condition holds, but the pooled measures at the two second-sign-one places are respectively \((\delta_2+\delta_{1/2})/2\) and \((\delta_{1/2}+\delta_1)/2\). They are unequal. Thus (10) is a precisely stated construction target, not a consequence of the source's size envelope.

## 7. The RH transfer reduces to three mean weights

This subsection assumes B=A and the source host's additional condition `PsQ`. The actual RH host supplier has this condition (`FieldChi.lean:53–58`, explicitly invoking `AnyGrp.psQ`). Here the four surviving primitive characters are

\[
                1,\qquad\chi_q,\qquad\chi_d,\qquad\chi_q\chi_d,
\]

where q and d are distinct odd primes and the quadratic characters have conductors q and d. The product has conductor qd: by the Chinese remainder theorem its restriction to each prime factor is nontrivial, so it cannot factor through either proper divisor of qd. Put

\[
 D_+=G_1+G_{\chi_q}-G_{\chi_d}-G_{\chi_q\chi_d},\qquad
 D_-=G_1-G_{\chi_q}-G_{\chi_d}+G_{\chi_q\chi_d}.
\]

### A convexity lemma with the exact zeta correction

For a>0 define \(F_{\pm,a}(w)=wD_\pm(a/w)\) on \(0<w\le a\). Then

\[
                       F_{\pm,a}(w)-a\log w
                  \quad\hbox{is convex}.                 \tag{12}
\]

Indeed, at every positive integer n, including multiples of q or d,

\[
             \kappa_\pm(n)=(1\pm\chi_q(n))(1-\chi_d(n))\ge0.
\]

The exact definitions in manuscript Section 1 give

\[
 F_{\pm,a}(w)-a\log w
   =\sum_{n\ge1}\Lambda(n)\kappa_\pm(n)(a/n-w)_++aC_{\pm,a},
\]

with C independent of w. The sum is locally finite for w>0 and consists of nonnegative multiples of convex hinge functions. This proves (12). The term is **plus** a log w before subtraction: it comes from \(-a\log(a/w)\) in the corrected zeta term. All nonprincipal logarithmic derivatives are in the constant C; no bound on them is used in this comparison.

For a finite nonempty list of positive weights w_j at most a and probability weights p_j, let \(\bar w=\sum p_jw_j\) and \(w_{\rm geom}=\prod w_j^{p_j}\). Jensen gives

\[
 \boxed{\quad
 \sum_jp_jF_{\pm,a}(w_j)
 \ge F_{\pm,a}(\bar w)-a\log(\bar w/w_{\rm geom}).
 \quad}                                                     \tag{13}
\]

If \(w_j\ge(1-\eta)\bar w\) on the positive-weight support, with \(0\le\eta<1\), then

\[
 0\le\log(\bar w/w_{\rm geom})
 \le\frac{\sum_jp_j(w_j-\bar w)^2}
           {2(1-\eta)\bar w^2}.                            \tag{14}
\]

For the proof put z_j=(w_j-bar w)/bar w, so their mean is zero. Integration of z/(1+z) gives \(z-\log(1+z)\le z^2/[2(1-\eta)]\) for every z at least -eta. Average this inequality. No upper bound on positive deviations is necessary. At eta=0 the mean condition forces all weights to be equal.

### Three-mean proposition

Assume the pooled symmetry (10), now with B=A. Write n=|A| and s=|S|>0, and partition the pairs of place and stage, including their translation label, as follows:

| Class | Weights included | Number of weights |
|---|---|---|
| Thick | w_{u,i}((0,1),a) with a-u in S | nms |
| Outer | w_{u,i}((0,1),a) with a-u outside S | nm(n-s) |
| Zero | w_{u,i}((0,0),a), all u,i,a | mn² |

Let their arithmetic means be b,c_+,c_- respectively, and their logarithmic arithmetic/geometric mean ratios be L_s,L_+,L_-. If S=A, omit the empty outer class and its terms; do not define an average over an empty class. Suppose all weights are at most \(\min_t a_t\), so every argument of G is at least one. Put

\[
 \bar a=\frac1{|T|}\sum_ta_t,\qquad
 Q_4=\frac1{|T|}\sum_tD_+(a_t/b),\qquad
 k=|T|mbd/2,\quad d=s/n,
\]

\[
 J_{\rm thin}=\frac m2\sum_t
   \bigl((1-d)c_+D_+(a_t/c_+)+c_-D_-(a_t/c_-)\bigr),
\]

\[
 J_{\log}=\frac{\bar a}{b}
      \left(L_s+\frac{1-d}{d}L_++\frac1dL_-\right).
\]

Then

\[
 \boxed{\quad Q_4\le
       \frac{\overline E-J_{\rm thin}}k+J_{\log}.\quad}     \tag{15}
\]

**Proof.** Equation (9) removes all but the four signs. At rho=((0,e),a), the phase is \((-1)^{\sigma+\tau(1-e)}\). Thus the exact remaining average is

\[
 \overline E=\frac1{2n^2}\sum_t\sum_{u,i,a}
 \bigl(F_{+,a_t}(w_{u,i}((0,1),a))
       +F_{-,a_t}(w_{u,i}((0,0),a))\bigr).
\]

Apply (13) to each nonempty class, pooling i and u before taking its mean. The thick mean contributes kQ_4, and the other means contribute J_thin. The logarithmic penalty is

\[
 \frac{m\sum_ta_t}{2n}
       \bigl(sL_s+(n-s)L_++nL_-\bigr)=kJ_{\log}.
\]

Hence \(\overline E\ge kQ_4+J_{\rm thin}-kJ_{\log}\). Division by k>0 proves (15). ∎

This removes individual thick-weight transfer estimates and all their separate logarithmic-derivative constants. Only a lower bound for the single signed thin mean J_thin is needed; separate absolute bounds for its two terms are stronger. The factor m cancels from J_log, with no fixed-rank assumption. The means and logarithmic dispersions still depend on the growing arithmetic datum and require genuine bounds.

The scale b in (15) is the **actual arithmetic mean** of the thick weights. The source's original b is only a lower endpoint, with thick weights between b and b+eta+1. Those conditions do not make their mean equal to b. To use (15), select the interpolation scale from the actual mean or explicitly keep the resulting short-shift error. Nothing in the proof discards this first-order change of scale.

For a zeta-only target, write the exact signed companion as

\[
 C_{q,d}(x)=G_{\chi_d}(x)+G_{\chi_q\chi_d}(x)-G_{\chi_q}(x).
\]

Since G_1(y)=D_+(y)+C_{q,d}(y), the most economical centering keeps the companion at its actual sampled arguments. For x at least two and \(|a_t/b-x|\le1\), the elementary zeta derivative estimate gives

\[
 \boxed{\quad
 G_1(x)\le\frac{\overline E-J_{\rm thin}}k+J_{\log}
       +\frac1{|T|}\sum_t C_{q,d}(a_t/b)
       +(1+\log(x+1))^2.
 \quad}                                                     \tag{18}
\]

Indeed, between cutoffs \(G_1'(y)=\sum_{n\le y}\Lambda(n)/n-\log y+\gamma\). For \(1\le y\le x+1\), the absolute value is at most \((1+\log(x+1))^2\), using \(0<\gamma<1\), \(\Lambda(n)\le\log n\), and the elementary harmonic-sum bound. The function is continuous at cutoffs, so integration proves the claimed centering error. Average the identity G_1=D_++C and apply (15). This uses no nonprincipal logarithmic-derivative bound. The primes q,d may vary with x: the target remains the fixed function G_1. If instead one uses the positive target G_1+G_chi_q, that primitive quadratic character and its coefficient must be fixed throughout each accuracy's window sequence.

## 8. One weighted geometric budget, retaining frame correlations

Use the same maps and rank-weighted means as `cs-weighted-lower`. For translation u let \(s_u=\langle\nu-h\rangle_u\) and define the two actual lower-comparison defects

\[
 a_u=\Gamma_u+F_u-\langle\nu-\mu+e+l\rangle_u,
 \qquad
 b_u=c_u+\langle h\rangle_u-F_u-\langle D\rangle_u.
\]

An exact rearrangement, with no inequality yet, gives

\[
 E_u=A_u-\Gamma_u+\langle D+e+l-\mu\rangle_u-M_u
          +(s_u-c_u)+a_u+b_u.                              \tag{16}
\]

Consequently, for any positive translation probabilities p_u, it suffices to bound the **joint** mean of a_u+b_u, and the mean of s_u-c_u. One does not need a_u and b_u to be nonpositive separately at every translation. Negative lower-comparison defects can cancel positive ones. This is a further weakening of applying `cs-weighted-lower` separately at every u. The inner probabilities are the actual positive rank weights divided by their total at that u; the outer probabilities are the specified translation weights. They must not be silently replaced by uniform weights over all word indices when the total ranks vary with u.

### Four moments for the frame term

On the finite nonempty translation index set, suppose a proved comparison for these same maps gives

\[
 s_u-c_u\le P_u=\log N_u+
 \frac{\beta U_u\log(1+H_u/U_u)+\eta_uH_u+4\sqrt{e_u}H_u}
      {1-\delta_u},
\]

where beta is nonnegative, N_u is at least one, \(0\le\delta_u<1\), and U_u,H_u,eta_u,e_u are nonnegative. Interpret the U_u=0 term continuously as zero; retain any further hypotheses of the supplying frame theorem, including its permitted range of e_u. Set

\[
 v_u=p_u/(1-\delta_u),\quad U_*=\sum_uv_uU_u,\quad H_*=\sum_uv_uH_u,
 \quad E_*=\sum_uv_ue_uH_u,\quad \eta_*=\sum_uv_u\eta_uH_u.
\]

Then

\[
 \boxed{\quad
 \sum_up_uP_u\le\sum_up_u\log N_u+
   \beta U_*\log(1+H_*/U_*)+\eta_*+4\sqrt{E_*H_*}.
 \quad}                                                     \tag{17}
\]

For the proof, the function \((U,H)\mapsto U\log(1+H/U)\) is concave and homogeneous of degree one on the nonnegative quadrant. Jensen, with probabilities proportional to v_u, bounds its sum by its value at (U_*,H_*). Cauchy–Schwarz gives \(\sum v_uH_u\sqrt{e_u}\le\sqrt{E_*H_*}\). The other terms are linear. The stated continuous convention covers U_*=0; when H_*=0 all height-dependent terms vanish.

The source `MeanBoundSecondForm.lean:151–158` supplies beta=4 and log N_u. Manuscript `cs-slope` supplies beta=2 and no log N_u **if** its integral maps, common target basis and matrix hypotheses hold for these same objects. Formula (17) does not assert that identification. It does replace a worst-case trace bound by the actual height-weighted moments, including the possible approach of delta_u to one.

Combining (16)–(17), (2), and either the general quotient estimates or (15) gives one explicit numerical acceptance criterion. Every error may grow with ranks; it is the complete normalized budget that must obey the required whole-window bounds at each fixed accuracy.

## 9. What Galois transport does and does not supply

There is an elementary exact transport statement for Hermitian lattices and their integral maps. Let E be a Galois number field and sigma an automorphism. For an O_E-lattice M, define its twist to have the same underlying abelian group and the scalar action \(a\cdot_\sigma m=\sigma^{-1}(a)m\). At an embedding v, give the twist the metric of M at v composed with sigma. An integral map f twists to the same additive map between the twisted modules.

This operation preserves positive rank, nonzeroness, indices of finite lattice quotients, normalized Arakelov degrees, all extremal slopes and global map heights. To check this, the scalar twist bijects integral submodules and quotients, the finite prime norms are merely permuted by sigma, and the archimedean determinant norms and map norms are permuted by v mapped to v composed with sigma. Degree and height are sums over precisely these places. The extremal slopes are preserved because their defining submodules and quotients correspond. At a chosen embedding, transport also the embedding by sigma inverse; the matrices in the transported bases are then exactly the old matrices. In particular their Hilbert–Schmidt errors, trace ratios and common-target-basis property have the same constants. No factor equal to the orbit size is introduced.

Thus, **if** one complete arithmetic construction is closed under these twists, with the specified place labels and canonical metrics, a B-orbit of that construction supplies exact weight covariance and the same frame costs. A convenient sufficient external design is T=pi^{-1}(T_0) with a_t depending only on pi(t): both the top set and its orders are then B-invariant. A single common target lattice is needed within each translated datum, as in the slope theorem; identifying all twisted targets with one fixed target across different translations would be an additional requirement if a later construction demanded it.

The exact source supplier comparison is as follows.

| Inspected source contract | What it supplies | What remains for the proposed symmetry |
|---|---|---|
| `QuadraticLogDerivCongr.lean:367–407` | A chosen point pt(u) for every translation and the weight read from its archimedean parameter through the place code | The selected points are not asserted to form a Galois orbit |
| `DataParams₂.lean:73–74` | wj is the corresponding rational coordinate of hc.e | No covariance of hc.e between different selected points |
| `FamCore.lean:90–105` | Common ranks, top set, field and reciprocity data across the family | These equalities do not identify the archimedean parameter functions |
| `FamCore.lean:132–136` | A point for every translation with the same interpolation orders aT and bT | Matching top orders is weaker than pooled equality of the weight measures |
| `AsmRec.lean:10–28` | The exposed core consists of ranks, a host and an arbitrary place-indexed HC parameter; its weights are read from that parameter | A translation rule on the HC parameter must be proved or imposed in a new construction |
| `SChain.lean:26–31`, `SplitInertia.lean:67–73` | Exact identification of arithmetic weights with the numerical slope datum | Numerical identification is not an equivariance theorem for the underlying theta maps or metrics |

This is a bounded audit of the public contracts, not a claim that no deeper source theorem could prove an orbit construction. The missing geometric step is precise: after conjugating the theta/lattice datum, its canonical integral modules, theta maps, period normalization and Hermitian metrics must agree with the transported ones, and its HC parameters must give the translated weights. The general lattice transport proof above does not establish those identifications. It shows that **once** they are proved, no additional abstract rank, frame or covolume loss is needed merely to form the orbit.

## 10. Necessary boundaries and counterexamples

Besides the unbalanced-fibre and failed-covariance examples above, the following prevent false savings.

1. **No automatic square-root gain in the number of translations.** A transfer defect equal to the same positive constant at every translation has that same average, however large B becomes. The same is true of a constant frame penalty. Independence, orthogonality or an actual signed cancellation must be proved before asserting a square-root saving.
2. **Small variance is insufficient without a lower weight bound, even for rational weights.** For an integer N at least two, assign probability 1/N to \(w_1=2^{-N^2}\) and probability (N-1)/N to \(w_2=(N-w_1)/(N-1)\). The arithmetic mean is one and the variance is \((1-w_1)^2/(N-1)\), which tends to zero, but the logarithmic arithmetic/geometric gap tends to infinity like N log 2. Thus the positivity margin in (14), or the actual logarithmic gap, cannot be dropped.
3. **Small mean frame defect does not control the frame cost.** On an exceptional set of outer probability epsilon, let e=1/4 and H=epsilon^{-2}, and let e=0 elsewhere. Then the mean e tends to zero while the mean H sqrt(e) is 1/(2 epsilon). This is why (17) retains E_* rather than substituting an unweighted mean of e.
4. **A small mean delta is insufficient.** On a set of probability epsilon take delta=1-epsilon^2 and eta=H=1; take delta=eta=0 elsewhere. The mean delta tends to zero, while the mean eta H/(1-delta) is 1/epsilon. The weights v_u in (17) must retain this denominator.
5. **Positive companion control can itself be a hard zero-free theorem.** The four-character projection has zero total coefficient, and its signed companion is not eliminated by calling it an error. A fixed positive companion with vanishing-loss bounds would itself imply zero-freeness for its retained characters. The present reductions leave this obligation explicit.

## Verification and remaining construction

The finite-group obstruction, fixed-quotient descent, exact signed budget, pooled symmetry reduction, convexity/Jensen lemma, three-mean proposition and frame-moment bound are ordinary mathematical deductions. The positive kernel and three-mean proposition were independently reviewed by both `global_inputs` and `endpoint_backbone`; both audits passed, including the ramified coefficients, domain, signs, cardinalities and every normalization factor. The frame-moment lemma was independently reviewed by `global_inputs`; its necessary beta nonnegativity hypothesis was then made explicit. The root independently reviewed the signed identity, quotient, symmetry, Jensen, three-mean and frame arguments and the analytic-independence proof; all passed. Finite nonempty probability and frame index sets are explicit. Exact rational finite-group checks separately verify six signed-balance/projection cases, Parseval, a nonzero off-quotient residual without symmetry, and positivity of both quadratic kernels at all 21 residue classes for q=3,d=7. The finite-group explanation was also checked against the short guide. No new Lean build was run.

All identities concern nonempty index sets and strictly positive denominators. Their arithmetic use requires the same host, weights, interpolation orders, logarithmic derivatives and integral maps on both sides. The newly isolated symmetry (10) has not been certified for the source's concrete theta/lattice supplier. Establishing it by a compatible Galois orbit construction, together with the actual thin, dispersion, frame and covolume budgets, is the remaining constructive task. Source hashes and bounded reads are recorded in `certificates/averaged-error-budget.json`; `build/averaged-budget-proposed.tex` contains conventional mathematical formulations for possible manuscript integration.
