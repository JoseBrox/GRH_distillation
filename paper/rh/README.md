# The RH manuscript

The current [30-page manuscript](main.pdf) develops the shorter route to
the ordinary Riemann hypothesis. It contains a complete proof of the eventual one-sided
prime-sum criterion, the direct positive-kernel transfer, and the
geometric and matrix comparisons used to state the remaining arithmetic
estimate. It does **not** claim a completed proof of RH.

The organization follows the mathematical dependencies:

1. The problem, corrected prime sums and two analytic targets.
2. The full short analytic proof, followed by the stronger averaged
   criterion and its finite integer-table version.
3. Primitive-character positivity at all primes, the thick/thin
   comparison, four surviving quadratic terms and zeta centering.
4. Classical Selmer finiteness and finite prime support, the smaller
   character family, and the weighted estimate still needed.
5. One mean volume, a single test intersection sensitive to the block
   weights, the classical all-point-height reduction, exact
   component-degree weights, selected tangent degrees, integral jets,
   the absolute Siegel lemma, short sections and descent.
6. Two positive spectral traces, direct slope comparison, and control
   under the actual source and target restrictions. Squared energies
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
`certificates/rh-build.json`. The seven-page didactic introduction
remains in `paper/guide` and is a separate reading aid.
