# Ordinary RH without a weight-symmetry hypothesis

## Status and purpose

This note proves a source-compatible replacement for the proposed symmetric
weight construction. It uses the actual thick/thin partition and the same
arithmetic discrepancy. It does not construct the integral theta maps or
prove their geometric estimate. The source's exact pooled symmetry is in
fact obstructed by its sparse fixed top set; see
[the source comparison](rh-weight-symmetry.md).

The new simplification is to use positivity of the complete finite Fourier
kernel **before** estimating the thick-weight perturbation. After averaging
translations, this perturbation has no field-degree or inverse-density
factor. The already available large-scale QRH estimate controls the thin
samples. No transport or equality of weight distributions is required.

## 1. The full prime kernel is nonnegative, including ramification

Let a finite abelian group \(G\) be a quotient of
\((\mathbb Z/N\mathbb Z)^\times\). For each character \(\psi\) of \(G\),
let \(\chi_\psi\) be the primitive Dirichlet character inducing its pullback.
The quotient map is surjective, so only the trivial \(\psi\) induces the
principal primitive character. For \(g\in G\), define
\[
 \kappa_g(p^j)=\sum_{\psi\in\widehat G}
                  \psi(-g)\chi_\psi(p^j),\qquad j\ge1.
\]
Write the group additively. For a prime \(p\), let \(I_p\) be the image of
the local unit factor at \(p\) in the Chinese remainder decomposition of
\((\mathbb Z/N\mathbb Z)^\times\); set \(I_p=\{0\}\) if \(p\nmid N\).
Let \(F_p\in G/I_p\) be the image of a unit congruent to \(p\) modulo
the prime-to-\(p\) part of \(N\). If \(p\nmid N\), use the ordinary
residue class of \(p\).

Then
\[
 \boxed{\quad
 \kappa_g(p^j)=|G/I_p|\,
       \mathbf1_{\{jF_p=g+I_p\}}\ge0.
 \quad}                                                     \tag{1.1}
\]

Indeed, \(\chi_\psi(p^j)=0\) precisely when \(\psi\) is nontrivial on
\(I_p\). Otherwise \(\chi_\psi(p^j)=\psi(jF_p)\). Orthogonality on
\(G/I_p\) proves (1.1). In particular
\(\sum_{g\in G}\kappa_g(p^j)=|G|\).
Only prime powers matter below because all other von Mangoldt coefficients
are zero. This proof also explains why replacing primitive characters by
characters with an arbitrarily enlarged modulus would be incorrect at
ramified primes.

Use the corrected sums \(G_\chi\) defined in the manuscript, and write
\[
 K_{g,a}(w)=\Re\sum_{\psi\in\widehat G}
           \psi(-g)\,wG_{\chi_\psi}(a/w),\qquad 0<w\le a.
\]
Expansion of the definitions gives
\[
 K_{g,a}(w)=\sum_{n\ge1}\Lambda(n)\kappa_g(n)(a/n-w)_+
                         +a\log w+a C_{g,a},                \tag{1.2}
\]
where \(C_{g,a}\) is independent of \(w\). Thus all nonprincipal
logarithmic derivatives disappear from differences in \(w\). The sum is
locally finite. In particular, if \(b\le w\le a\) and \(w-b\le r\), with \(r\ge0\),
\[
 K_{g,a}(w)\ge K_{g,a}(b)-r\Psi_g(a/b),\qquad
 \Psi_g(y)=\sum_{n\le y}\Lambda(n)\kappa_g(n).               \tag{1.3}
\]
Each hinge decreases by at most \(r\), and only terms with \(n\le a/b\)
can decrease; the remaining logarithm \(a\log(w/b)\) is nonnegative.
This is a one-sided comparison and does not require a bound on
\(L'(1,\chi)/L(1,\chi)\).

## 2. Freeze only the thick weights, then average

Take the manuscript's arithmetic balance with
\[
 G=(\mathbb Z/2\mathbb Z)^2\times A,\quad n=|A|,\quad
 B=A,\quad f=2n,\quad s=|S|>0,\quad d_0=s/n,
 \quad k=|T|mbd_0/2.
\]
Here \(m\ge1\), \(T\subset A\) is nonempty, \(a_t>0\), \(b>0\), and
the actual weight at \(\rho\in\Phi\) is \(w_{u,i}(\rho)>0\).
Assume all sampled arguments are at least one. The thick set is
\(\rho=((0,1),v)\) with \(v-u\in S\); its weights lie in \([b,b+r]\).
No invariance is assumed for these weights, their means, or their empirical
measures. The first and second sign characters induce respectively
\(\chi_d\) and \(\chi_q\), for the distinct source quadratic primes.
Put
\[
 D_+=G_1+G_{\chi_q}-G_{\chi_d}-G_{\chi_q\chi_d},\quad
 Q_4=\frac1{|T|}\sum_tD_+(a_t/b),\quad
 \overline a=\frac1{|T|}\sum_ta_t.
\]
Let \(J_{\rm actual}\) be the **signed actual thin contribution** to the
same arithmetic balance:
\[
 J_{\rm actual}=\frac1{nf}\sum_{u,t,i}
   \sum_{\rho\in\Phi\setminus\Phi_{S,u}}
       K_{\rho-c-t_0,a_t}\bigl(w_{u,i}(\rho)\bigr).
                                                               \tag{2.1}
\]
It is not the three-mean approximation \(J_{\rm thin}\).
Then
\[
 \boxed{\quad
 Q_4\le \frac{\overline E-J_{\rm actual}}k
       +\frac r b\frac1{|T|}\sum_t\Psi_+(a_t/b),
 \quad
 \Psi_+(y)=\sum_{n\le y}\Lambda(n)
                  (1+\chi_q(n))(1-\chi_d(n)).\quad}         \tag{2.2}
\]

**Proof.** On the thick set put \(\rho=((0,1),v+u)\), with \(v\in S\).
Then \(\rho-c-t_0=((1,0),v+u-t)\). Apply (1.3) and sum over \(u\) before
taking any absolute values. Character orthogonality gives
\[
 \sum_{u\in A}K_{((1,0),v+u-t),a}(b)=nbD_+(a/b),\qquad
 \sum_{u\in A}\Psi_{((1,0),v+u-t)}(y)=n\Psi_+(y).
\]
There are \(ms\) choices of \((i,v)\). Division by \(nf=2n^2\) therefore
gives
\[
 \overline E\ge kQ_4+J_{\rm actual}
                  -\frac{md_0r}{2}\sum_t\Psi_+(a_t/b).
\]
Divide by \(k>0\). This proves (2.2). All ramified coefficients are covered
by (1.1). \(\square\)

The normalized perturbation in (2.2) is at most
\[
                    4C_\Psi\frac r b\frac{\overline a}b,    \tag{2.3}
\]
where \(\Psi(y)=\sum_{n\le y}\Lambda(n)\le C_\Psi y\).
One may take the elementary absolute constant \(C_\Psi=4\log2\), as proved
in [the transport note](transport-symmetry-defect.md).
The disappearance of both \(n\) and \(d_0^{-1}\) in (2.3) is exact.

## 3. The thin contribution needs only the existing large-scale estimate

Suppose, at the actual thin samples only,
\[
 |G_{\chi_\psi}(a_t/w_{u,i}(\rho))|
             \le \vartheta\,a_t/w_{u,i}(\rho)
 \qquad(\psi\in\widehat G),\qquad\vartheta\ge0.
\]
There are \(f-s\) thin places for each translation and stage, and
\(|\widehat G|=2f\). The triangle inequality therefore gives
\[
 \boxed{\quad
 \frac{|J_{\rm actual}|}{k}
       \le\frac{2f(2-d_0)}{d_0}
                       \frac{\overline a}{b}\vartheta.
 \quad}                                                     \tag{3.1}
\]
Indeed the unnormalized bound is
\(2m(f-s)\vartheta\sum_t a_t\). This check keeps the counts for thick
and thin places separate.

For the source size conditions take \(r=\eta+1\), \(x\ge3\), and assume
\[
 |a_t/b-x|\le1,\quad
 2f(x+1)\vartheta\le1/x,\quad
 6f(x+1)r\le b/x.
\]
Combining (2.2)--(3.1) yields
\[
 \boxed{\quad
 Q_4\le\frac{\overline E}{k}
       +\frac{2-d_0}{d_0x}+\frac{2C_\Psi}{3fx}.
 \quad}                                                     \tag{3.2}
\]
The source also has \(d_0\ge x^{-\varepsilon}\), so the first error is at
most \(2x^{-1+\varepsilon}\). No equality of thick means or distributions
has entered the argument. Retaining a proved lower bound for the signed
\(J_{\rm actual}\) in (2.2) can improve (3.2).

The thin scale is justified by the same source data, not postulated anew.
If \(w\le2b'\), \(b'X'\le xb\), and \(a_t\ge(x-1)b\), then
\[
                   a_t/w\ge (x-1)X'/(2x)\ge X'/3.
\]
For \(X'\ge3\) these samples lie in the domain of the corrected sums.
The thick samples also have \(a_t/w\ge1\), because
\(r/b\le1/(6fx(x+1))\) and \(x\ge3\).
Under the uniform QRH hypothesis already explicit in the manuscript,
its larger-scale estimate proves
\(G_\chi(y)\ll y^{23/24}\log(Q+3)\), including the separate principal
case. With the source's exponentially large \(X'\) this supplies the
displayed thin bound and its cost. The QRH input remains a cited or stated
hypothesis; the present argument does not independently verify its proof.

## 4. The resulting RH target

Define the same single signed companion
\(C_{q,d}=G_{\chi_d}+G_{\chi_q\chi_d}-G_{\chi_q}\).
The identity \(G_1=D_++C_{q,d}\) and the elementary zeta centering lemma
now give
\[
 \boxed{\displaystyle
 G_1(x)\le\frac{\overline E}{k}
       +\frac1{|T|}\sum_t C_{q,d}(a_t/b)
       +\frac{2-d_0}{d_0x}+\frac{2C_\Psi}{3fx}
       +(1+\log(x+1))^2.}                                  \tag{4.1}
\]
Unlike the preceding conditional three-mean route, (4.1) imposes no weight
symmetry and uses the original lower endpoint \(b\), hence centering radius
one. Under the manuscript's simultaneous quadratic selection on an interval
containing all \(a_t/b\), its companion is at most
\(3(x+1)^{1/2+\varepsilon/2}\). Such intervals must include the endpoints
shifted by one; one may select on a slightly larger interval first.

Consequently, given these same compatible data on the required windows,
it remains to bound **the normalized averaged arithmetic discrepancy**
\(\overline E/k\) by a power with exponent tending to one half.
More economically, keep its sum with the signed companion in (4.1).
The existing vanishing-loss window theorem then yields RH. Constants and
window exponents are fixed for each accuracy before the window moves;
auxiliary primes and arithmetic objects may vary with the scale because
the analytic target remains the fixed zeta sum.

This closes the symmetry detour at the level of the analytic transfer.
It does not close the arithmetic construction: nonzero integral maps,
their normalized identities, the remaining Selmer estimates, and the
uniform geometric lower bound still have to supply \(\overline E/k\).
The [geometric combination](rh-geometric-combination.md) sharpens that
remaining budget. No new Lean compilation or kernel replay is claimed.

## Verification scope

The source size contract is
`Development/AutomorphicArithmetic/DedekindLFunctions/SplitInertia.lean:42--48`;
the two small-cost conditions are
`Formalism/SizeWindowBrackets/SChain.lean:50--51`, at the pinned mirror revision
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. The source reader verifies Git
blob hashes before returning bounded passages. The mathematical proof
above is independent of a Lean build. The exact finite tests in
`scripts/check_rh_direct_transfer.py` check primitive Fourier positivity
at ramified primes and the normalization of the thick comparison; they
supplement, rather than replace, the proof for arbitrary groups.

The independent source and transport reviewers checked the full mathematical
argument, including the primitive values at ramified primes, the one-sided
logarithmic correction, every finite normalization, the sampled domains,
and both source cost substitutions. Both reviews passed. Source hashes and
bounded excerpt hashes are recorded in
`certificates/rh-direct-transfer.json`.
