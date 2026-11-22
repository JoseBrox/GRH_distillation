# The prescribed complex multiplication point is algebraic

## 1. Result and scope

The actual pure-period point in the given fine moduli space is defined
over a number field. A short automorphism argument proves this for the
**same complex point**, with its original symmetric rigidified cubical
line, coefficient action and both finite level maps. It replaces the
spreading and countability argument in the pinned source. It does not
construct the moduli space or its pointwise period presentation.

The exact symmetric-line descent used below is already proved in
[the CM product calculation, Section 3.1](cm-product-period-calculation.md).
The subsequent integral extension is proved in
[the CM extension note](cm-integral-map-extension.md).
No infinite compatible Tate basis is descended.

## 2. An algebraicity criterion for a separated moduli point

Let \(k\subset\overline{\mathbf Q}\subset\mathbf C\) be a number field,
and let \(X/k\) be a scheme of finite type carrying a family of abelian
varieties with an action of a fixed order, an original symmetric
ample rigidified cubical line, and specified homomorphisms from finitely many
fixed finite groups to the fibres. Assume the following point-separation
property: two complex points of \(X\) are equal whenever their fibres
are isomorphic with **all these labelled data**.

**Proposition.** If the abelian variety at \(z\in X(\mathbf C)\) is
isogenous to a power of an elliptic curve with complex multiplication
defined over \(\overline{\mathbf Q}\), then \(z\in X(K)\) for a number
field \(K\supset k\). The same original line, action and finite level
maps descend with the point. Any fixed finite extension of \(k\) may
be included in \(K\).

**Proof.** Write the isogeny as \(C^g\to A_z\), where
\(C/\overline{\mathbf Q}\) is the chosen elliptic curve. Its kernel is
contained in \(C^g[N]\) for some positive integer \(N\). Every point
of this finite group is algebraic, so the kernel and its quotient are
defined over \(\overline{\mathbf Q}\). This gives a model of \(A_z\)
over that field with a specified complex isomorphism. Homomorphism
rigidity descends every coefficient endomorphism and the polarization.

Here the original symmetric line must be retained, not just its
polarization class. Choose an algebraic line inducing the polarization
and make it symmetric by a square-root adjustment in
\(\operatorname{Pic}^0\). Its ratio with the specified symmetric line
belongs to \(\operatorname{Pic}^0[2]\), hence is algebraic. Normalize
the comparison at zero. The cubical structure and normalized symmetry
are unique. This is exactly the descent argument already proved in
the CM product calculation, using Milne, Theorems 2.8--2.9,
Remark 8.12, Proposition 13.6 and Corollary 16.4. Arbitrary additional
scalar choices of adjunction are not included in the moduli labels;
normalized adjunctions are determined by the descended line and action.

All images of the finite level maps are torsion points, hence algebraic.
Thus the whole labelled object is defined over \(\overline{\mathbf Q}\).
For every \(\gamma\in\operatorname{Aut}(\mathbf C/\overline{\mathbf Q})\),
the objects at \(z\) and \(z^\gamma\) are labelled-isomorphic. Point
separation gives
\[
                             z^\gamma=z.                 \tag{1}
\]

Choose a \(k\)-affine open containing \(z\). Equation (1) makes each
of its coordinate values invariant under every such \(\gamma\).
The fixed field is \(\overline{\mathbf Q}\): if \(t\) is transcendental,
extend it to a transcendence basis of \(\mathbf C/\overline{\mathbf Q}\);
the automorphism sending \(t\) to \(t+1\) and fixing the other basis
elements extends to the algebraic closure \(\mathbf C\). Therefore
every coordinate of \(z\) is algebraic. Finite type puts these finitely
many coordinates in one number field. Enlarge that field to define the
labelled object and any prescribed auxiliary number field. Once the
universal fibre is over this field, homomorphism rigidity descends its
group comparison and the product maps; the original-line comparison
descends by normalizing at zero. A further finite extension defines
all of them. The finite level maps agree by faithful base change.
\(\square\)

Point separation is essential. A constant labelled CM family over
\(\mathbf A^1_k\) has the same CM fibre above a transcendental point,
and does not separate those points.

## 3. The exact pure-period hypothesis supplies the isogeny

Let \(F\) be the fixed imaginary quadratic field, and let
\(\Lambda\) be the integral coefficient lattice at the chosen period
point. Suppose the actual universal fibre has a holomorphic
exponential
\[
 e:\mathbf C^g\longrightarrow A_z(\mathbf C),\qquad
 \ker e=P\Lambda,
\]
which is surjective, with \(P\) injective, \(P\Lambda\) a full period lattice and
the prescribed \(\mathcal O_F\)-action. For the two embeddings
\(\iota_+,\iota_-:F\hookrightarrow\mathbf C\), put
\[
 \Lambda^\varepsilon=
 \{x\in\Lambda:P(ax)=\iota_\varepsilon(a)P(x)
                         \text{ for every }a\in\mathcal O_F\}.
\]
Retain the exact finite-index condition
\[
       N\Lambda\subset\Lambda^++\Lambda^-
                    \quad\text{for some integer }N>0.     \tag{2}
\]
The two rational pure subspaces have zero intersection: an element in
both would have \((\iota_+(a)-\iota_-(a))P(x)=0\) for a nonreal
\(a\), so \(x=0\). Condition (2) therefore gives a basis
\(x_1,\ldots,x_g\) of \(\Lambda\otimes\mathbf Q\) over \(F\), with
each \(x_j\) integral and pure. Their \(\mathcal O_F\)-span has finite
index in \(\Lambda\).

The maps \(w\mapsto e(wP(x_j))\) descend from
\(\mathbf C/\iota_+(\mathcal O_F)\), using the conjugate
\(\mathcal O_F\)-action for negative-pure vectors. Their product is
a holomorphic isogeny onto the **actual fibre** \(A_z\). Indeed, the
complex span of the \(P(x_j)\) contains the finite-index period
sublattice, whose real span is all \(\mathbf C^g\). The resulting
linear map is invertible, and its source and target period lattices
have finite index. The CM elliptic curve is algebraic because its
\(j\)-invariant at an imaginary quadratic period is algebraic
(Milne MF, Corollary 12.9). Holomorphic homomorphisms of complex abelian varieties
are algebraic. The preceding proposition applies. Dimension zero
causes no exception: the empty product is the trivial abelian variety.

Consequently the very point selected by the pure period is defined
over a number field. Its component and its original line are retained
because the complex point itself is unchanged. After the finite
extension used for the good CM model, properness and the exact
semiabelian extension theorem give the integral point and tangent
lattice comparison already proved in the CM extension note.

Only the period presentation at this one point is used. Neither
surjectivity of the global period map, algebraicity of that map, a
classification of all components, nor a separately descended infinite
Tate tower is required for this conclusion.

## 4. Exact correspondence with the pinned source

All source rows refer to `jsmorph/rh` at
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The checker authenticates the module bytes and the bounded ranges.

| Source module | Lines | Exact use |
| --- | --- | --- |
| ToroidalCompactification/PushInvertible | 29--39 | The moduli scheme is of finite type; uniqueness in its representing property over the reduced base \(\operatorname{Spec}\mathbf C\) supplies point separation. |
| ToroidalCompactification/TwoWeightEqOneAddRoot | 14--25, 30--39, 53--64 | The imaginary quadratic subfield is supplied; the coefficient lattice is finite projective; \(I\bar I=(M)\), so \(M\Lambda\subset I\Lambda\); the second level is killed by a positive integer. |
| ToroidalCompactification/TwoWeightEqOneAddRoot | 72--91, 144--166 | The labelled isomorphism preserves the group, coefficient action, original cubical line and the two level maps. Raw adjunction and primitivity witnesses are not extra scalar labels in this isomorphism. |
| ToroidalCompactification/TwoWeightEqOneAddRoot | 131--160 | A compatible infinite Tate system is existential geometric data; it is not a chosen tower required to descend. |
| ToroidalCompactification/IsHolPeriods | 16--20, 51--75, 84--93 | The full lattice and coordinatewise coefficient action, chosen actual point, holomorphic exponential and exact kernel give the pointwise period presentation. The two finite level maps are the original ones. |
| Statements/PrincipalLattices/FiniteDimensionalBase | 16--25 | The source's pure lattice consists of vectors supported on the coordinates where \(\sqrt{-d}\) has the specified sign; this is exactly \(\Lambda^\pm\) above. |
| SesquilinearFractions/GRational | 24--48, 79--100 | The exact target is number-field rationality of the prescribed pure-period point. The original proof uses spreading and a countability theorem. |
| GeometryProofs/FamilyPurePeriodsSpan | 8--11 | The downstream wrapper has the identical finite-index hypothesis and exact complex-point equality. |
| GeometryProofs/CmPeriodAlgebraic | 71--100, 108--137 | The consumer enlarges the field and identifies the universal fibre at that exact point when constructing the CM data. |

Let \(\Lambda_0\) be the fixed lattice indexing the level maps; it
need not be the chosen component's period lattice \(\Lambda\).
For the first level map, the source's relation \(I\bar I=(M)\)
implies \(M\Lambda_0\subset I\Lambda_0\), so the map factors through
the finite group \(\Lambda_0/M\Lambda_0\); the second factors through
\(\Lambda_0/A\Lambda_0\). Both **entire labelled maps**, not merely
their images, descend. The roots of unity and coefficient base data
belong to the base number field and are fixed throughout.

For completeness, the pure-lattice match is exact. Coordinatewise
coefficient linearity says \(P(ax)_j=\tau_j(a)P(x)_j\). Support only
where \(\tau_j(\sqrt{-d})=\iota_\varepsilon(\sqrt{-d})\) is therefore
equivalent to \(F\)-linearity of sign \(\varepsilon\): extend \(P\)
\(\mathbf Q\)-linearly and use that \(\sqrt{-d}\) generates \(F\).
Restriction to integral vectors gives the stated \(\mathcal O_F\) condition.
Thus no stronger pure decomposition has replaced the source's
finite-index hypothesis.

The proof compares the existing objects at \(z\) and \(z^\gamma\).
It never constructs a new moduli object over a field by asserting the
geometric Tate-system condition. This is why no descent of infinitely
many compatible torsion choices is hidden in the argument.

## 5. Remaining geometric inputs and verification

This proves the separate generic CM-point supplier from the actual
moduli separation and pointwise period hypotheses already required by
the geometry. The arithmetic moduli model, the original universal
family and its boundary-fibre conditions, and the required pointwise
period presentation remain to be constructed or supplied. The cusp
mean and finite-section estimates are unchanged. No proof-map node
is declared complete.

Run `python scripts/check_cm_period_point_descent.py` to authenticate
the source excerpts, the previously audited CM descent package and
the primary Milne reference. The script does not prove the descent
argument or replay Lean. Mathematical review is recorded separately in
`certificates/frontier-progress-review-2026-11-22.json`.
