# Integral coefficient freeness from the abelian quotient

## Result and exact scope

The formal Hodge module on a geometric boundary fibre admits a shorter
coefficient-freeness proof. The proper abelian part is the tangent space
of a universal vector extension, identified directly through
first-infinitesimal rigidifications. Its functorial Dieudonné crystal
provides a module free over Witt vectors. The toric part is handled by a
three-step filtration whose outer terms are scalar extensions of
projective integral lattices.

This proves the following supplier, including ramified coefficient primes:

> Let a semiabelian geometric fibre have its prescribed action of the
> full ring of integers \(\mathcal O_E\). Suppose its line bundle is the
> pullback of a line bundle on the abelian quotient which induces an
> isomorphism with the dual abelian variety, with the prescribed Rosati
> adjunction. Then the formal Hodge module is projective over
> \(k\otimes_{\mathbf Z}\mathcal O_E\). If its characteristic polynomials
> are those of the regular representation repeated \(r\) times, it is
> free of rank \(r\). The same assertion lifts to the original local
> stalk when the underlying module and its formation under residue-field
> base change are the prescribed ones.

The full argument is given below. Its exact coordinate comparison
identifies the module; it is not
an assumption that an unspecified formal object equals de Rham cohomology.

This is a proved replacement for the coefficient-freeness calculation
once the stated geometric fibre data have been constructed. It does not
construct that boundary model, identify its conjugate filtration, or
evaluate its integral complex multiplication determinant. No existing
RH or GRH node is completed by this result.

## 1. The proper module is the actual tangent module

Let \(k\) be algebraically closed of characteristic \(p>0\), let \(B/k\)
be an abelian variety, and let \(M\) be a rigidified line bundle with
\(\lambda_M:B\longrightarrow B^\vee\) an isomorphism.
Write \(\mathcal P_M(x,y)\) for its Poincaré biextension, and choose a
formal frame \(e(x,y)\), equal to the prescribed trivialization on both
axes. The source adjunction has precisely the convention
\[
  \alpha_a:\mathcal P_M(ax,y)\longrightarrow\mathcal P_M(x,\bar a y),
  \qquad
  \alpha_a(e(ax,y))=u_a(x,y)e(x,\bar a y).
\]
Let \(V=\operatorname{Lie}B\), let \(\rho(a)\) be its tangent action, and
write \(b_a\) for the matrix of the mixed bilinear coefficient of \(u_a\).

Mazur–Messing identify the universal vector extension of \(B^\vee\) with
rigidified extensions of \(B\) by \(\mathbf G_m\): a rigidification is a
pointed section on the first infinitesimal neighbourhood of the zero
section, not a splitting as group schemes. The construction commutes
with arbitrary base change and is functorial in \(B\).
Use \(\lambda_M\) to identify the parameter space with \(B\).

A tangent point is an extension with parameter \(\epsilon v\), together
with a rigidification reducing to the identity. On the first
neighbourhood in the second variable, it has the unique form
\[
             e(\epsilon v,y)(1+\epsilon\lambda(y)),
             \qquad \lambda\in V^*,\quad \epsilon^2=0.
\]
This is the differential of the local trivialization of the universal
extension obtained by restricting the frame to that first
neighbourhood; consequently it is a linear coordinate identification.

The endomorphism \(a\) on the parameter space acts by pulling the
rigidification back through \(\bar a\), then through \(\alpha_a^{-1}\).
Since
\[
   u_a(\epsilon v,y)=1+\epsilon(b_a^tv)(y)
\]
on this neighbourhood, the new coordinates are exactly
\[
             (v,\lambda)\longmapsto
       \bigl(\rho(a)v,\rho(\bar a)^t\lambda-b_a^tv\bigr).
\]
This matches the actual source action, including the transpose and
minus sign. No analytic logarithm, exponential, division by \(2\), or
division by \(p\) is involved. In particular the argument applies at
\(p=2\).

The associated Dieudonné crystal is functorial in endomorphisms.
Evaluation on the Witt thickenings and passage to their inverse limit
give a finite free \(W(k)\)-module whose reduction is this Lie algebra.
Equivalently, one can use the contravariant crystal of \(B[p^\infty]\),
with the action pulled back by \(\bar a\); this is the same action on
the universal extension after the identification by \(\lambda_M\).
No simultaneous lift of \(B\) and its endomorphisms to \(W(k)\) is
asserted or needed.

The source's trivial-translation-kernel condition is sufficiently
strong here. It is tested on every coefficient ring, not just
geometric points. For an abelian variety it says that the group-scheme
kernel of \(\lambda_M\) is trivial. The resulting proper monomorphism
between abelian varieties of equal dimension is an isomorphism.
The verified source ranges for this assertion and the frame convention
are recorded in §6.

## 2. Why the Witt module is free over each ramified factor

Put \(W=W(k)\) and \(R=W\otimes_{\mathbf Z}\mathcal O_E\).
First decompose \(\mathcal O_E\otimes\mathbf Z_p\) into its completed
local rings. The maximal unramified subfield in each local field splits
over \(W\), because \(k\) is algebraically closed. Each remaining
totally ramified factor is obtained by adjoining a root of an Eisenstein
polynomial. The result is a product of discrete valuation rings \(R_i\),
with \(p=u_i\varpi_i^{e_i}\).

If \(D\) is finite free over \(W\), its summand \(D_i\) has no
\(\varpi_i\)-torsion: such torsion would give \(p\)-torsion.
A finite torsion-free module over a discrete valuation ring is free.
Thus
\[
       D/pD=\prod_i D_i/pD_i
\]
is projective over
\[
       C=k\otimes_{\mathbf Z}\mathcal O_E
          =\prod_i C_i,\qquad C_i\simeq k[t]/(t^{e_i}).
\]
The factors may initially have different ranks. Freeness over each
factor is not yet freeness of one common rank over \(C\).

The regular characteristic-polynomial identity supplies that missing
rank equality. If the rank on \(C_i\) is \(r_i\), multiplication by
\(a\in\mathcal O_E\) has characteristic polynomial
\[
                    \prod_i(X-\tau_i(a))^{e_i r_i}.
\]
For any selected prime above \(p\), choose \(a\) by the Chinese
remainder theorem to be zero at the other primes and a nonzero
generator of the selected finite residue field. Its distinct embeddings
into \(k\) give distinct nonzero roots. Comparing multiplicities with
the \(r\)-fold regular representation gives \(e_i r_i=e_i r\), and
hence \(r_i=r\), on every factor.

The use of the full ring of integers is essential to this proof:
torsion-free modules over a nonmaximal order need not be projective.

## 3. The torus is removed by a filtration

Let \(q:G\to B\) be the prescribed equivariant semiabelian quotient.
Its torus has cocharacter lattice \(\Lambda\), and the tangent sequence is
\[
       0\longrightarrow T=k\otimes_{\mathbf Z}\Lambda
          \xrightarrow{j}V=\operatorname{Lie}G
          \xrightarrow{P}U=\operatorname{Lie}B
          \longrightarrow0.
\]
Suppose the prescribed rigidified line on \(G\) is \(q^*M\).
The corresponding biextension is then the pullback from \(B\times B\).

The comparison between two rigidified adjunctions is a global unit on
\(G\times G\) equal to one on both axes. The units-on-products theorem
makes this unit equal to one. Its hypotheses hold because a geometric
semiabelian fibre is smooth and connected. This argument is on the
geometric group variety; it does not apply that reducedness theorem to
the nonreduced coefficient algebra \(C\).

Write the comparison of formal frames as
\[
                 e_G(x,y)=\ell(x,y)^{-1}e_B(qx,qy).
\]
The scalar \(\ell\) equals one on both axes, and the adjunction relation
is therefore
\[
       u_a^G(x,y)
         =u_a^B(qx,qy)\frac{\ell(x,\bar a y)}{\ell(ax,y)}.
\]
Writing \(Z\) for its mixed bilinear coefficient gives, simultaneously
for every \(a\),
\[
          b_a+\rho(a)^tZ-Z\rho(\bar a)=P^tc_aP.
\]
This is the same gauge identity as the pinned source, derived directly
from the same pullback line bundle. The change
\[
                   (v,\lambda)\longmapsto(v,\lambda+Z^tv)
\]
maps the action with bilinear term \(P^tc_aP\) to the original action.

In these coordinates, projection onto \(T^*\) is
\((v,\lambda)\mapsto j^*\lambda\), with conjugate dual action on \(T^*\).
Its kernel is \(V\oplus P^*U^*\). The map
\[
              (v,P^*\mu)\longmapsto(Pv,\mu)
\]
from this kernel onto the abelian formal module has kernel \(T\oplus0\).
These are exact sequences of \(C\)-modules. The successive quotients
are \(T\), the abelian formal module, and the conjugate dual of \(T\).

The lattice \(\Lambda\) is a projective \(\mathcal O_E\)-module.
Indeed, it is finite and free over \(\mathbf Z\); nonzero
\(\mathcal O_E\)-torsion would, after multiplication by the integral
adjugate of that algebraic integer, give nonzero integer torsion.
The same proof applies to its integer dual with conjugate action.
Base change makes the two toric quotients projective over \(C\).
The middle quotient is projective by §§1–2. Both sequences split as
\(C\)-modules, so the whole formal Hodge module is projective.
The regular character then gives its common rank.

This proof avoids the long source estimate involving kernels of every
nonzero endomorphism and their isogeny degrees. It does not discard
ramified multiplicity, use a possibly degenerate residue trace pairing,
or replace a lattice by its semisimplification.

## 4. Return to the same local lattice

Let \(S\) be an original local stalk and \(H\) the prescribed finite free
\(S\)-module, with its actual \(\mathcal O_E\)-action. Assume that forming
its formal frame commutes with passage to the geometric closed fibre,
as in the source's germ base-change comparison.

Geometric-fibre freeness descends to the residue field. To see this
without an equivariant lift, work on each Artin local factor of
\(\kappa(S)\otimes\mathcal O_E\). After extension to an algebraic closure,
freeness of rank \(r\) implies that the minimal number of generators
before extension is \(r\). Choose that many generators modulo the
maximal ideal, use Nakayama to get a surjection from a free module, and
compare dimensions after scalar extension to see that it is an
isomorphism. The residue fields of these factors are separable over
\(\kappa(S)\), since they arise by tensoring finite fields over
\(\mathbf F_p\).

Now lift a residue-field coefficient basis to \(H\).
The induced map
\[
               (S\otimes_{\mathbf Z}\mathcal O_E)^r\longrightarrow H
\]
is a map between free \(S\)-modules of the same rank and is an
isomorphism modulo the maximal ideal. Its determinant is a unit.
This proves freeness on this very stalk, without changing its lattice.

In the source construction, the Hodge lattice projects onto the actual
Lie lattice, and its inverse image under the second summand is the
actual dual Lie lattice. Those integral equalities are separately
verified in the source ranges below. The argument here fits that
existing lattice once its germ and fibre comparisons are in place.
It does not infer those lattice equalities from a generic-fibre
isomorphism, and it changes no metric or different normalization.

## 5. Diagnostic: the regular character alone is insufficient

Take \(\mathcal O_E=\mathbf Z[i]\) and \(p=2\). Then
\[
         \mathbf F_2\otimes\mathbf Z[i]
            \simeq \mathbf F_2[\eta]/(\eta^2),\qquad \eta=i-1.
\]
On \(H=\mathbf F_2^2\), let \(i\) act as the identity.
Every \(a+bi\) has characteristic polynomial
\[
                       (X-(a+b))^2,
\]
which is the characteristic polynomial of its regular action on the
coefficient algebra. Nevertheless \(H\) is not free of rank one:
\(\eta H=0\), whereas multiplication by \(\eta\) has rank one on the
regular module.

This representation cannot be the reduction of a \(\mathbf Z_2\)-free
module with a \(\mathbf Z[i]\)-action. If \(J\) lifted the action of \(i\),
then \(J-I=2N\), while
\[
                      (J-I)^2=-2J.
\]
The left side is divisible by \(4\); the right side is not, because
\(J^2=-I\) makes \(J\) a unit. Thus the crystalline input contributes
a real integrality condition, not merely the regular character.

## 6. Bounded source and reference evidence

All Lean ranges below are from the immutable revision
[jsmorph/rh at ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de](https://github.com/jsmorph/rh/tree/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de).
Source bytes are checked against the pinned atlas before reading.
These are attribution and contract checks; the source project has not
been rebuilt or replayed in the Lean kernel.

| Source, relative to the source tree | Bounded ranges | Role |
| --- | --- | --- |
| Formalism/LocalToGlobal/ProjectiveLattices/IsChartIff | 74–117 | Actual rigidified frame and adjunction direction |
| Development/AbelianVarietyTheory/Definitions/Uniformization/ExistsInKNeOne | 19–35 | Trivial translation kernel on all test rings |
| Development/AutomorphicSpectrum/Definitions/GlobalGeometry/ToFirst | 18–42 | Actual geometric germ and semiabelian fibre supplier |
| Development/AutomorphicSpectrum/Definitions/GlobalGeometry/GermSys | 47–63 | Exact coefficient basis, regular character, and lattice comparison |
| Development/AutomorphicSpectrum/Proofs/GeometryProofs/AbelianQuotientOfPowerFns | 192–225 | Proper quotient, adjunction, self-duality and pullback line |
| Development/AutomorphicSpectrum/Proofs/GeometryProofs/AbelianQuotientLattice | 423–450 | Actual equivariant toric tangent sequence |
| Development/AutomorphicSpectrum/Proofs/GeometryProofs/AbelianQuotientBilinear | 27–58 | Same simultaneous gauge identity |
| Development/AutomorphicSpectrum/Proofs/GeometryProofs/HeightCharFreeGeometric | 29–35, 76–93, 230–290 | Actual module action, change of frame and replaced kernel argument |
| Development/WeilBound/CoreStatements/TorusUniformisation/ChowMahlerFamilies/HodgeFreeEveryStalk | 124–173 | Same-residue comparison and local basis lifting |
| Development/AutomorphicSpectrum/Proofs/GeometryProofs/ExistsHodgeLatticeGermSystem | 85–114 | Exact projection to the Lie lattice and exact dual inverse image |
| Development/AutomorphicSpectrum/Proofs/GeometryProofs/EigenLinePAdicBound | 193–251 | Signature character, coefficient freeness and degree consumers |
| Development/AutomorphicSpectrum/Proofs/GeometryProofs/FibreCurveGermPowers | 215–270 | Separate curvewise conjugate data still required |

Primary classical inputs were read directly:

- B. Mazur and W. Messing, *Universal Extensions and One Dimensional
  Crystalline Cohomology*, Lecture Notes in Mathematics 370, Springer,
  1974. I §2.1, printed p. 13, defines pointed first-neighbourhood
  rigidifications; I Proposition 2.6.7, pp. 24–25, proves the universal
  extension identification and arbitrary base change. II §§9, 13 and
  15, especially pp. 93–94, 121–122 and 126–127, give the finite locally
  free crystal, compatibility with abelian endomorphisms, and its
  evaluation as a finite free Witt module.
  [Primary PDF](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/mazur-messing.pdf).
  SHA-256: 54486ccb86cad19118bfdb9d1e56386b18a45c63529254f1a1f7b7d110ca5eee.
- B. Conrad, *Units on product varieties*, undated four-page notes,
  Theorem 1.1, p. 1, with proof in §§2–3, pp. 1–3.
  [Author's PDF](https://math.stanford.edu/~conrad/papers/unitthm.pdf).
  SHA-256: 0720c7f594d69049ebe70d804582a252fcd83852b6f530b3f52fabb7cee9e9e0.

The checker authenticates these files and bounded excerpts and verifies
the gauge and filtration matrix identities symbolically over the
integers. It also verifies the characteristic-polynomial diagnostic
exactly. It does not machine-prove the classical geometric argument.

## 7. Exact remaining geometry and next task

The coefficient-freeness obstacle has been reduced to actual geometric
data already isolated in the source: a semiabelian quotient, the
specified self-dual abelian line bundle, the pullback identification, and
formal base change on the same stalk. The above proof supplies
freeness from those data without the source's isogeny-kernel calculation.

The independent remaining task is to construct the compatible
Hodge and conjugate filtrations for that same lattice on every required
test curve. Curvewise construction suffices for numerical triviality;
it must not be promoted to a global bundle on the entire special-fibre
component without a gluing proof.

A possible classical route is the integral logarithmic Dieudonné
functor in K. Madapusi Pera, *Toroidal Compactifications of Integral
Models of Shimura Varieties of Hodge Type*, Ann. Sci. ENS 52 (2019),
393–514, §1.3 and Proposition 1.3.5, pp. 407–408.
Its actual assumptions are a complete local normal noetherian base,
an effective Cartier boundary divisor, and an abelian variety off the
divisor extending to a smooth group with semiabelian fibres.
Appendix A.1, especially A.1.8–A.1.10, pp. 500–501, constructs its
integral crystal by combining a one-motive extension and the monodromy
pairing, with finite étale descent.
[Published primary PDF](https://www.numdam.org/item/10.24033/asens.2391.pdf),
SHA-256: d7e0dfa1d9ef76f3f85682f1abcc52d3d66de9e9378e92fc9153a3ba5c10a077.

This theorem does not, by itself, identify that logarithmic realization
with the source's formal lattice or prove that the prescribed
compactification satisfies the boundary hypotheses. Those are the
specific comparisons to pursue next. The separate integral complex
multiplication evaluation and finite section and cusp estimates remain
unchanged.
