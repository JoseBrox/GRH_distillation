# Actual integral charts and Good3

Classification: **closed obligation**, for the exact local `Good3` supplier.
This does not close a whole proof-map node or the global arithmetic cover.

## Frontier and result

For every original integral framed point over a complete DVR with finite
residue field, construct a finite extension carrying the same frames and
theta generator, an actual `IntegralChartA3` with compatible truncation
frames, and `PELUnif/TorsionIso` for every integral model of that point.

The proof supplies this frontier over a **finite unramified extension**, so
the ramification index is exactly one. It constructs the actual integral
formal group and biextension frames and the canonical characteristic-zero
gauge. The original primitive line, all integer torsion orders, tangent
eigenspace lattice defects and ordinary-derivative conventions are retained.

## Mathematical mechanism

The closed torus splits over a finite residue extension, lifted by the
henselian finite-etale equivalence. Flat kernel base change preserves the
separate integral eigenspaces; flat H0 base change preserves the exact
theta generator even though the total semiabelian family is not proper.
Normal-base uniqueness transfers uniformization to every original integral
model. Smoothness supplies full integral tangent coordinates. A single
axis-normalized formal biextension frame gives all truncation identities.

The canonical gauge is explicitly constructed: formal logarithm and linear
cocycle homotopy kill the two addition cocycles; a separability idempotent
of the original CM algebra kills the adjoint derivation; the remaining
skew bilinear symmetry cocycle is removed over the fraction field.
No denominator introduced in constructing that gauge is assumed integral.

Gauge differences are balanced symmetric bilinear forms. Their correction
to the original harmonic values is a finite combination of exactly the
paired Laplacians that annihilate the original polynomial. Thus the values
are independent of the chosen chart and commute with the exact framed base
change. Arbitrary nonharmonic derivatives are not identified.

The existing discriminant-clearing theorem now applies to these actual
charts and actual integral sections. The unramified extension adds no
valuation loss, and descended integrality contracts to the original DVR.

## Scope still open

- No uniform degree bound for the local unramified extension is asserted.
- The extension is local and does not enlarge or replace the global
  coefficient field in the sized arithmetic-cover problem.
- The complete global cover and its theta-series/section identification,
  determinant-ideal comparison and archimedean norms remain separate.
- No Lean compilation is claimed; pinned source authentication verifies
  contracts and original normalizations.

## Evidence

- Proof: `paper/shared/geometry-arithmetic-frontier-good3.tex`.
- Primary references: its companion `-references.tex`.
- Checker: `scripts/check_geometry_arithmetic_frontier_good3.py`.
- Certificate: `certificates/geometry-arithmetic-frontier-good3.json`.
