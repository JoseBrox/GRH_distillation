# The two filtrations on the actual biextension lattice

## Proved result and remaining input

The two required filtrations can be constructed directly from the actual
symmetric biextension on the semiabelian family. This identifies their
bundle with the prescribed formal Hodge lattice, including its
coordinate changes, coefficient action, symplectic cross term, and the
two conjugate maps. The construction is global wherever the original
family and biextension are defined; a global abelian quotient is not
needed.

Precisely, let \(p\) be prime, let \(S/\mathbf F_p\) be a scheme, and let
\(G/S\) be a smooth separated commutative group scheme of relative
dimension \(d\). Let \(\mathcal P\) be a symmetric biextension on
\(G\times_S G\), rigidified on the axes, whose symmetry is the identity
on the diagonal. Assume that each geometric fibre is semiabelian and
that its biextension is pulled back from a line bundle on the abelian
quotient inducing an isomorphism with the dual quotient. Then the
actual bundle \(\mathcal H\) has exact sequences
\[
 0\longrightarrow\mathcal V^*\longrightarrow\mathcal H
       \longrightarrow\mathcal V\longrightarrow0,
 \qquad
 0\longrightarrow F_S^*\mathcal V\longrightarrow\mathcal H
       \longrightarrow F_S^*(\mathcal V^*)\longrightarrow0,
 \quad \mathcal V=\operatorname{Lie}(G/S).
\]
A coefficient action with its prescribed Hermitian adjunction makes
these the required equivariant sequences. The quotient actions are the
conjugate dual actions, and the Frobenius pullbacks use the pulled-back
coefficient action.

This proves the filtration supplier from the stated geometric data.
Together with the coefficient-freeness proof already checkpointed, it
supplies the actual bundles needed by the determinant-torsion argument.
Constructing the prescribed proper integral model and its
self-dual pullback fibre data is still an independent input. The
integral complex multiplication evaluation, finite section and cusp
comparisons are also separate. No RH or GRH node is declared complete.

## 1. A vector extension on the same family

Let \(G_1\) be the first infinitesimal neighbourhood of the zero section.
It is finite locally free over \(S\), of rank \(d+1\), with square-zero
ideal
\[
                     \omega_G=e^*\Omega^1_{G/S}=\mathcal V^*.
\]
For a point \(x\) of \(G\), consider pointed sections of
\(\mathcal P_x|_{G_1}\). Their differences are units \(1+\lambda\),
with \(\lambda\in\omega_G\); multiplication of such units is addition.

The pointed-section functor is an affine vector torsor over \(G\).
For an explicit construction, push the invertible sheaf
\(\mathcal P|_{G\times_SG_1}\) forward along the finite flat projection.
It sits in an exact sequence of vector bundles on \(G\),
\[
 0\longrightarrow \mathcal O_G\otimes\omega_G
 \longrightarrow \operatorname{pr}_*(\mathcal P|_{G\times_SG_1})
 \longrightarrow \mathcal O_G\longrightarrow0.
\]
The inverse image of the unit section is the required torsor.
The first biextension law defines a commutative group law on it.
Write the resulting vector extension as
\[
 0\longrightarrow(\omega_G)_{\mathrm{add}}
      \longrightarrow\mathcal E_{\mathcal P}
      \xrightarrow{\pi}G\longrightarrow0.
\]
Its Lie algebra is \(\mathcal H\), and taking Lie algebras gives the
first exact sequence. These constructions commute with arbitrary base
change. In particular they can first be made on the original mixed
characteristic model and then restricted to a special fibre.

At a proper abelian fibre, self-duality identifies
\(\mathcal E_{\mathcal P}\) with the universal vector extension.
This is precisely the rigidified-extension description already proved
in the coefficient-freeness note, not a new comparison with an
unspecified realization.

## 2. Multiplication by \(p\) constructs the conjugate map

Since \(p\) kills the vector subgroup of \(\mathcal E_{\mathcal P}\),
its multiplication-by-\(p\) map descends through \(\pi\) to
\[
 j:G\longrightarrow\mathcal E_{\mathcal P},
                       \qquad j\pi=[p]_{\mathcal E_{\mathcal P}}.
\]
At the identity, \(dj=0\), because \(d\pi\) is surjective and
\(d[p]=0\). Translation makes the relative differential zero
everywhere.

For a smooth scheme over an \(\mathbf F_p\)-scheme,
\[
 \ker(d_{G/S})
   =\operatorname{im}\bigl(F_{G/S}^{\#}:
                    \mathcal O_{G^{(p)}}\to F_{G/S*}\mathcal O_G\bigr).
\]
In polynomial coordinates this is the elementary assertion that a
polynomial with zero partial derivatives is a polynomial in the
\(p\)-th powers, with coefficients from the base. The assertion
passes to étale coordinates. Relative Frobenius is a finite locally
free universal homeomorphism, so the function-level factorization
gives a unique morphism
\[
       \Phi:G^{(p)}\longrightarrow\mathcal E_{\mathcal P},
                       \qquad \Phi F_{G/S}=j.
\]
It is a group homomorphism by uniqueness and faithfully flat descent.
Its differential gives
\[
                 \alpha:F_S^*\mathcal V\longrightarrow\mathcal H.
\]
No flatness assumption on the absolute Frobenius of \(S\) is used.

## 3. Exact match with the formal coordinates

Choose formal coordinates \(x\) and a frame \(e(x,y)\) of
\(\mathcal P\), rigidified on both axes. A pointed section is
\(e(x,y)(1+\lambda(y))\) on the first neighbourhood in \(y\).
If \(\varphi_1(x,x',y)\) is the scalar of the first biextension law,
multiplication in \(\mathcal E_{\mathcal P}\) adds
\(d_y\varphi_1(x,x',0)\) to \(\lambda+\lambda'\).

Let \(C(x,y)\) be the scalar of \(p\)-fold multiplication in the first
variable, with the exact convention
\[
                 e(x,y)^{\otimes p}\longmapsto
                                 C(x,y)e([p]x,y).
\]
Thus
\[
             C(x,y)=\prod_{n=0}^{p-1}\varphi_1([n]x,x,y).
\]
Let \(D\) be the corresponding second-variable scalar. Define
\[
 h_{ij}=[x_j^p]\,[p]_G(x)_i,\qquad
 A_{ij}=[x_i^p y_j]\,C(x,y).
\]
The descended map \(j\) has formal coordinates
\[
            j(x)=\bigl([p]_G(x),d_yC(x,0)\bigr).
\]
Since relative Frobenius raises the formal coordinates to their
\(p\)-th powers, differentiation after its factorization gives exactly
\[
                             \alpha(v)=(hv,A^tv).
\]
These are the source's actual matrices, with no unspecified linear
change or rescaling. The identity \(dj=0\) also proves
\([x_i y_j]C=0\).

The same first-neighbourhood construction gives the coefficient action.
For adjunction
\[
          e(ax,y)\longmapsto u_a(x,y)e(x,\bar a y),
                 \qquad b_a=[x_i y_j]u_a,
\]
inverse pullback of a pointed section gives
\[
              a(v,\lambda)
               =(\rho(a)v,\rho(\bar a)^t\lambda-b_a^tv).
\]
This is the action used in the earlier freeness proof.

## 4. Isotropy, including characteristic two

Write the symmetry of \(\mathcal P\) as
\[
                   e(x,y)\longmapsto s(x,y)^{-1}e(y,x),
                        \qquad \Sigma_{ij}=[x_i y_j]s.
\]
Comparing the two pointed sections at a pair of first-order tangent
points gives the intrinsic bilinear form
\[
 \langle(v,\lambda),(w,\mu)\rangle
                =\mu(v)-\lambda(w)+v^t\Sigma w.       \tag{1}
\]
The relation \(s(x,y)s(y,x)=1\) gives
\(\Sigma+\Sigma^t=0\). The diagonal identity \(s(x,x)=1\) also gives
\(\Sigma_{ii}=0\), which is needed in characteristic two.
Thus (1) is alternating. Its off-diagonal identity blocks make it
perfect.

The symmetry and interchange laws give two exact identities:
\[
 D(x,y)=C(y,x)\frac{s(x,[p]y)}{s(x,y)^p},              \tag{2}
\]
\[
 C(x,[p]y)D(x,y)^p=D([p]x,y)C(x,y)^p.                \tag{3}
\]
Equation (2) and \([x_i y_j]C=0\) imply \([x_i y_j]D=0\).
Because \([p]_G\) factors through relative Frobenius, every coordinate
has degree at least \(p\). Take the pure coefficient \(x_i^p y_j^p\)
in (3), then substitute (2). The factors \(C^p,D^p\) have zero
coefficient there: that coefficient is the \(p\)-th power of the
vanishing bilinear coefficient. The first-variable degree of
\(s([p]x,y)^{-p}-1\) is at least \(p^2\). Normalization on the axes
prevents lower mixed products from contributing. The surviving terms
give
\[
                            Ah=h^tA^t+h^t\Sigma h.   \tag{4}
\]
Consequently
\[
 \langle\alpha(v),\alpha(w)\rangle
      =v^t(h^t\Sigma h+h^tA^t-Ah)w=0.
\]
This proof is valid for every prime, including \(2\); it does not
require identifying a crystalline polarization pairing.

The adjunction is compatible with symmetry in the precise form
\[
 u_a(x,y)u_{\bar a}(y,x)=s(x,\bar a y)/s(ax,y).
\]
Taking the mixed coefficient gives
\[
              b_a+b_{\bar a}^t
                         =\Sigma\rho(\bar a)-\rho(a)^t\Sigma,
\]
which proves
\(\langle az,z'\rangle=\langle z,\bar a z'\rangle\)
for this same form.

## 5. Proper-fibre injectivity: Frobenius versus Verschiebung

Let \(B\) be a proper geometric fibre after the prescribed self-duality.
Its extension is \(E(B)\). For the Verschiebung
\(V_B:B^{(p)}\to B\), the map \(E(V_B)\) kills the additive vector
subgroup of \(E(B^{(p)})\): on that subgroup it is pullback on invariant
forms by the dual map
\[
                            (V_B)^\vee=F_{B^\vee},
\]
whose differential is zero.
It therefore factors through a map \(B^{(p)}\to E(B)\).
Functoriality of the universal extension and \(V_BF_B=[p]_B\)
show that this factor is exactly the previously constructed \(\Phi\).

Now take the **contravariant** Dieudonné module of
\(B^\vee[p^\infty]\). Its reduction is \(\operatorname{Lie}E(B)\).
The reduction of its crystalline Frobenius is the differential of
\(E((F_{B^\vee})^\vee)=E(V_B)\).
The standard Hodge-kernel comparison says
\[
             \ker(F\bmod p)=F_k^*\omega_{B^\vee}.
\]
Its induced map on the quotient
\(F_k^*\operatorname{Lie}B\) is therefore injective.
This is precisely \(\alpha_B\).

Thus the group-level projection of \(\Phi\) is Verschiebung, while the
map on the universal-extension Lie algebra is crystalline Frobenius
under the contravariant convention. Confusing those two statements
would reverse the required Hodge quotient.

The primary inputs are Mazur–Messing's functorial universal-extension
crystal comparison, II §§9 and 13, and the exact Hodge-kernel formula
in Madapusi Pera §1.1.4, equation (1.1.4.1), printed p. 405.
The latter is stated for every prime \(p\).

## 6. Toric fibres and gluing

At a geometric semiabelian fibre, choose its actual quotient
\[
                         0\to T\to G\xrightarrow{q}B\to0
\]
and its pullback biextension. Restriction of pointed sections to \(T_1\)
gives a homomorphism
\[
                         \mathcal E_{\mathcal P}\to\omega_T.
\]
Its kernel is
\[
                         \mathcal E'=G\times_B E_B.
\]
Indeed a first-order rigidification with zero restriction to \(T_1\)
is exactly the pullback of one on \(B_1\).

Since \(p\) kills \(\omega_T\), the map \(\Phi\) lands in \(\mathcal E'\).
Its composite to \(E_B\) is \(\Phi_Bq^{(p)}\). This follows by composing
with relative Frobenius and then using the defining multiplication
maps; both descent maps are faithfully flat. On \(T^{(p)}\), the map
is toric Verschiebung into \(T\subset\mathcal E'\). Over the
algebraically closed field this is an isomorphism.

If \(\alpha(v)=0\), proper-fibre injectivity gives
\(dq^{(p)}v=0\). The tangent sequence of the smooth torus quotient puts
\(v\) in \(\operatorname{Lie}T^{(p)}\), where toric Verschiebung is
injective. Hence \(\alpha\) is injective at every geometric point.
The fibrewise rank criterion makes it a locally split injection of
vector bundles on \(S\), without requiring a global quotient or
constant toric rank.

Define
\[
       \beta(z)(v)=\langle\alpha(v),z\rangle,\qquad
                    \beta:\mathcal H\to F_S^*(\mathcal V^*).
\]
Perfection makes \(\beta\) surjective. Isotropy gives
\(\operatorname{im}\alpha\subset\ker\beta\); equality follows because
both are subbundles of rank \(d\), with equal fibres.
In the same coordinates,
\[
                     \beta(v,\lambda)
                       =h^t\lambda-(A-h^t\Sigma)v.
\]
This is the source formula exactly.

Coefficient endomorphisms of \(\mathcal E_{\mathcal P}\) commute with
multiplication by \(p\). Uniqueness of Frobenius factorization proves
equivariance of \(\alpha\) for the pulled-back action. The adjoint
identity in §4 proves equivariance of \(\beta\) for the conjugate dual
action.

## 7. The same transition matrices and integral lattice

Fix frames and coordinates with
\[
 e_2(x,y)=\ell(x,y)e_1(\phi x,\phi y),\qquad
                  L=d\phi,\quad Z_{ij}=[x_i y_j]\ell.
\]
Expressing the same pointed section in the two frames gives the
transition \(T:\mathcal H_2\to\mathcal H_1\),
\[
 T(v,\lambda)=\bigl(Lv,L^{-t}(\lambda+Z^tv)\bigr),
 \qquad
                  \Sigma_2=L^t\Sigma_1L+Z^t-Z.        \tag{5}
\]
Thus \(T\) preserves (1), including when \(Z\) is nonsymmetric.
Equation (5) is precisely the source transition. At each original
local stalk, the chosen integral coordinates and frame identify the
lattice with the original free module. The projection is the actual
Lie lattice and the second summand is its actual dual. The comparison
uses no fractional isogeny, change of integral model, or metric
rescaling.

For the special fibre of the original model, this supplies a global
bundle and global filtrations if the original family and biextension
are global there and the fibre hypotheses hold at every geometric
point. In that situation the earlier determinant argument gives
global torsion of the indicated determinant powers. If only the
pullback to a test curve is supplied, the conclusion remains on that
test curve. This distinction is explicit, rather than being inferred
from agreement at generic points.

## 8. Exact curvewise consumer and the original line bundle

The construction also applies to compatible formal charts at the
generic point and local rings of a smooth curve. The first-neighbourhood
extension and its group law are formal constructions. In characteristic
\(p\), zero partial derivatives of a power series mean that each
exponent is divisible by \(p\); consequently the same relative
Frobenius factorization defines \(\alpha\) formally. The displayed
formulas for the pairing, \(\alpha\), \(\beta\), and the coefficient
action commute with the integral transitions (5). They therefore give
maps of the prescribed curve bundles. If every geometric residue
chart is the chart of an actual semiabelian variety satisfying the
proper-quotient hypothesis, the fibrewise argument proves rank \(d\).
The local rank criterion and isotropy give the exact sequences.

This is the precise interface in FibreCurveGermPowers 215–270:
one generic chart, valuation-ring charts and their residue charts,
the original IsIso/transH transports, and the almost-everywhere
integrality condition assemble the curve data. No new global
semiabelian scheme on the whole test curve is needed. A global
family, when available, is a convenient stronger hypothesis.

There is no untracked polarization power in this match.
IsChartIff 74–75 defines each frame on the two-variable cubical line
of the **original** t.PP.L. ToFirst 36–39 supplies an isomorphism
of that original line, after geometric base change, to \(q^*M\),
where \(M\) has trivial translation kernel on \(B\).
ExistsInKNeOne 32–35 tests the kernel on **all coefficient rings**;
this is scheme-theoretic triviality, including infinitesimal
\(p\)-primary points. Thus \(\lambda_M:B\to B^\vee\) has finite
kernel, full-dimensional image and degree one, so is an isomorphism.
Using only geometric pointwise kernel triviality would not suffice.

Normalize the line isomorphism at zero. It induces an isomorphism
of the associated biextensions: the quotient between either
multiplication law is a global unit on \(G^3\), equal to one on
the coordinate identity loci. By the units-on-products theorem
it factors into units in the separate variables, and the
normalizations make every factor constant and the product one.
The canonical exchange of the two factors of the cubical line is
identity on the diagonal. This gives \(s(x,x)=1\), which is needed
for alternation in characteristic two; the abstract identity
sy_inv alone would only give skew symmetry.

The primitive normalization in AbelianQuotientOfPowerFns
193–225 likewise preserves the original line class and trivial
kernel: the last returned field is an isomorphism of the original
line with the quotient's pullback, rather than an isogeny or a
tensor-power comparison. Our direct fibrewise injectivity proof
needs only the actual original-line pullback and trivial kernel
in GeomPF; the source's separate PowFns hypothesis is not
needed for this conclusion. The compatible-chart and global-model
construction hypotheses themselves are retained.

## 9. Source evidence and verification boundary

All source reads use
[jsmorph/rh at ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de](https://github.com/jsmorph/rh/tree/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de),
with full-file byte authentication and bounded displayed ranges.

| Source, relative to the source tree | Bounded ranges | Exact match |
| --- | --- | --- |
| Formalism/LocalToGlobal/ProjectiveLattices/IsChartIff | 74–117 | Original cubical line, actual multiplication frames, canonical symmetry and adjunction directions |
| Formalism/SharpRestriction/Divisibility/GeneratorPowers/GermCut | 111–125 | Coefficient action and adjoint-symmetry coherence |
| Development/AutomorphicSpectrum/Definitions/CommutativeAlgebra/GermComp1ZeroPointLeft | 17–52, 68–104 | Both \(p\)-fold scalars, \(h,A,\rho_H,\langle\, ,\,\rangle,\alpha,\beta\), and transitions |
| Development/AutomorphicSpectrum/Definitions/CommutativeAlgebra/IsSplitGaussChars | 101–131 | Exact equivariant two-filtration contract |
| Development/AutomorphicSpectrum/Proofs/GeometryProofs/ExistsHodgeLatticeGermSystem | 85–114 | Actual Lie projection and dual inverse image |
| Development/AutomorphicSpectrum/Proofs/GeometryProofs/FibreCurveGermPowers | 215–270 | Original curvewise supplier replaced by the intrinsic construction |
| Development/AutomorphicSpectrum/Proofs/GeometryProofs/AbelianQuotientOfPowerFns | 192–225 | Actual proper quotient, adjunction, self-duality and pullback line |
| Development/AutomorphicSpectrum/Proofs/GeometryProofs/AbelianQuotientLattice | 423–450 | Actual equivariant tangent quotient |
| Development/AutomorphicSpectrum/Definitions/GlobalGeometry/ToFirst | 18–39 | Actual original-line formal frame and geometric pullback condition |
| Development/AbelianVarietyTheory/Definitions/Uniformization/ExistsInKNeOne | 19–35 | Translation kernel tested on all coefficient rings |

Primary references, directly inspected:

- B. Conrad, *Units on products*, undated notes, Theorem 1.1,
  p. 1 and proof on pp. 1–3.
  [Author PDF](https://math.stanford.edu/~conrad/papers/unitthm.pdf),
  SHA-256: 0720c7f594d69049ebe70d804582a252fcd83852b6f530b3f52fabb7cee9e9e0.
- B. Mazur and W. Messing, *Universal Extensions and One Dimensional
  Crystalline Cohomology*, Lecture Notes in Mathematics 370, Springer,
  1974, I §2.1 and Proposition 2.6.7, printed pp. 13 and 24–25;
  II §§9 and 13, pp. 93–94 and 119–122.
  [Primary PDF](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/mazur-messing.pdf),
  SHA-256: 54486ccb86cad19118bfdb9d1e56386b18a45c63529254f1a1f7b7d110ca5eee.
- K. Madapusi Pera, *Toroidal compactifications of integral models of
  Shimura varieties of Hodge type*, Ann. Sci. ENS (4) 52 (2019),
  393–514, §1.1.4, pp. 404–405, especially (1.1.4.1).
  Only the ordinary integral Dieudonné/Hodge comparison is used here.
  [Published PDF](https://www.numdam.org/item/10.24033/asens.2391.pdf),
  SHA-256: d7e0dfa1d9ef76f3f85682f1abcc52d3d66de9e9378e92fc9153a3ba5c10a077.

The checker authenticates these references and the bounded source
excerpts and checks exact matrix identities, nonsymmetric frame
changes, and small-characteristic biextension examples. It does not
machine-prove the geometric theorem, replay the Lean kernel, or
construct the compactification.

The next model-level task is now narrower: supply the original
compatible formal charts, their actual integral transitions and the
self-dual pullback condition on every relevant geometric fibre of
the chosen proper integral model. An original semiabelian family
and its actual symmetric biextension provide such charts. No
separate logarithmic-realization comparison is required for the
two filtrations once those data are present.
