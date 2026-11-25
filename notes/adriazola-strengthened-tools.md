# Further strengthening of the Adriazola transfer (25 November 2026)

Source: the integration commit ec41c4cff2f95659bf32ea974b67a815217f0fd2,
which audits Jimmie Adriazola's reconstruction at aa9c86bf2a7d29b08575641fecea19a2a603e87c.
The three original transfers and provenance remain in the audit.
This is a further independent mathematical extension, not a claim
that the source reconstruction or either RH route is complete.

* **Fitting:** [proof](../paper/shared/residual-block-fitting-multiplicity.tex).
  For residue cardinality q, let w_q(t)=sum_h floor(t/q^h).
  If c ranges over distinct residual simple quotients of R and m_c
  counts repeats of its n_c-dimensional representation, the original
  supported defect is at most sum L_j + b sum_c n_c w_q(m_c).
  This is often much smaller than v(D0!); it vanishes whenever every
  repeat multiplicity is <q, even if there are many distinct blocks.
  The proof uses independent residual simple quotients and a
  unit-leading-monomial Newton interpolation estimate on a digit grid.
  It uses only the original pointwise determinant condition, even in
  equal characteristic. In mixed characteristic the normalized error
  is divided by v_O(ell). Arithmetic Ribet maps, local lengths and
  multiplicity bounds remain required.

* **Smith:** [proof](../paper/shared/padic-smith-local-radii.tex).
  For rectangular matrices, any nonzero d-minor polynomial controls
  the first d truncated Smith exponents simultaneously, including
  singular samples. The bound permits variable thresholds and arbitrary
  nonnegative weights, with the exact local Taylor radius and capped
  collision costs. In a generic rank-d family it removes the permanent
  nullity before bounding the additional loss. Actual Gram matrix
  polynomials and their nonzero minors/content still have to be
  constructed in W07/W10; this is not an archimedean return estimate.

* **Projectors:** [proof](../paper/shared/integral-isotypic-central-clusters.tex).
  The integral quadratic Casimir partitions the actual admissible
  lattice into exact residue clusters. Apply the AST bound in each
  smaller cluster, with a complement option, and also compare with
  polynomial separators. The result retains the dimension saving and
  balanced Fock descent. It is useful for a union of retained types,
  but does not prove that the arithmetic column lattices are admissible.

All three are written proofs of auxiliary estimates. No new whole-node
completion is claimed. For W08 the projector and Smith improvements
are reserved for the integral restriction/loss interfaces, not inserted
into the real orbital comparison without a common lattice dictionary.
The Fitting bound is a W04/W07 tool, especially for repeated cyclotomic
blocks in general Dirichlet GRH.
