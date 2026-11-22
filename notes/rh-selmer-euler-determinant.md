# The upper Selmer comparison as a determinant

## Result and scope

The last length calculation in the graded upper comparison has an elementary
determinant proof. It applies to the actual finite multigraded weight module,
even when that module has integral torsion. It also keeps the exact generic
point multiplicities before replacing them by a power of two.

The result below reconstructs the numerical supplier in
`GradedModulesLength.HerbrandFinLen.th_holds`, including its stronger exact
identity. It does **not** supply the mixed-intersection lower comparison,
the eventual support theorem, the local multiplicity bound, or the arithmetic
construction of the marked deformation model. Those inputs are stated
separately. In particular, a determinant on a finite degree-zero algebra is
not by itself a bound for the negative-weight Selmer module.

All source contracts use `jsmorph/rh` at
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. The bounded ranges and hashes are
recorded in `certificates/rh-selmer-euler-determinant.json`.

## 1. Torsion cancels in a one-operator Euler characteristic

Let \(\mathcal O\) be a discrete valuation ring, \(F\) its fraction field,
\(\pi\) a uniformizer, and \(v_\pi(\pi)=1\). Let \(M\) be a finite
\(\mathcal O\)-module and \(u:M\to M\) an endomorphism whose extension to
\(M_F=M\otimes_{\mathcal O}F\) is invertible. Set

\[
\chi(u;M)=\ell_{\mathcal O}(\operatorname{coker}u)
           -\ell_{\mathcal O}(\ker u).
\]

**Proposition 1.** Both lengths are finite and

\[
\boxed{\chi(u;M)=v_\pi\det_F(u\mid M_F).} \tag{1}
\]

**Proof.** Put \(T=M_{\mathrm{tors}}\) and \(L=M/T\). The module \(L\) is
finite free and \(u_L\) is injective. The kernel-cokernel sequence for
\(0\to T\to M\to L\to0\) therefore gives

\[
\ker u_M=\ker u_T,\qquad
0\longrightarrow\operatorname{coker}u_T
\longrightarrow\operatorname{coker}u_M
\longrightarrow\operatorname{coker}u_L\longrightarrow0.
\]

Every endomorphism of a finite-length module has kernel and cokernel of equal
length, by applying additivity of length to its image. Thus
\(\chi(u;M)=\ell_{\mathcal O}(\operatorname{coker}u_L)\).
Smith normal form on the free module \(L\) identifies this last length with
the valuation of its determinant, proving (1). If \(M_F=0\), the determinant
of the zero-dimensional automorphism is \(1\), and both sides are zero.
No flatness assumption on \(M\) has been used. \(\square\)

Subtracting the kernel length is essential. For example, the zero
endomorphism of \(\mathcal O/\pi^n\) has cokernel length \(n\), whereas
its Euler characteristic and generic determinant valuation are both zero.

## 2. The exact sum over characteristic-zero points

Assume now that \(F\) has characteristic zero. Fix an algebraic closure
\(\overline F\) and an extension of \(v_\pi\). Let \(B\) be a Noetherian
local \(\mathcal O\)-algebra whose residue map is an isomorphism. Suppose
\(M\) is finite over \(B\) and \(B/\operatorname{Ann}_B M\) is finite
over \(\mathcal O\). Then \(M\) is finite over \(\mathcal O\), and every
finite-length \(B\)-subquotient of \(M\) has the same length over \(B\)
and \(\mathcal O\): its composition factors are the common residue field.

For an \(\mathcal O\)-algebra homomorphism
\(\sigma:B\to\overline F\), put

\[
m_\sigma(M)=
\ell_{B_{\ker\sigma}}(M_{\ker\sigma}).
\]

Only finitely many such characters have nonzero multiplicity. Let
\(\Sigma(M)\) be this finite set. For \(a\in B\), assume
\(\sigma(a)\ne0\) for every \(\sigma\in\Sigma(M)\).

**Proposition 2.** Multiplication by \(a\) has finite kernel and cokernel,
and

\[
\boxed{
\chi_B(a;M)=
\sum_{\sigma\in\Sigma(M)}m_\sigma(M)v_\pi(\sigma(a)),
\quad
\chi_B(a;M)=\ell_B(M/aM)-\ell_B(M[a]).} \tag{2}
\]

**Proof.** The finite-dimensional commutative algebra
\(D=(B/\operatorname{Ann}_B M)\otimes_{\mathcal O}F\) is a product of
local Artinian algebras \(D_i\), with finite residue extensions \(F_i/F\).
The extensions are separable because \(F\) has characteristic zero.
For each embedding \(F_i\hookrightarrow\overline F\), the corresponding
local summand after extending scalars has residue field \(\overline F\).
A composition series of the \(D_i\)-module \(M_i\) becomes a composition
series with the same number of factors on each such summand. This number is
\(m_\sigma(M)\); localization at \(\ker\sigma\) gives the same local
module before extending scalars.

On each factor of this series, multiplication by \(a\) acts as the scalar
\(\sigma(a)\). Consequently

\[
\det_F(a\mid M_F)
 =\prod_{\sigma\in\Sigma(M)}\sigma(a)^{m_\sigma(M)}.
\]

This equality is understood inside \(\overline F\); its right side lies
in \(F\). Nonzero scalar factors make the generic endomorphism invertible.
Apply Proposition 1 and equality of the two length normalizations. This
argument allows nilpotents and repeated eigenvalues. \(\square\)

There is no missing residue-degree factor in (2). Different embeddings
of the same field \(F_i\) occur separately in the sum. If
\(\mathcal O\) is a coefficient ring over \(\mathbb Z_p\), with
\(e_{\mathcal O}=v_\pi(p)\), set

\[
\lambda(M)=\ell_{\mathcal O}(M)/e_{\mathcal O},
\qquad v_p=v_\pi/e_{\mathcal O}.
\]

Dividing (2) by \(e_{\mathcal O}\) is precisely the normalized identity
used in the Selmer comparison. This convention is not restriction of
scalars length over \(\mathbb Z_p\).

If a finite set \(S\) contains \(\Sigma(M)\), if
\(m_\sigma(M)\le C\), and if \(v_\pi(\sigma(a))\ge0\) for every
\(\sigma\in S\), then (2) gives

\[
\chi_B(a;M)\le C\sum_{\sigma\in S}v_\pi(\sigma(a)). \tag{3}
\]

## 3. The finite module in the marked-model upper comparison

Here is the exact module to which (2) applies. Let
\(A=\bigoplus_{j\in\mathbb Z}A_j\) be the augmented graded
\(\mathcal O\)-algebra of the marked model, with \(B=A_0\). The rational
chart is chosen to kill the weight-zero equations. Write the
nonzero-weight equations as

\[
F_1,\ldots,F_r,F_*\in A_{-1},\quad G_1,\ldots,G_s\in A_{-2},
\quad E_1,\ldots,E_{r'}\in A_1,\quad E'_1,\ldots,E'_{s'}\in A_2.
\]

The rational formal chart is \(\varphi:A\to F[[z_1,\ldots,z_n]]\).
Define the three finite \(B\)-submodules of \(A\)

\[
N_0=A_{-2},\qquad N_1=A_2,\qquad
N_2=BF_*^2+A_{-2}^2A_2
\]

and their multigraded algebra

\[
\mathcal R=
\bigoplus_{\boldsymbol d\in\mathbb N^3}
N_0^{d_0}N_1^{d_1}N_2^{d_2}
t_0^{d_0}t_1^{d_1}t_2^{d_2}\subset A[t_0,t_1,t_2].
\]

The ideal \(J_\varphi\) consists of elements whose every coefficient
lies in \(\ker\varphi\). Let \(\mathfrak s\) be generated by

\[
F_i^2t_0,\quad G_jt_0,\quad E_k^2t_1,
\quad E'_lt_1,\quad F_*^2t_2,
\]

with the index ranges displayed above. The finite weight module is

\[
\boxed{M_{\boldsymbol d}=
\left(\mathcal R/(J_\varphi+\mathfrak s)\right)_{\boldsymbol d}.} \tag{4}
\]

Weight-zero equations annihilated by \(\varphi\) already belong to
\(J_\varphi\). They are not omitted constraints.

Let \(a\in B\) be the trace difference used in the upper comparison.
Let \(\mathcal T\) be its finite set of torus-orbit representatives among
points of the equation scheme on which some negative-weight and some
positive-weight function are nonzero. Put

\[
\Sigma=\{\xi|_B:\xi\in\mathcal T\}.
\]

This is a **set of distinct degree-zero characters**. Distinct torus
representatives need not yield distinct restrictions, and the exact
formula must not count a restriction twice.

The retained graded inputs state that, for every sufficiently large
\(\boldsymbol d\) in the componentwise order:

1. \(M_{\boldsymbol d}\) is finite over \(B\), and
   \(B/\operatorname{Ann}_B M_{\boldsymbol d}\) is finite over
   \(\mathcal O\).
2. Its generic support is contained in \(\Sigma\), and
   \(\xi(a)\ne0\), \(v_\pi(\xi(a))\ge0\) for \(\xi\in\mathcal T\).
3. Its local multiplicities satisfy
   \(m_\sigma(\boldsymbol d)\le2^{r+1+r'}\).
4. With \(T^-\) the integral negative-weight conormal quotient,
   the mixed-intersection lower comparison gives
   \(2^{r+r'}\ell_{\mathcal O}(T^-)
      \le\chi_B(a;M_{\boldsymbol d})\).

Item 1 and the support part of item 2 use the eventual annihilator theorem.
Item 3 uses the one-dimensional tangent bound at the two-sided points and
the successive squaring of the \(r+1+r'\) equations. Item 4 uses the
three multigraded directions and the Smith exponents of the negative
cotangent equations. None follows just from finite degree-zero algebra.

Proposition 2 now gives the exact intermediate inequality

\[
\boxed{\ell_{\mathcal O}(T^-)
\le 2^{-r-r'}\sum_{\sigma\in\Sigma}
m_\sigma(\boldsymbol d)v_\pi(\sigma(a))
\le 2\sum_{\xi\in\mathcal T}v_\pi(\xi(a)).} \tag{5}
\]

The first inequality retains the actual point multiplicities. The second
uses item 3 and then nonnegativity to allow repeated restrictions in the
larger sum over \(\mathcal T\). There is no assertion that this coarse
step is uniformly strict. The conormal pairing gives
\(\ell_{\mathcal O}(S)\le\ell_{\mathcal O}(T^-)\); dividing (5) by
\(e_{\mathcal O}\) gives the correctly normalized strict Selmer bound.

## 4. What the classical multiplicity theorem supplies

The classical local formula is precise: for a finite module \(N\) over a
Noetherian local ring and \(I=(f_1,\ldots,f_q)\) with \(N/IN\) of finite
length, the alternating lengths of the Koszul homology equal the
degree-\(q\) Hilbert--Samuel multiplicity. The module-relative version
passes to the quotient by its annihilator. Primary references are
[Stacks, Theorem 43.15.5, tag 0AZZ](https://stacks.math.columbia.edu/tag/0AZZ)
and [Remark 43.15.6, tag 0B00](https://stacks.math.columbia.edu/tag/0B00),
checked on 2026-11-22.

This does not yet supply item 4. In (4), taking a fixed multidegree does not
turn the full sequence of positive-multidegree sections into endomorphisms
of one finite module: the Koszul maps connect different multidegrees.
The source first proves eventual finite-length homology, compares with a
flat leading-term quotient, extracts the factors \(\pi^{2c_i}\), and
computes a mixed finite difference in three directions. Ordinary local
Koszul positivity alone supplies neither that comparison nor its exact
constant \(2^{r+r'}\). A classical replacement must verify these graded
specialization and proper-intersection hypotheses; they remain explicit
suppliers here.

## 5. Bounded source audit and reproducible checks

The source contracts are:

| Contract | File under `CommutativeAlgebra/` | Lines |
|---|---|---:|
| Equal residue fields | `ResMapBijective.lean` | 9--13 |
| Local length, Euler characteristic, and three modules | `GradedModulesLength/ToDegInjective.lean` | 156--163, 187--218 |
| Exact point formula and its coarse bound | `GradedModulesLength/HerbrandFinLen.lean` | 83--99, 189--259 |
| Eventual finite annihilator and support | `GradedModulesLength/EventuallyMQGrFiniteAnnihilator.lean` | 77--123 |
| Local multiplicity after squaring | `GradedModulesLength/LocLenAPieceIdeal2LeTwoPow.lean` | 69--115 |
| Distinct restrictions and application | `GradedModulesLength/TwoSigned.lean` | 63--95 |
| Actual final quotient and both inequalities | `GradedModulesLength/AlgMemCoef.lean` | 92--143 |
| Retained mixed lower comparison | `GradedModulesLength/AdmissibleMonoIdeal.lean` | 191--237, 273--322 |

`scripts/check_rh_selmer_euler_determinant.py` verifies these source hashes
against the pinned atlas and checks (1) exactly on finite presentations
with free and torsion parts, arbitrary tested off-diagonal coupling, and
nonsemisimple generic operators. Cokernel orders are computed by maximal
minors; kernel orders are independently enumerated on the torsion part.
It also checks ramification normalization and records a repeated-eigenvalue
example. These finite checks supplement the proofs; they do not compute
an actual Selmer group, construct the growing model, or verify the retained
mixed lower comparison.
