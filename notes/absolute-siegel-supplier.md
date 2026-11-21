# The absolute Siegel input is supplied classically in the same metric

## Result and scope

The explicit absolute-Siegel consequence in the theta-and-jet reduction
is a classical theorem for the actual Hermitian tangent lattice. It
needs no comparison with a Néron lattice, no change of metric, and no
bound on the degree of an auxiliary number field.

The only passage beyond the published minimum inequality is elementary:
principalize the saturated line of an algebraic vector. Its integral
generator then has finite-place norms equal to one, so its adelic
height is exactly its mean archimedean logarithmic norm.

This discharges the absolute-Siegel subrequirement of
[the theta-and-jet reduction](theta-jet-slope-reduction.md).
The integral theta construction and its uniform norm bounds remain open.
No whole construction node is closed.

## 1. The precise classical theorem and normalization

Let \(\bar F\) be a nonzero Hermitian vector bundle over
\(\operatorname{Spec}\mathcal O_K\), of rank \(r\).
At a finite place, use the gauge norm whose unit ball is \(F_v\);
at an infinite place, use the given ordinary Euclidean or Hermitian
norm. For a nonzero algebraic vector \(y\), defined over a finite
extension \(K'/K\), put
\[
 h_{\bar F}(y)=
 \sum_{w}\frac{[K'_w:\mathbf Q_w]}{[K':\mathbf Q]}
                      \log\|y\|_w.
 \tag{1.1}
\]
This is independent of \(K'\) and invariant under multiplication by
any nonzero algebraic scalar, by the product formula. At infinite
places it equals the average over all complex embeddings; a complex
place has weight two and its two conjugate norms agree.

Gaudron–Rémond, *Minima, pentes et algèbre tensorielle*,
Israel Journal of Mathematics **195** (2013), 565–591,
[author-hosted PDF](https://lmbp.uca.fr/~gaudron/art10.pdf),
Theorem 3.1 and Lemma 3.2, imply
\[
 \inf_{0\ne y\in F_K\otimes_K\overline K}h_{\bar F}(y)
 \le-\widehat\mu(\bar F)+c_r,\qquad
 c_r=\frac12\sum_{j=2}^{r}\frac1j\le\frac12\log r.
 \tag{1.2}
\]
The empty sum is zero for \(r=1\).
The last inequality follows by integrating \(1/t\) over
\([j-1,j]\). Their Lemma 3.2 gives the stronger bound with
\(\widehat\mu_{\max}(\bar F)\) in place of \(\widehat\mu(\bar F)\);
only (1.2) is needed here.

The precise metric, local-degree weights, height and slope
conventions were checked on PDF pages 5–6 (journal pages 569–570);
the stated theorem and lemma were checked on PDF pages 9–10
(journal pages 573–574). They allow every Hermitian vector bundle
coming from an integral lattice, not just a standard Euclidean
lattice. The theorem is used as a verified classical input; its
general proof from Zhang's successive-minima theorem is not
reproduced here.

### The ordinary degree agrees exactly

Choose \(K\)-independent \(b_1,\ldots,b_r\in F\) whose integral span
\(F_0\) has finite index in \(F\). Let \(G_\sigma\) be their Hermitian
Gram matrix. The normalized degree used in this project is
\[
 \widehat{\deg}_{\rm n}\bar F
 =\frac{\log\#(F/F_0)-\frac12\sum_\sigma\log\det G_\sigma}
        {[K:\mathbf Q]}.
 \tag{1.3}
\]
The finite-place determinant norms in the adelic definition sum to
\(-[K:\mathbf Q]^{-1}\log\#(F/F_0)\). At infinity,
the logarithm of the determinant norm is
\(\frac12\log\det G_\sigma\). Thus (1.3) is exactly
Gaudron–Rémond's normalized degree, and division by \(r\) gives
their slope. There is no discriminant correction and no replacement
of an ordinary norm by its square.

In particular the actual tangent metric
\(\|x\|_\sigma^2=\pi H_\sigma(x,x)\) is kept as given.
The classical result applies to that Hermitian metric directly;
the factor \(\pi\) is not removed or charged a second time.

## 2. An algebraic line has an integral generator after extension

Fix \(0\ne y\in F_K\otimes_K K'\), and set
\[
 P=(F\otimes_{\mathcal O_K}\mathcal O_{K'})
                              \cap K'y .
 \tag{2.1}
\]
This is a saturated rank-one projective module. Write
\(P=Iy\) for a nonzero fractional ideal \(I\) of \(\mathcal O_{K'}\).
Its ideal class has finite order, so \(I^a=(b)\) for some integer
\(a\ge1\) and \(b\in K'^\times\).
Choose \(\alpha\) with \(\alpha^a=b\) and put \(L=K'(\alpha)\).
Then
\[
 (I\mathcal O_L)^a=(b)=(\alpha)^a
   \quad\Longrightarrow\quad I\mathcal O_L=(\alpha),
 \tag{2.2}
\]
because the group of fractional ideals of \(\mathcal O_L\) is
torsion-free. This argument allows fractional \(I\); \(\alpha\)
need not itself be an algebraic integer.

Consequently \(x=\alpha y\) generates \(P\otimes\mathcal O_L\)
and is a nonzero element of \(F\otimes\mathcal O_L\).
Saturation is preserved under this extension: the quotient by \(P\)
is a finite torsion-free module over the Dedekind ring
\(\mathcal O_{K'}\), hence projective, and remains projective after
base change. Thus \(x\) is primitive in the local lattice at every
finite place of \(L\). Its finite gauge norms are all one. Combining
this with scalar invariance of (1.1) gives the exact identity
\[
 \operatorname{av}_{L}\log\|x\|_\sigma
                      =h_{\bar F}(x)=h_{\bar F}(y).
 \tag{2.3}
\]
The archimedean metric is the pullback of the given metric throughout.
Clearing denominators without (2.2) would not, by itself, justify
this equality.

**Corollary.** For every \(\epsilon>0\), there are a finite extension
\(L/K\) and a nonzero integral vector \(x\in F\otimes\mathcal O_L\)
such that
\[
 \widehat\mu(\bar F)-c_r-\epsilon
                 \le-\operatorname{av}_{L}\log\|x\|_\sigma .
 \tag{2.4}
\]
Indeed choose \(y\) within \(\epsilon\) of the infimum in (1.2)
and apply (2.3). The extension may depend on \(F\) and \(\epsilon\).
No uniform degree bound is asserted or needed.

For a sublattice \(F\) of an ambient Hermitian lattice \(V\),
apply this argument to \(F\) with its own integral gauge norms and
the inherited archimedean norms. Its generator remains an integral
vector of \(V\otimes\mathcal O_L\). No saturation of \(F\) in \(V\)
is required.

## 3. Consequence for the actual theta comparison

Let the actual tangent lattice have rank \(g>0\), normalized
degree \(d\), and \(h=(-d)_+\). Suppose the proved theta-line bound
\[
 -\operatorname{av}_{L}\log\|x\|_\sigma
                 \le C_{\rm line}\log(2+g+h)
 \tag{3.1}
\]
is supplied for every nonzero integral vector after every finite
extension, using the prescribed isometric extension of the tangent
lattice. For each sublattice \(F\) of positive rank \(r\), apply
(2.4) and let \(\epsilon\downarrow0\). This gives
\[
 \boxed{\quad
 \widehat\mu(F)
       \le C_{\rm line}\log(2+g+h)+c_r
       \le(C_{\rm line}+\tfrac12)\log(2+g+h).
 \quad}
 \tag{3.2}
\]
The uniform line bound is evaluated separately at the extensions
chosen for each \(\epsilon\); no limiting number field is formed.
The argument depends only on its unchanged constant, rank, height
and metric, not on the sizes of those extensions.

For the actual selected lattices of ranks \(r_\tau\), put
\(R=\sum_\tau r_\tau\). Then the more precise summed consequence is
\[
 T\le R C_{\rm line}\log(2+g+h)
               +\sum_{\tau:r_\tau>0}r_\tau c_{r_\tau}.
 \tag{3.3}
\]
Thus the selected-sum interface holds with
\(C_s=C_{\rm line}+\tfrac12\), improving the earlier
\(C_{\rm line}+\tfrac32\). If every positive selected rank equals
\(k\), the last sum in (3.3) is \(Rc_k\).
Rank-zero summands contribute zero. If the entire abelian tangent
rank is zero, the selected sum is zero without invoking this theorem.

### Same-data source comparison

The following pinned contracts are sufficient to match this classical
argument to the actual consumer:

| Source at jsmorph/rh, revision ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de | Lines | Checked content |
|---|---:|---|
| HeightsOfSets.Slopes | 14–39 | Gram determinant, index, ordinary degree, normalized slope and saturation |
| IsThetaMeanSquareNorm | 98–105, 128–131 | Actual rank, \(h=(-d)_+\), ordinary norm and required line bound |
| ShortVectorOfSubmodule | 249–324 | The prior consumer asks only for the weaker loss \(\frac12\log g+1\) |
| PolarizedDataFieldExtensionStatement | 12 | Arbitrary finite coefficient-field extension; preserved rank and \(h\), full integral span and the same Hermitian form |

The host CM field is unchanged. The coefficient field in the last row
is allowed to be any finite extension, exactly as required by the
classical argument. The algebraic line and its principalization are
used inside this same integral base change; a Néron-model comparison
is unnecessary for this step.

This source comparison concerns bounded definitions and contracts.
It is not an upstream proof replay. The theta sections, their
finite-prime integrality, primitive determinant normalization and
uniform mean/supremum bounds are not supplied by absolute Siegel
and remain the geometric construction problem.
