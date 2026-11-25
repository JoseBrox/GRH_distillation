# Audit of Adriazola's Alpöge reconstruction

25 November 2026. The audited source is Jimmie Adriazola's
[RH-Alpoge-Reconstruction at aa9c86bf2a7d29b08575641fecea19a2a603e87c][A].
Its [287-page PDF][PDF] has SHA-256
8ced945d3a2fcf7fb7a2a760db6859416cd8db2ed11617d8bc28b43b82ed3a94.
The comparison starts from our revision
[e85b0c946408478b790b0b48ee4f37cab4710c73][ours-start].
All references to source lines and printed page numbers below refer to
that immutable external revision, not to a moving main branch.
Before delivery we reconciled our integration with the five concurrent
W08 commits through
[50315b7](https://github.com/JoseBrox/GRH_distillation/commit/50315b7).
The historical comparison remains tied to the stated starting revision;
the final status below reflects the newer checkpoint.

## Verdict and answers to the six questions

1. **No demonstrated unfixable flaw in the overall strategy.** There are
   false local assertions and an impossible residual-surjectivity condition
   in a proposed application. Several repairs are proved in this update.
   Those repairs do not complete the missing arithmetic constructions.
2. **It is not a complete conventional proof.** The current author
   expressly acknowledges this in the introduction, README and §18.7.
   The final deduction on p.281 assumes Hypotheses 17.11 and 18.10.
   Its omissions include entire arithmetic and geometric inputs, not
   simply routine details that a conventional proof may leave implicit.
3. **It substantially improves readability, but its length does not
   measure a completed simplification of Alpöge's proof.** It packages
   the formal route in ordinary mathematics, proves many useful pieces,
   and proposes some substitutions. Essential hypotheses remain.
   There is no defensible numerical compression factor for a fully
   supplied conventional proof.
4. **It is closely related to our project.** Both follow Alpöge's route
   through corrected prime sums, auxiliary CM data, long theta chains,
   divisibility versus archimedean degrees, global period estimates and
   Selmer/deformation bounds.
5. **It is shorter to survey; our ordinary-RH route has several simpler
   mathematical interfaces.** Neither full conventional proof is complete.
   It would be misleading to rank them globally by page count or to
   identify omitted arguments with simplifications.
6. **Three strengthened tools have been integrated with attribution:**
   arbitrary-window Smith estimates, more precise integral isotypic
   projectors, and Fitting bounds allowing repeated residual blocks.
   Their full proofs, application boundaries and exact finite checks
   are linked in §6 below. No entire proof-map node is closed by them.

This is a critical-dependency audit with detailed proof checks of
selected decisive arguments. It establishes the preceding negative
completeness conclusion. It does **not** certify every displayed lemma,
every literature application, or a fully repaired version of the
manuscript. It is also not a replay of the original Lean proof.

## 1. Evidence and audit coverage

We obtained the source and PDF from the pinned Git revision, read the
mathematical sources, and inspected rendered pages at the final
conditional deduction and the Fitting interface. Independent reviews
covered the geometry/coefficient and Galois/congruence regions; the
generalized Fitting proof received a separate second review.
The [source manifest](../certificates/adriazola-source-audit.json)
records hashes, source sizes and page count. Its lexical environment
counts are an inventory only; they are not numbers of independently
verified results or of distinct gaps.

| Region | Work performed | Important limit |
| --- | --- | --- |
| §§2–6: analysis and selection | Checked the nearest-pole positive-window mechanism, character accounting, thick/thin reduction, auxiliary-selection structure and final error exponents. | The precise Gallagher exceptional-character estimate was not independently matched in full to the cited primary theorem; no blanket certification of §5 is made. |
| §§7–11: chains and local arithmetic | Traced chain/divisibility dependencies into later consumers; checked selected coefficient and step-character arguments. | Odd-position lattice transfer and actual normalized-kernel compatibility remain inputs. |
| §§12–15: loss, frames, periods, geometry | Detailed inspection of Smith windows, AST projectors, trace-to-slope deductions, selected orbit arguments, norm normalizations and the covolume interface. | Far-orbit analytic estimates, filtration-aware near counting and all moving-level geometric interfaces were not fully verified. |
| §§16–17: local terms and Selmer/congruence | Checked conditional bookkeeping, elementary lattice/Fitting arguments, residual-block applicability and the new K1 shortcut against primary sources. | Actual deformation, automorphy, Ribet maps, crystalline lifting, theta integrality and uniform weighted sums are still required. |
| §18: assembly | Checked the implication from the stated hypotheses and examined the quantified chain records. | The records themselves are assumed, and their precise constants are not all checked even conditionally in the source. |

The supporting reports preserve more granular findings:
[geometry and coefficients](adriazola-geometry-2026-11-25.md) and
[Galois, congruences and K1](adriazola-galois-2026-11-25.md).
They distinguish successful proof checks, explicit assumptions,
identified false assertions and remaining uncertainty.

## 2. Why the proof is incomplete

The decisive evidence is already inside [§18][S18].
The deduction on p.281 begins from the Selmer-window and chain-record
hypotheses. The chain records must describe compatible actual objects,
with the prescribed integral lattices, metrics, nonzero maps, slopes and
parameter dependence. A chain of implications from those records does
not establish their existence.

At line 272 the source additionally says that the constants and exponents
needed to obtain the records have not all been checked, even modulo the
earlier hypotheses. Thus the short final assembly is not merely waiting
for a handful of bibliographic references.

Some important examples are:

| Source location | Missing requirement | Why it matters |
| --- | --- | --- |
| Hypotheses 11.38 and 11.42, pp.103–104 | Odd-position integral transfer and the normalized kernel law. | A correct coefficient calculation for a model kernel need not apply to the globally normalized arithmetic map. |
| Hypothesis 12.12, p.113 | The three loss engines, including actual test systems and comparisons between levels. | The polynomial and projector tools alone do not prove the required average rank/share estimates. |
| Hypotheses 14.10–14.12, p.163 | Actual periods, seesaw, dictionaries and rationality. | These identify the same arithmetic maps and pairings used by the norm argument. |
| Hypotheses 14.71–14.77, p.190; Theorem 14.79, p.191 | The expansion and estimates for all required rows and returns. | Conditional near-orthogonality is not a bound for the intended period operator until this identification is proved. |
| Inputs I1–I17, pp.236–237; Hypothesis 15.69, pp.239–240 | Integral models, section maps/ranks, metric comparisons and uniformity over growing covers. | A fixed-model arithmetic Hilbert–Samuel theorem does not give constants uniform in a moving tower. |
| §17, pp.255–268 | Quantitative deformation/automorphy, integral congruence and local lifting suppliers. | Qualitative rigidity and finite sets of eigensystems do not supply integral lengths or the weighted moving-family estimates. |
| Hypothesis 18.10, p.276 | The compatible chain records at every required scale. | Separate constructions with different normalizations or choices cannot simply be combined. |

There are also highly compressed passages that are written as proofs but
still need substantial verification. The far-orbit argument on pp.202–203
needs its precise representation model, derivative/packing estimates and
uniform constants. The near-count argument on pp.205–206 needs the
claimed induction through saturated quotient lattices. These are
**unverified interfaces**, not proven counterexamples.

We deliberately do not repeat stale accusations. The newer N1 valuation
calculation in Proposition 11.27 is valid under its normalizations.
Theorem 12.54 supplies the B7 projector argument. Earlier paragraphs
describing these calculations as absent are superseded by those
insertions. The unresolved issue is their remaining application
conditions, not an absence of every useful local proof.

## 3. Concrete defects and what repairs them

### 3.1 Character evaluation is not injective

The proof of Proposition 17.21, p.256
([§17, line 270][S17]), treats characters with a fixed kernel as if they
were distinguished by their value at one Frobenius norm.
This is false unless an additional condition on that element is imposed.

For an example within the nearby generic setting, take
\[
N=10,\qquad H=\{1\},\qquad K=\mathbf Q(\sqrt{-3}),\qquad
p=11,\qquad e=1,\qquad \ell=7.
\]
The group \((\mathbf Z/10)^\times\) is cyclic of order four and has two
faithful characters. The prime 11 is inert in \(K\), so its residue-field
norm is 121, congruent to 1 modulo 10. Both characters therefore have
the same evaluated value, despite being different characters with the
same kernel. Their oddness and order prime to 7 hold. The relevant
noncontainment is compatible with the disjoint ramification at 3
versus 5 and 7, and \(6\nmid2e\).

The repair must retain character labels or prove the required
disjointness when grouping representations with the same root value.
If a representation occurs more than once, its product multiplicity
must be retained. This disproves the claimed bijection; it does not
disprove every possible corrected Count-to-PropGK argument.

### 3.2 Joint residual surjectivity fails for repeated cyclotomic blocks

Proposition 17.27, pp.263–264, has a joint-surjectivity assumption F3.
The proposed application at [§17, lines 505 and 662][S17] uses consecutive
cyclotomic blocks. In residue characteristic \(\ell\),
\[
\bar\chi^{a+\ell-1}=\bar\chi^a.
\]
On two such scalar blocks the image lies in the diagonal of \(k\times k\);
it is not the whole product. A longer residue field does not distinguish
two already identical representations. In particular, a sufficiently
long consecutive family cannot meet that F3 literally.

This is a substantive applicability error. It does not invalidate the
abstract proposition under its stated hypotheses. Our replacement
requires only individual residual surjectivity and either a controlled
factorial error or an explicitly stable determinant law; see §6.3.
Regrouping constituents is another possible route, but multiplicities
and the associated modules must then be tracked.

### 3.3 An unramified extension need not split eigensystems

The coefficient enlargement on p.265
([§17, line 544][S17]) cannot be justified for arbitrary Hecke algebras
by an unramified extension alone. For example, the finite algebra
\[
\mathbf Z_5[T]/(T^2-5)
\]
acts on its regular lattice, but its eigenvalues have valuation \(1/2\).
No unramified extension of \(\mathbf Q_5\) contains them.

Allow a finite ramified splitting extension instead. Under an extension
of coefficient DVRs with relative ramification index \(h\),
finite module lengths and \(v_O(\ell)\) both multiply by \(h\).
The normalized defect is therefore unchanged. Flatness preserves the
relevant kernels, intersections and projection quotients for a
decomposition defined over the starting field. A new splitting
decomposition must of course be specified over the enlarged field.
The full normalized-base-change lemma is proved in our Fitting note.

### 3.4 Arbitrary \(\mathbf C_p\) coefficients need not lie in a finite field extension

Theorem 12.34, pp.129–130
([§12, lines 760–794][S12]), allows coefficients in \(\mathbf C_p\).
Its proof starts by placing them and all roots in a finite extension
of \(\mathbf Q_p\). This need not be possible: \(\mathbf C_p\)
contains elements transcendental over \(\mathbf Q_p\).

The conclusion can be recovered directly over the valuation ring of
\(\mathbf C_p\). Finite Smith elimination and finitely generated
determinantal ideals suffice; no noetherian or discrete-valuation
assumption is needed. Our strengthened theorem proves precisely this
and removes additional window restrictions.

### 3.5 Normalization and quantitative cautions

Proposition 15.48, p.228, invokes an extremal normalization. With
arbitrary fixed Fock norms the exact branching identity is
\[
\|\mathrm{br}\|^2
=|c|^2\kappa\,
\frac{\|\mathrm{hw}_\sigma\|^2}{\|\mathrm{hw}_\lambda\|^2}.
\]
Raw highest monomials of different degrees need not have equal norms.
The ratio can be made one by the stated renormalization, so this is
not an unconditional counterexample to the proposition. Its use for
the original integral polynomial and global metric must preserve that
normalization. The supporting geometry report gives an explicit
degree-two example.

Likewise, an unspecified big-O estimate in the proof of the passage
bound on p.232 cannot alone establish its particular displayed
coefficient 28. The source's own uniformity hypotheses must remain.
At the analytic endpoint, a minor “all sufficiently large windows”
wording should be weakened to arbitrarily late suitable windows;
the latter is enough for the stated criterion.

These findings have different statuses: explicit counterexamples
to local sentences, an impossible proposed hypothesis, and remaining
normalization/constant checks. They should not be collapsed into
either “the entire strategy is false” or “only typographical issues.”

## 4. Useful arguments that survived inspection

The nearest-pole argument behind Theorem 2.4 has a coherent
positive-residue mechanism and the required long-window quantifiers.
The character orthogonality/accounting, several coefficient
divisibility calculations and abstract trace-to-slope deductions
also survived the checks described above. They remain deductions
under their actual input hypotheses.

The AST construction of the whole isotypic projector in Theorem 12.54
is particularly useful. We checked its classical product formula
against [Tolstoy, Theorem 2.5][Tolstoy]. Passing to invariant maps in
\(\operatorname{Hom}(W,V)\), then taking a partial trace, handles
isotypic multiplicities correctly. It supports the stronger integral
theorem in §6.2.

The proposed K1 shortcut in §17.4.3, pp.260–262, also survived the
specific source and small-prime checks. The chain uses finite even
K-theory, a generator bound, a level-three torsion-free subgroup, a
finite well-rounded quotient, transfer and a Hurewicz-kernel exponent.
We checked the relevant hypotheses in [Mathew, Theorem 6.3][Mathew],
[Bayer–Fluckiger–Emery–Houriet, Corollary 5.2 and §3.1][BFH],
[Weibel, Theorem 73][Weibel], and
[Schmidt, Proposition 2.3 and its proof][Schmidt].
Transfer retains the primes dividing the subgroup index; the totally
imaginary comparison includes 2. These were potentially decisive
points and were not assumed away.

However, our [existing K-theory section](../paper/sections/recovered/27-kt-section.tex)
already uses the same rank/Hurewicz strategy and has exponent
\(C_K=14\), compared with the reconstruction's stated 150
(its displayed coarsening already yields 24).
Our existing argument also retains the sharper Brauer contribution
\(|S|-1\) and needs no extra fourth roots of unity at 2.
The short BFH/level-three proof is a useful alternative geometric
supplier, preserved with an explicit bound and proof in the
[Galois audit](adriazola-galois-2026-11-25.md#4-verification-of-k1-and-useful-alternative-supplier).
It is not a new solution of our K1 obligation or a numerical improvement
over our existing result.

## 5. Comparison with Alpöge and with our project

Alpöge's [announcement][Alpoge] describes a theta chain of length
roughly \(\sqrt X\), emphasizes the breadth and length of the formal
argument, and anticipates substantial simplification. Adriazola's
reconstruction follows this architecture. Changing formal code to
conventional prose eliminates large amounts of formal infrastructure;
it does not by itself eliminate the mathematics hidden in an assumed
automorphy or covolume statement.

The [Lean community's verification statement][Lean] concerns the
original formal RH theorem. The defects found here concern a later
human reconstruction. We did not rerun those external kernel checks,
and this audit supplies no reason to identify a reconstruction error
with an error in the original formal proof.

| Comparison | Adriazola reconstruction | Our project at the starting checkpoint |
| --- | --- | --- |
| Organization | Compact survey of the original route, with substantial hypotheses isolated. | Separate RH and Dirichlet routes, shared technical proofs and explicit ongoing construction targets. |
| Analytic target | A pointwise one-sided bound on suitable windows. | Direct four-character RH transfer, positive-part averaged budgets and fourth-power sampling. |
| Norm comparison | Frame/near-orthogonality estimates with their original losses. | One-sided trace-majorant comparisons and signed/averaged budgets, avoiding some unnecessary square-root losses. |
| Arithmetic progress | K1 and several local tools supplied; major §17 inputs remain conditional. | Written RH weighted-Selmer suppliers; general Dirichlet W04 remains open. |
| Current global gap | Actual compatible chain, periods, integral geometry and uniform estimates. | Actual common theta family and dictionaries, remaining return/trace estimates, corrected geometric means/rank losses and compatible tables. |
| Length at the audited snapshot | 287 pages. | Checked-in PDFs: RH 342, Dirichlet 919; some newer source suppliers had not yet been rebuilt. |

The page counts in that last row are historical artifact measurements,
not a comparison of fully completed proofs. The new builds in this
update include the current source and the transferred tools.

Our direct RH route is simpler at the analytic interface: it asks for
weaker averaged information, specializes character data and uses
sharper degree/trace comparisons. Those improvements do not
automatically simplify the hardest moving-family arithmetic
constructions. Conversely, Adriazola's smaller document is useful for
learning the overall route. The evidence does not justify claiming
either complete proof is globally simpler, because neither complete
conventional proof is presently written.

## 6. Strengthened results integrated with citation

### 6.1 Smith exponents on arbitrary finite p-adic windows

[Full statement and proof](../notes/padic-smith-window.md);
[shared manuscript source](../paper/shared/padic-smith-window.tex).
This refines Adriazola's Theorem 12.34, with its origin explicitly
attributed.

Let
\[
A(z)=\sum_{k=0}^{\Delta}C_k\binom zk,\quad C_k\in M_n(O_{\mathbf C_p}),
\qquad f(z)=\det A(z)\ne0,\qquad v(p)=1.
\]
For distinct \(z_j\in\mathbf Z_p\), let \(b_E(j)\) count Smith
exponents at least \(E>0\). Let \(s\) be the number of roots of
\(f\) in the unit disk, including multiplicities, put
\[
c=v(\operatorname{lc}f)+\sum_{v(\rho)<0}v(\rho),\quad
L=\lfloor\log_p\max(1,\Delta)\rfloor,\quad
C(Z)=\max_k\sum_{j\ne k}v(z_j-z_k).
\]
Then the proved bound is
\[
E\sum_j b_E(j)\le Yc+s\bigl(E+L+C(Z)\bigr).
\]
On a progression \(z_j=t+dj\),
\[
C(Z)=(Y-1)v_p(d)+v_p((Y-1)!).
\]
This allows arbitrary window length, steps divisible by \(p\),
real thresholds and arbitrary \(\mathbf C_p\) coefficients.
It uses the actual root count and exact collision term.
The proof is through integral perturbations, truncated determinant
ideals and a closest-sample bound for each root.

Application still requires the actual polynomial Gram family,
coefficient integrality and leading-coefficient control.
An abstract local theorem does not produce those arithmetic data.
The [exact script](../scripts/check_padic_smith_window.py) checks
2,205 inequalities across 50 matrices, including singular samples
and ranges beyond the source's window restriction.

### 6.2 More precise integral isotypic projectors

[Full statement and proof](../notes/integral-isotypic-projector.md);
[shared manuscript source](../paper/shared/integral-isotypic-projector.tex).
This retains and credits Adriazola's Hom-space/partial-trace argument
and the classical AST theorem.

For a weight-graded lattice stable under root divided powers, let
\(e_\lambda\) project onto an occurring \(\mathrm{GL}_r\)-type \(W\).
For each positive root \(\alpha\), of height \(h_\alpha\), put
\[
C_\lambda(p)=
\sum_{\alpha>0}
\max\left(\{0\}\cup
\left\{v_p\binom{h_\alpha+k}{k}:
k\ge1,\ k\alpha\in\operatorname{wt}\operatorname{Hom}(W,V)\right\}\right).
\]
The improved sufficient exponent is
\[
D_\lambda(p)=\max\{0,C_\lambda(p)-v_p(\dim W)\},\qquad
p^{D_\lambda(p)}e_\lambda\Lambda\subseteq\Lambda.
\]
For a set of types the cost is the maximum of these exponents.
Keeping root-by-root denominators and the dimension factor can
improve the coarse bound. The statement includes \(p=2\).
The balanced Fock valuation version removes a square-root-of-\(p\)
condition by proving the scalar-extension/descent step explicitly.

The [exact independent projector calculation](../scripts/check_integral_isotypic_projector.py)
uses rational Casimir projectors: 21 representations, 56 projectors
and 280 prime cases. It finds 99 strict improvements over the common
coarse numerical expression, of which 69 are odd-prime cases.
The 2-primary comparison extends the source theorem's range.
The actual theta lattice and its divided-power stability still need
to match the theorem before a global loss estimate follows.

### 6.3 Fitting inequalities permitting repeated residual blocks

[Full statement and proof](../notes/residual-block-fitting.md);
[shared manuscript source](../paper/shared/residual-block-fitting.tex).
This corrects the proposed applicability of Proposition 17.27.

With its determinant-tuple and off-target-kernel hypotheses retained,
let \(\delta\) be the supported congruence length, \(L_j\) the block
kernel lengths and \(D_0=b\sum_j n_j\). We prove:

* Joint residual surjectivity gives \(\delta\le\sum_jL_j\) with no
  residue-field-size condition. The source's extra F4 is unnecessary
  under its joint F3.
* Individual residual surjectivity gives the same exact bound when
  the residue field is infinite or has more than \(D_0\) elements.
  Repeated residual constituents are permitted.
* At every mixed-characteristic prime, individual surjectivity and
  the original pointwise determinant hypothesis give
  \[
  \delta\le\sum_jL_j+v_O(D_0!).
  \]
  A primitive determinant polynomial and finite differences on an
  integer grid prove the error bound.
* Over a complete DVR, an exact bound at all residue characteristics follows if the
  determinant law is explicitly stable under the needed unramified
  extension. Pointwise membership alone does not establish that
  stronger hypothesis.

After dividing by \(v_O(\ell)\), the error is \(v_\ell(D_0!)\).
For \(D_\ell\le D\) and \(0\le w_\ell\le W\),
\[
\sum_\ell w_\ell v_\ell(D_\ell!)\log\ell\le W\log(D!).
\]
The version with several applications retains their total weight or
number. Thus the correction is controlled algebraically; absorbing
it in the actual global budget still requires bounds for those
dimensions, weights and counts.

The same note proves normalized-length invariance under arbitrary
finite ramified coefficient extension, repairing the splitting issue.
The [exact witness script](../scripts/check_residual_block_fitting.py)
checks the residual coincidence, a common-left-inverse obstruction
over \(\mathbf F_2\) and its repair over \(\mathbf F_4\), sharp
factorial-grid examples, and the character-evaluation collision.
The general theorems rest on the written proofs, not these examples.

## 7. Integration, verification and remaining work

The three shared proofs are included in both the RH and Dirichlet
manuscripts, near their congruence and coefficient-space consumers.
Their bibliography cites the immutable Adriazola revision, his
CC BY 4.0 attribution, the AST original and the checked Tolstoy
formula. New results are explicitly distinguished from the source
arguments and from remaining arithmetic applications.
The source's reuse terms are
[Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/);
the transfer notes identify the original mechanisms and our changes.

The final reconciled RH and Dirichlet PDFs have 538 and 1,150 pages,
respectively. Both builds stabilized in two passes, with zero undefined
references/citations and zero overfull boxes. Their source hashes and
output hashes were checked against the build records. The growth from
the historical PDFs also includes previously unbuilt project suppliers
and the concurrent W08 work; it is not the length of these three imports.
The transferred sections occupy approximately eleven pages per route.
Representative pages containing their statements and proofs were
visually inspected. Compilation and finite checks do not establish the
unresolved mathematical inputs.

Verification records:

* [Smith-window finite checks](../certificates/padic-smith-window-check.json).
* [Projector finite checks](../certificates/integral-isotypic-projector-check.json).
* [Fitting witnesses](../certificates/residual-block-fitting.json).
* [Source identity and inventory](../certificates/adriazola-source-audit.json).
* [Integration/build review](../certificates/adriazola-integration-review.json).
* [RH build](../certificates/rh-build.json) and
  [Dirichlet build](../certificates/grh-build.json).

Our current arithmetic targets remain those in the
[continuation checkpoint](../notes/current-state.md).
The RH weighted Selmer estimate has written suppliers. The general
Dirichlet W04 is open. W06 still needs the actual common theta family,
row identities and norm dictionaries. The reconciled checkpoint records
the concrete diagonal zero-Gram estimate, including the matched local
data and amplitude suppliers; W08 next needs generic returns, finite
columns and final positive traces. W10 still needs
the exact two-level correction identities and rank-loss assembly.
No compatible set of final arithmetic tables is constructed here.

**Whole-node counts remain RH 6/9 and Dirichlet GRH 18/31.**
The imported lemmas strengthen tools inside existing obligations.
They do not change those counts, and counts are not percentages of a
finished proof.

[A]: https://github.com/jimjamzola/RH-Alpoge-Reconstruction/tree/aa9c86bf2a7d29b08575641fecea19a2a603e87c
[PDF]: https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/manuscript/main.pdf
[S12]: https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/manuscript/sec12_loss.tex
[S17]: https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/manuscript/sec17_twisted.tex
[S18]: https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/manuscript/sec18_assembly.tex
[ours-start]: https://github.com/JoseBrox/GRH_distillation/tree/e85b0c946408478b790b0b48ee4f37cab4710c73
[Alpoge]: https://alpo.ge/remark.pdf
[Lean]: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/
[Tolstoy]: https://arxiv.org/pdf/1010.4054
[Mathew]: https://msp.org/agt/2016/16-2/agt-v16-n2-p12-s.pdf
[BFH]: https://ftp.gwdg.de/pub/misc/EMIS/journals/DMJDMV/vol-merkurjev/bayer_emery_houriet.pdf
[Weibel]: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/weibel-ints.pdf
[Schmidt]: https://www.mathi.uni-heidelberg.de/~schmidt/papers/kpi1.pdf
