# A shorter theta-and-jet route to the selected degree bound

## Status and scope

The determinant part of the actual logarithmic tangent estimate admits
a short proof using leading integral derivatives, the product formula,
and the classical very ampleness of the third power of an ample line
bundle on an abelian variety. The required tensor exponent can also be
reduced from order \((g^2+h)^2\) to order
\(g+h+g\log(2+g+h)\).

These are proved reductions. The arithmetic construction of the integral
theta sections, with their prescribed metrics and uniform bounds at
every finite prime, remains a geometric input. In particular this note
does not close W10 or certify all upstream source proofs.

Write \(\operatorname{av}_K\) for the average over all
\([K:\mathbf Q]\) complex embeddings, with conjugate embeddings counted
separately. Degrees are ordinary normalized Arakelov degrees, and
all lengths below are norms, not squared norms.

## 1. Leading integral derivatives and one determinant

Let \(\mathcal G\) be a group scheme over \(\mathcal O_K\), with identity
\(e\), and let \(\mathcal L\) be a line bundle rigidified at \(e\).
An integral invariant tangent vector \(x\) gives a derivation \(D_x\)
on regular functions. Take integral sections \(s_1,\ldots,s_r\) of
\(\mathcal L^{\otimes n}\). On the generic fibre choose a local frame
at \(e\) whose value is the prescribed rigidification, and let \(f_a\)
be the functions representing these sections. Set
\[
 J_i(c)=\sum_{a=1}^r c_a D_x^i f_a(e)
       \quad(c\in K^r),\qquad
 W_i=\bigcap_{j<i}\ker J_j.
 \tag{1.1}
\]
The derivatives in (1.1) are **not divided by \(i!\)**.

For every \(c\in W_i\cap\mathcal O_K^r\),
\[
 J_i(c)\in\mathcal O_K.
 \tag{1.2}
\]
Indeed, at a finite prime choose an integral local frame near the
identity and normalize its value at the identity to the rigidification
by a unit. Its representing functions and their invariant derivatives
are integral. Changing to the generic frame multiplies their sum by
a function whose value at the identity is one. All terms in the
Leibniz formula except the \(i\)-th derivative vanish when the earlier
derivatives vanish. The leading derivative is therefore unchanged.
This proves (1.2) at every finite prime.

The same observation applies to a holomorphic frame with the same value
at the identity. Thus the leading algebraic derivative equals the
leading derivative in the canonical Gaussian theta frame. No choice
of divided powers, integral Taylor coefficients, or extra factorial
denominator is involved.

**Integral flag lemma.** Let \(J_0,\ldots,J_k\) be independent \(K\)-linear
forms on \(K^r\), with \(W_i\) as in (1.1), and suppose (1.2) holds.
If
\[
 \|J_i|_{W_i\otimes_\sigma\mathbf C}\|_{\rm op}\le A_{i,\sigma},
 \qquad A_{i,\sigma}>0,
 \tag{1.3}
\]
for the standard Euclidean metric on \(\mathbf C^r\), then
\[
 0\le\sum_{i=0}^k\operatorname{av}_K\log A_{i,\sigma}.
 \tag{1.4}
\]

To prove this, localize at a finite prime. The saturated flag
\(W_i\cap\mathcal O_{K,v}^r\) has a basis adapted to its successive
rank-one quotients. In that basis the row matrix of the \(J_i\)
is triangular in its first \(k+1\) columns and zero in the remaining
columns. Each diagonal entry is integral by (1.2). Consequently every
coordinate of \(J_0\wedge\cdots\wedge J_k\) in the original integral
basis is integral. Choose a nonzero coordinate \(c\in\mathcal O_K\).
Gram--Schmidt on the rows gives
\[
 |\sigma(c)|
 \le\|J_0\wedge\cdots\wedge J_k\|_\sigma
 =\prod_{i=0}^k\|J_i|_{W_i\otimes_\sigma\mathbf C}\|_{\rm op}
 \le\prod_{i=0}^k A_{i,\sigma}.
\]
The product formula in the form
\(|N_{K/\mathbf Q}(c)|\ge1\) proves (1.4).
Localization of (1.2) is valid because each kernel intersection is a
finitely generated module and localization commutes with these kernels.

## 2. Jet rank follows from very ampleness

Let the generic fibre \(A/K\) be an abelian variety of dimension
\(g\ge1\), and let \(L\) be ample. Fix a nonzero integral tangent
vector \(x\). At an embedding \(\sigma\) write
\(\ell_\sigma=\|x\|_\sigma>0\).

Suppose \(n=3k\), \(k\ge1\), and the integral sections
\(s_1,\ldots,s_r\) span \(H^0(A,L^{\otimes n})\) over \(K\).
Assume that in the canonical theta frame, for every \(c\in\mathbf C^r\),
\[
 |f_c(zx)|\le
 \sqrt r\,M_\sigma\|c\|_2
       \exp\!\left(\frac{n\ell_\sigma^2|z|^2}{2}\right),
 \qquad M_\sigma>0.
 \tag{2.1}
\]
For the actual Hodge metric, \(\ell_\sigma^2=\pi H_\sigma(x,x)\);
the weight of \(L^{\otimes n}\) is
\(\exp(-\pi nH_\sigma(w,w)/2)\). Thus (2.1) uses the actual
ordinary norm and introduces no further factor of \(\pi\).

The classical theorem that \(L^{\otimes3}\) is very ample supplies
sections \(u_0,u_1\) with \(u_0(e)\ne0\), \(u_1(e)=0\), and
\(D_x(u_1/u_0)(e)\ne0\). They may be chosen over \(K\):
the evaluation map and its first differential in the \(K\)-rational
direction \(x\) are nonzero \(K\)-linear maps.
For \(0\le i\le k\), the section
\[
 u_0^{\,k-i}u_1^i\in H^0(A,L^{\otimes3k})
 \tag{2.2}
\]
has exactly order \(i\) along the formal curve \(\exp(zx)\).
Consequently the jet rows \(J_0,\ldots,J_k\) of the supplied spanning
sections are independent. The sections in (2.2) need not themselves be
integral; they are used only to prove generic rank.

For \(1\le i\le k\), Cauchy's formula on the circle of radius
\(\sqrt{i/n}/\ell_\sigma\), followed by \(i!\le i^i\), gives
\[
 |f_c^{(i)}(0)|
 \le\sqrt r\,M_\sigma\|c\|_2
       \bigl(\sqrt{enk}\,\ell_\sigma\bigr)^i.
 \tag{2.3}
\]
The same bound for \(i=0\) follows from (2.1) at zero.
On \(W_i\) these are the leading derivatives in (1.1).
The integral flag lemma therefore gives, with
\(U=\operatorname{av}_K\log M_\sigma\),
\[
 \boxed{\quad
 -\operatorname{av}_K\log\ell_\sigma
 \le \frac12\log(enk)+\frac{\log r+2U}{k}.
 \quad}
 \tag{2.4}
\]
Indeed the two sums to divide are \(k+1\) and \(k(k+1)/2\).

The generator count in (2.4) is exact. If
\(d_L=h^0(A,L)\), then
\(\dim H^0(A,L^{\otimes n})=n^g d_L\).
For a spanning family of that cardinality, (2.4) contains the
additional term \(\log d_L/k\). The next section uses the principal
case \(d_L=1\). It does not apply a single section's \(m\)-torsion
orbit of size \(m^{2g}\) to a nonprincipal polarization.

The classical very-ampleness statement is Theorem 2.2.3, page 13, of
A. Genestier and B.-C. Ngô, *Lectures on Shimura varieties*
([author-hosted PDF](https://www.math.uchicago.edu/~ngo/Shimura.pdf)).
Its hypothesis is simply an ample line bundle on an abelian variety;
the same page explains the translation-divisor argument and points to
Mumford's full proof. It makes no arithmetic-integrality assertion.

## 3. A smaller allowed theta power

Assume the actual construction supplies, for every integer \(m\ge1\)
and after a finite number field extension, \(r=m^{2g}\) integral
sections spanning \(L^{\otimes m^2}\). Their supremum bounds must be
the same \(M_\sigma\) as those of the original theta section, pulled
back through the embeddings. In particular no factor \(m^2\) may be
inserted in \(\log M_\sigma\). This uniformity is an input, not a
consequence of very ampleness.

Let \(h\ge0\), \(A_0,B_0\ge0\), and suppose
\[
 U\le h/2+A_0g+B_0g\log Y,\qquad Y=2+g+h.
 \tag{3.1}
\]
Put
\[
 \begin{split}
 Z&=1+g+h+2A_0g+2B_0g\log Y,\\
 a&=\lceil\sqrt Z\rceil,\qquad
 m=3a,\qquad n=m^2=9a^2,\qquad k=n/3=3a^2.
 \end{split}
 \tag{3.2}
\]
Here \(m\) is the torsion order; \(n=m^2\) is the tensor exponent.
The choice \(3\mid m\) makes \(n=3k\) exactly. There is no residual
power of \(L\) requiring an additional nonvanishing section.

Since \(Z\ge1\),
\[
 3Z\le k\le12Z,\qquad m\le6\sqrt Z,\qquad n\le36Z.
 \tag{3.3}
\]
Using \(r=n^g=(3k)^g\), (2.4) becomes
\[
 -\operatorname{av}_K\log\ell_\sigma
 \le\log k+\tfrac12\log(3e)
       +\frac{g\log(3k)+2U}{k}.
 \tag{3.4}
\]
Because \(\log(3k)>1\) and
\(g+2\max(U,0)\le Z\), the last term is at most
\(\tfrac13\log(3k)\). Therefore
\[
 \boxed{\quad
 -\operatorname{av}_K\log\ell_\sigma
 \le\frac43\log(12Z)+\frac56\log3+\frac12.
 \quad}
 \tag{3.5}
\]

For an explicit uniform logarithmic bound, let
\[
 C_0=1+2A_0+2B_0,\qquad
 C_{\rm line}=\frac83+\frac43\log(12C_0)
                  +\frac56\log3+\frac12.
 \tag{3.6}
\]
As \(Y\ge3\), \(\log Y\ge1\) and
\[
 Z\le C_0Y\log Y,\qquad
 \log Z\le\log C_0+2\log Y.
 \tag{3.7}
\]
Thus (3.5) is at most \(C_{\rm line}\log Y\).

The tensor exponent needed here satisfies
\[
 n\le36\{1+g+h+2A_0g+2B_0g\log(2+g+h)\}.
 \tag{3.8}
\]
The inspected source instead chooses
\(m=3\lceil2+g^2+h\rceil\).
Both choices are allowed by the same integral-section theorem.
The smaller choice proves the same logarithmic estimate with a
shorter numerical argument; it does not weaken any norm or
integrality condition.

All normalized embedding averages used above are invariant under
finite field extension when the metric and bounds are pulled back.
For the actual construction this is a required same-data isometry,
not an arbitrary replacement of the integral tangent lattice.

## 4. Pass directly to the selected sum

Let \(\bar V\) be the prescribed tangent lattice of rank \(g>0\),
ordinary normalized degree \(d\), and put \(h=\max(-d,0)\).
Assume the preceding theta construction and its bounds are available
after every finite field extension, with the same constants and
isometric pullback of \(\bar V\).

The absolute Siegel input used in the source has the following precise
consequence: for each nonzero sublattice \(F\subset V\), some finite
extension and nonzero integral vector \(x\) in the extended tangent
lattice satisfy
\[
 \widehat\mu(F)-\tfrac12\log g-1
 \le-\operatorname{av}\log\|x\|.
 \tag{4.1}
\]
Applying (3.5)--(3.7) to that very vector gives
\[
 \widehat\mu(F)
 \le C_{\rm line}\log(2+g+h)+\tfrac12\log g+1
 \le(C_{\rm line}+\tfrac32)\log(2+g+h).
 \tag{4.2}
\]
The weaker selected-sum hypothesis (1.3) of
[the selected eigenspace note](selected-eigenspace-degree.md) follows
by multiplying (4.2) by each actual selected rank and summing.
No separate assertion about the whole Harder--Narasimhan filtration
is needed. Rank-zero selected lattices contribute zero. If the
ambient abelian tangent rank is zero, the selected sum is zero and
none of the theta or Siegel steps is invoked.

Equation (4.1) and preservation of the actual metric under extension
are explicit arithmetic inputs here. This note does not replace
them with an unnamed assertion about short vectors in a different
Hermitian lattice.

## 5. What remains arithmetic at the finite primes

The actual supplier has two separate arithmetic steps:

- A primitive integral theta section with mean logarithmic
  square-mean norm at most \(h/2+C_1g\), followed by the supremum
  estimate giving (3.1), with
  \(A_0=C_1\) and \(B_0=C_3(1+\log(1+C_1))\).
- For every \(m\), integral normalized torsion translates spanning
  \(L^{\otimes m^2}\) and retaining the original supremum bounds.

The local conclusion at a degeneration has an elementary final step.
If \(Q\) is a nonnegative quadratic form on a lattice, \(b_Q\) its
polar form, \(y\) a torsion label, and \(N\ge1\), then
\[
 Q(\chi)+\frac{b_Q(y,\chi)}N+\frac{Q(y)}{N^2}
       =\frac{Q(N\chi+y)}{N^2}\ge0.
 \tag{5.1}
\]
Thus, if the terms in the normalized theta expansion at that torsion
point have valuations bounded below by the left side of (5.1),
their convergent nonarchimedean sum has nonnegative valuation.
The valuation ring is closed, so passage from finite sums is valid.

This is the completing-the-square step used by the actual source.
The geometric work is the identification of the **same rigidified
torsion frame** and the coefficient valuation bound for the **same
integral theta section**, together with the comparison between its
primitive determinant value and its archimedean square-mean norm.
The square identity does not establish those identifications.
No counterexample to them is claimed here.

The first arithmetic step has also been located beyond its wrapper:
for a primitive integral theta section and an integral Lie basis, the
source applies a theorem making its prescribed key determinant a unit
over a discrete valuation ring. This theorem assumes the determinant
rule's homogeneity, functoriality, special-fibre unit condition,
theta-one law and exact archimedean norm. Its proof passes through a
square construction and a PEL moduli model. Reading the wrapper does
not identify this entire package with a classical matrix lemma or
verify that geometric comparison independently.

### Pinned implementation dictionary

All source references below are at
\(\texttt{jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de}\).
The accompanying checker records whole-file Git/SHA256 integrity and
the exact bounded excerpt hashes. It is not a Lean replay.

| Source module | Bounded lines | Exact role |
|---|---:|---|
| IsThetaMeanSquareNorm | 17–24, 51–66, 77–87, 98–131 | Rigidified torsion value, Gaussian norm, actual data and height |
| SlopeBoundSt | 69–76 | Proper, ample and trivial polarization kernel |
| RelAmpleAndKTrivIff | 17–23 | Trivial kernel means only the identity has trivial translation difference |
| ExistsIntegralJetBasis | 102–174, 239–276 | Undivided invariant derivatives and leading-jet integrality |
| IntegralFlagEmbeddingCriterion | 263–351 | The precise flag determinant contract |
| LineOfKeyDegree | 196–267, 269–375 | Gaussian bound with the ordinary \(\pi H\) norm, old level and mean bounds |
| ExistsThetaSectionsBounded | 403–468 | Exactly \(m^{2g}\) integral sections of \(L^{m^2}\), same bounds and full span |
| ShortVectorOfSubmodule | 249–324 | Exact absolute Siegel consequence (4.1) |
| SlopeBoundOfLargeDegreeLine | 117–142 | Isometric extension and transfer of the actual vector |
| PolarizedDataFieldExtensionStatement | 12 | Preserved rank, height, full integral span and the same Hermitian form |
| KeyDegreeOfBadReduction | 223–302 | Primitive determinant value and small mean theta norm |
| KeyBadReductionHolds | 18 | Exact supplier, rather than a classical slope citation |
| HodgeTatePoints.LieMultComp | 139–160 | Primitive section, integral Lie basis and the prescribed determinant rule |
| TorsionValueIntegral | 476–510, 679–732 | Same torsion frame and local-to-global integrality |
| ExistsWeightZeroSectionUnitIntegralTorsionPoint | 39–63 | The actual quadratic completion (5.1) |

On the characteristic-zero generic fibre, the trivial polarization
kernel in the second and third rows is the principal-polarization
condition. Equivalently, the usual degree formula for an ample
polarization gives \(h^0(L)=1\). Independently of terminology,
the displayed \(m^{2g}\)-section spanning contract itself forces that
dimension in the classical abelian-variety setting.

The surviving construction problem is the arithmetic theta input in
Section 5, with its actual uniformity and metric normalization.
Sections 1--4 show precisely what it would supply, using shorter
ordinary mathematics and a substantially smaller allowed tensor power.
