# Fixed-inducing savings in the global comparison

27 November 2026. A continuation of the [audit and centered power-free theorem](review.md) for Baiying Liu, [Joint marked moments and optimized zero-free half-planes for unitary Hecke L-functions, v2](https://hexagonmath.org/pdf/2611.00421v2).

**Result.** Inserting the stronger centered estimate into Appendix A.4 and Proposition 8.20 improves the fixed-inducing correlation estimates and relaxes the reference-length constraints, but does **not** improve the limiting zero-free boundary of the existing positive joint-moment/detector comparison. The limiting scalar obstruction remains B*=0.873345856106718576801.... This is a scope-limited negative result about the supplied estimates, not an obstruction to new analytic methods or a certification of all of Liu's analytic inputs. The arithmetic proof of Hecke GRH in this repository is unaffected.

## 1. Substitution in the actual fixed-inducing sum

Use the notation of Appendix A.4, printed pp. 94–98, particularly pp. 96–97. Write X for the residual full column scale, K for its raised frequency scale, g=NG, d=ND2, and D for the actual extracted norm. Then D>=gd>=1. Let L=max(1,Lf) where Lf is the pre-extraction minimum ordinary scale in the two signed arms. The reference construction has identical scale products, tests (including each normalized height), frozen marked primes and residual masks in both arms. On the fixed-inducing packets the relevant ordinary characters range over a fixed finite collection, including their fixed unitary anchors. These are precisely the hypotheses needed for the stronger centered estimate in Section 3 of the review; no bound for a moving-conductor reciprocal L-function is used. A pure norm twist must be normalized in its own coordinate in both arms, as in the source.

For the centered saving theta with 1/2<theta<1, the raw signed row is bounded, up to U^epsilon, by
\[
  (X/D)\max(1,L/D)^{-\theta}.
\]
It is enough to take theta=2/3 unconditionally relative to the source's native estimates. Conditional on the earlier unitary 7/8 theorem of [Hu, 2610.00216v2](https://hexagonmath.org/2610.00216v2), theta=707/1000 is valid uniformly over the fixed packets: the reciprocal contour is 1-theta=293/1000, and 3(1-theta)=879/1000>7/8. For finite order only, the earlier [Liu B2 theorem, 2611.00082v1](https://hexagonmath.org/2611.00082v1) allows theta arbitrarily close to 1-B2/3=0.70887267779559749... from below. Neither prior zero-free theorem has been freshly replayed in this continuation; the improvement never assumes B* itself.

The squared bound decreases with D, separately on D<=L and D>=L, since theta<1. Evaluate at gd. After multiplication by the second scalar K g/X^2 (and the original seed weight rho(G)), the bound per label becomes
\[
 U^\epsilon\,\frac{K\rho(G)}{d L}\,
       \Phi_\theta(gd/L),\qquad
 \Phi_\theta(t)=
 \begin{cases}t^{2\theta-1},&0<t\le1,\\ t^{-1},&t\ge1.\end{cases} \tag{1}
\]
This is the actual strengthened substitution for the relaxed bound on p. 97. It preserves central normalization; it does not multiply the marked prime lengths a second time. In particular it leaves the harmonic weight 1/d required by (119). There is a genuine extra power saving when gd/L lies outside [U^{-a},U^a] for fixed a>0, at least U^{-a min(2theta-1,1)}. At gd=L there is equality in the scalar relaxation, independently of theta.

### A uniformly bounded divisor sum

Let Q=L/g. For any fixed frame and fixed G,
\[
 \sum_{\mathfrak d\ne0}\frac{1}{N\mathfrak d}
       \Phi_\theta(N\mathfrak d/Q)
 \ll_{F,\theta}\min(1,Q) \quad (Q>0). \tag{2}
\]
Here the sum includes all nonzero integral ideals; any actual subset, including squarefree D2 coprime to G, is smaller. Put lambda=2theta-1>0. For Q>=1 the part N d<=Q is bounded by
\[
 Q^{-\lambda}\sum_{N\mathfrak d\le Q}(N\mathfrak d)^{-1+\lambda}
 \ll_{F,\lambda}1,
\]
and the remainder by Q sum_{N d>Q}(N d)^(-2) <<_F 1, using ideal counting and partial summation. For Q<1 the entire sum equals Q zeta_F(2). This proves (2). Apply it with the lower cap for L at a fixed pre-extraction frame (the raw squared bound decreases with L); hence the bound remains valid if the actual frame has a larger minimum. In (119) the possible pairs (G,A2) and unit packets for each y are divisor-many, and the original rho(G) multiplicities are subpower as in that proof. Thus this factor can remove the harmonic logarithmic loss from D2 in the fixed-inducing estimate, and gives a stronger bound when NG>L. All other subpower and profile losses still remain. Both first Cauchy orientations are independent; apply (1)–(2) with the appropriate c or d from the first correlation on each side.

The factor in (1) cannot yield a uniform new power of U by summing absolute values over all divisor labels. For instance, for g=1 and Q=L tending to infinity, the abstract allowed squarefree ideals with Q<=N d<=2Q have total weight bounded below by a positive constant: their number is asymptotic to Res_{s=1} zeta_F(s) Q/zeta_F(2), by the standard ideal-counting asymptotic and Mobius squarefree expansion. On this interval Phi is at least 1/2. This only establishes sharpness of the relaxed positive divisor estimate, not the existence of a physical correlation attaining it. A better bound would have to exploit genuine support, signs or other relations among these labels.

The finite-inducing row count is still U^{M/6+epsilon}. Since L>=U^{(ell_ref-c)_+} up to fixed scale constants, the exponent of the fixed side is still at most
\[
 k_C+M/6-(\ell_{\rm ref}-c)_+ +O(\eta+\epsilon).
\]
Its excess over the first-side allowance A-c+q_C=a+q_C+u' is at most
\[
 A+3u'-5/6-(5/6)t-c-(\ell_{\rm ref}-c)_++O(\eta+\epsilon)
 \le A+3u'-5/6-\ell_{\rm ref}+O(\eta+\epsilon). \tag{3}
\]
Here c,t are the first common width and frequency loss, t>=-O(eta), and u'<=u+O(eta). This uses the actual packed radius M=1+t-6u'+O(eta), not a separate cap for each D2 label. In particular the worst exponent in (3) does not improve just by increasing theta. The regular-row estimate (115), the origins, and the outer first-family exponent comparison remain unchanged.

## 2. A smaller reference length, with exact uniform margins

Proposition 8.20 (pp. 64–65) chooses ell_ref=101/1000 and checks the stronger intermediate inequality A+3u<5/6+(2/3)ell_ref. The actual packed proof in Proposition A.4 requires only A+3u<5/6+ell_ref, as is visible in (116) and (3). The positive short-reference estimate A.2 requires 4(ell_ref+W)<H, where W is the surviving mark width, H=1-6u. The diagonal requirements are A+4u<1 and 6u<1. Thus the relevant reference interval is
\[
 \max(0,A_{\max}+3u-5/6)<\ell_{\rm ref}<H/4-W_{\max}. \tag{4}
\]
Use any fixed reference in this interval before the asymptotic scale. Earlier kernel shortenings only reduce the widths, and a fresh reference is chosen before first correlation; as in the source, short arms are estimated directly, so no long arm with minimum below the chosen reference is passed into (1). When the lower endpoint in (4) is positive, the interval is nonempty exactly if A_max+W_max+(9/2)u<13/12; when it is zero, the only additional requirement is W_max<H/4. These are constraints of this ordinary reference argument, not a replacement for the inverse-stage inequalities.

The original stage hypotheses give A+4u<9/10, S/H<7/50, W<=S, H>=47/50. Consequently even with the original unconditional theta=2/3 one can replace ell_ref=101/1000 by **7/100** in Proposition 8.20, use (116) directly, and omit the unnecessarily stronger intermediate check. Exact margins:
\[
\begin{array}{c|c|c}
\ell_{\rm ref}& H-4(\ell_{\rm ref}+W)\text{ lower bound}
       &5/6+\ell_{\rm ref}-(A+3u)\text{ lower bound}\\
101/1000&6/625&103/3000\\
19/200&21/625&17/600\\
7/100&167/1250&1/300
\end{array}
\]
The lower bounds are strict where the source conditions are strict; mesh errors may be chosen below all fixed reserves. In fact any fixed ell_ref just greater than 1/15 and smaller than 517/5000 satisfies these two checks under the same stage hypotheses (the upper endpoint follows from (11/25)(47/50)/4=517/5000). If retaining the source's stronger intermediate inequality, the improved conditional theta=707/1000 permits ell_ref=19/200: its stronger margin is 5/6+(707/1000)(19/200)-9/10=299/600000. These choices do not alter the reference parameter in the separate reflection argument of Subsection 8.8. The 7/100 choice is the stronger simplification and does not need the improved prior-strip estimate.

No condition of Subsection 8.7 needed for the inverse half is deleted; in particular the stronger inverse diagonal condition A+4u<9/10 remains. The replacement is within the original physical stage, conditional on its unchanged packing and native analytic inputs.

## 3. Global obstruction after the substitution

The exact dependency is the key. Subsections 8.6–8.7 and the inverse half of Theorem 8.21 do not use Lemma A.1: they use the large-response detector, the canonical inverse transformation and the prior marked moments. The fixed-inducing estimate is invoked in the ordinary half, after the regular packed bound has been obtained from the same large-response prices (see pp. 57–60, 65–69 and A.4). Our improvements affect only the estimates on a finite inducing packet and the short-reference bookkeeping. The original regular bound and its witness cutoffs are unchanged.

For a descending stage R->r, put H=r/R, u=(1-H)/6, z the incoming improvement, and w_b the lowest cutoff. In the source w_b>=R. The binding large-response condition (Proposition 8.18 and condition 1 of Subsection 8.7) remains
\[
 F_{\rm high}=
  5/6-(5/4-3k/2)w_b-k(1+R)/2-kz>0 .
\]
Since 0<k<1/2, even dropping strict margins implies
\[
 k(R-1/2-z)\ \ge\ 5R/4-5/6.
\]
For 2/3<R<=7/9 this gives the same necessary cutoff
\[
 k\ge k_*(R,z)=\frac{5R/4-5/6}{R-1/2-z}.
\]
In particular even making the fixed-inducing contributions identically zero would not remove this inequality from the existing inverse proof. The propagated improvement remains no larger than
\[
 Y=Hz+(1/k-2)u \ \le\
 z+(r-R)\{a(R)z+b(R)\},
 \quad a(R)=\frac{45R-24}{R(45R-30)},\
 b(R)=\frac{9R-7}{R(45R-30)}.
\]
The affine tangent map is increasing in z since (R-r)a(R)<1 for r>2/3. The convex function
\[
 G(R)=11R/16-7/24-(5/16)\{7R^4(R-2/3)\}^{1/5}
\]
satisfies G'=aG+b, G(7/9)=0. Thus the same induction barrier G holds. The arbitrary-order, large-step envelope of Proposition 6.3 is likewise unchanged: it uses the regular short and long detector inequalities, and already grants the enlarged reference mark cap 1/6, removal of cutoff floors, and every finite step 0<u<1/6. Formula (4) relaxes only side conditions already absent from that envelope. It supplies no additional regular-row moment beyond this envelope by the specified recursion.

For the final comparison the critical r* is in (0.7523220538,0.7523220539), delta*=(45r*-14)/(6+54r*). The three active necessary planes in Proposition 6.5 are
\[
\begin{split}
 L_0&=5/6+M/12-\ell/6,\\
 L_K&=1/3+7M/12+\ell/3,\\
 H_c&=1+3\delta_*/4-(1/2+\delta_*/4)M+3\delta_*\ell/4 .
\end{split}
\]
Here ell is the final marked comparison length, **not** ell_ref. For any M,ell, their positive weighted sum with weights
\[
 (25\delta_*+8)/(6(4\delta_*+3)),\quad
 (4-\delta_*)/(6(4\delta_*+3)),\quad
 1/(4\delta_*+3)
\]
is B*=(14+25delta*)/(18+24delta*). None of these planes receives a new term from (1). The adverse amplitudes of Subsections 7.2–7.3 concern regular rows; the new fixed-packet estimates do not prohibit those scalar models. In particular one may assign zero signed differences on the fixed-inducing packet without violating any of the new upper bounds. The stated lower-bound theorem already grants all unequal ordinary moments within the envelope, including independent fixed unitary twists, and all variable comparison lengths. The two other numerator regimes of Subsection 7.3 have bounds >0.89 and 72703411/83204812=0.8737885376..., respectively. The attached exact script independently checks the floor identity and both additional dual identities, as well as the critical dual, root interval and inverse tangent map. It does not reverify every analytic hypothesis or model constraint of the source.

Hence, relative to the supplied positive comparison and its proved-as-stated analytic hypotheses, the substitution leaves the infimum exactly B*. The upper direction remains the original construction for every fixed B>B*, since the modified reference also satisfies all required strict side margins. The lower direction is unchanged even in the larger class of Proposition 6.3 and Definition 7.1. This is stronger than a failed numerical optimization: it identifies why neither enlarging the finite chain nor varying the auxiliary reference length can improve this endpoint using these substitutions. It does not rule out a new correlation argument on regular rows, an independent ordinary moment construction outside the supplied joint recursion, or a new mixed or signed numerator inequality. No new zero-free theorem is asserted.

## 4. Quantitative targets for a genuinely improved comparison

Two calculations identify meaningful research directions. Neither estimates an actual new arithmetic sum.

**Direct numerator target.** If the critical numerator plane H_c were replaced by H_c-epsilon, with the other two planes unchanged, its exact relaxed minimax would be
\[
 B_{\rm relax}(\epsilon)=B_*-\epsilon/(4\delta_*+3).
\]
The weighted dual gives the lower bound. Equality is attained in the unconstrained three-plane problem at M=4(B_relax-2/3), ell=1-M. The coefficient is about 0.2126157607, so a desired endpoint improvement of 10^(-6) would require a saving of at least (4delta*+3)10^(-6) in this plane if the other planes and critical amplitude stay fixed. A stronger ordinary moment that only holds on the already excluded packet cannot supply such a saving. Full feasibility would need the other amplitude classes and finite-stage margins as well.

**Inverse long-count target.** Suppose instead a new inverse long-count bound gives a normalized uniform saving epsilon at the binding stage (i.e. adds epsilon to F_high). With the same incoming envelope construction and initial value at 7/9, the ideal infinitesimal tangent map would then solve
\[
 G_\epsilon'(R)=\frac{G_\epsilon(R)+1/3}{R}
 -\frac{R-1/2-G_\epsilon(R)}
 {6R(5R/4-5/6-\epsilon)},\qquad G_\epsilon(7/9)=0.
\]
Work on a compact interval containing [r*,7/9], with the denominator positive and epsilon sufficiently small. Linear ODE parameter dependence gives J=partial_epsilon G_epsilon|_0:
\[
 J'=aJ-\frac{R-1/2-G(R)}{6R(5R/4-5/6)^2},\qquad J(7/9)=0.
\]
Writing f(R)=R^{4/5}(R-2/3)^{1/5}, so f'/f=a, yields
\[
 J(R)=f(R)\int_R^{7/9}
 \frac{t-1/2-G(t)}{6t(5t/4-5/6)^2 f(t)}\,dt>0
\]
for r*<=R<7/9; the positivity of the numerator follows from the original envelope (e.g. the denominator bound in Proposition 6.3). If the relaxed final contact is recomputed with this new envelope and the original final long detector, let delta(r)=(45r-14)/(6+54r) and G_req(r)=4/(9delta(r))-2/3-r/2. Its contact equation is G_epsilon(r_epsilon)=G_req(r_epsilon). It is simple at epsilon=0 (G'>-1/6 and G_req'<-1/2 there). Therefore
\[
 \frac{dB_{\rm rel}}{d\epsilon}\bigg|_0=
 -\frac{9}{4(9r_*-1)^2}
       \frac{J(r_*)}{G'(r_*)-G_{\rm req}'(r_*)}<0 .
\]
Illustrative 50-digit quadrature gives J(r*)≈0.0948306660524668 and derivative ≈-0.00405298069080656; these digits are not interval-certified, while the formula and strict sign are exact. This models a hypothetical saving to the *binding* long branch, not the centered fixed-inducing saving. One must still prove that the improved long estimates, the finite-stage approximation and all transverse comparison margins hold. Improving the final long detector itself would require a separate reoptimization.

## 5. Verification and research frontier

The [exact and sensitivity script](check_optimization.py) was run with SymPy, rational fractions and mpmath. The reference margins, inverse condition and tangent map, perturbed ODE differentiation, endpoint isolation, critical and auxiliary dual identities all passed exact checks. The final sensitivity figures are numerical evaluations only. Source locators: Proposition 6.3 pp. 23–24; Proposition 6.5 pp. 27–28; Definition 7.1 and Subsections 7.2–7.3 pp. 28–34; Proposition 8.18 pp. 57–59; Subsection 8.7 p. 60; Propositions 8.20–8.21 pp. 64–69; Lemmas A.1–A.3 and Proposition A.4 pp. 91–98. The versioned PDF text and relevant page images were inspected; no PDF byte hash or fresh formal replay is claimed.

The next worthwhile target is the **regular inverse large-value estimate** (not the fixed-inducing part), or a signed numerator estimate that breaks the active coefficient-two fourth-moment/Hölder plane. In particular merely feeding the stronger saving into the same positive recursion, refining the reference mesh, or iterating the same bootstrap cannot lower B*. A signed estimate must be proved on the actual regular arithmetic families and must change one of the binding inequalities. This note changes no dependency of the project's preferred arithmetic route and closes no legacy proof-map node.
