# Global proof architecture: a real branch cut and a smaller proof spine

Review of 21 November 2026, starting from commit
`14dd9c34639a6f5def07d1e42178d36243c8ffe8`. This note records a dependency
review of the recovered manuscript, not a fresh verification of all its
proofs and not a Lean kernel replay. The conventional proof is incomplete.
The source inventory, proposed allocation and exact reference audit are in
[`proof-architecture-allocation.json`](../certificates/proof-architecture-allocation.json).
Regenerate that bounded inventory with
`python scripts/build_proof_architecture.py`.

## What the number 96 counts

The 96 items are the sections of the recovered 48,261-line human
reconstruction. They are not the modules of the entire formal proof and
are not 96 independently verified mathematical inputs. The recovered
manuscript has 1,522 unique labels, 646 result environments and 611 proof
environments; this count includes remarks and examples alongside theorems,
lemmas, propositions and corollaries, including conditional statements.
The reconciliation certificate checks preservation, not mathematical truth.

At this review's starting point the main volume contains those 96 section
files and one new commutator section: **97 section files**. The analytic
companion has eight TeX files containing nine actual section commands.
The main inclusion list also contains the preamble and references, so its
100 input paths must not be described as 100 mathematical modules. New
theorem sections added after this review should be counted separately.

The preserved formal-source inventory reports **175,187 Lean files**, all
175,187 locally reachable from `Main`, with 17,374,215 newlines and maximum
import depth 203. These are historical inventory results read from
`source_archive/inspection_result.json` inside the recovered reproducibility
ZIP. That member's SHA-256 is
`d2f4aa8b64cdd94ebe77470f120faf41f41e9774cdd1374a6151ad31491fe4d4`.
The underlying source-tree enumeration and compilation have **not** been
rerun here. These figures therefore explain the scope of the archived
formal source; they do not certify the current status of an upstream tree.

## A substantive deletion from the preferred dependency chain

### Use the K-theory estimate directly

The preferred coarse input is Theorem `kt-fourteen` in recovered section 27.
For a totally imaginary number field (L), a prime (p) with

\[
\mu_p\subset L,\qquad E\ge1,\qquad n=[L:\mathbb Q],
\qquad D=|\operatorname{disc}L|,
\]

it proves, relative to its stated classical inputs,

\[
\log\#H^2(G_{L,S},\mathbb Z_p(E+1))
\le \exp\bigl((2En)^{14}\log(2D)\bigr).
\]

Here (S) consists of the primes above (p). The stated global duality
comparison gives finiteness and the same bound for the strict Selmer group
with coefficients \(\mathbb Q_p/\mathbb Z_p(-E)\). At (p=2), containment
of \(\mu_2\) is automatic, but total imaginarity is still a hypothesis.

This route uses Quillen finite generation, Borel's rank theorem, integral
homological stability, Quillen–Lichtenbaum including its totally imaginary
2-primary case, the étale–Galois comparison, Mathew's Hurewicz exponent
bound, Brauer–Hasse–Noether, and the stated global duality theorem. These
are explicitly cited inputs, not theorems newly proved by this review.
The shorter route has a clearly stated cost in standard imported results.

Its actual internal dependency chain is:

| Needed conclusion | Retained source |
| --- | --- |
| Torsion bound for the stable arithmetic group | `ht-arithmetic-numerical` in section 13 and the arithmetic complex in section 14 |
| Class-number bound | `sl-small-ideal`, `sl-ideal-count`, `sl-class-number` in section 16 |
| (p-1\le n) for odd (p) | The elementary Eisenstein calculation in section 16, before its cyclotomic-tower argument |
| Finite (H^1) groups and passage to inverse limits | `su-unit-theorem` in the first subsection of section 17, Kummer theory and finiteness of the class group |
| Number of cyclic (p)-primary factors and additive estimate | `kt-rank`, `kt-additive` in section 27 |
| Selmer order bounded by the finite (H^2) order | The global duality statement preceding `ht-h2-from-selmer`; its opposite-direction estimate is not needed here |

Thus the replacement does **not** remove arithmetic homology altogether.
Sections 13–14 remain, as do the relevant class-number and unit results.
It does remove the source-specific finite-field homology functionals,
arithmetic-cycle construction and their class-count comparison from the
preferred coarse bound: recovered **section 15 and sections 18–26**,
ten whole section files, become an alternate argument.

### The previously surviving edge has been replaced

Before this review, `sv-exact-case` in section 31 still invoked
`sw-coarse-consequence` in section 26. It now invokes `kt-fourteen` at
(E=1). This is an actual proof change, not a change of diagram colours.
The exponents in (SV7) and (SV8) consequently decrease from 86 to 14.

All relevant hypotheses have been checked at this invocation:

1. Section 31 fixes an **odd** prime (p), a conductor (M), and an order
   (o). The character has small 2-power conductor (2^c<R).
2. `sv-field` constructs (F=F_\theta(\mu_p)), where (F_\theta) kills
   the character. It is totally imaginary because it contains \(\mu_p\)
   and (p) is odd. Thus both the field hypothesis and the root-of-unity
   hypothesis of the K-theory theorem hold.
3. With (x=pN_h\ge3), that lemma proves
   (n=[F:\mathbb Q]\le n_0=2opH_p) and
   \(|\operatorname{disc}F|\le x^n\). The integer (n_0) depends only
   on the fixed (p,M,o); it does not grow with (h,q,d).
4. `sv-restriction` proves
   (s_p(1,\theta)\le\lambda_p(F,1)+n^2), with normalized coefficient
   lengths. It does not require (p\nmid n).
5. The positive twist (E=1) satisfies the K-theory range. Finiteness
   gives \(\log\#\mathcal S_p(F,1)=\lambda_p(F,1)\log p\).

Consequently

\[
\lambda_p(F,1)\log p
\le \exp\bigl((2n)^{14}\log(2|\operatorname{disc}F|)\bigr)
\le x^A,
\qquad A=(2n_0)^{14}(n_0+1).
\]

The second inequality uses (2|\operatorname{disc}F|\le x^{n+1}).
Choosing an integer (k\ge0) with (3^k\ge n_0^2\log p) then gives

\[
s_p(1,\theta)\log p\le x^A+n_0^2\log p
\le x^{\max(A,k)+1}.
\]

The exponent is fixed before (h,q,d) vary and is independent of the
coefficient extension. Additional zero local conditions only shrink the
group. This application makes no new assertion at (p=2), and does not
apply a fixed-degree estimate to fields whose degree grows with (h).

The old derivation is preserved unchanged in
`archive/recovered-2026-11-21/grh_reconstruction_v2.tex`, lines
10483–10725. The SHA-256 of that complete original section is
`6316a7846c8b85692fc73cd56a238f893cc58c1181241405ceb0da6af08c839d`;
this extraction hash was independently recomputed during the review.

### What remains mixed inside sections 16 and 17

The early class-number proof in section 16 and the early unit theorem in
section 17 are needed on the preferred route. Their later tower,
strict-Selmer and finite class-count material serves the alternative.
In particular, the statement `sl-enlargement` refers to `sc-layer`, and
`su-count` refers to `sc-count`. The cyclotomic tower statement (SL6) also
uses the valuation formula (SC18); the elementary degree calculation used
by K-theory occurs before that step.

A scan of all retained section files finds no outside reference to
`sl-enlargement`, `sl-selmer-monotonicity`, or any of the eight labelled
results after `su-unit-theorem`. The other incoming uses of section 16 are
section 29's small-ideal/class-number bound and section 32's
`sl-class-number`; neither needs the tower or the comparison argument.
There are no outside retained references to numbered (SL) or (SU) formulae.
The early proofs were also checked for use of the later assertions.

Preserving mixed sections in the main volume is compatible with this
dependency cut, provided the reader is told which results are used. A
later editorial split can place their optional subsections beside the
ten whole alternative sections. The old proof should remain available.

## A second branch cut under a uniform quasi-Riemann hypothesis

The chosen analytic input is one common number \(\vartheta<1\) such that
every Dirichlet (L)-function is zero-free in
\(\operatorname{Re}s>\vartheta\), allowing the pole of a principal
character at 1. A character-dependent boundary with no uniform gap from 1
does not suffice. Its claimed published proofs and precise source status
are recorded elsewhere in the project; this review uses it as an explicit
external input.

For a real zero \(\beta\) of conductor (q\ge3), it already gives

\[
1-\beta\ge1-\vartheta
\ge\frac{(1-\vartheta)\log3}{\log q}.
\]

Thus a separate real-zero exclusion theorem is not an additional premise
on this route. The uniform logarithmic-derivative consequences needed for
selection are already in section 5. Sections 7–9's independent real-zero
argument and tails can be retained as an alternative. Section 6 is a
different, conditional analytic bootstrap: its improved short-range
mean-square input has not been supplied. Its omission from the preferred
route is not a claim to have proved that improvement.

These are **four additional whole sections**, 6–9. Together with the
K-theory cut there are 14 alternative section files, leaving **83 retained
section files from the baseline total of 97**. This is a reading-path
count, not a count of indispensable lemmas or a certificate that the
remaining proof is finished.

## A smaller logical spine

The manuscript can now be organized around six mathematical stages,
with the technical material allocated to ten work packages in the JSON:

| Stage | Mathematical output | Present status |
| --- | --- | --- |
| Positive prime sums | A fixed positive combination satisfying the interval bound implies Dirichlet GRH | Implication written out in sections 1–3 |
| Compatible auxiliary choices | Fields, primes and common rank intervals under uniform QRH and the coarse K-theory bound | Partial compatibility proved; full refined errors still required |
| Cohomological and congruence estimates | The precise character-length budget used by the construction | Complementary-parity interface remains open |
| Integral theta maps | One family of actual maps with their lattices, quotient metrics, local divisors and weights | Seed nonvanishing and auxiliary-prime divisibility remain open |
| Analytic estimates for those maps | Ambient dimensions, Gram bounds, orbital energy and integrated residue norms | Global energy and integrated pairing remain open |
| One slope argument | The required prime-sum inequality uniformly in all construction parameters | Abstract inequalities proved; the compatible arithmetic realization is open |

The decisive compression is to prove one **compatible construction
theorem**, with arithmetic and analytic estimates about the same tuple
of objects, and apply the slope theorem once. Merely grouping existing
sections into these boxes would prove nothing. The central unresolved
theorem must construct the maps and certify every required estimate
simultaneously, with constants independent of the interval parameter.

More precisely, `cs-slope` takes Hermitian lattices (E_i,F), integral
maps (f_i:E_i\to F), their actual height and slope bounds, and matrices
(A_i) whose first (n=\operatorname{rank}F) rows represent those same
maps in one common target basis. If (n\ge(1-\delta)D), the stated Gram
errors are (e,\eta), and the numerical slope hypotheses hold, then

\[
s-\mu(F)\le
\frac{2u\log(1+H/u)+(\eta+4\sqrt e)H}{1-\delta}.
\]

The value of (u\log(1+H/u)) at (u=0) is its continuous value 0.
`cs-combination` cancels the local normalizations in this same system.
One must not replace the all-vector divisibility in `cs-required-divisor`
by a determinant divisibility statement, or substitute estimates for
different lattices, arbitrary quotient norms or unrelated maps.

For the final implication, `prop:size` and `cor:scalar-construction`
require one constant (C) such that for every sufficiently small
\(\varepsilon>0\), on arbitrarily large intervals
\([Y,Y^{b_0}]\) with fixed (b_0>1), the construction satisfies the
displayed scalar hypotheses at every (x), with (G=H_\chi(x)).
They yield

\[
H_\chi(x)\le x^{1/2+(C+3)\varepsilon}.
\]

The positive family (H_\chi) is fixed, and (C) cannot grow like
\(\varepsilon^{-1}\). The elementary optimization (x/m+m\ge2\sqrt x)
explains the length (m\asymp\sqrt x); it does not supply the maps or
justify uniform estimates for a growing chain.

This form isolates where further genuine simplification must occur:
replace a construction by a theorem delivering the same quantified
interface, or eliminate a premise from that interface. It does not hide
the current missing construction in a theorem presented as proved.

## Obstacles the branch cuts do not solve

The coarse bound with exponent 14 does not imply the refined
complementary-parity sum in `sa-missing-parts`. In a growing-degree field
its enormous degree factor need not fit the prescribed budget. The
fixed-degree argument in `sv-exact-case` is deliberately narrower.
Uniform QRH and the real-zero consequence do not give GRH by themselves,
nor the missing stronger short-range mean-square bound of section 6.

The remaining principal interfaces are the integrated residue pairing
for the generated functions; uniform global orbital energy and its
coordinate/lattice inputs; nonvanishing and local divisibility for the
actual integral theta maps; complementary-parity cohomological lengths
with integral congruence control; and assembly uniform in growing chains.
The new commutator result addresses an algebraic matrix/restriction step.
Its exact corrected domain, and the difference between every fixed finite
chain and chain-uniform estimates, are recorded in the contemporaneous
review of recent advances.

## Cross-reference evidence for optionality

The following table is generated from the current source by the inventory
script. It contains every explicit LaTeX reference from a retained
recovered section into the 14 whole alternative section files. A
reference to a section title, a forward comparison, or the assertion
being proved is not automatically a mathematical premise. The crucial
old premise `sv-exact-case` → `sw-coarse-consequence` is absent after the
checked substitution above. All 25 remaining references have been
classified by reading their surrounding argument.

| Retained section and line | Alternative reference | Classification |
| --- | --- | --- |
| r05:216 | `sec:qrh-bootstrap` (r06) | optional alternative |
| r16:4 | `sc-section` (r15) | optional comparison |
| r16:6 | `sc-layer` (r15) | optional definition |
| r16:11 | `sc-few` (r15) | optional comparison |
| r16:11 | `sc-count` (r15) | optional comparison |
| r16:280 | `sc-layer` (r15) | optional definition |
| r16:313 | `sc-exponent` (r15) | optional comparison |
| r16:317 | `sc-few` (r15) | optional comparison |
| r16:317 | `sc-sha` (r15) | optional comparison |
| r17:4 | `sc-count` (r15) | optional definition |
| r17:11 | `sc-few` (r15) | optional comparison |
| r17:486 | `sc-count` (r15) | optional definition |
| r27:8 | `sc-few` (r15) | optional comparison |
| r27:9 | `sw-few` (r26) | optional comparison |
| r27:327 | `sc-few` (r15) | optional comparison |
| r27:329 | `sw-few` (r26) | optional comparison |
| r96:22 | `sp-section` (r18) | historical summary |
| r96:46 | `sf-section` (r23) | historical summary |
| r96:46 | `sw-section` (r26) | historical summary |
| r96:50 | `sc-few` (r15) | historical summary |
| r96:53 | `sd-section` (r19) | historical summary |
| r96:53 | `sh-section` (r20) | historical summary |
| r96:56 | `si-section` (r21) | historical summary |
| r96:56 | `se-section` (r22) | historical summary |
| r96:365 | `prop:qrh-exponent-improvement` (r06) | historical summary |

There are also 16 manually numbered formula references to section 15
inside mixed sections 16–17, recorded individually in the JSON. The
(SC18) references are premises of their optional tower/class-count
arguments. The others state the optional data or compare consequences.
None is a premise of `sl-class-number`, the elementary cyclotomic-degree
calculation, `su-unit-theorem`, or the preferred K-theory proof.

This audit combines a reproducible textual inventory with a mathematical
reading of the relevant proofs. It is intentionally not described as
automatic extraction of a full formal proof dependency graph.
