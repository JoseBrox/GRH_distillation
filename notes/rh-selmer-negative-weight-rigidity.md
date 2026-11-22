# Negative-weight rigidity needs only qualitative Selmer finiteness

## Result and scope

Let \(k\) be a number field, let \(\ell\) be any prime, and let
\(\epsilon:G_k\to\overline{\mathbf Q}_\ell^\times\) be a continuous
finite-order character. For every integer \(m\ge1\),
\[
 H_f^1\bigl(k,\overline{\mathbf Q}_\ell(-m)\otimes\epsilon\bigr)=0.
 \tag{1}
\]
Here a global finite class is unramified at every finite place away from
\(\ell\), and satisfies the Bloch--Kato finite condition at each place
above \(\ell\). For algebraic coefficient fields this condition uses
algebraic tensor products, or equivalently finite coefficient extensions.
The cocycles are continuous for the usual \(\ell\)-adic topology.

We prove (1) from the already established
[qualitative strict Selmer finiteness theorem](qualitative-selmer-finiteness.md)
and the classical local Bloch--Kato calculation. The argument needs no
bound on a \(K\)-group, no prime-to-\(\ell\) assumption on
\(\epsilon\), and no restriction on the degree used to kill it.
It includes \(m=1\) and \(\ell=2\).

For the actual three-dimensional marked representation, this supplies
all negative-weight **base-point cohomological rigidity**. Together
with the preceding [weight-zero argument](rh-selmer-diagonal-rigidity.md),
it proves the cohomological part of nonpositive base-point rigidity.
The construction of the marked arithmetic model, its comparison of
tangent vectors with finite Selmer classes, and the rigidity of
non-diagonal two-sided points remain separate. Rational vanishing gives
no bound on the integral torsion needed in the uniform Selmer estimate.

## 1. Coefficients lie in one finite extension

**Lemma 1.** Let \(\Gamma\) be a compact Hausdorff group. Suppose a
character \(\theta:\Gamma\to E_0^\times\) has values in a finite
extension \(E_0/\mathbf Q_\ell\), and a continuous map
\(z:\Gamma\to\overline{\mathbf Q}_\ell\) satisfies
\[
 z(gh)=z(g)+\theta(g)z(h).
 \tag{2}
\]
Then all values of \(z\) lie in one finite extension \(E/E_0\).

**Proof.** There are only finitely many extensions of
\(\mathbf Q_\ell\) of each fixed degree, up to isomorphism; each
has finitely many embeddings in \(\overline{\mathbf Q}_\ell\).
Thus the algebraic closure is covered by countably many embedded finite
extensions \(E_i\). The classical finiteness assertion is Milne,
[*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
version 3.08 (2020), Proposition 7.64 and Remark 7.65, printed
page 133 (PDF page 135).

The sets
\[
             H_i=\{g\in\Gamma:z(g)\in E_0E_i\}
\]
are closed subgroups. Closedness follows because finite extensions are
complete, hence closed in the metric space
\(\overline{\mathbf Q}_\ell\). The subgroup assertions follow from
(2), including \(z(g^{-1})=-\theta(g)^{-1}z(g)\).
These subgroups cover \(\Gamma\). By the Baire theorem one has
nonempty interior; it is therefore open and has finite index.
Adjoin the finitely many values of \(z\) on coset representatives to
the corresponding \(E_0E_i\). Formula (2) puts every remaining value
in the resulting finite extension. \(\square\)

This proof uses the cocycle equation. An arbitrary compact subset of
\(\overline{\mathbf Q}_\ell\) need not lie in a finite extension.
For the character in (1), the finite image of \(\epsilon\) and
\(\chi_\ell(G_k)\subset\mathbf Z_\ell^\times\) supply \(E_0\).

Local finite conditions descend to a finite coefficient extension as
well. A witnessing element in
\(\overline{\mathbf Q}_\ell\otimes_{\mathbf Q_\ell}B_{\mathrm{cris}}\)
is a finite sum of elementary tensors. Enlarge \(E\) to contain those
finitely many algebraic coefficients, for each of the finitely many
places above \(\ell\). The equation saying that the cocycle becomes
a coboundary already holds over
\(E\otimes_{\mathbf Q_\ell}B_{\mathrm{cris}}\), since its inclusion
in the larger tensor product is injective. This is exactly the
Bloch--Kato condition over \(E\). Inertia coboundary conditions
also descend: when \(\theta(g)\ne1\), a primitive is forced to equal
\(z(g)/(\theta(g)-1)\); when the action is trivial, the coboundary
condition says the cocycle is zero.

## 2. A finite torsion group forces strict rational vanishing

Let \(L\) be totally imaginary, let \(m\ge1\), and let \(S\) consist
of the places above \(\ell\) and the archimedean places. Put
\(\theta=\chi_\ell^{-m}\). For a finite extension
\(E/\mathbf Q_\ell\), with ring of integers \(O\), define
\[
 \mathcal S_E=
 \ker\left(H^1(G_{L,S},(E/O)(-m))
       \longrightarrow\prod_{v\mid\ell}H^1(L_v,(E/O)(-m))\right).
 \tag{3}
\]
The local condition in (3) is zero in the **full** local cohomology.
Choosing a \(\mathbf Z_\ell\)-basis of \(O\) identifies (3) with a
finite direct sum of the strict groups with coefficients
\(\mathbf Q_\ell/\mathbf Z_\ell(-m)\). The existing finiteness
theorem therefore makes \(\mathcal S_E\) finite.
Choose \(a\ge0\) such that \(\ell^a\mathcal S_E=0\).
Only the existence of \(a\) is used.

**Lemma 2.** Every continuous cocycle
\(z:G_{L,S}\to E(-m)\) which is a coboundary on each decomposition
group above \(\ell\) is a global coboundary.

**Proof.** The cyclotomic character has infinite image over a number
field, so choose \(g_0\) for which
\[
                    d=\theta(g_0)-1\ne0.
\]
Subtract the coboundary with primitive \(z(g_0)/d\), and continue to
write \(z\) for the result. Now \(z(g_0)=0\), and all local
coboundary conditions remain true.

For every \(k\ge a\), reduce \(\ell^{-k}z\) modulo \(O\).
It is a continuous cocycle with values in the discrete module \(E/O\),
and its class belongs to the same finite group \(\mathcal S_E\).
Thus there is \(t_k\in E/O\) with
\[
  \ell^{a-k}z(g)=(\theta(g)-1)t_k\quad\text{in }E/O
                    \qquad(g\in G_{L,S}).
 \tag{4}
\]
At \(g_0\), equation (4) gives \(dt_k=0\). Hence \(t_k\) has a
representative in \(d^{-1}O\). Multiplying (4) by \(d\), and using
\(d,\theta(g)-1\in O\), yields
\[
                     dz(g)\in\ell^{k-a}O
                          \qquad\text{for every }k\ge a.
 \tag{5}
\]
The intersection of these ideals is zero. Therefore \(dz(g)=0\)
for all \(g\), and \(z=0\). Undo the normalization to obtain the
claimed global coboundary. \(\square\)

No compatibility among the primitives \(t_k\) is asserted or needed.
The single normalized value \(z(g_0)=0\) gives the common denominator
bound \(t_k\in d^{-1}O/O\). This replaces both a quantitative
cohomology estimate and a further inverse-limit argument.

## 3. The local finite condition supplies strictness

For a finite extension \(F/\mathbf Q_\ell\) and a de Rham
representation \(V\), Bloch--Kato's dimension formula is
\[
 \dim_{\mathbf Q_\ell}H_f^1(F,V)
   =\dim_{\mathbf Q_\ell}\bigl(D_{\mathrm{dR}}(V)/
                                     \operatorname{Fil}^0\bigr)
       +\dim_{\mathbf Q_\ell}H^0(F,V).
 \tag{6}
\]
For \(V=\mathbf Q_\ell(-m)\), \(m\ge1\), both terms on the right
are zero: the filtration is entirely in \(\operatorname{Fil}^0\),
and the negative cyclotomic character has no invariants.
Thus
\[
                    H_f^1(F,E(-m))=0.                 \tag{7}
\]
One can either apply (6) to the underlying \(\mathbf Q_\ell\)-space
or take a finite direct sum. The cited calculation is Corollary
3.8.4 and Example 3.9 of Bloch--Kato,
[*L-functions and Tamagawa numbers of motives*](https://math.stanford.edu/~conrad/BSDseminar/refs/BKTamagawa.pdf),
printed pages 355 and 359 (PDF pages 23 and 27). The latter table
explicitly gives zero for every negative twist, and identifies
\(H_f^1(F,\mathbf Q_\ell)\) with the unramified classes.

At a finite place \(v\nmid\ell\), the pure Tate character is
unramified and the unramified local cohomology is
\[
 H^1_{\mathrm{ur}}(L_v,E(-m))
       \simeq E/\bigl((Nv)^{-m}-1\bigr)E=0.
 \tag{8}
\]
Here arithmetic Frobenius has cyclotomic value \(Nv\); using the
opposite convention does not change the nonvanishing denominator.
Only unramifiedness away from \(\ell\) and (7) are needed for
Lemma 2.

## 4. Proof for every finite-order twist

Choose a finite Galois extension \(L/k\) on which \(\epsilon\) is
trivial and which is totally imaginary; one may adjoin \(i\) after
killing \(\epsilon\). Local finite classes remain finite after
restriction, directly from their defining period-ring kernel.
Likewise, unramified classes remain unramified after restriction.
After Lemma 1 and, if necessary, the finite enlargement for the local
period witnesses, all coefficients lie in one finite \(E\).

On \(G_L\), the representation is the pure twist \(E(-m)\).
At places above \(\ell\), (7) makes the restricted class a full-local
coboundary. Away from \(\ell\), the coefficient action is trivial
on inertia. An inertia coboundary is therefore the zero cocycle.
The cocycle vanishes on all these inertia groups, their conjugates,
and their closed normal closure, so it factors through \(G_{L,S}\).
Lemma 2 makes its restriction to \(G_L\) a global coboundary.

Here is a direct descent which does not divide by \([L:k]\).
Subtract this coboundary, so that \(z|_{G_L}=0\).
For \(g\in G_k\) and \(h\in G_L\), normality gives
\[
       \theta(h)z(g)=z(hg)
                    =z\bigl(g(g^{-1}hg)\bigr)=z(g).
 \tag{9}
\]
Choose \(h\in G_L\) with \(\theta(h)\ne1\); the pure negative
cyclotomic character on \(G_L\) supplies one. Then (9) forces
\(z(g)=0\). This proves (1).
It also explains why no divisibility restriction on
\(\operatorname{ord}(\epsilon)\) or \([L:k]\) is present. \(\square\)

## 5. The actual adjoint representation

Write \(\Psi=\chi_\ell^e\psi\), with \(e\ge1\) and \(\psi\)
finite order, and let \(\eta\) be the imaginary quadratic character.
Put \(w=(1,0,-1)\), and let
\[
              R(X)_{ab}=X_{4-b,\,4-a}\qquad(1\le a,b\le3).
 \tag{10}
\]
This involution preserves the weight \(j=w_a-w_b\). The actual
adjoint action on a homogeneous matrix of weight \(j\) is
\[
 g\cdot X=
 \begin{cases}
   \Psi(g)^jX,&\eta(g)=1,\\
   -\Psi(g)^jR(X),&\eta(g)=-1.
 \end{cases}
 \tag{11}
\]
Consequently the minus eigenspace of \(R\) has character \(\Psi^j\),
and the plus eigenspace has character \(\Psi^j\eta\).
The projections \((1\pm R)/2\) are available over every
characteristic-zero coefficient field, including \(\ell=2\).
They preserve the finite local condition because they commute with
the Galois action.

The full negative part has exactly these three scalar summands:

| Weight | Matrix generator | Character | Positive exponent \(m\) |
|---|---|---|---|
| \(-1\) | \(E_{21}-E_{32}\) | \(\chi_\ell^{-e}\psi^{-1}\) | \(e\) |
| \(-1\) | \(E_{21}+E_{32}\) | \(\chi_\ell^{-e}\psi^{-1}\eta\) | \(e\) |
| \(-2\) | \(E_{31}\) | \(\chi_\ell^{-2e}\psi^{-2}\eta\) | \(2e\) |

Apply (1) to each summand and recombine the primitives by these
projections. There are no other negative weights.
This gives all negative cases of the actual base-point rigidity
condition. For weight zero, restriction to the imaginary quadratic
field makes the action trivial. The local calculation following
(7) makes a finite class unramified there at \(\ell\); the defining
condition does so away from \(\ell\). The class-field argument and
the primitive \(-\gamma(c)/2\) in the preceding diagonal-rigidity
note therefore supply the zero-weight case as well.

### From a coboundary to a normalized tangent vector

Cohomological vanishing says that a cocycle is a coboundary. The
additional marking removes this conjugation freedom; it cannot be
omitted when concluding that a framed tangent vector is zero.
Here is the exact elementary calculation at the base representation.

Write
\[
 D(p)=\operatorname{diag}(p,1,p^{-1}),\qquad
 T=\operatorname{diag}(1,0,-1).
\]
Let \(c,g_1\) satisfy
\[
 c^2=1,\quad\eta(c)=-1,\quad\Psi(c)=1,\quad
 \eta(g_1)=1,\quad p=\Psi(g_1),\quad p^2-1\ne0.
 \tag{12}
\]
The integral marking actually assumes \(p^2-1\) is a unit, which
implies the displayed characteristic-zero condition. Set
\(g_1^*=cg_1^{-1}c\). The differentiated normalization conditions
on a tangent cocycle \(\gamma\) are
\[
 \gamma(c)=0,\qquad Z_{12}=Z_{21}=0,\qquad
 Z=\gamma(g_1)D(p)-\gamma(g_1^*)D(p^{-1}).
 \tag{13}
\]

Suppose \(\gamma(g)=X-g\cdot X\); a change of sign in the primitive
converts this convention to the preceding cohomological one.
The first condition in (13) gives \(X+R(X)=0\), so
\[
                 X=\begin{pmatrix}
                  a&b&0\\ d&0&-b\\0&-d&-a
                 \end{pmatrix}.
 \tag{14}
\]
The other two conditions use
\[
 Z=[X,D(p)-D(p^{-1})]
   =(p-p^{-1})[X,T],
 \qquad
 Z_{12}=-(p-p^{-1})b,\quad Z_{21}=(p-p^{-1})d.
 \tag{15}
\]
Since \(p-p^{-1}=p^{-1}(p^2-1)\ne0\), they give \(b=d=0\).
Thus \(X=aT\). Formula (11) fixes \(T\) for every \(g\), so
\(\gamma=0\). The argument works in characteristic zero, including
\(\ell=2\), and uses the actual two
marked entries rather than an assumed condition \(\gamma(g_1)=0\).

For the arithmetic algebra, two model comparisons still have to be
provided: a homogeneous derivation annihilating the equations must
lift to a normalized representation deformation whose cocycle has
the stated finite local conditions, and its cocycle must determine
the derivation on the model. Given these comparisons, the global
vanishing and (12)--(15) make every nonpositive such derivation zero;
ordinary cotangent duality then gives the required spanning of the
nonpositive equation classes. This is the complete passage from
cohomological vanishing to the framed assertion. Neither comparison
is established merely by naming the representation. None of this
concerns the non-diagonal two-sided points.
The scalar vanishing and matrix calculation include \(\ell=2\).
The actual graded-model implication cited below is used at odd
\(\ell\); its separate \(\ell\ne2\) hypothesis has not been removed.

## 6. Source contracts and verification

All source files are Levent Alpöge's development in
\(\mathrm{jsmorph/rh}\), commit
\(\mathrm{ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de}\).
Full bytes are checked locally against the pinned Git blobs;
only the listed bounded ranges are read. Hashes and ranges are in
the accompanying certificate.

For this table, \(U\) abbreviates
\(\mathrm{Development.AutomorphicArithmetic.AutomorphicVarieties.UnitaryThreeGroups}\),
and \(L\) abbreviates the same prefix ending in
\(\mathrm{LevelCohomology}\).

| Pinned source | Lines | Exact use |
|---|---:|---|
| \(U\).BlochKatoNonpositiveWeight | 194--243 | Negative scalar case; line 200 imports the numerical \(K\)-group package and lines 237--238 pass it to the global coboundary theorem |
| \(U\).BlochKatoNonpositiveWeight | 297--359 | Actual nonpositive adjoint theorem; negative characters have exponent \(en\) and finite factor \(\psi^{-n}\theta\), \(\theta\in\{1,\eta\}\) |
| \(U\).BlochKatoNonpositiveWeight | 363--414 | The two involution projections preserve the local condition and recombine scalar primitives |
| \(U\).AdRepBaseLiftApply | 18--39 | Exact adjoint action (11), including the minus sign |
| \(U\).UnitaryThreeReflectionRight | 235--257 | Weights \(1,0,-1\) and their differences |
| \(L\).FdAdjoinRange | 17--96 | Baire coefficient descent and the old quantitative global interface |
| Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CompactGroupRepDefinedOverFiniteExtension | 14--53 | An alternative countability proof by Krasner approximation |
| \(U\).TanCocIsBK | 162--190 | Actual marked-model tangent-to-finite-cocycle interface, retained |
| \(U\).GRepresents | 128--138 | The source's weightwise rigidity means existence of a coboundary primitive, not zero in the framed tangent space |
| \(U\).PtHypOf | 52--89 | Coboundary sign convention and the separation of base-point rigidity from fixed-point uniqueness and two-sided rigidity |
| \(U\).BaseRepGL3NormalisedOfPsiEqOne | 53--73 | Actual normalized cocycle and separating marked element |
| \(U\).UnitaryThreeReflectionRight | 277--301 | \(g_1^*=cg_1^{-1}c\), the three normalization equations, and the base representation |
| \(U\).ZetaReducibleRepEqSubInvAndIsUnit | 5--20 | The exact invertible coefficient \(p-p^{-1}=p^{-1}(p^2-1)\) |
| \(U\).NormCob | 30--49 | The source normalized-coboundary contract; (12)--(15) give its elementary base-representation specialization |
| \(U\).GradedModelSpansCotOfRigidWeights | 205--244 | Derivation lifting, normalization, rigidity, and tangent determination used in this order |
| Development.AutomorphicArithmetic.AutomorphicVarieties.GeneratorCountTuples.LemmaK | 13--17 | The old package couples qualitative \(H^2\)-finiteness to a numerical bound; only finiteness is used here |

The prior strict-finiteness certificate records the precise
Quillen--Lichtenbaum, finite even \(K\)-group and global duality
inputs, including the first positive twist and the prime 2.
The new checker verifies that dependency's hashes, the bounded
source contracts, the original Bloch--Kato and Milne PDFs, and exact finite
algebraic checks of the denominator argument, marked-normalization identities,
and adjoint decomposition.
These checks supplement the proofs above. They do not prove the
classical theorems, construct the marked model, bound an integral
Selmer length, run the full Lean development, or complete a whole
RH or GRH construction node.
