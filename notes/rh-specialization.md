# Ordinary RH: a smaller target and the surviving arithmetic work

## Status and first conclusions

This is a comparison of the current conventional proof program with the pinned source `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. It proves shorter sufficient analytic criteria and records exact specializations of the arithmetic interfaces. It does **not** prove the arithmetic estimate or the Riemann hypothesis. The source certificate records bounded reads and Git/SHA-256 checks; no new Lean compilation is claimed.

Ordinary RH needs only the corrected zeta sum

\[
G(x)=\sum_{n\le x}\Lambda(n)(x/n-1)-x\log x+(1+\gamma)x,
\qquad x\ge1.
\]

The shortest sufficient route is an eventual one-sided bound for this single real function. It removes all character-family bookkeeping from the analytic argument. The source arithmetic construction does not collapse to a fixed-dimensional construction: specializing its target to conductor one still leaves growing CM fields, auxiliary quadratic characters, integral theta maps and quantitative cohomology/covolume requirements. Those surviving requirements are being separated explicitly below.

## 1. A short one-sided criterion, with a complete proof

### A positivity lemma

Let \(f:[X,\infty)\to[0,\infty)\), where \(X\ge1\), be locally integrable and of at most polynomial growth. Write \(\alpha\) for the abscissa of convergence of
\[
F(s)=\int_X^\infty f(x)x^{-s-1}\,dx.
\]
If \(\alpha\) is finite, then the holomorphic function on \(\Re s>\alpha\) cannot extend holomorphically through the real point \(\alpha\).

Indeed, if such an extension existed on a disk of radius \(r>0\) about \(\alpha\), put \(\sigma_0=\alpha+r/4\). Its Taylor series about \(\sigma_0\), evaluated at \(\sigma_0-z\), has coefficients
\[
\frac{(-1)^k F^{(k)}(\sigma_0)}{k!}
=\int_X^\infty f(x)x^{-\sigma_0-1}\frac{(\log x)^k}{k!}\,dx\ge0.
\]
Differentiation is justified by convergence at any intervening real point between \(\alpha\) and \(\sigma_0\). Take \(r/4<z<r/2\). The Taylor series converges, and Tonelli's theorem identifies its sum with \(\int_X^\infty f(x)x^{-(\sigma_0-z)-1}\,dx\). This is finite at a point to the left of \(\alpha\), a contradiction. The case \(\alpha=-\infty\) needs no boundary argument.

### The zeta criterion

**Proposition.** Fix \(0<\theta<1\). Either of the eventual estimates
\[
G(x)\le Cx^\theta\quad(x\ge X),
\qquad\text{or}\qquad
G(x)\ge-Cx^\theta\quad(x\ge X),
\]
with fixed finite \(C\ge0\) and \(X\ge1\), implies that \(\zeta(s)\) has no zero in \(\Re s>\theta\), with its pole at one excluded from the assertion.

**Proof.** Direct integration of each prime-power term gives, initially for \(\Re s>1\),
\[
\mathcal G(s):=\int_1^\infty G(x)x^{-s-1}\,dx
=-\frac{\zeta'(s)/\zeta(s)}{s(s-1)}
 -\frac1{(s-1)^2}+\frac{1+\gamma}{s-1}.
\]
The Laurent expansion \(\zeta'/\zeta=-1/(s-1)+\gamma+O(s-1)\) makes the apparent singularity at one removable. At a nontrivial zero \(\rho\) of multiplicity \(m\), the residue is \(-m/[\rho(\rho-1)]\ne0\). The calculation is also proved in manuscript Section 2.

There is no real zeta zero in \((0,1)\): the alternating series \(\eta(s)=\sum_{k\ge1}((2k-1)^{-s}-(2k)^{-s})\) is positive for real \(s>0\), and \(\zeta(s)=\eta(s)/(1-2^{1-s})<0\) for \(0<s<1\). The Euler product handles real \(s>1\). Thus \(\mathcal G\) is holomorphic near every real \(s>0\).

For the upper bound use \(f(x)=Cx^\theta-G(x)\ge0\) on \([X,\infty)\); for the lower bound use \(f(x)=Cx^\theta+G(x)\). Its Mellin transform is
\[
\frac{CX^{\theta-s}}{s-\theta}\mp\mathcal G(s)
\quad\text{plus an entire finite-interval integral}.
\]
It is therefore holomorphic near every real \(s>\theta\). The positivity lemma forces its abscissa of convergence to be at most \(\theta\). The resulting holomorphy on \(\Re s>\theta\) makes \(\mathcal G\) holomorphic there, so it cannot have a pole arising from a zeta zero. This proves the proposition. \(\square\)

**Corollary.** Suppose \(\delta_j>0\) tends to zero and, for each fixed \(j\), one of these one-sided bounds holds eventually with exponent \(1/2+\delta_j<1\), allowing its finite constant, threshold and even its direction to depend on \(j\). Then RH follows from the proposition and the functional equation. A single eventual bound with exponent exactly \(1/2\) also suffices.

This is a stronger arithmetic hypothesis than the manuscript's cofinal-window criterion. A bound valid on arbitrarily late intervals must not be substituted into this eventual-positivity proof. Conversely the lower-bound variant is available here because zeta has no real zeros; it should not be carried over without qualification to general real Dirichlet characters.

The classical analytic inputs are the continuation and Laurent expansion in [DLMF §25.2](https://dlmf.nist.gov/25.2), the alternating series in its equation 25.2.3, and the functional equation and zero symmetry in [DLMF §25.4](https://dlmf.nist.gov/25.4) and [§25.10](https://dlmf.nist.gov/25.10). These pages were checked directly. The positivity lemma itself is proved above.

## 2. Exact source specialization already checked

The source has a primitive conductor-one character `PChar.one` (`PrimePairSizeCondition.lean:7–19`). Its cyclic level has selected set `{one}`, no designated quadratic character, and order one (`ExplicitFormulaErrorOfHostConditions.lean:105–121`). Consequently its `Level.Gm` is precisely the corrected zeta sum (same file, 32–38).

For a frame, `A0.index=o` (`FrameFacts.lean:208–217`). At order one, therefore, `A0=A`. The source subset-share requirement becomes automatic: its target share is \(4/(3\cdot1+1)=1\), and every translate belongs to `A0`. This removes a genuine distribution requirement, not just a character label.

However `EAtH` still asks for the auxiliary-character bounds and logarithmic derivatives (`ExplicitFormulaErrorOfHostConditions.lean:144–151`). `SupplyChi.lean:8–16` and `HostOfField.lean:17–23` still consume `VWinAt one 401`. That predicate retains all allowed growing page sizes, auxiliary prime pairs and local cohomology models (`ExistsPageN.lean:12–49`). It is not made automatic by the conductor-one substitution.

The source's assigned values at poles are not part of this ordinary-mathematics translation. Its own `zero_ne_one` lemma (`FirstClaimLemmaTwoFourOfLemmaTwoThree.lean:540–552`) explicitly disposes of the principal point using `riemannZeta_one_ne_zero`. Here the pole at one is excluded and its cancellation in \(\mathcal G\) is checked directly.

## Work continuing from this checkpoint

The remaining audit will record the four-character quotient, its signed companion obstruction, the specialized CM-field family and quantitative cohomology contract, and a precise list of supplier requirements that the current arithmetic route still needs. A fixed quadratic Dedekind-zeta alternative and the exact limitations of QRH/no-Siegel inputs will be compared without treating any unproved arithmetic estimate as a theorem.
