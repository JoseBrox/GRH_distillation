# The full original framed-return sum

**Classification: closed actual convergence obligation within W08**, in
the original arithmetic gap regime already used by the construction.
No whole proof-map node or uniform positive-trace estimate is closed.

## Exact theorem

For the original `GTerm` set, representatives `r`, original lattices
`Lambda,Lambda'`, and original subgroup
`R_t = N_Lambda intersect r N_Lambda' r^-1`, prove

`sum_t integral_(R_t\G_infinity) ||W_u(x)|| ||W_u'(r^-1 x)|| dx < infinity`.

This is precisely the original `OOLintSum` conclusion, including every
admitted framed return and its actual fundamental-domain measure. It
also gives integrability of every original orbital rank-one operator
and summability of their operator norms.

The proof is in
[`global-gram-continuation-framed-returns.tex`](../paper/shared/global-gram-continuation-framed-returns.tex).
It uses the already established `WuDecay` and compact reproducer under
their original gap hypothesis. The formal predicate `OOLintSumC` is
universally phrased from `FoldOK` alone; that stronger quantifier is not
silently asserted here.

## New argument

Let K0 be the compact open stabilizer of the **original** full finite
adelic lattice. Use the auxiliary nonnegative function

`F_u^+(g,y_f) = ||W_u(g)|| 1_(S_u,f x_u K0)(y_f)`.

It is defined without finite phases or a choice of decomposition.
The arithmetic return count and compact S quotient prove its
multiplicity-weighted integrability directly. The original compact
reproducer gives a reproducing inequality, averaged over K0 with the
retained factor `1/mu_f(K0)`. Its positive Poincare series P_u^+ is
everywhere finite and L2. Hence `J = integral P_u^+ P_u'^+` is finite.

The enlarged support is used only to dominate the original norms; no
actual theta map, raw kernel, source lattice, restriction or level
normalization is changed.

For each original Lambda, its full rational S stabilizer A_Lambda
contains the original N_Lambda with finite index h_Lambda. This is the
new arithmetic `LeviFinC` theorem. The slice with finite component
`a_Lambda K0` has precisely stabilizer A_Lambda, so its exact measure
calculation gives

`integral_(N_Lambda\G_infinity) ||W_u|| P_u'^+(.,a_Lambda)
 <= h_Lambda J / mu_f(K0)`.

The map from an original framed return t and a coset
`m in R_t\N_Lambda` to the scalar rational return
`S_u'(F) r^-1 m` has finite fibres. Choose one element in a fibre;
comparison with it lies in the finite set of Levi representatives
carrying the target lattice to its target lattice. Equality of those
representatives forces equality of the original double coset and then
of m. Thus one common finite M bounds the fibres.

The condition `r Lambda'=Lambda` puts every finite component of the
associated positive seed inside its support. Transversal unfolding
therefore yields the explicit bound

`original framed sum <= M (sum_Lambda h_Lambda) J / mu_f(K0)`.

This replaces the source's finite-column lower majorant, neat column
decomposition, phase invariance and detailed small-level slab covering
for the **positive convergence** conclusion. It neither assumes those
interfaces nor uses their names as a proof.

## Remaining frontier

The original complex raw-kernel/period-Gram identity still needs the
precise finite phases, K2 volume, class frames and restrictions. Positive
domination does not identify that operator. The constants M, h_Lambda,
`mu_f(K0)^-1` and J may grow with the original field, dimensions and
lattices. They are not the required uniform positive-trace budget.

The most direct next step is now the phase-sensitive regrouping from
the absolutely convergent original orbital sum to the original raw
kernel, before attempting a family-uniform trace estimate.

## Verification

Run `python scripts/global-gram-continuation-framed-check.py --offline`.
It authenticates seven exact pinned source interfaces and checks 36
noncommutative finite diagonal-group models. The diagnostics verify the
return-fibre map, transversal integrals, stabilizer index and finite
Haar factor. They detect dropping the index or Haar scalar, and include
nontrivial fibres. They do not prove the adelic theorem or audit Lean.
