# The next Selmer target: dual detection and reduction modulo every power

## Assessment

The source does control all classes modulo \(t^m\), including classes
that do not lift to integral cocycles. Finite generation of the integral
kernel alone would not do this. The needed additional algebra is supplied
by the source's complete linear-equation argument `SolCnt`; it does not
require a separate arithmetic Bockstein hypothesis.

The remaining human reconstruction is the **coupled determinant-detection
argument on the actual paired first-order dual module**, followed by the
choice of detecting auxiliary elements. This is more precise than asking
for an unspecified new uniform Selmer theorem. No characteristic-zero
rigidity theorem is applicable here: the coefficient ring is
\(A=k[[t]]\), with \(\operatorname{char}k=\ell\).

## Exact quantity and quantifiers

Fix one normalized characteristic-prime point, its odd Selmer generators
\(\kappa_1,\ldots,\kappa_g\), and finitely many auxiliary elements
\(\sigma_1,\ldots,\sigma_q\) in the prescribed cyclotomic kernel.
The source uses cocycles \(Z_m\) in the paired first-order dual matrix
module over \(A/t^m\), with its cyclotomic twist and conjugate-dual
condition. Its boundary set is \(B_m\). The detecting functional is
\[
 \lambda_\sigma(z)
   =\bigl(\operatorname{tr}(z(\sigma)\rho_1(\sigma))\bigr)_\eta,
                                                               \tag{1}
\]
where \(\rho_1\) is the first-order representation containing the
\(\kappa_i\), and \(\eta\) is its specified coefficient projection.
It is not the ordinary trace of an odd matrix against the original
block-diagonal representation.

The fixed-point bound is
\[
 \exists C\ \forall m:\quad
 \#\{z\in Z_m:\lambda_{\sigma_j}(z)=0\text{ for all }j\}
                      \leq \#B_m\,|k|^C.                    \tag{2}
\]
The source assumes `PhiCond` and `Detects`. The latter says exactly
that an **integral** paired cocycle annihilated by all (1) becomes a
prescribed integral boundary after multiplication by some \(t^s\),
where \(s\) may initially depend on the cocycle. The arithmetic
point and the finite auxiliary set are fixed before \(C\) is chosen.

`DualN` carries the same \(C\) to the auxiliary tower, with quantifiers
\(\exists C\,\forall m\,\forall N\gg_m0\). It is the term \(c_2\)
in the sum of constants defining the first Selmer estimate. This is not
a bound uniform over all points, conductors, or auxiliary sets.

## Why all modular classes are controlled

Here is the short algebra behind the actual source argument. Let \(A\)
be a complete discrete valuation ring with finite residue field \(k\).
Let \(C\) be a \(t\)-adically complete separated torsion-free
\(A\)-module, let \(C'\) be \(t\)-adically separated and
torsion-free, and let \(\Phi:C\to C'\)
be linear. Put
\[
 S_m=\Phi^{-1}(t^mC'),\qquad K=\ker\Phi.
\]
Assume \(S_1/tC\) is finite and \(B\subseteq K\) is an \(A\)-submodule with
\(K/B\) torsion. Then there is a constant \(E\) such that
\[
 \#(S_m/t^mC)\leq
 \#\bigl((B+t^mC)/t^mC\bigr)\,|k|^E
 \qquad(m\geq0).                                           \tag{3}
\]

To prove this, the images of the descending modules \(S_m\) in
\(S_1/tC\) stabilize at some \(m_0\geq1\). Division by \(t\)
is legitimate in the target: \(S_{r+1}\cap tC=tS_r\).
Induction therefore lifts the stabilized congruence from modulo \(t\)
to modulo \(t^j\): for \(x\in S_{m_0+j}\) and any \(M\), there
is \(y\in S_M\) with \(x-y\in t^jC\). Repeatedly choose these
approximants with successive differences in \(t^{j+r}C\).
Completeness and separatedness give an exact solution, so
\[
                         S_{m_0+j}\subseteq K+t^jS_{m_0}.   \tag{4}
\]
The final membership follows by applying \(\Phi\) and cancelling
\(t^j\). This step controls approximate solutions, not merely
reductions of exact solutions.

The kernel is complete, and \(K\cap t^mC=t^mK\). Hence
\(K/tK\) injects into the finite module \(S_1/tC\), and complete
Nakayama makes \(K\) finitely generated. Its torsion quotient \(K/B\)
is therefore finite. Every \(S_m/t^mC\) is finite as well: reduction
modulo \(t\) has image in \(S_1/tC\) and kernel isomorphic to
\(S_{m-1}/t^{m-1}C\). Now (4) bounds the number of cosets modulo
the image of \(B\) by
\(\#(K/B)\,\#(S_{m_0}/t^{m_0}C)\), independently of \(j\).
The finitely many smaller \(m\) are absorbed in \(E\). This proves
(3), including \(m=0\).

In the actual application, \(C\) consists of functions whose reductions
at every level are locally constant. The map \(\Phi\) lists all the
linear cocycle, coefficient-space, conjugation, and detection equations.
Every finite-level solution has a locally constant **function** lift
to \(C\); it is not assumed to have an integral cocycle lift.
The finite residual solution set follows from `finTw` and `PhiCond`.
The source proves completeness and exact reduction in `dg_abs`.
`Detects` supplies precisely \(K/B\) torsion. Integral boundaries
reduce into \(B_m\); equality or lifting of every modular boundary is
unnecessary, since replacing the image by the larger \(B_m\) only
increases the right side of (3).

This proves the required uniform counting implication once the actual
detection hypothesis is supplied. A Smith form of a finite complex would
be another valid route if that complex and its reduction comparison had
first been constructed. A Smith form of \(K\) alone misses (4).

For example, multiplication by \(t^r\) on \(A\) has zero integral
kernel but \(|k|^{\min(m,r)}\) solutions modulo \(t^m\).
The missing finite-level term is the torsion of its cokernel. More
strongly, the diagonal map \(\prod_{r\geq1}A\to\prod_{r\geq1}A\)
with entries \(t^r\) has zero kernel, but infinitely many solutions
modulo \(t\). The finite residual-solution hypothesis excludes this
example. Neither example is asserted to be an arithmetic representation.

## The genuine detection input

The original source has a specific proof, not an assumed trace theorem.
It passes to \(k((t))\), uses the full span of the two even matrix
blocks, the nontrivial cyclotomic twist, polarization, and independence
of the original odd \(\kappa_i\) modulo the prescribed boundaries.
The paired detection identity is
\[
 \operatorname{tr}(\varphi(g)\rho(g))
       +\sum_i\operatorname{tr}(\lambda_i(g)\kappa_i(g)\rho(g))=0
       \qquad(g\in\Gamma').                               \tag{5}
\]
The mixed term is essential. `DetAlg` first proves each odd
\(\lambda_i\) is a twisted boundary, then corrects \(\varphi\)
and treats its even part. `DetAsm` clears a finite set of denominators.
`DetFin` extracts finitely many detecting evaluations from a finitely
generated continuous cocycle module. `Choice` also ensures simultaneous
simple spectrum and compatible coefficient extensions for the finite
chain of points.

Ordinary trace cannot replace (5), even with full even block span.
For the upper triangular group over \(\mathbf F_5\), write
\(g=\left(\begin{smallmatrix}a&b\\0&d\end{smallmatrix}\right)\),
take \(\rho(g)=\operatorname{diag}(a,d)\), and put
\(z(g)=(b/d)E_{12}\). This is a nonzero adjoint cocycle.
It cannot be a boundary because all boundaries vanish on the
unipotent subgroup, whereas \(z\) does not. Yet
\(\operatorname{tr}(z(g)\rho(g))=0\) for every \(g\), and the
diagonal image spans both even blocks. This example does not satisfy
the additional coupled hypotheses of (5) and is not a counterexample
to the source.

**Next target.** Reconstruct `OddPart`, especially its relation-pairing
and block-principal arguments, then the short even correction in
`DetAlg`. Preserve the actual normalized-point span and independent
\(\kappa_i\), the twist, and simultaneous auxiliary choice. This
checkpoint does not claim those suppliers or the whole Selmer node are
closed. RH remains \(6/9\); GRH remains \(17/31\).

## Bounded source evidence

All suffixes below follow
`Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.`
at `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

| Module suffix | Bounded inspected ranges | Exact role |
|---|---:|---|
| `ThetaCoefficientMapEq` | 54–61, 235–264 | Tower quantifiers; paired cocycles, boundaries, \(\eta\)-trace and `Detects`. |
| `EpsilonEtaMatrices.ExistsNcardAnnihilatedCocyclesLeCoboundariesMul` | 21–130, 349–430 | Complete equations and the exact fixed-point count. |
| `DegreeCountCohomology.SolCnt` | 128–242, 293–393 | Approximation, finite generation, uniform counting. |
| `EpsilonEtaMatrices.FinTwLc` | 23–56 | Residual cocycle finiteness from `PhiCond`. |
| `EpsilonEtaMatrices.DualN` | 10–16 | Same constant passed to sufficiently large auxiliary levels. |
| `EpsilonEtaMatrices.W1BoundArithmeticRankTwo` | 40–61 | This constant is \(c_2\) in the first Selmer bound. |
| `DeterminantPadicFree.FrameWith` | 26–72 | Actual even span, twist, odd independence and paired equations. |
| `DeterminantPadicFree.MapSpan` | 14–83 | Normalized-point integral span supplies the fraction-field even span. |
| `DeterminantPadicFree.DetAsm` | 160–268 | Paired coefficient extraction and denominator clearing. |
| `DeterminantPadicFree.DetAlg` | 71–141 | Odd boundary theorem followed by an even correction. |
| `DeterminantPadicFree.OddPart` | 18–61 | Relation pairing and block-principal supplier. |
| `DeterminantPadicFree.DetFin` | 127–213 | Finite detecting set; uses the continuous cocycle module, not all modular lifts. |
| `AutomorphicDetection.Choice` | 14–40 | Shared detecting set and simultaneous eigenvalue conditions. |
| `ChebotarevFamilies.PFromAutOf` | 42–49, 83–91 | Actual finite-chain consumer. |

The companion certificate authenticates these pinned declarations and
records this assessment's scope. No Lean compilation is claimed.
Reproduce its byte checks and the exact finite-group example with
`python3 scripts/check_selmer_integral_frontier_dual_detection.py --offline`.
