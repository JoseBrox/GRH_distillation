# Integrability of the original isotropic lattice count

## Result and exact scope

For a Hermitian lattice of dimension at least three over a CM field,
the **full original count of nonzero isotropic lattice vectors** is
integrable on its arithmetic unitary quotient. No bound on the index
of the vector in its saturated line is needed. Its first moment is a
finite sum of partial Dedekind zeta values at \(N-1>1\).

This supplies the two analytic inputs retained in
[`cusp-counting-mean.md`](cusp-counting-mean.md): finite Haar volume
and integrability of one count. It also proves the scaling identity
for every radius. The count is the full count in the pinned source,
not a replacement by primitive vectors or vectors of bounded index.

The result applies once the original geometric component, lattice,
positive norm and measure have been identified with the indicated
arithmetic quotient. **That geometric identification, the arithmetic
model and the signed boundary intersection limit remain open.** No
whole proof-map node is completed: the counts remain RH \(6/9\),
GRH \(17/31\). Classical reduction theorems below are cited inputs;
the source audit authenticates statements and definitions and does not
claim a Lean build.

## 1. The arithmetic theorem

Let \(E/F\) be a CM extension, put \(f=[F:\mathbf Q]\), and let
\((V,h)\) be a nondegenerate Hermitian space of dimension \(N\ge3\)
over \(E\). Let \(L\subset V\) be a full \(\mathcal O_E\)-lattice.
Write

\[
 \mathbf G=\operatorname{Res}_{F/\mathbf Q}U(V,h),\qquad
 G=\mathbf G(\mathbf R)=\prod_{\sigma:F\hookrightarrow\mathbf R}U(h_\sigma).
 \tag{1}
\]

Let \(\Gamma\) be any subgroup of finite index in
\(\{g\in U(V,h)(F):gL=L\}\). Fix a positive definite Euclidean norm
on \(V\otimes_{\mathbf Q}\mathbf R\). Then \(\Gamma\backslash G\)
has finite positive Haar volume. With its normalized Haar probability
measure \(\nu\), define

\[
 N_t(g)=\#\{v\in L\setminus\{0\}:h(v,v)=0,\ \|g^{-1}v\|<t\}.
 \tag{2}
\]

**Theorem.** Every \(N_t\), \(t>0\), is integrable, and

\[
   \int N_t\,d\nu=t^{2f(N-1)}\int N_1\,d\nu.             \tag{3}
\]

The same statements hold for the special unitary group and a subgroup
of finite index in its lattice stabilizer. All lattice stabilizer
indices, component weights and Haar normalizations are retained.

Each count is finite at every point, since the transformed lattice is
discrete and the norm ball is bounded. It is measurable as a countable
sum of indicators. If \(h\) is definite at even one real place of
\(F\), no nonzero \(E\)-rational vector can be isotropic: its image
at that embedding is nonzero. Thus \(N_t=0\). The same conclusion
holds if \(h\) is globally anisotropic despite being indefinite at
every real place. We now prove the theorem in the remaining case.

## 2. Arithmetic quotients and finitely many cusp lines

The derived subgroup of \(\mathbf G\) is semisimple. Its connected
center is a product, after restriction of scalars, of norm-one tori
of the CM extension; its real points are compact. Consequently
\(\mathbf G\) has no nontrivial rational character. The lattice
stabilizer is arithmetic in the faithful rational representation on
\(V\), viewed as a rational vector space; a subgroup of finite index
is arithmetic too. Borel--Harish-Chandra, Theorem 9.4, gives
unimodularity and finite covolume. The same argument for \(SU(V,h)\)
is immediate from semisimplicity.

Arithmetic reduction theory gives finitely many \(\Gamma\)-orbits
of rational isotropic \(E\)-lines. Indeed, the stabilizer of one
such line is a rational parabolic subgroup, and unitary Witt
extension makes the rational action transitive. Apply
Platonov--Rapinchuk, Theorem 5.4, to
\(\mathbf G(\mathbf Q)/\mathbf P(\mathbf Q)\). Passing to a
subgroup of finite index only splits each orbit into finitely many.
For \(SU\), first extend the line isometry in \(U\), then correct
its determinant on a nonisotropic line in the nondegenerate
orthogonal complement of a hyperbolic plane. This complement has
dimension \(N-2\ge1\), and the correcting scalar has norm one.
Thus rational transitivity and the same parabolic argument hold.

Choose representatives \(\ell_j=Ee_j\), with
\(e_j\in L\setminus\{0\}\), for these finitely many cusp lines.
Set

\[
 J_j=\{a\in E:ae_j\in L\},\qquad
 U_j=\{u\in E^\times:\gamma e_j=ue_j
                     \text{ for some }\gamma\in\Gamma_{\ell_j}\}.
 \tag{4}
\]

Here \(J_j\) is a nonzero fractional ideal. Since every such
\(\gamma\) preserves \(L\cap\ell_j=J_je_j\), one has
\(uJ_j=J_j\), hence \(u\in\mathcal O_E^\times\).

### The unit image has finite index, including at finite level

Fix one representative \(e=e_j\). Complete it to a hyperbolic pair
\((e,f_0)\) with \(h(e,f_0)=1\), and write
\(V=Ee\oplus V_0\oplus Ef_0\). Let \(P_e,P_{f_0}\) be the
two coordinate projections. Choose a positive integer \(m\) such
that \(mP_eL,mP_{f_0}L\subset L\). For a unit
\(u\equiv1\pmod{m\mathcal O_E}\), put

\[
 T_u=\operatorname{diag}(u,1_{V_0},\bar u^{-1}),\qquad
 T_u-1=(u-1)P_e+(\bar u^{-1}-1)P_{f_0}.                    \tag{5}
\]

Both coefficients on the right belong to \(m\mathcal O_E\), as
do those for \(T_u^{-1}-1\). Thus \(T_uL=L\), and \(T_u\) is
unitary. The units congruent to one modulo \(m\) have finite index
in \(\mathcal O_E^\times\), because the residue ring is finite.
The map \(u\mapsto T_u\) is a homomorphism. Its inverse image of
the prescribed finite-index subgroup \(\Gamma\) still has finite
index. This proves

\[
                       [\mathcal O_E^\times:U_j]<\infty.  \tag{6}
\]

For \(SU\), restrict this construction to real units
\(u\in\mathcal O_F^\times\): then
\(\det T_u=u/\bar u=1\). These real units have finite index in
\(\mathcal O_E^\times\). Indeed, for every CM unit \(u\), all
conjugates of \(u/\bar u\) have absolute value one. An algebraic
integer with that property is a root of unity: the integer
coefficients of the polynomials of its powers are bounded, so only
finitely many powers occur. The map \(u\mapsto u/\bar u\) therefore
has finite image and kernel \(\mathcal O_F^\times\). This proves
(6) in the special unitary case as well. No finite-level index has
been set equal to one.

## 3. One vector orbit has finite first moment

For \(e\ne0\) isotropic, let \(H_e\subset G\) fix \(e\), and let
\(\Gamma_e=\Gamma\cap H_e\). The algebraic vector stabilizer is
an extension of \(U(V_0)\) by its unipotent radical, with the
splitting \(A\mapsto\operatorname{diag}(1,A,1)\). For \(SU\)
the reductive factor is \(SU(V_0)\). These groups are connected
and have no rational characters; the unipotent factor contributes
none, and the unitary factor has the same norm-one center as above.
\(\Gamma_e\) is arithmetic by intersection. Borel--Harish-Chandra,
Theorem 9.4, therefore gives finite Haar volume for
\(\Gamma_e\backslash H_e\).

It is essential here to fix the **vector**. Its line stabilizer
has an additional \(\operatorname{Res}_{E/F}\mathbf G_m\)
factor and does not satisfy this character argument.

Choose Haar measures on \(G\) and \(H_e\), and the compatible
quotient measure \(d\bar g\) on \(H_e\backslash G\). Nonnegative
unfolding, valid before knowing convergence, gives

\[
 \begin{aligned}
 A(e;t)
 &:=\int_{\Gamma\backslash G}
       \sum_{v\in\Gamma e}\mathbf1_{\{\|g^{-1}v\|<t\}}\,d\nu(g)\\
 &=\frac{\operatorname{vol}(\Gamma_e\backslash H_e)}
          {\operatorname{vol}(\Gamma\backslash G)}
       \int_{H_e\backslash G}\mathbf1_{\{\|g^{-1}e\|<t\}}\,d\bar g.
 \end{aligned}                                                    \tag{7}
\]

The quotient maps transitively to the product of the nonzero complex
null cones by \(H_eg\mapsto g^{-1}e\). Every embedding of a nonzero
\(E\)-vector is nonzero, so partial-zero strata do not enter. The
invariant measure on this product is, up to a positive finite
constant,

\[
 \omega=\prod_\sigma\frac{dS_\sigma}{\|\nabla q_\sigma\|},
 \qquad q_\sigma(v)=h_\sigma(v,v).                         \tag{8}
\]

Here the surface measure and gradient use the same Euclidean
coordinates. Coarea proves invariance because the unitary group
preserves both \(q_\sigma\) and ambient real volume. The radial
density is a constant times \(r^{2N-3}\,dr\), so a bounded norm
ball has finite measure. Uniqueness of invariant Radon measure on
the transitive homogeneous space identifies the quotient measure
with (8). Thus \(0<A(e;1)<\infty\).

For every \(a\in E^\times\), the vector stabilizers of \(e\)
and \(ae\) are **exactly the same groups**, including their
arithmetic subgroups. Keep these same Haar measures in (7).
For multiplication \(T_a\) by \(a\), the coarea measure satisfies
\(\omega(T_aB)=|N_{E/\mathbf Q}(a)|^{N-1}\omega(B)\):
at each embedding the Jacobian is \(|\sigma(a)|^{2N-2}\). Consequently, with \(s=N-1\) and
\(k=2f(N-1)\),

\[
 A(ae;t)=t^k|N_{E/\mathbf Q}(a)|^{-s}A(e;1).              \tag{9}
\]

This is a change of variables on the same quotient, with no unknown
relative stabilizer normalization. It holds for any fixed positive
norm; multiplication by \(a\) need not preserve that norm.

## 4. Sum every vector orbit by an ideal series

The vector orbits over the cusp line \(Ee_j\) are indexed by
\((J_j\setminus\{0\})/U_j\). For \(a\in J_j\setminus\{0\}\),

\[
       \mathfrak a=a\mathcal O_EJ_j^{-1}\subset\mathcal O_E,
       \qquad N\mathfrak a=|N_{E/\mathbf Q}(a)|/NJ_j.       \tag{10}
\]

These are exactly the integral ideals in the ideal class
\([J_j]^{-1}\). Every such ideal has
\([\mathcal O_E^\times:U_j]\) preimages modulo \(U_j\): its
generators form one free orbit under \(\mathcal O_E^\times\).
Tonelli, (9) and (10) give the exact first moment

\[
 \int N_t\,d\nu
 =t^k\sum_j A(e_j;1)\,[\mathcal O_E^\times:U_j]\,
             (NJ_j)^{-s}\,\zeta_{[J_j]^{-1}}(s),
 \qquad s=N-1>1.                                         \tag{11}
\]

The partial zeta function sums \((N\mathfrak a)^{-s}\) over
nonzero integral ideals in the indicated class. It converges for
real \(s>1\). An elementary comparison suffices: each rational
prime has at most \(2f\) prime ideals above it, each of norm at
least that prime, so its Euler product is bounded by
\(\zeta(s)^{2f}<\infty\). There are finitely many cusp lines,
and every other factor in (11) is finite. This proves the theorem.

Changing a representative \(e_j\) to \(be_j\) replaces \(J_j\)
by \(b^{-1}J_j\), leaves its ideal class and unit image unchanged,
and multiplies \(A(e_j;1)\) by \(|N(b)|^{-s}\). The factors
cancel in (11), as required. The condition \(N\ge3\) ensures
convergence of the ideal series and, for \(SU\), supplies the
nonzero complement for determinant correction. This argument does
not assert convergence in dimension two.

## 5. Actual quotient, finite support, and downstream use

If the original space is \(\Gamma\backslash G/K\), where \(K\)
is compact and preserves the positive norm, lift to normalized Haar
measure on \(\Gamma\backslash G\). The count is right
\(K\)-invariant, so its mean is unchanged. For finitely many
arithmetic components, apply (11) separately and combine with the
original normalized component weights. Orbifold stabilizer factors
belong to the measure identification and are not discarded.

The same integrability conclusion covers a bounded nonnegative
finite-adelic test weight with compact support, provided its rational
vector weight is \(\Gamma\)-invariant. Its support lies in
\(m^{-1}\widehat L\) for some positive integer \(m\), and its
bound \(C\) gives domination by \(C N_t\) for the lattice
\(m^{-1}L\), which has exactly the same stabilizer as \(L\).
Haar invariance and the coarea argument then supply the same scaling
law for this weighted mean. This assertion requires bounded weights
and fixed compact support; it says nothing about arbitrary unbounded
vector weights. The original packing argument continues to use its
original unweighted count.

In the cusp estimate, \(N\ge3j+1\), \(j\ge1\), so \(N\ge4\)
and the theorem applies. With the retained lattice/norm and Haar
identifications, it removes **both** the independent finite-covolume
and one-integrable-count requirements from the previous Haar lemma.
The counting-to-logarithmic-mean argument then gives its original
bound, including \(C_u=3\), without a numerical estimate for any
covolume, number of cusp lines, unit index or zeta value. Their
finiteness is enough because the counting moment is bounded by the
existing packing and scaling argument.

The actual geometric equality
\(\operatorname{mean}_X(g)=\int g\,d\nu\) must still be proved
for the original construction. This theorem also does not prove
existence of that construction over the integers or identify its
signed boundary term with a limit of these means.

## 6. Verified source correspondence

All source paths below are under
`lean/src/GroundTheory/HeightsAndTheta/Heights/` at
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The checker records each full blob hash and each bounded excerpt hash.

| Source | Lines | Role |
|---|---:|---|
| `FiniteCovolume/Objects.lean` | 57–68, 99–123 | Product of archimedean unitary groups, inverse action, fixed positive majorant norm. |
| same | 129–135, 162–176, 180–207 | Full integral lattice, lattice stabilizer, line index, archimedean arithmetic subgroup and full vector count. |
| `FiniteCovolume/StatementsVectorOrbits.lean` | 15–27, 45–48 | Congruence units and the original scalar lift to the lattice stabilizer; (5) supplies it directly. |
| `FiniteCovolume/Statements.lean` | 15–28, 43–52, 74–80 | Arithmetic covolume, bounded-line-index scaling, and one-vector unfolding. |
| `StabilizerCovolume/WeightedScaling.lean` | 16–37 | Positive weighted norm; the source integrability contract still restricts vector line index. |
| `StabilizerCovolume/StatementsMeanLogPlus.lean` | 25–29, 44–66 | The actual full count, normalized geometric mean, integrability requirement and scaling target. |

The distinction in the last two rows matters: unrestricted multiples
have unbounded line index. Their convergence is supplied here by
the ideal series (11), rather than by treating the bounded-index
contract as if it covered the full count. No assertion is made here
about how other source modules discharge that difference.

## 7. Primary references and verification

1. Armand Borel and Harish-Chandra, *Arithmetic Subgroups of Algebraic
   Groups*, Annals of Mathematics **75** (1962), 485–535, Theorem 9.4,
   printed p. 522. [Original paper scan](https://www.mathi.uni-heidelberg.de/~wienhard/retreat10/references/borel_harishchandra_2.pdf).
   PDF page 39 was inspected, including the proof for groups with
   unipotent radical; the theorem applies to the vector stabilizer,
   not only to reductive groups. Full PDF SHA-256:
   `7bc28593402ef043d9df14a9ac1a7875bec4b4054be0cd523081bf5e470da762`.
2. Vladimir Platonov and Andrei Rapinchuk, *Algebraic Groups and Number
   Theory*, Academic Press, 1994, Theorem 5.4, pp. 258–259.
   [Author-hosted book](https://uva.theopenscholar.com/files/andrei-rapinchuk/files/agnt_english.pdf).
   The spread on PDF page 136 was inspected. The theorem gives the
   finite rational parabolic double-coset set; its arithmetic subgroup
   notation is \(G_{\mathcal O}\), not the real group. Full PDF SHA-256:
   `75f1fff8a4b712f00d0c7db5790951c3c242c070b8cdd70380a2d04a398f4aa3`.

The reproducible checker authenticates the pinned source against the
compressed atlas, authenticates both primary PDFs, and checks exact
Witt-matrix, norm-exponent, representative-change and ideal Euler
factor identities. Those finite checks support the audit; the
unfolding, reduction theory and convergence arguments are mathematical
proofs, not conclusions inferred from numerical samples.
