# Actual valid-cut top lift

## Result and scope

**Closed local obligation, independently reviewed.** The new standard
proof constructs the actual valid-cut top-lift supplier
`TL.TopLiftExists3` with `Cb=11`. For each original word of length m,
the lift has original `InDDPlus` cost `(m*d, 11*m*(r+1)*d)`, where
`d=2*r+k+1`. It retains every tensor component, both signs, the old-word
rational factors, the weighted adjoint and the prescribed radial action.
Only full leading determinant, its conjugate and full Gram denominators
occur. The coefficients extend across zeros of internal leading minors.

This closes no whole W06/W08 node. The exact arithmetic period maps,
integral theta lattices, global rational returns, and uniform Gram
estimates are separate obligations. The constant 11 bounds differential
complexity, not norms of moving compact-type inverses.

## Decisive construction

The established cofactor/compact-Capelli construction (recovered Section84)
gives actual smooth equivariant fibre fields on the whole positive Gram
domain. For the original sign `sigma=(-1)^(k-l0)`, the signed compact
Capelli spectrum is `sigma*prod(Y+rho_i)`. Polynomial interpolation gives
the prescribed inverse only on the original covariant common-type fibres;
unused right constituents need not be invertible. The sphere homogeneity
proof supplies the original `FibBound`, including order zero, with its
allowed dependence on fixed representations and spectral parameters.

The new unbounded-word argument keeps each updated slope in the span of
compact-fibre commutators and two scalar terms. The plus update retains
`(Y-a)^-1`; the minus update retains
`q_w(a-1)/(a-Y-1)*xi_w(a)*xi_w(a-1)`. Taking the actual weighted adjoint
introduces exactly `-|w|*TT'/(bar(zeta)*G)`. Thus every letter has order
at most d and numerator degree at most `9*(r+1)*d`, independently of the
old-word length. Composition adds only `2*(r+1)*d` per letter. This is the
linear budget required downstream; naively expanding successive frames
would not establish it.

The basic letter lift is constructed from the actual full Capelli
operator by finite determinant conjugations and exact coefficient
extraction. The two first-column lifts use adjacent spectral parameters
and the original compact inverse. No intermediate leading-minor inverse
is introduced.

## Exact interface restriction

The source `TL.TopLiftExists3` requires `1 <= l0 <= k`.
The separately named `KB.TopLiftExists2` omits those bounds. The new proof
establishes the former. Every original `KB.Pl` includes the bounds (and
`k>=2`), so the actual place consumer can use the valid-cut supplier.
No unrestricted source predicate is silently marked closed.

## Evidence

- Proof: `paper/shared/global-norm-frontier-top-lift.tex`.
- Exact source ranges: accompanying references and certificate.
- Checker: `scripts/check_global_norm_frontier_top_lift.py`.
- The script authenticates pinned source bytes and performs exact finite
  noncommutative, scalar-differential and degree-budget diagnostics. These
  are diagnostics, not a Lean build or a substitute for the all-rank proof.
- Independent mathematical and exact-consumer review is recorded in the
  companion review certificate.

## Next frontier

Apply the accepted local top lift, terminal degree, Fourier, off-diagonal,
block-growth and finite-decay suppliers to the actual global kernel
consumer. The next research step is to locate its first genuine
rational-return/period-Gram requirement, with original normalizers and
moving arithmetic parameters; do not spend another cycle optimizing the
closed local inequalities.
