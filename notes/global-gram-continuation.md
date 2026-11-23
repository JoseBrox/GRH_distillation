# Arithmetic folding at the actual W08 frontier

## Result and exact scope

**Classification: closed obligations within W08** for the original
`MultPoly`, `IUnfold` and `LeviFinC` suppliers. `IUnfold` is the source's full
implication, retaining its explicit `PhWellDef` and weighted-seed
premises. An exact Poincare Gram identity is also proved under that
same original local decomposition premise. No whole proof-map node
is closed, and no uniform positive-trace estimate is claimed.

The full standard-mathematics proof is in
[`global-gram-continuation.tex`](../paper/shared/global-gram-continuation.tex).
It begins from the existing arithmetic setting, with the same field,
lattices, finite level, characters, word and Haar measures. The RH
application still permits growing field degree and geometric dimension.

## New arithmetic argument

For the actual rational group Gamma and compact Omega, define

`m_Omega(x) = sup_y #{gamma in Gamma : x^-1 gamma y in Omega}`.

Fix a compact set C. Choosing one return gamma0 injects every return
set into `Gamma intersect x Omega Omega^-1 x^-1`. For
`x = c(g,1)`, `c in C`, the finite matrices have one fixed denominator;
the v-th infinite-place block has radius at most
`B_v ||g_v||_op^2`. Counting these matrices in a single Minkowski
lattice gives the actual estimate

`m_Omega(c(g,1)) <= A_(X,Omega,C) (product_v ||g_v||_op)^(4 n^2)`.

Each block has real dimension `2 n^2`. Thus the product norm absorbs
the degree of the number field; the argument makes no bounded-degree
assumption. The constant retains the fractional-lattice covolume,
finite denominator, coordinate changes, compact sets and dimension.
This implies the source exponent `N1 = 4 n^2 sqrt(2 q_max)`.
When every signature is definite the norm is one, covering `N1=0`.

The original Bessel subgroup is `S=N semidirect H` with H everywhere
positive definite. Its arithmetic quotient is compact, by finite
positive-definite lattice classes and additive unipotent compactness.
The original finite column T is bounded by `M_T ||W(g)||`, since its
Levi class set is finite and its infinite action is unitary.

Take compact representatives C_S for `S(F)\S(A)`. On the original
finite support, for *every* s in S_infinity one can write

`y = gamma c (1,x_u k) (s g,1)`.

Rational invariance of return multiplicity and the count above then
give `m_Omega(y) <= A nu(g)^N1` after taking an infimum over s.
No measurable minimizing section and no new quotient norm are needed.
Quotient disintegration reduces the exact multiplicity-weighted seed
integral to the already proved weighted W integral. The finite Levi
quotient volume and finite quotient-support measure remain as their
actual product; arbitrary finite Haar choices cancel in that product.

This is a direct proof of the actual `IUnfold` contract and removes
the need to reconstruct the source's separate `SinfSection` cut for
this application. It does not merely assume polynomial multiplicity;
the actual arithmetic count is proved above.

The actual framed-lattice stabilizer also has a finite quotient by
the prescribed unipotent subgroup `NLam`. Project
`Lambda intersect X-perp` onto the positive definite complement W,
retaining its denominators. The stabilizer acts on this projected
trace lattice; its kernel is exactly `NLam`, since it already acts
trivially on the flag grades and on the distinguished vector modulo X.
The isometry group is finite by counting lattice vectors of each fixed
basis norm. Transporting a finite representative set between any two
original lattices proves the exact `LeviFinC` supplier. This is actual
arithmetic finiteness; its orders are not bounded uniformly.

## Downstream verification

The compact archimedean reproducer combines with
`conjugate(chi2) 1_K / mu_f(K)`; the level-volume factor is retained.
Positive unfolding gives everywhere absolute Poincare convergence,
L2 membership, and the exact identity

`integral P_T conjugate(P_T') = sum_[r] integral Phi_T(x) conjugate(Phi_T'(r^-1 x))`,

where `[r]` runs over **all** `S(F)\Gamma/S'(F)` and the term uses
`S(F) intersect r S'(F) r^-1`. The sum of the absolute integrals is
finite. A finite noncommutative-group diagnostic tests the full
stabilizer factors, conjugation orientation and Haar scaling; it is
not the proof of the adelic statement.

## Exact remaining frontier

Do not replace `IUnfold` by an unconditional `FoldOK` declaration:
`PhWellDef` is explicitly retained here. The finite local source
algebra identifies the decompositions and phases through `KsetSplit`,
`UnipotentConjugateInLevel`, `RatLevi` and `PsiProd`. Relevant bounded
source branches have been located, but this package does not claim
an independent reconstruction of every integral congruence calculation.

The displayed double-coset formula concerns the actual scalar
Poincare seeds. The source's `OOLintSumC` additionally refines these
returns by framed lattice classes. Its finite column lower majorant,
counting map from framed returns to rational returns and exact
slab/fundamental-domain dictionary must still be proved for those
same objects. The finite positive-Levi quotient required by that
counting map is now supplied by `LeviFinC`. Then
`SigRowsC` and `RowFormC` must retain every phase, class torsor,
finite volume and original normalization. `MassDataConc.bC`'s
replacement kernel `Sig/rho0` is still not a proof for raw `KVOf`.

The final positive-trace/period-return estimate remains open. The
finiteness constants in this package are not uniform arithmetic bounds.
Their purpose is to justify exact unfolding; they should not be
substituted into the final numerical budget without new estimates.

## Verification

Run `python scripts/global-gram-continuation-check.py --offline`.
It authenticates the exact pinned contracts and proof excerpts,
records manuscript dependencies, and executes the finite-group
normalization diagnostic. No Lean build or kernel audit is claimed.
