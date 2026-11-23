# Maximal integral Hermitian mass

**Classification: closed obligation — the actual maximal-lattice
mass input to the fixed-label genus pair count.** This is a direct
application of the classical mass theorem with a complete local
calculation, not a new unconditional proof of the return estimate.

For every CM extension E/F unramified at all finite places and
rank n >= 1, there is a positive constant C(E,n), chosen before
the Hermitian space and its maximal integral lattice vary, such that

    Mass(L) = C(E,n) product_(P bad) (q_P^n-(-1)^n)/(q_P+1).

Here "bad" means nonunimodular and q_P = sqrt(N_E P). Every bad prime
is inert, so this is an integer. The full proof and explicit constant
are in [the manuscript section](../paper/shared/maximal-hermitian-mass.tex).

## Local argument and normalization

At a split prime, maximality makes the two component lattices dual
to one another; hence the lattice is unimodular. At an inert prime
a Hermitian lattice has an orthogonal integral basis, also in
residue characteristic 2. Maximality forces all exponents to be 0
except possibly a single exponent 1. Two exponent-one coordinates
would give an isotropic residue vector and a proper integral
overlattice. The discriminant quotient at a bad prime therefore has
cardinality q^2.

For the original full unitary group, put
b_n(q) = product_(a=1)^n (1-(-1)^a/q^a). The nonunimodular local
density is (q+1)b_(n-1)(q), while the discriminant factor contributes
q^n. The ratio to the standard density is exactly

    q^n b_n(q) / ((q+1)b_(n-1)(q))
       = (q^n-(-1)^n)/(q+1).

The density is the stabilized congruence count, not automatically
the count modulo the residue field. All finite primes are good for
the cited Hermitian density theorem, including primes above 2:
only a *ramified relative quadratic extension* in residue
characteristic 2 is excluded. The base field may itself ramify
over the rational 2-adic field.

The same calculation supplies the next exact normalization. If a
rational prime T splits completely in E and
L-dual/L is isomorphic to O_E/T O_E, then

    Mass(L) = C(E,n) ((T^n-1)/(T-1))^f.

This is the literal cyclic-discriminant mass factor in the source's
primitive-sublattice genus mean. Such lattices in a fixed Hermitian
space form one genus. Both conclusions follow from the explicit
split elementary divisors and the same local density theorem;
they do not require an assumed comparison of unknown Haar constants.

## Published source and exact consumer

The external input is the classical Siegel mass formula and its
Jordan-block local density formula, as stated in Markus Kirschmer,
*Definite quadratic and hermitian forms with small class number*,
Theorems 4.2.3--4.2.4 and Lemma 4.2.5, printed pages 51--53. Definition 3.5.1
specifies the excluded primes. That research monograph attributes
the general theorem to Gan--Yu, *Group schemes and local densities*,
Duke Mathematical Journal 105 (2000), 497--524, Section 10; the
local formula is their Theorem 7.3.

The exact PDF was downloaded from
<https://www.math.uni-bielefeld.de/~mkirschm/papers/herm.pdf>;
its SHA256 and bounded extracted statement hashes are recorded in
the certificate. This is a cited standard theorem, not claimed to
have been reproved from the source's Lean development.

The original consumer is the proposition MaxMass, lines 10--14,
in Development.AbelianVarietyTheory.PublishedTheorems.DiscreteSeriesUnitary₂.MaxMass.
The definitions of IsMaxLat, badP, qIn, and lamMax are in
Development.AbelianVarietyTheory.Definitions.SemilocalFrames.ChartGen,
lines 104--137. The source's original proof is
Development.AbelianVarietyTheory.Proofs.FlagMeasures.MaximalHermitianLatticeMassRatio,
lines 31--117. Our proof supplies the same quantifier order,
unimodularity convention, full-unitary mass, and finite product.

The same section proves the exact mass bound for all integral
lattices of fixed discriminant n in a **fixed** positive definite
rank-a Hermitian space:

    sum_[L] 1/|Aut L| <= C(E,a) n^((a+log_2(2f))/2).

All maximal lattices in that space form one genus, so the proof
counts sublattices at a single index; it introduces no uncounted
sum over varying rational spaces.

The source uses these inputs in
TermPairCountBoundOfSiegelMassRatios.pair_count_bound_of_siegel_mass,
lines 70--163. The uniform primitive-sublattice genus mean, with
the exact final mass normalization, is now supplied in
[a separate proof](primitive-sublattice-genus-mean.md).
The next arithmetic suppliers used by DiscNResNeZero, lines
312--430, are the fixed-space isometry counts and the actual
row-to-lattice correspondence.
No genus mean or return multiplicity is declared bounded merely
because its mass input is now available.

## Verification

Run the script with Python:

    python scripts/maximal-hermitian-mass-check.py --offline

The certificate authenticates the pinned source files, preserves
the external statement hashes, checks the local factor identity
symbolically, and directly counts small congruence-level isometries
at an inert dyadic prime. Those finite counts check the normalization
and its stabilization; the general mass theorem is the cited result
and the local structural argument is a written proof.

Neither the complete W08 node nor either hypothesis is proved here.
