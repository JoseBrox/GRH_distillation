# Fresh audit of the RH rank-four chain and weighted assembly

**Historical audit snapshot.** The four interfaces identified below are addressed in the subsequent [closure review](rh-weighted-selmer-closure.md); consult that review for the current status.

24 November 2026. Audit baseline: `5dfafd71856b4769f0831ca727e81d8b83a44206`.
Pinned source: `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

**Status and boundary.** The numerical assembly is proved, including
both varying quadratic conductors. This is a fresh conventional
proof review against the earlier reconstructed suppliers, not an
external referee report or a kernel replay of the parent development.
It does not independently certify all of the earlier ordinary-family,
arithmetic propagation and abstract integral-length theorems.
Keep the individual rank-four bound (SL3) conditional until the
remaining source interfaces below are audited. No full W04 or RH
closure is claimed.

## 1. Arithmetic, local model and integral comparison

* The high-dyadic construction retains the actual odd conductor.
  In BU6--BU8 the choice of auxiliary conductor is polynomial in
  the ORIGINAL \(N=2^a qd\), not just in the dyadic layer. The
  strict odd-root cocycle conclusion uses the smoothed integral
  Stickelberger operator, not an assertion of a divisible class
  group. The required Bernoulli-unit estimate is a prior supplier.
* In the original relative presentation SM7--SM11 the local
  representation at the coefficient prime is fixed, not merely its
  conjugacy class. The degree-zero relative cochain term removes
  precisely the coboundary ambiguity. The other local quotients
  have Euler characteristic zero. The \(+2,+1,+1\) equation
  defects are therefore the dimensions of the even weight spaces.
  No loss of integral torsion is permitted in the relation ideal.
* The symplectic block normalization SM6 is compatible with the
  original local component. At a characteristic-zero point,
  distinct inertia exponents determine the ordinary flag.
  The prime-to-coefficient-prime element ph has finite order
  and the graded values on the selected domain are constant by
  specialization of a root of unity; this matters at \(e=2\).
  The ratios differing from the cyclotomic character on this
  element give the required zero dual invariants.
  Restricting to the finite field extension killing the inertial
  finite factors and applying the local Euler and Bloch--Kato
  dimension formulas controls the extensions as well as the
  graded pieces, including dual-number lifts.
* The self-twist argument SR2 uses all four distinct inertia
  exponents and a new ramified prime of the fixed quadratic
  field. A self-twist through the cyclotomic extension must fix
  each graded inertia character, not merely preserve the set.
  Thorne's theorem is applied to the polarized adjoint on
  the totally real base, with its negative-transpose action.
  The symplectic Lie algebra is a direct summand.
* In SL4 the two-sided slice tangent is lifted by inverting
  the product of actual opposite-first-weight entries. The
  resulting localized graded algebra is Laurent-polynomial
  over its first-weight-zero part, so this argument does not
  assume smoothness of a general invariant quotient.
  The lower integral comparison uses \(c_0=b(\theta(s_0)-1)\),
  not the original annihilator \(b\) of the strict group:
  the local coboundary primitive need not be annihilated by
  \(b\). The normalization and the final division by the
  coefficient ramification index are essential.

## 2. The arithmetic point suppliers

| Part reviewed | Decisive check / retained dependency |
| --- | --- |
| Mixed Hilbert seed | At a norm-two level place the projective stabilizer is pro-2, so taking its invariants is exact at every odd coefficient prime. The ordinary operator factors mod the uniformizer through the one-dimensional residual weight quotient. The weight-change implication is conditional on the mixed Eisenstein starting packet at the same tame level and central character. |
| Marked symplectic induction | Pair the original labels and retain the integral transported ordinary flags; the seed's cyclotomic-kernel irreducibility is indispensable for the adjoint theorem. Attachment uses solvable induction/base change with the stated normalizations, not residual irreducibility. |
| Three residual links | The auxiliary ramification is killed after adjoining the cyclic degree-coefficient-prime fields, since the relevant class-two unipotent groups have exponent that prime (also at three). The endpoint flags and the two cocycles are transported on the same extensions. |
| Seed membership | The fixed-weight tangent criterion uses both the lower dimension from the finite torsion-free ordinary Hecke quotient and the zero relative tangent, not just membership of one arithmetic point. Anticyclotomic interpolation uses Weierstrass preparation over a fixed finite coefficient field, not convergence of the roots of unity to zero. |
| Common sum ideal | The two links use the same labeled coefficient algebra. Finite weights follow from integrality of the image of the actual Hecke quotient; characteristic-polynomial coefficients of a matrix are integral over those of its square. The Speh-exclusion argument for good-prime purity uses the residual quotient-character obstruction to cyclotomic ratios. |
| Characteristic-prime clause | Distinct ratios on the local cyclotomic kernel yield a single element with four pairwise infinite-order ratios. The degree-four regular-spectrum argument includes the binomial degree-two Newton segment and the swapped two-block case; odd characteristic is necessary. The connected-component argument gives density on the required kernel. The final use of P1core remains an imported all-rank theorem. |
| Completed chart and connectedness | The presentation deficit and collision/reducibility bounds apply to the same ideal, after cutting by the coefficient uniformizer. The irreducible-fibre bound first contracts to the finite-type entry algebra; it does not estimate the transcendence degree of a completed fraction field. The nine support loci and the exceptional flag equations CP2/CP4 were recomputed independently. |
| Uniform bounds and lattice transport | The Ferrero--Washington bound is taken on the fixed abelian residual splitting field's cyclotomic tower. The class-rank and ramified-place constants are fixed before the depth. The lexicographic torus normalization uses the strict odd-root vanishing, and leaves the integral flags in the prescribed charts. |
| Common coefficient space | The completed invariant ring and the finite-type entry algebra are different rings. The reverse-complement path identity reduces every balanced weight monomial to cycle traces without denominators divisible by three. The auxiliary Laurent ring with nilpotent negative powers gives a valid coefficientwise specialization at 1; completion alone at the split point would not represent the nonsplit residues. |
| Endpoint exclusion | The symmetric square-zero block module has rank three, the local flag-preserving part rank one, and the odd complex conjugation action eliminates global invariants. Finite Poitou--Tate gives at least \(q^j\) normalized pairs. The primitive-compatible argument gives a nonzero integral cocycle and its local primitive. The two block determinants differ in modulus by \(p^2\); even a single strict common half-power window therefore excludes the endpoint. |
| Fixed-field descent | The chosen quadratic field is fixed before the varying towers, and its fresh ramified prime is avoided in all tower constructions. A self-twist through an abelian quotient has order dividing four, hence survives reduction. Residual distinctness on the tower rules out the first twist; ramification at the fresh prime rules out the extra quadratic one. This checks the irreducibility hypothesis of solvable descent, not the much stronger hypotheses of a residual automorphy-lifting theorem. |

These checks validate the indicated implications subject to their
declared inputs; they do not prove all those inputs anew.

## 3. Published theorem interfaces

The following published or author-hosted statements were consulted
in this review (the displayed statements were checked, not only
the abstracts).

* Ferrero--Washington, Ann. Math. 109 (1979), 377--395,
  DOI [10.2307/1971116](https://doi.org/10.2307/1971116):
  vanishing of the Iwasawa mu invariant for abelian fields.
  The class-rank bound is on the fixed abelian cyclotomic tower.
* Thorne, [author PDF](https://www.dpmms.cam.ac.uk/~jat58/adequate_new.pdf),
  Theorem 6.1, p.23; published DOI 10.4310/pamq.2022.v18.n5.a5.
  Regular algebraic cuspidal polarized automorphy and irreducibility
  on the full cyclotomic kernel suffice; no residual adequacy
  hypothesis is required there.
* BLGGT, *Potential automorphy and change of weight*, Ann. Math. 179
  (2014), 501--609, Lemma 2.2.2. Solvable base change/descent with
  irreducible restriction, not Theorem B on residual automorphy.
* Bergdall--Hansen, [author PDF](https://www.davidrenshawhansen.net/padicHMF.pdf),
  Theorem 6.5.1 and Remark 6.5.2, pp.58--59. The filtration jumps
  and crystalline Frobenius polynomial are the stated ones for
  spherical local representations; passing from the paper's
  geometric convention to the arithmetic convention needs the
  indicated contragredient. The local weight calculation does not
  follow from ordinary slopes alone without this identification.
* Andreatta--Goren, arXiv:math/0308040, Prop.7.14(1) and
  Lemma 11.10(1): cusp expansions of the Hasse invariant and
  high-power lifting at prime-to-p level. These statements do
  not by themselves assert the precise level-one normalized adelic
  multiplier; the finite descent/norm argument must be checked.
* Caraiani, [Monodromy and local-global compatibility for l=p](https://doi.org/10.2140/ant.2014.8.1597),
  Theorem 1.1, pp.1597--1598. Her geometric normalization includes
  a contragredient in the definition of the local correspondence;
  when comparing with BLGGT's rec convention one must take the
  contragredient automorphic representation if necessary.
  The polynomial counting bound is insensitive to this
  convention, but the Frobenius trace comparison is not.
  A weaker conductor-counting argument is recorded in the
  spectrum fragment; it needs only compatibility up to
  semisimplification at the coefficient prime. It leaves the
  conclusion (SL3) unchanged.

## 4. Corrections, computation and unverified inputs

The old residual-budget note asserted
\(\mathcal K\le\exp(x^{\varepsilon/2})\) from a bound including
\(\exp(x^{4\varepsilon/5})\). This stronger conclusion was not
justified. Replace it by \(\exp(x^{9\varepsilon/10})\), and
retain the required \(\mathcal K=o(\exp(x^\varepsilon))\).
The corrected bound and the new weighted assembly are committed.

Run `python scripts/check-rh-rank-four-audit.py` with SymPy.
The independent finite calculations checked all 14 proper nonempty
coordinate subsets, the nine loci and both strictness tables;
the exact symplectic lower-entry identities over the polynomial
ring; all four class-number-one discriminants and sixteen listed
split primes; and the resonance count for twists 2 through 500.
All checks passed. The last enumeration is a diagnostic only; the
uniform numerical estimate uses a direct inequality for every e.
No computation verifies the infinite-dimensional automorphic or
Selmer arguments.

The most important remaining independent checks are (i) the
level-one Hasse descent and unchanged-level mixed starting
eigenpacket with the exact central-character conventions,
(ii) the original all-rank ordinary-family arithmetic occurrence,
classicality and finite/torsion-free statements and their use
in the common determinant ideal, (iii) the all-rank P1core
arithmetic propagation theorem with the actual ordinary
Cayley--Hamilton algebra, and (iv) the abstract integral-length
theorem in the full coefficient ring. The preceding reconstruction
gives proofs of these suppliers or invokes their earlier proofs;
this audit does not certify all of them end-to-end. There is no
new claim that they are false. In particular the finite checks
must not be used to mark the individual rank-four bound or the
entire weighted estimate as unconditional.

No manuscript build, Lean replay, or external referee review
was performed in this audit. The stronger all-place WitA,
PotUnl and the general-Dirichlet version remain outside its
proved scope. See [weighted assembly](rh-weighted-selmer-assembly.md)
for the exact original quantitative conclusion under the individual
length estimate.
