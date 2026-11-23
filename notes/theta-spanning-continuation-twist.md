# Actual unramified frames and integral parallel twists

Classification: **closed obligations**, independently reviewed.
These are original arithmetic inputs to the shifted short spanning
family, not completion of W06 or W10.

The proof is `paper/shared/theta-spanning-continuation-twist.tex`.

## Actual unramified-point construction

For every original component Z and every coefficient-field place v
outside B=prime divisors of 2*d*disc(E)*M, the literal PEL datum has
maximal coefficient order, perfect alternating lattice, and level
prime to the residue characteristic. It is type A, so Lan's I_bad=1.
These are precisely the good-prime hypotheses of Lan 1.4.1.1 and
the maximal-order hypothesis in 1.4.3.10.

Lan 6.4.1.1 gives a proper smooth toroidal model with relative
normal-crossings boundary. The original half/full-level completion
and prescribed cyclotomic fibre are finite etale at this prime.
After base change to the original completion K_v, the selected
geometrically integral generic component extends as an open/closed
smooth proper component, via its finite etale Stein algebra.
Its special fibre has a point off the relative boundary. Smooth
Hensel lifting over a finite unramified extension gives an actual
abelian integral point on the same component.

The original tangent eigenlattices split freely because disc(E) is
a unit, and the primitive principal theta line has a rank-one
base-change-compatible section module. Choosing their integral
bases gives an original integral frame. The test-frame clause is
supplied by the finite-type framed moduli chart. The exact source
`IntFr.IsAlg` is `T.FinRes`: it asks for finite residue field, not
for algebraicity of a complete field over the number field. This
condition is retained. The valuation index is exactly one.

Thus the original UnramPts(B) holds without the source's separate
construction of unramified CM elliptic curves.

## Actual integral parallel twist

For an integer shift w, take the product of the uncorrected actual
flat determinant generators s_tau^(-w_tau). Its original weight
is parWt(w), theta tag zero. Its constant finite values rho_v are
integers away from B, by evaluation at the index-one point above.
Its degree is exactly -(p-q)*P_E*sum(w_tau)/2.

Minkowski applied to the fractional ideal with exponents ceil(-rho_v)
produces a nonzero scalar in the original coefficient field. The
resulting original twist is integral at every integral test frame,
and its constant complex log norm is at most

    |p-q|*|P_E|/2 * sum|w_tau|
      + (1/2)*log rd(K) + sum_{ell in B}log ell + 1.

The rounding cost is the sum over rational bad primes, not a cost
multiplied by [K:Q]. The proof retains the field degree in ideal
norms and in the lattice covolume. Under the original numerical
bounds this is at most

    (3/2)*r*Lb*sum|w_tau| + (1/2)*log rd(K) + 40*f*Lb + 1.

This direct geometric construction does not need `Nonempty KeySec`.
The source's helper uses that auxiliary input to transfer its cusp
predicates, while the actual generic determinant unit and its
inverse preserve the original cusp spaces directly.

The finite correction in FlatSec is still present in the preceding
flat-degree theorem. Here the uncorrected actual frame degree is
used explicitly for the fractional-ideal construction; no actual
finite valuation or metric has been changed.

## Remaining decisive shift

The raw theta family has a positive theta tag. Removing that tag
requires the original key-weight line, with controlled original
integral valuations, including primes above 2. A fourth determinant
power theorem valid only after inverting 2 does not settle this.
This is now the direct target for producing h0 and hsh from the
actual short theta family.

Run `python3 scripts/theta-spanning-continuation-twist.py --offline`.
