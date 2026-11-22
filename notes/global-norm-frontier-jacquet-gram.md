# Exact exterior-Pieri transfer to the original Jacquet norm

## Result and scope

This package supplies the exact transfer from the proved flag-product
moments to the **original** leading-minor Jacquet norm, including the
original real q0 budget and both original character scales. Its
discrete-series and signed exterior-Pieri decompositions remain supplied
data, together with the original period-normalized Bessel family and
the normalized-lowering theorem's exact Capelli scalar supplier.
Neither the radial measure nor the Gram form is changed.

Different exterior-Pieri summands have orthogonal Jacquet transforms.
The common radial normalization cancels exactly, and their same-measure
formal degrees satisfy
\[
 \sum_{|I|=\ell}\frac{d(\mu+\mathbf1_I)}{d(\mu)}
                         ={n\choose\ell}.                       \tag{1}
\]
The original gap preserves every shifted ordering. The identity of
positive degrees is not asserted across a chamber wall.

For \(n=2r+k+1\), \(m=2r+2\), \(0\le\ell\le r+1\), let
\(\mathcal N(F)\) be the actual squared Jacquet norm, and \(D_\ell\)
the original leading minor, equal to Dbig on the big cell. The result is
\[
 \mathcal N(D_\ell F)
 \le {n\choose\ell}(TT')^\ell b^{8m^2}\mathcal N(F).              \tag{2}
\]
Here the left side is exactly
\(\int|D_\ell|^2\|JF\|_{\rm HS}^2\,d\nu_{\rm rad}\), with the
original measure. The original positive \(T,T'\) remain explicit.
For \(\ell=0\) the norms agree without a moment reserve. If
\(T,T'\le b^{Cm}\), \(C\ge0\), the bound is at most
\(b^{(C+9)m^2}\mathcal N(F)\).

For the original character scale, the exact additional factor is
κ to the power 4rℓ−2ℓ(ℓ−1). It combines with the original scaled
T,T′ bounds and gives the original leading-minor estimate with
Cb≥Ch+5, Cq≥200 and Cg≥10^6. The two scales are treated separately
below; no inverse scale or measure factor is discarded.

**Classification:** closed Gram-transfer, real-budget and character-scale
subobligations; improved sufficient condition for the complete original
local interface. Representation, Pieri and period-normalized Bessel
family existence, the exact normalized-lowering inputs, weighted orbital
estimates and global norm assembly remain separate.
This does not close W08 or change a whole-node count.

## Exact identities and proof

Use inner products linear in the first variable. For original
period-normalized maps \(B_\mu,B'_\mu\), same-measure formal degree
\(d_\mu\), and a finite coefficient
\[
 F(g)=\sum_a\langle\sigma_\mu(g)y_a,x_a\rangle A_a,\qquad
 s_\mu(F)=\sum_a\langle A_aB'_\mu y_a,B_\mu x_a\rangle,
\]
the existing mixed Jacquet unfolding theorem and Schur orthogonality give
\[
 \langle JF,JH\rangle_{\rm rad}
 =c_{\rm rad}s_\mu(F)\overline{s_\mu(H)}/d_\mu.                 \tag{3}
\]
There is one positive \(c_{\rm rad}\) for the original measures and
compact data, independent of the representation parameter.
For inequivalent parameters the pairing is zero. Indeed, the group
pairing vanishes for every subgroup parameter before regularization.
The diagonal calculation uses the finite Schur sum and the two
absolute integrals in the original period identities. Its coefficient
decay hypothesis is the one already needed by the Jacquet theorem.

The original flag wedges \(\omega_\ell,\omega'_\ell\) are fixed by
their period subgroups. The signed exterior-Pieri projections have
scalars
\[
 B_{\mu+\mathbf1_I}p_I(\omega_\ell\otimes v)=\kappa_I B_\mu v,\qquad
 B_\mu(\operatorname{ev}_{\omega_\ell}i_Iy)
 =\epsilon_I\overline{\kappa_I}B_{\mu+\mathbf1_I}y,
\]
and analogously on the right. The adjoint identity requires the
original period normalization; equivariance alone does not imply it.
Zero shifted maps have scalar zero. The tensor coefficient decomposition
\(D_\ell F=\sum_I F_I\) gives
\[
 s_{\mu+\mathbf1_I}(F_I)
 =\epsilon_I\kappa'_I\overline{\kappa_I}s_\mu(F).
\]
Unitriangularity makes \(D_\ell\) constant on the original period orbit,
so \(J(D_\ell F)=D_\ell JF\). Applying mixed orthogonality proves
\[
 \boxed{\mathcal N(D_\ell F)=c_{\rm rad}|s_\mu(F)|^2
        \sum_{|I|=\ell}
          \frac{|\kappa_I\kappa'_I|^2}{d_{\mu+\mathbf1_I}}.}      \tag{4}
\]
This exact positive Gram formula is the main new transfer.

The proved isometric maps
\(T_\mu=\sqrt{d_\mu}B_\mu\sigma_\mu(\cdot)\) have mutually
orthogonal images in the same induced Hilbert space, by Schur's lemma
applied to their bounded cross pairing. The tensor identity and
Cauchy--Schwarz then give
\[
 |\kappa_I|^2\frac{d_\mu}{d_{\mu+\mathbf1_I}}\|y\|^2
 \le\int\|(\bigwedge^\ell g^{-1})\omega_\ell\|^2
                    \|T_{\mu+\mathbf1_I}y(g)\|^2dq.            \tag{5}
\]
Specifically, write \(i_Iy=(x_e)_e\) in an orthonormal exterior
basis, test with \(\Gamma e\otimes x_e\), and use the signed adjoint.
Cauchy--Schwarz gives the bound with \(\|x_e\|^2\) on the left;
when \(x_e=0\), no cancellation is made. Sum and use
\(\|y\|^2\le\sum_e\|x_e\|^2\). The scalar sum on the right is
the **positive** exterior norm in (5).

Gram--Schmidt identifies that norm with \(\prod_{a<\ell}L_a^2\).
Apply the established flag-product bound to a nonzero lowest
compact-type vector in the shifted family:
\[
 |\kappa_I|^2d_\mu/d_{\mu+\mathbf1_I}\le T^\ell b^{4m^2},
 \qquad
 |\kappa'_I|^2d_\mu/d_{\mu+\mathbf1_I}\le(T')^\ell b^{4m^2}.     \tag{6}
\]
Its sufficient integer reserve is
\(\|\nu\|_1+\ell+a_\ell\le q_{\rm fam}\), where
\(a_0=0,a_1=1,a_\ell=\ell+1\) for \(\ell\ge2\).
The original integer reserve \((r+1)(r+2)\) suffices, including
\(r=0\). The level reserve is valid since the vector has level zero.

For (1), the polynomial \(\sum_{|I|=\ell}\Delta(x+\mathbf1_I)\),
\(\Delta(x)=\prod_{i<j}(x_i-x_j)\), is alternating of degree at most
\(\deg\Delta\). It is divisible by \(\Delta\), hence is a constant
multiple of it. The top homogeneous term supplies \({n\choose\ell}\).
The gap at least two preserves the chamber and allows the same
positive formal-degree constant in every summand.
Inserting (6) and (1) into (4) proves (2), with no bound on an
individual formal-degree ratio. If \(s_\mu(F)=0\), (3) gives
\(JF=0\) almost everywhere, and its weighted norm is zero directly.

## The original real budget supplies the integer family

Set Q=q0(Cq,m,ε,u,λ0) and R=(r+1)(r+2), retaining the original
totalized real-infimum convention (the infimum of the empty finite set
is zero). Both λ and λ0 are Harish--Chandra parameters for the same
group. Each coordinate minus (n−1)/2 is an integer, so
ν=λ−λ0 is an integer vector and its real l1 norm is its exact integer
norm. Consequently

\[
 \|\lambda-\lambda_0\|_1+R\le Q
 \quad\Longrightarrow\quad
 \|\nu\|_1+R\le q_{\rm fam}:=\lfloor Q\rfloor.                 \tag{7}
\]

There is no rounding loss. In particular Q≥2 and q_fam≥2.
The compact highest weight is u−ρc. Its nonzero highest vector,
evaluated on each diagonal circle at angle 2π, shows that
u_i−(k−1)/2 is integral. Thus λ0,a−u_i lies in Z+1/2, exactly
as required by the original Num predicate. The same argument applies
to u′. This uses the supplied compact type, not a new integrality
hypothesis.

Original interlacing makes the cloud exactly the first k−1 indices,
for both u and u′: λ0,i lies strictly between u_i and u_i+1 for
i<k−1, and all remaining coordinates lie below u_k−1.
Thus their cloud gaps agree. Put ga=g_cloud(λ0) and
h=h_NC(λ0). If Cq≥200, then

\[
 ga\ge C_qQ\ge100(q_{\rm fam}+1),\qquad
 h\ge C_q^2\sqrt m\,Q\ge100(q_{\rm fam}+1).                  \tag{8}
\]

The sets defining h and ga are nonempty: the signature has both
signs, while an empty cloud-pair set would make Q=0 and contradict
(7). In particular the original interface has no instance with
k≤2 and this positive reserve; the empty case is not silently
assigned an infinite gap.

The remaining clauses of Num are the original shape, parameter
bounds and interlacing. Their large-gap gate follows directly from
the original noncompact-gap hypothesis. For a=(r+1), n≥2a,
the original quantities satisfy

\[
 A_G\le4an,\quad d_N\le2an,\quad A_S\le2an^2,\quad
 M\le2a^2,
\]
\[
 2M(A_S+A_G)+A_G+3\le20a^3n^2,\qquad
 9an^2+3A_G+3\le16an^2.
\]

For h at least Cg m^(9/2)(3an²+n³), the right side of that
gate is

\[
 a_{\rm gap}(h/4)=h/(32\sqrt{2a})
       \ge(C_g/2)a^4(3an^2+n^3).
\]

Cg≥10^6 therefore supplies both inequalities and h/4≥120n³.
It also supplies the required shape bound B≥10^6n^7.
The signature εSH is exactly ε48 in these same indices.
Hence the original assumptions imply Num for q_fam on both sides.
They do not by themselves construct the representation or tensor
decomposition family; that remains a distinct supplier.

## Exact transport of both original character scales

Write cκ=κc_std, c_std=−2i and κ>0. The original diagonal torus
tκ has first isotropic entries κ^(i−r), middle block the identity,
and the reciprocal entries on the opposite flag. It fixes z and z′,
centralizes both compact stabilizers, normalizes the original N,
and satisfies ψ_std(n)=ψκ(tκ n tκ^−1). In particular

\[
 (\bigwedge^\ell t_\kappa^{-1})\omega_\ell
       =\kappa^{S_\ell}\omega_\ell,\qquad
 S_\ell=r\ell-\ell(\ell-1)/2.                               \tag{9}
\]

Transport a period-normalized map by B1=Bκσ(tκ).
Push the original N measure by Ad(tκ^−1) and the quotient measure
by left multiplication by tκ^−1. Keep group Haar and both compact
Haar measures. Direct substitution in the original period integral
proves the normalization with these exact pushed measures. This is
the original torus conjugation, and introduces no scalar by fiat.
Since tκ fixes z,z′, the original T,T′ are unchanged.

Intertwining the exterior projection with tκ^−1 and using (9) gives

\[
 \kappa_I^{(\kappa)}
      =\kappa^{S_\ell}\kappa_I^{(1)},\qquad
 (\kappa'_I)^{(\kappa)}
      =\kappa^{S_\ell}(\kappa'_I)^{(1)}.                     \tag{10}
\]

Apply the standard-character moment bound with the exact pushed
measures, then use (4) for the **original** character and radial
measure. This avoids changing the original big-cell coordinates
or replacing its radial integral. It proves

\[
 \mathcal N_\kappa(D_\ell F)
 \le\binom n\ell\kappa^{4S_\ell}(TT')^\ell
                 b^{8m^2}\mathcal N_\kappa(F).              \tag{11}
\]

Only positivity of T,T′ was needed by the moment theorem, so this
application also covers original scales for which T or T′ is below 1.

Now retain the exact original bounds on
X=T(κ/a)^(2r) and X′=T′(κ/a)^(2r). Both are at most
b^(Ch m); also a≤b^Ch and a^−1≤b^Ch. The original shape
forces b>1, so these inequalities force Ch≥0. Direct algebra gives

\[
 \kappa^{4S_\ell}(TT')^\ell
 =(XX')^\ell a^{4r\ell}\kappa^{-2\ell(\ell-1)}.             \tag{12}
\]

If κ=1, the exponent of a is 4rℓ. If κ=a, it is
2ℓ(2r−ℓ+1), which lies between zero and 4rℓ.
Thus both original branches give

\[
 \kappa^{4S_\ell}(TT')^\ell
 \le b^{2C_hm\ell+4C_hr\ell}\le b^{2C_hm^2}.
\]

Since n≤b and ℓ≤m/2, (11) is at most
b^((2Ch+9)m²) times the original unweighted norm. Therefore
Cb≥Ch+5 supplies **the original BesselLeadingMinorBound** under
the explicitly retained representation, Pieri, period-normalized Bessel
and exact normalized-lowering suppliers. This
proves its parameter, normalization and scale transport, with its
original quantifiers and reserve. It does not assert that the named
Lean definition is itself a supplied proof.

## Exact frontier still open

The original BesselLeadingMinorBound uses the real budget
\[
 \|\lambda-\lambda_0\|_1+(r+1)(r+2)
 \le\min\{h_{\rm NC}(\lambda_0)/(C_q\sqrt m),
                     g_{\rm cloud}(\lambda_0)\}/C_q
\]
and retains \(\kappa\in\{1,a\}\) and \(T_z(\kappa/a)^{2r}\).
Equations (7)--(12) now transport those data without changing the
original radial measure or Dbig factors. The separate supplier of the
whole signed representation and normalized Bessel family, the exact
normalized-lowering inputs, the weighted orbital estimate
and the global return sum remain.
The local formula (4) does not identify the global automorphic
period Gram operator.

## Verification

All original sources are pinned to jsmorph/rh at
ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de. The checker records full
file hashes and bounded excerpts for TensorMomentTransfer,
TensorMomentWeighted, TensorMomentEstimate, TensorWeightedBesselGap,
BesselSettingUniformConstant, BesselExteriorPowerConstantBoundLargeGap,
WaveBallEstimateWeightedDualAlt, BesselNormSqEqConstMulArchPairing,
LeadMinorK, OnePlaceEstimates and the exact torus, compact-type,
integer-family and numerical-gap definitions used in (7)--(12).

Run python3 scripts/check_global_norm_frontier_jacquet_gram.py --offline.
Exact checks cover (1), a chamber-wall negative control, signed
projection identities, scalar/formal-degree cancellation, both scale
branches, exact rounding and numerical-gap reserve edges. They
supplement the written proof, without asserting a representation
construction, weighted orbital estimate, global assembly or Lean build.
