# Integral CM eigenframes from relative trace duality

## Result and scope

The finite-place scaling of a complex multiplication eigenframe is
exactly the relative different. A short trace-dual-basis proof supplies
the integral calculation, including ramified primes. It replaces the
longer coordinate calculation once the prescribed product frame has
been identified with the actual tangent lattice. That identification,
the existence of the CM point and the archimedean period evaluation
remain separate geometric inputs.

Together with [vertical line rigidity](determinant-torsion-rigidity.md),
the result separates two questions cleanly: why the finite norm is
constant on a connected fibre, and what that constant is at a CM point.
Neither statement permits replacing the CM host by a ramified quadratic
field or choosing a different integral model.

## 1. The exact eigenlattice

Let \(F\subset E\) be number fields, let \(\ell\) be a rational prime,
and put
\[
 A=\mathcal O_F\otimes\mathbf Z_{(\ell)},\qquad
 B=\mathcal O_E\otimes\mathbf Z_{(\ell)}.
\]
Both rings are semilocal Dedekind domains. The finite projective
\(A\)-module \(B\) is free. Let \(R\) be a discrete valuation ring
with fraction field \(K\) of characteristic zero, with a prescribed
map \(A\to R\), and suppose \(K\) splits \(E/F\) relative to this
map. Write
\[
 M=R\otimes_A B\subset K\otimes_F E.
\]
For an embedding \(\sigma:E\to K\) extending the prescribed map
on \(F\), let \(e_\sigma\) be the corresponding primitive
idempotent of the split algebra. All images \(\sigma(B)\) lie in
\(R\), since \(R\) is integrally closed. If \(\mathfrak D_{E/F}\)
denotes the relative different, then
\[
 \boxed{\quad
 M[\sigma]:=\{m\in M:bm=\sigma(b)m\text{ for all }b\in B\}
       =\bigl(\sigma(\mathfrak D_{E/F})R\bigr)e_\sigma.
 \quad}                                                    \tag{1}
\]
Here the different is localized at \(\ell\); extending its image to
\(R\) gives a principal ideal. If \(d_\sigma\) generates that ideal,
then \(d_\sigma e_\sigma\), not generally \(e_\sigma\), is an
integral eigenbasis.

**Proof.** Choose an \(A\)-basis \(b_1,\ldots,b_f\) of \(B\),
and its trace-dual basis \(b_1^*,\ldots,b_f^*\) in \(E\), so
\(\operatorname{Tr}_{E/F}(b_i b_j^*)=\delta_{ij}\). The
\(A\)-span of the dual basis is the inverse different
\(\mathfrak D_{E/F}^{-1}\). This is the trace definition of the
complementary module; see the Stacks Project, Tag 0BW0.

In the splitting algebra,
\[
                   e_\sigma=\sum_i\sigma(b_i^*)b_i.       \tag{2}
\]
Indeed, the matrix with entries \(\tau(b_i)\), indexed by the
embeddings \(\tau\), has inverse given by the transpose of the
dual-basis matrix. Evaluating the right side at \(\tau\) therefore
gives \(1\) for \(\tau=\sigma\) and \(0\) otherwise.

Every generic \(\sigma\)-eigenvector is \(c e_\sigma\). Since
the \(b_i\) form an integral \(R\)-basis of \(M\), (2) gives
\[
 c e_\sigma\in M
 \ \Longleftrightarrow\ c\sigma(b_i^*)\in R\text{ for all }i
 \ \Longleftrightarrow\ c\sigma(\mathfrak D_{E/F}^{-1})R\subset R.
\]
An invertible fractional ideal remains invertible after extension to
\(R\). The last condition is precisely
\(c\in\sigma(\mathfrak D_{E/F})R\), proving (1). No integral
idempotent, division by a group order, or discarded ramification
multiplicity is used. \(\square\)

The formula applies to each copy in \(M^r\). It also commutes with
flat extension of the valuation ring, because the eigenlattice is the
kernel of the finitely many equations \(b_i-\sigma(b_i)\), and the
different ideal extends to the same ideal in the new ring. Ordinary
valuation orders scale by the ramification index; normalized orders,
with \(v(\ell)=1\), do not change.

If the local integer ring has a monogenic presentation
\(B=A[\alpha]\) with minimal polynomial \(P\) and a chosen root
\(\theta\), the formula is particularly transparent:
\[
 e_\theta=\frac{P(X)}{(X-\theta)P'(\theta)},\qquad
 P'(\theta)e_\theta=\frac{P(X)}{X-\theta}.
\]
The latter vector has integral coefficients and leading coefficient
one. Thus it is primitive even when \(P'(\theta)\) is not a unit.
This example illustrates the scaling; the proof of (1) requires no
monogenic presentation.

## 2. Equal conjugate norms without a real generator

Let \(E\) be a CM field containing
\(F=\mathbf Q(\sqrt{-d})\), with
\(\mathfrak D_{F/\mathbf Q}=(\sqrt{-d})\). For this local
calculation, \(E/E^+\) need not be unramified. Different ideals
multiply in a tower. This follows directly from trace duality: locally
a generator of the inverse different for the lower extension multiplies
the inverse different for the upper extension, since field traces
compose. Inverting the fractional ideals gives
\[
 \mathfrak D_{E/\mathbf Q}
    =\mathfrak D_{E/F}\mathfrak D_{F/\mathbf Q}\mathcal O_E.
                                                               \tag{3}
\]

The ideal \(\mathfrak D_{E/F}\) is conjugation-invariant.
Indeed, if \(x\) belongs to its inverse, then for every
\(b\in\mathcal O_E\),
\[
 \operatorname{Tr}_{E/F}(b\bar x)
    =\overline{\operatorname{Tr}_{E/F}(\bar b x)}
                           \in\mathcal O_F.
\]
Thus the inverse different, and hence the different, is preserved.
Choose any generator \(\delta\in E^\times\) of its localization
in the semilocal ring \(B\) at all primes above \(\ell\). Since
\(B\) is itself conjugation-invariant,
\[
             \bar\delta/\delta\in B^\times.              \tag{4}
\]
Every \(\ell\)-adic embedding sends a unit of \(B\), together
with its inverse, to integral elements. Equations (3)–(4) therefore give
\[
 \log|j\delta|
   =\log|j\mathfrak D_{E/\mathbf Q}|
        -\log|j\sqrt{-d}|,
 \qquad \log|j\bar\delta|=\log|j\delta|                 \tag{5}
\]
for every \(j:E\to\mathbf C_\ell\). Localizing at all primes
above the same rational prime is what makes the conjugation argument
valid; a choice at only one nonstable prime would not suffice.

For the prescribed host, the stronger finite unramifiedness assumption
also gives \(\mathfrak D_{E/\mathbf Q}
=\mathfrak D_{E^+/\mathbf Q}\mathcal O_E\). Choosing a semilocal
generator \(\delta_0\in E^+\) then gives the particular generator
\(\delta_0/\sqrt{-d}\), with \(\bar\delta=-\delta\).
This is a convenient choice, but it is unnecessary for (5). The local
norm calculation therefore has fewer hypotheses than the global host
construction. None of that construction's separate host conditions is
removed here.

For an exact example, take \(E=\mathbf Q(\zeta_8)\) and
\(F=\mathbf Q(i)\), where \(i=\zeta_8^2\). The integer ring is
\(\mathbf Z[\zeta_8]\): the polynomial of \(\zeta_8-1\) is
Eisenstein at two, and the discriminant \(256\) has no other prime
factor. The relative polynomial is \(X^2-i\), so
\(\delta=2\zeta_8\) generates its different and
\(\bar\delta/\delta=-i\). The absolute and lower differents are
generated by \(4\zeta_8^3\) and \(2i\), respectively, giving
\(|\delta|_2=(1/4)/(1/2)=1/2\). The primitive integral
eigenvector is \(X+\zeta_8\). Nevertheless \(E/E^+\) is ramified
at two: \(E^+=\mathbf Q(\sqrt2)\) has discriminant \(8\), and
the relative discriminant norm is \(256/8^2=4\).
This illustrates the weaker local hypothesis, not a replacement host.

## 3. Application to the actual product-frame contract

Suppose the actual CM tangent lattice \(L\) has the integral basis
\[
       \{\rho(b_i)u_a:1\le a\le r\}
       \ \cup\ \{\rho(b_i)u'_b:1\le b\le s\},           \tag{6}
\]
where the \(b_i\) are the relative basis above, the \(u_a\) are
\(F\)-eigenvectors for the selected embedding, and the \(u'_b\)
have the conjugate \(F\)-action. The hypothesis in (6) is an equality
with the prescribed integral lattice, not just a generic basis or a
finite-index inclusion.

Each plus block in (6) identifies with \(R\otimes_{A}B\), and
each minus block with the scalar extension using the conjugate base
embedding. Over the fraction field the two \(F\)-characters are
distinct; hence a full \(\sigma\)-eigenvector has zero minus part.
Apply (1) to each plus block. If \(P_\sigma\) denotes the generic
eigenprojection, then
\[
       \{\sigma(\delta)P_\sigma u_a\}_{a=1}^r            \tag{7}
\]
is an integral basis of \(L[\sigma]\). Write
\(\bar\sigma=\sigma\circ\overline{(\cdot)}\). Similarly the conjugate
eigenlattice has basis
\(\{\bar\sigma(\delta)P_{\bar\sigma}u'_b\}_{b=1}^s\).
This proves the exact frame scaling used in the finite CM norm, with
no additional loss at primes dividing the discriminant, including two.

The pinned construction supplies (6) through a prime-to-\(\ell\)
product isogeny and its integral tangent comparison. The trace-duality
proof replaces the eigenlattice calculation after that comparison.
It does not justify an arbitrary isogeny: if its degree is divisible
by \(\ell\), the differential need not identify the integral lattices.
Nor does it construct the original CM point or prove its period formula.
After (7), frame covariance gives the finite value used in
[the exact determinant comparison](geometric-flat-determinant.md).

## 4. Verification and source correspondence

All Lean references are pinned to
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

| Source | Bounded ranges | Contract |
| --- | --- | --- |
| `AlgebraProofs.EigenLocalBasisLogNorm` | 38–80, 174–226 | Generic eigenprojection and the exact integral scaling contract. |
| `AlgebraProofs.DifferentTwistedGeneratorExists` | 46–57 | The relative-different generator and equal conjugate norms. |
| `GeometryProofs.CmPackProductFrame` | 27–42 | The actual integral tangent basis from the local product isogeny. |
| `GeometryProofs.CmPackPureNorm` | 129–158, 160–193, 234–291 | Integral-basis hypotheses, actual frame transport and scaling. |
| `GeometryProofs.FrameFunctionCmHeight` | 24–49, 50–114 | Use of those same frames in the finite norm. |
| `GeometryProofs.FlatDegreeHolds` | 60–118 | The remaining global CM-period assembly. |

The Stacks source for the trace-dual definition is
`stacks/stacks-project@a04446e57ec1fbc252a871afcec7752fb2807b14`,
`discriminant.tex:1417–1438,1477–1494` (Tag 0BW0).
The certificate authenticates these source bytes and bounded passages,
and checks the trace-dual and polynomial eigenprojector identities on
exact examples. The general proof is (1)–(7), not the finite checks.
No Lean kernel rebuild, boundary-family construction, or complete CM
period evaluation is claimed.
