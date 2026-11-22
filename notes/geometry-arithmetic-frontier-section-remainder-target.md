# The remaining arithmetic section estimate

## Status and next target

The compact-model mixed-integral dictionary, common vertical curvature,
and signed boundary comparison have now been supplied under the original
geometric data; see
[the compact-model checkpoint](geometry-arithmetic-frontier-compact-model-stokes.md).
The next geometric target is the **arithmetic degree of the actual section
lattice**, including its finite jet and height estimates. The existing
[finite section bound](finite-section-jet-bound.md) controls dimension
after its geometric hypotheses are supplied. It does not control the
arithmetic degree of that lattice. The
[geometric degree checkpoint](geometric-degree-frontier.md) already
records the subsequent scalar rearrangement and averaging.

This note locates the exact remaining source obligation and preserves a
smaller constant already present in the source. It proves no new supplier
and changes no whole-node status.

## Exact dependency to reconstruct

All source references below use
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The actual component estimate follows this chain:

| Source declaration | Bounded source evidence | Role |
|---|---|---|
| `HSShortRun.hsClaim_short_alt_alt` | `ThirdPlaceSeries.ExistsDegreeParametersBound`, 34–70 | Final component parameters and displayed remainder |
| `HSShortRun.hilbertSamuel_estimate_at_level` | `HodgeBundleWeights.ExistsDegreeParametersBound`, 33–76 | Actual frames, cusp lattices, and their short spanning families |
| `HSShort.hsClaimS_component_geo` | `HilbertSamuelComponentShortBasisBound`, 26–37 | Transfers model degree, height and integral lattice to the component |
| `HSShort.geoBound_of_quoted'` | `ArithmeticHilbertSamuelBound`, 19–20 | Calls the explicit estimate, arithmetic Bertini, height identity and complementary-lattice slope bound |
| `HSShort.GeoBound` | `HermSysHypOneLeLambdaZero`, 253–271 | Required arithmetic degree inequality under the original geometric hypotheses |

The last obligation retains a totally complex number field; the original
birational map; two nef and big line bundles; multiplication stability
and norm estimates; short integral spanning families at levels
\(0,D,T\); and the identification of the geometric height. In the
component application it also retains the actual arithmetic model,
canonical line-bundle identification, frames, metric and lattice
identifications. The cited source assembly depends on its package of
quoted theorems. An imported statement or an abstract degree inequality
does not supply those hypotheses in the new human proof.

The underlying finite jet obligation is explicit in
`IntegralBound.HermObject`, 34–70. It uses full integral section and
evaluation lattices, successive jet maps with the correct kernels,
integral lifts of every product-lattice jet, two-sided point-height
bounds, a lower degree bound for the evaluation lattice, quantitative
archimedean lifts, and short spanning families for the remaining deep
jet space and the whole section space. In particular, a generic-fibre
rank calculation cannot substitute for those integral and metric data.

The efficient next research step is to reconstruct this actual arithmetic
jet estimate and its application to the supplied component data, then
check the arithmetic Bertini and height suppliers used in that
construction. The analytic signed limit need not be reopened.

## Preserve the smaller constant already available

Write \(D\) for the flag dimension, \(T\) for the section level,
\(P\geq0\) for the source size parameter, and \(\kappa\geq0\) for
the weight parameter. Under the **same retained hypotheses**,
`hilbertSamuel_estimate_at_level`, 44–52, already gives
\[
 \Lambda_D=\Lambda_T=\exp(P\kappa),
 \qquad J=D P\left(\frac{\kappa}{T}+1\right).
\]
The later wrapper states the weaker allowance
\[
 J\leq 4\left[D P\left(\frac{\kappa}{T}+1\right)+TP\right]
          +2DP\frac{\kappa}{T}.
\]
Its proof calls the earlier theorem at lines 59–64 and merely weakens
this bound at lines 65–70. The difference between the displayed upper
allowance and the actual value is
\[
 3DP\left(\frac{\kappa}{T}+1\right)+4TP
       +2DP\frac{\kappa}{T}\geq0.
\]
Thus the direct value should be preserved when the section estimate is
reconstructed; no additional \(4TP\) allowance is required at this
particular step. Other remainder terms remain unchanged.

More precisely, `HSClaim`, 12–22, gives this \(J\) coefficient
\(-B\delta/r\), where \(B=\binom{T-1}{D}\), \(\delta\) is the
component degree and \(r\) the section rank. Replacing the wrapper's
larger allowance by the actual \(J\) raises its lower bound for degree
divided by rank by exactly \((B\delta/r)\) times their difference.
This is an existing source refinement, not a proof of the arithmetic
degree estimate or its geometric inputs.

## Verification scope

The accompanying script authenticates seven pinned source blobs and the
exact bounded ranges above, and checks the constant difference and its
rank-weighted coefficient symbolically. The certificate records full
source and artifact hashes. It does not build Lean, construct the
arithmetic models, prove the quoted arithmetic theorems, or discharge
the finite jet and height hypotheses.

Reproduce with:

```sh
python3 scripts/check_geometry_arithmetic_frontier_section_remainder_target.py --offline
```
