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

## Appendix. Applicability to the actual RH arithmetic data

The hypotheses in Section 1 hold for the source's chosen arithmetic data,
not merely for a possible realization of its abstract group. This appendix
records the bridge, including the ramified primes and the principal
correction. All source references below are to the immutable revision
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

### The quotient and the three quadratic characters

The actual data have a surjective map
\[
 r:(\mathbb Z/N\mathbb Z)^\times\longrightarrow
 G=(\mathbb Z/2\mathbb Z)^2\times A,
 \qquad N=Q_Sqd.
\]
The source defines this as its Artin map followed by the isomorphism
which **swaps the two sign coordinates**; the remaining factor is carried
by the fixed isomorphism to \(A\). The surjectivity proof composes the
surjective Artin map with that isomorphism. The definitions `recOf` and
`recH` are the same map, as direct comparison of their displayed formulas
shows. The source's actual host carries `PsQ`, in addition to the
quadratic identity `art_ch`; its field construction supplies this condition
for every target primitive character, hence also for conductor one.
Writing \(\sigma_d,\sigma_q\) for the first and second additive sign
characters respectively gives, on every unit \(u\bmod N\),
\[
 \sigma_d(r(u))=\left(\frac{u}{d}\right),\qquad
 \sigma_q(r(u))=\left(\frac{u}{q}\right).
\]
The host assumptions give prime \(q\equiv3\pmod8\) and prime
\(d\equiv7\pmod{16}\); in particular they are distinct odd primes.
Their nontrivial Legendre characters are primitive, and their product is
primitive of conductor \(qd\), by the Chinese remainder theorem.
Consequently the three surviving nonprincipal characters in Section 2
are exactly \(\chi_d,\chi_q,\chi_d\chi_q\), with the stated signs.
The source also proves the same sign dictionary explicitly in
`cOf_chC`, `cOf_psC`, and `cOf_chpsC`.

### Primitive values at every prime, including ramification

For each \(\psi\in\widehat G\), the source first forms the Dirichlet
character on \((\mathbb Z/N\mathbb Z)^\times\) induced by \(\psi\circ r\),
then takes its canonical primitive character \(\chi_\psi\).
For a prime \(p\), its inertia subgroup is exactly the image under \(r\)
of the kernel of reduction to the prime-to-\(p\) part of \(N\).
Its chosen Frobenius unit is congruent to \(p\) on that part and to one
on the \(p\)-primary part. Here \(F_p\in G\) denotes the image of that
unit, a lift of the class used in Section 1; the average below is
independent of the lift. Thus, for every \(j\ge1\),
\[
 \operatorname{primVal}(\psi,p^j)
 =\frac1{|I_p|}\sum_{h\in I_p}\psi(jF_p+h)
 =\begin{cases}\psi(jF_p),&\psi|_{I_p}=1,\\
                 0,&\psi|_{I_p}\ne1,
   \end{cases}
 =\chi_\psi(p)^j.                                      \tag{A.1}
\]
The bounded source proof checks both branches: triviality on inertia
makes the conductor divide the prime-to-\(p\) part; nontriviality makes
\(p\) divide the conductor and the primitive value vanish. Multiplicative
factorization proves \(\operatorname{primVal}(\psi,n)=\chi_\psi(n)\)
for every \(n\ge1\). In the actual arithmetic data, `primVal_eq`,
`prim_both`, and `prim_val` identify the primitive character used elsewhere
in the construction with this canonical one. `prim_one_iff` proves that
it is principal exactly when \(\psi\) is trivial.

In fact, positivity alone needs even less arithmetic: expanding the
inertia-coset mean and applying finite character orthogonality gives
\[
 \sum_{\psi\in\widehat G}\psi(-g)
     \operatorname{primVal}(\psi,p^j)
 =\frac{|G|}{|I_p|}\mathbf1_{\{g-jF_p\in I_p\}}.
\]
This identity holds for the abstract inertia-and-Frobenius data as well.
The actual quotient and (A.1) are needed to identify the resulting
functions with the analytic Dirichlet functions; no change of modulus or
discarding of ramified terms is involved.

### The thin estimate includes the corrected principal sum

The source's `GPsi` is defined as
\[
 G_1(y)=\sum_{n\le y}\Lambda(n)(y/n-1)-y\log y+(1+\gamma)y
 \quad(\psi=1),
\]
and as the sum with coefficients \(\operatorname{primVal}(\psi,n)\)
plus \(y\ell_\psi\) otherwise. Here \(\psi=1\) means the trivial
character; the additive-character notation in the source writes it as
`0`. Its `char_at` supplies the actual logarithmic derivative
\(\ell_\psi=L'(1,\chi_\psi)/L(1,\chi_\psi)\) for each nonprincipal
character. Its `GPsi_eq` proves equality with the corrected primitive
Dirichlet sum, treating the principal and nonprincipal branches separately.
In particular the subtraction \(-y\log y+(1+\gamma)y\) is present.

The source predicate `ThinScales` quantifies over **every** group
character and every \(y\ge X'/3\):
\[
                    |G_{\chi_\psi}(y)|\le\theta y.       \tag{A.2}
\]
The proof of `char_at` transports the host's all-character estimate to
precisely this predicate using `GPsi_eq`. Independently, `ThinChoice`
checks equality of the analytic functions in both branches before
applying the large-scale theorem `QH.thin`; that theorem includes the
principal character. The exceptional-zero hypothesis in it is imposed
only on nonprincipal real characters. The selected-character predicate
`ReadsKept` alone would not suffice for this conclusion; the all-character
identities just exhibited are the required stronger bridge. Section 3
therefore uses exactly the source's thin estimate, including its principal
pole correction. Supplying that analytic estimate remains the stated
analytic input; this appendix does not reprove its deep dependencies.

### Immutable source record and scope

Paths below are relative to `lean/src/`. The hashes are Git blob SHA-1
identities verified against the pinned source atlas; the certificate also
records SHA-256 hashes of source bytes and bounded excerpts. Abbreviations
in the path column are expanded here: `AA` is
`Development/AutomorphicArithmetic/`, `SR` is
`Formalism/SharpRestriction/`, and `SW` is
`Formalism/SizeWindowBrackets/`.

| Source path | Lines inspected for this bridge | Git blob SHA-1 |
|---|---|---|
| `Formalism/StatementOC.lean` | 9–13 | `12ab19c0176bd4135c2b23a7ee3ac22888df0122` |
| `Formalism/FrobeniusOrbits/Statement.lean` | 11–18 | `45d3b672d4649dd27309c092b3f9a24d279dd399` |
| `SW/FirstPrimeNeSecondPrime.lean` | 38–70 | `18deb7cb85d6f650a69f01fda6e0c789b9f04d89` |
| `SW/GaloisToProductIsIso.lean` | 12–32 | `4f314d4aed9d7969e3f275c9dd03aca3d015ee43` |
| `SW/ChainSlopeWindows/GaloisMapComplexConjugation.lean` | 164–245 | `b08d98f83d661d021b20ccff6c405af78e9afb59` |
| `SR/RamificationFrobenius/TotientGaloisClasses/ConjEMemHostFIff.lean` | 12–32, 54–55, 82–99 | `0ab34ba6d386bb84908efe66de6ce50108eacddc` |
| `Formalism/LocalRingCardinality/DataHost.lean` | 39–44 | `7e9af8ab364965c62be250ae93974098141598c0` |
| `AA/PrimitiveCosets/RecH.lean` | 10–23 | `b2712cc402765cea3fd406285e05e32a7ce64ec7` |
| `AA/PrimitiveCosets/ToEBij.lean` | 37–66 | `95598a5b86a7dc37af41dfdfd526e775a7a7e254` |
| `AA/ConductorsKronecker/RecSurj.lean` | 6–17 | `8a2ce64499b8d0f330b3a950fced60aa2e06d0b3` |
| `AA/CharacterBoxes/FieldChi.lean` | 20–26, 53–58 | `f3e2032b133ff64406a87e27438cdf467aa05a1f` |
| `SR/GlobalSchurBounds/TieGlobal.lean` | 24–34 | `00acf811793877fe42d18c0d69f2d5833f75bf94` |
| `SR/GlobalSchurBounds/TopDensityNGeSixteen.lean` | 295–391, 396–428, 476–495 | `cbccb968fd96afe14797b8890f4e5dc63bd11d26` |
| `SW/GrowthBoundGivesRiemannHypothesis.lean` | 55–56 | `a3ece4b4aea97a95ba2977fa9e8d437e72677774` |
| `AA/CharacterBoxes/ThinChoice.lean` | 15–35, 49–82 | `00b6f5fe9348e1d26ef97b7cdcc16ada3a38b489` |
| `AA/MeanSquareBounds/Thin.lean` | 10–15 | `d322f531dc42b40bee2cddc76f83f53a2f592ba6` |

This audit checks the displayed definitions, hypotheses, and intervening
proof passages. The elementary quotient, orthogonality, and sign arguments
are also given above in ordinary mathematics. It does not assert a fresh
Lean build, replay the full source construction, or certify all upstream
analytic and geometric theorems. An independent reviewer recomputed all
16 source identities and 22 excerpt hashes, read the critical bridge
passages, and checked the ordinary mathematical arguments; that review
passed. No additional primitive-character,
ramification, or principal-correction compatibility condition is needed
for the direct transfer once the actual source data and their stated
thin estimate are supplied.
