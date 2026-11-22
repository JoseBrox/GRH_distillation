# The original tensor projection estimate

## A missing quantitative supplier reconstructed

The theorem in
`paper/shared/global-norm-frontier-tensor-projections.tex` proves the
original algebraic estimate needed in the first-length recursion:
\[
 \sum_s\|p_s(e_c\otimes v)\|^2
                   \le(6B_0)^{2(2r+2)}\|v\|^2,
\]
and every projected vector has the original level increased by at most
two. This keeps the given representation, tensor decomposition,
indefinite Hermitian form and signed isometries. It does not replace the
projections by arbitrary orthogonal projections in a different norm.

The estimate holds in the exact source range: $n=2r+k+1$,
$B_0\ge10^6n^7$, initial level $j\le4n^2$, spectral gaps at least two,
the original positive compact cluster and separated negative parameter
interval. The exponent depends on $m=2r+2$, not on the much larger
compact cluster. This is a proved modular supplier, still conditional
on the original tensor decomposition as is the source theorem itself.

The Casimir identity was already reconstructed in Lemma `dc-derivative`
of recovered chapter 77. It is not counted again. The new work here is
the explicit cancellation of its large diagonal terms, the resulting
small off-diagonal estimate, and the complete application to the
original indefinite projections.

## The proof in five steps

1. For the lowest compact weight
   $\Lambda=\mu+\rho-2\rho_K$, its compact scalar $\kappa$ and the
   full scalar $c_G$, the quadratic parameter terms cancel:
   \[
    2\kappa-c_G-\|\Lambda\|^2
       =2\langle\mu,\rho\rangle+2\|\rho\|^2-4\|\rho_K\|^2.
   \]
   At level $J\le4n^2+2$, this gives
   $\sum_{a\ne b}\|E_{ab}v\|^2\le512n^4B_0\|v\|^2$.
   Since $B_0\ge10^6n^7$, it implies the **original small bound**
   $n\sum_{a\ne b}\|E_{ab}v\|^2\le(B_0/16)^2\|v\|^2$.

2. Tensoring with the standard or dual standard module adds at most
   $\sqrt n$ to the square root of compact energy. Intertwining maps
   preserve compact Casimir eigenvalues. The shifted lowest weight is
   $\Lambda-e_s$ and its scalar satisfies
   $\sqrt\kappa\le\sqrt{\kappa_s}+\sqrt n$.
   Weight differences cost at most two. This proves both the projected
   vectors' level bound and the same bound for their embedded components.

3. The split Casimir
   $(Tx)_a=-\sum_bE_{ab}x_b$ has exact eigenvalues
   $\zeta_s=-\mu_s+(1-n)/2$. The previous small estimate gives
   $\|T-D\|\le B_0/16$ on the finite span of the projected vectors,
   where $(Dx)_a=-E_{aa}x_a$. On the circle
   $|z+B_0/16|=9B_0/16$ one gets
   $\|(z-T)x\|\ge13B_0\|x\|/32$. Consequently the sum of all
   compact-cluster projections has norm at most $18/13$.

4. Only the $m=n+1-k=2r+2$ remaining eigenvalues need individual
   interpolation. Each of their projections has norm at most
   $3(6B_0)^{m-1}$. The bound on the whole compact cluster is essential:
   interpolating separately at every eigenvalue would introduce a power
   of $B_0$ depending on $n$ and would miss the original target.

5. A compact-cluster eigenvector has at most $1/15$ of its Euclidean
   norm in the coordinates which may have negative Hermitian sign.
   Its indefinite square is therefore nonnegative. The compact-cluster
   contribution can be summed as **one** indefinite square. The exact
   signed-isometry identity then gives
   \[
    \sum_s\|p_sx\|^2
    \le\bigl((18/13)^2+9m(6B_0)^{2m-2}\bigr)\|x\|^2
    \le(6B_0)^{2m}\|x\|^2.
   \]

The full proof, including all constants, the empty-cluster case and zero
vectors, is in the shared TeX. No division by a Bessel or vector norm is
used. This result is algebraic; it neither changes nor normalizes a
quotient measure.

## What remains for the first-length estimate

The original first-length step also needs the original Pieri tensor
decomposition, the normalized lowering constant
\[
       |\kappa_s|^2\,d_\eta/d_{\eta-e_s}\le T b^4,
\]
and the original Bessel mass/isometry on the quotient measure. The
projection estimate proved here provides one of those actual suppliers;
it does not make the other two automatic.

The lowering constant has now been located more sharply. The source
identifies its squared modulus with an explicit product ratio by a
dual-tensor Bessel identity. The formal-degree ratio cancels one
Vandermonde product, leaving
\[
 T\,\frac{\prod_{i=1}^k|\mu_s-\tfrac12-u_i|}
               {\prod_{t\ne s}|\mu_s-1-\mu_t|}.
\]
The required numerical bound is $b^4$. This exact product, its
integer/half-integer hypotheses, interlacing, and both parameter-gap
reserves must be retained in the next reconstruction. Its scalar
identity and analytic normalization are not proved in this package.

This leaves the original leading-minor norm and weighted orbital norm
targets open. No whole-node count change: RH **6/9**, GRH **17/31**.

## Authenticated bounded source locations

All original sources below use immutable revision
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
`J` denotes `Development.AbelianVarietyTheory.Proofs.JetHarmonics.`;
`B` denotes
`CompanionTheory.AutomorphicTheory.PieriRules.ThetaBesselIsometries.`.

| Module | Bounded lines | Role |
|---|---:|---|
| `Development.AbelianVarietyTheory.Definitions.Jets.SumIoPr` | 16--30, 39--57 | Original level, algebraic tensor maps and parameter shape |
| `J.UnitaryGlModuleLevelOffDiagNormSqLe` | 148--172 | Exact small off-diagonal target |
| `J.UnitaryGlModuleProjComponentsLevelAddTwo` | 11--35 | Original embedded-component level requirement |
| `J.UnitaryGlModuleProjDualTensorLevelAddTwo` | 13--43 | Original target-module level requirement |
| `J.InvariantHermitianFormNonnegOfCloudEigen` | 12--58 | Positive cluster eigenvectors in the original form |
| `J.CloudNodeProjectionNormLowLevel` | 17--92 | Exact circle, constants and exceptional spectral interpolation |
| `J.SumNormSqProjectionsTensorUnitaryGlLe` | 15--44 | Original signed projection norm target |
| `B.FamilySetupCayleyMoment` | 134--163 | Its actual consumer in the first-length recursion |
| `B.FamilySetupMomentGrowth` | 66--113 | Exact degree-normalized lowering scalar reduction, still open here |
| `J.LoweringBound` | 12--25, 43--49, 70--89 | Next numerical product and retained hypotheses |

Run `python3 scripts/check_global_norm_frontier_tensor_projections.py --offline`.
The certificate authenticates the bounded sources, checks the decisive
polynomial constants and cancellation identity exactly, and checks
finite signed tensor projection models. Those finite models supplement
the proof; they do not assert a Lean build or verify any unproved
analytic Bessel input.
