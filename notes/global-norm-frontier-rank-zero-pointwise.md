# The actual rank-zero weighted orbital theorem

## Classification and exact advance

**Closed obligation:** the original `TheoremBPrimePointwise`, with all
its representative and measure quantifiers, for the specialization
`D.R.rS = 0`.  For every original point with nonzero Gram discriminant,
the prescribed orbital integral satisfies

\[
\operatorname{ptWeight}\,\operatorname{orbSq}
\le b^4\max\{1,G^{-1}\}\,\operatorname{jNorm2}.
\]

For a representable point the discriminant is positive, and the stronger
right side `b^4/G * jNorm2` holds.  This is an actual uniform point
evaluation estimate for the source function, not merely an almost
everywhere estimate or a conditional regularity lemma.  It implies the
source `BpIneq` with `m=2`, `Cb>=1`, and the previously selected `Cg>=10^6`.
No whole W06/W08 node is declared closed.  Ordinary RH does not force this
rank-zero specialization; auxiliary rank, dimensions and fields remain
moving parameters in the global construction.

## Direct argument

At rank zero the source unipotent group is trivial.  Every point is one
nonzero scalar block.  Its root pattern is empty, its original unipotent
root stabilizer is `{1}`, the root measure is exactly `dirac(1)`, and the
Weil quotient identity forces the quotient measure to be `pairMeas`.
The orbital integral is therefore exactly the compact average `JF`, with
the original factor `kappa_N^2`.  No compact-stabilizer volume is divided
out.  All representatives in a fixed positive-discriminant fiber have
the same Hilbert--Schmidt norm.

After moving the two negative vectors to the last coordinate, the right
`U(k)` type together with the discrete-series central character fixes a
type for the full maximal compact `U(k) x U(1)`.  The central weight is
`sum(lambda)-sum(u')`; the Casimir identity gives the actual derivative
energy bound

\[
\sum_Y\|R_YJF\|_2^2\le b^4\|JF\|_2^2.
\]

Here `Y` is a Hilbert--Schmidt orthonormal real Lie-algebra basis.  There
is no compact-type dimension factor and no unproved boundedness claim
about a unipotent period map.

Writing `|zeta|=sqrt(TT') cosh(t)`, the exact source norm is

\[
2\pi(TT')^k\int_0^\infty
 (\sinh t)^{2k-1}\cosh t\,\|JF(a_t)\|_{HS}^2\,dt.
\]

An elementary Hilbert-valued Sobolev estimate on the interval of radius
`tanh(t)/(8k)` supplies the pointwise bound.  The original Haar constant
cancels only in the derivative-energy comparison.  The planar Jacobian,
`2*pi`, all powers of `TT'`, the original density and `kappa_N` are
retained.  No lower-dimensional relevant strata with `G != 0` remain
at rank zero.

## Source and verification scope

Pinned source: `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The checker authenticates the exact declaration excerpts against the
source atlas and records full-file and excerpt hashes.  The human proof
is in `paper/shared/global-norm-frontier-rank-zero-pointwise.tex`.
It uses the previously proved terminal Haar integration formula and
Casimir calculation, restating the normalizations needed here.  Exact
symbolic tests check the boost, Jacobian, energy-polynomial domination
and source budget.  Numerical interval checks are only diagnostic; the
all-parameter weight comparison and Sobolev argument are proved in TeX.
No Lean build is asserted.

## Remaining frontier

The next attack must handle the actual partial-head kernel for positive
unipotent rank.  The terminal restriction cannot silently be replaced
by a single `U(k,1)` discrete series with bounded parameter.  The kernel's
root-stabilizer quotient, density and gauge factors and its moving
representation spectrum must be retained.  The rank-zero theorem is a
complete base case and a possible terminal step of such a construction;
it does not by itself supply the higher-rank kernel Fourier bound,
lower-stratum comparisons, rational-return sum or global Gram defects.
