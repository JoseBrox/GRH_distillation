# The integral Selmer frontier: the characteristic-prime fibre

## Status and exact target

This checkpoint identifies the arithmetic supplier still needed by the actual
rank-three Selmer argument. It proves a small obstruction to discarding that
supplier, and traces its source proof to the characteristic-prime propagation
theorem. It does not close the RH or GRH Selmer node, does not assert an error in
the original source, and does not claim a Lean build.

All Lean references below are to
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, under
`Development.AutomorphicArithmetic.AutomorphicVarieties`. The companion
certificate records complete file hashes and bounded inspected ranges.

Write \(\mathcal O\) for the coefficient discrete valuation ring, \(\pi\) for
its uniformizer, and \(E\) for its fraction field. The source needs finiteness
over \(\mathcal O\) of the weight-zero subalgebra of the **actual normalized
global deformation ring** \(S\). This is the assertion `FinA`, quantified over
all choices of its universal local ring and normalized universal global ring
(`AutomorphicCases.AutomorphyUnramifiedCoefficients`, 12–13).

The ring \(S\) represents the full normalized global deformation problem:
`UnitaryThreeGroups.ConjStable`, 43–49, and `GRepresents`, 75–105. Its stated
structure does not impose flatness or reducedness over \(\mathcal O\). The
local crystalline component being flat does not make an arbitrary global
equation quotient flat. In particular, the already proved crystalline and
tangent comparisons do not supply this integral finiteness statement.

## Why rational rigidity cannot supply it

For an integer \(M\geq1\), put
\[
 S_M=\mathcal O[[x,y]]/(\pi^M x,\pi^M y),
 \qquad \operatorname{wt}(x)=1,\quad\operatorname{wt}(y)=-1.
\]
The ambient power series ring is flat over \(\mathcal O\), and both equations
are homogeneous. The augmentation sends \(x,y\) to zero. Nevertheless:

1. \(S_M[1/\pi]=E\). Every characteristic-zero point is the augmentation,
   and its characteristic-zero tangent space is zero.
2. Its completed weight-zero subring is
   \(\mathcal O[[z]]/(\pi^M z)\), with \(z=xy\). Indeed, every weight-zero
   monomial is \((xy)^j\), and the coefficient of every positive such monomial
   is taken modulo \(\pi^M\). Its reduction is \(k[[z]]\), so this subring
   is not finite over \(\mathcal O\).
3. Already \(S_1\) is reduced: in \(\mathcal O[[x,y]]\),
   \((\pi x,\pi y)=(\pi)\cap(x,y)\), an intersection of prime ideals.
   Thus taking radicals alone does not remove the obstruction.
4. The \(\pi\)-torsion-free quotient is \(\mathcal O\). It loses the entire
   negative augmentation conormal summand
   \[
   (\ker(S_M\to\mathcal O)/\ker(S_M\to\mathcal O)^2)_{-1}
      \simeq (\mathcal O/\pi^M)\,y.
   \]
   Saturating the global equations can therefore discard precisely the kind
   of integral tangent information used to bound Selmer length.

There is also an explicit characteristic-prime curve:
\(S_M\to k[[t]]\), \(x\mapsto t\), \(y\mapsto t\), \(\pi\mapsto0\).
It has both positive and negative coordinates nonzero and sends \(z\) to
\(t^2\). This curve is invisible after inverting \(\pi\).

This is an algebraic obstruction, not a Galois counterexample. It isolates the
extra statement an arithmetic proof must establish. A shortcut using a
torsion-free ring would require proving that property for the actual
weight-zero ring. Neither the universal ring definition nor the comparisons
already completed provide it.

## How the actual source excludes these curves

The source proves `FinA` using equal-characteristic curves, not only its
characteristic-zero points:

| Step | Mathematical content | Exact source |
|---|---|---|
| Uniform characteristic-prime assertion | There is one finite-index subgroup on which every ordinary deformation into every complete characteristic-\(\ell\) discrete valuation ring has the base characteristic polynomials. | `CurveDVRSpecialization.RatTorsionFree`, 21–32 (`FinEnd`) |
| Curve exclusion | These characteristic-polynomial identities force the diagonal entries to equal their base values and force every such point to be upper or lower triangular. | `CurveDVRSpecialization.GfResZpow`, 179–205 |
| Integral finiteness | Every nonconstant weight-zero generator lies in \(\sqrt{\pi S}\); contraction to the weight-zero ring and topological Nakayama give finiteness over \(\mathcal O\). | `CurveDVRSpecialization.FinCrit`, 122–186 |
| Source of the uniform assertion | `FinPt` on the linked frame supplies `FinEnd`, with the same finite-index subgroup for all coefficient curves. | `CurveDVRSpecialization.FinEndOfFinPt`, 9–48 |
| Source of `FinPt` | An ideal finite over the fixed-weight special fibre contains every off-triangular prime; this forces the characteristic polynomials of every coefficient curve to be the base polynomials. | `CurveDVRSpecialization.PropagationTheoremGL2`, 47, 74–84; `FinPtOf`, 183–260 |

The quantifier over characteristic-prime curves is essential. In the example
above the weight-zero generator \(xy\) is not in \(\sqrt{\pi S_M}\), as its
image \(t^2\) demonstrates. The construction therefore fails the precise
curve condition that the source uses; it is not an objection to that source
argument.

## The remaining arithmetic theorem, located precisely

The rank-three propagation theorem is a proved source declaration, not a
definition whose name is being used as evidence. Its final assembly is
`CurveDVRSpecialization.PropagationTheoremGL3`, 213–229. Its hypotheses are
rank-two component control, a finite ordinary automorphic quotient, propagation
at irreducible points, propagation through chains of reducible nonsemisimple
points, and a sufficiently large automorphic seed. It concludes that all
irreducible components are automorphic and that all off-triangular components
satisfy the required special-fibre finiteness condition.

`CurveDVRSpecialization.AbsMain`, 19–30, applies this theorem to `ModIn` data.
The latter data are constructed in
`ModularityArgument.ThresholdArguments.DenseThresholdCases.PrLinkedEnd`,
22–40, from the ordinary modular quotient theorem `ModUAlt`.

The difficult extra content in that theorem is explicit:

* `WeilGroupCharacters.UniversalOrdinaryDeterminantRing`, 284–298, defines
  propagation at an irreducible coefficient curve and along **arbitrary
  finite chains** of reducible coefficient curves. The linking primes have
  nonsemisimple Cayley–Hamilton algebra; they need not correspond to
  irreducible characteristic-zero representations.
* `PatchingModules.AutomorphicDetection.PfromAut`, 9–10, supplies the
  propagation theorem by the actual theorem `pFromAut_of`, using
  normalization, simultaneous detecting auxiliary primes, two cohomological
  bounds, and the patched-support theorem.
* `PatchingModules.ChebotarevFamilies.PFromAutOf`, 30–114, performs the
  simultaneous construction for the **whole finite chain**. Lines 116–131
  turn its conclusion into the two propagation statements.
* The patched-support theorem reaches its decisive local inclusion at
  `PatchingModules.AutomorphicDetection.LiftPt`, 139–175: a prime supporting
  an irreducible deformation of the required dimension must lie below every
  stable or nonsemisimple linking prime. Its local input is `galOut`, from
  `PatchingModules.AutomorphicDetection.GalOut`, 16–43. The reducible case
  uses `presOut1`, in addition to the ordinary irreducible case `presOut0`.

This is the next direct research target: reconstruct that local prime
inclusion for the rank-three ordinary deformation problem, and match the
actual patched automorphic modules supplying its dimension hypotheses.
The rational Selmer vanishing already available concerns characteristic-zero
self-extensions. It does not establish this statement about the entire
characteristic-prime component chain. The present checkpoint preserves that
distinction and the exact consumer to which a new proof must apply.

## Verification scope

The companion checker verifies pinned source blobs and exact polynomial
identities underlying the weighted counterexample. The mathematical
arguments about formal power series, reduction, conormal modules and the
source dependency contracts are given above. Source-byte verification is not
a Lean kernel check; the global arithmetic propagation input remains open in
the human proof. Existing node counts remain **RH 6/9; GRH 17/31**.
