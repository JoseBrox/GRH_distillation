# The integral Hodge determinant at ramified primes

## Result and scope

The character quotient of the full Hodge bundle is locally free even when
the tangent eigenlattices do not form locally free coefficient modules.
Their determinants differ by an explicit ideal depending only on the
coefficient field and the signature. A two-term cokernel calculation proves
this comparison, including wild and dyadic ramification.

Consequently, once the actual arithmetic model carries its prescribed Hodge
extension and the coefficient freeness already established for its fibres,
the required integral determinant line can be **constructed**. Its special
fibre degrees agree with those of the character determinant. The ramified
comparison is then a conclusion, rather than an additional identification
to be assumed. This does not construct the arithmetic moduli model, an
integral CM map to its chosen component, or the remaining cusp and section
estimates. No proof-map node is declared complete here.

## 1. The elementary index identity

Let \(R\) be a discrete valuation ring, \(F\) its fraction field, and
\(v\) its valuation with value one on a uniformizer. Choose distinct
\(a_i\in R\), indexed by a nonempty finite set \(I\), and put

\[
 B=R[t]/\prod_{i\in I}(t-a_i),\qquad H=B^n.
\]

Let \(L\) be a finite free \(R\)-module which is a \(B\)-linear
quotient of \(H\), and write \(K\) for its kernel. Over \(F\), let
\(e_i\) be the coefficient idempotents, \(L_i=e_iL_F\), and
\(d_i=\dim_F L_i\). Fix \(i\), and distinguish the image lattice
\(e_iL\) from the saturated kernel lattice
\(L^i=L\cap L_i\). Similarly, \(Q_i=e_iH\) is the character
quotient lattice; it is free of rank \(n\).

Under the rational determinant isomorphism furnished by
\(0\to e_iK_F\to e_iH_F\to L_i\to0\), one has the equality of
rank-one \(R\)-lattices

\[
 \det(e_iK)\otimes\det L^i
  =\left(\prod_{j\ne i}(a_i-a_j)^{d_j}\right)\det Q_i.
 \tag{1}
\]

The order of the two determinant factors changes only the usual sign,
which is an \(R\)-unit. Empty determinants and products have value one.

**Proof.** Let \(T\) denote multiplication by \(t\). Since
\(H/(T-a_i)H=Q_i\), right exactness gives

\[
 Q_i/e_iK\simeq L/(T-a_i)L.
 \tag{2}
\]

Set \(L_0=L\cap\bigoplus_{j\ne i}L_j\) and
\(P_0=(1-e_i)L\). Projection gives

\[
 P_0/L_0\simeq e_iL/L^i,
 \qquad
 \operatorname{tors}\bigl(L/(T-a_i)L\bigr)
       =L_0/(T-a_i)P_0.
 \tag{3}
\]

For the first isomorphism, both quotients record the two projections of
one element of \(L\), modulo elements supported in only one summand.
For the second, the map to the free lattice \(e_iL\) has precisely the
displayed kernel. Therefore the exact sequence

\[
 0\longrightarrow L_0/(T-a_i)P_0
 \longrightarrow P_0/(T-a_i)P_0
 \longrightarrow P_0/L_0\longrightarrow0
\]

shows that the sum of the lengths of the two modules in (3) equals

\[
 v\!\left(\det(T-a_i\mid\textstyle\bigoplus_{j\ne i}L_j)\right)
     =\sum_{j\ne i}d_jv(a_i-a_j).
 \tag{4}
\]

The determinant-length formula follows by diagonalizing an injective
map between free modules over a discrete valuation ring.

Finally, the kernel of \(Q_i\to e_iL\) is a saturated lattice
\(K_0\), and (2) identifies \(K_0/e_iK\) with its torsion module.
Choose a basis of \(e_iK\) and lift a basis of \(L^i\) to \(Q_i\).
The resulting full lattice has index

\[
 \operatorname{length}(K_0/e_iK)
       +\operatorname{length}(e_iL/L^i).
\]

By (3)--(4) this is the right side of (4), proving (1). Different
rational lifts have the same determinant. \(\square\)

## 2. Applying the identity to a Hodge extension

Let \(E\) be a number field with involution \(c\), let \(F\) be a
finite extension of a rational \(\ell\)-adic field containing every
embedding of \(E\), and let \(R=\mathcal O_F\). Suppose that

\[
 0\longrightarrow L^\vee\longrightarrow H\longrightarrow L
       \longrightarrow0
 \tag{5}
\]

is an exact sequence of finite free \(R\)-modules, with compatible
\(\mathcal O_E\)-actions. On its kernel the action is
\(a\lambda=\lambda\circ c(a)\). Assume that \(H\) is locally free
of rank \(n\) over \(\mathcal O_E\otimes_{\mathbf Z}R\).
Write \(d_\tau=\dim_F(L_F)_\tau\), so
\(d_\tau+d_{\tau c}=n\).

For an embedding \(\sigma:E\hookrightarrow F\), let \(S_\sigma\)
be the embeddings inducing the same character
\(\mathcal O_E\to R/\mathfrak m_R\). The corresponding local
coefficient factor has a presentation

\[
 B_\sigma=R[t]/\prod_{\tau\in S_\sigma}(t-a_\tau).
 \tag{6}
\]

To see this, complete \(E\) at the prime below \(\sigma\). Its
largest unramified subfield splits over \(R\), one factor for each
residue character. A uniformizer generates the remaining totally
ramified integer ring. Its minimal polynomial is Eisenstein before
this scalar extension, and its distinct roots after extension are
exactly the \(a_\tau\). This is the usual local-field construction;
see Milne, *Algebraic Number Theory*, Proposition 7.50, Corollary 7.51,
Proposition 7.55 and Remark 7.56, pp. 127--130. It applies at \(\ell=2\)
and to wild ramification. No assumption of an integral global power basis
is being made.

Define the principal ideal

\[
 \mathfrak c_{\sigma,R}
   =\left(\prod_{\substack{\tau\in S_\sigma\\\tau\ne\sigma}}
                 (a_\sigma-a_\tau)^{d_\tau}\right)R.
 \tag{7}
\]

It is independent of the generator in (6). Indeed, if two elements
generate the same \(R\)-algebra, each is a polynomial in the other;
the difference of their two character values is divisible by the
corresponding difference in the other presentation, in both directions.
Each factor in (7) consequently changes by a unit. The ideal commutes
with every finite extension of splitting valuation rings: the same
presentation remains valid and residue characters remain equal or
distinct. At an unramified coefficient prime \(S_\sigma\) has one
element, so \(\mathfrak c_{\sigma,R}=R\).

Let \(L^\sigma=L\cap(L_F)_\sigma\), and put
\(Q_\sigma=H\otimes_{\mathcal O_E\otimes R,\sigma}R=e_\sigma H\),
where \(a\otimes r\) acts on the last factor as \(\sigma(a)r\).
Then, inside the common rational determinant line,

\[
 \boxed{\quad
 \det L^\sigma\otimes(\det L^{\sigma c})^{-1}
       =\mathfrak c_{\sigma,R}\det Q_\sigma.
 \quad}                                                   \tag{8}
\]

**Proof.** Restriction identifies

\[
 e_\sigma(L^\vee)=(L^{\sigma c})^\vee.
 \tag{9}
\]

Indeed, the projector on the dual restricts a functional to the
\(\sigma c\)-eigenspace. The lattice \(L^{\sigma c}\) is saturated
in \(L\), hence a direct summand over \(R\); every integral
functional on it therefore extends to \(L\). This proves surjectivity
in (9), and injectivity follows on the rational eigenspace. Apply (1)
to the factor (6) of (5). \(\square\)

If \(d_\tau=d\) throughout \(S_\sigma\), (7) is the \(d\)-th
power of the evaluated different, since
\(f'(a_\sigma)=\prod_{\tau\ne\sigma}(a_\sigma-a_\tau)\).
For unequal signatures the weighted product is essential.

For clarity, if \(x\) is a basis of \(Q_\sigma\), and \(u\) is
the adapted rational basis obtained from integral bases of
\(L^\sigma,L^{\sigma c}\), write \(x=A u\). Then

\[
 v(\det A)=-\sum_{\substack{\tau\in S_\sigma\\\tau\ne\sigma}}
                       d_\tau v(a_\sigma-a_\tau).         \tag{10}
\]

Thus the prescribed norm with unit lattice on the left of (8) satisfies
\(\|s\|_{\rm tangent}=|c_\sigma|^{-1}\|s\|_{Q_\sigma}\),
where \(c_\sigma\) generates (7). This fixes the direction of the
correction, including its sign in logarithmic norms.

## 3. Constructing the integral line on the actual model

The global Hodge extension used here has a direct construction from the
original global family; it is not an extra vector bundle chosen to fit
the calculation. Let \(\mathcal Y\) be integral and let
\(G/\mathcal Y\) be the prescribed smooth separated semiabelian family,
with abelian fibre over the generic point of \(\mathcal Y\).
Let \(\mathcal P\) be the biextension associated with its original
rigidified symmetric cubical line, with the canonical rigidifications
and biextension laws. Retain the global coefficient action and global
line-bundle adjunction isomorphisms
\(\mathcal P(ax,y)\simeq\mathcal P(x,c(a)y)\). The word
"global" matters: curvewise formal charts alone do not assert this datum
on the whole arithmetic model.

These adjunctions have a unique coherent normalization. In fact, every
regular function on \(G^m\), for \(m\geq1\), equals its zero-section
pullback. On the proper geometrically connected generic fibre it is a
constant. Subtracting its zero-section value therefore gives zero
generically, hence everywhere by flatness over the integral base.
The same argument applies over every open subset of the base. Thus two
line-bundle isomorphisms with the same value at the origin are equal.
Divide each adjunction by its origin unit. All the following comparisons
then have the same source and target and the same rigidified origin
value, so they coincide:

- The addition comparison starts with
  \(\mathcal P((a+b)x,y)\), splits it as
  \(\mathcal P(ax,y)\otimes\mathcal P(bx,y)\), applies the two
  adjunctions, and recombines to \(\mathcal P(x,c(a+b)y)\).
- The multiplication comparison sends
  \(\mathcal P(abx,y)\) first to \(\mathcal P(bx,c(a)y)\),
  then to \(\mathcal P(x,c(b)c(a)y)\). This is the target of
  the adjunction for \(ab\).
- The biextension comparisons split either \(x+x'\) or \(y+y'\);
  both paths have the same two line-bundle factors after adjunction.
  The symmetry comparison sends \(\mathcal P(ax,y)\) to
  \(\mathcal P(c(a)y,x)\), either by adjunction followed by
  symmetry, or by symmetry followed by the inverse adjunction for
  \(c(a)\). The unit and zero comparisons are rigidified identities.

The canonical cubical identifications in each comparison preserve the
origin rigidification. This proves all required coherence, including
compatibility with symmetry, from the actual global isomorphisms.
Normalization commutes with base change; the resulting diagrams remain
valid on every special fibre. No new coherence hypothesis is needed
in this integral, generically abelian situation.

Let \(G_1\) be the first infinitesimal neighbourhood of zero and
\(q:G\times_{\mathcal Y}G_1\to G\). Its square-zero ideal is
\(\omega_G=\operatorname{Lie}(G)^\vee\). Axis rigidification gives
an exact sequence of vector bundles on \(G\):

\[
 0\longrightarrow\operatorname{pr}_G^*\omega_G
 \longrightarrow q_*\mathcal P\longrightarrow\mathcal O_G
 \longrightarrow0.
 \tag{11a}
\]

The inverse image of the section \(1\) is an additive
\(\omega_G\)-torsor \(\mathcal E\to G\). The first biextension
law multiplies its pointed sections and gives
\(0\to(\omega_G)_{\rm add}\to\mathcal E\to G\to0\).
This is a smooth commutative group extension. Hence
\(\mathcal H=\operatorname{Lie}(\mathcal E/\mathcal Y)\) supplies
(5) with \(\mathcal L=\operatorname{Lie}(G/\mathcal Y)\).
Pullback along \(c(a):G_1\to G_1\), followed by inverse adjunction,
defines the coefficient action. Its kernel action is exactly the
conjugate dual. The stated coherence makes these maps an action of the
ring, not merely a collection of lifts of its elements. Finite locally
free pushforward, the inverse-image torsor and its Lie algebra commute
with base change. They therefore glue functorially from the actual
rigidified charts, with the same first-order and mixed-coefficient
transition functions used in the established biextension comparison.
This first-order construction has no characteristic restriction.

Suppose each geometric fibre has the self-dual abelian-quotient
biextension required by the established proper and toric Hodge
comparisons. Those comparisons make \(\mathcal H\) projective over
the coefficient algebra on each geometric fibre. If its generic
coefficient rank is \(n\), flatness of the arithmetic model forces the
same rank on every coefficient factor. Here is an explicit argument
retaining ramification multiplicities. For an integral basis \(b_j\)
of \(\mathcal O_E\), the polynomial
\(\det(T-\sum_jX_jb_j\mid\mathcal H)\) equals the \(n\)-th
power of the regular coefficient polynomial on the generic fibre,
and hence on the flat model. At a geometric special point, its distinct
residue-character linear factors have multiplicities
\(m_\chi r_\chi\), where \(m_\chi\) is the length of the local
coefficient algebra and \(r_\chi\) is the projective rank. The regular
polynomial has multiplicities \(m_\chi\). Thus \(r_\chi=n\),
without dividing by a residue-characteristic integer in the field.

At a stalk with local base ring \(A\), lift a basis of the closed
fibre over \(\mathcal O_E\otimes(A/\mathfrak m_A)\). This fibre
basis descends from the geometric fibre: on each Artin local factor,
lift a residue-field basis and compare dimensions after field extension.
The lifts define
\((\mathcal O_E\otimes A)^n\to\mathcal H_A\).
It is a map between free \(A\)-modules of the same rank, an isomorphism
modulo \(\mathfrak m_A\); its determinant is a unit. It is therefore
an isomorphism of coefficient modules. This establishes the required
global coefficient local freeness from the actual fibre hypotheses.

Let \(K\) be a number field containing the normal closure of \(E\),
and let \(\mathcal Y/\mathcal O_K\) be the actual flat arithmetic
model. Assume it carries its specified locally free tangent bundle
\(\mathcal L\), its actual Hodge extension (5), and a Hodge bundle
\(\mathcal H\) locally free of rank \(n\) over
\(\mathcal O_E\otimes\mathcal O_\mathcal Y\). Assume its generic
signature \(d_\tau\) is constant on the component under consideration.
These hypotheses are supplied by the construction just given when its
global family, adjunction isomorphisms and geometric fibre data are present.
The index lemma itself does not construct that family.

For fixed \(\sigma:E\hookrightarrow K\), define the ideal
\(\mathfrak c_\sigma\) of \(\mathcal O_K\) by its completions (7).
There are only finitely many nonunit factors, all above the discriminant
of \(E\). Set

\[
 \mathcal Q_\sigma
      =\mathcal H\otimes_{\mathcal O_E\otimes\mathcal O_\mathcal Y,\sigma}
                        \mathcal O_\mathcal Y,
 \qquad
 \mathcal M_\sigma
      =\det\mathcal Q_\sigma\otimes
                        \operatorname{pr}^*\mathfrak c_\sigma.
 \tag{11}
\]

This is an invertible sheaf. On the generic fibre the Hodge sequence
identifies it with
\(\det\mathcal L_\sigma\otimes(\det\mathcal L_{\sigma c})^{-1}\).
For **every integral point**, including points after arbitrary finite
ramified extensions of \(K\), its pullback is exactly the determinant
of the two actual tangent eigenlattices. This follows from (8), the
extension compatibility of (7), and faithful flatness of completion.
Taking eigenkernels commutes with these flat extensions: it is the
kernel of finitely many coefficient-action equations. No local freeness
of the individual tangent eigensheaves on the model is required.

On every special-fibre test curve the base ideal in (11) is a constant
one-dimensional line, so it contributes degree zero. The other factor
is exactly the character quotient of the actual Hodge bundle reduced
to that curve. The established Hodge and conjugate filtrations and
coefficient freeness therefore give degree zero by the determinant
torsion theorem. There is no remaining ramified-line identification
in this step.

If the actual model is also normal and proper with nonempty connected
special fibres, the established vertical rigidity theorem now applies
to (11). A nowhere vanishing generic determinant generator has
point-independent finite norms in the prescribed tangent eigenlattices.
The complex extension theorem supplies its constant archimedean norms.
Integral CM maps to the same component, with the same original line and
tangent model, remain necessary to evaluate these constants using the
established product-period calculation.

## 4. Necessary hypotheses and exact tests

The tangent module need not be free over the coefficient algebra.
For \(B=R[t]/(t(t-\pi))\), the quotient \(L=B/(t)=R\) is free over
\(R\) but not projective over the local ring \(B\). Formula (1)
still applies. At the two characters its correction ideals are
\(R\) and \(\pi)\), respectively, as its ranks are \((1,0)\).

The coefficient freeness of the **full** Hodge module cannot be omitted.
If \(H=L=R^2\) and \(T=\operatorname{diag}(0,\pi)\), it has
generic rank one over that same \(B\), but is not \(B\)-free. At
the zero character the actual eigenlattice and character image are
both \(R\), although the right side of (1) would predict \((\pi)\).
This diagnostic pinpoints the needed hypothesis; it is not an example
of an actual Hodge family satisfying the theorem.

The accompanying checker constructs integral stable quotients of
\(B^n\), with different rational quotient subspaces at the different
roots. Smith and Hermite normal forms compute their actual saturated
kernels and projected lattices. The resulting determinant indices are
compared with (7), including dyadic cases, unequal ranks, zero ranks and
nontrivial mixing. These finite exact checks supplement the proof; they
are not a proof for all lattices or a replay of Lean.

## 5. Verified source correspondence

All Lean contracts below are pinned to `jsmorph/rh` revision
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. The checker authenticates
whole cached bytes against the atlas blob, then records only bounded
excerpts and hashes. Reading these contracts does not establish that
the entire upstream Lean project builds.

| Source under `lean/src/Development/` | Lines | Exact use |
|---|---:|---|
| `AutomorphicSpectrum/Proofs/AlgebraProofs/CmTypeValuationEmbedding.lean` | 20--63, 291--301 | Fixed local correction \(Q/P^n\), where the exponent in \(Q\) is the conjugate signature; (10) simplifies it to the inverse of (7). |
| `AutomorphicSpectrum/Proofs/AlgebraProofs/ValuationLatticeMatrixReduction.lean` | 198--254 | Source adapted determinant conclusion; the cokernel proof above replaces its filtration calculation over discrete valuation rings. |
| `AutomorphicSpectrum/Proofs/AlgebraProofs/StatementUnavailableOne.lean` | 5--8 | Exact local monogenic residue-character contract, not a global integral power-basis assertion. |
| `AutomorphicSpectrum/Proofs/GeometryProofs/EigenLinePAdicFrame.lean` | 72--88, 295--338 | The same correction is used for every actual integral point; the remaining factor is a unit. |
| `AutomorphicSpectrum/Proofs/GeometryProofs/HodgeLatticeSpanIndependent.lean` | 8--18 | The character quotient and its determinant are vector bundles. |
| `AutomorphicSpectrum/Proofs/GeometryProofs/ExistsHodgeLatticeGermSystem.lean` | 84--114 | Projection is the prescribed tangent lattice and the vertical kernel is its actual integral dual. |
| `AutomorphicSpectrum/Proofs/GeometryProofs/HodgeLatticeDvrDegree.lean` | 163--201, 202--237 | Same character quotient on the test curve, with the actual integral transitions. |
| `AutomorphicSpectrum/Proofs/GeometryProofs/EigenLinePAdicBound.lean` | 193--251 | Construction is applied to the actual model; its geometric, fibre and level hypotheses remain explicit. |

The global model contract is separately pinned in
`ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/PushInvertible.lean`,
52--66: it contains a global semiabelian datum.
In the same directory, `TwoWeightEqOneAddRoot.lean`, 72--91, records
the original rigidified cubical line, coefficient action, adjunction
isomorphisms and Cartesian transports. The generic abelian condition and
flatness prove the adjunction coherence by the normalization argument
above. The actual geometric fibre comparison and the existence of this
arithmetic model remain separate inputs; they are not inferred merely
from the names of structure fields.

Primary local-field reference: J. S. Milne, *Algebraic Number Theory*,
version 3.08, 19 July 2020,
<https://www.jmilne.org/math/CourseNotes/ANT.pdf>, pp. 127--130.
The downloaded PDF SHA-256 is
`24b83c789a89f25aebffb3cbe4ae5ca29edd0075acc072de093d140770630847`.
The bounded extracted-text ranges are 6742--6810 and 6863--6901,
counted with Python `splitlines()` on `pdftotext -layout` output.

The mathematical review and executable evidence have separate scopes.
The checker/certificate records source authentication and finite exact
tests. The independent mathematical review is recorded by the project
in `certificates/frontier-progress-review-2026-11-22.json`.
