# The CM determinant value from one elliptic curve

## Status

This supplies the CM-point, product-frame and period-calculation
subrequirements in the determinant comparison by ordinary classical
mathematics. It proves a locally integral pure decomposition, descent
and good reduction of the elliptic-product-isogenous abelian variety
with its **specified symmetric rigidified line**, an exact product
tangent basis, and the actual and corrected determinant degrees.
No higher dimensional CM height formula is used.

The construction of the arithmetic moduli space and the algebraic flat
determinant family, and identification of that family's finite norms
with the same integral eigenlattices, remain separate hypotheses.
Precisely, at each place the prescribed flat norm at the point under
comparison must equal its value at every allowed CM point, with the
same integral and metric normalizations. This is an equality
independent of the CM point chosen at that place; complex flatness
alone does not supply its finite-place part.
The note does not complete an existing RH or GRH node.
The checker authenticates sources and checks finite exact algebra;
it does not replay Lean or prove the geometric or analytic theorems.

## 1. Exact setting and conventions

Let \(F=\mathbf Q(\sqrt{-d})\subset E\), with the prescribed odd
fundamental discriminant \(-d\); the application has \(d\ge7\) prime.
The CM extension \(E/E^+\) is unramified at finite places.
Put \(\omega=(1+\sqrt{-d})/2\), \(m=[E:F]\), and let
\(\Psi\) be the embeddings of \(E\) extending the fixed embedding
of \(F\) in which \(\sqrt{-d}=i\sqrt d\).

Let \(L\) be a projective \(\mathcal O_E\)-lattice of rank \(p+q\).
The skew-Hermitian form \(h\) is **linear in the first argument**
and conjugate-linear in the second, takes values in
\(\mathfrak D_{E/\mathbf Q}^{-1}\), and its trace
\(B=\operatorname{Tr}_{E/\mathbf Q}h\) is a perfect alternating
form on \(L\). For every \(\tau\in\Psi\), \(i\tau h\) has signature
\((p,q)\). This convention is the pinned source's \(C G C^H\)
convention; it is distinct from the conjugate-linear-first
Poincaré convention used in other fragments.

The prescribed tangent metric is \(\pi H\), for the
Appell--Humbert form of the original principal line. Finite norms use
the actual smooth integral model. Normalize
\(|\ell|_\ell=\ell^{-1}\), count all complex embeddings separately,
and divide global sums by the field degree. Empty Gram blocks have
determinant one.

## 2. A pure basis integral at all places above a chosen prime

For every rational prime \(\ell\), there are orthogonal \(E\)-spaces
\(W_+,W_-\), positive and negative at every \(\tau\in\Psi\),
and \(x_1,\ldots,x_p\in L\cap W_+\),
\(x_{p+1},\ldots,x_{p+q}\in L\cap W_-\), forming a basis
of \(L_A\), where \(A=\mathcal O_E\otimes\mathbf Z_{(\ell)}\).

Here is a complete construction. The absolute different has a real
generator \(\delta_0\) over this semilocal ring because \(E/E^+\)
is unramified. Trace duality makes \(\delta_0h\) unimodular.
Choose \(a\) by the Chinese remainder theorem and put \(u=a-\bar a\).
At an inert odd place choose a nonzero residue difference. At an inert
dyadic place choose \(a\) with unit trace, so
\(u=2a-\operatorname{Tr}(a)\) is a unit. At a split pair choose
residues \(1,0\), giving \(u\) residues \(1,-1\).
Thus \(u\delta_0h\) is a unimodular Hermitian form over \(A\).

A nondegenerate Hermitian form over a quadratic finite field
extension has a vector of nonzero norm even in characteristic two:
otherwise the norms of \(v+aw\) would make the nondegenerate field
trace pairing vanish. At a split factor choose mutually dual vectors.
Lift these choices simultaneously, split off the unit norm line,
and induct. This gives an orthogonal semilocal basis \(e_i\);
clear denominators by integers prime to \(\ell\) to put it in \(L\).

Choose a positive \(p\)-frame at each embedding. Each coset
\(e_i+\ell L\) has bounded covering radius in the Minkowski space.
Approximate a large positive multiple of the prescribed frames in
these cosets. The bounded error is negligible after scaling, so the
resulting \(x_1,\ldots,x_p\) are simultaneously positive.
Their Hermitian Gram determinant remains a unit at every place above
\(\ell\), because of the fixed congruences.
Its inverse gives an integral orthogonal projector on \(L_A\).
Take \(W_+=E\{x_i\}_{i\le p}\), \(W_-=W_+^\perp\).
Choose a semilocal basis of the complement and clear denominators
prime to \(\ell\) to obtain the remaining \(x_i\).
Signature gives negativity on the complement.

This uses scaling in an open cone, **not** density of an integral
lattice. The global lattices \(L_\pm=L\cap W_\pm\) are saturated
and projective; they need not be globally free, and the splitting
is asserted only after localization. Their two Gram blocks satisfy
\[
 \log|j\det G_+|=-pD_\ell(j),\qquad
 \log|j\det G_-|=-qD_\ell(j),\qquad
 D_\ell(j)=\log|j\mathfrak D_{E/\mathbf Q}|.                 \tag{2.1}
\]
Indeed the corresponding blocks of \(u\delta_0h\) are unimodular.
This includes \(\ell=2\) and empty blocks.

## 3. The actual CM object, line and tangent lattice

Use the fixed complex structure on \(W_+\) and its conjugate on
\(W_-\). Then \(B\) is a principal Riemann form on the resulting
complex torus. Retain its specified symmetric principal line,
rigidified at zero. Choose one elliptic curve \(C\) with period lattice
homothetic to \(\mathcal O_F\), using its two conjugate
\(\mathcal O_F\)-actions for the two signs.

The pure vectors give homomorphisms from these elliptic types.
Choose \(b_1,\ldots,b_m\in\mathcal O_E\) forming a relative basis
over \(\mathcal O_F\) after localization at \(\ell\). The vectors
\(b_i x_a\) span a lattice of finite index prime to \(\ell\).
Hence their product map \(\psi:C^{mp}\times C^{mq}\to A\)
is an isogeny with kernel killed by some \(N\) prime to \(\ell\).

### 3.1 The original line descends, without a tensor power

Polarized complex tori and their homomorphisms are algebraic
(Milne AV, Theorems 2.8--2.9). The kernel of \(\psi\) lies in
the elliptic product's algebraic \(N\)-torsion; its quotient exists
over \(\overline{\mathbf Q}\) (Remark 8.12). Homomorphism rigidity
(Corollary 16.4) descends the coefficient action and polarization.
For \(\overline{\mathbf Q}\subset\mathbf C\), first spread the
homomorphism to a finitely generated regular subextension.

Choose an algebraic line \(L_0\) inducing the descended polarization
using Milne AV, Proposition 13.6 in characteristic zero. Its Tate
pairing is alternating since it becomes the specified polarization
after complex base change; an auxiliary prime different from \(2\)
may be used. Put \(M=[-1]^*L_0\otimes L_0^{-1}\in\operatorname{Pic}^0\),
and choose \(Q\in\operatorname{Pic}^0\) with \(Q^{\otimes2}=M\).
Then \(L_0\otimes Q\) is symmetric. Its difference from the specified
symmetric complex line lies in \(\operatorname{Pic}^0[2]\), hence is
algebraic. Normalize the comparison at zero. The normalized symmetry
and cubical structure are unique. Thus the **same** rigidified line
descends, together with the action and any finite level structure,
to one number field.

### 3.2 Good models preserve the product basis

The CM elliptic curve acquires good reduction everywhere after finite
extension (Milne MF, Theorem 12.14). Good reduction is invariant under
isogeny (Serre--Tate, Theorem 1 and Corollary 2, p.493), so \(A\)
does too. The local abelian models glue by Néron uniqueness.
The already audited Moret--Bailly theorem extends the specified
symmetric rigidified line after a further extension.
Its identity component is this same abelian scheme.
The vertical divisor and zero-rigidification argument from
[the theta supplier](moret-bailly-theta-supplier.md) preserves the
line and canonical metric. On products of the good model it also
preserves the cubical adjunction identifications.

Since \(N\) kills the homology cokernel, \(\chi=N\psi^{-1}\)
sends period lattices into period lattices and is algebraic.
The Néron mapping property extends both maps and both identities
\[
                    \chi\psi=[N],\qquad \psi\chi=[N].
\]
At every place above \(\ell\), \((d\psi)^{-1}=N^{-1}d\chi\)
is integral. Thus the elliptic tangent basis is an **exact**
basis of the actual tangent lattice of \(A\).
All coefficient actions and polarization adjunction identities
extend by the same uniqueness.

The condition \(\ell\nmid N\) is essential: multiplication by
\(\ell\) on a good elliptic curve multiplies its tangent lattice
by \(\ell\). If the fine moduli problem and its uniformization
are supplied, the descended object with this same line, action,
level and period gives the required CM point in that moduli space.
This is an application of that interface, not its construction.

## 4. The exact elliptic period

After finite extension principalize the integral differential line:
if \(I^a=(b)\), adjoining an \(a\)th root of \(b\) makes the
extended ideal principal, since the fractional-ideal group is
torsion free. Let \(v\) be the dual integral tangent basis and
\(\omega(v)=1\). At \(\sigma:M\hookrightarrow\mathbf C\), write
its periods as \(\omega_1(\mathbf Z+\tau\mathbf Z)\), \(y=\Im\tau>0\).
Then the original metric and the discriminant product give
\[
 n_\sigma=\|v\|_\sigma^2=\frac{\pi}{|\omega_1|^2y},\qquad
 \Delta_\omega(\sigma)=(2\pi)^{12}\omega_1^{-12}\eta(\tau)^{24}.
                                                               \tag{4.1}
\]
Good reduction and the integral differential make \(\Delta_\omega\)
a unit at all finite primes, including \(2,3\). Hence
\[
 \log n_\sigma=-\log(4\pi y|\eta(\tau)|^4)
                          +\tfrac16\log|\sigma\Delta_\omega|.   \tag{4.2}
\]
The last term has mean zero by the product formula.

The elliptic CM class theorem makes every ideal class occur with
equal multiplicity among the embeddings (Milne MF, Theorem 12.18).
The conjugate quadratic embedding permutes these classes and preserves
the real modular expression in (4.2). For
\(Z_\tau(s)=\sum' y^s/|u+v\tau|^{2s}\), the Kronecker limit formula is
\[
 Z_\tau(s)=\frac{\pi}{s-1}
 +2\pi\{\gamma-\log2-\log(\sqrt y|\eta(\tau)|^2)\}+O(s-1). \tag{4.3}
\]
Zagier's primary statement uses \(Q=|u+v\tau|^2/(2y)\), whose
zeta function is \(2^sZ_\tau\); dividing by \(2^s\) changes
the constant term as well as the residue.
An ideal has covolume \(\sqrt d\,N\mathfrak a/2\), so
\[
 \zeta_F(s)=\frac1{w_F}(2/\sqrt d)^s
                      \sum_{[\mathfrak a]}Z_{\tau_{\mathfrak a}}(s).
\]
Compare the constant term divided by the residue with
\(\zeta_F(s)=\zeta(s)L(s,\chi_{-d})\). It follows that
\[
 \boxed{-\overline{\log n}
 =x_d:=\gamma+\log(2\pi/\sqrt d)
                      -L'(1,\chi_{-d})/L(1,\chi_{-d}).}     \tag{4.4}
\]
Both quadratic actions may be put on the same curve and tangent
vector. Then \(n_{+,\sigma}=n_{-,\sigma}\) pointwise.

## 5. Gram matrices and the fixed algebraic scalar

With the stated linear-first convention, the elliptic pairing is
\[
 h_F^\epsilon(x,y)
 =\epsilon\sqrt{-d}\operatorname{Tr}_{E/F}h(x,y)
 =\epsilon\{B(\omega x,y)-B(x,y)+\omega B(x,y)\}.            \tag{5.1}
\]
To verify this, put \(\operatorname{Tr}_{E/F}h(x,y)=a+b\omega\)
and use \(\omega^2=\omega-(d+1)/4\).
Polarization adjunction of the actual maps gives
\(\langle d\psi_xv,d\psi_yv\rangle
 =n_\sigma\,\sigma(h_F^\epsilon(x,y))\).
Both metrics contain the same factor \(\pi\).

For an absolute integral basis \(b_i\) and trace-dual \(b_i^*\),
\(P_\tau=\sum_i\tau(b_i^*)\rho(b_i)\) is the character projector.
The identities
\(\sum_i\tau(b_i^*)\upsilon(b_i)=\mathbf1_{\tau=\upsilon}\)
collapse the two Gram sums. The surviving coefficient is
\(2\tau(\omega)-1=\tau(\sqrt{-d})\). Thus
\[
 \Gamma_+=n_+\epsilon_+\tau(\sqrt{-d}\,G_+),\qquad
 \Gamma_-=n_-\epsilon_-\bar\tau(\sqrt{-d}\,G_-).             \tag{5.2}
\]
There is no extra factor \(2\), \([E:F]\), or \(\pi\).

Fix a homology \(E\)-basis \(e\), write \(x=Te\), \(t=\det T\).
Then \(\det G_+\det G_-=t\bar t\det G_e\).
For the algebraic, base-change-natural frame scalar \(\varphi(v,w)\),
the source's period trivialization has blocks
\(z_+I_p\) and \(z_-^{-1}G_-^{-1}\).
The second block is dualized by the same \(h\). If its flat
constant is \(\rho\), then
\[
 \varphi(v,w)\tau(t)z_+^p=\rho z_-^q\tau(\det G_-),\qquad
 r=\frac{\varphi(v,w)\tau(t)}{\tau(\det G_-)}
                     \in\overline{\mathbf Q}^{\,\times}.  \tag{5.3}
\]
The relation \(rz_+^p=\rho z_-^q\) fixes the same \(r\) at
every chosen CM point. With one curve one can also take \(z_+=z_-\).

## 6. Finite norms and cancellation

The actual complex logarithmic norm is
\[
 a_\sigma=\log|\sigma r|
 +\frac p2(\log n_{+,\sigma}+\tfrac12\log d)
 -\frac q2(\log n_{-,\sigma}+\tfrac12\log d)
 +\tfrac12\log|\sigma\tau(\det G_e)|.                       \tag{6.1}
\]
At \(\ell\), the exact integral product basis from Section 3 and
[the relative-different calculation](cm-integral-eigenframes.md)
give integral eigenframes \(\delta v,\bar\delta w\), with
\[
 \log|j\delta|=\log|j\bar\delta|
                  =D_\ell(j)-\log|j\sqrt{-d}|.
\]
Using (2.1) and frame covariance yields
\[
 a_{\ell,j}=\log|jr|-\log|jt_\ell|-qD_\ell(j)
                  +(q-p)\{D_\ell(j)-\log|j\sqrt{-d}|\},    \tag{6.2}
\]
\[
 \log|jt_\ell|+\log|j\bar t_\ell|
             +\log|j\det G_e|=-(p+q)D_\ell(j).             \tag{6.3}
\]
The transition has norm one whenever \(e\) is already a local
integral basis, which holds for all but finitely many \(\ell\).

Fix one number field containing the coefficient field (in particular
\(\tau(E)\)), the elliptic data and \(r\).
Each \(\ell\) may use its own finite extension for its CM
point; embedding multiplicities descend the normalized identities.
One does not need one field containing infinitely many chosen points.
Conjugation permutes all \(\ell\)-adic embeddings, so the two
transition terms in (6.3) have equal means. The product formula
cancels \(r\) and \(\det G_e\); the remaining means are
\[
 \overline{\log n_\pm}=-x_d,\quad
 \sum_\ell\overline{D_\ell}=-\log\operatorname{rd}(E),\quad
 \sum_\ell\overline{\log|\sqrt{-d}|_\ell}=-\tfrac12\log d.
\]
Degree is the negative sum of logarithmic norms. Therefore
\[
 \boxed{\widehat{\deg}_{\rm actual}=\frac{p-q}{2}P_E,\qquad
 P_E=\gamma+\log(2\pi)-\log\operatorname{rd}(E)
                 -\frac{L'(1,\chi_{-d})}{L(1,\chi_{-d})}.}  \tag{6.4}
\]
Subtracting \(q(D_\ell-\log|d|_\ell)\) from the finite norms
changes the degree to
\[
 \widehat{\deg}_{\rm corrected}
       =\frac{p-q}{2}P_E+q(\log d-\log\operatorname{rd}(E)). \tag{6.5}
\]
This is the exact correction removed by the determinant bridge.

## 7. Verification evidence and exact remaining obligation

Every formal source below is pinned to jsmorph/rh revision
**ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de**.
The checker records source blob identities, SHA-256 values and hashes
of bounded inspected ranges. It never prints complete large sources.
Important source contracts, all under Development, are:

| Source suffix | Inspected lines | Use |
|---|---:|---|
| AutomorphicSpectrum/Proofs/AlgebraProofs/PurePeriodLocalBasisExists | 151–193, 202–237 | Congruence approximation and exact pure local basis |
| AutomorphicSpectrum/Proofs/AlgebraProofs/LocalBasisGramDeterminantBound | 146–162, 336–378, 465–505 | Anti-unit, different, exact Gram determinants |
| AutomorphicSpectrum/Definitions/GlobalGeometry/IsCMFrame | 15–30, 36–64, 75–88 | Original CM objects, integral model bridges, projections |
| AutomorphicSpectrum/Proofs/GeometryProofs/CmPeriodAlgebraic | 19–45, 71–110, 114–164 | Descended CM homomorphisms and original integral model |
| GeometryProofs/CmPackProductFrame and IsogenyDecompositionProduct | 27–64; 12–56 | Same integral product tangent basis |
| GeometryProofs/CmPackPureNorm | 129–158, 234–291 | Relative-different eigenframes on the same model |
| GeometryProofs/DualBasisHermitianSum | 20–34, 45–102 | Linear-first convention and trace-dual collapse |
| WeilBound/CoreStatements/SesquilinearFractions/LieNormSquareOfFamily | 11–45, 73–119 | Exact polarization/metric adjunction |
| GeometryProofs/CmPackPeriodProduct | 206–229, 262–331 | Formula (5.2) |
| GeometryProofs/CmPackPureFrameOpen | 19–24, 125–184 | Actual period blocks in (5.3) |
| GeometryProofs/FrameFunctionCmValue | 20–28, 43–53 | Fixed algebraic scalar \(r\) |
| GeometryProofs/FrameFunctionCmNumberField | 23–59, 65–88 | Formula (6.1) |
| GeometryProofs/FrameFunctionCmHeight | 22–49, 50–114 | Formula (6.2), transition identity, finite support |
| GeometryProofs/FlatDegreeHolds | 60–118 | Fixed-field means and degree assembly |
| AutomorphicSpectrum/Definitions/GlobalGeometry/IsConstMul | 30–50, 59–82 | Algebraicity, naturality and correction convention |
| GeometryProofs/ChowlaSelbergPeriod | 18–33 | Exact period mean (4.4) |
| AbelianVarietyTheory/Statements/PrincipalLattices/LogHermFormOfUnitDiscriminant | 28–50 | Metric \(\pi H\), global elliptic data |
| AbelianVarietyTheory/Proofs/CubicalLineBundles/IsLieNormSqIffEqPiDivCovolume | 13–24 | Factor \(\pi\) in (4.1) |
| AbelianVarietyTheory/Definitions/CMLattices/ExistsIsThetaDegOfIsLocalModel | 23–46 | Mean sign and homomorphism adjunction contract |

Unprefixed GeometryProofs paths are under
AutomorphicSpectrum/Proofs. Full immutable URLs are in the certificate.
These are checked source contracts, not a Lean replay.

The independently inspected primary references are:

* J. S. Milne, *Abelian Varieties*, v2.0 (2008),
  [author PDF](https://jmilne.org/math/CourseNotes/AV.pdf):
  Theorems 2.8–2.9, pp.14–15; Remark 8.12, p.39;
  Proposition 13.6, pp.58–59; Corollary 16.4, p.68.
* J. S. Milne, *Modular Functions and Modular Forms*, v1.31 (2017),
  [author PDF](https://www.jmilne.org/math/CourseNotes/MF.pdf):
  Theorem 4.21, p.57; Theorems 12.14 and 12.18, pp.125–126.
* D. Zagier, *A Kronecker limit formula for real quadratic fields*,
  Math. Ann. **213** (1975), 153–184,
  [author PDF](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BF01343950/KroneckerLimit.pdf):
  Section 2, pp.156–159, especially (2.3)–(2.5).
* B. Conrad, *Minimal models for elliptic curves* (2015),
  [author PDF](https://math.stanford.edu/~conrad/papers/minimalmodel.pdf):
  Definition 5.1 and Example 5.3, p.13.
* J.-P. Serre and J. Tate, *Good reduction of abelian varieties*,
  Ann. Math. **88** (1968), 492–517,
  [DOI](https://doi.org/10.2307/1970722),
  [scanned primary PDF](https://wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf):
  Theorem 1 and Corollary 2, p.493, inspected directly as an image.
* The earlier audited Pazuki/Moret--Bailly model theorem, Theorem
  3.4(i), as recorded in the theta-supplier package.

The remaining task is to construct the algebraic flat determinant family
on the actual arithmetic moduli problem and identify its integral norms
on the same model. The boundary-filtration, coefficient-freeness and
vertical-rigidity packages address parts of that separate task.
The present CM calculation must not be used to infer that family, the
cusp terms or the final section-surplus statement from scalar period
information alone.
