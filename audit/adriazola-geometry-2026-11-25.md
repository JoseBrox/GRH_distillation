# Independent geometry and coefficient audit

## Revision, scope, and conclusion

This report concerns `jimjamzola/RH-Alpoge-Reconstruction` at
`aa9c86bf2a7d29b08575641fecea19a2a603e87c`, principally Sections 7–15.
Page numbers refer to the actual `manuscript/main.pdf` at that revision;
the page number printed in the PDF agrees with the physical PDF page in
the passages cited below. The source and the rendered B7 theorem on page
140 were compared visually. The source files were used for formula and
dependency checks.

The work was a critical-path audit with detailed checks of selected
proofs, not an independent verification of every line or every external
input. Sections 11–15 received the greatest scrutiny; the earlier chain,
kernel, and divisibility sections were traced for the inputs they supply
to those later statements. No unfixable mathematical flaw was established
in this part of the reconstruction. Several deductions are correct and
useful. Nevertheless, these sections do **not** provide a complete
conventional proof of the required arithmetic construction: they retain
essential unproved hypotheses about the same theta maps, integral
lattices, geometric models, and estimates needed in the final argument.

The strongest positive result extracted here is the isotypic-projector
estimate, Theorem 12.54. Its argument is sound after checking the classical
extremal-projector formula, and it admits the stronger theorem integrated
into the project as `paper/shared/integral-isotypic-projector.tex`.

Immutable source base:
<https://github.com/jimjamzola/RH-Alpoge-Reconstruction/tree/aa9c86bf2a7d29b08575641fecea19a2a603e87c/manuscript>

## 1. Essential open dependencies

The following are substantive mathematical requirements, not merely
missing bibliographic citations or routine algebra.

| Location | Requirement retained | Effect on the claimed proof |
|---|---|---|
| Hypothesis 11.38, p.103; `sec11_lifts.tex:623–629`, label `r1:hyp:H2` | Integral odd-position contragredient transfer, (N2) | The even-position coefficient computation does not itself construct or control the odd-position lattice map. |
| Hypothesis 11.42, p.104; `sec11_lifts.tex:660–666`, `r1:hyp:H3` | Normalized kernel law and integral scalar, (N3) | The local polynomial estimates must refer to the actual globally normalized kernel. The compatibility is indispensable. |
| Theorem 12.11, pp.112–113; Hypothesis 12.12, p.113; `sec12_loss.tex:208–230`, `r2:LPthm`, `r2:engines` | The three nondegeneracy engines: symbol-space rank, twisted-Fock detection, and averaged shares | The proof is explicitly an outline. The Pieri splitting at tops and segment-to-LP assembly C11 are also not supplied there. Later subsections prove parts, not all, of these engines. |
| Hypotheses 14.10–14.12, p.163; `sec14_bessel.tex:168–185`, `w2:H-see`, `w2:H-dict`, `w2:H-rat` | The actual period map, seesaw, dictionaries, and rationality | A formal seesaw computation is conditional until the normalized arithmetic maps and pairings are identified. |
| Hypotheses 14.71–14.77, p.190; Theorem 14.79, p.191; `sec14_bessel.tex:1079–1126` | Kernel expansion, main row, loop terms, nongeneric/degenerate terms, multiplicities, and parameter sizes | The near-orthogonality theorem assumes precisely these inputs. Later volume/orbit work does not by itself identify all of them with the actual period operator. |
| Hypotheses 15.42–15.44, pp.226–227; `sec15_heights.tex:642–710`, `w3:W3:K3`, `K4`, `K5` | Normalized theta kernel, theta-null mean, class/index counts | Theorem 15.46's kernel norm estimate remains conditional. The algebraic averaging of a Weber value does not establish its transformation/integrality/period compatibility. |
| Hypothesis 15.50 and final pairing, p.229; `sec15_heights.tex:775–803` | Fock norm of the branching polynomial and factorization of the actual final pairing through the branching map | The operator estimate is useful once these objects are identified; it does not construct the arithmetic pairing. |
| `sec15_heights.tex:808–821`, label `w3:W3:HLprop` | Rallis/doubling normalization and frame constants for the actual chain | A general Rallis formula does not substitute for checking these theta maps, local measures, formal degrees, and scalars. |
| Hypothesis 15.56 and passage estimate, p.232; `sec15_heights.tex:871–885` | Two multiplicity/goodness counts and the explicit coefficient in the slope loss | A proof ending with an unspecified big-O constant cannot certify the displayed numerical coefficient 28. This is a repairable quantitative gap. |
| Inputs I1–I17 and Theorem 15.66, pp.236–238; `sec15_heights.tex:1027–1065`, `cov:main` | Integral descent, bad-locus ranks, core comparisons, deep-cover existence, section maps/ranks, flat twists, and height/volume comparison | The formal covolume deduction is conditional on these seventeen inputs, which the text does not prove. They are the geometric substance of the bound. |
| Proposition 15.68, pp.238–239; `sec15_heights.tex:1075–1093`, `cov:ck` | Hodge–Tate lattice/character-ideal identities and transition from test points to integral charts | The displayed Chern-class calculation assumes G1–G4; construction/refinement of the integral models is not supplied. |
| Hypothesis 15.69, pp.239–240; `sec15_heights.tex:1101–1146`, `w3:W3:unif` | A mean-slope estimate uniform over growing deep covers | The tower of integral models, exact good-prime comparison, and limiting argument removing level-dependent constants are not written. This is a major open proof interface. |

The fixed-model arithmetic Hilbert–Samuel theorem is not a theorem
uniform in the level of the varying covers. The reconstruction recognizes
that difference and proposes an exact identity at good primes to eliminate
the dependence. Until that identity, the model construction and the limit
are proved with their stated metrics and integral structures, the
uniformity claim is not supplied by the classical theorem.

### Avoid stale-status overclaims

There are revisions layered into the manuscript. A status paragraph can
be older than a subsequent inserted proof. Two examples matter:

* The end of Section 11 still calls all of N1–N3 unproved. Proposition
  11.27, p.97, `a8:prop:N1` at lines 414–440, now proves the required
  scalar/frame valuation under the step-character and unit determinant
  frame normalizations introduced immediately before it. That elementary
  valuation proof is valid. What still must be checked is the construction
  of those objects and their identification with the chain's actual
  arithmetic data. It is inaccurate to say that the N1 calculation has
  simply been omitted.
* The earlier residual-input discussion of B7 is superseded by Theorem
  12.54 at lines 1132–1209. B7 should be credited as proved. B8/B9, which
  turn the tools into actual source-test detection, remain separate.

The reconstruction's own final inventory on pp.281–282 preserves these
essential dependencies. Thus its under-300-page length is not the length
of a fully closed proof of all the requirements above.

## 2. Checks with positive outcomes

### 2.1 Coefficient arithmetic and the loss engine

The following local arguments survived direct mathematical inspection:

* The step-character valuation calculation for Proposition 11.27 uses
  principalization and the finite-order compact part of the character.
  It proves its asserted valuation under the definitions supplied there.
* The factorial splitting and Mahler-decay calculations in
  `sec12_loss.tex:944–1006` are consistent with their prime ranges and
  valuation normalizations. These are tools for the detection engine,
  not proofs of the complete engine.
* The elementary matrix-window mechanism in `sec12_loss.tex:732–796`
  is correct after repairing the coefficient-field step. A finite set of
  arbitrary elements of `C_p` need not lie in a finite extension of
  `Q_p`. The argument can be performed over the valuation ring or by
  an adequate approximation. The companion [Smith-window note](../notes/padic-smith-window.md)
  supplies a sharper direct proof, so that result is not duplicated here.
* The AST projector argument in `sec12_loss.tex:1086–1118,1132–1209`
  is valid: the extremal projection on `Hom(W,V)` extracts invariant
  intertwining maps, and their partial trace recovers the entire
  isotypic projection on `V`. Treating the *whole* isotypic component
  is essential in the presence of multiplicities.

The remaining rank/discriminant/comparison ingredients of engine A and
the source-test construction of B8/B9 and C11 cannot be inferred just
from these successful local calculations.

### 2.2 The frame theorem

Theorem 13.8, p.151, and its proof in `sec13_frame.tex` use the
Harder–Narasimhan filtration, the slope inequality, a reverse-Markov
estimate for source traces and an integral over truncation levels. The
appearance of a complex change of basis in the archimedean trace
calculation does not change the arithmetic lattice being measured.
The argument is a legitimate deduction from the trace hypotheses.

The central quantitative penalty is of the form

\[
\frac{4u\log(1+H/u)+(\eta+4\sqrt e)H}{1-\delta}.
\]

The proof does not silently establish those trace hypotheses for the
arithmetic theta maps. Our project already has related trace-budget
reductions with more flexible signed/averaged errors; this is useful
comparative exposition, not the most valuable new import.

### 2.3 Selected geometric estimates in Section 14

The abstract Hilbert-space pair estimate and its scalar closure in
`sec14_bessel.tex:1025–1075` are sound under their hypotheses. The
near-unipotence argument, Proposition 14.90, pp.203–204,
`fr:prop:near-unipotent` at lines 1855–1920, correctly uses the
radicality of the congruence ideal, integrality of traces and the product
formula bound. Its assumptions must be retained; proximity at infinity
alone would not force a rational matrix to be unipotent.

The geometric-mean packing argument at lines 1923–1947 is also a useful
standalone lemma. Its product-over-embeddings structure matches the
number-field geometry and does not require replacing each local norm
by its maximum.

The rank-two definite Hermitian lattice count at lines 1530–1776 has
a coherent mechanism: ideal counting, a simultaneous short vector,
orthogonal-line data and finite gluing. No contradiction or missing
power was found in those selected checks. The absolute-volume
substitution at lines 1778–1814 explicitly assumes that the rank
recurrence has already reduced to rank two; the substitution cannot
be cited as a proof of that recurrence.

### 2.4 Periods, local Fock norms, and slope algebra

The Kronecker-limit/CM-period calculation at `sec15_heights.tex:39–145`
is internally consistent in the stated squared-norm degree convention.
It is important to retain the factor of two that converts an arithmetic
degree normalized by `[F:Q]` into the manuscript's slope convention.

The Gaussian Fock block bound at lines 585–606, Schur class-sum bound
at lines 608–619, and the submean estimate for the theta sup norm at
lines 625–640 give legitimate local inequalities. None determines the
unproved normalization scalar of the actual theta kernel.

The conditional descent/mean-height/flat-twist calculations in Section
15.14 separate the sign and factor-of-two issues correctly. The actual
integral lattices and covers satisfying the hypotheses remain necessary.

## 3. High-risk interfaces still requiring verification

These are reasons to withhold a completeness conclusion; they are not
assertions that the relevant mathematical statement is false.

### 3.1 Siegel–Weil and the actual local normalization

The convergent-range choice `M>2n` in the normalized unitary Siegel–Weil
proposition (`sec14_bessel.tex:1182ff`, label
`prop:normalized-unitary-sw`) is consistent with the classical
convergent range. It was checked against Shunsuke Yamana,
*The Siegel–Weil formula for unitary groups*, Pacific Journal of
Mathematics 264(1) (2013), 235–256, DOI
<https://doi.org/10.2140/pjm.2013.264.235>, primary PDF
<https://msp.org/pjm/2013/264-1/pjm-v264-n1-p11-p.pdf>.
That paper states convergence for anisotropic spaces or `m-r>n` and
records the classical `m>2n` range; its chosen measure normalization
must be accounted for when comparing constants.

This check does **not** certify the manuscript's local Whittaker/coarea
identity, Weil-index conventions, integral test functions, Tamagawa
factors, or its identification of the resulting theta integral with the
specific chain. Those are exact scalar questions. Treating a general
Siegel–Weil theorem as an automatic proof of all those normalizations
would be unjustified. No concrete normalization counterexample was
established in this audit.

### 3.2 Adapted flag volumes

The flag Jacobian and lattice-covolume argument at lines 1354–1509
uses specific integral Hermitian models. The identification of real and
skew lattices invokes a skew algebraic integer that is a unit at the
relevant finite prime. This uses the unramified/split-at-two host-field
conditions available earlier in the construction. A general theorem
for arbitrary CM fields would require their replacement by explicit
different/discriminant factors. No failure in the stated actual host
family was found, but the model hypotheses should accompany any import.

### 3.3 Far orbits and deep-region decay

The subsection beginning on p.202, `sec14_bessel.tex:1817–1840`, is
very compressed. It asserts a compact integral formula for lowest
K-type matrix coefficients, identifies it by lowering equations and
Taylor jets, deduces decay, supplies a packing estimate and then a
high-order cuspidal Sobolev bound. This is substantial analysis.

For an independently checkable conventional proof, the exact lowest
K-type model, normalization of the compact integral, uniqueness
argument for the lowering equations, derivative constants, and
uniformity in rank and the moving weight gaps must be written or
matched to a precise theorem with those same hypotheses. The existing
paragraphs do not justify declaring those interfaces verified merely
because a familiar decay principle is named.

### 3.4 Filtration-aware near counting

Proposition 14.92, pp.205–206,
`sec14_bessel.tex:1950–2011`, uses an induction on block height and
dual indices. The sentence asserting that this induction propagates all
relations carries the principal content: it establishes the injection
into successive block quotients that makes the fibre-packing product
valid. A careful proof must specify the equivalence relations and
quotient lattices at each stage, prove the propagation and check that
the separation bound survives saturation and duality. The final product
arithmetic is explicit, but it does not replace this induction.

The following moderate-region estimate, Proposition 14.93, p.207,
also assumes the flag-measure bound and its constant. Proposition
14.94, p.208, is a deduction from a nonzero-flag bound. Neither closes
an omitted flag-measure theorem simply by naming its constant.

## 4. A repairable Fock-normalization ambiguity

Proposition 15.48, p.228,
`sec15_heights.tex:753–765`, gives a scaled-coisometry formula. Let
`xi` be the branching highest vector, `hw_lambda` and `hw_sigma`
highest vectors, and put

\[
 \kappa=\frac{\|\xi\|^2}{\|\mathrm{hw}_\lambda\|^2},
 \qquad \mathrm{br}(\xi)=c\kappa\mathrm{hw}_\sigma.
\]

Schur's lemma gives the exact squared operator norm

\[
 \|\mathrm{br}\|^2
 =|c|^2\kappa
   \frac{\|\mathrm{hw}_\sigma\|^2}
        {\|\mathrm{hw}_\lambda\|^2}.
\]

The manuscript's simpler formula therefore uses the equality of the
two highest-vector norms, introduced during its proof as an extremal
normalization. This equality is not automatic for ordinary Fock
monomials of different degrees. For example, in `Sym^2(C^2)` with
standard Fock norm, take `hw_lambda=x^2`, `xi=y^2`, and take the
trivial `GL_1` representation with `hw_sigma=1`. Then their squared
norms are 2, 2 and 1. With `c=1`, `kappa=1`, and `br(y^2)=1`, the
squared operator norm is `1/2`, not 1.

This is **not** a contradiction after explicitly renormalizing the
target highest vector (or its metric), as the proof proposes. It is a
normalization obligation: such a renormalization must be reconciled
with the integral branching polynomial and the global height metric.
The corrected ratio formula works in every normalization and makes
that obligation visible. It should not be presented as a fatal flaw in
the entire argument.

## 5. Strengthened result integrated into our project

The isotypic-projector mechanism of Theorem 12.54 was checked against
the primary AST formula, not merely the reconstruction's summary.
The primary source checked was V. N. Tolstoy,
*Extremal projectors for contragredient Lie (super)symmetries
(short review)*, arXiv:1010.4054v2, Theorem 2.5,
equations (2.10)–(2.13), pp.8–9:
<https://arxiv.org/pdf/1010.4054>.
The original attribution is Asherova, Smirnov and Tolstoy,
*Projection operators for simple Lie groups*, Theoretical and
Mathematical Physics 8 (1971), 813–825, DOI
<https://doi.org/10.1007/BF01038003>.

For a weight-graded lattice stable under all root divided powers, and
an occurring irreducible type `lambda`, define

\[
 C_\lambda(p)=\sum_{\alpha>0}
 \max_{\substack{k\ge0\\k\alpha\in\mathrm{wt}\operatorname{Hom}(W,V)}}
 v_p\binom{h_\alpha+k}{k},
 \qquad
 D_\lambda(p)=\max\{0,C_\lambda(p)-v_p(\dim W)\}.
\]

Then

\[
 p^{D_\lambda(p)}e_\lambda\Lambda\subseteq\Lambda.
\]

The proof retains the dimension factor in the exact partial-trace
identity. Sums of isotypic projectors incur the maximum, rather than
the sum, of their costs. Balanced Fock lattices satisfy the divided
power hypothesis even at `p=2`; extension to `K(sqrt(p))` proves the
seminorm inequality without assuming that `sqrt(p)` was in the
original field. No equality of the original and scalar-extended
integral lattices is asserted.

This strengthens the imported result in four ways: individual root
costs, the dimension saving, all primes, and removal of the square-root
field restriction for the valuation consequence. The denominator is
an explicit sufficient bound, not a claim to the minimal denominator.

The project files are:

* `notes/integral-isotypic-projector.md` — statement, complete proof,
  provenance, application boundary and checks;
* `paper/shared/integral-isotypic-projector.tex` — conventional proof
  for inclusion in both manuscript routes, with the three bibliographic
  keys supplied to the coordinating agent;
* `scripts/check_integral_isotypic_projector.py` — an independent exact
  rational matrix construction via the `sl_2` Casimir;
* `certificates/integral-isotypic-projector-check.json` — executed data.

The installed verifier was run successfully. It checks 21 tensor
representations `Sym^a(Q^2) tensor Sym^b(Q^2)`, `0<=a<=b<=5`, 56
projectors and 280 prime cases for `p=2,3,5,7,11`. It verifies
idempotence, pairwise orthogonality, sum equal to identity, commutation
with `E,F,H`, traces and exact denominators. The improved sufficient
bound is strictly smaller than the common coarse numerical expression
in 99 cases, of which 69 are at odd primes. Comparisons at 2 refer to
the same coarse expression; the source theorem itself only stated
the odd-prime case. The general theorem is proved symbolically; the
finite computations are corroborating checks.

The natural integration point is shared coefficient arithmetic and
W06 integral-theta/divisibility work, subject to matching the actual
polynomial representation and lattice. W07 is the project's
archimedean restriction/local residue positivity task, so it should
not be described as a coefficient-lattice task. This lemma does not
close B8/B9, construct source-test systems, normalize the global theta
kernel, or close any whole RH/GRH proof-map node.

## 6. Assessment for the comparison

In this geometric portion the reconstruction and our project largely
follow the same broad proof architecture: integral theta maps,
coefficient/loss estimates, traces or frames, arithmetic slopes and
a uniform geometric model. The reconstruction has helpful short
presentations of several local tools. Our project has its own more
developed reductions and explicit remaining compatibility conditions.
Neither manuscript can be judged simpler as a *complete proof*, since
the required complete proof is not supplied here. Comparing page
counts without counting the conditional inputs would misstate the
mathematical work remaining.

The outcome of this audit is therefore positive but limited: one
substantial reusable arithmetic lemma has been verified, strengthened,
and integrated; several other conditional deductions are sound; and
the essential geometric hypotheses remain visible. No fatal geometry
counterexample was found, and no claim is made that all high-risk
external theorem applications were independently verified.

## Source file fingerprints

SHA-256 of the pinned local source used for the audit:

| File | SHA-256 |
|---|---|
| `main.pdf` | `8ced945d3a2fcf7fb7a2a760db6859416cd8db2ed11617d8bc28b43b82ed3a94` |
| `sec7_chain.tex` | `24597d86b4e993648decced9ad1c9b6a440b74df47d813c5984f849e6a717356` |
| `sec8_kernel.tex` | `03c425fc632d87d0a6adeff0272cd974cca7734492b4622e7164e8b24452024e` |
| `sec8_gain.tex` | `9541f33d0a7a255b8c7b5ee037c8d42fa995a67b51360323f6777c7125553baa` |
| `sec10_chaindiv.tex` | `6d24b2be625c2c8aa50105da747b77fe6697a713c91ab61b0599f53307bb372e` |
| `sec11_lifts.tex` | `7dbc2f69e69e0209e2654c693ea2c73a64493189830da9032f0add616db39517` |
| `sec12_loss.tex` | `22929e6fd051373261a10e4c8281b4a1e77e50dd853821a39d0e60918c1744c7` |
| `sec13_frame.tex` | `caab7461d85f578b6222d14717d88b698d10062980bdecdba1727244e17b7b2b` |
| `sec14_bessel.tex` | `a5e8e98ebc11f11d557d348f56473646c6f0e2fb1c5845108c59ca52ef466185` |
| `sec15_heights.tex` | `8812dd53e24c5f6b50e5cfc3740e72e8b8bbbbe9260ec03cc33fa8e8e8f8f02f` |
