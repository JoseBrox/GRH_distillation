# Selected-coset Shintani transfer for full finite product types

The squarefree Green factor in
[the finite Shintani chapter](lsernau-shintani-label-transfer.md)
can be combined with every repeated determinant block appearing in
the source label. This uses genuine representations of finite
semidirect products. No extra sign or division by the extension
degree is introduced.

The relevant classical induction identity is Shintani's Lemma 2-8
and its product formulation, Lemma 2-9, pp. 403–404 of *Two remarks
on irreducible characters of finite general linear groups*
(1976). We give the flag proof below in the forward-norm convention
used by our local matching functions.

## 1. Finite parabolic induction and the selected coset

Let \(k=\mathbb F_q\), \(k_d=\mathbb F_{q^d}\), and let \(F\)
be \(q\)-power Frobenius. Let \(\mathbf G=\mathrm{GL}_N\), with an
\(F\)-stable standard parabolic \(\mathbf P\) and Levi
\(\mathbf M=\prod_{a=1}^s\mathrm{GL}_{n_a}\).
The \(n_a\) are positive and sum to \(N\); zero blocks are omitted.

For each factor suppose that \(\chi_a\) is a genuine character of
\(\mathrm{GL}_{n_a}(k)\) and \(S_a\) is a genuine character of
\(\mathrm{GL}_{n_a}(k_d)\rtimes\langle F\rangle\) satisfying
\[
 S_a(u,F)=\chi_a(v)
 \quad\text{whenever}\quad
 uF(u)\cdots F^{d-1}(u)\sim v\in\mathrm{GL}_{n_a}(k).
 \tag{1.1}
\]
Here similarity may be checked over \(\overline k\). For matrices
over a finite field it determines the rational similarity class:
the elementary-divisor data can be read after scalar extension.

Tensor the \(S_a\) using their common \(F\)-action, inflate from
\(\mathbf M^{F^d}\rtimes\langle F\rangle\) to
\(\mathbf P^{F^d}\rtimes\langle F\rangle\), and induce to
\(\mathbf G^{F^d}\rtimes\langle F\rangle\). Write \(S\) for the
resulting character, and put
\[
 \chi=\operatorname{Ind}_{\mathbf P^F}^{\mathbf G^F}
           \left(\boxtimes_a\chi_a\right).
 \tag{1.2}
\]
Then
\[
 \boxed{\quad S(g,F)=\chi(b)
 \quad\text{if}\quad
 gF(g)\cdots F^{d-1}(g)\sim b\in\mathbf G^F.\quad}
 \tag{1.3}
\]
The restriction of \(S\) to \(\mathbf G^{F^d}\) is the parabolic
product of the restrictions of the \(S_a\).

### Proof, including the norm orientation

Lang's theorem for the connected group \(\mathrm{GL}_N\) supplies
\(x\in\mathrm{GL}_N(\overline k)\) with \(g=x^{-1}F(x)\).
Put
\[
 n=gF(g)\cdots F^{d-1}(g)=x^{-1}F^d(x),\qquad
 b_0=F^d(x)x^{-1}.
 \tag{1.4}
\]
Since \(F^d(g)=g\), one has
\[
 F(b_0)=F^{d+1}(x)F(x)^{-1}
       =F^d(x)g(xg)^{-1}=b_0.
 \tag{1.5}
\]
Thus \(b_0\in\mathbf G^F\) and \(b_0=xnx^{-1}\). It is rationally
conjugate to the \(b\) in (1.3), so it suffices to use \(b_0\).

The induced representation is a sum of fibers over flags of the
specified dimensions in \(k_d^N\). The trace of \(gF\) is the sum
of its fiber traces over the flags it fixes; cycles of length
greater than one contribute zero. These are precisely the flags
\(\mathcal L\) such that
\[
 F^d(\mathcal L)=\mathcal L,\qquad gF(\mathcal L)=\mathcal L.
\]
The map
\[
                 \mathcal L\longmapsto x\mathcal L
 \tag{1.6}
\]
is a bijection from them to the \(b_0\)-stable flags over \(k\).
Indeed \(F(x\mathcal L)=xgF(\mathcal L)=x\mathcal L\), and
\(F^d(x\mathcal L)=b_0x\mathcal L\). Conversely, if
\(\mathcal U\) is \(F\)-fixed and \(b_0\)-stable, then
\(x^{-1}\mathcal U\) satisfies both required equations.

For a fixed flag choose \(y\in\mathbf G^{F^d}\) taking the
standard flag to \(\mathcal L\). Then
\(a=y^{-1}gF(y)\in\mathbf P^{F^d}\), and its forward norm is
\(y^{-1}ny\). On every successive quotient, conjugation by \(xy\),
followed by a rational frame for \(x\mathcal L\), identifies this
norm with the corresponding Levi block of \(b_0\). Applying (1.1)
to each block makes the fiber trace equal to the corresponding
fiber trace in (1.2). Summation over the bijection (1.6) proves
(1.3). In particular there is no factor \(d\), \(1/d\), or sign.

This proves the selected-coset assertion for any \(d\) whenever
the factor extensions (1.1) are supplied. It makes no assertion
about a different generating coset without a corresponding input.

## 2. Determinant blocks, with their full rank multiplicity

Let \(\eta:k^\times\to\mathbb C^\times\) and \(t\ge1\). The
character \(\eta\circ\det\) of \(\mathrm{GL}_t(k)\) lifts to
the following one-dimensional representation:
\[
 S_{\eta,t}(a,F^j)
   =\eta\!\left(N_{k_d/k}(\det a)\right).
 \tag{2.1}
\]
Frobenius acts as the identity on this representation. Equation
(2.1) is multiplicative because the norm character is
Frobenius-invariant, and
\[
 S_{\eta,t}(a,F)
 =\eta\!\left(\det(aF(a)\cdots F^{d-1}(a))\right).
 \tag{2.2}
\]
Thus it satisfies (1.1) with exactly the required determinant
character on a block of rank \(t\). The integer \(t\) is unchanged.

Take now the source product type
\[
 Y=\Xi_c\circ\prod_a(\eta_a\circ\det_{\mathrm{GL}_{t_a}}),
 \tag{2.3}
\]
where \(\circ\) denotes finite parabolic induction, \(c\) is
squarefree, and \(\Xi_c\) is its Green label character.
The squarefree supplier gives the selected positive Shintani
extension of \(\Xi_{c/k_d}\); equation (2.1) gives the other
factors. Equation (1.3) therefore supplies a genuine extension
character \(S_Y\) whose restriction is
\[
 Y'=\Xi_{c/k_d}\circ
       \prod_a\bigl((\eta_a\circ N_{k_d/k})
                         \circ\det_{\mathrm{GL}_{t_a}}\bigr)
 \tag{2.4}
\]
and whose selected-coset value is \(Y(b)\).

For a linear label \(X-a\), the faithful-character calculation
in the squarefree chapter identifies the same root name \(a\)
over \(k_d\) with \(\eta_a\circ N_{k_d/k}\). Thus (2.4)
preserves the source's labels, including every repeated
determinant-block multiplicity.

## 3. Positivity and absorption do not require irreducibility

It is useful to allow a general genuine product character \(Y\).
Write \(Y=\sum_\pi m_\pi\chi_\pi\), with \(m_\pi\) nonnegative
integers. In a unitary representation of \(H=\mathbf G^F\),
\[
 B_Y=\sum_{h\in H}\overline{Y(h)}\,\rho(h)
 \tag{3.1}
\]
acts on the \(\pi\)-isotypic subspace by
\[
                     |H|\,m_\pi/\dim\pi.
 \tag{3.2}
\]
Thus it is positive semidefinite, and it has strictly positive
trace on any finite-dimensional invariant subspace where it is
nonzero. This is precisely the nonzero-trace input for the
local-to-global trace transfer. An irreducibility assertion about
the product character is unnecessary.

If \(\widetilde\rho\) has character \(S_Y\), the selected function
\[
 h\longmapsto S_Y(h,F)
       =\operatorname{tr}(\widetilde\rho(h)\widetilde\rho(F))
\]
is a linear combination of matrix coefficients of
\(\widetilde\rho|_{\mathbf G^{F^d}}\), whose character is \(Y'\).
Finite Schur orthogonality therefore makes convolution by its
complex conjugate kill every irreducible representation absent
from \(Y'\). Its nonzero image has nonzero \(Y'\)-character
projection. The support, compact-root matching and quotient checks
in the squarefree chapter apply unchanged. This proves labelled
automorphic transfer for the full type (2.3), and supplies exactly
the product type required by
[sorted Iwahori extraction](lsernau-iwahori-type-sorting.md).

## References and source boundary

- S. Lang, *Algebraic groups over finite fields*, American Journal
  of Mathematics **78** (1956), 555–563, §2, Theorem 1 and its
  surjectivity corollary. [Full paper](https://wstein.org/papers/bib/Lang-Algebraic_Groups_Over_Finite_Fields.pdf).
  Only surjectivity of \(x\mapsto x^{-1}F(x)\) for the connected
  general linear group is used.
- T. Shintani, *Two remarks on irreducible characters of finite
  general linear groups*, Journal of the Mathematical Society of
  Japan **28** (1976), 396–414, Lemmas 2-8 and 2-9.
  [Published full paper](https://www.jstage.jst.go.jp/article/jmath1948/28/2/28_2_396/_pdf).
  The induction identity was inspected in the full paper; the flag
  calculation above fixes the chosen forward-norm convention.
- C. Bonnafé, *On a theorem of Shintani*, Journal of Algebra
  **218** (1999), 229–245, Theorem 4.3.1(a).
  [Author's published PDF](https://imag.umontpellier.fr/~bonnafe/Travaux/shintani.pdf).
  The full theorem supplies the positive genuine extension used
  for the squarefree factor.

At the pinned readable revision
\(72fead102f663d5c7a407964a13dc0cf9d977207\), the application is in
Lib/GaloisRep/LocalGlobal/LabelCompatibility.lean, lines 398–409
and 449–460, with blob
\(12d0155551faca1c923b601e78e655692b1fdf16\).
It is the product-lift operation followed by labelled base change.
The result here supplies that finite matching step. Global prime-step
construction, Galois attachment and local crystalline descent are
separate assertions. No Lean replay is claimed.
