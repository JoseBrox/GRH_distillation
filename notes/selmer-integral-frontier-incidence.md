# A short proof of the local prime inclusion used in patching

## Result and scope

The difficult reducible case of the actual characteristic-prime propagation
argument uses a local matrix-incidence lemma. The following proof replaces
that source algebra by the geometry of a projective space. It works directly
over an arbitrary Noetherian regular local ring, hence also over the complete
mixed-characteristic rings occurring in the source. It does not transfer
irreducibility from a generic fibre to a completion.

This proves the precise local algebra conclusion used by the source. The
construction of the arithmetic presentation, its independent first-order
relations, and the patched automorphic modules remains a separate obligation.
The whole Selmer nodes remain open.

## Matrix-incidence lemma

Let \((P,\mathfrak m,k)\) be a Noetherian regular local ring of dimension
\(d\). Let \(g\geq1\), let \(Z=(z_{ij})\) be a \(g\times g\) matrix,
and let \(y=(y_j)\) be a column vector. Suppose all \(g^2+g\) entries belong
to \(\mathfrak m\), and their classes in \(\mathfrak m/\mathfrak m^2\)
are linearly independent over \(k\). Put
\[
 I=((Zy)_1,\ldots,(Zy)_g),\qquad J=I+(\det Z).
\]
Then \(\sqrt J\) is prime and
\(\dim(P/\sqrt J)\leq d-g\). Consequently, if \(\mathfrak p\) is a prime
containing \(I\), some \(y_j\notin\mathfrak p\), and
\(\dim(P/\mathfrak p)\geq d-g\), then
\[
 \mathfrak p=\sqrt J.
\]
In particular, \(\mathfrak p\subseteq\mathfrak q\) for every prime
\(\mathfrak q\supseteq J\).

### Proof

Over \(\operatorname{Spec}P\), introduce the projective incidence scheme
\[
 Y=\{(Z,y,L): L\subset P^g\text{ is a line},\ ZL=0,\ y\in L\}
       \subset\mathbb P^{g-1}_P.
\]
Here “line” means the tautological line subbundle in the projective bundle;
the notation \(Z,y\) denotes the given functions on the base. Thus \(Y\)
is a closed subscheme of projective space, and its map to the base is proper.
On the chart in which the \(c\)-th coordinate of \(L\) is \(1\), with
the other coordinates \(u_j\), it is cut out by
\[
 z_{ic}+\sum_{j\ne c}u_jz_{ij}=0\quad(1\leq i\leq g),
 \qquad y_j-u_jy_c=0\quad(j\ne c).                         \tag{1}
\]
These equations imply \(Zy=0\) and \(\det Z=0\), so the map factors
through \(\operatorname{Spec}(P/J)\). It is surjective on points. Over a
residue field, if \(y\ne0\), take its span; if \(y=0\), the determinant
condition supplies a nonzero kernel vector of \(Z\).

Every closed point of \(Y\) maps to the closed point of \(\operatorname{Spec}P\),
because a proper morphism is closed. At such a point, the polynomial chart
over \(P\) has a regular local ring of dimension \(d+g-1\). The classes
coming from \(\mathfrak m/\mathfrak m^2\) remain independent after residue
field extension: a regular system of parameters of \(P\), followed by
parameters of the polynomial closed fibre, is a regular system of parameters
of that chart local ring. This uses neither perfection nor separability of
the residue field.

The \(2g-1\) equations in (1) have independent linear parts there. For the
first \(g\) equations, the coefficients of the distinct variables
\(z_{1c},\ldots,z_{gc}\) give an identity matrix. For the remaining
\(g-1\) equations, use \(y_j\), \(j\ne c\). All other terms use the
remaining independent base coordinates. Quotienting a regular local ring by
these independent parameters gives a regular local ring of dimension
\(d-g\).

Thus every closed local ring of \(Y\) is regular of dimension \(d-g\).
Every point of a Noetherian scheme specializes to a closed point, and a
localization of a regular local ring is regular. Hence \(Y\) is regular.
Its finitely many irreducible components are therefore disjoint and open as
well as closed. Every component meets the closed fibre, again by properness.
That fibre is the connected space \(\mathbb P^{g-1}_k\), so there can be
only one component. Therefore \(Y\) is irreducible.

The proper surjective image \(\operatorname{Spec}(P/J)\) is irreducible,
so \(K=\sqrt J\) is prime. Moreover, \(\dim Y=d-g\), as its closed local
rings have this dimension, and a closed surjective map of Noetherian spaces
cannot increase dimension. For clarity, a chain of irreducible closed sets
in the target lifts to such a chain in the source: choose an irreducible
component mapping onto the largest set, and then successively choose
components in its inverse images. Closedness and the finiteness of the
components ensure that each choice maps onto the specified irreducible set.
It follows that \(\dim(P/K)\leq d-g\).

Finally, in \(\operatorname{Frac}(P/\mathfrak p)\), the nonzero vector
\(y\) lies in the kernel of \(Z\), so \(\det Z\in\mathfrak p\).
Thus \(K\subseteq\mathfrak p\). If this inclusion were strict, a prime
chain would give
\[
 \dim(P/\mathfrak p)+1\leq\dim(P/K)\leq d-g,
\]
contrary to the dimension hypothesis. This proves the assertion.

The case \(g=1\) reduces to \(J=(z_{11})\), and the proof includes it.
For \(g=0\), the determinant is \(1\), so there is no prime containing
\(J\); the corresponding source implication is vacuous. No assumption on
the characteristic is used, and no assertion that \(J\) itself is radical
is needed.

## Exact application to the reducible deformation presentation

The relevant source is
`PatchingModules.SelmerScaling.CotangentIndependentOfResidues`, 74–211,
under `Development.AutomorphicArithmetic.AutomorphicVarieties`, at
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
Its theorem `presOut1` has the following data.

Let \(\mathcal O\) be a complete discrete valuation ring. Let \(B\) be a
complete Noetherian local \(\mathcal O\)-algebra with the same residue
field, and let \(A=B\oplus N\) be a finite commutative \(B\)-algebra with
injective scalar map, where \(N^2\subseteq\mathfrak m_B\). Let
\(\mathfrak r\subseteq B\) be generated by the products of elements of
\(N\). Choose \(X_1,\ldots,X_D\in\mathfrak m_B\) and generators
\(m_1,\ldots,m_g\) of \(N\). Set
\[
 H=\pi B+\mathfrak m_B^2+\mathfrak r.
\]
The source supplies the following first-order presentation:
\[
 \mathfrak m_B=(X_1,\ldots,X_D)+H,
 \qquad
 \sum_j\Bigl(\sum_a c_{ija}X_a\Bigr)m_j\in HN,
                                                               \tag{2}
\]
where the \(g^2\) row vectors \((\bar c_{ija})_a\) are independent over
the residue field.

Under these exact assumptions, the source conclusion is:
\[
 \begin{gathered}
 \dim(B/\mathfrak p)\geq1+D,\quad
 \mathfrak r\nsubseteq\mathfrak p,\quad
 \mathfrak r\nsubseteq\mathfrak q\ \text{or}\
       \operatorname{Ann}_B N\subseteq\mathfrak q
 \end{gathered}
 \quad\Longrightarrow\quad \mathfrak p\subseteq\mathfrak q          \tag{3}
\]
for prime ideals \(\mathfrak p,\mathfrak q\) of \(B\).

Here is a short derivation using the lemma. The complete algebra \(A\)
is a quotient of
\(P=\mathcal O[[X_1,\ldots,X_D,Y_1,\ldots,Y_g]]\), with
\(Y_j\mapsto m_j\). Indeed, the decomposition \(A=B\oplus N\), (2),
and \(N^2\subseteq\mathfrak m_A^2\) give the required surjection on
cotangent spaces; completeness and Nakayama give the ring surjection.
Write the relations (2) as \(\sum_j\zeta_{ij}m_j=0\), with
\(\zeta_{ij}=\sum_a c_{ija}X_a-w_{ij}\) and \(w_{ij}\in H\).
Since \(H\) maps into \(\pi A+\mathfrak m_A^2\), lift \(w_{ij}\) to
\(v_{ij}\in\pi P+\mathfrak m_P^2\), and put
\[
 z_{ij}=\sum_a c_{ija}X_a-v_{ij}.
\]
The independence in (2) says exactly that the entries \(z_{ij}\) and
\(Y_j\) have independent cotangent classes in \(P\). Their products
\(ZY\) vanish in \(A\).

Choose primes \(\mathfrak p',\mathfrak q'\) of \(A\) above
\(\mathfrak p,\mathfrak q\). Integrality preserves the quotient
dimensions. Some \(m_j\notin\mathfrak p'\), for otherwise all products
from \(N\) would lie in \(\mathfrak p\). The determinant trick applied
to the relations gives \(\det\zeta\in\operatorname{Ann}_B N\).
Consequently \((\det\zeta)\mathfrak r=0\); either alternative in (3)
therefore gives \(\det\zeta\in\mathfrak q\). Apply the incidence lemma
to the inverse images of \(\mathfrak p',\mathfrak q'\) in \(P\), whose
dimension is \(1+D+g\). It gives \(\mathfrak p'\subseteq\mathfrak q'\),
and contraction proves (3).

This matches `AlgebraTools.CaDetLocus`, 10–15, and its exact consumer
`AlgebraTools.CaDetCore`, 9–48. The construction of the surjection and the
matrix is the bounded source range 77–158 of `CotangentIndependentOfResidues`;
the determinant and prime contraction are 158–211. The ultimate local
consumer is `PatchingModules.AutomorphicDetection.GalOut`, 16–37.

## Remaining arithmetic obligation

The independence of all \(g^2\) coefficient rows in (2) is substantive. It
implies \(g^2\leq D\) and is not a consequence of ordinary pointwise
crystallinity, of characteristic-zero Selmer vanishing, or of the existence
of a finite number of automorphic points. In the actual source it is part of
`Ctx.Pres`, `PatchingModules.SelmerScaling.SelmerSpannedByKappaLaurent`,
166–171. The next task is to reconstruct its supplier from the first and
second cohomological bounds and the higher-order deformation relations, and
to identify where the actual automorphic modules supply the dimension
\(1+D\) in (3).

## References and verification

The primary references checked for the general algebraic facts are The Stacks
Project, [Tag 00NP](https://stacks.math.columbia.edu/tag/00NP) (regular local
rings are domains), [Tag 00NQ](https://stacks.math.columbia.edu/tag/00NQ)
(independent parameters and regular quotients),
[Tag 02IL](https://stacks.math.columbia.edu/tag/02IL) (closed specializations),
[Tag 02IT](https://stacks.math.columbia.edu/tag/02IT) (regularity checked at
closed points), and [Tag 01W1](https://stacks.math.columbia.edu/tag/01W1)
(proper maps are closed). The proof of the incidence lemma above supplies
the special geometry; none of these references is being used as a citation
for the unproved arithmetic presentation.

The companion certificate records the pinned source ranges, primary-reference
snapshots, exact symbolic chart pivots, and small finite-field incidence
checks. These computations check the local equations and edge cases; the
proof for all sizes and all residue fields is the argument above. No Lean
build or whole-node closure is claimed. Counts remain **RH 6/9; GRH 17/31**.
