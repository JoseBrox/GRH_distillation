# Exact class-number certificates on five auxiliary quadratic hosts

25 November 2026. Actual finite arithmetic certificates for the
[pure-cubic descent](pure-cubic-selmer-descent.md). All checks
below are unconditional integer computations; no GRH-based
class-group algorithm is used. They cover five concrete quadratic
host factors, not the full growing high-dyadic family.

## 1. Exact order and finite generating set

Write C=Q(alpha), alpha^3=2, B_q=Q(sqrt(-q)) for a prime q>3
congruent to 3 modulo 4, and L_q=C B_q. Set
beta=(1+sqrt(-q))/2 and m=(q+1)/4. The ordered basis used
in the certificate is


```math
1,\alpha,\alpha^2,\beta,\alpha\beta,\alpha^2\beta,
 \qquad \alpha^3=2,\quad\beta^2-\beta+m=0.
```


The power basis of C is maximal. Its discriminant is -108,
so only primes 2 and 3 need checking. At 2 the polynomial
X^3-2 is Eisenstein and alpha is a uniformizer. At 3
alpha+1 satisfies X^3-3X^2+3X-3, also Eisenstein, and is a
uniformizer. In either local field a sum of the powers
0,1,2 of the uniformizer with rational local coefficients
has term valuations distinct modulo three, so integrality
forces each coefficient integral. This verifies maximality
at both primes. The quadratic discriminant is -q, prime
to 108. At each rational prime at least one of the two
integer rings is therefore etale over the local integers;
the tensor of that ring with the other local integer
ring is a product of unramified extensions of DVRs,
hence integrally closed. Thus the product basis above is
the full integer ring. The product discriminant is


```math
D_{L_q}=-108^2 q^3 .
```


The degree-six field is totally imaginary with three
complex pairs. Minkowski gives an integral ideal in
each ideal class with norm at most


```math
M_q=(4/\pi)^3(6!/6^6)\,108 q^{3/2}.
```


The verifier uses the rational upper bound obtained from
pi>157/50 and sqrt(q)<(floor(sqrt(10^12 q))+1)/10^6.
Taking its integer floor B is safe because all ideal
norms are integers. The prime ideals of norm at most B
therefore generate the class group.

The verifier enumerates these ideals exactly. At each
rational prime p<=B, take all distinct irreducible factors
g of X^3-2 modulo p. The degree is at most three, so
exhaustive extraction of linear roots, followed by any
remaining irreducible factor, suffices, including repeated
factors at ramified primes. For each factor of degree f
with p^f<=B, factor beta's quadratic polynomial over
the explicit residue field F_p[X]/g by enumerating its
p^f elements. Every root gives one prime ideal of norm
p^f. If there is no root the quadratic is irreducible
and gives one prime of norm p^(2f), retained if within B.
These are all maximal ideals of the product order modulo
p, since its residue algebra is obtained by those
factorizations. Multiplicities of ramified factors do
not affect this enumeration. All computations are in
the explicit maximal order, so no index-at-p exception
to Dedekind factorization of a primitive power basis
is needed.

Each prime ideal is represented by the HNF basis of the
kernel of the corresponding reduction map. The verifier
checks the index p^f, and reconstructs integral
multiplication matrices directly in the product basis.

## 2. Principal relations and their verification

The [certificate](../certificates/pure-cubic-class-certificates.json)
contains one list of integral elements for each field,
with coordinates in the indicated order. It is enough to
store the elements: the verifier reconstructs the candidate
prime-ideal exponents from their norms and residue tests.

For each element x it checks the exact ideal identity


```math
(x)=\prod_i\mathfrak P_i^{a_i}
```


by multiplying the integer ideal lattices in the maximal
order, computing HNFs, and comparing with the HNF of
the multiplication matrix of x. The ideal norm from the
right side must equal the absolute determinant of that
matrix and the independently calculated norm of x
(using norm to C and then the cubic norm formula).
Thus a heuristic candidate factorization, including a
possible missing large prime ideal, cannot be accepted
as a relation merely on the basis of a numerical norm.

With n enumerated prime generators, the n certified
relation vectors form a square integer matrix M.
Its nonzero absolute determinant is the index of the
relation sublattice in Z^n. The quotient surjects
onto the class group, so its order is a certified
*multiple* of the class number, not necessarily
the class number itself. No analytic class-number
bound or saturation theorem is needed.

## 3. Completed computations

The exact verifier was run locally using SymPy 1.14.0.
It verifies these five certificates (368 actual principal
relations and five exact nonzero determinants):

| q | Field discriminant | Minkowski integer upper bound | Generators / independent relations | Certified multiple of h(L_q) |
|---:|---:|---:|---:|---:|
| 7 | -4000752 | 63 | 20 | 18 |
| 11 | -15524784 | 125 | 29 | 54 |
| 19 | -80003376 | 285 | 68 | 108 |
| 23 | -141915888 | 380 | 82 | 288 |
| 43 | -927369648 | 971 | 169 | 1620 |

Reproduce the check from the repository root with

    python hecke/scripts/verify_pure_cubic_class_certificates.py

The proof of the finite generating set is above; the
verifier checks every relation and the determinant using
exact HNFs and integer arithmetic. The stored witnesses
were found by a deterministic seeded search among small
integer coefficient vectors and rational integers; the
verification does not use that search or its probability
of success. The displayed multiples have no prime
divisor greater than five. In particular h(L_q) is prime
to every ell>3 congruent to 1 modulo 3.

An attempted general-purpose round-two calculation in
SymPy on the primitive polynomial of L_11 produced an
invalid integral order in this environment. It was not
used in any certificate. PARI/GP was unavailable, and
package installation failed at DNS resolution. This is
why the verifier uses the independently proved maximal
order and elementary finite-field/ideal arithmetic.
The first combined larger run also timed out; each
displayed certificate was then generated and checked
separately, and all five certificates were then run successfully in one exact
verification. The Git blob of the verified combined witness data is
ce5b76969829054c0d19ff7723cc85e7036dadf9, also checked against the
committed repository data.

## 4. Consequences for the actual coefficient sectors

For any displayed q take rho=chi_{-q}, or its inverse
(which is the same character). The fields B_q are actual
quadratic host factors of the cubic comparison. In
particular q=19 has the strengthened one-sign condition
q=3 mod 8 and 3-cycle Frobenius in K (2^6=7 mod 19);
q=7 has q=7 mod 16 and 3-cycle Frobenius. The other
three fields meet the indicated individual progression
conditions of the original auxiliary scheme. These
are small arithmetic examples, not choices asserted
to satisfy the asymptotic companion-selection sizes.

For every ell>3, ell=1 mod 3, ell!=q with 3-cycle
Frobenius in K, the nontrivial cubic class-group
components of K B_q at ell are zero at the initial layer.
Indeed the prime-to-ell S3 decomposition over the
quadratic base gives the standard multiplicity from
Cl(C B_q){ell} minus Cl(B_q){ell}; the former is zero
by the certificate. This also follows by taking the
C2-invariants of the standard component, one copy of
each nontrivial cubic eigenspace. At ell these cubic
extensions over F B_q are inert, because the residue
degrees of the quadratic base change divide two.
The earlier exact cyclotomic control theorem, which
does not require adjoining mu_ell when the tame
character is trivial, now gives zero cubic module
in the pro-ell tower of K B_q. Thus for both cubic
signs and every positive weight divisible by ell-1,


```math
S_F((E/O)(\varepsilon^{-e}\rho^{-1}\lambda))=0.
```


This improves the earlier one-prime test: it works
whether or not B_q itself is inert at ell. For example
ell=13 works for q=7,11,19,23,43 (except any equality
of q with ell, which does not occur here), because
13 is a 3-cycle coefficient prime, and the certified
multiples are all prime to 13.

At a split cubic coefficient prime ell=1 mod 3,
the same conclusion holds when rho(ell)=-1, since
then the actual finite character is nontrivial on
the decomposition group. Apply the
[characterwise strict-control theorem](cubic-characterwise-strict-control.md)
to L_0=K B_q and its cyclotomic pro-ell tower:
the ordinary class component is zero by the same
certificate, and the actual local correction s_theta
is zero by the nontrivial Frobenius. Again the weights
are divisible by ell-1. We do not claim this for
coefficient primes where the local character is trivial.

This gives infinite sets of vanishing coefficient
primes and weights for each of five certified fixed
quadratic sectors. It does not certify the whole tame
cyclotomic splitting field K B_q(mu_ell), or the
higher dyadic layers of the moving host. In particular
none of these quadratic-character examples is a
high-dyadic frame with 2^b>=24 ell(ell+1)^2.
The uniform high-dyadic class-rank problem remains
open. No numerical zero test or new full proof-map
node is claimed.
