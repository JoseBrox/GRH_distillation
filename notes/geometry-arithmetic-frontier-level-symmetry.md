# The original level symmetries and generic descent

**Classification: closed subobligations inside W06/W10.** The original
local integral PEL models can be chosen with the exact `LevelActs` and,
when the auxiliary full level is one, `Descends` clauses. Their prime-to-
residue-characteristic labels extend on the abelian locus, and the
full `GoodRedExt` holds, including its nondiscrete valuation rings. No coefficient extension, new
level labels or power of the primitive line is introduced.

## Precise theorem and construction

For every original coefficient field and `GoodAt` prime, choose the
projective rational cone decomposition invariant under the original
integral PEL group. The full-level subgroup is normal, so Lan's
Proposition 2.8(2) supplies this choice. The two prescribed label maps
and the original pairing root determine one full-level automorphism.
Comparison of the actual Tate markings proves its liftability; no
surjectivity assertion for reduction of an arbitrary integral group is
needed. Functoriality of the toroidal construction and normalization
extends the specified action and its exact family isomorphism.

When the full auxiliary level is one, the quotient of the half-level
stabilizer by full principal level is exactly the group of pairing-root
multipliers. Keeping all primitive roots gives a free finite action,
including on the boundary. Its quotient over the original smaller field
descends the compactification and the actual semiabelian line data.
The prescribed coefficient field selects its original root component
after base change; it need not be Galois over the smaller field.

On the abelian locus, prime-to-characteristic division is finite étale.
Normality extends every original generic label uniquely. For an arbitrary
specified valuation ring with supplied good reduction, approximate the
two families and their generic isomorphism over finite-type subalgebras
of that same valuation ring. Normalization is finite over the original
excellent arithmetic base and remains inside the valuation ring.
Normal-base full faithfulness then identifies the two models. This proves
both the discrete and the nondiscrete good-reduction clauses.

The complete proof, including the invariant cone choice, scalar-free
line comparison and effective descent, is in
[the shared theorem](../paper/shared/geometry-arithmetic-frontier-level-symmetry.tex).
Its references identify the exact Lan results.

## Remaining obligation

Together with the whole-model integral theta theorem, these results give
all of `LevelStructureConditions`. Simultaneous **finite** level
transitions, `SiegelCompare`, and global domination
remain separate. Projectivity of a transition is insufficient: a
refinement of a toroidal fan can have exceptional fibres. The present
theorem neither changes the whole-node counts nor supplies the height,
section or global theta estimates.

## Verification

The accompanying certificate authenticates bounded source interfaces
and primary reference excerpts, and checks the finite root action
exactly. The independent review records the hypotheses of the cited
construction and descent theorems. These checks supplement the written
proof; they are not a Lean build.

```sh
python scripts/check_geometry_arithmetic_frontier_level_symmetry.py --offline
```
