# Ordinary RH: a smaller target and the surviving arithmetic work

## Status and first conclusions

This is a comparison of the current conventional proof program with the pinned source `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. It proves shorter sufficient analytic criteria and records exact specializations of the arithmetic interfaces. It does **not** prove the arithmetic estimate or the Riemann hypothesis. The source certificate records bounded reads and Git/SHA-256 checks; no new Lean compilation is claimed.

Ordinary RH needs only the corrected zeta sum

\[
G(x)=\sum_{n\le x}\Lambda(n)(x/n-1)-x\log x+(1+\gamma)x,
\qquad x\ge1.
\]

The shortest sufficient route is an eventual one-sided bound for this single real function. It removes all character-family bookkeeping from the analytic argument. The source arithmetic construction does not collapse to a fixed-dimensional construction: specializing its target to conductor one still leaves growing CM fields, auxiliary quadratic characters, integral theta maps and quantitative cohomology/covolume requirements. The exact savings and surviving obligations are separated below.

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

## 3. The four-character quotient and the smallest signed companion

For a primitive nonprincipal character, use the manuscript convention
\[
G_\chi(y)=\sum_{n\le y}\Lambda(n)\chi(n)(y/n-1)
                 +yL'(1,\chi)/L(1,\chi).
\]
In the source host, the first additive sign is the quadratic character
\(\chi_d(n)=(n/d)\). The second sign is \(\chi_q(n)=(n/q)\) under the additional host condition `PsQ`. That condition is supplied by the actual field construction (`FieldChi.lean:53–58`); it is not a consequence of `HostAx` alone (`ConjEMemHostFIff.lean:82–83,98–101`). The swap between the additive and multiplicative sign coordinates is recorded in `RecH.toE`. Thus the quadratic attached to the unavoidable negative first-sign coefficient is the character of \(\mathbf Q(\sqrt{-d})\), not the designated quadratic at \(q\).

When the translation subgroup is the whole group \(A\), exactly four characters survive Fourier projection. At a common argument their signed sum is
\[
D_+(y)=G(y)+G_{\chi_q}(y)-G_{\chi_d}(y)
                         -G_{\chi_q\chi_d}(y).
\tag{3.1}
\]
Here \(q,d\) are distinct odd primes, and the product is primitive of conductor \(qd\). In the supplied hosts, both primes are \(3\pmod4\). The main-scale `EAtH.bdG` and `bdL` conditions therefore concern only these three nonprincipal quadratic characters, rather than characters of an arbitrary fixed target conductor. The existing manuscript Section 11 already proves their simultaneous selection, conditional on its stated uniform QRH input; its RH paragraph begins “For the RH subcase take the principal base character of conductor 1.” That result is reused, not counted as a new proof here. The separate larger-scale estimate can still involve characters of the growing group \(A\).

For RH alone, rearrange (3.1) as
\[
G(y)=D_+(y)+C_{q,d}(y),\qquad
C_{q,d}=G_{\chi_d}+G_{\chi_q\chi_d}-G_{\chi_q}.
\tag{3.2}
\]
Only an upper bound for this **single signed companion** is required. Three separate absolute bounds suffice but are stronger. The auxiliary primes may vary with the scale, since the positive target on the left is always the same zeta function. By contrast, applying the positive-family theorem directly to \(G+G_{\chi_q}\) requires \(q\) to remain fixed within each accuracy's sequence of windows. The source prime-selection construction does not have that property.

### Why cancellation alone cannot remove every companion

For a nonempty selected set \(T\) and any subgroup \(B\subseteq A\), the Fourier coefficients are
\[
\alpha_\psi=|T|^{-1}\sum_{t\in T}\psi(e_1(t)),
\qquad \psi\in B^\perp.
\]
The principal coefficient is 1 and the first-sign coefficient is \(-1\). Moreover,
\[
\sum_{\psi\in B^\perp}\alpha_\psi=0,
\]
because every \(e_1(t)\) is nonidentity in \(G/B\). Merging characters with the same primitive inducer preserves this total coefficient mass; so does any finite linear combination of such host projections. Consequently these coefficient identities alone cannot produce a nonzero combination with all coefficients nonnegative. This is a finite Fourier obstruction, not an assertion of linear independence of the functions \(G_\chi\). A companion estimate or a different arithmetic identity is needed.

## 4. A single RH arithmetic budget after averaging

The three-mean comparison in [the averaged-budget note](averaged-error-budget.md) is an additional conditional construction route. It assumes that the pooled empirical weight measures
\[
\frac1{|A|m}\sum_{u\in A}\sum_{i=1}^m\delta_{w_{u,i}(\rho)}
\]
are invariant under translation of \(\rho\) by \(A\). This exact symmetry is weaker than requiring every chosen frame to be a translate. It is **not yet verified for the source supplier**.

Under that symmetry, its exact Fourier identity and Jensen comparison give
\[
Q_4:=\frac1{|T|}\sum_{t\in T}D_+(a_t/b)
\le \frac{\overline E-J_{\rm thin}}k+J_{\log},
\qquad k=|T|mbd_0/2>0.
\tag{4.1}
\]
Here \(b\) is the actual mean of the thick weights, \(d_0\) their density, \(J_{\rm thin}\) the two signed thin mean samples, and \(J_{\log}\) the normalized logarithmic arithmetic/geometric-mean dispersion. These are defined using the same maps, top labels and weight profiles as \(\overline E\). They are not free numerical choices. All higher-order characters cancel only after the explicit symmetry hypothesis is imposed.

There is a useful elementary way to center the zeta target without estimating derivatives of any auxiliary \(L\)-function.

**Centering lemma.** For \(h\ge0\), \(x-h\ge1\) and \(|y-x|\le h\),
\[
|G(y)-G(x)|\le h(1+\log(x+h))^2.
\tag{4.2}
\]
Indeed, away from integers,
\[
G'(v)=\sum_{n\le v}\Lambda(n)/n-\log v+\gamma.
\]
The inequalities \(0\le\Lambda(n)\le\log n\), \(\sum_{n\le R}1/n\le1+\log R\), and \(0<\gamma<1\) bound its absolute value by \((1+\log(x+h))^2\) on \([x-h,x+h]\). The sum is continuous and piecewise differentiable, so integration proves (4.2).

Combining (3.2), (4.1) and (4.2), whenever \(x-h\ge1\) and \(|a_t/b-x|\le h\) for every top label, gives the proved conditional comparison
\[
\boxed{\displaystyle
G(x)\le
\frac{\overline E-J_{\rm thin}}k+J_{\log}
+\frac1{|T|}\sum_{t\in T}C_{q,d}(a_t/b)
+h(1+\log(x+h))^2.}
\tag{4.3}
\]
Thus it is enough to bound **the entire right side** by \(M_jx^{1/2+\delta_j}\), with \(\delta_j>0\) tending to zero, throughout arbitrarily late whole windows \([U,U^{b_j}]\), where \(b_j>1\) and finite \(M_j\ge0\) are fixed before \(U\) varies. The existing window theorem then gives RH. The host, growing dimensions, primes and auxiliary error decomposition may vary with \(x\). No separate absolute estimate of each summand is intrinsic to this criterion. An eventual bound would also allow the shorter argument of Section 1.

**The source centering condition survives taking the actual mean.** Write \(b_0>0\) for the source lower endpoint. `SplitInertia.lean:44–46` gives \(|a_t/b_0-x|\le1\) and all thick weights in \([b_0,b_0+\eta+1]\), so their mean \(b\) lies in that interval. `SChain.lean:50–51` gives \(6f(x+1)(\eta+1)\le b_0/x\). For \(f\ge1\), \(x\ge3\), and \(r=(b-b_0)/b_0\ge0\),
\[
\frac{x-1}{1+r}\le\frac{a_t}{b}\le x+1,
\qquad
\left|\frac{a_t}{b}-x\right|
\le1+\frac{(x-1)(\eta+1)}{b_0}
\le1+\frac{x-1}{6fx(x+1)}<2.
\]
Therefore the general centering lemma applies with \(h=2\), costing only \(2(1+\log(x+2))^2\). No additional exact centering-at-the-mean hypothesis is needed when reusing those source size conditions.

**Precise source symmetry gap.** `QuadraticLogDerivCongr.lean:367–407` defines the actual weights by choosing a point for each translation and reading its Harish–Chandra parameter: `DataParams₂.lean:73–74` gives \(w_j=(\mathrm{hc}(\tau).e_j:\mathbf R)\). `FamCore.lean:90–105,132–136` matches hosts, ranks and top orders between the chosen points; it does not assert equality of the translated weight profiles or pooled measures. `AsmRec.lean:10–28` exposes the same Harish–Chandra parameter as input data. These interfaces therefore do not yet justify the symmetry step. A coherent orbit construction of the same integral lattices and period-normalized maps would have to establish it. Without it, use the already proved general finite-error comparison in manuscript Section 10, retaining all characters and its transfer costs.

## 5. The specialized fields and the quantitative cohomology that remain

At order one, `FrameFacts.lean:178–192,208–225,250–264` gives
\[
A=A_0,\qquad A\simeq\mathbf Z/2^e\mathbf Z,\qquad |A|=2^e.
\]
Indeed the distinguished cyclic subgroup is all of \(A\); the frame map is injective there and surjective onto the cyclic group of order \(2^e\). The source page condition still requires
\[
x^{2+8\varepsilon}\le2^e\le2x^{2+8\varepsilon}.
\]
Consequently even this conductor-one case has growing field degree.

The exact kernel condition of `ExistsPageN.lean:19–25`, together with the conductor-one substitution, identifies the host field as
\[
E=\mathbf Q(\zeta_{2^{e+2}})^+
       (\sqrt{-q},\sqrt{-d}),\qquad [E:\mathbf Q]=4\cdot2^e.
\tag{5.1}
\]
To see the identification, its fixed subgroup consists of residue classes that are \(\pm1\) in the \(2\)-power factor and have both quadratic symbols equal to one. The Chinese remainder theorem makes these three conditions independent. Their fixed fields are the real cyclotomic field and the two imaginary quadratic fields displayed in (5.1). Thus the RH source fields are abelian extensions of degree a power of two; they are not fixed quadratic fields.

The two auxiliary primes also grow: `ExistsPageN.lean:27–39` puts \(\log q\) between \(Y^{\varepsilon/5}/2\) and \(Y^{\varepsilon/5}\), and \(\log d\) between \(Y^{\varepsilon/5}(\log Y)^2/2\) and \(Y^{\varepsilon/5}(\log Y)^2\). Their congruence and splitting requirements remain. Replacing one by 3 or 4 is incompatible with this particular supplier.

The surviving `VWinAt one 401` is much stronger than merely finite rational cohomology. The exact `VVle` predicate (`ExistsPageN.lean:12–17`) asks for finite lengths at every coefficient prime \(\ell\), every local-data realization, and every positive twist below the growing cutoff, with
\[
\sum_{\ell\in S}\log\ell
 \sum_{1\le k<\lfloor x^{401}\rfloor}
 \operatorname{length}_{\mathbf Z_\ell}\Sha(E,\ell,k)
\le \exp(x^\varepsilon/2)
\tag{5.2}
\]
for every finite set of coefficient primes \(S\). In the pinned definition the module is the kernel of localization in degree one for the discrete Tate twist \(\mathbf Q_\ell/\mathbf Z_\ell(-k)\), with ramification allowed at the places over \(\ell\) (`Formalism/GaloisCohomology/Statement.lean:54–83`). The window predicate quantifies all allowed page functions and auxiliary prime pairs before asserting cofinal whole windows. Finite-dimensional or characteristic-zero semisimplicity does not supply this integral quantitative bound.

The abelian structure suggests a possible alternative through characterwise integral cohomology or special-value formulas. That is a research option, not a completed replacement: an exact uniform bound for the localization kernel in (5.2), throughout the growing twists and fields, has not been identified. Odd-prime idempotents do not settle the prime 2, and regulator or denominator factors cannot be discarded from a special-value formula.

## 6. Complete dependency comparison

The comparison concerns the actual mathematical contracts, rather than the number of imported source files. The current preferred proof has already substituted the reviewed classical local/global correspondence theorem for its long universal Galois supplier; that substitution applies to both RH and GRH and is not an extra RH saving.

| Part of the full program | Genuine RH saving | What still has to be supplied in the present arithmetic route |
|---|---|---|
| Analytic conclusion (W01) | Only zeta; primitive/imprimitive transfer and all-target quantifiers disappear. Either eventual one-sided zeta bound suffices. | The bound itself, or the weaker cofinal-window bound. |
| Selected family and shares (W02–W03) | Selected family \(\{1\}\), order one, no designated exceptional selected character; \(A_0=A\) makes the share condition exact. | Nonempty spaces, allowed top labels, positive weights, compatible integral maps, and the same arithmetic/geometric data. |
| Main-scale auxiliary selection (W03) | Three quadratic companions instead of twists of an arbitrary target; the signed mean (3.2) is enough. | The growing pair's simultaneous estimates and congruences. Section 11 provides its stated part conditional on QRH. Larger-scale all-character estimates survive unless the new exact symmetry is proved. |
| Cyclotomic cohomology (W04) | Only the abelian 2-extension family (5.1). | The integral lengths, all coefficient primes, growing twists, and full window quantifiers in (5.2). No rank-one vanishing argument has replaced them. |
| Galois and local correspondence (W05) | No need to vary the final Dirichlet target. | Auxiliary high-rank automorphic representations still require the classical local/global and period-model theorem already adopted. Conductor one does not make those representations rank one. |
| Integral theta maps and divisibility (W06) | Fewer final character labels. | Existence, nonvanishing, integral divisibility, and normalization of the same maps. |
| Archimedean restriction and residues (W07) | Only parameters used in the RH family. | The proved local positivity/restriction results are still used at growing ranks; specialization does not erase them. |
| Global theta matching and norms (W08) | Only one target family. | Period-normalized matching, decay, fixed constants and nonzero theta realizations; local positivity is not a substitute. |
| Counting and finite types (W09) | Only the RH host and its local types. | Nonzero spaces and uniform spectral/type estimates needed by that host. |
| Geometry and covolumes (W10) | Only the RH family of section lattices. | The actual section-lattice degree, period normalization, integral projection indices, and averaged surplus or discarded-degree budget. |
| Final error budget (W11) | A single scalar zeta budget; companions may vary with scale. Under new symmetry, (4.3) uses only three weight means and logarithmic dispersion. | Prove that budget on whole windows, with its total exponent loss tending to zero. Prove symmetry before using (4.3). |

The geometric dimension does not collapse. The actual Hilbert–Samuel application explicitly extracts \(f\ge8\) and \(r\ge100\) (`HilbertSamuelLowerBoundOfComponents.lean:59–68`), and uses a positive-dimensional flag space. The source chain has \(m\ge x^{1/2-\varepsilon}\) (`SChain.lean:53–58`), while its signature is \((k+j-1,m-j)\) (`Params.lean:46`). Only its terminal stage is definite; taking the final Dirichlet character to be trivial does not turn the entire chain into Hodge lines or zero-dimensional geometry.

**Uniformity distinction.** The GRH program already permits constants depending on the fixed target character; it does not require a bound uniform over all target conductors at once. RH removes that outer all-target requirement. It does not remove uniformity over the growing auxiliary conductors, ranks, stages and points inside each accuracy's windows. Constants may depend on the accuracy, but the total exponent loss must tend to zero; a new uncontrolled constant at each scale is insufficient.

## 7. A fixed quadratic alternative and its limits

Fix a primitive quadratic character \(\chi_D\), and put
\[
G_K=G+G_{\chi_D},\quad K=\mathbf Q(\sqrt D),\quad
\gamma_K=\gamma+L'(1,\chi_D)/L(1,\chi_D).
\]
Its prime-power coefficients are \(\Lambda(n)(1+\chi_D(n))\ge0\), and
\[
G_K(x)=\sum_{n\le x}\Lambda(n)(1+\chi_D(n))(x/n-1)
       -x\log x+(1+\gamma_K)x.
\]
The elementary Euler factors identify the corresponding product with \(\zeta_K(s)=\zeta(s)L(s,\chi_D)\). Thus the positive-family window criterion applies and proves both RH for zeta and the critical-line assertion for this one quadratic \(L\)-function. No cancellation of zero poles is possible: multiplicities in a positive sum add.

For \(D=-4\) or \(-3\), the nonprincipal \(L\)-function is positive on every positive real argument: group its defining series respectively as
\(\sum_{j\ge0}((4j+1)^{-s}-(4j+3)^{-s})\), or
\(\sum_{j\ge0}((3j+1)^{-s}-(3j+2)^{-s})\).
The same elementary eventual-upper-or-lower proof as in Section 1 therefore applies to \(G_K\). This can be a useful alternative target if a new geometric construction naturally produces a fixed quadratic Dedekind-zeta function.

It is not currently a simpler completed arithmetic construction. It asks for an additional fixed quadratic conclusion, and the source's growing \(q,d\) supplier cannot be replaced by a fixed quadratic field through a change of notation. The pure-zeta target of Sections 1 and 4 has the fewest analytic requirements.

## 8. QRH and no-Siegel inputs: precise use and noncircularity

The repository records the supplied September and October QRH results at a verified `openai/math` source pin; the claimed half-planes are respectively \(\Re s>7/8\) and \(\Re s>11/12\). The conventional proof presently treats the relevant uniform statement as the explicit hypothesis of manuscript Section 11. It supplies the simultaneous moving quadratic choices and makes the required \(399/400\) zero-free boxes automatic. That selection proof does not estimate an arbitrary fixed quadratic character at every sufficiently large scale.

The supplied no-Siegel result is a lower bound of the form \((1-\beta)\log q\ge c>0\) for real zeros; it is not a statement that all real zeros are absent. A uniform QRH bound with a fixed exponent \(\theta<1\) already implies such a real-zero estimate for primitive real conductors \(q\ge3\), by taking \(c=(1-\theta)\log3\). Neither assertion by itself supplies the vanishing-loss zeta estimate needed here.

In particular, do not infer square-root cancellation by iterating a fixed-width QRH bound without a new input. The shortened mean-square bootstrap examined in manuscript Section 6 requires a smaller outer range that the existing argument does not establish. At arbitrarily small outer exponents its sum already includes the fixed term \(u=1\); the desired bound for that term is itself of square-root strength. This is a substantive missing estimate, not a formal consequence of QRH. Likewise a Dirichlet theorem does not automatically cover varying quadratic ray-class Hecke functions.

## Verification and next decisive steps

The elementary analytic criterion, exact conductor-one specialization, four-character coefficient reduction, zeta-centering lemma, and the implications (4.1) \(\Rightarrow\) (4.3) \(\Rightarrow\) RH under its stated window bound are proved. The root independently reviewed the analytic argument, the centering lemma and the signed-budget rearrangement; the three-mean/Jensen comparison was independently checked by this agent and the global-inputs agent. Source inspection and hashes certify the quoted contracts, not a new Lean build.

The next mathematical tasks are to construct the same integral theta data with the required nonzero spaces, prove their geometric/cohomological costs, and establish the single total error budget. In parallel, an equivariant construction of the actual weight measures could remove the larger character-transfer estimates. Until that symmetry and budget are proved, the existing general finite-error route and its suppliers remain available. Ordinary RH is a substantially smaller target at the analytic and finite-character ends, while the current high-rank arithmetic core remains the main unresolved work.
