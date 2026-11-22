# The actual ordinary Hecke determinant

## Result and scope

**Classification: closed subobligation inside W04.** For each original
fixed unitary Hecke datum, the ordinary modules now carry the required
action of the universal ordinary determinant ring. The construction
preserves the original type lattice, residual summand, weight coordinates,
unnormalized Hecke operators, uniformizers and auxiliary levels. Its
classical specializations separate vectors and have the local comparison
required at every auxiliary place.

The input is the actual datum of UnitaryHeckeData, not an arbitrary
finite free module with a postulated collection of Galois points. The
ordinary module and its good weight-zero points were constructed in the
[ordinary-module](selmer-integral-frontier-ordinary-diamond.md) and
[classical-control](selmer-integral-frontier-classical-control.md) notes.
The type lattice in that datum must satisfy its exact TypeForAlt
property. Existence of such a lattice is a separate supplier:
TTypeEx/PTypeEx, through NonzeroTypes. The adopted W05 theorem
does not by itself discharge that supplier.

No residual component is asserted to be nonzero. A zero component receives
the unique action on the zero module. This result does not supply the
remaining Taylor--Wiles level maps, their single exponent, patched
support, two-sided rigidity, or a uniform integral Selmer bound.

## 1. The frontier theorem

Fix the original Hida setting: an odd prime \(\ell\), a CM extension
\(L/F\) unramified at all finite places, the definite unitary group of the
original positive Hermitian space, the prescribed finite set \(S'\), the
coefficient DVR \(\mathcal O\), rank \(n\geq1\), the original residual
characters and local ordinary characters, and an original integral type
\(\tau_0\) satisfying TypeForAlt. Retain the original torus character
\(\theta\), its weight ring \(A=\mathcal O[[X_D]]\), its residual Hecke
eigenvalues \(a\), and its auxiliary set \(Q\).

Let \(M_K\) be the original ordinary residual module at any original
compact auxiliary level \(K\). When \(M_K\ne0\), let
\[
 T_K=A[H_i:i\in H.\mathrm{Op}]
       \ \subset\ \operatorname{End}_A(M_K)
\]
be the actual Hecke algebra, with exactly the original operator family.
Let \(B\), with universal pair \((D_B,\psi_B)\), be the original
universal ordinary determinant ring, and let \(\lambda:A\to B\) be its
map defined by the universal inertial characters.

**Theorem.** For every such datum and every \(K\) with \(M_K\ne0\), there
is a unique continuous surjective \(\mathcal O\)-algebra map
\[
                       f_K:B\longrightarrow T_K                 \tag{1}
\]
with the prescribed Frobenius characteristic polynomials and the
prescribed ordered ordinary characters. It satisfies
\(f_K\lambda(a)=a\,\mathrm{id}_{M_K}\). These maps give compatible
\(B\)-actions on the actual modules and their smooth auxiliary union.
Every nonzero vector of that union has a nonzero classical specialization
on which \(B\) acts through a character whose determinant is that of a
continuous semisimple \(n\)-dimensional Galois representation.

At every place above \(\ell\), this representation has the actual
ordered ordinary flag. At each original type place it has the prescribed
inertial representation and zero monodromy. At auxiliary places the
comparison is WOT for every allowed weak local correspondence. All
polynomial-law relations defining the original Pair hold integrally.

Only weight zero is needed. Its original Hodge--Tate labels are
\(0,\ldots,n-1\), at every embedding. The theorem does not assert the
source's larger base-change statement for arbitrary infinity types.

## 2. Ordinary vectors determine a single local Jacquet line

Work first over \(\mathbb C\), after the chosen identification
\(\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C\). For a place above
\(\ell\), write \(k=L_w\), \(N_0=N(\mathcal O_k)\), \(T_0=T(\mathcal O_k)\),
\(q=|\mathcal O_k/\mathfrak p_k|\), and retain the source uniformizer
\(\varpi\). Put
\[
 z=\operatorname{diag}(\varpi^{n-1},\ldots,1),\qquad
 U_z=\sum_{u\in N_0/zN_0z^{-1}}\sigma(uz).
\]
This is the unnormalized original operator. Let \(E\) be the part of a
smooth irreducible local component \(\sigma\) selected by the original
compact torus character and by the ordinary projector. Thus \(E\) is
\(N_0\)-fixed, \(U_z\) is invertible on \(E\), and its compact torus
character is \(\theta_x^{-1}\). The good point condition says that the
\(n\) coordinate characters of \(\theta_x\) are pairwise distinct.

The map \(q_N:\sigma\to\sigma_N\) to full upper-unipotent coinvariants is
injective on \(E\). Indeed, if \(q_N(v)=0\), write \(v\) as a finite sum
of \((\sigma(u)-1)w\). The increasing compact subgroups
\(N_m=z^{-m}N_0z^m\) exhaust \(N(k)\). For large \(m\), averaging over
\(N_m\) kills this sum. For \(N_0\)-fixed \(v\), coset multiplication gives
\[
 U_z^m v=[N_m:N_0]\,\sigma(z^m)e_{N_m}v.
\]
Hence a power of \(U_z\) kills \(v\), and \(v=0\).

Normalized Jacquet restriction is \(r_N=\delta_B^{-1/2}\sigma_N\).
Its selected compact-torus summand is finite dimensional by
admissibility. Choose a character quotient of this summand. Frobenius
reciprocity embeds \(\sigma\) in the normalized principal series
\(\chi_0\times\cdots\times\chi_{n-1}\), where
\(\chi_i|_{\mathcal O_k^\times}=\theta_{x,i}^{-1}\).
No ratio \(\chi_i/\chi_j\) is \(|\cdot|^{\pm1}\), because their unit
restrictions are distinct. Bernstein--Zelevinsky's irreducibility
criterion therefore makes this embedding an isomorphism.

The geometric lemma gives its Jacquet filtration with characters
\((\chi_{w(0)},\ldots,\chi_{w(n-1)})\), for permutations \(w\). Their
compact-torus restrictions are distinct. Taking a compact-character
summand is exact in characteristic zero, by averaging over a finite
quotient. The selected summand is consequently one dimensional.
Thus every original positive diagonal Hecke operator acts by a scalar
on \(E\). This is a statement about one local Jacquet line. It makes
no multiplicity-one assertion about a global type space.

For \(a_j=\operatorname{diag}(\varpi,\ldots,\varpi,1,\ldots,1)\), with
\(j\) copies of \(\varpi\), the exact scalar is
\[
 U_j=q^{j(n-j)/2}\prod_{i<j}\chi_i(\varpi),\qquad 1\leq j\leq n.
                                                               \tag{2}
\]
Indeed the index in the unnormalized sum is
\(\delta_B(a_j)^{-1}=q^{j(n-j)}\), while \(a_j\) acts on unnormalized
coinvariants by
\(\delta_B(a_j)^{1/2}\prod_{i<j}\chi_i(\varpi)\).
The two factors give (2). Put \(U_0=1\) and \(b_i=U_{i+1}/U_i\). Then
\[
                    b_i=q^{(n-1)/2-i}\chi_i(\varpi).             \tag{3}
\]

## 3. Classical eigencharacters separate the actual Hecke algebra

The definite unitary quotient has discrete automorphic spectrum; at
fixed compact level and infinity type the function space is finite
dimensional. The original type has open kernel, so it factors through
a finite group and is unitarizable after complexification. Finite-order
torus characters remain unitary under \(\iota\).

Decompose the classical function space into its automorphic
isotypic summands, retaining every multiplicity space. Spherical Hecke
operators outside \(S'\) act by scalars on the local spherical factor.
The preceding argument proves scalar action for all the original
ordinary operators on each summand's selected ordinary part. They act
as the identity on the remaining multiplicity factors. No normality
claim for a ramified \(U\)-operator is used. The original residual
idempotent selects a direct sum of these eigenspaces.

If \(t\in T_K\) is nonzero, choose \(v\in M_K\) with \(tv\ne0\).
The proved good weight-zero density gives a point \(x:A\to\mathcal O_E\)
where \((tv)_x\ne0\). Exact classical control and the preceding scalar
decomposition give an eigencharacter
\(\phi:T_K\to\overline{\mathbb Q}_\ell\), extending \(x\), with
\(\phi(t)\ne0\). Let \(\Sigma\) be the family of eigencharacters so
obtained, together with a choice of a contributing global constituent.
It separates \(T_K\).

There are two useful integral facts. First, \(T_K\) is a finite
\(A\)-module: it is an \(A\)-submodule of the finite module
\(\operatorname{End}_A(M_K)\). It is complete and compact, with its
induced adic topology. Second, it is local with the original residue
field. In the finite residual algebra, every original generator has
its prescribed generalized eigenvalue \(a_i\); hence its selected
factor has exactly that one residue character. These facts also show
that the \(A\)-adic and maximal-ideal-adic topologies agree.

Each \(\phi\in\Sigma\) is continuous. Its values lie in a finite
coefficient extension: use finitely many \(A\)-module generators of
\(T_K\). They are integral over \(x(A)\), so their images lie in its
integer ring. Reduction to its finite residue field has maximal kernel
in the local ring \(T_K\); therefore it kills \(\mathfrak m_{T_K}\).
The images of finitely many generators of this ideal have positive
valuation, proving continuity.

## 4. Actual Galois representations at the good points

### 4.1 The exact definite base change

The unitary group is compact at every real place, so every infinity
component occurring here is discrete series and Labesse's condition
\((*)\) is automatic. Also \([F:\mathbb Q]\geq2\): otherwise \(L\) would
be an imaginary quadratic extension of \(\mathbb Q\) unramified at all
finite places, which is excluded by its discriminant.

Labesse, Corollary 5.3, therefore supplies a base change
\[
                         \Pi=\boxplus_{\alpha}\Pi_\alpha
\]
with discrete conjugate-self-dual blocks, exact at split and
unramified places and with the matching infinity infinitesimal
character. This precise corollary has no added finite-place
quasi-split or parity hypothesis; it applies to the given inner form.
The original arithmetic group and its finite levels have not changed.

Mœglin--Waldspurger write each discrete block as
\(\operatorname{Speh}(\tau_\alpha,d_\alpha)\). At one of the good
places above \(\ell\), (2) identifies the base change with a principal
series whose cuspidal support has \(n\) distinct unit characters.
If \(d_\alpha>1\), the local support of that Speh block contains
\(d_\alpha\) unramified twists of each member of the cuspidal support
of \(\tau_{\alpha,w}\). Uniqueness of cuspidal support first makes
those members characters, and then gives a repeated unit character.
This is impossible. Hence every \(d_\alpha=1\).

The conclusion is that each \(\Pi_\alpha\) is cuspidal. The global
isobaric sum may have several blocks, which must all be retained.

### 4.2 Rank-dependent normalization

Put \(m_\alpha=\dim\Pi_\alpha\). At each infinity embedding its
infinitesimal-character entries form a subset of
\[
                   z_s=(n-1)/2-s,\qquad 0\leq s<n.
\]
Define
\[
 \pi_\alpha=\Pi_\alpha|\det|^{(m_\alpha-n)/2}.
                                                               \tag{4}
\]
Its entries are \((m_\alpha-1)/2-s\); they are distinct and lie in the
correct rank-\(m_\alpha\) algebraic coset. It is regular algebraic
and polarized. For the source's real-sign convention, take the
polarizing character on \(F\) to be
\(\delta_{L/F}^{\,m_\alpha}|\cdot|^{m_\alpha-n}\).
The quadratic character is trivial after the norm pullback, and its
value at \(-1\) at every real place is \((-1)^{m_\alpha}\).

The adopted W05 theorem applies to every \(\pi_\alpha\). Write
\(r_\alpha\) for its continuous semisimple Galois representation and
put \(r_\phi=\bigoplus_\alpha r_\alpha\). The normalization identity
\[
 \operatorname{algNorm}_{m_\alpha}(\pi_\alpha)
       =\Pi_\alpha|\det|^{(1-n)/2}                              \tag{5}
\]
shows that the direct sum has exactly the original rank-\(n\)
Frobenius polynomials and local parameters. Its labeled Hodge--Tate
weights are \(0,\ldots,n-1\), with each label accounted for once.

At places away from \(\ell\) the full classical correspondence gives
the local comparison block by block and hence for their direct sum.
At a place above \(\ell\), the good principal-series parameter has
zero monodromy; so do all its blocks. The already adopted
monodromy-dominance theorem gives full Frobenius-semisimplified
compatibility there. Distinct inertial characters make each inertial
summand one dimensional; Frobenius is scalar on each. Thus
Frobenius semisimplification introduces no ambiguity at these places.

Outside \(S'\), including nonsplit places, the original representation
is unramified and Labesse's unramified comparison applies. Therefore
\(r_\phi\) factors through the original group \(G_0\).
Conjugate self-duality, the normalization (5), and semisimplicity give
\[
                  r_\phi^c\simeq r_\phi^\vee\varepsilon^{1-n}.
                                                               \tag{6}
\]
This supplies the nondegenerate pairing required by IsForm.
That predicate imposes no symmetry condition on the pairing.

If \(r_\phi\) is irreducible, the direct sum has one block and that
block has rank \(n\); (4) then has no twist. This gives exactly the
source's conditional cuspidality assertion. No irreducibility of
the global representation has been presumed.

### 4.3 The arbitrary weak correspondences and the original type

For any allowed weak correspondence \(\mathrm{rc}\), put
\(y=\mathrm{rc}(\operatorname{algNorm}\sigma_w)\). If the source guard
Gd holds, \(y\) is toral with zero monodromy. The already proved
local preimage/uniqueness/injectivity transport identifies \(y\)
with the classical parameter of the same local representation.
Our full classical comparison therefore gives the demanded equality.
Without the guard, the actual Weil--Deligne representation itself
is the existence witness. This is WOT; the argument applies to
the whole isobaric direct sum and does not require its cuspidality.
At \(\ell\) the identical guarded transport preserves the period
models and the Hodge--Tate labels already audited under W05.

At a prescribed type place, apply the exact TypeForAlt property
of \(\tau_0\) to the nonzero global type vector and the classical
correspondence. It gives zero monodromy and the specified finite
Teichmüller inertial characters. In characteristic zero this is the
actual diagonal inertial representation. In particular every element
of the original subgroup
\(I_u\cap\bigcap_i\ker\bar\chi_i\) acts trivially.
This uses the supplied type, not an assumed construction of it.

## 5. Continuous integral local characters and actual ordinary flags

All the \(U_j\) are invertible on the finite free \(A\)-module \(M_K\).
For \(j<n\) this follows from the commuting invertible ordinary product
\(U_z=\prod_{j=1}^{n-1}U_j\); the last operator \(U_n\) is invertible
central translation. Cayley--Hamilton expresses each inverse in
\(A[U_j]\), since its determinant is an \(A\)-unit. Thus each \(U_j\)
is a unit of the actual subalgebra \(T_K\).
Set \(b_i=U_{i+1}U_i^{-1}\) in \(T_K^\times\).

Local reciprocity gives a unique continuous character
\(\xi_{v,i}:G_{L_w}\to T_K^\times\) characterized on its Weil
abelianization by
\[
 \xi_{v,i}(\operatorname{Art}^{-1}y)=\theta_i(y)^{-1}
 \ (y\in\mathcal O_{L_w}^{\times}),\qquad
 \xi_{v,i}(\operatorname{Art}^{-1}\varpi)=b_i .
\]
For clarity, its extension from the valuation factor
\(\mathbb Z\) to \(\widehat{\mathbb Z}\) exists because
\(T_K^\times\) is profinite: every element defines a continuous
map from the procyclic completion. Define
\[
                         \psi_{v,i}=\xi_{v,i}\varepsilon^{-i}.  \tag{7}
\]
These are the exact source characters. On units,
\(\psi_{v,i}\varepsilon^i\theta_i=1\), while on the original
uniformizer
\[
                 \prod_{i=0}^{j-1}\psi_{v,i}\varepsilon^i=U_j.  \tag{8}
\]
The original IsTheta equality identifies their inertial restrictions
with the original \(\kappa_{v,i}\). It also preserves the prescribed
finite torsion restrictions: a torsion class in the local
abelianization has zero valuation in the torsion-free group
\(\widehat{\mathbb Z}\), and hence lies in the unit factor.
The original IsRes.unif and its
successive quotients identify their residual unramified values;
together with the inertial values they give
\(\overline{\psi}_{v,i}=\bar\psi_{v,i}\) on the full local group.

At a good point \(\phi\), \(\xi_{v,i}\) has finite inertia and
Hodge--Tate weight zero. Thus \(\psi_{v,i}\) has weight \(i\).
Its Weil--Deligne Frobenius value is \(b_iq^i\), which by (3) is
\(\chi_i(\varpi)q^{(n-1)/2}\), the exact normalized local parameter
of \(r_\phi\). This calculation uses
\(\mathrm{WD}(\varepsilon)(\mathrm{Frob}_{\mathrm{geom}})=q^{-1}\).
It does **not** identify the value of the \(\ell\)-adic cyclotomic
character on a local uniformizer with \(q^{-1}\) at \(\ell\).

Here is a direct proof of the flag. After a finite extension killing
inertia, use the filtered crystalline module with descent data.
Twist first by \(\psi_{v,0}^{-1}\). Its Hodge--Tate labels are all
nonnegative and its designated one-dimensional Frobenius summand has
Newton number zero. The induced filtration on this line has
nonnegative Hodge number; weak admissibility gives the opposite
inequality, so it has Hodge number zero. Every labeled summand
therefore has filtration jump zero. Undoing the twist identifies
the line with its filtration and descent with the crystalline
module of \(\psi_{v,0}\).
Full faithfulness supplies the corresponding Galois subrepresentation.
Descent is respected, so it is defined over the original local field.

Pass to the quotient, whose labels are \(1,\ldots,n-1\), and repeat
after twisting by \(\psi_{v,1}^{-1}\), then by the successive
characters. This constructs the ordered flag with graded characters
\(\psi_{v,0},\ldots,\psi_{v,n-1}\). Only weak admissibility and full
faithfulness are needed: each rank-one admissible representation
has already been constructed in (7).

## 6. A determinant over the integral Hecke algebra

Embed \(T=T_K\) into \(\prod_{\phi\in\Sigma}\overline{\mathbb Q}_\ell\).
This is a continuous injection from a compact space into a Hausdorff
space, hence a homeomorphism onto a closed image.

For every \(g\in G_0\), the tuple of the \(j\)-th coefficients of
\(\det(X-r_\phi(g))\) varies continuously with \(g\). At the original
Frobenius elements it is the image of a coefficient of
\[
 P_w(X)=\sum_{j=0}^n(-1)^j q_w^{j(j-1)/2}T_{w,j}X^{n-j}.
                                                               \tag{9}
\]
Here \(T_{w,0}=1\), and the source's arithmetic Frobenius is inverted.
The original set of split places outside \(S'\), with all its
Frobenius representatives, is dense in \(G_0\) by Chebotarev.
Closedness now puts every coefficient tuple in \(T\), continuously.
No uniform continuity estimate across \(\phi\) was assumed.

To descend a determinant, rather than only a trace, use the integral
Amitsur identity
\[
 \det\!\left(1-\sum_i t_iA_i\right)
   =\prod_{[w]\ {\rm primitive\ cyclic}}
                   \det(1-t_w A_w).                            \tag{10}
\]
This is a formal power-series identity; a coefficient of total
degree at most \(n\) uses only finitely many words. Over \(\mathbb Q\),
take logarithms and collect traces by primitive cyclic words:
an orbit of length \(d\), repeated \(r\) times, contributes \(1/r\).
Both sides have integral coefficients in the entries of universal
matrices, so torsion-freeness of that universal polynomial ring
proves the integral identity. This proof leaves no division by
\(n!\) in (10).

Apply (10) to \(A_i=r_\phi(g_i)\). Its right side is an integral
polynomial in the already descended characteristic coefficients
of the words \(g_w\). It therefore defines the determinant of
every finite group-algebra sum over \(T\). Well-definedness,
homogeneity, naturality under every \(T\)-algebra, and
multiplicativity are polynomial identities. They hold after
every \(\phi\) and hence over \(T\), because \(\Sigma\) separates
coefficients. We obtain a unique continuous degree-\(n\)
determinant
\[
                           D:T[G_0]\longrightarrow T .          \tag{11}
\]
It specializes to \(\det r_\phi\). The same finite integral
identities prove the required continuity for tuples of group
elements. The argument is valid when \(\ell\leq n\).

## 7. The original deformation relations and the action of \(B\)

The reduction of (9) is the prescribed residual polynomial, by
IsRes.frob. Continuity, Frobenius density, and (10) show that the
reduction of \(D\) is the original residual determinant as a
polynomial law.

At every \(\phi\), (6) proves polarization. For the ordinary relation,
the flag from §5 makes the ordered product
\[
       \prod_{i=0}^{n-1}\bigl(r_\phi(g_i)-\psi_{v,i}(g_i)\bigr)
                                                               \tag{12}
\]
zero: the rightmost factor maps the full space into the preceding
flag step, and the remaining factors lower the step successively.
Thus the required traces after multiplication by arbitrary
group elements vanish. At every type place §4.3 makes
\(r_\phi(g)-1=0\) for \(g\in I_u\cap\bigcap_i\ker\bar\chi_i\).
The corresponding trace relation also vanishes.

Separation by \(\Sigma\) proves all these identities over \(T\).
Together with (7)--(8), continuity and the residual conditions,
they are exactly the fields of the original Pair, with
no condition omitted or weakened. Universality gives (1).
The universal property of the inertial weight ring gives
\(f_K\lambda(a)=a\).

The map is surjective. Its image contains \(A\); (9) gives every
spherical generator because \(q_w\) is a unit at \(\ell\); and
(8) gives every ordinary generator. These are exactly the generators
of \(T_K\). All images and inverses used in (8) are integral units.
Uniqueness follows from Frobenius density, (10), and local reciprocity.

For an inclusion of original levels, restriction of endomorphisms
maps the larger-level Hecke algebra to the smaller-level one and
preserves (7)--(9). Uniqueness therefore makes the \(B\)-actions
compatible. Auxiliary translations commute with the fixed original
Hecke family and give the action on the smooth union.

Given a nonzero vector in that union, choose a good point detecting
it and then a nonzero automorphic projection as in §3. Let \(Y\) be
the auxiliary representation generated by this projection. At
each auxiliary factor it is an isotypic sum of copies of the
chosen local component; all global multiplicities are retained.
The specialization map is auxiliary-equivariant and \(B\)-scalar
through \(\phi f_K\), and its determinant is (11). The comparison
from §4.3 is exactly the WOT required in LevPtAlt.
This proves the stated classical supplier for the original modules.

## 8. Dependencies and remaining frontier

This construction uses the two preceding actual-module theorems,
the already adopted full W05 local/global theorem and its weak
correspondence transport, and four primary inputs checked below.
It replaces a postulated AutomorphicHeckeSet by a construction
at the good weight-zero points actually needed in this argument.

| Primary input | Exact part used |
| --- | --- |
| Bernstein--Zelevinsky, *Induced representations of reductive p-adic groups I*, Ann. Sci. ENS 10 (1977), 441--472, [author PDF](https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/BZ-induced-1.pdf) | Proposition 2.3: adjunction/admissibility; geometric lemma 2.12; uniqueness of support §4.1; irreducibility Theorem 4.2 |
| Labesse, *Changement de base CM et séries discrètes*, in *On the Stabilization of the Trace Formula*, vol. 1 (2011), 429--470, [author PDF](https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf) | §5 hypothesis \([F:\mathbb Q]\geq2\), author pp.41--43; compact infinity implies \((*)\); Corollary 5.3, exact split/unramified comparison |
| Mœglin--Waldspurger, *Le spectre résiduel de GL(n)*, Ann. Sci. ENS 22 (1989), 605--674, [published PDF](https://www.numdam.org/item/10.24033/asens.1595.pdf) | Main theorem, pp.605--606, and normalized Speh induction, §I.1.1 |
| Colmez--Fontaine, *Construction des représentations p-adiques semi-stables*, Invent. Math. 140 (2000), 1--43, [author PDF](https://webusers.imj-prg.fr/~pierre.colmez/CF.pdf) | Author §3.4, pp.21--22, weak admissibility; Proposition 4.2, p.23, exact full faithfulness and stability under subquotients |

The certificate authenticates the exact pinned Lean interfaces and
the source ranges used for independent review. It also hashes the
downloaded primary PDFs and records their reviewed pages. This is
a proof in standard mathematics with cited theorems, not a new Lean
compilation or a computational proof.

The next arithmetic targets remain the exact integral type-existence
supplier, the original auxiliary spherical/Iwahori maps with one
exponent valid for all Taylor--Wiles levels, and the patched support
argument needed for two-sided rigidity. Finite freeness and this
determinant action alone imply no uniform integral torsion bound.
The RH specialization retains all these fields, ranks and lattices.
