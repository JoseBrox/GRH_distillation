# The actual Frobenius spectrum and fixed-field Selmer product

**Classification: closed original Frobenius-spectrum, fixed-field
orbit-bound and Case I obligations, independently reviewed.**
The complete proof is in
[the shared section](../paper/shared/selmer-support-continuation-spectrum.tex).
The stronger estimate uniform in a varying imaginary quadratic field is
not asserted. The complete W04 obligation remains open.

## Frontier theorem discharged

Fix an imaginary quadratic field `K` before choosing constants. For every
positive twist `e`, modulus `N`, and auxiliary rational prime
`p >= 7` prime to `N disc(K)`, construct one finite Galois-stable indexed
multiset of Frobenius traces that classifies every pairwise nonisomorphic
family of the source's actual admissible rank-three and rank-two-plus-line
representations, for all coefficient primes `ell != 2,p` simultaneously.
Its cardinality is bounded by a polynomial in `N(e+1)`, every trace has
complex absolute value at most three, and multiplication by `Q^e`, with
`Q = p^f` and `f <= 2`, makes it integral.

The existing resultant construction then supplies one nonzero integer
whose normalized valuations bound the full sum of congruence valuations
for every character in the orbit. Combining this with the actual
one-character integral comparison proves the original `PropGK` and
`CorGK`, including the factor two, coefficient ramification normalization,
and the exceptional coefficient prime handled by a second auxiliary prime.

This is the full original `CongruenceNumberRankThree` statement. It does
not assert the source's more general `CountK` or `CountQ` for arbitrary
rank or infinitesimal character.

## Decisive arithmetic steps

1. **The original coefficient-prime flag controls monodromy.** Each
   successive positive cyclotomic difference has negative Hodge--Tate
   weight. Bloch--Kato's de Rham dimension formula and local duality give
   `H^1 = H_f^1` exactly when the original character ratio is not
   cyclotomic. In rank three the differences are `e` and `2e`; at `e=1`
   the original disjunction supplies either this nonresonance or potential
   crystallinity directly. No small-weight exception is discarded.

2. **Full local compatibility gives a common conductor.** Finite inertia
   characters factoring through `F(mu_M)` have conductor exponent at most
   `v(M)`, by local reciprocity and the norm on principal units. Their
   direct sum has conductor at most `n v(M)`. This applies also at the
   coefficient prime. Caraiani supplies full rank-three compatibility;
   Saito's theorem together with his 2000 weight-monodromy supplement
   supplies full rank-two compatibility. The monodromy operator is retained.
   The corrected local new-vector theorem puts the same rank-three
   representations at principal level `N^3`, and the same rank-two
   newforms at level dividing `(N |disc(K)|)^2`.

3. **Finite cell complexes count the actual spectrum.** At a fixed neat
   level the Borel--Serre compactification has finitely many cells. The
   rank-three coefficient representation has highest weight
   `(e-1,0,1-e)` at both embeddings and dimension `e^6`. A finite covering
   has degree at most `N^54`, giving `C_K N^54 e^6` representations.
   A modular-curve cohomology bound handles the rank-two forms. These
   counts include all conjugates and keep repeated traces. They count
   representations, not just distinct trace values.

4. **The normalization is integral.** At primes different from the
   auxiliary prime, a stable lattice supplies integrality. At the
   auxiliary prime the unramified automorphic component gives a
   crystalline representation with weights `-e,0,e`; its Newton slopes
   lie in that interval. Hence `Q^e` clears the denominator at every
   coefficient embedding. The rank-two assertion follows directly from
   the good-prime Hecke polynomial. The rank-three normalization uses
   the rational factor `Q`, so scalar conjugation introduces no
   square-root ambiguity.

## Quantifier and consumer audit

The source `CongruenceNumberRankThree:125-140` fixes `K` before the
constants and then varies `e,N,p`, the roots of unity, every coefficient
prime, and every admissible family. `KatoUse:36-52` has the same fixed-field
order. The proof supplies exactly this order.

The source's `CountI:22-136` chooses
`K = Q(sqrt(-p_K(chi)))` from the fixed primitive character `chi` before
the host's `q,d,N,t` vary. It then chooses two fixed auxiliary primes and
groups host characters by their kernels. The elementary identity

    sum_H phi(index H) <= |(Z/NZ)^times| <= N

absorbs all character orbits. Thus no estimate uniform in `K` is required
by this particular downstream consumer. `GdOfHost:37-94` verifies its
good-data condition by excluding the fixed primes dividing
`disc(K) h_K` and by ramification at `p_K(chi)`: that prime ramifies in
`K` but not in `Q(mu_ell) F_{psi^(ell)}`. Together with the independently
reviewed local chart and one-character comparison, this closes the stated
nonresonant Case I supplier.

The full weighted RH product also contains Case II and the large-conductor
part of Case V. They do not satisfy the preceding good-data hypotheses
automatically, so their bounds remain open. The same distinction applies
to the GRH route. An auxiliary field used earlier to prove automorphy
need not have bounded degree: this count occurs after descent to the
original `K` or `Q`.

## Verification

The checker authenticates pinned source files and bounded excerpts,
checks the exact Weyl dimensions, the inverse-arithmetic-Frobenius twist,
the two possible residue-degree formulas for rank-two traces, and the
elementary archimedean inequalities used in the integer product. Primary
PDF hashes and checked page ranges are retained separately in its output.

This is not an automated proof of p-adic Hodge theory, automorphy,
local Langlands, or a computation of any actual Selmer group. No Lean
rebuild is claimed. Full mathematical proofs of the new reductions and
all theorem hypotheses are in the shared section; the deep classical
theorems are explicitly cited.
