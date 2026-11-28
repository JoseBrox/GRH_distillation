# Preferred proof plan: three constructions and one determinant

**Revised 28 November 2026.** This is the dependency plan for the ordinary
reconstruction of RH and Dirichlet GRH. It contains proved reductions and
explicitly open arithmetic suppliers; it is **not a completed proof**.
The [shared manuscript](../paper/determinant/body.tex) follows this order.
The [reading guide](../paper/guide/main.pdf) explains the mechanism.

The immutable comparison source is readable `grh/src/` at
[`lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207`](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207).
The original argument is attributed to Levent Alpöge and Claude; see
[sources](../sources/README.md), the [formal audit](../audit/lsernau-formal-audit-2026-11-26.md)
and the [architecture audit](../audit/merged-plan-readability-2026-11-26.md).
The original W04/W10 geometric route is retained as an alternative,
not imposed as an additional prerequisite.

## 1. The exact acceptance test

Work on one common integral target of dimension $D$. Choose $n>0$
independent normalized theta images and complete them to a basis. Let
$C$ bound their logarithmic squared covolume at infinity, $I$ be both
conjugate-side local clearing costs, and $Q$ be the actual complement
cost. In the symmetric normalization, $I=2\delta$.
The [finite determinant proof](../notes/lsernau-mathematical-extraction-2026-11-26.md)
gives

```math
0\le C+I+Q+B,
```

where $B$ is a height bound for the **combined** selected-twist correction,
with one common algebraic multiplier. The three constructions must give

```math
C\le n(H-mR+E_A),\qquad B\le-DH+E_B.
```

Consequently

```math
\boxed{nmR\le-(D-n)H+nE_A+E_B+I+Q.}                 \tag{1}
```

Keep the actual fraction $n/D$ and the signed missing-rank term.
When $H\ge0$ it is favorable; otherwise its size must be controlled.
Charge the actual complement determinant and combine corrections before
taking heights. An arbitrary metric rescaling or an uncontrolled missing
subspace invalidates the comparison.

The source's sufficient targets are

```math
D(H-3L)\le C+2\delta,\quad C\le n(H-mR+L),\quad
L=fa(\log b)^4,
```

```math
n\ge(1-4/b^2)D,\qquad
\delta\le10D\log(1+2b^2)fa(\log b)^3,
```

with $H\ge0$. They imply $mR\le fa(\log b)^5$ on the actual scales.
They are acceptance bounds, not all established ordinary suppliers.
The refined inequality (1) permits weaker aggregate bounds.

## 2. Common data: one normalization throughout

Fix $E=\mathbf Q(\sqrt{-d},\zeta_{q_1})$, an even number $m$ of lifts,
$k=r+1-m$ and $t=5r$. The upper ranks are $n_j=k+j(t+1)$;
the lower Bessel rank is $r$, with lower-chain ranks $r+jt$.
Use the actual levels, characters, lattices, Haar measures and
coefficient metrics of [common finite theta data](../notes/lsernau-common-theta-finite.md).
The upper principal levels have trivial stabilizers. Joint invariance
of the completed tensor suffices; individual summands need not be invariant.

The [Weil normalization](../notes/lsernau-weil-normalization.md),
[nonstandard transport](../notes/lsernau-nonstandard-weil-transport.md)
and [common jet comparison](../notes/lsernau-common-jet-conjugation.md)
fix phases, rational equivariance and conjugation before any twist varies.
The [graded period unfolding](../notes/lsernau-graded-period-unfolding.md)
and [terminal matching](../notes/lsernau-terminal-period-matching.md)
prove individual period identities with their volume factors.
The [Rallis identity](../notes/lsernau-rallis-sharp-inversion.md) gives
stable-range injectivity for supplied nonzero real edges. A raw terminal
scalar can vanish; the full common-chain nonzero-volume assertion is
still needed.

At noncompact real edges, the [explicit harmonics](../notes/lsernau-noncompact-real-edges.md),
[classical discrete-series inputs](../notes/lsernau-discrete-series-suppliers.md),
[projection bound](../notes/lsernau-projection-lower-bound.md) and
[quantitative smoothing](../notes/lsernau-quantitative-local-smearing.md)
are proved with their exact hypotheses. The harmonic-line norm and finite
polynomial smoothing do not yet control the entire projected quotient
or its total global cost.

## 3. Construction A: short integral theta images

The [CM scalar construction](../notes/lsernau-cm-theta-normal-form.md)
and [charged jets](../notes/lsernau-charged-jet-estimate.md) supply the
local arithmetic kernels. The
[common-chain transport theorem](../notes/lsernau-common-chain-transport.md)
then proves the actual global finite gauge in one step. If
$\delta\bar\delta=M$, the jet normalization $\bar\delta j_0$
cancels the translation denominator $\delta$. The auxiliary gluing has
exactly $D_N=N^{fm(n_0+n_m)/4}$ terms; its vacuum compression is a
left inverse and its restricted Gram operator is $D_N I$.
Joint invariance and the free upper levels give exact finite class sums.
This proves baseline integrality and transports the charged nonsplit gain.

The [norm-budget theorem](../notes/lsernau-common-chain-norm-budget.md)
closes the actual all-conjugate squared-norm bound, with remainder
$108fa\log b$ instead of $fa(\log b)^3$ (109 for the indicated terminal
class norm). A short definite class count records a bounded Gram matrix
and an intermediate module between $O_E^n$ and $G^{-1}O_E^n$.
Minkowski's second theorem and finite subgroup counting replace the
quantitative adelic-approximation/short-column class-count supplier.
The theorem uses the original admissible scales and fixed vacuum constant.

The [scalar sharpness theorem](../notes/lsernau-sharp-scalar-couplings.md)
needs six copies. The [actual six-copy comparison](../notes/lsernau-six-copy-test-transport.md)
uses blocks $(6,4,4,2z-14)$ in the same rank-$2z$ target, with integral
monomial contraction, exact vacuum cancellation and class sums. It halves
the sharp Fourier exponent from $12f$ to $6f$. The residual flat block
stays in the existing stable range. The
[rank-one false-lift theorem](../notes/lsernau-rank-one-false-lift-periods.md)
proves its actual orthogonality in the improved range $33<2z$.
Two compact finite orbits give bottom vanishing. A first nonzero tower
lift would be cuspidal and bounded, but the actual split Hecke polynomial
is invertible there. Fourier separation, with the good-place vacuum
level retained, then gives the block period. This removes the
quantitative hyperbolic-plane recursion for the actual rank-one case.

The [exceptional geometry](../notes/lsernau-exceptional-polynomial-geometry.md),
[middle-edge bound](../notes/lsernau-exceptional-middle-edge.md),
[branching matrix](../notes/lsernau-branching-normalization.md) and
[marked Hecke index](../notes/lsernau-marked-hecke-index.md) supply their
local corrections. The marked truncated colength improves the coefficient
14 to 6. The remaining work is the analytic see-saw construction of the
common datum, compatible nonzero volumes, exceptional-prime corrections
and the remaining noncompact global cost. The definite finite-chain
integrality and asymptotic norm are no longer open obligations.

## 4. Construction B: enough independent images

The [return theorem](../notes/lsernau-quantitative-returns.md) gives the
exact Gram coarea, integral-frame separation, absolute Poincaré
convergence and quantitative truncation. The
[Bessel-subgroup identity](../notes/lsernau-bessel-subgroup-moment.md)
computes the normalized main contribution. The
[two-place theorem](../notes/lsernau-good-form-multiplicities.md) proves
actual occurrence and equal good Hecke multiplicities using Harris–Labesse.

The preferred finite argument is now
[direct Bessel good-type transfer](../notes/lsernau-bessel-good-type-transfer.md).
Andrews–Thiem changes the balanced hook radical to its one-sided form;
the mirabolic generic representation then supplies a common lower
multiplicity, with equality for cuspidals. Together with the
[exact allowed/primitive counts](../notes/lsernau-finite-good-type-density.md),
this gives bad-type mass at most $2b^{-9}$ at each chosen prime.
The actual Bessel source trace equals its induced-character mass exactly.
No conjugacy-averaged local integral estimate is required for this step.

The [weighted lattice theorem](../notes/lsernau-link-lattice-counting.md)
proves the exact class-lattice average, including its $N^{-kf}$ gain.
The [frame-fibre proof](../notes/lsernau-corank-frame-fibres.md) uses
explicit integral moves and three finite quotients to close the full
weighted near-pair count. Its family includes the specified cell index;
reduction of the analytic terms to that family is a separate obligation.
The [link-gain proof](../notes/lsernau-link-gain-index.md) supplies
the congruence determinant gain, reciprocal torsion-index cancellation
and near-term gauge bound. It reduces the discriminant estimate to one
precise integral link-lattice cut; that cut also places pairs in the
proved corank and height range. The
[single-link reduction](../notes/lsernau-single-link-energy-frontier.md)
proves the complete summation step and scale comparisons from that cut,
the gauge-specific orbit bound and zero-term classification.
Under those explicit hypotheses it gives both
strips with the stronger bound $9b^{-40}|R|\dim X$ and source deficit
at most $5b^{-9}\dim X$. The pair-count theorem alone does not supply that
package. These are the precise shared prerequisites of the following
restricted estimates.

Let $r_\psi$ be the exact subgroup operator, extended by zero, and
$D_g=P^*\rho(g)P-r_\psi(g)$. The remaining restricted estimates are

```math
\sum_{g\in RG_i}\|D_g\|_{\rm HS}^2
       \le b^{-12}|R|\dim X,\qquad i=0,1.                 \tag{2}
```

Equivariance and contractive right convolution by the bad central
projectors prove from (2) both the identity estimate and mean positive
source deficit at most $4b^{-6}\dim X$. These conclusions should not
be pursued as additional analytic suppliers. The restricted estimates
(2), terminal-fixer and open-cell moments, and their remaining analytic
terms are still to be proved. The
[positive-type argument](../notes/lsernau-positive-type-moment.md) and
[common moment interface](../notes/lsernau-common-moment-interface.md)
then yield the quantitative independent family. Keep all source/target
weights and the actual positive rank.

## 5. Construction C: one aggregate arithmetic budget

[Spherical attachment](../notes/lsernau-split-galois-attachment.md),
[dominant matching](../notes/lsernau-iwahori-dominant-matching.md),
[type sorting](../notes/lsernau-iwahori-type-sorting.md),
[Shintani products](../notes/lsernau-shintani-product-types.md) and
[CM tower assembly](../notes/lsernau-tame-local-global-assembly.md)
supply the normalized representations and labelled local compatibility,
including coefficient prime 2. Use these on the actual common good
Hecke modules; the older quadratic/odd-rank attachment route is optional.

The [Selmer datum](../notes/lsernau-main-summand-data.md),
[critical systems](../notes/lsernau-critical-value-systems.md) and
[small-twist theorem](../notes/lsernau-general-small-twist.md) give the
selected-twist construction under the stated value and arithmetic inputs.
[Normalized transfer and critical norms](../notes/lsernau-normalized-transfer-critical-norm.md)
and [integral kernels](../notes/lsernau-integral-critical-kernels.md)
supply the stable-range formulas. The
[rank-two arithmetic theorem](../notes/lsernau-rank-two-period-arithmetic.md)
gives the endpoint measure and exact Euler relation. The
[rank-two period theorem](../notes/lsernau-rank-two-period-norm.md) closes
the fully ramified analytic norm and nonzero base case. Equal-rank Hecke
transfer forces a constant theta lift; anisotropic Siegel–Weil at
$m=n=2$, explicit Cartan integrals and the Hecke functional equation
replace three complementary theta exchanges.

[Integral separators](../notes/lsernau-integral-separators.md),
[tied rows](../notes/lsernau-tied-row-construction.md),
[local derivatives](../notes/lsernau-local-tied-derivatives.md),
[triangle detection](../notes/lsernau-triangle-detection.md),
[Kummer relations](../notes/lsernau-kummer-relations.md) and
[root selectors](../notes/lsernau-root-chain-selectors.md) supply detected
integral operators under their remaining numerical hypotheses.
Residue-field hyperplane avoidance combines them with no additional
valuation loss. A short Selmer group alone does not bound an arbitrary
spectral projector denominator.

[Fontaine–Laffaille](../notes/lsernau-fontaine-laffaille-zero-defect.md)
settles the aligned large-prime zero-loss range. The
[Smith](../notes/lsernau-fixed-relation-smith-bounds.md),
[inertia-algebra](../notes/lsernau-uniform-inertia-relations.md) and
[bounded-class](../notes/lsernau-bounded-class-crystalline-loss.md)
theorems supply fixed-data finiteness; the last is uniform in the full
auxiliary family, rank and precision. Its growing-field numerical cost
is not proved. The [exact cyclotomic theorem](../notes/lsernau-exact-cyclotomic-loss-and-budget.md)
shows that a width-only bound can incur genuine linear loss. It also
gives an effective sparse cyclotomic-inertia bound, a hypothesis not
established for the actual nonabelian family.

Only the following aggregate arithmetic inequality is needed. Put
$L=\log b$, $B_0=faL^3/(mk)$, $A=3fmbL^2$ and $\Delta=J-P$.
Let $\Lambda_j$ be the full-projection determinant cost, and
$C_{j,\alpha}$ the projected-pairing height at the $k/2$ main pairs.
The [aggregate comparison](../notes/lsernau-exact-cyclotomic-loss-and-budget.md#4-the-aggregate-projection-budget-is-the-needed-input)
proves that

```math
\mathscr A=\frac1d\sum_j\Lambda_j+2\sum_{j,\alpha}C_{j,\alpha}
 \le faL^4-mA-50m^2-mk(3B_0+10)                         \tag{3}
```

suffices when the norm and sharp-test costs are at most $B_0$.
It retains the favorable direction term $-mk\Delta$ in the full
inverse determinant. Every Selmer, detection and local denominator
cost must be included. There is no need for the original uniform
worst-case bound on each prime, eigensystem and critical pair.
Qualitative finiteness or auxiliary-precision enlargement does not
imply (3).

## 6. Finish at one common scale, then apply the analytic criterion

Prove the remaining common-chain analytic identities, higher-rank
gluing periods, moment bounds, aggregate budget and complement estimate at the same
admissible parameters. Insert them into (1), divide by the actual
positive rank and exact prime-sum normalizer, and control every error.

For fixed $q_0$ divisible by 18480 and a permitted prime
$d\equiv q_0/2-1\pmod{q_0}$, the exact analytic remainder is

```math
R_{q,d}(x)=\sum_{n\le x,\ n\equiv1\ (q)}
 \Lambda(n)(1-\chi_{-d}(n))(1/n-1/x)
 -\frac{\log x}{\varphi(q)}-c_{q,d}.
```

The [prime reduction](../notes/lsernau-moment-and-prime-reductions.md)
identifies the necessary Laurent constant and proves the large-cutoff
estimate by the fixed-modulus prime number theorem. For each fixed
accuracy, the arithmetic construction must work for every sufficiently
large integer $x$, with $m\ge\sqrt x$, $\log b\ll x^\varepsilon$
and $\log x_1\ge x^{\varepsilon/12}$. Then

```math
R_{q_0,d}(x)\le\frac{\varphi(q_0)(\log b)^6}{m}
       +|R_{q_0,d}(x_1)|+\log b\,|R_{1,d}(x_1)|.
```

The [zero-detection proof](../notes/lsernau-zero-detection.md) supplies
the finite-height quadratic-twist selection, one-sided Landau argument,
residue sign, functional-equation reflection and imprimitive-factor
checks. Choose the accuracy and auxiliary prime for a putative zero,
then keep them fixed while $x$ grows. For RH use $q_0=18480$;
for Dirichlet use a fixed multiple of 18480 and the target conductor.
Optional averaging/sampling variants need not be added when the
stronger pointwise interface is met.

## 7. Verification and the separate Hecke extension

Every imported theorem needs an ordinary proof or a primary reference
with checked hypotheses. A source `Lib` label is not a substitute.
The [verification index](../certificates/README.md) distinguishes exact
finite computations, pinned bytes, internal review, classical inputs
and formal evidence. There is no new full Lean replay.

The [Hecke transfer plan](../hecke/notes/lsernau-transfer-plan-2026-11-26.md)
records the CM structural inputs already proved for newly twisted
Selmer groups. Dirichlet GRH does not settle the nonabelian cubic
benchmark or infinite-order Hecke characters. Their common theta data,
exceptional primes, critical ratios and phase dependence remain separate.

Historical node counts remain RH **6/9**, Dirichlet **18/31**,
Hecke **6/9**. Changing the preferred route does not prove an old open
node. Earlier supplier proofs and alternative constructions remain
available through their files, the source atlas and Git history.
