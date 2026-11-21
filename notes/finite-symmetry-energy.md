# Finite symmetry and the remaining theta energy

## Result and scope

Finite unitary averaging can remove the part of the theta energy that
fails to commute with a given group. It cannot remove the energy already
in that commutant. In particular, irreducibility of a local finite type
does not imply isotropy of the global space containing its copies.

The exact reduction below is an ordinary finite-dimensional theorem.
The source has genuine integral isometries on an ambient cuspidal lattice,
so this is a relevant possibility, not a proposal to choose arbitrary
complex changes of basis. However, its type lattices impose additional
subgroup-character conditions. The inspected contracts do not identify
an action on the same retained arithmetic target with the required small
multiplicity-space variance. Thus this note supplies a precise optional
interface and an obstruction to a proposed shortcut; it does not supply
the remaining global energy estimate.

Use the definitions and actual-map comparison of
[the theta-energy note](averaged-theta-energy.md). All source citations
below refer to `jsmorph/rh` at the immutable revision
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. Full file hashes, bounded
excerpt hashes and the exact finite checks are in the
[certificate](../certificates/finite-symmetry-energy.json), reproduced by
[the checker](../scripts/check_finite_symmetry_energy.py). Source contracts
were read and compared; no upstream proof audit or Lean build is claimed.

## 1. The exact averaging identity

Let a finite group \(K\) act unitarily on a complex Hilbert space
\(H\) of dimension \(D>0\), with operators \(U_g\). Let
\(T_i:H_i\to H\) be a finite family, where \(r_i=\dim H_i\), and set
\[
 R=\sum_i r_i>0,\qquad Q=\sum_iT_iT_i^*,\qquad M=\operatorname{tr}Q>0,
\]
\[
 \Delta=\sum_i\|T_i^*T_i-I_{H_i}\|_{\rm HS}^2,\qquad
 e=\Delta/R,\qquad
 \eta=\frac{D}{M^2}\left\|Q-\frac MD I_H\right\|_{\rm HS}^2.
\]
Append all maps \(T_{g,i}=U_gT_i\), retaining an individual copy of
\(H_i\) for every pair \((g,i)\). Define the Reynolds operator
\[
 \mathcal R(X)=\frac1{|K|}\sum_{g\in K}U_gXU_g^*.
\]
For the enlarged family,
\[
 R_K=|K|R,\quad \Delta_K=|K|\Delta,\quad
 Q_K=|K|\mathcal R(Q),\quad M_K=|K|M.
\]
Consequently its diagonal error is still \(e\), and
\[
 \boxed{\quad
 \eta_K=\frac{D}{M^2}
       \left\|\mathcal R(Q)-\frac MD I_H\right\|_{\rm HS}^2
 =\eta-\frac{D}{M^2}\|Q-\mathcal R(Q)\|_{\rm HS}^2.
 \quad}                                                    \tag{1.1}
\]

**Proof.** Unitarity gives
\(T_{g,i}^*T_{g,i}=T_i^*T_i\), which proves the first identities.
Conjugation is unitary for the Hilbert--Schmidt inner product. Averaging
over a finite group is self-adjoint, since inversion permutes the group,
and idempotent, by multiplication of its indices. Its range is precisely
the operators commuting with every \(U_g\). It is therefore the
orthogonal projection onto that commutant. It preserves trace and fixes
the identity. Pythagoras applied to \(Q-(M/D)I_H\) proves (1.1). \(\square\)

One can first restrict the domains to the actual ramified subspaces and
then apply this argument. In that case \(R,\Delta,M\) must be those of
the restricted maps. Averaging does not restore discarded rank or repair
a diagonal denominator that has ceased to be positive.

## 2. What remains in the multiplicity spaces

Choose an orthogonal isotypic decomposition
\[
 H=\bigoplus_{\pi} V_\pi\otimes E_\pi,
 \qquad d_\pi=\dim V_\pi,\quad m_\pi=\dim E_\pi>0,
\]
where the \(V_\pi\) are pairwise inequivalent irreducible unitary
representations. Let \(P_\pi\) be the corresponding projections and put
\[
 A_\pi=\frac1{d_\pi}
       \operatorname{Tr}_{V_\pi}(P_\pi QP_\pi).
\]
Here the partial trace is taken over the representation factor, so that
\(A_\pi\) is a positive operator on the multiplicity space \(E_\pi\).
Schur's lemma and preservation of partial trace give
\[
 \mathcal R(Q)=\bigoplus_\pi I_{V_\pi}\otimes A_\pi,
 \qquad M=\sum_\pi d_\pi\operatorname{tr}A_\pi.
\]
Indeed, a commuting block between inequivalent irreducibles vanishes;
a commuting block between two copies of the same irreducible is scalar
on that irreducible. Taking its partial trace determines the scalar.
It follows that
\[
 \boxed{\quad
 \eta_K=\frac{D}{M^2}\sum_\pi d_\pi
       \left\|A_\pi-\frac MD I_{E_\pi}\right\|_{\rm HS}^2.
 \quad}                                                    \tag{2.1}
\]
Writing \(a_\pi=\operatorname{tr}(A_\pi)/m_\pi\) separates two losses:
\[
 \eta_K=\frac{D}{M^2}\left[
   \sum_\pi d_\pi\|A_\pi-a_\pi I\|_{\rm HS}^2
   +\sum_\pi d_\pi m_\pi(a_\pi-M/D)^2\right].             \tag{2.2}
\]
The first term is variance within multiplicity spaces; the second is
imbalance of mass between isotypic components. If the whole target
representation is irreducible, both terms vanish. If it is merely
multiplicity free, only the first necessarily vanishes. If there is a
single irreducible type with multiplicity \(m\), then
\[
 \eta_K=m\frac{\operatorname{tr}(A^2)}{(\operatorname{tr}A)^2}-1,
                                                               \tag{2.3}
\]
which can be as large as \(m-1\).

There is a second exact stopping rule. If each \(T_i\) intertwines the
target action with a unitary action \(V_{g,i}\) on its source, then
\[
 U_gT_i=T_iV_{g,i}
 \quad\Longrightarrow\quad
 U_gT_iT_i^*U_g^*=T_iT_i^*.
\]
Thus \(Q\) already commutes with \(K\), and (1.1) makes no improvement.
No such intertwining identity for all actual maps is assumed here.

### Sharp integral examples

Let \(K\) be the order-eight group generated on \(V=\mathbb C^2\) by
\[
 R_0=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
 S_0=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
These integral orthogonal matrices preserve \(\mathbb Z^2\). Their
complex representation is irreducible: an invariant line would be one
of the two eigenspaces of \(S_0\), and \(R_0\) exchanges those lines.
On \(H=V\otimes\mathbb C^m\), let the group act on the first factor.
Take \(m\) copies of the same isometric integral map
\(T_i:V\to H\), \(v\mapsto v\otimes e_1\). Then
\[
 e=0,\quad D=R=M=2m,\quad
 Q=m I_V\otimes |e_1\rangle\langle e_1|,\quad
 \eta=\eta_K=m-1.
\]
This satisfies irreducibility of the local type and every group action
is integral and unitary. It disproves a deduction of small global
isotropy error from those facts alone. It is an abstract obstruction,
not a computation of the actual source's error.

For a multiplicity-free example, let the order-two group act on
\(\mathbb C^2\) by \(\operatorname{diag}(1,-1)\), and take two copies
of \(z\mapsto(z,0)\). Again \(e=0\), but \(Q=\operatorname{diag}(2,0)\)
and \(\eta_K=\eta=1\). This time only the block-mass term survives.

## 3. The same arithmetic target is essential

Suppose the original maps are integral maps of full lattices over a
number field, with fixed norms at every infinite place. The enlarged
family is admissible for the refined frame comparison if there are
number-field-linear automorphisms \(\alpha_g\) of the same arithmetic
target which preserve its lattice and every specified norm, and whose
complex realizations agree with \(U_g\) in the actual matrix bridge.
For a retained target obtained by projecting a larger Hilbert space,
this requires the retained subspace to be invariant and the projection
to intertwine the two actions. An action on the larger space alone is
insufficient.

Under these hypotheses \(\alpha_g B_i\) preserves integrality, every
ideal divisibility condition on the image, and each actual map height.
The source's map height is the normalized sum of the logarithms of the
squared operator norms at infinite places, so preservation of those
norms proves this last assertion directly.
The inverse group element gives equality of lattices, rather than just
one inclusion. Repeating source ranks, slopes and height upper bounds
uniformly leaves their normalized means unchanged. Hence the refined
frame comparison can replace its isotropy term by (2.1) without changing
its diagonal error or target-rank denominator. These claims concern the
refined finite-family comparison. They do not remove additional
cardinality terms from a different quoted frame theorem, or prove that
the enlarged family satisfies every original word-indexing contract.

The source comparison gives both encouraging evidence and a concrete
limit:

| Pinned source, path under `lean/src/` | Bounded lines | What is supplied |
| --- | --- | --- |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/KeepsCuspLatticeNorm.lean` | 204–236 | Under its geometric hypotheses, level automorphisms preserve the ambient cusp lattice and its norm at every embedding. |
| `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ActCCoe.lean` | 38–48 | The actual finite level action restricts to the cuspidal vector space under the stated row conditions. |
| `Development/AbelianVarietyTheory/Definitions/Divisors/IsCoprimeOfNatCast.lean` | 436–473 | At a type level the finite type group and residual level group give the displayed product decomposition; subgroups pull back through the reduction map. |
| `Formalism/LocalToGlobal/IndefiniteReal/GramCEqTranspose.lean` | 76–101 | The type space consists of vectors satisfying a subgroup-character equation; its lattice and good part are intersections with this space. |
| `Development/AbelianVarietyTheory/Definitions/Divisors/NormNegCmConstantEqAtAllEmbeddings.lean` | 31–48 | The actual type, good and bad lattices are the same subgroup-character and spectral cuts of the ambient lattice. |
| `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PointRead.lean` | 24–38 | The actual type rank equals the dimension of a subgroup-character eigenspace; the bad rank imposes a further spectral kernel. |
| `Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/LabelDatum.lean` | 91–116 | The finite-general-linear-group classification and central-series tie concern local irreducible characters and their idempotents. They impose no global multiplicity-one clause. |
| `Development/AutomorphicArithmetic/TwistedTraces/IsotypicMultiplicityTensorProduct.lean` | 12–13 | Even with irreducible local representations, the displayed global trace factorization retains an unspecified multiplicity factor. |
| `Formalism/SharpRestriction/CuspSpanNormBounds/DataS.lean` | 33–48 | The frame interface has a common Hilbert target and a family of operators; it contains no irreducibility or finite-group action on that target. |
| `Formalism/HarderNarasimhan/StatementPl.lean` | 55–62 | The actual map height uses precisely the squared operator norms at infinite places. |
| `Formalism/SizeWindowBrackets/FrameTraceRatioFinEquiv.lean` | 59–77 | The arithmetic frame comparison requires full lattices, integral maps, actual heights and the common target matrix bridge. |

The eigenspace issue is elementary. If
\[
 E_{J,\lambda}=\{v:U_jv=\lambda(j)v\text{ for every }j\in J\},
\]
then
\[
 U_g E_{J,\lambda}=E_{gJg^{-1},\lambda^g},\qquad
 \lambda^g(gjg^{-1})=\lambda(j).
\]
A sufficient subgroup preserving the same cut is therefore the
normalizer that also preserves its character. The whole ambient group
need not preserve it. The original subgroup \(J\) certainly preserves
the cut, but acts there by the scalars \(\lambda(j)\); its conjugation
average fixes every operator and cannot reduce the energy. In the
order-eight example above, take
\(J=\langle S_0\rangle\) and \(\lambda=1\). Its eigenspace is
\(\mathbb C e_1\), which \(R_0\) carries to \(\mathbb C e_2\), although
the ambient lattice and metric are preserved. A further spectral cut
must also be preserved. This does not assert that the actual source cut
fails invariance; it shows why the ambient theorem alone cannot prove it.

## 4. The remaining supplier after this reduction

To use finite symmetry in the current construction, supply an action
compatible with the same arithmetic target, all its metrics, and the
actual common-basis bridge. Then it suffices to estimate the positive
quantity in (2.1), with the same height and scale weights used in the
theta-energy budget. Exact whole-target irreducibility would make it
zero. More generally, balanced block masses and nearly scalar positive
operators on the multiplicity spaces would suffice.

The inspected source contracts give neither of these stronger global
conclusions. Local irreducible types, central idempotents, and ambient
integral isometries do not replace them. Finite averaging is therefore a
precise reduction of the outstanding energy, conditional on the stated
compatibility, rather than a discharge of that energy. The main direct
arithmetic transfer and its construction frontier remain unchanged.

## Verification

The proofs above establish the universal identities and obstructions.
The checker verifies the eight-element integral group exactly, its
Reynolds projection and variance identity on explicit rational matrices,
the sharp isotypic examples, the multiplicity-free example and the
noninvariant eigenspace. It also verifies all cited source bytes against
the pinned source atlas and hashes each bounded excerpt. These finite
checks supplement the proofs; they do not assert the missing action or
energy bound for the actual arithmetic construction.

The independent transport reviewer checked Sections 1–3, including all
normalizations, the partial-trace formula, both counterexamples, the
scalar-stabilizer observation, and the stated arithmetic compatibility;
the review passed. The reviewer also independently hash-verified and
read the ambient-isometry and subgroup-character source excerpts. This
was not an independent audit of every other source-table clause or of
their upstream proofs.
