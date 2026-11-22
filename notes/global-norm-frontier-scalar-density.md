# Equality of the original local densities for scalar pairs

## Result and scope

The original scalar-pair identifications preserve the discriminant module
of the **actual modified frame lattice**. Consequently its residue Gram
corank, and hence its primitive local density, is unchanged. Together
with the previously reconstructed primitive-frame count, this proves
both clauses of the source's \(\mathrm{FamilyVolumeFourth}\), with
constant one for the original ranks. In particular it supplies the
original local assertion \(\mathrm T_1\).

The equality clause is the new result here. The primitive count and its
source application were already proved in
`paper/sections/recovered/70-md-section.tex`; the separate signed-density
checkpoint refines their error bound. No global period norm estimate,
archimedean orbital bound, other local assertion, or whole RH/GRH node is
claimed. The proof never replaces a designated split-level tuple by its
unmodified counterpart.

## 1. The original local data

Let \(F\) be a nonarchimedean local field of characteristic zero, \(E/F\)
an unramified quadratic field or the split algebra \(F\times F\), and
\(O\) its maximal integral algebra. The involution is denoted by a bar.
Let \(V\) be a nondegenerate Hermitian \(E\)-module of rank \(N\),
with the form linear in its first argument.

For \(i=1,2\), let \(\Lambda_i\) be self-dual \(O\)-lattices and let
\(f_i,f'_i\) be the original frames of length \(a=r+1\). Their internal
Gram matrices are \(-T_i ee^*\) and \(-T'_i ee^*\), where \(e\) is
the last standard vector. Put
\[
 Z_i=\bigl(h(f'_{i,b},f_{i,c})\bigr)_{c,b},\qquad
 G_i=\operatorname{Nm}(\det Z_i)
       -T_iT'_i\operatorname{Nm}(\det Z_i^{\circ}),
 \tag{1}
\]
where \(Z_i^\circ\) deletes the last row and column; its determinant is
one if \(a=1\). The original hypotheses say that \(Z_i\) is invertible
over \(E\) and \(G_i\ne0\).

There are two possible actual frame lattices:
\[
 M_i=
 \begin{cases}
  \displaystyle\sum_b Of_{i,b}+\sum_b Of'_{i,b},
       &\text{without a designated split level},\\[2mm]
  \displaystyle\sum_b Of_{i,b}
     +\sum_b O\,\frac{f'_{i,b}-f_{i,b}}{\varpi_s},
       &\text{at the designated split level}.
 \end{cases}                                                     \tag{2}
\]
Here \(\varpi_s\) is the original generator stored in the split data.
It is kept distinct from the arbitrary uniformizer used to define the
density. The original genericity hypothesis is precisely that the
displayed \(2a\)-tuple is \(E\)-independent, lies in \(\Lambda_i\), and
is primitive:
\[
                  \Lambda_i\cap E M_i=M_i.                        \tag{3}
\]
At the designated level, the congruence
\(f'_i-f_i\in\varpi_s\Lambda_i\) is part of the original term data.

Write \(X_i\) for the span of the **first \(r\)** vectors of \(f_i\),
and \(X'_i\) for that of \(f'_i\). Write \(P_i=EM_i\), so that
\(P_i\) is the span of **all \(r+1\)** vectors in both frames. Set
\[
 W_i=P_i^\perp,\qquad K_i=\Lambda_i\cap W_i,\qquad
 Q_i=X_i^\perp/X_i,\qquad Q'_i=(X'_i)^\perp/X'_i.                  \tag{4}
\]
The frames make \(X_i,X'_i\) totally isotropic. Let \(L_i\subset Q_i\)
be the image of \(\Lambda_i\cap X_i^\perp\), and define \(L'_i\)
similarly.

An original scalar pair gives Hermitian \(E\)-linear isomorphisms
\(\phi:Q_1\to Q_2\), \(\phi':Q'_1\to Q'_2\), with the following
properties:

1. For each \(w\in W_1\) there is \(w_2\in W_2\) whose two quotient
   classes are \(\phi([w])\) and \(\phi'([w])\).
2. \(\phi(L_1)=L_2\) and \(\phi'(L'_1)=L'_2\).
3. At a designated split level, \(\phi'\times\phi\) carries the
   original congruence graph onto its counterpart. The graph consists
   of pairs \(([u'],[u])\) with integral representatives
   \(u'\in(X'_i)^\perp\), \(u\in X_i^\perp\), and
   \(u-u'\in\varpi_s\Lambda_i\).

The scalar-pair definition has additional marked-vector and determinant
conditions. They are retained in the application, although the three
properties above suffice for the density conclusion.

## 2. The complementary Hermitian spaces are isometric

The Gram matrix of the raw tuple \((f_i,f'_i)\) is
\[
 B_i=\begin{pmatrix}-T_i ee^*&Z_i\\
                       Z_i^*&-T'_i ee^*\end{pmatrix},\qquad
                      \det B_i=(-1)^aG_i.                         \tag{5}
\]
For example, the determinant identity follows by applying the
rank-two determinant lemma to the invertible matrix with off-diagonal
blocks \(Z_i,Z_i^*\) and zero diagonal blocks. The relevant inverse
entries are the two conjugate cofactors
\(\det Z_i^\circ/\det Z_i\). This proves (5) without division by
\(T_i\) or by a residue characteristic.

The element \(G_i\) is fixed by the involution, hence belongs to \(F\).
Its being nonzero therefore makes it a unit of \(E\), including when
\(E\) is split. Thus \(P_i\) is nondegenerate. Changing from the raw
tuple to (2) is invertible over \(E\), so it does not change \(P_i\).
Consequently \(W_i\) is nondegenerate, has rank \(N-2a\), and
\(W_i\cap X_i=0\).

The vector \(w_2\) in property 1 is unique: the difference of two
choices lies in \(W_2\cap X_2=0\). Denote it by \(\alpha(w)\).
Uniqueness makes \(\alpha:W_1\to W_2\) \(E\)-linear. Since the
quotient maps preserve the Hermitian forms, so does \(\alpha\).
Its kernel is zero by nondegeneracy of \(W_1\). The spaces have the
same rank, so \(\alpha\) is onto; in the split algebra this assertion
is made in each of the two \(F\)-components. The inverse therefore
also intertwines both quotient maps. The assertion includes
rank-zero complements.

## 3. The same map preserves the complementary lattices

First suppose there is no designated split level. For \(w\in K_1\),
property 2 gives integral representatives of the two classes of
\(w_2=\alpha(w)\):
\[
 u=w_2+\sum_{j<r}a_j f_{2,j}\in\Lambda_2,\qquad
 u'=w_2+\sum_{j<r}b_j f'_{2,j}\in\Lambda_2.                        \tag{6}
\]
Their difference lies in \(\Lambda_2\cap P_2=M_2\). The raw frame
tuple is the basis in (2), so its independent coordinates show that
all \(a_j,b_j\) belong to \(O\). Hence \(w_2\in\Lambda_2\).

Now suppose the designated split level is present. The pair of
classes of \(w\) lies in the first congruence graph, using the same
integral representative twice. Property 3 provides representatives
(6) with
\[
                            u-u'\in\varpi_s\Lambda_2.
 \tag{7}
\]
Extend \(a_j,b_j\) by zero in the last frame position and put
\(g_{2,j}=(f'_{2,j}-f_{2,j})/\varpi_s\). Dividing (7) by the
**original** \(\varpi_s\) gives
\[
 \frac{u-u'}{\varpi_s}
    =\sum_j\frac{a_j-b_j}{\varpi_s}f_{2,j}
       -\sum_j b_jg_{2,j}
       \ \in\ \Lambda_2\cap P_2=M_2.                             \tag{8}
\]
Primitivity of the modified tuple now forces
\(b_j,(a_j-b_j)/\varpi_s\in O\), hence \(a_j,b_j\in O\) and again
\(w_2\in\Lambda_2\). This step uses the congruence graph, not merely
the two separate quotient-lattice images.

Apply the same arguments to \(\alpha^{-1}\), using the equalities
in properties 2 and 3 in reverse. We have proved the exact lattice
isometry
\[
                              \alpha(K_1)=K_2.                    \tag{9}
\]

## 4. Primitive complements have the same discriminant module

We record the elementary lattice argument to avoid imposing an
isometry on the original frame lattices themselves. If \(M\) is a
primitive nondegenerate sublattice of a self-dual \(O\)-lattice
\(\Lambda\), put \(K=\Lambda\cap(EM)^\perp\) and let
\[
 M^\#=\{x\in EM:h(x,M)\subset O\},\qquad D(M)=M^\#/M.
\]
Both \(M\) and \(K\) are primitive direct summands as \(O\)-modules:
the quotient by either is torsion-free, and \(O\) is a discrete
valuation ring or a product of two such rings. They need not be
orthogonal direct summands of \(\Lambda\).

Self-duality identifies \(\Lambda\) with its conjugate dual. Because
\(M\) is a module direct summand, restriction to its conjugate dual
is onto, with kernel \(K\). Identifying that dual with \(M^\#\)
by the nondegenerate form gives
\[
                 \Lambda/(M+K)\ \simeq\ M^\#/M.                  \tag{10}
\]
The same argument, now using primitivity of \(K\), gives
\[
                D(M)\ \simeq\ \Lambda/(M+K)\ \simeq\ D(K).        \tag{11}
\]
These are finite \(O\)-module isomorphisms. No assertion about the
sign of their discriminant pairings is needed.

Apply (11) to \(M_1,M_2\) and use (9). It follows that
\[
                             D(M_1)\simeq D(M_2).                 \tag{12}
\]
When \(E\) is a field, for any uniformizer \(\varpi\) the residue
corank of the Gram matrix of a lattice \(M\) is
\(\dim_{O/\varpi O}D(M)/\varpi D(M)\). This is the elementary
cokernel calculation, or the Smith normal form of its integral Gram
matrix. In the split case use either component: the two Gram matrices
are conjugate transposes, so their coranks agree. Equation (12) proves
equality of the two original residue coranks.

## 5. Exact density conclusion and its consumer

The previously reconstructed formula, with the original denominator,
is
\[
 \delta(M_i)=\prod_{j=N-m-c_i+1}^{N}(1-\eta^j q^{-j}),\qquad
 m=2r+2,\quad q=\#k_F,\quad
 \eta=\begin{cases}1&\text{split},\\-1&\text{inert}.\end{cases}      \tag{13}
\]
Thus \(c_1=c_2\) proves \(\delta(M_1)=\delta(M_2)\).
The density is formed over the maximal algebra \(O\), exactly as in
the original definition. At a designated split place the separate
congruence order is nonmaximal; no assertion about self-dual lattices
or discriminant modules over that order has been substituted here.

For the original ranks, \(N=k+m-1\), \(m=2r+2\ge2\), and
\(d_0=k-m\ge4\). The already proved count bound is
\[
                   |\delta(M)-1|\le2q^{-d_0}\le m q^{-d_0}.        \tag{14}
\]
Equations (13)--(14) give both clauses of
\(\mathrm{FamilyVolumeFourth}(M,r,k,N,1)\) for every actual local
model. Therefore the original assertion \(\mathrm T_1(D,1)\) holds.
The stronger numerical restriction used when this assertion is
assembled with the other local estimates remains unchanged.

## Source correspondence and reproducibility

All source bytes below are pinned to
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The adjacent certificate records their blob and bounded-excerpt hashes.

| Source | Lines | Role |
|---|---:|---|
| `FractionFieldToGenericStalkAlgebraMapEq` | 10--26, 31--59, 76--80 | Maximal algebra, involution, original split generator, distinct nonmaximal order, actual local-field hypothesis |
| `LinQRawRange` | 12--19, 43--78 | Hermitian form, self-duality, primitivity, two distinct spans and quotient lattices |
| `LinQRawRange` | 105--120, 133--174 | Actual modified tuple, genericity, full scalar-pair conditions, split congruence graph and density |
| `LocalBesselAndTopKernel` | 87--96, 149--167 | Both clauses of the exact consumer and original all-local-model assertion |
| `Formalism.LocalRingCardinality.Params` | 6--46 | Exact original ranks and their numerical range |

Run `python3 scripts/check_global_norm_frontier_scalar_density.py --offline`.
The checker authenticates these sources and performs exact determinant,
complement-quotient, residue-corank and split-generator checks. Negative
controls show why primitivity, self-duality and the congruence condition
cannot be dropped from the indicated steps. These checks supplement the
general proof above; they are not a full Lean build.
