# Terminal Fock matching and the common see-saw scalar

This proves the real/finite separation for the actual evaluated double
lifts, including the exceptional last pair, and their terminal
branching pairing. It uses the fixed pointed-space transport,
mixed zero-term normalization, graded double-period identity and
compact edge realization proved in the companion chapters.
The initial real Bessel reproducing formula and its quantitative
return estimates, and the arithmetic support-to-cut bounds, remain
independent inputs to the complete global see-saw theorem.

## 1. The actual last pair

Use the rational Hermitian spaces and gradings of
[lsernau-graded-period-unfolding.md](lsernau-graded-period-unfolding.md).
In the middle pairs the three string lengths are \(s,s-1,s-2\),
with \(s\geq3\) odd. Write \(V,V',V''\) for the three
lower-chain spaces and \(X,X',X''\) for the definite upper-chain
spaces. The joined space is
\[
 W=\operatorname{Hom}(V',V^-\oplus V'').
\]
Its grading is target grade minus source grade. Since the two
outer strings have even grades and the middle string has odd
grades, its degree-zero part is precisely
\(\operatorname{Hom}(X',Z)\), where \(Z\) is the degree-zero
part of the outer sum. The two central string coordinates form
one split Hermitian plane (their norms are \(N,-N\));
their sum is isotropic, and dividing the difference by \(2N\)
gives its dual. The positive degree subspace of \(W\) is
isotropic and pairs perfectly with its negative degree
subspace. Hence the reduction removes the positive/negative
degree coordinates and the one plane in \(Z\), leaving
\[
 W_0=\operatorname{Hom}(X',X^-\oplus X'').
\]
This is the splitting used in the graded double-period identity.

The last pair \(i=\varrho\), \(m=2\varrho+2\), is different.
Its string lengths are \(1,0,0\). Write \(z\) for the first
space's sole string vector, of norm \(-N\), and
\(X_0''=\operatorname{InitIndex}(m)\) for the actual definite
part of \(Y_m\). Then \(X''=X_0''\oplus E\), and
\(z/\pi_N\) has norm \(1\) in \(V^-\), since
\(\pi_N\overline{\pi_N}=N\). The map
\[
 X^-\oplus (X_0''\oplus E)\longrightarrow V^-\oplus V'',
 \qquad (a,b,t)\longmapsto(a+t z/\pi_N,b)
\]
is a rational isometry. There are no positive-degree coordinates,
no middle grade-one row, and no plane to remove. Both string maps
\(T:V\to V'\), \(T':V'\to V''\) vanish: in each case the
definite summand is killed and there is no common string
coordinate. Thus the joined Heisenberg translation \((T^*,T')\)
is zero in this case. The last reduction is simply transport by
the displayed isometry. The last lower group acts on \(X_0''\)
and fixes the adjoined unit coordinate: its image in the last
upper group is exactly \(k\mapsto\operatorname{diag}(k,1)\).
In particular it has the same determinant, not its conjugate.

These assertions give the actual splitting and the terminal
embedding, including the scale \(\pi_N^{-1}\) (not a square
root of \(N^{-1}\) chosen separately at the places).
They are the ordinary calculation in
EdgePairEvaluation.lean, lines 1083--1200. The preceding
middle-pair splitting is lines 830--881. Its local phases and
pointed changes of coordinates are those of the previously
proved nonstandard transport; no new period is chosen.

## 2. Separation of real and finite data

In each pair use the above splitting \(R\), and write
\[
 {\cal E}_R=\operatorname{zeroTermFin}_R
        \circ \rho_f\bigl((T^*,T')_f\bigr).
\]
The joined datum is a tensor product over the infinite and
finite places. Its components are the two arrow-product
components, after applying the prescribed Weil operators to
each edge. The arrow product is the flip of the first component
followed by the external tensor product with the second.
These operations, the Heisenberg translation, and the mixed
zero term factor over the places. For a restricted tensor
product this follows by computing in Schrödinger coordinates:
the change of splitting is a product of metaplectic transports;
evaluation at zero in the removed variables is separately
evaluation on each tensor factor. In the mixed-mean convention
the same assertion follows by the already proved mixed
summation and zero-term laws. Outside the finite exceptional
set the data, transport and removed variables are the
unramified vacuum. Its evaluation at zero is the normalized
unit. Thus no infinite product of unspecified constants occurs.

The map \(\operatorname{arrowTensor}\) identifies the algebraic
tensor product of the two upper finite data spaces with the
finite part of the joined space \(W_0\).
Indeed at each finite place the two sets of variables are
independent after the flip. Locally constant compactly supported
functions on their product are finite sums of characteristic
functions of rectangles, by a finite compact-open refinement.
These rectangles span, and the map of the algebraic tensor
product is injective by independence of functions (or by finite
dimensional evaluation on each finite sum). Restricted tensor
products give the same conclusion globally. This applies as
well to the finite vacuum-generated realization, since its
Schrödinger transport identifies it with these finite data.
Consequently the actual evaluation on joined finite data is
\[
 \operatorname{finEval}_R=\operatorname{arrowTensor}^{-1}
                             {\cal E}_R .
\]
All the operators in \({\cal E}_R\) preserve finite data;
the inverse is used only on the finite part. In particular
there is no choice of a preimage that could depend on the twist.

Take the lower data of a pair, moved at the specified real
points \(\boldsymbol\xi\) and finite points \(\mathbf y\),
and apply its joined translation and mixed zero term.
The result is exactly
\[
 v_R(\boldsymbol\xi)\otimes
  \operatorname{arrowTensor}\bigl(
       \operatorname{evaluatedDatum}_i(\vartheta,\mathbf y)\bigr).
 \tag{1}
\]
Here the finite factor is the one just constructed, using
\(\operatorname{doubleLiftEvalY}(i)=\operatorname{finEval}_R\).
The real factor depends on the real points and on the fixed
weights, not on \(\vartheta,\mathbf y\) or the input form.
The reason is that the tame character has trivial infinite
component; the infinite Weil operators and the real flip and
zero term do not vary. In the last pair the assertion uses
exactly the rank-one border from section 1. This proves the
separation asserted in UnfoldingStages.lean 680--737.

## 3. One common terminal functional, including nonpolynomial data

For any fixed two consecutive upper definite spaces the
compact realization identifies integration of a polynomial
Fock vector against an algebraic-form coefficient with the
coefficient of the corresponding fixed-weight theta lift at
a new linear functional. More explicitly the compact
projection onto the specified first lowest \(K\)-type kills
all other Schur summands of the polynomial data. The surviving
summand has the second prescribed type, by the weight match
and the multiplicity-one Cauchy decomposition. A polynomial
there is a finite linear combination of matrix coefficients
obtained from the same highest vector by compact translation.
Moving these translations through the theta kernel gives the
new functional on the second coefficient module. All
coefficients of this finite linear combination depend only
on the polynomial, the first functional, and the fixed
infinite types. The conversion of the adelic integral into
the normalized class integral uses the volume and
Schur-orthogonality factors of the compact-edge chapter;
these are independent of the finite character. Thus this
is the uniform IsThetaLift statement, not just an equality
for the particular source vector of one twist.

For the joined pair a polynomial is a finite sum of products
of polynomials in its two disjoint sets of variables.
For such a product, use the flip/arrow-product theta identity,
then Fubini over the two definite quotients, and the preceding
single-edge assertion twice. For a simple finite tensor the
result is the coefficient of the composite of the two
upper lifts. Linearity gives the result for every finite tensor
\(f\). The flip constant is the fixed one, absorbed in the
second functional. In symbols, let \(L_\vartheta(f)\) denote
the prescribed composite map from the first to the last
upper form space. The joined theta integral \(J(v)\) with
first coefficient functional \(t\) and real datum \(v\)
satisfies for polynomial \(v\)
\[
 J(v)(\vartheta,f,\phi,g)
   = t_v\bigl(\rho''(g_\infty^{-1})
                  (L_\vartheta(f)\phi)(g_f)\bigr).       \tag{2}
\]
The same \(t_v\) works for all four displayed variables.

Here it is essential to extend (2) simultaneously, not to
choose a different functional for each finite datum. Let
\(\mathcal I\) be the set of quadruples
\((\vartheta,f,\phi,g)\) and let \(A\) denote the finite
dimensional last coefficient module. Define a linear map
\(\Lambda:A^*\to\mathbb C^{\mathcal I}\) by the right side
of (2). Its image is closed in the product topology:
choose finitely many coordinate functionals separating
\(A^*/\ker\Lambda\), by successively reducing the common
kernel until its dimension stops decreasing. The remaining
coordinates are linear combinations of the separating
coordinates. Hence the image is specified by closed linear
equations. No finite-dimensional assumption on the set
of twists is required.

For each fixed quadruple, \(J(v)\) is continuous on the real
vacuum model of the joined space: the bounded integration map
against fixed finite data is followed by the fixed theta
functional and compact quotient integration. One can verify
continuity either in the source vacuum-coefficient norm, using
the compact-set Weil operator bounds, or for the actual
Schwartz vectors in the Schwartz topology. In the latter
model Hermite polynomials times the Gaussian are dense,
and the metaplectic transports and partial evaluations of
section 2 preserve Schwartz vectors. The compact quotient
integration is continuous in that topology by the absolute
Schwartz lattice-sum majorant for the theta functional and
bounded Weil operators on compact sets of representatives.
Thus the real vector in (1), obtained from the specified
Schwartz real data by these transports, is in the closure
of the polynomial vectors in this topology.
The coordinate-continuous map \(J\) sends this closure to
\(\operatorname{im}\Lambda\). This proves (2) for (1) with
one functional \(t_R\) independent of all finite variables.
It supplies the terminal functional even if a transported
real vacuum is not a polynomial vacuum in the new splitting.

The double-period formula of the graded chapter now gives
the coefficient of the double lift at this functional.
At each nonterminal even stage the surviving period is
equivariant for the specified unipotent character, so its
restriction to the definite block determines it everywhere
on the Bessel group. Iterating (2) gives the coefficient of
the upper-chain composite. At the last stage, use section 1
to evaluate it at \(\operatorname{diag}(k,1)\) on the full
last lower group. This is the terminal coefficient match of
UnfoldingStages.lean 128--244, 739--end of the even-stage
induction. It uses the proved double-period identity; the
separate support bounds needed to insert finite cuts are
not part of this calculation.

## 4. Terminal branching and the scalar

Let \(H=U(Y_m)(F_\infty)\) be the compact terminal group,
with the source Haar measure, and write \(A,B\) for the
last lower and upper coefficient modules, with
representations \(\rho_0,\rho\) in the source conjugate Weyl
convention. Let \(b:B\to A\) be the actual branching matrix
constructed in the bounded-branching chapter. For the terminal
highest vector \(v_0\in A\) and the functional \(t_R\in B^*\)
given by the last coefficient match, put
\[
 I(t_R)=\int_H \rho_0(k)\,(v_0t_R)\,
          \rho(\operatorname{diag}(k^{-1},1))\,dk .
\]
Haar invariance makes this an intertwiner. The compact
branching multiplicity one implies \(I(t_R)=\lambda(t_R)b\).
For example, with any invariant Hermitian metrics on \(A,B\)
and the nonzero \(b\), one has the explicit formula
\[
 \lambda(t_R)=
 \frac{\operatorname{tr}(b^* I(t_R))}
      {\operatorname{tr}(b^*b)}.
\]
The denominator is positive, but the numerator can vanish;
indeed the zero functional gives zero.

For an algebraic test form \(x\) on \(Y_m\), the conjugate
scalar coefficient at a finite point \(h\) and real point
\(k\) is
\(\langle x(h),\rho_0(k)v_0\rangle\), in the source
Hermitian form. For a last upper form \(\psi\), the other
coefficient is
\(t_R(\rho(\operatorname{diag}(k^{-1},1))
                        \psi(\operatorname{diag}(h,1)))\).
Their product, integrated over \(k\), is therefore exactly
\(\lambda(t_R)\langle x(h),
                 b\psi(\operatorname{diag}(h,1))\rangle\).
Integrate over the finite classes with the source weights.
Write
\[
 c_b=\prod_\tau \Phi_\tau(\overline{\pi_N})^{
                               \mathrm{branchExponent}_\tau}.
\]
By definition the actual restriction is
\(R\psi(h)=c_b^{-1}b\psi(\operatorname{diag}(h,1))\).
The source inner product equals the class integral of the
coefficient-module Gram form divided by
\(d_A=\dim A\). Both groups at this step have the prescribed
standard compact measures, so no additional level index
occurs. Consequently the exact terminal pairing is
\[
 \int_{[Y_m]}F(g)\overline{x_{\mathrm{sc}}(g)}\,dg
       = \lambda(t_R)d_A c_b\,\langle x,R\psi\rangle .
 \tag{3}
\]
The factor is independent of the twist and of both forms.
This derives the source BlockPeriods.lean 123--end and
SeesawIdentity.lean 90--164 with the physical branching
matrix, not an unspecified proportional restriction.

Finally the raw see-saw scalar need not be nonzero. Given
the weighted cut sum, the terminal match and the normalized
quotient recursion give \(\Theta_\vartheta{\cal P}
=c_0 R L_\vartheta(\operatorname{seesawDatum}_\vartheta)\)
for a common \(c_0\in\mathbb C\). Suppose the finite
coefficient construction gives the raw datum as
\(C\sum_x r_\vartheta(x)\,\mathrm{gluedVacuum}(x)\), with
\(d r_\vartheta(x)\) integral off the twist and the prescribed
untwisted bound, \(d=\mathrm{residueMatrixCount}^{2m}\).
If \(c_0 C\ne0\), take the common nonzero scalar
\(c=c_0 C/d\) and the integral coefficients \(d r_\vartheta\).
If \(c_0 C=0\), take \(c=1\) and the zero datum for every
twist. In both cases the equality with a nonzero outer scalar
and admissible integral data holds, with the same support
and invariance conclusions and coefficient bound.
This is exactly the normUnit argument of SeesawIdentity.lean
624--end; proving the raw scalar nonzero is **not** an
additional requirement of the see-saw theorem. Nontriviality
of the resulting image, wherever needed, is a separate
spanning or injectivity issue. We remove the stronger
unnecessary obligation from the dependency plan.

## Sources and remaining obligations

All source references are to
[lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src):
* New/UpperBound/Seesaw/EdgePairEvaluation.lean 830--881,
  1083--1200, blob fade1bf126d4e50c2e802f9d02427d1fdbb2d459.
* New/UpperBound/Seesaw/UnfoldingStages.lean 128--244,
  680--837, blob ca9eae23d80a0dc582113498975731964f88a4e6.
* Lib/Adelic/AutomorphicForms/BlockPeriods.lean 123--end,
  blob 6f3a29be9e12c8cf2f8042781e36d1041620e1f2.
* New/UpperBound/Seesaw/SeesawIdentity.lean 90--164,
  540--end, blob 4d0a5499ce992297b859168c21408f9ed3b21aba.

The terminal matching and normalization are now proved using the
compact, graded, and mixed-model chapters. The full global
see-saw still requires the initial real Bessel reproducing
kernel, quantitative Poincare and return majorants, and the
arithmetic support-to-cut statements. The noncompact real-edge
checks and lower tests are not consequences of this terminal
calculation. No new Lean replay is asserted.
