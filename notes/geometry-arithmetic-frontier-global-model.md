# The actual global arithmetic model and all-place domination

## Status and exact scope

**Closed construction obligation:** the canonical individual models can be chosen to satisfy the original `N6` clause. For every original level with `A=1` and `GoodAt(p)` at every prime, and every original coefficient field, there is a normal projective flat model over that field's original ring of integers. It carries the original semiabelian family and primitive cubical line, retains the original generic descent, and dominates every prescribed local model with the exact source comparison maps.

This is a construction clause inside W10. It does not close W10 or all of the geometric `PartI` contract. It does not claim that an arbitrary uncoordinated infinite family of local modifications has a common finite-type global dominator.

## The actual cofinite arithmetic family

Fix the original singleton lattice and invariant rational cone data, presented by the auxiliary Siegel construction. Lan's global good-prime theorem permits an entire cofinite set of good primes. It therefore gives a genuine projective auxiliary Siegel toroidal scheme, with its universal semiabelian family, over the ring of integers with one integer `N` inverted.

Normalize the closure of the original generic PEL locus in this scheme in the original generic function fields, retaining all original components. The resulting model has the exact generic compactification and family. Its coefficient action and original symmetric primitive line extend by the already verified normal-base extension theorems.

At every place not dividing `N`, this model localizes to the canonical local model: schematic closure and normalization commute with localization. Lan's Theorem 7.14 identifies any different auxiliary presentation with the same induced rational fan. This verifies agreement at all but finitely many places by the actual normalization construction; generic isomorphism alone would not suffice.

## Incorporating the finitely many remaining places

At each place `v | N`, embed the actual local projective model `Y_v` into projective space over `O_v`. Normalize the closure of its generic embedded compactification in the same projective space over the full ring of integers. Call that global model `C_v`. It restricts exactly to `Y_v`: flatness identifies the local model with the closure of its generic fibre, and normality makes the local normalization unchanged.

Likewise close the good-prime model to a global projective normal model `C_0`. Normalize the closure of the common generic diagonal in the **finite** product of `C_0` and the exceptional `C_v`. The result is normal, projective and flat and has the original generic compactification. Its projections dominate every local model: use `C_0` away from `N`, and the relevant `C_v` at a place dividing `N`.

The source's `Dominates` asks for these maps and exact cartesian family comparisons; it does not ask that the projections be finite. The construction makes no such extra assertion.

## Gluing the actual family without an ineffective descent step

The ring with `N` inverted, together with the finitely many local rings `O_v` for `v | N`, is a finite faithfully flat quasi-compact cover of the original arithmetic base. Any two distinct pieces intersect in the original coefficient field. Pull back the given semiabelian family and primitive line on each piece. The overlaps are canonically the same original generic family and line; normal-base full faithfulness extends the original interior comparisons over the generic boundary and makes the cocycle exact.

The original symmetric cubical line is relatively ample on each piece. To ensure effective descent in **schemes**, descend the graded section algebras of all nonnegative powers of those lines, using flat cohomology base change. Relative ampleness gives the canonical open immersion of each local family into the relative Proj of its section algebra. These compatible opens descend to an open scheme in the descended relative Proj. The group, coefficient action, line, rigidification, symmetry and primitive identities then descend faithfully flatly. This explicit construction avoids assuming that arbitrary projective descent is effective.

The global generic fibre and its family are unchanged. Consequently the original generic abelian-locus equality and the `A=1` generic descent to `K_A` survive the vertical modifications.

## Every valuation in the original quantifier

The source ranges over valuation subrings `W` of the complex numbers with a rational prime `p` nonunit. Its local ring is exactly the restriction `V=F intersect W` to the finite original coefficient field. This ring contains all algebraic integers, and its maximal ideal contracts to a place `v | p`. Hence `O_v subset V subset F`. A DVR has only itself and its fraction field as overrings in that fraction field. The nonunit condition excludes `V=F`, giving `V=O_v` exactly.

Thus all the source valuations reduce to the actual finite places already treated. There are finitely many places above each exceptional rational prime; the graph construction includes all of them. The original inclusion condition fixes the ring map, and the generic-open lift is unique because localization is a monomorphism. The projected map and descended cartesian family comparisons meet every equality in `Dominates`, including the universal test-scheme equality.

## Remaining frontier

Coordinated finite transitions, the exact Siegel comparison, formal boundary/arc compatibility, and the numerical height and section-remainder estimates remain separate obligations. This construction introduces no uniform arithmetic estimate and no simplification of the growing dimensions or period lattices. It removes the existence of the original all-place global model as a missing hypothesis for the constructed canonical family.

## Evidence

The shared TeX contains the mathematical proof. The checker authenticates the pinned `Model`, `Descends`, `Coeff.V`, `Dominates` and `N6` interfaces, the actual cofinite good-prime and normalization references, and the flat base-change/relative Proj statements used for scheme descent. No finite computation or Lean build is used as a substitute for the construction.
