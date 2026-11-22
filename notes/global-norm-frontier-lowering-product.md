# The numerical part of the original lowering constant

## Proved result

The standard-mathematics proof in
`paper/shared/global-norm-frontier-lowering-product.tex` establishes
the original numerical target
\[
 \frac{\prod_{i=1}^k|\mu_s-\tfrac12-u_i|}
      {\prod_{t\ne s}|\mu_s-1-\mu_t|}\le b^4
\]
under the original interlacing, family size, separation and shift-budget
hypotheses. It gives the sharper bounds $8e\sqrt{k}\,b^2$ on a compact
cluster index and $6eb^2$ on an exceptional index. The source majorant
was respectively $64e\sqrt{k}\,b^3$ and $16eb^2$.

This is a new proved numerical supplier in the actual first-length
recursion. It is not by itself a proof of the normalized Bessel scalar
identity or the leading-minor norm. The two retained shift constraints
are $q\le\gamma/8$ for the compact cluster and $q\le B_0/4$ for the
separated negative parameters. The ambient bound $q\le b$ is also kept.

The proof avoids an exponential loss in the compact rank. If $Q$ is
the polynomial with roots $u_i$ and $P$ has the interlacing compact
roots $\lambda_a$, then
\[
 Q(y)/P(y)=y-a-\sum_t w_t/(y-\lambda_t),\qquad w_t>0.
\]
An elementary real symmetric matrix with these diagonal entries and
last-column entries $\sqrt{w_t}$ has characteristic polynomial $Q$.
Since every $u_i$ lies in $[-b,b]$, its last-column squared norm gives
$a^2+\sum_tw_t\le b^2$. Thus one controls the **sum** of the residues,
independently of their number. The original shift budget then costs at
most $e\sqrt{k}$ in the compact cluster and at most $e$ outside it.

The proof includes $k=1$, empty products and vanishing numerators.
The gap condition proves that every denominator has absolute value at
least one. No division by a Bessel norm or unproved positive scalar is
made.

## Exact point where normalization is still needed

Let $\kappa_s$ be the original lowering scalar and $d_\mu$ the formal
degree with the original Haar measure. The source proves
\[
 |\kappa_s|^2
 =T\frac{\prod_i|\mu_s-\tfrac12-u_i|}
          {\prod_{t\ne s}|\mu_s-\mu_t|},\qquad
 \frac{d_\mu}{d_{\mu-e_s}}
 =\frac{\prod_{t\ne s}|\mu_s-\mu_t|}
          {\prod_{t\ne s}|\mu_s-1-\mu_t|}.
\]
The second is the same-measure formal-degree ratio. The first is not
an elementary consequence of interlacing: it is the original Capelli
cofactor evaluation combined with the normalized Bessel adjoint
identity. Their cancellation gives $T$ times the product just bounded.

The reconstructed resolvent chapter 81 concerns a different terminal
operator with two compact spectra. Its interlacing formulas must not be
silently substituted for this one-slot Bessel projector identity.
The precise next source is
`ProjectorEntryValueUnderLinearFunctional.capelli_projector_entry_value`.
Its full determinant acts by $\prod_s(Y+\mu_s)$, its compact quantum
minor acts by $\prod_i(-\mu_s+\tfrac12+u_i)$, and the spectral cofactor
denominator is $\prod_{t\ne s}(\mu_t-\mu_s)$. For positive isotropic
rank it also removes two triangular strings of operators, contributing
the exact geometric factor $T$; rank zero has a separate normalization.
These operator identities and the original Bessel quotient mass are
not proved in the current package.

No whole-node count changes: RH **6/9**, GRH **17/31**.

## Source and verification record

All original entries are pinned to
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The certificate records full-file and bounded-excerpt hashes.

| Module | Lines | Role |
|---|---:|---|
| `Development.AbelianVarietyTheory.Proofs.JetHarmonics.LoweringBound` | 12--25, 43--89 | Original numerical target, family hypotheses and constants |
| `CompanionTheory.AutomorphicTheory.PieriRules.ThetaBesselIsometries.FamilySetupMomentGrowth` | 66--113 | Same-measure formal-degree cancellation |
| `CompanionTheory.AutomorphicTheory.PieriRules.ThetaBesselIsometries.DualTensorBesselMoment` | 88--95, 116--146 | Actual Bessel projector scalar and geometric factor |
| `Development.AbelianVarietyTheory.Proofs.JetHarmonics.ProjectorEntryValueUnderLinearFunctional` | 24--55, 69--103 | Exact Capelli cofactor identity still to reconstruct |

Run `python3 scripts/check_global_norm_frontier_lowering_product.py --offline`.
The checker verifies partial fractions, residue signs and sums,
arrowhead characteristic polynomials, parameter ranges and product
bounds in exact rational examples, and checks counterexamples to
dropping interlacing or the denominator gap. These checks supplement
the general proof in the shared TeX; they are not a Lean build or an
analytic Bessel normalization proof.
