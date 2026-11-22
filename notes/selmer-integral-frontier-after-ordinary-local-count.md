# The next Selmer supplier after the ordinary local count

## What is now proved

The companion [ordinary local count](selmer-integral-frontier-ordinary-local-count.md)
supplies the original ordinary-place factor, with
\[
 C_v=\sum_{i<j}w_{ij}c_{ij},\qquad
 \#Z_{v,m}\leq |k|^{m(n+\nu)(d_v+1)+C_v}.
\]
The point, coefficient field and odd family are fixed first. The
constant works for every truncation and every auxiliary level.
The proof counts the actual finite modules, retains their integral
defect lengths, and assumes no lifting of their cocycles.

The first global Selmer estimate still has other factors. Their exact
consumer chooses
\(C=c_1+c_2+c_0+\sum_v C_v+\sum_j C_{q,j}\)
before choosing the truncation. The source then obtains, for each
truncation, all sufficiently large auxiliary levels. Its leading
dimension is \(n[L^+:\mathbf Q]+nq_{\rm aux}\).

## Exact next inputs

The next focused reconstruction should combine the finite matrix
invariant estimates, then assemble the already developed detecting
count with the auxiliary-level descent. The required statements are:

| Input | Actual object and quantifiers | Dependency to retain |
|---|---|---|
| Global invariants | Skew matrices in the primal first-order module, fixed by the full first-order representation; one bound \(|k|^{c_1}\) for all \(m\). | Odd characteristic and the original full even matrix span. |
| Distinguished-place invariants | Cyclotomically twisted fixed matrices in the paired dual module; one bound \(|k|^{c_0}\) for all \(m\). | The original condition on the subgroup \(D\) displayed below. |
| Auxiliary invariants | Fixed matrices in the paired dual module at each chosen simple-spectrum element; bound \(|k|^{mn+C_{q,j}}\) for all \(m\). | All original eigenvalues distinct in the fraction field; block separation alone is not substituted. |
| Dual detecting count in the tower | Cocycles satisfying the two auxiliary local boundary conditions; at most \(|k|^{c_2}\) times the boundary count, for every \(m\) and eventually every \(N\). | The complete congruence equations, exact descent, eventual matching of auxiliary evaluations, and original polarization. |

The distinguished-place condition is precisely
\[
 \bigl[\bar\varepsilon(g)\rho(g)Z=Z\rho(g)
       \text{ for every }g\in D\bigr]\quad\Longrightarrow\quad Z=0
             \qquad\bigl(Z\in M_n(k[[t]])\bigr).       \tag{1}
\]
It is an assertion over the actual characteristic-prime coefficient
ring. It is not a characteristic-zero rigidity assertion. The source
first applies (1) to the \(\epsilon'_i\) coefficients of an invariant
paired matrix, then to its \(\eta\) coefficient. The finite-level
bound is obtained separately from the finite matrix equation count;
vanishing of the integral kernel alone does not erase its torsion
correction. Construction of the actual point satisfying (1) must
remain visible when the normalized-point hypotheses are discharged.

The earlier detecting-count checkpoint identified the complete
linear-equation argument that handles all finite-level cocycles.
Its then-open odd/even paired detection, integral assembly, finite
selection and coefficient transfer have now been proved in the
corresponding later notes. They must be reused. In particular, there
is no reason to introduce a new unspecified arithmetic Bockstein
assumption. The remaining tower bridge must retain the same constant
through descent and the eventual auxiliary-evaluation identity.

This checkpoint locates the next exact supplier; it does not claim
that these remaining estimates, the patched-module construction, or
the full first Selmer bound have been reconstructed. Ordinary RH
remains **6/9** and Dirichlet GRH **17/31**.

## Bounded source evidence

All source modules below have prefix
`Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.`
and revision `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

| Module suffix | Inspected ranges | Exact role |
|---|---:|---|
| `EpsilonEtaMatrices.W1BoundArithmeticRankTwo` | 40--61 | Four remaining factors, one total constant, tower quantifiers. |
| `EpsilonEtaMatrices.CommutingMatrixOffdiagZero` | 158--188 | Global skew invariant bound and its exact integral-kernel input. |
| `EpsilonEtaMatrices.Rho1MapReductionLevel` | 42--64, 66--91 | Distinguished paired coefficients and fixed-module count. |
| `PairedDualFirstOrderDualMatrixSpace` | 292--294 | Exact distinguished-place condition (1). |
| `EpsilonEtaMatrices.FinrankCentralizerW1Le` | 106--131 | Auxiliary simple-spectrum estimate with leading rank \(n\). |
| `EpsilonEtaMatrices.FixBdQZero` | 181--206 | Finite matrix-equation count, including integral torsion. |
| `EpsilonEtaMatrices.ExistsNcardAnnihilatedCocyclesLeCoboundariesMul` | 349--385 | Exact all-truncations detecting count from complete equations. |
| `EpsilonEtaMatrices.DualN` | 10--16, 27--38, 67--100 | Same detecting constant, tower descent and eventual evaluation. |

The companion provenance certificate records the full pinned file
hashes and these bounded excerpt hashes. No new theorem or Lean
compilation is claimed here.
