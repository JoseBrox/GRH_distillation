# Specific weak base-change Hecke levels and matched operators

We complete the transfer-level and matching-product inputs of
[definite base-change trace transfer](lsernau-base-change-trace-transfer.md)
using [global norm roots and compact levels](lsernau-global-norm-roots.md).
This proves weak prime-degree base change for the source definite groups
under its actual Step and local matching hypotheses. The construction
of special local matching data (particularly finite Shintani labels),
and the Galois attachment and local-global theorems, are distinct.

Write E'/E for the cyclic prime-degree CM step, p for its degree,
sigma for a generator, j for base change, and D for the kernel
of the finite-idele character mu composed with the norm.
All unitary groups are those of the definite standard spaces.
Use the local-adelic product decomposition over places of the
maximal real field, i.e. a conjugate pair of split CM places
is a single factor GL_n(E_w). At such a place the other
component is obtained by inverse conjugate transpose.
A matched place w is completely split in E'/E and mu is
trivial on the entire local multiplicative group E_w^times.
The latter is an essential part of the source IsMatched
hypothesis, not just triviality on local units.

## 1. Split matched Hecke functions

Fix a split matched place w and one place u above it.
Identify all p upstairs components above w with GL_n(E_w)
via the canonical local-field embeddings; sigma cyclically
permutes them. Write K=GL_n(O_w) and label the selected
component 0, the others in their cyclic order. For any
K-biinvariant compactly supported function f on GL_n(E_w)
use the matching function
\[
             f'(g_0,\ldots,g_{p-1})
                    =f(g_0)\prod_{i=1}^{p-1}1_K(g_i).
                                                               \tag{1}
\]
The polynomial root in the source IsNormRoot definition
is X on the selected place u and 1 at every other place,
including the conjugate of u. Over a conjugation-closed
collection of places take one representative w of each
pair, one selected u above it, and use X exactly on this
set of u. This is the adelic polynomial
\[
                         z=1+\mathbf1_V(X-1).
\]
Its coefficients are finite adeles (indeed integral),
even if the set of chosen places V is infinite.

For a unitary matrix gamma with characteristic polynomial
P, the twisted polynomial norm of z is X at all places
above the selected side and 1 on the conjugate side.
Thus its quotient by its adjoint evaluates to gamma
on this whole conjugation-closed collection; elsewhere
it evaluates to 1. The determinant condition holds for
a matrix M of *any* size killed by P. As P has invertible
constant coefficient, M is invertible, by the Bezout
identity between P and X. The determinant of z(M) is the
idele equal to det M at V and 1 elsewhere. Its norm to E
is killed by mu because mu kills each local component on
the selected side. The product assertion for a possibly
infinite set of components follows by the continuity of
mu and approximation of an idele by finite-support ideles.
Consequently this is a genuine IsNormRoot with values in D.

The root quotient a=z(gamma)/z(gamma)^* is gamma on the
selected upstairs component and 1 on all the other
components above w. The two matching conditions can now
be checked without classifying twisted conjugacy classes.
First, if gamma=j(h) is a base-changed matrix, its components
are all h, so f'(a)=f(h). Here N_sigma(a)=j(h).
Second, if delta is supported in (1) and
gamma=N_sigma(delta), then delta_i belongs to K for i!=0.
The selected component gamma_0 is delta_0 followed by a
product of those other integral components. Thus
gamma_0^{-1}delta_0 belongs to K, as do the other components
of a^{-1}delta. In particular a^{-1}delta is in the
upstairs maximal compact. Finally (1) is invariant under
twisted conjugation by that maximal compact: each left
and right factor in every coordinate is integral.
These are all the required matching assertions.

In the source normalization a spherical Hecke operator is
the sum over the right cosets of the minuscule double coset,
with each coset of K assigned measure one. Base and selected
upstairs completion are literally isomorphic and have the
same residue cardinality and uniformizer valuation, hence
their coset lists correspond. Left translation convolution
by the base Hecke function and the selected upstairs Hecke
function therefore sends (1) to the pair
\[
                (T_{w,i}f,\ (T_{w,i}f)\otimes 1_K^{\otimes(p-1)}).
                                                               \tag{2}
\]
The other factors do not change. The same conclusion holds
at the opposite CM place by inverse conjugate transpose:
the local-field isomorphism respects the conjugate double
coset, including its inverse and Haar normalization.
We never identify the i-th operator at a place with the
i-th operator at its conjugate by an unjustified equality.

On any collection X of matched split pairs, start with
the maximal compact indicator at all places of X.
Apply finitely many spherical operators and take their
linear span. All resulting functions are restricted
products (finite sums thereof), with the property (1)
in each matched pair. Every such pair matches by the same
universal polynomial z, and the class is closed under
each simultaneous operation (2). The identity indicators
are included. Thus the actual IsHeckeStableMatching
supplier is constructed, not assumed.

Source: StepMatchingPairs.lean 58–147, 147–212,
213–286, 326–469, 470–591.

## 2. Disjoint support and the exact transfer level

Suppose the source IsLocalMatching data are supplied on a
finite conjugation-closed collection Z (replace the input
set by its closure for the product decomposition).
Use its compact subgroups L_Z, L'_Z, K_Z on the supported
local groups, with L'_Z contained in K_Z contained in the
integral level there. The source retractions and embeddings
identify the local groups with their supported factors;
their preimages under the retractions place no conditions
on complementary factors. The pullback of L'_Z is L_Z,
L'_Z is stable under sigma, and the norm-one cocycles of
K_Z split in K_Z. For now retain these local hypotheses;
Z may be empty, when all of them are vacuous.

Let f be the nonzero base form of the indicated weight.
Its right stabilizer is open. Choose the compact base-change
level family m_u of Section 4 of the global norm-root chapter
below this stabilizer. More precisely intersect the base
stabilizer with the maximal compact before applying that
construction. This does not lose any maximal compact at
a place where f is spherical. The pullback of the product
of m_u fixes f. The family is stable under sigma and CM
conjugation, and at every place unramified in the Step
where f is spherical the family is maximal over that
place. All but finitely many factors are maximal:
the original stabilizer contains a compact open product
level and the step and mu are unramified away from finitely
many places.

Let X consist of all pairs outside Z at which the place is
split and matched and the m_u above it are maximal.
Let Y be all the remaining pairs outside Z. Put
\[
 \begin{split}
 N&=\prod_{u\mid X}K_u\times\prod_{u\mid Y}m_u,\qquad
 C_Y=\prod_{u\mid Y}m_u,\\
 \mathcal L&= L'_Z\times N,\qquad
 K_1= K_Z\times N .
 \end{split}                                                  \tag{3}
\]
Here products denote the restrictions on the indicated
factors; in particular C_Y imposes no condition outside Y
when used as a subgroup of the global group. The level
mathcal L is open compact, contained in K_1 and in the
global maximal compact, and sigma-stable. A norm-one
cocycle of K_1 is a tuple of such cocycles on Z, X, Y,
since sigma preserves each collection. Split it on Z by
the supplied local hypothesis and elsewhere by the matching
compact-level construction. The local splitting elements
lie in the compact level at every complementary place,
so they form a finite adelic element, not merely a product
in the unrestricted adeles. Thus the cocycle splits in K_1.

The pullback of mathcal L is precisely L_Z times the
pullback of N, and f is fixed by this latter subgroup
on the complementary factors: a base point trivial on
Z and in the pullback of N lies in the pullback of the
entire m-family. This proves the exact invariance needed
in the nonzero-trace argument. Above every unramified
spherical place outside Z, mathcal L contains the full
local maximal compact. Every such split matched place
lies in X.

Combine a supplied matching pair on Z, a pair from (1)–(2)
on X, and the matching indicator pair of C_Y on Y by
pointwise product. It is a matching pair at K_1.
Indeed, the support of its polynomial root condition at
each collection is supplied by the corresponding local
pair; a supported global polynomial is supported at each
collection after restriction, and its characteristic
polynomial remains sigma-fixed. Glue the three local
polynomial roots coefficientwise with the three disjoint
adelic idempotents; their degrees have a common finite
bound (the X root is linear, the Y root has degree at
most n-1 in X at almost all places, and the Z root is an
actual finite polynomial). On each collection the norm,
root quotient and matching equalities are just the
original ones. The determinant of the global polynomial
at an arbitrary matrix killed by P is the product of
the three supported determinant ideles, all in D.
The support implications give membership in each of
the three local compacts separately and hence in K_1.
This also proves twisted invariance under K_1.
It is important that this is a *disjoint-place pointwise
product*. No assertion is made that arbitrary overlapping
matching functions multiply by convolution.

These verify the conditions of IsTransferLevel in
PrimeDegreeTransfer.lean 440–594, including preservation
of spherical vectors at unramified places, and the
disjoint-product matching clause. The base-change family
is the one of the preceding global norm-root chapter;
no choice of f' or its eigencharacter is used to choose
the transfer level.

## 3. Operators and the trace identity at this level

At the actual finite-dimensional mathcal L-invariant form
spaces and their base pullback, a Hecke function on a
supported factor acts by the usual coset sum there.
The remaining factors act trivially on the vector if their
functions are level indicators, since the Haar measure
of the corresponding level is normalized to one.
On disjoint factors the coset sets are Cartesian products;
expanding the finite sum proves that the operator for the
pointwise product is the product of the respective
operators. This proves the operator-of-function relation
needed in the source IsHeckeFunctionRelation, both for
the original operators and for simultaneous products.
It also proves commutation across places.

Use the source family of local Hecke functions on Z and
its two hypotheses: the operators commute on each side,
and multiplication by any distinguished matching generator
carries the indexed matching family to itself, with the
same resulting index on both sides. The family of spherical
operators over X and all spherical operators on the
upstairs maximal split places off Z commute by the
ordinary spherical Hecke algebra. The split coset
identification (2) and disjoint-factor coset sums give
closure of the *actual* matching products under every
base generator and its selected upstairs counterpart.

For every such pair the trace formula (2) of the trace
transfer chapter now applies, with the same nonzero
scalar [K_1:mathcal L]/[j^{-1}K_1:j^{-1}mathcal L].
All its polynomial-root, rational descent, cocycle and
level hypotheses have been verified. Therefore it applies
to a polynomial in finitely many of the matching generators
times the distinguished local operator B,B', where B is
the chosen indexed local function and B' its mate.

The source HasNonzeroTraceAround hypothesis is exactly
sufficient to make the source trace nonzero on the
desired joint generalized eigenspace. Indeed form the
space W of base forms fixed by the pullback of N on
the complementary factors and lying in every specified
generalized spherical eigenspace of f there. It contains
f and is stable under the whole supported group on Z,
since that group acts only on the Z-factor. Its intersection
with the L_Z-fixed local generalized eigenspace is the
desired finite-dimensional joint generalized eigenspace
at the full pulled-back level. It is stable under B
by commutation. Apply HasNonzeroTraceAround to W.
For an empty Z take B=1 and there is no local label:
the trace is the positive dimension since the space
contains f. In the genuine-character case positivity of
the finite character operator supplies this hypothesis as
in the trace transfer chapter. Other special local matching
operators require their actual nonzero-trace input.

Here is a slightly more precise spectral extraction that
does not require sigma to permute the chosen local Hecke
operators. Let P,P' be simultaneous polynomial projectors
onto the matched eigencharacter in the two level spaces.
Such a common polynomial exists by the finite-dimensional
commutative Artinian algebra argument of the trace chapter:
use the direct sum of the two spaces, finite many separating
generators and Chinese remainders modulo the requisite
powers of maximal ideals. The trace identity says
tr(P' B' S) is nonzero, where S is the twisting operator.
Decompose the upstairs level space only by the joint
generalized characters of **all the spherical operators**
at maximal split places off Z. This family is permuted by
sigma, so S permutes these blocks. Both P' and B' preserve
every block because they commute with the spherical
operators. A block moved by S makes no contribution to
the trace. Hence on some sigma-fixed spherical block V
the trace of P' B' S is nonzero. In particular
P' B' V is nonzero. This image is preserved by the entire
commuting family of spherical and local operators, and
is contained in the generalized character selected by P'.
Simultaneous triangularization on that nonzero image
gives a common eigenvector g there. Its prescribed local
and matched spherical eigenvalues agree with those of f,
and its full spherical character is sigma-invariant.
No permutation property is required for the local
generalized characters, no assumption that B' is
invertible is made, and g belongs to the image of B'.

Above a matched w in X, the eigenvalues at the selected u
are those of f. The other places above w form one
sigma-orbit, and S intertwines their coset sums (the
integral compact levels and valuation-one double cosets
are transported exactly). Thus the invariant spherical
character gives the same eigenvalues at *every* place
above w. As the norm is unchanged, their unnormalized
monic Hecke polynomials are identical. At an unramified
spherical w outside Z, even if not matched, sphericity
of g follows directly from (3).

Finally g is a nonzero definite form of the base-changed
weight; its level is maximal off a finite set, and the
construction diagonalizes all spherical operators at the
split maximal places off Z. In particular g is an eigenform
in the source sense (at almost all prime-norm places);
ramified primes over the maximal real subfield can be
discarded as a finite set. The two conclusions just proved
are exactly IsWeakBaseChange. It follows that the source
exists_isWeakBaseChange_of_matching is supplied under its
stated local matching, commutation, multiplicative closure
and nonzero trace-around hypotheses. In particular the
empty-local-data weak base change needed for odd-rank
patching is supplied under the actual Step hypothesis.

## 4. Source and boundary

Pinned source: [readable revision 72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).
Besides StepMatchingPairs.lean above, see
Lib/GaloisRep/BaseChange/PrimeDegreeTransfer.lean 55–122,
196–234, 299–328, 362–439, 440–655, 699–end.
The operator argument replaces the abstract supported
retraction bookkeeping by the explicit direct product.

This closes the specific transfer levels and matching
products for the weak base-change theorem, relative to
the already proved norm-root/trace chapters. It supplies
weak transfer with no local labels and transfer of
prescribed local matching data when the latter are proved.
It does not yet supply the common finite Shintani characters,
other special local matching data, split-case attachment
or labelled local-global compatibility. No new Lean replay
or independent verification is asserted.
