# Simplicity of zeros: limitation of the RH/GRH endpoints

**Audit, 22 November 2026. Conclusion: not established.** The project
currently proves several conditional zero-location and nonvanishing reductions,
not nonvanishing of zeta or Dirichlet-L derivatives at their zeros. This audit
checks the pinned outer Lean statements, the analytic endpoint, the newer
Selmer and theta-energy reductions, and relevant 2026 literature. It is **not**
a complete proof-term audit of all Lean source declarations.

## 1. Nonzero residue is not multiplicity one

The pinned [formal statements](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Statements.lean)
and [Main.lean](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Main.lean)
assert zero location and right-half-plane nonvanishing, not derivative
nonvanishing. For a zero rho of multiplicity m_chi(rho) >= 1,

```math
\frac{L'(s,\chi)}{L(s,\chi)}
=\frac{m_\chi(\rho)}{s-\rho}+O(1).
```

The corrected Mellin transform F_chi from our
[RH manuscript](../paper/rh/sections/02-analytic-endpoint.tex)
has the residue

```math
\mathrm{Res}_{s=\rho}F_\chi(s)
=-\frac{m_\chi(\rho)}{\rho(\rho-1)}\ne0. \tag{1}
```

The [source PoleData interface](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauZeroFreeCriterion.lean)
requires simple *transform* poles with nonzero residues (positive residues
when poles are real). It excludes zeros on the right by their pole's
presence, but never asserts that m_chi(rho)=1. A multiple L-zero
produces a simple logarithmic-derivative pole with residue proportional
to its multiplicity.

## 2. Explicit abstract countermodel

**Proposition.** For every integer m >= 1, the exact source
PoleData and WindowHypU analytic conditions hold for a model with two
critical-line poles of residue m. In particular these conditions do
not imply unit residues.

**Proof.** Fix gamma>0 and let

```math
g_m(u)=2m e^{u/2}\cos(\gamma u),\quad
Z=\{\tfrac12+i\gamma,\tfrac12-i\gamma\},
```

```math
\Phi_m(s)=\frac{m}{s-\tfrac12-i\gamma}
+\frac{m}{s-\tfrac12+i\gamma}.
```

The unilateral Laplace integral of g_m equals Phi_m in Re(s)>1/2.
Growth on u>=0 is at most 2m exp(2u); the pole set Z is isolated;
Phi_m is holomorphic elsewhere; both residues equal m and there are
no real poles. Thus all fields of PoleData hold. For every
1/2<theta<1 and delta,eta>0 take the positive majorant
R(u)=2m exp(u/2). For arbitrarily large U,

```math
\int_U^{(1+\delta)U}R(u)e^{-\theta u}\,du
\le\frac{2m}{\theta-\tfrac12}
 e^{-(\theta-\tfrac12)U}\le e^{\eta U}.
```

This is WindowHypU, and the fixed forward-logarithmic averaged
positive-part criterion also holds, because the averaged function
is O_m,h(exp(u/2)). None of the conditions depends on m=1.
Moreover, the entire toy function

```math
\Xi_m(s)=\big((s-\tfrac12)^2+\gamma^2\big)^m
\quad\text{satisfies}\quad\Xi_m(s)=\Xi_m(1-s)
```

and has the same two zeros of multiplicity m, with
Xi_m'/Xi_m=Phi_m. It is **not** a Dirichlet L-function; this
establishes an obstruction to the abstract pole/location/functional
equation mechanism, not to an argument using further arithmetic
information. QED.

The same reason is visible in scale invariance: for any c>0,
the source conditions for (g,Phi) persist for (cg,cPhi).
For WindowHypU, use the old property with eta/2, then absorb
the fixed factor c on sufficiently late windows. The residues
multiply by c. A subpower positive-part bound also persists after
fixed scaling.

## 3. Why newer arithmetic multiplicities do not answer this

The [Selmer upper-multiplicity theorem](rh-selmer-upper-multiplicity.md)
bounds lengths of localized arithmetic/deformation modules by 2^q,
using a reduced finite slice. The
[theta-energy theorem](averaged-theta-energy.md)
bounds ranks and energies of integral arithmetic maps.
Neither identifies these multiplicities with the analytic vanishing
order of zeta or a Dirichlet L-function. The proof program has
no checked determinant representation of these functions by
an operator with *simple spectral eigenvalues*.

## 4. Exact missing target

By (1), simplicity at a fixed zero rho is equivalent to

```math
-\rho(\rho-1)\mathrm{Res}_{s=\rho}F_\chi(s)=1.
```

Because this value is a positive integer, the strict upper bound

```math
\big|\rho(\rho-1)\mathrm{Res}_{s=\rho}F_\chi(s)\big|<2 \tag{2}
```

at every nontrivial zero would suffice. No currently proved or
conditional arithmetic supplier establishes (2). This would require
new zero-specific control (for example an oscillatory prime-sum
residue estimate, or a proved spectral-multiplicity bridge). Such
an input has not been identified in the audited source endpoints.

The 2026 papers of
[Alpöge--Furman](https://arxiv.org/abs/2608.13637)
and [Lamzouri](https://arxiv.org/abs/2609.02882)
give asymptotic lower proportions around 67.25% for simple zeta zeros
on the critical line, using Weil-form and pair-correlation methods.
These are not zero-by-zero statements and do not become 100%
merely by assuming RH. The Alpöge--Furman work also covers primitive
Dirichlet L-functions.

**Result:** Neither ordinary RH nor Dirichlet GRH simplicity follows
from the inspected reductions. The next required theorem is a
unit-residue/derivative-nonvanishing statement at *every* zero.
This audit adds no completed node to either proof map.
