# Energy convergence for the original bounded cusp approximation

## Result and exact scope

This proves the bounded-approximation comparison left as item 2 in
Section 4 of [the signed boundary checkpoint](geometry-arithmetic-frontier-signed-boundary-energy.md).
It uses the original bounded regularization and its stated compatibility
conditions. No continuity of the bounded cusp potential, monotonicity in
the smoothing parameter, or new analytic hypothesis is added.

The result is convergence of the original bounded cusp approximations
in every positively corrected Kähler energy. Existence of the actual
geometric data and their arithmetic intersection dictionary remain
separate obligations. No whole RH or GRH node is completed.

## 1. The original kernel has enough symmetry

The source's mollifier is a nonnegative smooth function
\(\rho\) on \(\mathbb C^n\), supported in the open unit ball, with
\(\int\rho=1\). Its symmetry is
\[
             \rho(cw)=\rho(w)\qquad(|c|=1).
 \tag{1}
\]
Full radial symmetry is not assumed. Put
\[
 \rho_t(w)=t^{-2n}\rho(w/t),\qquad
       M_tu(z)=\int\rho_t(w)u(z-w)\,dw .
\]
If \(u\) is plurisubharmonic on a neighborhood of
\(\overline B(z,t)\), then
\[
                    u(z)\leq M_tu(z)
                         \leq\sup_{\overline B(z,t)}u .
 \tag{2}
\]
For the lower bound, average \(M_tu(z)\) over the changes of variable
\(w\mapsto cw\), \(|c|=1\). Lebesgue measure and \(\rho_t\) are
unchanged. The mean-value inequality on each complex disc
\(\zeta\mapsto z-\zeta w\) bounds its circular average below by
\(u(z)\). Integration against the normalized nonnegative kernel gives
the claim. All functions are bounded on the compact neighborhoods used
below, so Fubini applies. Upper semicontinuity and (2) imply
\[
                         M_tu(z)\longrightarrow u(z)
 \tag{3}
\]
at every interior point.

These are the actual hypotheses and proof in
IsPshLocallyIntegrableStatement, 13--17 and 72--98, and
PshMollB, 142--185. The source's PshMoll, 315--328, obtains the same
pointwise convergence. The dimension-zero case is just integration
over one point.

## 2. The inner charts give an exact global sandwich

Let \(X\) be the original compact complex manifold and let \(\psi\)
be its bounded relative cusp potential. Write \(\theta\) for the
curvature of the specified smooth reference metric. The source provides
finitely many coordinate charts \(V_j\), intermediate regions \(M_j\),
and inner regions \(I_j\), with
\[
 \overline I_j\subset M_j,\quad
 \overline M_j\subset V_j,\quad
 \bigcup_jI_j=X .
 \tag{4}
\]
In chart \(j\), the smooth function \(q_j\) is a local potential of
\(\theta\), up to a real holomorphic function, and
\(u_j=q_j+\psi\) is plurisubharmonic. Define
\[
             f_{j,t}=M_tu_j-q_j .
\]
The source has cutoffs \(-1\leq\eta_j\leq0\), with
\(\eta_j=0\) on \(I_j\), and a positive error
\(\epsilon(t)\geq t\) tending to zero. The overlap condition is
\[
 |f_{j,t}(x)-f_{k,t}(x)|\leq\epsilon(t)
               \quad(x\in M_j\cap M_k)
 \tag{5}
\]
for all sufficiently small \(t>0\).

Its gluing operation \(\mathcal G_\epsilon\) satisfies
\[
 \max_{j:x\in M_j}a_j(x)
 \leq\mathcal G_\epsilon(a)(x)
 \leq\max_{j:x\in M_j}a_j(x)+\epsilon ,
 \tag{6}
\]
and its **original** bounded approximation is
\[
 \psi_t=\mathcal G_{\epsilon(t)}
                \bigl(f_{j,t}+4\epsilon(t)\eta_j\bigr).
 \tag{7}
\]
These statements are definitions or proved bounds for the actual
gluing, not a replacement approximation.

Fix \(x\), and choose \(j\) with \(x\in I_j\). Equations (2) and (6),
together with \(\eta_j(x)=0\), give
\(\psi(x)\leq f_{j,t}(x)\leq\psi_t(x)\).
For every active chart \(k\), (5) and \(\eta_k\leq0\) give
\[
 f_{k,t}(x)+4\epsilon(t)\eta_k(x)
       \leq f_{j,t}(x)+\epsilon(t).
 \]
The upper bound in (6) therefore gives the exact sandwich
\[
       \boxed{\quad
       \psi(x)\leq f_{j,t}(x)\leq\psi_t(x)
                         \leq f_{j,t}(x)+2\epsilon(t).\quad}
 \tag{8}
\]
The chosen inner chart is fixed while \(t\to0\). Thus (3) implies
\(\psi_t(x)\to\psi(x)\) at **every** point of \(X\).

There is also a bound independent of \(t\). By (4) and compactness,
the convolution neighborhoods of every \(\overline M_j\) lie in a
fixed compact subset of its chart for all sufficiently small \(t\).
On those finitely many compact sets, \(|q_j|\leq Q\). If
\(|\psi|\leq M\), then
\[
             -M\leq\psi_t\leq M+2Q+2
 \tag{9}
\]
once \(\epsilon(t)\leq1\). Dominated convergence gives
\(\psi_t\to\psi\) in \(L^1\) for any smooth volume form on \(X\).
No smoothness or continuity of \(\psi\) has been used.

## 3. Positive correction and energy convergence

The source's gluing theorem proves that \(\psi_t\) is smooth and, in
each intermediate chart, its local Levi form satisfies
\[
             dd^c(q_j+\psi_t)\geq
                  -4C_\eta\epsilon(t)\,\omega_{\mathrm{chart}} .
 \tag{10}
\]
For a fixed Kähler form \(\omega\), finite-chart compactness compares
these coordinate forms with \(\omega\). Replacing \(C_\eta\) by
\(\max(C_\eta,0)\) if needed, (10) gives a constant \(C'\) such that
\[
                 \theta+dd^c\psi_t\geq-C'\epsilon(t)\omega .
 \tag{11}
\]
Consequently, for every \(z>0\), the original approximants are
\((\theta+z\omega)\)-plurisubharmonic for sufficiently small \(t\).
This uses BRegWeightLevi, 17--40, whose proof invokes the actual
bounded gluing theorem. It does not assume that the uncorrected
reference form is Kähler.

Choose \(t_0\) small enough for
\(\theta+dd^c\psi_{t_0}+(z/2)\omega\geq0\). Then
\[
          \omega_z=\theta+dd^c\psi_{t_0}+z\omega
 \]
is Kähler. Set \(v=\psi-\psi_{t_0}\) and
\(v_t=\psi_t-\psi_{t_0}\). They are \(\omega_z\)-plurisubharmonic
for small \(t\), \(v\) is bounded, \(v_t\geq v\), and
\(v_t\to v\) in \(L^1\). Monotonicity and upper semicontinuity of the
unnormalized Monge--Ampère energy give
\[
 E_{\omega_z}(v)
 \leq\liminf E_{\omega_z}(v_t)
 \leq\limsup E_{\omega_z}(v_t)
 \leq E_{\omega_z}(v).
 \tag{12}
\]
Thus the required energy convergence holds in every positively
corrected class. Changing the fixed smooth reference changes these
energies by a constant, so the conclusion holds for the original
reference as well.

The cited energy properties are BBGZ, Proposition 2.4, p. 195, in
the [published paper](https://www.numdam.org/item/10.1007/s10240-012-0046-6.pdf).
Its volume normalization can be removed by multiplication by the
fixed positive volume. The bounds and limiting statements above do
not assert uniformity over different models, arithmetic points or
conductors.

## 4. Mapping back to the exact cusp weight

Weights, 70--91, identifies this \(\psi\) with the prescribed bounded
weight relative to its smooth reference and defines \(\psi_t\)
exactly by (7). CpRegPhRegOfNonneg, 26--29, supplies precisely
\(\epsilon(t)\to0\) and the overlap comparison (5).

In the signed-boundary application, CpRegPhRegOfNonneg, 71--73, sets
the corrected weight to \(\operatorname{phMu}+U/2\).
StokesLimitBound, 33--34, requires the bounded and logarithmic
regularizations to have the same reference on the original variety.
Thus their relative potentials satisfy
\[
                         \psi-\varphi=U/2
 \tag{13}
\]
on the original open part. Equations (8)--(12) apply to that exact
bounded sequence, closing its energy-convergence obligation.

| Pinned source excerpt | Role |
|---|---|
| Regularisation.Statements, 32--56, 79--88, 121--125 | Finite inner cover, reference potentials, cutoffs, bounded plurisubharmonic data |
| Regularisation.BoundedStatements, 19--28 | Exact local smoothing and global gluing |
| Regularisation.ChartFun, 20--33 | The two sides of (6) |
| FrameDefinitions.Weights, 70--91 | Exact original bounded regularization |
| FrameDefinitions.CpRegPhRegOfNonneg, 26--29, 71--73 | Parameter compatibility and the factor \(1/2\) |
| StabilizerCovolume.BRegWeightLevi, 17--40 | Uniform chart neighborhoods, smoothness and near-semipositivity |
| ParallelGeometry.StokesLimitBound, 33--34, 76--85 | This compatibility is already part of the original signed-limit hypotheses |

The arithmetic intersection metric-variation identity, its comparison
with integration on the original compact model, and the vertical and
rational twists remain distinct from this theorem. They are not
silently supplied by energy convergence.

## Verification

The companion checker authenticates the source modules at
\(\texttt{ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de}\), records
bounded excerpt hashes and the primary-reference hash, and checks the
finite gluing inequalities exactly. A negative control shows why
normalization and nonnegativity alone cannot replace the actual
circle invariance; another records the role of an inner cutoff that
vanishes. These computations supplement the proof and do not
constitute a Lean build.
