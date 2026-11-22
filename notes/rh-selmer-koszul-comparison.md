# A short Koszul proof of the graded lower comparison

## Result and remaining input

The lower mixed-intersection comparison can be reconstructed from a short
graded prime-filtration argument. It proves eventual positivity, passage
to a quotient, and an exact scalar-extraction formula. Together with the
proved leading quotient and mixed count, it yields

\[
2^{r+r'}\sum_i c_i
\le\chi(\boldsymbol f; (\mathcal R/J_\varphi)/a)
\le\chi(a;\mathcal R/(J_\varphi+\boldsymbol f)). \tag{1}
\]

The remaining actual lower-side input is the precise admissibility
containment (12) below. No regular-sequence hypothesis or flatness of the
original deformation quotient is imposed. Flatness is used only for the
explicit leading quotient already proved free over \(\mathcal O\).
Eventual support and generic point multiplicity bounds remain separate
inputs to the determinant upper estimate.

Pinned source contracts refer to `jsmorph/rh` at
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. This note proves the stated
mathematics directly; the certificate distinguishes its ordinary proofs
from source-byte checks and finite computations.

## 1. Admissibility and finite Euler characteristics

Let \((B,\mathfrak m)\) be a Noetherian local ring. Let
\(R=\bigoplus_{\boldsymbol n\in\mathbb N^k}R_{\boldsymbol n}\) be a
standard finitely generated multigraded \(B\)-algebra: \(R_0=B\), and it
is generated over \(B\) by finitely many elements in the degrees
\(e_1,\ldots,e_k\). Let \(M\) be a finite \(\mathbb Z^k\)-graded
\(R\)-module, and put

\[
I_{\mathrm{irr}}=\prod_{i=1}^k(R_{e_i})R.
\]

All degree comparisons below are componentwise. A finite sequence
\(\boldsymbol f=(f_1,\ldots,f_q)\), with homogeneous elements of
degrees \(\delta_i\in\mathbb N^k\), is **admissible on \(M\)** if

\[
(\mathfrak m R I_{\mathrm{irr}})^N
\subset\operatorname{Ann}_R M+(f_1,\ldots,f_q)
\quad\text{for some }N\ge0. \tag{2}
\]

For \(\boldsymbol n\) sufficiently large, define

\[
\chi(\boldsymbol f;M)_{\boldsymbol n}
=\sum_{i=0}^q(-1)^i
\ell_B H_i(K_\bullet(\boldsymbol f;M))_{\boldsymbol n}. \tag{3}
\]

**Finiteness.** The Koszul homology modules are finite graded
\(R\)-modules, annihilated by both \(\operatorname{Ann}_R M\) and the
sections \(f_i\). Hence \(\mathfrak m^N I_{\mathrm{irr}}^N\)
annihilates them. For any finite graded module \(H\), standardness gives
\(H_{\boldsymbol n}=(I_{\mathrm{irr}}^N H)_{\boldsymbol n}\) for
\(\boldsymbol n\) sufficiently large: factor a product of \(N\)
degree-\(e_i\) generators for every coordinate from each coefficient
of a finite homogeneous generating set. Consequently
\(\mathfrak m^N H_{\boldsymbol n}=0\). Each graded piece is finite
over \(B\), and therefore has finite length. There are only finitely
many homology modules, so one common degree bound works in (3).

Admissibility passes to graded subquotients of \(M\), because their
annihilators contain \(\operatorname{Ann}_R M\). It also passes when
the ideal of sections is enlarged.

We use the shift convention \(M(-\delta)_{\boldsymbol n}
=M_{\boldsymbol n-\delta}\). The Koszul complex on a first element
\(f\) of degree \(\delta\) is
\([M(-\delta)\xrightarrow{f}M]\). Its two homology modules give

\[
\chi(f,\boldsymbol t;M)
=\chi(\boldsymbol t;M/fM)
 -\chi(\boldsymbol t;M[f](-\delta)) \tag{4}
\]

in all sufficiently large degrees. One may obtain (4) by filtering the
Koszul double complex by its first factor. Admissibility of the full
sequence implies admissibility of the tail on both displayed modules,
so the homology lengths used in this identity are finite. The same
argument shows that (3) agrees with the source's recursive definition.

For a graded exact sequence, Koszul complexes give a long exact homology
sequence. Thus \(\chi\) is additive whenever the full sequence is
admissible on the middle module. Permuting the sections does not change
\(\chi\), by the usual signed isomorphism of Koszul complexes.

## 2. Eventual positivity without regular sequences

**Proposition 1.** If \(\boldsymbol f\) is admissible on \(M\), then

\[
\chi(\boldsymbol f;M)_{\boldsymbol n}\ge0
\quad\text{for all sufficiently large }\boldsymbol n. \tag{5}
\]

**Proof.** Induct on the number of sections. The empty sequence gives
the nonnegative finite length of \(M_{\boldsymbol n}\).

At a fixed induction stage, take a finite graded prime filtration of
\(M\). Such a filtration requires no dimension bound: choose a
nonzero homogeneous element with maximal annihilator; its annihilator
is prime on homogeneous elements, and hence prime because
\(\mathbb Z^k\) admits a compatible total order. Noetherian induction
on graded submodules gives a finite filtration whose factors are shifts
of \(R/\mathfrak p\), with \(\mathfrak p\) homogeneous and prime.
Each factor inherits admissibility. Additivity and the shift rule reduce
the assertion to \(M=R/\mathfrak p\).

If \(I_{\mathrm{irr}}\subset\mathfrak p\), all sufficiently large
pieces of this module, and hence of its Koszul complex, vanish. Assume
instead that \(\mathfrak p\) is relevant, namely
\(I_{\mathrm{irr}}\not\subset\mathfrak p\). For each coordinate
choose \(x_i\in R_{e_i}\setminus\mathfrak p\). Products of these
elements supply a nonzero element of every degree
\(\delta\in\mathbb N^k\) in the domain \(R/\mathfrak p\).

Write the sequence as \((f,\boldsymbol t)\), with
\(\deg f=\delta\). If \(f\notin\mathfrak p\), it acts injectively
on \(R/\mathfrak p\), so (4) reduces the Euler characteristic to that
of the shorter sequence \(\boldsymbol t\) on \(M/fM\). Apply the
induction hypothesis.

If \(f\in\mathfrak p\), it acts as zero and the tail is already
admissible on \(M\): the first section adds nothing to
\(\operatorname{Ann}_R M\). Choose
\(g\in R_\delta\setminus\mathfrak p\). Formula (4) for the zero
section gives

\[
\chi(f,\boldsymbol t;M)_{\boldsymbol n}
=\chi(\boldsymbol t;M)_{\boldsymbol n}
 -\chi(\boldsymbol t;M)_{\boldsymbol n-\delta}.
\]

The exact sequence
\(0\to M(-\delta)\xrightarrow{g}M\to M/gM\to0\)
identifies this difference with
\(\chi(\boldsymbol t;M/gM)_{\boldsymbol n}\), which is eventually
nonnegative by the shorter-sequence induction. This proves (5).
Only finitely many filtration factors, sections, shifts, and inductive
applications occur; their degree bounds have a finite componentwise
maximum. Thus the argument gives one eventual range for the original
module. \(\square\)

The first section was varied only when the tail was already admissible.
There is no general invariance under varying a section. For example,
on \(\mathcal O[x]\) in positive degree the sections \(x\) and
\(\pi x\), both of degree one, have Euler characteristics \(0\)
and \(1\), respectively. The empty tail has infinite-length graded
pieces in this example.

**Corollary 2.** For a graded surjection \(M\twoheadrightarrow N\),
and a sequence admissible on \(M\), one has eventually

\[
\chi(\boldsymbol f;M)\ge\chi(\boldsymbol f;N). \tag{6}
\]

Indeed, the difference is the nonnegative Euler characteristic of the
kernel. Also, for a split list \((\boldsymbol f,\boldsymbol t)\)
admissible on \(M\),

\[
\chi(\boldsymbol f,\boldsymbol t;M)
\le\chi(\boldsymbol t;M/(\boldsymbol f)M) \tag{7}
\]

eventually. Remove the elements of \(\boldsymbol f\) successively in
(4), discarding only a nonnegative tail Euler characteristic. The tail
is admissible on each kernel because that kernel is killed by the
removed element. No regularity assumption is used.

## 3. Exact extraction of scalar powers

Let \(\pi\in B\) have degree zero, act injectively on a finite graded
module \(C\), and suppose every graded piece of \(C/\pi C\) has finite
\(B\)-length. Write
\(h(\boldsymbol n)=\ell_B(C/\pi C)_{\boldsymbol n}\).
Let \(y_1,\ldots,y_q\) have a common degree
\(\delta\in\mathbb N^k\), let \(b_i\ge0\), and let
\(\boldsymbol t\) be a further homogeneous sequence of nonnegative
degrees \(\epsilon_1,\ldots,\epsilon_v\). Assume
\((\pi^{b_1}y_1,\ldots,\pi^{b_q}y_q,\boldsymbol t)\) is admissible
on \(C\), where \(q\ge1\).

**Proposition 3.** For all sufficiently large degrees,

\[
\begin{split}
&\chi(\pi^{b_1}y_1,\ldots,\pi^{b_q}y_q,\boldsymbol t;C)\\
&\quad=\chi(y_1,\ldots,y_q,\boldsymbol t;C)
 +(\textstyle\sum_i b_i)
 \Delta_\delta^{q-1}\Delta_{\epsilon_1}\cdots
 \Delta_{\epsilon_v}h. \tag{8}
\end{split}
\]

Here \(\Delta_\gamma h(\boldsymbol n)=h(\boldsymbol n)
-h(\boldsymbol n-\gamma)\).

**Proof.** For homogeneous \(u,v\) of degrees \(\alpha,\beta\), use
the composable maps
\(C(-\alpha-\beta)\xrightarrow{v}C(-\alpha)\xrightarrow{u}C\).
Their ordinary kernel--cokernel sequence is

\[
0\to\ker v\to\ker(uv)\to\ker u\to
\operatorname{coker}v\to\operatorname{coker}(uv)\to
\operatorname{coker}u\to0.
\]

The shifts are those of the displayed maps. All six modules inherit
tail admissibility from the product sequence, since they are killed
by \(uv\). Applying additivity of the tail Euler characteristic and
then (4) gives

\[
\chi(uv,\boldsymbol t;C)_{\boldsymbol n}
=\chi(u,\boldsymbol t;C)_{\boldsymbol n}
 +\chi(v,\boldsymbol t;C)_{\boldsymbol n-\deg u}. \tag{9}
\]

All three complexes have finite-length homology in large degree when
the product sequence is admissible: replacing \(uv\) by either factor
enlarges the section ideal. This identity retains arbitrary torsion
kernels; it does not identify a cokernel length with an Euler
characteristic.

Take \(u=\pi\), whose degree is zero, and iterate (9). Since \(\pi\)
acts injectively, its Koszul factor reduces to \(C/\pi C\). All the
terms of every graded Koszul complex over \(C/\pi C\) have finite
length; their alternating lengths equal those of their homology.
Consequently that Euler characteristic depends only on the degrees
of the remaining sections and equals the corresponding backward
difference of \(h\). Peel off the \(b_i\) scalar factors one at a
time. In every contribution the other \(q-1\) elements still have
degree \(\delta\), regardless of their remaining scalar factors.
This gives the same difference in every term, proving (8).
Admissibility of each intermediate list follows from enlargement of
the initial section ideal; only finitely many operations are used.
\(\square\)

Combining (8) with (5) gives a lower bound by its explicit second term.
The possible higher Koszul homology of the unscaled sequence is fully
retained inside its nonnegative Euler characteristic.

For a concrete example with higher homology, take
\(C=\mathcal O[x,y]\), sections \(\pi^a x,\pi^b y\), and degree
\(d\ge1\). Writing \(m=\min(a,b)\), the endpoint monomials and
the \(d-1\) mixed monomials give

\[
\ell H_0=a+b+(d-1)m,\qquad
\ell H_1=(d-1)m,\qquad \chi=a+b.
\]

For the middle identity, the primitive syzygy
\((\pi^{b-m}y,-\pi^{a-m}x)\) generates the kernel; Koszul boundaries
are \(\pi^m\) times that syzygy. This displays the torsion cancellation
even though \(C\) itself is flat. The checker also treats integral
changes of the linear forms, including a pair with determinant \(\pi\).

## 4. Application to the actual leading quotient

Use the three-graded algebra \(\mathcal R\), chart ideal
\(J_\varphi\), and leading quotient \(C=\mathcal R/\mathfrak q\)
from `notes/rh-selmer-mixed-count.md`. Let the section sequence be

\[
\boldsymbol f=
\bigl(F_i^2t_0\bigr)_{i=1}^r,
\bigl(G_jt_0\bigr)_{j=1}^s,
\bigl(E_k^2t_1\bigr)_{k=1}^{r'},
\bigl(E'_lt_1\bigr)_{l=1}^{s'}, F_*^2t_2. \tag{10}
\]

The Smith-normalized negative equations satisfy
\(F_i-\pi^{c_i}u_i\) in the saturated square of the augmentation ideal,
with \(u_i\in A_{-1}\). The leading-quotient square identity therefore
gives

\[
F_i^2t_0=\pi^{2c_i}u_i^2t_0\quad\text{in }C. \tag{11}
\]

Take \(a\in B\) with augmentation zero and \(\varphi(a)\ne0\).
The exact remaining admissibility input is

\[
\boxed{(\mathfrak m_B\mathcal R I_{\mathrm{irr}})^N
\subset J_\varphi+(\boldsymbol f,a)
\quad\text{for some }N.} \tag{12}
\]

Because \(a\in\mathfrak q\) and \(J_\varphi\subset\mathfrak q\),
there is a graded surjection

\[
D=(\mathcal R/J_\varphi)/a
\twoheadrightarrow C.
\]

The list \(\boldsymbol f\) is admissible on \(D\), and therefore on
\(C\). Corollary 2 proves the quotient comparison
\(\chi(\boldsymbol f;D)\ge\chi(\boldsymbol f;C)\).
Apply (8) to (11), with \(q=r\), \(\delta=e_0\),
\(b_i=2c_i\), and the remaining degrees
\(s\) copies of \(e_0\), \(r'+s'\) copies of \(e_1\), and one
copy of \(e_2\). The proved leading Hilbert function and mixed count
make its difference \(2^{r-1+r'}\). Hence

\[
\chi(\boldsymbol f;D)
\ge\chi(\boldsymbol f;C)
\ge(\textstyle\sum_i2c_i)2^{r-1+r'}
=2^{r+r'}\sum_i c_i. \tag{13}
\]

There is no comparison with \(\chi(a,\boldsymbol f;C)\): multiplication
by \(a\) on \(C\) is zero, and its degree is zero, so that latter
Euler characteristic is zero.

On \(P=\mathcal R/J_\varphi\), however, \(a\) acts injectively.
Indeed, coefficientwise application of \(\varphi\) embeds this quotient
in a polynomial algebra over the domain \(F[[z]]\), and
\(\varphi(a)\ne0\). Permuting the Koszul factors and applying (7)
therefore gives

\[
\chi(\boldsymbol f;D)
=\chi(a,\boldsymbol f;P)
=\chi(\boldsymbol f,a;P)
\le\chi(a;P/(\boldsymbol f)P). \tag{14}
\]

This proves (1). In the right side, taking degree \(\boldsymbol d\)
is exactly the one-operator Euler characteristic of the finite weight
module used in `notes/rh-selmer-euler-determinant.md`.

## 5. The precise remaining source supplier

`GradedModulesLength.AdmissibilityHolds` lines 30--77 proves (12) in the
source from negative cotangent spanning, finiteness of the degree-zero
equation quotient, the fixed-point separation condition, and a trace
difference nonzero at every two-sided solution. Its proof examines
prime ideals outside the irrelevant locus, shows that their contraction
to \(B\) is maximal, and then uses finite generation to obtain a power
containment. Its nontrivial point-classification inputs are retained;
this note has not silently replaced them by regularity or flatness.

The Artinian-base hypothesis in Viet--Thanh's
[Theorem 3.7](https://doi.org/10.2206/kyushujm.69.393),
*Kyushu Journal of Mathematics* **69** (2015), 393--411, does not directly
cover the actual \(B\), which need not be Artinian. The theorem and its
base-ring assumption were checked in the published paper, pages 394 and
402; no result from it is used here.
The direct proof above works over this Noetherian local base, with the
exact admissibility condition and without assuming an infinite residue
field. It needs no external mixed multiplicity theorem.

| Contract | Pinned source file | Lines |
|---|---|---:|
| Standard grading, recursive Euler characteristic, admissibility | `NoetherianQuotientCalc/EulerVanishingBelowDimension.lean` | 66--107, 113--167 |
| Relevant-prime replacement of a zero section | `NoetherianQuotientCalc/VanishingBelowDimensionRule.lean` | 309--336 |
| Positivity and exact-sequence monotonicity | `NoetherianQuotientCalc/RulePos.lean`; `RuleMono.lean` | 24--45; 11--22 |
| Quotient upper bound | `NoetherianQuotientCalc/RuleUB.lean` | 25--42 |
| Product additivity with the correct shift | `NoetherianQuotientCalc/EulerRuleProductZero.lean` | 17--66 |
| Original scalar extraction | `GradedModulesLength/LaDifPerm.lean` | 49--124 |
| Actual leading quotient comparison and lower bound | `GradedModulesLength/AdmissibleMonoIdeal.lean` | 111--130, 191--237, 273--322 |
| Admissibility from the geometric hypotheses | `GradedModulesLength/AdmissibilityHolds.lean` | 30--77 |
| Nonzero trace in the chart and final chain | `GradedModulesLength/AlgMemCoef.lean` | 22--43, 113--143 |

The first group of files is under
`Formalism/SharpRestriction/ValuationFrobeniusEpsilon/LeastPrimeTwists/QuotientShiftIrreducible/`;
the second is under
`Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/`.
`scripts/check_rh_selmer_koszul_comparison.py` and its certificate record
exact file and excerpt hashes and finite checks with nonzero higher
Koszul homology. They do not constitute
a Lean replay, verify the remaining point-classification suppliers, or
complete an existing RH or GRH proof-map node.
