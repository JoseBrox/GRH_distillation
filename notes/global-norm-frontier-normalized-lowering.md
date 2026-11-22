# Original normalized lowering scalar

## Result

The theorem `original-normalized-lowering-bound` in
`paper/shared/global-norm-frontier-normalized-lowering.tex` proves
\[
             |\kappa_s|^2 d_\mu/d_{\mu-e_s}\le T b^4
\]
with the original signed Pieri maps, original Bessel subgroup periods,
original central and compact parameters, the actual geometric factor
$T=-h(z,z)>0$, and formal degrees for the **same** Haar measure.
It uses the numerical lowering product already proved in the companion
package. This is a conditional supplier in precisely the original
normalized family; the family has not been replaced or rescaled.

The essential distinction is visible in the original definitions:
`SumIoPrAlt.IsBeL`, lines 135--139, assumes absolute integrability of
the subgroup period and its rank-one factorization. The different
`IsIsoB`, lines 141--144, asserts quotient $L^2$ isometry. Only the
first normalization enters the lowering-scalar proof. The quotient
mass/isometry and identification with the original Jacquet transform
remain open.

## Mathematical proof and decisive checks

Let $A_s=p_s(\operatorname{flat}(f_0)\otimes\cdot)$, and let $C_s$
be contraction of the original inclusion $i_s$ against the same fixed
dual vector using the invariant Hermitian form. The signed isometry
gives $C_s=\epsilon_s A_s^*$. Because the dual vector is fixed by the
Bessel subgroup, their matrix coefficients agree up to $\epsilon_s$.
Integrating against the unchanged period kernel and using the original
rank-one factorization gives
$\mathcal B C_s=\epsilon_s\overline{\kappa_s}\mathcal B_s$ whenever
$\mathcal B_s A_s=\kappa_s\mathcal B$ and $\mathcal B\ne0$.
This is an actual proof of the normalized adjoint relation, without
assuming any quotient mass bound. A zero target Bessel map gives
$\kappa_s=0$ and is included.

The split Casimir has eigenvalues
$-\mu_s-(n-1)/2$. The ordered quantum comatrix evaluated at $-\mu_s$
therefore equals the corresponding spectral projection multiplied by
$D_s=\prod_{t\ne s}(\mu_t-\mu_s)$. This follows as a polynomial
identity from the ordered cofactor expansion and the original central
character, so evaluation at the vanishing factor causes no illegal
division by zero.

For positive isotropic rank $r$, the original Bessel character removes
$r$ initial rows and $r$ terminal columns from the relevant cofactor.
The two strings each contribute a factor of modulus $\sqrt T$.
Row removal preserves the minor parameter; each column removal lowers
it by one. The surviving compact minor is consequently evaluated at
$-\mu_s+k/2$, and its character is
$\prod_i(-\mu_s+1/2+u_i)$. No factor is moved past another
noncommuting factor: row and column expansions put the applicable
character operator on the left before applying the Bessel functional.
For $r=0$ the minor is already compact, and the original dual vector
and evaluation supply the missing factors $-\sqrt T$ and $\sqrt T$.

Thus
\[
 |\kappa_s|^2
       =T\frac{\prod_i|\mu_s-1/2-u_i|}
                    {\prod_{t\ne s}|\mu_s-\mu_t|}.
\]
The original same-measure formal-degree ratio cancels the denominator
and leaves exactly the lowering product already bounded by $b^4$.

## Scope and remaining analytic task

This proof retains the original tensor family, its intertwining and
signed-isometry identities, the original central-character and compact
Capelli parameter identities, subgroup-period normalization, and a
nonzero Bessel vector in the original test domain: the span of group
translates of compact finite smooth vectors. This distinction matters:
the source's `R.TK` is this translate span, not just the compact finite
vectors. Its existence is the source's cyclicity argument; the
norm-recursion vectors lie in this domain, and the tensor maps preserve
it. No normalized quotient norm is inferred from this nonvanishing.

The existing algebraic identities for ordered minors and formal-degree
formula are reused and credited, not counted as new theorems. The new
reconstruction applies them to the original one-slot lowering scalar,
including both rank regimes, phase-independent absolute values, and
the normalized adjoint relation. The earlier two-spectrum radial
operator was not substituted for this one-slot operator.

To use this result in the leading-minor Jacquet norm, one must still
construct the relevant normalized Bessel family from the actual
Jacquet transform, retain its quotient measure and formal degree,
prove its mass/isometry, and justify the Pieri decomposition and its
identification in that realization. No whole-node count change:
RH **6/9**, GRH **17/31**.

## Source and verification record

All original modules are pinned to
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
Use prefixes `J = Development.AbelianVarietyTheory.Proofs.JetHarmonics.`
and `B = CompanionTheory.AutomorphicTheory.PieriRules.ThetaBesselIsometries.`.

| Module | Lines | Role |
|---|---:|---|
| `Development.AbelianVarietyTheory.Definitions.Jets.SumIoPrAlt` | 25--39, 123--144 | Exact translate test domain, period normalization and quotient isometry |
| `B.TensorMomentEstimate` | 59--83, 108--121 | Original signed normalized adjoint comparison |
| `J.CapelliComatrixPicksSplitCasimirEigencomponent` | 48--103, 109--119 | Exact ordered comatrix shift and eigensummand extraction |
| `J.QuantumMinorRowExpansionEigenFunctional` | 13--47 | Left row extraction, unchanged parameter |
| `J.QuantumMinorColumnExpansionUnderLinearMap` | 29--72 | Left column extraction, parameter minus one |
| `J.GlRelationRowStepsFunctionalEigen` | 164--178 | Original row string and boundary factor |
| `J.BesselColumnStepsFunctionalEigen` | 93--101 | Original column string and exact shift |
| `J.ProjectorEntryValueUnderLinearFunctional` | 24--55, 69--103 | Original compact evaluation and cofactor product |
| `B.DualTensorBesselMoment` | 88--95, 116--146, 147--174 | Exact geometric normalization and original cofactor entry in both ranks |
| `B.FamilySetupMomentGrowth` | 66--113 | Original scalar and formal-degree consumer |
| `B.ExistsKTypeNonzeroBessel` | 19--38 | Nonzero vector in the original translate test domain |
| `J.FrameWConjMatrixUnits` | 337--340 | Original character amplitudes and both frame normalizations |

Run `python3 scripts/check_global_norm_frontier_normalized_lowering.py --offline`.
The certificate checks source bytes and bounded ranges, exact quantum
comatrix identities in finite matrix-unit modules, the polynomial
spectral extraction, and the two original row/column index strings.
It does not certify an unrun Lean build or the still open analytic
realization of the Bessel family.
