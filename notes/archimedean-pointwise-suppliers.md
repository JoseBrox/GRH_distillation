# Archimedean pointwise suppliers and their completed assembly

## Status

The actual pointwise supplier is now proved on the explicit retained spectral reserve, and that reserve is supplied for every shifted coefficient used by the weighted point sum. The proof uses the sufficient Gram power `p=6(r+1)²`; it does not assert the stronger original interface for every smaller power or every near parameter. The new proofs have passed independent mathematical review. No Lean replay has been performed.

The complete assembly is [archimedean-pointwise-assembly.tex](../paper/shared/archimedean-pointwise-assembly.tex); its application is [archimedean-ap7-reserve.tex](../paper/shared/archimedean-ap7-reserve.tex). The [W08 continuation record](w08-analytic-and-retained-continuation.md) states the result, normalization, verification scope and remaining retained-column obligations. Sections 1–2 below give the new adaptive-grid and all-head argument. Section 3 records the original endpoint diagnosis; its two missing suppliers are now proved by the spectral-word and direct PBW cutoff arguments. Sections 5–6 give the latter proof and the actual Wigner transport.

Repository reviewed: `JoseBrox/GRH_distillation@9a362ab91b1bf25dffc182feb86868c7e40ecff5`. Pinned source: `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

The current compact Fourier and off-diagonal proofs use an interval of length at least `6(20s)^3+6(20s)`, where `s=r+1`. Their algebraic identities are valid on arbitrary fresh interpolation nodes. The original `ThmBpDS` pointwise application provides a cut of length only `30s^2+6`. No fixed choice of the source gap constant can absorb that cubic-versus-quadratic discrepancy for unbounded rank. The following adaptive choice removes the discrepancy. It does not contradict the earlier theorem, whose explicit stronger interval hypothesis remains valid.

## 1. Adaptive grids on the actual quadratic cut

Let `s=r+1`, `N=3s`, and `M=N(2r+1)=3s(2s-1)`. Let the original cut have endpoints determined by two real compact parameters `u_l,u'_l`, and put `a=min(u_l,u'_l)`. Assume

\[
 |u_l-u'_l|\ge 5M.
\]

Choose

\[
 \mathcal Y=\{-a-3-5i:0\le i<M\}.
\]

Every `y,y+1` lies in the original cut (each lies strictly between the negatives of the endpoint parameters, in the closed interval `[−max(u_l,u′_l)+2,−min(u_l,u′_l)−2]`), and distinct nodes have distance at least five. The actual source allowance suffices, because

\[
 5M=30s^2-15s\le30s^2+6.
\]

An admissible old word `w` has letters `(+ ,y)` or `(-,y+1)` for `y` in `Y`, and its numerical letter parameters are pairwise more than two apart. In particular, each underlying node is used at most once. For any `K` with `|w|+K<=N` and any interpolation degree `0<=d<=2r`, there are `K` disjoint blocks of `d+1` unused nodes: indeed

\[
 |\mathcal Y|-|w|=N(2r+1)-|w|
 \ge(N-|w|)(2r+1)\ge K(d+1).
\]

All new plus and minus letters remain more than two apart from each other and from the old letters, since underlying nodes are five apart and each letter has shift zero or one. Both signs therefore preserve the exact source admissibility condition.

For one selected block `y_0,...,y_d`, the leading-coefficient Lagrange weights are

\[
 c_j=\prod_{i\ne j}(y_j-y_i)^{-1},\qquad
 \sum_{j=0}^d|c_j|\le(d+1)5^{-d}\le1.
\]

The last inequality follows from `d+1<=5^d`, including `d=0`. It is not necessary to use widely separated long blocks.

Write the original compact polynomial and positive word normalizer as

\[
 q_0(y)=-TT'\prod_{i=1}^k(y+\tfrac12+u_i)(y+\tfrac12+u'_i),
 \qquad S_w=\prod_{(\epsilon,t)\in w}\nu(t),
\]

where `nu(t)>0` for every permitted letter parameter. The original exact modified polynomial is

\[
 q_w(y)=q_0(y)
 \prod_{(+,t)\in w}\left(1+\frac1{y-t}\right)
 \prod_{(-,t)\in w}\left(1+\frac1{t-1-y}\right).
\]

At a fresh node, every denominator in this product has absolute value at least five: for a negative old letter `t=z+1`, the denominator is exactly `z-y`. Each real factor is consequently at least `4/5`. Thus

\[
 q_w(y)\ge(4/5)^{|w|}q_0(y)>0.
\]

Suppose the actual normalizers obey

\[
 \nu(y)\nu(y+1)\le\Lambda_0^2q_0(y)
 \quad(y\in\mathcal Y).
\]

Put

\[
 \Lambda=\max\{1,\Lambda_0(5/4)^{N/2}\}.
\]

Then every fresh insertion at every intermediate old word of length at most `N` obeys

\[
 \sqrt{\nu(y)\nu(y+1)/q_w(y)}\le\Lambda.
\]

Now repeat the existing exact Capelli leading-coefficient calculation in `global-norm-frontier-kernel-fourier.tex` and `global-norm-frontier-off-diagonal.tex`. The only numerical inputs in their positive interpolation argument are: admissible fresh nodes; the sum of absolute Lagrange weights; positivity of `q_w`; and the displayed normalizer ratio. All four have just been proved on the new grid. The exact Fourier identity has degree `2j<=2r`; the off-diagonal identity has degree `2j-t<=2r-1`. Thus the original compact Fourier and inverse-parameter estimates both hold with this common `Lambda`, for every old word, every required head and every `K` with `|w|+K<=N`. The original quotient measures, two signs, word order, and normalizers are unchanged.

This argument supplies the original `WaveGrid`/`LiftGrid` type numerical input on a quadratic-length cut. It is an ordinary proof and does not invoke those predicates as black boxes.

If in addition `b>=3`, `C>=0` and the original spectral normalizer estimate gives `Lambda_0<=b^((6+C)m)`, with `m=2s`, then

\[
 \Lambda\le b^{(7+C)m}.
\]

Indeed `(5/4)^(3s/2)<=b^(2s)=b^m`; the other branch of the maximum is harmless. The explicit normalizer proof is now included as NC1–NC15 in [the shared fragment](../paper/shared/archimedean-adaptive-grid.tex); it discharges this premise. Its original pinned elementary source is `ProdFinEqProdIcc.lean`, theorem `NormaliserCutBound.main`, and its underlying two-bracket telescoping estimate.

## 2. Explicit scalar pointwise recursion on every head

Retain the original compact smooth coefficient with positive Gram cutoff, the actual place and top-lift hypotheses, and its original normalized kernels `N_{j,w}` and nonnegative diagonals `E_{j,w}`. Assume the just-established Fourier and inverse-parameter estimates at the common scale `Lambda`, and the previously proved original compact block-growth inequality. Let `W_K(w)` denote the finite set of original admissible extensions of `w` by at most `K` letters from `Y`.

### Singleton step

Let `h` have size `j`. The actual continuous integrable diagonal density

\[
 H(c)=N_{j+1,w}(h\mathbin\Vert(1,c),h\mathbin\Vert(1,c))
\]

agrees with its orbital value for every nonzero `c`. The Fourier kernel is `exp(sc-bar(s)bar(c))`, with planar Lebesgue measure. Its inversion constant is `pi^(-2)`. Put

\[
 B=\max_{v\in W_3(w)}E_{j,v}(h).
\]

Although the maximizing extension in the Fourier estimate can depend on the Fourier variable, this single finite maximum bounds all of them. Since

\[
 \int_{\mathbb C}\min\{1,(\Lambda/|s|)^3\}\,ds=3\pi\Lambda^2,
\]

Fourier inversion gives the pointwise bound

\[
 E_{j+1,w}(h\mathbin\Vert(1,c))
 \le\frac3\pi\Lambda^2B\le6\Lambda^2B.
\]

The Fourier transform is integrable by this explicit majorant, so this use of inversion is pointwise for the given continuous representative. There is no almost-everywhere substitution.

### Longer-block step

Consider a block of size `t>=2` appended to a head `h`, and write its new total level as `j`. Suppose all preceding diagonals

\[
 E_{j-1,v}(h\mathbin\Vert(t-1,z))\le B\quad(z\ne0, v\in W_3(w))
\]

are uniformly bounded. For each fixed complex `sigma`, the inverse-parameter estimate applied to `z` and `(z^(-1)+sigma)^(-1)` gives

\[
 \limsup_{z\to0,z\ne0}
 |N_{j-1,w}(h\mathbin\Vert(t-1,z),
 h\mathbin\Vert(t-1,(z^{-1}+\sigma)^{-1}))|
 \le \min\{1,(\Lambda/|\sigma|)^3\}B.
\]

The exceptional point at which the second parameter is undefined is absent from a sufficiently small punctured neighborhood. At `sigma=0`, the majorant is one. This validates the full punctured-complex limsup required by the original block-growth theorem.

Choose the original primal square lattice

\[
 \mathscr L=(\pi/\Lambda)(\mathbb Z+i\mathbb Z).
\]

For the actual character its dual is `Lambda(Z+iZ)` and its covolume is `pi^2/Lambda^2`. In the original block-growth inequality use the translate containing the prescribed target parameter. Positivity lets us retain that one summand. Its right-hand side is at most

\[
 B\sum_{(a,b)\in\mathbb Z^2}
 \min\{1,(a^2+b^2)^{-3/2}\}.
\]

The origin contributes one. The square shell `max(|a|,|b|)=n>=1` has `8n` points, each with Euclidean norm at least `n`, so the sum is at most

\[
 1+8\sum_{n\ge1}n^{-2}\le17<6\pi.
\]

Here `sum n^(-2)<=2` follows directly by comparison with `1+integral_1^infty x^(-2) dx`. Dividing by the exact left-hand factor `covol(L)/pi=pi/Lambda^2` proves

\[
 E_{j,w}(h\mathbin\Vert(t,z_0))\le6\Lambda^2 B.
\]

No parameter-lattice counting constant depends on the rank, compact type or coefficient.

### All-head theorem

For a valid original head `gamma` of total size `s=r+1`,

\[
 \boxed{
 E_{s,\varnothing}(\gamma)
 \le (6\Lambda^2)^s
 \max_{\substack{w\text{ original admissible}\ |w|\le3s}}
 E_{0,w}(\varnothing).}
\]

More generally, appending any valid head of total size `t` to a fixed head costs at most `(6 Lambda^2)^t` and at most `3t` additional letters. Prove this first for one block by induction on its size, using the singleton estimate as the base and the longer-block step for the induction. The preceding diagonals are uniformly bounded by the induction hypothesis, so the finiteness condition in block growth is verified, not assumed. Then concatenate the blocks. An extension of an extension is still an original admissible extension; its total added length is the sum of the two lengths. Since only finite maxima are used, there is no factor equal to the number of words or cells. This also proves the rank-zero case, where only the singleton argument occurs.

With the additional spectral normalizer premise in section 1,

\[
 (6\Lambda^2)^s\le b^{(8+C)m^2}.
\]

Indeed `6<=b^2`, so the exponent is at most `m+(7+C)m^2<=(8+C)m^2`.

## 3. Original endpoint diagnosis, now discharged on the sufficient reserve

Taken alone, the all-head theorem is not AP6 because its right-hand side is a maximum of normalized level-zero word energies. No norm bound for that maximum follows just from the compact interpolation identities.

The original route takes a smooth Gram cutoff `chi(G/epsilon)`, a power `G^p`, and, in the equal-compact-type case, one of two polynomial compact-type shift maps `A_+`, `A_-`. Let

\[
 F_{\pm,\epsilon}(g)=\chi(G(g)/\epsilon)G(g)^p F(g)A_\pm(g).
\]

For different types `A` can be the identity and `n0=0`. For equal types the source takes `n0=30s^2+6` and `deg(A_\pm)<=n0 s`; a separating compact gap of at least `2n0+1` is retained. The source uses `N=3s<=2p`, and smooth finite decay exponent

\[
 A_0-2sp-n_0s\ge C_c s^4(Nn^2+n^3),\qquad n=k+2r+1,
\]

with a uniform `C_c`. The all-gap and near-parameter reserve also must dominate the polynomial degree `2sp+n0s`.

To use the all-head theorem after compact exhaustion one still needs the actual level-zero endpoint

\[
 \limsup_{\epsilon\downarrow0}
 \max_{|w|\le N}E_{0,w}(F_{\pm,\epsilon})
 \le jN^2(G^pFA_\pm).
 \tag{EP}
\]

The normalizers on the left are the original positive products built from the base Harish--Chandra parameter; the right side is the original unscaled Jacquet norm. Finite word sets permit the maximum and limsup to commute in the required inequality. But (EP) itself has two distinct ingredients:

1. **Cutoff convergence.** For each allowed word the derivative terms from `chi(G/epsilon)` have an integrable common majorant and vanish as `epsilon` tends to zero. The source needs only `N<=2p`, not `N<=p`. Existing finite-decay exhaustion concerns a fixed positive Gram cutoff; it does not establish this limit as the cutoff approaches `G=0`.
2. **Spectral normalized energy.** The uncut polynomial coefficient `G^pFA_\pm` has Capelli spectral support in shifts of total degree at most `2sp+n0s`. The actual positive level-zero form makes the normalized word operators contractive on that finite spectral sum. This requires the same-form operator identity and orthogonality, as well as the stated all-gap reserve. Smooth decay alone does not prove it.

If (EP) is proved and `A=id`, the exact orbital invariance of `G` and the all-head theorem give

\[
 E_F(\gamma)\le (6\Lambda^2)^sG(\gamma)^{-2p}
 jN^2(G^pF).
\]

The existing determinant moment bounds then control the last norm because `0<G<=|D_s|^2` on the positive domain. Thus for `p<=C_0s^2`, this conditional conclusion has precisely the allowed `b^(O(m^4))` and `G^(-O(m^2))` shape. It includes zero Jacquet norm homogeneously.

For equal compact types one must additionally construct and prove the source two-map inequality

\[
 (G/T')^{n_0}\|v\|^2\le(3b)^{2n_0}
 (\|A_+(\omega)^*v\|^2+\|A_-(\omega)^*v\|^2),
\]

where the actual cofactor vector satisfies `||omega||^2=G/T'`, and the matching upper bound `||A_\pm(omega)||^2<=||omega||^(2n0)` must hold. This shifts a pair of adjacent compact parameters in the prescribed separating gap and is not furnished by the exterior-Pieri minor bounds alone. The source's `ExistsShiftedTypesLowerBound` provides an explicit finite-dimensional route via compact branching coefficients; its two-chain construction, actual orbital transport, and original norm comparison are now proved in the linked shared fragments and independently reviewed.

The smaller concrete moment exponent in RM3 reduces the desired final weight, but does not by itself remove (EP) or the equal-type comparison. Generic saturation does not mean every relevant point is on the regular big cell; hence the all-head control remains useful for that shortcut.

## 4. Source verification ledger

All source rows below are at the immutable Lean revision stated above. These are bounded reads and proof inspections, not kernel checks.

| File under `lean/src/` | Git blob | Lines read | Role |
|---|---|---:|---|
| `Development/AbelianVarietyTheory/Statements/DiscreteSeriesShifts/ThmBpDS.lean` | `ee9d3566504b7c3fc887401194b7512aefcbfe92` | 1–29 | Actual quantified target and near-parameter reserve |
| `Formalism/HermitianCurvature/StatementTBB.lean` | `1943087061b73cb08fe6059f7e9ac9ac2edd6fd8` | 1–199 | Original head, word, energy and pointwise predicates |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/ExistsGridFiveApartOnCut.lean` | `021e8a10bae8c9959e7add956a5c5d1be945dbe3` | 1–49 | Explicit quadratic cut grid |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/WaveGridLiftGridOfLayoutNormaliserBound.lean` | `63127a6447514fa0096e8ab4f00f0d26cdbaab07` | 1–120 | Old-word ratio and adaptive interpolation |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/ProdFinEqProdIcc.lean` | `1dab4d5caa78e6fac2ca247bb1236d0620c3d446` | 1–107 | Exact spectral normalizer comparison |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/PointwiseBoundDiscreteSeriesCoefficients.lean` | `b1baa8ed29ed72ea9f632999bf9e690b9ab86633` | 1–89 | Original DS-to-Capelli assembly |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/CapelliEigenfunctionBoundThreePlaces.lean` | `551326e1b284ba953e1fb605e9b0a8bcdcdef12d` | 1–118 | Precise cutoff and level-zero endpoints |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/EnergyBoundPolynomialWeightPowCapelliEigen.lean` | `b006e1d29fa316fbe3e388db2c02c445b5324445` | 1–39 | Spectral degree and normalized word-energy interface |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/ExistsShiftedTypesLowerBound.lean` | `72c67f418b4eb45d82bcd61ce51bc6c107f05f96` | 1–67 | Exact two-shift compact-type estimate |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/ChainLowerBound.lean` | `4f6e6e75de1c0bb65432111e7f6383935ef10d1c` | 1–117 | Branching-product lower bound |

The new scalar recursion proof is independent of the upstream scalar-recursion source; it uses the repository's actual Fourier, off-diagonal and compact block-growth identities and the elementary lattice-shell estimate above.

## 5. New sufficient cutoff proof: direct PBW control of the central word

Written proof: [archimedean-cutoff-pbw.tex](../paper/shared/archimedean-cutoff-pbw.tex).

The original endpoint can be proved with a larger but still quadratic Gram power, without the sharp no-inverse normal form. The key is the exact **level-zero** identity

\[
 \mathrm{RR}_{0,w}(F;\varnothing,\varnothing)
 =\beta(\mathcal C_w F,F),\qquad
 \mathcal C_w=\prod_{(\epsilon,t)\in w}\sigma\mathcal C_V(t),
 \quad\sigma=(-1)^{k-l_0}.
\]

Here every factor is the full central Capelli operator. Both signs of letter use their actual numerical parameter, so the minus-grid shift `y+1` is retained. At level zero the bit-zero site operator is the identity and the bit-one operator is zero; the all-zero corner of the original residue recursion appends exactly `Q00(t)`. The empty-head slice is the identity. These facts prove the displayed formula by induction; no terminal-density limit is used.

Let `n=k+2r+1`, `s=r+1`, and let the actual compact group `K_z'≅U(k)` fix the right Witt frame and `z'`. In a basis adapted to its positive `k`-space, give an invariant-differential word degree equal to the number of factors outside its `gl_k` block. Every permutation monomial of the full Capelli determinant has at most

\[
 q=2(n-k)=4s-2
\]

outside factors: at most `n-k` have an outside column and at most `n-k` further factors have an outside row. Moving compact factors to the far right by PBW does not increase this number, because `[gl_k,outside]⊂outside`. It does not increase total derivative order either. Thus for `|w|=L`,

\[
 \mathcal C_w=\sum_\alpha c_\alpha R_{X_{\alpha,1}}\cdots R_{X_{\alpha,h_\alpha}}
 R_{Z_{\alpha,1}}\cdots R_{Z_{\alpha,v_\alpha}},
 \quad h_\alpha\le qL,\quad h_\alpha+v_\alpha\le nL,
\]

where every `Z` is in the complexified Lie algebra of the actual right compact subgroup. The source convention is indeed right differentiation: `EabH` is `RdV(hpart1(Eab))+i RdV(hpart2(Eab))`, whose complexified direction is exactly `Eab`.

The cofactor identity gives

\[
 \mathcal G(g)=T'\|\Omega(g)\|^2,
 \qquad\deg\Omega=s,
\]

on the entire group, and `G` is right `K_z'`-invariant. Therefore the compact suffix annihilates every derivative of the scalar cutoff and acts only on the input coefficient. There is **no need for the coefficient to be finite under this compact group or to be covariant**. This avoids the potentially false assertion that a vector finite under one maximal compact remains finite under a conjugate one.

For `eta_epsilon=(chi(G/epsilon)-1)G^p`, scaling the smooth compactly supported Euclidean function

\[
 h_\epsilon(v)=(\chi(T'\|v\|^2/\epsilon)-1)(T'\|v\|^2)^p
 =\epsilon^p h_1(v/\sqrt\epsilon)
\]

and applying the ordered chain rule proves, for `2p>m`,

\[
 \|\eta_\epsilon f\|_{B,m}
 \le C\epsilon^{p-m/2}\|f\|_{B+sm,m}.
\]

The compact-suffix expansion strengthens this to

\[
 \|\mathcal C_w(\eta_\epsilon f)\|_{B,5}
 \le C_w\epsilon^{p-m/2}\|f\|_{B+sm,J},
 \quad m=5+(4s-2)N,\quad J=5+nN,
 \quad |w|\le N.
\]

The original coefficient has **all finite derivative orders at the same decay exponent**. Consequently the possibly large `J` is harmless; only the decay loss `sm` must be uniform in the compact dimension. If the original finite-decay reserve gives `A>=B+2sp`, then `sm<2sp` supplies the required seminorm. The original Jacquet pairing continuity theorem `|beta(H,F)|<=C||H||_(B,4)||F||_(B,4)` on `C_B^5` now proves

\[
 \mathrm{RR}_{0,w}(\chi(\mathcal G/\epsilon)\mathcal G^pf)
 \longrightarrow\mathrm{RR}_{0,w}(\mathcal G^pf).
\]

This is convergence of the original quadratic integral. Both factors are proved to lie in the pairing domain before invoking continuity. No interchange of an unproved terminal-density limit is used.

For `N=3s`, choose **`p=6s²`**. Then

\[
 2p-m=12s^2-(12s^2-6s+5)=6s-5>0
 \quad(s\ge1).
\]

All constants depending on the compact type or dimension occur only in this convergence proof and disappear in the exact limit. They do not become factors in the AP6 inequality. This proves a sufficient quadratic-power cutoff supplier, **not the stronger original assertion for every smaller admissible `p`**. The parent's separate normalized spectral-word proof completes the other half of (EP) using the same form and no number-of-components loss.

Independent review: `/root/retained_theta` checked the PBW count and cofactor scaling and supplied the direct compact-suffix refinement above, which removes the preliminary compact-projection domain issue. Final review of the source orientation is ongoing at this checkpoint.

## 6. Exact Wigner/cofactor transport and norm cancellation

Written proof: [archimedean-wigner-transport.tex](../paper/shared/archimedean-wigner-transport.tex).

For the compact two-chain maps `A_±:W'_+→Hom(W_±,W_0)` of degree `a`, define the actual group polynomial `Acal_±(g)=A_±(Omega(g))`. The degree is at most `as`. The original cofactor proof gives

\[
 \Omega(k_L^{-1}n_L^{-1}g n_Rk_R)=k_R^{-1}\Omega(g),
 \quad\|\Omega(g)\|^2=\mathcal G(g)/T'.
\]

The compact covariance therefore makes the entire shifted orbital integrand equal to the original integrand postcomposed with the fixed matrix `A_±(Omega(g))`. The original character, both unipotent integrations, both compact factors, stabilizer quotient cut and measure normalization are retained. Hence, at every valid original representative,

\[
 \operatorname{Orb}_\pm(FAcal_\pm;g)
 =\operatorname{Orb}_0(F;g)A_\pm(\Omega(g)).
\]

Applying the compact lower inequality row by row and the operator upper bound in the Hilbert–Schmidt norm gives, with the identical point-density factor,

\[
 (\mathcal G/T')^aE_0(F)
 \le\kappa^2(E_+(FAcal_+)+E_-(FAcal_-)),
 \qquad E_\pm(FAcal_\pm)\le(\mathcal G/T')^aE_0(F).
\]

There is no representation-dimension loss. Since `0<G<=|D_s|²` and `D_s` is invariant under the same original actions,

\[
 jN_\pm^2(\mathcal G^pFAcal_\pm)
 \le (T')^{-a}jN_0^2(D_s^{2p+a}F).
\]

Combining the two shifted pointwise estimates with common numerical constant `C` yields exactly

\[
 E_0(F;\gamma)
 \le2C\kappa^2\mathcal G(\gamma)^{-2p-a}
                  jN_0^2(D_s^{2p+a}F).
\]

The `T'^a` and `T'^(-a)` factors cancel. At `p=6s²`, `a=30s²+6`, the pole is `42s²+6<=48s²` and the polynomial spectral degree is `42s³+6s<=48s³`. Thus the weaker cutoff power remains within the permitted quadratic pole and cubic spectral reserve. This transport uses the maps only on the actual cofactor image; it does not require an unproved ambient extension of the source `WigMap` predicate.

## 7. Additional pinned source ledger for the new proofs

All paths are under `lean/src/` and at `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

| Source | Git blob | Bounded ranges | Verified role |
|---|---|---:|---|
| `Formalism/FormalDegreeBessel/StatementIO.lean` | `6bcd97ca58319c4cc1f7c0adb02a14d5a94e49e0` | 78–112 | Exact `EabH` as complexified right derivative and Capelli convention |
| `Formalism/HermitianCurvature/StatementQ.lean` | `1e7035a15be9a61cbbe34f56091f376dcd464a07` | 150–208 | Full `CV`, scalar parameter shift, actual `tL00` |
| `Formalism/HermitianCurvature/StatementJF.lean` | `277bed43fa3155518a532b1aa28937728fb9b951` | 102–158 | Full Capelli left/right/postcomposition contracts and right-word form |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/ComponentFamilySettingOfSetting.lean` | `ccf66988236877f3ca879e2e519a8819400d9bb9` | 1–70, 355–460, 635–744 | Original all-zero residue corner and exact level-zero central-product form |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/CutLimE.lean` | `cfdb7cc60ae155100547acb63aa1118cfb49104c` | 1–90, 125–199 | Same actual `RR`, beta and central fold conventions |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/CutLimEvT.lean` | `2cab804bba05e5e5b9cf57d650be5f3f14b79bbe` | 1–56 | Actual level-zero integral, orientation and normalization |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/LevelZeroFormLeNormCOfEigenSum.lean` | `928405270b44a62052311b94e01b146d3405d8f7` | 1–39 | Same-form eigen-sum endpoint |

The ordinary geometric and analytic inputs were inspected in `paper/sections/recovered/84-rl-section.tex` (cofactor identity and covariance, 13–195), `paper/sections/recovered/94-jp-section.tex` (original derivative convention and pairing continuity, 1–90 and 382–425), `paper/sections/recovered/79-ca-section.tex` (level-zero site convention, 130–190), and `paper/shared/global-norm-frontier-top-lift.tex` (actual compact/unipotent covariance and quotient identity). These source checks are not Lean kernel replay.
