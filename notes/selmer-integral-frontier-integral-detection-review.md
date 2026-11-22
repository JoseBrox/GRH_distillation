# Independent review of integral paired detection

Reviewed on 22 November 2026, against the pinned source inventory and the
previously reviewed fraction-field paired determinant theorem.

**Decision: accepted as a proved supplier for a given normalized point and
its prescribed independent odd Selmer family.** This does not construct
the arithmetic point or close a whole RH or GRH node.

The review checked the following decisive steps.

1. The original coefficient module is the split integral module
   \(\eta E_A\oplus\bigoplus_i\varepsilon'_iO_A\). In particular,
   integral assembly does not require a saturation assertion about an
   unspecified lattice.
2. The first-order representation has inverse
   \(\rho(g)^{-1}(1-\sum_i\varepsilon_i\kappa_i(g))\). Expanding its
   action gives the commutator in the even coordinate and the detecting
   trace in the order \(Y_i\kappa_i(g)\rho(g)\).
3. Integral independence extends to the fraction field by clearing both
   the relation coefficients and the skew odd primitive. The integral
   span condition applies to each of the finitely many even matrix units.
4. One power of the uniformizer clears every primitive entry, preserves
   transpose polarization, and gives the required equality over the
   integral module by its injection into the fraction-field module.
5. The subgroup is the original cyclotomic kernel. The quantifiers are
   \(\forall z\,\exists N,Y\,\forall g\); neither a uniform exponent
   over cocycles nor lifting of modular cocycles is asserted.
6. Empty odd families, an empty second block, and zero primitives cause
   no exception to the argument.

The independent offline rerun of
`scripts/check_selmer_integral_frontier_integral_detection.py` passed:
seven authenticated source modules, 800 coefficient-basis associativity
triples, exact noncommutative coefficient identities, 108 denominator
and polarization cases, and three rejected negative controls. These
checks support the written mathematical proof; they are not a Lean
build or a proof of the remaining arithmetic inputs.

The companion proof and certificate are
`notes/selmer-integral-frontier-integral-detection.md` and
`certificates/selmer-integral-frontier-integral-detection.json`.
The next dependency is a finite simultaneous detecting set, followed by
coefficient extension and the original integral congruence estimates.
Whole-node counts remain ordinary RH **6/9**, Dirichlet GRH **17/31**.
