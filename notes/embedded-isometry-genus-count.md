# The original embedded-isometry genus mean

**Classification: closed obligation — the full quantitative genus
mean of the original embedded triples.** This supplies
DiscNResNeZero.main with its stated constants. The weighted term-to-triple correspondence and the fixed-label global count are now also supplied; the complete W08 node remains open.

The definitions and complete proofs are in
[the manuscript section](../paper/shared/embedded-isometry-genus-count.tex).

## The exact arithmetic estimate

Let E/F be the original CM extension, unramified at all finite
places, [E:Q] = 2f, rho = rd(E) = 2 vInv(E) >= 2, and
c = 1 + log_2(2f). For rank k >= 3 and a rational prime T
splitting completely in E, let L0 be integral positive definite
with L0-dual/L0 isomorphic to O_E/T O_E. Set

    D = T^(2f),  Mb = (20 f rho^2)^(2f(6+c)).

For g >= 2, j >= 0, and x,x' >= 1, set X = xx' and Y = X D^2.
The genus-weighted number of original embedded triples is at most

    Mass(L0) X^(k/2) Y^(6j+10+4c)
      [1 + Mb rho^f sum_(s=1)^(k-1)
             ((32/g)^(kf) (4kf)^(4f) Y^7)^s
         + ((2/g)^(kf) (4kf)^(4f) D X)^k].

The embedded datum consists of an integral lattice of the original
discriminant and the actual graph of an isometry modulo g to the
base lattice. Its fixed lattice has the specified index and quotient
generator bound. A triple includes the original compatible rational
isometry between its two data. None of these objects is replaced.

## The decisive estimates

For a compatible isometry eta, write U = Fix(eta), let s be its
codimension, and let A be the common intersection with U of the
two fixed lattices. Compatibility of the original graphs gives

    h((eta-1)F', F) is contained in g O_E.

Projection to U-perpendicular and the integral index in the dual
lattice give

    discr(A) <= (2/g)^(2sf) D x x'.

The factor 2 comes from the norm of a unitary isometry minus the
identity at every embedding. The full norm exponent 2sf, and the
exact normalized covolume, are retained.

For a fixed lattice F, the embedded datum can be encoded by its
overlattice L/F inside F-dual/F and the homomorphism

    Lambda/F -> F-dual/L,
    y -> (y'-y)/g modulo L.

The original mod-g isometry makes this well defined, and the
homomorphism recovers the graph. The dual quotient has at most
2j+1 generators. This proves the source bound (xD)^(3(2j+1))
for the fiber, independently of g.

Prescribed intersections are counted by splitting a saturated
submodule of the base lattice. Minkowski's classical finite-group
bound controls the remaining isometries by (4sf)^(4sf).
The [proved primitive-sublattice mean](primitive-sublattice-genus-mean.md)
then cancels the discriminant powers exactly. Summing the fixed
spaces gives the displayed original genus estimate.

## Application to the original terms

The [fixed-row theorem](flag-row-congruence.md) supplies the weighted term-to-triple inequality PerRowC, and the [global fixed-label theorem](flag-global-pair-count.md) combines it with the genus mean and the finite parameter sum to prove PairsP. The full amplitude and return-series estimates remain separate.

## Verification

Run:

    python scripts/embedded-isometry-genus-count-check.py --offline

The certificate authenticates the source definitions and consumers,
records the primary statement of Minkowski's theorem, checks the
exact exponent cancellations, and checks a sharp congruence example
in the finite-unramified CM extension Q(zeta_12)/Q(sqrt(3)).
The field example is a diagnostic of the general theorem, not an
assertion that it is an auxiliary field in the original RH family.
No Lean build or full return-series bound is claimed.
