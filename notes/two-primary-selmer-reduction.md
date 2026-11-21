# Fewer Selmer cases for characters of power-of-two order

## Result and status

For ordinary RH, and more generally for a target Dirichlet character whose
order is a power of two, one entire case in the source's complementary-parity
Selmer argument is empty: the case of a nontrivial odd-order host character.
Its separate counting theorem is therefore unnecessary on this restricted
route. The other character estimates, the prime 2, and the exceptional odd
primes remain.

A second simplification applies to both RH and general Dirichlet GRH.
The residual congruence condition couples the coefficient prime and the
twist. Counting these pairs together gives a harmonic sum, instead of a
separate bound for every prime at every twist. This improves the elementary
assembly of the conditional character estimates; it does not prove those
estimates.

All source statements below refer to
**jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de**.
No new cohomological supplier, integral theta construction, or blueprint-node
completion is claimed. The companion certificate records bounded source
reads and exact supplemental calculations, without a Lean replay.

## 1. The odd-order case disappears

Fix a primitive target character \(\chi\) of order \(o\). At a page \(h\),
the construction uses a field inside a cyclotomic extension, obtained from
the target field, a real field of conductor a power of two, and two
quadratic fields. Every character \(\psi\) of this host has

\[
             \operatorname{ord}(\psi)\mid 2^{h+1}o,
             \qquad \operatorname{ord}(\psi)>0.                 \tag{1.1}
\]

This is the precise source statement in **HostComp**, lines 21–34. It is
an integral character-order statement; no rational decomposition of a
cohomology group is used.

**Proposition.** If \(o=2^a\) with \(a\ge0\), every nontrivial host
character has even order. In particular, no host character satisfies the
source's **Case III** condition.

**Proof.** By (1.1), the positive integer \(\operatorname{ord}(\psi)\)
divides \(2^{h+1+a}\), so it is a power of two. If it is odd, it equals
one, and the character is trivial. Case III requires both odd order and
nontriviality, a contradiction. \(\square\)

The full definition of that case is

\[
 p\notin\mathcal B_\chi,\qquad p-1\mid2e,\qquad
 \operatorname{ord}(\psi)\text{ odd},\qquad \psi\ne1,           \tag{1.2}
\]

where \(p\) is the coefficient prime, \(e\) the positive twist and
\(\mathcal B_\chi\) the fixed finite exceptional set. The conclusion
therefore holds for every coefficient field, page, twist and allowed pair
of auxiliary primes. It includes the conductor-one character of order one.

### The exact consumer

For odd \(p\notin\mathcal B_\chi\), the source divides the host
characters into cases I, Z, II and III. The proof of **SumOut** uses the
case-III bound only in the fourth alternative, at lines 117–118; its
finiteness deduction and final sum then use that local case split.
For a fixed target of power-of-two order this fourth alternative is
impossible by the proposition. Thus the restricted outside-exceptional-set
argument requires only cases I, Z and II.

This does not produce the universally quantified **CountIII** statement,
nor justify deleting that premise from the unchanged universal Lean
theorem. It produces a smaller ordinary-mathematics argument after fixing
the target. The later assembly in **JointWinOfCounts**, lines 16–33, can
use this restricted outside-prime estimate with the same remaining inputs.

For a target with odd order greater than one the conclusion fails in
general: a character of order three already supplies a nontrivial odd-order
character. Such a character need not satisfy every other Case III
condition, but character order alone no longer excludes that case.

## 2. Count coefficient primes and twists together

The following elementary lemma keeps the congruence used by the actual
case split. Put \(m=t-1\ge1\), and let
\(H_m=\sum_{j=1}^m1/j\).

**Lemma.** The number of pairs consisting of an odd prime \(p\) and an
integer \(1\le e<t\) satisfying \(p-1\mid2e\) is at most

\[
  \sum_{j=1}^{m}\left\lfloor\frac mj\right\rfloor
      \le mH_m\le m(1+\log m).                                \tag{2.1}
\]

**Proof.** Write \(j=(p-1)/2\). The divisibility condition is exactly
\(j\mid e\). Different odd primes give different positive integers
\(j\), and necessarily \(j\le m\). For a fixed \(j\), there are
\(\lfloor m/j\rfloor\) possible twists. Summing over all positive
\(j\le m\) only enlarges the count. The last inequality follows from
\(\sum_{j=2}^m1/j\le\int_1^m dx/x\). \(\square\)

Let \(N\ge1\) be the comparison modulus and suppose each permitted
character set has at most \(N\) elements. Let
\(\ell(p,e,\psi)\ge0\) be its finite normalized integral Selmer length.
Retain all local conditions and coefficient normalizations. Suppose:

- for every twist, the total contribution of case I is at most
  \((Nt)^{C_I}\), where \(C_I\ge0\);
- every remaining character occurs at \(p-1\mid2e\), and satisfies
  \((\log p)\ell(p,e,\psi)\le(pNe)^C\), where \(C\ge0\).

For power-of-two-order targets, the last hypothesis covers cases Z and
II, so one may take \(C=\max(C_Z,C_{II})\). For a general target it
also includes case III, so take \(C=\max(C_Z,C_{II},C_{III})\).
These replacements are valid because \(pNe\ge1\). If a separate
same-local-conditions theorem shows that case Z contributes zero, its
exponent can also be omitted; no such vanishing is needed here.

**Proposition.** For every finite set of odd coefficient primes outside
\(\mathcal B_\chi\), the total weighted character contribution
\(\sum_p\sum_{1\le e<t}\sum_\psi(\log p)\ell(p,e,\psi)\)
is at most

\[
 m(Nt)^{C_I}
       +NmH_m\bigl((2m+1)Nm\bigr)^C.                         \tag{2.2}
\]

In particular it is at most

\[
 (1+2^C)(Nt)^{\max\{C_I+1,\,2C+2\}}.                       \tag{2.3}
\]

**Proof.** Sum the case-I estimate over the \(m\) twists. Every other
nonzero contribution has \(p\le2m+1\) and \(e\le m\), so its
individual bound is at most \(((2m+1)Nm)^C\). There are at most
\(mH_m\) prime–twist pairs by (2.1), and at most \(N\) characters per
pair. This proves (2.2), uniformly over the finite set of primes.

For (2.3), use \(m\le t\), \(H_m\le t\), \(pNe\le2Nt^2\), and
\(N^{C+1}\le N^{2C+2}\). The two terms are bounded by
\((Nt)^{C_I+1}\) and \(2^C(Nt)^{2C+2}\), respectively. \(\square\)

The source's **SumOut**, lines 167–231, instead bounds the number of
resonant primes by \(2t\) separately for each twist and produces an
exponent \(C_I+3\max(C_Z,C_{II},C_{III})+4\). The improved assembly
retains a fixed multiplicative constant and takes a maximum of exponents.
It is compatible with the project's analytic endpoint, where constants
may depend on the fixed target and accuracy. Its character-to-Selmer
comparison and all individual finiteness assertions remain prerequisites.

## 3. What survives, and what the source implication means

For RH the remaining cohomological requirements include:

- case I and the even-order case II outside \(\mathcal B_\chi\);
- the cases at the fixed exceptional odd primes, including the
  exponent-one case V and its two conductor ranges;
- the prime 2, the other complex-conjugation parity, and the common-window
  quantifiers;
- the integral comparison with the actual congruence modules.

The exceptional set is not empty merely because the target is trivial:
**BchiFacts**, lines 7–10 and 75–85, retains the prime 3 and further fixed
arithmetic primes. Nothing here asserts that their Selmer lengths vanish.

The required **VVle** statement still bounds all finite sums
\(\sum_p(\log p)\sum_{1\le e<t}\operatorname{length}_{\mathbf Z_p}
\Sha(E,p,e)\), with individual finiteness. **VWinAt** fixes the page
function and permitted auxiliary-prime family before providing whole
windows. Specializing the target does not remove these quantifiers.

At the pinned source, **VwinOfRow** is an implication from the global
Galois-representation interface to the full window theorem. Its body calls
the automorphic-window assembly, including local representation theory,
base change, arithmetic deformation and period inputs. A short exported
statement is not an independent ordinary proof of the intermediate
integral estimates. The present reconstruction has not replayed that
dependency closure. The case omission above is verified directly at its
consumers and does not rely on treating that short implication as a new
classical theorem.

## 4. Separate the analytic literature input from cohomology

The endpoint field **hLit** has type **LitThin**. The inspected definition
in **MainSup**, lines 88–94, consists of the three short-interval prime
inputs used in the thin-character estimate. Its supplier
**GlobalInterpolation.LitThin**, lines 8–9, combines a zero-near-one input
with an explicit-formula and window-count input. It is not a Selmer or
integral congruence hypothesis.

Accordingly, the cohomological work package should refer to **VWin** and
its actual congruence consumers. The analytic thin-family input belongs
with the auxiliary analytic estimates. This dependency correction changes
no completion count.

## Verification scope

The dedicated certificate records the exact source files, Git blob and
SHA256 hashes, and bounded passages for the order constraint, case split,
case-III consumer, summation, surviving inputs and analytic/cohomological
separation. The script checks finite power-of-two order cases, the exact
prime–twist count, and rational versions of (2.2)–(2.3).
These checks supplement the proofs; they do not calculate an actual
Selmer group, construct a nonzero theta map, prove auxiliary-level
divisibility, or close W04/W06.

Independent reviews verified the ordinary order and summation proofs.
One reviewer additionally reread the pinned host-order, Case III and
exact summation-consumer passages. Their precise scopes are recorded
in the certificate; neither review claims a cohomological supplier or
an upstream kernel replay.
