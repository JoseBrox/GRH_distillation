# Strictly dominant Iwahori matching by compactness and interpolation

## Result and scope

This note proves the local matrix supplier that was left open in
[the split attachment chapter](lsernau-split-galois-attachment.md):
strictly dominant pro-unipotent Iwahori double cosets admit one
polynomial norm root for every characteristic polynomial in their
support. The same polynomial works for **all** matrices with that
characteristic polynomial. It gives both double-coset membership
equivalence and the single-coset statement for every twisted norm
fiber. These quantifiers are needed for the trace-transfer argument.

The proof uses integral Gaussian elimination, compactness of the
Iwahori subgroup, and polynomial interpolation. It does not assume
regularity of an automorphic representation or an orbital-integral
fundamental lemma. Section 4 then supplies the global unitary
packaging, including the determinant condition for matrices of every
size, and instantiates the existing trace-transfer theorem.

The source comparison is pinned to
[lsernau/grh-lean, revision
72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207).
No Lean build is claimed.

## 1. Twisted diagonalization inside a dominant double coset

Let \(N\ge1\), let \(L\) be a nonarchimedean local field and let
\(K=I_1(L)\subset\mathrm{GL}_N(\mathcal O_L)\) be the inverse
image of the upper unitriangular group over the residue field.
Let \(\sigma\) be a continuous valuation-preserving automorphism
of \(L\). Write
\[
 t=\operatorname{diag}(t_0,\ldots,t_{N-1}),\qquad
 |t_0|<\cdots<|t_{N-1}|.
\]

**Theorem 1.1.** For every \(\delta\in KtK\), there are
\(k\in K\) and a diagonal \(d\in K\) such that
\[
 k^{-1}\delta\sigma(k)=td.                              \tag{1.1}
\]

**Proof.** Define compact open subgroups
\[
 H_j=t^{-j}Kt^j\quad(j\in\mathbb Z)
\]
and, for \(k\in K\), put
\[
 X(k)=t^{-1}k^{-1}\delta\sigma(k).
\]
The automorphism \(\sigma\) preserves every \(H_j\), since
membership is a condition on the valuations of matrix entries and
\(|\sigma(t_i)|=|t_i|\). We first show that for every finite interval
\([-a,b]\), with \(a,b\ge0\), some \(k\in K\) has
\(X(k)\in\bigcap_{j=-a}^bH_j\).

The interval \([0,0]\) is immediate: write
\(\delta=k_0tk_1\) with \(k_0,k_1\in K\). Then
\(X(k_0)=k_1\sigma(k_0)\in K\).

For the widening step, suppose \(x=X(k)\in H_0\cap\cdots\cap H_b\).
Integral Gaussian elimination factors
\[
 x=uh,
\]
where \(u\) is upper unitriangular integral and \(h\) is lower
triangular in \(K\). All the necessary pivots are units: every
leading or trailing principal minor of a matrix in \(K\) is
congruent to \(1\). Dominance gives
\[
 u\in H_j\ (j\ge0),\qquad h\in H_{-1}.
\]
The second assertion follows because \(t^{-1}ht\) contracts each
strictly lower entry. Since \(h=u^{-1}x\), it also belongs to
\(H_0,\ldots,H_b\). Put \(z=\sigma^{-1}(h)\). Then
\(z\in H_{-1}\cap H_0\cap\cdots\cap H_b\), in particular
\(z\in K\). The replacement \(k'=kz^{-1}\) satisfies
\[
 X(k')=t^{-1}zt\,u\in H_0\cap\cdots\cap H_{b+1}.        \tag{1.2}
\]
This constructs every interval \([0,b]\).

For the shifting step, suppose
\(x=X(k)\in\bigcap_{j=-a}^{b+1}H_j\). Put
\(y=txt^{-1}\). Since \(x\in H_1\), we have \(y\in K\).
Direct multiplication gives
\[
 X(ky)=\sigma(y).
\]
Conjugation by \(t\) carries \(H_{j+1}\) to \(H_j\), so this
new element belongs to every \(H_j\) for
\(-a-1\le j\le b\). Start with \([0,a+b]\) and shift \(a\)
times to obtain the claimed arbitrary finite interval.

For each \(M\), choose \(k_M\in K\) handling \([-M,M]\).
Compactness gives a convergent subsequence with limit \(k\in K\).
For each fixed \(j\), continuity of \(X\) and closedness of
\(H_j\) give \(X(k)\in H_j\). An off-diagonal entry of a matrix
in every \(H_j\) must vanish: its absolute value, multiplied by
\(|t_i/t_j|^m\), stays bounded for every positive and negative
integer \(m\), while \(|t_i/t_j|\ne1\).
Thus \(X(k)\) is diagonal. Since it belongs to \(H_0=K\), its
diagonal entries lie in \(1+\mathfrak p_L\). This proves (1.1).
\(\square\)

The finite-interval argument only needs weak dominance. Strict
dominance is used precisely to make the intersection of all the
\(H_j\) diagonal. This identifies the actual scope of the result.

## 2. A common polynomial norm root

Now let \(L/F\) be cyclic of degree \(p\), with generator
\(\sigma\). For matrices or polynomial coefficients define
\[
 N_\sigma(b)=b\sigma(b)\cdots\sigma^{p-1}(b).
\]
Let \(K_L=I_1(L)\), \(K_F=I_1(F)\), and suppose
\[
 N_{L/F}(1+\mathfrak p_L)=1+\mathfrak p_F.               \tag{2.1}
\]
Keep the strictly dominant diagonal \(t\), and put
\[
 s=\operatorname{diag}(N_{L/F}(t_i))\in\mathrm{GL}_N(F).
\]
Suppose a monic polynomial \(P\) is the characteristic polynomial
of either a matrix \(x\in K_FsK_F\), viewed over \(L\), or of
\(N_\sigma(\delta)\) for \(\delta\in K_LtK_L\).

**Theorem 2.1.** There is a polynomial \(z\in L[X]\), of degree
less than \(N\), with the following three properties.

1. \(P\mid N_\sigma(z)-X\).
2. If \(\gamma\in\mathrm{GL}_N(F)\) has characteristic
   polynomial \(P\) and \(a=z(\gamma)\), then
   \(N_\sigma(a)=\gamma\), and
   \[
   \gamma\in K_FsK_F\quad\Longleftrightarrow\quad
   a\in K_LtK_L.
   \]
3. For every \(\gamma\in\mathrm{GL}_N(L)\) of characteristic
   polynomial \(P\), every \(\delta\in K_LtK_L\) satisfying
   \(N_\sigma(\delta)=\gamma\) obeys
   \[
   z(\gamma)^{-1}\delta\in K_L.                         \tag{2.2}
   \]

In all three statements the matrix \(z(\gamma)\) is invertible.

**Proof.** First produce a seed diagonal representative. If the seed
is \(N_\sigma(\delta_0)\), apply Theorem 1.1:
\(k_0^{-1}\delta_0\sigma(k_0)=td_0\), with diagonal
\(d_0\in K_L\). Multiplication of the twisted conjugates gives
\[
 k_0^{-1}N_\sigma(\delta_0)k_0
   =N_\sigma(td_0)=\operatorname{diag}(c_i),\qquad
 c_i=N_{L/F}(t_i d_{0,i}).                              \tag{2.3}
\]
If the seed is \(x\in K_FsK_F\), apply Theorem 1.1 over \(F\)
with the identity automorphism. It gives an ordinary conjugate
\(se\), with diagonal \(e\in K_F\). Lift each \(e_i\) to a
norm of \(d_{0,i}\in1+\mathfrak p_L\) by (2.1). Formula (2.3)
then gives the same kind of representative.

The roots \(c_i\) belong to \(F^\times\) and have pairwise
distinct valuations, since
\(|c_i|_L=|t_i|_L^p\). Thus
\[
 P(X)=\prod_i(X-c_i).
\]
In particular \(P\in F[X]\) is squarefree. Set
\[
 z(X)=\sum_i t_i d_{0,i}
             \prod_{j\ne i}\frac{X-c_j}{c_i-c_j}.        \tag{2.4}
\]
Since \(c_i\) is fixed by \(\sigma\), evaluation at \(c_i\)
commutes with applying \(\sigma\) to coefficients. Hence
\[
 N_\sigma(z)(c_i)=N_{L/F}(t_i d_{0,i})=c_i.
\]
The distinct linear factors of \(P\) therefore divide
\(N_\sigma(z)-X\). Also \(z(c_i)=t_id_{0,i}\ne0\), so
\(\gcd(P,z)=1\). Bézout's identity and Cayley--Hamilton prove
that \(z(\gamma)\) is invertible for every \(\gamma\) with
characteristic polynomial \(P\).

We record how the ordering removes a possible ambiguity. If
\(d\in K_L\) is diagonal and
\(\operatorname{diag}(N(t_i d_i))\) has characteristic polynomial
\(P\), its roots must be the \(c_i\) **in that order**. Equality
of two such roots implies equality of the valuations of the
corresponding \(t_i\), hence equality of their indices. Consequently,
whenever
\[
 k^{-1}\gamma k=\operatorname{diag}(N(t_i d_i)),
\]
polynomial evaluation gives
\[
 z(\gamma)=k(td_0)k^{-1}.                               \tag{2.5}
\]

For property 3, apply Theorem 1.1 to the given \(\delta\), obtaining
\(k\in K_L\), diagonal \(d\in K_L\), and
\(k^{-1}\delta\sigma(k)=td\). Its norm conjugates to the
diagonal in (2.5). Therefore
\[
 z(\gamma)^{-1}\delta
  =k(d_0^{-1}d)\sigma(k)^{-1}\in K_L,
\]
as required. Notice that the polynomial has not been chosen again
for this \(\delta\).

For property 2, first \(\sigma(\gamma)=\gamma\). Thus the
matrices \(\sigma^j(z)(\gamma)\) commute, and property 1 with
Cayley--Hamilton gives \(N_\sigma(z(\gamma))=\gamma\).

If \(\gamma\in K_FsK_F\), its ordinary diagonalization over
\(F\), followed by (2.1), supplies (2.5) with \(k\in K_F\).
It follows that \(z(\gamma)=k(td_0)k^{-1}\in K_LtK_L\).

Conversely, suppose \(a=z(\gamma)\in K_LtK_L\). Apply
Theorem 1.1 to \(a\):
\[
 k^{-1}a\sigma(k)=td,
 \qquad k^{-1}\gamma k=\operatorname{diag}(c_i).
\]
Equation (2.5) also gives \(a=k(td_0)k^{-1}\). Comparing these
two expressions shows
\[
 \sigma(k)=k(d_0^{-1}d).
\]
Write \(e=\operatorname{diag}(k_{ii})\). Its entries lie in
\(1+\mathfrak p_L\), so it is invertible and belongs to \(K_L\).
Each column of \(k\) transforms under \(\sigma\) by the same
scalar as its diagonal entry. Hence \(g=ke^{-1}\) is fixed by
\(\sigma\); it lies in \(K_L\cap\mathrm{GL}_N(F)=K_F\).
As diagonal matrices commute,
\[
 \gamma=g\operatorname{diag}(c_i)g^{-1}
        =g\,s\,\operatorname{diag}(N(d_{0,i}))g^{-1}
        \in K_FsK_F.
\]
This completes the proof. \(\square\)

No bounded-denominator assertion is needed for (2.4). If one later
needs such bounds, strict dominance at least makes every interpolation
denominator explicit:
\[
 \operatorname{ord}_L(c_i-c_j)
   =p\min(\operatorname{ord}_L(t_i),
                 \operatorname{ord}_L(t_j))\quad(i\ne j).
\]
This follows from unequal valuations; it is an equality, not a
cancellation estimate.

## 3. When the local hypotheses hold

Condition (2.1) holds for unramified extensions. On successive
principal-unit quotients, the norm is the residue-field trace, which
is surjective; successive approximation and completeness give the
norm preimage. This also covers unramified degree equal to the
residue characteristic.

It also holds for a cyclic, tamely ramified extension of prime
degree \(p\). Such a ramified extension is totally ramified, and
\(p\) is invertible in \(\mathcal O_F\). For every
\(u\in1+\mathfrak p_F\), Hensel's lemma gives
\(v\in1+\mathfrak p_F\) with \(v^p=u\). As \(v\in F\),
\(N_{L/F}(v)=v^p=u\).

The same alternatives give an integral element of trace one. In
the unramified case, lift an element of residue trace one and
divide by its unit-valued trace. In the tamely ramified prime case
take \(1/p\). For \(s\in K_L\) satisfying
\(s\sigma(s)\cdots\sigma^{p-1}(s)=1\), an integral trace-one
element \(c\) gives the explicit coboundary
\[
 b=\sum_{j=0}^{p-1}\sigma^j(c)
       s\sigma(s)\cdots\sigma^{j-1}(s)\in K_L,
 \qquad s\sigma(b)=b.
\]
This is the calculation already proved in Section 5 of the split
attachment chapter. Combined with Theorem 2.1, it supplies both the
matrix norm-root datum and the Iwahori cocycle splitting.

## 4. Global unitary packaging and exact eigencharacter transfer

We now use the conventions and proved transfer machinery of
[global norm roots](lsernau-global-norm-roots.md),
[definite trace transfer](lsernau-base-change-trace-transfer.md), and
[specific matched Hecke levels](lsernau-specific-hecke-transfer.md).
These chapters were read at the repository revision
\(618c7aaa32c2655f4e16ce37d131aca7f3ef63e8\).

Let \(E'/E\) be a source CM step of prime degree \(p\), with
generator \(\sigma\), integral trace-one element, and the finite
idele character \(\mu\) in the source Step definition. Choose a
standard totally definite unitary form space of rank \(N\), and
assume \(\mu_{5040}\subset E\), as in the source Step hypothesis.
Choose a split CM place \(w\) of \(E\) with a unique place \(u\) above it
in \(E'\); write \(F=E_w\), \(L=E'_u\). Assume, as required in
the source local matching theorem,
\[
 \mu(\operatorname{locIdele}_w x)=1
                \qquad\text{for every }x\in F^\times.  \tag{4.1}
\]
This condition concerns the auxiliary character \(\mu\); it does
not assert that the local extension \(L/F\) is trivial. The Step
norm criterion involves \(\mu(t\bar t)\).

The unique-place hypothesis makes the local extension cyclic of
degree \(p\), with entrywise Galois action. The global integral
trace-one element has local trace one. A ramified extension of
prime degree is totally ramified; if its residue characteristic
were \(p\), the trace of every integral element would reduce to
zero. Thus this local extension is unramified or tamely ramified.
Section 3 verifies (2.1) and Iwahori cocycle splitting in both cases.

At the pair \((u,\bar u)\), a unitary matrix is specified by its
\(u\)-component; its \(\bar u\)-component is the inverse conjugate
transpose. The local group is therefore exactly
\(\mathrm{GL}_N(L)\). The local level is \(K_L\), stable under
\(\sigma\), and its pullback from \(E\) is exactly \(K_F\),
because integrality and principal-unit congruences restrict correctly
along \(F\subset L\). The local embeddings and retractions are
the supported insertion and evaluation maps.

Fix strictly dominant \(t\). The two test functions are
\[
 f_t=1_{K_FN(t)K_F},\qquad f'_t=1_{K_LtK_L}.             \tag{4.2}
\]
They are bi-invariant under the respective levels. Moreover \(f'_t\)
is invariant under \(\delta\mapsto k^{-1}\delta\sigma(k)\) for
\(k\in K_L\), since \(\sigma(K_L)=K_L\).

For a global characteristic polynomial in the support required by
matching, its localization \(P_u\) satisfies Theorem 2.1. Let
\(z\in L[X]\) be the polynomial (2.4), and make an adelic
polynomial \(Z\) equal to \(z\) at \(u\) and \(1\) everywhere
else, including \(\bar u\). Concretely,
\[
 Z=1+\mathbf1_{\{u\}}(\widetilde z-1),                  \tag{4.3}
\]
where \(\widetilde z\) is any coefficientwise lift to finite
adeles. Such a lift exists by inserting each coefficient at \(u\).

We verify the universal determinant condition, not only the
condition at the original rank-\(N\) matrix. If a matrix \(M\) of
**any size** is killed by the global characteristic polynomial,
then \(M_u\) is killed by \(P_u\). The identity
\(\gcd(z,P_u)=1\) makes \(z(M_u)\) invertible by Bézout.
All other components of \(Z(M)\) are identity matrices. Hence
\(\det Z(M)\) is an invertible finite idele supported at \(u\),
and its norm to \(E\) is supported at \(w\). Equation (4.1)
therefore gives
\[
 \mu\bigl(N_{E'/E}\det Z(M)\bigr)=1.                  \tag{4.4}
\]
There is no infinite-product issue: this insertion has one-place
support.

Coefficientwise twisted polynomial norm in (4.3), evaluated at a
unitary \(\gamma\) killed by the characteristic polynomial, is
\(\gamma_u\) at \(u\), by Theorem 2.1(1), and identity elsewhere.
Its quotient by its adjoint is consequently \(\gamma\) on
\((u,\bar u)\) and identity off that pair. Indeed at \(\bar u\)
the quotient is the inverse conjugate transpose of \(\gamma_u\),
which is \(\gamma_{\bar u}\) by unitarity. Together with (4.4),
this is the precise one-side `IsNormRoot` condition.

Likewise the root quotient
\(a=Z(\gamma)Z(\gamma)^{*-1}\) has \(u\)-component
\(z(\gamma_u)\), the paired inverse conjugate transpose at
\(\bar u\), and identity elsewhere. For a base-changed \(\gamma\),
Theorem 2.1(2) proves equality of the two indicator values in
(4.2). For every supported \(\delta\) of twisted norm
\(\gamma\), Theorem 2.1(3) gives \(a^{-1}\delta\in K_L\) at
\(u\), and hence at its paired unitary component as well.
These are the two matching-root assertions. The trace-one
coboundary in Section 3 inserts at the same pair and is identity
off it, giving precisely the required local cocycle splitting.
Thus all the source `IsLocalMatching` hypotheses at this protected
place have now been constructed.

Apply the existing specific-level trace-transfer theorem to these
data. The commutation and matching-family stability hypotheses
follow from multiplication of dominant operators: a dominant
diagonal times a strictly dominant one is strictly dominant.
The remaining nonzero-trace input is also explicit. On any relevant
finite-dimensional joint generalized eigenspace containing the
original form, a fixed strictly dominant raw operator has the
single generalized eigenvalue
\(D_F(Nt_0)\chi_\theta(Nt_0)\ne0\). Its trace is this scalar
times the positive dimension, so is nonzero. This supplies the
source `HasNonzeroTraceAround` condition, including the auxiliary
stable subspaces used in spectral extraction.

To identify the transferred eigenvalues, use Haar measures giving the
level subgroups volume one. The raw dominant double-coset operator
is the averaging operator multiplied by
\[
 D_L(t)=\prod_{i<j}|t_j/t_i|_L.
\]
Normalized absolute values satisfy
\(|N_{L/F}x|_F=|x|_L\), so \(D_F(Nt)=D_L(t)\). For the
torus character
\(\chi_\theta(t)=\prod_i\theta_i(t_i)|t_i|^{N-1-i}\), the
matched raw eigenvalue is therefore
\[
 D_F(Nt)\chi_\theta(Nt)
   =D_L(t)\chi_{\theta\circ N}(t).                     \tag{4.5}
\]
Spectral extraction from the trace identity produces a nonzero
upstairs eigenform with these common eigenvalues for strictly
dominant \(t\), preserving the weak base-change Hecke system away
from the protected place.

For a merely dominant \(s\), choose one strictly dominant
\(t_0\). Both \(t_0\) and \(st_0\) are strictly dominant.
Dominant averaging operators satisfy \(A_sA_{t_0}=A_{st_0}\).
Their eigenvalues at \(t_0\) are nonzero, so cancellation gives
\(A_s f'=\chi_{\theta\circ N}(s)f'\). This proves the exact
source conclusion
\[
 \theta'_i=\theta_i\circ N_{L/F}\quad\text{for every }i, \tag{4.6}
\]
with the normalization in (3.4) of the split attachment chapter.
It preserves the full torus character and its individual component
characters; equality of only an unordered Satake multiset would
not suffice for this step.

The finite-product-type-to-sorted-Iwahori extraction remains a
separate representation-theoretic supplier. The present note
constructs the dominant local matching and its eigencharacter
transfer under the explicit Step and protected-place hypotheses.

## Source crosswalk

| Pinned source | Relevant material | Git blob SHA |
| --- | --- | --- |
| `grh/src/Lib/LocalGL/Iwahori/ParahoricStructure.lean` | finite conjugate-subgroup intervals, 699--754; compactness diagonalization, 755--811 | 08cddd361feb0d96e99ffcaa1a074f86189b6b9e |
| `grh/src/Lib/GaloisRep/BaseChange/IwahoriEigenforms.lean` | norm-root structure, 317--340; universal double-coset matching, 343--433; global insertion, 590--729 | 63be7acd09541c80cf00b11e6bfe33ade5dcae8d |
| `grh/src/Lib/LocalGL/Iwahori/HeckeDegrees.lean` | dominant double-coset degree and averaging normalization | 4bfc4da3628c746b24e28d1f452358305cb303ad |

The proofs here are ordinary arguments reconstructed from the stated
local objects. The pinned source was read to identify all required
quantifiers and normalizations; no imported declaration is used as
a substitute for an argument.
