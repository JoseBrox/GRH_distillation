# Integral transport of the original flag lattices

**Classification: closed obligation — the original normal-form integral
transport and the top and central stabilizer bounds.** This supplies an
arithmetic input to W08; it does not complete that proof-map node.

The [manuscript section](../paper/shared/flag-lattice-transport.tex)
contains the full proof, including projective modules and primes above 2.
It continues the actual middle stabilizer theorem.

## Exact statement and original objects

Let Lambda be an original admissible unimodular lattice for a normal
form of flag length r and paired length j. The two flags have the actual
successive leading ideals, not an assumed literal containment of every
weighted frame vector. Let P0 be the source's rank-(2r+1) reference
module. If a_l is the normalized nonzero leading-minor ideal, put

    c = (T) product_l a_l conjugate(a_l),
    Norm(c) = (D_b N_T)^2.

There is an element of the SAME common flag unipotent group carrying
Lambda to a split lattice whose intersection with P0's vector space is
between c^(12r+50) P0 and c^(-12r-50) P0. Once split, all further
transformations fix the definite complement pointwise. The proof
actually gives exponent 6r+10, but retains the original sufficient
exponent in its downstream applications.

For a split lattice satisfying this inclusion with exponent e, each
of the top and central stabilizer ratios is bounded by

    Norm(c)^((3e+11)(2r+1)^2).

Together with the proved middle quotient, this gives the original full
stabilizer weight bound, with the original integral defect b retained.

## Construction and decisive interfaces

Projective splitting of the common isotropic quotient is realized by an
explicit unitary triangular matrix. Both paired flag lattices are then
controlled by one common isometry: the two block changes are related by
the inverse adjoint for their actual signed antidiagonal pairing.
Cramer's rule at block endpoints and a Schur complement bound every
needed denominator by the original normalized minors.

The common isotropic directions are put in their prescribed ideal
positions by one triangular map and its inverse adjoint. A final
Eichler transformation handles the last vector of norm -T. Projective
extension of the integral conjugate-dual functional then constructs
the missing dual directions. An explicit skew-adjoint correction
removes the remaining unrestricted part.

The ordered product for the top stabilizer lift is

    n_(B A^(-1)) diag(D,A,D^(-*)),

so its induced action on the actual degenerate flag span is exactly
the prescribed block matrix. Deep integral congruence makes this lift
stabilize Lambda. The central group is normal in the same common
unipotent group, because that group sends W into W+I and preserves V0.

The source's ordered block definition is Pt.mat, with its column signs
in NF.pair; the reference P0 is literally the four ideal-weighted
summands in NormalFormDualOrthogonalLast, lines 72--75. The stronger
splitting constructed here implies the original Split condition.

## Verification and remaining frontier

Run:

    python scripts/flag-lattice-transport-check.py --offline

The certificate authenticates the exact source interfaces and checks
simultaneous paired-block changes, Cramer and Schur identities, including
j=0, j=r and r=1. Exact calculations over Q(zeta_12) check the unitary
graph splitting, ordered top lift and skew correction. These diagnostics
support the written general proofs; they are not a Lean build.

The [weighted lattice sum](weighted-flag-lattice-sum.md) uses this
construction and the original stabilizer weight. The remaining term
frontier is the assignment to adapted normal forms, its precise class
equivalence and the reciprocal row-automorphism multiplicity.
