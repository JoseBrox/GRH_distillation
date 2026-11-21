# Integral theta sections on the prescribed tangent lattice

## Status

The classical Moret–Bailly model theorem supplies the **arithmetic**
theta inputs used by the shorter jet argument, on the same integral
tangent lattice and with the same complex metric. This replaces the
primitive determinant construction and the local torsion-value
integrality construction for this particular application. It does not
assert a new formula for their separately defined local invariants.

An elementary ball estimate and Autissier's classical matrix lemma
supply the archimedean comparison as well. Together with the already
proved jet and absolute-Siegel arguments, this gives the universal
bound
\[
 \widehat\mu_{\max}(V)
 \le 12\log\bigl(2+g+\max\{-\widehat{\deg}_nV,0\}\bigr)
\]
for the exact principally polarized semistable tangent lattices below.
This closes the selected tangent-slope subrequirement. The remaining
height, intersection and section-surplus obligations of the geometric
construction node remain separate.

## 1. Exact classical statements used

Let \(A/K\) be a principally polarized abelian variety of dimension
\(g\ge1\), and let \(L\) be its **specified** symmetric ample line
bundle, with a specified rigidification at zero. A Moret–Bailly model
is a smooth separated group scheme of finite type over a ring of
integers, with semiabelian identity components, together with an
extension of this line bundle carrying its cubical structure and the
canonical metric. Its definition requires a finite flat model of
\(K(L^{\otimes2})\), and may include sections through a prescribed
finite set of algebraic points. It need not have connected special
fibres.

The primary reference is F. Pazuki, *Theta height and Faltings height*,
Bull. Soc. Math. France **140** (2012), 19–49,
[published PDF](https://www.numdam.org/item/BSMF_2012__140_1_19_0.pdf),
Definition 3.1, Theorem 3.4 and Proposition 5.1. The exact used clauses
are these:

* A model exists after a finite extension, for the given \(L\) and any
  prescribed finite set of points (Theorem 3.4\(i\)).
* The section module \(\pi_*\mathcal L\), with the \(L^2\) norm for
  **Haar probability measure**, is invariant up to canonical isometry
  under choice of model and under finite extension (3.4(iii),(iv)).
* For the principal line bundle, its rank is one and
  \[
  \widehat{\deg}_n(\pi_*\overline{\mathcal L})
       =-\frac12h_F(A)-\frac g4\log(2\pi).                 \tag{1.1}
  \]
  Here \(h_F\) uses the Deligne metric of Definition 2.1, with
  denominator \((2\pi)^g\) in the square of the norm (3.4\(v\)).
* For every **positive even** integer \(m\), after an extension
  containing \(A[m^2]\), the maps induced by \([m]^*L\simeq L^{m^2}\)
  and the good theta-group translations extend integrally and
  isometrically on a model containing those torsion sections (5.1).
  Representatives of \(A[m^2]/A[m]\) give \(m^{2g}\) maps whose generic
  direct sum is an isomorphism (2.5).

The reference's existence statement is about the given line bundle,
not only its polarization class. Choosing the generic isomorphism to
respect the supplied rigidification fixes its scalar. The cubical
metric gives the rigidification norm one. We use the stated
model-independence and base-change theorems for that fixed generic
identification.

## 2. The model comparison preserves the integral lattice and line

Suppose \(G/\mathcal O_K\) is the prescribed smooth separated group
scheme, of finite type, with geometrically connected semiabelian
fibres and abelian generic fibre \(A\). Let \(\mathcal L_0\) be the
prescribed rigidified extension of \(L\).

The semistable comparison theorem identifies

\[
             G=\mathcal N(A)^0.                            \tag{2.1}
\]

It also gives, for every finite extension \(K'/K\),

\[
 G\otimes\mathcal O_{K'}
     =\mathcal N(A_{K'})^0.                                 \tag{2.2}
\]

This is the smooth semistable case of B. Conrad, *Semistable reduction
for abelian varieties*, Theorem 4.4 and Corollary 4.5,
[author PDF](https://math.stanford.edu/~conrad/DarmonCM/2011Notes/SemistableReduction.pdf),
pages 10–11; the proof occupies pages 12–16. We include smoothness
explicitly. The argument uses the Néron mapping property; the special
kernel is finite because prime-to-residue-characteristic torsion lifts
over the strict henselization; Zariski's main theorem then makes the
generic identity morphism an open immersion. Its connected special
identity component is all of the target identity component. Applying
this statement to the base change proves (2.2). The statements are
local at the primes and glue by uniqueness of the generic identity.

Consequently the identity component of a Moret–Bailly model over
\(\mathcal O_{K'}\) is canonically \(G_{\mathcal O_{K'}}\). In
particular its tangent module at zero is **exactly**

\[
         \operatorname{Lie}(G)\otimes\mathcal O_{K'}.        \tag{2.3}
\]

There is no vertical index or change of integral lattice in (2.3).

**Rigidified restriction lemma.** On a smooth group scheme with
geometrically connected fibres over a Dedekind domain, an isomorphism
between the generic fibres of two line bundles extends uniquely if
both have rigidifications at zero and the isomorphism respects them.

For this statement the given generic isomorphism is required to be
regular and invertible everywhere on the generic group. Its divisor
as a rational section of the Hom line bundle is vertical. The total
space is regular, and each special fibre is geometrically integral:
a smooth geometrically connected algebraic group is geometrically
irreducible. Thus locally over a DVR the divisor is \(aG_k\) for an
integer \(a\). After dividing by a uniformizer to that power, the
section has no codimension-one zero or pole and is an invertible
section on the normal total space. Pulling back at zero shows that
its valuation is \(a\); the compatible rigidification has valuation
zero, hence \(a=0\). This works at every prime and proves existence.
Generic density proves uniqueness.

Apply this lemma to the restriction of the Moret–Bailly line bundle
and \(\mathcal L_0\otimes\mathcal O_{K'}\). The generic bundle is the
same specified \(L\), so the lemma gives an isomorphism on the
identity component preserving the rigidification. At an archimedean
place both canonical metrics have the same translation-invariant
curvature and give the zero rigidification norm one. The logarithm
of their ratio is harmonic on the compact complex torus and hence
constant; its value at zero is zero. The isomorphism is therefore
isometric. These arguments also show compatibility after further
finite extension. The integral comparison is not inferred merely
from the agreement of the complex polarizations.

## 3. Exact degree normalization and a small integral section

Give the tangent lattice \(V=\operatorname{Lie}(G)\) its prescribed
norm \(\|v\|^2=\pi H(v,v)\), where \(H\) is the Appell–Humbert form
of the principal polarization. Write

\[
          d=\widehat{\deg}_n V,\qquad h=\max\{-d,0\}.
\]

In symplectic complex coordinates
\(A(\mathbf C)=\mathbf C^g/(\mathbf Z^g+\tau\mathbf Z^g)\), put
\(Y=\operatorname{Im}\tau\). Then \(H\) has matrix \(Y^{-1}\).
The square of the induced dual determinant norm on
\(dz_1\wedge\cdots\wedge dz_g\) is

\[
 (\pi^g\det Y^{-1})^{-1}=\frac{\det Y}{\pi^g}
 =\frac{i^{g^2}}{(2\pi)^g}
       \int_{A(\mathbf C)}dz_1\wedge\cdots\wedge dz_g
                       \wedge d\bar z_1\wedge\cdots\wedge d\bar z_g.
                                                               \tag{3.1}
\]

At finite places the dual determinant lattice is the invariant Hodge
line of the same Néron identity component, by Section 2. Thus the
ordinary normalized degrees satisfy the exact identity

\[
                         h_F(A)=-d.                          \tag{3.2}
\]

In particular no discriminant term, extra factor two or additional
power of \(\pi\) is being hidden in the comparison.

Choose a Moret–Bailly model and principalize the rank-one projective
module \(\pi_*\mathcal L\) after a finite extension. This elementary
step is justified in [the absolute-Siegel note](absolute-siegel-supplier.md):
if an ideal \(I\) satisfies \(I^a=(b)\), adjoining a root
\(\alpha^a=b\) makes \(I\mathcal O_{K'}=(\alpha)\), because the group
of fractional ideals is torsion free. Model independence and base
change preserve its Hermitian degree. An integral generator \(\theta\)
therefore has

\[
 \operatorname{av}_{K'}\log\|\theta\|_2
       =\frac12h_F(A)+\frac g4\log(2\pi)
       \le\frac h2+\frac g4\log(2\pi).                     \tag{3.3}
\]

Restrict \(\theta\) to the identity component and apply the line
isomorphism of Section 2. This is a nonzero **integral section of the
prescribed line bundle**, with exactly the norms in (3.3). It is
primitive in the Moret–Bailly rank-one section module. We do not need,
and do not assert, that restriction is primitive in any larger module
of sections on the identity component.

## 4. Integral translates with no growth in their supremum bound

Fix the preceding section \(\theta\) and its field of definition.
For every positive even integer \(m\), pass to an extension where all
\(A[m^2]\) are rational and choose a Moret–Bailly model containing
these sections. By 3.4(iii),(iv), \(\theta\) remains integral there
under the same generic identification; its original complex norms
are unchanged.

Let \(\Gamma\subset A[m^2]\) represent \(A[m^2]/A[m]\). Use the
normalized theta-group maps of Proposition 5.1 to form

\[
 s_a=i_a\,t_a^*\bigl(j\,[m]^*\theta\bigr),\qquad a\in\Gamma,
 \quad j:[m]^*L\simeq L^{m^2}.                              \tag{4.1}
\]

They are integral sections on the whole chosen model and hence, by
Section 2, integral sections of the prescribed
\(\mathcal L_0^{\otimes m^2}\) on its identity component. There are
exactly \(m^{2g}\) of them, and Proposition 2.5 gives

\[
 \operatorname{span}_{K'}\{s_a:a\in\Gamma\}
                  =H^0(A_{K'},L^{m^2}).                     \tag{4.2}
\]

This is a generic spanning assertion, sufficient for the jet
determinant proof. It does not require an integral basis of the whole
section module. Translation by \(A[m]\) alone is not enough:
the representatives in (4.1) come from the full \(A[m^2]\) action.

The isomorphisms \(j,i_a\) are isometries for the canonical metrics.
Consequently, pointwise on every complex fibre,

\[
                  \|s_a(z)\|=\|\theta([m](z+a))\|.          \tag{4.3}
\]

Since multiplication by \(m\) and translation are surjective on the
complex torus, their supremum norms equal that of \(\theta\). Thus
every original bound \(\|\theta\|_{\infty,\sigma}\le M_\sigma\)
gives the **same** bound \(M_\sigma\) for all the sections (4.1),
pulled back along embeddings of the extension. No \(m^2\) multiplier
or extra finite-place denominator occurs in \(\log M_\sigma\).
The possible change of a good theta-group choice is a root of unity;
it changes neither integrality nor the norms.

## 5. The torsion average needed by the analytic argument

There is also a direct replacement for the arithmetic product-formula
step inside the source's supremum estimate. Given a torsion point
\(P\) with \(\theta(P)\ne0\), choose a model containing it. Theorem
3.4(ii) gives

\[
         \widehat{\deg}_n(P^*\overline{\mathcal L})
                    =\widehat h_L(P)=0.
\]

The nonzero value \(\theta(P)\) is an integral section of this
rank-one module. The degree formula therefore implies

\[
 \operatorname{av}\log\|\theta(P)\|
      =\frac{\log\#(P^*\mathcal L/\mathcal O\theta(P))}
                   {[K':\mathbf Q]}\ge0.                  \tag{5.1}
\]

For any finite set of nonzero torsion evaluations this holds after
one common finite extension, and may be summed. This supplies the
nonnegative global arithmetic average directly. It makes no claim
that a particular value expressed in an arbitrary nonintegral
trivialization is itself integral, and uses no unverified local
theta determinant identity.

## 6. The supremum bound follows from one ball and the matrix lemma

All norms in the present local calculation use the Riemann form \(H\),
not \(\pi H\). Write
\[
 \rho_\sigma=\min_{\lambda\in\Lambda_\sigma\setminus\{0\}}
                         H_\sigma(\lambda,\lambda)^{1/2},
 \qquad r_\sigma=\min\{1,\rho_\sigma/2\}.
\]
For a principal polarization the real \(H\)-covolume of the period
lattice is one. Indeed in the coordinates of Section 3 its Euclidean
covolume is \(\det Y\), and changing volume to the metric \(Y^{-1}\)
multiplies it by \(\det(Y^{-1})\). Thus the volume of an \(H\)-ball
of radius \(r\), in Haar probability units, is
\(\pi^g r^{2g}/g!\).

For any centre \(z\), choose the Gaussian holomorphic frame centered
there and let \(f(w)\) represent the theta section. Its norm is
\[
 |f(w)|e^{-\pi H(w,w)/2},\qquad |f(0)|=\|\theta(z)\|.
\]
The ball of radius \(r_\sigma\) injects into the torus. The mean-value
inequality for the squared absolute value of a holomorphic function
therefore gives
\[
 \|\theta(z)\|^2
 \le \frac{g!}{\pi^g r_\sigma^{2g}}
                 \int_{\|w\|_H<r_\sigma}|f(w)|^2\,dw_H
 \le \frac{g!\,e^{\pi r_\sigma^2}}
              {\pi^g r_\sigma^{2g}}\|\theta\|_2^2.           \tag{6.1}
\]
The first inequality also follows by expanding the power series:
the constant term contributes its squared norm and all other
diagonal terms contribute nonnegative quantities to the ball average.
The boundary at \(2r_\sigma=\rho_\sigma\) has measure zero and
does not affect either inequality.

The one arithmetic estimate used here is P. Autissier,
*Un lemme matriciel effectif*, Math. Z. **273** (2013), 355–361,
Corollary 1.4. The immutable
[arXiv version](https://arxiv.org/pdf/1104.5644v1) states this
corollary on page 2, defines \(\rho\) using \(H\) on page 4, and
defines the height \(h_{\rm Fa}\) on page 5 using the Hodge norm
\(i^{g^2}2^{-g}\int\omega\wedge\bar\omega\).
These are the exact clauses also present in the later
[author version](https://www.math.u-bordeaux.fr/~pautissi/Matrix2.pdf),
pages 2–3. Consequently
\[
       h_{\rm Fa}=h_F-\frac g2\log\pi .
\]
Taking \(\varepsilon=1/2\) in that corollary gives
\[
 \operatorname{av}\rho_\sigma^{-2}
 \le \frac{12}{\pi}
       \left(h_{\rm Fa}+\frac g2\log(4\pi^2)\right)
 =\frac{12}{\pi}h_F+\frac{6g}{\pi}\log(4\pi)
 \le 4h+6g.                                                \tag{6.2}
\]
Here \(h=\max\{h_F,0\}\); the last constants follow, for example,
from \(\pi>3\) and \(\log(4\pi)<3\).
In particular, for \(Y=2+g+h\),
\[
 \operatorname{av}r_\sigma^{-2}
 \le1+4\operatorname{av}\rho_\sigma^{-2}
 \le1+16h+24g\le24Y.                                       \tag{6.3}
\]
Taking logarithms in (6.1), averaging, and using Jensen's inequality
in (6.3) proves
\[
 \begin{split}
 \operatorname{av}\log
       \frac{\|\theta\|_{\infty,\sigma}}{\|\theta\|_{2,\sigma}}
 &\le\frac\pi2+\frac12\log(g!)
             -\frac g2\log\pi+\frac g2\log(24Y)\\
 &\le\left(2+\frac12\log24\right)g+g\log Y .
 \end{split}                                               \tag{6.4}
\]
Indeed \(g\ge1\), \(\pi/2<2\), and
\(\log(g!)\le g\log g\le g\log Y\).
Combine (6.4) with (3.3), and put
\(M_\sigma=\|\theta\|_{\infty,\sigma}>0\). We obtain the explicit
uniform supplier
\[
 \boxed{\quad
 U:=\operatorname{av}\log M_\sigma
       \le\frac h2+5g+g\log(2+g+h).
 \quad}                                                    \tag{6.5}
\]
For the displayed constant it suffices that
\(2+\frac12\log24+\frac14\log(2\pi)<5\).
The same section and bounds pull back under every finite extension:
all complex norms are repeated with the usual embedding
multiplicities, and normalized averages do not change. Section 4
therefore supplies the required integral spanning sections with the
bounds (6.5), for every positive even \(m\). No estimate for a
growing-degree extension is required.

This replaces the current source's separate complex theta-function
supremum argument; that implementation is not silently adopted as an
unproved supplier.

## 7. Even level and the resulting tangent-slope theorem

The classical translation statement was verified for even \(m\).
It is therefore not substituted into a theorem requiring all positive
\(m\). Set \(A_0=5\), \(B_0=1\), or take any nonnegative larger
constants in (6.5). In the already proved jet argument put

\[
 \begin{split}
 Y&=2+g+h,\qquad
 Z=1+g+h+2A_0g+2B_0g\log Y,\\
 a&=\lceil\sqrt Z\rceil,\qquad m=6a,\qquad
 n=m^2=36a^2=3k,\qquad k=12a^2.
 \end{split}                                                 \tag{7.1}
\]

Then \(12Z\le k\le48Z\), \(n\le144Z\), and \(m\) is both even
and divisible by three. All supplied integral and supremum estimates
remain valid at this level. The exact jet estimate, with
\(\log r=g\log n\), gives

\[
 -\operatorname{av}\log\|x\|
 \le\tfrac12\log(3ek^2)+\frac{g\log(3k)+2U}{k}
 \le\frac{13}{12}\log(48Z)+\frac7{12}\log3+\frac12.          \tag{7.2}
\]

Indeed \(g+2U_+\le Z\), \(\log(3k)>1\), and \(Z/k\le1/12\).
If \(C_0=1+2A_0+2B_0\), then \(Z\le C_0Y\log Y\), so (7.2)
is at most \(C_{\rm line}\log Y\), where one may take

\[
 C_{\rm line}=\frac{13}{6}+\frac{13}{12}\log(48C_0)
                         +\frac7{12}\log3+\frac12.          \tag{7.3}
\]

The proved bound (6.5) supplies \(A_0=5\), \(B_0=1\), and
\(C_0=13\). Thus \(Z=1+11g+h+2g\log(2+g+h)\), and the already
proved absolute-Siegel comparison gives
\[
 \widehat\mu_{\max}(V)
 \le (C_{\rm line}+1/2)\log(2+g+h)
 <12\log(2+g+h).                                           \tag{7.4}
\]
For the last elementary numerical inequality, use
\(\log624<7\) and \(\log3<2\); then
\[
 C_{\rm line}+\tfrac12
 <\tfrac{13}{6}+\tfrac{91}{12}+\tfrac{14}{12}+1
 =\tfrac{143}{12}<12.
\]
Both logarithmic inequalities follow already from \(e>8/3\).
The maximal slope is the supremum of the ordinary mean slopes of all
nonzero integral submodules with inherited metrics; the
absolute-Siegel comparison applies also to nonsaturated submodules.

For selected submodules \(V_\tau\) of total rank \(R\), (7.4) in
particular gives
\[
       \sum_\tau\widehat{\deg}_n V_\tau
          \le 12R\log(2+g+h).                              \tag{7.5}
\]
For the actual selected rank
\(R=fk_{\rm ab}=f(m_{\rm chain}-r_{\rm tor})\), the signed total-degree
identity and the two-case argument in
[the selected-sum note](selected-eigenspace-degree.md) now apply with
\(C_s=12\). No universal conjectural tangent-slope statement is
needed for this substep. The other geometric height, intersection
and section-surplus obligations are outside this result.

## Pinned source correspondence and verification scope

All source references use
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

| Module (shortened) | Inspected lines | Exact role |
|---|---:|---|
| `...ToroidalCompactification.TwoWeightEqOneAddRoot` | 72–91 | Prescribed connected semiabelian group, rigidified cubical symmetric line, Cartesian model maps |
| `...ToroidalCompactification.IsGrpPullback` | 25–29 | The model map is an actual Cartesian group pullback |
| `...AbelianSchemeQuotients.IsAbelianScheme` | 13–17, 41–48 | Smoothness, proper generic fibre, separatedness, connected semiabelian fibres |
| `...ExtensionDescent.NonzeroLocus` | 26–57 | Relative ampleness via projective charts and the trivial polarization-kernel condition |
| `...GlobalGeometry.SlopeBoundSt` | 69–76 | Principal generic line and actual tangent-metric slope interface |
| `...GlobalGeometry.IsThetaMeanSquareNorm` | 26–66, 77–118, 122–131 | Rigidification, Gaussian norm, Haar probability norm, actual degree and extension interface |
| `...GeometryProofs.LineOfKeyDegree` | 213–215, 269–299, 311–324, 348–367 | Exactly \(\pi H\), unchanged extension means, and where the separate analytic bound enters |
| `...GeometryProofs.ExistsThetaSectionsBounded` | 403–468 | The integral span and unchanged supremum contracts replaced here at even levels |
| `...MetricProofs.ExistsThetaSupBoundLogMean` | 452–485, 521–556 | Complex estimate, global torsion average, and analytic averaging remain distinct |

The dedicated checker records full pinned-file hashes, bounded excerpt
hashes, primary PDF hashes and the actually viewed primary pages. Its
exact calculations check normalization and the even-level constants;
they do not replace the ordinary model comparison proof, the cited
Moret–Bailly theorem, or a Lean kernel replay.

Independent review passed for the complete ordinary argument, including
the same-model source bridge, all three primary references at the exact
used pages, the supremum estimate, and the explicit coefficient 12.
The certificate preserves each reviewer's precise scope.
