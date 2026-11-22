# A direct bound for the average cusp correction

## Result and scope

The counting part of the cusp estimate can be shortened to one tail integral.
Under the quotient-measure and counting identities specified below, it gives

\[
 \int\log^+\frac{v_r^{-1/2}}{\lambda_1}\,d\nu
 \le\frac{23}{24}<1,
 \qquad
 \int U\,d\nu\le fj\bigl(2+\log j+3\log\operatorname{rd}(E)\bigr).
 \tag{1}
\]

Here \(E/\mathbb Q\) is abelian CM of degree \(2f\), \(j\ge1\),
\(N\ge3j+1\), \(\nu\) is the *same normalized quotient probability measure*
as in the geometric mean, and \(U\) is the original nonnegative cusp
correction. In particular, if \(B\ge4fN^2\) and
\(\Lambda_B\ge\log B+\log\operatorname{rd}(E)\), then

\[
                 \int U\,d\nu\le3fj\Lambda_B.                  \tag{2}
\]

Thus the numerical cusp allowance can be taken to be \(C_u=3\), once the
retained geometric identifications hold. The source's intermediate bound
for the logarithmic minimum is 3, and its subsequent constant term is 6;
the present proof gives less than 1 and hence the constant term 2.

The new proof supplies the short-vector packing argument, the passage from
counting to an integrable logarithmic mean, and the bounded integral
spanning set for an abelian coefficient field. Section 1a also derives
counting-mean homogeneity directly from the original Haar quotient and
one integrable counting function. It does **not** construct the arithmetic
model or identify its geometric measure with that quotient, nor identify
this mean with the signed boundary term in an arithmetic intersection
limit. Those remain explicit inputs. No new analytic hypothesis is added.

## 1. A probability lemma with its own normalization

Let \((X,\nu)\) be a probability space, \(\lambda:X\to(0,\infty)\)
measurable, and \(N_t:X\to[0,\infty)\) measurable for \(0<t\le r\), where
\(r>0\). Fix real numbers \(0<a<k\). Assume \(N_r\) is integrable and

\[
 \mathbf1_{\{\lambda<t\}}\le N_t,\qquad
 N_r\le(3r/\lambda)^a\mathbf1_{\{\lambda<r\}},\qquad
 \int N_t\,d\nu\le(t/r)^k\int N_r\,d\nu
 \quad(0<t\le r).                                             \tag{3}
\]

The last inequality also guarantees integrability of each \(N_t\).
Write \(M=\int N_r\,d\nu\). For \(0<t\le r\),

\[
       \nu\{\lambda<t\}\le\min\{1,M(t/r)^k\}.                 \tag{4}
\]

If \(M\ge1\), apply Tonelli's formula to the nonnegative function
\(Y=(r/\lambda)^a\mathbf1_{\{\lambda<r\}}\). Splitting at
\(u=M^{a/k}\) gives

\[
 \begin{aligned}
 \int Y\,d\nu
 &\le1+\int_1^\infty\min\{1,Mu^{-k/a}\}\,du\\
 &=\frac{k}{k-a}M^{a/k}.
 \end{aligned}
\]

Consequently \(M\le3^a kM^{a/k}/(k-a)\). The resulting bound also holds
when \(M<1\):

\[
 M\le M_*:=\left(\frac{3^ak}{k-a}\right)^{k/(k-a)}.             \tag{5}
\]

Use (4) at \(t=re^{-s}\). A second nonnegative tail integral proves both
integrability and the bound

\[
 \begin{aligned}
 \int\log^+(r/\lambda)\,d\nu
 &\le\int_0^\infty\min\{1,M_*e^{-ks}\}\,ds\\
 &=\frac{a\log3+\log(k/(k-a))}{k-a}+\frac1k.                 \tag{6}
 \end{aligned}
\]

There is no circular assumption that the logarithm is integrable. If
\(M=0\), (4) gives \(\lambda\ge r\) almost everywhere and the integral is
zero. If \(a\ge2\) and \(k\ge3a\), the right side of (6) is at most

\[
 \frac{\log3}{2}+\frac{\log(3/2)}4+\frac16
 \le\frac23+\frac18+\frac16=\frac{23}{24}.                    \tag{7}
\]

The rational comparison uses \(\log x\le(x-x^{-1})/2\) for \(x\ge1\)
and \(\log x\le x-1\); each follows by differentiating the difference.

**Why homogeneity must stay.** On a one-point probability space, let
\(r=1\), \(\lambda=2^{-m}\), and
\(N_t=\mathbf1_{\{\lambda<t\}}\). Both pointwise conditions in (3) hold,
but the logarithmic mean is \(m\log2\), with no uniform bound. Counting
and packing alone cannot supply the average; the scaling condition is
essential to this argument.

## 1a. Haar invariance supplies the scaling law

The separate homogeneity assumption in (3) can be removed when the
original lattice count and Haar quotient are identified. Here is the
precise replacement, including convergence requirements.

Let \(V\) be an \(N\)-dimensional Hermitian space over the CM field
\(E\) of degree \(2f\), and choose one embedding from each conjugate
pair. At embedding \(\sigma\), suppose the real quadratic form
\(q_\sigma(v)=h_\sigma(v,v)\) has complex signature
\((p_\sigma,N-p_\sigma)\) with \(1\le p_\sigma\le N-1\). Set

\[
 G=\prod_\sigma U(q_\sigma),\qquad
 C=\prod_\sigma\{v\in\mathbb C^N\setminus\{0\}:q_\sigma(v)=0\}.
 \tag{16}
\]

One may instead use the product of special unitary groups if \(N\ge3\).
Let \(\Gamma\subset G\) preserve the actual full lattice \(L\subset V\),
and assume \(\Gamma\backslash G\) has finite Haar volume. Normalize its
right-invariant Haar measure to a probability measure \(\nu\). Fix a
positive definite Euclidean norm on \(V\otimes_\mathbb Q\mathbb R\),
and put

\[
 N_t(g)=\sum_{\substack{v\in L\setminus\{0\}\\h(v,v)=0}}
               \mathbf1_{\{\|g^{-1}v\|<t\}}.
 \tag{17}
\]

**Proposition.** If \(\int N_r\,d\nu<\infty\) for one \(r>0\), then
every \(N_t\), \(t>0\), is integrable and

\[
       \int N_t\,d\nu=(t/r)^{2f(N-1)}\int N_r\,d\nu.          \tag{18}
\]

**Proof.** For a Borel subset \(A\subset C\), define the averaged
counting measure

\[
 \mu(A)=\int_{\Gamma\backslash G}
       \sum_{\substack{v\in L\setminus\{0\}\\h(v,v)=0}}
                 \mathbf1_A(g^{-1}v)\,d\nu(g).
 \tag{19}
\]

The count is well-defined on the left quotient because \(\Gamma\)
permutes the lattice vectors. Every nonzero \(E\)-vector has nonzero
image at **every** embedding; hence no partial-zero embedding stratum
occurs in (19). Nonnegative Tonelli justifies countable additivity and
changes of order before convergence is known. Right Haar invariance
gives \(\mu(hA)=\mu(A)\) for \(h\in G\), by replacing \(g\) with
\(gh\).

The action of \(G\) on \(C\) is transitive. In one factor, complete two
nonzero null vectors to hyperbolic pairs and send one pair to the
other; the nondegenerate orthogonal complements have the same signature,
so the map extends to a unitary isometry. If \(N\ge3\), the complement
contains a nonisotropic line. Multiplying that line by a scalar of
absolute value one adjusts the determinant to one while fixing the
target null vector. Thus the special unitary action is transitive too.
This determinant argument is why the special unitary version assumes
\(N\ge3\).

The set \(C\cap\{\|v\|<r\}\) is nonempty and open in \(C\), and
has \(\mu\)-measure \(\int N_r\,d\nu<\infty\). Its translates cover
\(C\); finitely many cover any compact subset. Thus \(\mu\) is locally
finite and is a Radon measure on the second-countable smooth manifold
\(C\).

On the nonzero null cone in a single factor, define the smooth positive
measure

\[
       d\omega_\sigma=\frac{dS_\sigma}{\|\nabla q_\sigma\|},
       \qquad \omega=\prod_\sigma\omega_\sigma.              \tag{20}
\]

Here surface measure and gradient use the same Euclidean coordinates;
equivalently (20) is the coarea measure on the regular level
\(q_\sigma=0\). Unitary transformations preserve both \(q_\sigma\)
and ambient real volume, so coarea gives invariance of \(\omega\).
Scalar dilation by \(s>0\) scales surface measure by
\(s^{2N-1}\) and the gradient norm by \(s\). Consequently

\[
                         \omega(sA)=s^{2f(N-1)}\omega(A).
 \tag{21}
\]

The invariant Radon measure on a transitive homogeneous manifold is
unique up to a nonnegative scalar. For completeness, average \(\mu\)
against a smooth compactly supported probability density on \(G\).
Invariance leaves \(\mu\) unchanged. The orbit maps are smooth
submersions, so this average has a smooth density with respect to
\(\omega\); local coordinates and ordinary Fubini give this assertion.
Local finiteness permits differentiation on compact sets. The density
is invariant, hence constant by transitivity. Therefore
\(\mu=c\omega\) for a finite \(c\ge0\).

The measure \(\omega\) of every ambient norm ball is finite: in one
factor, polar coordinates on a null cone have radial density a constant
times \(u^{2N-3}\,du\), integrable at zero since \(N\ge2\); the angular
factors are compact. Products and equivalence of positive norms finish
the assertion. Apply (21) to the balls in (17) to obtain (18). The case
with no rational isotropic vector has \(\mu=0\) and is included.
\(\square\)

If the geometric space is \(\Gamma\backslash G/K\) with \(K\) compact
and preserving the chosen norm, use its normalized Haar lift to
\(\Gamma\backslash G\); (17) is right \(K\)-invariant, so its mean is
unchanged. This is a quotient by a compact subgroup, not an assertion
that the geometric quotient itself is compact. For several adelic
components, keep their actual nonnegative normalized weights and apply
the proof to each corresponding \((\Gamma,L)\). Fixed finite-adelic
support is absorbed in the component lattice or in a
\(\Gamma\)-invariant nonnegative weight on rational vectors. Archimedean
right translation never alters that support. Tonelli then combines the
component identities with precisely the original weights. No volume or
stabilizer constant is set equal to one.
The optional use of weights on individual vectors concerns homogeneity
only: the pointwise lower and packing bounds in Section 2 still use the
original unweighted count, or require their own verification for a
different weighted count.

This supplies (18) from Haar invariance and one integrable count. It
does not prove finite Haar volume, integrability of that one count, or
the identification of (17) with the original geometric count and
measure. In particular an abstract probability measure satisfying only
the pointwise packing estimate still does not suffice.

## 2. Why short vectors fit in a small real space

Let \(E\) be CM of degree \(d=2f\), let \(V\) be an \(N\)-dimensional
Hermitian \(E\)-space of Witt index at most \(j\), and let
\(L\subset V\) be a full \(\mathbb Z\)-lattice stable under
\(\mathcal O_E\). Choose \(\xi\in E^\times\). Suppose the trace pairing

\[
 b(v,w)=\operatorname{Tr}_{E/\mathbb Q}(\xi h(v,w))
\]

is integral on \(L\times L\). At each parameter point use the original
positive definite Hodge norm, with the two elementary metric properties

\[
 |b(v,w)|\le\|v\|\|w\|,\qquad
 \|\alpha v\|\le\bigl(\max_\sigma|\sigma(\alpha)|\bigr)\|v\|.
 \tag{8}
\]

These are Cauchy--Schwarz and the diagonal action of \(E\) in the
archimedean decomposition. Their constants, including the factor 2 in
the source's squared Hodge norm, are verified in the pinned source
anchors below; the norm is not rescaled in this argument.

Suppose \(\alpha_1,\ldots,\alpha_m\in\mathcal O_E\) span \(E\) over
\(\mathbb Q\) and every conjugate has absolute value at most \(v_r\), with
\(v_r\ge1\). Put \(r=v_r^{-1/2}\). If \(v,w\in L\) have norm less than
\(r\), then for every \(i\)

\[
 |b(\alpha_i v,w)|\le v_r\|v\|\|w\|<1.
\]

This is the absolute value of an integer, so it is zero. The spanning
property and nondegeneracy of the trace pairing imply \(h(v,w)=0\).
For the convention that \(h\) is conjugate-linear in its first variable,
the spanning family becomes \(\overline{\alpha_i}\), which also spans.
Hence the \(E\)-span \(W\) of all vectors shorter than \(r\) is totally
isotropic, and \(\dim_E W\le j\).

Let \(\lambda\) be the shortest nonzero lattice-vector norm and count

\[
 N_t=\#\{v\in L\setminus\{0\}:h(v,v)=0,\ \|v\|<t\}.
 \tag{9}
\]

Discreteness gives \(\lambda>0\), attainment, and finite counts. For
\(0<t\le r\) and \(\lambda<t\), a shortest vector proves \(N_t\ge1\).
All counted vectors lie in the real space \(W\otimes_\mathbb Q\mathbb R\)
of dimension at most \(dj=2fj\). Their pairwise distances are at least
\(\lambda\). The disjoint open balls of radius \(\lambda/2\) around them
fit in the ball of radius \(t+\lambda/2\). Comparison of Euclidean
volumes in that real space gives

\[
 N_t\le(1+2t/\lambda)^{\dim_\mathbb R W_\mathbb R}
       \le(3t/\lambda)^{2fj}.                                \tag{10}
\]

If \(t\le\lambda\), the count is zero. The zero-dimensional case has
no nonzero short vectors and satisfies the same assertion. Thus (3)'s
pointwise conditions hold with \(a=2fj\). The source mean homogeneity
has exponent \(k=2f(N-1)\), and \(N\ge3j+1\) gives \(k\ge3a\).

This proof needs an integral *spanning family*, not an integral basis.
One may select a \(\mathbb Q\)-basis from it without increasing \(v_r\).
The resulting \(\mathbb Z\)-span may have nontrivial finite index in
\(\mathcal O_E\); no such index is discarded or claimed to be one.

## 3. An abelian field supplies the spanning family

Let \(E/\mathbb Q\) be finite abelian, of degree \(d\), and let \(c\) be
its conductor. Kronecker--Weber gives \(E\subset K=\mathbb Q(\zeta_c)\).
For the \(d\) characters \(\chi\) of \(\operatorname{Gal}(E/\mathbb Q)\),
the conductor--discriminant formula says

\[
 |\operatorname{Disc}(E)|=\prod_\chi\operatorname{cond}(\chi),
 \qquad c=\operatorname{lcm}_\chi\operatorname{cond}(\chi).
 \tag{11}
\]

Fix a prime \(p\mid c\) and let \(b=v_p(c)>0\). The characters with
\(p\)-conductor exponent at most \(b-1\) form a proper subgroup: they
are exactly those trivial on the last required local congruence
subgroup. There are at most \(d/2\) of them. At least \(d/2\) characters
therefore have exponent \(b\), so

\[
 v_p|\operatorname{Disc}(E)|\ge db/2,
 \qquad c\le\operatorname{rd}(E)^2.                          \tag{12}
\]

Take the integral elements

\[
 \alpha_i=\operatorname{Tr}_{K/E}(\zeta_c^i),
 \qquad 0\le i<\varphi(c).
\]

They span \(E\) over \(\mathbb Q\): the powers span \(K\) and the trace
map is surjective in characteristic zero. Every conjugate of every
\(\alpha_i\) is a sum of \([K:E]\) roots of unity. Consequently

\[
      v_r=[K:E]=\frac{\varphi(c)}d\ge1                       \tag{13}
\]

is a valid spanning bound. Again this says that *integral elements span
the field over \(\mathbb Q\)*; it neither produces a
\(\mathbb Z\)-basis of \(\mathcal O_E\) nor determines the index of
their integral span.

The external ingredients (11) and Kronecker--Weber are cited classical
theorems, not newly verified upstream proofs. Primary reference:
J. S. Milne, *Class Field Theory*, version 4.03 (6 August 2020),
[Theorem I.4.16, pp. 49--50; Example V.3.10, p. 159; Theorem V.3.27,
p. 165](https://www.jmilne.org/math/CourseNotes/CFT.pdf).
The conductor identities and cyclotomic inclusion were checked directly
in those passages. The subgroup estimate and trace construction above
are proved here.

## 4. The original cusp correction and the retained geometric inputs

Assume the following are identified for the *actual component*:

1. The original quotient carries a probability measure \(\nu\), and
   for the invariant functions under discussion, their integrals equal
   the original geometric integral divided by its degree, with all
   component weights and stabilizer normalizations retained.
2. The functions \(\lambda\) and \(N_t\) in (9) are measurable and
   \(N_r\) is integrable. Either identify the actual Haar quotient and
   lattice count of Section 1a, which proves the mean homogeneity, or
   retain directly the source identity
   \(\int N_t\,d\nu=(t/r)^{2f(N-1)}\int N_r\,d\nu\).
3. The same \(U\) occurring in the metric and boundary comparison is
   measurable, nonnegative, and has the source pointwise estimate

   \[
    U\le fj\bigl(2\log^+(1/\lambda)
                     +\log(2fj\operatorname{rd}(E))\bigr).    \tag{14}
   \]

The source obtains (14) by applying Minkowski to the original isotropic
lattice with its specified covolume. Neither that arithmetic lattice
identification nor the arithmetic intersection limit is replaced by a
generic-fibre statement here.

Since \(r=v_r^{-1/2}\) and \(v_r\ge1\),
\(\log^+(1/\lambda)\le\log^+(r/\lambda)+\tfrac12\log v_r\).
The probability lemma therefore proves \(U\) integrable and gives

\[
 \int U\,d\nu\le fj\bigl(2+\log v_r
                               +\log(2fj\operatorname{rd}(E))\bigr).
 \tag{15}
\]

Use \(d=2f\), (12), and (13):

\[
 \log v_r+\log(2fj\operatorname{rd}(E))
 =\log(\varphi(c)j\operatorname{rd}(E))
 \le\log j+3\log\operatorname{rd}(E).
\]

This proves (1). Finally \(B\ge4fN^2\ge4(3j+1)^2\ge64j\) for
\(j\ge1\). Since \(\log64\ge3>2\),
\(2+\log j\le\log B\), proving (2). A scale such as
\(\Lambda_B=\log B+\log\operatorname{rd}(E)+|\lambda_E|\) is therefore
admissible, without using an estimate for \(\lambda_E\) in this step.

The sign in the subsequent intersection inequality is unchanged: an
upper bound on the same nonnegative \(U\) controls a term such as
\(-\tfrac12\int U\). A different signed function requires its actual
integrability and equality to the geometric term; an upper bound alone
would not establish integrability of its negative part. In particular,
the one-sided signed cusp *limit* remains part of the frontier in
`paper/shared/base-test-height.tex`.

## 5. Source alignment and verification

All Lean anchors below are from
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, read with
`scripts/source_excerpt.py --atlas`. The certificate records the full
file hashes, atlas Git object hashes, and bounded excerpt hashes.

| Module suffix | Lines | What was inspected |
|---|---:|---|
| `StabilizerCovolume.StatementsMeanLogPlus` | 14--66 | Rational spanning bound; actual count; normalized geometric mean; retained probability measure and homogeneity contracts |
| `StabilizerCovolume.ShortIsotropic` | 147--217, 219--281 | Exact norm constants; integral traces force Hermitian orthogonality; isotropic short span |
| `CountingLowerBound.Statements` | 141--189 | Existing probability assumptions and constants 3 and 6 |
| `CountingLowerBound.PMeanCountBound` | 13--100 | Source comparison replaced by the direct tail integral |
| `CountingLowerBound.PCuspWeightBound` | 19--53 | Pointwise cusp inequality and original covolume input |
| `HodgeLowerBound.FlagIndices` | 78--80 | Exact numerical cusp-mean obligation |
| `ParallelGeometry.CuspMeanBound` | 21--24, 42--44, 58--84 | Geometric mean and metric correction have the same normalization |

The first six suffixes begin
`GroundTheory.HeightsAndTheta.Heights.`; the last begins
`Development.AutomorphicSpectrum.ParallelStatements.`.

Run `python scripts/check_cusp_counting_mean.py`. It reauthenticates
these bounded source anchors, checks the exact rational constant
comparisons and finite character-filtration models, the coarea scaling
exponents, and the counterexample without scaling. These computations
supplement the proof; they do not construct the quotient or replay the
Lean project.
No existing RH or GRH node is marked complete by this package.
