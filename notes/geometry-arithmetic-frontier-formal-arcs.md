# The original formal arcs and their specialization

## Status and exact frontier

**Closed construction obligation:** the canonical local models satisfy the complete original `Model.N4` clause. The proof constructs the prescribed arc over the original power-series ring, verifies its exact abelian locus, retains the selected half-level and full auxiliary labels, recovers uniqueness from the actual `PELUnif` contract, and proves the stated specialization for every allowed evaluation homomorphism.

Together with the previously established `N0`, `N2`, `SplitFibres`, `N3`, and `N6`, this supplies the original geometric `PartI` construction. It does not complete W10: numerical height, arithmetic section-remainder, cusp and signed-boundary estimates remain separate obligations. No proof-map completion count changes here.

## Actual periods, line, and labels

Write `O'` for the original characteristic-zero field or complete DVR, `varpi` for 1 or its prescribed uniformizer, and `R=O'[[t]]`. Keep the original abelian scheme, primitive line, coefficient action, lattice, and point map. Twist the given periods by

\[
\psi_y=\psi_y^0t^{b(y,y)/2},\qquad
\tau_{y,z}=\tau_{y,z}^0t^{b(y,z)}.
\]

The source expressly requires every original `psi` to be a unit generator on all of `O'`. Positive definiteness of the integral `b` therefore proves positivity and convergence for the actual ideal `(t)`. The original adjunction and `w+bar(w)=1` give `b(y,w y)=b(y,y)/2`, preserving the transported original primitive identity, including its line exponents and normalization.

The actual complete-pair Mumford construction supplies the semiabelian family, its original symmetric cubical line, and the prescribed Fourier and all-integer torsion maps. For `k=M,A`, multiply a selected torsion coordinate by `t^(b(y,z)/k)`. The exact divisibility by `2*lcm(M,A)` makes the exponent integral; addition, period equivalence, coefficient action, tower maps, and Weil pairing retain their original values.

The input `eta` is unconstrained away from `bar(b) Lambda`. Choose `e+` in `bar(b)` with `1-e+` in `b` and define the actual half-label at `x` from the transformed class of `eta(e+ x)`. The geometric Tate condition proves independence, linearity, kernel `b Lambda`, and agreement on the selected submodule. The full `A` label uses all its supplied values. No unasserted linearity of the unused half-label inputs is assumed.

## The actual toroidal extension

At every centered valuation the monodromy form is exactly `v(t)*b`; no second `varpi` contribution survives the input unit condition. The exact torus submodule, its annihilator, the coefficient action, and the transported Tate marking determine the original admissible cusp filtration and torus argument. The singleton auxiliary Siegel degeneration, and any equivalent auxiliary tuple, carries the corresponding image of this same ray. The fixed cone datum therefore satisfies Lan's actual centered-valuation criterion at that cusp.

The normal-base extension theorem gives a map from the entire possibly two-dimensional `Spec R` to the prescribed model. The unit-period subgroup is the whole lattice when `t` is invertible and is zero otherwise. Its exact torsion-rank sequence proves that the abelian locus is precisely `D(t)`. The generic moduli object lies on `D(varpi*t)` as required.

## Uniqueness from the source contract

The proof uses the actual multiplication and zero-normalization clauses of `Unif`, not only equal dimensions of coefficient spaces. Clear the two common denominators in `Expands`; multiply the literal finite expansions on every thickening using `t_mul`, the original cube structure, `gt_t`, and `w_compat`. This proves that all-power `ExpBij` gives an isomorphism of graded section rings. The entire section ring of the original ample generic line recovers the polarized abelian variety. The same coefficient sum evaluates at zero, by `t_unit` and `w_rig`, so the recovered isomorphism is a group isomorphism.

Every competing source SAB also has a relatively ample line: it is symmetric cubical and has ample generic fibre, so Lan's Lemma 4.2.1.6 applies. Normal-base full faithfulness extends the recovered group and line comparisons; the relative-Proj open immersion separates their formal coordinate maps. The `OLinear` conditions identify the coefficient action on the quotient and torus, and the difference factors through a homomorphism from a proper abelian scheme to a torus, hence is zero.

The exact `PhiRel` condition fixes each selected torsion point by its projective theta action and the perfect principal Weil pairing. The selected half-label determines the entire actual map since `Lambda=b Lambda+bar(b) Lambda`. Fine moduli and separatedness give the required equivalence characterizing the arc.

## The nonflat specialization is checked in the construction

There is no field homomorphism from the whole fraction field of `O'[[t]]` taking `t` to `varpi`, and none is used. The actual relatively complete Mumford charts are character-graded algebras whose coefficient modules are sums of unit multiples of integral powers of `t`. For each character such a sum is either its smallest power or the localization obtained from unbounded negative powers. Both descriptions commute with the particular evaluation `t -> varpi`, as do their multiplication and period translation maps.

The same positive auxiliary powers and finite character sets work before and after evaluation, because their inequalities depend only on the integral exponents. Chart gluing and represented fpqc period quotients commute with this base change. Proper algebraization then identifies the specialized model and its original line with the actual model for the `varpi`-twisted periods. This checks the period action itself; the formal Raynaud group alone would not retain that information.

Apply the preceding source-contract uniqueness over `O'` to identify any proposed specialization with this one. Finally every ring homomorphism fixing `O'` and taking `t` to `varpi` is automatically the usual convergent evaluation: tails of order `r` map into `varpi^r O'`. Thus the last universal quantifier in `N4` is preserved exactly.

## Evidence and limits

The shared TeX is the mathematical proof. The checker authenticates the original `ArcIn`, `HasArcData`, `N4`, `PartI`, Fourier multiplication, coefficient-action, and torsion interfaces, together with the primary degeneration, chart, algebraization, and toroidal-extension references. Exact symbolic checks cover the quadratic twist, adjunction, period shift, and Weil cancellation; these finite checks do not prove the geometric construction or realize an entire source CM host. No Lean build or quantitative section estimate is claimed.
