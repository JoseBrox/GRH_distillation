# A discriminant denominator for actual harmonic chart values

> **Later status (23 November 2026).** The [full primary trace](geometry-arithmetic-frontier-primary-trace.md) and [actual integral theta denominator](geometry-arithmetic-frontier-actual-theta-denominator.md) were subsequently constructed. The “remaining significant step” discussion below refers to this earlier checkpoint; do not infer that these suppliers are still missing. The final theta-map compatibility and norm budget remain open; see [current state](current-state.md).

## Status and relevance

The shared proof establishes a local supplier for the theta denominator:
under the original integral formal-biextension chart data, including its
integral trace-one element, `Delta^d` clears every integral pluriharmonic
column value of total degree `d`. Here `Delta=|disc(E)|`.

This is new work inside the open arithmetic-geometric supplier. The old
sharp ramified estimate requires different ideals, place idempotents, and
pairing primes under complex conjugation. The coarser result has a short
trace-projector proof and uses exactly the discriminant power already in
the proposed integer `intZ`. It does not improve a previously closed
real-variable estimate or infer short generators from a full lattice.

The actual normalized theta trace, the determinant-ideal comparison of a
scalar, global integral models, spanning, and the raw theta norm remain
separate inputs. No whole RH or GRH node is closed by this result.

## Exact new argument

The canonical gauge gives the actual integral graph lattice

`H_R={(u,phi-Su): u,phi in R^g}`.

Its original integral adjoint cocycle proves
`S A_a - A_bar(a)^t S` integral. Thus the original `O_E` action preserves
this lattice. This is an explicit free lattice; no unproved integral
extension splitting or choice of an `O_E` basis is inserted.

An integral trace basis has Gram determinant `disc(E)`. The adjugate makes
`Delta` times the dual basis integral. Consequently `Delta e_tau` preserves
`H_R`. Applied to `(u_tau,-S u_tau)`, it produces an integral eigenlift of
`Delta u_tau`, with no local different or Galois prime matching.

The adjoint pairing forces every contraction between the vertical part of
this lift and a horizontal direction to vanish outside conjugate CM
types. The ordinary Wick expansion therefore has correction operator
`Q=sum c_(tau,i,j) sum_b d_(tau,i,b)d_(bar(tau),j,b)`.
Pluriharmonicity makes `Q P=0`. All terms `Q^r P/r!` for `r>0` vanish in
the fraction field before taking integral values. The surviving expression
is an integral linear combination of ordinary differential words.
Homogeneity then gives the factor `Delta^d`.

## The prime 2 and the trace-one hypothesis

No divided differentiation is used. Graph stability takes the degree-two
coefficient of an exponential whose argument has order at least two; that
coefficient is the argument's coefficient, without a factor `1/2`.
The conjugated first-order connection has integral coefficients by the
logarithmic derivative of integral unit cocycles. All factorial terms in
normal ordering vanish by harmonicity. This covers residue characteristic
2 **under the retained original hypotheses**.

In particular the theorem explicitly requires the original `w in O_E`
with `w+bar(w)=1`. This is not true in every CM order: in `Z[i]`, every
trace is even. We do not replace it by `w=1/2`, and do not assert that the
discriminant factor clears a different, nonintegral choice of gauge.
The source's `Host.w0` and `cmHostUnit_add_conj_eq_one` supply this element
in the original application.

## Bounded source contract

Every module below is pinned to `jsmorph/rh` revision
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. The checker records complete
file hashes and bounded excerpt hashes; none of this is a Lean build.

Let `W` denote
`ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.TaylorDiscriminants.WickVanishing.`,
`H` denote
`ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.PullbackSections.HolomorphicFamilies.`,
and `R` denote
`Development.AbelianVarietyTheory.Proofs.RingsOfIntegers.`.

| Source declaration | Bounded range | Role and exact restriction |
| --- | --- | --- |
| `W.HStable.M_int`, `gauge_stable` | 270–334 | Actual graph lattice stable under the given integral adjoint action. |
| `W.GaugeBilinearTermEqNegDoubleSum.gaugeBilinearTerm_eq_neg_double_sum`, `coeff_expS_two` | 157–163, 223–240 | No hidden factor 2 in `S`; degree-two exponential coefficient is unchanged. |
| `H.BiextCoeffSecondLinear.eigLift_core` | 169–238 | Original integral graph/eigenlift mechanism; the new proof replaces normalized integral idempotents by `Delta e_tau` and scales the direction. |
| `W.SigCancel.rel_hL` | 149–200 | The integral trace-one element is used; logarithmic derivatives give the integral scalar term. |
| `W.ExpConjConnectionIntegral.exp_conj_connection_integral` | 40–90 | Explicit integral first-order coefficients; no factorial or 2 inversion. |
| `W.LemmaH.ordNabla_expand` | 34–67 | The only `1/r!` occurs in the contraction expansion over the fraction field. |
| `W.LemmaHCols.lemmaHCols_of` | 223–238 | Multi-column contraction is the sum over columns, annihilated by the actual harmonic condition. |
| `W.HarmonicValueIntegral.E_nabla`, `E_nablaPoly` | 89–113, 123–147 | Graph restriction identifies the horizontal word value with the actual invariant differential value. |
| `H.ChartValJ` | 31–55, 95–158 | Original harmonic-value consumer; specialize the error `psi` to zero and replace directions by `Delta u`. |
| `R.IntegralChartFormalBiextensionGaugeBound.integralBiext_gauge_eig_bound` | 50–108 | Original integral chart supplies the integral biextension, canonical gauge and eigenaction. |
| `R.HarmonicValueIntegralOfUnitDiscriminant.chBound_zero_of_isUnit_discr` | 168–234 | Actual integral `uvecT` and finite-place embeddings; use of the retained `Host.w0`. |
| `R.HarmonicValueBoundOfColumnProducts.chBound_of_columns` | 18–22 | Converts all column-product bounds to the original `ChBound`; does not alter the valuation set. |
| `H.ChartValueRamifiedOfLifts.sum_pairMin_le` | 110–125 | The actual row-degree hypothesis sums to `DF`; the new proof uses its total degree, not `pairMin`. |
| `DivisorProofs.IsIntegralFourierCoeffClassIndicatorLevelPoint.intZ` | 23–30 | `Z=|Q| Delta^DF M^DF`, already sufficient for the new local loss. |

## Exact application and what remains

For normalized valuation `v/e`, `e>0`, the new bound is
`ChBound C e (d*v(Delta)/e) w n`. The original integral chart and row
homogeneity provide every hypothesis of the theorem. The factor
`Delta^d` in `Z` cancels this loss at every place. We do not claim the
stronger original bound involving half the degree and a local different.

The remaining significant step is the **actual normalized primary-torsion
sum**, with its index cancellation and adapted-lattice determinant factor.
The current exact target is recorded separately in
`notes/geometry-arithmetic-frontier-theta-denominator-target.md`.
In the level branch, `R.ShortBoundOfTrivAt` uses primary kernel constancy
to cancel the primary part of the index. Away from the level,
`DivisorProofs.ShortSeriesBoundCoprimeTorsionMul` uses the normalized
primary-kernel identity and the determinant/type-norm comparison. Neither
statement follows merely because a sum is a trace: on `R x R`, the
normalized trace of `(1,0)` is `1/2`.

Once those two actual local suppliers are established, one copy of `Z`
already suffices for the original global assembly: the stronger local
conclusion `smul_nonneg_of_shortRule` in `SmulIntZSqNonnegOfSqDvd` has no
prime-square restriction, and the outside-level theorem also uses one
`Z`. This is a conditional assembly simplification, not a proof of either
remaining local theta trace.

## Verification scope

`scripts/check_geometry_arithmetic_frontier_discriminant_clearing.py`
authenticates the pinned source ranges and the proof/reference files.
It checks integral trace projectors and nonintegral stable graph lattices
over explicit quadratic fields, exact harmonic normal-ordering identities
including nonintegral contraction coefficients at 2, homogeneity, and
negative controls. These finite checks supplement the written proof;
they do not prove the general formal-biextension identities or build Lean.
The trace-one negative control prevents extending the theorem to arbitrary
CM data. The normalized-trace negative control prevents treating the
global theta denominator as already closed.
