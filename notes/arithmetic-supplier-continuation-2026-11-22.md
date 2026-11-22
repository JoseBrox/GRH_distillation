# Current arithmetic suppliers and remaining research

This checkpoint continues main at
`32de5c1887329aaa813007b7cf6f31e625f4ff8f`. The two conventional
proofs remain incomplete. The purpose of this continuation is to finish
specific missing suppliers inside the open Selmer, geometric and global
norm nodes, and to distinguish that work from refinement of already
proved estimates.

## Completed suppliers

### Integral detection and the complete auxiliary choice

The fraction-field paired determinant argument now returns to the
**original integral module**. Its coefficient coordinates form an
actual direct sum, so clearing one common denominator in finitely many
primitive entries preserves block support and transpose polarization.
This proves the original detection statement on the full cyclotomic
kernel. The [proof](selmer-integral-frontier-integral-detection.md) was
published at `eb5d5d0e4b93d5619008ee347fb50aa073681229`.

The exact open-subgroup finiteness condition makes continuous cocycle
modules finite. It also constructs the original odd Selmer family from
the quotient by skew boundaries, retaining every local witness. A basis
of the detecting functionals over the fraction field preserves their
**exact integral common kernel**, and finite intersections of the
original open spectral loci give one simultaneous finite detecting set.
Finite coordinate projections then preserve all local conditions,
polarization and detection through ramified coefficient extensions.
Splitting the selected characteristic polynomials and enlarging residue
fields completes the original auxiliary-choice statement.

The [finite-selection](selmer-integral-frontier-finite-selection.md) and
[coefficient-extension](selmer-integral-frontier-coefficient-extension.md)
proofs, with independent reviews, were published at
`a86977f7415b364639de07f35d611f9b0a4be591`.
The given arithmetic points, group finiteness, spectral density and
nontrivial residual cyclotomic character remain their original inputs.
A single denominator works for integral detecting cocycles at each
fixed point, without claiming uniformity over moving points or lifting
of modular cocycles. The earlier complete-equation theorem still
handles the full set of modular solutions.

### The original signed arithmetic boundary comparison

On the supplied smooth compact model, change of variables identifies
the original sum over projection branches with the mixed curvature
integral, retaining every complex component and existing cover weight.
The original vertical unit equations express every vertical factor
locally as the absolute value of a nonvanishing holomorphic function.
Their curvature therefore vanishes **at the boundary as well**.

Exact metric variation, the two previously proved energy limits and
energy concavity now give the signed arithmetic inequality at each
fixed positive rational twist. One common polynomial recovers the
untwisted limit. This removes the need for a separate convergence
claim for the unbounded cusp function against varying regularized
measures. No bounded metric at zero positive twist is assumed.

The [complete comparison](geometry-arithmetic-frontier-compact-model-stokes.md)
and its independent review were published at
`f6b85addc3d98cb33d5810cd31bc84a752ed1143`.
The arithmetic model, intersection system, smoothness and height
hypotheses remain supplied data. The theorem does not construct them
or bound the arithmetic section remainder.

### The ordinary local arithmetic count

Local Tate duality and Euler characteristic give an exact rank-one
cocycle count. The defect is the length of the annihilator of the ideal
of differences between the original ordinary characters and the
cyclotomic character. The exact typed triangular filtration then counts
all entries in the original first-order module. This gives the original
ordinary local bound with an explicit constant independent of both
truncation and auxiliary level at fixed arithmetic data. The proof
retains the local torsion subgroup and the residue-field trace pairing,
including cases in which the trace of one vanishes.

See the [ordinary local theorem](selmer-integral-frontier-ordinary-local-count.md),
published with its independent review at
`e9b76c5b6bb238d446f2437f0cb88dcb6565c6b3`.
Its remaining global and distinguished-place cohomological consumers
are explicit; this is not uniformity over changing arithmetic points.

### Equality of the original scalar-pair densities

The [complementary-lattice argument](global-norm-frontier-scalar-density.md)
proves a genuinely missing local equality. The original quotient
isometries and designated split-level congruence graph identify the
orthogonal integral lattices. Self-duality then identifies the
discriminant modules of the actual primitive modified frame lattices,
so their residue Gram coranks and their primitive densities agree.
Together with the previously proved frame count, this finishes the
original local density assertion with constant one. The raw tuple
cannot replace the modified tuple: an exact original-data example has
different residue coranks for them. The theorem and the three next-target
checkpoints were published at
`e26c5bace6641d96a18e21e6b163e170a3ca363c`.

## A refinement, correctly separated from a new closure

The exact primitive Hermitian frame count, including singular residue
Gram matrices and residue characteristic two, was **already proved**
in the local-density chapter. Repeating it would not advance an open
supplier. The [new local estimate](global-norm-frontier-primitive-density.md)
is instead the signed refinement: pairing consecutive factors removes
a rank multiplier, and the original even ranks force positive errors
to occur only at inert places of odd corank, with one additional power
of the residue-field size. The original primitive cutoff and modified
split tuple remain unchanged.

This refinement was published at
`48ab6a2c9cdcc0b9f0c38dbe22be1857a19fd1b0`.
It improves a finite-place coefficient. It does not prove the global
period norm estimates or a new leading exponent in the final height
contradiction. The main manuscripts reuse the existing count and add
only the short signed estimate.

## Priorities after these suppliers

1. **Selmer arithmetic.** Apply the proved ordinary local count, then
   establish the distinguished-place and global cohomological inputs and
   construct the actual patched modules with their dimensions. Propagation must take place in
   the full normalized ring, including its characteristic-prime fibre.
2. **Global norms.** Use the now-proved scalar-pair density equality
   with the remaining original local orbital laws. The principal
   remaining estimate is the actual archimedean orbital/Bessel
   contribution and its assembly
   into a small normalized source deficit and target excess, with all
   returns, restrictions, volumes and normalizers retained.
3. **Geometry.** Construct the actual model, sheets, lattice and height
   inputs used above. The arithmetic section remainder has a separate
   supplier involving the original short-vector frames and jet lattices;
   the finite jet-rank theorem alone does not supply it. Do not return to
   the now-completed limiting-energy argument as a substitute.

The next steps have bounded, authenticated restart records:

- [Selmer invariant factors and tower descent](selmer-integral-frontier-after-ordinary-local-count.md).
- [The exact normalized archimedean target](global-norm-frontier-archimedean-target.md).
- [The arithmetic section and jet-lattice target](geometry-arithmetic-frontier-section-remainder-target.md).

These checkpoints assert no additional closure. They retain the precise
objects, constants and hypotheses needed to resume without loading
large source files or reopening completed subarguments.

## Verification and organization

Each proved supplier has a full mathematical note, a compact shared
manuscript fragment, pinned source hashes and an independent review.
The coefficient identities, characteristic-two counts and rational
normalizations have exact reproducible checks where useful. Source
authentication and finite computations support the written proofs;
**no Lean build has been performed**.

The [integration record](../certificates/arithmetic-supplier-integration-2026-11-22.json)
records the final builds, artifact hashes, scoped visual review and
unchanged short analytic proof.

Both routes use these shared results with their original hypotheses.
The eight-page guide remains an organizational explanation, and its
complete short analytic RH proof is preserved byte for byte. The
blueprints record completed suppliers inside existing open nodes;
no node has been subdivided to increase the count.

**Whole-node counts: ordinary RH 6/9; Dirichlet GRH 17/31.** These are
counts of stated interfaces, not percentages of either conjecture
proved.
