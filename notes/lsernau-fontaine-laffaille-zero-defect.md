# Zero crystalline defect in the unramified Fontaine–Laffaille range

## Result and scope

The zero-loss part of the crystalline-defect estimate admits a shorter
ordinary proof through Fontaine–Laffaille theory. The decisive condition
is that, at each labelled embedding of an **absolutely unramified** local
field, the allowed weights together with \(0\) fit in an interval of
length at most \(p-2\). The intervals may differ between embeddings.

Under this condition every map between reductions of crystalline lattices
preserves the reductions of their integral Bloch–Kato classes. Consequently,
for a lattice \(T\) in the class,
\[
                  D_{\mathcal Q}\bigl(T^\vee(1)\bigr)=0.       \tag{1}
\]
This applies to the source's crystalline branch with
\(\lambda_p=0\), provided \(p\) is not a level prime. It does not establish
the positive numerical defect bound at the remaining primes, or the
existence of the Galois representations to which that bound is to be
applied.

The classical input is the exact Fontaine–Laffaille classification in the
range \(0,\ldots,p-2\), including full faithfulness for torsion objects and
compatibility with reduction. The fixed-lattice extension lifting,
the passage through different labelled intervals, and the deduction of
(1) are proved below. These are ordinary mathematical arguments using a
named established theorem; no reconstruction of the Fontaine–Laffaille
period-ring construction or Lean replay is claimed.

The notation \(D_{\mathcal Q}\), including its tests against all modular
pairings and all full lattices in the class, is as in
[integral defects and separators](lsernau-integral-separators.md).

## 1. Labelled intervals and the statement to prove

Let \(p\geq3\), let \(K/\mathbb Q_p\) be finite and unramified, and let
\(O\) be the integers of a finite coefficient extension \(F/\mathbb Q_p\)
containing all embeddings of \(K\). Put
\(\Sigma=\operatorname{Hom}_{\mathbb Q_p}(K,F)\).
We use the Hodge–Tate convention in which \(O(1)\) has weight \(-1\).

For each \(\sigma\in\Sigma\), choose integers
\[
 a_\sigma\leq0\leq b_\sigma,\qquad
             b_\sigma-a_\sigma\leq p-2.                    \tag{2}
\]
Let \(\mathcal Q\) be any class of crystalline \(O\)-lattices whose
labelled weights at \(\sigma\) lie in
\([a_\sigma,b_\sigma]\). There is no bound on their ranks.

Write \(H_f^1(K,T)\) for the inverse image of the rational Bloch–Kato
subspace in \(H^1(K,T_F)\). In particular it includes the torsion of
\(H^1(K,T)\). Write
\[
 H_{f,n}^1(K,T)=
  \operatorname{im}\bigl(H_f^1(K,T)\longrightarrow
                              H^1(K,T/p^nT)\bigr).
\]

**Theorem.** For \(Y,T\in\mathcal Q\), every \(O/p^n[G_K]\)-linear map
\(q_n:Y/p^nY\to T/p^nT\) satisfies
\[
                    (q_n)_*H_{f,n}^1(K,Y)
                         \subset H_{f,n}^1(K,T).             \tag{3}
\]
It follows that (1) holds for every \(T\in\mathcal Q\).

Both the coefficient ring and the target lattice in (3) are fixed.
The conclusion is stronger than the existence of some crystalline lift
of the resulting residual representation.

A finite unramified extension of the coefficient ring may be made to
contain \(K\). The argument then descends: cohomology with a finite free
coefficient extension is obtained by tensoring, and this extension is
faithfully flat. In particular an \(O/p^n\)-valued cup product which
vanishes after this extension already vanished before it. For the
source's eventual coefficient-ring statements, one may simply choose a
coefficient field large enough at the outset.

## 2. The precise Fontaine–Laffaille input

Set \(W=O_K\) and \(R=O\otimes_{\mathbb Z_p}W\). Since \(K\) is unramified
and \(F\) contains its embeddings,
\[
                           R=\prod_{\sigma\in\Sigma}O.
\]
Frobenius on \(W\), acting trivially on \(O\), permutes these factors.

For \(0\leq r\leq p-2\), a free Fontaine–Laffaille module in the range
\([0,r]\) consists of a finite free \(R\)-module \(D\), a decreasing
filtration by direct summands with
\(\operatorname{Fil}^0D=D\) and \(\operatorname{Fil}^{r+1}D=0\),
and maps \(\varphi_i:\operatorname{Fil}^iD\to D\), semilinear for this
Frobenius, with
\[
 \varphi_i|_{\operatorname{Fil}^{i+1}D}=p\varphi_{i+1},
 \qquad \sum_i\varphi_i(\operatorname{Fil}^iD)=D.              \tag{4}
\]
The torsion category has the corresponding \(p\)-power torsion objects;
its exact sequences are strict for the filtrations.

We use the following standard form of Fontaine–Laffaille theory:

1. The contravariant functor \(T_{\mathrm{cris}}^*\) is an exact,
   fully faithful functor on torsion objects in this range.
2. On free objects it is an exact anti-equivalence with crystalline
   lattices whose weights, in our convention, lie in \([-r,0]\).
   The inverse is exact on short exact sequences of such lattices.
3. These functors commute with reduction modulo \(p^n\).

The \(O\)-coefficient version follows by carrying the commuting
\(O\)-action through the fully faithful functors. There is no small
ramification hypothesis on \(O\); the unramified hypothesis is on the
**base field \(K\)**.

For completeness, the freeness needed below also survives the coefficient
action. An integral Fontaine–Laffaille module is \(p\)-torsion free. Any
uniformizer of \(O\) divides a power of \(p\), so its factors \(D_\sigma\)
are torsion-free \(O\)-modules and hence free. The filtration is
\(p\)-saturated; it is therefore saturated over \(O\) and each graded
piece is free over \(O\). Adapted \(O\)-bases exist in each factor.

The original source is Fontaine–Laffaille [FL], especially the exactness
and full-faithfulness results in §§3 and 6 and the crystalline
classification in §8. A convenient precise formulation with the reduction
diagram is Iovita–Marmora [IM], §3.1.3. This use of [IM] concerns its
unramified Fontaine–Laffaille recollection; it does not use its
strongly-divisible-module argument over a ramified field.

## 3. Lifting extensions with the two integral endpoints fixed

**Lemma.** Let \(M,N\) be free Fontaine–Laffaille modules over \(R\) in
\([0,r]\). Every strict extension
\[
 0\longrightarrow M/p^nM\longrightarrow \bar E
        \longrightarrow N/p^nN\longrightarrow0              \tag{5}
\]
in the Fontaine–Laffaille category annihilated by \(p^n\) lifts to an extension
\[
 0\longrightarrow M\longrightarrow E\longrightarrow N
        \longrightarrow0                                   \tag{6}
\]
of the given integral modules.

The condition \(p^n\bar E=0\) is part of the hypothesis. An arbitrary
extension in the full torsion category can be killed only by \(p^{2n}\)
and is not covered by this lemma. The pullback used below is a submodule
of a product of modules killed by \(p^n\), so it meets the hypothesis.

**Proof.** At each factor \(\sigma\), choose bases of \(M_\sigma\) and
\(N_\sigma\) adapted to their filtrations. Write \(w_j\) for the
filtration index of a basis vector: it belongs to
\(\operatorname{Fil}^{w_j}\) but not
\(\operatorname{Fil}^{w_j+1}\). These indices lie in \([0,r]\).

Lift the adapted basis vectors of \(N_\sigma/p^n\) to
\(\operatorname{Fil}^{w_j}\bar E_\sigma\). Strictness permits the lift.
Together with the basis of \(M_\sigma/p^n\), the lifted vectors form an
adapted basis of \(\bar E_\sigma\). Indeed, the underlying sequence
splits because its quotient is free over \(O/p^n\); and subtracting
lifts of a filtered basis leaves exactly the corresponding filtered
part of \(M_\sigma/p^n\).

The maps in (4) are determined by the vectors
\(\varphi_{w_j}(e_j)\). Put these vectors in columns. Between one
component and its Frobenius successor, the resulting normalized
Frobenius matrix of \(\bar E\) has block form
\[
                    \begin{pmatrix}
                       A_M&\bar B\\0&A_N
                    \end{pmatrix}.                         \tag{7}
\]
Here the diagonal blocks are precisely the reductions of the fixed
normalized matrices for \(M,N\), and \(\bar B\) is the only new datum.

Choose any integral lift \(B\) of \(\bar B\). Give
\(E=M\oplus N\) the direct-sum filtration and normalized Frobenius
matrix
\[
                    \begin{pmatrix}
                       A_M&B\\0&A_N
                    \end{pmatrix}.                         \tag{8}
\]
For a basis vector of index \(w_j\), define its lower Frobenii by
\(\varphi_i(e_j)=p^{w_j-i}\varphi_{w_j}(e_j)\) for \(i\leq w_j\).
This verifies every compatibility in (4).

Strong divisibility says that the normalized columns generate. The
diagonal matrices \(A_M,A_N\) are invertible over \(O\), so (8) is
invertible over \(O\), regardless of \(B\). Thus \(E\) is a free
Fontaine–Laffaille module, (6) is strict, and its reduction is the
original extension (5), with its specified endpoint identifications.
\(\square\)

The construction adds no denominator. It also shows why merely knowing
that \(\bar E\) has some crystalline lift would be inadequate: both
diagonal blocks, and hence both prescribed integral endpoints, have
been held fixed.

## 4. Moving the labelled windows and proving (3)

Let
\[
                        r=\max_\sigma(b_\sigma-a_\sigma).
\]
The upper endpoints \(b_\sigma\) lie in \([0,r]\).
There is a crystalline rank-one \(O\)-lattice \(C\) with labelled weights
\(-b_\sigma\). One can construct it directly in the Fontaine–Laffaille
category: take \(D_\sigma=Oe_\sigma\), give \(e_\sigma\) filtration
index \(b_\sigma\), and send it by its normalized Frobenius to the basis
of the Frobenius successor. Equation (4) holds. The contravariant
realization has rank one over \(O\) and the stated weights.

Consequently the labelled weights of
\[
                            Y\otimes C,\quad T\otimes C,\quad C
\]
all lie in \([-r,0]\). The last inclusion uses
\(a_\sigma\leq0\leq b_\sigma\); keeping the rank-one quotient inside
the same range is essential.

Take a class \(c\in H_f^1(K,Y)\). It corresponds to an extension of
\(O\)-lattices
\[
                   0\longrightarrow Y\longrightarrow E_c
                         \longrightarrow O\longrightarrow0
                                                               \tag{9}
\]
whose rational representation is crystalline. After tensoring by \(C\),
all three terms of (9) have weights in \([-r,0]\).
Apply the exact contravariant Fontaine–Laffaille functor. It yields
\[
 0\longrightarrow D(C)\longrightarrow D(E_c\otimes C)
                \longrightarrow D(Y\otimes C)\longrightarrow0. \tag{10}
\]

Tensor \(q_n\) by \(C/p^nC\). Full faithfulness for torsion objects
identifies this Galois map with a morphism
\[
 D(T\otimes C)/p^n\longrightarrow D(Y\otimes C)/p^n.
\]
Pull back the reduction of (10) along this morphism. The resulting
strict extension has endpoints \(D(C)/p^n\) and
\(D(T\otimes C)/p^n\), each the reduction of a prescribed integral
module. The lemma lifts it with those endpoints fixed.

Realizing the lift and then tensoring by \(C^\vee\) gives a crystalline
extension of \(O\) by the original lattice \(T\). Its reduction is the
pushout of (9) by \(q_n\). This is exactly (3).

Notice that \(C\) need not be a power of the cyclotomic character:
its labelled weights can vary with \(\sigma\). A single common
cyclotomic shift would require a bound on the union of all labelled
windows and would miss the aligned-window argument.

## 5. From functoriality to zero dual defect

Put \(L=T^\vee(1)\). Any modular equivariant pairing
\[
                       Y/p^nY\otimes L/p^nL
                               \longrightarrow O/p^n(1)    \tag{11}
\]
corresponds to a map \(q_n:Y/p^nY\to T/p^nT\).
For \(c\in Z_f(Y)\) and \(d\in Z_f(L)\), equation (3) gives an
integral class \(\tilde c\in H_f^1(K,T)\) such that
\((q_n)_*[c]\) is its reduction.

The canonical cup product
\[
                   \tilde c\cup[d]\in H^2(K,O(1))
\]
vanishes after inverting \(p\), by Bloch–Kato local orthogonality.
But \(H^2(K,O(1))\simeq O\), by local Tate duality, is torsion free.
The integral cup product therefore vanishes, as does its reduction
under (11).

Composing with any integral \(\mathbb Z_p\)-linear map
\(O\to\mathbb Z_p\) preserves the vanishing. Thus every \(d\in Z_f(L)\)
annihilates every test used in \(H_{\mathcal Q}(L)\), proving
\[
                   H_{\mathcal Q}(L)=Z_f(L),\qquad
                   D_{\mathcal Q}(L)=0.                     \tag{12}
\]
Only equivariance of (11) was needed; the source's additional
crystalline lifting requirement on a modular pairing is automatically
covered.

The local duality inputs are Bloch–Kato [BK], Proposition 3.8, and
Milne [ADT], I Corollary 2.3. The equality
\(H^2(K,O(1))\simeq O\) follows by taking inverse limits of the
finite local invariant maps and extending coefficients.

## 6. Applying the theorem to the zero-loss source branch

Let
\[
 \begin{split}
 A_{h,b}
   &=(2b)!\left(\prod_{b-30h^3<a\leq b+30h^3}a\right)^{h^3},\\
 \lambda_p&=v_p(A_{h,b}),\\
 \delta_p&=10^6\frac{m}{k}\bigl(b\,v_p(M)+\lambda_p\bigr).
 \end{split}                                                \tag{13}
\]
The size hypotheses ensure \(b>30h^3\), so the product has positive
integer factors. In particular,
\[
                            \lambda_p=0\ \Longrightarrow\ p>2b.
                                                               \tag{14}
\]
This implication uses only the factorial factor.

Suppose first that \(K/\mathbb Q_p\) is unramified and the class is
**crystalline**. At each labelled embedding the source's allowed
weights satisfy
\[
 U_\sigma\subset[-\eta,\eta]\ \cup\
                   \epsilon_\sigma[c_\sigma,c_\sigma+W],
 \qquad c_\sigma\in\{G+\delta,b+\delta\},\quad
                   \epsilon_\sigma\in\{1,-1\}.               \tag{15}
\]
Here \(\delta\) is the integral window shift, not the local loss
\(\delta_p\). Since \(c_\sigma\geq\eta\), the hull of (15) and \(0\)
is either
\[
       [-\eta,c_\sigma+W]\quad\hbox{or}\quad
       [-c_\sigma-W,\eta].
\]
Its length is
\[
                c_\sigma+W+\eta\leq b+\delta+W+\eta.          \tag{16}
\]

The source's \(\operatorname{CrystallineSizes}\) assumptions include
\[
 \begin{gathered}
 Q\geq1,\quad
 99\bigl(Q^2+(W+1)Q+Q+W+m\bigr)\leq h,\\
 99h^3\leq G,\qquad 99(Gh^3+G)\leq b,\qquad \delta<\eta,\\
                  99\bigl((\eta+W)Q+\eta+h\bigr)\leq h^3.
 \end{gathered}                                             \tag{17}
\]
They imply
\[
       \delta+W+\eta\leq2\eta+W-1<b,\qquad G\leq b.
\]
Indeed \(99(2\eta+W+h)\leq h^3\) follows from \(Q\geq1\), while
\(b\geq99G\geq99^2h^3\). All quantities are integers.
Hence the length in (16) is at most \(2b-1\).
By (14), \(p\geq2b+1\), so
\[
                        b_\sigma-a_\sigma\leq p-2.          \tag{18}
\]
The theorem applies to every \(T\) in the class. No estimate involving
the number of low jumps is needed in this branch.

### Crystallinity and absolute unramifiedness must be checked separately

For the actual source application, these two checks have different
reasons.

First, the source's IsSummandClass.tame_or_crystalline says either
\(p\) is one of the two level primes, or the class has \(F=\top\),
\(K=\bot\); the latter is the class of crystalline lattices with the
stated weight sets. Since \(M\) is the product of the level primes,
\(p\nmid M\) eliminates the first alternative. A large prime by
itself does not eliminate a finite inertial type.

Second, the number field \(E\) lies in the cyclotomic field with
conductor \(C=D.\mathrm{cyclotomicConductor}\), and the admissible
data give
\[
                            q\mid C\ \Longrightarrow\ q\leq Q
                            \quad(q\text{ prime}).           \tag{19}
\]
The conventional implication is elementary: the source writes
\(C\mid q_2^N\) for its auxiliary integer \(q_2\), and has
\(q_2\leq Q\). A prime divisor of \(C\) divides \(q_2\).
Since (17) gives \(Q<2b<p\), (19) implies \(p\nmid C\).
Cyclotomic extensions are unramified outside their conductor;
therefore every \(E_v/\mathbb Q_p\) above \(p\) is unramified.

The source exposes (19) explicitly as h_small in
eventually_exists_lettersReadThick. It also shows that at
\(p>Q\) both the far-window choice and its sign depend only on
the residue-field letter. Over the unramified completion this is
precisely the labelled embedding data needed in (15). After enlarging
the coefficient field to contain the completion, the labels and
the rank-one twist used above are available.

Thus, assuming the stated conventional cyclotomic and weight data
for the actual attached lattices, the source's entire
\(\delta_p=0\) branch has the ordinary conclusion
\[
       p\nmid M,\quad \lambda_p=0
       \quad\Longrightarrow\quad
       D_{\mathcal Q_v}(T_v^\vee(1))=0
                         \quad\hbox{for every }v\mid p.       \tag{20}
\]
For an arbitrary local field or an arbitrary potentially crystalline
class, only the theorem under its explicit hypotheses is asserted.
In particular, killing inertia by a ramified extension would not
justify applying Fontaine–Laffaille theory over an unramified base.

There is also a slightly stronger vanishing range. The proof of (18)
only needs the width in (16) to be at most \(p-2\). Thus the same
conventional field and weight data give
\[
 p\nmid M,\qquad p\geq b+\delta+W+\eta+2
 \quad\Longrightarrow\quad D_{\mathcal Q_v}(T_v^\vee(1))=0.
                                                               \tag{20a}
\]
The size inequalities already imply \(b>Q\), so this threshold
also excludes the field's ramified primes. Equation (20a) can hold
when \(\lambda_p>0\); for example the factorial in (13) still has
positive valuation at primes at most \(2b\). For a collection of
classes with different window shifts, take the largest shift in
(20a). More precisely one may use the largest actual labelled
interval width instead of the uniform bound (16).

## 7. Effect on lengths and separators

There is a direct cocycle-level strengthening. In the Smith-lattice
construction of the integral-separator chapter, a relation-respecting
cocycle \(c:G_K\to T/p^nT\) is the image of a crystalline cocycle
\(A:G_K\to Y\), with \(Y\in\mathcal Q\), under an equivariant map
\(Y/p^nY\to T/p^nT\). Equation (3) supplies a crystalline integral
cocycle of \(T\) whose reduction has the same cohomology class as
\(c\). Their difference is a coboundary \(g\mapsto gv-v\) with
\(v\in T/p^nT\). Lift \(v\) to \(\tilde v\in T\) and add the
integral coboundary \(g\mapsto g\tilde v-\tilde v\). Hence
\[
                   \operatorname{Rib}_n\subset
                        \operatorname{red} Z_f(T).          \tag{20b}
\]
Thus in this range one gets actual integral crystalline lifts of the
cocycles, in addition to satisfaction of the relation-defined condition.

Combining (20) with the Smith-lattice realization and local-duality
inequality from [the integral-separator chapter](lsernau-integral-separators.md)
gives zero crystalline colength at these primes:
\[
                  \operatorname{crystallineColength}_n=0
                              \qquad(n\geq1).                \tag{21}
\]
Every relevant relation-respecting cocycle already satisfies the
source's crystalline relations. After imposing the global
normalizations and unramified conditions, the arithmetic tied-row
length is bounded by the original Selmer length, without a local
crystalline defect term.

Consequently the conditional individual-operator construction at such
a prime uses its Selmer, ramification and integral-denominator costs;
the \(r'\operatorname{localDefectBound}_p\) contribution is zero.
The generic combination of individually detected operators still adds
no further valuation loss.

This proves the vanishing portion of the finite prime support in (13),
and (20a) can remove further primes from the support of the actual
defect.
The following numerical work remains:

- positive \(\lambda_p\) below the range (20a), including the
  small-prime sparse-letter branch;
- the positive nonresonant bound when some low jumps contribute;
- the tame level primes dividing \(M\).

The character-triangle, Selmer-size, detection and actual labelled
Galois-attachment inputs remain separate dependencies of the full
separator theorem. The argument here does not discharge them.

## Sources and verification

All source declarations below refer to
[lsernau/grh-lean, revision 72fead102f663d5c7a407964a13dc0cf9d977207][source].
They identify the target classes and inequalities. The mathematical
proof in §§3–6 uses the classical inputs stated in §2, not the
unreconstructed Kummer-chart declarations.

| Pinned source file | Blob SHA | Decisive inspected material |
|---|---|---|
| Lib/ClassField/LocalDuality/CrystallineDuality.lean | ef4116053f3f421b0bfdddec747dc840e1aa3e0e | InClass 112–142; Pairing 149–212; InClass.of_jointly_injective 284–301 |
| New/Congruences/LocalLoss/CrystallineCocycles.lean | 6caafed79f54a3257f0f3f927e868c8565f3be09 | factorial loss 182–207; CrystallineSizes 240–254; zero branch 469–548 |
| New/Congruences/LocalLoss/CrystallineDefect.lean | c21212f774df81bff52003cbf8c6bf42ee2d7e95 | conductor and unramifiedness 223–299; IsSummandClass 383–404; actual windows 560–628 |
| New/Congruences/Lifting/CupOrthogonalityBounds.lean | 33ff1d8099302c487eb2621acac93ce54a04dc4b | source zero-defect target 225–278 |

Classical references:

- [FL] J.-M. Fontaine and G. Laffaille, *Construction de représentations
  \(p\)-adiques*, Ann. Sci. ÉNS 15 (1982), 547–608.
  The original PDF was inspected, including §§0.9 and 8.4; the exact
  bounded-weight formulation was checked against [IM, §3.1.3].
- [IM] A. Iovita and A. Marmora, *On the continuity of the finite
  Bloch–Kato cohomology*, Rend. Sem. Mat. Univ. Padova 134 (2015),
  239–271, §3.1.3 and its reduction diagram. Their main ramified-base
  theorem is not needed here.
- [BK] S. Bloch and K. Kato, *L-functions and Tamagawa numbers of
  motives*, §3, Proposition 3.8.
- [ADT] J. S. Milne, *Arithmetic Duality Theorems*, second edition,
  I Corollary 2.3.

No computational experiment is used for the decisive assertion.
The fixed-endpoint lifting is given by the explicit matrix (8), and
the endpoint and integrality checks are included in its proof.

[source]: https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207
[FL]: https://www.imo.universite-paris-saclay.fr/~fontaine/laffaille.pdf
[IM]: https://irma.math.unistra.fr/~marmora/Fin_BK_Coh.pdf
[BK]: https://math.stanford.edu/~conrad/BSDseminar/refs/BKTamagawa.pdf
[ADT]: https://www.jmilne.org/math/Books/ADTnot.pdf

