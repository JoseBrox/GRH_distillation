# Quantitatively normalized integral branching

This chapter establishes the bounded branching matrix required by
the terminal gauge calculation in the [exceptional polynomial chapter](lsernau-exceptional-polynomial-geometry.md).
In particular, it identifies the normalized map as the orthogonal
projection of an integral exterior-tensor contraction. Its denominator
depends only on the diagram below the common leading rows.

Source: [lsernau/grh-lean@72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src),
Lib/GLn/Branching/{IntegralMap,NormBound}.lean,
Lib/GLn/SchurModule/{GramMatrix,LeadingRows}.lean.
We use the usual integral straightening basis of flag-minor
products (the source nablaBasis); the representation and Gram
normalizations below are the source's, not an arbitrary integral
form of the irreducible representation.

## 1. Tensor coordinates and an integral hook bound

Work at all the complex places simultaneously, with positive old
rank \(k_\tau\) and new rank \(k_\tau+1\). For a column diagram
\(\lambda\), let \(T_\lambda\) be the tensor of exterior powers,
one factor for each column, with its orthonormal increasing-wedge
basis. Heights run from \(1\) through one less than the rank;
full-height columns are treated as determinant factors.
Let \(b_i\) be the standard integral basis of products of flag
minors. The rows of the filling matrix \(E_\lambda\) express all
increasing column-filling polynomials in the \(b_i\) basis.
Thus, with \(v_\lambda(y)=(b_i(y))_i\),
\[
 E_\lambda v_\lambda(y)
 =\bigotimes_{\text{columns of height }j}
          (y_1\wedge\cdots\wedge y_j).
 \tag{1}
\]
The standard monomial basis is selected from these fillings,
so \(E_\lambda\) has an integral left inverse. The evaluations
span the coordinate space over \(\mathbb Q\) or \(\mathbb C\)
by independence of the \(b_i\). Their generic coefficient vectors
span integrally as well: standard monomials have distinct unit
leading monomials for the diagonal term order (the row words of a
semistandard tableau determine it), so the coefficient matrix of
the \(b_i\) has an integral left inverse by triangular elimination.
Equivalently the integral standard monomial space is saturated
in the polynomial ring. These are the usual straightening
properties, also used in IntegralMap.lean (coord_mem_of_coeff_mem).

Put \(G_\lambda=E_\lambda^tE_\lambda\).
The source Weyl vector \(\xi\) has norm squared
\(\xi^*G_\lambda\xi\) and polynomial
\[
 {\rm toPoly}_\lambda(\xi)=\sum_i(G_\lambda\xi)_i b_i.
\]
In particular its polynomial at \(x\) is
\((E_\lambda v_\lambda(x))^tE_\lambda\xi\).

For any diagram \(\delta\), let \(H\) be the Fock pairing matrix
of the \(b_i\), for which the monomials are orthogonal and
\(\langle x^\alpha,x^\alpha\rangle=\alpha!\).
Set \(c_\delta=\langle f_\delta,f_\delta\rangle\), where
\(f_\delta\) is the product of leading principal flag minors.
Then \(H G_\delta=c_\delta 1\).
Indeed the Hermitian Fock form on the polynomial image of the
Weyl module and its tensor Gram form are invariant under the
product of unitary groups. By irreducibility they are proportional.
At the evaluation of the identity, (1) is the unit highest-weight
tensor, and its polynomial is \(f_\delta\) by the exterior
Cauchy–Binet identity, giving the proportionality constant.
Thus \(G_\delta H G_\delta=c_\delta G_\delta\), and cancellation
is valid since \(G_\delta\) is positive definite.
The identity over the integers follows by characteristic zero.
In particular \(c_\delta\) times the orthogonal projection of
any integral tensor onto the Weyl module has integral Weyl
coordinates: these coordinates are \(H E_\delta^t\) of that
tensor. In polynomial terms, \(c_\delta\) times any integral
column-filling polynomial equals \({\rm toPoly}_\delta(\xi)\)
for some integral \(\xi\).

The coefficient \(\ell^1\)-norm of a height-\(j\) minor is \(j!\).
For a diagram of total size \(D\), the Fock norm therefore gives
the explicit elementary bound
\[
 1\le c_\delta
 \le D!\prod_{\text{columns of height }j}(j!)^2
 \le D^{3D}.
 \tag{2}
\]
Indeed each multiindex factorial is at most \(D!\) and the sum
of squared coefficients is at most the square of the coefficient
\(\ell^1\)-norm. For \(D=0\) take \(c_\delta=1\).
The constant is a positive integer; no hook-length formula is
needed. This gives the source GramMatrix.lean normalization.

## 2. Delete common initial rows before taking the hook

Suppose a filling of \(\lambda\), after a row permutation, has
the first \(\min(j,p_\tau)\) rows of the old space in every
height-\(j\) column at \(\tau\). Delete those rows from each
column, obtaining a tail diagram \(\delta\) with heights
\((j-p_\tau)_+\).
There is an integral isometric tensor embedding
\(L:T_\delta\to T_\lambda\) by prepending the leading wedge
to the remaining factors and inserting the fixed unit wedges
in the short columns. It maps the rational Weyl space to the
rational Weyl space: on evaluations this is exactly
\[
 L E_\delta v_\delta(z)
 =E_\lambda v_\lambda(\operatorname{diag}(1_{p_\tau},z_\tau)_\tau)
\]
by (1). The evaluations span and \(E_\lambda\) has an
integral left inverse, hence the induced map on integral Weyl
coordinates is integral.

We also need the polynomial image of this embedding, rather
than only the tensor statement. On an array \(x_\tau\) with
invertible leading \(p_\tau\)-square block, every prefix-filled
minor of height \(j>p_\tau\) is the determinant of that block
times the appropriate minor of its Schur complement.
For \(j\le p_\tau\) it is the fixed leading \(j\)-minor.
Consequently evaluation on \(L T_\delta\) is evaluation on the
tail tensor of the Schur complements, times one factor independent
of the filling. Apply this identity to the integral Weyl vector
of Section 1 for a tail filling. The product of its prefix-filled
minors, multiplied by \(c_\delta\), is a polynomial of an
integral Weyl vector for \(\lambda\), first on the dense open
set of invertible leading blocks, hence as an integral polynomial
identity. Undoing a row permutation uses the integral Schur
matrix of its inverse transpose; signs are units. This proves the
leading-row integrality lemma (LeadingRows.lean 431–end).

## 3. Actual branching operator and its kernel

At each place split the upper column counts \(\kappa=\gamma+\kappa'\):
\(\gamma_j\) columns of height \(j\) lose a box, and \(\kappa'_j\)
keep their boxes. The lower diagram has counts
\(\kappa_{0,j}=\kappa'_j+\gamma_{j+1}\) for \(1\le j<k_\tau\);
the \(\kappa'_{k_\tau}\) kept full-height columns give the
extra determinant power \(d_\tau\). Assume
\(\kappa'_{\tau,j}=0\) for \(j<Q\), where \(Q\) is the
source lower-height cutoff. Define the integral isometric
embedding \(J:T_{\kappa_0}\to T_\kappa\) as follows.
For each shortened column, put the new unit vector first
in the corresponding lower wedge; for each kept column
embed the lower wedge unchanged. Insert the fixed unit
determinant tensors in full-height kept columns and the
fixed new vector in shortened columns of height one.
Reorder the factors as prescribed by the upper diagram.
Use the induced orientation signs in the increasing wedge
basis. All these operations are isometries.

Over the rationals the normalized operator is
\[
 B_* =G_{\kappa_0}^{-1}E_{\kappa_0}^t J^t E_\kappa.
 \tag{3}
\]
It satisfies \(\|B_*\xi\|_{\kappa_0}\le\|\xi\|_\kappa\):
in tensor coordinates (3) is \(J^t\) followed by orthogonal
projection onto the lower Weyl space. In particular this uses
the specified Gram matrices, not coefficient Euclidean norms.
For an invertible block \(\operatorname{diag}(g,s)\), the
contraction \(J^t\) commutes with the old matrix action up
to \(\prod_\tau s_\tau^{\sum_j\gamma_{\tau,j}}\det(g_\tau)^{d_\tau}\).
This holds on each wedge because the decomposition into wedges
with and without the new vector is block invariant.
The orthogonal projection onto the lower Weyl space commutes
with the lower unitary group, hence with the complex general
linear group by Zariski density; equivalently the orthogonal
complement is also a subrepresentation. Thus (3) has the
required equivariance, initially over \(\mathbb C\), then
over every characteristic-zero field after clearing determinant
denominators. Including the upper determinant twist \(e_\tau\)
gives the lower twist \(e_\tau+d_\tau\) and last exponent
\(e_\tau+\sum_j\gamma_{\tau,j}\).

To prove a small integral normalization for (3), write
\(d(x)=\prod_\tau\det(x_\tau)^{d_\tau}\), where \(x_\tau\)
is the square old-rank part of the array.
Let \(f_{\rm br}(y)\) be the upper product of leading minors
with the new row first in the shortened columns and last
in the kept columns. Set
\[
 K(x,y)=f_{\rm br}(\operatorname{diag}(x_\tau^t,1)_\tau\,y).
\]
Cauchy–Binet applied to each wedge factor in (1) gives the
exact polynomial identity
\[
 d(x)\,{\rm toPoly}_{\kappa_0}(B_*v_\kappa(y))(x)=K(x,y).
 \tag{4}
\]
For kept determinant columns this is the factor \(d(x)\);
for a shortened column it is expansion of the wedge pairing
with the new vector placed first, and for the other columns
it is the ordinary minor pairing. This is precisely the
branchKernel identity, with its determinant power.
In particular \(B_*\ne0\), because at \(x=1\), \(K=f_{\rm br}\)
is a nonzero product of minors.

## 4. Integral normalization with the correct tail count

Set \(p_\tau=\min(\max(Q-1,0),k_\tau-1)\).
Clear the new row of the generic array \(Y\) except in its
first column by integral column operations: write \(t_\tau\)
for its first entry, replace every column by \(t_\tau\)
times that column, subtracting \(Y_{\rm new,j}\) times
the original column zero when \(j>0\).
The resulting \(Y'\) has new row \((t_\tau^2,0,\ldots)\).
Every height-\(j\) flag minor is multiplied by \(t_\tau^j\)
since the triangular transformation of its first \(j\)
columns has diagonal \(t_\tau\). In particular
\[
 K(x,Y')=M(Y)K(x,Y),\qquad
 M(Y)=\prod_\tau t_\tau^{\sum_j j\kappa_{\tau,j}}.
 \tag{5}
\]
There is no localization in these operations.

At \(Y'\), expansion in the new row expresses \(K(x,Y')/d(x)\)
as an integral scalar in \(\mathbb Z[Y]\) times the following
lower polynomial evaluated at \(g_\tau^t x_\tau\), where
\(g_\tau\) is the old square part of \(Y'\):
for each lower height \(j\), the shortened columns have
row set \(\{1,\ldots,j\}\) and the kept columns row set
\(\{0,\ldots,j-1\}\) (zero-based), both using the first \(j\)
columns of the argument. This follows by transposing the
minors: expansion of a shortened height-\(j+1\) minor uses
old columns \(1,\ldots,j\), whereas kept minors use columns
\(0,\ldots,j-1\). A shortened height-one column contributes
only \(t_\tau^2\); a kept determinant column contributes
\(\det(g_\tau)\det(x_\tau)\).
The scalar is therefore the product of powers of \(t_\tau^2\)
and \(\det g_\tau\).

All columns of positive height \(j\le p_\tau\) are shortened
because \(j<Q\). Every larger column contains the common rows
\(1,\ldots,p_\tau\). Reorder the rows so these are the leading
ones, in that order. The prefix lemma of Section 2 applies to
this filling, with tail size
\[
 D=\sum_\tau\sum_{1\le j<k_\tau}
          (j-p_\tau)_+\kappa_{0,\tau,j}.
\]
Let \(c=c_\delta\) be the hook integer of its tail diagram.
The lower polynomial times \(c\) is the polynomial of an
integral lower Weyl vector. Substitution \(g_\tau^t x_\tau\)
acts via the integral Schur matrix of \(g_\tau\), a polynomial
matrix defined even for singular \(g_\tau\); scalar multiplication
by the integral factor above is also integral. Thus for some
vector \(\eta(Y)\) with entries in \(\mathbb Z[Y]\),
\[
 cK(x,Y')=d(x){\rm toPoly}_{\kappa_0}(\eta(Y))(x).
\]
By (4)–(5), cancellation of the nonzero polynomial \(d(x)\)
and injectivity of toPoly give
\[
 M(Y)cB_*v_\kappa(Y)=\eta(Y).
\]
Since \(M(Y)\) is a monomial with coefficient one, multiplication
by it cannot clear rational coefficient denominators. Hence
\(cB_*v_\kappa(Y)\) has integral polynomial entries. The
integral coefficient-span property of the standard basis in
Section 1 implies \(B=cB_*\) is an integer matrix.

The tail size \(D\) is bounded by the number of boxes in lower
columns of height \(j\ge Q\). Thus for every integer bound \(L\)
on that latter number,
\[
 1\le c\le D^{3D}\le L^{3L},\qquad
 \|B\xi\|_{\kappa_0}^2\le c^2\|\xi\|_\kappa^2.
 \tag{6}
\]
Zero exponents use \(0^0=1\). Equation (2) even allows the
factorial bound for the actual flattened diagram. The nonzero
map \(B\) spans all equivariant maps by the classical
multiplicity-one \(\mathrm{GL}_{k+1}\) to
\(\mathrm{GL}_{k}\times\mathrm{GL}_1\) branching rule
(the same rule cited in the source IntegralMap.lean;
alternatively its spansBranchingMaps_of_equivariant).
Unitary equivariance is equivalent here by Zariski density.
Equations (3), (4), (6) together with the determinant-twist
calculation establish all three clauses of
exists_branching_matrix in IntegralMap.lean 472–end.

This proves the quantitative local branching normalization in
the source's Weyl lattices. It does not supply the global
nonstandard Weil transport or the common theta analytic bounds;
the terminal gauge calculation may now use the same bounded
matrix. This is a conventional reconstruction, using integral
straightening and the classical characteristic-zero branching
rule. No new Lean replay is asserted.
