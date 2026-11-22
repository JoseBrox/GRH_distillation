# Why finite level alone does not supply a dominant return

## Checkpoint and outcome

The [sharp scalar return bound](dominant-return-deficit.md) gives an exact
test for nonvanishing, but the inspected source does not yet verify that
test for the prescribed arithmetic family. There is a concrete obstruction
to the simplest attempt: in the isotropic case, **infinitely many distinct
rational returns satisfy the same finite-place support condition**. Thus
finite-level support cannot by itself produce a single-return region.
An actual estimate of the archimedean tails, with the existing parameters,
is still needed. No nonvanishing or proof-map node is claimed here.

## 1. Infinitely many supported rational returns

Use the original unitary group over the totally real field \(F\), with
CM coefficient field \(E\), and suppose the prescribed frame contains
at least one hyperbolic pair \(e_1,f_1\). Its rational scalar-seed
stabilizer \(\Delta_u\) fixes \(e_1\): this is the first flag equation
in the definition of \(S_u\). Let \(K\) be the actual finite compact
open level. The finite seed support is
\[
                         N_fH_{u,f}x_uK.                 \tag{1}
\]
Fix any \(g_f\) in (1). Choose \(0\ne\xi\in E\) with
\(\bar\xi=-\xi\). For \(t\in F\), define a rational unitary
transvection by
\[
 \gamma_t(e_1)=e_1+t\xi f_1,\qquad \gamma_t(f_1)=f_1,
\]
fixing the orthogonal complement of this hyperbolic plane. Its matrix
on the plane is \(\left(\begin{smallmatrix}1&0\\t\xi&1\end{smallmatrix}\right)\).
The equation \(\xi+\bar\xi=0\) proves unitarity directly, and
\(\gamma_t\gamma_s=\gamma_{t+s}\).

The inverse image of \(g_fKg_f^{-1}\) under this adelic one-parameter
subgroup is an open neighbourhood of zero in \(\mathbb A_{F,f}\).
It contains the completion of a nonzero fractional ideal of \(F\).
Choose a nonzero rational element \(b\) in that ideal; then every
\(t=nb\), \(n\in\mathbb Z\), satisfies
\[
 \gamma_tg_f\in g_fK\subset N_fH_{u,f}x_uK.              \tag{2}
\]
These elements represent distinct left cosets in
\(\Delta_u\backslash G(F)\). Indeed equality of two cosets would
put \(\gamma_{t-s}\) in \(\Delta_u\), forcing it to fix \(e_1\),
and hence \(t=s\). All finite-level indicators in (2) are therefore
one. The argument allows any depth of the original finite level; making
it smaller changes the congruence ideal but does not make it finite.

This statement concerns the finite support only. It does not assert
that every associated archimedean Whittaker value is nonzero, or that
their norms are comparable. In particular it does not rule out one
dominant return. The argument does not cover the anisotropic case with
no prescribed hyperbolic pair.

## 2. What the actual decay contract supplies

The displayed \(W_u\) contract gives covariance, projector reproduction,
continuity, finite \(L^1\) norm and unit \(L^2\) norm. The more detailed
source decay package also gives
\[
 \int_{S_{u,\infty}\backslash G_\infty}
       \|W_u(g)\|\,\nu_u(g)^{N_1}\,d\nu(g)<\infty,
 \qquad
 N_1=4n^2\sqrt{2\max_v q_v},                            \tag{3}
\]
where \(\nu_u(g)\) is the infimum of the product of matrix operator
norms over the left stabilizer. It supplies a compactly supported
reproducing kernel as well. The inspected proof multiplies local finite
weighted integrals to prove finiteness of (3).

The displayed conclusion is qualitative finiteness, without a numerical
bound for the integral or the reproducing-kernel constant in terms of
the growing field, rank, weights and the already chosen level. It
ensures the convergence needed for the period formula, but does not
compare the sum of the other return norms to one chosen return on a
positive-measure region. Such a comparison needs the original congruence
lattice separation/counting bound together with a quantitative
archimedean concentration or tail bound, in the same normalization.
Changing the finite level after fixing the archimedean seed would require
a separate compatibility argument with the construction; it is not
licensed by (3).

This is a scope statement about the bounded source contracts inspected
here, not an assertion that no stronger estimate exists elsewhere in
the source. The pairwise amplitude supplier is separately quantitative,
but its inspected contract retains a mass-admissibility input and does
not identify the relative pointwise return sum needed here.

## 3. Two nonvanishing distinctions to retain

First, the source declaration named `NonvanishingBesselPeriod` is not
a statement that a global Poincaré map is nonzero. Its definition is
existence of a formal degree for a local discrete-series representation.
Its nine-line wrapper invokes the corresponding Schur-orthogonality
theorem. It cannot close the global nonvanishing obligation.

Second, even dominance for a raw seed need not survive the prescribed
source and target restrictions. With the **retained** evaluation norms,
the already proved sufficient quantity is
\[
 \mathcal C_u=c_u^{-1}\int_Y(2m_u-A_u)_+^2.
\]
If \(\mathcal C_u>0\), the map \(P_uJ_u\) is nonzero before the
target restriction. For the final family, one needs
\[
 \sum_u\mathcal C_u>
 L_t:=\sum_uc_u^{-1}\|(I-\Pi)P_uJ_u\|_{\mathrm{HS}}^2.
\]
That conclusion is aggregate nonvanishing. It does not prove that
every word survives. None of these strict inequalities has been
established for the actual growing family in this checkpoint.

## 4. Bounded source record and next decisive step

All paths are pinned to
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The certificate records exact hashes and excerpt ranges.

| Source suffix | Inspected ranges | Relevant contract |
|---|---|---|
| `HaarTransversals/HidaSetting.lean` | 26–34, 151–156, 349–363 | First flag vector is fixed; actual seed conditions; original level and its character. |
| `HaarTransversals/PoincareInHH.lean` | 149–199 | Rational stabilizer, full finite support, period sum and absolute convergence. |
| `HaarTransversals/WuDecay.lean` | 14–43 | Exact weight exponent; qualitative weighted integrability; compact reproduction; folding finiteness. |
| `RootLatticeThresholds/WuDecayAll.lean` | 422–435, 468–489 | Local decay contract and product proof of weighted finiteness. |
| `RootLatticeThresholds/AmplitudeBoundsAllChoicesUniform.lean` | 26–47 | Separate amplitude estimate retains its mass-admissibility hypothesis. |
| `GlobalSchurBounds/StandardLattice.lean` | 357–361 | Meaning of the named local nonvanishing contract. |
| `UnitTraceSumBounds/NonvanishingBesselPeriod.lean` | 1–9 | Wrapper invokes the local formal-degree theorem. |
| `CuspSpanNormBounds/BridgeCSchur.lean` | 626–629 | Actual conclusion is existence of the formal degree. |

Resume by deriving an explicit bound for the actual nonleading-return
sum on an original finite-level region, using (3) with controlled
constants and the original rational return lattice. Then compare with
the retained-source leading value and the actual target-loss bound.
Do not substitute a qualitative large-level existence theorem or local
formal-degree positivity for this compatibility calculation.
