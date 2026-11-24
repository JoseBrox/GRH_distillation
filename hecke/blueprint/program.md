# Hecke GRH proof program

The preferred route is arithmetic; the spectral trace route is
an optional alternative. The eight stable nodes are:

| ID | Responsibility | State | Exact output or remaining task |
| --- | --- | --- | --- |
| H01 | Hecke analytic setup | Cited | Classical continuation, functional equation, norm normalization, fixed-character zero count and explicit formula. |
| H02 | One-sided zero detection | Proved | Detecting profiles, exact obstruction exponent, arbitrary polynomial grids and three compact integrated tests. |
| H03 | Degree-one prime reduction | Proved | Full smoothed spectral sum equals degree-one prime deficit plus bounded error. |
| H04 | Galois-field reduction | Proved | Positive induction identity and zero-order inequality for norm pullbacks of every unitary Hecke character. |
| H05 | Positive arithmetic kernels | Proved | Nonabelian induction/inertia Fourier kernel for genuine finite-order Hecke functions; nonnegative weighted split-prime coefficients for all unitary characters. |
| H06 | Rational and abelian calibration | Cited | Alpöge's independently verified theorem, abelian factorization and imaginary norm twists in their precise scope. |
| H07 | Actual arithmetic supplier | Open | Prove the fixed-field weighted split-prime estimate, starting with the S3 benchmark. |
| H08 | Actual spectral trace supplier | Open (optional) | Prove the normalized one-sided global/local trace budget on actual compatible operators, with full edge convention. |

H01 supplies H02 and H03. H04 reduces the field scope and H05 supplies
positive kernels for H07. H07 then supplies the estimate to H03 and H02,
proving the reduced critical-line assertion; H04 transfers it to all
number fields. H08 is an alternative input to H02. H06 calibrates
the constructions; it does not close H07 or H08.

The finite-order-only program and the S3 test case are milestones
within H07, not extra proof-completion nodes. The exact quantifiers and
acceptance conditions are in [open frontier](../notes/open-frontier.md).
See [manuscript](../paper/main.md) and [progress](progress.md).

A finished node is a written implication or cited input, not an assertion
that its open antecedents hold. No part of an earlier proof-map count has
been changed.
