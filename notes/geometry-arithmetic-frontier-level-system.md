# The actual simultaneous level system

## Status

**Closed obligation:** the original `N0` Siegel-family supplier and the
entire `N2` simultaneous level-system supplier, including its finite,
étale, surjective, and formally unramified comparisons. This is a
subobligation of the larger geometric construction; no whole RH or
Dirichlet GRH proof-map node is closed by this result alone.

The proof is [shared by both manuscripts](../paper/shared/geometry-arithmetic-frontier-level-system.tex).
Its [source certificate](../certificates/geometry-arithmetic-frontier-level-system.json)
authenticates the exact interfaces and primary references. No Lean build
is claimed.

## Precise frontier theorem

For each original host and datum, choose one rational cone system on the
original unimodular symplectic lattice. For each prime p and valuation
subring W of C in which p is a nonunit, choose the canonical normalization
models for **every** original level and coefficient field. Then:

1. Every model has the already established complete
   `LevelStructureConditions`.
2. Every original `Level.Dvd` and coefficient-field inclusion has a
   transition finite **after the exact coefficient base change**, preserving
   the original family, primitive line, and the label powers M2/M and A2/A.
3. One odd prime n different from p is coprime to M for every original
   level, and the actual Siegel family can be taken at n, with j=1.
4. Adding exactly that n-level and exactly F(zeta_n) gives a finite étale
   surjective transition on the actual abelian loci, and a finite map to
   the specified Siegel space with the exact underlying family and
   biextension line.
5. If p does not divide lcm(M,A), this finite Siegel map factors through
   the original required reduced flat scheme XX, finite and formally
   unramified over the Siegel base; its normalization is the actual
   abelian locus, with the prescribed extended label sections.

The same cone choices support the
[all-place global model](geometry-arithmetic-frontier-global-model.md).

## The decisive constructions

### Finite transitions

A smooth projective fan invariant under the integral Siegel compact
group is chosen once. Principal-level cusp lattices are homothetic:
the central symmetric matrices at level m are m times their integral
lattice. Thus the rational cones remain smooth at every auxiliary
principal Siegel level; the induced PEL cones may be nonsmooth.

For two comparable levels, both PEL models can be presented as finite
normalizations over the **same** auxiliary Siegel model. The upper
normalization contains the image of the lower finite ring by
integrality. Its finite ambient generators still generate it over the
lower ring, proving finiteness. Lan's Theorem 7.14 identifies these
presentations with the actual chosen models. No assertion that arbitrary
toroidal level maps are finite, or that normalization commutes with
ramified base change, is used.

### One prime for all M

The source's `Level.fromK` is essential. It makes the half-level ideal
the extension of an ideal from O_Q(sqrt(-d)) = Z[w0]. Faithful flatness
contracts the product and coprimality identities to that quadratic
ring. Hence an inert prime cannot divide any admissible M. An elementary
quadratic-character and Chinese-remainder argument supplies an odd
inert prime outside any specified finite set. No GRH or effective
Chebotarev estimate is involved.

### Exact Siegel interfaces

The source line P on A x A, rigidified on both axes and symmetric, is
the Poincaré line for a symmetric homomorphism lambda. Its diagonal has
polarization 2*lambda, which explains and preserves the original factor
two in the torsion pairing. The odd auxiliary level recovers the
unsquared pairing uniquely. Generic principality extends over each
specified, possibly nondiscrete, valuation ring using normal finite
approximation and full faithfulness for abelian schemes.

At prime-to-p original level, Rosati-compatible endomorphism structures
form a finite formally unramified scheme over the fine Siegel space;
the label schemes are finite étale. The reduced schematic closure of
the exact generic PEL locus is flat over the original DVR, and its
normalization is precisely the chosen abelian locus. This constructs
XX and its original labels, rather than postulating an integral PEL
moduli space with suitable properties.

## Remaining obligations

The formal-arc clause `Model.N4`, the numerical arithmetic height and
section estimates, the prescribed global period norms, and the final
uniform fourth-power assembly remain separate. These theorems do not
bound integral Selmer torsion, global rational returns, or growing
auxiliary dimensions.

## Reproduction

```bash
python scripts/check_geometry_arithmetic_frontier_level_system.py --offline
```

The checker authenticates bounded source and primary-reference ranges.
There is no numerical proof claim: the all-level construction is the
standard mathematical argument in the shared text.
