# Actual pointwise big-cell convergence and coefficient expansions

## Closed obligations

The original two-sided Bessel integral is now proved absolutely
convergent and continuous at every regular big-cell point.
This identifies its prescribed pointwise values with the L2
representatives used in the preceding higher-moment proof.

Consequently the original BesselExpansionNearParameter and
BesselExpansionCoefficientSum interfaces are supplied, with
their every-big-cell-point equality, finite support
||ν||1≤(r+1)|α|, and sum bound b^(Cb m² |α|).
The constants remain Cq≥200, Cg≥10^6, Cb≥Ch+5; both character
scales κ=1,a and the original real gap reserve are unchanged.
No whole W06 or W08 node is declared closed.

## Exact properness estimate

Put n=2r+k+1 and use blocks (1^r,k+1,1^r).
The prescribed unipotent group is upper block-unitriangular.
The outer Weyl element w exchanges the paired isotropic flags,
fixes the middle block, and conjugates N to a lower group.
The original big-cell matrix is

\[
 wD(c,\mu),\quad
 D(c,\mu)=\operatorname{diag}(c_0,\ldots,c_{r-1},
      \mu,\bar c_{r-1}^{-1},\ldots,\bar c_0^{-1}),
 \qquad\mu\in U(k,1).
\]

For X=nL^-1 wD nR, the decomposition w^-1 X=LDU has
L=w^-1 nL^-1 w and U=nR.
Only the leading block boundaries
1,…,r and r+k+1,…,n−1 are used. Their determinants equal
the products of the corresponding diagonal blocks of D.
Because |det μ|=1, they are bounded away from zero when the
nonzero c coordinates stay in a compact set.

Cramer's rule expresses each off-diagonal entry of L or U as
a determinant of size at most n−1 divided by such a boundary
determinant. Hadamard's inequality gives

\[
 \max(\|n_L\|_{\mathrm{HS}},\|n_R\|_{\mathrm{HS}})
      \le C\|X\|_{\mathrm{HS}}^{n-1}.
\]

The equality of the norms of nL and its inverse follows from
Hpk being a unitary Hermitian involution. The two compact
stabilizers only change C by a fixed finite conjugation factor.
No measure has been pushed or renormalized.

Internal scalar pivots inside the middle block must not be used:
they can vanish even when the block is unitary and invertible.
The exact checker includes this case.

## Convergence and continuity

Each original unipotent Haar ball of matrix radius R has volume
at most C R^(2n²), by the existing ambient packing proof.
The product has growth at most R^(4n²).
Thus coefficient decay ||F(g)||≤C_F ||g||^−A is integrable on
every such orbit if A>4n²(n−1), uniformly on compact sets of
the nonzero c parameters.

The actual source gap gives

\[
 A=\frac{h}{32\sqrt{2r+2}}-1
 \ge\frac{C_g}{2}(r+1)^4(3(r+1)n^2+n^3)-1
 >4n^2(n-1).
\]

The original IsSection explicitly requires smoothness on
|ζ|²>TT′. Dominated convergence therefore proves continuity
of the actual orbital integral for every such section.
The constants used here may depend on the compact parameter
set and on the chosen coefficient; they are used only for
convergence and do not enter the uniform norm exponent.

The exact radial measure has strictly positive density at
every point of the regular big cell. Hence a continuous
difference which vanishes almost everywhere is zero everywhere.
This upgrades the finite expansions, including zero-image
representations, to precisely the original pointwise interface.

## Remaining pointwise frontier

Absolute convergence and continuity do not by themselves bound a
point evaluation by b^(C m^4) times the global Jacquet norm.
The source TBB kernel/Fourier inequality remains to be supplied.
Its lower-dimensional relevant strata also need their exact
stabilizer measures and signed comparisons: some boundary minors
in the Gauss estimate can vanish there.

Those strata and prescribed rational points cannot be discarded
as ambient Haar-null sets. The new theorem resolves the regular
big-cell identification issue only; it does not silently weaken
the later arithmetic sum.

Full proof: paper/shared/global-norm-frontier-big-cell-continuity.tex.
Run python3 scripts/check_global_norm_frontier_big_cell_continuity.py --offline.
