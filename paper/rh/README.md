# The RH manuscript

The current [manuscript](main.pdf) develops the shorter route to
the ordinary Riemann hypothesis. It contains a complete proof of the eventual one-sided
prime-sum criterion, the direct positive-kernel transfer, and the
geometric and matrix comparisons used to state the remaining arithmetic
estimate. It does **not** claim a completed proof of RH.

The organization follows the mathematical dependencies:

1. The problem, corrected prime sums and two analytic targets.
2. The full short analytic proof, followed by the more flexible averaged
   criterion and its finite-table version at fourth powers.
3. Primitive-character positivity at all primes, the thick/thin
   comparison, four surviving quadratic terms and zeta centering.
4. Classical Selmer finiteness and finite prime support, the smaller
   character family, the integral weighted product, a compatible
   conormal pairing, exact graded comparisons, four-weight admissibility,
   the finite-slice multiplicity bound, diagonal point uniqueness and
   nonpositive base-point rigidity from qualitative finiteness and the actual
   marking. Resultants
   and common divisors retain their same-orbit hypotheses; the actual
   models and the uniform product estimate remain open.
5. One mean volume, a single test intersection sensitive to the block
   weights, the classical all-point-height reduction, exact
   component-degree weights, selected tangent degrees, integral jets,
   the absolute Siegel lemma, classical theta sections, the signed
   determinant comparison, the integral Hodge module and its two
   filtrations, a direct boundary period argument, determinant torsion,
   constant finite order, an exact ramified determinant calculation, CM
   eigenframes, the elliptic product and period calculation, and exact
   exact algebraic descent and integral extension of the prescribed CM point.
6. Two positive spectral traces, direct slope comparison, and control
   under the actual source and target restrictions, with a prescribed mass
   and explicit scalar sufficient bounds for the complete period sum and
   its rational returns. Squared energies
   remain available when they give a smaller cost.
7. The combined signed arithmetic budget, scalar parameter losses and
   the construction estimates still required.

The companion GRH manuscript is in `paper/grh`. Its technical chapters
in `paper/sections`, together with the common preamble, are shared
mathematical sources. Deep results imported into the RH text are cited
by their ordinary theorem names. The compact RH text is not a second
copy of the entire technical development. Verification records and
source dictionaries remain outside both mathematical manuscripts.

Build from the repository root with:

```sh
python scripts/build_paper.py --rh
```

The output is `paper/rh/main.pdf`; build evidence is recorded in
`certificates/rh-build.json`. The eight-page didactic introduction
remains in `paper/guide` and is a separate reading aid.
