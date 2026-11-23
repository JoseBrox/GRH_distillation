# The original half-level supplies the actual integral PEL model

> **Later status (23 November 2026).** The later [integral theta/uniformization](geometry-arithmetic-frontier-integral-theta.md), [level symmetries](geometry-arithmetic-frontier-level-symmetry.md), [coordinated level system](geometry-arithmetic-frontier-level-system.md), and [global model](geometry-arithmetic-frontier-global-model.md) supply several stronger conditions listed below as missing. The original local-model theorem and proof remain unchanged. For live outstanding hypotheses consult [current state](current-state.md).

## Status and frontier

**Closed arithmetic construction subobligation:** the original coefficient field and level supply the individual normal, flat, projective `Model`, with the original semiabelian family and primitive rigidified cubical line, at every prime satisfying the original `GoodAt` condition. No new coefficient-field extension, line power, generic lattice rescaling, or auxiliary moduli cover is used.

This does not close W10. The stronger coordinated `LevelStructureConditions`, `PushInvertible`, complete `PELUnif`/`TorsionIso` supplier, height and section estimates, and signed cusp comparison remain distinct obligations. The current theta denominator still retains its good-cover and full integral-chart hypotheses.

The smallest construction frontier was: over the original coefficient valuation ring, construct all the fields of `PushInvertible.Model`, including the same line and the exact generic abelian locus. The theorem now supplies them.

## Exact level completion

Put `L = lcm(M,A)`. The original `Coeff` already contains the prescribed `zeta_L`. The complementary modules `bar(b)Lambda/M Lambda` and `b Lambda/M Lambda` are isotropic and perfectly paired. The given half-marking on the first and the prescribed `zeta_M` uniquely determine the second marking by Cartier duality.

The completed M-marking agrees with the original A-marking on `gcd(M,A)`-division, because the original coherent Tate marking has the prescribed A-root. The two glue uniquely to a full L-marking. Thus forgetting the completed labels is an **equivalence of moduli functors over the original coefficient field**, not a cover.

The full-Tate liftability condition is retained. If the original root system needs adjustment by `r` modulo L, choose `r` in the profinite unit group with `r = 1 mod A`. At every place over M the CM extension must split, by the original complementary-ideal condition; use the norm-r unit `(1,r)` with the identity on the fixed half. At other places use the unramified norm on units, and on principal units at primes dividing A. The trace-lifting argument includes dyadic primes and ramification in the totally real base. Multiplying the original Tate marking by this coefficient unit preserves both original label maps and gives the chosen L-root.

The stabilizer with multiplier one modulo M is exactly full principal level L. The source's `GoodAt(p)` says `M / p^v_p(M) >= 3`, so its prime-to-p image is neat by Lan's explicit congruence criterion. This is the missing step beyond the earlier half-level automorphism argument.

## Actual local construction

Apply Lan's projective ramified toroidal compactification theorem to this full level and the **singleton original lattice**, with no isogeny twist. Use a projective compatible cone decomposition, whose existence is in the same primary source. Base change to the original coefficient valuation ring, take the reduced closure of the prescribed cyclotomic generic component, and normalize. Excellence makes the normalization finite. Every retained component dominates the discrete valuation base, so normality, projectivity and flatness hold.

Lan supplies the semiabelian family and its coefficient action. His symmetric cubical extension theorem extends the **actual primitive line**, not merely its square. Full faithfulness extends the zero rigidification, symmetry, adjoint and primitive identities without a scalar. The boundary torus has positive rank away from the zero cusp, which verifies exactly the source's generic abelian-locus requirement.

This proves the individual original `Model` supplier. It does not establish all of the stronger properties bundled into the separate source `PartI` proposition.

## Next decisive step

Lan's formal boundary comparison identifies the family with the original-lattice Mumford family, including ramified primes. The next task is to compare this data field by field with `PELUnif` and `TorsionIso`, and establish the original integral rank-one theta section property `PushInvertible`. These are actual remaining suppliers. A global model with coordinated finite level transitions and domination of the local models is also stronger than the individual model constructed here.

## Verification

- Written standard proof: `paper/shared/geometry-arithmetic-frontier-integral-pel.tex`.
- Exact source contracts: `TwoWeightEqOneAddRoot`, `PushInvertible`, `Clauses`, `UniformisationConclusion`, `AdaptStd`, pinned at `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
- Primary references: Lan's revised thesis, ramified compactification paper, and projective cone paper; exact URLs, hashes and bounded text ranges are in the certificate.
- Checker: `python3 scripts/check_geometry_arithmetic_frontier_integral_pel.py --offline`.

Finite exact level and norm checks supplement the written proof and cited construction theorems. They do not constitute a Lean build or computational proof of the general compactification theorem.
