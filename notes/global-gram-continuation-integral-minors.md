# Integral leading minors in the actual degenerate sum

**Classification: closed obligations — the actual leading-minor label sum,
normalized minor bound and product of local degenerate orbital estimates.**
The label sum is also stronger than its original source version: its
displayed bound has no root-discriminant factor. The fixed-label genus
pair count and the complete W08 obligation remain open.

The full definitions and proofs are in
[the shared manuscript section](../paper/shared/global-gram-continuation-integral-minors.tex).

## The arithmetic input that makes the difference

For the original CM field `E/F`, let `d` be the extension of the different
of `F`, and let `rho` be the root discriminant of `E`. The original
finite-unramified hypothesis gives `N(d)=rho^(2f)`, where `[E:Q]=2f`.
Both actual flag lattices

```
sum_(a=0)^(r-1) d^(-(r-a)) e_a,
sum_(a=0)^(r-1) d^(-(r-a)) e'_a
```

lie in the same integral unimodular Hermitian lattice. The exact source
dictionary is `FlagEEqHyperbolic.XS`, lines 93--97, together with
`IsRowLat`, lines 99--100, and `FrameOK`, lines 119--120: both
weighted modules equal the intersection of their isotropic subspace
with the same lattice `Lambda`. The definition of that intersection
is unfolded in `MinorIntegralityTorus.e_mem_lam`, lines 122--127;
`pair_int`, lines 129--141, extracts integrality from unimodularity.
These are statements about the original two flags, not replacement
flags or an auxiliary normalized lattice. Set
`a_l=sum_(a=0)^(l-1)(r-a)` and let `delta_l` be the corresponding
leading Gram determinant. Localizing at any prime shows that each
matrix entry lies in `d^(2r-a-b)`. The determinant expansion therefore
gives the exact divisibility

```
delta_l in d^(2a_l).
```

Consequently `(delta_l)d^(-2a_l)` is an integral ideal; if the minor
is nonzero, its norm is a positive integer. This direct proof does
not require an adapted normal form for the pair of flags, a principal
different, or a free integral lattice.

## Actual estimates supplied

Write `D_(tau,l)=|tau(delta_l)|rho^(-2a_l)`, `M=(2H)^(2r)`,
`sigma_tau=max(1,D_(tau,l)/M:1<=l<=j)`, and `S=product_tau sigma_tau`.
Zero internal minors are allowed. For distinct actual labels with
`delta_0=1` and `delta_l=0` for `l>j`,

```
sum_delta S(delta)^(-3r) <= 2^j [64(2H)^(2r)]^(2fj).
```

This holds for the full countable label set, not only finite subsets.
The reason for uniformity in the growing field is that differences of
two labels lie in the same ideal `d^(2a_l)`. Their normalized embeddings
have product separation at least one. A fixed grid in `C^f` then gives
the required packing bound without a field-shape constant.

At `H=b^(CH*m)`, `m=2r+2`, `b>=2`, `CH>=0`, this implies the
literal original consumer with `Cc=21+4CH`:

```
sum_delta S(delta)^(-3r) <= b^(Cc^2 m^2 f r).
```

No extra root-discriminant-versus-scale inequality is needed for this
part of the argument. For each selected nonzero minor its original
normalized ideal norm satisfies

```
1 <= Delta_l <= b^(C m^2 f) S^2,  C>=2(CH+1).
```

The same integrality controls the reciprocals of the minors across
all real places. It combines the proved local orbital estimates into

```
product_tau ||J_tau||op
 <= product_tau(kappa_tau/s_tau)
    (16*pi*e/k)^(j(k-1-j)f) Delta^(-(k-1-j)/2)
    (8*r*H)^(80r^4 f) S^(-Cs*k).
```

Here `k>=40r^4`, `k>=5r`, `Cs>=0`, and the original admissible moment
is `q=(ceil(Cs)+2)kr`. The original Haar factors remain explicit.
No finite-place stabilizer factor or representation dimension is
discarded. The existing local moment allowance supplies this fixed
choice of moment before the arithmetic family varies.

## Direct attack on the remaining fixed-label count

The source's actual next supplier is `PairsP` in
`Development.AbelianVarietyTheory.Definitions.SemilocalFrames.PerRowC`,
lines 42--45, not merely another bound on the distinct minor labels.
For each pair of fixed labels it must bound the sum of the products
of the original term weights and stabilizer factors by

```
mass_of_actual_rows * e(j',delta') * e(j'',delta''),

e(j,delta) = Delta(delta)^(k/2)
             b^(Ch^2 m^2 f r^4) S(delta)^(Cp*k),
```

with `Ch,Cp` fixed before the arithmetic family varies. The actual
source uses `Cp=16`.

The source reduces this to a genus mean of triples consisting of
two embedded integral data and an isometry between them, then divides
the isometries by the dimension of their fixed subspace. The actual
primitive-sublattice genus mean, including all original mass constants,
is now supplied in [a separate proof](primitive-sublattice-genus-mean.md).
The [maximal and cyclic-discriminant mass laws](maximal-hermitian-mass.md)
are supplied with their exact local correction factors as well.

The remaining arithmetic estimates are the fixed-space isometry
counts and the actual weighted row-to-lattice correspondence; they
are not silently adopted from the source's dependency names.
The two normalizations must meet in the actual weighted return series
before one can claim

```
||K''_uu||HS^2 <= dim(pi_u) exp(-k f log k).
```

The generic returns, remaining finite-column sums, final arithmetic-map
identification and positive traces remain separate. Ordinary RH still
has growing auxiliary degree and rank.

## Verification

Run `python3 scripts/global-gram-continuation-integral-minors-check.py`.
It authenticates the pinned definitions and consumer interfaces; checks
the different-ideal exponent identity and all displayed polynomial
reserves exactly; and checks an exact Gaussian-integer Hermitian example
with a vanishing internal minor. The general ideal and packing arguments
are written proofs, not consequences of the finite tests. No Lean build
or whole-node completion is claimed.
