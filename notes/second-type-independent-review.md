# Independent review: reversible lattice moves and quotient weights

25 November 2026. Reviewer task: `/root/retained_theta`.
Reviewed local `paper/shared/flag-second-type-cancellation.tex`,
SHA-256 `c10ca08343cf722b33ba4f512a2e045f0ab8db157fc53b5aac73acc71969745b`,
lines 109–506. The new ambient trace-zero Haar wording was already
present in this snapshot. This review does not re-audit the Fourier
lemma, GL/DS suppliers, all manuscript dependencies, or execute Lean.

## Result

No blocking mathematical error found in the actual move, datum,
family-preservation, normalized kernel or orbit-weight arguments.
The argument needs the stated independent frame coordinates,
self-duality, unramified trace surjectivity and the original
second-type cross test. It does not claim a bound on arbitrary
subsets of a second-type family.

## Decisive checks

1. **Integral congruence STC6.** Let A=h(z,v), B=h(z,x),
   C=h(x',x)/θ and z⊥X'. Then e'z=z+A x',
   e(x')=x'−θC(v+σx), and B=θh(z,z0). Hence

       ee'z−z = A(x+x')−(B+AθC)(v+σx),

   which is exactly STC6. All bracket coefficients are integral.
   The primed integrality statement in the revised draft supplies
   the inverse congruence on Λ1 as well. Those two congruences give
   equality of the traces in X'⊥, not merely one inclusion.

2. **Integral extension.** For the common primitive isotropic
   intersection A=Λ_i∩I, self-duality makes pairing Λ_i→A∨ onto.
   The common trace modulo A has perfect induced form. A common
   lift of a basis of that quotient is a unimodular sublattice;
   its orthogonal splitting is integral in both Λ_i. Dual vectors
   to A in the remaining summand are made isotropic by adding an
   integral matrix times A. Trace O→R onto solves the diagonal
   equations, including dyadic places. Matching these hyperbolic
   bases fixes the common trace pointwise and gives the stated g.

3. **Graph preservation.** e' acts trivially on X'⊥/X', and e^-1
   trivially on X⊥/X. Applying STC6 to old representatives gives
   the congruence equivalence for the graph. The inverse congruence
   applies to every new pair, so this is equality of the original
   level graph rather than a containment.

4. **No-leak transport.** If w∈Λ∩W0 and h(v,w)=1, pairing e(y)
   with w for y∈Mh1 gives −h(y,x)∈O. Thus y+h(y,v)x∈Mh.
   Write it y0+m with y0∈B=Λ∩Y. Direct substitution in the new
   generators gives

       m1=m−h(m,v)x+(Σ B_i h(u'_i,v)) z0.

   The last coefficient is integral. Since h(y0,v)=h(x,v)=0,
   h(m,v)=h(y,v), and y∈B+M1. The unchanged lower adapted
   vectors give M1∩Y=M∩Y and unchanged levels there. B therefore
   represents both defect quotients with the same kernel and
   level distribution. This proves β,j,β_j preservation.

5. **Remaining TypeBe cross test.** For a linked p+p' in θΛ1,
   the representation θy0+θm1 has y0∈B. The last two frame
   coefficients vanish, so the X and X' components of θm1 are
   integral vectors in Λ1. Such an integral X component paired
   with the X' component of any linked pair is in θO by isotropy;
   the analogous statement holds with X and X' interchanged.
   In making the two successive reductions it matters that the
   reduced pair θy0 is still linked in Λ1: this follows from
   B⊂Λ1. Both errors are therefore in θO. The remaining two
   representatives are linked in the old Λ, where TypeBe applies.
   There is no missing θ-denominator in this reduction.

6. **Nontrivial character.** Exact level j means the coefficient
   pair at j−1 violates RR. If χ_b were trivial on U, multiplying
   arguments by all O-elements and using the conductor identifies
   θ^-1(cu_j+c'u'_j)∈Λ+Y. The Λ component lies in D and has the
   same violating pair at index j, contradicting maximum level j.
   This uses the dual of a saturated intersection Λ∩Y⊥; it does
   not assume Y nondegenerate.

7. **Kernel reversibility and measures.** On the ambient trace-zero
   scalar line, conjugating σ=Q(v)/2+t sends t to −t. The pair b
   stays fixed and v goes to −v. Both moves have the same level
   when the target lies in the fixed family. Fixed covolumes of
   B and U follow from [B:M∩Y]=β, triangular determinant one,
   and the exact self-dual pairing sequence Λ→B∨. Thus the
   parameter flip preserves the same normalized Haar measure.
   Compact support plus local constancy gives finitely many target
   lattices in every row. The β/β_j factor cancels the exact-level
   pair fraction in both the main row and the discarded-leak row;
   it creates no hidden extra error factor.

8. **Weighted quotient sum.** GΛ=S_t∩Aut Λ is compact open.
   For every pair orbit the weighted number of targets is

       [GΛ:GΛ∩GΛ1]/vol(GΛ)=1/vol(GΛ∩GΛ1).

   This is symmetric under reversing the pair. The common group
   S_t is unipotent, hence unimodular, so stabilizer volumes are
   invariant under its conjugation. With finite term orbits and
   finite row supports, the pair-orbit reindexing is a finite
   calculation. The two row errors each contribute at most E
   times total positive mass, giving 2E≤7ε. Partition into whole
   second-type families then adds masses, with no family-count
   multiplier. Arbitrary subfamilies need not be reversible and
   are correctly excluded by the theorem.

## Minor exposition recommendations

* Say explicitly that S_t is unipotent and hence unimodular at the
  point where its reciprocal stabilizer weights are declared orbit
  invariant. This fact is already consistent with the GL4 group
  description as a product of upper unitriangular groups.
* For the convention that h is linear in its first variable, define
  the cross matrix in the character-agreement paragraph by
  Z_ab=h(f'_b,f_a). With ordinary column frame matrices this gives
  A* Z B=Z. The reversed pairing is the pinned source's `Zh`.
  Choosing instead Z_ab=h(f_a,f'_b) would conjugate the displayed
  matrix equation; the final character equality is unchanged, but
  an explicit convention avoids an apparent mismatch.

Pinned source cross-check for that last point:
`Development/AbelianVarietyTheory/Proofs/FlagMeasures/FramesCharactersAgreeCommonStabiliser.lean`,
blob `b14885e65129a1c6e7ace937516aa81133188527`, lines 147–208,
at `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The source's linear-first expansion, matrix coefficient formula and
simple-sum character relation agree with the computation above.

## Integration and complementary Fourier audit

Both exposition recommendations were applied to the manuscript. The scalar
measure is explicitly Haar measure on the full trace-zero space, normalized
by T; this keeps the nontrivial dyadic coset and its unit volume. The new
equations are STC1–STC9, avoiding the older SC tags.

The root review checked the orthogonal-summand rank argument, conductor-wise
Gauss estimate, both split maximal-ideal leakage branches, the original
positive-mass use of DS3 and the final height exponents. No blocking error
was found under the stated GL/DS hypotheses. The independent finite check
[scripts/check_second_type_fourier.py](../scripts/check_second_type_fourier.py)
verified 1,592 complete one-coordinate Gauss sums by exact cyclotomic
reduction, and ten rank-four density/leakage cases. It covers split and
unramified quadratic models over residue fields of sizes 2 and 3, at the
listed small conductors; see [the results](../certificates/second-type-fourier.json).
It is not a check of every local field or a substitute for the argument.

Additional pinned-source checks in this review authenticated
ExistsIsometryOfSameTrace.lean (blob 1463fa48ebc6b2515c9e4185b59af4ae3bf46884,
lines 98–188), FramesCharactersAgreeCommonStabiliser.lean (blob
b14885e65129a1c6e7ace937516aa81133188527, lines 63–140), and
NormOrbitSumLeOfSymmKernel.lean (blob d47eb09887621d866bf21a02c6b4fab4f26107b8,
lines 68–114), all under Development/AbelianVarietyTheory/Proofs/FlagMeasures
at jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de. These are
source-byte and ordinary proof checks, not a Lean replay.
