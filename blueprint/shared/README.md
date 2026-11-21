# Mathematics shared by the RH and GRH routes

The two manuscripts have different final targets. Their geometric and integral
construction still shares substantial mathematics. A result is transferred
only with its hypotheses, normalization and parameter dependence intact.

| Shared result | Common proof or evidence | Ordinary RH application | Dirichlet GRH application |
| --- | --- | --- | --- |
| Weighted positive-part criterion and fixed local averaging | [Scale-averaged criterion](../../notes/scale-averaged-criterion.md) | The analytic target is the fixed zeta prime sum. | Each accuracy stage retains the chosen primitive character in a fixed positive family. |
| Positive primitive-character kernel | [Quotient comparison](../../notes/positive-kernel-transfer.md) | The conductor-one quotient has four characters. | The error retains the actual target-character order and signed projection. |
| Degree from short sections and one mean volume | [Geometric degree reduction](../../notes/geometric-degree-frontier.md) | Actual cuspidal section lattices and periods remain. | The same statement applies with the general field and weight dependence. |
| Total intersection to mean volume | [Mean-volume supplier](../../notes/mean-volume-supplier.md) | It is enough to bound the selected towers and modified weights. | The all-character route retains the required conductor and tower uniformity. |
| One test intersection and the signed determinant term | [Tower reduction](../../notes/tower-intersection-reduction.md); [common proof](../../paper/shared/tower-intersection.tex) | One normalized base test supplies the weight-dependent intersection estimate, conditional on the same tower comparison. | The same elimination retains the exact block ranks, metric and uniformity in the target family. |
| Aggregate theta energies and retained-energy compression | [Exact energy argument](../../notes/averaged-theta-energy.md) | Bounds must concern the same integral maps as the zeta comparison. | Common target bases, positive normalizers and field/rank dependence remain explicit. |
| One upper bound for all periods together | [Centered global-energy reduction](../../notes/centered-global-energy-reduction.md); [common proof](../../paper/shared/period-bessel.tex) | A calibrated Bessel bound controls centered energy and survives the actual joint cuts with explicit mass loss. | A signed orbital quadratic-form estimate is a sufficient supplier for the same normalized maps; it remains open. |
| Centered slope comparison and optimum normalization | [Centered frame theorem](../../notes/frame-degree-compatibility.md) | Use the minimum with the older estimate; separate arithmetic errors remain. | The same inequalities compare the general quotient sources and final target. |
| Determinant, discarded-degree and integral-index corrections | [Covolume comparison](../../notes/covolume-defect-budget.md) | Four retained characters do not bound an integral index. | The full rank weights and type indices must be retained. |
| Classical Galois representations and period comparison | [Adopted replacement](../../notes/classical-galois-substitution.md) | The selected growing fields still need their stated compatibility. | One representation supplies all required weak correspondences and period laws. |

## Concurrent research

The [RH program](../rh/program.md) and [GRH program](../grh/program.md) are
maintained together. Each new shared deduction records its proof, exact
source evidence where used, and its remaining inputs. Before adoption, both
applications are checked for changes in hypotheses or constants. A new
reduction can simplify an open node without completing that node.

The [common technical chapters](../../paper/sections/) remain the detailed
mathematical library. Small proof fragments used literally by both papers
belong in `paper/shared/`; route-specific exposition belongs in its own
manuscript. Source inspection and verification records remain outside the
papers. The [progress table](../progress.md) counts each route separately;
overlapping shared results are never added to form a proof percentage.
