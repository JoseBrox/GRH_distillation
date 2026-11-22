# The remaining arithmetic bridge after the resultant

## Scope

The resultant and corrected-gcd theorem reconstruct an elementary supplier
of the residual Selmer estimate. They do not give a further uniform gcd
saving from the trace-class assumptions alone. The exact example below
shows that the logarithm of the corrected gcd can already grow linearly
with the twist, with two fixed auxiliary primes and one trace in each
family. This is not an example of actual automorphic spectra or Selmer
groups.

The second result is a bounded audit of the missing arithmetic bridge.
The source controls negative-weight deformations, not merely the
cotangent space of a finite weight-zero algebra. Its automorphy,
integral deformation and rigidity requirements survive the ordinary-RH
specialization. No additional proof node is closed.

## 1. An exact limitation of the spectral gcd argument

Fix the auxiliary primes \(r=7,s=11\), and the coefficient prime
\(\ell=13\). For each integer \(L\ge1\), put

\[
 M=13^L,\qquad e=\min\{k\ge1:7^k\ge M\},\qquad
 a_q=q^e\quad(q=7,11).
\]

Let \(u_q\) be the least nonnegative residue of
\(a_q^2+a_q+1\) modulo \(M\), and take the single trace and
single root of unity

\[
 \alpha_q=u_q/a_q,\qquad z=1.
\]

Then \(0\le\alpha_q<1\), each trace family is Galois-stable,
and \(q^e\alpha_q=u_q\) is an integer. Thus every assumption
of the elementary resultant theorem is satisfied, with the same twist
and root multiset for both auxiliary primes. Its integer is

\[
 n_q=a_q^2+a_q+1-u_q\in M\mathbf Z_{>0}.                 \tag{1.1}
\]

Because \(13\notin\{7,11\}\), the corrected gcd from the
resultant note therefore satisfies

\[
 v_{13}(G_{7,11})\ge L,\qquad
 \log G_{7,11}\ge L\log13>(e-1)\log7.                  \tag{1.2}
\]

The last inequality follows from minimality of \(e\). Conversely,
\(a_q^2<n_q\le a_q^2+a_q+1<2a_q^2\), so the individual
logarithmic sizes are \(2e\log q+O(1)\). The lower bound in
(1.2) is consequently on the scale of these available logarithmic
majorants, not merely an unbounded sequence of negligible errors.
In particular, neither a bound independent of the twist nor a bound
\(\log G=o(e)\) follows from these trace-class properties alone.

This example deliberately does **not** supply the global automorphic
families, their classification of actual Galois representations, or any
trace-to-Selmer inequality. It proves no lower bound for an actual
Selmer group and no obstruction to the allowed RH estimate. A saving
for the real spectra would require additional arithmetic information
relating their Hecke eigenvalues at different auxiliary primes.

## 2. What the source actually uses to bound Selmer lengths

All source passages below are at
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, under
`lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties/`.
The accompanying checker authenticates file and excerpt hashes.

| Bounded source | Exact role |
| --- | --- |
| `UnitaryThreeGroups/KatoUse.lean:19–34,54–64` | States the cohomological, commutative-algebra, Kato, adjoint-vanishing and automorphy inputs, and the required character-length inequality. |
| `AutomorphicCases/AutomorphyUnramifiedCoefficients.lean:12–27` | Supplies a marked deformation problem whose weight-zero algebra is finite, whose rank-three points are automorphic, and whose rank-two points are modular. |
| `UnitaryThreeGroups/OneCharOf.lean:114–140` | Constructs the local/global rings and graded model; applies the preceding finiteness, automorphy and point-rigidity inputs before the trace estimate. |
| `UnitaryThreeGroups/ModelLower.lean:373–401` | Sends strict cocycles into model derivations and applies the comparison specifically in weight \(-1\), at lines 387–388. |
| `UnitaryThreeGroups/VlenLe.lean:43–67` | Passes from every finite-torsion Selmer submodule to its total length, bounded by the same model length. |
| `UnitaryThreeGroups/PtHypOf.lean:74–89` | Uses base-point rigidity and adjoint Bloch–Kato vanishing at the two kinds of characteristic-zero points. |
| `UnitaryThreeGroups/ModelUpper.lean:103–120,133–160` | Constructs the five graded-model conditions and bounds its normalized length by twice the trace-difference valuations. |
| `UnitaryThreeGroups/OneCharOf.lean:64–93,158–178` | Passes to unramified coefficient integers and preserves normalized length and trace. Prime-to-coefficient-prime character order suffices; the RH two-group case does not remove the preceding arithmetic steps. |

Here is the useful minimal target in ordinary mathematics, with the
good-character and admissibility hypotheses retained from the displayed
source contracts. Fix an actual character \(\psi\), odd coefficient
prime \(\ell\), CM auxiliary field, host and twist. Choose \(\sigma\)
such that every admissible trace differs from
\(\Psi(\sigma)+1+\Psi(\sigma)^{-1}\). Construct a finite set of
pairwise nonisomorphic admissible representations such that

\[
 \ell(\ell,e,\psi)
 \le2\sum_\rho
 v_\ell\bigl(\operatorname{tr}\rho(\sigma)
              -(\Psi(\sigma)+1+\Psi(\sigma)^{-1})\bigr),
 \qquad v_\ell(\ell)=1.                                  \tag{2.1}
\]

The local deformation conditions and the admissibility of these very
representations must match the finite trace family used in the
resultant. The strict Selmer coefficient is
\((K/\mathcal O)(\psi^{-1}\varepsilon_\ell^{-e})\), and its
length is divided by the ramification index of \(\mathcal O\), as
in the residual-product theorem. The source proves (2.1) by the
negative-weight lower comparison and the graded-model upper comparison;
it is not an immediate consequence of having finitely many eigenvalues.

For RH, the host characters have power-of-two order, and hence have
prime-to-\(\ell\) order at odd \(\ell\). This simplifies the
coefficient and character bookkeeping. It supplies neither finite
weight-zero deformation algebras nor modularity of their points or
the integral length comparison. The nontrivial odd-order case was
already removed; no additional branch is deleted here.

## 3. Why finite weight-zero spectra do not replace the graded comparison

Let \(\mathcal O\) be a discrete valuation ring with uniformizer
\(\pi\), and consider the graded augmented algebra

\[
 A_L=\mathcal O[X]/(\pi^L X,X^2),\qquad
 \deg X=-1,\qquad \epsilon(X)=0.                         \tag{3.1}
\]

Its weight-zero algebra is exactly \(\mathcal O\), hence is finite
and flat. After inverting \(\pi\), the entire algebra is its base
field, so there is only the base point and it has no nonzero tangent
direction. Nevertheless, if \(I=\ker\epsilon\), then

\[
 I/I^2=(\mathcal O/\pi^L)X,
 \qquad\operatorname{length}_{\mathcal O}(I/I^2)=L.        \tag{3.2}
\]

Thus an arbitrarily large integral negative-weight contribution can be
invisible both in the weight-zero algebra and in the characteristic-zero
point set. A determinant argument on the finite weight-zero algebra
alone cannot control it. This is an algebraic counterexample to the
proposed shortcut, not a model of the actual Galois deformation problem:
the additional graded presentation, local conditions and comparisons
used in the source have not been imposed on (3.1).

The [compatible conormal pairing](rh-selmer-conormal-pairing.md)
and [full abstract length theorem](rh-selmer-core-wrapper.md) now supply
the negative-weight comparison and graded length bound under the
original model hypotheses. The remaining task is to construct the
actual marked arithmetic models and verify those hypotheses, retaining
automorphy, rigidity, integral lifting and exceptional primes, then
bound the resulting weighted Selmer product uniformly. A generic
Fitting-ideal or spectral determinant claim cannot supply these data.

## Verification scope

The general examples and deductions above have direct proofs. The script
checks (1.1)–(1.2) in exact integer arithmetic for a finite range of \(L\),
and authenticates only the listed bounded source contracts. No actual
automorphic representation or Selmer group is computed, and no Lean
kernel replay or upstream proof audit is claimed.
