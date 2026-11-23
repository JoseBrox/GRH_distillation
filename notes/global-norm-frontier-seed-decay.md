# Actual weighted arithmetic seeds

## Frontier and result

**Classification: closed supplier, independently reviewed.**
The precise frontier was the original `WuDecay` package for every
existing `HidaSetting` under its `GapHyp`: weighted L1 for the original
Whittaker/Bessel seed with exponent
`N1 = 4 n^2 sqrt(2 max_v q_v)`, and a bounded compactly supported exact
right convolution reproducer. The new proof supplies both and also
integrability of the exact original coefficient `phInf`.

This is an implication from the actual setting, which already contains
the prescribed continuous equivariant seed of quotient L2 norm one and
its original formal-degree convolution equation. It does not construct
that setting and does not claim a uniform bound for the weighted L1
integral, its compact cutoff, or its reproducer. W06/W08 remain open.

## Direct proof and removed dependency

The actual gap is `n>=1801`, adjacent tail gaps at least `16 n^19`.
The ordered signed parameter makes every noncompact gap at least this
large, including comparisons with the compact head. The previously
proved actual smooth coefficient decay and elementary Cartan integration
give weighted L1 of the original matrix coefficient, with the exact
weight exponent. Every formal degree and Haar scalar remains unchanged.

Its normalized coefficient p is a self-adjoint convolution idempotent.
The identity `p * delta_g * p = <w,sigma(g)w> p` identifies any vector
in its induced-space range with a copy of the same discrete series.
Evaluation on smooth vectors and the previously checked Bessel
multiplicity-one theorem make this range one-dimensional. Thus for the
already given normalized W, `P beta = W <W,beta>`.

Choose `beta = 1_E W`, with E compact in the actual quotient and
`A_E = integral_E ||W||^2 >0`. Weighted Young/Tonelli gives

`A_E integral nu^N ||W|| <= (integral_E nu^N ||W||) (integral |p| M^N)`.

Both right factors are finite. No new local Bessel period nonvanishing
theorem is used. The original setting's own normalization is retained;
the argument does not infer it from a different map.

A compact K-conjugation-invariant smooth approximate identity acts by a
scalar tending to one on the multiplicity-one lowest compact type.
Dividing one nonzero scalar gives a compact function alpha fixing the
original w exactly. The same induced intertwiner proves `R(alpha)W=W`.
Continuity and full support of the correct quotient Haar measure give
the equality at every group point. Every integral is absolutely
convergent, and the auxiliary probability K average changes no source
measure.

## Actual downstream use

`FoldOK` requires precisely the resulting compact reproducer and weighted
integral. Its arithmetic folding argument also uses the finite local
support and polynomial rational multiplicity; those actual steps are
the next current attack. `OOLintSumC` then uses the exact finite-column
majorant and finite positive-Levi fibre count. Only after those proofs
may one assert absolute convergence of all original rational returns
and unfold the actual period Gram operator.

Important interface audit: `MassDataConc.bC` overrides raw `KVOf` by
`Sig/rho0`. Therefore its tautological `InForm` is not a raw kernel/Gram
identification. The genuine subsequent frontier is actual `SigRowsC`
and the scalar-normalized `RowFormC`, with all phases, class torsors,
finite volumes and rational returns retained.

## Verification scope

The shared TeX is the proof for all original settings, dimensions,
places and words. Its checker authenticates bounded pinned sources and
the primary lowest-type reference, checks all-rank exponent budgets by
nonnegative polynomial certificates, and tests the exact projection,
corner and weighted-convolution identities independently on a finite
nonabelian group. Finite diagnostics are not proofs of the Lie-group
statements. No Lean build is claimed.
