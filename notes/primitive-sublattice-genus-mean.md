# The primitive-sublattice genus mean

**Classification: closed obligation — the original quantitative
primitive-sublattice genus mean, with its actual reference mass,
field parameter, and growing-rank exponents.** The fixed-label pair
count and the complete W08 node remain open.

The complete statements and proofs are in
[the manuscript section](../paper/shared/primitive-sublattice-genus-mean.tex),
using [the exact mass calculations](maximal-hermitian-mass.md).

## The theorem actually supplied

Let E/F be the original CM extension unramified at every finite
place, [E:Q] = 2f, rho = rd(E) = 2 vInv(E) >= 2, and
c = 1 + log_2(2f). Let k >= 3, 1 <= s < k, and let T be a
rational prime splitting completely in E. For the original
positive definite integral lattice L0 with
L0-dual/L0 isomorphic to O_E/T O_E, set

    D0 = T^(2f),
    Mb = (20 f rho^2)^(2f(6+c)).

For every positive integer n, the sum over the genus of L0 of
the number of primitive rank-(k-s) sublattices of discriminant n,
weighted by 1/|Aut L|, is at most

    Mass(L0) Mb rho^f 16^(skf)
      (n/D0)^(k/2) (n D0)^(5s+5+2c).

This is precisely MeanPrimitiveSublatticesGenusDefiniteLattice.main,
lines 158--198 of the pinned source. The root discriminant and
the inverse-volume parameter are matched by the exact definition
in Formalism.HermitianLattices.StatementMass, lines 25--28.

## The arithmetic argument

For a fixed positive definite Hermitian space of rank a, all
maximal integral lattices form one genus. Their local determinant
parities fix the nonunimodular prime set. Counting pairs
L contained in a maximal lattice therefore has only one maximal
discriminant and one index. It gives

    sum_(L in fixed space, discr L=n) 1/|Aut L|
       <= C(E,a) n^((a+log_2(2f))/2).

No sum over different rational spaces is hidden here. Such a sum
occurs separately when classifying the rational primitive span.
Its possible inert determinant parities form at most
n^(1+log_2(2f)) patterns, by ideal counting and the Hermitian
local-to-global principle.

For a fixed orthogonal decomposition U plus W, put A = L intersect U
and B = L intersect W. The extension L/(A plus B) is a graph between
submodules of their finite discriminant modules. A submodule of
B-dual/B has at most dim(W) generators over O_E; the local cyclic
decompositions combine by the Chinese remainder theorem. Thus
there are at most (discr A times discr B)^dim(W) graphs.
The identity discr L = discr A times discr B divided by the square
of the extension index gives discr B <= discr A times discr L.
Orbit--stabilizer keeps every reciprocal automorphism weight.
This graph argument works even without a cyclic dual quotient.

The remaining normalization is also proved. The rank-one mass
is at most 2^f h_E: for a fixed ideal class the possible Hermitian
classes inject into O_F-units modulo norms of O_E-units, whose
order is at most 2^f. Minkowski and the ideal coefficient bound
give h_E <= rho^(f(1+log_2(2f))). Explicit factorial and Euler
factors then give

    C(E,k-s) C(E,s) <= C(E,k) Mb rho^f 16^(skf).

The exact cyclic-discriminant mass is
C(E,k)((T^k-1)/(T-1))^f. Substituting it yields the stated
normalized genus mean. This proof needs no separate rank-two
class-number bound and no replacement of the arithmetic lattices.

## The next frontier

The next original arithmetic theorem is the genus mean of triples
of two embedded data and an isometry between them:
DiscNResNeZero.main, lines 312--430. Its proof separates the
isometry by the dimension of its fixed subspace. The primitive
sublattice mean needed for the intermediate fixed-space dimensions
is now supplied; the counts of isometries with a prescribed fixed
space and with no fixed vector still need complete reconstruction.

After those estimates, the original weighted row-to-lattice
correspondence must deliver the fixed-label pair bound PairsP.
The new theorem is not itself a bound on all return multiplicities,
and it does not assert the full zero-Gram operator estimate.

## Verification

Run:

    python scripts/primitive-sublattice-genus-mean-check.py --offline

The certificate authenticates the exact source interfaces, checks
the mass and exponent identities symbolically, and checks the
finite-module generator bound on a nonsemisimple example.
The general argument is the written proof. The local-to-global
principle, Minkowski bound, Dirichlet unit theorem, and global
mass formula are cited classical theorems. No Lean build is claimed.
