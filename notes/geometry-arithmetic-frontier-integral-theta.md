# The actual integral theta module and complete local uniformization

## Status and frontier

**Closed obligation:** the actual individual integral PEL model now satisfies the entire source `PushInvertible`, `SplitFibres` and `N3` clauses. This closes construction subobligations inside W10. It does not close W10 or any other whole proof-map node.

The previous complete-DVR supplier left a real gap: integral section modules along arithmetic curves do not imply an invertible theta pushforward over a singular higher-dimensional model. The new argument constructs the section on each complete normal local base, cancels its actual common denominator there, and descends the exact all-open generation and fibrewise nonvanishing statement to the model.

## The decisive argument

Let `R` be a complete noetherian normal local domain of characteristic zero. Take the actual semiabelian family with nonempty abelian locus and split closed torus, exactly as in source `N3`. Symmetric generic ampleness gives the ampleness required by the degeneration theorem before that theorem is used. The exact squared degree formula for the principal polarization identifies the original period lattice with the character lattice and makes the abelian quotient principally polarized. The transported **original primitive identity** fixes the line, its torus character, rigidification and all period factors.

Write `d_y` for the original period generator in an integral fibre generator. Symmetry and the cube identity give `d_y^2 = unit * tau(y,y)`. Riemann positivity makes the right side integral, and in the maximal ideal for `y != 0`. Normality therefore makes every `d_y` integral; every nonzero-index `d_y` lies in the maximal ideal.

Normalize the actual generic theta section by its nonzero coefficient zero, which generates the rank-one theta module of the proper abelian quotient. Its coefficient at `y` is exactly `d_y` times an integral generator. Clear **one** common denominator `f` on the actual semiabelian scheme. Formal Raynaud expansion of this actual integral section has finite support on each infinitesimal thickening. Thus, for every `n`, all but finitely many `f*d_y` lie in the `n`-th maximal-ideal power.

Artin–Rees for the single submodule `f*R` supplies a constant `C` with `m^(n+C) intersect fR subset f*m^n`. Since each `d_y` is already integral, cancel `f` to prove maximal-ideal convergence of the original coefficients. This is the exact source `psi_tendsto`, without any claimed parameter-uniform bound on `C`.

The resulting formal theta section algebraizes **as the given generic section**. At every closed-fibre point, Krull intersection in the coherent quotient line modulo `f` proves actual divisibility of the denominator-cleared section by `f`. Thus the generic section is regular near the closed fibre. Each vertical divisor of this smooth family with geometrically integral fibres is the unique divisor over a height-one base prime, and its closure meets the closed fibre. Horizontal divisors have no pole because the section is already regular generically. Normality gives a global regular section. Coefficient zero then proves that it generates the entire theta module. Its closed-fibre restriction is the pullback of the nonzero abelian theta section; smooth openness makes it nonzero on every fibre.

## Exact descent to the source PushInvertible contract

Complete the model at an arbitrary point. Flat cohomology base change is valid for the actual quasi-compact separated family and the flat completion map. Express the completed generator as a finite sum of tensors of actual local sections; at least one such section is nonzero on the closed fibre. Spread that section to a neighborhood and shrink to the smooth image of its nonzero locus. It is now nonzero on every fibre.

For **every** open subset of this neighborhood, any section is generically a scalar times this section, because the generic theta space is one-dimensional. At each base point, choose a fibre point where the chosen section is nonzero. Its ratio with the other section lies in the local ring of the family; faithful flatness contracts that ratio into the base local ring. The scalar is therefore regular on the whole open set and unique. This proves the exact all-open sheaf clause, without assuming coherence of the nonproper pushforward or residue-field cohomology base change.

## The other two actual clauses

The original `GoodAt` level supplies an odd prime invertible at every relevant residue field. The exact half-to-full completion over the original coefficient field makes generic full torsion constant. Lan's finite étale torus part over the whole henselian base is then constant. The root of unity is already present, and a finite subgroup of the odd principal congruence subgroup of `GL(X)` is trivial. Hence the fibre torus is already split over the **original** residue field; `SplitFibres` uses a separable extension of degree one.

For `N3`, the full Fourier expansion, common-denominator, theta-action and all-integer torsion arguments of the DVR supplier apply over a complete normal local base. The source's maximal-ideal period convergence has now been proved directly. On the abelian locus, Lan's exact torsion sequence shows that the subgroup of periods with unit diagonal factor has full rank. It is saturated by bimultiplicativity, so it is the entire period lattice. The square identity makes each original `psi_y` a unit there. This supplies the precise `PsiUnitOn` field on every affine open, completing the original `UniformisationConclusion` rather than only its generic part.

All ranks, the original trace-one line, the signed coefficient recurrence, the `(k,-k)` theta multiplier and the original Weil-pairing convention are retained. Torsion includes levels divisible by the residue characteristic; no assertion that the whole integral torsion kernel is finite is made.

## Remaining obligations

Combined with the separate normal-approximation proof of good-reduction extension over arbitrary valuation rings, these results supply all of `LevelStructureConditions`. Finite coordinated level transitions, the exact Siegel comparison, global domination, arithmetic height and section-remainder estimates, and global theta norm estimates remain open. The Artin–Rees argument supplies qualitative integral existence and exact generation; it does not supply a uniform numerical height or section bound. Ordinary RH and Dirichlet GRH inherit these same verified construction clauses with their original data.

## Verification

The shared TeX is the mathematical proof. The checker authenticates the pinned source contracts and the primary degeneration and commutative-algebra references, verifies exact finite algebra models of denominator cancellation and the rank comparison, and retains explicit negative controls. No finite test replaces the normality, Artin–Rees, proper base-change or smooth-descent arguments, and no Lean build is claimed.
