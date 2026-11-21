# One averaged construction at each scale

## Checkpoint and result

This note refines work packages W02/W11. It identifies a strictly weaker sufficient arithmetic target than the source's pointwise construction package. The source facts are byte-verified against `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`; the certificate records only bounded inspected excerpts. The new inequalities below are ordinary mathematical deductions, not newly kernel-checked Lean declarations. The missing arithmetic/geometric construction is not being declared proved.

Three simplifications are already established at the displayed interface:

1. It suffices to bound the **average arithmetic discrepancy over the translation subgroup**. The source final comparison assumes a bound for every translation separately and then averages it.
2. The source already has a mean-slope theorem that needs only the **averages of two loss terms**, rather than the two pointwise bounds imposed by `CoreAtH`.
3. Finite multiplicative factors can remain explicit. The final extra exponent loss in `core_gm` merely absorbs a factor depending on the fixed character level; the varying-family analytic criterion allows that factor to depend on accuracy.

The complete clause ledger and a more flexible finite-error criterion appear below. Both averaged comparisons and the weighted lower-estimate lemma are proved here; construction of their arithmetic inputs remains open.

The finite character-averaging theorem and weighted lower-estimate lemma are now incorporated into manuscript Section 10, with labels `cs-finite-average` and `cs-weighted-lower`. The same section proves the exact loss from an orthogonal integral splitting, its discarded-degree budget, and a sufficient polynomial-decay criterion (`cs-orthogonal-cut`, `cs-exceptional-budget`, `cs-polynomial-exceptional`). Those estimates may supply the covolume contribution below only after the lattice, metric, projection and required quotient comparison have been identified with the same arithmetic construction. Their existence does not supply that identification or the remaining theta and integral-map estimates.

## 1. The averaged comparison

Retain one of the source's arithmetic hosts, its finite abelian group A, translation subgroup B, selected set T, and nonempty thick set S contained in B. Write

\[
 n_T=|T|>0,\qquad m\geq1,\qquad b>0,\qquad d=|S|/|A|>0.
\]

For each u in B, define the arithmetic discrepancy

\[
 E_u=\sum_{t\in T}\sum_{i=1}^{m}
       \bigl(\mathcal A(a_t,t,w_{u,i})-
                    \operatorname{Re}\mathcal M(a_t,w_{u,i})\bigr),
 \qquad \overline E=\frac1{|B|}\sum_{u\in B}E_u.
\]

The functions are the explicit prime-power sum and its main term in `FirstPrimeNeSecondPrime.lean:75–91`; their full conventional formulas are recorded below. All terms use the same host, Frobenius and inertia data, weights, logarithmic derivatives and top labels. The sets used in the arithmetic and geometric sides cannot be chosen independently.

Assume the source's size/thick-thin conditions, character-projection conditions and costs in `SplitInertia.SizesA`, `ThinScales`, `CostWindows` and `CharsA`, at sufficiently large x for their elementary character-translation estimates. Let H(x) be the resulting positive selected-character sum, and let

\[
 R(x)=\sum_{\psi\in B^\perp\setminus K}|G_\psi(x)|
\]

be the auxiliary-character remainder. Then

\[
 \boxed{\quad
 H(x)\le R(x)+4x^{1/2+\varepsilon}
       +\frac{2\overline E}{n_T m b d}
       +\frac4{dx}.
 \quad}                                                    \tag{1}
\]

In particular the numerator needs only an averaged upper bound; negative discrepancies may cancel positive discrepancies. One does not need an upper bound for every E_u separately.

### Proof

The local thick-part comparison in `ChCore.lean:75–152`, combined with the exact arithmetic balance in `ChBalance.lean:200–202`, gives for every u

\[
 \sum_{t\in T}\sum_{i=1}^{m}\operatorname{Re}\Theta_{u,t}(a_t/b)
       \le E_u+2n_Tmb/x.
\]

The source applies a pointwise upper bound on E_u before summing (`ChCore.lean:302–325`). Instead, sum this displayed inequality first and divide by the positive cardinality of B. Character orthogonality gives exactly

\[
 \frac1{|B|}\sum_{u\in B}\sum_{t,i}
       \operatorname{Re}\Theta_{u,t}(a_t/b)
 =\frac{mbd}{2}
       \sum_{t\in T}\operatorname{Re}
          \sum_{\psi\in B^\perp}\psi((1,0),t)G_\psi(a_t/b).
\]

This is `sum_Th` together with `ChCore.lean:326–333`. The character-translation estimate in lines 419–439 bounds the last t-sum below by

\[
 n_T\bigl(H(x)-R(x)-4x^{1/2+\varepsilon}\bigr).
\]

Divide the resulting inequality by n_T m b d/2. Every denominator is positive, giving (1). No estimate on an individual E_u has been used. ∎

## 2. Consequences for the source numerical envelope

If the source's auxiliary-character hypotheses hold for a fixed level of order o, then `SigALe.lean:38–60` gives R(x)≤4o x^(1/2+ε). The original construction is one supplier of an upper bound on the normalized averaged discrepancy in (1).

The last four lines of `CoreGm.lean` absorb the finite factor 1+4o into x^ε. Before that absorption, the same proof already gives

\[
 H(x)\le(1+4o)x^{1/2+(e_D+e_L+6)\varepsilon}.
\]

Thus the final +ε loss and its extra threshold are dispensable when multiplicative constants may depend on the accuracy stage. This does not improve a nonvanishing geometric exponent loss; it simply avoids demanding an unnecessary exponent absorption.

More substantially, (1) imposes no intrinsic square-root restriction on m. The familiar m≈√x choice comes from the particular construction's error terms x/m and m, not from Fourier averaging itself. A different construction may be accepted if its normalized averaged discrepancy and its other explicit errors fit a vanishing total-loss budget. If m or any rank grows with x, that budget must hold for all x in the required whole windows at a fixed accuracy; a theorem for each fixed m separately is insufficient.

## 3. The existing mean-slope route

`ChainSlopeWindows/LevelOfCongruence.lean:199–235` proves the source mean bound from averaged loss assumptions

\[
 \operatorname{avg}_u(\mathcal A_u-\Gamma_u)\le L,
 \qquad \operatorname{avg}_u I_u\le L.
\]

The pointwise package instead asks both inequalities for every u (`QuotientSlopeBoundsWith.lean:34–35`). Therefore an averaged construction can use the weaker mean theorem directly. Reindex its data by B, or prove that the chosen indexing has the required uniform pushforward to B. A surjection alone does not preserve uniform averages.

Each word set W(u) must be finite and nonempty, and its rank weights d_w must be strictly positive. These requirements justify the weighted means, maxima and rank-normalised slope expressions. An empty space cannot be used to make the construction clauses vacuous.

Within a word set, the divisibility inequality enters `s_lower5` only through its positive rank-weighted average (`LevelOfCongruence.lean:50–66`). The same proof permits that averaged divisibility inequality, provided it concerns the same h, log T and quotient maps. The upper/maximal-slope and variation estimates used separately to control the maximum-minus-mean term still need their own proofs; they are not erased by averaging.

## 4. An exact finite-error criterion

The preceding inequality retains several convenient uniform bounds. They can be replaced by explicitly averaged finite errors. This makes the proposed arithmetic target independent of the particular source error envelope.

Let A be a finite abelian group, B a subgroup, T a nonempty subset of A, and S a nonempty subset of B. Put n=|A|, n_T=|T|, d=|S|/n, and

\[
 G=(\mathbf Z/2\mathbf Z)^2\times A,\quad
 \Phi=\{((0,e),a):e\in\mathbf Z/2\mathbf Z,\ a\in A\},\quad f=|\Phi|=2n.
\]

Write c=((1,1),0), e_1(t)=((1,0),t), and t_0=((0,0),t). The thick positions for a translation u are

\[
 \Phi_{S,u}=\{((0,1),s+u):s\in S\}.
\]

The arithmetic host supplies primitive Dirichlet characters χ_ψ for every character ψ of G; the trivial character supplies the corrected zeta sum. Set Z_ψ(y)=G_{χ_ψ}(y), with the same normalised smoothed functions as in manuscript section 2. In particular the logarithmic derivative used in each main term is the actual one belonging to that primitive character.

Choose positive a_t, b and w_{u,i}(ρ), for t∈T, u∈B, 1≤i≤m, ρ∈Φ, where m≥1. Embed B in G by u↦((0,0),u). Let X=B^⊥ denote the characters of G trivial on this embedded subgroup. Choose K⊂X and positive real weights λ_ψ, and set

\[
 H(x)=\sum_{\psi\in K}\lambda_\psi\operatorname{Re}Z_\psi(x),\qquad
 \alpha_\psi=\frac1{n_T}\sum_{t\in T}\psi(e_1(t)).
\]

Here H must agree exactly with the chosen positive primitive-character combination. This equality includes multiplicities and normalisations, even when the host changes with x.

Define the **finite projection error**

\[
\begin{split}
 R_F(x)={}&\sum_{\psi\in K}|\alpha_\psi-\lambda_\psi|\,|Z_\psi(x)|
 +\sum_{\psi\in X\setminus K}|\alpha_\psi|\,|Z_\psi(x)|\\
 &+\frac1{n_T}\sum_{t\in T}\sum_{\psi\in X}
       |Z_\psi(a_t/b)-Z_\psi(x)|.
\end{split}                                                   \tag{2}
\]

For ρ=c+g+t_0, define the **finite transfer error**

\[
\begin{split}
 R_T={1\over |B|f}\sum_{u\in B}\sum_{t\in T}\sum_{i=1}^m
 \sum_{g\notin\Phi}\sum_{\psi\in\widehat G}
 \left|w_{u,i}(\rho)Z_\psi\!\left({a_t\over w_{u,i}(\rho)}\right)
 -\mathbf1_{\Phi_{S,u}}(\rho)bZ_\psi(a_t/b)\right|.
\end{split}                                                   \tag{3}
\]

All the sums in (2)–(3) are finite. They use the same weights and labels as the arithmetic discrepancy. The prime-power sum and its explicit main term give \(\overline E\) as in section 1.

### The finite-error theorem

Assume the exact arithmetic character-balance identity for this host. Then

\[
 \boxed{\qquad
 H(x)\le R_F(x)+{2(\overline E+R_T)\over n_Tmbd}.
 \qquad}                                                     \tag{4}
\]

One may replace R_F by any proved upper bound for the actual real projection error in the first inequality below. The sum in (2) is an explicit nonnegative sufficient bound.

**Proof.** The triangle inequality and (2) give

\[
 H(x)-R_F(x)\le {1\over n_T}\sum_{t\in T}
       \operatorname{Re}\sum_{\psi\in X}
                    \psi(e_1(t))Z_\psi(a_t/b).
\]

The exact arithmetic balance expresses every individual discrepancy as

\[
 \operatorname{Re}{1\over f}\sum_{g\notin\Phi}\sum_{\psi\in\widehat G}
       \psi(-g)w_{u,i}(c+g+t_0)
             Z_\psi\!\left({a_t\over w_{u,i}(c+g+t_0)}\right).
\]

Replacing the weight expression by its thick constant-b counterpart costs at most (3) after averaging. Orthogonality on B kills the characters outside X. Since S⊂B, each surviving character is also trivial on S; the remaining factor is |S|/f=d/2. Thus

\[
 {n_Tmbd\over2}\bigl(H(x)-R_F(x)\bigr)
                   \le\overline E+R_T.
\]

All denominators are positive. Division proves (4). ∎

This is a genuine weakening of the earlier sufficient conditions:

- A translated-subset count need not be estimated separately at every translate. Only the selected Fourier coefficients and the actual projection error (2) enter.
- The logarithmic derivatives need no separate uniform O(log x) bound if the actual short-shift errors in (2) are controlled by another argument.
- A bound for every character at **every** y≥X′/3 is unnecessary. Only the sampled values a_t/w and a_t/b in (3) enter. The original `ThinScales` is one sufficient way to bound these samples.
- The errors in (3) may vary with u,t,i and the place. Their sum is what matters; one worst-case bound for every summand is not required.
- The geometric inequality needs only \(\overline E\), not all individual E_u.

These changes do not make the analytic errors automatic. In particular, using a bound of order y for an uncontrolled character at the scale x would generally be too large. The source's carefully chosen auxiliary characters remain one method of controlling (2).

Under the original thick/thin assumptions, the source proof gives

\[
 R_T\le n_Tm\,2f(x+1)\{3(\eta+1)+b\theta\}.
\]

Its two cost inequalities give R_T≤2n_Tmb/x. The original character estimates bound the projection error needed in the proof by Σ_aux|Z_ψ(x)|+4x^(1/2+ε). Using that projection estimate in the proof of (4) recovers (1), including its factors 2 and 4. The explicit nonnegative R_F in (2) is one sufficient majorant, not a requirement to discard a sharper estimate of the same real projection error. This verifies the connection to the original route without silently replacing a signed estimate by an absolute-value estimate.

### The arithmetic sum is explicit and finite without a separate cutoff parameter

One sufficient host is an abelian extension with group G, a finite set of bad primes P, and a distinguished prime p_* outside P. The exact source conditions are: 2 and q_1 belong to P; all primes outside P∪{p_*} are unramified; the inertia and the chosen Frobenius lifts at P lie in Φ; and inertia at p_* is {0,e_1(0)}. The source host provides all these conditions (`SplitInertia.lean:14–22`).

Write F_p for a Frobenius lift. Then the arithmetic quantity is

\[
\begin{split}
\mathcal A(a,t,w)={}&2\sum_{p\notin P\cup\{p_*\}}\log p
 \sum_{\substack{k\ge1\\kF_p\notin\Phi}}
          (a/p^k-w(c+kF_p+t_0))_+\\
 &+\log p_*\sum_{k\ge1}
       \sum_{\substack{g\in kF_{p_*}+I_{p_*}\\g\notin\Phi}}
          (a/p_*^k-w(c+g+t_0))_+.
\end{split}                                                   \tag{5}
\]

Only primes are summed. Every summand is nonnegative and vanishes once its prime power exceeds a/min_ρ w(ρ). Thus (5) is a finite sum despite its unrestricted notation. A common cutoff exists automatically because all indexing sets are finite and all weights are positive; the source's integer N and the last size clause need not be independent construction parameters.

The main term is

\[
 \mathcal M(a,w)=a\left(\log a-1-\gamma+ell_{\chi_c}
                   -{1\over f}\sum_{\rho\in\Phi}\log w(\rho)\right),
                                                               \tag{6}
\]

where χ_c is the quadratic character ψ((e_1,e_2),a)=(-1)^{e_1}, and \(\ell_{\chi_c}=L'(1,\chi_c)/L(1,\chi_c)\). Take its real part when forming the discrepancy. Formulas (5)–(6), including the factor 2 at unramified inert primes and factor 1 at the distinguished ramified prime, are `FirstPrimeNeSecondPrime.lean:75–91` and `ChBalance.lean:200–202`.

## 5. A smaller slope supplier: weighted lower inequalities and the actual frame cost

There is a more flexible way to supply \(\overline E\) than the eleven separate slope/count/error conditions of the source. It refines the already proved manuscript lemma `cs-combination`.

For each translation u, let W_u be finite and nonempty, with positive rank weights r_{u,v}. Write \(\langle\cdot\rangle_u\) for their weighted mean. The relevant real data are quotient slopes ν_v, source slopes μ_v, map heights h_v, exponent terms e_v, divisor terms D_v and quotient losses l_v, together with a common target slope c_u, a correction F_u and a geometric term Γ_u. Assume only the two weighted inequalities

\[
 \langle\nu-\mu+e+l\rangle_u\ge\Gamma_u+F_u,
 \qquad c_u+\langle h\rangle_u-F_u\le\langle D\rangle_u.
                                                               \tag{7}
\]

Put s_u=⟨ν−h⟩_u, and suppose a proved frame comparison gives

\[
                         s_u-c_u\le P_u.                       \tag{8}
\]

The source supplies P_u=log|W_u| plus its explicit nonlinear slope penalty. In the human proof, `cs-slope` or `qrh-sharper-slope` may supply a smaller P_u **when their integral-map, common-basis and frame hypotheses have been verified for these very same objects**. The recent orthogonal-cut bounds `cs-orthogonal-cut` and `cs-exceptional-budget` can be used only after identifying their covolume/index term in (7) or (8); no such identification follows merely from the same word “slope”.

### Weighted lower-estimate lemma

Under (7)–(8), for any arithmetic sum A_u and main term M_u,

\[
 A_u-M_u\le A_u-\Gamma_u
 +\langle D+e+l-\mu\rangle_u-M_u+P_u.                           \tag{9}
\]

**Proof.** The first inequality in (7) gives
s_u≥Γ_u+F_u+⟨μ−e−l−h⟩_u. The second gives
F_u−⟨h⟩_u≥c_u−⟨D⟩_u. Hence
Γ_u≤s_u−c_u+⟨D+e+l−μ⟩_u. Use (8), add A_u−Γ_u−M_u, and rearrange. ∎

Apply (9) to A_u equal to the arithmetic prime-power sum over t,i and M_u equal to its main term, with the exact identification of section 1. Averaging yields

\[
 \overline E\le\operatorname{avg}_{u\in B}
 \left[A_u-\Gamma_u+\langle D+e+l-\mu\rangle_u-M_u+P_u\right].
                                                               \tag{10}
\]

Consequently the right side of (10), together with R_F and R_T, is one explicit sufficient budget. There is no independent requirement that every individual height error, loss constant or frame defect have the same upper bound.

**What has actually been removed.** If P_u is controlled directly, one need not first prove the source's upper quotient-slope bound, pairwise height comparison, upper source-slope bound, or pairwise count oscillation solely to bound the maximum-minus-mean variable. The lower divisor and lower quotient statements may be proved only in weighted mean. The actual frame cost may also be averaged over translations instead of replacing it by uniform maxima. The source's polynomial height-gap bound, fixed exponent constants, and twenty-seven scalar window comparisons are one way to bound (10), rather than an intrinsic requirement of (4).

This is not a proof that those omitted estimates are unnecessary inside every possible construction. It is a weaker acceptance criterion for a new construction. The integral maps, positive-rank source lattices, their common target and their matrix realizations must still exist and satisfy (7)–(8). An arbitrary collection of unrelated numerical inequalities is not a geometric construction.

## 6. Complete ledger of the original six host conditions

The following ledger records the original conditions before any weakening. All source paths are recorded with hashes in the certificate.

| Source field | Explicit mathematical obligation | Use in the reduced criterion |
|---|---|---|
| `o_eq` | The fixed level order o equals the index [A:B]. | Fixes the original positive coefficients and bounds the annihilator cardinality by 4o. The general finite-error version instead specifies the positive coefficients explicitly. |
| `kept` | Every selected primitive character is induced by a host character trivial on B and equal to +1 on e_1(0). | Identifies the fixed positive target combination with H. This identity must still be exact. |
| `ps` | The designated quadratic character is identified with its selected primitive character when present, and is absent from the selected set otherwise. | Correctly assigns its weight 1 rather than 1/(3o+1). This is a quadratic-character bookkeeping condition, not a hypothesis asserting existence of a Siegel zero. |
| `shares` | For every γ∈A, the absolute difference between the cardinality of T∩(γ+B) and λ_γ times the cardinality of T is at most x^(−1+ε) times the cardinality of T; λ_γ is 4/(3o+1) on B and 3/(3o+1) off B. | Supplies the original selected Fourier-coefficient bounds; replaced by the explicit first term of (2) if a different construction is used. |
| `bdG` | Every character in the plus class not selected, and every character in the minus class, has absolute smoothed sum at most x^(1/2+ε). | Bounds the unwanted-character part of (2). A total weighted bound suffices in the new criterion. |
| `bdL` | Those same auxiliary characters have logarithmic-derivative absolute value at most C log x. | Bounds the short shifts a_t/b−x in (2). The exact finite short-shift error may be bounded directly instead. |

The plus/minus classes are the characters trivial on B with value respectively +1/−1 on e_1(0). The selected sum is

\[
 G_1(x)+\sum_{\chi\in\mathcal K\setminus\{1\}}
       c_\chi\operatorname{Re}G_\chi(x),\qquad
 c_\chi=\begin{cases}1&\chi\text{ is the designated quadratic},\\
                         1/(3o+1)&\text{otherwise.}\end{cases}
\]

The source definitions and exact identity are `ExplicitFormulaErrorOfHostConditions.lean:32–38,144–151`, `Analytic.lean:127–159`, and `GmAEq.lean:61–64`. The ledger does not reinterpret these source coefficients as freely variable inside one original source-level theorem.

## 7. Complete ledger of the original construction conditions

### Common indexing and exact identifications

The original package chooses a finite translation index U and a map tr:U→A covering B; finite **nonempty** word sets W(u); a finite top-index set; integers m,f; one numerical slope datum; one set of constants; and one X″. It also chooses one function of logarithmic derivatives, cutoff N, thick set S, interpolation orders a_t, weights w_{u,i}(ρ), top/character-type identifications, and scales η,X′,θ.

Its exact equalities are:

- the numerical datum uses the given x and ε;
- its top orders and archimedean weights are exactly a_t and w_{tr(u),i}(ρ), through the stated bijections;
- its Euler constant is γ and its quadratic logarithmic derivative is the actual real part of the character's logarithmic derivative;
- its arithmetic quantity is exactly the sum of (5) over the same t,i;
- its divisibility and loss exponents are at most e_D,e_L, and its height-gap exponent is at most c_H;
- every element of B has at least one translating index; S⊂B.

These are `CoreAtH.lean:29–41` and `SplitInertia.lean:67–77`. To replace the pointwise source proof by a mean proof, reindex by B or prove a measure-preserving indexing. A surjection is insufficient: uniform averaging over U biases translations with larger fibres.

### The eleven slope, count and lattice requirements

Use a for the global height scale; A_Σ=Σ_t a_t; L,L_a,B_0,N_c for the source size scales; v>0 and g_0 for its archimedean/local normalisation; and

\[
 \log\Omega=\gamma+\log(\pi/v)-\ell_c,\quad
 E_{u,z}=\sum_i E_{u,z,i},\quad
 s_u=\langle\nu-h\rangle_u,\quad
 U_u=\max_{z\in W(u)}(\nu^+_{u,z}-h_{u,z})-s_u.
\]

All slopes and heights with the same indices belong to the same maps/lattices in a geometric realization. Write c_D,c_E,c_H,c_C,c_S,c_Q,c_L for the seven nonnegative magnitude constants and e_D,e_L,c_* for exponent constants. The following formulas are `MeanBoundSecondForm.lean:111–163` and `QuotientSlopeBoundsWith.lean:19–35`.

1. **Admissibility.** x,b,k,v,f are positive; a,b′≥0; top orders are nonnegative and all weights are positive; word rank weights and their T_{u,z} are positive; ν≤ν⁺; c_Q≥0; δ̄<1; η̄≥0; and 0≤ē≤1/4.
2. **Divisibility.** For every u,z,
   \[
   \mu_{C,u}+h_{u,z}-F_u\le
   \sum_t\{m(a_t\log a_t-a_t-a_t\log\Omega)-a_t\log T_{u,z}\}
   +c_D n_T aL_a+c_Dm(B_0+N_c)x^{e_D\varepsilon}.
   \]
3. **Exponent comparison.** \(|E_{u,z}-mA_\Sigma g_0|\le c_E mB_0\).
4. **Height comparison.** The difference of \(h_{u,z}+A_\Sigma\log T_{u,z}\) between any two words at u has absolute value at most \(c_H(n_TaL_a+mB_0)\).
5. **Counting.** For every u,z,
   \[
   \sum_i{1\over f}\sum_\rho\log(w_{u,i,\rho}v/\pi)+mg_0
      -c_C(L_a+m^2L_a/k)\le\log T_{u,z}\le c_CmL,
   \]
   and every within-u logarithmic difference is at most c_C log k in absolute value.
6. **Source slopes.** \(-c_Sn_TaL_a(1+m/k)\le\mu_{M,u,z}\) and \(\mu^+_{M,u,z}\le c_Sn_TaL_a\).
7. **Quotient slopes.**
   \[
   \nu^+_{u,z}\le\mu^+_{M,u,z}+\Gamma_u+F_u-E_{u,z}+c_QmB_0,
   \quad
   \nu_{u,z}\ge\mu_{M,u,z}+\Gamma_u+F_u-E_{u,z}-L_{u,z},
   \]
   where
   \[
   L_{u,z}=c_QI_u+c_Qn_Tm(a/k+b')\log T_{u,z}+c_QX''+1.
   \]
8. **Two losses.** Both A_u−Γ_u and I_u are at most \(c_Ln_Tmbx^{e_L\varepsilon}\), for every u. The inspected mean theorem permits only their uniform means to obey these bounds.
9. **Slope comparison.** Whenever its range and height-gap premises hold,
   \[
   s_u-\mu_{C,u}\le\log|W(u)|+
   {4U_u\log(1+H_u/U_u)+(\eta_u+4\sqrt{e_u})H_u\over1-\delta_u}.
   \]
   The term U log(1+H/U) has continuous value zero at U=0. This is the actual source contract; stronger manuscript frame comparisons require their own same-map verification before substitution.
10. **Height gap.** \(s_u-\mu_{C,\min,u}\le H_u\), with \(0<H_u\le x^{c_*}b\).
11. **Frame parameters.** \(0\le\delta_u\le\bar\delta\), \(0\le\eta_u\le\bar\eta\), and \(0\le e_u\le\bar e\).

The numerical data also contain some fields used by older variants, such as a separate gamma-size parameter. They are not additional assumptions of these eleven displayed clauses. They must not be counted as independent mathematical obligations merely because they remain in a record.

### The scalar error windows and trace budget

`ErrorFormsWeakWindowsFalse.lean:23–45` requires all of the following:

\[
\begin{gathered}
 x\ge1,\quad0<\varepsilon\le1,\quad b\ge1,\quad xb\le a,\quad n_T\ge1,\\
 m\le x^{1/2+\varepsilon/2},\quad xm\le k,\quad e_K\ge0,\quad
 1\le k\le x^{e_K},\quad k\le a,\\
 0\le L,L_a\le2x^\varepsilon,\quad b'\ge0,\quad kb'\le a,\quad
 0\le X''\le a,\quad0\le a_t\le2a,\quad B_0,N_c\ge0,\\
 \log|W(u)|\le(k-3)\log2\quad\text{for every }u,\qquad
 \bar\delta\le1/2,\quad\bar\eta,\bar e\ge0.
\end{gathered}
\]

Each of c_D,c_E,c_H,c_C,c_S,c_Q,c_L lies in [0,K], and e_D,e_L,c_* are nonnegative. The additional trace budget is

\[
 (\bar\eta+4\sqrt{\bar e})x^{c_*}b
                  \le Kx^\varepsilon n_Ta.
\]

Replacing that last inequality by only η̄,ē≤1 is not justified; the source explicitly distinguishes the invalid weak-window assertion from the actual trace budget. In the reduced criterion the actual frame cost is retained in (10), so a sufficient averaged trace budget may replace these separate uniform inequalities.

### Size, thick/thin, and remaining arithmetic requirements

`SplitInertia.lean:42–48,74–77`, `SChain.lean:50–58`, and `GrowthBoundGivesRiemannHypothesis.lean:55–56` give the rest:

\[
 B_0\le2nmbx^\varepsilon,\qquad
 N_c\le {|S|kbx^\varepsilon\over n\,(nx^{-\varepsilon})}.
\]

There are η≥0,X′>0,b′>0,θ≥0 such that b′X′≤xb and |a_t/b−x|≤1. All weights on Φ are positive; on Φ_{S,u} they lie in [b,b+η+1], and elsewhere on Φ they are at most 2b′. All a_t/w ratios are at most the chosen N. The thin estimate is |Z_ψ(y)|≤yθ for every character and every y≥X′/3. The costs obey

\[
 2f(x+1)\theta\le1/x,\qquad6f(x+1)(\eta+1)\le b/x.
\]

Finally,

\[
 a\le2xb,\quad n_T\ge\tfrac12nx^{-\varepsilon/8},\quad
 d\ge x^{-\varepsilon},\quad m\ge x^{1/2-\varepsilon},\quad
 k\le n^2x^{1/2-\varepsilon},\qquad S\subset B.
\]

No condition in `CoreAtH` has been omitted from this ledger. Its dependencies have been grouped only after being unfolded. The source's eventual elementary inequalities log x≤x^ε and 200(1+K)^2(1+c_*)(1+e_K)≤x^ε are consequences for fixed constants, not extra arithmetic constructions.

## 8. Growing dimension and the final sufficient program

The original scalar windows force growth even before any geometric input. Combining xm≤k≤n²x^(1/2−ε) with m≥x^(1/2−ε) gives

\[
                         n\ge\sqrt x.
\]

The source's actual page-size supplier grows faster. Every frame has
\(2^e\le n\le o2^e\) (`FrameFacts.lean:188–192,258–260`). When its page size satisfies
\(x^{2+8\varepsilon}\le2^e\le2x^{2+8\varepsilon}\), one therefore has

\[
 x^{2+8\varepsilon}\le n\le2o x^{2+8\varepsilon},\qquad
                     [E:\mathbf Q]=4n.
\]

The page condition is `ExistsPageN.lean:39`; the degree identity is `ConjEMemHostFIff.lean:181–184`. At fixed accuracy, source-field degree, the number of selected top indices, the interpolation chain length and the possible word sets therefore vary as x grows. Finite-dimensional positivity for each fixed instance does not establish a common quantitative window estimate.

For a new proof, the acceptance criterion is instead the following:

- Fix a target primitive χ, including the conductor-one case.
- At accuracy j choose a finite positive combination H_j containing χ or its conjugate with positive weight. The auxiliary family may vary with j, but H_j remains fixed while its windows tend to infinity.
- At every x in arbitrarily late whole windows [Y,Y^{b_j}], construct one compatible arithmetic/geometric datum as above. It may depend on x, including all ranks and dimensions.
- Prove an upper bound E_j(x) for the average discrepancy using (10) or another rigorous construction, and establish
  \[
  R_{F,j}(x)+{2(E_j(x)+R_{T,j}(x))\over n_{T,j}m_j b_j^{\rm wt}d_j}
                  \le M_jx^{1/2+\delta_j},\qquad\delta_j\to0.
  \]
  Here \(b_j^{\rm wt}\) is the weight scale at x, distinct from the fixed window exponent b_j. It may depend on x; M_j is finite and fixed at accuracy j.

The finite-error theorem and `cor:varying-positive-families` then prove zero-freeness for the target to the right of one half. Supplying this construction for every primitive target and applying the established functional-equation and imprimitive reductions gives GRH.

This is a complete sufficient mathematical program with an explicit numerical acceptance criterion. The outstanding work is to construct the common maps, integral lattices, global theta identities and averaged norm/covolume estimates and to control the finite character errors on whole cofinal windows. It does not replace those open obligations by an assumption that GRH already holds, nor claim that the source's particular growing-rank supplier has been verified by fixed-rank local arguments.

## Verification and independent review

The root agent independently reviewed the averaged comparison, the finite character-error theorem, and the weighted lower-estimate lemma. The review checked the positive denominators, the thick-part phase g=e_1(s+u−t), orthogonality on the embedded subgroup B, the exact density factor d/2, both finite error sums, and the weighted linear rearrangements. All passed; the subgroup embedding was then stated explicitly for clarity. The source hashes and all recorded excerpt bounds were rechecked. These are mathematical deductions from the inspected identities and the proved analytic criterion, not claims of a newly compiled Lean theorem or completed arithmetic construction.

The endpoint reviewer subsequently checked all five integrated manuscript statements named above. The review passed after the explicit embedding of B in G and the integer condition on m were restored in the manuscript. It also checked x>0, the squared-slope factor two in the index term, the rank-zero discarded summand, the uniform polynomial-decay estimate, and the two counterexamples showing why discarded slope and gluing index must be controlled. The certificate now records the actual Section 10 file and its SHA-256 hash; the earlier ignored LaTeX proposal is retained only as a historical drafting artifact.
