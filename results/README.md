# Results proved in the manuscript

These are mathematical reductions and comparisons. Their proofs are in [the paper](../paper/main.pdf); none establishes the missing arithmetic input for a complete proof of GRH.

## Recovering a matrix from one scalar operator

Let D be the full Capelli differential operator, and let Z be multiplication
by the relevant Hermitian matrix coefficient. With [A,B] = AB − BA, the full
contracted matrix is

```math
\begin{pmatrix}
D&-[D,Z]\\
{[D,\overline Z]}&-[[D,Z],\overline Z]
\end{pmatrix}.
```

The [new proof](../paper/sections/new/commutator-matrix.tex) retains the
spectral shifts and coefficient order. It shows that the scalar restriction
identity determines all four entries and gives their restrictions along any
fixed finite standard flag. The group operators remain smooth without
dividing by intermediate minors, and they preserve the support and decay
conditions used in the Jacquet argument. The application retains the prescribed
terminal signature, character vectors and normalized orthogonal splittings.
Estimates uniform in growing chains remain open.

## One integration theorem for every finite residue word

For compact smooth coefficients with positive Gram support, all the required
first-coordinate marginals form a finite matrix of Schwartz functions. The
exact integration formula therefore follows by integrating derivatives whose
boundary terms vanish. This replaces separate analytic premises for every
subset of a residue word by one invariant-class theorem.

The [written proof](../paper/sections/new/jacquet-integrated-descent.tex)
combines this integration with ordered matrix congruences to prove actual
Jacquet positivity for every fixed finite mixture of both operations, under the
terminal domain, sign and separation hypotheses. An explicit cutoff argument
extends it to smooth coefficients with decay index A + 2h + δ and derivative
order (k + 2r + 1)h + 5, where δ > 0 and A satisfies the existing pairing bound.

Only the scalar paired density is asserted Schwartz. The factors involving
inverse coordinates need not separately be globally square integrable. The
local source word, operator, gauge and measure dictionary is now checked on
smooth coefficient classes. Source lists recurse tail first; the existing
original-parameter positivity criterion avoids imposing the stronger shifted
separation. One positive pairing constant works for every word. Quantitative
estimates for growing chains remain separate. See the
[source dictionary](../notes/residue-source-dictionary.md) and
[independent review](../notes/matrix-schwartz-review.md).

## Vanishing total exponent loss

For the same fixed positive character combination H, suppose

```math
H(x)\le M_jx^{1/2+\delta_j}\qquad(Y\le x\le Y^{b_j}),
\qquad\delta_j\longrightarrow0,
```

holds on arbitrarily late whole windows for each fixed j, with M_j ≥ 0 and
b_j > 1 fixed before choosing the windows. Then the occurring L-functions
have no zero to the right of one half. The multiplicative constants and window
shapes need not be uniform across j. Apply the existing one-sided criterion
separately at each exponent, then let those exponents approach one half.

The auxiliary families may also vary with j: if every positive combination
H_j contains a fixed target character or its conjugate with a positive
coefficient, the same proof excludes every target zero to the right of one
half. No uniform positive lower bound on that coefficient is needed. Each
H_j stays fixed throughout its own sequence of windows. Thus a common family
across accuracies is sufficient but unnecessary.

For the scalar arithmetic construction, the sufficient condition becomes
(C_j + 3) ε_j → 0. Bounded C_j is one sufficient possibility, not a necessary
uniformity requirement. Uniform control within each fixed-accuracy construction
remains essential. The proof, limiting cases and independent review are in
[vanishing-loss-program.md](../notes/vanishing-loss-program.md); the theorems
are integrated into the existing analytic and numerical sections.

## Removing a cohomological dependency

The bounded-order character argument now uses the coarse K-theory bound with
exponent 14, replacing its use of the older exponent 86. The field degree is
bounded before the varying parameters are chosen, and the comparison retains
the possible prime-dividing-degree error. This removes the finite-field
homology and arithmetic-cycle construction from this application.

Ten older cohomological sections, and four analytic alternatives under the
chosen uniform quasi-RH route, are preserved in the appendix. The
[structural review](../notes/global-architecture-review.md) verifies that the
preferred route retains the arithmetic complex and the needed class-number
and unit arguments.

## A redundant real-zero assumption

If every primitive Dirichlet L-function is zero-free for real part greater
than a common number ϑ < 1, every real zero β of a primitive nonprincipal
real character of conductor q ≥ 3 satisfies

```math
(1-\beta)\log q\ge (1-\vartheta)\log 3.
```

Thus the real-zero exclusion needed for the logarithmic-derivative estimate
is already included in that uniform hypothesis. The determinant proof gives
an independent route to the real-zero bound.

## Primitive characters and reflection

If a character modulo $N$ is induced by a primitive character $\psi$ of conductor $q$, then

```math
L(s,\chi)=L(s,\psi)\prod_{p\mid N,\ p\nmid q}(1-\psi(p)p^{-s}).
```

Every added factor is nonzero for $\mathrm{Re}\,s>0$. The primitive and imprimitive functions therefore have the same zeros, with multiplicities, in that half-plane away from poles. The normalized functional equation reflects a primitive zero at $s$ to a zero for the conjugate character at $1-s$. Thus primitive nonvanishing in the right half of the critical strip implies Dirichlet GRH.

The proof includes conductors, Gauss sums, the theta transformation, the conductor-one case, and the boundary at real part zero.

## A one-sided prime-sum criterion

Put

```math
G(x)=\sum_{n\leq x}\Lambda(n)(x/n-1)-x\log x+(1+\gamma)x.
```

For nonprincipal $\chi$ with $L(1,\chi)\ne0$, put

```math
g_\chi(x)=\sum_{n\leq x}\Lambda(n)\chi(n)(x/n-1)+x\frac{L'(1,\chi)}{L(1,\chi)}.
```

Let $R$ and the $m_\chi$ be positive integers, with a finite character family closed under conjugation and $m_{\bar\chi}=m_\chi$. An eventual upper bound

```math
R G(x)+\sum_\chi m_\chi\mathrm{Re}\,g_\chi(x)\leq Cx^\theta,\qquad 0\leq\theta<1,
```

implies zero-freeness in $\mathrm{Re}\,s>\theta$ for zeta and all characters in the family. No lower bound is needed. The paper proves the exact Mellin identities, the positivity argument, and the sign of the possible residue. It does not prove this arithmetic upper bound.

## A smoothed Möbius-sum criterion

If, for every fixed smooth compactly supported test $W$ and every $\varepsilon>0$,

```math
\sum_n\mu(n)\chi(n)W(n/X)\ll_{\chi,W,\varepsilon}X^{\theta+\varepsilon},
```

then $L(s,\chi)$ has no zero in $\mathrm{Re}\,s>\theta$, for $\theta\geq0$. The paper also proves the version for ideals and deleted Euler factors. A test chosen to have nonzero Mellin transform at a hypothetical zero gives a direct contradiction.

## Consequences of a second-moment bound

The paper proves the exact inequality that extracts one sum from many approximately equal sums. Applying it to sixth powers gives the October source's $11/12$ exponent **conditional on its displayed arithmetic inputs**. The precise optimization limitation is recorded in [negative-results](../negative-results/README.md).

## Inversion and uniformity

The remaining proved results include exact Möbius inversion for added cube factors, an induction with an explicit bound on its number of steps, and a continuation theorem with a common positive saving over a family. All multiplicativity, support, and uniformity hypotheses are stated in the paper.

## Average arithmetic losses and the geometric defect

The existing slope section now proves finite character averaging with explicit projection and transfer errors, and a weighted lower-estimate lemma. Their exact source correspondence and complete original clause ledger are in [the reduced construction target](../notes/one-construction-target.md).

The same section proves an exact orthogonal lattice splitting identity. A covolume bound needs only the discarded mean-degree and integral-index budget; suitable polynomial rank decay can suffice. The [geometric defect note](../notes/covolume-defect-budget.md) gives the proof interface, two necessary-control examples and the remaining core lower-slope problem. These reductions do not construct the missing global arithmetic data.

## Classical Galois representations

The Galois and adjoint-vanishing section now states the classical Galois
representation theorem with the required weights and local normalizations,
and proves the comparison between the permitted period realizations. The
local correspondence laws, depth-zero types and transfer to every allowed
weak correspondence have been matched separately. The
[adopted substitution](../notes/classical-galois-substitution.md) therefore
replaces the separate source construction of this input. The same global
representation supplies all required local comparisons and the repeated
uses in the Selmer argument. Independent theta identities, integral maps
and geometric lower bounds remain obligations of the construction.
